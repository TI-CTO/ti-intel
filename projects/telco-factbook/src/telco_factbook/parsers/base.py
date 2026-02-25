"""Base Excel parser interface."""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from pathlib import Path

from telco_factbook.models import Carrier, ParseResult

logger = logging.getLogger(__name__)


class BaseExcelParser(ABC):
    """Abstract base class for carrier-specific Excel parsers."""

    carrier: Carrier

    @abstractmethod
    def parse(self, file_path: Path, year: int, quarter: int) -> ParseResult:
        """Parse financial metrics from an Excel file.

        Args:
            file_path: Path to the downloaded Excel file.
            year: Fiscal year.
            quarter: Fiscal quarter (1-4).

        Returns:
            ParseResult with metrics, confidence score, and any issues.
        """
        ...

    def _safe_int(self, value: object) -> int | None:
        """Safely convert a cell value to int (million KRW)."""
        if value is None:
            return None
        try:
            num = float(str(value).replace(",", "").replace(" ", ""))
            return int(num)
        except (ValueError, TypeError):
            return None

    def _safe_float(self, value: object) -> float | None:
        """Safely convert a cell value to float (for percentages)."""
        if value is None:
            return None
        try:
            text = str(value).replace(",", "").replace(" ", "").replace("%", "")
            return float(text)
        except (ValueError, TypeError):
            return None
