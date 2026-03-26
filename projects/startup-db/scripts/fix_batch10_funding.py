"""Fix funding data for batch 10 — companies ranked 111-121 by total_raised.

Verified 2026-03-26. Skipped: Evinced(correct), Voltron Data(correct),
AssemblyAI(already fixed), Yellow AI(already fixed).
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
    # 112. Labelbox — DB $110M → $189M
    {
        "slug": "label-box",
        "rounds": [
            _r("series_a", "2020-02-04", 10_000_000),
            _r("series_b", "2020-02-04", 25_000_000),
            _r("series_c", "2021-02-12", 40_000_000),
            _r("series_d", "2022-01-06", 110_000_000),
        ],
        "total_raised": 185_000_000,
        "growth_stage": "late",
        "last_funding_date": "2022-01-06",
        "last_funding_type": "series_d",
        "extra_updates": {},
    },
    # 113. FuriosaAI — DB $110M → $246M
    {
        "slug": "furiosaai",
        "rounds": [
            _r("series_a", "2019-01-01", 7_000_000),
            _r("series_b", "2021-06-01", 72_200_000),
            _r("other", "2025-07-31", 125_000_000, "Series C Bridge"),
        ],
        "total_raised": 204_200_000,
        "growth_stage": "late",
        "last_funding_date": "2025-07-31",
        "last_funding_type": "other",
        "extra_updates": {},
    },
    # 114. Balbix — DB $110M → $99M
    {
        "slug": "balbix",
        "rounds": [
            _r("series_a", "2017-06-06", 8_600_000),
            _r("series_b", "2018-06-01", 20_000_000),
            _r("series_c", "2022-03-01", 70_000_000),
        ],
        "total_raised": 98_600_000,
        "growth_stage": "growth",
        "last_funding_date": "2022-03-01",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    # 117. Drift — correct $107M, mark as acquired
    {
        "slug": "drift",
        "rounds": [
            _r("series_a", "2015-01-15", 15_000_000),
            _r("series_b", "2017-09-26", 32_000_000),
            _r("series_c", "2018-04-17", 60_000_000),
        ],
        "total_raised": 107_000_000,
        "growth_stage": "growth",
        "last_funding_date": "2018-04-17",
        "last_funding_type": "series_c",
        "extra_updates": {"status": "acquired"},
    },
    # 118. Cursor AI — DB $105M → $3.5B
    {
        "slug": "cursor-ai",
        "rounds": [
            _r("pre_seed", "2022-04-01", 400_000),
            _r("seed", "2023-10-01", 8_000_000),
            _r("series_a", "2024-08-09", 60_000_000),
            _r("series_b", "2025-01-01", 105_000_000),
            _r("series_c", "2025-06-01", 900_000_000),
            _r("series_d", "2025-11-13", 2_300_000_000),
        ],
        "total_raised": 3_373_400_000,
        "growth_stage": "late",
        "last_funding_date": "2025-11-13",
        "last_funding_type": "series_d",
        "extra_updates": {},
    },
    # 120. Mathpresso — DB $102M → $130M
    {
        "slug": "mathpresso",
        "rounds": [
            _r("series_a", "2018-06-12", 5_300_000),
            _r("series_b", "2019-10-14", 14_500_000),
            _r("series_c", "2021-06-21", 50_000_000),
            _r("other", "2023-09-01", 8_000_000, "KT Strategic"),
        ],
        "total_raised": 77_800_000,
        "growth_stage": "growth",
        "last_funding_date": "2023-09-01",
        "last_funding_type": "other",
        "extra_updates": {},
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
