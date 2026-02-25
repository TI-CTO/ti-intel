"""Data models for trend tracking."""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, Field


class ReliabilityTag(str, Enum):
    """Source reliability classification."""

    OFFICIAL = "A"
    REPUTABLE = "B"
    INDICATIVE = "C"
    UNVERIFIED = "D"


class NewsItem(BaseModel):
    """A collected news article or web content."""

    id: int | None = None
    title: str
    source: str
    url: str
    published_date: date | None = None
    collected_date: date = Field(default_factory=date.today)
    topic_id: int
    summary: str = ""
    reliability_tag: ReliabilityTag = ReliabilityTag.INDICATIVE
    keywords: list[str] = Field(default_factory=list)


class TrendSnapshot(BaseModel):
    """A periodic snapshot of a topic's trend status."""

    id: int | None = None
    topic_id: int
    snapshot_date: date = Field(default_factory=date.today)
    source_type: str = "news"  # news | papers | patents | combined
    summary: str
    key_signals: list[str] = Field(default_factory=list)
    item_count: int = 0
    sentiment: str = "neutral"
    change_level: str = "none"  # none | minor | notable | urgent


class WatchTopic(BaseModel):
    """A topic registered for periodic monitoring."""

    id: int | None = None
    topic_id: int
    keywords: list[str] = Field(default_factory=list)
    frequency: str = "weekly"  # daily | weekly | monthly
    is_active: bool = True
    last_scanned: datetime | None = None
    created_at: datetime | None = None
