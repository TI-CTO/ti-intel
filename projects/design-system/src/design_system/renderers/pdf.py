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

from design_system.models import Presentation, RenderResult, ThemeInfo
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


def _postprocess(html: str) -> str:
    """Add CSS class to tables, wrap in div, and convert citation refs to styled badges."""
    html = re.sub(
        r"<table>", '<div class="table-wrapper"><table class="data-table">', html
    )
    html = re.sub(r"</table>", "</table></div>", html)
    html = re.sub(
        r"\[([GNEPTI]-\d+)\]",
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

        html = _postprocess(md(content))

        sections.append(
            ReportSection(
                title=title,
                clean_title=clean_title,
                number=number,
                html=html,
                is_exec_summary=any(k in title for k in _EXEC_SUMMARY_KEYS),
                is_references=any(k in title for k in _REFERENCES_KEYS),
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
        "        bl.textContent = 'LG U+ WTIS';\n"
        "        bl.style.cssText = 'font-size:7.5pt;color:#888;';\n"
        "      }\n"
        "      if (br) {\n"
        "        br.textContent = (idx + 1) + ' / ' + total;\n"
        "        br.style.cssText = 'font-size:7.5pt;color:#888;text-align:right;';\n"
        "      }\n"
        "    });\n"
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
            RenderResult with output_path, format, theme name.
        """
        post = frontmatter.load(str(markdown_path))
        meta: dict = post.metadata
        body: str = post.content

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
            confidence=meta.get("confidence", "medium"),
            status=meta.get("status", ""),
            sources_count=len(sources_used) if isinstance(sources_used, list) else 0,
            executive_summary_html=exec_summary.html if exec_summary else "",
            main_sections=main_sections,
            references_html=references.html if references else "",
            css=css,
            pagedjs_script=_build_pagedjs_script(),
        )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        _html_to_pdf(html, output_path)
        logger.info("PDF rendered: %s", output_path)

        return RenderResult(
            output_path=output_path,
            format="pdf",
            theme=theme.name,
            slide_count=0,
        )
