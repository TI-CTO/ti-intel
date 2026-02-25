"""Data models and enums for telco factbook."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from pathlib import Path

from pydantic import BaseModel


class Carrier(StrEnum):
    """Supported telecom carriers."""

    SKT = "SKT"
    KT = "KT"


class DocType(StrEnum):
    """IR document types."""

    FINANCIAL_STATEMENT = "financial_statement"
    BRIEFING = "briefing"
    PRESS_RELEASE = "press_release"


class PeriodType(StrEnum):
    """Financial period types."""

    QUARTERLY = "quarterly"


class IRDocument(BaseModel):
    """Metadata for a downloadable IR document."""

    carrier: Carrier
    year: int
    quarter: int
    doc_type: DocType
    file_format: str  # "xlsx", "pdf"
    source_url: str
    local_path: Path | None = None
    downloaded_at: datetime | None = None
    file_hash: str | None = None


class FinancialMetrics(BaseModel):
    """Parsed financial metrics from an IR document."""

    carrier: Carrier
    year: int
    quarter: int
    period_type: PeriodType

    # Income statement (million KRW)
    revenue: int | None = None
    operating_income: int | None = None
    net_income: int | None = None
    ebitda: int | None = None

    # Revenue breakdown
    revenue_mobile: int | None = None
    revenue_fixed: int | None = None
    revenue_media: int | None = None
    revenue_enterprise: int | None = None

    # Profitability (%)
    operating_margin: float | None = None
    net_margin: float | None = None

    # Balance sheet
    total_assets: int | None = None
    total_debt: int | None = None
    capex: int | None = None

    # Subscribers
    mobile_subscribers: int | None = None
    mobile_5g_subscribers: int | None = None
    iptv_subscribers: int | None = None
    broadband_subscribers: int | None = None
    arpu_mobile: int | None = None

    # Meta
    source_doc_id: int | None = None
    unit: str = "billion_krw"
    notes: str | None = None


class ParseResult(BaseModel):
    """Result of parsing an Excel financial statement."""

    metrics: FinancialMetrics
    confidence: float  # 0.0 ~ 1.0
    issues: list[ParseIssue] = []


class ParseIssue(BaseModel):
    """A problem encountered during Excel parsing."""

    field_name: str
    raw_value: str | None = None
    issue_type: str  # "format_mismatch", "missing", "ambiguous"
    description: str = ""
