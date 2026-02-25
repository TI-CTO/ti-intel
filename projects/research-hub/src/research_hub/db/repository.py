"""Data access layer for research-hub tables."""

from __future__ import annotations

import json
from datetime import date

from supabase import Client

from research_hub.db.client import get_client


class PaperRepository:
    """Supabase queries for papers, paper_topics, and paper_stats."""

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
                f"Topic not found: '{slug}'. Available topics can be listed via the topics table."
            )
        return topic_id

    # ── papers ───────────────────────────────────────────────

    def upsert_papers(self, papers: list[dict]) -> int:
        """Insert or update papers. Returns count of upserted rows."""
        if not papers:
            return 0
        for paper in papers:
            if "authors" in paper and isinstance(paper["authors"], list):
                paper["authors"] = json.dumps(paper["authors"], ensure_ascii=False)
        result = (
            self._client.table("papers")
            .upsert(papers, on_conflict="external_id")
            .execute()
        )
        return len(result.data)

    def link_paper_topic(self, paper_id: int, topic_id: int, relevance: float = 1.0) -> None:
        """Create or update a paper-topic association."""
        self._client.table("paper_topics").upsert(
            {"paper_id": paper_id, "topic_id": topic_id, "relevance": relevance},
            on_conflict="paper_id,topic_id",
        ).execute()

    def get_paper_by_external_id(self, external_id: str) -> dict | None:
        """Fetch a single paper by its external ID."""
        result = (
            self._client.table("papers")
            .select("*")
            .eq("external_id", external_id)
            .limit(1)
            .execute()
        )
        return result.data[0] if result.data else None

    def get_trending_papers(
        self,
        topic: str,
        *,
        since: str | None = None,
        limit: int = 20,
    ) -> list[dict]:
        """Get papers for a topic, sorted by citation count descending."""
        topic_id = self._require_topic_id(topic)
        query = (
            self._client.table("paper_topics")
            .select("papers(*)")
            .eq("topic_id", topic_id)
        )
        result = query.execute()
        papers = [row["papers"] for row in result.data if row.get("papers")]
        if since:
            papers = [
                p for p in papers
                if p.get("published_date") and p["published_date"] >= since
            ]
        papers.sort(key=lambda p: p.get("citation_count", 0), reverse=True)
        return papers[:limit]

    # ── paper_stats ──────────────────────────────────────────

    def get_paper_stats(
        self,
        topic: str,
        *,
        year: int | None = None,
        month: int | None = None,
    ) -> list[dict]:
        """Get monthly paper statistics for a topic."""
        topic_id = self._require_topic_id(topic)
        query = self._client.table("paper_stats").select("*").eq("topic_id", topic_id)
        if year:
            query = query.eq("stat_year", year)
        if month:
            query = query.eq("stat_month", month)
        return query.order("stat_year", desc=True).order("stat_month", desc=True).execute().data

    def update_paper_stats(self, topic: str, year: int, month: int) -> dict:
        """Recompute and upsert paper_stats for (topic, year, month)."""
        topic_id = self._require_topic_id(topic)
        # Pull papers for this topic published in this year/month
        result = (
            self._client.table("paper_topics")
            .select("papers(citation_count, published_date)")
            .eq("topic_id", topic_id)
            .execute()
        )
        month_str = f"{year}-{month:02d}"
        matching = [
            row["papers"]
            for row in result.data
            if row.get("papers")
            and row["papers"].get("published_date", "")[:7] == month_str
        ]
        paper_count = len(matching)
        avg_citations = (
            sum(p.get("citation_count", 0) for p in matching) / paper_count
            if paper_count > 0
            else 0.0
        )
        stats = {
            "topic_id": topic_id,
            "stat_year": year,
            "stat_month": month,
            "paper_count": paper_count,
            "avg_citations": round(avg_citations, 2),
        }
        upsert_result = (
            self._client.table("paper_stats")
            .upsert(stats, on_conflict="topic_id,stat_year,stat_month")
            .execute()
        )
        return upsert_result.data[0] if upsert_result.data else stats
