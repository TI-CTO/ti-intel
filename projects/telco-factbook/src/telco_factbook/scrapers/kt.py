"""KT IR site scraper using REST API."""

from __future__ import annotations

import logging

from telco_factbook.models import Carrier, DocType, IRDocument
from telco_factbook.scrapers.base import BaseScraper

logger = logging.getLogger(__name__)

_BASE_URL = "https://corp.kt.com"
_YEARS_API = f"{_BASE_URL}/corp/announcements/v1.0/achievements/years"
_ACHIEVEMENTS_API = f"{_BASE_URL}/corp/announcements/v1.0/achievements"


class KTScraper(BaseScraper):
    """Scraper for KT IR earnings page via REST API."""

    carrier = Carrier.KT

    def fetch_available_years(self) -> list[int]:
        """Fetch list of years with available earnings data."""
        response = self._client.get(
            _YEARS_API,
            params={"langDivType": "KOR"},
        )
        response.raise_for_status()
        data = response.json()

        years_raw = data.get("yeareList", data.get("yearList", []))
        years: list[int] = []
        for item in years_raw:
            if isinstance(item, dict):
                year_val = item.get("yyInfo") or item.get("year")
                if year_val:
                    years.append(int(year_val))
            elif isinstance(item, (int, str)):
                years.append(int(item))

        logger.info("KT available years: %s", sorted(years, reverse=True))
        return sorted(years, reverse=True)

    def fetch_documents(self, year: int) -> list[IRDocument]:
        """Fetch available IR documents for a given year."""
        response = self._client.get(
            _ACHIEVEMENTS_API,
            params={"langDivType": "KOR"},
        )
        response.raise_for_status()
        data = response.json()

        items = data.get("achPreList", [])
        documents: list[IRDocument] = []

        for item in items:
            item_year = int(item.get("yyInfo", 0))
            if item_year != year:
                continue

            quarter = self._extract_quarter(item)
            if quarter is None:
                continue

            # Excel financial statement (saveFilePath02 + saveFileNm02)
            excel_path = item.get("saveFilePath02", "")
            excel_name = item.get("saveFileNm02", "")
            if excel_path and excel_name:
                documents.append(
                    IRDocument(
                        carrier=Carrier.KT,
                        year=year,
                        quarter=quarter,
                        doc_type=DocType.FINANCIAL_STATEMENT,
                        file_format="xlsx",
                        source_url=f"{_BASE_URL}{excel_path}{excel_name}",
                    )
                )

            # PDF briefing (saveFilePath01 + saveFileNm01)
            pdf_path = item.get("saveFilePath01", "")
            pdf_name = item.get("saveFileNm01", "")
            if pdf_path and pdf_name:
                documents.append(
                    IRDocument(
                        carrier=Carrier.KT,
                        year=year,
                        quarter=quarter,
                        doc_type=DocType.BRIEFING,
                        file_format="pdf",
                        source_url=f"{_BASE_URL}{pdf_path}{pdf_name}",
                    )
                )

        logger.info(
            "KT %d: found %d documents (%s)",
            year,
            len(documents),
            ", ".join(f"Q{d.quarter}" for d in documents if d.doc_type == DocType.FINANCIAL_STATEMENT),
        )
        return documents

    def _extract_quarter(self, item: dict) -> int | None:
        """Extract quarter number from API response item."""
        title = item.get("title", "") or item.get("subjNm", "")
        title_lower = title.lower()

        for q in range(1, 5):
            if f"{q}q" in title_lower or f"{q}분기" in title:
                return q

        # Check qqInfo field
        qq_info = item.get("qqInfo", "")
        if qq_info:
            try:
                q = int(qq_info)
                if 1 <= q <= 4:
                    return q
            except (ValueError, TypeError):
                pass

        logger.warning("Could not extract quarter from: %s", title)
        return None
