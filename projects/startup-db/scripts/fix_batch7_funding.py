"""Fix funding data for batch 7 — companies ranked 81-91 by total_raised.

Verified 2026-03-26. Skipped: Barracuda(correct+acquired), Alteryx(correct+acquired),
DataGrand(already fixed in batch6).
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
    # 81. Hyperscience — DB $180M → $299M
    {
        "slug": "hyperscience",
        "rounds": [
            _r("series_a", "2015-07-22", 10_900_000),
            _r("other", "2016-12-15", 18_000_000, "Series A-2"),
            _r("series_b", "2019-01-16", 30_000_000),
            _r("series_c", "2020-06-04", 60_000_000),
            _r("series_d", "2020-10-16", 80_000_000),
            _r("series_e", "2021-12-22", 100_000_000),
        ],
        "total_raised": 298_900_000,
        "growth_stage": "late",
        "last_funding_date": "2021-12-22",
        "last_funding_type": "series_e",
        "extra_updates": {},
    },
    # 82. Aisera — DB $180M → $150M, acquired by Automation Anywhere
    {
        "slug": "aisera",
        "rounds": [
            _r("series_b", "2020-02-18", 20_000_000),
            _r("series_c", "2021-04-21", 40_000_000),
            _r("series_d", "2022-08-03", 90_000_000),
        ],
        "total_raised": 150_000_000,
        "growth_stage": "growth",
        "last_funding_date": "2022-08-03",
        "last_funding_type": "series_d",
        "extra_updates": {"status": "acquired"},
    },
    # 84. Amelia — DB $175M → $189M, acquired by SoundHound
    {
        "slug": "amelia",
        "rounds": [
            _r("seed", "2020-01-24", 25_000, "Arcadis"),
            _r("seed", "2020-10-11", 125_000, "LAUNCH Accelerator"),
            _r("series_d", "2023-03-07", 175_000_000),
            _r("other", "2023-04-05", 14_000_000, "Debt estimate"),
        ],
        "total_raised": 189_150_000,
        "growth_stage": "growth",
        "last_funding_date": "2023-04-05",
        "last_funding_type": "other",
        "extra_updates": {"status": "acquired"},
    },
    # 85. Sift — DB $170M → $157M
    {
        "slug": "sift",
        "rounds": [
            _r("seed", "2011-09-01", 1_500_000),
            _r("series_a", "2013-03-19", 5_500_000),
            _r("series_b", "2014-05-14", 18_000_000),
            _r("series_c", "2016-07-19", 30_000_000),
            _r("series_d", "2018-03-21", 53_000_000),
            _r("series_e", "2021-04-22", 50_000_000),
        ],
        "total_raised": 158_000_000,
        "growth_stage": "late",
        "last_funding_date": "2021-04-22",
        "last_funding_type": "series_e",
        "extra_updates": {},
    },
    # 86. Alteryx — correct $163M but mark as acquired
    {
        "slug": "alteryx",
        "rounds": [
            _r("seed", "2011-04-05", 6_000_000),
            _r("series_a", "2013-05-20", 12_000_000),
            _r("series_b", "2014-10-06", 60_000_000),
            _r("series_c", "2015-10-28", 85_000_000),
        ],
        "total_raised": 163_000_000,
        "growth_stage": "public",
        "last_funding_date": "2015-10-28",
        "last_funding_type": "series_c",
        "extra_updates": {"status": "acquired"},
    },
    # 88. Augment AI — DB $158M → $252M
    {
        "slug": "augment-ai",
        "rounds": [
            _r("series_a", "2024-01-01", 25_000_000),
            _r("series_b", "2024-04-24", 227_000_000),
        ],
        "total_raised": 252_000_000,
        "growth_stage": "late",
        "last_funding_date": "2024-04-24",
        "last_funding_type": "series_b",
        "extra_updates": {},
    },
    # 89. AssemblyAI — DB $158M → $115M
    {
        "slug": "assemblyai",
        "rounds": [
            _r("seed", "2017-08-23", 120_000, "Y Combinator"),
            _r("series_a", "2022-03-04", 28_000_000),
            _r("series_b", "2022-07-14", 30_000_000),
            _r("series_c", "2023-12-04", 50_000_000),
        ],
        "total_raised": 108_120_000,
        "growth_stage": "growth",
        "last_funding_date": "2023-12-04",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    # 90. 梅卡曼德 — DB $150M → $350M+
    {
        "slug": "\u6885\u5361\u66fc\u5fb7",
        "rounds": [
            _r("series_a", "2019-04-26", 15_000_000, "Series A+A+ combined"),
            _r("series_b", "2020-03-02", 14_200_000),
            _r("other", "2020-12-01", 15_480_000, "Series B+"),
            _r("series_c", "2021-09-29", 155_000_000),
            _r("other", "2022-06-01", 155_000_000, "Series C+"),
            _r("series_d", "2022-08-01", 38_000_000),
        ],
        "total_raised": 392_680_000,
        "growth_stage": "late",
        "last_funding_date": "2022-08-01",
        "last_funding_type": "series_d",
        "extra_updates": {},
    },
    # 91. Character AI — DB $150M → $193M
    {
        "slug": "character-ai",
        "rounds": [
            _r("seed", "2021-12-01", 43_000_000),
            _r("series_a", "2023-03-23", 150_000_000),
        ],
        "total_raised": 193_000_000,
        "growth_stage": "growth",
        "last_funding_date": "2023-03-23",
        "last_funding_type": "series_a",
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
