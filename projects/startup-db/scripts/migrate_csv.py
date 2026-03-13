"""Migrate legacy CSV data into startup-db tables.

Usage:
    cd projects/startup-db
    uv run python scripts/migrate_csv.py /path/to/companies.csv

Migrates:
  - companies → su_companies
  - investment_stage/amount → su_funding_rounds
  - key_personnel → su_people + su_company_people
"""

from __future__ import annotations

import csv
import json
import logging
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from startup_db.db import StartupRepository  # noqa: E402
from startup_db.models import (  # noqa: E402
    STAGE_MAP,
    STATUS_MAP,
    CompanyStatus,
    parse_personnel,
    role_from_title,
    slugify,
)

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

BATCH_SIZE = 50


def parse_tags(raw: str) -> list[str]:
    """Parse JSON array string like '["tag1","tag2"]' into list."""
    if not raw or not raw.strip():
        return []
    try:
        tags = json.loads(raw)
        if isinstance(tags, list):
            return [str(t).strip() for t in tags if t]
    except (json.JSONDecodeError, TypeError):
        pass
    return []


def csv_to_company_row(row: dict) -> dict:
    """Convert a CSV row to a su_companies insert dict."""
    stage = row.get("investment_stage", "").strip()
    status = STATUS_MAP.get(stage, CompanyStatus.ACTIVE)

    metadata: dict = {}
    if row.get("tech_competitiveness"):
        metadata["tech_competitiveness"] = int(row["tech_competitiveness"])
    if row.get("business_alignment"):
        metadata["business_alignment"] = row["business_alignment"]
    if row.get("bigtech_collaboration"):
        metadata["bigtech_collaboration"] = row["bigtech_collaboration"]

    name = row["company_name"].strip()
    return {
        "name": name,
        "slug": slugify(name),
        "description": row.get("company_overview", "").strip() or None,
        "website": row.get("website", "").strip() or None,
        "status": status.value,
        "main_category": row.get("main_category", "").strip() or None,
        "sub_category": row.get("sub_category", "").strip() or None,
        "tags": parse_tags(row.get("tags", "")),
        "country": row.get("location", "").strip() or None,
        "technology": row.get("technology", "").strip() or None,
        "main_product": row.get("main_product", "").strip() or None,
        "discovery_source": row.get("discovery_source", "").strip() or None,
        "metadata": json.dumps(metadata, ensure_ascii=False) if metadata else "{}",
    }


def migrate(csv_path: Path) -> None:
    """Run the full migration."""
    repo = StartupRepository()

    # Read CSV
    with csv_path.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    logger.info("Read %d rows from CSV", len(rows))

    # ── Phase 1: Companies ──
    logger.info("Phase 1: Inserting companies...")
    company_rows = []
    slug_to_csv: dict[str, dict] = {}  # for funding/people lookup later

    seen_slugs: set[str] = set()
    for row in rows:
        crow = csv_to_company_row(row)
        slug = crow["slug"]

        # Handle duplicate slugs
        if slug in seen_slugs:
            suffix = 2
            while f"{slug}-{suffix}" in seen_slugs:
                suffix += 1
            slug = f"{slug}-{suffix}"
            crow["slug"] = slug

        seen_slugs.add(slug)
        company_rows.append(crow)
        slug_to_csv[slug] = row

    # Batch insert
    inserted_companies = []
    for i in range(0, len(company_rows), BATCH_SIZE):
        batch = company_rows[i : i + BATCH_SIZE]
        result = repo.batch_insert_companies(batch)
        inserted_companies.extend(result)
        logger.info("  Inserted companies %d-%d", i + 1, i + len(batch))

    logger.info("  Total companies: %d", len(inserted_companies))

    # Build slug → id map
    slug_to_id: dict[str, str] = {}
    for c in inserted_companies:
        slug_to_id[c["slug"]] = c["id"]

    # ── Phase 2: Funding rounds ──
    logger.info("Phase 2: Creating funding rounds...")
    funding_rows = []
    for slug, csv_row in slug_to_csv.items():
        stage = csv_row.get("investment_stage", "").strip()
        amount = csv_row.get("investment_amount", "").strip()

        if not stage or slug not in slug_to_id:
            continue

        round_type = STAGE_MAP.get(stage)
        if not round_type:
            logger.warning("  Unknown stage '%s' for %s, skipping", stage, slug)
            continue

        fr: dict = {
            "company_id": slug_to_id[slug],
            "round_type": round_type.value,
            "currency": "KRW",
        }
        if amount:
            try:
                fr["raised_amount"] = float(amount)
            except ValueError:
                pass

        funding_rows.append(fr)

    for i in range(0, len(funding_rows), BATCH_SIZE):
        batch = funding_rows[i : i + BATCH_SIZE]
        repo.batch_insert_funding_rounds(batch)
        logger.info("  Inserted funding rounds %d-%d", i + 1, i + len(batch))

    logger.info("  Total funding rounds: %d", len(funding_rows))

    # ── Phase 3: People + company-people links ──
    logger.info("Phase 3: Creating people and company-people links...")
    people_count = 0
    link_count = 0

    for slug, csv_row in slug_to_csv.items():
        raw_personnel = csv_row.get("key_personnel", "").strip()
        if not raw_personnel or slug not in slug_to_id:
            continue

        parsed = parse_personnel(raw_personnel)
        for person_name, title in parsed:
            if not person_name:
                continue
            role = role_from_title(title) if title else role_from_title("")
            company_name = csv_row.get("company_name", "").strip()

            result = repo.upsert_person(
                name=person_name,
                title=title or None,
                organization=company_name or None,
                company_id=slug_to_id[slug],
                role=role.value,
            )
            if result:
                people_count += 1
                link_count += 1

    logger.info("  People created/updated: %d", people_count)
    logger.info("  Company-people links: %d", link_count)

    # ── Summary ──
    logger.info("Migration complete!")
    logger.info("  Companies: %d", len(inserted_companies))
    logger.info("  Funding rounds: %d", len(funding_rows))
    logger.info("  People+links: %d", people_count)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python scripts/migrate_csv.py <csv_file>")
        sys.exit(1)

    csv_path = Path(sys.argv[1])
    if not csv_path.exists():
        print(f"Error: File not found: {csv_path}")
        sys.exit(1)

    migrate(csv_path)


if __name__ == "__main__":
    main()
