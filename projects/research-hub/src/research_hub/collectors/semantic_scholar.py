"""Semantic Scholar API client for academic paper discovery."""

from __future__ import annotations

import logging
import time
from datetime import date

import httpx

logger = logging.getLogger(__name__)

_BASE_URL = "https://api.semanticscholar.org/graph/v1"
_FIELDS = "title,authors,year,publicationDate,citationCount,abstract,externalIds,url"
_REQUEST_DELAY = 1.1  # seconds between requests to respect rate limit (1 req/sec)


def search_papers(
    query: str,
    *,
    limit: int = 10,
    since_year: int | None = None,
) -> list[dict]:
    """Search Semantic Scholar and return normalised paper dicts.

    Args:
        query: Search query string (keywords, title fragments, etc.)
        limit: Maximum number of results to return (max 100).
        since_year: If set, filter papers published on or after this year.

    Returns:
        List of paper dicts ready for DB upsert.
    """
    params: dict = {
        "query": query,
        "fields": _FIELDS,
        "limit": min(limit, 100),
    }

    with httpx.Client(timeout=30.0) as client:
        resp = client.get(f"{_BASE_URL}/paper/search", params=params)
        resp.raise_for_status()
        data = resp.json()

    raw_papers = data.get("data", [])
    papers = []
    for raw in raw_papers:
        paper = _normalise(raw)
        if paper is None:
            continue
        if since_year and paper.get("published_date"):
            pub_year = int(str(paper["published_date"])[:4])
            if pub_year < since_year:
                continue
        papers.append(paper)

    time.sleep(_REQUEST_DELAY)
    return papers


def get_paper(paper_id: str) -> dict | None:
    """Fetch a single paper by Semantic Scholar paper ID.

    Args:
        paper_id: Semantic Scholar paper ID (not prefixed).

    Returns:
        Normalised paper dict, or None if not found.
    """
    with httpx.Client(timeout=30.0) as client:
        resp = client.get(
            f"{_BASE_URL}/paper/{paper_id}",
            params={"fields": _FIELDS},
        )
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
        raw = resp.json()

    time.sleep(_REQUEST_DELAY)
    return _normalise(raw)


def _normalise(raw: dict) -> dict | None:
    """Convert a raw Semantic Scholar paper dict to our DB schema."""
    paper_id = raw.get("paperId")
    if not paper_id:
        return None

    title = raw.get("title", "").strip()
    if not title:
        return None

    authors = [a.get("name", "") for a in raw.get("authors", []) if a.get("name")]

    pub_date_str = raw.get("publicationDate")
    pub_year = raw.get("year")
    published_date: date | None = None
    if pub_date_str:
        try:
            published_date = date.fromisoformat(pub_date_str)
        except ValueError:
            pass
    elif pub_year:
        try:
            published_date = date(int(pub_year), 1, 1)
        except (ValueError, TypeError):
            pass

    external_ids = raw.get("externalIds", {}) or {}
    arxiv_id = external_ids.get("ArXiv")
    raw_url = raw.get("url") or (
        f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else None
    )

    return {
        "external_id": f"ss:{paper_id}",
        "source": "semantic_scholar",
        "title": title,
        "authors": authors,
        "published_date": published_date.isoformat() if published_date else None,
        "abstract": (raw.get("abstract") or "").strip(),
        "citation_count": raw.get("citationCount") or 0,
        "reliability_tag": "A",
        "raw_url": raw_url,
    }
