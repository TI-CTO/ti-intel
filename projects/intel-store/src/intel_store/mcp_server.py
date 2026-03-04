"""Intel Store MCP server — unified intelligence search and collection tools."""

from __future__ import annotations

import logging
import sys

from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.WARNING, stream=sys.stderr)
logger = logging.getLogger(__name__)

mcp = FastMCP("intel-store")


def _rrf_merge(*result_lists: list[dict], limit: int = 20, k: int = 60) -> list[dict]:
    """Merge multiple ranked result lists using Reciprocal Rank Fusion.

    Args:
        *result_lists: Ranked lists of item dicts (must have 'id' key).
        limit: Maximum results to return.
        k: RRF smoothing constant (default 60).

    Returns:
        Merged list sorted by RRF score, highest first.
    """
    scores: dict[int, float] = {}
    items_by_id: dict[int, dict] = {}

    for results in result_lists:
        for rank, item in enumerate(results):
            item_id = item.get("id")
            if item_id is None:
                continue
            scores[item_id] = scores.get(item_id, 0.0) + 1.0 / (k + rank + 1)
            if item_id not in items_by_id:
                items_by_id[item_id] = item

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [items_by_id[item_id] for item_id, _ in ranked[:limit]]


def _get_repo():
    from functools import lru_cache

    @lru_cache(maxsize=1)
    def _cached():
        from intel_store.db.repository import IntelRepository

        return IntelRepository()

    return _cached()


# ── search tools ─────────────────────────────────────────────────


@mcp.tool()
def search_intel(
    query: str,
    topic: str | None = None,
    types: list[str] | None = None,
    since: str | None = None,
    limit: int = 20,
    mode: str = "keyword",
) -> list[dict]:
    """Search intel items by keyword, semantic similarity, or hybrid.

    Args:
        query: Search query text.
        topic: Filter by topic slug (e.g. 'ondevice-pqc').
        types: Filter by item types (e.g. ['news', 'paper', 'patent']).
        since: Filter items published since this date (YYYY-MM-DD).
        limit: Maximum results (default 20).
        mode: Search mode — 'keyword', 'semantic', or 'hybrid' (default 'keyword').

    Returns:
        List of matching intel items sorted by relevance or date.
    """
    repo = _get_repo()

    if mode == "keyword":
        return repo.search_fulltext(query, types=types, topic=topic, since=since, limit=limit)
    elif mode == "semantic":
        from intel_store import embeddings

        query_vec = embeddings.embed_query(query)
        return repo.search_semantic(query_vec, types=types, topic=topic, since=since, limit=limit)
    elif mode == "hybrid":
        from intel_store import embeddings

        fetch_limit = limit * 2
        kw_results = repo.search_fulltext(
            query, types=types, topic=topic, since=since, limit=fetch_limit
        )
        query_vec = embeddings.embed_query(query)
        sem_results = repo.search_semantic(
            query_vec, types=types, topic=topic, since=since, limit=fetch_limit
        )

        return _rrf_merge(kw_results, sem_results, limit=limit)
    else:
        return [{"error": f"Unknown mode: {mode}. Use 'keyword', 'semantic', or 'hybrid'."}]


@mcp.tool()
def find_similar(
    item_id: int | None = None,
    text: str | None = None,
    threshold: float = 0.8,
    limit: int = 10,
) -> list[dict]:
    """Find items similar to a given item or text.

    Args:
        item_id: Intel item ID to find similar items for.
        text: Free text to find similar items for (alternative to item_id).
        threshold: Minimum cosine similarity (default 0.8).
        limit: Maximum results (default 10).

    Returns:
        List of similar items with similarity scores.
    """
    from intel_store import embeddings

    repo = _get_repo()

    if item_id is not None:
        item = repo.get_item(item_id)
        if not item:
            return [{"error": f"Item not found: {item_id}"}]
        embedding = item.get("embedding")
        if not embedding:
            # Generate embedding on the fly
            passage = f"{item['title']}. {item.get('abstract', '')}"
            embedding = embeddings.embed_passage(passage)
        return repo.find_similar(embedding, threshold=threshold, limit=limit, exclude_id=item_id)
    elif text:
        query_vec = embeddings.embed_query(text)
        return repo.search_semantic(query_vec, threshold=threshold, limit=limit)
    else:
        return [{"error": "Provide either item_id or text"}]


@mcp.tool()
def get_weekly_diff(
    topic: str,
    week_date: str | None = None,
    types: list[str] | None = None,
) -> dict:
    """Compare this week's intel items with last week for a topic.

    Args:
        topic: Topic slug to compare.
        week_date: Reference date (YYYY-MM-DD). Defaults to today.
        types: Filter by item types.

    Returns:
        Dict with this_week, last_week items and counts.
    """
    return _get_repo().get_weekly_diff(topic, week_date=week_date, types=types)


@mcp.tool()
def get_item_detail(
    item_id: int | None = None,
    external_id: str | None = None,
) -> dict:
    """Get full details of a single intel item.

    Args:
        item_id: Internal database ID.
        external_id: External identifier (e.g. 'ss:abc123', 'uspto:US1234').

    Returns:
        Full item record or error dict.
    """
    repo = _get_repo()
    if item_id is not None:
        result = repo.get_item(item_id)
    elif external_id:
        result = repo.get_item_by_external_id(external_id)
    else:
        return {"error": "Provide either item_id or external_id"}
    return result or {"error": "Item not found"}


# ── write tools ──────────────────────────────────────────────────


@mcp.tool()
def upsert_items(
    items: list[dict],
    generate_embedding: bool = False,
) -> dict:
    """Store intel items with content_hash deduplication.

    Args:
        items: List of item dicts. Required fields: item_type, title, source_name.
               Optional: abstract, external_id, source_url, published_date, reliability,
               metadata, language.
        generate_embedding: If True, generate embeddings for items on insert.

    Returns:
        Dict with upserted count and skipped (duplicate) count.
    """
    from intel_store.models import IntelItem

    repo = _get_repo()
    models = []
    for raw in items:
        try:
            model = IntelItem(**raw)
            if generate_embedding:
                from intel_store import embeddings

                model.embedding = embeddings.embed_passage(model.embedding_input())
            models.append(model)
        except (ValueError, TypeError, KeyError) as e:
            logger.warning("Skipping invalid item: %s — %s", raw.get("title", "?")[:40], e)

    results = repo.upsert_items(models)
    return {"upserted": len(results), "submitted": len(items)}


@mcp.tool()
def link_topics(
    item_id: int,
    topic_slugs: list[str],
    assigned_by: str = "collector",
) -> dict:
    """Link an intel item to one or more topics.

    Args:
        item_id: The intel item ID.
        topic_slugs: List of topic slugs to link (e.g. ['ondevice-pqc', 'secure-ai']).
        assigned_by: How the link was created — 'collector', 'embedding', or 'manual'.

    Returns:
        Dict with linked count.
    """
    count = _get_repo().link_topics(item_id, topic_slugs, assigned_by=assigned_by)
    return {"linked": count, "item_id": item_id}


@mcp.tool()
def link_relation(
    source_id: int,
    target_id: int,
    relation_type: str,
    confidence: float = 1.0,
) -> dict:
    """Create a relation between two intel items.

    Args:
        source_id: Source item ID.
        target_id: Target item ID.
        relation_type: One of: 'cites', 'mentions', 'same_event', 'updates', 'contradicts'.
        confidence: Confidence score 0.0~1.0 (default 1.0).

    Returns:
        The created relation record.
    """
    return _get_repo().link_relation(source_id, target_id, relation_type, confidence=confidence)


# ── collection tools ─────────────────────────────────────────────


@mcp.tool()
def collect_papers(
    topic: str,
    query: str,
    since_year: int | None = None,
    limit: int = 10,
    generate_embedding: bool = True,
) -> dict:
    """Collect papers from Semantic Scholar, store in DB, and link to topic.

    Args:
        topic: Topic slug to associate papers with (e.g. 'ondevice-pqc').
        query: Search query for Semantic Scholar.
        since_year: Filter papers published on or after this year.
        limit: Maximum papers to collect (default 10).
        generate_embedding: Generate embeddings for collected papers.

    Returns:
        Dict with fetched, stored counts and paper titles.
    """
    from intel_store.collectors import semantic_scholar
    from intel_store.models import paper_from_collector

    repo = _get_repo()
    repo._require_topic_id(topic)  # validate topic exists

    raw_papers = semantic_scholar.search_papers(query, limit=limit, since_year=since_year)

    models = []
    for raw in raw_papers:
        model = paper_from_collector(raw)
        if generate_embedding:
            from intel_store import embeddings

            model.embedding = embeddings.embed_passage(model.embedding_input())
        models.append(model)

    results = repo.upsert_items(models)

    # Batch link to topic
    item_ids = [row["id"] for row in results if row.get("id")]
    if item_ids:
        repo.batch_link_topic(item_ids, topic)

    return {
        "topic": topic,
        "query": query,
        "fetched": len(raw_papers),
        "stored": len(results),
        "titles": [r.get("title", "") for r in results],
    }


@mcp.tool()
def collect_patents(
    topic: str,
    query: str,
    since_year: int | None = None,
    limit: int = 10,
    generate_embedding: bool = True,
) -> dict:
    """Collect patents from USPTO PatentsView, store in DB, and link to topic.

    Args:
        topic: Topic slug to associate patents with.
        query: Search keywords for patent title/abstract.
        since_year: Filter patents filed on or after this year.
        limit: Maximum patents to collect (default 10).
        generate_embedding: Generate embeddings for collected patents.

    Returns:
        Dict with fetched, stored counts and patent titles.
    """
    from intel_store.collectors import patents_view
    from intel_store.models import patent_from_collector

    repo = _get_repo()
    repo._require_topic_id(topic)  # validate topic exists

    raw_patents = patents_view.search_patents(query, limit=limit, since_year=since_year)

    models = []
    for raw in raw_patents:
        model = patent_from_collector(raw)
        if generate_embedding:
            from intel_store import embeddings

            model.embedding = embeddings.embed_passage(model.embedding_input())
        models.append(model)

    results = repo.upsert_items(models)

    item_ids = [row["id"] for row in results if row.get("id")]
    if item_ids:
        repo.batch_link_topic(item_ids, topic)

    return {
        "topic": topic,
        "query": query,
        "fetched": len(raw_patents),
        "stored": len(results),
        "titles": [r.get("title", "") for r in results],
    }


@mcp.tool()
def collect_news(
    topic: str,
    query: str,
    since_days: int = 7,
    limit: int = 20,
    source: str = "all",
    generate_embedding: bool = True,
) -> dict:
    """Collect news from Tavily/GDELT, store in DB, and link to topic.

    Args:
        topic: Topic slug to associate news with.
        query: Search query string.
        since_days: Look back this many days (default 7).
        limit: Max results per source (default 20).
        source: Collector to use — 'tavily', 'gdelt', or 'all' (default).
        generate_embedding: Generate embeddings for collected news.

    Returns:
        Dict with collection results per source and stored count.
    """
    from intel_store.collectors import gdelt, tavily
    from intel_store.collectors.tavily import QuotaExhaustedError
    from intel_store.models import news_from_collector

    repo = _get_repo()
    repo._require_topic_id(topic)  # validate topic exists

    results: dict = {"topic": topic, "query": query, "sources": {}}
    all_raw: list[dict] = []
    tavily_quota_hit = False

    if source in ("tavily", "all"):
        try:
            tavily_items = tavily.collect(query, since_days=since_days, limit=limit)
            results["sources"]["tavily"] = {"fetched": len(tavily_items)}
            all_raw.extend(tavily_items)
        except QuotaExhaustedError:
            tavily_quota_hit = True
            results["sources"]["tavily"] = {"fetched": 0, "error": "quota_exhausted"}
            if source == "tavily":
                source = "gdelt"
                results["fallback"] = "tavily quota exhausted, falling back to gdelt"

    if source in ("gdelt", "all") or tavily_quota_hit:
        gdelt_items = gdelt.collect(query, since_days=since_days, limit=limit)
        results["sources"]["gdelt"] = {"fetched": len(gdelt_items)}
        all_raw.extend(gdelt_items)

    # Deduplicate by URL
    seen_urls: set[str] = set()
    unique_raw: list[dict] = []
    for raw in all_raw:
        url = raw.get("url", "")
        if url and url not in seen_urls:
            seen_urls.add(url)
            unique_raw.append(raw)

    models = []
    for raw in unique_raw:
        model = news_from_collector(raw)
        if generate_embedding:
            from intel_store import embeddings

            model.embedding = embeddings.embed_passage(model.embedding_input())
        models.append(model)

    stored_rows = repo.upsert_items(models)

    item_ids = [row["id"] for row in stored_rows if row.get("id")]
    if item_ids:
        repo.batch_link_topic(item_ids, topic)

    results["total_fetched"] = len(all_raw)
    results["unique_items"] = len(unique_raw)
    results["stored"] = len(stored_rows)
    return results


# ── orchestration tools ──────────────────────────────────────────


@mcp.tool()
def collect_all(
    topic: str,
    query: str = "",
    queries: dict[str, str] | None = None,
    since_days: int = 7,
    since_year: int | None = None,
    limit: int = 10,
    generate_embedding: bool = True,
) -> dict:
    """Collect papers, patents, and news in one call, store and link to topic.

    Args:
        topic: Topic slug to associate all items with.
        query: Default search query (used when queries dict does not specify a source).
        queries: Per-source query overrides, e.g. {"papers": "...", "news": "...", "patents": "..."}.
        since_days: Look-back days for news (default 7).
        since_year: Filter papers/patents published on or after this year.
        limit: Max results per source (default 10).
        generate_embedding: Generate embeddings for collected items.

    Returns:
        Dict with per-source results and overall summary.
    """
    queries = queries or {}
    results: dict = {"topic": topic, "sources": {}, "errors": []}

    source_calls = [
        ("papers", lambda q: collect_papers(
            topic=topic, query=q, since_year=since_year,
            limit=limit, generate_embedding=generate_embedding,
        )),
        ("patents", lambda q: collect_patents(
            topic=topic, query=q, since_year=since_year,
            limit=limit, generate_embedding=generate_embedding,
        )),
        ("news", lambda q: collect_news(
            topic=topic, query=q, since_days=since_days,
            limit=limit, source="all", generate_embedding=generate_embedding,
        )),
    ]

    total_stored = 0
    for source_name, call_fn in source_calls:
        source_query = queries.get(source_name, query)
        if not source_query:
            results["sources"][source_name] = {"skipped": "no query provided"}
            continue
        try:
            result = call_fn(source_query)
            results["sources"][source_name] = result
            total_stored += result.get("stored", 0)
        except Exception as e:
            logger.error("collect_all: %s failed — %s", source_name, e)
            results["sources"][source_name] = {"error": str(e)}
            results["errors"].append(source_name)

    results["total_stored"] = total_stored
    return results


# ── stats tool ───────────────────────────────────────────────────


@mcp.tool()
def get_intel_stats(
    topic: str | None = None,
    type: str | None = None,
    period: int = 30,
) -> dict:
    """Get aggregate statistics for intel items.

    Args:
        topic: Filter by topic slug.
        type: Filter by item type (news/paper/patent/statement/report/standard).
        period: Look back period in days (default 30).

    Returns:
        Dict with total_count, recent_count, and period info.
    """
    return _get_repo().get_stats(topic=topic, item_type=type, period_days=period)


if __name__ == "__main__":
    mcp.run()
