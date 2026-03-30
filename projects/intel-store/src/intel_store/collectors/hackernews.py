"""HackerNews Algolia API collector for community signals."""

from __future__ import annotations

import logging
import time
from datetime import datetime, timedelta, timezone

import httpx

logger = logging.getLogger(__name__)

_BASE_URL = "https://hn.algolia.com/api/v1"
_REQUEST_DELAY = 0.5  # 10,000 req/hour
_ENGAGEMENT_THRESHOLD = 100  # points >= 100 → reliability B


def collect(
    query: str,
    *,
    since_days: int = 7,
    limit: int = 25,
) -> list[dict]:
    """Search HackerNews and return normalised community signal dicts.

    Args:
        query: Search query string.
        since_days: Look back this many days.
        limit: Maximum number of results (max 1000).

    Returns:
        List of normalised community item dicts.
    """
    limit = max(1, min(limit, 1000))
    since_ts = int((datetime.now(tz=timezone.utc) - timedelta(days=since_days)).timestamp())

    params = {
        "query": query,
        "tags": "story",
        "numericFilters": f"created_at_i>{since_ts}",
        "hitsPerPage": limit,
    }

    try:
        with httpx.Client(timeout=30.0) as client:
            resp = client.get(f"{_BASE_URL}/search", params=params)
            resp.raise_for_status()
            data = resp.json()
    except httpx.HTTPStatusError as e:
        logger.error("HN API error: %s %s", e.response.status_code, e.response.text[:200])
        return []
    except httpx.RequestError as e:
        logger.error("HN request failed: %s", e)
        return []

    hits = data.get("hits", [])
    items = [_normalise(hit) for hit in hits]

    time.sleep(_REQUEST_DELAY)
    return [i for i in items if i is not None]


def _normalise(hit: dict) -> dict | None:
    """Convert a HN story hit to community item schema."""
    title = (hit.get("title") or "").strip()
    object_id = hit.get("objectID")
    if not title or not object_id:
        return None

    created_at = hit.get("created_at", "")
    published_date = created_at[:10] if len(created_at) >= 10 else None

    url = hit.get("url") or f"https://news.ycombinator.com/item?id={object_id}"
    points = hit.get("points", 0) or 0

    return {
        "external_id": f"hn:{object_id}",
        "title": title,
        "url": url,
        "source": "hackernews",
        "platform": "hackernews",
        "published_date": published_date,
        "summary": None,
        "engagement": points,
        "comments": hit.get("num_comments", 0) or 0,
        "collector": "hackernews",
        "reliability_tag": "B" if points >= _ENGAGEMENT_THRESHOLD else "C",
    }
