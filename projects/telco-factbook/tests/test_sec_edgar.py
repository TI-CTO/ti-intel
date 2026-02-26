"""Tests for the SEC EDGAR collector module."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from telco_factbook.collectors.sec_edgar import (
    _CARRIERS,
    _extract_annual_value,
    _extract_value,
    _normalise,
    _normalise_annual,
    fetch_financials,
    get_available_carriers,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def verizon_facts() -> dict:
    """Minimal EDGAR company facts payload for Verizon (2024 Q1)."""
    return {
        "cik": 732712,
        "entityName": "VERIZON COMMUNICATIONS INC",
        "facts": {
            "us-gaap": {
                "Revenues": {
                    "units": {
                        "USD": [
                            {
                                "end": "2024-03-31",
                                "val": 32981000000,
                                "fy": 2024,
                                "fp": "Q1",
                                "form": "10-Q",
                                "filed": "2024-04-22",
                                "accn": "0000732712-24-000019",
                            },
                            {
                                "end": "2023-03-31",
                                "val": 32906000000,
                                "fy": 2023,
                                "fp": "Q1",
                                "form": "10-Q",
                                "filed": "2023-04-25",
                                "accn": "0000732712-23-000017",
                            },
                        ]
                    }
                },
                "OperatingIncomeLoss": {
                    "units": {
                        "USD": [
                            {
                                "end": "2024-03-31",
                                "val": 7200000000,
                                "fy": 2024,
                                "fp": "Q1",
                                "form": "10-Q",
                                "filed": "2024-04-22",
                                "accn": "0000732712-24-000019",
                            }
                        ]
                    }
                },
                "NetIncomeLoss": {
                    "units": {
                        "USD": [
                            {
                                "end": "2024-03-31",
                                "val": 4714000000,
                                "fy": 2024,
                                "fp": "Q1",
                                "form": "10-Q",
                                "filed": "2024-04-22",
                                "accn": "0000732712-24-000019",
                            }
                        ]
                    }
                },
            }
        },
    }


@pytest.fixture
def verizon_annual_facts() -> dict:
    """Minimal EDGAR payload for Verizon 2023 10-K."""
    return {
        "cik": 732712,
        "entityName": "VERIZON COMMUNICATIONS INC",
        "facts": {
            "us-gaap": {
                "Revenues": {
                    "units": {
                        "USD": [
                            {
                                "end": "2023-12-31",
                                "val": 133974000000,
                                "fy": 2023,
                                "fp": "FY",
                                "form": "10-K",
                                "filed": "2024-02-09",
                                "accn": "0000732712-24-000007",
                            }
                        ]
                    }
                },
                "NetIncomeLoss": {
                    "units": {
                        "USD": [
                            {
                                "end": "2023-12-31",
                                "val": 11614000000,
                                "fy": 2023,
                                "fp": "FY",
                                "form": "10-K",
                                "filed": "2024-02-09",
                                "accn": "0000732712-24-000007",
                            }
                        ]
                    }
                },
            }
        },
    }


@pytest.fixture
def empty_facts() -> dict:
    """EDGAR payload with no relevant XBRL concepts."""
    return {
        "cik": 999999999,
        "entityName": "EMPTY CORP",
        "facts": {"us-gaap": {}},
    }


# ---------------------------------------------------------------------------
# Tests: get_available_carriers
# ---------------------------------------------------------------------------


class TestGetAvailableCarriers:
    """Tests for the get_available_carriers function."""

    def test_returns_all_carriers(self) -> None:
        """Should return one entry per carrier in _CARRIERS."""
        carriers = get_available_carriers()
        assert len(carriers) == len(_CARRIERS)

    def test_has_required_keys(self) -> None:
        """Each carrier dict must contain carrier, cik, display_name."""
        for entry in get_available_carriers():
            assert "carrier" in entry
            assert "cik" in entry
            assert "display_name" in entry

    def test_cik_values_match_internal_map(self) -> None:
        """CIK values should match the module-level _CARRIERS dict."""
        carriers = get_available_carriers()
        by_key = {c["carrier"]: c["cik"] for c in carriers}
        assert by_key == _CARRIERS


# ---------------------------------------------------------------------------
# Tests: _extract_value (quarterly)
# ---------------------------------------------------------------------------


class TestExtractValue:
    """Tests for the _extract_value helper."""

    def test_extracts_revenue_in_millions(self, verizon_facts: dict) -> None:
        """Revenue val 32_981_000_000 should convert to 32_981 million USD."""
        value = _extract_value(verizon_facts, "Revenues", 2024, 1)
        assert value == 32_981

    def test_extracts_operating_income(self, verizon_facts: dict) -> None:
        """Operating income should be extracted and converted to millions."""
        value = _extract_value(verizon_facts, "OperatingIncomeLoss", 2024, 1)
        assert value == 7_200

    def test_returns_none_for_missing_concept(self, verizon_facts: dict) -> None:
        """Missing XBRL concept should return None without raising."""
        value = _extract_value(verizon_facts, "NonExistentConcept", 2024, 1)
        assert value is None

    def test_returns_none_for_wrong_year(self, verizon_facts: dict) -> None:
        """No entry for 2099 Q1 — should return None."""
        value = _extract_value(verizon_facts, "Revenues", 2099, 1)
        assert value is None

    def test_returns_none_for_wrong_quarter(self, verizon_facts: dict) -> None:
        """Q2 is not present in fixture — should return None."""
        value = _extract_value(verizon_facts, "Revenues", 2024, 2)
        assert value is None

    def test_ignores_non_10q_forms(self, verizon_facts: dict) -> None:
        """10-K entries should not be returned by _extract_value."""
        # Inject an annual 10-K entry for 2024 Q1 fp — should still be ignored
        verizon_facts["facts"]["us-gaap"]["Revenues"]["units"]["USD"].append(
            {
                "end": "2024-03-31",
                "val": 99_000_000_000,
                "fy": 2024,
                "fp": "Q1",
                "form": "10-K",  # wrong form
                "filed": "2024-04-22",
            }
        )
        # Should still return the 10-Q value
        value = _extract_value(verizon_facts, "Revenues", 2024, 1)
        assert value == 32_981

    def test_empty_facts_returns_none(self, empty_facts: dict) -> None:
        """Payload with no us-gaap data should return None."""
        value = _extract_value(empty_facts, "Revenues", 2024, 1)
        assert value is None

    def test_picks_most_recent_filing(self) -> None:
        """When multiple 10-Q amendments exist, use the most recently filed."""
        facts: dict = {
            "facts": {
                "us-gaap": {
                    "Revenues": {
                        "units": {
                            "USD": [
                                {
                                    "val": 1_000_000_000,
                                    "fy": 2024,
                                    "fp": "Q1",
                                    "form": "10-Q",
                                    "filed": "2024-04-01",
                                },
                                {
                                    "val": 2_000_000_000,  # amended / later filing
                                    "fy": 2024,
                                    "fp": "Q1",
                                    "form": "10-Q",
                                    "filed": "2024-05-01",
                                },
                            ]
                        }
                    }
                }
            }
        }
        value = _extract_value(facts, "Revenues", 2024, 1)
        assert value == 2_000  # most recent


# ---------------------------------------------------------------------------
# Tests: _extract_annual_value
# ---------------------------------------------------------------------------


class TestExtractAnnualValue:
    """Tests for the _extract_annual_value helper."""

    def test_extracts_annual_revenue(self, verizon_annual_facts: dict) -> None:
        """Annual revenue 133_974_000_000 → 133_974 million USD."""
        value = _extract_annual_value(verizon_annual_facts, "Revenues", 2023)
        assert value == 133_974

    def test_extracts_annual_net_income(self, verizon_annual_facts: dict) -> None:
        """Annual net income should be extracted and converted."""
        value = _extract_annual_value(verizon_annual_facts, "NetIncomeLoss", 2023)
        assert value == 11_614

    def test_returns_none_for_missing_year(self, verizon_annual_facts: dict) -> None:
        """No 10-K for 2099 — should return None."""
        value = _extract_annual_value(verizon_annual_facts, "Revenues", 2099)
        assert value is None

    def test_ignores_10q_forms(self, verizon_annual_facts: dict) -> None:
        """10-Q entries should not be returned by _extract_annual_value."""
        value = _extract_annual_value(verizon_annual_facts, "Revenues", 2023)
        # Should only pick the 10-K entry
        assert value == 133_974


# ---------------------------------------------------------------------------
# Tests: _normalise (quarterly)
# ---------------------------------------------------------------------------


class TestNormalise:
    """Tests for the _normalise helper."""

    def test_returns_correct_schema_fields(self, verizon_facts: dict) -> None:
        """Normalised dict must contain all expected schema keys."""
        result = _normalise(verizon_facts, "verizon", 2024, 1)
        assert result is not None
        required_keys = {
            "carrier",
            "year",
            "quarter",
            "unit",
            "revenue",
            "operating_income",
            "net_income",
            "total_assets",
            "capex",
        }
        assert required_keys.issubset(result.keys())

    def test_unit_is_million_usd(self, verizon_facts: dict) -> None:
        """Unit field should always be 'million_usd'."""
        result = _normalise(verizon_facts, "verizon", 2024, 1)
        assert result is not None
        assert result["unit"] == "million_usd"

    def test_revenue_converted(self, verizon_facts: dict) -> None:
        """Revenue should equal the raw val // 1_000_000."""
        result = _normalise(verizon_facts, "verizon", 2024, 1)
        assert result is not None
        assert result["revenue"] == 32_981

    def test_missing_concepts_are_none(self, verizon_facts: dict) -> None:
        """Fields with no EDGAR data should be None, not absent."""
        result = _normalise(verizon_facts, "verizon", 2024, 1)
        assert result is not None
        # total_assets and capex are not in fixture
        assert result["total_assets"] is None
        assert result["capex"] is None

    def test_returns_none_when_no_data(self, empty_facts: dict) -> None:
        """Should return None if no concepts are found."""
        result = _normalise(empty_facts, "verizon", 2024, 1)
        assert result is None

    def test_carrier_year_quarter_metadata(self, verizon_facts: dict) -> None:
        """Carrier, year, quarter metadata should be preserved as-is."""
        result = _normalise(verizon_facts, "att", 2024, 3)
        # The fixture has no Q3 data, so result is None — test with Q1
        result = _normalise(verizon_facts, "verizon", 2024, 1)
        assert result is not None
        assert result["carrier"] == "verizon"
        assert result["year"] == 2024
        assert result["quarter"] == 1

    def test_uses_fallback_concept(self) -> None:
        """Should fall back to secondary concept if primary is absent."""
        facts: dict = {
            "facts": {
                "us-gaap": {
                    # No "Revenues" — only the fallback concept
                    "RevenueFromContractWithCustomerExcludingAssessedTax": {
                        "units": {
                            "USD": [
                                {
                                    "val": 5_000_000_000,
                                    "fy": 2024,
                                    "fp": "Q2",
                                    "form": "10-Q",
                                    "filed": "2024-07-01",
                                }
                            ]
                        }
                    }
                }
            }
        }
        result = _normalise(facts, "tmobile", 2024, 2)
        assert result is not None
        assert result["revenue"] == 5_000


# ---------------------------------------------------------------------------
# Tests: _normalise_annual
# ---------------------------------------------------------------------------


class TestNormaliseAnnual:
    """Tests for the _normalise_annual helper."""

    def test_quarter_is_none(self, verizon_annual_facts: dict) -> None:
        """Annual normalised dict must have quarter=None."""
        result = _normalise_annual(verizon_annual_facts, "verizon", 2023)
        assert result is not None
        assert result["quarter"] is None

    def test_annual_revenue_extracted(self, verizon_annual_facts: dict) -> None:
        """Annual revenue should be converted to millions."""
        result = _normalise_annual(verizon_annual_facts, "verizon", 2023)
        assert result is not None
        assert result["revenue"] == 133_974

    def test_returns_none_when_no_data(self, empty_facts: dict) -> None:
        """Should return None if no annual concepts are found."""
        result = _normalise_annual(empty_facts, "verizon", 2023)
        assert result is None


# ---------------------------------------------------------------------------
# Tests: fetch_financials (integration-level, mocked HTTP)
# ---------------------------------------------------------------------------


class TestFetchFinancials:
    """Tests for the public fetch_financials function (HTTP mocked)."""

    def test_raises_for_unsupported_carrier(self) -> None:
        """Unknown carrier string should raise ValueError immediately."""
        with pytest.raises(ValueError, match="Unsupported carrier"):
            fetch_financials("unknown_carrier", 2024, 1)

    def test_carrier_name_is_case_insensitive(self, verizon_facts: dict) -> None:
        """Carrier argument should be normalised to lowercase."""
        with (
            patch(
                "telco_factbook.collectors.sec_edgar._fetch_company_facts",
                return_value=verizon_facts,
            ),
            patch("telco_factbook.collectors.sec_edgar.time.sleep"),
        ):
            results = fetch_financials("Verizon", 2024, 1)
        assert isinstance(results, list)

    def test_returns_list_of_dicts(self, verizon_facts: dict) -> None:
        """fetch_financials should return a list even for a single result."""
        with (
            patch(
                "telco_factbook.collectors.sec_edgar._fetch_company_facts",
                return_value=verizon_facts,
            ),
            patch("telco_factbook.collectors.sec_edgar.time.sleep"),
        ):
            results = fetch_financials("verizon", 2024, 1)
        assert isinstance(results, list)
        assert len(results) == 1

    def test_quarterly_result_has_quarter_set(self, verizon_facts: dict) -> None:
        """Quarterly fetch should populate the quarter field."""
        with (
            patch(
                "telco_factbook.collectors.sec_edgar._fetch_company_facts",
                return_value=verizon_facts,
            ),
            patch("telco_factbook.collectors.sec_edgar.time.sleep"),
        ):
            results = fetch_financials("verizon", 2024, 1)
        assert results[0]["quarter"] == 1

    def test_annual_fetch_quarter_is_none(self, verizon_annual_facts: dict) -> None:
        """Annual fetch (quarter=None) should return quarter=None in result."""
        with (
            patch(
                "telco_factbook.collectors.sec_edgar._fetch_company_facts",
                return_value=verizon_annual_facts,
            ),
            patch("telco_factbook.collectors.sec_edgar.time.sleep"),
        ):
            results = fetch_financials("verizon", 2023)
        assert len(results) == 1
        assert results[0]["quarter"] is None

    def test_returns_empty_list_when_no_data(self, empty_facts: dict) -> None:
        """When the carrier has no matching period, an empty list is returned."""
        with (
            patch(
                "telco_factbook.collectors.sec_edgar._fetch_company_facts",
                return_value=empty_facts,
            ),
            patch("telco_factbook.collectors.sec_edgar.time.sleep"),
        ):
            results = fetch_financials("att", 2024, 2)
        assert results == []

    def test_request_delay_is_called(self, verizon_facts: dict) -> None:
        """time.sleep should be called once per fetch to respect rate limit."""
        with (
            patch(
                "telco_factbook.collectors.sec_edgar._fetch_company_facts",
                return_value=verizon_facts,
            ),
            patch("telco_factbook.collectors.sec_edgar.time.sleep") as mock_sleep,
        ):
            fetch_financials("verizon", 2024, 1)
        mock_sleep.assert_called_once()

    def test_http_error_propagates(self) -> None:
        """HTTPStatusError from EDGAR should propagate to the caller."""
        import httpx

        with patch(
            "telco_factbook.collectors.sec_edgar._fetch_company_facts",
            side_effect=httpx.HTTPStatusError(
                "404",
                request=MagicMock(),
                response=MagicMock(status_code=404),
            ),
        ):
            with pytest.raises(httpx.HTTPStatusError):
                fetch_financials("verizon", 2024, 1)
