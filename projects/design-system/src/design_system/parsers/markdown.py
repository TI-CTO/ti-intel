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
        # H1          → COVER slide (first H1 = title; immediately following > = subtitle)
        ## H2         → title for the NEXT content slide (not a standalone section)
        > blockquote  → QUOTE slide (key message); but merged into cover/closing when adjacent
        | table |     → TABLE slide
        - list items  → BULLET slide
        plain text    → TEXT slide (body content)

    Section divider slides are only created when ## has no content before the
    next ## (i.e. back-to-back headings or heading at end of document).
    """
    lines = text.strip().split("\n")
    lines = _strip_frontmatter(lines)

    presentation = Presentation(title="Untitled")
    current_section = ""
    buffer: list[str] = []
    buffer_type: SlideType | None = None
    pending_section: str | None = None  # H2 waiting for content

    def flush() -> None:
        """Flush accumulated buffer into a slide."""
        nonlocal buffer, buffer_type, pending_section
        if not buffer:
            return
        # Use pending section title if available
        title = pending_section or current_section
        slide = _build_slide(buffer, buffer_type, title)
        if slide:
            presentation.slides.append(slide)
        buffer = []
        buffer_type = None
        pending_section = None

    def flush_pending_section() -> None:
        """If there's a pending H2 with no content, emit it as a section slide."""
        nonlocal pending_section
        if pending_section is not None:
            presentation.slides.append(
                SlideContent(
                    slide_type=SlideType.SECTION,
                    title=pending_section,
                )
            )
            pending_section = None

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
            flush_pending_section()
            title = stripped.lstrip("# ").strip()
            if not presentation.slides and presentation.title == "Untitled":
                presentation.title = title

                # Look ahead for subtitle (> blockquote immediately after H1)
                subtitle = None
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j < len(lines) and lines[j].strip().startswith("> "):
                    subtitle = lines[j].strip().lstrip("> ").strip()
                    i = j  # skip the subtitle line

                presentation.slides.append(
                    SlideContent(
                        slide_type=SlideType.COVER,
                        title=title,
                        subtitle=subtitle or "",
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

        # H2 — Set as pending section title (don't create a slide yet)
        if stripped.startswith("## "):
            flush()
            flush_pending_section()
            current_section = stripped.lstrip("# ").strip()
            pending_section = current_section
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
    flush_pending_section()

    # Convert trailing quote into closing subtitle if it's the last content
    closing_subtitle = None
    if (
        presentation.slides
        and presentation.slides[-1].slide_type == SlideType.QUOTE
        and presentation.slides[-1].quote
    ):
        last = presentation.slides[-1]
        # Heuristic: short quotes at the end are closing subtitles
        if len(last.quote) < 80:
            closing_subtitle = last.quote
            presentation.slides.pop()

    # Add closing slide
    if presentation.slides and presentation.slides[-1].slide_type != SlideType.CLOSING:
        presentation.slides.append(
            SlideContent(
                slide_type=SlideType.CLOSING,
                title="Thank You",
                subtitle=closing_subtitle or "",
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
