"""MCP server for startup-db — company, funding, and investor tools."""

from __future__ import annotations

import logging
from functools import lru_cache

from mcp.server.fastmcp import FastMCP

from startup_db.db import StartupRepository
from startup_db.models import (
    Company,
    CompanyStatus,
    FundingRound,
    Investor,
    InvestorType,
    RoundType,
    slugify,
)
from startup_db.taxonomy import (
    get_l3_slugs_for_l1,
    get_l3_slugs_for_l2,
    is_valid_l3,
)

logger = logging.getLogger(__name__)

mcp = FastMCP("startup-db")


@lru_cache(maxsize=1)
def _get_repo() -> StartupRepository:
    return StartupRepository()


# ── Phase 1 Tools ────────────────────────────────────────────


@mcp.tool()
def search_companies(
    query: str | None = None,
    main_category: str | None = None,
    sub_category: str | None = None,
    country: str | None = None,
    status: str | None = None,
    tags: list[str] | None = None,
    l1: str | None = None,
    l2: str | None = None,
    l3_slug: str | None = None,
    limit: int = 50,
    offset: int = 0,
) -> list[dict]:
    """Search startups by name, category, country, status, tags, or tech taxonomy.

    Args:
        query: Free-text search across name, description, technology.
        main_category: Filter by main category (e.g. "Service", "Data", "Infra").
        sub_category: Filter by sub-category (e.g. "Work Agent", "Data 증강/ 라벨링").
        country: Filter by country (e.g. "한국", "미국").
        status: Filter by status: active, acquired, ipo, defunct, unknown.
        tags: Filter by overlapping tags (any match).
        l1: Filter by L1 domain: agentic-ai, voice-ai, secure-ai.
        l2: Filter by L2 area slug (e.g. "hybrid-ai-infra").
        l3_slug: Filter by L3 technology slug (e.g. "adaptive-rag").
        limit: Max results (default 50).
        offset: Pagination offset.

    Returns:
        List of company records.
    """
    repo = _get_repo()

    # If taxonomy filter is provided, use topic-based search
    topic_slugs: list[str] | None = None
    if l3_slug:
        topic_slugs = [l3_slug]
    elif l2:
        topic_slugs = get_l3_slugs_for_l2(l2)
    elif l1:
        topic_slugs = get_l3_slugs_for_l1(l1)

    if topic_slugs:
        # Get companies by topic, then apply additional filters
        companies = repo.search_companies_by_topics(topic_slugs, limit=limit, offset=offset)
        # Apply filters in-memory for topic-based search
        if query:
            q_lower = query.lower()
            companies = [
                c for c in companies
                if q_lower in (c.get("name") or "").lower()
                or q_lower in (c.get("description") or "").lower()
                or q_lower in (c.get("technology") or "").lower()
            ]
        if main_category:
            companies = [c for c in companies if c.get("main_category") == main_category]
        if sub_category:
            companies = [c for c in companies if c.get("sub_category") == sub_category]
        if country:
            companies = [c for c in companies if c.get("country") == country]
        if status:
            companies = [c for c in companies if c.get("status") == status]
        return companies

    return repo.search_companies(
        query=query,
        main_category=main_category,
        sub_category=sub_category,
        country=country,
        status=status,
        tags=tags,
        limit=limit,
        offset=offset,
    )


@mcp.tool()
def get_company(slug: str) -> dict:
    """Get full company details by slug, including funding rounds, people, and scores.

    Args:
        slug: URL-safe company identifier (e.g. "sim2real", "xl8-inc").

    Returns:
        Company record with funding_rounds, people, and latest_score nested.
        Empty dict if not found.
    """
    repo = _get_repo()
    result = repo.get_company_detail(slug)
    return result or {}


@mcp.tool()
def upsert_company(
    name: str,
    slug: str | None = None,
    description: str | None = None,
    website: str | None = None,
    status: str = "active",
    main_category: str | None = None,
    sub_category: str | None = None,
    tags: list[str] | None = None,
    country: str | None = None,
    city: str | None = None,
    technology: str | None = None,
    main_product: str | None = None,
    discovery_source: str | None = None,
    metadata: dict | None = None,
) -> dict:
    """Add or update a startup company. Uses slug for upsert matching.

    Args:
        name: Company name (required).
        slug: URL-safe identifier. Auto-generated from name if omitted.
        description: Company overview.
        website: Company website URL.
        status: Lifecycle status: active, acquired, ipo, defunct, unknown.
        main_category: Main category (e.g. "Service", "Data").
        sub_category: Sub-category.
        tags: List of keyword tags.
        country: Country (e.g. "한국", "미국").
        city: City.
        technology: Core technology description.
        main_product: Main product/service.
        discovery_source: How the company was first found.
        metadata: Additional JSON metadata.

    Returns:
        The upserted company record.
    """
    company = Company(
        name=name,
        slug=slug or slugify(name),
        description=description,
        website=website,
        status=CompanyStatus(status),
        main_category=main_category,
        sub_category=sub_category,
        tags=tags or [],
        country=country,
        city=city,
        technology=technology,
        main_product=main_product,
        discovery_source=discovery_source,
        metadata=metadata or {},
    )
    repo = _get_repo()
    return repo.upsert_company(company)


@mcp.tool()
def get_company_stats() -> dict:
    """Get aggregate statistics: total count, breakdown by category/country/status.

    Returns:
        Dict with total, by_category, by_sub_category, by_country, by_status.
    """
    repo = _get_repo()
    return repo.get_company_stats()


@mcp.tool()
def add_funding_round(
    company_slug: str,
    round_type: str,
    raised_amount: float | None = None,
    currency: str = "KRW",
    announced_date: str | None = None,
    pre_money_valuation: float | None = None,
    post_money_valuation: float | None = None,
    lead_investor_slug: str | None = None,
    investor_slugs: list[str] | None = None,
    source_url: str | None = None,
) -> dict:
    """Record a funding round for a company.

    Args:
        company_slug: Target company slug.
        round_type: Round type: pre_seed, seed, series_a~f, bridge, grant, ipo, undisclosed, other.
        raised_amount: Amount raised.
        currency: Currency code (default KRW).
        announced_date: Date string (YYYY-MM-DD).
        pre_money_valuation: Pre-money valuation.
        post_money_valuation: Post-money valuation.
        lead_investor_slug: Slug of the lead investor.
        investor_slugs: Slugs of participating investors.
        source_url: Source article URL.

    Returns:
        The created funding round record.
    """
    repo = _get_repo()
    company = repo.get_company_by_slug(company_slug)
    if not company:
        return {"error": f"Company not found: {company_slug}"}

    from datetime import date as date_type

    lead_id = None
    if lead_investor_slug:
        inv = repo.get_investor_by_slug(lead_investor_slug)
        if inv:
            lead_id = inv["id"]

    investor_ids = []
    if investor_slugs:
        for s in investor_slugs:
            inv = repo.get_investor_by_slug(s)
            if inv:
                investor_ids.append(inv["id"])

    parsed_date = None
    if announced_date:
        try:
            parsed_date = date_type.fromisoformat(announced_date)
        except ValueError:
            pass

    fr = FundingRound(
        company_id=company["id"],
        round_type=RoundType(round_type),
        raised_amount=raised_amount,
        currency=currency,
        announced_date=parsed_date,
        pre_money_valuation=pre_money_valuation,
        post_money_valuation=post_money_valuation,
        lead_investor_id=lead_id,
        source_url=source_url,
    )
    return repo.add_funding_round(fr, investor_ids=investor_ids or None)


@mcp.tool()
def upsert_investor(
    name: str,
    slug: str | None = None,
    investor_type: str | None = None,
    description: str | None = None,
    website: str | None = None,
    country: str | None = None,
) -> dict:
    """Add or update an investor entity.

    Args:
        name: Investor name (required).
        slug: URL-safe identifier. Auto-generated from name if omitted.
        investor_type: Type: vc, angel, pe, cvc, accelerator, government, other.
        description: Investor description.
        website: Website URL.
        country: Country.

    Returns:
        The upserted investor record.
    """
    inv = Investor(
        name=name,
        slug=slug or slugify(name),
        investor_type=InvestorType(investor_type) if investor_type else None,
        description=description,
        website=website,
        country=country,
    )
    repo = _get_repo()
    return repo.upsert_investor(inv)


# ── Phase 2 Tools ────────────────────────────────────────────


@mcp.tool()
def score_company(
    company_slug: str,
    tech_strength: int | None = None,
    market_potential: int | None = None,
    team_quality: int | None = None,
    business_fit: int | None = None,
    traction: int | None = None,
    overall_score: int | None = None,
    scored_by: str | None = None,
    rationale: str | None = None,
) -> dict:
    """Record a multi-dimensional score for a company (1-10 per dimension, 0-100 overall).

    Args:
        company_slug: Target company slug.
        tech_strength: Technology strength score (1-10).
        market_potential: Market potential score (1-10).
        team_quality: Team quality score (1-10).
        business_fit: Business fit score (1-10).
        traction: Traction/momentum score (1-10).
        overall_score: Overall composite score (0-100).
        scored_by: Who performed the scoring (e.g. "analyst", "auto").
        rationale: Free-text explanation for the scores.

    Returns:
        The created score record. Error dict if company not found.
    """
    repo = _get_repo()
    company = repo.get_company_by_slug(company_slug)
    if not company:
        return {"error": f"Company not found: {company_slug}"}

    return repo.score_company(
        company_id=company["id"],
        tech_strength=tech_strength,
        market_potential=market_potential,
        team_quality=team_quality,
        business_fit=business_fit,
        traction=traction,
        overall_score=overall_score,
        scored_by=scored_by,
        rationale=rationale,
    )


@mcp.tool()
def add_company_relation(
    company_slug: str,
    related_company_slug: str,
    relation_type: str,
    description: str | None = None,
    bidirectional: bool = False,
) -> dict:
    """Add a relationship between two companies.

    Args:
        company_slug: Source company slug.
        related_company_slug: Related company slug.
        relation_type: Relation type: competitor, partner, customer, supplier, spin_off.
        description: Optional description of the relationship.
        bidirectional: If true, create the reverse relation as well.

    Returns:
        The created relation record. Error dict if company not found.
    """
    repo = _get_repo()
    company = repo.get_company_by_slug(company_slug)
    if not company:
        return {"error": f"Company not found: {company_slug}"}

    related = repo.get_company_by_slug(related_company_slug)
    if not related:
        return {"error": f"Related company not found: {related_company_slug}"}

    result = repo.add_company_relation(
        company_id=company["id"],
        related_company_id=related["id"],
        relation_type=relation_type,
        description=description,
    )

    if bidirectional:
        repo.add_company_relation(
            company_id=related["id"],
            related_company_id=company["id"],
            relation_type=relation_type,
            description=description,
        )

    return result


@mcp.tool()
def search_investors(
    query: str | None = None,
    investor_type: str | None = None,
    country: str | None = None,
    limit: int = 50,
    offset: int = 0,
) -> list[dict]:
    """Search investors by name, type, or country.

    Args:
        query: Free-text search across investor name and description.
        investor_type: Filter by type: vc, angel, pe, cvc, accelerator, government, other.
        country: Filter by country.
        limit: Max results (default 50).
        offset: Pagination offset.

    Returns:
        List of matching investor records.
    """
    repo = _get_repo()
    return repo.search_investors(
        query=query,
        investor_type=investor_type,
        country=country,
        limit=limit,
        offset=offset,
    )


@mcp.tool()
def get_investor_portfolio(investor_slug: str) -> dict:
    """Get all companies that received funding from a specific investor.

    Args:
        investor_slug: Investor's URL-safe slug.

    Returns:
        Investor info with a 'portfolio' key listing companies and their rounds.
        Error dict if investor not found.
    """
    repo = _get_repo()
    investor = repo.get_investor_by_slug(investor_slug)
    if not investor:
        return {"error": f"Investor not found: {investor_slug}"}

    companies = repo.get_investor_portfolio(investor["id"])
    return {
        "investor": investor,
        "portfolio_count": len(companies),
        "portfolio": companies,
    }


@mcp.tool()
def get_funding_stats() -> dict:
    """Get funding statistics: totals, breakdown by round type, year, and category.

    Returns:
        Dict with total_rounds, total_raised, by_round_type, by_year, by_category.
    """
    repo = _get_repo()
    return repo.get_funding_stats()


@mcp.tool()
def manage_collection(
    action: str,
    name: str | None = None,
    collection_id: str | None = None,
    description: str | None = None,
    collection_type: str | None = None,
    company_slugs: list[str] | None = None,
) -> dict | list[dict]:
    """Manage watchlists and market map collections.

    Args:
        action: Operation: create, get, add_items, remove_items, list, delete.
        name: Collection name (required for 'create').
        collection_id: Collection UUID (required for get/add_items/remove_items/delete).
        description: Collection description (for 'create').
        collection_type: Type tag (for 'create', e.g. "watchlist", "market_map").
        company_slugs: Company slugs to add/remove (for 'add_items'/'remove_items').

    Returns:
        Collection record(s) or operation result.
    """
    repo = _get_repo()

    # Resolve slugs to IDs
    company_ids = None
    if company_slugs:
        company_ids = []
        for s in company_slugs:
            c = repo.get_company_by_slug(s)
            if c:
                company_ids.append(c["id"])

    return repo.manage_collection(
        action=action,
        name=name,
        collection_id=collection_id,
        description=description,
        collection_type=collection_type,
        company_ids=company_ids,
    )


@mcp.tool()
def search_people(
    query: str | None = None,
    organization: str | None = None,
    role: str | None = None,
    limit: int = 50,
    offset: int = 0,
) -> list[dict]:
    """Search people (founders, executives, advisors) by name, organization, or role.

    Args:
        query: Free-text search across name, title, organization.
        organization: Filter by organization name.
        role: Filter by role: founder, ceo, cto, advisor, board_member, employee, other.
        limit: Max results (default 50).
        offset: Pagination offset.

    Returns:
        List of matching person records.
    """
    repo = _get_repo()
    return repo.search_people(
        query=query,
        organization=organization,
        role=role,
        limit=limit,
        offset=offset,
    )


# ── Phase 3 Tools ────────────────────────────────────────────


@mcp.tool()
def assign_company_topics(
    company_slug: str,
    l3_slugs: list[str],
    assigned_by: str = "manual",
) -> dict:
    """Assign L3 technology topics to a company.

    Args:
        company_slug: Target company slug.
        l3_slugs: List of L3 technology slugs to assign
            (e.g. ["adaptive-rag", "agent-orchestration"]).
        assigned_by: Who performed the assignment (default "manual").

    Returns:
        Dict with assigned topics and L1/L2 context. Error if company not found or slugs invalid.
    """
    repo = _get_repo()
    company = repo.get_company_by_slug(company_slug)
    if not company:
        return {"error": f"Company not found: {company_slug}"}

    # Validate all slugs
    invalid = [s for s in l3_slugs if not is_valid_l3(s)]
    if invalid:
        from startup_db.taxonomy import get_all_l3_slugs
        return {
            "error": f"Invalid L3 slugs: {invalid}",
            "valid_slugs": get_all_l3_slugs(),
        }

    result = repo.assign_company_topics(
        company_id=company["id"],
        l3_slugs=l3_slugs,
        assigned_by=assigned_by,
    )
    return {
        "company": company_slug,
        "assigned": len(result),
        "topics": [r["l3_slug"] for r in result],
    }


@mcp.tool()
def remove_company_topics(
    company_slug: str,
    l3_slugs: list[str],
) -> dict:
    """Remove L3 technology topic assignments from a company.

    Args:
        company_slug: Target company slug.
        l3_slugs: List of L3 slugs to remove.

    Returns:
        Dict with removal count. Error if company not found.
    """
    repo = _get_repo()
    company = repo.get_company_by_slug(company_slug)
    if not company:
        return {"error": f"Company not found: {company_slug}"}

    removed = repo.remove_company_topics(company_id=company["id"], l3_slugs=l3_slugs)
    return {"company": company_slug, "removed": removed}


if __name__ == "__main__":
    mcp.run()
