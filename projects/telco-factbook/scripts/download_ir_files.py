"""Generic IR file downloader via Playwright browser automation.

Navigates to any IR earnings page, optionally selects a year,
waits for dynamic content, and downloads files matching a pattern.

Usage:
    # SKT press releases
    uv run --extra browser python scripts/download_ir_files.py \\
        --url https://www.sktelecom.com/investor/lib/announce.do \\
        --pattern "PressRelease.*\\.pdf" --year 2025

    # KT PDF files
    uv run --extra browser python scripts/download_ir_files.py \\
        --url https://m.corp.kt.com/html/investors/resources/earnings.html \\
        --pattern "\\.pdf$" --year 2025

    # All Excel files from any page
    uv run --extra browser python scripts/download_ir_files.py \\
        --url https://example.com/ir --pattern "\\.xlsx$"
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Download files from IR earnings pages via browser automation",
    )
    parser.add_argument(
        "--url", required=True, help="IR page URL to navigate to",
    )
    parser.add_argument(
        "--pattern", default=r"\.pdf$",
        help="Regex pattern to match file URLs (default: '\\.pdf$')",
    )
    parser.add_argument(
        "--year", type=int, default=None,
        help="Year to select from dropdown (if available)",
    )
    parser.add_argument(
        "--output-dir", type=Path, default=None,
        help="Output directory (default: data/downloads/<domain>/)",
    )
    parser.add_argument(
        "--headless", action="store_true",
        help="Run in headless mode (default: headful)",
    )
    parser.add_argument(
        "--wait", type=float, default=3.0,
        help="Extra wait time in seconds for AJAX content (default: 3.0)",
    )
    return parser.parse_args()


def _select_year(page, year: int) -> None:  # noqa: ANN001
    """Try to select a year from any dropdown on the page."""
    year_str = str(year)

    # Strategy 1: find <select> containing the year as an option
    selects = page.locator("select")
    for i in range(selects.count()):
        select = selects.nth(i)
        try:
            options_text = select.inner_text(timeout=2000)
            if year_str in options_text:
                select.select_option(year_str)
                logger.info("Selected year %d from dropdown", year)

                # Look for a confirm/submit button nearby
                for label in ("확인", "조회", "검색", "Submit", "Search", "Go"):
                    btn = page.get_by_text(label, exact=True)
                    if btn.count() > 0:
                        btn.first.click()
                        logger.info("Clicked '%s' button", label)
                        return
                # No button found — the select change event may auto-trigger
                logger.info("No confirm button found; relying on change event")
                return
        except Exception:
            continue

    logger.warning("No year dropdown found for %d", year)


def _collect_file_urls(page, pattern: re.Pattern[str], base_url: str) -> list[str]:  # noqa: ANN001
    """Collect all file URLs from the page matching the pattern."""
    html = page.content()

    # Extract all href values from anchor tags
    href_re = re.compile(r'href=["\']([^"\']+)["\']', re.IGNORECASE)
    all_hrefs = href_re.findall(html)

    urls: list[str] = []
    seen: set[str] = set()

    for href in all_hrefs:
        if pattern.search(href):
            url = href if href.startswith("http") else urljoin(base_url, href)
            if url not in seen:
                seen.add(url)
                urls.append(url)

    return urls


def download_files(
    url: str,
    pattern: re.Pattern[str],
    year: int | None,
    headless: bool,
    output_dir: Path,
    wait: float,
) -> list[Path]:
    """Navigate to page and download all matching files."""
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

    # Derive base URL for resolving relative links
    parsed = urlparse(url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()

        # 1. Navigate
        logger.info("Navigating to %s", url)
        try:
            page.goto(url, wait_until="load", timeout=60000)
        except Exception:
            logger.warning("Page load timed out, proceeding anyway")
        page.wait_for_timeout(3000)

        # 2. Select year if specified
        if year is not None:
            _select_year(page, year)
            page.wait_for_timeout(3000)

        # 3. Wait for dynamic content
        page.wait_for_timeout(int(wait * 1000))

        # 4. Collect matching URLs
        file_urls = _collect_file_urls(page, pattern, base_url)
        logger.info("Found %d file(s) matching pattern '%s'", len(file_urls), pattern.pattern)

        if not file_urls:
            logger.warning("No matching files found")
            browser.close()
            return []

        # 5. Download each file
        for file_url in file_urls:
            filename = Path(urlparse(file_url).path).name
            if not filename:
                continue
            dest = output_dir / filename

            logger.info("Downloading: %s", filename)
            try:
                response = page.request.get(file_url)
                if response.ok:
                    dest.write_bytes(response.body())
                    size_kb = dest.stat().st_size / 1024
                    logger.info("  Saved: %s (%.0f KB)", dest.name, size_kb)
                    downloaded.append(dest)
                else:
                    logger.error("  HTTP %d for %s", response.status, filename)
            except Exception as e:
                logger.error("  Failed: %s — %s", filename, e)

        browser.close()

    return downloaded


def main() -> None:
    """Entry point."""
    args = parse_args()

    # Default output dir: data/downloads/<domain>/
    if args.output_dir is None:
        domain = urlparse(args.url).netloc.replace(".", "_")
        project_root = Path(__file__).resolve().parent.parent
        output_dir = project_root / "data" / "downloads" / domain
    else:
        output_dir = args.output_dir

    pattern = re.compile(args.pattern, re.IGNORECASE)

    logger.info("=== IR File Downloader ===")
    logger.info("URL:     %s", args.url)
    logger.info("Pattern: %s", args.pattern)
    logger.info("Year:    %s", args.year or "(all)")
    logger.info("Output:  %s", output_dir)

    downloaded = download_files(
        url=args.url,
        pattern=pattern,
        year=args.year,
        headless=args.headless,
        output_dir=output_dir,
        wait=args.wait,
    )

    if downloaded:
        logger.info("=== Download Summary ===")
        total_size = sum(f.stat().st_size for f in downloaded)
        for f in downloaded:
            logger.info("  %s  (%.0f KB)", f.name, f.stat().st_size / 1024)
        logger.info("Total: %d files, %.0f KB", len(downloaded), total_size / 1024)
    else:
        logger.warning("No files downloaded")


if __name__ == "__main__":
    main()
