"""Fix funding data for batch 19 — companies ranked 251-280.

Verified 2026-03-26. Skipped: Nexla(≈correct), 微亿智造/潞晨科技(Chinese unclear),
Aible(≈correct), Arcee duplicate, Kindo(correct), Odyssey(correct), Openedges(≈correct).
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
    return {"round_type": round_type, "date": date, "amount": amount, "currency": "USD", "note": note}

COMPANIES_DATA = [
    {"slug": "rasa", "rounds": [_r("seed", "2018-01-01", 3_000_000), _r("series_a", "2020-06-01", 14_000_000), _r("series_b", "2021-06-01", 26_000_000), _r("series_c", "2024-02-01", 30_000_000)],
     "total_raised": 73_000_000, "growth_stage": "growth", "last_funding_date": "2024-02-01", "last_funding_type": "series_c", "extra_updates": {}},
    {"slug": "chalk", "rounds": [_r("seed", "2022-09-01", 10_000_000), _r("series_a", "2025-05-01", 50_000_000)],
     "total_raised": 60_000_000, "growth_stage": "growth", "last_funding_date": "2025-05-01", "last_funding_type": "series_a", "extra_updates": {}},
    {"slug": "orbem", "rounds": [_r("seed", "2021-01-01", 5_000_000), _r("series_a", "2023-06-01", 30_000_000), _r("series_b", "2026-01-01", 55_500_000)],
     "total_raised": 90_500_000, "growth_stage": "growth", "last_funding_date": "2026-01-01", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "clearml", "rounds": [_r("series_a", "2022-01-01", 11_000_000)],
     "total_raised": 11_000_000, "growth_stage": "early", "last_funding_date": "2022-01-01", "last_funding_type": "series_a", "extra_updates": {}},
    {"slug": "deepbrain", "rounds": [_r("series_a", "2021-01-01", 12_000_000), _r("series_b", "2023-01-01", 44_000_000)],
     "total_raised": 56_000_000, "growth_stage": "growth", "last_funding_date": "2023-01-01", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "physicsx", "rounds": [_r("seed", "2022-01-01", 20_000_000), _r("series_b", "2024-01-01", 135_000_000)],
     "total_raised": 155_000_000, "growth_stage": "late", "last_funding_date": "2024-01-01", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "datologyai", "rounds": [_r("seed", "2023-06-01", 11_600_000), _r("series_a", "2024-06-01", 46_000_000)],
     "total_raised": 57_600_000, "growth_stage": "early", "last_funding_date": "2024-06-01", "last_funding_type": "series_a", "extra_updates": {}},
    {"slug": "atomic-industries", "rounds": [_r("seed", "2023-12-04", 17_000_000), _r("series_a", "2025-09-01", 25_000_000)],
     "total_raised": 42_000_000, "growth_stage": "early", "last_funding_date": "2025-09-01", "last_funding_type": "series_a", "extra_updates": {}},
    {"slug": "elice", "rounds": [_r("series_a", "2020-01-01", 3_000_000), _r("series_b", "2022-01-01", 8_000_000), _r("series_c", "2024-01-01", 14_900_000)],
     "total_raised": 25_900_000, "growth_stage": "growth", "last_funding_date": "2024-01-01", "last_funding_type": "series_c", "extra_updates": {}},
    # 261. Noetica — acquired by Thomson Reuters
    {"slug": "noetica", "rounds": [_r("seed", "2023-01-01", 8_000_000), _r("series_a", "2024-10-01", 22_000_000)],
     "total_raised": 30_000_000, "growth_stage": "early", "last_funding_date": "2024-10-01", "last_funding_type": "series_a", "extra_updates": {"status": "acquired"}},
    {"slug": "nous-research", "rounds": [_r("seed", "2024-03-01", 20_000_000), _r("series_a", "2025-04-01", 50_000_000)],
     "total_raised": 70_000_000, "growth_stage": "growth", "last_funding_date": "2025-04-01", "last_funding_type": "series_a", "extra_updates": {}},
    # 264. JetCool — acquired by Flex
    {"slug": "jetcool", "rounds": [_r("seed", "2021-01-01", 10_000_000), _r("series_a", "2023-10-01", 17_000_000)],
     "total_raised": 27_000_000, "growth_stage": "early", "last_funding_date": "2023-10-01", "last_funding_type": "series_a", "extra_updates": {"status": "acquired"}},
    {"slug": "mechanical-orchard", "rounds": [_r("seed", "2022-01-01", 24_000_000), _r("series_b", "2024-01-01", 50_000_000)],
     "total_raised": 74_000_000, "growth_stage": "growth", "last_funding_date": "2024-01-01", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "hebbia", "rounds": [_r("seed", "2022-01-01", 10_000_000), _r("series_a", "2023-07-01", 30_000_000), _r("series_b", "2024-07-01", 130_000_000)],
     "total_raised": 170_000_000, "growth_stage": "late", "last_funding_date": "2024-07-01", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "arcee-ai", "rounds": [_r("seed", "2023-10-01", 5_500_000), _r("series_a", "2024-07-01", 24_000_000)],
     "total_raised": 29_500_000, "growth_stage": "early", "last_funding_date": "2024-07-01", "last_funding_type": "series_a", "extra_updates": {}},
    {"slug": "nearthlab", "rounds": [_r("series_a", "2020-01-01", 5_000_000), _r("series_b", "2021-06-01", 15_000_000), _r("series_c", "2023-02-01", 4_500_000)],
     "total_raised": 24_500_000, "growth_stage": "growth", "last_funding_date": "2023-02-01", "last_funding_type": "series_c", "extra_updates": {}},
    # 272. Valimail — acquired by DigiCert
    {"slug": "valimail", "rounds": [_r("seed", "2015-01-01", 6_000_000), _r("series_a", "2017-01-01", 12_000_000), _r("series_b", "2018-06-01", 25_000_000), _r("series_c", "2019-01-01", 45_000_000)],
     "total_raised": 88_000_000, "growth_stage": "growth", "last_funding_date": "2019-01-01", "last_funding_type": "series_c", "extra_updates": {"status": "acquired"}},
    # 273. Spoke — acquired by Okta
    {"slug": "spoke", "rounds": [_r("seed", "2016-01-01", 8_000_000), _r("series_b", "2017-10-01", 20_000_000)],
     "total_raised": 28_000_000, "growth_stage": "early", "last_funding_date": "2017-10-01", "last_funding_type": "series_b", "extra_updates": {"status": "acquired"}},
    {"slug": "resistant-ai", "rounds": [_r("seed", "2021-01-01", 5_000_000), _r("series_a", "2022-09-01", 27_600_000), _r("series_b", "2025-10-01", 25_000_000)],
     "total_raised": 57_600_000, "growth_stage": "growth", "last_funding_date": "2025-10-01", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "lovable", "rounds": [_r("seed", "2024-06-01", 2_600_000), _r("series_a", "2025-03-01", 17_000_000), _r("other", "2025-06-01", 30_000_000, "Series A ext"), _r("series_b", "2025-12-18", 330_000_000)],
     "total_raised": 379_600_000, "growth_stage": "late", "last_funding_date": "2025-12-18", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "browserbase", "rounds": [_r("seed", "2024-01-01", 6_000_000), _r("series_a", "2024-10-01", 21_000_000), _r("series_b", "2025-06-01", 40_000_000)],
     "total_raised": 67_000_000, "growth_stage": "growth", "last_funding_date": "2025-06-01", "last_funding_type": "series_b", "extra_updates": {}},
    # 279. Rewind/Limitless — acquired by Meta
    {"slug": "rewind", "rounds": [_r("seed", "2022-01-01", 10_000_000), _r("series_a", "2023-01-01", 23_000_000)],
     "total_raised": 33_000_000, "growth_stage": "early", "last_funding_date": "2023-01-01", "last_funding_type": "series_a", "extra_updates": {"status": "acquired"}},
]

def get_company_id(client, slug):
    res = client.table("su_companies").select("id").ilike("slug", slug).execute()
    return res.data[0]["id"] if res.data and len(res.data) == 1 else None

def process(client, entry):
    slug = entry["slug"]
    cid = get_company_id(client, slug)
    if not cid:
        log.warning("[%s] Not found", slug)
        return
    client.table("su_funding_rounds").delete().eq("company_id", cid).execute()
    for r in entry["rounds"]:
        p = {"company_id": cid, "round_type": r["round_type"], "announced_date": r["date"], "raised_amount": r["amount"], "currency": r["currency"]}
        if r.get("note"): p["metadata"] = {"note": r["note"]}
        client.table("su_funding_rounds").insert(p).execute()
    up = {"total_raised": entry["total_raised"], "growth_stage": entry["growth_stage"], "last_funding_date": entry["last_funding_date"], "last_funding_type": entry["last_funding_type"]}
    up.update(entry["extra_updates"])
    client.table("su_companies").update(up).eq("id", cid).execute()
    extra = f", extra={entry['extra_updates']}" if entry["extra_updates"] else ""
    log.info("[%s] Done: $%s, %s%s", slug, f"{entry['total_raised']:,}", entry["growth_stage"], extra)

def main():
    client = create_client(settings.supabase_url, settings.supabase_key)
    log.info("Processing %d companies...", len(COMPANIES_DATA))
    ok = fail = 0
    for e in COMPANIES_DATA:
        try: process(client, e); ok += 1
        except Exception as exc: log.error("[%s] FAILED: %s", e["slug"], exc); fail += 1
    log.info("=== %d succeeded, %d failed ===", ok, fail)

if __name__ == "__main__":
    main()
