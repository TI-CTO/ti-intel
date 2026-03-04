"""Tests for intel_store MCP server tool registration."""

import pytest


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
        "get_intel_stats",
    }

    assert expected_tools.issubset(tool_names), f"Missing tools: {expected_tools - tool_names}"
