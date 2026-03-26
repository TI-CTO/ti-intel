"""Fix funding data for batch 23 — companies ranked 401-450.

Verified 2026-03-26.
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
    {"slug": "nomic-ai", "rounds": [_r("seed", "2023-01-01", 4_000_000), _r("series_a", "2023-07-01", 13_000_000)],
     "total_raised": 17_000_000, "growth_stage": "early", "last_funding_date": "2023-07-01", "last_funding_type": "series_a", "extra_updates": {}},
    {"slug": "resemble-ai", "rounds": [_r("seed", "2020-01-01", 2_000_000), _r("series_a", "2023-01-01", 10_000_000), _r("series_b", "2025-12-01", 13_000_000)],
     "total_raised": 25_000_000, "growth_stage": "growth", "last_funding_date": "2025-12-01", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "higgsfield", "rounds": [_r("seed", "2024-01-01", 8_000_000), _r("series_a", "2025-06-01", 50_000_000), _r("other", "2026-01-01", 80_000_000, "Series A Extension")],
     "total_raised": 138_000_000, "growth_stage": "growth", "last_funding_date": "2026-01-01", "last_funding_type": "other", "extra_updates": {}},
    {"slug": "lovo", "rounds": [_r("seed", "2020-01-01", 2_600_000), _r("other", "2023-01-01", 10_800_000, "Pre-Series A")],
     "total_raised": 13_400_000, "growth_stage": "early", "last_funding_date": "2023-01-01", "last_funding_type": "other", "extra_updates": {}},
    # Celestial AI — acquired by Marvell (pending)
    {"slug": "celestial-ai", "rounds": [_r("seed", "2021-01-01", 5_700_000), _r("series_a", "2022-06-01", 56_000_000), _r("series_b", "2023-06-01", 100_000_000), _r("series_c", "2024-06-01", 175_000_000), _r("other", "2025-08-01", 250_000_000, "Series C1")],
     "total_raised": 586_700_000, "growth_stage": "late", "last_funding_date": "2025-08-01", "last_funding_type": "other", "extra_updates": {"status": "acquired"}},
    # OpenPipe — acquired by CoreWeave
    {"slug": "openpipe", "rounds": [_r("seed", "2024-03-26", 6_700_000)],
     "total_raised": 6_700_000, "growth_stage": "seed", "last_funding_date": "2024-03-26", "last_funding_type": "seed", "extra_updates": {"status": "acquired"}},
    {"slug": "mem", "rounds": [_r("seed", "2022-01-01", 5_600_000), _r("series_a", "2025-10-28", 24_000_000)],
     "total_raised": 29_600_000, "growth_stage": "early", "last_funding_date": "2025-10-28", "last_funding_type": "series_a", "extra_updates": {}},
    {"slug": "flip-ai", "rounds": [_r("seed", "2023-01-01", 6_500_000), _r("other", "2024-06-01", 5_000_000, "Bridge"), _r("series_a", "2026-01-13", 20_000_000)],
     "total_raised": 31_500_000, "growth_stage": "early", "last_funding_date": "2026-01-13", "last_funding_type": "series_a", "extra_updates": {}},
    {"slug": "vijil", "rounds": [_r("seed", "2024-01-01", 6_000_000), _r("series_a", "2025-11-01", 17_000_000)],
     "total_raised": 23_000_000, "growth_stage": "early", "last_funding_date": "2025-11-01", "last_funding_type": "series_a", "extra_updates": {}},
    # Nuclia — acquired by Progress
    {"slug": "nuclia", "rounds": [_r("seed", "2022-04-01", 5_400_000)],
     "total_raised": 5_400_000, "growth_stage": "seed", "last_funding_date": "2022-04-01", "last_funding_type": "seed", "extra_updates": {"status": "acquired"}},
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
