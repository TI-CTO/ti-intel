"""Tests for intel_store.models."""

from datetime import date

from intel_store.models import (
    IntelItem,
    IntelItemRelation,
    IntelItemTopic,
    ItemType,
    Language,
    NewsMetadata,
    PaperMetadata,
    PatentMetadata,
    ReliabilityTag,
    news_from_collector,
    paper_from_collector,
    patent_from_collector,
)


class TestIntelItem:
    def test_default_values(self):
        item = IntelItem(
            item_type=ItemType.NEWS,
            title="Test Title",
            source_name="test_source",
        )
        assert item.id is None
        assert item.abstract == ""
        assert item.language == Language.EN
        assert item.reliability == ReliabilityTag.INDICATIVE
        assert item.metadata == {}
        assert item.embedding is None
        assert item.collected_date == date.today()

    def test_compute_content_hash(self):
        item = IntelItem(
            item_type=ItemType.PAPER,
            title="Quantum Computing",
            abstract="This is a long abstract about quantum computing." * 10,
            source_name="semantic_scholar",
        )
        h = item.compute_content_hash()
        assert len(h) == 64  # SHA-256 hex
        assert h == item.compute_content_hash()  # deterministic

    def test_ensure_content_hash(self):
        item = IntelItem(
            item_type=ItemType.NEWS,
            title="Breaking News",
            source_name="reuters",
        )
        assert item.content_hash == ""
        item.ensure_content_hash()
        assert len(item.content_hash) == 64

    def test_embedding_input(self):
        item = IntelItem(
            item_type=ItemType.PAPER,
            title="PQC Migration",
            abstract="Post-quantum cryptography for mobile.",
            source_name="semantic_scholar",
        )
        text = item.embedding_input()
        assert text.startswith("passage: ")
        assert "PQC Migration" in text
        assert "Post-quantum" in text


class TestMetadataModels:
    def test_news_metadata(self):
        m = NewsMetadata(keywords=["ai", "llm"], collector="tavily")
        assert m.keywords == ["ai", "llm"]

    def test_paper_metadata(self):
        m = PaperMetadata(authors=["Alice", "Bob"], citation_count=42, venue="ICML 2026")
        assert m.citation_count == 42

    def test_patent_metadata(self):
        m = PatentMetadata(applicant="Samsung", ipc_codes=["H04L9/00"])
        assert m.applicant == "Samsung"


class TestItemTopic:
    def test_defaults(self):
        link = IntelItemTopic(item_id=1, topic_id=2)
        assert link.relevance == 1.0
        assert link.assigned_by.value == "collector"


class TestItemRelation:
    def test_defaults(self):
        rel = IntelItemRelation(source_id=1, target_id=2, relation_type="cites")
        assert rel.confidence == 1.0


class TestCollectorConversions:
    def test_news_from_collector(self):
        raw = {
            "title": "AI Breakthrough",
            "url": "https://example.com/news",
            "source": "example.com",
            "published_date": "2026-03-01",
            "summary": "Major AI advancement.",
            "reliability_tag": "B",
            "collector": "tavily",
        }
        item = news_from_collector(raw)
        assert item.item_type == ItemType.NEWS
        assert item.title == "AI Breakthrough"
        assert item.external_id == "https://example.com/news"
        assert item.reliability == ReliabilityTag.REPUTABLE
        assert item.metadata["collector"] == "tavily"

    def test_paper_from_collector(self):
        raw = {
            "external_id": "ss:abc123",
            "source": "semantic_scholar",
            "title": "PQC Survey",
            "authors": ["Alice"],
            "published_date": "2026-01-15",
            "abstract": "A survey of PQC.",
            "citation_count": 10,
            "reliability_tag": "A",
            "raw_url": "https://arxiv.org/abs/2026.12345",
        }
        item = paper_from_collector(raw)
        assert item.item_type == ItemType.PAPER
        assert item.external_id == "ss:abc123"
        assert item.metadata["authors"] == ["Alice"]

    def test_patent_from_collector(self):
        raw = {
            "external_id": "uspto:US12345",
            "source": "uspto",
            "title": "Method for PQC",
            "applicant": "Samsung",
            "filing_date": "2025-06-01",
            "publication_date": "2026-01-01",
            "ipc_codes": ["H04L9/00"],
            "abstract": "A method for post-quantum.",
            "reliability_tag": "A",
            "raw_url": "https://patents.google.com/patent/US12345",
        }
        item = patent_from_collector(raw)
        assert item.item_type == ItemType.PATENT
        assert item.metadata["applicant"] == "Samsung"
        assert item.metadata["ipc_codes"] == ["H04L9/00"]
