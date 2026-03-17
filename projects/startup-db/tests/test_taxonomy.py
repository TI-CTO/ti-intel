"""Tests for taxonomy module."""

from startup_db.taxonomy import (
    TAXONOMY,
    L1_BY_SUBCATEGORY,
    get_all_l3_slugs,
    get_l1_for_l3,
    get_l2_for_l3,
    get_l2_slugs_for_l1,
    get_l3_slugs_for_l1,
    get_l3_slugs_for_l2,
    is_valid_l3,
)


def test_total_l3_count():
    """Should have 25 L3 technologies."""
    assert len(get_all_l3_slugs()) == 25


def test_l1_domains():
    """Should have exactly 3 L1 domains."""
    assert set(TAXONOMY.keys()) == {"agentic-ai", "voice-ai", "secure-ai"}


def test_l3_per_l1():
    """Agentic AI has 12, Voice AI has 8, Secure AI has 5."""
    assert len(get_l3_slugs_for_l1("agentic-ai")) == 12
    assert len(get_l3_slugs_for_l1("voice-ai")) == 8
    assert len(get_l3_slugs_for_l1("secure-ai")) == 5


def test_get_l1_for_l3():
    assert get_l1_for_l3("adaptive-rag") == "agentic-ai"
    assert get_l1_for_l3("voice-cloning") == "voice-ai"
    assert get_l1_for_l3("secure-vector-search") == "secure-ai"
    assert get_l1_for_l3("nonexistent") is None


def test_get_l2_for_l3():
    assert get_l2_for_l3("adaptive-rag") == "intent-recognition"
    assert get_l2_for_l3("voice-cloning") == "speech-generation"
    assert get_l2_for_l3("nonexistent") is None


def test_get_l3_slugs_for_l2():
    slugs = get_l3_slugs_for_l2("speech-generation")
    assert "voice-cloning" in slugs
    assert "voice-synthesis" in slugs
    assert len(slugs) == 2


def test_get_l2_slugs_for_l1():
    l2s = get_l2_slugs_for_l1("voice-ai")
    assert "speech-perception-interaction" in l2s
    assert "personal-intelligence" in l2s
    assert "speech-generation" in l2s
    assert len(l2s) == 3


def test_is_valid_l3():
    assert is_valid_l3("adaptive-rag") is True
    assert is_valid_l3("nonexistent") is False


def test_l1_by_subcategory_keys():
    """Strategic domains should be in L1_BY_SUBCATEGORY."""
    assert L1_BY_SUBCATEGORY["RAG"] == "agentic-ai"
    assert L1_BY_SUBCATEGORY["Speech"] == "voice-ai"
    assert L1_BY_SUBCATEGORY["안심 / 보안"] == "secure-ai"


def test_no_duplicate_l3_slugs():
    """All L3 slugs should be unique across the taxonomy."""
    all_slugs = get_all_l3_slugs()
    assert len(all_slugs) == len(set(all_slugs))


def test_empty_l1_returns_empty():
    assert get_l3_slugs_for_l1("nonexistent") == []
    assert get_l2_slugs_for_l1("nonexistent") == []


def test_empty_l2_returns_empty():
    assert get_l3_slugs_for_l2("nonexistent") == []
