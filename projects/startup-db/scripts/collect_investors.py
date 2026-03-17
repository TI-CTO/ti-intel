"""Collect investor data for top-funded companies via web search.

Usage:
    cd projects/startup-db
    uv run python scripts/collect_investors.py [--limit 200] [--dry-run]

Pipeline:
  1. Query top N companies by total funding from su_funding_rounds
  2. For each company, search "{name} funding investors" via DuckDuckGo
  3. Extract investor names from search snippets using pattern matching
  4. Upsert into su_investors + link to su_round_investors
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
import time
from pathlib import Path

from duckduckgo_search import DDGS

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from startup_db.db import StartupRepository  # noqa: E402
from startup_db.models import slugify  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

# Well-known VC/investor names for validation
KNOWN_INVESTORS: set[str] = {
    "Sequoia Capital", "Andreessen Horowitz", "a16z", "Accel",
    "Benchmark", "Greylock", "Lightspeed Venture Partners",
    "Tiger Global", "SoftBank Vision Fund", "SoftBank",
    "Founders Fund", "Khosla Ventures", "Bessemer Venture Partners",
    "General Catalyst", "Insight Partners", "Coatue",
    "GV", "Y Combinator", "Kleiner Perkins",
    "NEA", "Battery Ventures", "Index Ventures",
    "Thrive Capital", "DST Global", "Spark Capital",
    "Union Square Ventures", "Ribbit Capital", "IVP",
    "Microsoft", "Google Ventures", "Alphabet",
    "Samsung Ventures", "Naver D2SF", "Kakao Ventures",
    "SBI Investment", "Korea Investment Partners",
    "KB Investment", "IMM Investment", "Altos Ventures",
    "Stonebridge Ventures", "Capstone Partners",
    "LB Investment", "Company K Partners", "Smilegate Investment",
    "Atinum Investment", "Premier Partners",
}

# Patterns to exclude (not investor names)
EXCLUDE_PATTERNS: list[re.Pattern] = [
    re.compile(r"^\d"),  # starts with number
    re.compile(r"^(the|a|an|in|at|on|for|and|or|of|to|by|as|is|was|has|had)\b", re.I),
    re.compile(r"\b(raised|funding|round|series|seed|valuation|ipo|total|million|billion)\b", re.I),
    re.compile(r"\b(company|startup|founded|ceo|cto|platform|product|revenue|growth)\b", re.I),
    re.compile(r"(\.com|\.io|\.ai|\.co)$", re.I),
    re.compile(r"^\w$"),  # single character
]

# Pattern to extract "led by X", "backed by X", "investors include X"
INVESTOR_EXTRACT_PATTERNS: list[re.Pattern] = [
    re.compile(
        r"(?:led by|backed by|from|investors?(?:\s+include)?)\s+"
        r"([A-Z][A-Za-z\s&'.]+?)(?:\s*[,.]|\s+and\s+|\s+with\s+|$)",
        re.I,
    ),
    re.compile(
        r"([A-Z][A-Za-z\s&'.]+?)\s+(?:led|co-led|participated|joined|invested)",
        re.I,
    ),
    re.compile(
        r"(?:participation from|investment from|funding from)\s+"
        r"([A-Z][A-Za-z\s&'.]+?)(?:\s*[,.]|$)",
        re.I,
    ),
]

# Comma/and splitter for multiple investors in one match
SPLIT_PATTERN = re.compile(r"\s*(?:,\s*(?:and\s+)?|(?:\s+and\s+))\s*")


def is_valid_investor_name(name: str) -> bool:
    """Check if extracted string looks like an investor name."""
    name = name.strip()
    if len(name) < 2 or len(name) > 60:
        return False
    for pat in EXCLUDE_PATTERNS:
        if pat.search(name):
            return False
    # Must start with uppercase or be a known investor
    if not name[0].isupper() and name not in KNOWN_INVESTORS:
        return False
    return True


def extract_investors_from_text(text: str) -> list[str]:
    """Extract investor names from a search snippet."""
    investors: list[str] = []

    # First check for known investors
    for known in KNOWN_INVESTORS:
        if known.lower() in text.lower():
            investors.append(known)

    # Then try pattern extraction
    for pattern in INVESTOR_EXTRACT_PATTERNS:
        for match in pattern.finditer(text):
            raw = match.group(1).strip()
            # Split by comma/and
            parts = SPLIT_PATTERN.split(raw)
            for part in parts:
                part = part.strip().rstrip(".")
                if is_valid_investor_name(part) and part not in investors:
                    investors.append(part)

    return investors


def guess_investor_type(name: str) -> str:
    """Guess investor type from name."""
    lower = name.lower()
    if any(kw in lower for kw in ["venture", "capital", "partners", "vc"]):
        return "vc"
    if any(kw in lower for kw in ["accelerator", "y combinator", "techstars"]):
        return "accelerator"
    if any(kw in lower for kw in ["samsung", "google", "microsoft", "naver", "kakao",
                                   "intel", "qualcomm", "nvidia"]):
        return "cvc"
    if any(kw in lower for kw in ["government", "fund of", "국민", "정책"]):
        return "government"
    return "vc"


def get_top_companies(repo: StartupRepository, limit: int) -> list[dict]:
    """Get top companies by total funding amount."""
    result = (
        repo._client.table("su_funding_rounds")
        .select("raised_amount,company_id,su_companies(id,name,slug,country)")
        .order("raised_amount", desc=True)
        .limit(2000)
        .execute()
    )

    company_totals: dict[str, dict] = {}
    for r in result.data:
        comp = r.get("su_companies", {})
        slug = comp.get("slug", "")
        if not slug:
            continue
        if slug not in company_totals:
            company_totals[slug] = {
                "id": comp.get("id"),
                "name": comp.get("name"),
                "slug": slug,
                "country": comp.get("country"),
                "total": 0,
                "round_ids": [],
            }
        company_totals[slug]["total"] += float(r.get("raised_amount") or 0)

    # Get round IDs for top companies
    top = sorted(company_totals.values(), key=lambda x: x["total"], reverse=True)[:limit]
    top_ids = {c["id"] for c in top}

    for r in result.data:
        comp = r.get("su_companies", {})
        if comp.get("id") in top_ids:
            slug = comp.get("slug", "")
            if slug in company_totals:
                company_totals[slug]["round_ids"].append(r)

    return top


def search_company_investors(company_name: str, country: str | None = None) -> list[str]:
    """Search web for investor data of a company."""
    query = f"{company_name} funding investors series round"
    if country and country == "한국":
        query = f"{company_name} 투자 라운드 투자자 VC"

    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
    except Exception as e:
        logger.warning("Search failed for %s: %s", company_name, e)
        return []

    all_investors: list[str] = []
    for r in results:
        text = f"{r.get('title', '')} {r.get('body', '')}"
        found = extract_investors_from_text(text)
        for inv in found:
            if inv not in all_investors:
                all_investors.append(inv)

    return all_investors


def main() -> None:
    """Run investor collection pipeline."""
    parser = argparse.ArgumentParser(description="Collect investor data via web search")
    parser.add_argument("--limit", type=int, default=200, help="Number of top companies")
    parser.add_argument("--dry-run", action="store_true", help="Print only, don't write to DB")
    parser.add_argument("--delay", type=float, default=1.5, help="Delay between searches (sec)")
    args = parser.parse_args()

    repo = StartupRepository()

    logger.info("Fetching top %d companies by funding...", args.limit)
    companies = get_top_companies(repo, args.limit)
    logger.info("Found %d companies to process", len(companies))

    stats = {"searched": 0, "investors_found": 0, "investors_upserted": 0, "errors": 0}

    for i, company in enumerate(companies, 1):
        name = company["name"]
        slug = company["slug"]
        country = company.get("country")

        logger.info("[%d/%d] Searching investors for: %s", i, len(companies), name)

        investors = search_company_investors(name, country)
        stats["searched"] += 1

        if not investors:
            logger.info("  No investors found")
            time.sleep(args.delay)
            continue

        logger.info("  Found %d investors: %s", len(investors), ", ".join(investors[:5]))
        stats["investors_found"] += len(investors)

        if args.dry_run:
            time.sleep(args.delay)
            continue

        # Upsert each investor
        for inv_name in investors:
            inv_slug = slugify(inv_name)
            inv_type = guess_investor_type(inv_name)
            try:
                result = repo._client.table("su_investors").upsert(
                    {
                        "slug": inv_slug,
                        "name": inv_name,
                        "investor_type": inv_type,
                        "country": None,
                        "description": None,
                        "website": None,
                        "metadata": json.dumps({"source": "web_search"}),
                    },
                    on_conflict="slug",
                ).execute()
                stats["investors_upserted"] += 1
            except Exception as e:
                logger.warning("  Failed to upsert investor %s: %s", inv_name, e)
                stats["errors"] += 1

        time.sleep(args.delay)

    logger.info("=" * 50)
    logger.info("Collection complete")
    logger.info("  Companies searched  : %d", stats["searched"])
    logger.info("  Investors found     : %d", stats["investors_found"])
    logger.info("  Investors upserted  : %d", stats["investors_upserted"])
    logger.info("  Errors              : %d", stats["errors"])


if __name__ == "__main__":
    main()
