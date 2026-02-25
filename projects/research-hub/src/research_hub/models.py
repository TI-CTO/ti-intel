"""Data models for research hub."""

from __future__ import annotations

from datetime import date
from enum import Enum

from pydantic import BaseModel, Field


class ReliabilityTag(str, Enum):
    """Source reliability classification."""

    OFFICIAL = "A"
    REPUTABLE = "B"
    INDICATIVE = "C"
    UNVERIFIED = "D"


class Paper(BaseModel):
    """A cached academic paper record."""

    id: int | None = None
    external_id: str               # e.g. "ss:abc123" or "arxiv:2312.00752"
    source: str                    # semantic_scholar | arxiv
    title: str
    authors: list[str] = Field(default_factory=list)
    published_date: date | None = None
    abstract: str = ""
    citation_count: int = 0
    reliability_tag: ReliabilityTag = ReliabilityTag.OFFICIAL
    raw_url: str | None = None


class PaperTopic(BaseModel):
    """Join record linking a paper to a topic."""

    paper_id: int
    topic_id: int
    relevance: float = 1.0


class PaperStats(BaseModel):
    """Monthly aggregated paper statistics per topic."""

    id: int | None = None
    topic_id: int
    stat_year: int
    stat_month: int                # 1-12
    paper_count: int = 0
    avg_citations: float = 0.0
