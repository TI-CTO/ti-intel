"""Migrate existing data from news_items, papers, patents to intel_items.

Usage:
    cd projects/intel-store
    uv run python scripts/migrate_data.py [--dry-run]

Reads from existing Supabase tables (news_items, papers, paper_topics,
patents, patent_topics, source_refs) and inserts into intel_items +
intel_item_topics.
"""

from __future__ import annotations

import hashlib
import json
import logging
import sys
from datetime import date

from supabase import Client

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def get_client() -> Client:
    """Create a Supabase client from intel_store config."""
    from intel_store.db.client import get_client

    return get_client()


def compute_hash(title: str, abstract: str) -> str:
    """Compute content_hash: SHA-256(title + abstract[:200])."""
    text = title + (abstract or "")[:200]
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def migrate_news(client: Client, *, dry_run: bool = False) -> int:
    """Migrate news_items → intel_items."""
    rows = client.table("news_items").select("*").execute().data
    logger.info("Found %d news items to migrate", len(rows))

    count = 0
    for row in rows:
        title = row.get("title", "").strip()
        if not title:
            continue

        item = {
            "item_type": "news",
            "external_id": row.get("url"),
            "content_hash": compute_hash(title, row.get("summary", "")),
            "title": title,
            "abstract": row.get("summary", "") or "",
            "source_name": row.get("source", "unknown"),
            "source_url": row.get("url"),
            "published_date": row.get("published_date"),
            "collected_date": row.get("collected_date") or date.today().isoformat(),
            "reliability": row.get("reliability_tag", "C"),
            "metadata": json.dumps(
                {
                    "keywords": _parse_json(row.get("keywords", "[]")),
                    "collector": "",
                    "key_highlights": row.get("key_highlights", ""),
                },
                ensure_ascii=False,
            ),
        }

        if dry_run:
            logger.info("  [DRY RUN] Would insert news: %s", title[:60])
        else:
            result = (
                client.table("intel_items")
                .upsert(item, on_conflict="item_type,source_name,external_id")
                .execute()
            )
            if result.data:
                item_id = result.data[0]["id"]
                topic_id = row.get("topic_id")
                if topic_id:
                    client.table("intel_item_topics").upsert(
                        {"item_id": item_id, "topic_id": topic_id, "assigned_by": "collector"},
                        on_conflict="item_id,topic_id",
                    ).execute()
        count += 1

    return count


def migrate_papers(client: Client, *, dry_run: bool = False) -> int:
    """Migrate papers + paper_topics → intel_items + intel_item_topics."""
    rows = client.table("papers").select("*").execute().data
    logger.info("Found %d papers to migrate", len(rows))

    # Fetch paper_topics mapping
    topic_rows = client.table("paper_topics").select("paper_id, topic_id, relevance").execute().data
    paper_topics: dict[int, list[dict]] = {}
    for tr in topic_rows:
        paper_topics.setdefault(tr["paper_id"], []).append(tr)

    count = 0
    for row in rows:
        title = row.get("title", "").strip()
        if not title:
            continue

        item = {
            "item_type": "paper",
            "external_id": row.get("external_id"),
            "content_hash": compute_hash(title, row.get("abstract", "")),
            "title": title,
            "abstract": row.get("abstract", "") or "",
            "source_name": row.get("source", "semantic_scholar"),
            "source_url": row.get("raw_url"),
            "published_date": row.get("published_date"),
            "collected_date": row.get("collected_date") or date.today().isoformat(),
            "reliability": row.get("reliability_tag", "A"),
            "metadata": json.dumps(
                {
                    "authors": _parse_json(row.get("authors", "[]")),
                    "citation_count": row.get("citation_count", 0),
                    "venue": "",
                    "key_highlights": row.get("key_highlights", ""),
                },
                ensure_ascii=False,
            ),
        }

        if dry_run:
            logger.info("  [DRY RUN] Would insert paper: %s", title[:60])
        else:
            result = (
                client.table("intel_items")
                .upsert(item, on_conflict="item_type,source_name,external_id")
                .execute()
            )
            if result.data:
                item_id = result.data[0]["id"]
                paper_id = row.get("id")
                for tp in paper_topics.get(paper_id, []):
                    client.table("intel_item_topics").upsert(
                        {
                            "item_id": item_id,
                            "topic_id": tp["topic_id"],
                            "relevance": tp.get("relevance", 1.0),
                            "assigned_by": "collector",
                        },
                        on_conflict="item_id,topic_id",
                    ).execute()
        count += 1

    return count


def migrate_patents(client: Client, *, dry_run: bool = False) -> int:
    """Migrate patents + patent_topics → intel_items + intel_item_topics."""
    rows = client.table("patents").select("*").execute().data
    logger.info("Found %d patents to migrate", len(rows))

    topic_rows = (
        client.table("patent_topics").select("patent_id, topic_id, relevance").execute().data
    )
    patent_topics: dict[int, list[dict]] = {}
    for tr in topic_rows:
        patent_topics.setdefault(tr["patent_id"], []).append(tr)

    count = 0
    for row in rows:
        title = row.get("title", "").strip()
        if not title:
            continue

        item = {
            "item_type": "patent",
            "external_id": row.get("external_id"),
            "content_hash": compute_hash(title, row.get("abstract", "")),
            "title": title,
            "abstract": row.get("abstract", "") or "",
            "source_name": row.get("source", "uspto"),
            "source_url": row.get("raw_url"),
            "published_date": row.get("publication_date"),
            "collected_date": row.get("collected_date") or date.today().isoformat(),
            "reliability": row.get("reliability_tag", "A"),
            "metadata": json.dumps(
                {
                    "applicant": row.get("applicant", ""),
                    "filing_date": row.get("filing_date"),
                    "ipc_codes": _parse_json(row.get("ipc_codes", "[]")),
                    "key_highlights": row.get("key_highlights", ""),
                },
                ensure_ascii=False,
            ),
        }

        if dry_run:
            logger.info("  [DRY RUN] Would insert patent: %s", title[:60])
        else:
            result = (
                client.table("intel_items")
                .upsert(item, on_conflict="item_type,source_name,external_id")
                .execute()
            )
            if result.data:
                item_id = result.data[0]["id"]
                patent_id = row.get("id")
                for tp in patent_topics.get(patent_id, []):
                    client.table("intel_item_topics").upsert(
                        {
                            "item_id": item_id,
                            "topic_id": tp["topic_id"],
                            "relevance": tp.get("relevance", 1.0),
                            "assigned_by": "collector",
                        },
                        on_conflict="item_id,topic_id",
                    ).execute()
        count += 1

    return count


def migrate_source_refs(client: Client, *, dry_run: bool = False) -> int:
    """Migrate source_refs → intel_items (as report/standard type)."""
    rows = client.table("source_refs").select("*").execute().data
    logger.info("Found %d source refs to migrate", len(rows))

    topic_rows = client.table("source_ref_topics").select("source_ref_id, topic_id").execute().data
    ref_topics: dict[int, list[int]] = {}
    for tr in topic_rows:
        ref_topics.setdefault(tr["source_ref_id"], []).append(tr["topic_id"])

    type_map = {
        "whitepaper": "report",
        "standard": "standard",
        "internal": "report",
        "url": "report",
        "report": "report",
    }

    count = 0
    for row in rows:
        title = row.get("title", "").strip()
        if not title:
            continue

        source_type = row.get("source_type", "report")
        item_type = type_map.get(source_type, "report")

        item = {
            "item_type": item_type,
            "external_id": row.get("file_path") or row.get("url"),
            "content_hash": compute_hash(title, row.get("description", "")),
            "title": title,
            "abstract": row.get("description", "") or "",
            "source_name": row.get("publisher", "internal"),
            "source_url": row.get("url"),
            "published_date": row.get("published_date"),
            "collected_date": date.today().isoformat(),
            "reliability": "B",
            "metadata": json.dumps(
                {
                    "report_path": row.get("file_path", ""),
                    "section": "",
                    "original_type": source_type,
                },
                ensure_ascii=False,
            ),
        }

        if dry_run:
            logger.info("  [DRY RUN] Would insert source_ref: %s", title[:60])
        else:
            result = (
                client.table("intel_items")
                .upsert(item, on_conflict="item_type,source_name,external_id")
                .execute()
            )
            if result.data:
                item_id = result.data[0]["id"]
                for topic_id in ref_topics.get(row["id"], []):
                    client.table("intel_item_topics").upsert(
                        {"item_id": item_id, "topic_id": topic_id, "assigned_by": "manual"},
                        on_conflict="item_id,topic_id",
                    ).execute()
        count += 1

    return count


def _parse_json(value) -> list:
    """Parse JSON string to list, or return as-is if already a list."""
    if isinstance(value, list):
        return value
    try:
        return json.loads(value)
    except (json.JSONDecodeError, TypeError):
        return []


def main() -> None:
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        logger.info("=== DRY RUN MODE — no data will be written ===")

    client = get_client()

    news_count = migrate_news(client, dry_run=dry_run)
    paper_count = migrate_papers(client, dry_run=dry_run)
    patent_count = migrate_patents(client, dry_run=dry_run)
    ref_count = migrate_source_refs(client, dry_run=dry_run)

    logger.info(
        "\nMigration %s: news=%d, papers=%d, patents=%d, source_refs=%d",
        "preview" if dry_run else "complete",
        news_count,
        paper_count,
        patent_count,
        ref_count,
    )


if __name__ == "__main__":
    main()
