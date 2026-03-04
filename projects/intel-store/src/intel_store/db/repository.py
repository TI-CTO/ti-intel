"""Data access layer for the unified intel_items table."""

from __future__ import annotations

import json
import logging
from datetime import date, timedelta

from supabase import Client

from intel_store.db.client import get_client
from intel_store.models import IntelItem

logger = logging.getLogger(__name__)


class IntelRepository:
    """Supabase queries for intel_items, intel_item_topics, intel_item_relations."""

    def __init__(self) -> None:
        self._client: Client = get_client()

    # ── topic helpers ────────────────────────────────────────

    def _resolve_topic_id(self, slug: str) -> int | None:
        """Resolve a topic slug to its integer PK."""
        result = self._client.table("topics").select("id").eq("slug", slug).limit(1).execute()
        return result.data[0]["id"] if result.data else None

    def _require_topic_id(self, slug: str) -> int:
        """Resolve a topic slug to its integer PK. Raises ValueError if not found."""
        topic_id = self._resolve_topic_id(slug)
        if topic_id is None:
            raise ValueError(
                f"Topic not found: '{slug}'. Register it first via manage_watch_topics."
            )
        return topic_id

    # ── upsert ───────────────────────────────────────────────

    def upsert_items(self, items: list[IntelItem]) -> list[dict]:
        """Insert or update intel items with content_hash deduplication.

        Args:
            items: List of IntelItem models to upsert.

        Returns:
            List of upserted row dicts.
        """
        if not items:
            return []

        results = []
        for item in items:
            item.ensure_content_hash()
            existing = self._find_by_content_hash(item.content_hash)
            if existing:
                logger.debug("Skipping duplicate (content_hash): %s", item.title[:60])
                results.append(existing)
                continue

            row = self._item_to_row(item)
            result = (
                self._client.table("intel_items")
                .upsert(row, on_conflict="item_type,source_name,external_id")
                .execute()
            )
            if result.data:
                results.append(result.data[0])
        return results

    def _find_by_content_hash(self, content_hash: str) -> dict | None:
        """Check if an item with this content_hash already exists."""
        result = (
            self._client.table("intel_items")
            .select("id, title, item_type")
            .eq("content_hash", content_hash)
            .limit(1)
            .execute()
        )
        return result.data[0] if result.data else None

    @staticmethod
    def _item_to_row(item: IntelItem) -> dict:
        """Convert an IntelItem to a dict suitable for Supabase upsert."""
        item_type = getattr(item.item_type, "value", item.item_type)
        lang = getattr(item.language, "value", item.language)
        rel = getattr(item.reliability, "value", item.reliability)
        meta = (
            json.dumps(item.metadata, ensure_ascii=False)
            if isinstance(item.metadata, dict)
            else item.metadata
        )
        row = {
            "item_type": item_type,
            "external_id": item.external_id,
            "content_hash": item.content_hash,
            "title": item.title,
            "abstract": item.abstract,
            "source_name": item.source_name,
            "source_url": item.source_url,
            "published_date": (item.published_date.isoformat() if item.published_date else None),
            "collected_date": item.collected_date.isoformat(),
            "language": lang,
            "reliability": rel,
            "metadata": meta,
        }
        if item.embedding is not None:
            row["embedding"] = item.embedding
        return row

    # ── get / detail ─────────────────────────────────────────

    def get_item(self, item_id: int) -> dict | None:
        """Get a single item by ID."""
        result = self._client.table("intel_items").select("*").eq("id", item_id).limit(1).execute()
        return result.data[0] if result.data else None

    def get_item_by_external_id(self, external_id: str) -> dict | None:
        """Get a single item by external_id."""
        result = (
            self._client.table("intel_items")
            .select("*")
            .eq("external_id", external_id)
            .limit(1)
            .execute()
        )
        return result.data[0] if result.data else None

    # ── keyword search ───────────────────────────────────────

    def search_keyword(
        self,
        keyword: str,
        *,
        types: list[str] | None = None,
        topic: str | None = None,
        since: str | None = None,
        limit: int = 20,
    ) -> list[dict]:
        """Search items by keyword (title ilike).

        Args:
            keyword: Search term for title matching.
            types: Filter by item_type (e.g. ["news", "paper"]).
            topic: Filter by topic slug.
            since: Filter by published_date >= since (YYYY-MM-DD).
            limit: Maximum results.

        Returns:
            List of matching item dicts.
        """
        query = self._client.table("intel_items").select("*")

        if keyword:
            query = query.ilike("title", f"%{keyword}%")
        if types:
            query = query.in_("item_type", types)
        if topic:
            topic_id = self._resolve_topic_id(topic)
            if topic_id is None:
                return []
            item_ids = self._get_item_ids_for_topic(topic_id)
            if not item_ids:
                return []
            query = query.in_("id", item_ids)
        if since:
            query = query.gte("published_date", since)

        return query.order("published_date", desc=True).limit(limit).execute().data

    def search_fulltext(
        self,
        query_text: str,
        *,
        types: list[str] | None = None,
        topic: str | None = None,
        since: str | None = None,
        limit: int = 20,
    ) -> list[dict]:
        """Full-text search using tsvector (plainto_tsquery).

        Args:
            query_text: Search query for full-text matching.
            types: Filter by item_type.
            topic: Filter by topic slug.
            since: Filter by published_date >= since.
            limit: Maximum results.

        Returns:
            List of matching item dicts.
        """
        query = self._client.table("intel_items").select("*")
        if types:
            query = query.in_("item_type", types)
        if topic:
            topic_id = self._resolve_topic_id(topic)
            if topic_id is None:
                return []
            item_ids = self._get_item_ids_for_topic(topic_id)
            if not item_ids:
                return []
            query = query.in_("id", item_ids)
        if since:
            query = query.gte("published_date", since)

        query = query.order("published_date", desc=True).limit(limit)
        query = query.text_search(
            "search_text", query_text, options={"config": "simple", "type": "plain"}
        )
        return query.execute().data

    # ── semantic search (via RPC) ────────────────────────────

    def search_semantic(
        self,
        query_embedding: list[float],
        *,
        types: list[str] | None = None,
        topic: str | None = None,
        since: str | None = None,
        threshold: float = 0.7,
        limit: int = 20,
    ) -> list[dict]:
        """Semantic vector search using the search_intel_semantic RPC function.

        Args:
            query_embedding: 1024-dim query vector.
            types: Filter by item_type.
            topic: Filter by topic slug.
            since: Filter by published_date >= since.
            threshold: Minimum cosine similarity.
            limit: Maximum results.

        Returns:
            List of dicts with item fields + similarity score.
        """
        topic_id = None
        if topic:
            topic_id = self._resolve_topic_id(topic)

        params: dict = {
            "query_embedding": query_embedding,
            "match_threshold": threshold,
            "match_count": limit,
            "filter_types": types,
            "filter_topic_id": topic_id,
            "filter_since": since,
        }

        result = self._client.rpc("search_intel_semantic", params).execute()
        return result.data or []

    # ── find similar ─────────────────────────────────────────

    def find_similar(
        self,
        embedding: list[float],
        *,
        threshold: float = 0.8,
        limit: int = 10,
        exclude_id: int | None = None,
    ) -> list[dict]:
        """Find items with similar embeddings.

        Args:
            embedding: 1024-dim vector to compare against.
            threshold: Minimum cosine similarity.
            limit: Maximum results.
            exclude_id: Item ID to exclude from results (self-match).

        Returns:
            List of dicts with item fields + similarity score.
        """
        results = self.search_semantic(
            embedding,
            threshold=threshold,
            limit=limit + 1,
        )
        if exclude_id is not None:
            results = [r for r in results if r.get("id") != exclude_id]
        return results[:limit]

    # ── weekly diff ──────────────────────────────────────────

    def get_weekly_diff(
        self,
        topic: str,
        *,
        week_date: str | None = None,
        types: list[str] | None = None,
    ) -> dict:
        """Compare this week vs last week for a topic.

        Args:
            topic: Topic slug.
            week_date: Reference date (YYYY-MM-DD). Defaults to today.
            types: Filter by item_type.

        Returns:
            Dict with this_week items, last_week items, and counts.
        """
        topic_id = self._resolve_topic_id(topic)
        if topic_id is None:
            return {"error": f"Topic not found: '{topic}'", "this_week": [], "last_week": []}

        ref = date.fromisoformat(week_date) if week_date else date.today()
        this_week_start = ref - timedelta(days=ref.weekday())  # Monday
        last_week_start = this_week_start - timedelta(days=7)

        item_ids = self._get_item_ids_for_topic(topic_id)
        if not item_ids:
            return {
                "topic": topic,
                "this_week": [],
                "last_week": [],
                "this_week_count": 0,
                "last_week_count": 0,
            }

        cols = (
            "id, item_type, title, abstract, source_name, source_url,"
            " published_date, collected_date, reliability, metadata"
        )

        def _build_query():
            q = self._client.table("intel_items").select(cols).in_("id", item_ids)
            if types:
                q = q.in_("item_type", types)
            return q

        this_week = (
            _build_query()
            .gte("collected_date", this_week_start.isoformat())
            .lt("collected_date", (this_week_start + timedelta(days=7)).isoformat())
            .order("published_date", desc=True)
            .execute()
            .data
        )

        last_week = (
            _build_query()
            .gte("collected_date", last_week_start.isoformat())
            .lt("collected_date", this_week_start.isoformat())
            .order("published_date", desc=True)
            .execute()
            .data
        )

        return {
            "topic": topic,
            "this_week": this_week,
            "last_week": last_week,
            "this_week_count": len(this_week),
            "last_week_count": len(last_week),
        }

    # ── topic linking ────────────────────────────────────────

    def batch_link_topic(
        self,
        item_ids: list[int],
        topic_slug: str,
        *,
        assigned_by: str = "collector",
    ) -> int:
        """Link multiple items to a single topic in one DB call.

        Args:
            item_ids: List of intel_items.id values.
            topic_slug: Topic slug to link.
            assigned_by: How the link was created.

        Returns:
            Number of links created.
        """
        topic_id = self._require_topic_id(topic_slug)
        rows = [
            {"item_id": iid, "topic_id": topic_id, "assigned_by": assigned_by} for iid in item_ids
        ]
        result = (
            self._client.table("intel_item_topics")
            .upsert(rows, on_conflict="item_id,topic_id")
            .execute()
        )
        return len(result.data)

    def link_topics(
        self,
        item_id: int,
        topic_slugs: list[str],
        *,
        assigned_by: str = "collector",
    ) -> int:
        """Link an item to topics by slug.

        Args:
            item_id: The intel_items.id to link.
            topic_slugs: List of topic slugs.
            assigned_by: How the link was created.

        Returns:
            Number of links created.
        """
        rows = []
        for slug in topic_slugs:
            topic_id = self._resolve_topic_id(slug)
            if topic_id is None:
                logger.warning("Topic not found, skipping: %s", slug)
                continue
            rows.append(
                {
                    "item_id": item_id,
                    "topic_id": topic_id,
                    "assigned_by": assigned_by,
                }
            )

        if not rows:
            return 0

        result = (
            self._client.table("intel_item_topics")
            .upsert(rows, on_conflict="item_id,topic_id")
            .execute()
        )
        return len(result.data)

    # ── relation linking ─────────────────────────────────────

    def link_relation(
        self,
        source_id: int,
        target_id: int,
        relation_type: str,
        *,
        confidence: float = 1.0,
    ) -> dict:
        """Create a relation between two items.

        Args:
            source_id: Source item ID.
            target_id: Target item ID.
            relation_type: One of cites/mentions/same_event/updates/contradicts.
            confidence: Confidence score (0.0~1.0).

        Returns:
            The created relation dict.
        """
        row = {
            "source_id": source_id,
            "target_id": target_id,
            "relation_type": relation_type,
            "confidence": confidence,
        }
        result = (
            self._client.table("intel_item_relations")
            .upsert(row, on_conflict="source_id,target_id,relation_type")
            .execute()
        )
        return result.data[0] if result.data else {}

    # ── stats ────────────────────────────────────────────────

    def get_stats(
        self,
        *,
        topic: str | None = None,
        item_type: str | None = None,
        period_days: int = 30,
    ) -> dict:
        """Get aggregate statistics for items.

        Args:
            topic: Filter by topic slug.
            item_type: Filter by item_type.
            period_days: Look back this many days.

        Returns:
            Dict with total_count, by_type counts, recent_count.
        """
        since = (date.today() - timedelta(days=period_days)).isoformat()

        # Total count
        query = self._client.table("intel_items").select("id", count="exact")
        if item_type:
            query = query.eq("item_type", item_type)
        if topic:
            topic_id = self._resolve_topic_id(topic)
            if topic_id is None:
                return {"error": f"Topic not found: '{topic}'"}
            item_ids = self._get_item_ids_for_topic(topic_id)
            if item_ids:
                query = query.in_("id", item_ids)
            else:
                return {"total_count": 0, "recent_count": 0, "by_type": {}}
        total_result = query.execute()
        total_count = total_result.count or 0

        # Recent count
        recent_query = self._client.table("intel_items").select("id", count="exact")
        recent_query = recent_query.gte("collected_date", since)
        if item_type:
            recent_query = recent_query.eq("item_type", item_type)
        if topic:
            if item_ids:
                recent_query = recent_query.in_("id", item_ids)
        recent_result = recent_query.execute()
        recent_count = recent_result.count or 0

        return {
            "total_count": total_count,
            "recent_count": recent_count,
            "period_days": period_days,
        }

    # ── update embedding ─────────────────────────────────────

    def update_embedding(self, item_id: int, embedding: list[float]) -> bool:
        """Update the embedding vector for an item.

        Args:
            item_id: The intel_items.id.
            embedding: 1024-dim float vector.

        Returns:
            True if updated successfully.
        """
        result = (
            self._client.table("intel_items")
            .update({"embedding": embedding})
            .eq("id", item_id)
            .execute()
        )
        return len(result.data) > 0

    def get_items_without_embedding(self, *, limit: int = 100) -> list[dict]:
        """Get items that don't have embeddings yet.

        Args:
            limit: Maximum number of items to return.

        Returns:
            List of item dicts without embeddings.
        """
        result = (
            self._client.table("intel_items")
            .select("id, title, abstract, item_type")
            .is_("embedding", "null")
            .order("created_at", desc=False)
            .limit(limit)
            .execute()
        )
        return result.data

    # ── internal helpers ─────────────────────────────────────

    def _get_item_ids_for_topic(self, topic_id: int) -> list[int]:
        """Get all item IDs linked to a topic."""
        result = (
            self._client.table("intel_item_topics")
            .select("item_id")
            .eq("topic_id", topic_id)
            .execute()
        )
        return [r["item_id"] for r in result.data]
