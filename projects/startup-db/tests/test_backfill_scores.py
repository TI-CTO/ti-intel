"""Tests for scripts/backfill_scores.py pure logic functions."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

# Add src and scripts to path so imports resolve without installing
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from backfill_scores import build_score_rows, parse_metadata

# ── parse_metadata ────────────────────────────────────────────────────────────


def test_parse_metadata_dict() -> None:
    """Dict input is returned as-is."""
    meta = {"tech_competitiveness": 3, "other": "value"}
    assert parse_metadata(meta) == meta


def test_parse_metadata_json_string() -> None:
    """JSON string is parsed to dict."""
    meta = {"tech_competitiveness": 4}
    assert parse_metadata(json.dumps(meta)) == meta


def test_parse_metadata_none_returns_empty() -> None:
    """None input returns empty dict."""
    assert parse_metadata(None) == {}


def test_parse_metadata_invalid_string_returns_empty() -> None:
    """Malformed JSON string returns empty dict."""
    assert parse_metadata("not-json") == {}


def test_parse_metadata_non_object_json_returns_empty() -> None:
    """JSON array (not an object) returns empty dict."""
    assert parse_metadata(json.dumps([1, 2, 3])) == {}


# ── build_score_rows ──────────────────────────────────────────────────────────


@pytest.fixture()
def companies_with_tc() -> list[dict]:
    """Companies with valid tech_competitiveness in metadata."""
    return [
        {"id": "c1", "name": "Alpha", "slug": "alpha", "metadata": {"tech_competitiveness": 1}},
        {"id": "c2", "name": "Beta", "slug": "beta", "metadata": {"tech_competitiveness": 3}},
        {"id": "c3", "name": "Gamma", "slug": "gamma", "metadata": {"tech_competitiveness": 5}},
    ]


def test_build_score_rows_conversion(companies_with_tc: list[dict]) -> None:
    """tech_competitiveness is multiplied by 2 to produce tech_strength."""
    rows = build_score_rows(companies_with_tc, set())
    assert len(rows) == 3
    strengths = {r["company_id"]: r["tech_strength"] for r in rows}
    assert strengths["c1"] == 2   # 1 * 2
    assert strengths["c2"] == 6   # 3 * 2
    assert strengths["c3"] == 10  # 5 * 2


def test_build_score_rows_scored_by_and_rationale(companies_with_tc: list[dict]) -> None:
    """Each row has correct scored_by and rationale values."""
    rows = build_score_rows(companies_with_tc, set())
    for row in rows:
        assert row["scored_by"] == "csv_migration"
        assert row["rationale"] == "Initial score from CSV tech_competitiveness field"


def test_build_score_rows_skips_already_scored(companies_with_tc: list[dict]) -> None:
    """Companies whose IDs are in scored_ids are excluded from output."""
    rows = build_score_rows(companies_with_tc, scored_ids={"c1", "c3"})
    assert len(rows) == 1
    assert rows[0]["company_id"] == "c2"


def test_build_score_rows_skips_missing_tc() -> None:
    """Companies without tech_competitiveness in metadata are skipped."""
    companies = [
        {"id": "c1", "name": "No TC", "slug": "no-tc", "metadata": {"other_field": "x"}},
        {"id": "c2", "name": "Null Meta", "slug": "null-meta", "metadata": None},
        {"id": "c3", "name": "Has TC", "slug": "has-tc", "metadata": {"tech_competitiveness": 2}},
    ]
    rows = build_score_rows(companies, set())
    assert len(rows) == 1
    assert rows[0]["company_id"] == "c3"
    assert rows[0]["tech_strength"] == 4


def test_build_score_rows_tc_as_json_string() -> None:
    """tech_competitiveness stored as JSON string in metadata field is handled."""
    companies = [
        {
            "id": "c1",
            "name": "StringMeta",
            "slug": "string-meta",
            "metadata": json.dumps({"tech_competitiveness": 3}),
        }
    ]
    rows = build_score_rows(companies, set())
    assert len(rows) == 1
    assert rows[0]["tech_strength"] == 6


def test_build_score_rows_out_of_range_skipped() -> None:
    """tech_competitiveness values outside 1-5 are skipped."""
    companies = [
        {"id": "c1", "name": "Zero", "slug": "zero", "metadata": {"tech_competitiveness": 0}},
        {"id": "c2", "name": "Six", "slug": "six", "metadata": {"tech_competitiveness": 6}},
        {"id": "c3", "name": "Valid", "slug": "valid", "metadata": {"tech_competitiveness": 4}},
    ]
    rows = build_score_rows(companies, set())
    assert len(rows) == 1
    assert rows[0]["company_id"] == "c3"


def test_build_score_rows_non_integer_tc_skipped() -> None:
    """Non-integer tech_competitiveness values are skipped gracefully."""
    companies = [
        {"id": "c1", "name": "Bad", "slug": "bad", "metadata": {"tech_competitiveness": "high"}},
        {"id": "c2", "name": "Good", "slug": "good", "metadata": {"tech_competitiveness": 2}},
    ]
    rows = build_score_rows(companies, set())
    assert len(rows) == 1
    assert rows[0]["company_id"] == "c2"


def test_build_score_rows_empty_input() -> None:
    """Empty company list returns empty row list."""
    assert build_score_rows([], set()) == []


def test_build_score_rows_all_already_scored(companies_with_tc: list[dict]) -> None:
    """All companies skipped when all are in scored_ids."""
    all_ids = {c["id"] for c in companies_with_tc}
    rows = build_score_rows(companies_with_tc, scored_ids=all_ids)
    assert rows == []
