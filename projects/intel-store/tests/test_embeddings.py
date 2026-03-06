"""Tests for embedding utility functions (no model loading required)."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from intel_store.embeddings import cosine_similarity, filter_by_relevance

# ── cosine_similarity tests ───────────────────────────────────────


class TestCosineSimilarity:
    def test_identical_vectors(self):
        """Identical normalised vectors should produce similarity of 1.0."""
        vec = [1.0, 0.0, 0.0]
        assert cosine_similarity(vec, vec) == pytest.approx(1.0)

    def test_orthogonal_vectors(self):
        """Orthogonal vectors should produce similarity of 0.0."""
        a = [1.0, 0.0, 0.0]
        b = [0.0, 1.0, 0.0]
        assert cosine_similarity(a, b) == pytest.approx(0.0)

    def test_opposite_vectors(self):
        """Opposite vectors should produce similarity of -1.0."""
        a = [1.0, 0.0, 0.0]
        b = [-1.0, 0.0, 0.0]
        assert cosine_similarity(a, b) == pytest.approx(-1.0)

    def test_partial_similarity(self):
        """Vectors at 60-degree angle have cosine similarity of 0.5."""
        import math

        a = [1.0, 0.0]
        b = [0.5, math.sqrt(3) / 2]
        assert cosine_similarity(a, b) == pytest.approx(0.5, abs=1e-6)

    def test_returns_float(self):
        """Return type must be float."""
        result = cosine_similarity([1.0, 0.0], [0.0, 1.0])
        assert isinstance(result, float)


# ── filter_by_relevance tests ─────────────────────────────────────


def _make_unit_vec(dim: int, index: int) -> list[float]:
    """Helper: unit vector with 1.0 at position ``index``."""
    v = [0.0] * dim
    v[index] = 1.0
    return v


class TestFilterByRelevance:
    """Tests for filter_by_relevance using mocked embed_* calls."""

    def _patch_embeds(self, query_vec: list[float], passage_vecs: list[list[float]]):
        """Return context-manager pair that patches embed_query and embed_passages_batch."""
        patch_query = patch(
            "intel_store.embeddings.embed_query",
            return_value=query_vec,
        )
        patch_batch = patch(
            "intel_store.embeddings.embed_passages_batch",
            return_value=passage_vecs,
        )
        return patch_query, patch_batch

    def test_all_items_pass_threshold(self):
        """All items above threshold should be kept."""
        query_vec = _make_unit_vec(3, 0)
        # Both passages are identical to query → similarity 1.0
        passage_vecs = [query_vec, query_vec]
        items = [
            {"title": "Relevant Paper A", "abstract": "content a"},
            {"title": "Relevant Paper B", "abstract": "content b"},
        ]
        pq, pb = self._patch_embeds(query_vec, passage_vecs)
        with pq, pb:
            result = filter_by_relevance("query text", items, threshold=0.3)
        assert len(result) == 2

    def test_all_items_filtered_out(self):
        """All items below threshold should be removed."""
        query_vec = _make_unit_vec(3, 0)
        # Both passages are orthogonal to query → similarity 0.0
        orthogonal = _make_unit_vec(3, 1)
        passage_vecs = [orthogonal, orthogonal]
        items = [
            {"title": "Unrelated Paper A", "abstract": "physics stuff"},
            {"title": "Unrelated Paper B", "abstract": "astronomy stuff"},
        ]
        pq, pb = self._patch_embeds(query_vec, passage_vecs)
        with pq, pb:
            result = filter_by_relevance("security query", items, threshold=0.3)
        assert len(result) == 0

    def test_partial_filtering(self):
        """Only items at or above threshold should survive."""
        query_vec = _make_unit_vec(3, 0)
        relevant_vec = _make_unit_vec(3, 0)  # similarity 1.0 ✓
        irrelevant_vec = _make_unit_vec(3, 2)  # similarity 0.0 ✗
        passage_vecs = [relevant_vec, irrelevant_vec, relevant_vec]
        items = [
            {"title": "Good Paper", "abstract": "homomorphic encryption"},
            {"title": "Bad Paper", "abstract": "stellar evolution"},
            {"title": "Good Paper 2", "abstract": "lattice cryptography"},
        ]
        pq, pb = self._patch_embeds(query_vec, passage_vecs)
        with pq, pb:
            result = filter_by_relevance("encryption", items, threshold=0.3)
        assert len(result) == 2
        assert result[0]["title"] == "Good Paper"
        assert result[1]["title"] == "Good Paper 2"

    def test_exact_threshold_is_kept(self):
        """Items exactly at the threshold should be kept (>=, not >)."""
        import math

        # Build a vector with cosine similarity exactly equal to threshold (0.3).
        # For 2D normalised vectors: cos(θ) = 0.3 when the second component is sqrt(1-0.09).
        threshold = 0.3
        query_vec = [1.0, 0.0]
        passage_vec = [threshold, math.sqrt(1 - threshold**2)]

        items = [{"title": "Edge Case Paper", "abstract": "borderline"}]
        pq, pb = self._patch_embeds(query_vec, [passage_vec])
        with pq, pb:
            result = filter_by_relevance("query", items, threshold=threshold)
        assert len(result) == 1

    def test_empty_items_returns_empty(self):
        """Empty input should return empty list without touching embeddings."""
        with patch("intel_store.embeddings.embed_query") as mock_eq:
            result = filter_by_relevance("query", [], threshold=0.3)
        assert result == []
        mock_eq.assert_not_called()

    def test_custom_abstract_key(self):
        """abstract_key parameter should be respected."""
        query_vec = _make_unit_vec(3, 0)
        passage_vecs = [query_vec]
        items = [{"title": "Paper", "summary": "relevant content"}]
        pq, pb = self._patch_embeds(query_vec, passage_vecs)
        with pq, pb:
            result = filter_by_relevance("query", items, threshold=0.3, abstract_key="summary")
        assert len(result) == 1

    def test_missing_abstract_key_handled_gracefully(self):
        """Items missing the abstract key should be handled without error."""
        query_vec = _make_unit_vec(3, 0)
        passage_vecs = [query_vec]
        items = [{"title": "Paper with no abstract"}]
        pq, pb = self._patch_embeds(query_vec, passage_vecs)
        with pq, pb:
            result = filter_by_relevance("query", items, threshold=0.3)
        assert len(result) == 1


# ── filter_by_relevance integration with mcp_server helpers ──────


class TestFilterByRelevanceInCollectContext:
    """Verify that filter_by_relevance is wired into the collect helpers."""

    def test_collect_papers_calls_filter(self):
        """collect_papers should invoke filter_by_relevance after dedup."""
        from intel_store.mcp_server import collect_papers

        fake_papers = [
            {
                "external_id": "ss:aaa",
                "arxiv_id": None,
                "title": "Secure Enclave Design",
                "abstract": "On-device secure computation.",
                "authors": ["Alice"],
                "year": 2026,
                "citation_count": 5,
                "venue": "IEEE S&P",
                "published_date": "2026-01-01",
                "url": "https://example.com",
                "reliability_tag": "A",
                "source": "semantic_scholar",
            }
        ]

        mock_repo = MagicMock()
        mock_repo._require_topic_id.return_value = None
        mock_repo.get_item_by_external_id.return_value = None
        mock_repo.upsert_items.return_value = [{"id": 1, "title": "Secure Enclave Design"}]
        mock_repo.batch_link_topic.return_value = None

        with (
            patch("intel_store.mcp_server._get_repo", return_value=mock_repo),
            patch(
                "intel_store.collectors.semantic_scholar.search_papers",
                return_value=fake_papers,
            ),
            patch(
                "intel_store.embeddings.filter_by_relevance",
                return_value=fake_papers,
            ) as mock_filter,
            patch("intel_store.embeddings.embed_passage", return_value=[0.0] * 1024),
        ):
            result = collect_papers(
                topic="secure-ai",
                query="secure enclave",
                relevance_threshold=0.25,
            )

        mock_filter.assert_called_once()
        call_kwargs = mock_filter.call_args
        assert call_kwargs.kwargs.get("threshold") == 0.25 or (
            len(call_kwargs.args) >= 1 and call_kwargs.args[0] == "secure enclave"
        )
        assert result["fetched"] == 1
        assert result["filtered_out"] == 0

    def test_collect_arxiv_calls_filter(self):
        """collect_arxiv should invoke filter_by_relevance after dedup."""
        from intel_store.mcp_server import collect_arxiv

        fake_papers = [
            {
                "external_id": "arxiv:2301.99999",
                "arxiv_id": "2301.99999",
                "title": "Lattice-Based Cryptography",
                "abstract": "A study of lattice schemes.",
                "authors": ["Bob"],
                "year": 2023,
                "citation_count": 0,
                "venue": "cs.CR",
                "published_date": "2023-01-30",
                "url": "https://arxiv.org/abs/2301.99999",
                "reliability_tag": "A",
                "source": "arxiv",
            }
        ]

        mock_repo = MagicMock()
        mock_repo._require_topic_id.return_value = None
        mock_repo.get_item_by_external_id.return_value = None
        mock_repo.upsert_items.return_value = [{"id": 2, "title": "Lattice-Based Cryptography"}]
        mock_repo.batch_link_topic.return_value = None

        with (
            patch("intel_store.mcp_server._get_repo", return_value=mock_repo),
            patch(
                "intel_store.collectors.arxiv.search_papers",
                return_value=fake_papers,
            ),
            patch(
                "intel_store.embeddings.filter_by_relevance",
                return_value=fake_papers,
            ) as mock_filter,
            patch("intel_store.embeddings.embed_passage", return_value=[0.0] * 1024),
        ):
            result = collect_arxiv(
                topic="ondevice-pqc",
                query="lattice cryptography",
                relevance_threshold=0.4,
            )

        mock_filter.assert_called_once()
        assert result["source"] == "arxiv"
        assert result["fetched"] == 1
        assert result["filtered_out"] == 0

    def test_filtered_items_not_stored(self):
        """Items removed by filter_by_relevance must not reach upsert_items."""
        from intel_store.mcp_server import collect_arxiv

        fake_papers = [
            {
                "external_id": "arxiv:9999.00001",
                "arxiv_id": "9999.00001",
                "title": "Galaxy Formation via Dark Matter",
                "abstract": "Astrophysics paper.",
                "authors": ["Astronomer"],
                "year": 2025,
                "citation_count": 0,
                "venue": "astro-ph.GA",
                "published_date": "2025-01-01",
                "url": "https://arxiv.org/abs/9999.00001",
                "reliability_tag": "A",
                "source": "arxiv",
            }
        ]

        mock_repo = MagicMock()
        mock_repo._require_topic_id.return_value = None
        mock_repo.get_item_by_external_id.return_value = None
        mock_repo.upsert_items.return_value = []
        mock_repo.batch_link_topic.return_value = None

        with (
            patch("intel_store.mcp_server._get_repo", return_value=mock_repo),
            patch(
                "intel_store.collectors.arxiv.search_papers",
                return_value=fake_papers,
            ),
            patch(
                "intel_store.embeddings.filter_by_relevance",
                return_value=[],  # all items filtered out
            ),
        ):
            result = collect_arxiv(
                topic="secure-ai",
                query="homomorphic encryption",
                relevance_threshold=0.3,
            )

        mock_repo.upsert_items.assert_called_once_with([])
        assert result["fetched"] == 1
        assert result["filtered_out"] == 1
        assert result["stored"] == 0
