"""Unit tests for Phase 2 StartupRepository methods (no real DB required)."""

from __future__ import annotations

from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from startup_db.db import StartupRepository

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_repo() -> tuple[StartupRepository, MagicMock]:
    """Return a repository instance whose Supabase client is fully mocked."""
    mock_client = MagicMock()
    with patch("startup_db.db.get_client", return_value=mock_client):
        repo = StartupRepository()
    return repo, mock_client


def _chain(*return_value: Any) -> MagicMock:
    """Build a fluent mock chain that returns *return_value* from .execute()."""
    mock_execute = MagicMock()
    mock_execute.return_value = return_value[0] if return_value else MagicMock()

    chain = MagicMock()
    # Every attribute access and call returns the same chain object,
    # except for .execute() which returns the preset value.
    chain.execute = mock_execute
    chain.__getattr__ = lambda self, name: chain  # noqa: ARG001
    chain.return_value = chain
    return chain


def _result(data: list[dict] | None, count: int | None = None) -> MagicMock:
    """Create a mock Supabase result object."""
    r = MagicMock()
    r.data = data or []
    r.count = count
    return r


# ---------------------------------------------------------------------------
# score_company
# ---------------------------------------------------------------------------


class TestScoreCompany:
    def test_inserts_row_with_all_fields(self) -> None:
        repo, client = _make_repo()
        expected = {"id": "s1", "company_id": "c1", "overall_score": 8.0}
        client.table.return_value.insert.return_value.execute.return_value = _result([expected])

        result = repo.score_company(
            company_id="c1",
            tech_strength=9.0,
            market_potential=8.5,
            team_quality=7.0,
            business_fit=8.0,
            traction=6.5,
            overall_score=8.0,
            scored_by="analyst-agent",
            rationale="Strong tech, moderate traction.",
        )

        assert result == expected
        insert_call_args = client.table.return_value.insert.call_args[0][0]
        assert insert_call_args["company_id"] == "c1"
        assert insert_call_args["overall_score"] == 8.0
        assert insert_call_args["scored_by"] == "analyst-agent"

    def test_omits_none_fields(self) -> None:
        repo, client = _make_repo()
        client.table.return_value.insert.return_value.execute.return_value = _result(
            [{"id": "s2", "company_id": "c1"}]
        )

        repo.score_company(company_id="c1", overall_score=7.5)

        inserted = client.table.return_value.insert.call_args[0][0]
        assert "tech_strength" not in inserted
        assert inserted["overall_score"] == 7.5

    def test_returns_empty_dict_when_no_data(self) -> None:
        repo, client = _make_repo()
        client.table.return_value.insert.return_value.execute.return_value = _result([])

        result = repo.score_company(company_id="c1")

        assert result == {}


# ---------------------------------------------------------------------------
# add_company_relation
# ---------------------------------------------------------------------------


class TestAddCompanyRelation:
    def test_upserts_relation(self) -> None:
        repo, client = _make_repo()
        expected = {"id": "r1", "company_id": "c1", "related_company_id": "c2"}
        client.table.return_value.upsert.return_value.execute.return_value = _result([expected])

        result = repo.add_company_relation(
            company_id="c1",
            related_company_id="c2",
            relation_type="competitor",
            description="Direct competitor in APAC.",
        )

        assert result == expected
        upserted = client.table.return_value.upsert.call_args[0][0]
        assert upserted["relation_type"] == "competitor"
        assert upserted["description"] == "Direct competitor in APAC."

    def test_description_omitted_when_none(self) -> None:
        repo, client = _make_repo()
        client.table.return_value.upsert.return_value.execute.return_value = _result([{"id": "r2"}])

        repo.add_company_relation("c1", "c2", "partner")

        upserted = client.table.return_value.upsert.call_args[0][0]
        assert "description" not in upserted


# ---------------------------------------------------------------------------
# search_investors
# ---------------------------------------------------------------------------


class TestSearchInvestors:
    def test_returns_matching_rows(self) -> None:
        repo, client = _make_repo()
        rows = [{"id": "i1", "name": "SoftBank Ventures"}]

        # Build a simple fluent chain mock
        mock_q = MagicMock()
        mock_q.or_.return_value = mock_q
        mock_q.eq.return_value = mock_q
        mock_q.order.return_value = mock_q
        mock_q.range.return_value = mock_q
        mock_q.execute.return_value = _result(rows)
        client.table.return_value.select.return_value = mock_q

        result = repo.search_investors(query="SoftBank", investor_type="vc", country="JP")

        assert result == rows

    def test_returns_empty_list_when_no_data(self) -> None:
        repo, client = _make_repo()
        mock_q = MagicMock()
        mock_q.order.return_value = mock_q
        mock_q.range.return_value = mock_q
        mock_q.execute.return_value = _result([])
        client.table.return_value.select.return_value = mock_q

        result = repo.search_investors()

        assert result == []


# ---------------------------------------------------------------------------
# get_investor_portfolio
# ---------------------------------------------------------------------------


class TestGetInvestorPortfolio:
    def test_returns_empty_list_when_no_rounds(self) -> None:
        repo, client = _make_repo()
        # su_round_investors returns nothing
        client.table.return_value.select.return_value.eq.return_value.execute.return_value = (
            _result([])
        )

        result = repo.get_investor_portfolio("inv-1")

        assert result == []

    def test_builds_portfolio_with_rounds(self) -> None:
        repo, client = _make_repo()
        ri_rows = [{"round_id": "round-1"}]
        round_rows = [{"id": "round-1", "company_id": "co-1", "round_type": "Series A"}]
        company_rows = [{"id": "co-1", "name": "Acme Corp"}]

        table_mock = MagicMock()
        client.table.return_value = table_mock

        # Three sequential calls to .execute()
        execute_results = [
            _result(ri_rows),
            _result(round_rows),
            _result(company_rows),
        ]
        call_count = 0

        def execute_side_effect():
            nonlocal call_count
            res = execute_results[call_count]
            call_count += 1
            return res

        # Build a chain mock where every method returns itself and execute() cycles
        chain = MagicMock()
        chain.execute.side_effect = execute_side_effect
        chain.select.return_value = chain
        chain.eq.return_value = chain
        chain.in_.return_value = chain
        table_mock.select.return_value = chain
        table_mock.return_value = table_mock

        client.table.return_value = chain

        result = repo.get_investor_portfolio("inv-1")

        assert len(result) == 1
        assert result[0]["name"] == "Acme Corp"
        assert result[0]["funding_rounds"] == round_rows


# ---------------------------------------------------------------------------
# get_funding_stats
# ---------------------------------------------------------------------------


class TestGetFundingStats:
    def test_aggregates_correctly(self) -> None:
        repo, client = _make_repo()
        round_rows = [
            {
                "id": "r1",
                "round_type": "Seed",
                "raised_amount": 500_000,
                "announced_date": "2024-06-01",
                "company_id": "c1",
            },
            {
                "id": "r2",
                "round_type": "Series A",
                "raised_amount": 5_000_000,
                "announced_date": "2024-09-15",
                "company_id": "c2",
            },
        ]
        company_rows = [
            {"id": "c1", "main_category": "AI"},
            {"id": "c2", "main_category": "Fintech"},
        ]

        execute_results = [_result(round_rows), _result(company_rows)]
        call_count = 0

        chain = MagicMock()

        def execute_side_effect():
            nonlocal call_count
            res = execute_results[call_count]
            call_count += 1
            return res

        chain.execute.side_effect = execute_side_effect
        chain.select.return_value = chain
        chain.in_.return_value = chain
        client.table.return_value = chain

        stats = repo.get_funding_stats()

        assert stats["total_rounds"] == 2
        assert stats["total_raised"] == 5_500_000
        assert stats["by_round_type"]["Seed"]["count"] == 1
        assert stats["by_year"]["2024"]["count"] == 2
        assert stats["by_category"]["AI"]["total_raised"] == 500_000


# ---------------------------------------------------------------------------
# manage_collection
# ---------------------------------------------------------------------------


class TestManageCollection:
    def test_create_inserts_row(self) -> None:
        repo, client = _make_repo()
        expected = {"id": "col-1", "name": "Watchlist"}
        client.table.return_value.insert.return_value.execute.return_value = _result([expected])

        result = repo.manage_collection(action="create", name="Watchlist", description="My list")

        assert result == expected

    def test_create_raises_without_name(self) -> None:
        repo, _ = _make_repo()

        with pytest.raises(ValueError, match="'name' is required"):
            repo.manage_collection(action="create")

    def test_list_attaches_item_counts(self) -> None:
        repo, client = _make_repo()
        collections = [{"id": "col-1", "name": "A"}, {"id": "col-2", "name": "B"}]

        call_count = 0
        results = [
            _result(collections),
            _result([], count=3),
            _result([], count=0),
        ]

        chain = MagicMock()

        def execute_side_effect():
            nonlocal call_count
            res = results[call_count]
            call_count += 1
            return res

        chain.execute.side_effect = execute_side_effect
        chain.select.return_value = chain
        chain.order.return_value = chain
        chain.eq.return_value = chain
        client.table.return_value = chain

        result = repo.manage_collection(action="list")

        assert isinstance(result, list)
        assert result[0]["item_count"] == 3
        assert result[1]["item_count"] == 0

    def test_add_items_returns_count(self) -> None:
        repo, client = _make_repo()
        client.table.return_value.upsert.return_value.execute.return_value = _result(
            [{"id": "ci1"}, {"id": "ci2"}]
        )

        result = repo.manage_collection(
            action="add_items", collection_id="col-1", company_ids=["c1", "c2"]
        )

        assert result == {"added": 2}

    def test_remove_items_returns_count(self) -> None:
        repo, client = _make_repo()
        del_chain = MagicMock()
        del_chain.eq.return_value = del_chain
        del_chain.in_.return_value = del_chain
        del_chain.execute.return_value = _result([{"id": "ci1"}])
        client.table.return_value.delete.return_value = del_chain

        result = repo.manage_collection(
            action="remove_items", collection_id="col-1", company_ids=["c1"]
        )

        assert result == {"removed": 1}

    def test_delete_returns_id(self) -> None:
        repo, client = _make_repo()
        client.table.return_value.delete.return_value.eq.return_value.execute.return_value = (
            _result([])
        )

        result = repo.manage_collection(action="delete", collection_id="col-1")

        assert result == {"deleted": "col-1"}

    def test_unknown_action_raises(self) -> None:
        repo, _ = _make_repo()

        with pytest.raises(ValueError, match="Unknown action"):
            repo.manage_collection(action="explode", collection_id="col-1")

    def test_missing_collection_id_raises(self) -> None:
        repo, _ = _make_repo()

        with pytest.raises(ValueError, match="'collection_id' is required"):
            repo.manage_collection(action="get")


# ---------------------------------------------------------------------------
# search_people
# ---------------------------------------------------------------------------


class TestSearchPeople:
    def test_returns_all_people_without_filters(self) -> None:
        repo, client = _make_repo()
        rows = [{"id": "p1", "name": "Alice"}]
        mock_q = MagicMock()
        mock_q.or_.return_value = mock_q
        mock_q.eq.return_value = mock_q
        mock_q.order.return_value = mock_q
        mock_q.range.return_value = mock_q
        mock_q.execute.return_value = _result(rows)
        client.table.return_value.select.return_value = mock_q

        result = repo.search_people()

        assert result == rows

    def test_role_filter_returns_empty_when_no_match(self) -> None:
        repo, client = _make_repo()
        mock_q = MagicMock()
        mock_q.eq.return_value = mock_q
        mock_q.execute.return_value = _result([])
        client.table.return_value.select.return_value = mock_q

        result = repo.search_people(role="cfo")

        assert result == []
