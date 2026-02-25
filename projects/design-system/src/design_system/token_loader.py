"""Load design tokens from JSON files and merge base + theme overrides."""

from __future__ import annotations

import json
import logging
from pathlib import Path

from design_system.models import (
    ColorTokens,
    DesignTokens,
    SpacingTokens,
    ThemeInfo,
    TypographyTokens,
)

logger = logging.getLogger(__name__)

TOKENS_DIR = Path(__file__).parent / "tokens"
THEMES_DIR = TOKENS_DIR / "themes"


def _extract_values(group: dict) -> dict:
    """Extract $value fields from a W3C DTCG token group into flat key-value pairs."""
    return {
        k: v["$value"]
        for k, v in group.items()
        if isinstance(v, dict) and "$value" in v
    }


def load_base_tokens() -> DesignTokens:
    """Load base design tokens from base.json."""
    base_path = TOKENS_DIR / "base.json"
    with open(base_path, encoding="utf-8") as f:
        raw = json.load(f)

    return DesignTokens(
        color=ColorTokens(**_extract_values(raw.get("color", {}))),
        typography=TypographyTokens(**_extract_values(raw.get("typography", {}))),
        spacing=SpacingTokens(**_extract_values(raw.get("spacing", {}))),
    )


def _merge_token_group(base_dict: dict, override_raw: dict) -> dict:
    """Merge override values into a base token dict."""
    merged = base_dict.copy()
    overrides = _extract_values(override_raw)
    merged.update(overrides)
    return merged


def load_theme(name: str) -> ThemeInfo:
    """Load a theme by name, merging overrides onto base tokens."""
    theme_path = THEMES_DIR / f"{name}.json"
    if not theme_path.exists():
        raise FileNotFoundError(f"Theme not found: {name} (looked at {theme_path})")

    with open(theme_path, encoding="utf-8") as f:
        theme_raw = json.load(f)

    base = load_base_tokens()
    base_dict = base.model_dump()

    merged_color = _merge_token_group(
        base_dict["color"],
        theme_raw.get("color", {}),
    )
    merged_typo = _merge_token_group(
        base_dict["typography"],
        theme_raw.get("typography", {}),
    )
    merged_spacing = _merge_token_group(
        base_dict["spacing"],
        theme_raw.get("spacing", {}),
    )

    tokens = DesignTokens(
        color=ColorTokens(**merged_color),
        typography=TypographyTokens(**merged_typo),
        spacing=SpacingTokens(**merged_spacing),
    )

    return ThemeInfo(
        name=theme_raw.get("name", name),
        display_name=theme_raw.get("display_name", name.title()),
        description=theme_raw.get("description", ""),
        tokens=tokens,
    )


def list_themes() -> list[dict[str, str]]:
    """List all available themes with metadata."""
    themes = []
    for path in sorted(THEMES_DIR.glob("*.json")):
        with open(path, encoding="utf-8") as f:
            raw = json.load(f)
        themes.append(
            {
                "name": raw.get("name", path.stem),
                "display_name": raw.get("display_name", path.stem.title()),
                "description": raw.get("description", ""),
            }
        )
    return themes
