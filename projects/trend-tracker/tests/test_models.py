"""Tests for trend_tracker.models."""

from datetime import date

from trend_tracker.models import NewsItem, ReliabilityTag, TrendSnapshot, WatchTopic


def test_news_item_defaults():
    item = NewsItem(
        title="Test news",
        source="Test Source",
        url="https://example.com/news",
        topic_id=1,
    )
    assert item.title == "Test news"
    assert item.collected_date == date.today()
    assert item.reliability_tag == ReliabilityTag.INDICATIVE
    assert item.keywords == []
    assert item.summary == ""


def test_news_item_with_all_fields():
    item = NewsItem(
        title="Full news",
        source="Reuters",
        url="https://reuters.com/test",
        topic_id=2,
        published_date=date(2026, 2, 20),
        summary="Test summary",
        reliability_tag=ReliabilityTag.REPUTABLE,
        keywords=["edge", "ai"],
    )
    assert item.reliability_tag == ReliabilityTag.REPUTABLE
    assert item.keywords == ["edge", "ai"]


def test_trend_snapshot_defaults():
    snap = TrendSnapshot(
        topic_id=1,
        summary="AI is growing",
    )
    assert snap.snapshot_date == date.today()
    assert snap.key_signals == []
    assert snap.item_count == 0
    assert snap.sentiment == "neutral"
    assert snap.change_level == "none"
    assert snap.source_type == "news"


def test_watch_topic_defaults():
    wt = WatchTopic(topic_id=1)
    assert wt.keywords == []
    assert wt.frequency == "weekly"
    assert wt.is_active is True
    assert wt.last_scanned is None


def test_reliability_tag_values():
    assert ReliabilityTag.OFFICIAL.value == "A"
    assert ReliabilityTag.REPUTABLE.value == "B"
    assert ReliabilityTag.INDICATIVE.value == "C"
    assert ReliabilityTag.UNVERIFIED.value == "D"
