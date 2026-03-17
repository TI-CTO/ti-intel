"""Backfill derived enrichment fields on su_companies.

Computes from existing data:
- one_liner: first sentence of description (max 120 chars)
- total_raised: SUM(su_funding_rounds.raised_amount) per company
- last_funding_date: MAX(su_funding_rounds.announced_date)
- last_funding_type: round_type of the most recent round
- growth_stage: derived from last_funding_type

Usage:
    cd projects/startup-db
    uv run python scripts/backfill_enrichment.py
    uv run python scripts/backfill_enrichment.py --dry-run
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from supabase import create_client  # noqa: E402

from startup_db.config import settings  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

PAGE_SIZE = 1000

# round_type → growth_stage mapping
_STAGE_BY_ROUND: dict[str, str] = {
    "pre_seed": "pre-seed",
    "seed": "seed",
    "series_a": "early",
    "series_b": "early",
    "series_c": "growth",
    "series_d": "growth",
    "series_e": "late",
    "series_f": "late",
    "ipo": "public",
    "acquired": "late",
}


def extract_one_liner(description: str | None) -> str | None:
    """Extract first sentence from description, max 120 chars."""
    if not description:
        return None
    # Split on sentence-ending punctuation
    match = re.match(r"^(.+?[.!?。])\s", description)
    if match:
        sentence = match.group(1).strip()
    else:
        sentence = description.strip()
    if len(sentence) > 120:
        sentence = sentence[:117] + "..."
    return sentence


def main() -> None:
    """Run the enrichment backfill."""
    parser = argparse.ArgumentParser(description="Backfill enrichment fields on su_companies.")
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
            .select("id,description")
            .range(offset, offset + PAGE_SIZE - 1)
            .execute()
        )
        companies.extend(batch.data or [])
        if len(batch.data or []) < PAGE_SIZE:
            break
        offset += PAGE_SIZE
    logger.info("Fetched %d companies", len(companies))

    # Fetch all funding rounds
    logger.info("Fetching funding rounds...")
    rounds: list[dict] = []
    offset = 0
    while True:
        batch = (
            client.table("su_funding_rounds")
            .select("company_id,raised_amount,announced_date,round_type")
            .range(offset, offset + PAGE_SIZE - 1)
            .execute()
        )
        rounds.extend(batch.data or [])
        if len(batch.data or []) < PAGE_SIZE:
            break
        offset += PAGE_SIZE
    logger.info("Fetched %d funding rounds", len(rounds))

    # Aggregate per company
    rounds_by_company: dict[str, list[dict]] = defaultdict(list)
    for r in rounds:
        rounds_by_company[r["company_id"]].append(r)

    updated = 0
    skipped = 0

    for comp in companies:
        cid = comp["id"]
        updates: dict[str, object] = {}

        # one_liner
        one_liner = extract_one_liner(comp.get("description"))
        if one_liner:
            updates["one_liner"] = one_liner

        # Funding-derived fields
        comp_rounds = rounds_by_company.get(cid, [])
        if comp_rounds:
            total = sum(r.get("raised_amount") or 0 for r in comp_rounds)
            updates["total_raised"] = total

            # Find most recent round
            dated = [r for r in comp_rounds if r.get("announced_date")]
            if dated:
                latest = max(dated, key=lambda r: r["announced_date"])
                updates["last_funding_date"] = latest["announced_date"]
                updates["last_funding_type"] = latest.get("round_type")

                # Derive growth_stage
                rt = latest.get("round_type", "")
                stage = _STAGE_BY_ROUND.get(rt)
                if stage:
                    updates["growth_stage"] = stage

        if not updates:
            skipped += 1
            continue

        if args.dry_run:
            logger.debug("[DRY RUN] %s: %s", cid[:8], updates)
        else:
            client.table("su_companies").update(updates).eq("id", cid).execute()

        updated += 1

    logger.info("=" * 50)
    logger.info("Enrichment backfill %s", "preview" if args.dry_run else "complete")
    logger.info("  Updated: %d", updated)
    logger.info("  Skipped: %d", skipped)


if __name__ == "__main__":
    main()
