"""Cached data loading layer for the Streamlit dashboard."""

from __future__ import annotations

import streamlit as st

from startup_db.db import StartupRepository


@st.cache_resource
def get_repo() -> StartupRepository:
    """Singleton StartupRepository instance."""
    return StartupRepository()


@st.cache_data(ttl=3600)
def cached_company_stats() -> dict:
    """Company aggregate stats (cached 1h)."""
    return get_repo().get_company_stats()


@st.cache_data(ttl=3600)
def cached_funding_stats() -> dict:
    """Funding aggregate stats (cached 1h)."""
    return get_repo().get_funding_stats()


@st.cache_data(ttl=600)
def cached_search_companies(
    query: str | None = None,
    main_category: str | None = None,
    sub_category: str | None = None,
    country: str | None = None,
    status: str | None = None,
    limit: int = 50,
    offset: int = 0,
) -> list[dict]:
    """Search companies with caching (10 min)."""
    return get_repo().search_companies(
        query=query,
        main_category=main_category,
        sub_category=sub_category,
        country=country,
        status=status,
        limit=limit,
        offset=offset,
    )


@st.cache_data(ttl=600)
def cached_company_detail(slug: str) -> dict | None:
    """Company detail with rounds, people, score (cached 10 min)."""
    return get_repo().get_company_detail(slug)


@st.cache_data(ttl=600)
def cached_search_investors(
    query: str | None = None,
    investor_type: str | None = None,
    country: str | None = None,
    limit: int = 50,
    offset: int = 0,
) -> list[dict]:
    """Search investors with caching."""
    return get_repo().search_investors(
        query=query,
        investor_type=investor_type,
        country=country,
        limit=limit,
        offset=offset,
    )


@st.cache_data(ttl=600)
def cached_investor_portfolio(investor_id: str) -> list[dict]:
    """Investor portfolio with caching."""
    return get_repo().get_investor_portfolio(investor_id)


@st.cache_data(ttl=3600)
def cached_all_scores() -> list[dict]:
    """Fetch all scores for analytics."""
    client = get_repo()._client
    result = client.table("su_scores").select("*").execute()
    return result.data or []


@st.cache_data(ttl=3600)
def cached_all_companies_slim() -> list[dict]:
    """Fetch all companies with minimal fields for filters/lookups."""
    client = get_repo()._client
    result = (
        client.table("su_companies")
        .select("id,name,slug,main_category,sub_category,country,status")
        .order("name")
        .execute()
    )
    return result.data or []


@st.cache_data(ttl=3600)
def cached_company_relations(company_id: str) -> list[dict]:
    """Fetch relations for a company."""
    client = get_repo()._client
    result = (
        client.table("su_company_relations")
        .select("*")
        .or_(f"company_id.eq.{company_id},related_company_id.eq.{company_id}")
        .execute()
    )
    return result.data or []


@st.cache_data(ttl=600)
def cached_search_companies_by_topic(l3_slugs: tuple[str, ...]) -> list[dict]:
    """Search companies by L3 topic slugs (cached 10 min)."""
    return get_repo().search_companies_by_topics(list(l3_slugs), limit=500)


@st.cache_data(ttl=3600)
def cached_funding_by_domain() -> dict:
    """Aggregate funding by L1/L2 tech domains.

    Joins su_funding_rounds with su_company_topics via taxonomy mapping.

    Returns:
        {
            "by_l1": {l1_slug: {"count": int, "total_raised": float}},
            "by_l2": {l2_slug: {"count": int, "total_raised": float, "l1": str}},
            "companies_by_l2": {l2_slug: [{"name", "slug", "raised", "country"}]},
        }
    """
    from startup_db.taxonomy import get_l1_for_l3, get_l2_for_l3

    client = get_repo()._client

    # Step 1: All funding rounds
    all_rounds: list[dict] = []
    offset = 0
    while True:
        batch = (
            client.table("su_funding_rounds")
            .select("company_id,raised_amount")
            .range(offset, offset + 999)
            .execute()
        ).data or []
        all_rounds.extend(batch)
        if len(batch) < 1000:
            break
        offset += 1000

    # Step 2: Aggregate raised per company
    company_raised: dict[str, float] = {}
    company_rounds: dict[str, int] = {}
    for r in all_rounds:
        cid = r["company_id"]
        amt = float(r.get("raised_amount") or 0)
        company_raised[cid] = company_raised.get(cid, 0) + amt
        company_rounds[cid] = company_rounds.get(cid, 0) + 1

    # Step 3: Topics map
    topics_map = cached_company_topics_bulk()

    # Step 4: Company info for display
    cids_with_topics = [cid for cid in company_raised if cid in topics_map]
    company_info: dict[str, dict] = {}
    for i in range(0, len(cids_with_topics), 50):
        chunk = cids_with_topics[i : i + 50]
        result = (
            client.table("su_companies")
            .select("id,name,slug,country")
            .in_("id", chunk)
            .execute()
        )
        for c in result.data or []:
            company_info[c["id"]] = c

    # Step 5: Aggregate by L1/L2
    by_l1: dict[str, dict] = {}
    by_l2: dict[str, dict] = {}
    companies_by_l2: dict[str, list[dict]] = {}
    seen_company_l2: dict[str, set[str]] = {}  # avoid double-count

    for cid, l3_slugs in topics_map.items():
        raised = company_raised.get(cid, 0)
        rounds = company_rounds.get(cid, 0)
        info = company_info.get(cid, {})

        for l3 in l3_slugs:
            l1 = get_l1_for_l3(l3)
            l2 = get_l2_for_l3(l3)
            if not l1 or not l2:
                continue

            # Deduplicate: count each company once per L2
            seen_company_l2.setdefault(l2, set())
            if cid in seen_company_l2[l2]:
                continue
            seen_company_l2[l2].add(cid)

            by_l1.setdefault(l1, {"count": 0, "total_raised": 0})
            by_l1[l1]["count"] += rounds
            by_l1[l1]["total_raised"] += raised

            by_l2.setdefault(l2, {"count": 0, "total_raised": 0, "l1": l1})
            by_l2[l2]["count"] += rounds
            by_l2[l2]["total_raised"] += raised

            if info:
                companies_by_l2.setdefault(l2, []).append({
                    "name": info.get("name", ""),
                    "slug": info.get("slug", ""),
                    "country": info.get("country", ""),
                    "raised": raised,
                    "rounds": rounds,
                })

    return {
        "by_l1": by_l1,
        "by_l2": by_l2,
        "companies_by_l2": companies_by_l2,
    }


@st.cache_data(ttl=3600)
def cached_investor_count() -> int:
    """Total investor count (cached 1h)."""
    client = get_repo()._client
    result = client.table("su_investors").select("id", count="exact").execute()
    return len(result.data or [])


@st.cache_data(ttl=3600)
def cached_company_topics_bulk() -> dict[str, list[str]]:
    """Fetch all company topic assignments as {company_id: [l3_slugs]}.

    Returns:
        Dict mapping company_id → list of L3 slug strings.
    """
    client = get_repo()._client
    all_rows: list[dict] = []
    offset = 0
    while True:
        result = (
            client.table("su_company_topics")
            .select("company_id,l3_slug")
            .range(offset, offset + 999)
            .execute()
        )
        batch = result.data or []
        all_rows.extend(batch)
        if len(batch) < 1000:
            break
        offset += 1000

    topics: dict[str, list[str]] = {}
    for row in all_rows:
        topics.setdefault(row["company_id"], []).append(row["l3_slug"])
    return topics
