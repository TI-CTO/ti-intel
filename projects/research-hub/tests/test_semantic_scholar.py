"""Tests for the Semantic Scholar normalisation logic."""

from research_hub.collectors.semantic_scholar import _normalise


def test_normalise_full_paper():
    raw = {
        "paperId": "abc123",
        "title": "Deep Learning for Network Slicing",
        "authors": [{"name": "Alice Kim"}, {"name": "Bob Lee"}],
        "year": 2024,
        "publicationDate": "2024-03-15",
        "citationCount": 37,
        "abstract": "We propose a new approach...",
        "externalIds": {"ArXiv": "2403.00001"},
        "url": "https://www.semanticscholar.org/paper/abc123",
    }
    paper = _normalise(raw)
    assert paper is not None
    assert paper["external_id"] == "ss:abc123"
    assert paper["source"] == "semantic_scholar"
    assert paper["title"] == "Deep Learning for Network Slicing"
    assert paper["authors"] == ["Alice Kim", "Bob Lee"]
    assert paper["published_date"] == "2024-03-15"
    assert paper["citation_count"] == 37
    assert paper["reliability_tag"] == "A"


def test_normalise_missing_paper_id():
    raw = {"title": "No ID paper", "year": 2023}
    assert _normalise(raw) is None


def test_normalise_missing_title():
    raw = {"paperId": "def456", "title": "", "year": 2023}
    assert _normalise(raw) is None


def test_normalise_year_only():
    raw = {
        "paperId": "ghi789",
        "title": "Quantum Comms",
        "year": 2022,
        "publicationDate": None,
        "citationCount": 0,
        "authors": [],
        "abstract": None,
        "externalIds": {},
        "url": None,
    }
    paper = _normalise(raw)
    assert paper is not None
    assert paper["published_date"] == "2022-01-01"
    assert paper["raw_url"] is None


def test_normalise_arxiv_url_fallback():
    raw = {
        "paperId": "jkl012",
        "title": "Edge AI",
        "year": 2023,
        "publicationDate": None,
        "citationCount": 5,
        "authors": [],
        "abstract": "",
        "externalIds": {"ArXiv": "2303.12345"},
        "url": None,
    }
    paper = _normalise(raw)
    assert paper is not None
    assert paper["raw_url"] == "https://arxiv.org/abs/2303.12345"
