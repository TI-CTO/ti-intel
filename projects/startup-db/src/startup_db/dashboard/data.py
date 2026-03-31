"""Cached data loading layer for the Streamlit dashboard."""

from __future__ import annotations

import json

import streamlit as st

from startup_db.db import StartupRepository, get_client


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
            client.table("su_companies").select("id,name,slug,country").in_("id", chunk).execute()
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
                companies_by_l2.setdefault(l2, []).append(
                    {
                        "name": info.get("name", ""),
                        "slug": info.get("slug", ""),
                        "country": info.get("country", ""),
                        "raised": raised,
                        "rounds": rounds,
                    }
                )

    return {
        "by_l1": by_l1,
        "by_l2": by_l2,
        "companies_by_l2": companies_by_l2,
    }


@st.cache_data(ttl=3600)
def cached_funding_momentum() -> list[dict]:
    """Fetch all funding rounds with company info and L3 topics.

    Joins su_funding_rounds (announced_date, raised_amount, company_id) with
    su_company_topics (l3_slug) and su_companies (name, slug). Uses taxonomy
    to derive L1/L2 from each L3 slug.

    Returns:
        List of dicts: {company_id, company_name, slug, announced_date,
                        raised_amount, l3_slug, l1, l2}
    """
    from startup_db.taxonomy import get_l1_for_l3, get_l2_for_l3

    client = get_repo()._client

    # Step 1: All funding rounds with date and amount
    all_rounds: list[dict] = []
    offset = 0
    while True:
        batch = (
            client.table("su_funding_rounds")
            .select("company_id,announced_date,raised_amount")
            .range(offset, offset + 999)
            .execute()
        ).data or []
        all_rounds.extend(batch)
        if len(batch) < 1000:
            break
        offset += 1000

    # Step 2: Topics map {company_id: [l3_slugs]}
    topics_map = cached_company_topics_bulk()

    # Step 3: Company info for display
    cids_with_rounds = {r["company_id"] for r in all_rounds}
    company_info: dict[str, dict] = {}
    cids_list = list(cids_with_rounds)
    for i in range(0, len(cids_list), 50):
        chunk = cids_list[i : i + 50]
        result = client.table("su_companies").select("id,name,slug").in_("id", chunk).execute()
        for c in result.data or []:
            company_info[c["id"]] = c

    # Step 4: Expand rounds × topics → flat records
    records: list[dict] = []
    for round_row in all_rounds:
        cid = round_row["company_id"]
        l3_slugs = topics_map.get(cid, [])
        if not l3_slugs:
            continue
        info = company_info.get(cid, {})
        for l3 in l3_slugs:
            l1 = get_l1_for_l3(l3)
            l2 = get_l2_for_l3(l3)
            if not l1 or not l2:
                continue
            records.append(
                {
                    "company_id": cid,
                    "company_name": info.get("name", ""),
                    "slug": info.get("slug", ""),
                    "announced_date": round_row.get("announced_date"),
                    "raised_amount": float(round_row.get("raised_amount") or 0),
                    "l3_slug": l3,
                    "l1": l1,
                    "l2": l2,
                }
            )
    return records


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


# ── Intel Store data functions ──────────────────────────────────


def _intel_client():
    """Reuse the same Supabase client for intel_items tables."""
    return get_client()


@st.cache_data(ttl=3600)
def cached_intel_stats() -> dict:
    """Aggregate intel stats: total, by type, by source, by month.

    Returns:
        {
            "total": int,
            "by_type": {type: count},
            "by_source": {source_name: count},
            "by_month": [{month: "YYYY-MM", count: int}],
        }
    """
    client = _intel_client()

    # Fetch all items (id, item_type, source_name, collected_date)
    all_items: list[dict] = []
    offset = 0
    while True:
        batch = (
            client.table("intel_items")
            .select("id,item_type,source_name,collected_date")
            .range(offset, offset + 999)
            .execute()
        ).data or []
        all_items.extend(batch)
        if len(batch) < 1000:
            break
        offset += 1000

    by_type: dict[str, int] = {}
    by_source: dict[str, int] = {}
    by_month: dict[str, int] = {}

    for item in all_items:
        t = item.get("item_type", "unknown")
        by_type[t] = by_type.get(t, 0) + 1

        s = item.get("source_name", "unknown")
        by_source[s] = by_source.get(s, 0) + 1

        cd = item.get("collected_date", "")
        if cd and len(cd) >= 7:
            month = cd[:7]
            by_month[month] = by_month.get(month, 0) + 1

    monthly = [{"month": k, "count": v} for k, v in sorted(by_month.items())]

    return {
        "total": len(all_items),
        "by_type": by_type,
        "by_source": by_source,
        "by_month": monthly,
    }


@st.cache_data(ttl=3600)
def cached_intel_by_topic() -> list[dict]:
    """Intel items grouped by topic.

    Returns:
        [{topic_slug, topic_name, count, latest_date}]
    """
    client = _intel_client()

    # Fetch topic assignments
    all_links: list[dict] = []
    offset = 0
    while True:
        batch = (
            client.table("intel_item_topics")
            .select("item_id,topic_id")
            .range(offset, offset + 999)
            .execute()
        ).data or []
        all_links.extend(batch)
        if len(batch) < 1000:
            break
        offset += 1000

    # Count by topic_id
    topic_counts: dict[int, int] = {}
    for link in all_links:
        tid = link["topic_id"]
        topic_counts[tid] = topic_counts.get(tid, 0) + 1

    if not topic_counts:
        return []

    # Fetch topic metadata
    topic_ids = list(topic_counts.keys())
    topics_data: list[dict] = []
    for i in range(0, len(topic_ids), 50):
        chunk = topic_ids[i : i + 50]
        result = (
            client.table("topics")
            .select("id,slug,display_name")
            .in_("id", chunk)
            .execute()
        )
        topics_data.extend(result.data or [])

    topic_map = {t["id"]: t for t in topics_data}

    results = []
    for tid, count in sorted(topic_counts.items(), key=lambda x: -x[1]):
        info = topic_map.get(tid, {})
        results.append({
            "topic_slug": info.get("slug", f"topic-{tid}"),
            "topic_name": info.get("display_name", f"Topic {tid}"),
            "count": count,
        })

    return results


@st.cache_data(ttl=600)
def cached_intel_items_by_topic(topic_slug: str, limit: int = 50) -> list[dict]:
    """Fetch intel items for a specific topic.

    Returns:
        [{id, title, item_type, source_name, source_url, collected_date, metadata}]
    """
    client = _intel_client()

    # Get topic id
    topic_result = (
        client.table("topics")
        .select("id")
        .eq("slug", topic_slug)
        .limit(1)
        .execute()
    )
    if not topic_result.data:
        return []
    topic_id = topic_result.data[0]["id"]

    # Get item ids for this topic
    links = (
        client.table("intel_item_topics")
        .select("item_id")
        .eq("topic_id", topic_id)
        .execute()
    ).data or []

    if not links:
        return []

    item_ids = [link["item_id"] for link in links]

    # Fetch items
    items: list[dict] = []
    for i in range(0, min(len(item_ids), limit), 50):
        chunk = item_ids[i : i + 50]
        result = (
            client.table("intel_items")
            .select("id,title,item_type,source_name,source_url,collected_date,metadata")
            .in_("id", chunk)
            .order("collected_date", desc=True)
            .execute()
        )
        items.extend(result.data or [])

    # Sort by collected_date desc
    items.sort(key=lambda x: x.get("collected_date", ""), reverse=True)

    # Parse metadata JSON string
    for item in items:
        meta = item.get("metadata")
        if isinstance(meta, str):
            try:
                item["metadata"] = json.loads(meta)
            except (json.JSONDecodeError, TypeError):
                item["metadata"] = {}

    return items[:limit]


@st.cache_data(ttl=600)
def cached_intel_recent(limit: int = 20) -> list[dict]:
    """Fetch most recent intel items across all topics."""
    client = _intel_client()
    result = (
        client.table("intel_items")
        .select("id,title,item_type,source_name,source_url,collected_date,metadata")
        .order("collected_date", desc=True)
        .limit(limit)
        .execute()
    )
    items = result.data or []
    for item in items:
        meta = item.get("metadata")
        if isinstance(meta, str):
            try:
                item["metadata"] = json.loads(meta)
            except (json.JSONDecodeError, TypeError):
                item["metadata"] = {}
    return items


@st.cache_data(ttl=3600)
def cached_intel_community_engagement() -> list[dict]:
    """Fetch community items with engagement data for trend analysis.

    Returns:
        [{title, source_name, collected_date, platform, engagement, comments}]
    """
    client = _intel_client()
    result = (
        client.table("intel_items")
        .select("id,title,source_name,collected_date,metadata")
        .eq("item_type", "community")
        .order("collected_date", desc=True)
        .execute()
    )
    items = []
    for row in result.data or []:
        meta = row.get("metadata", {})
        if isinstance(meta, str):
            try:
                meta = json.loads(meta)
            except (json.JSONDecodeError, TypeError):
                meta = {}
        items.append({
            "title": row.get("title", ""),
            "source_name": row.get("source_name", ""),
            "collected_date": row.get("collected_date", ""),
            "platform": meta.get("platform", "unknown"),
            "engagement": meta.get("engagement", 0),
            "comments": meta.get("comments", meta.get("num_comments", 0)),
        })
    return items
