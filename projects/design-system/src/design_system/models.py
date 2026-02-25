"""Pydantic models for design system tokens, themes, and slide content."""

from __future__ import annotations

from enum import Enum
from pathlib import Path

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Design Token Models
# ---------------------------------------------------------------------------


class ColorTokens(BaseModel):
    """Color palette tokens."""

    primary: str = "#C50063"
    secondary: str = "#6B21A8"
    accent: str = "#0EA5E9"
    background: str = "#FFFFFF"
    surface: str = "#F8FAFC"
    text: str = "#1F2937"
    text_secondary: str = "#6B7280"
    border: str = "#E5E7EB"
    success: str = "#10B981"
    warning: str = "#F59E0B"
    error: str = "#EF4444"


class TypographyTokens(BaseModel):
    """Typography tokens."""

    font_family: str = "Pretendard"
    font_family_mono: str = "JetBrains Mono"
    title_size: int = 36
    heading_size: int = 28
    subheading_size: int = 20
    body_size: int = 16
    caption_size: int = 12
    title_weight: int = 700
    heading_weight: int = 600
    body_weight: int = 400


class SpacingTokens(BaseModel):
    """Spacing tokens (in points for PPTX)."""

    xs: int = 4
    sm: int = 8
    md: int = 16
    lg: int = 32
    xl: int = 48
    xxl: int = 64


class DesignTokens(BaseModel):
    """Complete set of design tokens."""

    color: ColorTokens = Field(default_factory=ColorTokens)
    typography: TypographyTokens = Field(default_factory=TypographyTokens)
    spacing: SpacingTokens = Field(default_factory=SpacingTokens)


# ---------------------------------------------------------------------------
# Theme Model
# ---------------------------------------------------------------------------


class ThemeInfo(BaseModel):
    """Theme metadata and resolved tokens."""

    name: str
    display_name: str
    description: str
    tokens: DesignTokens


# ---------------------------------------------------------------------------
# Slide Content Models
# ---------------------------------------------------------------------------


class SlideType(str, Enum):
    """Slide layout types mapped from markdown elements."""

    COVER = "cover"
    SECTION = "section"
    BULLET = "bullet"
    TABLE = "table"
    QUOTE = "quote"
    TEXT = "text"
    CLOSING = "closing"


class TableData(BaseModel):
    """Parsed markdown table."""

    headers: list[str]
    rows: list[list[str]]


class SlideContent(BaseModel):
    """Content for a single slide."""

    slide_type: SlideType
    title: str = ""
    subtitle: str = ""
    body: str = ""
    bullets: list[str] = Field(default_factory=list)
    table: TableData | None = None
    quote: str = ""
    note: str = ""


class Presentation(BaseModel):
    """Complete parsed presentation structure."""

    title: str
    subtitle: str = ""
    metadata: dict[str, str] = Field(default_factory=dict)
    slides: list[SlideContent] = Field(default_factory=list)


class RenderResult(BaseModel):
    """Result of rendering a presentation."""

    output_path: Path
    format: str
    theme: str
    slide_count: int
