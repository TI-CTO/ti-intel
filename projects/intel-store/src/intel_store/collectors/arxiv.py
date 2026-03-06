"""arXiv API collector for academic paper discovery (Atom/XML feed)."""

from __future__ import annotations

import logging
import re
import time
from datetime import date
from urllib.parse import quote

import feedparser

logger = logging.getLogger(__name__)

_BASE_URL = "https://export.arxiv.org/api/query"
_REQUEST_DELAY = 3.0  # arXiv asks for 3-second gap between requests


def search_papers(
    query: str,
    *,
    limit: int = 10,
    since_year: int | None = None,
) -> list[dict]:
    """Search arXiv and return normalised paper dicts.

    Args:
        query: arXiv search query (e.g. 'all:homomorphic encryption').
        limit: Maximum number of results (max 100).
        since_year: If set, filter papers published on or after this year.

    Returns:
        List of paper dicts ready for IntelItem conversion via paper_from_collector.
    """
    limit = max(1, min(limit, 100))
    encoded_query = quote(query, safe=":")
    params = (
        f"search_query={encoded_query}&start=0&max_results={limit}"
        "&sortBy=submittedDate&sortOrder=descending"
    )
    url = f"{_BASE_URL}?{params}"

    try:
        feed = feedparser.parse(url)
    except Exception as e:
        logger.error("arXiv feed parse failed: %s", e)
        return []

    papers = []
    for entry in feed.entries:
        paper = _normalise(entry)
        if paper is None:
            continue
        if since_year and paper.get("published_date"):
            pub_year = int(str(paper["published_date"])[:4])
            if pub_year < since_year:
                continue
        papers.append(paper)

    time.sleep(_REQUEST_DELAY)
    return papers


def _normalise(entry: dict) -> dict | None:
    """Convert an arXiv Atom entry to our paper schema."""
    arxiv_id = _extract_arxiv_id(entry.get("id", ""))
    if not arxiv_id:
        return None

    title = (entry.get("title") or "").strip().replace("\n", " ")
    if not title:
        return None

    authors = [a.get("name", "") for a in entry.get("authors", []) if a.get("name")]
    abstract = (entry.get("summary") or "").strip().replace("\n", " ")

    published_date: date | None = None
    published_str = entry.get("published", "")
    if published_str:
        try:
            published_date = date.fromisoformat(published_str[:10])
        except (ValueError, TypeError):
            pass

    # arXiv categories as venue
    categories = [t.get("term", "") for t in entry.get("tags", []) if t.get("term")]
    venue = ", ".join(categories) if categories else ""

    raw_url = f"https://arxiv.org/abs/{arxiv_id}"

    return {
        "external_id": f"arxiv:{arxiv_id}",
        "source": "arxiv",
        "title": title,
        "authors": authors,
        "published_date": published_date.isoformat() if published_date else None,
        "abstract": abstract,
        "citation_count": 0,
        "venue": venue,
        "reliability_tag": "A",
        "raw_url": raw_url,
    }


def _extract_arxiv_id(url: str) -> str | None:
    """Extract arXiv paper ID from an Atom entry URL.

    Args:
        url: arXiv URL like 'http://arxiv.org/abs/2301.12345v1'.

    Returns:
        ID string like '2301.12345' (version stripped), or None.
    """
    match = re.search(r"(\d{4}\.\d{4,5})(v\d+)?$", url)
    return match.group(1) if match else None
