"""PDF rendering quality validator — checks markdown, HTML, and PDF output.

Validates reports at three levels with polymorphic type-specific checks:
  L1 (markdown source) — frontmatter, structure, citation integrity
  L2 (HTML post-processing) — badge links, anchor escaping, table classes
  L3 (PDF output) — file existence, page count, text extractability

Report types: weekly (weekly-monitor), wtis (WTIS analysis), generic (common only).
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------


@dataclass
class CheckResult:
    """Result of a single validation check."""

    check_id: str
    name: str
    passed: bool
    severity: str  # "error" | "warning" | "info"
    message: str = ""


@dataclass
class ValidationReport:
    """Aggregated validation results across all levels."""

    checks: list[CheckResult] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return all(c.passed for c in self.checks if c.severity == "error")

    @property
    def error_count(self) -> int:
        return sum(1 for c in self.checks if not c.passed and c.severity == "error")

    @property
    def warning_count(self) -> int:
        return sum(1 for c in self.checks if not c.passed and c.severity == "warning")

    @property
    def summary(self) -> str:
        total = len(self.checks)
        passed = sum(1 for c in self.checks if c.passed)
        return f"{passed}/{total} PASS"

    def to_dict(self) -> dict:
        """Serialize for MCP response."""
        errors = [
            {"id": c.check_id, "name": c.name, "message": c.message}
            for c in self.checks
            if not c.passed and c.severity == "error"
        ]
        warnings = [
            {"id": c.check_id, "name": c.name, "message": c.message}
            for c in self.checks
            if not c.passed and c.severity == "warning"
        ]
        return {
            "passed": self.passed,
            "summary": self.summary,
            "errors": errors,
            "warnings": warnings,
        }


# ---------------------------------------------------------------------------
# Report type detection
# ---------------------------------------------------------------------------

_REQUIRED_KEYS: dict[str, list[str]] = {
    "weekly": ["type", "date", "domain", "week"],
    "wtis": ["topic", "domain", "date", "wtis_version"],
    "generic": ["date"],
}


def _detect_report_type(meta: dict) -> str:
    """Detect report type from frontmatter metadata."""
    if meta.get("type") == "weekly-monitor":
        return "weekly"
    if "wtis_version" in meta or "l2_topic" in meta:
        return "wtis"
    return "generic"


# ---------------------------------------------------------------------------
# Level 1: Markdown source validation
# ---------------------------------------------------------------------------

_CITATION_PATTERN = re.compile(r"\[([GNEPTI]-\d+[a-z]?)\]")
_CITATION_LINK_PATTERN = re.compile(
    r"\[\[([GNEPTI]-\d+[a-z]?)\]\]\(#ref-[a-z]+-\d+[a-z]?\)"
)
_ANCHOR_PATTERN = re.compile(r'<a\s+id="ref-([a-z]+-\d+[a-z]?)"\s*>\s*</a>')


def validate_markdown(source: str, meta: dict) -> list[CheckResult]:
    """Run Level 1 checks on markdown source and frontmatter.

    Automatically detects report type from meta and applies
    common checks + type-specific checks.
    """
    report_type = _detect_report_type(meta)
    results: list[CheckResult] = []

    # --- Common checks ---

    # M-01: frontmatter required keys (type-specific key set)
    required = _REQUIRED_KEYS.get(report_type, _REQUIRED_KEYS["generic"])
    missing_keys = [k for k in required if k not in meta]
    results.append(
        CheckResult(
            check_id="M-01",
            name="frontmatter required keys",
            passed=len(missing_keys) == 0,
            severity="error",
            message=f"Missing keys: {', '.join(missing_keys)}" if missing_keys else "",
        )
    )

    # M-02: H1 title exists
    h1_match = re.search(r"^# .+", source, re.MULTILINE)
    results.append(
        CheckResult(
            check_id="M-02",
            name="H1 title exists",
            passed=h1_match is not None,
            severity="error",
            message="" if h1_match else "No H1 heading found",
        )
    )

    # M-04: References section exists
    has_refs = bool(re.search(r"^## References", source, re.MULTILINE))
    results.append(
        CheckResult(
            check_id="M-04",
            name="References section exists",
            passed=has_refs,
            severity="error",
            message="" if has_refs else "No References section found",
        )
    )

    # M-05: Citation→Anchor mapping completeness
    citations = set(_CITATION_PATTERN.findall(source))
    anchors_raw = set(_ANCHOR_PATTERN.findall(source))
    # Normalize anchors to uppercase format (e.g. "g-01" → "G-01")
    anchors = {a.upper() for a in anchors_raw}
    # Normalize citations to uppercase for comparison
    citations_upper = {c.upper() for c in citations}
    missing_anchors = citations_upper - anchors
    orphan_anchors = anchors - citations_upper
    m05_passed = len(missing_anchors) == 0 and len(orphan_anchors) == 0
    m05_msgs: list[str] = []
    if missing_anchors:
        m05_msgs.append(f"Citations without anchors: {sorted(missing_anchors)}")
    if orphan_anchors:
        m05_msgs.append(f"Anchors without citations: {sorted(orphan_anchors)}")
    results.append(
        CheckResult(
            check_id="M-05",
            name="Citation-Anchor mapping",
            passed=m05_passed,
            severity="error",
            message="; ".join(m05_msgs),
        )
    )

    # M-06: Citation markdown link format
    all_citations = _CITATION_PATTERN.findall(source)
    linked_citations = set(_CITATION_LINK_PATTERN.findall(source))
    bare_citations = [c for c in all_citations if c not in linked_citations]
    # Filter out citations in the References table (# column with anchor tags)
    refs_section = ""
    refs_match = re.search(r"^## References\b.*", source, re.MULTILINE)
    if refs_match:
        refs_section = source[refs_match.start() :]
    # Citations in refs section anchors are expected to be bare
    refs_citations = set(_CITATION_PATTERN.findall(refs_section))
    body_bare = [c for c in bare_citations if c not in refs_citations]
    results.append(
        CheckResult(
            check_id="M-06",
            name="Citation link format",
            passed=len(body_bare) == 0,
            severity="warning",
            message=(
                f"Bare citations (not clickable): {body_bare[:10]}"
                if body_bare
                else ""
            ),
        )
    )

    # M-07: References table 6 columns
    if has_refs and refs_section:
        ref_table_rows = re.findall(r"^\|(.+)\|$", refs_section, re.MULTILINE)
        if ref_table_rows:
            # Check header row (first non-separator row)
            header_cols = [
                c.strip()
                for c in ref_table_rows[0].split("|")
                if c.strip() and not re.match(r"^-+$", c.strip())
            ]
            m07_passed = len(header_cols) == 6
            results.append(
                CheckResult(
                    check_id="M-07",
                    name="References table 6 columns",
                    passed=m07_passed,
                    severity="error",
                    message=(
                        f"Expected 6 columns, found {len(header_cols)}"
                        if not m07_passed
                        else ""
                    ),
                )
            )
        else:
            results.append(
                CheckResult(
                    check_id="M-07",
                    name="References table 6 columns",
                    passed=False,
                    severity="error",
                    message="No table found in References section",
                )
            )
    else:
        results.append(
            CheckResult(
                check_id="M-07",
                name="References table 6 columns",
                passed=False,
                severity="error",
                message="References section missing",
            )
        )

    # M-11: References no sub-heading split
    if has_refs and refs_section:
        h3_in_refs = re.findall(r"^### .+", refs_section, re.MULTILINE)
        results.append(
            CheckResult(
                check_id="M-11",
                name="References no type split",
                passed=len(h3_in_refs) < 2,
                severity="warning",
                message=(
                    f"References has {len(h3_in_refs)} H3 sub-headings (should be unified)"
                    if len(h3_in_refs) >= 2
                    else ""
                ),
            )
        )
    else:
        results.append(
            CheckResult(
                check_id="M-11",
                name="References no type split",
                passed=True,
                severity="warning",
            )
        )

    # --- Type-specific checks ---
    if report_type == "weekly":
        results.extend(_validate_weekly(source, meta))
    elif report_type == "wtis":
        results.extend(_validate_wtis(source, meta))

    return results


# ---------------------------------------------------------------------------
# Weekly-specific checks (W-xx + relocated M-03, M-08, M-09, M-10)
# ---------------------------------------------------------------------------


def _validate_weekly(source: str, meta: dict) -> list[CheckResult]:
    """Run weekly-monitor specific checks."""
    results: list[CheckResult] = []

    # M-03: Executive Summary exists (weekly: English heading)
    has_exec = bool(
        re.search(r"^## Executive Summary", source, re.MULTILINE)
    )
    results.append(
        CheckResult(
            check_id="M-03",
            name="Executive Summary exists",
            passed=has_exec,
            severity="warning",
            message="" if has_exec else "No Executive Summary section found",
        )
    )

    # W-01: Executive Summary table 4 columns
    exec_match = re.search(r"^## Executive Summary\b.*", source, re.MULTILINE)
    if exec_match:
        start = exec_match.end()
        next_heading = re.search(r"^## ", source[start:], re.MULTILINE)
        end = start + next_heading.start() if next_heading else len(source)
        exec_content = source[start:end]

        table_rows = re.findall(r"^\|(.+)\|$", exec_content, re.MULTILINE)
        if table_rows:
            header_cols = [c.strip() for c in table_rows[0].split("|") if c.strip()]
            w01_passed = len(header_cols) == 4
            results.append(
                CheckResult(
                    check_id="W-01",
                    name="Executive Summary table 4 columns",
                    passed=w01_passed,
                    severity="error",
                    message=(
                        f"Expected 4 columns, found {len(header_cols)}"
                        if not w01_passed
                        else ""
                    ),
                )
            )
        else:
            results.append(
                CheckResult(
                    check_id="W-01",
                    name="Executive Summary table 4 columns",
                    passed=False,
                    severity="error",
                    message="No table in Executive Summary",
                )
            )
    else:
        results.append(
            CheckResult(
                check_id="W-01",
                name="Executive Summary table 4 columns",
                passed=False,
                severity="error",
                message="Executive Summary section missing",
            )
        )

    # W-02: Signal emoji exists (🔴🟡🟢)
    has_emoji = bool(re.search(r"[🔴🟡🟢]", source))
    results.append(
        CheckResult(
            check_id="W-02",
            name="Signal emoji exists",
            passed=has_emoji,
            severity="warning",
            message="" if has_emoji else "No signal emoji (🔴🟡🟢) found",
        )
    )

    # W-03: Deep analysis section count >= deep_count
    deep_count = meta.get("deep_count", 0)
    if deep_count > 0:
        # Count numbered H2 sections (deep analysis sections)
        numbered_h2 = re.findall(r"^## \d+\.\s+", source, re.MULTILINE)
        actual_count = len(numbered_h2)
        w03_passed = actual_count >= deep_count
        results.append(
            CheckResult(
                check_id="W-03",
                name="Deep analysis section count",
                passed=w03_passed,
                severity="warning",
                message=(
                    f"Expected >= {deep_count} deep sections, found {actual_count}"
                    if not w03_passed
                    else f"{actual_count} deep sections found"
                ),
            )
        )
    else:
        results.append(
            CheckResult(
                check_id="W-03",
                name="Deep analysis section count",
                passed=True,
                severity="warning",
                message="No deep_count in frontmatter (skipped)",
            )
        )

    # M-08: Player trends table 3 columns (relocated from common)
    _check_section_table(
        source, results, "M-08", "Player trends table 3 columns",
        section_pattern=r"(?:플레이어 동향|Player)",
        expected_cols=3, severity="warning",
    )

    # M-09: Key papers table 3 columns (relocated from common)
    _check_section_table(
        source, results, "M-09", "Key papers table 3 columns",
        section_pattern=r"(?:주요 논문|학술 동향|Key Papers|Academic)",
        expected_cols=3, severity="warning",
    )

    # M-10: Market signals = bullet list (relocated from common)
    _check_market_signals(source, results)

    return results


# ---------------------------------------------------------------------------
# WTIS-specific checks (T-xx)
# ---------------------------------------------------------------------------


def _validate_wtis(source: str, meta: dict) -> list[CheckResult]:
    """Run WTIS analysis specific checks."""
    results: list[CheckResult] = []

    # T-01: 경영진 요약 exists (Korean heading)
    has_exec_kr = bool(re.search(r"^## 경영진 요약", source, re.MULTILINE))
    results.append(
        CheckResult(
            check_id="T-01",
            name="경영진 요약 exists",
            passed=has_exec_kr,
            severity="warning",
            message="" if has_exec_kr else "No '## 경영진 요약' section found",
        )
    )

    # T-02: 200-point scoring table exists (in 전략 권고 section)
    has_scoring = bool(
        re.search(r"전략\s*권고", source)
        and re.search(r"\b\d{2,3}\s*/\s*200\b|\b200점|\b/\s*200\b", source)
    )
    # Also check for a scoring table with point values
    if not has_scoring:
        has_scoring = bool(
            re.search(r"점수|배점|Score", source, re.IGNORECASE)
            and re.search(r"\|\s*\d+\s*\|", source)
            and re.search(r"전략\s*권고|채점|Scoring", source, re.IGNORECASE)
        )
    results.append(
        CheckResult(
            check_id="T-02",
            name="200-point scoring table",
            passed=has_scoring,
            severity="error",
            message="" if has_scoring else "No scoring table found in 전략 권고 section",
        )
    )

    # T-03: 교차검증 결과 section exists
    has_cross = bool(
        re.search(r"^##\s+\d*\.?\s*교차검증|^##.*cross.?valid", source, re.MULTILINE | re.IGNORECASE)
    )
    results.append(
        CheckResult(
            check_id="T-03",
            name="교차검증 section exists",
            passed=has_cross,
            severity="warning",
            message="" if has_cross else "No 교차검증 (cross-validation) section found",
        )
    )

    # T-04: 3B decision matrix mention (Buy/Borrow/Build)
    bbb_keywords = re.findall(r"\b(Buy|Borrow|Build)\b", source, re.IGNORECASE)
    unique_bbb = {k.lower() for k in bbb_keywords}
    has_3b = len(unique_bbb) >= 2  # At least 2 of 3 B's mentioned
    results.append(
        CheckResult(
            check_id="T-04",
            name="3B decision matrix mention",
            passed=has_3b,
            severity="warning",
            message="" if has_3b else "Buy/Borrow/Build keywords not found",
        )
    )

    # T-05: 경쟁사 비교표 exists (table in 경쟁 환경 section)
    has_competitor = bool(
        re.search(r"경쟁\s*환경|경쟁사|Competitive", source, re.IGNORECASE)
    )
    if has_competitor:
        # Find the section and check for a table
        comp_match = re.search(
            r"^##\s+.*(?:경쟁\s*환경|경쟁사|Competitive).*$",
            source, re.MULTILINE | re.IGNORECASE,
        )
        if comp_match:
            start = comp_match.end()
            next_h2 = re.search(r"^## ", source[start:], re.MULTILINE)
            end = start + next_h2.start() if next_h2 else len(source)
            section = source[start:end]
            has_comp_table = bool(re.search(r"^\|.+\|$", section, re.MULTILINE))
        else:
            has_comp_table = False
    else:
        has_comp_table = False
    results.append(
        CheckResult(
            check_id="T-05",
            name="경쟁사 비교표 exists",
            passed=has_comp_table,
            severity="warning",
            message="" if has_comp_table else "No competitor comparison table found",
        )
    )

    # T-06: frontmatter consistency (wtis_mode + skills_executed)
    wtis_mode = meta.get("wtis_mode")
    skills = meta.get("skills_executed", [])
    if wtis_mode and skills:
        t06_passed = True
        t06_msg = ""
        if wtis_mode == "standard" and len(skills) < 3:
            t06_passed = False
            t06_msg = f"wtis_mode=standard but only {len(skills)} skills executed"
    else:
        t06_passed = True
        t06_msg = "wtis_mode or skills_executed not set (skipped)"
    results.append(
        CheckResult(
            check_id="T-06",
            name="frontmatter consistency",
            passed=t06_passed,
            severity="info",
            message=t06_msg,
        )
    )

    return results


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _check_section_table(
    source: str,
    results: list[CheckResult],
    check_id: str,
    name: str,
    section_pattern: str,
    expected_cols: int,
    severity: str,
) -> None:
    """Check that a section's table has the expected number of columns."""
    # Find section by H3 or H4 heading
    pattern = re.compile(
        rf"^#{'{3,4}'}\s+.*{section_pattern}.*$", re.MULTILINE | re.IGNORECASE
    )
    match = pattern.search(source)
    if not match:
        # Section not found — skip (not all reports have these)
        results.append(
            CheckResult(
                check_id=check_id, name=name, passed=True,
                severity=severity, message="Section not found (skipped)",
            )
        )
        return

    # Extract content until next heading of same or higher level
    start = match.end()
    next_heading = re.search(r"^#{1,4}\s+", source[start:], re.MULTILINE)
    end = start + next_heading.start() if next_heading else len(source)
    section_content = source[start:end]

    table_rows = re.findall(r"^\|(.+)\|$", section_content, re.MULTILINE)
    if not table_rows:
        results.append(
            CheckResult(
                check_id=check_id, name=name, passed=True,
                severity=severity, message="No table in section (skipped)",
            )
        )
        return

    header_cols = [c.strip() for c in table_rows[0].split("|") if c.strip()]
    passed = len(header_cols) == expected_cols
    results.append(
        CheckResult(
            check_id=check_id, name=name, passed=passed,
            severity=severity,
            message=(
                f"Expected {expected_cols} columns, found {len(header_cols)}"
                if not passed
                else ""
            ),
        )
    )


def _check_market_signals(source: str, results: list[CheckResult]) -> None:
    """M-10: Market signals section should use bullet lists, not tables."""
    pattern = re.compile(
        r"^#{3,4}\s+.*(?:시장 시그널|Market Signal).*$",
        re.MULTILINE | re.IGNORECASE,
    )
    match = pattern.search(source)
    if not match:
        results.append(
            CheckResult(
                check_id="M-10", name="Market signals = bullet list",
                passed=True, severity="warning",
                message="Section not found (skipped)",
            )
        )
        return

    start = match.end()
    next_heading = re.search(r"^#{1,4}\s+", source[start:], re.MULTILINE)
    end = start + next_heading.start() if next_heading else len(source)
    section_content = source[start:end]

    has_table = bool(re.search(r"^\|.+\|$", section_content, re.MULTILINE))
    results.append(
        CheckResult(
            check_id="M-10", name="Market signals = bullet list",
            passed=not has_table, severity="warning",
            message="Market signals section contains a table (should be bullet list)" if has_table else "",
        )
    )


# ---------------------------------------------------------------------------
# Level 2: HTML validation
# ---------------------------------------------------------------------------


def validate_html(html: str) -> list[CheckResult]:
    """Run Level 2 checks on post-processed HTML."""
    results: list[CheckResult] = []

    # H-01: Citation badge click links
    badge_links = len(re.findall(r'<a\s+href[^>]*class="citation-badge"', html))
    badge_spans = len(re.findall(r'<span\s+class="citation-badge"', html))
    total_badges = badge_links + badge_spans
    if total_badges > 0:
        link_ratio = badge_links / total_badges
        h01_passed = link_ratio > 0.5
        results.append(
            CheckResult(
                check_id="H-01",
                name="Citation badge click links",
                passed=h01_passed,
                severity="error",
                message=(
                    f"{badge_links}/{total_badges} badges have links "
                    f"({link_ratio:.0%})"
                    if not h01_passed
                    else f"{badge_links}/{total_badges} badges linked"
                ),
            )
        )
    else:
        results.append(
            CheckResult(
                check_id="H-01",
                name="Citation badge click links",
                passed=True,
                severity="error",
                message="No citation badges found (skipped)",
            )
        )

    # H-02: Escaped anchor tags
    escaped_anchors = len(re.findall(r"&lt;a id=", html))
    results.append(
        CheckResult(
            check_id="H-02",
            name="No escaped anchor tags",
            passed=escaped_anchors == 0,
            severity="error",
            message=(
                f"{escaped_anchors} escaped <a id=...> tags remain"
                if escaped_anchors > 0
                else ""
            ),
        )
    )

    # H-03: Tables have data-table class
    all_tables = len(re.findall(r"<table", html))
    classed_tables = len(re.findall(r'<table\s+class="data-table"', html))
    h03_passed = all_tables == 0 or all_tables == classed_tables
    results.append(
        CheckResult(
            check_id="H-03",
            name="Tables have data-table class",
            passed=h03_passed,
            severity="warning",
            message=(
                f"{classed_tables}/{all_tables} tables have data-table class"
                if not h03_passed
                else ""
            ),
        )
    )

    # H-04: Bare URLs converted to links
    # Find https:// not inside href="..."
    bare_urls = re.findall(r'(?<!href=")(https?://[^\s<,"]+)', html)
    # Filter: urls that are already link text inside <a>...</a> are OK
    # We just check if any url exists outside of href attribute
    h04_passed = len(bare_urls) == 0
    results.append(
        CheckResult(
            check_id="H-04",
            name="Bare URLs converted to links",
            passed=h04_passed,
            severity="info",
            message=(
                f"{len(bare_urls)} bare URLs found"
                if not h04_passed
                else ""
            ),
        )
    )

    return results


# ---------------------------------------------------------------------------
# Level 3: PDF output validation
# ---------------------------------------------------------------------------


def validate_pdf(pdf_path: Path) -> list[CheckResult]:
    """Run Level 3 checks on the rendered PDF file."""
    results: list[CheckResult] = []

    # P-01: File exists and non-empty
    exists = pdf_path.exists() and pdf_path.stat().st_size > 0
    results.append(
        CheckResult(
            check_id="P-01",
            name="PDF file exists and non-empty",
            passed=exists,
            severity="error",
            message="" if exists else f"PDF not found or empty: {pdf_path}",
        )
    )

    if not exists:
        # Skip remaining checks
        results.append(
            CheckResult(
                check_id="P-02", name="Minimum page count",
                passed=False, severity="warning",
                message="Skipped (PDF missing)",
            )
        )
        results.append(
            CheckResult(
                check_id="P-03", name="Text extractable",
                passed=False, severity="warning",
                message="Skipped (PDF missing)",
            )
        )
        return results

    try:
        from pypdf import PdfReader

        reader = PdfReader(str(pdf_path))
        page_count = len(reader.pages)

        # P-02: Minimum page count
        results.append(
            CheckResult(
                check_id="P-02",
                name="Minimum page count",
                passed=page_count >= 2,
                severity="warning",
                message=(
                    f"Only {page_count} page(s)"
                    if page_count < 2
                    else f"{page_count} pages"
                ),
            )
        )

        # P-03: Text extractable
        text = ""
        for page in reader.pages[:3]:
            text += page.extract_text() or ""
        has_text = len(text.strip()) > 0
        results.append(
            CheckResult(
                check_id="P-03",
                name="Text extractable",
                passed=has_text,
                severity="warning",
                message="" if has_text else "No text extracted from first 3 pages",
            )
        )
    except ImportError:
        logger.warning("pypdf not installed — skipping PDF content checks")
        results.append(
            CheckResult(
                check_id="P-02", name="Minimum page count",
                passed=True, severity="warning",
                message="Skipped (pypdf not installed)",
            )
        )
        results.append(
            CheckResult(
                check_id="P-03", name="Text extractable",
                passed=True, severity="warning",
                message="Skipped (pypdf not installed)",
            )
        )
    except Exception as exc:
        logger.warning("PDF validation error: %s", exc)
        results.append(
            CheckResult(
                check_id="P-02", name="Minimum page count",
                passed=False, severity="warning",
                message=f"Error reading PDF: {exc}",
            )
        )
        results.append(
            CheckResult(
                check_id="P-03", name="Text extractable",
                passed=False, severity="warning",
                message=f"Error reading PDF: {exc}",
            )
        )

    return results


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


def run_validation(
    source: str,
    meta: dict,
    html: str,
    pdf_path: Path,
) -> ValidationReport:
    """Run all validation levels and return aggregated report.

    Args:
        source: Raw markdown source text.
        meta: Parsed frontmatter metadata dict.
        html: Post-processed HTML (after _postprocess).
        pdf_path: Path to the rendered PDF file.

    Returns:
        ValidationReport with all check results.
    """
    report = ValidationReport()
    report.checks.extend(validate_markdown(source, meta))
    report.checks.extend(validate_html(html))
    report.checks.extend(validate_pdf(pdf_path))
    return report
