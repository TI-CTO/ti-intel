"""Trend Tracker MCP server — exposes news/trend tracking tools via FastMCP."""

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


# ── search & read tools ──────────────────────────────────────


@mcp.tool()
def search_news(
    topic: str | None = None,
    keyword: str | None = None,
    since: str | None = None,
    limit: int = 20,
) -> list[dict]:
    """Search stored news items by topic, keyword, or date.

    Args:
        topic: Filter by topic slug (e.g. 'ai-network').
        keyword: Search keyword in news titles.
        since: Filter news from this date (YYYY-MM-DD).
        limit: Maximum number of results (default 20).

    Returns:
        List of matching news items sorted by published date descending.
    """
    return _get_repo().search_news(topic=topic, keyword=keyword, since=since, limit=limit)


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
def upsert_news(items: list[dict]) -> dict:
    """Store or update news items in the database.

    Args:
        items: List of news item objects. Each needs: title, source, url, topic.

    Returns:
        Dict with upserted count.
    """
    count = _get_repo().upsert_news(items)
    return {"upserted": count}


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


# ── collect_news: external API collection ─────────────────────


@mcp.tool()
def collect_news(
    topic: str,
    query: str,
    since_days: int = 7,
    limit: int = 20,
    source: str = "all",
) -> dict:
    """Collect news from external APIs (Tavily, GDELT) and store in DB.

    Args:
        topic: Topic slug to associate collected news with (e.g. 'quantum-comm').
        query: Search query string (e.g. '양자암호 통신사').
        since_days: Look back this many days (default 7).
        limit: Max results per source (default 20).
        source: Which collector to use: 'tavily', 'gdelt', or 'all' (default).

    Returns:
        Dict with collection results per source and total stored count.
    """
    from trend_tracker.collectors import tavily, gdelt
    from trend_tracker.collectors.tavily import QuotaExhaustedError

    repo = _get_repo()
    topic_id = repo._require_topic_id(topic)

    results: dict = {"topic": topic, "query": query, "sources": {}}
    all_items: list[dict] = []
    tavily_quota_hit = False

    if source in ("tavily", "all"):
        try:
            tavily_items = tavily.collect(query, since_days=since_days, limit=limit)
            results["sources"]["tavily"] = {"fetched": len(tavily_items)}
            all_items.extend(tavily_items)
        except QuotaExhaustedError:
            tavily_quota_hit = True
            results["sources"]["tavily"] = {"fetched": 0, "error": "quota_exhausted"}
            if source == "tavily":
                # Tavily-only request but quota hit → auto-fallback to GDELT
                source = "gdelt"
                results["fallback"] = "tavily quota exhausted, falling back to gdelt"

    if source in ("gdelt", "all") or tavily_quota_hit:
        gdelt_items = gdelt.collect(query, since_days=since_days, limit=limit)
        results["sources"]["gdelt"] = {"fetched": len(gdelt_items)}
        all_items.extend(gdelt_items)

    # Deduplicate by URL
    seen_urls: set[str] = set()
    unique_items: list[dict] = []
    for item in all_items:
        url = item.get("url", "")
        if url and url not in seen_urls:
            seen_urls.add(url)
            item["topic_id"] = topic_id
            unique_items.append(item)

    stored = 0
    if unique_items:
        stored = repo.upsert_news(unique_items)

    results["total_fetched"] = len(all_items)
    results["unique_items"] = len(unique_items)
    results["stored"] = stored
    return results


if __name__ == "__main__":
    mcp.run()
