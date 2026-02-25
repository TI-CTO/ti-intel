"""Parse markdown content into slide structures for presentation rendering."""

from __future__ import annotations

import re

from design_system.models import (
    Presentation,
    SlideContent,
    SlideType,
    TableData,
)


def parse_markdown(text: str) -> Presentation:
    """Parse a markdown document into a Presentation with typed slides.

    Mapping rules:
        # H1          → COVER slide (first H1 = title)
        ## H2         → SECTION divider slide
        > blockquote  → QUOTE slide (key message)
        | table |     → TABLE slide
        - list items  → BULLET slide
        plain text    → TEXT slide (body content)
    """
    lines = text.strip().split("\n")
    lines = _strip_frontmatter(lines)

    presentation = Presentation(title="Untitled")
    current_section = ""
    buffer: list[str] = []
    buffer_type: SlideType | None = None

    def flush() -> None:
        """Flush accumulated buffer into a slide."""
        nonlocal buffer, buffer_type
        if not buffer:
            return
        slide = _build_slide(buffer, buffer_type, current_section)
        if slide:
            presentation.slides.append(slide)
        buffer = []
        buffer_type = None

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip empty lines between blocks
        if not stripped:
            if buffer and buffer_type in (SlideType.BULLET, SlideType.TEXT):
                flush()
            i += 1
            continue

        # H1 — Cover slide
        if stripped.startswith("# ") and not stripped.startswith("## "):
            flush()
            title = stripped.lstrip("# ").strip()
            if not presentation.slides and presentation.title == "Untitled":
                presentation.title = title
                presentation.slides.append(
                    SlideContent(
                        slide_type=SlideType.COVER,
                        title=title,
                    )
                )
            else:
                presentation.slides.append(
                    SlideContent(
                        slide_type=SlideType.SECTION,
                        title=title,
                    )
                )
            i += 1
            continue

        # H2 — Section divider
        if stripped.startswith("## "):
            flush()
            current_section = stripped.lstrip("# ").strip()
            presentation.slides.append(
                SlideContent(
                    slide_type=SlideType.SECTION,
                    title=current_section,
                )
            )
            i += 1
            continue

        # H3+ — Treated as subtitle within current context
        if stripped.startswith("### "):
            flush()
            subtitle = stripped.lstrip("# ").strip()
            buffer = [subtitle]
            buffer_type = SlideType.TEXT
            i += 1
            continue

        # Blockquote — Quote slide
        if stripped.startswith("> "):
            if buffer_type != SlideType.QUOTE:
                flush()
                buffer_type = SlideType.QUOTE
            buffer.append(stripped.lstrip("> ").strip())
            i += 1
            continue

        # Table — collect all table lines
        if stripped.startswith("|") and "|" in stripped[1:]:
            if buffer_type != SlideType.TABLE:
                flush()
                buffer_type = SlideType.TABLE
            buffer.append(stripped)
            i += 1
            continue

        # Bullet list
        if re.match(r"^[-*+]\s", stripped) or re.match(r"^\d+\.\s", stripped):
            if buffer_type != SlideType.BULLET:
                flush()
                buffer_type = SlideType.BULLET
            item = re.sub(r"^[-*+]\s|^\d+\.\s", "", stripped).strip()
            buffer.append(item)
            i += 1
            continue

        # Horizontal rule — skip (section divider)
        if stripped in ("---", "***", "___"):
            flush()
            i += 1
            continue

        # Plain text
        if buffer_type != SlideType.TEXT:
            flush()
            buffer_type = SlideType.TEXT
        buffer.append(stripped)
        i += 1

    flush()

    # Add closing slide if not present
    if presentation.slides and presentation.slides[-1].slide_type != SlideType.CLOSING:
        presentation.slides.append(
            SlideContent(
                slide_type=SlideType.CLOSING,
                title="Thank You",
            )
        )

    return presentation


def _strip_frontmatter(lines: list[str]) -> list[str]:
    """Remove YAML frontmatter (--- delimited) from the beginning."""
    if not lines or lines[0].strip() != "---":
        return lines
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[i + 1 :]
    return lines


def _build_slide(
    buffer: list[str],
    slide_type: SlideType | None,
    section: str,
) -> SlideContent | None:
    """Build a SlideContent from accumulated buffer lines."""
    if not buffer or slide_type is None:
        return None

    if slide_type == SlideType.QUOTE:
        return SlideContent(
            slide_type=SlideType.QUOTE,
            title=section,
            quote=" ".join(buffer),
        )

    if slide_type == SlideType.TABLE:
        table = _parse_table(buffer)
        if table:
            return SlideContent(
                slide_type=SlideType.TABLE,
                title=section,
                table=table,
            )
        return None

    if slide_type == SlideType.BULLET:
        return SlideContent(
            slide_type=SlideType.BULLET,
            title=section,
            bullets=buffer,
        )

    if slide_type == SlideType.TEXT:
        title = buffer[0] if len(buffer) > 1 else section
        body = "\n".join(buffer[1:]) if len(buffer) > 1 else buffer[0]
        return SlideContent(
            slide_type=SlideType.TEXT,
            title=title,
            body=body,
        )

    return None


def _parse_table(lines: list[str]) -> TableData | None:
    """Parse markdown table lines into TableData."""
    if len(lines) < 2:
        return None

    def split_row(line: str) -> list[str]:
        cells = line.strip().strip("|").split("|")
        return [c.strip() for c in cells]

    headers = split_row(lines[0])

    # Skip separator row (e.g., |---|---|)
    start = 1
    if start < len(lines) and re.match(r"^\|[\s\-:|]+\|$", lines[start].strip()):
        start = 2

    rows = []
    for line in lines[start:]:
        row = split_row(line)
        if row and any(cell for cell in row):
            rows.append(row)

    if not headers:
        return None

    return TableData(headers=headers, rows=rows)
