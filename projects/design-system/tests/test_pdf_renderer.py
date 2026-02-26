"""Tests for PDF renderer helper functions."""

from design_system.models import DesignTokens, ThemeInfo
from design_system.renderers.pdf import _css_vars, _parse_sections, _postprocess


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_theme(**color_overrides: str) -> ThemeInfo:
    """Build a minimal ThemeInfo for testing."""
    from design_system.models import ColorTokens

    tokens = DesignTokens(color=ColorTokens(**color_overrides))
    return ThemeInfo(
        name="test",
        display_name="Test Theme",
        description="Unit test theme",
        tokens=tokens,
    )


# ---------------------------------------------------------------------------
# _postprocess
# ---------------------------------------------------------------------------


class TestPostprocess:
    def test_plain_table_gets_class(self):
        html = "<table><tr><td>cell</td></tr></table>"
        result = _postprocess(html)
        assert '<table class="data-table">' in result
        assert "<table>" not in result

    def test_multiple_tables(self):
        html = "<table></table><table></table>"
        result = _postprocess(html)
        assert result.count('<table class="data-table">') == 2
        assert "<table>" not in result

    def test_citation_badge_g_prefix(self):
        html = "See [G-01] for details."
        result = _postprocess(html)
        assert '<span class="citation-badge">G-01</span>' in result

    def test_citation_badge_various_prefixes(self):
        """All supported prefixes G N E P T I should be converted."""
        for prefix in ("G", "N", "E", "P", "T", "I"):
            html = f"ref [{prefix}-42]"
            result = _postprocess(html)
            assert f'<span class="citation-badge">{prefix}-42</span>' in result

    def test_no_false_positive_citations(self):
        """Brackets not matching the pattern should be left alone."""
        html = "See [Figure 1] and [table A]."
        result = _postprocess(html)
        assert "citation-badge" not in result
        assert "[Figure 1]" in result

    def test_passthrough_unrelated_html(self):
        html = "<p>No tables or citations here.</p>"
        assert _postprocess(html) == html


# ---------------------------------------------------------------------------
# _parse_sections
# ---------------------------------------------------------------------------


class TestParseSections:
    def test_empty_body_returns_empty(self):
        assert _parse_sections("") == []

    def test_no_h2_returns_empty(self):
        body = "# Title\n\nSome text without h2."
        assert _parse_sections(body) == []

    def test_single_section_title(self):
        body = "## Introduction\n\nSome text."
        sections = _parse_sections(body)
        assert len(sections) == 1
        assert sections[0].title == "Introduction"
        assert sections[0].clean_title == "Introduction"
        assert sections[0].number is None

    def test_numbered_section_extracts_number(self):
        body = "## 1. 기술 현황\n\nContent here."
        sections = _parse_sections(body)
        assert sections[0].number == "1"
        assert sections[0].clean_title == "기술 현황"

    def test_multiple_sections_order(self):
        body = "## Alpha\n\nA.\n\n## Beta\n\nB.\n\n## Gamma\n\nG."
        sections = _parse_sections(body)
        assert [s.title for s in sections] == ["Alpha", "Beta", "Gamma"]

    def test_section_content_between_headings(self):
        body = "## First\n\nfirst content\n\n## Second\n\nsecond content"
        sections = _parse_sections(body)
        assert "first content" in sections[0].html
        assert "second content" in sections[1].html
        # First section must not bleed into second
        assert "second content" not in sections[0].html

    def test_exec_summary_korean(self):
        body = "## 경영진 요약\n\nSome summary."
        sections = _parse_sections(body)
        assert sections[0].is_exec_summary is True
        assert sections[0].is_references is False

    def test_exec_summary_english(self):
        body = "## Executive Summary\n\nSome summary."
        sections = _parse_sections(body)
        assert sections[0].is_exec_summary is True

    def test_references_section(self):
        body = "## References\n\n| # | URL |\n|---|---|\n| 1 | https://x.com |"
        sections = _parse_sections(body)
        assert sections[0].is_references is True
        assert sections[0].is_exec_summary is False

    def test_normal_section_flags_false(self):
        body = "## 1. 시장 분석\n\nContent."
        sections = _parse_sections(body)
        assert sections[0].is_exec_summary is False
        assert sections[0].is_references is False

    def test_html_generated_for_content(self):
        body = "## Section\n\n- item A\n- item B"
        sections = _parse_sections(body)
        assert "<ul>" in sections[0].html or "<li>" in sections[0].html

    def test_table_in_section_gets_data_table_class(self):
        body = "## Data\n\n| A | B |\n|---|---|\n| 1 | 2 |"
        sections = _parse_sections(body)
        assert 'class="data-table"' in sections[0].html

    def test_citation_in_section_becomes_badge(self):
        body = "## Analysis\n\nSee [G-01] for reference."
        sections = _parse_sections(body)
        assert 'citation-badge' in sections[0].html


# ---------------------------------------------------------------------------
# _css_vars
# ---------------------------------------------------------------------------


class TestCssVars:
    def test_output_starts_with_root(self):
        theme = _make_theme()
        css = _css_vars(theme)
        assert css.startswith(":root {")

    def test_output_ends_with_closing_brace(self):
        theme = _make_theme()
        css = _css_vars(theme)
        assert css.strip().endswith("}")

    def test_primary_color_injected(self):
        theme = _make_theme(primary="#C50063")
        css = _css_vars(theme)
        assert "--color-primary: #C50063;" in css

    def test_dark_color_is_secondary_token(self):
        """--color-dark maps to the token's secondary color."""
        theme = _make_theme(secondary="#1E3A5F")
        css = _css_vars(theme)
        assert "--color-dark: #1E3A5F;" in css

    def test_all_required_variables_present(self):
        theme = _make_theme()
        css = _css_vars(theme)
        required = [
            "--color-primary",
            "--color-dark",
            "--color-background",
            "--color-surface",
            "--color-text",
            "--color-text-secondary",
            "--color-border",
            "--font-main",
            "--font-mono",
        ]
        for var in required:
            assert var in css, f"Missing CSS variable: {var}"

    def test_font_family_injected(self):
        theme = _make_theme()
        css = _css_vars(theme)
        assert theme.tokens.typography.font_family in css
        assert theme.tokens.typography.font_family_mono in css
