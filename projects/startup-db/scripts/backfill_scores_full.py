"""Backfill remaining 4 score dimensions using heuristic signals from DB data.

Computes market_potential, team_quality, business_fit, traction, and overall_score
from existing data: funding amounts, round stages, investor quality, and category.

Usage:
    cd projects/startup-db
    uv run python scripts/backfill_scores_full.py [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from supabase import Client, create_client  # noqa: E402

from startup_db.config import settings  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s", datefmt="%H:%M:%S")
logger = logging.getLogger(__name__)

BATCH_SIZE = 100

# Top-tier investors (signal for team_quality)
TIER1_INVESTORS = {
    "andreessen-horowitz", "sequoia-capital", "benchmark", "accel",
    "kleiner-perkins", "greylock", "greylock-partners", "lightspeed-venture-partners",
    "founders-fund", "khosla-ventures", "general-catalyst", "index-ventures",
    "bessemer-venture-partners", "thrive-capital", "coatue", "coatue-management",
    "insight-partners", "tiger-global", "tiger-global-management",
    "y-combinator", "ivp", "battery-ventures",
}

TIER2_INVESTORS = {
    "softbank", "softbank-vision-fund", "softbank-vision-fund-2",
    "nvidia", "google", "google-ventures", "gv", "microsoft", "amazon",
    "salesforce-ventures", "new-enterprise-associates", "nea",
    "spark-capital", "union-square-ventures", "lux-capital",
    "radical-ventures", "menlo-ventures", "sapphire-ventures",
    "bain-capital-ventures", "wellington-management", "blackrock",
    "fidelity-management", "goldman-sachs",
}

# Round stage scoring (for traction)
ROUND_TRACTION: dict[str, int] = {
    "seed": 2,
    "series_a": 4,
    "series_b": 6,
    "series_c": 7,
    "series_d": 8,
    "series_e": 9,
    "series_f": 9,
    "ipo": 10,
    "acquired": 8,
    "other": 5,
}

# Sub-categories with high business fit (core to telco AI strategy)
HIGH_FIT_SUBCATS = {
    "AICC", "Speech", "안심 / 보안", "Agent", "Work Agent",
    "sLLM", "sLM", "RAG", "AI Ops", "mVoIP",
}
MEDIUM_FIT_SUBCATS = {
    "LLM", "Media Agent", "Coding Agent", "ML Ops", "MLOps",
    "AI 검색", "Cloud", "NPU", "개인화", "Data Ops",
}


def get_client() -> Client:
    """Return a Supabase client."""
    return create_client(settings.supabase_url, settings.supabase_key)


def fetch_paginated(client: Client, table: str, select: str) -> list[dict]:
    """Fetch all rows with pagination."""
    rows: list[dict] = []
    offset = 0
    while True:
        result = (
            client.table(table)
            .select(select)
            .range(offset, offset + BATCH_SIZE - 1)
            .execute()
        )
        rows.extend(result.data)
        if len(result.data) < BATCH_SIZE:
            break
        offset += BATCH_SIZE
    return rows


def compute_market_potential(funding_total: float, best_round: str, num_rounds: int) -> int:
    """Compute market_potential (1-10) from funding signals."""
    score = 1

    # Funding amount signal (log scale)
    if funding_total > 1_000_000_000:  # > $1B
        score = 9
    elif funding_total > 500_000_000:
        score = 8
    elif funding_total > 100_000_000:
        score = 7
    elif funding_total > 50_000_000:
        score = 6
    elif funding_total > 10_000_000:
        score = 5
    elif funding_total > 5_000_000:
        score = 4
    elif funding_total > 1_000_000:
        score = 3
    elif funding_total > 0:
        score = 2

    # Boost for later rounds
    round_boost = {"series_d": 1, "series_e": 1, "series_f": 1, "ipo": 2}
    score += round_boost.get(best_round, 0)

    return min(score, 10)


def compute_team_quality(investor_slugs: list[str]) -> int:
    """Compute team_quality (1-10) from investor tier signals."""
    tier1_count = sum(1 for s in investor_slugs if s in TIER1_INVESTORS)
    tier2_count = sum(1 for s in investor_slugs if s in TIER2_INVESTORS)
    total = len(investor_slugs)

    if tier1_count >= 3:
        return 9
    elif tier1_count >= 2:
        return 8
    elif tier1_count >= 1 and tier2_count >= 1:
        return 7
    elif tier1_count >= 1:
        return 6
    elif tier2_count >= 2:
        return 6
    elif tier2_count >= 1:
        return 5
    elif total >= 3:
        return 4
    elif total >= 1:
        return 3
    else:
        return 2  # No investor data = unknown, give baseline


def compute_business_fit(sub_category: str | None) -> int:
    """Compute business_fit (1-10) from sub_category alignment."""
    if not sub_category:
        return 3
    if sub_category in HIGH_FIT_SUBCATS:
        return 8
    elif sub_category in MEDIUM_FIT_SUBCATS:
        return 6
    else:
        return 4


def compute_traction(best_round: str, num_rounds: int, status: str) -> int:
    """Compute traction (1-10) from funding stage and status."""
    base = ROUND_TRACTION.get(best_round, 3)

    # Multi-round bonus
    if num_rounds >= 4:
        base += 1
    elif num_rounds >= 2:
        base += 0

    # Status adjustments
    if status == "ipo":
        base = max(base, 9)
    elif status == "acquired":
        base = max(base, 7)
    elif status == "defunct":
        base = max(base - 3, 1)

    return min(max(base, 1), 10)


def compute_overall(tech: int, market: int, team: int, fit: int, traction: int) -> int:
    """Compute overall_score (0-100) as weighted average."""
    # Weights: tech 25%, market 25%, team 15%, fit 15%, traction 20%
    weighted = (tech * 25 + market * 25 + team * 15 + fit * 15 + traction * 20) / 100
    return round(weighted * 10)  # Scale 1-10 → 10-100


def main() -> None:
    """Run full score backfill."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    client = get_client()

    # 1. Fetch all companies
    logger.info("Fetching companies...")
    companies = fetch_paginated(client, "su_companies", "id,slug,status,sub_category")
    logger.info("Companies: %d", len(companies))

    # 2. Fetch all funding rounds
    logger.info("Fetching funding rounds...")
    rounds = fetch_paginated(client, "su_funding_rounds", "company_id,raised_amount,round_type,currency")

    # Aggregate per company
    company_funding: dict[str, dict] = {}
    for r in rounds:
        cid = r["company_id"]
        if cid not in company_funding:
            company_funding[cid] = {"total": 0.0, "best_round": "seed", "rounds": 0}
        amt = float(r.get("raised_amount") or 0)
        # Normalize KRW to USD rough estimate
        currency = r.get("currency", "KRW")
        if currency == "KRW":
            amt = amt / 1400  # rough conversion
        company_funding[cid]["total"] += amt
        company_funding[cid]["rounds"] += 1
        # Track best round
        rt = r.get("round_type", "seed")
        current_best = company_funding[cid]["best_round"]
        if ROUND_TRACTION.get(rt, 0) > ROUND_TRACTION.get(current_best, 0):
            company_funding[cid]["best_round"] = rt

    # 3. Fetch investor links
    logger.info("Fetching investor links...")
    links = fetch_paginated(client, "su_round_investors", "round_id,investor_id,su_investors(slug)")

    # Map round_id → company_id
    round_to_company: dict[str, str] = {}
    for r in rounds:
        rid = r.get("id")
        if rid:
            round_to_company[rid] = r["company_id"]
    # Re-fetch rounds with id
    rounds_with_id = fetch_paginated(client, "su_funding_rounds", "id,company_id")
    for r in rounds_with_id:
        round_to_company[r["id"]] = r["company_id"]

    company_investors: dict[str, list[str]] = {}
    for link in links:
        rid = link.get("round_id")
        cid = round_to_company.get(rid)
        inv = link.get("su_investors", {})
        inv_slug = inv.get("slug", "") if inv else ""
        if cid and inv_slug:
            company_investors.setdefault(cid, []).append(inv_slug)

    # 4. Fetch existing scores
    logger.info("Fetching existing scores...")
    scores = fetch_paginated(client, "su_scores", "id,company_id,tech_strength")
    score_map: dict[str, dict] = {s["company_id"]: s for s in scores}

    # 5. Compute and update scores
    logger.info("Computing scores for %d companies...", len(companies))
    updated = 0
    skipped = 0

    for company in companies:
        cid = company["id"]
        slug = company.get("slug", "")
        sub_cat = company.get("sub_category")
        status = company.get("status", "active")

        existing = score_map.get(cid)
        if not existing:
            skipped += 1
            continue

        tech = existing.get("tech_strength") or 5
        funding = company_funding.get(cid, {"total": 0, "best_round": "seed", "rounds": 0})
        investors = company_investors.get(cid, [])

        market = compute_market_potential(funding["total"], funding["best_round"], funding["rounds"])
        team = compute_team_quality(investors)
        fit = compute_business_fit(sub_cat)
        traction = compute_traction(funding["best_round"], funding["rounds"], status)
        overall = compute_overall(tech, market, team, fit, traction)

        if args.dry_run:
            if updated < 5:
                logger.info(
                    "  %s: tech=%d market=%d team=%d fit=%d traction=%d overall=%d",
                    slug, tech, market, team, fit, traction, overall,
                )
            updated += 1
            continue

        try:
            client.table("su_scores").update({
                "market_potential": market,
                "team_quality": team,
                "business_fit": fit,
                "traction": traction,
                "overall_score": overall,
                "scored_by": "heuristic_v1",
                "rationale": "Heuristic scores from funding, investors, category signals",
            }).eq("id", existing["id"]).execute()
            updated += 1
        except Exception as e:
            logger.warning("Failed to update %s: %s", slug, e)

    logger.info("=" * 50)
    logger.info("Backfill complete")
    logger.info("  Updated: %d", updated)
    logger.info("  Skipped (no existing score): %d", skipped)


if __name__ == "__main__":
    main()
