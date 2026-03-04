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
