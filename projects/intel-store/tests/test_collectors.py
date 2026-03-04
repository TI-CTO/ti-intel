"""Tests for collector _normalise functions (no network calls)."""

from intel_store.collectors import (
    arxiv,
    gdelt,
    google_patents,
    naver_news,
    semantic_scholar,
    tavily,
)


class TestTavilyNormalise:
    def test_valid_result(self):
        raw = {
            "title": "Test Article",
            "url": "https://www.example.com/article",
            "content": "This is the article content for testing.",
            "published_date": "2026-03-01T12:00:00Z",
        }
        result = tavily._normalise(raw)
        assert result is not None
        assert result["title"] == "Test Article"
        assert result["source"] == "example.com"
        assert result["published_date"] == "2026-03-01"
        assert result["reliability_tag"] == "B"
        assert result["collector"] == "tavily"

    def test_missing_title(self):
        raw = {"url": "https://example.com"}
        assert tavily._normalise(raw) is None

    def test_missing_url(self):
        raw = {"title": "Test"}
        assert tavily._normalise(raw) is None


class TestGdeltNormalise:
    def test_valid_article(self):
        raw = {
            "title": "Global News",
            "url": "https://news.example.com/article",
            "seendate": "20260301T120000Z",
            "domain": "news.example.com",
        }
        result = gdelt._normalise(raw)
        assert result is not None
        assert result["title"] == "Global News"
        assert result["published_date"] == "2026-03-01"
        assert result["source"] == "news.example.com"
        assert result["reliability_tag"] == "C"

    def test_empty_seendate(self):
        raw = {"title": "No Date", "url": "https://example.com", "seendate": ""}
        result = gdelt._normalise(raw)
        assert result is not None
        assert result["published_date"] is None


class TestSemanticScholarNormalise:
    def test_valid_paper(self):
        raw = {
            "paperId": "abc123",
            "title": "PQC Survey Paper",
            "authors": [{"name": "Alice"}, {"name": "Bob"}],
            "year": 2026,
            "publicationDate": "2026-01-15",
            "citationCount": 42,
            "abstract": "A comprehensive survey.",
            "externalIds": {"ArXiv": "2026.12345"},
            "url": "https://api.semanticscholar.org/abc123",
        }
        result = semantic_scholar._normalise(raw)
        assert result is not None
        assert result["external_id"] == "ss:abc123"
        assert result["arxiv_id"] == "2026.12345"
        assert result["title"] == "PQC Survey Paper"
        assert result["authors"] == ["Alice", "Bob"]
        assert result["citation_count"] == 42
        assert result["reliability_tag"] == "A"

    def test_no_arxiv_id(self):
        raw = {
            "paperId": "xyz",
            "title": "Paper Without ArXiv",
            "externalIds": {},
        }
        result = semantic_scholar._normalise(raw)
        assert result is not None
        assert result["arxiv_id"] is None

    def test_no_paper_id(self):
        raw = {"title": "Test"}
        assert semantic_scholar._normalise(raw) is None


class TestArxivNormalise:
    def test_valid_entry(self):
        entry = {
            "id": "http://arxiv.org/abs/2301.12345v2",
            "title": "Fully Homomorphic Encryption Survey",
            "authors": [{"name": "Alice"}, {"name": "Bob"}],
            "summary": "A comprehensive survey on FHE schemes.",
            "published": "2023-01-30T18:00:00Z",
            "tags": [{"term": "cs.CR"}, {"term": "cs.AI"}],
        }
        result = arxiv._normalise(entry)
        assert result is not None
        assert result["external_id"] == "arxiv:2301.12345"
        assert result["title"] == "Fully Homomorphic Encryption Survey"
        assert result["authors"] == ["Alice", "Bob"]
        assert result["published_date"] == "2023-01-30"
        assert result["venue"] == "cs.CR, cs.AI"
        assert result["reliability_tag"] == "A"
        assert result["source"] == "arxiv"

    def test_no_id(self):
        entry = {"id": "", "title": "Test"}
        assert arxiv._normalise(entry) is None

    def test_no_title(self):
        entry = {"id": "http://arxiv.org/abs/2301.99999v1", "title": ""}
        assert arxiv._normalise(entry) is None


class TestArxivExtractId:
    def test_standard_url(self):
        assert arxiv._extract_arxiv_id("http://arxiv.org/abs/2301.12345v2") == "2301.12345"

    def test_no_version(self):
        assert arxiv._extract_arxiv_id("http://arxiv.org/abs/2301.12345") == "2301.12345"

    def test_five_digit_id(self):
        assert arxiv._extract_arxiv_id("http://arxiv.org/abs/2301.00001v1") == "2301.00001"

    def test_invalid_url(self):
        assert arxiv._extract_arxiv_id("https://example.com") is None


class TestGooglePatentsNormalise:
    def test_valid_patent(self):
        raw = {
            "patent_id": "US12345678B2",
            "title": "Method for Quantum Key Distribution",
            "snippet": "A novel method for secure quantum key distribution.",
            "assignee": "Samsung Electronics",
            "publication_date": "2026-01-01",
            "filing_date": "2025-06-01",
            "classifications": [{"code": "H04L9/00"}],
        }
        result = google_patents._normalise(raw)
        assert result is not None
        assert result["external_id"] == "gp:US12345678B2"
        assert result["source"] == "google_patents"
        assert result["applicant"] == "Samsung Electronics"
        assert result["ipc_codes"] == ["H04L9/00"]
        assert result["reliability_tag"] == "A"
        assert result["raw_url"] == "https://patents.google.com/patent/US12345678B2"

    def test_no_title(self):
        raw = {"patent_id": "US999", "title": ""}
        assert google_patents._normalise(raw) is None

    def test_no_patent_id(self):
        raw = {"title": "Some Patent"}
        assert google_patents._normalise(raw) is None


class TestNaverNewsNormalise:
    def test_valid_result(self):
        raw = {
            "title": "<b>양자암호</b> 통신 기술 발전",
            "originallink": "https://news.example.kr/article/123",
            "link": "https://n.news.naver.com/redirect/123",
            "description": "<b>양자암호</b> 기반의 보안 통신 기술이 발전하고 있다.",
            "pubDate": "Mon, 03 Mar 2026 09:00:00 +0900",
        }
        result = naver_news._normalise(raw)
        assert result is not None
        assert result["title"] == "양자암호 통신 기술 발전"  # HTML stripped
        assert result["url"] == "https://news.example.kr/article/123"  # originallink
        assert result["published_date"] == "2026-03-03"
        assert result["reliability_tag"] == "B"
        assert result["collector"] == "naver"
        assert "<b>" not in result["summary"]

    def test_missing_title(self):
        raw = {"title": "", "link": "https://example.com"}
        assert naver_news._normalise(raw) is None

    def test_fallback_to_link(self):
        raw = {
            "title": "Test",
            "originallink": "",
            "link": "https://n.news.naver.com/article/123",
        }
        result = naver_news._normalise(raw)
        assert result is not None
        assert result["url"] == "https://n.news.naver.com/article/123"


class TestNaverStripHtml:
    def test_removes_bold_tags(self):
        assert naver_news._strip_html("<b>양자</b>암호") == "양자암호"

    def test_unescapes_html_entities(self):
        assert naver_news._strip_html("&quot;hello&quot; &amp; world") == '"hello" & world'

    def test_empty_string(self):
        assert naver_news._strip_html("") == ""

    def test_no_tags(self):
        assert naver_news._strip_html("plain text") == "plain text"


class TestNaverParseDateRfc822:
    def test_valid_date(self):
        assert naver_news._parse_rfc822_date("Mon, 03 Mar 2026 09:00:00 +0900") == "2026-03-03"

    def test_empty_string(self):
        assert naver_news._parse_rfc822_date("") is None

    def test_invalid_date(self):
        assert naver_news._parse_rfc822_date("not a date") is None
