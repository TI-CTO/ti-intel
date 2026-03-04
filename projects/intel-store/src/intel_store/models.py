"""Pydantic models for the unified intel_items schema."""

from __future__ import annotations

import hashlib
from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, Field


class ItemType(str, Enum):
    """Intel item type discriminator."""

    NEWS = "news"
    PAPER = "paper"
    PATENT = "patent"
    STATEMENT = "statement"
    REPORT = "report"
    STANDARD = "standard"


class ReliabilityTag(str, Enum):
    """Source reliability classification.

    A = official announcement / peer-reviewed journal
    B = reputable media / established source
    C = general / indicative
    D = unverified / rumour
    """

    OFFICIAL = "A"
    REPUTABLE = "B"
    INDICATIVE = "C"
    UNVERIFIED = "D"


class Language(str, Enum):
    """Content language."""

    EN = "en"
    KO = "ko"
    MIXED = "mixed"


class AssignedBy(str, Enum):
    """How a topic was linked to an item."""

    COLLECTOR = "collector"
    EMBEDDING = "embedding"
    MANUAL = "manual"


class RelationType(str, Enum):
    """Relationship between two intel items."""

    CITES = "cites"
    MENTIONS = "mentions"
    SAME_EVENT = "same_event"
    UPDATES = "updates"
    CONTRADICTS = "contradicts"


# ── Type-specific metadata models ────────────────────────────────────


class NewsMetadata(BaseModel):
    """JSONB metadata for news items."""

    keywords: list[str] = Field(default_factory=list)
    collector: str = ""  # "tavily", "gdelt"


class PaperMetadata(BaseModel):
    """JSONB metadata for academic papers."""

    authors: list[str] = Field(default_factory=list)
    citation_count: int = 0
    venue: str = ""


class PatentMetadata(BaseModel):
    """JSONB metadata for patents."""

    applicant: str = ""
    filing_date: str | None = None
    ipc_codes: list[str] = Field(default_factory=list)


class StatementMetadata(BaseModel):
    """JSONB metadata for corporate/person statements."""

    speaker: str = ""
    organization: str = ""
    event: str = ""


class ReportMetadata(BaseModel):
    """JSONB metadata for report sections."""

    report_path: str = ""
    section: str = ""


class StandardMetadata(BaseModel):
    """JSONB metadata for standards/regulations."""

    organization: str = ""
    standard_id: str = ""


# ── Core models ──────────────────────────────────────────────────────


class IntelItem(BaseModel):
    """A unified intelligence item stored in intel_items table."""

    id: int | None = None
    item_type: ItemType
    external_id: str | None = None
    content_hash: str = ""
    title: str
    abstract: str = ""
    source_name: str
    source_url: str | None = None
    published_date: date | None = None
    collected_date: date = Field(default_factory=date.today)
    language: Language = Language.EN
    reliability: ReliabilityTag = ReliabilityTag.INDICATIVE
    metadata: dict = Field(default_factory=dict)
    embedding: list[float] | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    def compute_content_hash(self) -> str:
        """Compute SHA-256 hash of title + abstract[:200] for deduplication."""
        text = self.title + (self.abstract or "")[:200]
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    def ensure_content_hash(self) -> None:
        """Set content_hash if not already computed."""
        if not self.content_hash:
            self.content_hash = self.compute_content_hash()

    def embedding_input(self) -> str:
        """Build the text for embedding generation with passage prefix."""
        return f"passage: {self.title}. {self.abstract or ''}"


class IntelItemTopic(BaseModel):
    """Link between an intel item and a topic."""

    item_id: int
    topic_id: int
    relevance: float = 1.0
    assigned_by: AssignedBy = AssignedBy.COLLECTOR


class IntelItemRelation(BaseModel):
    """Directional relationship between two intel items."""

    source_id: int
    target_id: int
    relation_type: RelationType
    confidence: float = 1.0
    created_at: datetime | None = None


# ── Helper: build IntelItem from collector output ────────────────────


def news_from_collector(raw: dict, *, topic_id: int | None = None) -> IntelItem:
    """Convert a news collector dict to an IntelItem."""
    return IntelItem(
        item_type=ItemType.NEWS,
        external_id=raw.get("url"),
        title=raw["title"],
        abstract=raw.get("summary") or "",
        source_name=raw.get("source", "unknown"),
        source_url=raw.get("url"),
        published_date=_parse_date(raw.get("published_date")),
        reliability=raw.get("reliability_tag", "C"),
        metadata=NewsMetadata(
            keywords=raw.get("keywords", []),
            collector=raw.get("collector", ""),
        ).model_dump(),
    )


def paper_from_collector(raw: dict) -> IntelItem:
    """Convert a paper collector dict to an IntelItem."""
    return IntelItem(
        item_type=ItemType.PAPER,
        external_id=raw.get("external_id"),
        title=raw["title"],
        abstract=raw.get("abstract") or "",
        source_name=raw.get("source", "semantic_scholar"),
        source_url=raw.get("raw_url"),
        published_date=_parse_date(raw.get("published_date")),
        reliability=raw.get("reliability_tag", "A"),
        metadata=PaperMetadata(
            authors=raw.get("authors", []),
            citation_count=raw.get("citation_count", 0),
            venue=raw.get("venue", ""),
        ).model_dump(),
    )


def patent_from_collector(raw: dict) -> IntelItem:
    """Convert a patent collector dict to an IntelItem."""
    return IntelItem(
        item_type=ItemType.PATENT,
        external_id=raw.get("external_id"),
        title=raw["title"],
        abstract=raw.get("abstract") or "",
        source_name=raw.get("source", "uspto"),
        source_url=raw.get("raw_url"),
        published_date=_parse_date(raw.get("publication_date")),
        reliability=raw.get("reliability_tag", "A"),
        metadata=PatentMetadata(
            applicant=raw.get("applicant", ""),
            filing_date=raw.get("filing_date"),
            ipc_codes=raw.get("ipc_codes", []),
        ).model_dump(),
    )


def _parse_date(value: str | date | None) -> date | None:
    """Parse a date string (YYYY-MM-DD) or pass through a date object."""
    if value is None:
        return None
    if isinstance(value, date):
        return value
    try:
        return date.fromisoformat(str(value)[:10])
    except (ValueError, TypeError):
        return None
