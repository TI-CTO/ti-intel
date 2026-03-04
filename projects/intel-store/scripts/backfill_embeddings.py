"""Backfill embeddings for intel_items that don't have them yet.

Usage:
    cd projects/intel-store
    uv run python scripts/backfill_embeddings.py [--batch-size 32] [--limit 1000]

This script:
1. Fetches items without embeddings from intel_items
2. Generates embeddings using multilingual-e5-large
3. Updates each row with the embedding vector
"""

from __future__ import annotations

import argparse
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def main() -> None:
    parser = argparse.ArgumentParser(description="Backfill intel_items embeddings")
    parser.add_argument("--batch-size", type=int, default=32, help="Texts per batch (default 32)")
    parser.add_argument(
        "--limit",
        type=int,
        default=1000,
        help="Max items to process",
    )
    args = parser.parse_args()

    from intel_store import embeddings
    from intel_store.db.repository import IntelRepository

    repo = IntelRepository()

    processed = 0
    while processed < args.limit:
        fetch_limit = min(args.batch_size, args.limit - processed)
        items = repo.get_items_without_embedding(limit=fetch_limit)
        if not items:
            logger.info("No more items without embeddings.")
            break

        texts = []
        for item in items:
            passage = f"{item['title']}. {item.get('abstract', '')}"
            texts.append(passage)

        logger.info("Generating embeddings for %d items...", len(texts))
        vectors = embeddings.embed_passages_batch(texts, batch_size=args.batch_size)

        for item, vector in zip(items, vectors):
            repo.update_embedding(item["id"], vector)

        processed += len(items)
        logger.info("Progress: %d items processed", processed)

    logger.info("Backfill complete: %d items embedded", processed)


if __name__ == "__main__":
    main()
