"""Data models for patent intel."""

from __future__ import annotations

from datetime import date
from enum import Enum

from pydantic import BaseModel, Field


class ReliabilityTag(str, Enum):
    """Source reliability classification.

    NOTE: Intentionally duplicated in trend-tracker and research-hub models.
    Projects are architecturally isolated (no cross-project Python imports);
    keep all three definitions in sync.
    """

    OFFICIAL = "A"
    REPUTABLE = "B"
    INDICATIVE = "C"
    UNVERIFIED = "D"


class Patent(BaseModel):
    """A cached patent record."""

    id: int | None = None
    external_id: str              # e.g. "uspto:US11234567B2" or "epo:EP1234567A1"
    source: str                   # uspto | epo | kipris
    title: str
    applicant: str
    filing_date: date | None = None
    publication_date: date | None = None
    ipc_codes: list[str] = Field(default_factory=list)  # IPC classification codes
    abstract: str = ""
    key_highlights: str | None = None
    reliability_tag: ReliabilityTag = ReliabilityTag.OFFICIAL
    raw_url: str | None = None


class PatentTopic(BaseModel):
    """Join record linking a patent to a topic."""

    patent_id: int
    topic_id: int
    relevance: float = 1.0


class PatentStats(BaseModel):
    """Quarterly aggregated patent filing statistics per topic."""

    id: int | None = None
    topic_id: int
    stat_year: int
    stat_quarter: int             # 1-4
    filing_count: int = 0
    top_applicants: list[str] = Field(default_factory=list)
