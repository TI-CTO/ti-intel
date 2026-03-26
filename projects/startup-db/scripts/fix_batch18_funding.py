"""Fix funding data for batch 18 — companies ranked 231-250.

Verified 2026-03-26. Skipped: Living Carbon(correct), VoyagerX(≈correct),
Boost AI(unclear), Gaudio Lab(conflicting data), Flawless AI(already fixed).
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
    # 231. AITRICS — DB $38.1M → $50M
    {"slug": "aitrics", "rounds": [
        _r("series_a", "2019-06-01", 8_000_000),
        _r("series_b", "2021-11-01", 18_000_000),
        _r("series_c", "2024-01-01", 24_000_000),
    ], "total_raised": 50_000_000, "growth_stage": "growth",
     "last_funding_date": "2024-01-01", "last_funding_type": "series_c", "extra_updates": {}},
    # 232. RideFlux — DB $37.3M → $57M
    {"slug": "rideflux", "rounds": [
        _r("series_a", "2021-01-01", 10_000_000),
        _r("series_b", "2023-01-01", 18_000_000),
        _r("other", "2025-01-01", 14_900_000, "Pre-IPO"),
    ], "total_raised": 42_900_000, "growth_stage": "late",
     "last_funding_date": "2025-01-01", "last_funding_type": "other", "extra_updates": {}},
    # 234. CentML — DB $36M → $30.5M, acquired by NVIDIA
    {"slug": "centml", "rounds": [
        _r("seed", "2023-10-25", 30_500_000),
    ], "total_raised": 30_500_000, "growth_stage": "early",
     "last_funding_date": "2023-10-25", "last_funding_type": "seed",
     "extra_updates": {"status": "acquired"}},
    # 235. Pryon — DB $36M → $136M
    {"slug": "pryon", "rounds": [
        _r("series_a", "2020-11-01", 20_000_000),
        _r("other", "2022-08-01", 16_000_000, "Series A extension"),
        _r("series_b", "2024-01-01", 100_000_000),
    ], "total_raised": 136_000_000, "growth_stage": "late",
     "last_funding_date": "2024-01-01", "last_funding_type": "series_b", "extra_updates": {}},
    # 236. Qdrant — DB $36M → $88M
    {"slug": "qdrant", "rounds": [
        _r("seed", "2023-04-01", 7_500_000),
        _r("series_a", "2024-01-01", 28_000_000),
        _r("series_b", "2026-03-12", 50_000_000),
    ], "total_raised": 85_500_000, "growth_stage": "growth",
     "last_funding_date": "2026-03-12", "last_funding_type": "series_b", "extra_updates": {}},
    # 238. Orby AI — DB $35M, acquired by Uniphore
    {"slug": "orby-ai", "rounds": [
        _r("seed", "2023-01-01", 4_500_000),
        _r("series_a", "2024-06-27", 30_000_000),
    ], "total_raised": 34_500_000, "growth_stage": "early",
     "last_funding_date": "2024-06-27", "last_funding_type": "series_a",
     "extra_updates": {"status": "acquired"}},
    # 239. Bioptimus — DB $35M → $76M
    {"slug": "bioptimus", "rounds": [
        _r("seed", "2024-02-01", 35_000_000),
        _r("series_a", "2025-01-14", 41_000_000),
    ], "total_raised": 76_000_000, "growth_stage": "early",
     "last_funding_date": "2025-01-14", "last_funding_type": "series_a", "extra_updates": {}},
    # 240. Protect AI — DB $35M → $129M, acquired by Palo Alto Networks
    {"slug": "protect-ai", "rounds": [
        _r("seed", "2022-06-01", 13_500_000),
        _r("series_a", "2023-07-01", 35_000_000),
        _r("series_b", "2024-07-01", 60_000_000),
    ], "total_raised": 108_500_000, "growth_stage": "growth",
     "last_funding_date": "2024-07-01", "last_funding_type": "series_b",
     "extra_updates": {"status": "acquired"}},
    # 241. Reality Defender — DB $34M → $52M
    {"slug": "reality-defender", "rounds": [
        _r("seed", "2021-06-01", 5_000_000),
        _r("series_a", "2024-08-01", 33_000_000),
        _r("other", "2025-04-01", 15_000_000, "Extension"),
    ], "total_raised": 53_000_000, "growth_stage": "growth",
     "last_funding_date": "2025-04-01", "last_funding_type": "other", "extra_updates": {}},
    # 243. Superb AI — DB $33.5M → $43M
    {"slug": "superb-ai", "rounds": [
        _r("seed", "2019-01-01", 2_000_000),
        _r("series_a", "2021-05-01", 9_300_000),
        _r("series_b", "2022-06-01", 16_000_000),
        _r("series_c", "2024-02-01", 10_200_000),
        _r("other", "2025-12-01", 10_000_000, "Pre-IPO"),
    ], "total_raised": 47_500_000, "growth_stage": "late",
     "last_funding_date": "2025-12-01", "last_funding_type": "other", "extra_updates": {}},
    # 245. OnePredict — DB $33.4M → $42.5M
    {"slug": "onepredit", "rounds": [
        _r("series_a", "2019-01-01", 5_000_000),
        _r("series_b", "2020-09-01", 12_500_000),
        _r("series_c", "2022-03-01", 25_000_000),
    ], "total_raised": 42_500_000, "growth_stage": "growth",
     "last_funding_date": "2022-03-01", "last_funding_type": "series_c", "extra_updates": {}},
    # 246. Cloaked — DB $33M → $400M
    {"slug": "cloaked", "rounds": [
        _r("seed", "2022-01-01", 5_000_000),
        _r("series_a", "2023-06-01", 25_000_000),
        _r("series_b", "2026-03-19", 375_000_000),
    ], "total_raised": 405_000_000, "growth_stage": "late",
     "last_funding_date": "2026-03-19", "last_funding_type": "series_b", "extra_updates": {}},
    # 247. V7 — DB $33M → $43.3M
    {"slug": "v7", "rounds": [
        _r("seed", "2020-03-01", 3_000_000),
        _r("other", "2021-06-01", 7_300_000, "Seed extension"),
        _r("series_a", "2022-11-01", 33_000_000),
    ], "total_raised": 43_300_000, "growth_stage": "growth",
     "last_funding_date": "2022-11-01", "last_funding_type": "series_a", "extra_updates": {}},
    # 248. Opaque — DB $32M → $55.5M
    {"slug": "opaque", "rounds": [
        _r("seed", "2021-09-01", 9_500_000),
        _r("series_a", "2023-03-01", 22_000_000),
        _r("series_b", "2026-02-01", 24_000_000),
    ], "total_raised": 55_500_000, "growth_stage": "growth",
     "last_funding_date": "2026-02-01", "last_funding_type": "series_b", "extra_updates": {}},
    # 249. Upstage — DB $31.8M → $163M
    {"slug": "upstage", "rounds": [
        _r("series_a", "2022-06-01", 27_300_000),
        _r("series_b", "2024-04-16", 72_000_000),
        _r("other", "2025-08-01", 45_000_000, "Series B Bridge"),
    ], "total_raised": 144_300_000, "growth_stage": "late",
     "last_funding_date": "2025-08-01", "last_funding_type": "other", "extra_updates": {}},
    # 250. Rembrand — DB $31M → $68.5M, merged with Spaceback
    {"slug": "rembrand", "rounds": [
        _r("seed", "2022-06-01", 8_000_000),
        _r("series_a", "2023-11-01", 23_000_000),
        _r("series_b", "2025-12-01", 37_500_000),
    ], "total_raised": 68_500_000, "growth_stage": "growth",
     "last_funding_date": "2025-12-01", "last_funding_type": "series_b", "extra_updates": {}},
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
