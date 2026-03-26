"""Fix funding data for batch 14 — companies ranked 151-160.

Verified 2026-03-26. Skipped: Cloudfactory(correct), Foundry(correct),
Mathpresso/Neeva(already fixed).
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
    # 151. LiveKit — DB $83M → $168M
    {
        "slug": "livekit",
        "rounds": [
            _r("series_a", "2024-06-04", 22_500_000),
            _r("series_b", "2025-04-01", 45_000_000),
            _r("series_c", "2026-01-22", 100_000_000),
        ],
        "total_raised": 167_500_000,
        "growth_stage": "late",
        "last_funding_date": "2026-01-22",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    # 153. Harvey — DB $80M → $1.02B
    {
        "slug": "harvey",
        "rounds": [
            _r("seed", "2022-11-01", 5_000_000),
            _r("series_a", "2023-04-01", 21_000_000),
            _r("series_b", "2023-12-01", 80_000_000),
            _r("series_c", "2024-07-01", 100_000_000),
            _r("series_d", "2025-02-01", 300_000_000),
            _r("series_e", "2025-06-23", 300_000_000),
            _r("series_f", "2025-12-01", 160_000_000),
            _r("other", "2026-03-25", 200_000_000, "Series G"),
        ],
        "total_raised": 1_166_000_000,
        "growth_stage": "late",
        "last_funding_date": "2026-03-25",
        "last_funding_type": "other",
        "extra_updates": {},
    },
    # 154. ElevenLabs — DB $80M → $791M
    {
        "slug": "elevenlabs",
        "rounds": [
            _r("seed", "2023-01-25", 2_000_000),
            _r("series_a", "2023-06-01", 19_000_000),
            _r("series_b", "2024-01-22", 80_000_000),
            _r("series_c", "2025-01-30", 180_000_000),
            _r("series_d", "2026-02-04", 500_000_000),
        ],
        "total_raised": 781_000_000,
        "growth_stage": "late",
        "last_funding_date": "2026-02-04",
        "last_funding_type": "series_d",
        "extra_updates": {},
    },
    # 155. Weights & Biases — DB $80M → $250M, acquired by CoreWeave
    {
        "slug": "weights-biases",
        "rounds": [
            _r("series_a", "2018-05-31", 5_000_000),
            _r("series_b", "2021-02-01", 45_000_000),
            _r("series_c", "2021-10-13", 135_000_000),
            _r("other", "2023-08-09", 50_000_000, "Venture round"),
        ],
        "total_raised": 235_000_000,
        "growth_stage": "late",
        "last_funding_date": "2023-08-09",
        "last_funding_type": "other",
        "extra_updates": {"status": "acquired"},
    },
    # 157. Ideogram — DB $80M → $97M
    {
        "slug": "ideogram-ai",
        "rounds": [
            _r("seed", "2023-08-31", 16_500_000),
            _r("series_a", "2024-02-28", 80_000_000),
        ],
        "total_raised": 96_500_000,
        "growth_stage": "growth",
        "last_funding_date": "2024-02-28",
        "last_funding_type": "series_a",
        "extra_updates": {},
    },
    # 158. Dexory — DB $80M → $277M
    {
        "slug": "dexory",
        "rounds": [
            _r("seed", "2022-06-23", 13_000_000),
            _r("series_a", "2023-06-27", 19_000_000),
            _r("series_b", "2024-10-02", 80_000_000),
            _r("series_c", "2025-10-14", 165_000_000),
        ],
        "total_raised": 277_000_000,
        "growth_stage": "late",
        "last_funding_date": "2025-10-14",
        "last_funding_type": "series_c",
        "extra_updates": {},
    },
    # 159. Leonardo.ai — DB $78M → $31M, acquired by Canva
    {
        "slug": "leonardoai",
        "rounds": [
            _r("seed", "2023-01-01", 7_500_000, "Estimate"),
            _r("series_a", "2023-12-06", 23_500_000),
        ],
        "total_raised": 31_000_000,
        "growth_stage": "early",
        "last_funding_date": "2023-12-06",
        "last_funding_type": "series_a",
        "extra_updates": {"status": "acquired"},
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
