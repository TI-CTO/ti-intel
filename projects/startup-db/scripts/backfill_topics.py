"""Backfill L1 topic assignments based on sub_category → L1 mapping.

Only assigns the first L3 slug of each L1 domain as a placeholder.
Detailed L3 assignment should be done via MCP/startup-analyst.

Usage:
    cd projects/startup-db
    uv run python scripts/backfill_topics.py
    uv run python scripts/backfill_topics.py --dry-run
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from supabase import create_client  # noqa: E402

from startup_db.config import settings  # noqa: E402
from startup_db.taxonomy import L1_BY_SUBCATEGORY, get_l3_slugs_for_l1  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

PAGE_SIZE = 1000


def main() -> None:
    """Run the topic backfill."""
    parser = argparse.ArgumentParser(description="Backfill L1 topic assignments from sub_category.")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing.")
    args = parser.parse_args()

    client = create_client(settings.supabase_url, settings.supabase_key)

    # Fetch all companies
    logger.info("Fetching companies...")
    companies: list[dict] = []
    offset = 0
    while True:
        batch = (
            client.table("su_companies")
            .select("id,name,sub_category")
            .range(offset, offset + PAGE_SIZE - 1)
            .execute()
        )
        companies.extend(batch.data or [])
        if len(batch.data or []) < PAGE_SIZE:
            break
        offset += PAGE_SIZE
    logger.info("Fetched %d companies", len(companies))

    # Fetch existing topic assignments to avoid duplicates
    logger.info("Fetching existing topic assignments...")
    existing: set[tuple[str, str]] = set()
    offset = 0
    while True:
        batch = (
            client.table("su_company_topics")
            .select("company_id,l3_slug")
            .range(offset, offset + PAGE_SIZE - 1)
            .execute()
        )
        for row in batch.data or []:
            existing.add((row["company_id"], row["l3_slug"]))
        if len(batch.data or []) < PAGE_SIZE:
            break
        offset += PAGE_SIZE
    logger.info("Existing assignments: %d", len(existing))

    # Pre-compute first L3 per L1 (used as placeholder)
    first_l3_for_l1: dict[str, str] = {}
    for l1_slug in ("agentic-ai", "voice-ai", "secure-ai"):
        slugs = get_l3_slugs_for_l1(l1_slug)
        if slugs:
            first_l3_for_l1[l1_slug] = slugs[0]

    rows_to_insert: list[dict] = []
    matched = 0
    skipped_no_match = 0
    skipped_exists = 0

    for comp in companies:
        sub = comp.get("sub_category")
        if not sub:
            skipped_no_match += 1
            continue

        l1 = L1_BY_SUBCATEGORY.get(sub)
        if not l1 or l1 not in first_l3_for_l1:
            skipped_no_match += 1
            continue

        l3_slug = first_l3_for_l1[l1]
        cid = comp["id"]

        if (cid, l3_slug) in existing:
            skipped_exists += 1
            continue

        rows_to_insert.append({
            "company_id": cid,
            "l3_slug": l3_slug,
            "assigned_by": "backfill-l1",
        })
        matched += 1

    logger.info("Companies matched for L1 assignment: %d", matched)
    logger.info("Skipped (no L1 match): %d", skipped_no_match)
    logger.info("Skipped (already assigned): %d", skipped_exists)

    if not rows_to_insert:
        logger.info("Nothing to insert.")
        return

    if args.dry_run:
        logger.info("[DRY RUN] Would insert %d topic assignments", len(rows_to_insert))
        # Show sample
        for row in rows_to_insert[:5]:
            logger.info("  %s → %s", row["company_id"][:8], row["l3_slug"])
        return

    # Batch insert (Supabase handles up to 1000 rows per call)
    for i in range(0, len(rows_to_insert), PAGE_SIZE):
        batch = rows_to_insert[i : i + PAGE_SIZE]
        client.table("su_company_topics").upsert(batch, on_conflict="company_id,l3_slug").execute()
        logger.info("Inserted batch %d–%d", i + 1, i + len(batch))

    logger.info("=" * 50)
    logger.info("Topic backfill complete: %d assignments created", len(rows_to_insert))


if __name__ == "__main__":
    main()
