"""Polymarket Gamma API collector for prediction market signals."""

from __future__ import annotations

import json
import logging
import time

import httpx

logger = logging.getLogger(__name__)

_BASE_URL = "https://gamma-api.polymarket.com"
_REQUEST_DELAY = 3.6  # 1,000 req/hour
_VOLUME_THRESHOLD = 100_000  # volume >= $100k → reliability B


def collect(
    query: str,
    *,
    limit: int = 20,
) -> list[dict]:
    """Search Polymarket active markets and return normalised community signal dicts.

    Args:
        query: Search query string.
        limit: Maximum number of results.

    Returns:
        List of normalised community item dicts.
    """
    limit = max(1, min(limit, 100))

    params = {
        "_q": query,
        "active": "true",
        "closed": "false",
        "limit": limit,
    }

    try:
        with httpx.Client(timeout=30.0) as client:
            resp = client.get(f"{_BASE_URL}/markets", params=params)
            resp.raise_for_status()
            markets = resp.json()
    except httpx.HTTPStatusError as e:
        logger.error("Polymarket API error: %s %s", e.response.status_code, e.response.text[:200])
        return []
    except httpx.RequestError as e:
        logger.error("Polymarket request failed: %s", e)
        return []

    if not isinstance(markets, list):
        logger.warning("Polymarket returned non-list response: %s", type(markets))
        return []

    items = [_normalise(m) for m in markets]

    time.sleep(_REQUEST_DELAY)
    return [i for i in items if i is not None]


def _normalise(market: dict) -> dict | None:
    """Convert a Polymarket market to community item schema."""
    question = (market.get("question") or "").strip()
    slug = market.get("slug") or market.get("condition_id", "")
    if not question or not slug:
        return None

    volume = float(market.get("volume", 0) or 0)
    liquidity = float(market.get("liquidity", 0) or 0)

    outcome_prices = _parse_outcome_prices(market.get("outcomePrices"))
    price_summary = _format_prices(outcome_prices)

    end_date = market.get("endDate", "")
    published_date = end_date[:10] if end_date and len(end_date) >= 10 else None

    summary = f"Probability: {price_summary}. Volume: ${volume:,.0f}"
    if liquidity > 0:
        summary += f". Liquidity: ${liquidity:,.0f}"

    return {
        "external_id": f"poly:{slug}",
        "title": question,
        "url": f"https://polymarket.com/event/{slug}",
        "source": "polymarket",
        "platform": "polymarket",
        "published_date": published_date,
        "summary": summary,
        "engagement": int(volume),
        "comments": 0,
        "outcome_prices": outcome_prices,
        "liquidity": liquidity,
        "collector": "polymarket",
        "reliability_tag": "B" if volume >= _VOLUME_THRESHOLD else "C",
    }


def _parse_outcome_prices(raw: str | list | None) -> dict | None:
    """Parse outcome prices from string or list format."""
    if raw is None:
        return None
    if isinstance(raw, str):
        try:
            parsed = json.loads(raw)
        except (json.JSONDecodeError, TypeError):
            return None
    else:
        parsed = raw

    if isinstance(parsed, list) and len(parsed) >= 2:
        return {"Yes": float(parsed[0]), "No": float(parsed[1])}
    if isinstance(parsed, dict):
        return parsed
    return None


def _format_prices(prices: dict | None) -> str:
    """Format outcome prices as human-readable string."""
    if not prices:
        return "N/A"
    parts = [f"{k} {v:.0%}" for k, v in prices.items()]
    return ", ".join(parts)
