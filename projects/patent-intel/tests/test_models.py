"""Tests for patent_intel.models."""

from datetime import date

from patent_intel.models import Patent, PatentStats, PatentTopic, ReliabilityTag


def test_patent_defaults():
    patent = Patent(
        external_id="uspto:US11234567B2",
        source="uspto",
        title="AI-Based Network Slicing Method",
        applicant="LG Electronics Inc.",
    )
    assert patent.ipc_codes == []
    assert patent.abstract == ""
    assert patent.reliability_tag == ReliabilityTag.OFFICIAL
    assert patent.raw_url is None
    assert patent.id is None
    assert patent.filing_date is None


def test_patent_with_all_fields():
    patent = Patent(
        external_id="uspto:US10987654B1",
        source="uspto",
        title="Quantum Key Distribution in 5G Networks",
        applicant="Samsung Electronics",
        filing_date=date(2023, 3, 15),
        publication_date=date(2024, 1, 10),
        ipc_codes=["H04L9/08", "H04W12/04"],
        abstract="A method for quantum key distribution...",
        reliability_tag=ReliabilityTag.OFFICIAL,
        raw_url="https://patents.google.com/patent/US10987654B1",
    )
    assert patent.ipc_codes == ["H04L9/08", "H04W12/04"]
    assert patent.filing_date == date(2023, 3, 15)
    assert patent.applicant == "Samsung Electronics"


def test_patent_topic():
    pt = PatentTopic(patent_id=1, topic_id=5)
    assert pt.relevance == 1.0


def test_patent_stats_defaults():
    stats = PatentStats(topic_id=2, stat_year=2025, stat_quarter=2)
    assert stats.filing_count == 0
    assert stats.top_applicants == []
    assert stats.id is None


def test_reliability_tag_values():
    assert ReliabilityTag.OFFICIAL.value == "A"
    assert ReliabilityTag.REPUTABLE.value == "B"
    assert ReliabilityTag.INDICATIVE.value == "C"
    assert ReliabilityTag.UNVERIFIED.value == "D"
