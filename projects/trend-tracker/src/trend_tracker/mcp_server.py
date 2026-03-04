"""Trend Tracker MCP server — snapshot comparison and watch topic management.

NOTE: News search, upsert, and collection have moved to intel-store.
This server retains only snapshot/timeline and watch_topics tools.
"""

from __future__ import annotations

import logging
import sys

from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.WARNING, stream=sys.stderr)
logger = logging.getLogger(__name__)

mcp = FastMCP("trend-tracker")


def _get_repo():
    from trend_tracker.db.repository import TrendRepository

    return TrendRepository()


# ── snapshot & timeline tools ────────────────────────────────────


@mcp.tool()
def get_trend_timeline(
    topic: str,
    since: str | None = None,
    limit: int = 30,
) -> list[dict]:
    """Get chronological trend snapshots for a topic.

    Args:
        topic: Topic slug to get timeline for.
        since: Start date for timeline (YYYY-MM-DD).
        limit: Maximum number of snapshots (default 30).

    Returns:
        List of trend snapshots showing how a topic evolved over time.
    """
    return _get_repo().get_trend_timeline(topic, since=since, limit=limit)


@mcp.tool()
def get_topic_summary(topic: str) -> dict:
    """Get the latest snapshot and recent news count for a topic.

    Args:
        topic: Topic slug to summarize.

    Returns:
        Dict with latest_snapshot and recent_news_count.
    """
    return _get_repo().get_topic_summary(topic)


@mcp.tool()
def compare_snapshots(topic: str, date_a: str, date_b: str) -> dict:
    """Compare two snapshots of a topic to detect changes.

    Args:
        topic: Topic slug to compare.
        date_a: Earlier date (YYYY-MM-DD).
        date_b: Later date (YYYY-MM-DD).

    Returns:
        Dict with old_snapshot, new_snapshot, and detected changes.
    """
    return _get_repo().compare_snapshots(topic, date_a, date_b)


# ── write tools ──────────────────────────────────────────────


@mcp.tool()
def upsert_snapshot(
    topic: str,
    summary: str,
    snapshot_date: str | None = None,
    key_signals: list[str] | None = None,
    news_count: int | None = None,
    sentiment: str | None = None,
    change_level: str | None = None,
) -> dict:
    """Store a trend snapshot for a topic at a specific date.

    Args:
        topic: Topic slug.
        summary: Snapshot summary text.
        snapshot_date: Date of snapshot (YYYY-MM-DD). Defaults to today.
        key_signals: List of key trend signals detected.
        news_count: Number of news items in this period.
        sentiment: One of: positive, neutral, negative, mixed.
        change_level: One of: none, minor, notable, urgent.

    Returns:
        The upserted snapshot record.
    """
    data: dict = {"topic": topic, "summary": summary}
    if snapshot_date:
        data["snapshot_date"] = snapshot_date
    if key_signals is not None:
        data["key_signals"] = key_signals
    if news_count is not None:
        data["news_count"] = news_count
    if sentiment:
        data["sentiment"] = sentiment
    if change_level:
        data["change_level"] = change_level
    return _get_repo().upsert_snapshot(data)


@mcp.tool()
def manage_watch_topics(
    action: str,
    topic: str | None = None,
    keywords: list[str] | None = None,
    frequency: str | None = None,
    is_active: bool | None = None,
) -> dict | list:
    """Add, update, list, or remove monitored topics.

    Args:
        action: One of: list, add, update, remove.
        topic: Topic slug (required for add/update/remove).
        keywords: Search keywords for the topic.
        frequency: Monitoring frequency: daily, weekly, or monthly.
        is_active: Whether the topic is actively monitored.

    Returns:
        List of topics (for list action) or the modified topic record.
    """
    repo = _get_repo()
    if action == "list":
        return repo.get_watch_topics(active_only=is_active if is_active is not None else True)
    if action in ("add", "update"):
        topic_data: dict = {}
        if topic:
            topic_data["topic"] = topic
        if keywords:
            topic_data["keywords"] = keywords
        if frequency:
            topic_data["frequency"] = frequency
        if is_active is not None:
            topic_data["is_active"] = is_active
        return repo.upsert_watch_topic(topic_data)
    if action == "remove":
        if not topic:
            return {"error": "topic is required for remove action"}
        deleted = repo.delete_watch_topic(topic)
        return {"deleted": deleted, "topic": topic}
    return {"error": f"Unknown action: {action}"}


if __name__ == "__main__":
    mcp.run()
