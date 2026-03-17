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
