"""Fix funding data for batch 22 — companies ranked 351-400.

Verified 2026-03-26. Skipped: Binarly/Vayu/Reliant/42Maru/ClearML(already fixed),
Extropic/Udio/Groundlight(≈correct), Mycroft(ceased ops), Beam AI(unclear),
Korean small cos, Cartwheel(small delta).
"""

import logging
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from startup_db.config import settings  # noqa: E402
from supabase import create_client  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)

def _r(rt, d, a, n=None):
    return {"round_type": rt, "date": d, "amount": a, "currency": "USD", "note": n}

COMPANIES_DATA = [
    # Argilla — acquired by Hugging Face
    {"slug": "argilla", "rounds": [_r("seed", "2022-01-01", 7_280_000)],
     "total_raised": 7_280_000, "growth_stage": "seed", "last_funding_date": "2022-01-01", "last_funding_type": "seed", "extra_updates": {"status": "acquired"}},
    {"slug": "gather-ai", "rounds": [_r("seed", "2021-01-01", 6_000_000), _r("series_a", "2024-01-01", 17_000_000), _r("other", "2025-06-01", 11_000_000, "Series A ext"), _r("series_b", "2026-02-09", 40_000_000)],
     "total_raised": 74_000_000, "growth_stage": "growth", "last_funding_date": "2026-02-09", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "deephow-corp", "rounds": [_r("seed", "2020-01-01", 5_000_000), _r("series_a", "2022-01-01", 14_000_000), _r("other", "2025-05-01", 5_000_000, "Series A-2")],
     "total_raised": 24_000_000, "growth_stage": "early", "last_funding_date": "2025-05-01", "last_funding_type": "other", "extra_updates": {}},
    # Mycroft — mark as defunct
    {"slug": "mycroft-ai", "rounds": [_r("seed", "2016-01-01", 2_500_000), _r("other", "2019-01-01", 5_300_000, "Crowdfunding")],
     "total_raised": 7_800_000, "growth_stage": "seed", "last_funding_date": "2019-01-01", "last_funding_type": "other", "extra_updates": {"status": "defunct"}},
    {"slug": "rebellions", "rounds": [_r("seed", "2021-01-01", 7_000_000), _r("series_a", "2022-06-01", 50_000_000), _r("series_b", "2024-05-01", 124_000_000), _r("other", "2025-03-01", 200_000_000, "Sapeon merger"), _r("series_c", "2025-11-01", 250_000_000)],
     "total_raised": 631_000_000, "growth_stage": "late", "last_funding_date": "2025-11-01", "last_funding_type": "series_c", "extra_updates": {}},
    {"slug": "archetype-ai", "rounds": [_r("seed", "2023-01-01", 13_000_000), _r("series_a", "2025-11-20", 35_000_000)],
     "total_raised": 48_000_000, "growth_stage": "early", "last_funding_date": "2025-11-20", "last_funding_type": "series_a", "extra_updates": {}},
    {"slug": "sambanova", "rounds": [_r("seed", "2017-01-01", 6_000_000), _r("series_a", "2018-03-01", 56_000_000), _r("series_b", "2019-01-01", 150_000_000), _r("series_c", "2020-04-01", 250_000_000), _r("series_d", "2021-04-01", 676_000_000), _r("series_e", "2026-02-01", 350_000_000)],
     "total_raised": 1_488_000_000, "growth_stage": "late", "last_funding_date": "2026-02-01", "last_funding_type": "series_e", "extra_updates": {}},
    {"slug": "langchain", "rounds": [_r("seed", "2023-04-01", 10_000_000), _r("series_a", "2024-02-01", 25_000_000), _r("other", "2024-10-01", 100_000_000, "Growth round"), _r("series_b", "2025-10-21", 125_000_000)],
     "total_raised": 260_000_000, "growth_stage": "late", "last_funding_date": "2025-10-21", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "greyparrot", "rounds": [_r("seed", "2020-01-01", 2_200_000), _r("series_a", "2022-11-01", 10_000_000), _r("series_b", "2024-01-01", 15_000_000)],
     "total_raised": 27_200_000, "growth_stage": "growth", "last_funding_date": "2024-01-01", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "riot", "rounds": [_r("seed", "2021-01-01", 3_000_000), _r("series_a", "2023-05-01", 12_000_000), _r("series_b", "2025-02-03", 30_000_000)],
     "total_raised": 45_000_000, "growth_stage": "growth", "last_funding_date": "2025-02-03", "last_funding_type": "series_b", "extra_updates": {}},
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
