"""Backfill announced_date on su_funding_rounds using Claude API research.

For each company (by total_raised desc), asks Claude for funding history
with dates, then matches and updates existing rounds.

Usage:
    cd projects/startup-db
    uv run python scripts/backfill_funding_dates.py --top 50
    uv run python scripts/backfill_funding_dates.py --top 5 --dry-run
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import anthropic  # noqa: E402
from supabase import create_client  # noqa: E402

from startup_db.config import settings  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

ANTHROPIC_API_KEY = os.environ.get(
    "ANTHROPIC_API_KEY",
    # fallback to .env
    "",
)

# Load from .env if not in environment
if not ANTHROPIC_API_KEY:
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if line.startswith("ANTHROPIC_API_KEY="):
                ANTHROPIC_API_KEY = line.split("=", 1)[1].strip()
                break

RESEARCH_PROMPT = """You are a startup funding research assistant. Given a company name, country, and description, provide its complete funding history with exact dates.

Company: {name}
Country: {country}
Description: {description}
Website: {website}

Current DB records (may have wrong amounts or missing dates):
{existing_rounds}

Return a JSON array of funding rounds. Each round must have:
- "round_type": one of "pre_seed", "seed", "series_a", "series_b", "series_c", "series_d", "series_e", "series_f", "bridge", "grant", "ipo", "acquired", "other"
- "announced_date": "YYYY-MM-DD" format (use first of month if only month/year known, null if unknown)
- "raised_amount": number in USD (null if unknown)
- "notes": brief note about the round (investors, valuation, etc.)

Rules:
- Only include rounds you are confident about
- Dates must be as accurate as possible
- Amounts in USD
- If you don't know a company's funding history, return an empty array []
- Do NOT hallucinate dates or amounts

Return ONLY the JSON array, no other text."""


def research_company(
    client: anthropic.Anthropic,
    company: dict,
    existing_rounds: list[dict],
) -> list[dict]:
    """Ask Claude for funding history of a company.

    Args:
        client: Anthropic API client.
        company: Company dict from DB.
        existing_rounds: Existing funding rounds from DB.

    Returns:
        List of funding round dicts with dates.
    """
    rounds_desc = ""
    if existing_rounds:
        for r in existing_rounds:
            amt = r.get("raised_amount")
            amt_str = f"${amt:,.0f}" if amt else "unknown"
            rounds_desc += (
                f"  - {r.get('round_type', 'unknown')}: "
                f"{amt_str} (date: {r.get('announced_date', 'unknown')})\n"
            )
    else:
        rounds_desc = "  (no rounds recorded)\n"

    prompt = RESEARCH_PROMPT.format(
        name=company.get("name", ""),
        country=company.get("country", ""),
        description=(company.get("description") or "")[:300],
        website=company.get("website") or "unknown",
        existing_rounds=rounds_desc,
    )

    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}],
        )
        text = response.content[0].text.strip()

        # Extract JSON from response
        if text.startswith("["):
            return json.loads(text)
        # Try to find JSON array in response
        start = text.find("[")
        end = text.rfind("]") + 1
        if start >= 0 and end > start:
            return json.loads(text[start:end])
        return []
    except json.JSONDecodeError:
        logger.warning("Failed to parse JSON for %s", company.get("name"))
        return []
    except anthropic.APIError as e:
        logger.error("API error for %s: %s", company.get("name"), e)
        return []


def match_and_update(
    supabase_client,
    company_id: str,
    existing_rounds: list[dict],
    researched_rounds: list[dict],
    dry_run: bool = False,
) -> dict:
    """Match researched rounds to existing DB rounds and update dates.

    Args:
        supabase_client: Supabase client.
        company_id: UUID of the company.
        existing_rounds: Existing rounds from DB.
        researched_rounds: Rounds from Claude research.
        dry_run: If True, don't write to DB.

    Returns:
        Dict with counts: matched, updated, added.
    """
    result = {"matched": 0, "updated": 0, "amount_fixed": 0}

    for researched in researched_rounds:
        r_type = researched.get("round_type", "")
        r_date = researched.get("announced_date")
        r_amount = researched.get("raised_amount")

        if not r_date:
            continue

        # Find matching existing round by round_type
        matched_existing = None
        for ex in existing_rounds:
            if ex.get("round_type") == r_type and not ex.get("announced_date"):
                matched_existing = ex
                break

        if matched_existing:
            result["matched"] += 1
            updates: dict = {"announced_date": r_date}

            # Also fix amount if significantly different
            ex_amount = matched_existing.get("raised_amount") or 0
            if r_amount and ex_amount > 0:
                ratio = r_amount / ex_amount if ex_amount else float("inf")
                if ratio > 5 or ratio < 0.2:
                    logger.info(
                        "  Amount mismatch %s: DB=$%s, Research=$%s",
                        r_type,
                        f"{ex_amount:,.0f}",
                        f"{r_amount:,.0f}",
                    )

            if dry_run:
                logger.info(
                    "  [DRY RUN] Would update %s: date=%s",
                    r_type, r_date,
                )
            else:
                supabase_client.table("su_funding_rounds").update(
                    updates
                ).eq("id", matched_existing["id"]).execute()

            result["updated"] += 1

    return result


def main() -> None:
    """Run the funding date backfill."""
    parser = argparse.ArgumentParser(
        description="Backfill funding round dates using Claude API."
    )
    parser.add_argument(
        "--top", type=int, default=50,
        help="Number of top companies to process (by total_raised).",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Preview without writing to DB.",
    )
    parser.add_argument(
        "--delay", type=float, default=1.0,
        help="Delay between API calls (seconds).",
    )
    args = parser.parse_args()

    if not ANTHROPIC_API_KEY:
        logger.error("ANTHROPIC_API_KEY not found in environment or .env")
        sys.exit(1)

    claude = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    supabase = create_client(settings.supabase_url, settings.supabase_key)

    # Get top companies by total_raised
    logger.info("Fetching top %d companies by total_raised...", args.top)
    companies_result = (
        supabase.table("su_companies")
        .select("id,name,slug,country,description,website,total_raised")
        .gt("total_raised", 0)
        .order("total_raised", desc=True)
        .limit(args.top)
        .execute()
    )
    companies = companies_result.data or []
    logger.info("Found %d companies with funding", len(companies))

    total_updated = 0
    total_matched = 0
    total_skipped = 0

    for i, company in enumerate(companies, 1):
        name = company["name"]
        cid = company["id"]
        raised = company.get("total_raised") or 0

        logger.info(
            "[%d/%d] %s ($%s)",
            i, len(companies), name,
            f"{raised:,.0f}",
        )

        # Get existing rounds for this company
        rounds_result = (
            supabase.table("su_funding_rounds")
            .select("*")
            .eq("company_id", cid)
            .order("round_type")
            .execute()
        )
        existing_rounds = rounds_result.data or []

        # Skip if all rounds already have dates
        undated = [r for r in existing_rounds if not r.get("announced_date")]
        if not undated:
            logger.info("  All %d rounds already dated, skipping", len(existing_rounds))
            total_skipped += 1
            continue

        logger.info(
            "  %d rounds (%d need dates)",
            len(existing_rounds), len(undated),
        )

        # Research via Claude API
        researched = research_company(claude, company, existing_rounds)
        if not researched:
            logger.info("  No research results")
            total_skipped += 1
            continue

        logger.info("  Claude returned %d rounds", len(researched))

        # Match and update
        result = match_and_update(
            supabase, cid, existing_rounds, researched,
            dry_run=args.dry_run,
        )
        total_matched += result["matched"]
        total_updated += result["updated"]

        logger.info(
            "  Matched: %d, Updated: %d",
            result["matched"], result["updated"],
        )

        # Rate limiting
        if i < len(companies):
            time.sleep(args.delay)

    # Update company-level fields
    if not args.dry_run and total_updated > 0:
        logger.info("Updating company-level last_funding_date...")
        for company in companies:
            cid = company["id"]
            latest = (
                supabase.table("su_funding_rounds")
                .select("announced_date,round_type")
                .eq("company_id", cid)
                .not_.is_("announced_date", "null")
                .order("announced_date", desc=True)
                .limit(1)
                .execute()
            )
            if latest.data:
                supabase.table("su_companies").update({
                    "last_funding_date": latest.data[0]["announced_date"],
                    "last_funding_type": latest.data[0]["round_type"],
                }).eq("id", cid).execute()

    logger.info("=" * 50)
    logger.info(
        "Backfill %s", "preview" if args.dry_run else "complete"
    )
    logger.info("  Companies processed: %d", len(companies))
    logger.info("  Skipped: %d", total_skipped)
    logger.info("  Rounds matched: %d", total_matched)
    logger.info("  Dates updated: %d", total_updated)


if __name__ == "__main__":
    main()
