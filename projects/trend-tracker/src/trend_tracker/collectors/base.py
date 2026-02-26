"""Base protocol for news collectors."""

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class NewsCollector(Protocol):
    """Protocol that all news collectors must implement."""

    source_name: str

    def collect(
        self,
        query: str,
        *,
        since_days: int = 7,
        limit: int = 20,
    ) -> list[dict]:
        """Collect news articles matching the query.

        Args:
            query: Search query string.
            since_days: Look back this many days from today.
            limit: Maximum number of results.

        Returns:
            List of normalised news item dicts with keys:
                - title: str
                - url: str
                - source: str (publication name)
                - published_date: str (YYYY-MM-DD) or None
                - summary: str or None
                - reliability_tag: str (A/B/C/D)
                - collector: str (e.g. 'tavily', 'gdelt')
        """
        ...
