"""Fix funding data for batch 15 — companies ranked 161-180.

Verified 2026-03-26. Skipped: Kinetica/Arize(already fixed), Galileo/Weaviate/
Bland AI/Bria(correct), Eve(unclear data).
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
    # 161. You.com — DB $76M → $199M
    {"slug": "youcom", "rounds": [
        _r("seed", "2021-01-01", 9_000_000),
        _r("series_a", "2022-07-01", 25_000_000),
        _r("series_b", "2024-03-01", 65_000_000),
        _r("series_c", "2025-09-01", 100_000_000),
    ], "total_raised": 199_000_000, "growth_stage": "late",
     "last_funding_date": "2025-09-01", "last_funding_type": "series_c", "extra_updates": {}},
    # 162. Superhuman — DB $75M → $118M, acquired by Grammarly
    {"slug": "superhuman", "rounds": [
        _r("seed", "2015-01-01", 8_000_000),
        _r("series_a", "2017-06-01", 14_000_000),
        _r("series_b", "2019-06-01", 21_000_000),
        _r("series_c", "2021-08-01", 75_000_000),
    ], "total_raised": 118_000_000, "growth_stage": "growth",
     "last_funding_date": "2021-08-01", "last_funding_type": "series_c",
     "extra_updates": {"status": "acquired"}},
    # 163. Roboflow — DB $75M → $63M
    {"slug": "roboflow", "rounds": [
        _r("seed", "2020-12-01", 2_100_000),
        _r("series_a", "2022-01-01", 20_650_000),
        _r("series_b", "2024-11-01", 40_000_000),
    ], "total_raised": 62_750_000, "growth_stage": "growth",
     "last_funding_date": "2024-11-01", "last_funding_type": "series_b", "extra_updates": {}},
    # 164. Snips — DB $75M → $21M, acquired by Sonos
    {"slug": "snips", "rounds": [
        _r("seed", "2016-01-01", 6_300_000),
        _r("series_a", "2017-06-01", 13_000_000),
    ], "total_raised": 21_200_000, "growth_stage": "early",
     "last_funding_date": "2017-06-01", "last_funding_type": "series_a",
     "extra_updates": {"status": "acquired"}},
    # 165. Bespoke Labs — DB $72.5M → $7.25M (10x error)
    {"slug": "bespoke-labs", "rounds": [
        _r("series_a", "2024-05-01", 7_250_000),
    ], "total_raised": 7_250_000, "growth_stage": "early",
     "last_funding_date": "2024-05-01", "last_funding_type": "series_a", "extra_updates": {}},
    # 166. Deepgram — DB $72M → $229M
    {"slug": "deepgram", "rounds": [
        _r("seed", "2016-01-01", 5_000_000),
        _r("series_a", "2020-09-01", 12_000_000),
        _r("series_b", "2022-02-01", 72_000_000),
        _r("series_c", "2026-01-01", 130_000_000),
    ], "total_raised": 219_000_000, "growth_stage": "late",
     "last_funding_date": "2026-01-01", "last_funding_type": "series_c", "extra_updates": {}},
    # 168. Charm Therapeutics — DB $70M → $150M
    {"slug": "charm-therapeutics", "rounds": [
        _r("series_a", "2023-01-01", 50_000_000),
        _r("series_b", "2025-01-01", 80_000_000),
    ], "total_raised": 130_000_000, "growth_stage": "growth",
     "last_funding_date": "2025-01-01", "last_funding_type": "series_b", "extra_updates": {}},
    # 170. Twelve Labs — DB $70M → $110M
    {"slug": "twelve-labs", "rounds": [
        _r("seed", "2022-01-01", 10_000_000),
        _r("series_a", "2023-09-01", 50_000_000),
        _r("series_b", "2025-01-01", 50_000_000),
    ], "total_raised": 110_000_000, "growth_stage": "growth",
     "last_funding_date": "2025-01-01", "last_funding_type": "series_b", "extra_updates": {}},
    # 173. Parloa — DB $66M → $560M
    {"slug": "parloa", "rounds": [
        _r("seed", "2018-01-01", 4_000_000),
        _r("series_a", "2022-06-01", 21_000_000),
        _r("series_b", "2023-11-01", 66_000_000),
        _r("series_c", "2024-11-01", 120_000_000),
        _r("series_d", "2026-01-15", 350_000_000),
    ], "total_raised": 561_000_000, "growth_stage": "late",
     "last_funding_date": "2026-01-15", "last_funding_type": "series_d", "extra_updates": {}},
    # 174. Hume AI — DB $66M → $75M
    {"slug": "hume-ai", "rounds": [
        _r("seed", "2022-03-01", 5_000_000),
        _r("series_a", "2023-03-01", 15_000_000),
        _r("series_b", "2024-03-01", 50_000_000),
    ], "total_raised": 70_000_000, "growth_stage": "growth",
     "last_funding_date": "2024-03-01", "last_funding_type": "series_b", "extra_updates": {}},
    # 178. Zilliz/Milvus — DB $60M → $113M
    {"slug": "milvus", "rounds": [
        _r("series_a", "2020-10-01", 10_000_000),
        _r("series_b", "2022-02-01", 43_000_000),
        _r("other", "2022-08-01", 60_000_000, "Series B Extension"),
    ], "total_raised": 113_000_000, "growth_stage": "growth",
     "last_funding_date": "2022-08-01", "last_funding_type": "other", "extra_updates": {}},
    # 179. WorkFusion — DB $60M → $251M (equity)
    {"slug": "workfusion", "rounds": [
        _r("series_a", "2014-01-01", 12_000_000),
        _r("series_b", "2015-06-01", 25_000_000),
        _r("series_c", "2017-04-01", 50_000_000),
        _r("series_d", "2019-09-01", 100_000_000),
        _r("other", "2025-09-01", 45_000_000, "Series C/Growth"),
    ], "total_raised": 232_000_000, "growth_stage": "late",
     "last_funding_date": "2025-09-01", "last_funding_type": "other", "extra_updates": {}},
    # 180. Phaidra — DB $60M → $120M
    {"slug": "phaidra", "rounds": [
        _r("seed", "2021-01-01", 12_000_000),
        _r("series_a", "2022-07-01", 25_000_000),
        _r("other", "2024-01-01", 12_000_000, "Extension"),
        _r("series_b", "2025-10-01", 50_000_000),
    ], "total_raised": 99_000_000, "growth_stage": "growth",
     "last_funding_date": "2025-10-01", "last_funding_type": "series_b", "extra_updates": {}},
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
