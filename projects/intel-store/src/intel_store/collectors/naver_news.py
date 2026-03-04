"""Naver News Search API collector for Korean-language news."""

from __future__ import annotations

import logging
import re
from datetime import date, timedelta
from email.utils import parsedate_to_datetime

import httpx

from intel_store.config import settings

logger = logging.getLogger(__name__)

_BASE_URL = "https://openapi.naver.com/v1/search/news.json"


def collect(
    query: str,
    *,
    since_days: int = 7,
    limit: int = 20,
) -> list[dict]:
    """Search Naver News and return normalised news dicts.

    Args:
        query: Search query string (Korean or English).
        since_days: Look back this many days from today.
        limit: Maximum number of results (max 100 per Naver request).

    Returns:
        List of normalised news item dicts ready for IntelItem conversion.
    """
    client_id = settings.naver_client_id
    client_secret = settings.naver_client_secret
    if not client_id or not client_secret:
        logger.warning("NAVER_CLIENT_ID/SECRET not set, skipping Naver collection")
        return []

    limit = max(1, min(limit, 100))
    cutoff = date.today() - timedelta(days=since_days)

    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret,
    }
    params = {
        "query": query,
        "display": limit,
        "start": 1,
        "sort": "date",
    }

    try:
        with httpx.Client(timeout=15.0, headers=headers) as client:
            resp = client.get(_BASE_URL, params=params)
            resp.raise_for_status()
            data = resp.json()
    except httpx.HTTPStatusError as e:
        logger.error("Naver API error: %s %s", e.response.status_code, e.response.text[:200])
        return []
    except httpx.RequestError as e:
        logger.error("Naver request failed: %s", e)
        return []

    raw_items = data.get("items", [])
    items = []
    for raw in raw_items:
        item = _normalise(raw)
        if item is None:
            continue
        # Post-filter by date (Naver API has no date range parameter)
        pub_date = item.get("published_date")
        if pub_date:
            try:
                if date.fromisoformat(pub_date) < cutoff:
                    continue
            except (ValueError, TypeError):
                pass
        items.append(item)

    return items


def _normalise(raw: dict) -> dict | None:
    """Convert a Naver News search result to our news item schema."""
    title = _strip_html(raw.get("title", "")).strip()
    if not title:
        return None

    # Prefer originallink (direct publisher URL) over Naver redirect link
    url = (raw.get("originallink") or raw.get("link") or "").strip()
    if not url:
        return None

    description = _strip_html(raw.get("description", "")).strip()
    published_date = _parse_rfc822_date(raw.get("pubDate", ""))

    return {
        "title": title,
        "url": url,
        "source": _extract_domain(url),
        "published_date": published_date,
        "summary": description[:500] if description else None,
        "reliability_tag": "B",
        "collector": "naver",
    }


def _strip_html(text: str) -> str:
    """Remove HTML tags from text (Naver returns <b> highlighting)."""
    return re.sub(r"<[^>]+>", "", text)


def _parse_rfc822_date(date_str: str) -> str | None:
    """Parse RFC 822 date string to YYYY-MM-DD.

    Args:
        date_str: RFC 822 date like 'Mon, 03 Mar 2026 09:00:00 +0900'.

    Returns:
        ISO date string 'YYYY-MM-DD', or None on failure.
    """
    if not date_str:
        return None
    try:
        dt = parsedate_to_datetime(date_str)
        return dt.date().isoformat()
    except (ValueError, TypeError):
        return None


def _extract_domain(url: str) -> str:
    """Extract domain from URL."""
    try:
        from urllib.parse import urlparse

        domain = urlparse(url).netloc
        if domain.startswith("www."):
            domain = domain[4:]
        return domain
    except Exception:
        return "unknown"
