"""Download SKT press release PDFs via Playwright browser automation.

Usage:
    uv run --extra browser python scripts/download_press_releases.py --year 2025
    uv run --extra browser python scripts/download_press_releases.py --year 2024 --headless
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

_BASE_URL = "https://www.sktelecom.com"
_IR_PAGE = f"{_BASE_URL}/investor/lib/announce.do"

_PRESS_RELEASE_PATTERN = re.compile(r"[Pp]ress[Rr]elease", re.IGNORECASE)
_QUARTER_PATTERN = re.compile(r"(\d)[Qq](\d{2})")


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Download SKT press release PDFs via browser automation",
    )
    parser.add_argument(
        "--year", type=int, required=True, help="Year to download (e.g. 2025)",
    )
    parser.add_argument(
        "--headless", action="store_true",
        help="Run in headless mode (default: headful — browser visible)",
    )
    parser.add_argument(
        "--output-dir", type=Path, default=None,
        help="Output directory (default: data/raw/skt/press_release/)",
    )
    return parser.parse_args()


def _collect_press_release_urls(page) -> list[str]:  # noqa: ANN001
    """Extract press release PDF URLs from the loaded page."""
    content = page.content()

    # Find all PDF hrefs containing "PressRelease"
    href_pattern = re.compile(
        r'href=["\']([^"\']*[Pp]ress[Rr]elease[^"\']*\.pdf)["\']',
    )
    matches = href_pattern.findall(content)

    urls: list[str] = []
    seen: set[str] = set()
    for href in matches:
        url = href if href.startswith("http") else f"{_BASE_URL}{href}"
        if url not in seen:
            seen.add(url)
            urls.append(url)

    return urls


def download_press_releases(
    year: int, headless: bool, output_dir: Path,
) -> list[Path]:
    """Navigate to SKT IR page and download press release PDFs."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        logger.error(
            "playwright is not installed. Run:\n"
            "  ~/.local/bin/uv run --extra browser playwright install chromium",
        )
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)
    downloaded: list[Path] = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()

        # 1. Navigate to IR page
        logger.info("Navigating to %s", _IR_PAGE)
        page.goto(_IR_PAGE, wait_until="domcontentloaded")
        page.wait_for_load_state("networkidle")

        # 2. Select year from dropdown and submit
        logger.info("Selecting year: %d", year)
        try:
            # Try <select> element first
            selects = page.locator("select")
            for i in range(selects.count()):
                select = selects.nth(i)
                options_text = select.inner_text()
                if str(year) in options_text:
                    select.select_option(str(year))
                    logger.info("Year selected via dropdown")
                    break

            # Click confirm button
            confirm = page.get_by_text("확인")
            if confirm.count() > 0:
                confirm.first.click()
                logger.info("Clicked confirm button")
        except Exception as e:
            logger.warning("Year selection failed (%s), continuing with default", e)

        # 3. Wait for AJAX content to load
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(3000)

        # 4. Collect press release PDF URLs
        urls = _collect_press_release_urls(page)
        logger.info("Found %d press release PDF link(s)", len(urls))

        if not urls:
            logger.warning("No press release links found for year %d", year)
            logger.info("Page title: %s", page.title())
            browser.close()
            return []

        # 5. Download each PDF via browser request context
        for url in urls:
            filename = Path(url).name
            dest = output_dir / filename

            logger.info("Downloading: %s", filename)
            try:
                response = page.request.get(url)
                if response.ok:
                    dest.write_bytes(response.body())
                    size_kb = dest.stat().st_size / 1024
                    logger.info("  Saved: %s (%.0f KB)", dest.name, size_kb)
                    downloaded.append(dest)
                else:
                    logger.error("  HTTP %d for %s", response.status, filename)
            except Exception as e:
                logger.error("  Failed to download %s: %s", filename, e)

        browser.close()

    return downloaded


def main() -> None:
    """Entry point."""
    args = parse_args()
    project_root = Path(__file__).resolve().parent.parent
    output_dir = args.output_dir or project_root / "data" / "raw" / "skt" / "press_release"

    logger.info("=== SKT Press Release Downloader ===")
    logger.info("Year: %d | Headless: %s | Output: %s", args.year, args.headless, output_dir)

    downloaded = download_press_releases(args.year, args.headless, output_dir)

    if downloaded:
        logger.info("=== Download Summary ===")
        total_size = 0
        for f in downloaded:
            size = f.stat().st_size
            total_size += size
            match = _QUARTER_PATTERN.search(f.name)
            quarter_info = f"Q{match.group(1)} 20{match.group(2)}" if match else "unknown"
            logger.info("  %s  %s  %.0f KB", f.name, quarter_info, size / 1024)
        logger.info("Total: %d files, %.0f KB", len(downloaded), total_size / 1024)
    else:
        logger.warning("No files downloaded")


if __name__ == "__main__":
    main()
