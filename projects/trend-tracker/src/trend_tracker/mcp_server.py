"""Trend Tracker MCP server — exposes news/trend tracking tools."""

from __future__ import annotations

import asyncio
import json

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

server = Server("trend-tracker")


def _get_repo():
    from trend_tracker.db.repository import TrendRepository

    return TrendRepository()


@server.list_tools()
async def list_tools() -> list[Tool]:
    """Register all trend-tracker MCP tools."""
    return [
        Tool(
            name="search_news",
            description=(
                "Search stored news items by topic, keyword, or date."
                " Returns recent news sorted by published date."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "Filter by topic name",
                    },
                    "keyword": {
                        "type": "string",
                        "description": "Search keyword in news titles",
                    },
                    "since": {
                        "type": "string",
                        "description": "Filter news from this date (YYYY-MM-DD)",
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of results (default 20)",
                        "default": 20,
                    },
                },
            },
        ),
        Tool(
            name="get_trend_timeline",
            description=(
                "Get chronological trend snapshots for a topic."
                " Shows how a topic evolved over time."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "Topic name to get timeline for",
                    },
                    "since": {
                        "type": "string",
                        "description": "Start date for timeline (YYYY-MM-DD)",
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of snapshots (default 30)",
                        "default": 30,
                    },
                },
                "required": ["topic"],
            },
        ),
        Tool(
            name="get_topic_summary",
            description="Get the latest snapshot and recent news count for a topic.",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "Topic name to summarize",
                    },
                },
                "required": ["topic"],
            },
        ),
        Tool(
            name="compare_snapshots",
            description=(
                "Compare two snapshots of a topic to detect changes"
                " (news count, sentiment, signals)."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "Topic name to compare",
                    },
                    "date_a": {
                        "type": "string",
                        "description": "Earlier date (YYYY-MM-DD)",
                    },
                    "date_b": {
                        "type": "string",
                        "description": "Later date (YYYY-MM-DD)",
                    },
                },
                "required": ["topic", "date_a", "date_b"],
            },
        ),
        Tool(
            name="upsert_news",
            description=("Store or update news items. Each item needs: title, source, url, topic."),
            inputSchema={
                "type": "object",
                "properties": {
                    "items": {
                        "type": "array",
                        "description": "List of news item objects",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {"type": "string"},
                                "source": {"type": "string"},
                                "url": {"type": "string"},
                                "topic": {"type": "string"},
                                "published_date": {"type": "string"},
                                "summary": {"type": "string"},
                                "reliability_tag": {
                                    "type": "string",
                                    "enum": ["A", "B", "C", "D"],
                                },
                                "keywords": {
                                    "type": "array",
                                    "items": {"type": "string"},
                                },
                            },
                            "required": ["title", "source", "url", "topic"],
                        },
                    },
                },
                "required": ["items"],
            },
        ),
        Tool(
            name="upsert_snapshot",
            description="Store a trend snapshot for a topic at a specific date.",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {"type": "string"},
                    "snapshot_date": {
                        "type": "string",
                        "description": "Date of snapshot (YYYY-MM-DD). Defaults to today.",
                    },
                    "summary": {"type": "string"},
                    "key_signals": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of key trend signals detected",
                    },
                    "news_count": {"type": "integer"},
                    "sentiment": {
                        "type": "string",
                        "enum": ["positive", "neutral", "negative", "mixed"],
                    },
                    "change_level": {
                        "type": "string",
                        "enum": ["none", "minor", "notable", "urgent"],
                    },
                },
                "required": ["topic", "summary"],
            },
        ),
        Tool(
            name="manage_watch_topics",
            description="Add, update, list, or remove monitored topics.",
            inputSchema={
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["list", "add", "update", "remove"],
                        "description": "Action to perform",
                    },
                    "topic": {
                        "type": "string",
                        "description": "Topic name (required for add/update/remove)",
                    },
                    "keywords": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Search keywords for the topic",
                    },
                    "frequency": {
                        "type": "string",
                        "enum": ["daily", "weekly", "monthly"],
                        "description": "Monitoring frequency",
                    },
                    "is_active": {
                        "type": "boolean",
                        "description": "Whether the topic is actively monitored",
                    },
                },
                "required": ["action"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Dispatch tool calls to repository methods."""
    try:
        result = _dispatch(name, arguments)
        return [
            TextContent(
                type="text",
                text=json.dumps(result, ensure_ascii=False, indent=2, default=str),
            )
        ]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e}")]


def _dispatch(name: str, args: dict) -> dict | list:
    """Route tool name to repository method."""
    repo = _get_repo()

    if name == "search_news":
        return repo.search_news(
            topic=args.get("topic"),
            keyword=args.get("keyword"),
            since=args.get("since"),
            limit=args.get("limit", 20),
        )

    if name == "get_trend_timeline":
        return repo.get_trend_timeline(
            args["topic"],
            since=args.get("since"),
            limit=args.get("limit", 30),
        )

    if name == "get_topic_summary":
        return repo.get_topic_summary(args["topic"])

    if name == "compare_snapshots":
        return repo.compare_snapshots(args["topic"], args["date_a"], args["date_b"])

    if name == "upsert_news":
        count = repo.upsert_news(args["items"])
        return {"upserted": count}

    if name == "upsert_snapshot":
        return repo.upsert_snapshot(args)

    if name == "manage_watch_topics":
        action = args["action"]
        if action == "list":
            return repo.get_watch_topics(active_only=args.get("is_active", True))
        if action == "add" or action == "update":
            topic_data = {k: v for k, v in args.items() if k != "action" and v is not None}
            return repo.upsert_watch_topic(topic_data)
        if action == "remove":
            deleted = repo.delete_watch_topic(args["topic"])
            return {"deleted": deleted, "topic": args["topic"]}

    return {"error": f"Unknown tool: {name}"}


async def main() -> None:
    """Run the MCP server over stdio."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )


if __name__ == "__main__":
    asyncio.run(main())
