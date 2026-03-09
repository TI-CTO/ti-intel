"""Tests for PDF rendering quality validator."""

from pathlib import Path

from design_system.renderers.validator import (
    CheckResult,
    ValidationReport,
    _detect_report_type,
    validate_html,
    validate_markdown,
    validate_pdf,
    run_validation,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

WEEKLY_META = {
    "type": "weekly-monitor",
    "date": "2026-03-09",
    "domain": "agentic-ai",
    "week": "W10",
}

WTIS_META = {
    "topic": "agent-frameworks",
    "domain": "agentic-ai",
    "date": "2026-03-09",
    "wtis_version": "4.1",
}

GENERIC_META = {"date": "2026-03-09"}

MINIMAL_WEEKLY_MD = """\
# Weekly Report

## Executive Summary

| 세부기술 | 신호 | 핵심 내용 | 분석 |
|----------|------|-----------|------|
| Topic A | 🟢 | Content | Analysis |

## 1. Deep Analysis

Details here with [[G-01]](#ref-g-01) citation.

### 플레이어 동향

| 기업 | 동향 | 의미 |
|------|------|------|
| Co A | News | Impact |

### 주요 논문

| 논문 | 핵심 기여 | 시사점 |
|------|-----------|--------|
| Paper A | Contribution | Implication |

### 시장 시그널

- Signal A
- Signal B

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Source | [link](https://example.com) | news | 2026-03-09 | [B] |
"""

MINIMAL_WTIS_MD = """\
# WTIS Analysis: Agent Frameworks

## 경영진 요약

요약 내용 [[G-01]](#ref-g-01).

## 2. 경쟁 환경

| 기업 | 제품 | 강점 |
|------|------|------|
| OpenAI | Agents SDK | First mover |

## 3. 전략 권고

총점: 145 / 200

| 항목 | 배점 | 점수 |
|------|------|------|
| 기술 성숙도 | 50 | 35 |

권고: Buy 전략 기반, 일부 Build 병행, 필요시 Borrow.

## 5. 교차검증

교차검증 결과 기술.

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Source | [link](https://example.com) | news | 2026-03-09 | [B] |
"""

MINIMAL_GENERIC_MD = """\
# Generic Report

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


def _has_check(results: list[CheckResult], check_id: str) -> bool:
    """Check if a result with the given ID exists."""
    return any(r.check_id == check_id for r in results)


# ---------------------------------------------------------------------------
# Report type detection
# ---------------------------------------------------------------------------


class TestDetectReportType:
    def test_weekly(self):
        assert _detect_report_type({"type": "weekly-monitor"}) == "weekly"

    def test_wtis_by_version(self):
        assert _detect_report_type({"wtis_version": "4.1"}) == "wtis"

    def test_wtis_by_l2_topic(self):
        assert _detect_report_type({"l2_topic": "agent-fw"}) == "wtis"

    def test_generic_fallback(self):
        assert _detect_report_type({"type": "other"}) == "generic"

    def test_empty_meta(self):
        assert _detect_report_type({}) == "generic"


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
# Level 1: Common markdown checks
# ---------------------------------------------------------------------------


class TestCommonMarkdownChecks:
    """Common checks that apply to all report types."""

    def test_generic_all_pass(self):
        results = validate_markdown(MINIMAL_GENERIC_MD, GENERIC_META)
        errors = [r for r in results if not r.passed and r.severity == "error"]
        assert len(errors) == 0, [f"{r.check_id}: {r.message}" for r in errors]

    # M-01: frontmatter keys (type-specific)
    def test_m01_generic_only_needs_date(self):
        results = validate_markdown(MINIMAL_GENERIC_MD, {"date": "2026-01-01"})
        assert _find(results, "M-01").passed

    def test_m01_generic_missing_date(self):
        results = validate_markdown(MINIMAL_GENERIC_MD, {})
        r = _find(results, "M-01")
        assert not r.passed
        assert "date" in r.message

    def test_m01_weekly_needs_all_keys(self):
        # Missing week and domain
        results = validate_markdown(
            MINIMAL_WEEKLY_MD, {"type": "weekly-monitor", "date": "2026-01-01"}
        )
        r = _find(results, "M-01")
        assert not r.passed
        assert "domain" in r.message
        assert "week" in r.message

    def test_m01_weekly_all_present(self):
        results = validate_markdown(MINIMAL_WEEKLY_MD, WEEKLY_META)
        assert _find(results, "M-01").passed

    def test_m01_wtis_needs_version(self):
        results = validate_markdown(MINIMAL_WTIS_MD, {"date": "2026-01-01", "wtis_version": "4.1"})
        r = _find(results, "M-01")
        assert not r.passed
        assert "topic" in r.message

    def test_m01_wtis_all_present(self):
        results = validate_markdown(MINIMAL_WTIS_MD, WTIS_META)
        assert _find(results, "M-01").passed

    # M-02: H1 title
    def test_m02_no_h1(self):
        md = "## Only H2\n\nContent."
        results = validate_markdown(md, GENERIC_META)
        assert not _find(results, "M-02").passed

    def test_m02_has_h1(self):
        results = validate_markdown(MINIMAL_GENERIC_MD, GENERIC_META)
        assert _find(results, "M-02").passed

    # M-04: References section
    def test_m04_no_references(self):
        md = "# Title\n\nText."
        results = validate_markdown(md, GENERIC_META)
        assert not _find(results, "M-04").passed

    def test_m04_has_references(self):
        results = validate_markdown(MINIMAL_GENERIC_MD, GENERIC_META)
        assert _find(results, "M-04").passed

    # M-05: Citation-Anchor mapping
    def test_m05_citation_without_anchor(self):
        md = "# T\n\n## Body\n\nSee [[G-01]](#ref-g-01).\n\n## References\n\n| # | a | b | c | d | e |\n|---|---|---|---|---|---|"
        results = validate_markdown(md, GENERIC_META)
        r = _find(results, "M-05")
        assert not r.passed
        assert "G-01" in r.message

    def test_m05_matched(self):
        results = validate_markdown(MINIMAL_GENERIC_MD, GENERIC_META)
        assert _find(results, "M-05").passed

    # M-06: Citation link format
    def test_m06_bare_citation_in_body(self):
        md = "# T\n\n## Body\n\nSee [G-01] here.\n\n## References\n\n| # | a | b | c | d | e |\n|---|---|---|---|---|---|\n| <a id=\"ref-g-01\"></a>G-01 | S | u | n | d | A |"
        results = validate_markdown(md, GENERIC_META)
        r = _find(results, "M-06")
        assert not r.passed

    def test_m06_linked_citation(self):
        results = validate_markdown(MINIMAL_GENERIC_MD, GENERIC_META)
        assert _find(results, "M-06").passed

    # M-07: References table columns
    def test_m07_wrong_column_count(self):
        md = "# T\n\n## References\n\n| # | 출처 | URL |\n|---|---|---|\n| 1 | s | u |"
        results = validate_markdown(md, GENERIC_META)
        r = _find(results, "M-07")
        assert not r.passed
        assert "3" in r.message

    def test_m07_correct_columns(self):
        results = validate_markdown(MINIMAL_GENERIC_MD, GENERIC_META)
        assert _find(results, "M-07").passed

    # M-11: References no sub-heading split
    def test_m11_split_references(self):
        md = "# T\n\n## References\n\n### News\n\n| # | a | b | c | d | e |\n|---|---|---|---|---|---|\n\n### Papers\n\n| # | a | b | c | d | e |\n|---|---|---|---|---|---|"
        results = validate_markdown(md, GENERIC_META)
        r = _find(results, "M-11")
        assert not r.passed

    def test_m11_unified_references(self):
        results = validate_markdown(MINIMAL_GENERIC_MD, GENERIC_META)
        assert _find(results, "M-11").passed


class TestGenericNoWeeklyChecks:
    """Generic reports should NOT have weekly-specific checks."""

    def test_no_weekly_checks_in_generic(self):
        results = validate_markdown(MINIMAL_GENERIC_MD, GENERIC_META)
        ids = {r.check_id for r in results}
        # M-03, M-08, M-09, M-10 are weekly-only now
        assert "M-03" not in ids
        assert "M-08" not in ids
        assert "M-09" not in ids
        assert "M-10" not in ids
        # W-xx should not appear
        assert not any(i.startswith("W-") for i in ids)
        # T-xx should not appear
        assert not any(i.startswith("T-") for i in ids)

    def test_no_wtis_checks_in_generic(self):
        results = validate_markdown(MINIMAL_GENERIC_MD, GENERIC_META)
        ids = {r.check_id for r in results}
        assert not any(i.startswith("T-") for i in ids)


# ---------------------------------------------------------------------------
# Level 1: Weekly-specific checks
# ---------------------------------------------------------------------------


class TestWeeklyChecks:
    """Weekly-monitor specific validation checks."""

    def test_weekly_all_pass(self):
        results = validate_markdown(MINIMAL_WEEKLY_MD, WEEKLY_META)
        errors = [r for r in results if not r.passed and r.severity == "error"]
        assert len(errors) == 0, [f"{r.check_id}: {r.message}" for r in errors]

    def test_weekly_has_type_specific_checks(self):
        results = validate_markdown(MINIMAL_WEEKLY_MD, WEEKLY_META)
        ids = {r.check_id for r in results}
        assert "M-03" in ids  # Executive Summary
        assert "W-01" in ids  # Exec Summary table
        assert "W-02" in ids  # Signal emoji
        assert "W-03" in ids  # Deep analysis count
        assert "M-08" in ids  # Player trends
        assert "M-09" in ids  # Key papers
        assert "M-10" in ids  # Market signals

    # M-03: Executive Summary (weekly version)
    def test_m03_no_exec_summary(self):
        md = "# Title\n\n## Introduction\n\nText.\n\n## References\n\n| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |\n|---|---|---|---|---|---|\n| <a id=\"ref-g-01\"></a>G-01 | S | [l](u) | n | d | A |"
        results = validate_markdown(md, WEEKLY_META)
        assert not _find(results, "M-03").passed

    def test_m03_has_exec_summary(self):
        results = validate_markdown(MINIMAL_WEEKLY_MD, WEEKLY_META)
        assert _find(results, "M-03").passed

    # W-01: Executive Summary table 4 columns
    def test_w01_correct_columns(self):
        results = validate_markdown(MINIMAL_WEEKLY_MD, WEEKLY_META)
        assert _find(results, "W-01").passed

    def test_w01_wrong_columns(self):
        md = MINIMAL_WEEKLY_MD.replace(
            "| 세부기술 | 신호 | 핵심 내용 | 분석 |",
            "| 세부기술 | 신호 | 핵심 내용 |",
        ).replace(
            "| Topic A | 🟢 | Content | Analysis |",
            "| Topic A | 🟢 | Content |",
        )
        results = validate_markdown(md, WEEKLY_META)
        r = _find(results, "W-01")
        assert not r.passed
        assert "3" in r.message

    def test_w01_no_table(self):
        md = "# T\n\n## Executive Summary\n\nJust text, no table.\n\n## References\n\n| # | a | b | c | d | e |\n|---|---|---|---|---|---|"
        results = validate_markdown(md, WEEKLY_META)
        r = _find(results, "W-01")
        assert not r.passed
        assert "No table" in r.message

    # W-02: Signal emoji
    def test_w02_has_emoji(self):
        results = validate_markdown(MINIMAL_WEEKLY_MD, WEEKLY_META)
        assert _find(results, "W-02").passed

    def test_w02_no_emoji(self):
        md = MINIMAL_WEEKLY_MD.replace("🟢", "green")
        results = validate_markdown(md, WEEKLY_META)
        assert not _find(results, "W-02").passed

    # W-03: Deep analysis section count
    def test_w03_with_deep_count(self):
        meta = {**WEEKLY_META, "deep_count": 1}
        results = validate_markdown(MINIMAL_WEEKLY_MD, meta)
        assert _find(results, "W-03").passed

    def test_w03_insufficient_sections(self):
        meta = {**WEEKLY_META, "deep_count": 5}
        results = validate_markdown(MINIMAL_WEEKLY_MD, meta)
        r = _find(results, "W-03")
        assert not r.passed
        assert "5" in r.message

    def test_w03_no_deep_count_skips(self):
        results = validate_markdown(MINIMAL_WEEKLY_MD, WEEKLY_META)
        r = _find(results, "W-03")
        assert r.passed
        assert "skipped" in r.message

    # M-08: Player trends (now weekly-only)
    def test_m08_correct_columns(self):
        results = validate_markdown(MINIMAL_WEEKLY_MD, WEEKLY_META)
        assert _find(results, "M-08").passed

    # M-09: Key papers (now weekly-only)
    def test_m09_correct_columns(self):
        results = validate_markdown(MINIMAL_WEEKLY_MD, WEEKLY_META)
        assert _find(results, "M-09").passed

    # M-10: Market signals (now weekly-only)
    def test_m10_table_in_market_signals(self):
        md = "# T\n\n## Executive Summary\n\n| a | b | c | d |\n|---|---|---|---|\n| 1 | 🟢 | 3 | 4 |\n\n### 시장 시그널\n\n| A | B |\n|---|---|\n| 1 | 2 |\n\n## References\n\n| # | a | b | c | d | e |\n|---|---|---|---|---|---|"
        results = validate_markdown(md, WEEKLY_META)
        r = _find(results, "M-10")
        assert not r.passed

    def test_m10_bullet_list_ok(self):
        results = validate_markdown(MINIMAL_WEEKLY_MD, WEEKLY_META)
        assert _find(results, "M-10").passed


# ---------------------------------------------------------------------------
# Level 1: WTIS-specific checks
# ---------------------------------------------------------------------------


class TestWtisChecks:
    """WTIS analysis specific validation checks."""

    def test_wtis_all_pass(self):
        results = validate_markdown(MINIMAL_WTIS_MD, WTIS_META)
        errors = [r for r in results if not r.passed and r.severity == "error"]
        assert len(errors) == 0, [f"{r.check_id}: {r.message}" for r in errors]

    def test_wtis_has_type_specific_checks(self):
        results = validate_markdown(MINIMAL_WTIS_MD, WTIS_META)
        ids = {r.check_id for r in results}
        assert "T-01" in ids
        assert "T-02" in ids
        assert "T-03" in ids
        assert "T-04" in ids
        assert "T-05" in ids
        assert "T-06" in ids

    def test_wtis_no_weekly_checks(self):
        results = validate_markdown(MINIMAL_WTIS_MD, WTIS_META)
        ids = {r.check_id for r in results}
        assert not any(i.startswith("W-") for i in ids)
        assert "M-03" not in ids
        assert "M-08" not in ids
        assert "M-09" not in ids
        assert "M-10" not in ids

    # T-01: 경영진 요약
    def test_t01_has_summary(self):
        results = validate_markdown(MINIMAL_WTIS_MD, WTIS_META)
        assert _find(results, "T-01").passed

    def test_t01_no_summary(self):
        md = MINIMAL_WTIS_MD.replace("## 경영진 요약", "## Summary")
        results = validate_markdown(md, WTIS_META)
        assert not _find(results, "T-01").passed

    # T-02: Scoring table
    def test_t02_has_scoring(self):
        results = validate_markdown(MINIMAL_WTIS_MD, WTIS_META)
        assert _find(results, "T-02").passed

    def test_t02_no_scoring(self):
        md = MINIMAL_WTIS_MD.replace("전략 권고", "권고사항").replace("배점", "항목값").replace("점수", "값")
        results = validate_markdown(md, WTIS_META)
        assert not _find(results, "T-02").passed

    # T-03: 교차검증
    def test_t03_has_cross_validation(self):
        results = validate_markdown(MINIMAL_WTIS_MD, WTIS_META)
        assert _find(results, "T-03").passed

    def test_t03_no_cross_validation(self):
        md = MINIMAL_WTIS_MD.replace("## 5. 교차검증", "## 5. 결론")
        results = validate_markdown(md, WTIS_META)
        assert not _find(results, "T-03").passed

    # T-04: 3B decision matrix
    def test_t04_has_3b(self):
        results = validate_markdown(MINIMAL_WTIS_MD, WTIS_META)
        assert _find(results, "T-04").passed

    def test_t04_no_3b(self):
        md = MINIMAL_WTIS_MD.replace("Buy", "구매").replace("Build", "구축").replace("Borrow", "차용")
        results = validate_markdown(md, WTIS_META)
        assert not _find(results, "T-04").passed

    # T-05: 경쟁사 비교표
    def test_t05_has_competitor_table(self):
        results = validate_markdown(MINIMAL_WTIS_MD, WTIS_META)
        assert _find(results, "T-05").passed

    def test_t05_no_competitor_section(self):
        md = MINIMAL_WTIS_MD.replace("경쟁 환경", "시장 분석")
        results = validate_markdown(md, WTIS_META)
        assert not _find(results, "T-05").passed

    # T-06: Frontmatter consistency
    def test_t06_skips_when_no_mode(self):
        results = validate_markdown(MINIMAL_WTIS_MD, WTIS_META)
        r = _find(results, "T-06")
        assert r.passed
        assert "skipped" in r.message

    def test_t06_standard_with_enough_skills(self):
        meta = {**WTIS_META, "wtis_mode": "standard", "skills_executed": ["a", "b", "c"]}
        results = validate_markdown(MINIMAL_WTIS_MD, meta)
        assert _find(results, "T-06").passed

    def test_t06_standard_with_few_skills(self):
        meta = {**WTIS_META, "wtis_mode": "standard", "skills_executed": ["a"]}
        results = validate_markdown(MINIMAL_WTIS_MD, meta)
        r = _find(results, "T-06")
        assert not r.passed
        assert "1 skills" in r.message


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
        report = run_validation(MINIMAL_WEEKLY_MD, WEEKLY_META, html, pdf)

        # Should have checks from all three levels
        ids = {c.check_id for c in report.checks}
        assert any(i.startswith("M-") for i in ids)
        assert any(i.startswith("H-") for i in ids)
        assert any(i.startswith("P-") for i in ids)
        # Weekly-specific checks included
        assert any(i.startswith("W-") for i in ids)

    def test_report_dict_serializable(self, tmp_path: Path):
        from pypdf import PdfWriter

        writer = PdfWriter()
        writer.add_blank_page(width=595, height=842)
        pdf = tmp_path / "test.pdf"
        with open(pdf, "wb") as f:
            writer.write(f)

        report = run_validation(MINIMAL_WEEKLY_MD, WEEKLY_META, "<p>hi</p>", pdf)
        d = report.to_dict()
        assert "passed" in d
        assert "summary" in d
        assert isinstance(d["errors"], list)
        assert isinstance(d["warnings"], list)
