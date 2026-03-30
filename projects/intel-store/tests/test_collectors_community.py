"""Tests for community collector _normalise functions (no network calls)."""

from intel_store.collectors import hackernews, polymarket, reddit
from intel_store.models import (
    CommunityMetadata,
    ItemType,
    community_from_collector,
)


class TestRedditNormalise:
    def test_valid_post(self):
        data = {
            "id": "abc123",
            "title": "AI Agent Framework Comparison",
            "permalink": "/r/MachineLearning/comments/abc123/ai_agent/",
            "selftext": "Here is my comparison of agent frameworks...",
            "score": 150,
            "num_comments": 42,
            "subreddit": "MachineLearning",
            "created_utc": 1711756800.0,  # 2024-03-30
        }
        result = reddit._normalise(data)
        assert result is not None
        assert result["external_id"] == "reddit:abc123"
        assert result["title"] == "AI Agent Framework Comparison"
        assert result["platform"] == "reddit"
        assert result["engagement"] == 150
        assert result["comments"] == 42
        assert result["subreddit"] == "MachineLearning"
        assert result["reliability_tag"] == "B"  # score >= 50

    def test_low_engagement_reliability(self):
        data = {
            "id": "low1",
            "title": "Small Post",
            "permalink": "/r/test/comments/low1/small/",
            "score": 10,
            "num_comments": 2,
            "created_utc": 1711756800.0,
        }
        result = reddit._normalise(data)
        assert result is not None
        assert result["reliability_tag"] == "C"  # score < 50

    def test_missing_title(self):
        data = {"id": "nope", "title": "", "permalink": "/r/test/nope/"}
        assert reddit._normalise(data) is None

    def test_missing_id(self):
        data = {"title": "No ID"}
        assert reddit._normalise(data) is None


class TestHackernewsNormalise:
    def test_valid_story(self):
        hit = {
            "objectID": "12345",
            "title": "Show HN: New AI Tool",
            "url": "https://example.com/tool",
            "points": 200,
            "num_comments": 80,
            "created_at": "2026-03-28T10:00:00.000Z",
        }
        result = hackernews._normalise(hit)
        assert result is not None
        assert result["external_id"] == "hn:12345"
        assert result["url"] == "https://example.com/tool"
        assert result["engagement"] == 200
        assert result["published_date"] == "2026-03-28"
        assert result["reliability_tag"] == "B"  # points >= 100

    def test_no_url_falls_back_to_hn_link(self):
        hit = {
            "objectID": "67890",
            "title": "Ask HN: Best practices?",
            "url": None,
            "points": 50,
            "num_comments": 30,
            "created_at": "2026-03-28T10:00:00.000Z",
        }
        result = hackernews._normalise(hit)
        assert result is not None
        assert result["url"] == "https://news.ycombinator.com/item?id=67890"
        assert result["reliability_tag"] == "C"  # points < 100

    def test_missing_title(self):
        hit = {"objectID": "111", "title": ""}
        assert hackernews._normalise(hit) is None

    def test_missing_object_id(self):
        hit = {"title": "No ID"}
        assert hackernews._normalise(hit) is None


class TestPolymarketNormalise:
    def test_valid_market(self):
        market = {
            "question": "Will GPT-5 be released by 2026?",
            "slug": "will-gpt5-release-2026",
            "outcomePrices": "[0.72, 0.28]",
            "volume": "250000",
            "liquidity": "50000",
            "endDate": "2026-12-31T23:59:59Z",
        }
        result = polymarket._normalise(market)
        assert result is not None
        assert result["external_id"] == "poly:will-gpt5-release-2026"
        assert result["title"] == "Will GPT-5 be released by 2026?"
        assert result["platform"] == "polymarket"
        assert result["engagement"] == 250000
        assert result["outcome_prices"] == {"Yes": 0.72, "No": 0.28}
        assert result["liquidity"] == 50000.0
        assert result["reliability_tag"] == "B"  # volume >= 100k

    def test_low_volume_reliability(self):
        market = {
            "question": "Small market?",
            "slug": "small-market",
            "volume": "5000",
            "liquidity": "1000",
        }
        result = polymarket._normalise(market)
        assert result is not None
        assert result["reliability_tag"] == "C"  # volume < 100k

    def test_missing_question(self):
        market = {"slug": "no-question", "volume": "1000"}
        assert polymarket._normalise(market) is None

    def test_missing_slug(self):
        market = {"question": "No slug?"}
        assert polymarket._normalise(market) is None

    def test_outcome_prices_dict_format(self):
        market = {
            "question": "Dict prices?",
            "slug": "dict-prices",
            "outcomePrices": '{"Yes": 0.65, "No": 0.35}',
            "volume": "10000",
        }
        result = polymarket._normalise(market)
        assert result is not None
        # JSON string dict should be parsed
        assert result["outcome_prices"] is not None


class TestCommunityFromCollector:
    def test_reddit_item(self):
        raw = {
            "external_id": "reddit:abc",
            "title": "Test Reddit Post",
            "url": "https://reddit.com/r/test/abc",
            "source": "reddit",
            "platform": "reddit",
            "published_date": "2026-03-28",
            "summary": "Post content",
            "engagement": 100,
            "comments": 20,
            "subreddit": "test",
            "collector": "reddit",
            "reliability_tag": "B",
        }
        item = community_from_collector(raw)
        assert item.item_type == ItemType.COMMUNITY
        assert item.external_id == "reddit:abc"
        assert item.source_name == "reddit"
        assert item.metadata["platform"] == "reddit"
        assert item.metadata["engagement"] == 100
        assert item.metadata["subreddit"] == "test"

    def test_polymarket_item(self):
        raw = {
            "external_id": "poly:test-market",
            "title": "Will X happen?",
            "url": "https://polymarket.com/event/test-market",
            "source": "polymarket",
            "platform": "polymarket",
            "summary": "Probability: Yes 72%, No 28%. Volume: $250,000",
            "engagement": 250000,
            "comments": 0,
            "collector": "polymarket",
            "outcome_prices": {"Yes": 0.72, "No": 0.28},
            "liquidity": 50000.0,
            "reliability_tag": "B",
        }
        item = community_from_collector(raw)
        assert item.item_type == ItemType.COMMUNITY
        assert item.metadata["outcome_prices"] == {"Yes": 0.72, "No": 0.28}
        assert item.metadata["liquidity"] == 50000.0


class TestCommunityMetadataDefaults:
    def test_defaults(self):
        meta = CommunityMetadata()
        assert meta.platform == ""
        assert meta.engagement == 0
        assert meta.comments == 0
        assert meta.subreddit is None
        assert meta.outcome_prices is None
        assert meta.liquidity is None
