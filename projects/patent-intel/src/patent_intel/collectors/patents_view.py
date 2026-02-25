"""USPTO PatentsView API client for patent discovery.

API docs: https://api.patentsview.org/
Free, no API key required. Rate limit: ~45 requests/minute.
Covers US patents from 1976 onwards.
"""

from __future__ import annotations

import logging
import time

import httpx

logger = logging.getLogger(__name__)

_BASE_URL = "https://api.patentsview.org/patents/query"
_REQUEST_DELAY = 1.5  # seconds between requests

_FIELDS = [
    "patent_id",
    "patent_title",
    "patent_abstract",
    "patent_date",
    "app_date",
    "patent_number",
    "assignee_organization",
    "assignee_country",
    "ipc_subgroup_id",
    "ipc_main_group",
]


def search_patents(
    query: str,
    *,
    limit: int = 10,
    since_year: int | None = None,
) -> list[dict]:
    """Search USPTO PatentsView and return normalised patent dicts.

    Args:
        query: Keywords to search in patent title and abstract.
        limit: Maximum number of results (max 100).
        since_year: If set, filter patents filed on or after this year.

    Returns:
        List of patent dicts ready for DB upsert.
    """
    limit = max(1, min(limit, 100))

    # Build query: full-text search on title + abstract
    q: dict = {"_or": [
        {"_text_all": {"patent_title": query}},
        {"_text_all": {"patent_abstract": query}},
    ]}
    if since_year:
        q = {"_and": [q, {"_gte": {"app_date": f"{since_year}-01-01"}}]}

    payload = {
        "q": q,
        "f": _FIELDS,
        "o": {"per_page": limit, "sort": [{"app_date": "desc"}]},
    }

    with httpx.Client(timeout=30.0) as client:
        resp = client.post(_BASE_URL, json=payload)
        resp.raise_for_status()
        data = resp.json()

    raw_patents = data.get("patents") or []
    patents = [p for raw in raw_patents if (p := _normalise(raw)) is not None]

    time.sleep(_REQUEST_DELAY)
    return patents


def _normalise(raw: dict) -> dict | None:
    """Convert a raw PatentsView patent dict to our DB schema."""
    patent_id = raw.get("patent_id")
    if not patent_id:
        return None

    title = (raw.get("patent_title") or "").strip()
    if not title:
        return None

    # Applicant: take first assignee organisation
    assignees = raw.get("assignees") or []
    applicant = ""
    if assignees and isinstance(assignees, list):
        org = assignees[0].get("assignee_organization") or ""
        country = assignees[0].get("assignee_country") or ""
        applicant = f"{org} ({country})" if country else org
    applicant = applicant.strip() or "Unknown"

    # IPC codes
    ipcs = raw.get("ipcs") or []
    ipc_codes: list[str] = []
    if isinstance(ipcs, list):
        for ipc in ipcs:
            code = ipc.get("ipc_subgroup_id") or ipc.get("ipc_main_group") or ""
            if code and code not in ipc_codes:
                ipc_codes.append(code)

    filing_date = raw.get("app_date") or None
    publication_date = raw.get("patent_date") or None
    patent_number = raw.get("patent_number") or patent_id
    raw_url = f"https://patents.google.com/patent/US{patent_number}"

    return {
        "external_id": f"uspto:{patent_number}",
        "source": "uspto",
        "title": title,
        "applicant": applicant,
        "filing_date": filing_date,
        "publication_date": publication_date,
        "ipc_codes": ipc_codes,
        "abstract": (raw.get("patent_abstract") or "").strip(),
        "reliability_tag": "A",
        "raw_url": raw_url,
    }
