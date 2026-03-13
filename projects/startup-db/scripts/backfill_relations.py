"""Auto-generate company relations from shared sub_category + country and bigtech partnerships.

Usage:
    cd projects/startup-db
    uv run python scripts/backfill_relations.py

Two relation types are generated:
  - competitor: companies sharing the same (sub_category, country) pair
  - partner:    companies referenced in metadata.bigtech_collaboration that match
                another company name in the DB (case-insensitive)
"""

from __future__ import annotations

import json
import logging
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path
from typing import Any

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from supabase import Client, create_client  # noqa: E402

from startup_db.config import settings  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

BATCH_SIZE = 100
TABLE = "su_company_relations"


def get_client() -> Client:
    """Return a Supabase client using project settings.

    Returns:
        Authenticated Supabase client instance.
    """
    return create_client(settings.supabase_url, settings.supabase_key)


def fetch_all_companies(client: Client) -> list[dict[str, Any]]:
    """Fetch all companies from su_companies.

    Retrieves id, name, slug, sub_category, country, main_category, and metadata
    for every company in the database using paginated requests.

    Args:
        client: Authenticated Supabase client.

    Returns:
        List of company row dicts.
    """
    rows: list[dict[str, Any]] = []
    page_size = 1000
    offset = 0

    while True:
        result = (
            client.table("su_companies")
            .select("id,name,slug,sub_category,country,main_category,metadata")
            .range(offset, offset + page_size - 1)
            .execute()
        )
        batch = result.data or []
        rows.extend(batch)
        logger.debug("Fetched %d companies (total so far: %d)", len(batch), len(rows))
        if len(batch) < page_size:
            break
        offset += page_size

    logger.info("Total companies fetched: %d", len(rows))
    return rows


def build_competitor_relations(
    companies: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Generate competitor relation rows from shared (sub_category, country) groups.

    For every pair of companies in the same sub_category + country bucket,
    creates both the forward and reverse relation rows.

    Args:
        companies: List of company dicts from su_companies.

    Returns:
        List of relation dicts ready for upsert into su_company_relations.
    """
    groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)

    for company in companies:
        sub_cat = (company.get("sub_category") or "").strip()
        country = (company.get("country") or "").strip()
        if not sub_cat:
            continue
        groups[(sub_cat, country)].append(company)

    relations: list[dict[str, Any]] = []
    total_groups = 0
    skipped_groups = 0

    for (sub_cat, country), members in groups.items():
        if len(members) < 2:
            skipped_groups += 1
            continue

        total_groups += 1
        if country:
            description = f"Same sub-category ({sub_cat}) in {country}"
        else:
            description = f"Same sub-category ({sub_cat})"

        for a, b in combinations(members, 2):
            # Forward
            relations.append(
                {
                    "company_id": a["id"],
                    "related_company_id": b["id"],
                    "relation_type": "competitor",
                    "description": description,
                }
            )
            # Reverse (bidirectional)
            relations.append(
                {
                    "company_id": b["id"],
                    "related_company_id": a["id"],
                    "relation_type": "competitor",
                    "description": description,
                }
            )

    logger.info(
        "Competitor groups: %d active, %d singleton skipped",
        total_groups,
        skipped_groups,
    )
    return relations


def build_partner_relations(
    companies: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Generate partner relation rows from metadata.bigtech_collaboration references.

    For each company whose metadata contains a bigtech_collaboration value that
    matches another company's name (case-insensitive substring match), creates
    a bidirectional partner relation pair.

    Args:
        companies: List of company dicts from su_companies.

    Returns:
        List of relation dicts ready for upsert into su_company_relations.
    """
    # Build name → id lookup (lowercase for case-insensitive matching)
    name_to_id: dict[str, str] = {}
    for company in companies:
        name_lower = (company.get("name") or "").strip().lower()
        if name_lower:
            name_to_id[name_lower] = company["id"]

    relations: list[dict[str, Any]] = []

    for company in companies:
        raw_meta = company.get("metadata") or {}
        if isinstance(raw_meta, str):
            try:
                raw_meta = json.loads(raw_meta)
            except (json.JSONDecodeError, TypeError):
                raw_meta = {}

        collaboration = (raw_meta.get("bigtech_collaboration") or "").strip()
        if not collaboration:
            continue

        collaboration_lower = collaboration.lower()

        for partner_name_lower, partner_id in name_to_id.items():
            # Skip self-references
            if partner_id == company["id"]:
                continue
            if partner_name_lower in collaboration_lower:
                description = f"bigtech_collaboration: {collaboration}"
                # Forward
                relations.append(
                    {
                        "company_id": company["id"],
                        "related_company_id": partner_id,
                        "relation_type": "partner",
                        "description": description,
                    }
                )
                # Reverse (bidirectional)
                relations.append(
                    {
                        "company_id": partner_id,
                        "related_company_id": company["id"],
                        "relation_type": "partner",
                        "description": description,
                    }
                )

    return relations


def batch_upsert_relations(
    client: Client,
    relations: list[dict[str, Any]],
) -> int:
    """Upsert relation rows into su_company_relations in batches.

    Uses on_conflict="company_id,related_company_id,relation_type" so that
    re-running the script is safe (idempotent).

    Args:
        client: Authenticated Supabase client.
        relations: List of relation row dicts to upsert.

    Returns:
        Total number of rows processed.
    """
    if not relations:
        return 0

    total = 0
    for i in range(0, len(relations), BATCH_SIZE):
        batch = relations[i : i + BATCH_SIZE]
        client.table(TABLE).upsert(
            batch,
            on_conflict="company_id,related_company_id,relation_type",
        ).execute()
        total += len(batch)
        logger.info(
            "  Upserted relations %d-%d / %d",
            i + 1,
            i + len(batch),
            len(relations),
        )

    return total


def backfill(client: Client) -> None:
    """Run the full relation backfill.

    Steps:
      1. Fetch all companies.
      2. Generate competitor relations from (sub_category, country) groups.
      3. Generate partner relations from metadata.bigtech_collaboration.
      4. Batch-upsert all generated relations.
      5. Log a summary.

    Args:
        client: Authenticated Supabase client.
    """
    companies = fetch_all_companies(client)

    # ── Competitor relations ──
    logger.info("Building competitor relations...")
    competitor_relations = build_competitor_relations(companies)
    logger.info("Competitor relation rows to upsert: %d", len(competitor_relations))

    # ── Partner relations ──
    logger.info("Building partner relations from bigtech_collaboration...")
    partner_relations = build_partner_relations(companies)
    logger.info("Partner relation rows to upsert: %d", len(partner_relations))

    # ── Upsert ──
    all_relations = competitor_relations + partner_relations

    if not all_relations:
        logger.info("No relations to upsert. Done.")
        return

    logger.info("Upserting %d total relation rows...", len(all_relations))
    total_upserted = batch_upsert_relations(client, all_relations)

    # ── Summary ──
    logger.info("Backfill complete.")
    logger.info("  Companies processed:        %d", len(companies))
    logger.info(
        "  Competitor pairs (rows):    %d  (%d bidirectional pairs)",
        len(competitor_relations),
        len(competitor_relations) // 2,
    )
    logger.info(
        "  Partner pairs (rows):       %d  (%d bidirectional pairs)",
        len(partner_relations),
        len(partner_relations) // 2,
    )
    logger.info("  Total rows upserted:        %d", total_upserted)


def main() -> None:
    """Entry point for the backfill script."""
    client = get_client()
    backfill(client)


if __name__ == "__main__":
    main()
