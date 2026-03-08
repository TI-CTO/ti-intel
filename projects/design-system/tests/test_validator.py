"""Tests for PDF rendering quality validator."""

from pathlib import Path

from design_system.renderers.validator import (
    CheckResult,
    ValidationReport,
    validate_html,
    validate_markdown,
    validate_pdf,
    run_validation,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

VALID_FRONTMATTER = {"type": "weekly-monitor", "date": "2026-03-09"}

MINIMAL_VALID_MD = """\
# Weekly Report

## Executive Summary

Summary here.

## 1. Analysis

Content with [[G-01]](#ref-g-01) citation.

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Source | [link](https://example.com) | news | 2026-03-09 | [B] |
"""


def _find(results: list[CheckResult], check_id: str) -> CheckResult:
    """Find a check result by ID."""
    for r in results:
        if r.check_id == check_id:
            return r
    raise ValueError(f"Check {check_id} not found")


# ---------------------------------------------------------------------------
# ValidationReport
# ---------------------------------------------------------------------------


class TestValidationReport:
    def test_empty_report_passes(self):
        report = ValidationReport()
        assert report.passed is True
        assert report.error_count == 0
        assert report.warning_count == 0
        assert report.summary == "0/0 PASS"

    def test_all_pass(self):
        report = ValidationReport(checks=[
            CheckResult("T-01", "test", True, "error"),
            CheckResult("T-02", "test", True, "warning"),
        ])
        assert report.passed is True
        assert report.error_count == 0

    def test_error_fails_report(self):
        report = ValidationReport(checks=[
            CheckResult("T-01", "test", False, "error", "broken"),
            CheckResult("T-02", "test", True, "warning"),
        ])
        assert report.passed is False
        assert report.error_count == 1

    def test_warning_only_still_passes(self):
        report = ValidationReport(checks=[
            CheckResult("T-01", "test", True, "error"),
            CheckResult("T-02", "test", False, "warning", "minor"),
        ])
        assert report.passed is True
        assert report.warning_count == 1

    def test_to_dict(self):
        report = ValidationReport(checks=[
            CheckResult("T-01", "fail check", False, "error", "bad"),
            CheckResult("T-02", "warn check", False, "warning", "meh"),
            CheckResult("T-03", "ok check", True, "error"),
        ])
        d = report.to_dict()
        assert d["passed"] is False
        assert d["summary"] == "1/3 PASS"
        assert len(d["errors"]) == 1
        assert len(d["warnings"]) == 1
        assert d["errors"][0]["id"] == "T-01"


# ---------------------------------------------------------------------------
# Level 1: Markdown validation
# ---------------------------------------------------------------------------


class TestValidateMarkdown:
    def test_valid_markdown_all_pass(self):
        results = validate_markdown(MINIMAL_VALID_MD, VALID_FRONTMATTER)
        errors = [r for r in results if not r.passed and r.severity == "error"]
        assert len(errors) == 0, [f"{r.check_id}: {r.message}" for r in errors]

    # M-01: frontmatter keys
    def test_m01_missing_type(self):
        results = validate_markdown(MINIMAL_VALID_MD, {"date": "2026-01-01"})
        r = _find(results, "M-01")
        assert not r.passed
        assert "type" in r.message

    def test_m01_missing_date(self):
        results = validate_markdown(MINIMAL_VALID_MD, {"type": "report"})
        r = _find(results, "M-01")
        assert not r.passed
        assert "date" in r.message

    def test_m01_both_present(self):
        results = validate_markdown(MINIMAL_VALID_MD, VALID_FRONTMATTER)
        assert _find(results, "M-01").passed

    # M-02: H1 title
    def test_m02_no_h1(self):
        md = "## Only H2\n\nContent."
        results = validate_markdown(md, VALID_FRONTMATTER)
        assert not _find(results, "M-02").passed

    def test_m02_has_h1(self):
        results = validate_markdown(MINIMAL_VALID_MD, VALID_FRONTMATTER)
        assert _find(results, "M-02").passed

    # M-03: Executive Summary
    def test_m03_no_exec_summary(self):
        md = "# Title\n\n## Introduction\n\nText.\n\n## References\n\n| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |\n|---|---|---|---|---|---|\n| <a id=\"ref-g-01\"></a>G-01 | S | [l](u) | n | d | A |"
        results = validate_markdown(md, VALID_FRONTMATTER)
        assert not _find(results, "M-03").passed

    def test_m03_korean_exec_summary(self):
        md = "# Title\n\n## 경영진 요약\n\nSummary.\n\n## References\n\n| # | a | b | c | d | e |\n|---|---|---|---|---|---|"
        results = validate_markdown(md, VALID_FRONTMATTER)
        assert _find(results, "M-03").passed

    # M-04: References section
    def test_m04_no_references(self):
        md = "# Title\n\n## Executive Summary\n\nText."
        results = validate_markdown(md, VALID_FRONTMATTER)
        assert not _find(results, "M-04").passed

    def test_m04_has_references(self):
        results = validate_markdown(MINIMAL_VALID_MD, VALID_FRONTMATTER)
        assert _find(results, "M-04").passed

    # M-05: Citation-Anchor mapping
    def test_m05_citation_without_anchor(self):
        md = "# T\n\n## Body\n\nSee [[G-01]](#ref-g-01).\n\n## References\n\n| # | a | b | c | d | e |\n|---|---|---|---|---|---|"
        results = validate_markdown(md, VALID_FRONTMATTER)
        r = _find(results, "M-05")
        assert not r.passed
        assert "G-01" in r.message

    def test_m05_matched(self):
        results = validate_markdown(MINIMAL_VALID_MD, VALID_FRONTMATTER)
        assert _find(results, "M-05").passed

    # M-06: Citation link format
    def test_m06_bare_citation_in_body(self):
        md = "# T\n\n## Body\n\nSee [G-01] here.\n\n## References\n\n| # | a | b | c | d | e |\n|---|---|---|---|---|---|\n| <a id=\"ref-g-01\"></a>G-01 | S | u | n | d | A |"
        results = validate_markdown(md, VALID_FRONTMATTER)
        r = _find(results, "M-06")
        assert not r.passed

    def test_m06_linked_citation(self):
        results = validate_markdown(MINIMAL_VALID_MD, VALID_FRONTMATTER)
        assert _find(results, "M-06").passed

    # M-07: References table columns
    def test_m07_wrong_column_count(self):
        md = "# T\n\n## References\n\n| # | 출처 | URL |\n|---|---|---|\n| 1 | s | u |"
        results = validate_markdown(md, VALID_FRONTMATTER)
        r = _find(results, "M-07")
        assert not r.passed
        assert "3" in r.message

    def test_m07_correct_columns(self):
        results = validate_markdown(MINIMAL_VALID_MD, VALID_FRONTMATTER)
        assert _find(results, "M-07").passed

    # M-10: Market signals no table
    def test_m10_table_in_market_signals(self):
        md = "# T\n\n### 시장 시그널\n\n| A | B |\n|---|---|\n| 1 | 2 |\n\n## References\n\n| # | a | b | c | d | e |\n|---|---|---|---|---|---|"
        results = validate_markdown(md, VALID_FRONTMATTER)
        r = _find(results, "M-10")
        assert not r.passed

    def test_m10_bullet_list_ok(self):
        md = "# T\n\n### 시장 시그널\n\n- Signal A\n- Signal B\n\n## References\n\n| # | a | b | c | d | e |\n|---|---|---|---|---|---|"
        results = validate_markdown(md, VALID_FRONTMATTER)
        assert _find(results, "M-10").passed

    # M-11: References no sub-heading split
    def test_m11_split_references(self):
        md = "# T\n\n## References\n\n### News\n\n| # | a | b | c | d | e |\n|---|---|---|---|---|---|\n\n### Papers\n\n| # | a | b | c | d | e |\n|---|---|---|---|---|---|"
        results = validate_markdown(md, VALID_FRONTMATTER)
        r = _find(results, "M-11")
        assert not r.passed

    def test_m11_unified_references(self):
        results = validate_markdown(MINIMAL_VALID_MD, VALID_FRONTMATTER)
        assert _find(results, "M-11").passed


# ---------------------------------------------------------------------------
# Level 2: HTML validation
# ---------------------------------------------------------------------------


class TestValidateHtml:
    def test_h01_all_linked_badges(self):
        html = '<a href="#ref-g-01" class="citation-badge">G-01</a>'
        results = validate_html(html)
        assert _find(results, "H-01").passed

    def test_h01_all_span_badges_fail(self):
        html = '<span class="citation-badge">G-01</span><span class="citation-badge">G-02</span>'
        results = validate_html(html)
        assert not _find(results, "H-01").passed

    def test_h01_no_badges_passes(self):
        html = "<p>No badges here.</p>"
        results = validate_html(html)
        assert _find(results, "H-01").passed

    def test_h02_escaped_anchors(self):
        html = '&lt;a id=&quot;ref-g-01&quot;&gt;&lt;/a&gt;'
        results = validate_html(html)
        assert not _find(results, "H-02").passed

    def test_h02_clean(self):
        html = '<a id="ref-g-01"></a>'
        results = validate_html(html)
        assert _find(results, "H-02").passed

    def test_h03_tables_with_class(self):
        html = '<table class="data-table"><tr><td>x</td></tr></table>'
        results = validate_html(html)
        assert _find(results, "H-03").passed

    def test_h03_table_without_class(self):
        html = "<table><tr><td>x</td></tr></table>"
        results = validate_html(html)
        assert not _find(results, "H-03").passed

    def test_h04_bare_url(self):
        html = "<p>Visit https://example.com for info.</p>"
        results = validate_html(html)
        r = _find(results, "H-04")
        assert not r.passed

    def test_h04_wrapped_url(self):
        html = '<p>Visit <a href="https://example.com">link</a>.</p>'
        results = validate_html(html)
        assert _find(results, "H-04").passed


# ---------------------------------------------------------------------------
# Level 3: PDF validation
# ---------------------------------------------------------------------------


class TestValidatePdf:
    def test_p01_missing_file(self, tmp_path: Path):
        results = validate_pdf(tmp_path / "nonexistent.pdf")
        assert not _find(results, "P-01").passed

    def test_p01_empty_file(self, tmp_path: Path):
        pdf = tmp_path / "empty.pdf"
        pdf.write_bytes(b"")
        results = validate_pdf(pdf)
        assert not _find(results, "P-01").passed

    def test_p01_valid_file(self, tmp_path: Path):
        """Create a minimal valid PDF to test P-01."""
        from pypdf import PdfWriter

        writer = PdfWriter()
        writer.add_blank_page(width=595, height=842)
        writer.add_blank_page(width=595, height=842)
        pdf = tmp_path / "test.pdf"
        with open(pdf, "wb") as f:
            writer.write(f)
        results = validate_pdf(pdf)
        assert _find(results, "P-01").passed
        assert _find(results, "P-02").passed


# ---------------------------------------------------------------------------
# run_validation orchestrator
# ---------------------------------------------------------------------------


class TestRunValidation:
    def test_aggregates_all_levels(self, tmp_path: Path):
        # Create a minimal PDF
        from pypdf import PdfWriter

        writer = PdfWriter()
        writer.add_blank_page(width=595, height=842)
        writer.add_blank_page(width=595, height=842)
        pdf = tmp_path / "test.pdf"
        with open(pdf, "wb") as f:
            writer.write(f)

        html = '<a href="#ref-g-01" class="citation-badge">G-01</a>'
        report = run_validation(MINIMAL_VALID_MD, VALID_FRONTMATTER, html, pdf)

        # Should have checks from all three levels
        ids = {c.check_id for c in report.checks}
        assert any(i.startswith("M-") for i in ids)
        assert any(i.startswith("H-") for i in ids)
        assert any(i.startswith("P-") for i in ids)

    def test_report_dict_serializable(self, tmp_path: Path):
        from pypdf import PdfWriter

        writer = PdfWriter()
        writer.add_blank_page(width=595, height=842)
        pdf = tmp_path / "test.pdf"
        with open(pdf, "wb") as f:
            writer.write(f)

        report = run_validation(MINIMAL_VALID_MD, VALID_FRONTMATTER, "<p>hi</p>", pdf)
        d = report.to_dict()
        assert "passed" in d
        assert "summary" in d
        assert isinstance(d["errors"], list)
        assert isinstance(d["warnings"], list)
