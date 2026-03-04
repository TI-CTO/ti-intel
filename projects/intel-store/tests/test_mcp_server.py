"""Tests for intel_store MCP server tool registration and helpers."""

import pytest

from intel_store.mcp_server import _rrf_merge


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
        "collect_all",
        "get_intel_stats",
    }

    assert expected_tools.issubset(tool_names), f"Missing tools: {expected_tools - tool_names}"
