"""Fix funding data for batch 17 — companies ranked 201-230.

Verified 2026-03-26. Skipped: Intsig(unclear), LeapMind(correct),
DEFCON AI(correct), Sarvam AI(correct), Credo AI(correct), Voiceflow(correct).
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
    # 201. Prisma — DB $50M → $56.5M
    {"slug": "prisma", "rounds": [
        _r("seed", "2019-06-01", 4_500_000),
        _r("series_a", "2020-06-01", 12_000_000),
        _r("series_b", "2022-05-01", 40_000_000),
    ], "total_raised": 56_500_000, "growth_stage": "growth",
     "last_funding_date": "2022-05-01", "last_funding_type": "series_b", "extra_updates": {}},
    # 203. Stepfun — DB $50M → $719M
    {"slug": "stepfun", "rounds": [
        _r("series_a", "2023-09-01", 100_000_000, "Estimate"),
        _r("series_b", "2025-01-01", 719_000_000, "CNY 5B"),
    ], "total_raised": 819_000_000, "growth_stage": "late",
     "last_funding_date": "2025-01-01", "last_funding_type": "series_b", "extra_updates": {}},
    # 204. Edge Impulse — DB $49M → $54M
    {"slug": "edge-impulse", "rounds": [
        _r("seed", "2020-01-01", 2_000_000),
        _r("series_a", "2021-01-01", 18_000_000),
        _r("series_b", "2021-12-01", 34_000_000),
    ], "total_raised": 54_000_000, "growth_stage": "growth",
     "last_funding_date": "2021-12-01", "last_funding_type": "series_b", "extra_updates": {}},
    # 205. Nota AI — DB $48M → $43M, IPO KOSDAQ
    {"slug": "nota-ai", "rounds": [
        _r("series_a", "2020-01-01", 5_000_000),
        _r("series_b", "2022-01-01", 13_000_000),
        _r("series_c", "2024-06-01", 19_900_000),
        _r("ipo", "2025-11-01", 5_000_000, "KOSDAQ IPO"),
    ], "total_raised": 42_900_000, "growth_stage": "public",
     "last_funding_date": "2025-11-01", "last_funding_type": "ipo",
     "extra_updates": {"status": "ipo"}},
    # 206. Plivo — DB $47M → $2M (massive overestimate)
    {"slug": "plivo", "rounds": [
        _r("seed", "2021-11-01", 2_020_000),
    ], "total_raised": 2_020_000, "growth_stage": "seed",
     "last_funding_date": "2021-11-01", "last_funding_type": "seed", "extra_updates": {}},
    # 208. Encord — DB $45M → $110M
    {"slug": "encord", "rounds": [
        _r("seed", "2021-06-01", 3_000_000),
        _r("series_a", "2022-05-01", 12_500_000),
        _r("series_b", "2024-01-01", 30_000_000),
        _r("series_c", "2026-02-01", 60_000_000),
    ], "total_raised": 105_500_000, "growth_stage": "growth",
     "last_funding_date": "2026-02-01", "last_funding_type": "series_c", "extra_updates": {}},
    # 209. Nillion — DB $45M → $50M
    {"slug": "nillion", "rounds": [
        _r("seed", "2022-09-01", 20_000_000),
        _r("series_a", "2024-10-01", 25_000_000),
    ], "total_raised": 45_000_000, "growth_stage": "early",
     "last_funding_date": "2024-10-01", "last_funding_type": "series_a", "extra_updates": {}},
    # 210. IRONSCALES — DB $45M → $95M
    {"slug": "ironscales", "rounds": [
        _r("seed", "2015-01-01", 2_000_000),
        _r("series_a", "2018-01-01", 6_500_000),
        _r("series_b", "2020-04-01", 15_000_000),
        _r("series_c", "2021-12-01", 64_000_000),
    ], "total_raised": 87_500_000, "growth_stage": "growth",
     "last_funding_date": "2021-12-01", "last_funding_type": "series_c", "extra_updates": {}},
    # 211. Botpress — DB $45M → $40M
    {"slug": "botpress", "rounds": [
        _r("seed", "2020-01-01", 2_000_000),
        _r("series_a", "2023-01-01", 15_000_000),
        _r("series_b", "2025-06-01", 25_000_000),
    ], "total_raised": 42_000_000, "growth_stage": "growth",
     "last_funding_date": "2025-06-01", "last_funding_type": "series_b", "extra_updates": {}},
    # 212. Fiddler AI — DB $45M → $100M
    {"slug": "fiddler-ai", "rounds": [
        _r("seed", "2019-01-01", 10_000_000),
        _r("series_a", "2021-06-01", 25_000_000),
        _r("series_b", "2023-09-01", 35_000_000),
        _r("series_c", "2026-01-01", 30_000_000),
    ], "total_raised": 100_000_000, "growth_stage": "growth",
     "last_funding_date": "2026-01-01", "last_funding_type": "series_c", "extra_updates": {}},
    # 213. Braintrust — DB $44.3M → $121M
    {"slug": "braintrust", "rounds": [
        _r("seed", "2023-01-01", 5_000_000),
        _r("series_a", "2024-05-01", 36_000_000),
        _r("series_b", "2026-02-01", 80_000_000),
    ], "total_raised": 121_000_000, "growth_stage": "growth",
     "last_funding_date": "2026-02-01", "last_funding_type": "series_b", "extra_updates": {}},
    # 215. D-Matrix — DB $44M → $450M
    {"slug": "d-matrix", "rounds": [
        _r("seed", "2020-01-01", 10_000_000),
        _r("series_a", "2022-01-01", 44_000_000),
        _r("series_b", "2024-03-01", 110_000_000),
        _r("series_c", "2025-11-01", 275_000_000),
    ], "total_raised": 439_000_000, "growth_stage": "late",
     "last_funding_date": "2025-11-01", "last_funding_type": "series_c", "extra_updates": {}},
    # 216. Orca AI — DB $44M → $111M
    {"slug": "orca-ai", "rounds": [
        _r("seed", "2019-01-01", 2_500_000),
        _r("series_a", "2021-11-01", 13_000_000),
        _r("other", "2023-03-01", 23_000_000, "Series A extension"),
        _r("series_b", "2025-05-01", 72_500_000),
    ], "total_raised": 111_000_000, "growth_stage": "growth",
     "last_funding_date": "2025-05-01", "last_funding_type": "series_b", "extra_updates": {}},
    # 217. Fireworks AI — DB $43.2M → $327M
    {"slug": "fireworks", "rounds": [
        _r("seed", "2022-12-01", 7_000_000),
        _r("series_a", "2023-08-01", 25_000_000),
        _r("series_b", "2024-06-01", 52_000_000),
        _r("series_c", "2025-10-01", 250_000_000),
    ], "total_raised": 334_000_000, "growth_stage": "late",
     "last_funding_date": "2025-10-01", "last_funding_type": "series_c", "extra_updates": {}},
    # 218. Sahara — DB $43M → $50M
    {"slug": "sahara", "rounds": [
        _r("seed", "2023-08-01", 6_000_000),
        _r("series_a", "2024-08-01", 43_000_000),
    ], "total_raised": 49_000_000, "growth_stage": "early",
     "last_funding_date": "2024-08-01", "last_funding_type": "series_a", "extra_updates": {}},
    # 219. webAI — DB $43M → $60M
    {"slug": "webai", "rounds": [
        _r("series_a", "2024-09-01", 60_000_000),
    ], "total_raised": 60_000_000, "growth_stage": "early",
     "last_funding_date": "2024-09-01", "last_funding_type": "series_a", "extra_updates": {}},
    # 220. Adaptive Security — DB $43M → $147M
    {"slug": "adaptive-security", "rounds": [
        _r("seed", "2023-06-01", 5_000_000),
        _r("series_a", "2024-05-01", 20_000_000),
        _r("other", "2024-10-01", 40_000_000, "Series A extension"),
        _r("series_b", "2025-12-01", 81_000_000),
    ], "total_raised": 146_000_000, "growth_stage": "growth",
     "last_funding_date": "2025-12-01", "last_funding_type": "series_b", "extra_updates": {}},
    # 223. Unstructured — DB $40M → $65M
    {"slug": "unstructured", "rounds": [
        _r("seed", "2023-06-01", 5_000_000),
        _r("series_a", "2023-09-01", 20_000_000),
        _r("series_b", "2024-03-01", 40_000_000),
    ], "total_raised": 65_000_000, "growth_stage": "growth",
     "last_funding_date": "2024-03-01", "last_funding_type": "series_b", "extra_updates": {}},
    # 224. Replicate — DB $40M → $58M, acquired by Cloudflare
    {"slug": "replicate", "rounds": [
        _r("seed", "2021-10-01", 5_000_000),
        _r("series_a", "2022-10-01", 12_800_000),
        _r("series_b", "2023-12-01", 40_000_000),
    ], "total_raised": 57_800_000, "growth_stage": "growth",
     "last_funding_date": "2023-12-01", "last_funding_type": "series_b",
     "extra_updates": {"status": "acquired"}},
    # 225. Liminal — DB $40M → $17M
    {"slug": "liminal", "rounds": [
        _r("series_a", "2025-11-01", 17_000_000),
    ], "total_raised": 17_000_000, "growth_stage": "early",
     "last_funding_date": "2025-11-01", "last_funding_type": "series_a", "extra_updates": {}},
    # 226. Voyage AI — DB $40M → $28M, acquired by MongoDB
    {"slug": "voyage-ai", "rounds": [
        _r("series_a", "2024-10-01", 28_000_000),
    ], "total_raised": 28_000_000, "growth_stage": "early",
     "last_funding_date": "2024-10-01", "last_funding_type": "series_a",
     "extra_updates": {"status": "acquired"}},
    # 227. Maze — DB $40M → $60M
    {"slug": "maze", "rounds": [
        _r("seed", "2019-01-01", 5_000_000),
        _r("series_a", "2021-04-01", 15_000_000),
        _r("series_b", "2022-06-01", 40_000_000),
    ], "total_raised": 60_000_000, "growth_stage": "growth",
     "last_funding_date": "2022-06-01", "last_funding_type": "series_b", "extra_updates": {}},
    # 230. MakinaRocks — DB $39M → $25M
    {"slug": "makinarocks", "rounds": [
        _r("seed", "2018-01-01", 3_000_000),
        _r("series_a", "2020-01-01", 10_000_000),
        _r("series_b", "2022-01-01", 12_000_000),
    ], "total_raised": 25_000_000, "growth_stage": "growth",
     "last_funding_date": "2022-01-01", "last_funding_type": "series_b", "extra_updates": {}},
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
