"""Tests for markdown to slide structure parsing."""

from design_system.models import SlideType
from design_system.parsers.markdown import parse_markdown


SAMPLE_MD = """\
---
topic: Test Report
date: 2026-02-24
---

# Test Presentation Title

## Section One

This is body text for section one.

- First bullet point
- Second bullet point
- Third bullet point

## Section Two

> This is an important quote that should become a quote slide.

### Data Table

| Column A | Column B | Column C |
|----------|----------|----------|
| Row 1A   | Row 1B   | Row 1C   |
| Row 2A   | Row 2B   | Row 2C   |

## 한글 섹션

- 첫 번째 항목
- 두 번째 항목
"""


class TestMarkdownParser:
    def test_parse_title(self):
        pres = parse_markdown(SAMPLE_MD)
        assert pres.title == "Test Presentation Title"

    def test_frontmatter_stripped(self):
        pres = parse_markdown(SAMPLE_MD)
        # Title should not be "topic: Test Report"
        assert "topic" not in pres.title

    def test_cover_slide_created(self):
        pres = parse_markdown(SAMPLE_MD)
        assert pres.slides[0].slide_type == SlideType.COVER
        assert pres.slides[0].title == "Test Presentation Title"

    def test_section_slides_created(self):
        pres = parse_markdown(SAMPLE_MD)
        sections = [s for s in pres.slides if s.slide_type == SlideType.SECTION]
        section_titles = [s.title for s in sections]
        assert "Section One" in section_titles
        assert "Section Two" in section_titles

    def test_bullet_slide(self):
        pres = parse_markdown(SAMPLE_MD)
        bullets = [s for s in pres.slides if s.slide_type == SlideType.BULLET]
        assert len(bullets) >= 1
        assert "First bullet point" in bullets[0].bullets

    def test_quote_slide(self):
        pres = parse_markdown(SAMPLE_MD)
        quotes = [s for s in pres.slides if s.slide_type == SlideType.QUOTE]
        assert len(quotes) >= 1
        assert "important quote" in quotes[0].quote

    def test_table_slide(self):
        pres = parse_markdown(SAMPLE_MD)
        tables = [s for s in pres.slides if s.slide_type == SlideType.TABLE]
        assert len(tables) >= 1
        table = tables[0].table
        assert table is not None
        assert "Column A" in table.headers
        assert len(table.rows) == 2

    def test_korean_content(self):
        pres = parse_markdown(SAMPLE_MD)
        sections = [s for s in pres.slides if s.slide_type == SlideType.SECTION]
        assert any("한글" in s.title for s in sections)

    def test_closing_slide_appended(self):
        pres = parse_markdown(SAMPLE_MD)
        assert pres.slides[-1].slide_type == SlideType.CLOSING

    def test_empty_markdown(self):
        pres = parse_markdown("")
        assert pres.title == "Untitled"
        # Empty markdown produces no slides
        assert len(pres.slides) == 0

    def test_no_frontmatter(self):
        md = "# Simple Title\n\nSome content."
        pres = parse_markdown(md)
        assert pres.title == "Simple Title"
