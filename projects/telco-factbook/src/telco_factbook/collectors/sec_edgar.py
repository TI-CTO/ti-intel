"""SEC EDGAR API client for US telecom carrier financial data.

Uses the EDGAR XBRL Company Facts API (no API key required).
Rate limit: 10 req/s — uses _REQUEST_DELAY between calls.
"""

from __future__ import annotations

import logging
import time

import httpx

logger = logging.getLogger(__name__)

_BASE_URL = "https://data.sec.gov/api/xbrl/companyfacts"
_REQUEST_DELAY = 0.5  # seconds between requests (10 req/s limit)
_USER_AGENT = "TechIntelPlatform ctoti@example.com"

# CIK numbers are zero-padded to 10 digits in the EDGAR URL
_CARRIERS: dict[str, str] = {
    "verizon": "0000732712",
    "att": "0000732717",
    "tmobile": "0001283699",
}

# Maps our schema field names to XBRL concept names (primary, then fallbacks).
# The first concept found in the facts payload is used.
_CONCEPT_MAP: dict[str, list[str]] = {
    "revenue": [
        "Revenues",
        "RevenueFromContractWithCustomerExcludingAssessedTax",
        "SalesRevenueNet",
    ],
    "operating_income": [
        "OperatingIncomeLoss",
    ],
    "net_income": [
        "NetIncomeLoss",
    ],
    "total_assets": [
        "Assets",
    ],
    "capex": [
        "PaymentsToAcquirePropertyPlantAndEquipment",
    ],
}


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def get_available_carriers() -> list[dict]:
    """Return metadata for all supported US telecom carriers.

    Returns:
        List of dicts with keys: carrier, cik, display_name.
    """
    _display = {
        "verizon": "Verizon Communications Inc.",
        "att": "AT&T Inc.",
        "tmobile": "T-Mobile US Inc.",
    }
    return [
        {"carrier": key, "cik": cik, "display_name": _display[key]}
        for key, cik in _CARRIERS.items()
    ]


def fetch_financials(
    carrier: str,
    year: int,
    quarter: int | None = None,
) -> list[dict]:
    """Fetch financial metrics for a US carrier from SEC EDGAR.

    Queries the XBRL Company Facts endpoint and extracts key income-statement
    and balance-sheet figures for the requested period.

    Args:
        carrier: Carrier identifier — one of "verizon", "att", "tmobile".
        year: Fiscal year (e.g. 2024).
        quarter: Fiscal quarter 1-4. If None, returns the annual (10-K) filing.

    Returns:
        List of normalised metric dicts.  Usually one element; may be empty
        if the requested period is not found in EDGAR data.

    Raises:
        ValueError: If carrier is not supported.
        httpx.HTTPStatusError: On non-2xx HTTP response from EDGAR.
    """
    carrier = carrier.lower()
    if carrier not in _CARRIERS:
        supported = ", ".join(sorted(_CARRIERS))
        raise ValueError(f"Unsupported carrier '{carrier}'. Choose from: {supported}")

    cik = _CARRIERS[carrier]
    facts = _fetch_company_facts(cik)

    time.sleep(_REQUEST_DELAY)

    if quarter is not None:
        result = _normalise(facts, carrier, year, quarter)
        return [result] if result is not None else []

    # Annual: try Q4 of 10-K form first, fall back to synthesising from facts
    result = _normalise_annual(facts, carrier, year)
    return [result] if result is not None else []


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _fetch_company_facts(cik: str) -> dict:
    """Download company facts JSON from SEC EDGAR.

    Args:
        cik: Zero-padded 10-digit CIK string.

    Returns:
        Parsed JSON response dict.
    """
    url = f"{_BASE_URL}/CIK{cik}.json"
    logger.debug("Fetching EDGAR company facts: %s", url)

    with httpx.Client(
        timeout=30.0,
        headers={"User-Agent": _USER_AGENT},
    ) as client:
        resp = client.get(url)
        resp.raise_for_status()
        data: dict = resp.json()

    logger.debug("Fetched facts for CIK %s (%s)", cik, data.get("entityName", "?"))
    return data


def _extract_value(
    facts: dict,
    concept: str,
    year: int,
    quarter: int,
) -> int | None:
    """Extract a single USD value for a given XBRL concept and period.

    Searches the us-gaap taxonomy for 10-Q filings matching the requested
    year/quarter, and returns the value converted to millions of USD.

    Args:
        facts: Raw company facts dict from EDGAR API.
        concept: XBRL concept name (e.g. "Revenues").
        year: Fiscal year.
        quarter: Fiscal quarter (1-4).

    Returns:
        Value in millions USD (integer), or None if not found.
    """
    us_gaap: dict = facts.get("facts", {}).get("us-gaap", {})
    concept_data = us_gaap.get(concept)
    if not concept_data:
        return None

    fp_label = f"Q{quarter}"
    usd_entries: list[dict] = concept_data.get("units", {}).get("USD", [])

    # Prefer 10-Q entries for the exact period; fall back to instant-type
    candidates = [
        e
        for e in usd_entries
        if e.get("form") == "10-Q" and e.get("fy") == year and e.get("fp") == fp_label
    ]

    if not candidates:
        logger.debug("No 10-Q entry for concept=%s year=%d Q%d", concept, year, quarter)
        return None

    # If multiple filings match, pick the most recently filed one
    candidates.sort(key=lambda e: e.get("filed", ""), reverse=True)
    raw_val = candidates[0].get("val")

    if raw_val is None:
        return None

    # EDGAR values are in raw USD; convert to millions
    return int(raw_val) // 1_000_000


def _extract_annual_value(
    facts: dict,
    concept: str,
    year: int,
) -> int | None:
    """Extract a USD value for an annual (10-K) filing.

    Args:
        facts: Raw company facts dict from EDGAR API.
        concept: XBRL concept name.
        year: Fiscal year.

    Returns:
        Value in millions USD (integer), or None if not found.
    """
    us_gaap: dict = facts.get("facts", {}).get("us-gaap", {})
    concept_data = us_gaap.get(concept)
    if not concept_data:
        return None

    usd_entries: list[dict] = concept_data.get("units", {}).get("USD", [])

    candidates = [
        e
        for e in usd_entries
        if e.get("form") == "10-K" and e.get("fy") == year and e.get("fp") == "FY"
    ]

    if not candidates:
        logger.debug("No 10-K entry for concept=%s year=%d", concept, year)
        return None

    candidates.sort(key=lambda e: e.get("filed", ""), reverse=True)
    raw_val = candidates[0].get("val")

    if raw_val is None:
        return None

    return int(raw_val) // 1_000_000


def _normalise(
    facts: dict,
    carrier: str,
    year: int,
    quarter: int,
) -> dict | None:
    """Convert raw EDGAR facts to our financial metrics schema for a quarter.

    Args:
        facts: Raw company facts dict from EDGAR API.
        carrier: Carrier identifier string.
        year: Fiscal year.
        quarter: Fiscal quarter (1-4).

    Returns:
        Normalised metrics dict, or None if no usable data was found.
    """
    row: dict = {
        "carrier": carrier,
        "year": year,
        "quarter": quarter,
        "unit": "million_usd",
        "revenue": None,
        "operating_income": None,
        "net_income": None,
        "total_assets": None,
        "capex": None,
    }

    found_any = False
    for field, concepts in _CONCEPT_MAP.items():
        for concept in concepts:
            value = _extract_value(facts, concept, year, quarter)
            if value is not None:
                row[field] = value
                found_any = True
                logger.debug(
                    "carrier=%s year=%d Q%d field=%s concept=%s value=%d",
                    carrier,
                    year,
                    quarter,
                    field,
                    concept,
                    value,
                )
                break  # use first matching concept

    if not found_any:
        logger.warning(
            "No EDGAR data found for carrier=%s year=%d Q%d", carrier, year, quarter
        )
        return None

    return row


def _normalise_annual(
    facts: dict,
    carrier: str,
    year: int,
) -> dict | None:
    """Convert raw EDGAR facts to our schema for an annual (10-K) period.

    Args:
        facts: Raw company facts dict from EDGAR API.
        carrier: Carrier identifier string.
        year: Fiscal year.

    Returns:
        Normalised metrics dict with quarter=None, or None if no data found.
    """
    row: dict = {
        "carrier": carrier,
        "year": year,
        "quarter": None,
        "unit": "million_usd",
        "revenue": None,
        "operating_income": None,
        "net_income": None,
        "total_assets": None,
        "capex": None,
    }

    found_any = False
    for field, concepts in _CONCEPT_MAP.items():
        for concept in concepts:
            value = _extract_annual_value(facts, concept, year)
            if value is not None:
                row[field] = value
                found_any = True
                logger.debug(
                    "carrier=%s year=%d annual field=%s concept=%s value=%d",
                    carrier,
                    year,
                    field,
                    concept,
                    value,
                )
                break

    if not found_any:
        logger.warning(
            "No annual EDGAR data found for carrier=%s year=%d", carrier, year
        )
        return None

    return row
