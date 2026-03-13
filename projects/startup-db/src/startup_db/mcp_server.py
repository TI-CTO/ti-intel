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
    limit: int = 50,
    offset: int = 0,
) -> list[dict]:
    """Search startups by name, category, country, status, or tags.

    Args:
        query: Free-text search across name, description, technology.
        main_category: Filter by main category (e.g. "Service", "Data", "Infra").
        sub_category: Filter by sub-category (e.g. "Work Agent", "Data 증강/ 라벨링").
        country: Filter by country (e.g. "한국", "미국").
        status: Filter by status: active, acquired, ipo, defunct, unknown.
        tags: Filter by overlapping tags (any match).
        limit: Max results (default 50).
        offset: Pagination offset.

    Returns:
        List of company records.
    """
    repo = _get_repo()
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


if __name__ == "__main__":
    mcp.run()
