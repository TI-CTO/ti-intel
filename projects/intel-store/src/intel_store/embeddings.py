"""Local embedding service using multilingual-e5-large.

multilingual-e5-large uses asymmetric query/passage prefixes:
- Documents: "passage: {text}"
- Queries: "query: {text}"
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)

_model = None


def _get_model():
    """Lazy-load the sentence-transformers model."""
    global _model
    if _model is None:
        from sentence_transformers import SentenceTransformer

        from intel_store.config import settings

        logger.info("Loading embedding model: %s", settings.embedding_model)
        _model = SentenceTransformer(settings.embedding_model)
    return _model


def embed_passage(text: str) -> list[float]:
    """Embed a document passage (prefixed with 'passage:').

    Args:
        text: Raw text to embed (title + abstract). Prefix is added internally.

    Returns:
        1024-dimensional float vector.
    """
    model = _get_model()
    prefixed = f"passage: {text}"
    vector = model.encode(prefixed, normalize_embeddings=True)
    return vector.tolist()


def embed_query(text: str) -> list[float]:
    """Embed a search query (prefixed with 'query:').

    Args:
        text: Search query string. Prefix is added internally.

    Returns:
        1024-dimensional float vector.
    """
    model = _get_model()
    prefixed = f"query: {text}"
    vector = model.encode(prefixed, normalize_embeddings=True)
    return vector.tolist()


def embed_passages_batch(texts: list[str], *, batch_size: int = 32) -> list[list[float]]:
    """Embed multiple passages in batches.

    Args:
        texts: List of raw texts. 'passage:' prefix is added internally.
        batch_size: Number of texts per batch.

    Returns:
        List of 1024-dimensional float vectors.
    """
    model = _get_model()
    prefixed = [f"passage: {t}" for t in texts]
    vectors = model.encode(prefixed, normalize_embeddings=True, batch_size=batch_size)
    return [v.tolist() for v in vectors]


def cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    """Compute cosine similarity between two pre-normalised vectors.

    Both vectors must already be L2-normalised (as produced by embed_query /
    embed_passage), so the similarity reduces to a plain dot product.

    Args:
        vec_a: First normalised float vector.
        vec_b: Second normalised float vector.

    Returns:
        Cosine similarity in the range [-1.0, 1.0].
    """
    import numpy as np

    a = np.array(vec_a, dtype=float)
    b = np.array(vec_b, dtype=float)
    return float(np.dot(a, b))


def filter_by_relevance(
    query: str,
    items: list[dict],
    *,
    threshold: float = 0.3,
    title_key: str = "title",
    abstract_key: str = "abstract",
) -> list[dict]:
    """Filter collected items by embedding-based relevance to a query.

    Computes cosine similarity between the query embedding and each item's
    title+abstract passage embedding, then discards items below threshold.

    Args:
        query: The search query used to collect the items.
        items: List of raw collector dicts (each must have at least a title).
        threshold: Minimum cosine similarity to retain an item (default 0.3).
        title_key: Dict key for item title.
        abstract_key: Dict key for item abstract / summary.

    Returns:
        Filtered list containing only items at or above the threshold.
    """
    if not items:
        return items

    query_vec = embed_query(query)

    passages = [
        f"{item.get(title_key, '')}. {item.get(abstract_key, '') or ''}".strip() for item in items
    ]
    passage_vecs = embed_passages_batch(passages)

    kept: list[dict] = []
    filtered_count = 0
    for item, passage_vec in zip(items, passage_vecs):
        score = cosine_similarity(query_vec, passage_vec)
        if score >= threshold:
            kept.append(item)
        else:
            filtered_count += 1
            logger.debug(
                "Relevance filter: score=%.3f < %.3f — skipping '%s'",
                score,
                threshold,
                item.get(title_key, "")[:60],
            )

    logger.info(
        "Relevance filter: kept %d/%d items (threshold=%.2f, filtered=%d)",
        len(kept),
        len(items),
        threshold,
        filtered_count,
    )
    return kept
