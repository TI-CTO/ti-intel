"""Fix funding data for batch 11 — companies ranked 121-131 by total_raised.

Verified 2026-03-26. Skipped: Helm.ai(already fixed), Chorus AI(correct+acquired),
Skyflow(correct).
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
    # 121. 1X — DB $100M → $126M
    {
        "slug": "1x",
        "rounds": [
            _r("other", "2023-03-01", 23_500_000, "Series A2"),
            _r("series_b", "2024-01-01", 100_000_000),
        ],
        "total_raised": 123_500_000,
        "growth_stage": "growth",
        "last_funding_date": "2024-01-01",
        "last_funding_type": "series_b",
        "extra_updates": {},
    },
    # 122. SSI — DB $100M → $3B
    {
        "slug": "safe-superintelligence",
        "rounds": [
            _r("seed", "2024-09-04", 1_000_000_000),
            _r("series_a", "2025-03-01", 2_000_000_000),
        ],
        "total_raised": 3_000_000_000,
        "growth_stage": "early",
        "last_funding_date": "2025-03-01",
        "last_funding_type": "series_a",
        "extra_updates": {},
    },
    # 123. Cognigy — DB $100M → $165M, acquired by NICE
    {
        "slug": "cognigy",
        "rounds": [
            _r("series_a", "2019-11-26", 6_000_000),
            _r("series_b", "2021-06-01", 44_000_000),
            _r("other", "2022-02-01", 15_000_000, "Series B+"),
            _r("series_c", "2024-06-11", 100_000_000),
        ],
        "total_raised": 165_000_000,
        "growth_stage": "growth",
        "last_funding_date": "2024-06-11",
        "last_funding_type": "series_c",
        "extra_updates": {"status": "acquired"},
    },
    # 124. Flawless AI — DB $100M → $33.5M
    {
        "slug": "flawless-ai",
        "rounds": [
            _r("seed", "2021-03-29", 1_390_000),
            _r("series_a", "2021-11-08", 32_100_000),
        ],
        "total_raised": 33_490_000,
        "growth_stage": "early",
        "last_funding_date": "2021-11-08",
        "last_funding_type": "series_a",
        "extra_updates": {},
    },
    # 125. Ambience — DB $100M → $349M
    {
        "slug": "ambience",
        "rounds": [
            _r("seed", "2020-09-11", 6_300_000),
            _r("series_a", "2022-04-01", 30_000_000),
            _r("series_b", "2024-02-06", 70_000_000),
            _r("series_c", "2025-07-29", 243_000_000),
        ],
        "total_raised": 349_300_000,
        "growth_stage": "late",
        "last_funding_date": "2025-07-29",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    # 126. Chorus AI — correct $100M, mark as acquired
    {
        "slug": "chorus-ai",
        "rounds": [
            _r("seed", "2016-09-01", 6_300_000),
            _r("series_a", "2017-01-01", 16_000_000),
            _r("series_b", "2018-11-01", 33_000_000),
            _r("series_c", "2020-07-01", 45_000_000),
        ],
        "total_raised": 100_300_000,
        "growth_stage": "growth",
        "last_funding_date": "2020-07-01",
        "last_funding_type": "series_c",
        "extra_updates": {"status": "acquired"},
    },
    # 128. Iambic — DB $100M → $306M
    {
        "slug": "iambic-therapeutics",
        "rounds": [
            _r("series_a", "2021-07-14", 53_000_000),
            _r("series_b", "2023-10-01", 100_000_000),
            _r("other", "2024-01-01", 50_000_000, "Series B Extension"),
            _r("series_c", "2025-11-06", 100_000_000),
        ],
        "total_raised": 303_000_000,
        "growth_stage": "late",
        "last_funding_date": "2025-11-06",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    # 129. Pinecone — DB $100M → $138M
    {
        "slug": "pinecone",
        "rounds": [
            _r("seed", "2021-01-01", 10_000_000),
            _r("series_a", "2022-03-29", 28_000_000),
            _r("series_b", "2023-04-27", 100_000_000),
        ],
        "total_raised": 138_000_000,
        "growth_stage": "growth",
        "last_funding_date": "2023-04-27",
        "last_funding_type": "series_b",
        "extra_updates": {},
    },
    # 130. Typeface — DB $100M → $206M
    {
        "slug": "typeface",
        "rounds": [
            _r("series_a", "2023-02-01", 65_000_000),
            _r("series_b", "2023-06-29", 141_000_000),
        ],
        "total_raised": 206_000_000,
        "growth_stage": "late",
        "last_funding_date": "2023-06-29",
        "last_funding_type": "series_b",
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
