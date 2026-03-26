"""Fix funding data for batch 6 — companies ranked 71-80 by total_raised.

Verified 2026-03-26. Skipped: People AI(correct), Ada(correct).
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


COMPANIES_DATA = [
    # 71. Genesis Therapeutics — DB $200M → $304M
    {
        "slug": "genesis-therapeutics",
        "rounds": [
            _r("seed", "2019-11-21", 4_100_000),
            _r("series_a", "2020-12-02", 52_000_000),
            _r("other", "2023-08-01", 24_000_000, "SAFE conversion"),
            _r("series_b", "2023-08-21", 200_000_000),
        ],
        "total_raised": 280_100_000,
        "growth_stage": "late",
        "last_funding_date": "2023-08-21",
        "last_funding_type": "series_b",
        "extra_updates": {},
    },
    # 72. Waabi — DB $200M → $1.033B
    {
        "slug": "waabi",
        "rounds": [
            _r("series_a", "2021-06-08", 83_500_000),
            _r("series_b", "2024-06-18", 200_000_000),
            _r("series_c", "2026-01-28", 750_000_000),
        ],
        "total_raised": 1_033_500_000,
        "growth_stage": "late",
        "last_funding_date": "2026-01-28",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    # 73. Five9 — DB $200M → $164M, public since 2014
    {
        "slug": "five9",
        "rounds": [
            _r("series_a", "2004-04-28", 5_000_000),
            _r("other", "2008-03-01", 12_000_000, "Venture Round"),
            _r("series_c", "2011-01-19", 8_600_000),
            _r("other", "2012-04-01", 12_000_000, "Venture Round"),
            _r("series_d", "2013-05-29", 22_000_000),
            _r("ipo", "2014-04-03", 80_500_000, "NASDAQ IPO"),
        ],
        "total_raised": 140_100_000,
        "growth_stage": "public",
        "last_funding_date": "2014-04-03",
        "last_funding_type": "ipo",
        "extra_updates": {"status": "ipo"},
    },
    # 74. DataGrand — DB $200M → $162M
    {
        "slug": "datagrand",
        "rounds": [
            _r("seed", "2015-01-01", 1_500_000, "Zhenfund angel"),
            _r("series_a", "2017-01-01", 7_500_000),
            _r("series_b", "2018-11-01", 23_000_000),
            _r("other", "2020-05-01", 38_000_000, "Series B+"),
            _r("series_c", "2022-03-09", 92_000_000),
        ],
        "total_raised": 162_000_000,
        "growth_stage": "late",
        "last_funding_date": "2022-03-09",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    # 75. Fadu — DB $200M → $183M, KOSDAQ IPO 2023
    {
        "slug": "fadu",
        "rounds": [
            _r("series_b", "2022-04-01", 23_000_000),
            _r("other", "2023-02-28", 9_200_000, "Pre-IPO"),
            _r("ipo", "2023-08-07", 151_000_000, "KOSDAQ IPO"),
        ],
        "total_raised": 183_200_000,
        "growth_stage": "public",
        "last_funding_date": "2023-08-07",
        "last_funding_type": "ipo",
        "extra_updates": {"status": "ipo"},
    },
    # 76. Glean — DB $200M → $765M
    {
        "slug": "glean",
        "rounds": [
            _r("series_a", "2019-03-01", 15_000_000),
            _r("series_b", "2021-03-01", 40_000_000),
            _r("series_c", "2022-05-18", 100_000_000),
            _r("series_d", "2024-02-27", 200_000_000),
            _r("series_e", "2024-09-10", 260_000_000),
            _r("series_f", "2025-06-10", 150_000_000),
        ],
        "total_raised": 765_000_000,
        "growth_stage": "late",
        "last_funding_date": "2025-06-10",
        "last_funding_type": "series_f",
        "extra_updates": {},
    },
    # 78. Lila Sciences — DB $200M → $550M
    {
        "slug": "lila-sciences",
        "rounds": [
            _r("seed", "2025-03-10", 200_000_000),
            _r("series_a", "2025-09-15", 235_000_000),
            _r("other", "2025-10-14", 115_000_000, "Series A 2nd close"),
        ],
        "total_raised": 550_000_000,
        "growth_stage": "early",
        "last_funding_date": "2025-10-14",
        "last_funding_type": "other",
        "extra_updates": {},
    },
    # 80. Riiid — DB $191M → $248M
    {
        "slug": "riiid-뤼이드",
        "rounds": [
            _r("series_a", "2016-01-01", 1_700_000),
            _r("series_b", "2018-04-01", 10_770_000),
            _r("series_c", "2019-07-15", 18_000_000),
            _r("other", "2020-07-24", 41_800_000, "Pre-Series D"),
            _r("series_d", "2021-05-24", 175_000_000),
        ],
        "total_raised": 247_270_000,
        "growth_stage": "late",
        "last_funding_date": "2021-05-24",
        "last_funding_type": "series_d",
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
    client, company_id: str, total_raised: int, growth_stage: str,
    last_funding_date: str, last_funding_type: str, extra: dict,
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
    for i, r in enumerate(entry["rounds"], 1):
        insert_funding_round(client, company_id, r)
        log.info("[%s]   Round %d/%d: %s %s $%s", slug, i, len(entry["rounds"]),
                 r["round_type"], r["date"], f"{r['amount']:,}")
    update_company(client, company_id, entry["total_raised"], entry["growth_stage"],
                   entry["last_funding_date"], entry["last_funding_type"],
                   entry["extra_updates"])
    extra_str = f", extra={entry['extra_updates']}" if entry["extra_updates"] else ""
    log.info("[%s] Updated: total=$%s, stage=%s%s", slug,
             f"{entry['total_raised']:,}", entry["growth_stage"], extra_str)


def main() -> None:
    """Fix funding data for batch 6 — 8 companies ranked 71-80."""
    client = create_client(settings.supabase_url, settings.supabase_key)
    log.info("Processing %d companies...", len(COMPANIES_DATA))
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
