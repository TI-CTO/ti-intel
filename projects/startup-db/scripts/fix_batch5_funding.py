"""Fix funding data for batch 5 — companies ranked 61-70 by total_raised.

Verified 2026-03-26. Skipped: Windsurf(correct), Imbue(correct),
Covariant(correct), Sendbird(already fixed in batch2).
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
    # 62. Runway ML — DB $236.5M → $860M
    {
        "slug": "runway-ml",
        "rounds": [
            _r("seed", "2018-12-01", 2_000_000),
            _r("series_a", "2020-12-15", 8_500_000),
            _r("series_b", "2021-12-15", 35_000_000),
            _r("series_c", "2022-12-21", 50_000_000),
            _r("other", "2023-06-29", 141_000_000, "Series C Extension"),
            _r("series_d", "2025-04-03", 308_000_000),
            _r("series_e", "2026-02-10", 315_000_000),
        ],
        "total_raised": 859_500_000,
        "growth_stage": "late",
        "last_funding_date": "2026-02-10",
        "last_funding_type": "series_e",
        "extra_updates": {},
    },
    # 63. Hugging Face — DB $235M → $395M
    {
        "slug": "hugging-face",
        "rounds": [
            _r("other", "2017-03-09", 1_200_000, "Angel"),
            _r("seed", "2018-05-23", 4_000_000),
            _r("series_a", "2019-12-17", 15_000_000),
            _r("series_b", "2021-03-11", 40_000_000),
            _r("series_c", "2022-05-09", 100_000_000),
            _r("series_d", "2023-08-22", 235_000_000),
        ],
        "total_raised": 395_200_000,
        "growth_stage": "late",
        "last_funding_date": "2023-08-22",
        "last_funding_type": "series_d",
        "extra_updates": {},
    },
    # 65. Sakana AI — DB $230M → $379M
    {
        "slug": "sakana-ai",
        "rounds": [
            _r("seed", "2024-01-16", 30_000_000),
            _r("series_a", "2024-09-04", 214_000_000),
            _r("series_b", "2025-11-17", 135_000_000),
        ],
        "total_raised": 379_000_000,
        "growth_stage": "late",
        "last_funding_date": "2025-11-17",
        "last_funding_type": "series_b",
        "extra_updates": {},
    },
    # 66. Talkdesk — DB $230M → $498M
    {
        "slug": "talkdesk",
        "rounds": [
            _r("other", "2011-10-01", 450_000, "Angel"),
            _r("seed", "2014-09-01", 3_000_000),
            _r("series_a", "2015-06-09", 15_000_000),
            _r("other", "2015-10-01", 6_000_000, "Series A Extension"),
            _r("series_b", "2018-10-03", 100_000_000),
            _r("series_c", "2020-07-23", 143_000_000),
            _r("series_d", "2021-08-12", 230_000_000),
        ],
        "total_raised": 497_450_000,
        "growth_stage": "late",
        "last_funding_date": "2021-08-12",
        "last_funding_type": "series_d",
        "extra_updates": {},
    },
    # 68. Dialpad — DB $220M → $476M
    {
        "slug": "dialpad",
        "rounds": [
            _r("series_a", "2011-05-04", 3_000_000),
            _r("series_b", "2012-07-01", 15_000_000),
            _r("series_c", "2015-05-19", 35_000_000),
            _r("series_d", "2018-07-17", 50_000_000),
            _r("series_e", "2020-10-06", 100_000_000),
            _r("series_f", "2021-12-16", 170_000_000),
            _r("other", "2022-12-22", 50_000_000, "Series F Tranche 2"),
        ],
        "total_raised": 423_000_000,
        "growth_stage": "late",
        "last_funding_date": "2022-12-22",
        "last_funding_type": "other",
        "extra_updates": {},
    },
    # 69. Yellow AI — DB $220M → $102M (overestimated)
    {
        "slug": "yellow-ai",
        "rounds": [
            _r("seed", "2016-01-01", 500_000, "Seed estimate"),
            _r("series_a", "2019-06-01", 4_000_000),
            _r("series_b", "2020-04-01", 20_000_000),
            _r("series_c", "2021-08-04", 78_150_000),
        ],
        "total_raised": 102_650_000,
        "growth_stage": "growth",
        "last_funding_date": "2021-08-04",
        "last_funding_type": "series_c",
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
    """Fix funding data for batch 5 — 6 companies ranked 62-69."""
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
