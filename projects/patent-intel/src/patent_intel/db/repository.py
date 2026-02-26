"""Data access layer for patent-intel tables."""

from __future__ import annotations

import calendar
import json
from collections import Counter

from supabase import Client

from patent_intel.db.client import get_client


class PatentRepository:
    """Supabase queries for patents, patent_topics, and patent_stats."""

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

    # ── patents ──────────────────────────────────────────────

    def upsert_patents(self, patents: list[dict]) -> int:
        """Insert or update patents. Returns count of upserted rows."""
        if not patents:
            return 0
        for patent in patents:
            if "ipc_codes" in patent and isinstance(patent["ipc_codes"], list):
                patent["ipc_codes"] = json.dumps(patent["ipc_codes"], ensure_ascii=False)
        result = (
            self._client.table("patents")
            .upsert(patents, on_conflict="external_id")
            .execute()
        )
        return len(result.data)

    def link_patent_topic(self, patent_id: int, topic_id: int, relevance: float = 1.0) -> None:
        """Create or update a patent-topic association."""
        self._client.table("patent_topics").upsert(
            {"patent_id": patent_id, "topic_id": topic_id, "relevance": relevance},
            on_conflict="patent_id,topic_id",
        ).execute()

    def get_patent_by_external_id(self, external_id: str) -> dict | None:
        """Fetch a single patent by its external ID."""
        result = (
            self._client.table("patents")
            .select("*")
            .eq("external_id", external_id)
            .limit(1)
            .execute()
        )
        return result.data[0] if result.data else None

    def get_recent_patents(
        self,
        topic: str,
        *,
        since: str | None = None,
        limit: int = 20,
    ) -> list[dict]:
        """Get patents for a topic, sorted by filing date descending."""
        topic_id = self._require_topic_id(topic)
        query = (
            self._client.table("patent_topics")
            .select("patents(*)")
            .eq("topic_id", topic_id)
        )
        result = query.execute()
        patents = [row["patents"] for row in result.data if row.get("patents")]
        if since:
            patents = [
                p for p in patents
                if p.get("filing_date") and p["filing_date"] >= since
            ]
        patents.sort(key=lambda p: p.get("filing_date") or "", reverse=True)
        return patents[:limit]

    # ── patent_stats ─────────────────────────────────────────

    def get_patent_stats(
        self,
        topic: str,
        *,
        year: int | None = None,
        quarter: int | None = None,
    ) -> list[dict]:
        """Get quarterly patent filing statistics for a topic."""
        topic_id = self._require_topic_id(topic)
        query = self._client.table("patent_stats").select("*").eq("topic_id", topic_id)
        if year:
            query = query.eq("stat_year", year)
        if quarter:
            query = query.eq("stat_quarter", quarter)
        return (
            query.order("stat_year", desc=True)
            .order("stat_quarter", desc=True)
            .execute()
            .data
        )

    def update_patent_stats(self, topic: str, year: int, quarter: int) -> dict:
        """Recompute and upsert patent_stats for (topic, year, quarter)."""
        topic_id = self._require_topic_id(topic)
        # Determine date range for the quarter
        q_start_month = (quarter - 1) * 3 + 1
        q_end_month = quarter * 3
        last_day = calendar.monthrange(year, q_end_month)[1]
        start_date = f"{year}-{q_start_month:02d}-01"
        end_date = f"{year}-{q_end_month:02d}-{last_day:02d}"

        result = (
            self._client.table("patent_topics")
            .select("patents(applicant, filing_date)")
            .eq("topic_id", topic_id)
            .execute()
        )
        matching = [
            row["patents"]
            for row in result.data
            if row.get("patents")
            and row["patents"].get("filing_date")
            and start_date <= row["patents"]["filing_date"] <= end_date
        ]

        filing_count = len(matching)
        applicant_counts = Counter(p["applicant"] for p in matching if p.get("applicant"))
        top_applicants = [name for name, _ in applicant_counts.most_common(5)]

        stats = {
            "topic_id": topic_id,
            "stat_year": year,
            "stat_quarter": quarter,
            "filing_count": filing_count,
            "top_applicants": json.dumps(top_applicants, ensure_ascii=False),
        }
        upsert_result = (
            self._client.table("patent_stats")
            .upsert(stats, on_conflict="topic_id,stat_year,stat_quarter")
            .execute()
        )
        return upsert_result.data[0] if upsert_result.data else stats
