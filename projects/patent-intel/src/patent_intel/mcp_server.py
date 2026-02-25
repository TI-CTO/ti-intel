"""Patent Intel MCP server — patent discovery and filing trend tracking."""

from __future__ import annotations

import logging
from datetime import date

from mcp.server.fastmcp import FastMCP

from patent_intel.collectors import patents_view
from patent_intel.db.repository import PatentRepository

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

mcp = FastMCP("patent-intel")
_repo = PatentRepository()


@mcp.tool()
def search_patents(
    topic: str,
    query: str,
    since_year: int | None = None,
    limit: int = 10,
) -> dict:
    """Search USPTO patents and store them in the DB.

    Args:
        topic: Topic slug to associate patents with (e.g. 'ai-network', '6g').
        query: Search keywords (e.g. 'machine learning network slicing').
        since_year: Only include patents filed from this year onwards.
        limit: Maximum number of patents to fetch and store (1-50).

    Returns:
        Dict with stored_count and list of patent summaries.
    """
    limit = max(1, min(limit, 50))
    topic_id = _repo._require_topic_id(topic)

    patents = patents_view.search_patents(query, limit=limit, since_year=since_year)
    if not patents:
        return {"topic": topic, "query": query, "stored_count": 0, "patents": []}

    stored = _repo.upsert_patents(patents)

    results = []
    for patent in patents:
        saved = _repo.get_patent_by_external_id(patent["external_id"])
        if saved:
            _repo.link_patent_topic(saved["id"], topic_id)
            results.append({
                "external_id": saved["external_id"],
                "title": saved["title"],
                "applicant": saved.get("applicant"),
                "filing_date": saved.get("filing_date"),
                "ipc_codes": saved.get("ipc_codes", []),
                "raw_url": saved.get("raw_url"),
            })

    return {
        "topic": topic,
        "query": query,
        "stored_count": stored,
        "patents": results,
    }


@mcp.tool()
def get_recent_patents(
    topic: str,
    since: str | None = None,
    limit: int = 20,
) -> dict:
    """Get the most recently filed patents for a topic from the DB.

    Args:
        topic: Topic slug (e.g. 'quantum-comm').
        since: Only include patents filed on or after this date (YYYY-MM-DD).
        limit: Maximum number of patents to return.

    Returns:
        Dict with topic and list of patents sorted by filing date.
    """
    patents = _repo.get_recent_patents(topic, since=since, limit=limit)
    return {"topic": topic, "patent_count": len(patents), "patents": patents}


@mcp.tool()
def get_patent_detail(external_id: str) -> dict:
    """Get the full details of a specific patent.

    Args:
        external_id: Patent external ID (e.g. 'uspto:US11234567B2').

    Returns:
        Full patent record, or error dict if not found.
    """
    patent = _repo.get_patent_by_external_id(external_id)
    if patent is None:
        return {"error": f"Patent not found: '{external_id}'"}
    return patent


@mcp.tool()
def get_patent_stats(
    topic: str,
    year: int | None = None,
    quarter: int | None = None,
) -> dict:
    """Get quarterly patent filing statistics for a topic.

    Args:
        topic: Topic slug (e.g. '6g').
        year: Filter to this year (optional).
        quarter: Filter to this quarter 1-4 (optional, requires year).

    Returns:
        Dict with topic and list of quarterly stats.
    """
    stats = _repo.get_patent_stats(topic, year=year, quarter=quarter)
    return {"topic": topic, "stats": stats}


@mcp.tool()
def update_patent_stats(topic: str, year: int, quarter: int) -> dict:
    """Recompute and store patent filing statistics for a given topic and quarter.

    Args:
        topic: Topic slug (e.g. 'open-ran').
        year: Year (e.g. 2025).
        quarter: Quarter 1-4.

    Returns:
        The updated stats record.
    """
    today = date.today()
    current_quarter = (today.month - 1) // 3 + 1
    if year > today.year or (year == today.year and quarter > current_quarter):
        return {
            "error": f"Cannot compute stats for a future quarter: {year} Q{quarter}"
        }
    result = _repo.update_patent_stats(topic, year=year, quarter=quarter)
    return {"topic": topic, "updated": result}


if __name__ == "__main__":
    mcp.run()
