"""GDELT 2.0 Doc API collector for free global news coverage."""

from __future__ import annotations

import logging
import time
from datetime import date, timedelta
from urllib.parse import quote

import httpx

logger = logging.getLogger(__name__)

_BASE_URL = "https://api.gdeltproject.org/api/v2/doc/doc"
_REQUEST_DELAY = 1.0  # seconds between requests (be polite to free API)


def collect(
    query: str,
    *,
    since_days: int = 7,
    limit: int = 20,
) -> list[dict]:
    """Search GDELT 2.0 Doc API and return normalised news dicts.

    Args:
        query: Search query string.
        since_days: Look back this many days from today.
        limit: Maximum number of results (max 250 per GDELT request).

    Returns:
        List of normalised news item dicts ready for DB upsert.

    Note:
        GDELT is completely free, no API key required.
    """
    limit = max(1, min(limit, 250))
    start_date = date.today() - timedelta(days=since_days)
    start_str = start_date.strftime("%Y%m%d%H%M%S")

    params = {
        "query": query,
        "mode": "ArtList",
        "maxrecords": str(limit),
        "format": "json",
        "startdatetime": start_str,
        "sort": "DateDesc",
    }

    try:
        with httpx.Client(timeout=60.0) as client:
            resp = client.get(_BASE_URL, params=params)
            resp.raise_for_status()
            data = resp.json()
    except httpx.HTTPStatusError as e:
        logger.error("GDELT API error: %s %s", e.response.status_code, e.response.text[:200])
        return []
    except httpx.RequestError as e:
        logger.error("GDELT request failed: %s", e)
        return []
    except Exception as e:
        logger.error("GDELT parse error: %s", e)
        return []

    raw_articles = data.get("articles", [])
    items = [_normalise(a) for a in raw_articles]
    items = [i for i in items if i is not None]

    time.sleep(_REQUEST_DELAY)
    return items


def _normalise(raw: dict) -> dict | None:
    """Convert a GDELT article to our news item schema."""
    title = (raw.get("title") or "").strip()
    url = (raw.get("url") or "").strip()
    if not title or not url:
        return None

    # GDELT seendate format: "20250226T120000Z"
    seen_date = raw.get("seendate", "")
    published_date = None
    if seen_date and len(seen_date) >= 8:
        try:
            published_date = f"{seen_date[:4]}-{seen_date[4:6]}-{seen_date[6:8]}"
        except (IndexError, ValueError):
            pass

    domain = raw.get("domain", "")

    return {
        "title": title,
        "url": url,
        "source": domain or "gdelt",
        "published_date": published_date,
        "summary": None,
        "reliability_tag": "C",
        "collector": "gdelt",
    }
