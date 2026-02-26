"""Research Hub MCP server — academic paper discovery and trend tracking."""

from __future__ import annotations

import logging
import sys
from datetime import date

from mcp.server.fastmcp import FastMCP

from research_hub.collectors import semantic_scholar
from research_hub.db.repository import PaperRepository

logging.basicConfig(level=logging.WARNING, stream=sys.stderr)
logger = logging.getLogger(__name__)

mcp = FastMCP("research-hub")
_repo = PaperRepository()


@mcp.tool()
def search_papers(
    topic: str,
    query: str,
    since_year: int | None = None,
    limit: int = 10,
) -> dict:
    """Search Semantic Scholar for papers and store them in the DB.

    Args:
        topic: Topic slug to associate the papers with (e.g. 'ai-network', '6g').
        query: Search keywords (e.g. 'LTE AI optimization', 'quantum key distribution').
        since_year: Only include papers published from this year onwards.
        limit: Maximum number of papers to fetch and store (1-50).

    Returns:
        Dict with stored_count and list of paper summaries.
    """
    limit = max(1, min(limit, 50))
    topic_id = _repo._require_topic_id(topic)

    papers = semantic_scholar.search_papers(query, limit=limit, since_year=since_year)
    if not papers:
        return {"topic": topic, "query": query, "stored_count": 0, "papers": []}

    stored = _repo.upsert_papers(papers)

    results = []
    for paper in papers:
        saved = _repo.get_paper_by_external_id(paper["external_id"])
        if saved:
            _repo.link_paper_topic(saved["id"], topic_id)
            results.append({
                "external_id": saved["external_id"],
                "title": saved["title"],
                "authors": saved.get("authors", []),
                "published_date": saved.get("published_date"),
                "citation_count": saved.get("citation_count", 0),
                "raw_url": saved.get("raw_url"),
            })

    return {
        "topic": topic,
        "query": query,
        "stored_count": stored,
        "papers": results,
    }


@mcp.tool()
def get_trending_papers(
    topic: str,
    since: str | None = None,
    limit: int = 20,
) -> dict:
    """Get the most cited papers for a topic from the DB.

    Args:
        topic: Topic slug (e.g. 'ai-network').
        since: Only include papers published on or after this date (YYYY-MM-DD).
        limit: Maximum number of papers to return.

    Returns:
        Dict with topic and list of papers sorted by citation count.
    """
    papers = _repo.get_trending_papers(topic, since=since, limit=limit)
    return {"topic": topic, "paper_count": len(papers), "papers": papers}


@mcp.tool()
def get_paper_detail(external_id: str) -> dict:
    """Get the full details of a specific paper.

    Args:
        external_id: Paper external ID (e.g. 'ss:abc123' for Semantic Scholar).

    Returns:
        Full paper record, or error dict if not found.
    """
    paper = _repo.get_paper_by_external_id(external_id)
    if paper is None:
        return {"error": f"Paper not found: '{external_id}'"}
    return paper


@mcp.tool()
def get_paper_stats(
    topic: str,
    year: int | None = None,
    month: int | None = None,
) -> dict:
    """Get monthly paper publication statistics for a topic.

    Args:
        topic: Topic slug (e.g. '6g').
        year: Filter to this year (optional).
        month: Filter to this month 1-12 (optional, requires year).

    Returns:
        Dict with topic and list of monthly stats.
    """
    stats = _repo.get_paper_stats(topic, year=year, month=month)
    return {"topic": topic, "stats": stats}


@mcp.tool()
def update_paper_stats(topic: str, year: int, month: int) -> dict:
    """Recompute and store paper statistics for a given topic and month.

    Args:
        topic: Topic slug (e.g. 'edge-computing').
        year: Year (e.g. 2025).
        month: Month 1-12.

    Returns:
        The updated stats record.
    """
    today = date.today()
    if year > today.year or (year == today.year and month > today.month):
        return {"error": f"Cannot compute stats for a future period: {year}-{month:02d}"}
    result = _repo.update_paper_stats(topic, year=year, month=month)
    return {"topic": topic, "updated": result}


if __name__ == "__main__":
    mcp.run()
