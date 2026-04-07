"""Tests for trend_tracker.db.repository.

Covers TrendRepository methods with mocked Supabase client
and _parse_json_list utility function.
"""

from __future__ import annotations

import json
from unittest.mock import MagicMock

import pytest

from trend_tracker.db.repository import _parse_json_list


# ── _parse_json_list ──────────────────────────────────────


def test_parse_json_list_from_string():
    assert _parse_json_list('["a", "b", "c"]') == ["a", "b", "c"]


def test_parse_json_list_from_list():
    assert _parse_json_list(["x", "y"]) == ["x", "y"]


def test_parse_json_list_empty_string():
    assert _parse_json_list("[]") == []


def test_parse_json_list_invalid_json():
    assert _parse_json_list("not json") == []


def test_parse_json_list_none():
    assert _parse_json_list(None) == []


# ── _resolve_topic_id / _require_topic_id ─────────────────


def test_resolve_topic_id_found(repo, mock_client):
    chain = mock_client.table("topics").select("id").eq("slug", "ai").limit(1)
    chain.execute.return_value = MagicMock(data=[{"id": 42}])

    result = repo._resolve_topic_id("ai")
    assert result == 42


def test_resolve_topic_id_not_found(repo, mock_client):
    chain = mock_client.table("topics").select("id").eq("slug", "nope").limit(1)
    chain.execute.return_value = MagicMock(data=[])

    result = repo._resolve_topic_id("nope")
    assert result is None


def test_require_topic_id_raises_on_not_found(repo, mock_client):
    chain = mock_client.table("topics").select("id").eq("slug", "nope").limit(1)
    chain.execute.return_value = MagicMock(data=[])

    with pytest.raises(ValueError, match="Topic not found"):
        repo._require_topic_id("nope")


# ── search_news ───────────────────────────────────────────


def test_search_news_no_filters(repo, mock_client):
    items = [{"id": 1, "title": "Test"}]
    chain = mock_client.table("news_items").select("*")
    chain.order.return_value.limit.return_value.execute.return_value = MagicMock(data=items)

    result = repo.search_news()
    assert result == items


def test_search_news_topic_not_found_returns_empty(repo, mock_client):
    # topic resolution returns empty
    topic_chain = mock_client.table("topics").select("id").eq("slug", "nope").limit(1)
    topic_chain.execute.return_value = MagicMock(data=[])

    result = repo.search_news(topic="nope")
    assert result == []


# ── upsert_news ───────────────────────────────────────────


def test_upsert_news_empty_list(repo):
    assert repo.upsert_news([]) == 0


def test_upsert_news_encodes_keywords(repo, mock_client):
    items = [{"title": "Test", "url": "http://x", "keywords": ["a", "b"]}]
    chain = mock_client.table("news_items").upsert(items, on_conflict="url")
    chain.execute.return_value = MagicMock(data=items)

    result = repo.upsert_news(items)
    assert result == 1
    # keywords should be JSON-encoded
    assert items[0]["keywords"] == json.dumps(["a", "b"], ensure_ascii=False)


# ── get_trend_timeline ────────────────────────────────────


def test_get_trend_timeline_success(repo, mock_client):
    # topic resolution
    topic_chain = mock_client.table("topics").select("id").eq("slug", "ai").limit(1)
    topic_chain.execute.return_value = MagicMock(data=[{"id": 10}])
    # snapshot query
    snap_chain = mock_client.table("trend_snapshots").select("*").eq("topic_id", 10)
    snap_chain.order.return_value.limit.return_value.execute.return_value = MagicMock(
        data=[{"snapshot_date": "2026-04-01", "summary": "test"}]
    )

    result = repo.get_trend_timeline("ai")
    assert len(result) == 1


# ── get_latest_snapshot ───────────────────────────────────


def test_get_latest_snapshot_not_found(repo, mock_client):
    topic_chain = mock_client.table("topics").select("id").eq("slug", "nope").limit(1)
    topic_chain.execute.return_value = MagicMock(data=[])

    assert repo.get_latest_snapshot("nope") is None


# ── upsert_snapshot ───────────────────────────────────────


def test_upsert_snapshot_encodes_key_signals(repo, mock_client):
    snapshot = {"topic_id": 1, "key_signals": ["signal-a", "signal-b"], "summary": "test"}
    chain = mock_client.table("trend_snapshots").upsert(
        snapshot, on_conflict="topic_id,snapshot_date,source_type"
    )
    chain.execute.return_value = MagicMock(data=[snapshot])

    result = repo.upsert_snapshot(snapshot)
    assert result == snapshot
    assert snapshot["key_signals"] == json.dumps(["signal-a", "signal-b"], ensure_ascii=False)


def test_upsert_snapshot_string_signals_untouched(repo, mock_client):
    snapshot = {"topic_id": 1, "key_signals": '["already-json"]', "summary": "test"}
    chain = mock_client.table("trend_snapshots").upsert(
        snapshot, on_conflict="topic_id,snapshot_date,source_type"
    )
    chain.execute.return_value = MagicMock(data=[snapshot])

    repo.upsert_snapshot(snapshot)
    # string should not be double-encoded
    assert snapshot["key_signals"] == '["already-json"]'


# ── compare_snapshots ─────────────────────────────────────


def test_compare_snapshots_topic_not_found(repo, mock_client):
    topic_chain = mock_client.table("topics").select("id").eq("slug", "nope").limit(1)
    topic_chain.execute.return_value = MagicMock(data=[])

    result = repo.compare_snapshots("nope", "2026-01-01", "2026-01-08")
    assert result["error"] == "Topic not found: 'nope'"
    assert result["changes"] == []


# ── watch_topics ──────────────────────────────────────────


def test_get_watch_topics(repo, mock_client):
    data = [{"topic_id": 1, "is_active": True}]
    chain = mock_client.table("watch_topics").select("*, topics(slug, display_name)")
    chain.eq.return_value.order.return_value.execute.return_value = MagicMock(data=data)

    result = repo.get_watch_topics()
    assert result == data


def test_upsert_watch_topic_encodes_keywords(repo, mock_client):
    topic_data = {"topic_id": 1, "keywords": ["kw1", "kw2"]}
    chain = mock_client.table("watch_topics").upsert(topic_data, on_conflict="topic_id")
    chain.execute.return_value = MagicMock(data=[topic_data])

    result = repo.upsert_watch_topic(topic_data)
    assert result == topic_data
    assert topic_data["keywords"] == json.dumps(["kw1", "kw2"], ensure_ascii=False)


def test_delete_watch_topic_not_found(repo, mock_client):
    topic_chain = mock_client.table("topics").select("id").eq("slug", "nope").limit(1)
    topic_chain.execute.return_value = MagicMock(data=[])

    assert repo.delete_watch_topic("nope") is False


def test_get_topic_summary_not_found(repo, mock_client):
    topic_chain = mock_client.table("topics").select("id").eq("slug", "nope").limit(1)
    topic_chain.execute.return_value = MagicMock(data=[])

    result = repo.get_topic_summary("nope")
    assert result["error"] == "Topic not found: 'nope'"
    assert result["recent_news_count"] == 0
