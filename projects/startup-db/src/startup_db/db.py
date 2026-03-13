"""Supabase client and repository for startup-db."""

from __future__ import annotations

import json
import logging
from datetime import date
from typing import Any

from supabase import Client, create_client

from startup_db.config import settings
from startup_db.models import (
    Company,
    CompanyStatus,
    FundingRound,
    Investor,
    RoundType,
)

logger = logging.getLogger(__name__)

_client: Client | None = None


def get_client() -> Client:
    """Return the shared Supabase client, creating it on first call."""
    global _client
    if _client is None:
        _client = create_client(settings.supabase_url, settings.supabase_key)
    return _client


class StartupRepository:
    """Data access layer for startup-db tables."""

    def __init__(self) -> None:
        self._client = get_client()

    # ── Company ──────────────────────────────────────────────

    def upsert_company(self, company: Company) -> dict:
        """Insert or update a company by slug."""
        company.ensure_slug()
        row = _company_to_row(company)
        result = (
            self._client.table("su_companies")
            .upsert(row, on_conflict="slug")
            .execute()
        )
        return result.data[0] if result.data else {}

    def get_company_by_slug(self, slug: str) -> dict | None:
        """Fetch a single company by slug."""
        result = (
            self._client.table("su_companies")
            .select("*")
            .eq("slug", slug)
            .limit(1)
            .execute()
        )
        return result.data[0] if result.data else None

    def get_company_by_id(self, company_id: str) -> dict | None:
        """Fetch a single company by ID."""
        result = (
            self._client.table("su_companies")
            .select("*")
            .eq("id", company_id)
            .limit(1)
            .execute()
        )
        return result.data[0] if result.data else None

    def search_companies(
        self,
        *,
        query: str | None = None,
        main_category: str | None = None,
        sub_category: str | None = None,
        country: str | None = None,
        status: str | None = None,
        tags: list[str] | None = None,
        limit: int = 50,
        offset: int = 0,
    ) -> list[dict]:
        """Search companies with filters."""
        q = self._client.table("su_companies").select("*")

        if query:
            q = q.or_(
                f"name.ilike.%{query}%,description.ilike.%{query}%,"
                f"technology.ilike.%{query}%"
            )
        if main_category:
            q = q.eq("main_category", main_category)
        if sub_category:
            q = q.eq("sub_category", sub_category)
        if country:
            q = q.eq("country", country)
        if status:
            q = q.eq("status", status)
        if tags:
            q = q.overlaps("tags", tags)

        q = q.order("name").range(offset, offset + limit - 1)
        result = q.execute()
        return result.data or []

    def get_company_stats(self) -> dict:
        """Get aggregate statistics about companies."""
        all_companies = (
            self._client.table("su_companies")
            .select("main_category,sub_category,country,status")
            .execute()
        )
        rows = all_companies.data or []
        total = len(rows)

        by_category: dict[str, int] = {}
        by_sub_category: dict[str, int] = {}
        by_country: dict[str, int] = {}
        by_status: dict[str, int] = {}

        for r in rows:
            cat = r.get("main_category") or "unknown"
            by_category[cat] = by_category.get(cat, 0) + 1

            sub = r.get("sub_category") or "unknown"
            by_sub_category[sub] = by_sub_category.get(sub, 0) + 1

            country = r.get("country") or "unknown"
            by_country[country] = by_country.get(country, 0) + 1

            status = r.get("status") or "unknown"
            by_status[status] = by_status.get(status, 0) + 1

        return {
            "total": total,
            "by_category": dict(sorted(by_category.items(), key=lambda x: -x[1])),
            "by_sub_category": dict(sorted(by_sub_category.items(), key=lambda x: -x[1])),
            "by_country": dict(sorted(by_country.items(), key=lambda x: -x[1])),
            "by_status": dict(sorted(by_status.items(), key=lambda x: -x[1])),
        }

    def get_company_detail(self, slug: str) -> dict | None:
        """Get company with funding rounds, people, and latest score."""
        company = self.get_company_by_slug(slug)
        if not company:
            return None

        cid = company["id"]

        # Funding rounds
        rounds = (
            self._client.table("su_funding_rounds")
            .select("*")
            .eq("company_id", cid)
            .order("announced_date", desc=True)
            .execute()
        )
        company["funding_rounds"] = rounds.data or []

        # People
        people_links = (
            self._client.table("su_company_people")
            .select("person_id,role,is_current")
            .eq("company_id", cid)
            .execute()
        )
        if people_links.data:
            person_ids = [p["person_id"] for p in people_links.data]
            people = (
                self._client.table("su_people")
                .select("*")
                .in_("id", person_ids)
                .execute()
            )
            people_map = {p["id"]: p for p in (people.data or [])}
            company["people"] = [
                {
                    **people_map.get(link["person_id"], {}),
                    "role": link["role"],
                    "is_current": link["is_current"],
                }
                for link in people_links.data
                if link["person_id"] in people_map
            ]
        else:
            company["people"] = []

        # Latest score
        score = (
            self._client.table("su_scores")
            .select("*")
            .eq("company_id", cid)
            .order("scored_at", desc=True)
            .limit(1)
            .execute()
        )
        company["latest_score"] = score.data[0] if score.data else None

        return company

    # ── Funding ──────────────────────────────────────────────

    def add_funding_round(
        self,
        round_data: FundingRound,
        investor_ids: list[str] | None = None,
    ) -> dict:
        """Add a funding round and optionally link investors."""
        row = _funding_to_row(round_data)
        result = (
            self._client.table("su_funding_rounds")
            .insert(row)
            .execute()
        )
        if not result.data:
            return {}

        round_record = result.data[0]
        round_id = round_record["id"]

        if investor_ids:
            links = [
                {"round_id": round_id, "investor_id": inv_id, "role": "participant"}
                for inv_id in investor_ids
            ]
            self._client.table("su_round_investors").insert(links).execute()

        return round_record

    # ── Investor ─────────────────────────────────────────────

    def upsert_investor(self, investor: Investor) -> dict:
        """Insert or update an investor by slug."""
        investor.ensure_slug()
        row = _investor_to_row(investor)
        result = (
            self._client.table("su_investors")
            .upsert(row, on_conflict="slug")
            .execute()
        )
        return result.data[0] if result.data else {}

    def get_investor_by_slug(self, slug: str) -> dict | None:
        """Fetch a single investor by slug."""
        result = (
            self._client.table("su_investors")
            .select("*")
            .eq("slug", slug)
            .limit(1)
            .execute()
        )
        return result.data[0] if result.data else None

    # ── People ───────────────────────────────────────────────

    def upsert_person(
        self,
        name: str,
        title: str | None = None,
        organization: str | None = None,
        *,
        company_id: str | None = None,
        role: str | None = None,
    ) -> dict:
        """Insert or update a person, optionally linking to a company."""
        # Check if person already exists by name + organization
        q = self._client.table("su_people").select("*").eq("name", name)
        if organization:
            q = q.eq("organization", organization)
        existing = q.limit(1).execute()

        if existing.data:
            person = existing.data[0]
            updates: dict[str, Any] = {}
            if title and not person.get("title"):
                updates["title"] = title
            if organization and not person.get("organization"):
                updates["organization"] = organization
            if updates:
                self._client.table("su_people").update(updates).eq("id", person["id"]).execute()
                person.update(updates)
        else:
            row = {"name": name}
            if title:
                row["title"] = title
            if organization:
                row["organization"] = organization
            result = self._client.table("su_people").insert(row).execute()
            person = result.data[0] if result.data else {}

        # Link to company
        if company_id and role and person.get("id"):
            link = {
                "company_id": company_id,
                "person_id": person["id"],
                "role": role,
            }
            self._client.table("su_company_people").upsert(
                link, on_conflict="company_id,person_id,role"
            ).execute()

        return person

    # ── Batch operations (for migration) ─────────────────────

    def batch_insert_companies(self, rows: list[dict]) -> list[dict]:
        """Bulk insert company rows."""
        if not rows:
            return []
        result = (
            self._client.table("su_companies")
            .upsert(rows, on_conflict="slug")
            .execute()
        )
        return result.data or []

    def batch_insert_funding_rounds(self, rows: list[dict]) -> list[dict]:
        """Bulk insert funding round rows."""
        if not rows:
            return []
        result = (
            self._client.table("su_funding_rounds")
            .insert(rows)
            .execute()
        )
        return result.data or []

    def batch_insert_people(self, rows: list[dict]) -> list[dict]:
        """Bulk insert people rows."""
        if not rows:
            return []
        result = self._client.table("su_people").insert(rows).execute()
        return result.data or []

    def batch_insert_company_people(self, rows: list[dict]) -> list[dict]:
        """Bulk insert company-people links."""
        if not rows:
            return []
        result = (
            self._client.table("su_company_people")
            .upsert(rows, on_conflict="company_id,person_id,role")
            .execute()
        )
        return result.data or []


# ── Row serialization ────────────────────────────────────────


def _company_to_row(c: Company) -> dict:
    """Convert Company model to a DB row dict."""
    row: dict[str, Any] = {
        "name": c.name,
        "slug": c.slug,
        "status": c.status.value if isinstance(c.status, CompanyStatus) else c.status,
        "tags": c.tags,
        "metadata": json.dumps(c.metadata, ensure_ascii=False) if c.metadata else "{}",
    }
    if c.id:
        row["id"] = c.id
    for field in (
        "description", "website", "logo_url", "founded_date", "main_category",
        "sub_category", "country", "city", "technology", "main_product", "discovery_source",
    ):
        val = getattr(c, field, None)
        if val is not None:
            row[field] = str(val) if isinstance(val, date) else val
    return row


def _funding_to_row(f: FundingRound) -> dict:
    """Convert FundingRound model to a DB row dict."""
    row: dict[str, Any] = {
        "company_id": f.company_id,
        "round_type": f.round_type.value if isinstance(f.round_type, RoundType) else f.round_type,
        "currency": f.currency,
    }
    if f.raised_amount is not None:
        row["raised_amount"] = f.raised_amount
    if f.announced_date:
        row["announced_date"] = str(f.announced_date)
    if f.pre_money_valuation is not None:
        row["pre_money_valuation"] = f.pre_money_valuation
    if f.post_money_valuation is not None:
        row["post_money_valuation"] = f.post_money_valuation
    if f.lead_investor_id:
        row["lead_investor_id"] = f.lead_investor_id
    if f.source_url:
        row["source_url"] = f.source_url
    if f.metadata:
        row["metadata"] = json.dumps(f.metadata, ensure_ascii=False)
    return row


def _investor_to_row(inv: Investor) -> dict:
    """Convert Investor model to a DB row dict."""
    row: dict[str, Any] = {
        "name": inv.name,
        "slug": inv.slug,
    }
    if inv.id:
        row["id"] = inv.id
    if inv.investor_type:
        row["investor_type"] = inv.investor_type.value
    for field in ("description", "website", "country"):
        val = getattr(inv, field, None)
        if val is not None:
            row[field] = val
    row["portfolio_count"] = inv.portfolio_count
    if inv.metadata:
        row["metadata"] = json.dumps(inv.metadata, ensure_ascii=False)
    return row
