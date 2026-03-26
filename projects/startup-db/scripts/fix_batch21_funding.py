"""Fix funding data for batch 21 — companies ranked 301-350.

Verified 2026-03-26. Skipped: Snips/Fireflies/Liminal(already fixed),
Edera/Akkio/BentoML/Chroma/Krisp(≈correct), Korean small cos, Spread/Mangoslab(no data).
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
    {"slug": "dust", "rounds": [_r("seed", "2023-06-01", 5_500_000), _r("series_a", "2024-06-27", 16_000_000)],
     "total_raised": 21_500_000, "growth_stage": "early", "last_funding_date": "2024-06-27", "last_funding_type": "series_a", "extra_updates": {}},
    # Predibase — acquired by Rubrik
    {"slug": "predibase", "rounds": [_r("seed", "2022-01-01", 16_200_000), _r("series_a", "2023-05-31", 12_200_000)],
     "total_raised": 28_400_000, "growth_stage": "early", "last_funding_date": "2023-05-31", "last_funding_type": "series_a", "extra_updates": {"status": "acquired"}},
    {"slug": "dropzone-ai", "rounds": [_r("seed", "2023-06-01", 5_000_000), _r("series_a", "2024-06-01", 17_000_000), _r("series_b", "2025-07-01", 37_000_000)],
     "total_raised": 59_000_000, "growth_stage": "growth", "last_funding_date": "2025-07-01", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "unifyapps", "rounds": [_r("seed", "2023-01-01", 10_000_000), _r("series_a", "2024-05-01", 20_000_000), _r("series_b", "2025-10-01", 50_000_000)],
     "total_raised": 80_000_000, "growth_stage": "growth", "last_funding_date": "2025-10-01", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "llamaindex", "rounds": [_r("seed", "2023-06-01", 8_500_000), _r("series_a", "2025-03-01", 19_000_000)],
     "total_raised": 27_500_000, "growth_stage": "early", "last_funding_date": "2025-03-01", "last_funding_type": "series_a", "extra_updates": {}},
    {"slug": "binarly", "rounds": [_r("seed", "2022-01-01", 3_600_000), _r("series_a", "2024-03-01", 10_500_000)],
     "total_raised": 14_100_000, "growth_stage": "early", "last_funding_date": "2024-03-01", "last_funding_type": "series_a", "extra_updates": {}},
    # PlayHT — acquired by Meta
    {"slug": "playht", "rounds": [_r("seed", "2023-01-01", 4_300_000), _r("other", "2024-11-01", 21_000_000, "Seed 2")],
     "total_raised": 25_300_000, "growth_stage": "early", "last_funding_date": "2024-11-01", "last_funding_type": "other", "extra_updates": {"status": "acquired"}},
    {"slug": "contextual-ai", "rounds": [_r("seed", "2023-09-01", 20_000_000), _r("series_a", "2024-08-01", 80_000_000)],
     "total_raised": 100_000_000, "growth_stage": "growth", "last_funding_date": "2024-08-01", "last_funding_type": "series_a", "extra_updates": {}},
    {"slug": "patronus-ai", "rounds": [_r("seed", "2023-06-01", 3_000_000), _r("series_a", "2024-09-01", 17_000_000), _r("series_b", "2025-12-01", 20_000_000)],
     "total_raised": 40_000_000, "growth_stage": "growth", "last_funding_date": "2025-12-01", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "baseten", "rounds": [_r("seed", "2020-01-01", 8_000_000), _r("series_a", "2022-04-01", 20_000_000), _r("series_b", "2023-06-01", 40_000_000), _r("series_c", "2024-04-01", 75_000_000), _r("series_d", "2024-09-01", 150_000_000), _r("series_e", "2026-01-01", 300_000_000)],
     "total_raised": 593_000_000, "growth_stage": "late", "last_funding_date": "2026-01-01", "last_funding_type": "series_e", "extra_updates": {}},
    {"slug": "deepdub", "rounds": [_r("seed", "2020-01-01", 6_000_000), _r("series_a", "2022-02-10", 20_000_000)],
     "total_raised": 26_000_000, "growth_stage": "early", "last_funding_date": "2022-02-10", "last_funding_type": "series_a", "extra_updates": {}},
    # XetHub — acquired by Hugging Face
    {"slug": "xethub", "rounds": [_r("seed", "2023-01-01", 7_930_000)],
     "total_raised": 7_930_000, "growth_stage": "seed", "last_funding_date": "2023-01-01", "last_funding_type": "seed", "extra_updates": {"status": "acquired"}},
    {"slug": "orbital-materials", "rounds": [_r("seed", "2023-01-01", 4_800_000), _r("series_a", "2024-07-01", 16_000_000), _r("series_b", "2025-09-01", 200_000_000)],
     "total_raised": 220_800_000, "growth_stage": "late", "last_funding_date": "2025-09-01", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "friendliai", "rounds": [_r("seed", "2022-09-01", 6_500_000), _r("other", "2024-03-01", 20_000_000, "Seed Extension")],
     "total_raised": 26_500_000, "growth_stage": "early", "last_funding_date": "2024-03-01", "last_funding_type": "other", "extra_updates": {}},
    {"slug": "crew-ai", "rounds": [_r("seed", "2024-04-01", 6_500_000), _r("series_a", "2024-10-22", 18_000_000)],
     "total_raised": 24_500_000, "growth_stage": "early", "last_funding_date": "2024-10-22", "last_funding_type": "series_a", "extra_updates": {}},
    {"slug": "tavus", "rounds": [_r("seed", "2022-01-01", 3_000_000), _r("series_a", "2024-06-01", 18_000_000), _r("series_b", "2025-11-01", 43_200_000)],
     "total_raised": 64_200_000, "growth_stage": "growth", "last_funding_date": "2025-11-01", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "delfina", "rounds": [_r("seed", "2021-01-01", 6_000_000), _r("series_a", "2025-01-01", 17_000_000)],
     "total_raised": 23_000_000, "growth_stage": "early", "last_funding_date": "2025-01-01", "last_funding_type": "series_a", "extra_updates": {}},
    {"slug": "code-metal", "rounds": [_r("seed", "2023-01-01", 5_000_000), _r("series_a", "2024-09-01", 36_500_000), _r("series_b", "2026-02-01", 125_000_000)],
     "total_raised": 166_500_000, "growth_stage": "late", "last_funding_date": "2026-02-01", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "exein", "rounds": [_r("seed", "2021-01-01", 5_000_000), _r("series_a", "2023-09-01", 15_000_000), _r("series_c", "2025-01-01", 100_000_000)],
     "total_raised": 120_000_000, "growth_stage": "late", "last_funding_date": "2025-01-01", "last_funding_type": "series_c", "extra_updates": {}},
    # Vayu Robotics — acquired by Serve Robotics
    {"slug": "vayu-robotics", "rounds": [_r("seed", "2023-10-01", 12_700_000)],
     "total_raised": 12_700_000, "growth_stage": "seed", "last_funding_date": "2023-10-01", "last_funding_type": "seed", "extra_updates": {"status": "acquired"}},
    {"slug": "reliant-ai", "rounds": [_r("seed", "2024-08-01", 11_300_000)],
     "total_raised": 11_300_000, "growth_stage": "seed", "last_funding_date": "2024-08-01", "last_funding_type": "seed", "extra_updates": {}},
    {"slug": "sf-compute", "rounds": [_r("seed", "2024-01-01", 12_000_000), _r("series_a", "2025-01-01", 40_000_000)],
     "total_raised": 52_000_000, "growth_stage": "early", "last_funding_date": "2025-01-01", "last_funding_type": "series_a", "extra_updates": {}},
    {"slug": "42maru", "rounds": [_r("series_a", "2019-01-01", 3_000_000), _r("series_b", "2021-01-01", 6_270_000)],
     "total_raised": 9_270_000, "growth_stage": "early", "last_funding_date": "2021-01-01", "last_funding_type": "series_b", "extra_updates": {}},
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
