"""Fix funding data for batch 20 — companies ranked 281-300.

Verified 2026-03-26. Skipped: Monumental/Lamini(correct), 한국 소규모(unclear),
Voyage AI/MakinaRocks/ePapyrus(already fixed).
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
    {"slug": "mindsdb", "rounds": [_r("seed", "2020-01-01", 5_500_000), _r("other", "2022-06-01", 25_000_000, "NVIDIA+others"), _r("series_a", "2023-06-01", 25_000_000)],
     "total_raised": 55_500_000, "growth_stage": "growth", "last_funding_date": "2023-06-01", "last_funding_type": "series_a", "extra_updates": {}},
    # Cleanlab — acquired by Handshake
    {"slug": "cleanlab", "rounds": [_r("seed", "2022-01-01", 5_000_000), _r("series_a", "2023-10-01", 25_000_000)],
     "total_raised": 30_000_000, "growth_stage": "early", "last_funding_date": "2023-10-01", "last_funding_type": "series_a", "extra_updates": {"status": "acquired"}},
    # Numbers Station — acquired by Alation
    {"slug": "numbers-station", "rounds": [_r("seed", "2022-01-01", 5_000_000), _r("series_a", "2023-03-20", 17_500_000)],
     "total_raised": 22_500_000, "growth_stage": "early", "last_funding_date": "2023-03-20", "last_funding_type": "series_a", "extra_updates": {"status": "acquired"}},
    {"slug": "ema", "rounds": [_r("seed", "2023-11-01", 11_000_000), _r("series_a", "2024-07-01", 50_000_000)],
     "total_raised": 61_000_000, "growth_stage": "growth", "last_funding_date": "2024-07-01", "last_funding_type": "series_a", "extra_updates": {}},
    {"slug": "corintis", "rounds": [_r("seed", "2023-01-01", 8_000_000), _r("series_a", "2024-05-01", 25_000_000), _r("series_b", "2025-12-01", 25_000_000)],
     "total_raised": 58_000_000, "growth_stage": "growth", "last_funding_date": "2025-12-01", "last_funding_type": "series_b", "extra_updates": {}},
    # Gretel.ai — acquired by NVIDIA
    {"slug": "gretelai", "rounds": [_r("seed", "2020-06-01", 3_500_000), _r("series_a", "2021-01-01", 12_000_000), _r("series_b", "2021-10-07", 50_000_000)],
     "total_raised": 65_500_000, "growth_stage": "growth", "last_funding_date": "2021-10-07", "last_funding_type": "series_b", "extra_updates": {"status": "acquired"}},
    {"slug": "marqvision", "rounds": [_r("seed", "2021-01-01", 6_000_000), _r("series_a", "2023-01-01", 20_000_000), _r("series_b", "2025-09-01", 48_000_000)],
     "total_raised": 74_000_000, "growth_stage": "growth", "last_funding_date": "2025-09-01", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "elicit", "rounds": [_r("seed", "2022-01-01", 9_000_000), _r("series_a", "2025-01-01", 22_000_000)],
     "total_raised": 31_000_000, "growth_stage": "early", "last_funding_date": "2025-01-01", "last_funding_type": "series_a", "extra_updates": {}},
    {"slug": "cradle", "rounds": [_r("seed", "2022-01-01", 5_500_000), _r("series_a", "2023-04-01", 24_000_000), _r("series_b", "2024-10-01", 73_000_000)],
     "total_raised": 102_500_000, "growth_stage": "growth", "last_funding_date": "2024-10-01", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "sixfold", "rounds": [_r("seed", "2022-01-01", 6_500_000), _r("series_a", "2023-08-01", 15_000_000), _r("series_b", "2026-01-01", 30_000_000)],
     "total_raised": 51_500_000, "growth_stage": "growth", "last_funding_date": "2026-01-01", "last_funding_type": "series_b", "extra_updates": {}},
    {"slug": "neosapiencetypecast", "rounds": [_r("seed", "2018-01-01", 3_000_000), _r("series_a", "2020-01-01", 8_000_000), _r("series_b", "2022-01-01", 10_000_000), _r("other", "2025-12-01", 11_500_000, "Bridge")],
     "total_raised": 32_500_000, "growth_stage": "growth", "last_funding_date": "2025-12-01", "last_funding_type": "other", "extra_updates": {}},
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
