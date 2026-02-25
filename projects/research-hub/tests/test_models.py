"""Tests for research_hub.models."""

from datetime import date

from research_hub.models import Paper, PaperStats, PaperTopic, ReliabilityTag


def test_paper_defaults():
    paper = Paper(
        external_id="ss:abc123",
        source="semantic_scholar",
        title="AI in 5G Networks",
    )
    assert paper.authors == []
    assert paper.abstract == ""
    assert paper.citation_count == 0
    assert paper.reliability_tag == ReliabilityTag.OFFICIAL
    assert paper.raw_url is None
    assert paper.id is None


def test_paper_with_all_fields():
    paper = Paper(
        external_id="ss:xyz789",
        source="semantic_scholar",
        title="Quantum Key Distribution over 5G",
        authors=["Alice Kim", "Bob Lee"],
        published_date=date(2025, 6, 15),
        abstract="We propose a QKD scheme...",
        citation_count=42,
        reliability_tag=ReliabilityTag.OFFICIAL,
        raw_url="https://arxiv.org/abs/2506.00001",
    )
    assert paper.authors == ["Alice Kim", "Bob Lee"]
    assert paper.citation_count == 42
    assert paper.published_date == date(2025, 6, 15)


def test_paper_topic():
    pt = PaperTopic(paper_id=1, topic_id=3)
    assert pt.relevance == 1.0


def test_paper_stats_defaults():
    stats = PaperStats(topic_id=1, stat_year=2025, stat_month=6)
    assert stats.paper_count == 0
    assert stats.avg_citations == 0.0
    assert stats.id is None


def test_reliability_tag_values():
    assert ReliabilityTag.OFFICIAL.value == "A"
    assert ReliabilityTag.REPUTABLE.value == "B"
    assert ReliabilityTag.INDICATIVE.value == "C"
    assert ReliabilityTag.UNVERIFIED.value == "D"
