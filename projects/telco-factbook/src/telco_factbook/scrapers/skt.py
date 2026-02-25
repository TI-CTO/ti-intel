"""SKT IR site scraper using HTML parsing."""

from __future__ import annotations

import logging
import re

from bs4 import BeautifulSoup

from telco_factbook.models import Carrier, DocType, IRDocument
from telco_factbook.scrapers.base import BaseScraper

logger = logging.getLogger(__name__)

_BASE_URL = "https://www.sktelecom.com"
_IR_PAGE = f"{_BASE_URL}/en/investor/lib/announce.do"


class SKTScraper(BaseScraper):
    """Scraper for SKT IR earnings page via HTML parsing.

    SKT's IR page always returns the latest Excel files regardless of
    paramYear. Each Excel file contains ~2 years of data, so we download
    the available files and rely on the parser to extract the correct
    year's data via column headers (e.g. "1Q24", "4Q25").
    """

    carrier = Carrier.SKT

    def fetch_available_years(self) -> list[int]:
        """Fetch list of years from the dropdown on the IR page."""
        response = self._client.get(_IR_PAGE)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        years: list[int] = []
        for option in soup.select("select option, .year-select option, [class*=year] option"):
            text = option.get_text(strip=True)
            if text.isdigit() and 2000 <= int(text) <= 2030:
                years.append(int(text))

        if not years:
            year_pattern = re.compile(r"(?:paramYear|year)\s*[=:]\s*['\"]?(\d{4})['\"]?")
            for script in soup.find_all("script"):
                if script.string:
                    for match in year_pattern.finditer(script.string):
                        y = int(match.group(1))
                        if 2000 <= y <= 2030:
                            years.append(y)

        if not years:
            from datetime import datetime

            current_year = datetime.now().year
            years = list(range(current_year, current_year - 5, -1))
            logger.warning("Could not detect years, using fallback: %s", years)

        years = sorted(set(years), reverse=True)
        logger.info("SKT available years: %s", years)
        return years

    def fetch_documents(self, year: int) -> list[IRDocument]:
        """Fetch available IR documents for a given year.

        Note: SKT page always returns the latest files. The parser handles
        year-specific column extraction from the multi-year Excel files.
        """
        response = self._client.get(_IR_PAGE)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        documents: list[IRDocument] = []
        seen_quarters: set[int] = set()

        for link in soup.find_all("a", href=True):
            href = link["href"]
            self._classify_link(href, year, documents, seen_quarters)

        for script in soup.find_all("script"):
            if script.string:
                self._extract_links_from_script(script.string, year, documents, seen_quarters)

        logger.info(
            "SKT %d: found %d documents (%s)",
            year,
            len(documents),
            ", ".join(f"Q{d.quarter}" for d in documents if d.doc_type == DocType.FINANCIAL_STATEMENT),
        )
        return documents

    def _classify_link(
        self, href: str, year: int, documents: list[IRDocument],
        seen_quarters: set[int],
    ) -> None:
        """Classify a link as Excel/PDF and extract quarter info."""
        href_lower = href.lower()

        # Excel financial statement
        if href_lower.endswith(".xlsx") or href_lower.endswith(".xls"):
            result = self._extract_quarter_and_year_from_url(href)
            if result:
                quarter, _file_year = result
                if quarter not in seen_quarters:
                    seen_quarters.add(quarter)
                    url = href if href.startswith("http") else f"{_BASE_URL}{href}"
                    documents.append(
                        IRDocument(
                            carrier=Carrier.SKT,
                            year=year,
                            quarter=quarter,
                            doc_type=DocType.FINANCIAL_STATEMENT,
                            file_format="xlsx",
                            source_url=url,
                        )
                    )

        # PDF briefing
        elif href_lower.endswith(".pdf") and "briefing" in href_lower:
            result = self._extract_quarter_and_year_from_url(href)
            if result:
                quarter, _ = result
                url = href if href.startswith("http") else f"{_BASE_URL}{href}"
                documents.append(
                    IRDocument(
                        carrier=Carrier.SKT,
                        year=year,
                        quarter=quarter,
                        doc_type=DocType.BRIEFING,
                        file_format="pdf",
                        source_url=url,
                    )
                )

    def _extract_links_from_script(
        self, script_text: str, year: int, documents: list[IRDocument],
        seen_quarters: set[int],
    ) -> None:
        """Extract file links from inline JavaScript."""
        url_pattern = re.compile(r'["\']([^"\']*(?:\.xlsx|\.xls|\.pdf)[^"\']*)["\']', re.IGNORECASE)
        for match in url_pattern.finditer(script_text):
            href = match.group(1)
            self._classify_link(href, year, documents, seen_quarters)

    def _extract_quarter_and_year_from_url(self, url: str) -> tuple[int, int] | None:
        """Extract quarter and year from file URL.

        Returns (quarter, full_year) or None.
        Examples:
            "FinancialStatements4Q25Engilsh.xlsx" → (4, 2025)
            "3Q24InvestorBriefing_Eng.pdf" → (3, 2024)
        """
        match = re.search(r"(\d)[Qq](\d{2})", url)
        if match:
            q = int(match.group(1))
            yy = int(match.group(2))
            if 1 <= q <= 4:
                full_year = 2000 + yy
                return (q, full_year)
        return None
