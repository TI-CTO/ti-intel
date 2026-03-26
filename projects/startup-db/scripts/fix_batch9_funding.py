"""Fix funding data for batch 9 — companies ranked 101-111 by total_raised.

Verified 2026-03-26. Skipped: Arize(correct), Xiao-i(already fixed).
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
    return {"round_type": round_type, "date": date, "amount": amount,
            "currency": "USD", "note": note}


COMPANIES_DATA = [
    # 101. ePapyrus — DB $131.5M → $21.2M (massive overestimate)
    {
        "slug": "epapyrus",
        "rounds": [
            _r("series_a", "2022-02-04", 21_200_000),
        ],
        "total_raised": 21_200_000,
        "growth_stage": "early",
        "last_funding_date": "2022-02-04",
        "last_funding_type": "series_a",
        "extra_updates": {},
    },
    # 102. Overjet — DB $131M → $159M
    {
        "slug": "overjet",
        "rounds": [
            _r("seed", "2020-06-01", 7_850_000),
            _r("series_a", "2021-08-26", 27_000_000),
            _r("series_b", "2021-12-20", 42_500_000),
            _r("series_c", "2024-03-05", 53_200_000),
        ],
        "total_raised": 130_550_000,
        "growth_stage": "growth",
        "last_funding_date": "2024-03-05",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    # 104. Suno — DB $125M → $375M
    {
        "slug": "suno",
        "rounds": [
            _r("series_a", "2023-03-01", 10_000_000, "Undisclosed amount, Matrix"),
            _r("series_b", "2024-05-21", 125_000_000),
            _r("series_c", "2025-11-19", 250_000_000),
        ],
        "total_raised": 385_000_000,
        "growth_stage": "late",
        "last_funding_date": "2025-11-19",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    # 105. Jasper — DB $125M → $131M
    {
        "slug": "jasper",
        "rounds": [
            _r("seed", "2021-06-01", 6_000_000),
            _r("series_a", "2022-10-17", 125_000_000),
        ],
        "total_raised": 131_000_000,
        "growth_stage": "growth",
        "last_funding_date": "2022-10-17",
        "last_funding_type": "series_a",
        "extra_updates": {},
    },
    # 106. Etched — DB $120M → $625M
    {
        "slug": "etched",
        "rounds": [
            _r("seed", "2023-03-01", 5_400_000),
            _r("series_a", "2024-06-25", 120_000_000),
            _r("series_b", "2026-01-13", 500_000_000),
        ],
        "total_raised": 625_400_000,
        "growth_stage": "late",
        "last_funding_date": "2026-01-13",
        "last_funding_type": "series_b",
        "extra_updates": {},
    },
    # 107. Poly AI — DB $120M → $205M
    {
        "slug": "poly-ai",
        "rounds": [
            _r("seed", "2017-01-01", 2_400_000),
            _r("series_a", "2019-03-08", 12_000_000),
            _r("series_b", "2022-09-07", 40_000_000),
            _r("series_c", "2024-05-16", 50_000_000),
            _r("series_d", "2025-12-15", 86_000_000),
        ],
        "total_raised": 190_400_000,
        "growth_stage": "late",
        "last_funding_date": "2025-12-15",
        "last_funding_type": "series_d",
        "extra_updates": {},
    },
    # 108. AInnovation — DB $120M → $267M+, HKEX IPO
    {
        "slug": "ainnovation",
        "rounds": [
            _r("other", "2018-05-01", 14_500_000, "Angel RMB 100M"),
            _r("series_a", "2019-01-24", 58_800_000, "Series A+A+"),
            _r("series_b", "2019-12-01", 57_200_000),
            _r("ipo", "2022-01-27", 151_000_000, "HKEX IPO"),
        ],
        "total_raised": 281_500_000,
        "growth_stage": "public",
        "last_funding_date": "2022-01-27",
        "last_funding_type": "ipo",
        "extra_updates": {"status": "ipo"},
    },
    # 110. Intercom — DB $116M → $241M (equity)
    {
        "slug": "intercom",
        "rounds": [
            _r("seed", "2012-01-01", 1_000_000),
            _r("seed", "2012-08-01", 750_000, "Seed 2"),
            _r("series_a", "2013-06-19", 6_000_000),
            _r("series_b", "2014-01-22", 23_000_000),
            _r("series_c", "2015-08-01", 35_000_000),
            _r("other", "2016-04-07", 50_000_000, "Series C expansion"),
            _r("series_d", "2018-03-27", 125_000_000),
        ],
        "total_raised": 240_750_000,
        "growth_stage": "late",
        "last_funding_date": "2018-03-27",
        "last_funding_type": "series_d",
        "extra_updates": {},
    },
    # 111. Pika — DB $115M → $135M
    {
        "slug": "pika-labs",
        "rounds": [
            _r("seed", "2023-11-28", 55_000_000, "Pre-Seed+Seed+Series A combined"),
            _r("series_b", "2024-06-04", 80_000_000),
        ],
        "total_raised": 135_000_000,
        "growth_stage": "growth",
        "last_funding_date": "2024-06-04",
        "last_funding_type": "series_b",
        "extra_updates": {},
    },
]


def get_company_id(client, slug: str) -> str | None:
    res = client.table("su_companies").select("id").ilike("slug", slug).execute()
    if res.data and len(res.data) == 1:
        return res.data[0]["id"]
    return None


def delete_funding_rounds(client, company_id: str) -> int:
    res = client.table("su_funding_rounds").delete().eq("company_id", company_id).execute()
    return len(res.data) if res.data else 0


def insert_funding_round(client, company_id: str, rd: dict) -> None:
    payload = {"company_id": company_id, "round_type": rd["round_type"],
               "announced_date": rd["date"], "raised_amount": rd["amount"],
               "currency": rd["currency"]}
    if rd.get("note"):
        payload["metadata"] = {"note": rd["note"]}
    client.table("su_funding_rounds").insert(payload).execute()


def update_company(client, cid: str, entry: dict) -> None:
    up: dict = {"total_raised": entry["total_raised"], "growth_stage": entry["growth_stage"],
                "last_funding_date": entry["last_funding_date"],
                "last_funding_type": entry["last_funding_type"]}
    up.update(entry["extra_updates"])
    client.table("su_companies").update(up).eq("id", cid).execute()


def process(client, entry: dict) -> None:
    slug = entry["slug"]
    log.info("[%s] Starting...", slug)
    cid = get_company_id(client, slug)
    if not cid:
        log.warning("[%s] Not found — skipping", slug)
        return
    deleted = delete_funding_rounds(client, cid)
    log.info("[%s] Deleted %d rounds", slug, deleted)
    for i, r in enumerate(entry["rounds"], 1):
        insert_funding_round(client, cid, r)
        log.info("[%s]   %d/%d: %s %s $%s", slug, i, len(entry["rounds"]),
                 r["round_type"], r["date"], f"{r['amount']:,}")
    update_company(client, cid, entry)
    extra = f", extra={entry['extra_updates']}" if entry["extra_updates"] else ""
    log.info("[%s] Done: $%s, %s%s", slug, f"{entry['total_raised']:,}",
             entry["growth_stage"], extra)


def main() -> None:
    client = create_client(settings.supabase_url, settings.supabase_key)
    log.info("Processing %d companies...", len(COMPANIES_DATA))
    ok = fail = 0
    for e in COMPANIES_DATA:
        try:
            process(client, e)
            ok += 1
        except Exception as exc:
            log.error("[%s] FAILED: %s", e["slug"], exc)
            fail += 1
    log.info("=== %d succeeded, %d failed ===", ok, fail)


if __name__ == "__main__":
    main()
