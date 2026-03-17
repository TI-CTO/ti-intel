"""Fix funding data for batch 2 — 10 companies with verified round-by-round records."""

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
        "slug": "wayve",
        "rounds": [
            _r("seed", "2017-09-30", 2_150_000),
            _r("series_a", "2019-11-01", 20_000_000),
            _r("series_b", "2022-01-01", 200_000_000),
            _r("series_c", "2024-05-06", 1_050_000_000),
            _r("series_d", "2026-02-25", 1_200_000_000),
        ],
        "total_raised": 2_472_150_000,
        "growth_stage": "late",
        "last_funding_date": "2026-02-25",
        "last_funding_type": "series_d",
        "extra_updates": {},
    },
    {
        "slug": "sendbird",
        "rounds": [
            _r("seed", "2015-11-01", 120_000),
            _r("series_a", "2017-12-20", 16_000_000),
            _r("series_b", "2019-05-01", 102_000_000),
            _r("series_c", "2021-04-06", 100_000_000),
        ],
        "total_raised": 218_120_000,
        "growth_stage": "growth",
        "last_funding_date": "2021-04-06",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    {
        "slug": "groq",
        "rounds": [
            _r("series_a", "2016-12-07", 10_300_000),
            _r("seed", "2017-04-01", 10_000_000),
            _r("series_b", "2018-09-05", 52_300_000),
            _r("series_c", "2021-04-14", 300_000_000),
            _r("series_d", "2024-08-01", 640_000_000),
            _r("series_e", "2025-09-17", 750_000_000),
        ],
        "total_raised": 1_762_600_000,
        "growth_stage": "late",
        "last_funding_date": "2025-09-17",
        "last_funding_type": "series_e",
        "extra_updates": {},
    },
    {
        "slug": "figure",
        "rounds": [
            _r("seed", "2022-05-01", 100_000_000),
            _r("series_a", "2023-05-24", 70_000_000),
            _r("series_b", "2024-02-01", 675_000_000),
            _r("series_c", "2025-09-16", 1_000_000_000),
        ],
        "total_raised": 1_845_000_000,
        "growth_stage": "late",
        "last_funding_date": "2025-09-16",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    {
        "slug": "lightmatter",
        "rounds": [
            _r("series_a", "2019-02-26", 33_000_000),
            _r("series_b", "2021-05-06", 80_000_000),
            _r("series_c", "2023-05-31", 154_000_000),
            _r("other", "2023-12-01", 155_000_000, "Series C-2"),
            _r("series_d", "2024-10-16", 400_000_000),
        ],
        "total_raised": 822_000_000,
        "growth_stage": "late",
        "last_funding_date": "2024-10-16",
        "last_funding_type": "series_d",
        "extra_updates": {},
    },
    {
        "slug": "messagebird",
        "rounds": [
            _r("pre_seed", "2016-08-01", 120_000),
            _r("series_a", "2017-10-03", 60_000_000),
            _r("series_b", "2019-02-01", 40_000_000),
            _r("series_c", "2020-10-08", 200_000_000),
            _r("other", "2021-04-28", 800_000_000, "Series C-2"),
        ],
        "total_raised": 1_100_120_000,
        "growth_stage": "late",
        "last_funding_date": "2021-04-28",
        "last_funding_type": "other",
        "extra_updates": {},
    },
    {
        "slug": "saronic",
        "rounds": [
            _r("series_a", "2023-10-09", 55_000_000),
            _r("series_b", "2024-07-19", 175_000_000),
            _r("series_c", "2025-02-19", 600_000_000),
        ],
        "total_raised": 830_000_000,
        "growth_stage": "growth",
        "last_funding_date": "2025-02-19",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    {
        "slug": "moonshot-ai",
        "rounds": [
            _r("seed", "2023-06-01", 60_000_000),
            _r("series_a", "2024-02-21", 1_000_000_000),
            _r("series_b", "2024-08-05", 300_000_000),
            _r("series_c", "2025-12-31", 500_000_000),
            _r("series_d", "2026-02-18", 700_000_000),
        ],
        "total_raised": 2_560_000_000,
        "growth_stage": "late",
        "last_funding_date": "2026-02-18",
        "last_funding_type": "series_d",
        "extra_updates": {},
    },
    {
        "slug": "helsing",
        "rounds": [
            _r("series_a", "2021-11-09", 122_000_000),
            _r("series_c", "2024-07-11", 487_000_000),
            _r("series_d", "2025-06-17", 694_000_000),
        ],
        "total_raised": 1_303_000_000,
        "growth_stage": "late",
        "last_funding_date": "2025-06-17",
        "last_funding_type": "series_d",
        "extra_updates": {},
    },
    {
        "slug": "coreweave",
        "rounds": [
            _r("series_b", "2023-04-20", 221_000_000),
            _r("other", "2023-05-20", 200_000_000, "Series B Extension"),
            _r("series_c", "2024-05-01", 1_100_000_000),
            _r("ipo", "2025-03-28", 1_500_000_000),
        ],
        "total_raised": 1_521_000_000,
        "growth_stage": "public",
        "last_funding_date": "2025-03-28",
        "last_funding_type": "ipo",
        "extra_updates": {"status": "ipo"},
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
    total_raised: int,
    growth_stage: str,
    last_funding_date: str,
    last_funding_type: str,
    extra: dict,
) -> None:
    """Update su_companies summary fields after funding round changes.

    Args:
        client: Supabase client instance.
        company_id: Company UUID.
        total_raised: Total raised amount in USD.
        growth_stage: Growth stage string.
        last_funding_date: Date of most recent funding round.
        last_funding_type: Round type of most recent funding round.
        extra: Additional fields to update (e.g. status).
    """
    update_payload: dict = {
        "total_raised": total_raised,
        "growth_stage": growth_stage,
        "last_funding_date": last_funding_date,
        "last_funding_type": last_funding_type,
    }
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
        entry["total_raised"],
        entry["growth_stage"],
        entry["last_funding_date"],
        entry["last_funding_type"],
        entry["extra_updates"],
    )
    extra_str = f", extra={entry['extra_updates']}" if entry["extra_updates"] else ""
    log.info(
        "[%s] Updated company: total_raised=$%s, growth_stage=%s, last_funding=%s (%s)%s",
        slug,
        f"{entry['total_raised']:,}",
        entry["growth_stage"],
        entry["last_funding_date"],
        entry["last_funding_type"],
        extra_str,
    )
    log.info("[%s] Done.", slug)


def main() -> None:
    """Entry point: fix funding data for batch 2 — 10 companies."""
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
