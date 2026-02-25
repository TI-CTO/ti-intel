"""Tests for MCP server tool registration."""

import pytest

from trend_tracker.mcp_server import list_tools


@pytest.mark.asyncio
async def test_list_tools_returns_seven_tools():
    tools = await list_tools()
    assert len(tools) == 7


@pytest.mark.asyncio
async def test_tool_names():
    tools = await list_tools()
    names = {t.name for t in tools}
    expected = {
        "search_news",
        "get_trend_timeline",
        "get_topic_summary",
        "compare_snapshots",
        "upsert_news",
        "upsert_snapshot",
        "manage_watch_topics",
    }
    assert names == expected


@pytest.mark.asyncio
async def test_all_tools_have_input_schema():
    tools = await list_tools()
    for tool in tools:
        assert tool.inputSchema is not None
        assert tool.inputSchema["type"] == "object"


@pytest.mark.asyncio
async def test_required_fields_present():
    tools = await list_tools()
    tool_map = {t.name: t for t in tools}

    assert "topic" in tool_map["get_trend_timeline"].inputSchema.get("required", [])
    assert "topic" in tool_map["get_topic_summary"].inputSchema.get("required", [])
    assert "action" in tool_map["manage_watch_topics"].inputSchema.get("required", [])

    compare_required = tool_map["compare_snapshots"].inputSchema.get("required", [])
    assert "topic" in compare_required
    assert "date_a" in compare_required
    assert "date_b" in compare_required
