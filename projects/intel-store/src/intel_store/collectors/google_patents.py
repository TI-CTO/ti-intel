"""Google Patents search via SerpAPI.

Uses the SerpAPI google_patents engine to search granted patents.
Free tier: 250 requests/month. API key required (SERPAPI_API_KEY).
"""

from __future__ import annotations

import logging
import time

import httpx

from intel_store.config import settings

logger = logging.getLogger(__name__)

_BASE_URL = "https://serpapi.com/search"
_REQUEST_DELAY = 1.5  # seconds between requests


def search_patents(
    query: str,
    *,
    limit: int = 10,
    since_year: int | None = None,
) -> list[dict]:
    """Search Google Patents via SerpAPI and return normalised patent dicts.

    Args:
        query: Keywords to search in patent title and abstract.
        limit: Maximum number of results (max 100).
        since_year: If set, filter patents filed on or after this year.

    Returns:
        List of patent dicts ready for IntelItem conversion.
    """
    api_key = settings.serpapi_api_key
    if not api_key:
        logger.warning("SERPAPI_API_KEY not set — skipping Google Patents search")
        return []

    limit = max(10, min(limit, 100))

    search_query = query
    if since_year:
        search_query = f"{query} after:priority:{since_year}0101"

    params = {
        "engine": "google_patents",
        "q": search_query,
        "num": limit,
        "api_key": api_key,
    }

    try:
        with httpx.Client(timeout=30.0) as client:
            resp = client.get(_BASE_URL, params=params)
            resp.raise_for_status()
            data = resp.json()
    except httpx.HTTPStatusError as e:
        logger.error("SerpAPI error: %s %s", e.response.status_code, e.response.text[:200])
        return []
    except httpx.RequestError as e:
        logger.error("SerpAPI request failed: %s", e)
        return []

    raw_results = data.get("organic_results") or []
    patents = [p for raw in raw_results if (p := _normalise(raw)) is not None]

    time.sleep(_REQUEST_DELAY)
    return patents


def _normalise(raw: dict) -> dict | None:
    """Convert a SerpAPI Google Patents result to our schema."""
    patent_id = raw.get("patent_id") or ""
    if not patent_id:
        return None

    title = (raw.get("title") or "").strip()
    if not title:
        return None

    # Assignee / applicant
    assignee = (raw.get("assignee") or "").strip() or "Unknown"

    # Snippet as abstract
    abstract = (raw.get("snippet") or "").strip()

    # Dates
    publication_date = raw.get("publication_date") or None
    filing_date = raw.get("filing_date") or None

    # IPC / CPC classification codes
    ipc_codes: list[str] = []
    classifications = raw.get("classifications") or []
    if isinstance(classifications, list):
        for cls in classifications:
            code = cls.get("code") or "" if isinstance(cls, dict) else str(cls)
            if code and code not in ipc_codes:
                ipc_codes.append(code)

    raw_url = f"https://patents.google.com/patent/{patent_id}"

    return {
        "external_id": f"gp:{patent_id}",
        "source": "google_patents",
        "title": title,
        "applicant": assignee,
        "filing_date": filing_date,
        "publication_date": publication_date,
        "ipc_codes": ipc_codes,
        "abstract": abstract,
        "reliability_tag": "A",
        "raw_url": raw_url,
    }
