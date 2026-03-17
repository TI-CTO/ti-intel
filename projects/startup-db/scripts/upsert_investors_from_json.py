"""Upsert investor data from JSON files into su_investors table.

Usage:
    cd projects/startup-db
    uv run python scripts/upsert_investors_from_json.py /tmp/batch1_investors.json [/tmp/batch2_investors.json ...]

JSON format:
  [{"company_slug": "openai", "investors": [{"name": "Microsoft", "type": "cvc"}, ...]}, ...]
"""

from __future__ import annotations

import json
import logging
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from startup_db.db import StartupRepository  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s", datefmt="%H:%M:%S")
logger = logging.getLogger(__name__)


def slugify(name: str) -> str:
    """Convert investor name to URL-safe slug."""
    s = name.lower().strip()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[\s]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def main() -> None:
    """Load JSON files and upsert investors."""
    if len(sys.argv) < 2:
        print("Usage: upsert_investors_from_json.py <file1.json> [file2.json ...]")
        sys.exit(1)

    repo = StartupRepository()

    all_entries: list[dict] = []
    for fpath in sys.argv[1:]:
        with open(fpath) as f:
            data = json.load(f)
        all_entries.extend(data)
        logger.info("Loaded %d companies from %s", len(data), fpath)

    # Deduplicate investors across all entries
    investor_map: dict[str, dict] = {}  # slug -> {name, type}
    company_investors: list[tuple[str, list[str]]] = []  # (company_slug, [investor_slugs])

    for entry in all_entries:
        company_slug = entry["company_slug"]
        inv_slugs: list[str] = []
        for inv in entry.get("investors", []):
            inv_slug = slugify(inv["name"])
            if not inv_slug:
                continue
            if inv_slug not in investor_map:
                investor_map[inv_slug] = {
                    "name": inv["name"],
                    "type": inv.get("type", "vc"),
                }
            inv_slugs.append(inv_slug)
        company_investors.append((company_slug, inv_slugs))

    logger.info("Unique investors to upsert: %d", len(investor_map))
    logger.info("Companies with investor data: %d", len(company_investors))

    # Batch upsert investors
    upserted = 0
    errors = 0
    for inv_slug, inv_data in investor_map.items():
        try:
            repo._client.table("su_investors").upsert(
                {
                    "slug": inv_slug,
                    "name": inv_data["name"],
                    "investor_type": inv_data["type"],
                    "metadata": json.dumps({"source": "web_search", "collected": "2026-03-16"}),
                },
                on_conflict="slug",
            ).execute()
            upserted += 1
        except Exception as e:
            logger.warning("Failed to upsert %s: %s", inv_slug, e)
            errors += 1

    logger.info("Investors upserted: %d, errors: %d", upserted, errors)

    # Link investors to companies via su_round_investors
    # First get investor IDs
    inv_result = repo._client.table("su_investors").select("id,slug").execute()
    inv_id_map: dict[str, str] = {r["slug"]: r["id"] for r in inv_result.data}

    linked = 0
    for company_slug, inv_slugs in company_investors:
        # Get company's funding rounds
        company = repo.get_company_by_slug(company_slug)
        if not company:
            logger.warning("Company not found: %s", company_slug)
            continue

        rounds_result = (
            repo._client.table("su_funding_rounds")
            .select("id")
            .eq("company_id", company["id"])
            .order("raised_amount", desc=True)
            .limit(1)
            .execute()
        )
        if not rounds_result.data:
            continue

        round_id = rounds_result.data[0]["id"]

        for inv_slug in inv_slugs:
            inv_id = inv_id_map.get(inv_slug)
            if not inv_id:
                continue
            try:
                repo._client.table("su_round_investors").upsert(
                    {
                        "round_id": round_id,
                        "investor_id": inv_id,
                        "role": "participant",
                    },
                    on_conflict="round_id,investor_id",
                ).execute()
                linked += 1
            except Exception as e:
                logger.warning("Failed to link %s → %s: %s", company_slug, inv_slug, e)

    logger.info("Round-investor links created: %d", linked)
    logger.info("Done.")


if __name__ == "__main__":
    main()
