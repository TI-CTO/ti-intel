"""Fix funding data for batch 12 — companies ranked 131-140 by total_raised.

Verified 2026-03-26. Skipped: Helm.ai, Skyflow, Balbix(already fixed),
wrtn(≈correct), Rossum(≈correct).
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
    # 131. Flexiv — DB $100M → $322M
    {
        "slug": "flexiv",
        "rounds": [
            _r("series_a", "2019-01-01", 22_000_000),
            _r("series_b", "2020-12-01", 100_000_000),
            _r("other", "2022-06-01", 100_000_000, "Series B+"),
            _r("series_c", "2025-06-01", 100_000_000),
        ],
        "total_raised": 322_000_000,
        "growth_stage": "late",
        "last_funding_date": "2025-06-01",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    # 132. Gupshup — DB $100M → $445M
    {
        "slug": "gupshup",
        "rounds": [
            _r("series_a", "2005-01-01", 1_130_000),
            _r("series_b", "2007-01-01", 10_000_000),
            _r("series_c", "2008-10-01", 12_300_000),
            _r("series_d", "2010-01-01", 12_000_000),
            _r("series_e", "2011-08-01", 10_000_000),
            _r("series_f", "2021-04-01", 100_000_000),
            _r("other", "2021-07-01", 240_000_000, "Series F-II"),
            _r("other", "2025-07-01", 60_000_000, "Series F-III"),
        ],
        "total_raised": 445_430_000,
        "growth_stage": "late",
        "last_funding_date": "2025-07-01",
        "last_funding_type": "other",
        "extra_updates": {},
    },
    # 134. Modular — DB $100M → $380M
    {
        "slug": "modular",
        "rounds": [
            _r("seed", "2022-06-01", 30_000_000),
            _r("series_b", "2023-08-01", 100_000_000),
            _r("series_c", "2025-09-01", 250_000_000),
        ],
        "total_raised": 380_000_000,
        "growth_stage": "late",
        "last_funding_date": "2025-09-01",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    # 136. Instabase — DB $100M → $322M
    {
        "slug": "instabase",
        "rounds": [
            _r("seed", "2015-08-31", 3_750_000),
            _r("series_a", "2017-05-24", 23_000_000),
            _r("series_b", "2019-10-21", 105_000_000),
            _r("series_c", "2023-06-06", 45_000_000),
            _r("series_d", "2025-01-17", 100_000_000),
        ],
        "total_raised": 276_750_000,
        "growth_stage": "late",
        "last_funding_date": "2025-01-17",
        "last_funding_type": "series_d",
        "extra_updates": {},
    },
    # 138. Xanadu — DB $100M → $244M
    {
        "slug": "xanadu",
        "rounds": [
            _r("seed", "2018-04-01", 9_000_000),
            _r("series_a", "2019-06-26", 32_000_000),
            _r("series_b", "2021-05-25", 100_000_000),
            _r("series_c", "2022-11-09", 100_000_000),
        ],
        "total_raised": 241_000_000,
        "growth_stage": "late",
        "last_funding_date": "2022-11-09",
        "last_funding_type": "series_c",
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
