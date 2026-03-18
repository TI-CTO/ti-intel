"""Fix funding data for companies ranked 21-50 based on verified research."""
import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger(__name__)

# Add project to path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from startup_db.db import get_client


# Verified funding updates (from 3 batch research agents)
UPDATES = [
    # Batch 1 (21-30)
    {"slug": "tenstorrent", "total_raised": 1_180_000_000, "last_funding_type": "series_d", "last_funding_date": "2024-12-02"},
    {"slug": "cerebras", "total_raised": 2_550_000_000, "last_funding_type": "series_h", "last_funding_date": "2026-02-03"},
    {"slug": "baichuan-ai", "total_raised": 1_038_000_000, "last_funding_type": "series_a", "last_funding_date": "2024-07-25"},
    # Poolside: $626M correct, skip
    {"slug": "chainguard", "total_raised": 892_000_000, "last_funding_type": "growth", "last_funding_date": "2025-10-23"},
    {"slug": "vercel", "total_raised": 863_000_000, "last_funding_type": "series_f", "last_funding_date": "2025-09-30"},
    # Abnormal Security: $557M correct, skip
    {"slug": "thoughtspot", "total_raised": 809_000_000, "last_funding_type": "series_f", "last_funding_date": "2021-11-12"},
    {"slug": "shield-ai", "total_raised": 1_660_000_000, "last_funding_type": "series_f", "last_funding_date": "2025-03-06"},
    {"slug": "ainnovation", "total_raised": 120_000_000, "last_funding_type": "ipo", "last_funding_date": "2022-01-27"},

    # Batch 2 (31-40)
    {"slug": "avaya", "total_raised": 628_000_000, "last_funding_type": "post_ipo", "last_funding_date": "2019-10-04"},
    {"slug": "isomorphic-laboratories", "total_raised": 600_000_000, "last_funding_type": "series_d", "last_funding_date": "2025-03-31"},
    {"slug": "apptronik", "total_raised": 963_000_000, "last_funding_type": "series_a", "last_funding_date": "2026-02-11"},
    {"slug": "crusoe", "total_raised": 3_900_000_000, "last_funding_type": "series_e", "last_funding_date": "2025-10-24"},
    {"slug": "zhipu-ai", "total_raised": 1_500_000_000, "last_funding_type": "ipo", "last_funding_date": "2026-01-08"},
    {"slug": "cohere", "total_raised": 1_540_000_000, "last_funding_type": "series_d", "last_funding_date": "2025-08-31"},
    {"slug": "uniphore", "total_raised": 987_000_000, "last_funding_type": "series_f", "last_funding_date": "2025-10-22"},
    {"slug": "ponyai", "total_raised": 1_190_000_000, "last_funding_type": "ipo", "last_funding_date": "2024-11-27"},
    {"slug": "kobold-metals", "total_raised": 1_210_000_000, "last_funding_type": "series_c", "last_funding_date": "2025-10-30"},
    {"slug": "grammarly", "total_raised": 1_545_000_000, "last_funding_type": "debt", "last_funding_date": "2025-05-29"},

    # Batch 3 (41-50)
    # Zhipu: duplicate of zhipu-ai, will be handled separately
    {"slug": "weride", "total_raised": 1_442_000_000, "last_funding_type": "ipo", "last_funding_date": "2024-10-23"},
    # Denodo: $336M correct, skip
    {"slug": "ai21-labs", "total_raised": 636_000_000, "last_funding_type": "series_d", "last_funding_date": "2025-05-09"},
    {"slug": "lambda-labs", "total_raised": 800_000_000, "last_funding_type": "series_d", "last_funding_date": "2025-01-01"},
    # Moveworks: $305M~315M close enough, skip
    # Skilled AI: verification failed, skip
    {"slug": "deepexi", "total_raised": 271_000_000, "last_funding_type": "ipo", "last_funding_date": "2025-10-31"},
    # CloudWalk: ambiguous, skip
    {"slug": "writer", "total_raised": 369_000_000, "last_funding_type": "series_c", "last_funding_date": "2024-11-06"},
]

# Zhipu duplicate slug to delete
DUPLICATE_SLUG = "zhipu"


def main() -> None:
    client = get_client()

    # Update funding data
    updated = 0
    for item in UPDATES:
        slug = item["slug"]
        update_data = {
            "total_raised": item["total_raised"],
            "last_funding_type": item["last_funding_type"],
            "last_funding_date": item["last_funding_date"],
        }

        result = client.table("su_companies").update(update_data).eq("slug", slug).execute()
        if result.data:
            old = "unknown"
            log.info(f"  ✓ {slug}: total_raised → ${item['total_raised']:,.0f}, last: {item['last_funding_type']} ({item['last_funding_date']})")
            updated += 1
        else:
            log.warning(f"  ✗ {slug}: not found in DB")

    # Handle Zhipu duplicate
    log.info(f"\n--- Checking duplicate: {DUPLICATE_SLUG} ---")
    dup = client.table("su_companies").select("id,name,slug").eq("slug", DUPLICATE_SLUG).execute()
    if dup.data:
        dup_id = dup.data[0]["id"]
        log.info(f"  Found duplicate: {dup.data[0]['name']} (id={dup_id})")
        # Delete related records first
        client.table("su_company_topics").delete().eq("company_id", dup_id).execute()
        client.table("su_funding_rounds").delete().eq("company_id", dup_id).execute()
        client.table("su_company_relations").delete().eq("company_a_id", dup_id).execute()
        client.table("su_company_relations").delete().eq("company_b_id", dup_id).execute()
        client.table("su_scores").delete().eq("company_id", dup_id).execute()
        client.table("su_companies").delete().eq("id", dup_id).execute()
        log.info(f"  ✓ Deleted duplicate '{DUPLICATE_SLUG}' (merged into zhipu-ai)")
    else:
        log.info(f"  '{DUPLICATE_SLUG}' not found, skipping")

    log.info(f"\n=== Done: {updated} companies updated, 1 duplicate removed ===")


if __name__ == "__main__":
    main()
