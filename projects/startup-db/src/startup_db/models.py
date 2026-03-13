"""Pydantic models for the startup-db schema."""

from __future__ import annotations

import re
import unicodedata
from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, Field


class CompanyStatus(str, Enum):
    """Company lifecycle status."""

    ACTIVE = "active"
    ACQUIRED = "acquired"
    IPO = "ipo"
    DEFUNCT = "defunct"
    UNKNOWN = "unknown"


class RoundType(str, Enum):
    """Funding round type."""

    PRE_SEED = "pre_seed"
    SEED = "seed"
    SERIES_A = "series_a"
    SERIES_B = "series_b"
    SERIES_C = "series_c"
    SERIES_D = "series_d"
    SERIES_E = "series_e"
    SERIES_F = "series_f"
    BRIDGE = "bridge"
    GRANT = "grant"
    IPO = "ipo"
    UNDISCLOSED = "undisclosed"
    OTHER = "other"
    ACQUIRED = "acquired"


class InvestorType(str, Enum):
    """Investor classification."""

    VC = "vc"
    ANGEL = "angel"
    PE = "pe"
    CVC = "cvc"
    ACCELERATOR = "accelerator"
    GOVERNMENT = "government"
    OTHER = "other"


class PersonRole(str, Enum):
    """Person's role at a company."""

    FOUNDER = "founder"
    CEO = "ceo"
    CTO = "cto"
    ADVISOR = "advisor"
    BOARD_MEMBER = "board_member"
    EMPLOYEE = "employee"
    OTHER = "other"


class RelationType(str, Enum):
    """Company-to-company relationship."""

    COMPETITOR = "competitor"
    PARTNER = "partner"
    CUSTOMER = "customer"
    SUPPLIER = "supplier"
    SPIN_OFF = "spin_off"


class SignalType(str, Enum):
    """Intelligence signal type."""

    MENTIONED_IN = "mentioned_in"
    FUNDING_NEWS = "funding_news"
    PATENT_FILED = "patent_filed"
    PARTNERSHIP = "partnership"
    HIRING = "hiring"


# Core models


class Company(BaseModel):
    """A startup company."""

    id: str | None = None
    name: str
    slug: str = ""
    description: str | None = None
    website: str | None = None
    logo_url: str | None = None
    founded_date: date | None = None
    status: CompanyStatus = CompanyStatus.ACTIVE
    main_category: str | None = None
    sub_category: str | None = None
    tags: list[str] = Field(default_factory=list)
    country: str | None = None
    city: str | None = None
    technology: str | None = None
    main_product: str | None = None
    discovery_source: str | None = None
    metadata: dict = Field(default_factory=dict)
    created_at: datetime | None = None
    updated_at: datetime | None = None

    def ensure_slug(self) -> None:
        """Generate slug from name if not set."""
        if not self.slug:
            self.slug = slugify(self.name)


class Person(BaseModel):
    """A person (founder, executive, advisor)."""

    id: str | None = None
    name: str
    title: str | None = None
    organization: str | None = None
    linkedin_url: str | None = None
    email: str | None = None
    bio: str | None = None
    metadata: dict = Field(default_factory=dict)


class Investor(BaseModel):
    """An investor entity."""

    id: str | None = None
    name: str
    slug: str = ""
    investor_type: InvestorType | None = None
    description: str | None = None
    website: str | None = None
    country: str | None = None
    portfolio_count: int = 0
    metadata: dict = Field(default_factory=dict)

    def ensure_slug(self) -> None:
        """Generate slug from name if not set."""
        if not self.slug:
            self.slug = slugify(self.name)


class FundingRound(BaseModel):
    """A single funding round."""

    id: str | None = None
    company_id: str
    round_type: RoundType
    raised_amount: float | None = None
    currency: str = "KRW"
    announced_date: date | None = None
    pre_money_valuation: float | None = None
    post_money_valuation: float | None = None
    lead_investor_id: str | None = None
    source_url: str | None = None
    metadata: dict = Field(default_factory=dict)


class Score(BaseModel):
    """Multi-dimensional company score."""

    id: str | None = None
    company_id: str
    tech_strength: int | None = None
    market_potential: int | None = None
    team_quality: int | None = None
    business_fit: int | None = None
    traction: int | None = None
    overall_score: int | None = None
    scored_by: str | None = None
    rationale: str | None = None
    scored_at: datetime | None = None


# Helpers


def slugify(text: str) -> str:
    """Convert text to a URL-safe slug."""
    text = unicodedata.normalize("NFKD", text)
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


# CSV migration helpers


STAGE_MAP: dict[str, RoundType] = {
    "Seed": RoundType.SEED,
    "Series A": RoundType.SERIES_A,
    "Series A ": RoundType.SERIES_A,
    "Series B": RoundType.SERIES_B,
    "Series C": RoundType.SERIES_C,
    "Series D": RoundType.SERIES_D,
    "Series E": RoundType.SERIES_E,
    "Series F": RoundType.SERIES_F,
    "Series I": RoundType.OTHER,
    "IPO": RoundType.IPO,
    "기타": RoundType.OTHER,
    "인수": RoundType.ACQUIRED,
}


STATUS_MAP: dict[str, CompanyStatus] = {
    "IPO": CompanyStatus.IPO,
    "인수": CompanyStatus.ACQUIRED,
}


def parse_personnel(raw: str) -> list[tuple[str, str]]:
    """Parse key_personnel string into (name, role) pairs.

    Handles formats like:
      '전다형 (CEO)'
      '정영훈(CEO)'
      '김철수 (CEO), 박영희 (CTO)'
    """
    if not raw or not raw.strip():
        return []

    results: list[tuple[str, str]] = []
    parts = re.split(r"[,;/]", raw)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        match = re.match(r"(.+?)\s*[(\uff08](.+?)[)\uff09]", part)
        if match:
            name = match.group(1).strip()
            role = match.group(2).strip()
            results.append((name, role))
        else:
            results.append((part, ""))
    return results


def role_from_title(title: str) -> PersonRole:
    """Map a Korean/English title to a PersonRole enum."""
    t = title.upper().strip()
    if t in ("CEO", "대표", "대표이사"):
        return PersonRole.CEO
    if t in ("CTO", "기술이사"):
        return PersonRole.CTO
    if "FOUNDER" in t or "창업" in t:
        return PersonRole.FOUNDER
    if "ADVISOR" in t or "자문" in t:
        return PersonRole.ADVISOR
    if "BOARD" in t or "이사" in t:
        return PersonRole.BOARD_MEMBER
    return PersonRole.OTHER
