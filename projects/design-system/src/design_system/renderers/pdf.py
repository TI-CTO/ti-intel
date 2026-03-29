"""PDF renderer — converts WTIS markdown reports to consulting-style PDFs.

Uses Playwright (headless Chromium) for HTML-to-PDF conversion.
Runs Playwright in a thread pool to avoid conflicts with the async MCP event loop.
"""

from __future__ import annotations

import concurrent.futures
import logging
import re
from dataclasses import dataclass
from pathlib import Path

import frontmatter
import mistune
from jinja2 import Environment, FileSystemLoader

from design_system.models import Presentation, RenderResult, ThemeInfo, ValidationSummary
from design_system.renderers.base import BaseRenderer

logger = logging.getLogger(__name__)

_ASSETS_DIR = Path(__file__).parent.parent / "assets"
_TEMPLATES_DIR = _ASSETS_DIR / "templates"
_STYLES_DIR = _ASSETS_DIR / "styles"
_PAGEDJS_PATH = _ASSETS_DIR / "js" / "paged.polyfill.min.js"

_EXEC_SUMMARY_KEYS = ("경영진 요약", "Executive Summary")
_REFERENCES_KEYS = ("References", "참조", "Reference")


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------


@dataclass
class TocEntry:
    """Single TOC item with anchor ID."""

    level: int  # 2 = h2 section, 3 = h3 sub-section
    title: str
    anchor: str


@dataclass
class ReportSection:
    """Parsed section from a WTIS markdown report."""

    title: str
    clean_title: str
    number: str | None
    html: str
    is_exec_summary: bool = False
    is_references: bool = False


# ---------------------------------------------------------------------------
# Markdown → HTML helpers
# ---------------------------------------------------------------------------


def _make_md() -> mistune.Markdown:
    return mistune.create_markdown(plugins=["table", "strikethrough"])


def _preprocess(md_text: str) -> str:
    """Pre-process markdown before mistune parsing.

    Handles:
      1. Citation double-brackets: [[G-06-S]](#ref-g-06-s) → [G-06-S](#ref-g-06-s)
         (mistune cannot parse nested brackets with hyphenated suffixes)
      2. Obsidian wikilinks: [[path/to/file]] → [file](path/to/file)
    """
    # Step 1: Flatten citation double-bracket links to single-bracket
    # [[G-01]](#ref-g-01) → [G-01](#ref-g-01)
    # [[G-06-S]](#ref-g-06-s) → [G-06-S](#ref-g-06-s)
    _cid = r"[A-Z]+-\d+(?:-[A-Za-z]+)?"
    md_text = re.sub(
        rf"\[\[({_cid})\]\]\((#ref-[^)]+)\)",
        r"[\1](\2)",
        md_text,
    )

    def _replace_wikilink(m: re.Match) -> str:
        inner = m.group(1)
        # Skip citation patterns like [G-01], [G-06-S] — not wikilinks
        if re.match(r"^[A-Z]+-\d+(?:-[A-Za-z]+)?$", inner):
            return m.group(0)
        if "|" in inner:
            path, alias = inner.split("|", 1)
            return f"[{alias.strip()}]({path.strip()})"
        # Use last path segment as display text
        display = inner.strip().rsplit("/", 1)[-1]
        return f"[{display}]({inner.strip()})"

    return re.sub(r"\[\[([^\]]+)\]\]", _replace_wikilink, md_text)


def _split_large_tables(html: str, max_rows: int = 30) -> str:
    """Split large tables into smaller chunks to work around paged.js duplication bug.

    paged.js has a known issue where tables spanning multiple pages get duplicated.
    This splits any table with more than max_rows into multiple tables, each with
    the same thead, so paged.js can handle them without duplication.
    """
    def _split_table(match: re.Match) -> str:
        full = match.group(0)
        thead_m = re.search(r"<thead>(.*?)</thead>", full, re.DOTALL)
        tbody_m = re.search(r"<tbody>(.*?)</tbody>", full, re.DOTALL)
        if not thead_m or not tbody_m:
            return full

        thead = thead_m.group(0)
        rows = re.findall(r"<tr>.*?</tr>", tbody_m.group(1), re.DOTALL)
        if len(rows) <= max_rows:
            return full

        # Extract wrapper div attrs
        wrapper_prefix = match.group(1) if match.group(1) else ""
        table_tag = re.search(r"<table[^>]*>", full)
        table_open = table_tag.group(0) if table_tag else "<table>"

        # Avoid orphan chunks and unnecessary splits
        min_orphan = 8
        total = len(rows)
        remainder = total % max_rows
        if remainder == 0:
            chunk_size = max_rows
        elif total <= max_rows + min_orphan:
            # Only slightly over threshold — don't split at all
            chunk_size = total
        elif remainder < min_orphan:
            # Would create a tiny orphan — split evenly instead
            n_chunks = (total + max_rows - 1) // max_rows
            chunk_size = (total + n_chunks - 1) // n_chunks
        else:
            chunk_size = max_rows

        chunks: list[str] = []
        for i in range(0, len(rows), chunk_size):
            chunk_rows = rows[i : i + chunk_size]
            chunk = (
                f'{table_open}\n{thead}\n<tbody>\n'
                + "\n".join(chunk_rows)
                + "\n</tbody>\n</table>"
            )
            chunks.append(chunk)

        return "</div>\n".join(
            f'<div class="table-wrapper">{c}' for c in chunks
        ) + "</div>"

    return re.sub(
        r'(<div class="table-wrapper">)\s*(<table[^>]*>.*?</table>)\s*</div>',
        _split_table,
        html,
        flags=re.DOTALL,
    )


def _postprocess(html: str) -> str:
    """Add CSS class to tables, wrap in div, and convert citation refs to styled badges."""
    html = re.sub(
        r"<table>", '<div class="table-wrapper"><table class="data-table">', html
    )
    html = re.sub(r"</table>", "</table></div>", html)
    # Add wide-table class to tables with 5+ columns
    def _add_wide_class(m: re.Match) -> str:
        table_html = m.group(0)
        th_count = len(re.findall(r"<th\b", table_html.split("</tr>")[0]))
        if th_count >= 5:
            return table_html.replace(
                'class="data-table"', 'class="data-table wide-table"', 1
            )
        return table_html
    html = re.sub(
        r'<table class="data-table">.*?</table>',
        _add_wide_class,
        html,
        flags=re.DOTALL,
    )
    # Move bold text before table into <caption> (displayed below table via CSS)
    html = re.sub(
        r"<p><strong>(.*?)</strong></p>\s*(<div class=\"table-wrapper\"><table class=\"data-table\">)",
        r'\2<caption>&lt; \1 &gt;</caption>',
        html,
    )
    # NOTE: h3→caption 변환은 References 섹션 전용으로 _postprocess_references()에서 수행.
    # 본문 h3("플레이어 동향" 등)이 삼켜지는 버그 방지를 위해 여기서는 수행하지 않는다.
    # Citation ID pattern: G-01, P-03, G-13-S, G-01-C (optional hyphen-suffix)
    _cid = r"[A-Z]+-\d+(?:-[A-Za-z]+)?"
    # Case 1a: mistune converted [[G-01]](#ref-g-01) → <a href="#ref-...">[G-01]</a>
    html = re.sub(
        rf'<a href="(#ref-[^"]*)">\[({_cid})\]</a>',
        r'<a href="\1" class="citation-badge">\2</a>',
        html,
    )
    # Case 1b: mistune converted [S-01](#ref-s-01) → <a href="#ref-...">S-01</a> (no brackets)
    html = re.sub(
        rf'<a href="(#ref-[^"]*)">({_cid})</a>',
        r'<a href="\1" class="citation-badge">\2</a>',
        html,
    )
    # Case 2: raw [G-01] or [G-01b] not yet parsed by mistune (no link target)
    html = re.sub(
        rf"\[({_cid})\]",
        r'<span class="citation-badge">\1</span>',
        html,
    )
    # Restore escaped <a id="..."> anchor tags (mistune escapes raw HTML in table cells)
    html = re.sub(
        r"&lt;a id=&quot;([^&]+)&quot;&gt;&lt;/a&gt;",
        r'<a id="\1"></a>',
        html,
    )
    # Convert bare URLs to clickable links (skip URLs already inside href="...")
    html = re.sub(
        r'(?<!href=")(https?://[^\s<,|"]+)',
        r'<a href="\1" target="_blank">\1</a>',
        html,
    )
    return html


def _build_toc(
    exec_summary: ReportSection | None,
    main_sections: list[ReportSection],
    has_references: bool,
) -> list[TocEntry]:
    """Build table of contents from section structure.

    Extracts h2 (sections) and h3 (sub-sections) for a 2-level TOC.
    Generates stable anchor IDs for cross-linking.
    """
    entries: list[TocEntry] = []
    counter = 0

    if exec_summary:
        entries.append(TocEntry(level=2, title="Executive Summary", anchor="toc-exec"))

    for section in main_sections:
        counter += 1
        sec_anchor = f"toc-s{counter}"
        entries.append(TocEntry(level=2, title=section.clean_title, anchor=sec_anchor))

        # Extract h3 sub-headings from section HTML
        h3_matches = re.findall(r"<h3>(.*?)</h3>", section.html)
        for j, h3_title in enumerate(h3_matches, 1):
            # Strip HTML tags from title (e.g. <strong>)
            clean = re.sub(r"<[^>]+>", "", h3_title).strip()
            entries.append(
                TocEntry(level=3, title=clean, anchor=f"{sec_anchor}-{j}")
            )

    if has_references:
        entries.append(TocEntry(level=2, title="References", anchor="toc-refs"))

    return entries


def _inject_toc_anchors(
    exec_summary: ReportSection | None,
    main_sections: list[ReportSection],
    toc: list[TocEntry],
) -> None:
    """Inject anchor IDs into section HTML so TOC links work."""
    sec_idx = 0

    # Skip exec summary entry in TOC
    if exec_summary:
        sec_idx = 1  # toc[0] = Executive Summary

    for section in main_sections:
        # Find this section's TOC entry
        sec_entry = next((e for e in toc[sec_idx:] if e.level == 2), None)
        if not sec_entry:
            break
        sec_idx = toc.index(sec_entry)

        # Get h3 entries for this section
        h3_entries = []
        for e in toc[sec_idx + 1 :]:
            if e.level == 2:
                break
            h3_entries.append(e)

        # Inject anchor IDs into h3 tags in section HTML
        h3_idx = 0

        def _add_h3_anchor(m: re.Match) -> str:
            nonlocal h3_idx
            if h3_idx < len(h3_entries):
                anchor = h3_entries[h3_idx].anchor
                h3_idx += 1
                return f'<h3 id="{anchor}">{m.group(1)}</h3>'
            return m.group(0)

        section.html = re.sub(r"<h3>(.*?)</h3>", _add_h3_anchor, section.html)
        sec_idx += 1 + len(h3_entries)


def _postprocess_references(html: str) -> str:
    """References 섹션 전용 후처리: h3 heading을 table caption으로 변환."""
    html = re.sub(
        r"<h3>(.*?)</h3>\s*(<div class=\"table-wrapper\"><table class=\"data-table\">)",
        r'\2<caption>&lt; \1 &gt;</caption>',
        html,
    )
    return html


# ---------------------------------------------------------------------------
# Section parser
# ---------------------------------------------------------------------------


def _parse_sections(body: str) -> list[ReportSection]:
    """Split markdown body into sections on ## headings."""
    pattern = re.compile(r"^## (.+)$", re.MULTILINE)
    matches = list(pattern.finditer(body))
    if not matches:
        return []

    md = _make_md()
    sections: list[ReportSection] = []

    for i, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        content = body[start:end].strip()

        # Extract leading number, e.g. "1. 기술 현황" → number="1", clean="기술 현황"
        num_match = re.match(r"^(\d+)\.\s*(.+)$", title)
        if num_match:
            number: str | None = num_match.group(1)
            clean_title = num_match.group(2).strip()
        else:
            number = None
            clean_title = title

        html = _postprocess(md(_preprocess(content)))

        is_references = any(k in title for k in _REFERENCES_KEYS)
        if is_references:
            html = _postprocess_references(html)

        sections.append(
            ReportSection(
                title=title,
                clean_title=clean_title,
                number=number,
                html=html,
                is_exec_summary=any(k in title for k in _EXEC_SUMMARY_KEYS),
                is_references=is_references,
            )
        )

    return sections


# ---------------------------------------------------------------------------
# CSS variable injection
# ---------------------------------------------------------------------------


def _css_vars(theme: ThemeInfo) -> str:
    """Build a CSS :root block from theme tokens (overrides stylesheet defaults)."""
    t = theme.tokens
    return (
        ":root {\n"
        f"  --color-primary: {t.color.primary};\n"
        f"  --color-dark: {t.color.secondary};\n"
        f"  --color-background: {t.color.background};\n"
        f"  --color-surface: {t.color.surface};\n"
        f"  --color-text: {t.color.text};\n"
        f"  --color-text-secondary: {t.color.text_secondary};\n"
        f"  --color-border: {t.color.border};\n"
        f"  --font-main: '{t.typography.font_family}', "
        "'Apple SD Gothic Neo', 'Malgun Gothic', 'Noto Sans KR', sans-serif;\n"
        f"  --font-mono: '{t.typography.font_family_mono}', monospace;\n"
        "}\n"
    )


# ---------------------------------------------------------------------------
# paged.js injection
# ---------------------------------------------------------------------------


def _build_pagedjs_script() -> str:
    """Build paged.js inline script block for template injection."""
    if not _PAGEDJS_PATH.exists():
        logger.warning("paged.js bundle not found at %s", _PAGEDJS_PATH)
        return ""
    pagedjs_bundle = _PAGEDJS_PATH.read_text(encoding="utf-8")
    return (
        '<script>window.PagedConfig = { auto: false };</script>\n'
        f"<script>{pagedjs_bundle}</script>\n"
        "<script>\n"
        "class ReadyHandler extends Paged.Handler {\n"
        "  afterRendered(pages) {\n"
        "    const total = pages.length;\n"
        "    pages.forEach((page, idx) => {\n"
        "      if (idx === 0) return;\n"
        "      const bl = page.element.querySelector("
        "'.pagedjs_margin-bottom-left .pagedjs_margin-content');\n"
        "      const br = page.element.querySelector("
        "'.pagedjs_margin-bottom-right .pagedjs_margin-content');\n"
        "      if (bl) {\n"
        "        bl.textContent = 'WTIS';\n"
        "        bl.style.cssText = 'font-size:7.5pt;color:#888;';\n"
        "      }\n"
        "      if (br) {\n"
        "        br.textContent = (idx + 1) + ' / ' + total;\n"
        "        br.style.cssText = 'font-size:7.5pt;color:#888;text-align:right;';\n"
        "      }\n"
        "    });\n"
        "    // Push footer to bottom of last page\n"
        "    const lastPage = pages[pages.length - 1];\n"
        "    if (lastPage) {\n"
        "      const area = lastPage.element.querySelector('.pagedjs_page_content');\n"
        "      const footer = area && area.querySelector('.report-footer');\n"
        "      if (area && footer) {\n"
        "        // Set flex on all intermediate containers between area and footer\n"
        "        let el = footer.parentElement;\n"
        "        while (el && el !== area) {\n"
        "          el.style.display = 'flex';\n"
        "          el.style.flexDirection = 'column';\n"
        "          el.style.flex = '1';\n"
        "          el = el.parentElement;\n"
        "        }\n"
        "        area.style.display = 'flex';\n"
        "        area.style.flexDirection = 'column';\n"
        "        area.style.height = '100%';\n"
        "        footer.style.marginTop = 'auto';\n"
        "      }\n"
        "    }\n"
        "    window.pagedJsReady = true;\n"
        "  }\n"
        "}\n"
        "Paged.registerHandlers(ReadyHandler);\n"
        "window.PagedPolyfill.preview();\n"
        "</script>"
    )


# ---------------------------------------------------------------------------
# Playwright PDF generation
# ---------------------------------------------------------------------------


def _playwright_pdf(html: str, output_path: Path) -> None:
    """Render HTML to PDF using Playwright headless Chromium.

    Waits for paged.js to finish rendering before capturing PDF.
    Runs synchronously; call via thread pool from async contexts.
    """
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html, wait_until="domcontentloaded")
        page.wait_for_function("window.pagedJsReady === true", timeout=60_000)
        page.pdf(
            path=str(output_path),
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"},
        )
        browser.close()


def _html_to_pdf(html: str, output_path: Path) -> None:
    """Run Playwright in a thread pool to avoid async event loop conflicts."""
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(_playwright_pdf, html, output_path)
        future.result()


# ---------------------------------------------------------------------------
# Renderer
# ---------------------------------------------------------------------------


class PdfRenderer(BaseRenderer):
    """Renders WTIS markdown reports to consulting-style PDF files."""

    @property
    def format_name(self) -> str:
        return "pdf"

    def render(
        self,
        presentation: Presentation,
        theme: ThemeInfo,
        output_path: Path,
    ) -> RenderResult:
        """BaseRenderer interface: converts Presentation to a minimal report PDF."""
        lines: list[str] = [f"---\ntopic: {presentation.title}\n---\n\n"]
        lines.append(f"# {presentation.title}\n\n")
        for slide in presentation.slides:
            if slide.title:
                lines.append(f"\n## {slide.title}\n\n")
            if slide.body:
                lines.append(slide.body + "\n")
            for bullet in slide.bullets:
                lines.append(f"- {bullet}\n")

        tmp = output_path.with_suffix(".tmp.md")
        tmp.write_text("".join(lines), encoding="utf-8")
        try:
            return self.render_markdown(tmp, theme, output_path)
        finally:
            if tmp.exists():
                tmp.unlink()

    def render_markdown(
        self,
        markdown_path: Path,
        theme: ThemeInfo,
        output_path: Path,
    ) -> RenderResult:
        """Render a WTIS markdown report file to a consulting-style PDF.

        Args:
            markdown_path: Absolute path to the source .md file.
            theme: Resolved ThemeInfo with design tokens.
            output_path: Destination .pdf path.

        Returns:
            RenderResult with output_path, format, theme name, and validation.
        """
        from design_system.renderers.validator import (
            run_validation,
            validate_html,
            validate_markdown,
        )

        post = frontmatter.load(str(markdown_path))
        meta: dict = post.metadata
        body: str = post.content

        # L1: Validate markdown source
        md_checks = validate_markdown(body, meta)
        for c in md_checks:
            if not c.passed:
                logger.warning("L1 %s: %s — %s", c.check_id, c.name, c.message)

        # Extract H1 title from markdown body
        h1_match = re.match(r"^#\s+(.+)$", body, re.MULTILINE)
        report_title = h1_match.group(1).strip() if h1_match else meta.get(
            "topic", markdown_path.stem
        )

        sections = _parse_sections(body)
        exec_summary = next((s for s in sections if s.is_exec_summary), None)
        references = next((s for s in sections if s.is_references), None)
        main_sections = [
            s for s in sections if not s.is_exec_summary and not s.is_references
        ]

        # Build TOC and inject anchor IDs
        toc = _build_toc(exec_summary, main_sections, references is not None)
        _inject_toc_anchors(exec_summary, main_sections, toc)

        # Extract intro content between H1 and first ## heading
        intro_html = ""
        first_h2 = re.search(r"^## ", body, re.MULTILINE)
        if h1_match and first_h2:
            intro_text = body[h1_match.end() : first_h2.start()].strip()
            if intro_text:
                md = _make_md()
                intro_html = _postprocess(md(_preprocess(intro_text)))

        # Build CSS: theme variables first, then base stylesheet
        css = _css_vars(theme) + "\n" + (_STYLES_DIR / "report-consulting.css").read_text(
            encoding="utf-8"
        )

        env = Environment(
            loader=FileSystemLoader(str(_TEMPLATES_DIR)),
            autoescape=False,
        )
        template = env.get_template("report-consulting.html.j2")

        sources_used = meta.get("sources_used", [])
        html = template.render(
            title=report_title,
            topic=meta.get("topic", markdown_path.stem),
            filename=markdown_path.name,
            date=str(meta.get("date", "")),
            confidence=meta.get("confidence"),
            status=meta.get("status", ""),
            verdict=meta.get("verdict", ""),
            score=meta.get("score", ""),
            strategy=meta.get("strategy", ""),
            sources_count=len(sources_used) if isinstance(sources_used, list) else 0,
            intro_html=intro_html,
            executive_summary_html=exec_summary.html if exec_summary else "",
            main_sections=main_sections,
            toc=toc,
            references_html=_split_large_tables(references.html) if references else "",
            css=css,
            pagedjs_script=_build_pagedjs_script(),
        )

        # L2: Validate HTML
        html_checks = validate_html(html)
        for c in html_checks:
            if not c.passed and c.severity == "error":
                logger.warning("L2 %s: %s — %s", c.check_id, c.name, c.message)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        _html_to_pdf(html, output_path)
        logger.info("PDF rendered: %s", output_path)

        # L3 + aggregate: Full validation
        report = run_validation(body, meta, html, output_path)
        validation = ValidationSummary(**report.to_dict())

        logger.info("Validation: %s", report.summary)

        return RenderResult(
            output_path=output_path,
            format="pdf",
            theme=theme.name,
            slide_count=0,
            validation=validation,
        )
