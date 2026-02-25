"""Tests for scraper modules."""

from unittest.mock import MagicMock, patch

import pytest

from telco_factbook.models import Carrier, DocType
from telco_factbook.scrapers.kt import KTScraper
from telco_factbook.scrapers.skt import SKTScraper


class TestKTScraper:
    """Tests for KT REST API scraper."""

    def test_fetch_documents_parses_response(self, sample_kt_response: dict) -> None:
        """KT scraper should extract Excel and PDF docs from API response."""
        scraper = KTScraper()

        with patch.object(scraper._client, "get") as mock_get:
            mock_resp = MagicMock()
            mock_resp.json.return_value = sample_kt_response
            mock_resp.raise_for_status = MagicMock()
            mock_get.return_value = mock_resp

            docs = scraper.fetch_documents(2024)

        excel_docs = [d for d in docs if d.doc_type == DocType.FINANCIAL_STATEMENT]
        assert len(excel_docs) == 2
        assert all(d.carrier == Carrier.KT for d in excel_docs)
        assert {d.quarter for d in excel_docs} == {2, 3}

        scraper.close()

    def test_extract_quarter_from_title(self) -> None:
        """Quarter extraction should handle various title formats."""
        scraper = KTScraper()

        assert scraper._extract_quarter({"title": "2024년 1분기 실적"}) == 1
        assert scraper._extract_quarter({"title": "3Q 2024 Earnings"}) == 3
        assert scraper._extract_quarter({"qqInfo": "2"}) == 2
        assert scraper._extract_quarter({"title": "연간 실적"}) is None

        scraper.close()


class TestSKTScraper:
    """Tests for SKT HTML scraper."""

    def test_fetch_documents_from_html(self, sample_skt_html: str) -> None:
        """SKT scraper should extract Excel links from HTML."""
        scraper = SKTScraper()

        with patch.object(scraper._client, "get") as mock_get:
            mock_resp = MagicMock()
            mock_resp.text = sample_skt_html
            mock_resp.raise_for_status = MagicMock()
            mock_get.return_value = mock_resp

            docs = scraper.fetch_documents(2024)

        excel_docs = [d for d in docs if d.doc_type == DocType.FINANCIAL_STATEMENT]
        assert len(excel_docs) == 2
        assert all(d.carrier == Carrier.SKT for d in excel_docs)

        scraper.close()

    def test_extract_quarter_and_year_from_url(self) -> None:
        """Quarter and year extraction from URL pattern should work."""
        scraper = SKTScraper()

        assert scraper._extract_quarter_and_year_from_url("FinancialStatements1Q24Engilsh.xlsx") == (1, 2024)
        assert scraper._extract_quarter_and_year_from_url("3Q24InvestorBriefing.pdf") == (3, 2024)
        assert scraper._extract_quarter_and_year_from_url("annual_report.pdf") is None

        scraper.close()
