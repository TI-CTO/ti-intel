"""Fix funding data for top 10 companies with verified round-by-round records."""

import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from startup_db.config import settings  # noqa: E402  # isort: skip
from supabase import create_client  # noqa: E402  # isort: skip

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)


def _r(round_type: str, date: str, amount: int, note: str | None = None) -> dict:
    """Build a round dict with default currency USD."""
    return {
        "round_type": round_type,
        "date": date,
        "amount": amount,
        "currency": "USD",
        "note": note,
    }


# ---------------------------------------------------------------------------
# Data definitions
# Each entry: slug, rounds, total_raised, growth_stage, extra_updates
# ---------------------------------------------------------------------------

COMPANIES_DATA = [
    {
        "slug": "databricks",
        "rounds": [
            _r("series_a", "2013-09-11", 14_000_000),
            _r("series_b", "2014-07-17", 33_000_000),
            _r("series_c", "2016-12-15", 60_000_000),
            _r("series_d", "2017-08-22", 140_000_000),
            _r("series_e", "2019-02-05", 250_000_000),
            _r("series_f", "2019-10-22", 400_000_000),
            _r("other", "2021-02-01", 1_000_000_000, "Series G"),
            _r("other", "2021-08-31", 1_600_000_000, "Series H"),
            _r("other", "2023-09-14", 500_000_000, "Series I"),
            _r("other", "2024-11-01", 10_000_000_000, "Series J"),
        ],
        "total_raised": 14_000_000_000,
        "growth_stage": "late",
        "extra_updates": {},
    },
    {
        "slug": "automation-anywhere",
        "rounds": [
            _r("series_a", "2018-07-02", 250_000_000),
            _r("series_a", "2018-11-15", 300_000_000),
            _r("series_b", "2019-11-21", 290_000_000),
        ],
        "total_raised": 840_000_000,
        "growth_stage": "late",
        "extra_updates": {"status": "active"},
    },
    {
        "slug": "openai",
        "rounds": [
            _r("other", "2015-12-01", 130_000_000, "Grant"),
            _r("series_d", "2019-07-22", 1_000_000_000),
            _r("series_e", "2023-04-28", 10_000_000_000),
            _r("series_f", "2025-03-31", 40_000_000_000),
        ],
        "total_raised": 51_130_000_000,
        "growth_stage": "late",
        "extra_updates": {},
    },
    {
        "slug": "xai",
        "rounds": [
            _r("seed", "2023-12-01", 135_000_000),
            _r("series_b", "2024-05-26", 6_000_000_000),
            _r("series_c", "2024-12-05", 6_000_000_000),
        ],
        "total_raised": 12_135_000_000,
        "growth_stage": "late",
        "extra_updates": {},
    },
    {
        "slug": "edge-impulse",
        "rounds": [
            _r("series_a", "2021-05-01", 15_000_000),
            _r("series_b", "2021-12-09", 34_000_000),
            _r("acquired", "2025-03-31", 0, "Qualcomm acquisition, price not disclosed"),
        ],
        "total_raised": 49_000_000,
        "growth_stage": "late",
        "extra_updates": {"status": "acquired"},
    },
    {
        "slug": "moveworks",
        "rounds": [
            _r("series_a", "2019-04-17", 30_000_000),
            _r("series_b", "2019-11-01", 75_000_000),
            _r("series_c", "2021-06-01", 200_000_000),
            _r("acquired", "2025-12-15", 2_850_000_000),
        ],
        "total_raised": 305_000_000,
        "growth_stage": "late",
        "extra_updates": {"status": "acquired"},
    },
    {
        "slug": "celonis",
        "rounds": [
            _r("series_a", "2016-06-01", 27_500_000),
            _r("series_b", "2018-06-26", 50_000_000),
            _r("series_c", "2019-11-21", 290_000_000),
            _r("series_d", "2021-06-02", 1_000_000_000),
            _r("other", "2022-08-23", 400_000_000, "Series D Extension"),
        ],
        "total_raised": 1_767_500_000,
        "growth_stage": "late",
        "extra_updates": {},
    },
    {
        "slug": "prosper-robotics",
        "rounds": [],
        "total_raised": 0,
        "growth_stage": "pre-seed",
        "extra_updates": {},
    },
    {
        "slug": "bentoml",
        "rounds": [
            _r("seed", "2023-06-27", 9_000_000),
            _r("series_a", "2024-07-09", 9_000_000),
        ],
        "total_raised": 18_000_000,
        "growth_stage": "early",
        "extra_updates": {},
    },
    {
        "slug": "barracuda-networks",
        "rounds": [
            _r("series_a", "2006-01-09", 40_000_000),
            _r("series_b", "2009-01-01", 5_600_000),
            _r("series_c", "2012-10-03", 130_000_000),
            _r("ipo", "2013-11-13", 0),
            _r("acquired", "2018-01-01", 1_600_000_000, "Thoma Bravo"),
        ],
        "total_raised": 175_600_000,
        "growth_stage": "late",
        "extra_updates": {"status": "acquired"},
    },
]


def get_company_id(client, slug: str) -> str | None:
    """Fetch the company UUID for a given slug.

    Args:
        client: Supabase client instance.
        slug: Company slug identifier.

    Returns:
        Company UUID string, or None if not found.
    """
    res = client.table("su_companies").select("id").eq("slug", slug).single().execute()
    if res.data:
        return res.data["id"]
    return None


def delete_funding_rounds(client, company_id: str) -> int:
    """Delete all funding rounds for a company.

    Args:
        client: Supabase client instance.
        company_id: Company UUID.

    Returns:
        Number of deleted rows.
    """
    res = client.table("su_funding_rounds").delete().eq("company_id", company_id).execute()
    return len(res.data) if res.data else 0


def insert_funding_round(client, company_id: str, round_data: dict) -> None:
    """Insert a single funding round record.

    Args:
        client: Supabase client instance.
        company_id: Company UUID.
        round_data: Dict with round_type, date, amount, currency, note.
    """
    payload = {
        "company_id": company_id,
        "round_type": round_data["round_type"],
        "announced_date": round_data["date"],
        "raised_amount": round_data["amount"],
        "currency": round_data["currency"],
        "metadata": {"note": round_data["note"]} if round_data.get("note") else {},
    }
    client.table("su_funding_rounds").insert(payload).execute()


def update_company(
    client,
    company_id: str,
    rounds: list[dict],
    total_raised: int,
    growth_stage: str,
    extra: dict,
) -> None:
    """Update su_companies summary fields after funding round changes.

    Args:
        client: Supabase client instance.
        company_id: Company UUID.
        rounds: List of round dicts (sorted by date ascending in COMPANIES_DATA).
        total_raised: Total raised amount in USD.
        growth_stage: Growth stage string.
        extra: Additional fields to update (e.g. status).
    """
    update_payload: dict = {
        "total_raised": total_raised,
        "growth_stage": growth_stage,
    }

    if rounds:
        last_round = max(rounds, key=lambda r: r["date"])
        update_payload["last_funding_date"] = last_round["date"]
        update_payload["last_funding_type"] = last_round["round_type"]
    else:
        update_payload["last_funding_date"] = None
        update_payload["last_funding_type"] = None

    update_payload.update(extra)
    client.table("su_companies").update(update_payload).eq("id", company_id).execute()


def process_company(client, entry: dict) -> None:
    """Process a single company: delete rounds, insert corrected rounds, update summary.

    Args:
        client: Supabase client instance.
        entry: Company data dict from COMPANIES_DATA.
    """
    slug = entry["slug"]
    log.info("[%s] Starting...", slug)

    company_id = get_company_id(client, slug)
    if not company_id:
        log.warning("[%s] Company not found — skipping", slug)
        return

    deleted = delete_funding_rounds(client, company_id)
    log.info("[%s] Deleted %d existing rounds", slug, deleted)

    rounds = entry["rounds"]
    for i, r in enumerate(rounds, 1):
        insert_funding_round(client, company_id, r)
        log.info(
            "[%s]   Inserted round %d/%d: %s %s $%s",
            slug,
            i,
            len(rounds),
            r["round_type"],
            r["date"],
            f"{r['amount']:,}",
        )

    update_company(
        client,
        company_id,
        rounds,
        entry["total_raised"],
        entry["growth_stage"],
        entry["extra_updates"],
    )
    extra_str = f", extra={entry['extra_updates']}" if entry["extra_updates"] else ""
    log.info(
        "[%s] Updated company: total_raised=$%s, growth_stage=%s%s",
        slug,
        f"{entry['total_raised']:,}",
        entry["growth_stage"],
        extra_str,
    )
    log.info("[%s] Done.", slug)


def main() -> None:
    """Entry point: fix funding data for all top 10 companies."""
    client = create_client(settings.supabase_url, settings.supabase_key)
    log.info("Connected to Supabase. Processing %d companies...", len(COMPANIES_DATA))

    success = 0
    failed = 0
    for entry in COMPANIES_DATA:
        try:
            process_company(client, entry)
            success += 1
        except Exception as exc:
            log.error("[%s] FAILED: %s", entry["slug"], exc)
            failed += 1

    log.info("=== Completed: %d succeeded, %d failed ===", success, failed)


if __name__ == "__main__":
    main()
