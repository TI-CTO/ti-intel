"""Backfill su_scores from metadata.tech_competitiveness in su_companies.

Reads the tech_competitiveness field (integer 1-5) from each company's metadata
and inserts an initial su_scores record with tech_strength converted to the 1-10
scale (tech_competitiveness * 2). Companies that already have a score are skipped.

Usage:
    cd projects/startup-db
    uv run python scripts/backfill_scores.py
"""

from __future__ import annotations

import json
import logging
import sys
from pathlib import Path
from typing import Any

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from supabase import Client, create_client  # noqa: E402

from startup_db.config import settings  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

BATCH_SIZE = 100
SCORES_TABLE = "su_scores"
SCORED_BY = "csv_migration"
RATIONALE = "Initial score from CSV tech_competitiveness field"


def get_client() -> Client:
    """Return a Supabase client using project settings.

    Returns:
        Authenticated Supabase client instance.
    """
    return create_client(settings.supabase_url, settings.supabase_key)


def fetch_all_companies(client: Client) -> list[dict[str, Any]]:
    """Fetch all companies with id, name, slug, and metadata from su_companies.

    Uses paginated requests to retrieve the full dataset regardless of size.

    Args:
        client: Authenticated Supabase client.

    Returns:
        List of company row dicts containing id, name, slug, and metadata.
    """
    rows: list[dict[str, Any]] = []
    page_size = 1000
    offset = 0

    while True:
        result = (
            client.table("su_companies")
            .select("id,name,slug,metadata")
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


def fetch_scored_company_ids(client: Client) -> set[str]:
    """Fetch the set of company IDs that already have a score in su_scores.

    Uses paginated requests to collect all existing scored company IDs.

    Args:
        client: Authenticated Supabase client.

    Returns:
        Set of company UUID strings that already have at least one score record.
    """
    scored_ids: list[str] = []
    page_size = 1000
    offset = 0

    while True:
        result = (
            client.table(SCORES_TABLE)
            .select("company_id")
            .range(offset, offset + page_size - 1)
            .execute()
        )
        batch = result.data or []
        scored_ids.extend(row["company_id"] for row in batch)
        if len(batch) < page_size:
            break
        offset += page_size

    result_set = set(scored_ids)
    logger.info("Companies already scored: %d", len(result_set))
    return result_set


def parse_metadata(raw: Any) -> dict[str, Any]:
    """Parse a metadata value that may be a JSON string or a dict.

    Args:
        raw: The raw metadata value from the database row. May be a dict,
            a JSON-encoded string, or None.

    Returns:
        Parsed metadata dict, or an empty dict if parsing fails or input is None.
    """
    if raw is None:
        return {}
    if isinstance(raw, dict):
        return raw
    if isinstance(raw, str):
        try:
            parsed = json.loads(raw)
            return parsed if isinstance(parsed, dict) else {}
        except (json.JSONDecodeError, ValueError):
            return {}
    return {}


def build_score_rows(
    companies: list[dict[str, Any]],
    scored_ids: set[str],
) -> list[dict[str, Any]]:
    """Build su_scores insert rows from companies with tech_competitiveness metadata.

    Converts tech_competitiveness (1-5 scale) to tech_strength (1-10 scale)
    by multiplying by 2. Companies already in scored_ids are skipped.

    Args:
        companies: List of company dicts with id, name, slug, and metadata fields.
        scored_ids: Set of company IDs that already have a score record.

    Returns:
        List of score row dicts ready for insertion into su_scores.
    """
    rows: list[dict[str, Any]] = []
    missing_field = 0
    already_scored = 0

    for company in companies:
        company_id = company["id"]

        if company_id in scored_ids:
            already_scored += 1
            continue

        metadata = parse_metadata(company.get("metadata"))
        raw_tc = metadata.get("tech_competitiveness")

        if raw_tc is None:
            missing_field += 1
            continue

        try:
            tc = int(raw_tc)
        except (ValueError, TypeError):
            logger.warning(
                "Company %s (%s): non-integer tech_competitiveness=%r, skipping",
                company.get("name"),
                company_id,
                raw_tc,
            )
            missing_field += 1
            continue

        if not (1 <= tc <= 5):
            logger.warning(
                "Company %s (%s): tech_competitiveness=%d out of range 1-5, skipping",
                company.get("name"),
                company_id,
                tc,
            )
            missing_field += 1
            continue

        tech_strength = tc * 2

        rows.append(
            {
                "company_id": company_id,
                "tech_strength": tech_strength,
                "scored_by": SCORED_BY,
                "rationale": RATIONALE,
            }
        )

    logger.info(
        "Score rows to insert: %d | already scored (skipped): %d | no tech_competitiveness: %d",
        len(rows),
        already_scored,
        missing_field,
    )
    return rows


def batch_insert_scores(
    client: Client,
    score_rows: list[dict[str, Any]],
) -> int:
    """Insert score rows into su_scores in batches.

    Args:
        client: Authenticated Supabase client.
        score_rows: List of score row dicts to insert.

    Returns:
        Total number of rows inserted.
    """
    if not score_rows:
        return 0

    total = 0
    for i in range(0, len(score_rows), BATCH_SIZE):
        batch = score_rows[i : i + BATCH_SIZE]
        client.table(SCORES_TABLE).insert(batch).execute()
        total += len(batch)
        logger.info(
            "  Inserted scores %d-%d / %d",
            i + 1,
            i + len(batch),
            len(score_rows),
        )

    return total


def backfill(client: Client) -> None:
    """Run the full score backfill pipeline.

    Steps:
      1. Fetch all companies (id, name, slug, metadata).
      2. Fetch company IDs that already have a score (for skip logic).
      3. Build score rows from companies with metadata.tech_competitiveness.
      4. Batch-insert new score rows into su_scores.
      5. Log a final summary.

    Args:
        client: Authenticated Supabase client.
    """
    companies = fetch_all_companies(client)
    scored_ids = fetch_scored_company_ids(client)

    score_rows = build_score_rows(companies, scored_ids)

    with_tc = sum(
        1
        for c in companies
        if parse_metadata(c.get("metadata")).get("tech_competitiveness") is not None
    )
    logger.info("Companies with tech_competitiveness field: %d", with_tc)

    if not score_rows:
        logger.info("No new scores to insert. Done.")
        return

    inserted = batch_insert_scores(client, score_rows)

    logger.info("Backfill complete.")
    logger.info("  Total companies fetched:           %d", len(companies))
    logger.info("  Companies with tech_competitiveness: %d", with_tc)
    logger.info("  Scores created:                    %d", inserted)
    logger.info("  Companies skipped (already scored): %d", len(scored_ids))


def main() -> None:
    """Entry point for the score backfill script."""
    client = get_client()
    backfill(client)


if __name__ == "__main__":
    main()
