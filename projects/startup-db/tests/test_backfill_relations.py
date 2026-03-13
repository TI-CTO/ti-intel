"""Tests for scripts/backfill_relations.py pure logic functions."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

# Add src and scripts to path so imports resolve without installing
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from backfill_relations import build_competitor_relations, build_partner_relations

# ── Fixtures ──────────────────────────────────────────────────────────────────


@pytest.fixture()
def companies_same_sub_country() -> list[dict]:
    """Three companies in the same (sub_category, country) bucket."""
    return [
        {"id": "a", "name": "Alpha", "sub_category": "AICC", "country": "한국", "metadata": {}},
        {"id": "b", "name": "Beta", "sub_category": "AICC", "country": "한국", "metadata": {}},
        {"id": "c", "name": "Gamma", "sub_category": "AICC", "country": "한국", "metadata": {}},
    ]


@pytest.fixture()
def companies_mixed() -> list[dict]:
    """Companies spanning different categories and countries."""
    return [
        {"id": "a", "name": "Alpha", "sub_category": "AICC", "country": "한국", "metadata": {}},
        {"id": "b", "name": "Beta", "sub_category": "AICC", "country": "한국", "metadata": {}},
        {"id": "c", "name": "Delta", "sub_category": "Vision", "country": "한국", "metadata": {}},
        {"id": "d", "name": "Echo", "sub_category": "AICC", "country": "미국", "metadata": {}},
    ]


# ── build_competitor_relations ─────────────────────────────────────────────────


class TestBuildCompetitorRelations:
    def test_three_in_same_group_produces_six_rows(
        self, companies_same_sub_country: list[dict]
    ) -> None:
        """3 companies → C(3,2)=3 pairs × 2 directions = 6 rows."""
        relations = build_competitor_relations(companies_same_sub_country)
        assert len(relations) == 6

    def test_all_rows_have_competitor_type(self, companies_same_sub_country: list[dict]) -> None:
        relations = build_competitor_relations(companies_same_sub_country)
        assert all(r["relation_type"] == "competitor" for r in relations)

    def test_bidirectional_pairs_present(self, companies_same_sub_country: list[dict]) -> None:
        """Every forward pair must have a corresponding reverse pair."""
        relations = build_competitor_relations(companies_same_sub_country)
        forward = {(r["company_id"], r["related_company_id"]) for r in relations}
        for cid, rid in list(forward):
            assert (rid, cid) in forward, f"Reverse of ({cid}, {rid}) missing"

    def test_description_contains_sub_category_and_country(
        self, companies_same_sub_country: list[dict]
    ) -> None:
        relations = build_competitor_relations(companies_same_sub_country)
        for r in relations:
            assert "AICC" in r["description"]
            assert "한국" in r["description"]

    def test_description_without_country(self) -> None:
        """When country is empty, description omits the country clause."""
        companies = [
            {"id": "a", "name": "A", "sub_category": "RPA", "country": "", "metadata": {}},
            {"id": "b", "name": "B", "sub_category": "RPA", "country": "", "metadata": {}},
        ]
        relations = build_competitor_relations(companies)
        assert len(relations) == 2
        assert all("in " not in r["description"] for r in relations)

    def test_singleton_group_produces_no_rows(self) -> None:
        """A group with only one company creates no competitor relations."""
        companies = [
            {"id": "x", "name": "Solo", "sub_category": "NLP", "country": "한국", "metadata": {}},
        ]
        assert build_competitor_relations(companies) == []

    def test_missing_sub_category_skipped(self) -> None:
        """Companies without sub_category are excluded from grouping."""
        companies = [
            {"id": "a", "name": "A", "sub_category": None, "country": "한국", "metadata": {}},
            {"id": "b", "name": "B", "sub_category": "", "country": "한국", "metadata": {}},
            {"id": "c", "name": "C", "sub_category": "AICC", "country": "한국", "metadata": {}},
        ]
        assert build_competitor_relations(companies) == []

    def test_different_country_same_sub_category_not_paired(
        self, companies_mixed: list[dict]
    ) -> None:
        """Alpha (한국/AICC) and Echo (미국/AICC) should NOT be competitors."""
        relations = build_competitor_relations(companies_mixed)
        ids_involved = {(r["company_id"], r["related_company_id"]) for r in relations}
        # Only Alpha+Beta (same bucket) should be paired
        assert ("a", "d") not in ids_involved
        assert ("d", "a") not in ids_involved

    def test_two_companies_produce_two_rows(self) -> None:
        """Exactly 2 companies → 1 pair × 2 directions = 2 rows."""
        companies = [
            {"id": "1", "name": "Foo", "sub_category": "X", "country": "KR", "metadata": {}},
            {"id": "2", "name": "Bar", "sub_category": "X", "country": "KR", "metadata": {}},
        ]
        assert len(build_competitor_relations(companies)) == 2

    def test_empty_input(self) -> None:
        assert build_competitor_relations([]) == []


# ── build_partner_relations ────────────────────────────────────────────────────


class TestBuildPartnerRelations:
    def _make_company(self, cid: str, name: str, collaboration: str | None = None) -> dict:
        metadata: dict = {}
        if collaboration is not None:
            metadata["bigtech_collaboration"] = collaboration
        return {
            "id": cid,
            "name": name,
            "sub_category": "X",
            "country": "한국",
            "metadata": metadata,
        }

    def test_matching_name_creates_bidirectional_pair(self) -> None:
        """A collaboration value containing another company's name → 2 rows."""
        companies = [
            self._make_company("a", "AlphaAI", collaboration="Partnership with BetaCorp"),
            self._make_company("b", "BetaCorp"),
        ]
        relations = build_partner_relations(companies)
        assert len(relations) == 2
        assert all(r["relation_type"] == "partner" for r in relations)
        ids = {(r["company_id"], r["related_company_id"]) for r in relations}
        assert ("a", "b") in ids
        assert ("b", "a") in ids

    def test_case_insensitive_match(self) -> None:
        """Name matching is case-insensitive."""
        companies = [
            self._make_company("a", "AlphaAI", collaboration="betacorp alliance"),
            self._make_company("b", "BetaCorp"),
        ]
        relations = build_partner_relations(companies)
        assert len(relations) == 2

    def test_no_collaboration_field_skipped(self) -> None:
        """Companies with no bigtech_collaboration produce no partner relations."""
        companies = [
            self._make_company("a", "AlphaAI"),
            self._make_company("b", "BetaCorp"),
        ]
        assert build_partner_relations(companies) == []

    def test_self_reference_skipped(self) -> None:
        """A company mentioning its own name in collaboration is not self-related."""
        companies = [
            self._make_company("a", "AlphaAI", collaboration="AlphaAI internal notes"),
        ]
        assert build_partner_relations(companies) == []

    def test_no_match_produces_no_rows(self) -> None:
        companies = [
            self._make_company("a", "AlphaAI", collaboration="Google Cloud"),
            self._make_company("b", "BetaCorp"),
        ]
        assert build_partner_relations(companies) == []

    def test_description_contains_collaboration_value(self) -> None:
        companies = [
            self._make_company("a", "AlphaAI", collaboration="BetaCorp cloud deal"),
            self._make_company("b", "BetaCorp"),
        ]
        relations = build_partner_relations(companies)
        for r in relations:
            assert "BetaCorp cloud deal" in r["description"]

    def test_metadata_as_json_string(self) -> None:
        """metadata stored as a JSON string (as serialized by migrate_csv) is parsed."""
        companies = [
            {
                "id": "a",
                "name": "AlphaAI",
                "sub_category": "X",
                "country": "한국",
                "metadata": json.dumps({"bigtech_collaboration": "BetaCorp deal"}),
            },
            self._make_company("b", "BetaCorp"),
        ]
        relations = build_partner_relations(companies)
        assert len(relations) == 2

    def test_empty_collaboration_skipped(self) -> None:
        companies = [
            self._make_company("a", "AlphaAI", collaboration="   "),
            self._make_company("b", "BetaCorp"),
        ]
        assert build_partner_relations(companies) == []

    def test_empty_input(self) -> None:
        assert build_partner_relations([]) == []
