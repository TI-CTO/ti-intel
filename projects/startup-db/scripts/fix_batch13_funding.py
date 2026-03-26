"""Fix funding data for batch 13 — companies ranked 141-150 by total_raised.

Verified 2026-03-26. Skipped: Cartesia(correct).
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
    # 141. Forethought — DB $92M → $117M, acquired by Zendesk
    {
        "slug": "forethought",
        "rounds": [
            _r("seed", "2017-12-19", 650_000),
            _r("series_a", "2019-01-01", 9_520_000),
            _r("series_b", "2020-10-28", 17_000_000),
            _r("series_c", "2021-12-15", 65_000_000),
            _r("series_d", "2025-05-23", 25_000_000),
        ],
        "total_raised": 117_170_000,
        "growth_stage": "growth",
        "last_funding_date": "2025-05-23",
        "last_funding_type": "series_d",
        "extra_updates": {"status": "acquired"},
    },
    # 142. Tessian — DB $90M → $182M, acquired by Proofpoint
    {
        "slug": "tessian",
        "rounds": [
            _r("seed", "2014-04-04", 255_000),
            _r("series_a", "2018-03-28", 13_000_000),
            _r("series_b", "2019-02-27", 42_000_000),
            _r("series_c", "2021-05-25", 65_000_000),
            _r("other", "2021-07-29", 9_800_000, "Series C extension"),
        ],
        "total_raised": 130_055_000,
        "growth_stage": "growth",
        "last_funding_date": "2021-07-29",
        "last_funding_type": "other",
        "extra_updates": {"status": "acquired"},
    },
    # 143. DEEPX — DB $90M → $103M
    {
        "slug": "deepx",
        "rounds": [
            _r("series_b", "2021-05-20", 17_700_000),
            _r("series_c", "2024-05-10", 80_500_000),
        ],
        "total_raised": 98_200_000,
        "growth_stage": "late",
        "last_funding_date": "2024-05-10",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    # 144. Synthesia — DB $90M → $536M
    {
        "slug": "synthesia",
        "rounds": [
            _r("seed", "2019-04-01", 3_100_000),
            _r("series_a", "2021-04-01", 12_500_000),
            _r("series_b", "2021-12-01", 50_000_000),
            _r("series_c", "2023-06-01", 90_000_000),
            _r("series_d", "2025-01-14", 180_000_000),
            _r("series_e", "2025-10-01", 200_000_000),
        ],
        "total_raised": 535_600_000,
        "growth_stage": "late",
        "last_funding_date": "2025-10-01",
        "last_funding_type": "series_e",
        "extra_updates": {},
    },
    # 145. Zama — DB $89M → $150M
    {
        "slug": "zama",
        "rounds": [
            _r("series_a", "2024-03-07", 73_000_000),
            _r("series_b", "2025-06-25", 57_000_000),
        ],
        "total_raised": 130_000_000,
        "growth_stage": "late",
        "last_funding_date": "2025-06-25",
        "last_funding_type": "series_b",
        "extra_updates": {},
    },
    # 146. Rescale — DB $89M → $369M
    {
        "slug": "rescale",
        "rounds": [
            _r("series_b", "2018-07-24", 32_000_000),
            _r("series_d", "2025-04-07", 115_000_000),
        ],
        "total_raised": 369_000_000,
        "growth_stage": "late",
        "last_funding_date": "2025-04-07",
        "last_funding_type": "series_d",
        "extra_updates": {},
    },
    # 147. Norm AI — DB $86M → $201M
    {
        "slug": "norm-ai",
        "rounds": [
            _r("seed", "2023-01-01", 12_000_000, "Seed estimate"),
            _r("series_a", "2024-06-11", 27_000_000),
            _r("series_b", "2025-03-11", 48_000_000),
            _r("series_c", "2025-11-03", 103_000_000),
        ],
        "total_raised": 190_000_000,
        "growth_stage": "late",
        "last_funding_date": "2025-11-03",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    # 149. Snorkel AI — DB $85M → $238M
    {
        "slug": "snorkel-ai",
        "rounds": [
            _r("seed", "2019-01-01", 3_300_000),
            _r("series_a", "2020-07-01", 12_000_000),
            _r("series_b", "2021-04-01", 35_000_000),
            _r("series_c", "2021-08-01", 85_000_000),
            _r("series_d", "2025-05-30", 100_000_000),
        ],
        "total_raised": 235_300_000,
        "growth_stage": "late",
        "last_funding_date": "2025-05-30",
        "last_funding_type": "series_d",
        "extra_updates": {},
    },
    # 150. Kinetica — DB $85M → $77.5M
    {
        "slug": "kinetica",
        "rounds": [
            _r("seed", "2016-04-01", 7_000_000),
            _r("series_a", "2017-06-29", 50_100_000),
            _r("other", "2020-08-21", 14_400_000, "Funding round"),
        ],
        "total_raised": 71_500_000,
        "growth_stage": "growth",
        "last_funding_date": "2020-08-21",
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
