"""Tavily Search API collector for AI-optimised news search."""

from __future__ import annotations

import logging
import time

import httpx

from trend_tracker.config import settings

logger = logging.getLogger(__name__)

_BASE_URL = "https://api.tavily.com"
_REQUEST_DELAY = 0.5  # seconds between requests


class QuotaExhaustedError(Exception):
    """Raised when Tavily monthly quota (free: 1,000 req/mo) is exhausted."""


def collect(
    query: str,
    *,
    since_days: int = 7,
    limit: int = 20,
) -> list[dict]:
    """Search Tavily and return normalised news dicts.

    Args:
        query: Search query string.
        since_days: Look back this many days from today.
        limit: Maximum number of results (max 20 per Tavily request).

    Returns:
        List of normalised news item dicts ready for DB upsert.

    Raises:
        QuotaExhaustedError: When monthly API quota is exceeded (HTTP 429).
    """
    api_key = settings.tavily_api_key
    if not api_key:
        logger.warning("TAVILY_API_KEY not set, skipping Tavily collection")
        return []

    limit = max(1, min(limit, 20))

    payload = {
        "api_key": api_key,
        "query": query,
        "max_results": limit,
        "search_depth": "advanced",
        "include_answer": False,
        "include_raw_content": False,
        "days": since_days,
    }

    try:
        with httpx.Client(timeout=30.0) as client:
            resp = client.post(f"{_BASE_URL}/search", json=payload)
            if resp.status_code == 429:
                logger.warning("Tavily quota exhausted (HTTP 429). Falling back to GDELT.")
                raise QuotaExhaustedError(
                    "Tavily monthly quota exceeded. Use GDELT as fallback."
                )
            resp.raise_for_status()
            data = resp.json()
    except QuotaExhaustedError:
        raise
    except httpx.HTTPStatusError as e:
        logger.error("Tavily API error: %s %s", e.response.status_code, e.response.text[:200])
        return []
    except httpx.RequestError as e:
        logger.error("Tavily request failed: %s", e)
        return []

    raw_results = data.get("results", [])
    items = [_normalise(r) for r in raw_results]
    items = [i for i in items if i is not None]

    time.sleep(_REQUEST_DELAY)
    return items


def _normalise(raw: dict) -> dict | None:
    """Convert a Tavily search result to our news item schema."""
    title = (raw.get("title") or "").strip()
    url = (raw.get("url") or "").strip()
    if not title or not url:
        return None

    published_date = raw.get("published_date")
    if published_date and len(published_date) >= 10:
        published_date = published_date[:10]
    else:
        published_date = None

    return {
        "title": title,
        "url": url,
        "source": _extract_domain(url),
        "published_date": published_date,
        "summary": (raw.get("content") or "")[:500].strip() or None,
        "reliability_tag": "B",
        "collector": "tavily",
    }


def _extract_domain(url: str) -> str:
    """Extract a readable domain name from a URL."""
    try:
        from urllib.parse import urlparse
        parsed = urlparse(url)
        domain = parsed.netloc
        if domain.startswith("www."):
            domain = domain[4:]
        return domain
    except Exception:
        return "unknown"
