"""Reddit public JSON collector for community signals."""

from __future__ import annotations

import logging
import time
from datetime import datetime, timezone

import httpx

logger = logging.getLogger(__name__)

_BASE_URL = "https://www.reddit.com"
_REQUEST_DELAY = 1.0  # 60 req/min rate limit
_USER_AGENT = "intel-store/0.1 (community signal collector)"
_ENGAGEMENT_THRESHOLD = 50  # score >= 50 → reliability B


def collect(
    query: str,
    *,
    since_days: int = 7,
    limit: int = 25,
    subreddits: list[str] | None = None,
) -> list[dict]:
    """Search Reddit and return normalised community signal dicts.

    Args:
        query: Search query string.
        since_days: Look back this many days (uses 'week' or 'month' filter).
        limit: Maximum number of results per request (max 100).
        subreddits: Optional list of subreddits to search within.

    Returns:
        List of normalised community item dicts.
    """
    limit = max(1, min(limit, 100))
    time_filter = "week" if since_days <= 7 else "month"

    all_items: list[dict] = []

    if subreddits:
        for sub in subreddits:
            items = _search_subreddit(query, sub, time_filter, limit)
            all_items.extend(items)
            time.sleep(_REQUEST_DELAY)
    else:
        all_items = _search_global(query, time_filter, limit)

    return all_items


def _search_global(query: str, time_filter: str, limit: int) -> list[dict]:
    """Search across all of Reddit."""
    params = {
        "q": query,
        "sort": "relevance",
        "t": time_filter,
        "limit": limit,
        "type": "link",
    }
    return _fetch(f"{_BASE_URL}/search.json", params)


def _search_subreddit(query: str, subreddit: str, time_filter: str, limit: int) -> list[dict]:
    """Search within a specific subreddit."""
    params = {
        "q": query,
        "restrict_sr": "on",
        "sort": "relevance",
        "t": time_filter,
        "limit": limit,
    }
    return _fetch(f"{_BASE_URL}/r/{subreddit}/search.json", params)


def _fetch(url: str, params: dict) -> list[dict]:
    """Execute Reddit API request and return normalised items."""
    try:
        with httpx.Client(
            timeout=30.0,
            headers={"User-Agent": _USER_AGENT},
            follow_redirects=True,
        ) as client:
            resp = client.get(url, params=params)
            resp.raise_for_status()
            data = resp.json()
    except httpx.HTTPStatusError as e:
        logger.error("Reddit API error: %s %s", e.response.status_code, e.response.text[:200])
        return []
    except httpx.RequestError as e:
        logger.error("Reddit request failed: %s", e)
        return []

    children = data.get("data", {}).get("children", [])
    items = [_normalise(child.get("data", {})) for child in children]
    return [i for i in items if i is not None]


def _normalise(data: dict) -> dict | None:
    """Convert a Reddit post to community item schema."""
    title = (data.get("title") or "").strip()
    post_id = data.get("id")
    permalink = data.get("permalink", "")
    if not title or not post_id:
        return None

    created_utc = data.get("created_utc")
    published_date = None
    if created_utc:
        published_date = datetime.fromtimestamp(float(created_utc), tz=timezone.utc).strftime(
            "%Y-%m-%d"
        )

    score = data.get("score", 0) or 0
    selftext = (data.get("selftext") or "")[:500].strip()

    return {
        "external_id": f"reddit:{post_id}",
        "title": title,
        "url": f"https://www.reddit.com{permalink}" if permalink else None,
        "source": "reddit",
        "platform": "reddit",
        "published_date": published_date,
        "summary": selftext or None,
        "engagement": score,
        "comments": data.get("num_comments", 0) or 0,
        "subreddit": data.get("subreddit"),
        "collector": "reddit",
        "reliability_tag": "B" if score >= _ENGAGEMENT_THRESHOLD else "C",
    }
