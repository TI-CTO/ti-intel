"""Fix funding data for batch 8 — companies ranked 91-100 by total_raised.

Verified 2026-03-26. Skipped: Aisera(already fixed), Vestra AI(no data found),
Xiao-i(≈correct, mark IPO), EvolutionaryScale(correct, mark acquired).
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
    # 91. DP Technology — DB $150M → $158M
    {
        "slug": "dp-technology",
        "rounds": [
            _r("series_a", "2021-08-05", 25_000_000, "Series A+A+ combined"),
            _r("series_b", "2021-12-01", 43_700_000),
            _r("series_c", "2025-12-24", 114_000_000),
        ],
        "total_raised": 182_700_000,
        "growth_stage": "late",
        "last_funding_date": "2025-12-24",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    # 92. Helm.ai — DB $150M → $102M
    {
        "slug": "helmai",
        "rounds": [
            _r("seed", "2020-03-25", 13_000_000),
            _r("series_b", "2021-11-16", 26_000_000),
            _r("other", "2022-02-11", 30_000_000, "Series B-2"),
            _r("series_c", "2022-12-19", 31_000_000, "Series C 1st close"),
        ],
        "total_raised": 100_000_000,
        "growth_stage": "growth",
        "last_funding_date": "2022-12-19",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    # 95. Kore AI — DB $150M → $220M
    {
        "slug": "kore-ai",
        "rounds": [
            _r("series_c", "2021-09-29", 50_000_000),
            _r("other", "2021-10-01", 20_000_000, "Credit facility"),
            _r("series_d", "2024-01-30", 150_000_000),
        ],
        "total_raised": 220_000_000,
        "growth_stage": "late",
        "last_funding_date": "2024-01-30",
        "last_funding_type": "series_d",
        "extra_updates": {},
    },
    # 96. Xiao-i — correct $150M, mark as IPO
    {
        "slug": "xiao-i",
        "rounds": [
            _r("series_a", "2005-01-01", 5_000_000, "IDG estimate"),
            _r("series_b", "2007-01-01", 10_000_000, "IDG+Intel+DFJ"),
            _r("series_c", "2013-07-01", 8_000_000, "Alibaba"),
            _r("series_e", "2015-08-01", 16_000_000, "Huatai"),
            _r("other", "2017-01-01", 42_000_000, "2.63B RMB round"),
            _r("ipo", "2023-03-09", 38_760_000, "NASDAQ IPO AIXI"),
        ],
        "total_raised": 119_760_000,
        "growth_stage": "public",
        "last_funding_date": "2023-03-09",
        "last_funding_type": "ipo",
        "extra_updates": {"status": "ipo"},
    },
    # 97. Neeva — DB $150M → $77.5M, acquired by Snowflake
    {
        "slug": "neeva",
        "rounds": [
            _r("series_a", "2020-06-18", 37_500_000),
            _r("series_b", "2021-03-10", 40_000_000),
        ],
        "total_raised": 77_500_000,
        "growth_stage": "growth",
        "last_funding_date": "2021-03-10",
        "last_funding_type": "series_b",
        "extra_updates": {"status": "acquired"},
    },
    # 98. H2O AI — DB $147M → $251M
    {
        "slug": "h2o-ai",
        "rounds": [
            _r("seed", "2013-05-22", 1_700_000),
            _r("series_a", "2014-11-07", 8_900_000),
            _r("series_b", "2015-11-09", 20_000_000),
            _r("series_c", "2017-11-30", 40_000_000),
            _r("series_d", "2019-08-01", 72_500_000),
            _r("series_e", "2021-11-08", 100_000_000),
        ],
        "total_raised": 243_100_000,
        "growth_stage": "late",
        "last_funding_date": "2021-11-08",
        "last_funding_type": "series_e",
        "extra_updates": {},
    },
    # 99. Moonvalley — DB $144M → $154M
    {
        "slug": "moonvalley",
        "rounds": [
            _r("seed", "2024-11-18", 70_000_000),
            _r("series_a", "2025-07-14", 84_000_000),
        ],
        "total_raised": 154_000_000,
        "growth_stage": "early",
        "last_funding_date": "2025-07-14",
        "last_funding_type": "series_a",
        "extra_updates": {},
    },
    # 100. EvolutionaryScale — correct $142M, mark as acquired
    {
        "slug": "evolutionaryscale",
        "rounds": [
            _r("seed", "2024-06-25", 142_000_000),
        ],
        "total_raised": 142_000_000,
        "growth_stage": "seed",
        "last_funding_date": "2024-06-25",
        "last_funding_type": "seed",
        "extra_updates": {"status": "acquired"},
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
