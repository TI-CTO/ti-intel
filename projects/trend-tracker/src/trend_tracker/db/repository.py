"""Data access layer for trend tracking tables."""

from __future__ import annotations

import json
from datetime import date

from supabase import Client

from trend_tracker.db.client import get_client


class TrendRepository:
    """Supabase queries for news_items, trend_snapshots, and watch_topics."""

    def __init__(self) -> None:
        self._client: Client = get_client()

    # ── topic helpers ────────────────────────────────────────

    def _resolve_topic_id(self, slug: str) -> int | None:
        """Resolve a topic slug to its integer PK. Returns None if not found."""
        result = (
            self._client.table("topics")
            .select("id")
            .eq("slug", slug)
            .limit(1)
            .execute()
        )
        return result.data[0]["id"] if result.data else None

    def _require_topic_id(self, slug: str) -> int:
        """Resolve a topic slug to its integer PK. Raises ValueError if not found."""
        topic_id = self._resolve_topic_id(slug)
        if topic_id is None:
            raise ValueError(
                f"Topic not found: '{slug}'. Register it first via manage_watch_topics."
            )
        return topic_id

    # ── news_items ──────────────────────────────────────────

    def search_news(
        self,
        *,
        topic: str | None = None,
        keyword: str | None = None,
        since: str | None = None,
        limit: int = 20,
    ) -> list[dict]:
        """Search stored news items by topic, keyword, or date range."""
        query = self._client.table("news_items").select("*")
        if topic:
            topic_id = self._resolve_topic_id(topic)
            if topic_id is None:
                return []
            query = query.eq("topic_id", topic_id)
        if keyword:
            query = query.ilike("title", f"%{keyword}%")
        if since:
            query = query.gte("published_date", since)
        query = query.order("published_date", desc=True).limit(limit)
        return query.execute().data

    def upsert_news(self, items: list[dict]) -> int:
        """Insert or update news items. Returns count of upserted rows."""
        if not items:
            return 0
        for item in items:
            if "keywords" in item and isinstance(item["keywords"], list):
                item["keywords"] = json.dumps(item["keywords"], ensure_ascii=False)
        result = self._client.table("news_items").upsert(items, on_conflict="url").execute()
        return len(result.data)

    # ── trend_snapshots ─────────────────────────────────────

    def get_trend_timeline(
        self,
        topic: str,
        *,
        source_type: str | None = None,
        since: str | None = None,
        limit: int = 30,
    ) -> list[dict]:
        """Get chronological snapshots for a topic."""
        topic_id = self._require_topic_id(topic)
        query = self._client.table("trend_snapshots").select("*").eq("topic_id", topic_id)
        if source_type:
            query = query.eq("source_type", source_type)
        if since:
            query = query.gte("snapshot_date", since)
        query = query.order("snapshot_date", desc=True).limit(limit)
        return query.execute().data

    def get_latest_snapshot(self, topic: str, *, source_type: str = "news") -> dict | None:
        """Get the most recent snapshot for a topic."""
        topic_id = self._resolve_topic_id(topic)
        if topic_id is None:
            return None
        result = (
            self._client.table("trend_snapshots")
            .select("*")
            .eq("topic_id", topic_id)
            .eq("source_type", source_type)
            .order("snapshot_date", desc=True)
            .limit(1)
            .execute()
        )
        return result.data[0] if result.data else None

    def upsert_snapshot(self, snapshot: dict) -> dict:
        """Insert or update a trend snapshot."""
        if "key_signals" in snapshot and isinstance(snapshot["key_signals"], list):
            snapshot["key_signals"] = json.dumps(snapshot["key_signals"], ensure_ascii=False)
        result = (
            self._client.table("trend_snapshots")
            .upsert(snapshot, on_conflict="topic_id,snapshot_date,source_type")
            .execute()
        )
        return result.data[0] if result.data else {}

    def compare_snapshots(
        self,
        topic: str,
        date_a: str,
        date_b: str,
        *,
        source_type: str = "news",
    ) -> dict:
        """Compare two snapshots and return differences.

        Args:
            topic: The topic slug to compare.
            date_a: Earlier date (YYYY-MM-DD).
            date_b: Later date (YYYY-MM-DD).
            source_type: Snapshot source type to compare (news/papers/patents/combined).

        Returns:
            Dict with old_snapshot, new_snapshot, and detected changes.
        """
        topic_id = self._resolve_topic_id(topic)
        if topic_id is None:
            return {
                "topic": topic,
                "date_a": date_a,
                "date_b": date_b,
                "old_snapshot": None,
                "new_snapshot": None,
                "changes": [],
                "error": f"Topic not found: '{topic}'",
            }

        old = (
            self._client.table("trend_snapshots")
            .select("*")
            .eq("topic_id", topic_id)
            .eq("source_type", source_type)
            .eq("snapshot_date", date_a)
            .limit(1)
            .execute()
        )
        new = (
            self._client.table("trend_snapshots")
            .select("*")
            .eq("topic_id", topic_id)
            .eq("source_type", source_type)
            .eq("snapshot_date", date_b)
            .limit(1)
            .execute()
        )

        old_data = old.data[0] if old.data else None
        new_data = new.data[0] if new.data else None

        if not old_data or not new_data:
            return {
                "topic": topic,
                "date_a": date_a,
                "date_b": date_b,
                "old_snapshot": old_data,
                "new_snapshot": new_data,
                "changes": [],
                "error": "One or both snapshots not found",
            }

        changes = []

        old_count = old_data.get("item_count", 0)
        new_count = new_data.get("item_count", 0)
        if old_count != new_count:
            delta = new_count - old_count
            changes.append(
                f"Item count changed: {old_count} → {new_count} ({'+' if delta > 0 else ''}{delta})"
            )

        old_sentiment = old_data.get("sentiment", "")
        new_sentiment = new_data.get("sentiment", "")
        if old_sentiment != new_sentiment:
            changes.append(f"Sentiment shifted: {old_sentiment} → {new_sentiment}")

        old_signals = set(_parse_json_list(old_data.get("key_signals", "[]")))
        new_signals = set(_parse_json_list(new_data.get("key_signals", "[]")))
        added = new_signals - old_signals
        removed = old_signals - new_signals
        if added:
            changes.append(f"New signals: {', '.join(added)}")
        if removed:
            changes.append(f"Removed signals: {', '.join(removed)}")

        return {
            "topic": topic,
            "date_a": date_a,
            "date_b": date_b,
            "old_snapshot": old_data,
            "new_snapshot": new_data,
            "changes": changes,
        }

    # ── watch_topics ────────────────────────────────────────

    def get_watch_topics(self, *, active_only: bool = True) -> list[dict]:
        """List all monitored topics."""
        query = self._client.table("watch_topics").select("*, topics(slug, display_name)")
        if active_only:
            query = query.eq("is_active", True)
        return query.order("created_at", desc=False).execute().data

    def upsert_watch_topic(self, topic_data: dict) -> dict:
        """Add or update a watch topic."""
        if "keywords" in topic_data and isinstance(topic_data["keywords"], list):
            topic_data["keywords"] = json.dumps(topic_data["keywords"], ensure_ascii=False)
        result = (
            self._client.table("watch_topics")
            .upsert(topic_data, on_conflict="topic_id")
            .execute()
        )
        return result.data[0] if result.data else {}

    def delete_watch_topic(self, topic: str) -> bool:
        """Remove a watch topic by slug."""
        topic_id = self._resolve_topic_id(topic)
        if topic_id is None:
            return False
        result = self._client.table("watch_topics").delete().eq("topic_id", topic_id).execute()
        return len(result.data) > 0

    def get_topic_summary(self, topic: str) -> dict:
        """Get combined summary: latest snapshot + recent news count."""
        topic_id = self._resolve_topic_id(topic)
        if topic_id is None:
            return {
                "topic": topic,
                "latest_snapshot": None,
                "recent_news_count": 0,
                "error": f"Topic not found: '{topic}'",
            }
        snapshot = self.get_latest_snapshot(topic)
        today = date.today().isoformat()
        recent_news = (
            self._client.table("news_items")
            .select("id", count="exact")
            .eq("topic_id", topic_id)
            .gte("collected_date", today)
            .execute()
        )
        return {
            "topic": topic,
            "latest_snapshot": snapshot,
            "recent_news_count": recent_news.count or 0,
        }


def _parse_json_list(value: str | list) -> list:
    """Parse a JSON string to list, or return as-is if already a list."""
    if isinstance(value, list):
        return value
    try:
        return json.loads(value)
    except (json.JSONDecodeError, TypeError):
        return []
