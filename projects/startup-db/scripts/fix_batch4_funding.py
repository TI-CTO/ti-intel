"""Fix funding data for batch 4 — companies ranked 51-60 by total_raised.

Verified 2026-03-26 via web research. Anyscale (#57) excluded — DB value correct.
"""

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
# Data definitions — verified 2026-03-26
# ---------------------------------------------------------------------------

COMPANIES_DATA = [
    # 51. Sierra — DB $285M → $635M
    {
        "slug": "sierra",
        "rounds": [
            _r("seed", "2024-02-13", 110_000_000),
            _r("series_a", "2024-10-28", 175_000_000),
            _r("series_c", "2025-09-04", 350_000_000),
        ],
        "total_raised": 635_000_000,
        "growth_stage": "late",
        "last_funding_date": "2025-09-04",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    # 52. Replit — DB $272M → $877M
    {
        "slug": "replit",
        "rounds": [
            _r("pre_seed", "2018-01-01", 120_000, "Y Combinator"),
            _r("seed", "2018-10-22", 4_500_000),
            _r("series_a", "2021-02-18", 20_000_000),
            _r("series_b", "2021-12-10", 80_000_000),
            _r("other", "2022-05-01", 5_240_000, "Seed Extension"),
            _r("other", "2023-04-25", 97_400_000, "Series B Extension"),
            _r("other", "2023-11-06", 20_000_000, "Liquidity Event"),
            _r("series_e", "2025-09-10", 250_000_000),
            _r("series_d", "2026-03-11", 400_000_000),
        ],
        "total_raised": 877_260_000,
        "growth_stage": "late",
        "last_funding_date": "2026-03-11",
        "last_funding_type": "series_d",
        "extra_updates": {},
    },
    # 53. Deepexi — DB $271M → $362M, now public (HK IPO)
    {
        "slug": "deepexi",
        "rounds": [
            _r("seed", "2018-07-01", 2_200_000, "Angel/Seed estimate"),
            _r("other", "2019-03-29", 12_400_000, "Pre-A"),
            _r("series_a", "2019-09-24", 35_000_000),
            _r("other", "2020-05-28", 50_000_000, "Series A+"),
            _r("other", "2020-11-01", 15_000_000, "Series A3 estimate"),
            _r("other", "2020-12-11", 40_000_000, "Series A4"),
            _r("series_b", "2021-08-20", 100_000_000),
            _r("other", "2022-07-04", 15_900_000, "Series B+"),
            _r("ipo", "2025-10-28", 91_400_000, "Hong Kong IPO HK$710M"),
        ],
        "total_raised": 361_900_000,
        "growth_stage": "public",
        "last_funding_date": "2025-10-28",
        "last_funding_type": "ipo",
        "extra_updates": {"status": "ipo"},
    },
    # 54. Sisense — DB $270M → $276M, acquired by Perforce 2024-05
    {
        "slug": "sisense",
        "rounds": [
            _r("other", "2005-01-01", 1_500_000, "Angel"),
            _r("series_a", "2010-07-13", 4_000_000),
            _r("series_b", "2013-04-03", 10_000_000),
            _r("series_c", "2014-06-12", 30_000_000),
            _r("series_d", "2016-01-07", 50_000_000),
            _r("series_e", "2018-09-12", 80_000_000),
            _r("series_f", "2020-01-09", 100_000_000),
        ],
        "total_raised": 275_500_000,
        "growth_stage": "growth",
        "last_funding_date": "2020-01-09",
        "last_funding_type": "series_f",
        "extra_updates": {"status": "acquired"},
    },
    # 55. Cresta — DB $270M → $282M
    {
        "slug": "cresta",
        "rounds": [
            _r("seed", "2018-12-21", 500_000),
            _r("seed", "2020-02-02", 6_000_000, "Seed 2"),
            _r("series_a", "2020-02-03", 15_000_000),
            _r("series_b", "2021-03-31", 50_000_000),
            _r("series_c", "2022-03-17", 80_000_000),
            _r("series_d", "2024-11-19", 125_000_000),
        ],
        "total_raised": 282_000_000,
        "growth_stage": "late",
        "last_funding_date": "2024-11-19",
        "last_funding_type": "series_d",
        "extra_updates": {},
    },
    # 56. Hippocratic AI — DB $264M → $385M
    {
        "slug": "hippocratic-ai",
        "rounds": [
            _r("seed", "2023-05-16", 50_000_000),
            _r("other", "2023-07-25", 15_000_000, "Seed Extension"),
            _r("series_a", "2024-03-18", 53_000_000),
            _r("series_b", "2025-01-09", 141_000_000),
            _r("series_c", "2025-11-03", 126_000_000),
        ],
        "total_raised": 385_000_000,
        "growth_stage": "late",
        "last_funding_date": "2025-11-03",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    # 58. MiniMax — DB $250M → $1.83B (incl IPO), now public
    {
        "slug": "minimax",
        "rounds": [
            _r("other", "2021-12-01", 31_000_000, "Angel"),
            _r("other", "2022-03-01", 20_000_000, "Pre-Series A"),
            _r("seed", "2022-07-01", 10_000_000, "Seed estimate"),
            _r("series_a", "2023-06-01", 250_000_000),
            _r("series_b", "2024-03-05", 600_000_000),
            _r("other", "2025-07-13", 300_000_000, "Series B Extension"),
            _r("ipo", "2026-01-09", 619_000_000, "Hong Kong IPO"),
        ],
        "total_raised": 1_830_000_000,
        "growth_stage": "public",
        "last_funding_date": "2026-01-09",
        "last_funding_type": "ipo",
        "extra_updates": {"status": "ipo"},
    },
    # 59. Gong — DB $250M → $584M
    {
        "slug": "gong",
        "rounds": [
            _r("series_a", "2016-06-21", 6_000_000),
            _r("other", "2017-07-12", 20_000_000, "Series A1"),
            _r("series_b", "2019-02-07", 40_000_000),
            _r("series_c", "2019-12-03", 65_000_000),
            _r("series_d", "2020-08-12", 200_000_000),
            _r("series_e", "2021-05-28", 250_000_000),
        ],
        "total_raised": 584_000_000,
        "growth_stage": "late",
        "last_funding_date": "2021-05-28",
        "last_funding_type": "series_e",
        "extra_updates": {},
    },
    # 60. Perplexity — DB $250M → $1.55B
    {
        "slug": "perplexity",
        "rounds": [
            _r("seed", "2022-09-01", 3_100_000),
            _r("series_a", "2023-03-28", 25_600_000),
            _r("series_b", "2024-01-04", 73_600_000),
            _r("series_c", "2024-06-27", 250_000_000),
            _r("series_d", "2024-12-18", 500_000_000),
            _r("other", "2025-06-01", 500_000_000, "Series D Extension - Accel"),
            _r("other", "2025-09-10", 200_000_000, "Series D Extension 2"),
        ],
        "total_raised": 1_552_300_000,
        "growth_stage": "late",
        "last_funding_date": "2025-09-10",
        "last_funding_type": "other",
        "extra_updates": {},
    },
]


def get_company_id(client, slug: str) -> str | None:
    """Fetch the company UUID for a given slug."""
    res = (
        client.table("su_companies").select("id").eq("slug", slug).single().execute()
    )
    if res.data:
        return res.data["id"]
    return None


def delete_funding_rounds(client, company_id: str) -> int:
    """Delete all funding rounds for a company."""
    res = (
        client.table("su_funding_rounds")
        .delete()
        .eq("company_id", company_id)
        .execute()
    )
    return len(res.data) if res.data else 0


def insert_funding_round(client, company_id: str, round_data: dict) -> None:
    """Insert a single funding round record."""
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
    """Update su_companies summary fields after funding round changes."""
    update_payload: dict = {
        "total_raised": total_raised,
        "growth_stage": growth_stage,
        "last_funding_date": last_funding_date,
        "last_funding_type": last_funding_type,
    }
    update_payload.update(extra)
    (
        client.table("su_companies")
        .update(update_payload)
        .eq("id", company_id)
        .execute()
    )


def process_company(client, entry: dict) -> None:
    """Process a single company: delete rounds, insert corrected, update summary."""
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
        "[%s] Updated: total=$%s, stage=%s, last=%s (%s)%s",
        slug,
        f"{entry['total_raised']:,}",
        entry["growth_stage"],
        entry["last_funding_date"],
        entry["last_funding_type"],
        extra_str,
    )


def main() -> None:
    """Fix funding data for batch 4 — 9 companies ranked 51-60."""
    client = create_client(settings.supabase_url, settings.supabase_key)
    log.info(
        "Connected to Supabase. Processing %d companies...", len(COMPANIES_DATA)
    )

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
