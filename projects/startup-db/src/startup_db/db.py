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
    DealStage,
    FundingRound,
    Investor,
    RoundType,
    Score,  # noqa: F401 — re-exported for callers
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
        result = self._client.table("su_companies").upsert(row, on_conflict="slug").execute()
        return result.data[0] if result.data else {}

    def get_company_by_slug(self, slug: str) -> dict | None:
        """Fetch a single company by slug."""
        result = self._client.table("su_companies").select("*").eq("slug", slug).limit(1).execute()
        return result.data[0] if result.data else None

    def get_company_by_id(self, company_id: str) -> dict | None:
        """Fetch a single company by ID."""
        result = (
            self._client.table("su_companies").select("*").eq("id", company_id).limit(1).execute()
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
        deal_stage: str | None = None,
        limit: int = 50,
        offset: int = 0,
    ) -> list[dict]:
        """Search companies with filters."""
        q = self._client.table("su_companies").select("*")

        if query:
            q = q.or_(
                f"name.ilike.%{query}%,description.ilike.%{query}%,technology.ilike.%{query}%"
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
        if deal_stage:
            q = q.eq("deal_stage", deal_stage)

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
            people = self._client.table("su_people").select("*").in_("id", person_ids).execute()
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

        # Topics
        topics = (
            self._client.table("su_company_topics")
            .select("l3_slug,assigned_by,assigned_at")
            .eq("company_id", cid)
            .order("l3_slug")
            .execute()
        )
        company["topics"] = topics.data or []

        return company

    # ── Funding ──────────────────────────────────────────────

    def add_funding_round(
        self,
        round_data: FundingRound,
        investor_ids: list[str] | None = None,
    ) -> dict:
        """Add a funding round and optionally link investors."""
        row = _funding_to_row(round_data)
        result = self._client.table("su_funding_rounds").insert(row).execute()
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
        result = self._client.table("su_investors").upsert(row, on_conflict="slug").execute()
        return result.data[0] if result.data else {}

    def get_investor_by_slug(self, slug: str) -> dict | None:
        """Fetch a single investor by slug."""
        result = self._client.table("su_investors").select("*").eq("slug", slug).limit(1).execute()
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

    # ── Scoring ───────────────────────────────────────────────

    def score_company(
        self,
        company_id: str,
        tech_strength: float | None = None,
        market_potential: float | None = None,
        team_quality: float | None = None,
        business_fit: float | None = None,
        traction: float | None = None,
        overall_score: float | None = None,
        scored_by: str | None = None,
        rationale: str | None = None,
    ) -> dict:
        """Insert a score record for a company.

        Args:
            company_id: UUID of the company to score.
            tech_strength: Technology strength score (0–10).
            market_potential: Market potential score (0–10).
            team_quality: Team quality score (0–10).
            business_fit: Business fit score (0–10).
            traction: Traction score (0–10).
            overall_score: Composite overall score (0–10).
            scored_by: Identifier of the scorer (user, agent name, etc.).
            rationale: Free-text explanation for the scores.

        Returns:
            The created score row as a dict.
        """
        row: dict[str, Any] = {"company_id": company_id}
        for field, val in (
            ("tech_strength", tech_strength),
            ("market_potential", market_potential),
            ("team_quality", team_quality),
            ("business_fit", business_fit),
            ("traction", traction),
            ("overall_score", overall_score),
            ("scored_by", scored_by),
            ("rationale", rationale),
        ):
            if val is not None:
                row[field] = val
        result = self._client.table("su_scores").insert(row).execute()
        return result.data[0] if result.data else {}

    # ── Company Relations ─────────────────────────────────────

    def add_company_relation(
        self,
        company_id: str,
        related_company_id: str,
        relation_type: str,
        description: str | None = None,
    ) -> dict:
        """Upsert a directional relation between two companies.

        Args:
            company_id: UUID of the source company.
            related_company_id: UUID of the related company.
            relation_type: Type of relation (e.g. 'competitor', 'partner', 'customer').
            description: Optional free-text description of the relation.

        Returns:
            The upserted relation row as a dict.
        """
        row: dict[str, Any] = {
            "company_id": company_id,
            "related_company_id": related_company_id,
            "relation_type": relation_type,
        }
        if description is not None:
            row["description"] = description
        result = (
            self._client.table("su_company_relations")
            .upsert(row, on_conflict="company_id,related_company_id,relation_type")
            .execute()
        )
        return result.data[0] if result.data else {}

    # ── Investor Search & Portfolio ───────────────────────────

    def search_investors(
        self,
        query: str | None = None,
        investor_type: str | None = None,
        country: str | None = None,
        limit: int = 50,
        offset: int = 0,
    ) -> list[dict]:
        """Search investors with optional text and attribute filters.

        Args:
            query: Free-text search applied to investor name and description.
            investor_type: Filter by investor type (e.g. 'vc', 'angel', 'cvc').
            country: Filter by country code / name.
            limit: Maximum number of results to return.
            offset: Number of results to skip (for pagination).

        Returns:
            List of matching investor rows ordered by name.
        """
        q = self._client.table("su_investors").select("*")
        if query:
            q = q.or_(f"name.ilike.%{query}%,description.ilike.%{query}%")
        if investor_type:
            q = q.eq("investor_type", investor_type)
        if country:
            q = q.eq("country", country)
        q = q.order("name").range(offset, offset + limit - 1)
        result = q.execute()
        return result.data or []

    def get_investor_portfolio(self, investor_id: str) -> list[dict]:
        """Return companies that received funding from a given investor.

        Performs a three-step join:
        su_round_investors → su_funding_rounds → su_companies.

        Args:
            investor_id: UUID of the investor.

        Returns:
            List of company dicts, each augmented with a ``funding_rounds``
            key containing only the rounds where this investor participated.
        """
        # Step 1: round IDs for this investor
        ri_result = (
            self._client.table("su_round_investors")
            .select("round_id")
            .eq("investor_id", investor_id)
            .execute()
        )
        round_ids = [r["round_id"] for r in (ri_result.data or [])]
        if not round_ids:
            return []

        # Step 2: funding rounds → company_ids
        rounds_result = (
            self._client.table("su_funding_rounds").select("*").in_("id", round_ids).execute()
        )
        rounds = rounds_result.data or []
        company_ids = list({r["company_id"] for r in rounds})
        if not company_ids:
            return []

        # Step 3: companies
        companies_result = (
            self._client.table("su_companies").select("*").in_("id", company_ids).execute()
        )
        companies = companies_result.data or []

        # Attach relevant rounds to each company
        rounds_by_company: dict[str, list[dict]] = {}
        for r in rounds:
            rounds_by_company.setdefault(r["company_id"], []).append(r)

        for company in companies:
            company["funding_rounds"] = rounds_by_company.get(company["id"], [])

        return companies

    # ── Funding Stats ─────────────────────────────────────────

    def get_funding_stats(self) -> dict:
        """Aggregate statistics across all funding rounds.

        Fetches all su_funding_rounds joined with su_companies and computes:
        - total_rounds and total_raised
        - breakdown by round type
        - breakdown by year (from announced_date)
        - breakdown by company main_category

        Returns:
            Dict with keys: total_rounds, total_raised, by_round_type,
            by_year, by_category.
        """
        # Fetch rounds with company main_category
        rounds_result = (
            self._client.table("su_funding_rounds")
            .select("id,round_type,raised_amount,announced_date,company_id")
            .execute()
        )
        rounds = rounds_result.data or []

        # Fetch company categories
        company_ids = list({r["company_id"] for r in rounds if r.get("company_id")})
        category_map: dict[str, str] = {}
        if company_ids:
            companies_result = (
                self._client.table("su_companies")
                .select("id,main_category")
                .in_("id", company_ids)
                .execute()
            )
            for c in companies_result.data or []:
                category_map[c["id"]] = c.get("main_category") or "unknown"

        total_rounds = len(rounds)
        total_raised = 0.0
        by_round_type: dict[str, dict[str, Any]] = {}
        by_year: dict[str, dict[str, Any]] = {}
        by_category: dict[str, dict[str, Any]] = {}

        for r in rounds:
            amount = r.get("raised_amount") or 0
            total_raised += amount

            # by round type
            rt = r.get("round_type") or "unknown"
            bucket = by_round_type.setdefault(rt, {"count": 0, "total_raised": 0.0})
            bucket["count"] += 1
            bucket["total_raised"] += amount

            # by year
            announced = r.get("announced_date")
            year = str(announced)[:4] if announced else "unknown"
            ybucket = by_year.setdefault(year, {"count": 0, "total_raised": 0.0})
            ybucket["count"] += 1
            ybucket["total_raised"] += amount

            # by category
            cat = category_map.get(r.get("company_id", ""), "unknown")
            cbucket = by_category.setdefault(cat, {"count": 0, "total_raised": 0.0})
            cbucket["count"] += 1
            cbucket["total_raised"] += amount

        return {
            "total_rounds": total_rounds,
            "total_raised": total_raised,
            "by_round_type": dict(sorted(by_round_type.items(), key=lambda x: -x[1]["count"])),
            "by_year": dict(sorted(by_year.items())),
            "by_category": dict(sorted(by_category.items(), key=lambda x: -x[1]["count"])),
        }

    # ── Collections ───────────────────────────────────────────

    def manage_collection(
        self,
        action: str,
        name: str | None = None,
        collection_id: str | None = None,
        description: str | None = None,
        collection_type: str | None = None,
        company_ids: list[str] | None = None,
    ) -> dict | list[dict]:
        """CRUD operations for collections and their items.

        Args:
            action: One of 'create', 'get', 'add_items', 'remove_items',
                'list', 'delete'.
            name: Collection name (required for 'create').
            collection_id: UUID of the collection (required for most actions
                except 'create' and 'list').
            description: Optional description (used in 'create').
            collection_type: Optional type tag (used in 'create').
            company_ids: List of company UUIDs (used in 'add_items' /
                'remove_items').

        Returns:
            For 'list': list of collection dicts with item counts.
            For all other actions: a single dict describing the result.

        Raises:
            ValueError: If a required argument is missing for the given action.
        """
        if action == "create":
            if not name:
                raise ValueError("'name' is required for action='create'")
            row: dict[str, Any] = {"name": name}
            if description:
                row["description"] = description
            if collection_type:
                row["collection_type"] = collection_type
            result = self._client.table("su_collections").insert(row).execute()
            return result.data[0] if result.data else {}

        if action == "list":
            collections_result = (
                self._client.table("su_collections").select("*").order("name").execute()
            )
            collections = collections_result.data or []
            for col in collections:
                count_result = (
                    self._client.table("su_collection_items")
                    .select("id", count="exact")
                    .eq("collection_id", col["id"])
                    .execute()
                )
                col["item_count"] = count_result.count or 0
            return collections

        if not collection_id:
            raise ValueError(f"'collection_id' is required for action='{action}'")

        if action == "get":
            col_result = (
                self._client.table("su_collections")
                .select("*")
                .eq("id", collection_id)
                .limit(1)
                .execute()
            )
            if not col_result.data:
                return {}
            collection = col_result.data[0]

            items_result = (
                self._client.table("su_collection_items")
                .select("company_id,added_at")
                .eq("collection_id", collection_id)
                .execute()
            )
            items = items_result.data or []
            if items:
                cids = [i["company_id"] for i in items]
                companies_result = (
                    self._client.table("su_companies")
                    .select("id,name,slug,main_category")
                    .in_("id", cids)
                    .execute()
                )
                company_map = {c["id"]: c for c in (companies_result.data or [])}
                collection["items"] = [
                    {**company_map.get(i["company_id"], {}), "added_at": i["added_at"]}
                    for i in items
                    if i["company_id"] in company_map
                ]
            else:
                collection["items"] = []
            return collection

        if action == "add_items":
            if not company_ids:
                return {"added": 0}
            rows = [{"collection_id": collection_id, "company_id": cid} for cid in company_ids]
            result = (
                self._client.table("su_collection_items")
                .upsert(rows, on_conflict="collection_id,company_id")
                .execute()
            )
            return {"added": len(result.data or [])}

        if action == "remove_items":
            if not company_ids:
                return {"removed": 0}
            result = (
                self._client.table("su_collection_items")
                .delete()
                .eq("collection_id", collection_id)
                .in_("company_id", company_ids)
                .execute()
            )
            return {"removed": len(result.data or [])}

        if action == "delete":
            self._client.table("su_collections").delete().eq("id", collection_id).execute()
            return {"deleted": collection_id}

        raise ValueError(f"Unknown action: '{action}'")

    # ── People Search ─────────────────────────────────────────

    def search_people(
        self,
        query: str | None = None,
        organization: str | None = None,
        role: str | None = None,
        limit: int = 50,
        offset: int = 0,
    ) -> list[dict]:
        """Search people with optional text and attribute filters.

        When *role* is specified, only people linked to at least one company
        with that role (via su_company_people) are returned.

        Args:
            query: Free-text search applied to name, title, and organization.
            organization: Filter by exact organization name.
            role: Filter by role in su_company_people (e.g. 'founder', 'ceo').
            limit: Maximum number of results to return.
            offset: Number of results to skip (for pagination).

        Returns:
            List of matching person rows ordered by name.
        """
        if role:
            # Collect person_ids that have the requested role
            role_result = (
                self._client.table("su_company_people")
                .select("person_id")
                .eq("role", role)
                .execute()
            )
            person_ids = list({r["person_id"] for r in (role_result.data or [])})
            if not person_ids:
                return []
            q = self._client.table("su_people").select("*").in_("id", person_ids)
        else:
            q = self._client.table("su_people").select("*")

        if query:
            q = q.or_(f"name.ilike.%{query}%,title.ilike.%{query}%,organization.ilike.%{query}%")
        if organization:
            q = q.eq("organization", organization)

        q = q.order("name").range(offset, offset + limit - 1)
        result = q.execute()
        return result.data or []

    # ── Company Topics ────────────────────────────────────────

    def assign_company_topics(
        self,
        company_id: str,
        l3_slugs: list[str],
        assigned_by: str | None = None,
    ) -> list[dict]:
        """Assign L3 topic slugs to a company.

        Args:
            company_id: UUID of the company.
            l3_slugs: List of L3 technology slugs to assign.
            assigned_by: Who performed the assignment.

        Returns:
            List of upserted topic rows.
        """
        if not l3_slugs:
            return []
        rows = [
            {
                "company_id": company_id,
                "l3_slug": slug,
                "assigned_by": assigned_by,
            }
            for slug in l3_slugs
        ]
        result = (
            self._client.table("su_company_topics")
            .upsert(rows, on_conflict="company_id,l3_slug")
            .execute()
        )
        return result.data or []

    def remove_company_topics(
        self,
        company_id: str,
        l3_slugs: list[str],
    ) -> int:
        """Remove L3 topic assignments from a company.

        Args:
            company_id: UUID of the company.
            l3_slugs: List of L3 slugs to remove.

        Returns:
            Number of rows deleted.
        """
        if not l3_slugs:
            return 0
        result = (
            self._client.table("su_company_topics")
            .delete()
            .eq("company_id", company_id)
            .in_("l3_slug", l3_slugs)
            .execute()
        )
        return len(result.data or [])

    def get_company_topics(self, company_id: str) -> list[dict]:
        """Get all topic assignments for a company.

        Args:
            company_id: UUID of the company.

        Returns:
            List of topic rows with l3_slug, assigned_by, assigned_at.
        """
        result = (
            self._client.table("su_company_topics")
            .select("*")
            .eq("company_id", company_id)
            .order("l3_slug")
            .execute()
        )
        return result.data or []

    def search_companies_by_topics(
        self,
        l3_slugs: list[str],
        limit: int = 50,
        offset: int = 0,
    ) -> list[dict]:
        """Search companies that have any of the given L3 topic assignments.

        Args:
            l3_slugs: L3 slugs to filter by.
            limit: Maximum results.
            offset: Pagination offset.

        Returns:
            List of company dicts.
        """
        if not l3_slugs:
            return []

        # Get company IDs from topics table
        topics_result = (
            self._client.table("su_company_topics")
            .select("company_id")
            .in_("l3_slug", l3_slugs)
            .execute()
        )
        company_ids = list({r["company_id"] for r in (topics_result.data or [])})
        if not company_ids:
            return []

        result = (
            self._client.table("su_companies")
            .select("*")
            .in_("id", company_ids)
            .order("name")
            .range(offset, offset + limit - 1)
            .execute()
        )
        return result.data or []

    # ── Batch operations (for migration) ─────────────────────

    def batch_insert_companies(self, rows: list[dict]) -> list[dict]:
        """Bulk insert company rows."""
        if not rows:
            return []
        result = self._client.table("su_companies").upsert(rows, on_conflict="slug").execute()
        return result.data or []

    def batch_insert_funding_rounds(self, rows: list[dict]) -> list[dict]:
        """Bulk insert funding round rows."""
        if not rows:
            return []
        result = self._client.table("su_funding_rounds").insert(rows).execute()
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
        "description",
        "website",
        "logo_url",
        "founded_date",
        "main_category",
        "sub_category",
        "country",
        "city",
        "technology",
        "main_product",
        "discovery_source",
    ):
        val = getattr(c, field, None)
        if val is not None:
            row[field] = str(val) if isinstance(val, date) else val
    if c.deal_stage is not None:
        ds = c.deal_stage
        row["deal_stage"] = ds.value if isinstance(ds, DealStage) else ds
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
