"""Fix funding data for batch 16 — companies ranked 181-200.

Verified 2026-03-26. Skipped: LandingAI(correct), Atropos(correct), ModelBest(unclear).
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
    # 181. Pilot — DB $58M → $222M
    {"slug": "pilot", "rounds": [
        _r("seed", "2017-04-01", 9_000_000),
        _r("series_a", "2018-05-01", 15_000_000),
        _r("series_b", "2019-09-01", 40_000_000),
        _r("series_c", "2021-03-01", 100_000_000),
    ], "total_raised": 164_000_000, "growth_stage": "late",
     "last_funding_date": "2021-03-01", "last_funding_type": "series_c", "extra_updates": {}},
    # 182. Reka AI — DB $58M → $168M
    {"slug": "reka-ai", "rounds": [
        _r("seed", "2023-06-01", 10_000_000),
        _r("series_a", "2024-04-01", 58_000_000),
        _r("series_b", "2025-07-01", 110_000_000),
    ], "total_raised": 178_000_000, "growth_stage": "late",
     "last_funding_date": "2025-07-01", "last_funding_type": "series_b", "extra_updates": {}},
    # 184. Xscape Photonics — DB $57M → $95M
    {"slug": "xscape-photonics", "rounds": [
        _r("series_a", "2024-06-01", 44_000_000),
        _r("other", "2026-03-11", 37_000_000, "Series A additional"),
    ], "total_raised": 81_000_000, "growth_stage": "early",
     "last_funding_date": "2026-03-11", "last_funding_type": "other", "extra_updates": {}},
    # 185. Luma AI — DB $56M → $1.07B
    {"slug": "luma-ai", "rounds": [
        _r("seed", "2022-01-01", 6_000_000),
        _r("series_a", "2023-05-01", 25_000_000),
        _r("series_b", "2024-03-01", 43_000_000),
        _r("series_c", "2025-11-01", 900_000_000),
    ], "total_raised": 974_000_000, "growth_stage": "late",
     "last_funding_date": "2025-11-01", "last_funding_type": "series_c", "extra_updates": {}},
    # 186. Lilt — DB $55M → $92.5M
    {"slug": "lilt", "rounds": [
        _r("seed", "2015-01-01", 2_500_000),
        _r("series_a", "2019-10-01", 10_000_000),
        _r("series_b", "2021-03-01", 25_000_000),
        _r("series_c", "2022-04-07", 55_000_000),
    ], "total_raised": 92_500_000, "growth_stage": "growth",
     "last_funding_date": "2022-04-07", "last_funding_type": "series_c", "extra_updates": {}},
    # 187. Bear Robotics — DB $54M → $175M, acquired by LG
    {"slug": "bear-robotics", "rounds": [
        _r("seed", "2018-01-01", 6_000_000),
        _r("series_a", "2020-01-01", 32_000_000),
        _r("series_b", "2022-03-15", 81_000_000),
        _r("series_c", "2024-03-01", 60_000_000),
    ], "total_raised": 179_000_000, "growth_stage": "late",
     "last_funding_date": "2024-03-01", "last_funding_type": "series_c",
     "extra_updates": {"status": "acquired"}},
    # 188. Vectara — DB $53.5M → $73.5M
    {"slug": "vectara", "rounds": [
        _r("seed", "2022-10-01", 28_500_000),
        _r("other", "2023-08-01", 20_000_000, "Seed extension"),
        _r("series_a", "2024-07-01", 25_000_000),
    ], "total_raised": 73_500_000, "growth_stage": "growth",
     "last_funding_date": "2024-07-01", "last_funding_type": "series_a", "extra_updates": {}},
    # 189. Espressive — correct $53M, mark acquired
    {"slug": "espressive", "rounds": [
        _r("series_a", "2018-10-01", 13_000_000),
        _r("other", "2019-04-01", 10_000_000, "Series A extension"),
        _r("series_b", "2020-03-01", 30_000_000),
    ], "total_raised": 53_000_000, "growth_stage": "growth",
     "last_funding_date": "2020-03-01", "last_funding_type": "series_b",
     "extra_updates": {"status": "acquired"}},
    # 190. Decart — DB $52.6M → $153M
    {"slug": "decart", "rounds": [
        _r("seed", "2024-03-01", 3_000_000),
        _r("series_a", "2024-12-01", 50_000_000),
        _r("series_b", "2025-08-01", 100_000_000),
    ], "total_raised": 153_000_000, "growth_stage": "late",
     "last_funding_date": "2025-08-01", "last_funding_type": "series_b", "extra_updates": {}},
    # 191. Magic — DB $52M → $515M
    {"slug": "magic", "rounds": [
        _r("seed", "2022-01-01", 5_000_000),
        _r("series_a", "2023-02-01", 23_000_000),
        _r("other", "2024-03-01", 117_000_000, "Series B/Growth"),
        _r("series_c", "2024-08-29", 320_000_000),
    ], "total_raised": 465_000_000, "growth_stage": "late",
     "last_funding_date": "2024-08-29", "last_funding_type": "series_c", "extra_updates": {}},
    # 192. SuperAnnotate — DB $51M → $75M
    {"slug": "superannotate", "rounds": [
        _r("seed", "2020-01-01", 2_000_000),
        _r("series_a", "2021-11-01", 14_000_000),
        _r("series_b", "2023-07-01", 36_000_000),
        _r("other", "2025-07-01", 13_500_000, "Dell Technologies Capital"),
    ], "total_raised": 65_500_000, "growth_stage": "growth",
     "last_funding_date": "2025-07-01", "last_funding_type": "other", "extra_updates": {}},
    # 195. KEENON — DB $50M → $233M
    {"slug": "keenon-robotics", "rounds": [
        _r("series_a", "2018-01-01", 10_000_000),
        _r("series_b", "2019-06-01", 15_000_000),
        _r("series_c", "2020-06-01", 8_000_000),
        _r("series_d", "2021-09-01", 200_000_000),
    ], "total_raised": 233_000_000, "growth_stage": "late",
     "last_funding_date": "2021-09-01", "last_funding_type": "series_d", "extra_updates": {}},
    # 196. Tines — DB $50M → $272M
    {"slug": "tines", "rounds": [
        _r("seed", "2019-01-01", 4_300_000),
        _r("series_a", "2020-11-01", 11_000_000),
        _r("series_b", "2022-05-01", 55_000_000),
        _r("other", "2024-04-24", 50_000_000, "Series B extension"),
        _r("series_c", "2024-11-01", 125_000_000),
    ], "total_raised": 245_300_000, "growth_stage": "late",
     "last_funding_date": "2024-11-01", "last_funding_type": "series_c", "extra_updates": {}},
    # 197. Inworld AI — DB $50M → $126M
    {"slug": "inworld-ai", "rounds": [
        _r("seed", "2022-02-01", 7_000_000),
        _r("series_a", "2022-08-01", 50_000_000),
        _r("series_b", "2023-08-01", 56_000_000),
    ], "total_raised": 113_000_000, "growth_stage": "growth",
     "last_funding_date": "2023-08-01", "last_funding_type": "series_b", "extra_updates": {}},
    # 198. Hammerspace — DB $50M → $157M
    {"slug": "hammerspace", "rounds": [
        _r("series_a", "2023-07-01", 56_700_000),
        _r("series_b", "2025-04-16", 100_000_000),
    ], "total_raised": 156_700_000, "growth_stage": "growth",
     "last_funding_date": "2025-04-16", "last_funding_type": "series_b", "extra_updates": {}},
    # 199. Fireflies — DB $50M → $24M
    {"slug": "firefliesai", "rounds": [
        _r("seed", "2019-01-01", 5_000_000),
        _r("series_a", "2021-09-01", 14_000_000),
    ], "total_raised": 19_000_000, "growth_stage": "growth",
     "last_funding_date": "2021-09-01", "last_funding_type": "series_a", "extra_updates": {}},
    # 200. EvolutionIQ — DB $50M → $64M, acquired by CCC
    {"slug": "evolutioniq", "rounds": [
        _r("seed", "2019-01-01", 3_500_000),
        _r("series_a", "2021-06-01", 20_000_000),
        _r("series_b", "2023-02-01", 33_100_000),
    ], "total_raised": 56_600_000, "growth_stage": "growth",
     "last_funding_date": "2023-02-01", "last_funding_type": "series_b",
     "extra_updates": {"status": "acquired"}},
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
