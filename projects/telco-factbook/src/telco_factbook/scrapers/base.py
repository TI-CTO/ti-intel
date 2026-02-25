"""Base scraper interface for IR sites."""

from __future__ import annotations

import hashlib
import logging
from abc import ABC, abstractmethod
from pathlib import Path

import httpx

from telco_factbook.models import Carrier, IRDocument

logger = logging.getLogger(__name__)


class BaseScraper(ABC):
    """Abstract base class for IR site scrapers."""

    carrier: Carrier

    def __init__(self, timeout: int = 30) -> None:
        self._client = httpx.Client(
            timeout=timeout,
            follow_redirects=True,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            },
        )

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def __enter__(self) -> BaseScraper:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    @abstractmethod
    def fetch_available_years(self) -> list[int]:
        """Return list of years with available IR documents."""
        ...

    @abstractmethod
    def fetch_documents(self, year: int) -> list[IRDocument]:
        """Return list of available IR documents for a given year."""
        ...

    def download_file(self, doc: IRDocument, dest_dir: Path) -> Path:
        """Download a file and return the local path."""
        carrier_dir = dest_dir / self.carrier.value.lower()
        carrier_dir.mkdir(parents=True, exist_ok=True)

        filename = f"{doc.year}Q{doc.quarter}_{doc.doc_type.value}.{doc.file_format}"
        dest_path = carrier_dir / filename

        if dest_path.exists():
            logger.info("File already exists: %s", dest_path)
            return dest_path

        logger.info("Downloading %s → %s", doc.source_url, dest_path)
        response = self._client.get(doc.source_url)
        response.raise_for_status()

        dest_path.write_bytes(response.content)

        doc.local_path = dest_path
        doc.file_hash = hashlib.sha256(response.content).hexdigest()

        logger.info("Downloaded %d bytes", len(response.content))
        return dest_path
