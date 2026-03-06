"""Tests for intel_store MCP server tool registration and helpers."""

from unittest.mock import MagicMock

import pytest

from intel_store.mcp_server import _dedup_papers, _rrf_merge

# ── RRF merge tests ──────────────────────────────────────────────


class TestRRFMerge:
    def test_overlapping_items_ranked_higher(self):
        """Items appearing in both lists should get higher scores."""
        list_a = [{"id": 1, "title": "A"}, {"id": 2, "title": "B"}]
        list_b = [{"id": 2, "title": "B"}, {"id": 3, "title": "C"}]
        merged = _rrf_merge(list_a, list_b, limit=10)
        ids = [item["id"] for item in merged]
        # id=2 appears in both, should be ranked first
        assert ids[0] == 2
        assert set(ids) == {1, 2, 3}

    def test_respects_limit(self):
        """Result count should not exceed limit."""
        items = [{"id": i} for i in range(100)]
        merged = _rrf_merge(items, limit=5)
        assert len(merged) == 5

    def test_empty_lists(self):
        """Empty input lists should return empty result."""
        assert _rrf_merge([], [], limit=10) == []

    def test_skips_items_without_id(self):
        """Items without 'id' key should be skipped."""
        list_a = [{"id": 1}, {"title": "no id"}, {"id": 2}]
        merged = _rrf_merge(list_a, limit=10)
        ids = [item["id"] for item in merged]
        assert ids == [1, 2]

    def test_single_list_preserves_order(self):
        """Single list input should preserve original rank order."""
        items = [{"id": 10}, {"id": 20}, {"id": 30}]
        merged = _rrf_merge(items, limit=10)
        ids = [item["id"] for item in merged]
        assert ids == [10, 20, 30]


# ── Cross-source dedup tests ─────────────────────────────────────


class TestDedupPapers:
    def _mock_repo(self, existing_ids: dict[str, dict | None]):
        """Create a mock repo that returns existing items by external_id."""
        repo = MagicMock()
        repo.get_item_by_external_id.side_effect = lambda eid: existing_ids.get(eid)
        return repo

    def test_ss_paper_skipped_when_arxiv_exists(self):
        """SS paper with arxiv_id should be skipped if arXiv copy already in DB."""
        repo = self._mock_repo({"arxiv:2301.12345": {"id": 1, "title": "Paper"}})
        papers = [{"external_id": "ss:abc", "arxiv_id": "2301.12345", "title": "Paper"}]
        result = _dedup_papers(papers, repo)
        assert len(result) == 0

    def test_ss_paper_kept_when_no_arxiv_match(self):
        """SS paper should be kept when no arXiv copy exists."""
        repo = self._mock_repo({"arxiv:2301.12345": None})
        papers = [{"external_id": "ss:abc", "arxiv_id": "2301.12345", "title": "Paper"}]
        result = _dedup_papers(papers, repo)
        assert len(result) == 1

    def test_ss_paper_without_arxiv_id_kept(self):
        """SS paper without arxiv_id should always be kept."""
        repo = self._mock_repo({})
        papers = [{"external_id": "ss:abc", "arxiv_id": None, "title": "Paper"}]
        result = _dedup_papers(papers, repo)
        assert len(result) == 1

    def test_arxiv_paper_skipped_when_already_stored(self):
        """arXiv paper should be skipped if same external_id already in DB."""
        repo = self._mock_repo({"arxiv:2301.99999": {"id": 2, "title": "Existing"}})
        papers = [{"external_id": "arxiv:2301.99999", "title": "Paper"}]
        result = _dedup_papers(papers, repo)
        assert len(result) == 0

    def test_arxiv_paper_kept_when_new(self):
        """arXiv paper should be kept when not in DB."""
        repo = self._mock_repo({"arxiv:2301.99999": None})
        papers = [{"external_id": "arxiv:2301.99999", "title": "Paper"}]
        result = _dedup_papers(papers, repo)
        assert len(result) == 1

    def test_mixed_batch(self):
        """Batch with both duplicates and new papers filters correctly."""
        repo = self._mock_repo(
            {
                "arxiv:111": {"id": 1},  # exists
                "arxiv:222": None,  # doesn't exist
            }
        )
        papers = [
            {"external_id": "ss:a", "arxiv_id": "111", "title": "Dup"},
            {"external_id": "ss:b", "arxiv_id": "222", "title": "New SS"},
            {"external_id": "ss:c", "arxiv_id": None, "title": "No arXiv"},
        ]
        result = _dedup_papers(papers, repo)
        assert len(result) == 2
        assert result[0]["title"] == "New SS"
        assert result[1]["title"] == "No arXiv"


# ── Tool registration test ───────────────────────────────────────


@pytest.mark.asyncio
async def test_mcp_tools_registered():
    """Verify all expected MCP tools are registered."""
    from intel_store.mcp_server import mcp

    tools = await mcp.list_tools()
    tool_names = {t.name for t in tools}

    expected_tools = {
        "search_intel",
        "find_similar",
        "get_weekly_diff",
        "upsert_items",
        "get_item_detail",
        "link_topics",
        "link_relation",
        "collect_papers",
        "collect_patents",
        "collect_news",
        "collect_arxiv",
        "collect_all",
        "get_intel_stats",
    }

    assert expected_tools.issubset(tool_names), f"Missing tools: {expected_tools - tool_names}"
