"""Tests for GDELT collector normalisation and HTTP behaviour."""

from unittest.mock import MagicMock, patch

import pytest

from trend_tracker.collectors.gdelt import _normalise, collect


# ---------------------------------------------------------------------------
# _normalise
# ---------------------------------------------------------------------------


class TestNormalise:
    def test_valid_article_returns_dict(self):
        raw = {
            "title": "5G Deployment News",
            "url": "https://example.com/5g",
            "seendate": "20260215T120000Z",
            "domain": "example.com",
        }
        result = _normalise(raw)
        assert result is not None
        assert result["title"] == "5G Deployment News"
        assert result["url"] == "https://example.com/5g"

    def test_missing_title_returns_none(self):
        raw = {"url": "https://example.com/5g", "seendate": "20260215T120000Z"}
        assert _normalise(raw) is None

    def test_empty_title_returns_none(self):
        raw = {"title": "   ", "url": "https://example.com/5g"}
        assert _normalise(raw) is None

    def test_missing_url_returns_none(self):
        raw = {"title": "Some Title", "seendate": "20260215T120000Z"}
        assert _normalise(raw) is None

    def test_empty_url_returns_none(self):
        raw = {"title": "Some Title", "url": ""}
        assert _normalise(raw) is None

    def test_date_parsed_correctly(self):
        raw = {
            "title": "Test",
            "url": "https://example.com",
            "seendate": "20260215T120000Z",
        }
        result = _normalise(raw)
        assert result["published_date"] == "2026-02-15"

    def test_date_with_short_seendate(self):
        """seendate shorter than 8 chars should produce None published_date."""
        raw = {
            "title": "Test",
            "url": "https://example.com",
            "seendate": "2026",
        }
        result = _normalise(raw)
        assert result["published_date"] is None

    def test_missing_seendate_gives_none_published_date(self):
        raw = {"title": "Test", "url": "https://example.com"}
        result = _normalise(raw)
        assert result["published_date"] is None

    def test_domain_used_as_source(self):
        raw = {
            "title": "Test",
            "url": "https://reuters.com/news",
            "domain": "reuters.com",
        }
        result = _normalise(raw)
        assert result["source"] == "reuters.com"

    def test_missing_domain_falls_back_to_gdelt(self):
        raw = {"title": "Test", "url": "https://example.com"}
        result = _normalise(raw)
        assert result["source"] == "gdelt"

    def test_empty_domain_falls_back_to_gdelt(self):
        raw = {"title": "Test", "url": "https://example.com", "domain": ""}
        result = _normalise(raw)
        assert result["source"] == "gdelt"

    def test_reliability_tag_is_c(self):
        raw = {"title": "Test", "url": "https://example.com"}
        result = _normalise(raw)
        assert result["reliability_tag"] == "C"

    def test_collector_is_gdelt(self):
        raw = {"title": "Test", "url": "https://example.com"}
        result = _normalise(raw)
        assert result["collector"] == "gdelt"

    def test_summary_is_none(self):
        raw = {"title": "Test", "url": "https://example.com"}
        result = _normalise(raw)
        assert result["summary"] is None

    def test_schema_keys_present(self):
        raw = {"title": "Test", "url": "https://example.com"}
        result = _normalise(raw)
        expected_keys = {
            "title", "url", "source", "published_date",
            "summary", "reliability_tag", "collector",
        }
        assert set(result.keys()) == expected_keys

    def test_title_and_url_stripped(self):
        raw = {"title": "  Padded Title  ", "url": "  https://example.com  "}
        result = _normalise(raw)
        assert result["title"] == "Padded Title"
        assert result["url"] == "https://example.com"


# ---------------------------------------------------------------------------
# collect — HTTP layer (mocked)
# ---------------------------------------------------------------------------


class TestCollect:
    def _make_mock_response(self, articles: list[dict]) -> MagicMock:
        mock_resp = MagicMock()
        mock_resp.json.return_value = {"articles": articles}
        mock_resp.raise_for_status = MagicMock()
        return mock_resp

    @patch("trend_tracker.collectors.gdelt.time.sleep")
    @patch("trend_tracker.collectors.gdelt.httpx.Client")
    def test_successful_response_returns_normalised_items(self, mock_client_cls, mock_sleep):
        articles = [
            {"title": "Article A", "url": "https://a.com", "domain": "a.com", "seendate": "20260215T000000Z"},
            {"title": "Article B", "url": "https://b.com", "domain": "b.com", "seendate": "20260216T000000Z"},
        ]
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.get.return_value = self._make_mock_response(articles)
        mock_client_cls.return_value = mock_client

        result = collect("5G news", limit=10)

        assert len(result) == 2
        assert result[0]["title"] == "Article A"
        assert result[1]["title"] == "Article B"

    @patch("trend_tracker.collectors.gdelt.time.sleep")
    @patch("trend_tracker.collectors.gdelt.httpx.Client")
    def test_invalid_articles_filtered_out(self, mock_client_cls, mock_sleep):
        """Articles missing title or url should be excluded from results."""
        articles = [
            {"title": "Valid", "url": "https://valid.com"},
            {"url": "https://no-title.com"},   # missing title
            {"title": "No URL"},               # missing url
        ]
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.get.return_value = self._make_mock_response(articles)
        mock_client_cls.return_value = mock_client

        result = collect("query")
        assert len(result) == 1
        assert result[0]["title"] == "Valid"

    @patch("trend_tracker.collectors.gdelt.time.sleep")
    @patch("trend_tracker.collectors.gdelt.httpx.Client")
    def test_empty_articles_returns_empty_list(self, mock_client_cls, mock_sleep):
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.get.return_value = self._make_mock_response([])
        mock_client_cls.return_value = mock_client

        result = collect("query")
        assert result == []

    @patch("trend_tracker.collectors.gdelt.httpx.Client")
    def test_http_status_error_returns_empty(self, mock_client_cls):
        import httpx

        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_response = MagicMock()
        mock_response.status_code = 429
        mock_response.text = "Too Many Requests"
        mock_client.get.side_effect = httpx.HTTPStatusError(
            "429", request=MagicMock(), response=mock_response
        )
        mock_client_cls.return_value = mock_client

        result = collect("query")
        assert result == []

    @patch("trend_tracker.collectors.gdelt.httpx.Client")
    def test_request_error_returns_empty(self, mock_client_cls):
        import httpx

        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.get.side_effect = httpx.RequestError("Connection refused")
        mock_client_cls.return_value = mock_client

        result = collect("query")
        assert result == []

    @patch("trend_tracker.collectors.gdelt.httpx.Client")
    def test_json_parse_error_returns_empty(self, mock_client_cls):
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_resp = MagicMock()
        mock_resp.raise_for_status = MagicMock()
        mock_resp.json.side_effect = ValueError("invalid JSON")
        mock_client.get.return_value = mock_resp
        mock_client_cls.return_value = mock_client

        result = collect("query")
        assert result == []

    @patch("trend_tracker.collectors.gdelt.time.sleep")
    @patch("trend_tracker.collectors.gdelt.httpx.Client")
    def test_limit_clamped_to_250(self, mock_client_cls, mock_sleep):
        """limit > 250 should be sent as 250 to the API."""
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.get.return_value = self._make_mock_response([])
        mock_client_cls.return_value = mock_client

        collect("query", limit=999)

        call_kwargs = mock_client.get.call_args
        params = call_kwargs[1].get("params") or call_kwargs[0][1]
        assert params["maxrecords"] == "250"

    @patch("trend_tracker.collectors.gdelt.time.sleep")
    @patch("trend_tracker.collectors.gdelt.httpx.Client")
    def test_limit_clamped_minimum_to_1(self, mock_client_cls, mock_sleep):
        """limit <= 0 should be sent as 1 to the API."""
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.get.return_value = self._make_mock_response([])
        mock_client_cls.return_value = mock_client

        collect("query", limit=0)

        call_kwargs = mock_client.get.call_args
        params = call_kwargs[1].get("params") or call_kwargs[0][1]
        assert params["maxrecords"] == "1"
