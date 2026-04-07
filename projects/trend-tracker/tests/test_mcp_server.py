"""Tests for MCP server tool registration and invocation."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from trend_tracker.mcp_server import mcp


async def list_tools():
    return await mcp.list_tools()


# ── tool registration ─────────────────────────────────────


@pytest.mark.asyncio
async def test_list_tools_returns_five_tools():
    tools = await list_tools()
    assert len(tools) == 5


@pytest.mark.asyncio
async def test_tool_names():
    tools = await list_tools()
    names = {t.name for t in tools}
    expected = {
        "get_trend_timeline",
        "get_topic_summary",
        "compare_snapshots",
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


# ── tool invocation tests ─────────────────────────────────


def _make_mock_repo():
    """Create a mock TrendRepository."""
    repo = MagicMock()
    repo._require_topic_id.return_value = 42
    repo._resolve_topic_id.return_value = 42
    return repo


@patch("trend_tracker.mcp_server._get_repo")
def test_get_trend_timeline_calls_repo(mock_get_repo):
    from trend_tracker.mcp_server import get_trend_timeline

    repo = _make_mock_repo()
    repo.get_trend_timeline.return_value = [{"snapshot_date": "2026-04-01"}]
    mock_get_repo.return_value = repo

    result = get_trend_timeline("ai", since="2026-03-01", limit=10)
    repo.get_trend_timeline.assert_called_once_with("ai", since="2026-03-01", limit=10)
    assert len(result) == 1


@patch("trend_tracker.mcp_server._get_repo")
def test_get_topic_summary_calls_repo(mock_get_repo):
    from trend_tracker.mcp_server import get_topic_summary

    repo = _make_mock_repo()
    repo.get_topic_summary.return_value = {"topic": "ai", "latest_snapshot": None}
    mock_get_repo.return_value = repo

    result = get_topic_summary("ai")
    repo.get_topic_summary.assert_called_once_with("ai")
    assert result["topic"] == "ai"


@patch("trend_tracker.mcp_server._get_repo")
def test_compare_snapshots_calls_repo(mock_get_repo):
    from trend_tracker.mcp_server import compare_snapshots

    repo = _make_mock_repo()
    repo.compare_snapshots.return_value = {"changes": ["count +5"]}
    mock_get_repo.return_value = repo

    result = compare_snapshots("ai", "2026-03-01", "2026-03-08")
    repo.compare_snapshots.assert_called_once_with("ai", "2026-03-01", "2026-03-08")
    assert result["changes"] == ["count +5"]


@patch("trend_tracker.mcp_server._get_repo")
def test_upsert_snapshot_maps_news_count_to_item_count(mock_get_repo):
    from trend_tracker.mcp_server import upsert_snapshot

    repo = _make_mock_repo()
    repo.upsert_snapshot.return_value = {"topic_id": 42, "item_count": 15}
    mock_get_repo.return_value = repo

    result = upsert_snapshot("ai", summary="test", news_count=15, sentiment="positive")
    call_data = repo.upsert_snapshot.call_args[0][0]
    assert call_data["item_count"] == 15
    assert "news_count" not in call_data
    assert call_data["sentiment"] == "positive"


@patch("trend_tracker.mcp_server._get_repo")
def test_upsert_snapshot_topic_not_found_raises(mock_get_repo):
    from trend_tracker.mcp_server import upsert_snapshot

    repo = _make_mock_repo()
    repo._require_topic_id.side_effect = ValueError("Topic not found: 'nope'")
    mock_get_repo.return_value = repo

    with pytest.raises(ValueError, match="Topic not found"):
        upsert_snapshot("nope", summary="test")


@patch("trend_tracker.mcp_server._get_repo")
def test_manage_watch_topics_list(mock_get_repo):
    from trend_tracker.mcp_server import manage_watch_topics

    repo = _make_mock_repo()
    repo.get_watch_topics.return_value = [{"topic_id": 1}]
    mock_get_repo.return_value = repo

    result = manage_watch_topics(action="list")
    repo.get_watch_topics.assert_called_once_with(active_only=True)
    assert result == [{"topic_id": 1}]


@patch("trend_tracker.mcp_server._get_repo")
def test_manage_watch_topics_add(mock_get_repo):
    from trend_tracker.mcp_server import manage_watch_topics

    repo = _make_mock_repo()
    repo.upsert_watch_topic.return_value = {"topic_id": 42}
    mock_get_repo.return_value = repo

    result = manage_watch_topics(action="add", topic="ai", keywords=["llm"], frequency="daily")
    call_data = repo.upsert_watch_topic.call_args[0][0]
    assert call_data["topic_id"] == 42
    assert call_data["keywords"] == ["llm"]
    assert call_data["frequency"] == "daily"


@patch("trend_tracker.mcp_server._get_repo")
def test_manage_watch_topics_remove(mock_get_repo):
    from trend_tracker.mcp_server import manage_watch_topics

    repo = _make_mock_repo()
    repo.delete_watch_topic.return_value = True
    mock_get_repo.return_value = repo

    result = manage_watch_topics(action="remove", topic="ai")
    assert result == {"deleted": True, "topic": "ai"}


@patch("trend_tracker.mcp_server._get_repo")
def test_manage_watch_topics_remove_no_topic(mock_get_repo):
    from trend_tracker.mcp_server import manage_watch_topics

    mock_get_repo.return_value = _make_mock_repo()
    result = manage_watch_topics(action="remove")
    assert "error" in result


@patch("trend_tracker.mcp_server._get_repo")
def test_manage_watch_topics_unknown_action(mock_get_repo):
    from trend_tracker.mcp_server import manage_watch_topics

    mock_get_repo.return_value = _make_mock_repo()
    result = manage_watch_topics(action="invalid")
    assert "error" in result
    assert "Unknown action" in result["error"]
