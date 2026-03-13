"""Export startup-db companies to Obsidian-compatible markdown notes.

Generates one .md file per company with YAML frontmatter and wikilinks,
enabling Obsidian graph view to visualize company relationships.

Output structure:
    /Users/ctoti/Obsidian/Obsidian_Work/50-Startups/
      _index.md               ← Dataview query table
      companies/
        {slug}.md             ← One note per company (807 files)

Usage:
    cd projects/startup-db
    uv run python scripts/export_to_obsidian.py
    uv run python scripts/export_to_obsidian.py --dry-run
"""

from __future__ import annotations

import argparse
import logging
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from supabase import Client, create_client  # noqa: E402

from startup_db.config import settings  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

OBSIDIAN_VAULT = Path("/Users/ctoti/Obsidian/Obsidian_Work")
STARTUPS_DIR = OBSIDIAN_VAULT / "50-Startups"
COMPANIES_DIR = STARTUPS_DIR / "companies"

PAGE_SIZE = 1000
TODAY = date.today().isoformat()


# ── Supabase helpers ──────────────────────────────────────────


def get_client() -> Client:
    """Create and return a Supabase client.

    Returns:
        Authenticated Supabase client instance.
    """
    return create_client(settings.supabase_url, settings.supabase_key)


def fetch_all_companies(client: Client) -> list[dict]:
    """Fetch all companies from su_companies with pagination.

    Args:
        client: Supabase client.

    Returns:
        List of all company row dicts.
    """
    all_rows: list[dict] = []
    offset = 0

    while True:
        result = (
            client.table("su_companies")
            .select("*")
            .order("name")
            .range(offset, offset + PAGE_SIZE - 1)
            .execute()
        )
        batch = result.data or []
        all_rows.extend(batch)
        logger.debug("Fetched companies %d–%d", offset + 1, offset + len(batch))

        if len(batch) < PAGE_SIZE:
            break
        offset += PAGE_SIZE

    return all_rows


def fetch_funding_rounds_bulk(client: Client) -> dict[str, list[dict]]:
    """Fetch all funding rounds grouped by company_id.

    Args:
        client: Supabase client.

    Returns:
        Mapping of company_id → list of funding round rows.
    """
    all_rows: list[dict] = []
    offset = 0

    while True:
        result = (
            client.table("su_funding_rounds")
            .select("*")
            .order("announced_date", desc=True)
            .range(offset, offset + PAGE_SIZE - 1)
            .execute()
        )
        batch = result.data or []
        all_rows.extend(batch)
        if len(batch) < PAGE_SIZE:
            break
        offset += PAGE_SIZE

    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in all_rows:
        grouped[row["company_id"]].append(row)
    return grouped


def fetch_round_investors_bulk(client: Client) -> dict[str, list[dict]]:
    """Fetch all round-investor links grouped by round_id.

    Args:
        client: Supabase client.

    Returns:
        Mapping of round_id → list of round_investor rows.
    """
    all_rows: list[dict] = []
    offset = 0

    while True:
        result = (
            client.table("su_round_investors")
            .select("*")
            .range(offset, offset + PAGE_SIZE - 1)
            .execute()
        )
        batch = result.data or []
        all_rows.extend(batch)
        if len(batch) < PAGE_SIZE:
            break
        offset += PAGE_SIZE

    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in all_rows:
        grouped[row["round_id"]].append(row)
    return grouped


def fetch_investors_bulk(client: Client) -> dict[str, dict]:
    """Fetch all investors indexed by id.

    Args:
        client: Supabase client.

    Returns:
        Mapping of investor_id → investor row dict.
    """
    all_rows: list[dict] = []
    offset = 0

    while True:
        result = (
            client.table("su_investors").select("*").range(offset, offset + PAGE_SIZE - 1).execute()
        )
        batch = result.data or []
        all_rows.extend(batch)
        if len(batch) < PAGE_SIZE:
            break
        offset += PAGE_SIZE

    return {row["id"]: row for row in all_rows}


def fetch_company_people_bulk(client: Client) -> dict[str, list[dict]]:
    """Fetch all company-people links grouped by company_id.

    Args:
        client: Supabase client.

    Returns:
        Mapping of company_id → list of company_people rows.
    """
    all_rows: list[dict] = []
    offset = 0

    while True:
        result = (
            client.table("su_company_people")
            .select("*")
            .range(offset, offset + PAGE_SIZE - 1)
            .execute()
        )
        batch = result.data or []
        all_rows.extend(batch)
        if len(batch) < PAGE_SIZE:
            break
        offset += PAGE_SIZE

    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in all_rows:
        grouped[row["company_id"]].append(row)
    return grouped


def fetch_people_bulk(client: Client) -> dict[str, dict]:
    """Fetch all people indexed by id.

    Args:
        client: Supabase client.

    Returns:
        Mapping of person_id → person row dict.
    """
    all_rows: list[dict] = []
    offset = 0

    while True:
        result = (
            client.table("su_people").select("*").range(offset, offset + PAGE_SIZE - 1).execute()
        )
        batch = result.data or []
        all_rows.extend(batch)
        if len(batch) < PAGE_SIZE:
            break
        offset += PAGE_SIZE

    return {row["id"]: row for row in all_rows}


def fetch_company_relations_bulk(client: Client) -> dict[str, list[dict]]:
    """Fetch all company relations grouped by company_id.

    Args:
        client: Supabase client.

    Returns:
        Mapping of company_id → list of relation rows.
    """
    all_rows: list[dict] = []
    offset = 0

    while True:
        result = (
            client.table("su_company_relations")
            .select("*")
            .range(offset, offset + PAGE_SIZE - 1)
            .execute()
        )
        batch = result.data or []
        all_rows.extend(batch)
        if len(batch) < PAGE_SIZE:
            break
        offset += PAGE_SIZE

    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in all_rows:
        grouped[row["company_id"]].append(row)
    return grouped


# ── Formatting helpers ────────────────────────────────────────


def format_amount(amount: float | None, currency: str = "KRW") -> str | None:
    """Format a funding amount with appropriate scale suffix.

    Args:
        amount: Numeric amount value.
        currency: ISO currency code (KRW, USD, etc.).

    Returns:
        Formatted string like "$5.5M", "₩3B", or None if amount is None.
    """
    if amount is None:
        return None

    symbol = "₩" if currency == "KRW" else "$"

    if amount >= 1_000_000_000:
        return f"{symbol}{amount / 1_000_000_000:.1f}B"
    if amount >= 1_000_000:
        return f"{symbol}{amount / 1_000_000:.1f}M"
    if amount >= 1_000:
        return f"{symbol}{amount / 1_000:.1f}K"
    return f"{symbol}{amount:.0f}"


def format_round_type(round_type: str) -> str:
    """Format a round_type slug into a display label.

    Args:
        round_type: Raw round type string (e.g. "series_a").

    Returns:
        Human-readable label (e.g. "Series A").
    """
    return round_type.replace("_", " ").title()


def extract_year(date_str: str | None) -> int | None:
    """Extract year from a date string.

    Args:
        date_str: ISO date string like "2024-03-01".

    Returns:
        Year as integer, or None if not parseable.
    """
    if not date_str:
        return None
    try:
        return int(str(date_str)[:4])
    except (ValueError, TypeError):
        return None


def yaml_str(value: Any) -> str:
    """Safely quote a string value for YAML frontmatter.

    Args:
        value: The value to render.

    Returns:
        Quoted YAML string, or empty string for None/empty.
    """
    if value is None:
        return ""
    text = str(value).replace('"', '\\"')
    return f'"{text}"'


def yaml_tags(tags: list[str]) -> str:
    """Render a list of tags as a YAML inline list.

    Args:
        tags: List of tag strings.

    Returns:
        YAML inline array string like "[tag1, tag2]".
    """
    if not tags:
        return "[]"
    items = ", ".join(tags)
    return f"[{items}]"


def investor_wikilink(investor_name: str) -> str:
    """Convert an investor name to a wikilink slug reference.

    Args:
        investor_name: Display name of the investor.

    Returns:
        Wikilink string like "[[flybridge-capital-partners|Flybridge Capital Partners]]".
    """
    import re
    import unicodedata

    text = unicodedata.normalize("NFKD", investor_name)
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    slug = re.sub(r"-+", "-", text).strip("-")
    return f"[[{slug}|{investor_name}]]"


def company_wikilink(slug: str, name: str | None = None) -> str:
    """Create a company wikilink using slug as the note filename.

    Args:
        slug: Company slug matching the note filename.
        name: Optional display name. If omitted, slug is displayed.

    Returns:
        Wikilink string like "[[bland-ai|Bland AI]]" or "[[bland-ai]]".
    """
    if name and name != slug:
        return f"[[{slug}|{name}]]"
    return f"[[{slug}]]"


# ── Competitor detection ──────────────────────────────────────


def build_sub_category_index(companies: list[dict]) -> dict[tuple[str, str], list[dict]]:
    """Index companies by (sub_category, country) for competitor lookup.

    Args:
        companies: Full list of company dicts from the DB.

    Returns:
        Mapping of (sub_category, country) → list of company rows.
    """
    index: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for c in companies:
        sub = c.get("sub_category")
        country = c.get("country")
        if sub and country:
            index[(sub, country)].append(c)
    return index


# ── Note generation ───────────────────────────────────────────


def build_frontmatter(
    company: dict,
    funding_rounds: list[dict],
) -> str:
    """Build YAML frontmatter block for a company note.

    Args:
        company: Company row dict from su_companies.
        funding_rounds: Funding rounds for this company.

    Returns:
        Multi-line YAML frontmatter string (including --- delimiters).
    """
    name = company.get("name", "")
    status = company.get("status", "active")
    main_category = company.get("main_category", "")
    sub_category = company.get("sub_category", "")
    country = company.get("country", "")
    city = company.get("city", "")
    website = company.get("website", "")
    tags: list[str] = company.get("tags") or []

    # Compute funding_total and latest_round from funding_rounds
    funding_total: float | None = None
    currency = "KRW"
    latest_round: str | None = None

    if funding_rounds:
        totals_krw: float = 0.0
        totals_usd: float = 0.0
        for fr in funding_rounds:
            amt = fr.get("raised_amount")
            cur = fr.get("currency", "KRW")
            if amt:
                if cur == "KRW":
                    totals_krw += float(amt)
                else:
                    totals_usd += float(amt)
        # Prefer USD if any USD rounds exist
        if totals_usd > 0:
            funding_total = totals_usd
            currency = "USD"
        elif totals_krw > 0:
            funding_total = totals_krw
            currency = "KRW"

        # Latest round = most recent by announced_date
        sorted_rounds = sorted(
            funding_rounds,
            key=lambda r: r.get("announced_date") or "0000-00-00",
            reverse=True,
        )
        latest_round = sorted_rounds[0].get("round_type") if sorted_rounds else None

    # Extract founded year from founded_date
    founded = extract_year(company.get("founded_date"))

    lines = ["---"]
    lines.append(f"name: {yaml_str(name)}")
    lines.append(f"status: {status}")
    if main_category:
        lines.append(f"category: {yaml_str(main_category)}")
    if sub_category:
        lines.append(f"sub_category: {yaml_str(sub_category)}")
    if country:
        lines.append(f"country: {yaml_str(country)}")
    if city:
        lines.append(f"city: {yaml_str(city)}")
    if website:
        lines.append(f"website: {website}")
    lines.append(f"tags: {yaml_tags(tags)}")
    if funding_total is not None:
        formatted = format_amount(funding_total, currency)
        lines.append(f"funding_total: {formatted}")
    if latest_round:
        lines.append(f"latest_round: {format_round_type(latest_round).lower()}")
    if founded:
        lines.append(f"founded: {founded}")
    lines.append(f"updated: {TODAY}")
    lines.append("---")

    return "\n".join(lines)


def build_funding_section(
    funding_rounds: list[dict],
    round_investors_map: dict[str, list[dict]],
    investors_map: dict[str, dict],
) -> str:
    """Build the funding section markdown.

    Args:
        funding_rounds: Funding rounds for this company.
        round_investors_map: Mapping of round_id → list of investor link rows.
        investors_map: Global investor id → investor row mapping.

    Returns:
        Markdown string for the funding section, or empty string if no rounds.
    """
    if not funding_rounds:
        return ""

    sorted_rounds = sorted(
        funding_rounds,
        key=lambda r: r.get("announced_date") or "0000-00-00",
        reverse=True,
    )

    lines = ["## 펀딩"]
    for fr in sorted_rounds:
        round_type = format_round_type(fr.get("round_type") or "undisclosed")
        amount = format_amount(fr.get("raised_amount"), fr.get("currency", "KRW"))
        date_str = fr.get("announced_date") or ""
        year = extract_year(date_str)

        # Investor wikilinks
        round_id = fr.get("id", "")
        inv_links = round_investors_map.get(round_id, [])
        investor_parts: list[str] = []
        for link in inv_links:
            inv_id = link.get("investor_id")
            if inv_id and inv_id in investors_map:
                inv_name = investors_map[inv_id].get("name", "")
                if inv_name:
                    investor_parts.append(investor_wikilink(inv_name))

        # Build line
        parts: list[str] = [round_type]
        if amount:
            parts.append(amount)
        if year:
            parts.append(f"({year})")
        line = "- " + " ".join(parts)
        if investor_parts:
            line += " — " + ", ".join(investor_parts)

        lines.append(line)

    return "\n".join(lines)


def build_people_section(
    company_id: str,
    company_people_map: dict[str, list[dict]],
    people_map: dict[str, dict],
) -> str:
    """Build the people section markdown.

    Args:
        company_id: UUID of the company.
        company_people_map: Mapping of company_id → list of company_people rows.
        people_map: Global person_id → person row mapping.

    Returns:
        Markdown string for the people section, or empty string if no people.
    """
    links = company_people_map.get(company_id, [])
    if not links:
        return ""

    lines = ["## 인물"]
    for link in links:
        person_id = link.get("person_id")
        if not person_id or person_id not in people_map:
            continue
        person = people_map[person_id]
        name = person.get("name", "")
        title = person.get("title") or link.get("role") or ""
        if not name:
            continue
        if title:
            lines.append(f"- {name} ({title})")
        else:
            lines.append(f"- {name}")

    if len(lines) == 1:
        return ""
    return "\n".join(lines)


def build_relations_section(
    company: dict,
    company_relations_map: dict[str, list[dict]],
    slug_to_company: dict[str, dict],
    sub_category_index: dict[tuple[str, str], list[dict]],
) -> str:
    """Build the relations section with wikilinks.

    Includes explicit relations from su_company_relations plus auto-detected
    competitors from same sub_category + country.

    Args:
        company: Company row dict.
        company_relations_map: Mapping of company_id → list of relation rows.
        slug_to_company: Mapping of slug → company row.
        sub_category_index: Mapping of (sub_category, country) → companies.

    Returns:
        Markdown string for the relations section, or empty string if none.
    """
    company_id = company.get("id", "")
    current_slug = company.get("slug", "")
    sub = company.get("sub_category")
    country = company.get("country")

    # Explicit relations grouped by type
    explicit_relations = company_relations_map.get(company_id, [])
    by_type: dict[str, list[str]] = defaultdict(list)

    for rel in explicit_relations:
        related_id = rel.get("related_company_id")
        rel_type = rel.get("relation_type") or "유사"
        if not related_id:
            continue

        # Find related company slug
        related_slug: str | None = None
        related_name: str | None = None
        for s, c in slug_to_company.items():
            if c.get("id") == related_id:
                related_slug = s
                related_name = c.get("name")
                break

        if related_slug:
            wl = company_wikilink(related_slug, related_name)
            label = _relation_label(rel_type)
            by_type[label].append(wl)

    # Auto-detected competitors (same sub_category + country, excluding self)
    auto_competitors: list[str] = []
    if sub and country:
        peers = sub_category_index.get((sub, country), [])
        for peer in peers:
            peer_slug = peer.get("slug", "")
            peer_name = peer.get("name")
            if peer_slug and peer_slug != current_slug:
                wl = company_wikilink(peer_slug, peer_name)
                # Only add if not already in explicit competitor list
                if wl not in by_type.get("경쟁", []):
                    auto_competitors.append(wl)

    if not by_type and not auto_competitors:
        return ""

    lines = ["## 관계"]
    for label, wikilinks in by_type.items():
        lines.append(f"- {label}: " + ", ".join(wikilinks))

    if auto_competitors:
        existing_competitors = by_type.get("경쟁", [])
        all_competitors = existing_competitors + auto_competitors
        # Replace if already listed, otherwise add
        if "경쟁" not in by_type:
            lines.append("- 경쟁: " + ", ".join(all_competitors))
        else:
            # Merge: rebuild the line
            for i, line in enumerate(lines):
                if line.startswith("- 경쟁:"):
                    lines[i] = "- 경쟁: " + ", ".join(all_competitors)
                    break

    return "\n".join(lines)


def _relation_label(relation_type: str) -> str:
    """Map relation_type enum value to a Korean display label.

    Args:
        relation_type: Raw relation type string.

    Returns:
        Korean label string.
    """
    mapping = {
        "competitor": "경쟁",
        "partner": "파트너",
        "customer": "고객",
        "supplier": "공급",
        "spin_off": "스핀오프",
    }
    return mapping.get(relation_type.lower(), relation_type)


def build_company_note(
    company: dict,
    funding_rounds: list[dict],
    round_investors_map: dict[str, list[dict]],
    investors_map: dict[str, dict],
    company_people_map: dict[str, list[dict]],
    people_map: dict[str, dict],
    company_relations_map: dict[str, list[dict]],
    slug_to_company: dict[str, dict],
    sub_category_index: dict[tuple[str, str], list[dict]],
) -> str:
    """Assemble the full Obsidian markdown note for a company.

    Args:
        company: Company row dict from su_companies.
        funding_rounds: This company's funding rounds.
        round_investors_map: Global round_id → investor links mapping.
        investors_map: Global investor_id → investor row mapping.
        company_people_map: Global company_id → people links mapping.
        people_map: Global person_id → person row mapping.
        company_relations_map: Global company_id → relations mapping.
        slug_to_company: Global slug → company row mapping.
        sub_category_index: (sub_category, country) → companies mapping.

    Returns:
        Full markdown note content as a string.
    """
    name = company.get("name", "")
    description = company.get("description") or ""
    technology = company.get("technology") or ""

    # Frontmatter
    frontmatter = build_frontmatter(company, funding_rounds)

    # Body sections
    sections: list[str] = [frontmatter, "", f"# {name}", ""]

    if description:
        sections.append(f"> {description}")
        sections.append("")

    if technology:
        sections.append("## 기술")
        sections.append(technology)
        sections.append("")

    funding_section = build_funding_section(funding_rounds, round_investors_map, investors_map)
    if funding_section:
        sections.append(funding_section)
        sections.append("")

    people_section = build_people_section(company.get("id", ""), company_people_map, people_map)
    if people_section:
        sections.append(people_section)
        sections.append("")

    relations_section = build_relations_section(
        company, company_relations_map, slug_to_company, sub_category_index
    )
    if relations_section:
        sections.append(relations_section)
        sections.append("")

    return "\n".join(sections).rstrip() + "\n"


# ── Index note ────────────────────────────────────────────────


def build_index_note(companies: list[dict]) -> str:
    """Build the _index.md Dataview query table.

    Args:
        companies: Full list of company dicts.

    Returns:
        Markdown content for the index note.
    """
    total = len(companies)
    lines = [
        "---",
        'title: "Startup Database Index"',
        f"updated: {TODAY}",
        f"total: {total}",
        "---",
        "",
        "# Startup Database",
        "",
        f"Total: **{total}** companies",
        "",
        "## All Companies",
        "",
        "```dataview",
        "TABLE name, status, category, sub_category, country, funding_total, latest_round",
        'FROM "50-Startups/companies"',
        "SORT name ASC",
        "```",
        "",
        "## By Category",
        "",
        "```dataview",
        "TABLE rows.file.link AS Companies, length(rows) AS Count",
        'FROM "50-Startups/companies"',
        "GROUP BY category",
        "SORT length(rows) DESC",
        "```",
        "",
        "## Recent Funding",
        "",
        "```dataview",
        "TABLE name, funding_total, latest_round, country",
        'FROM "50-Startups/companies"',
        'WHERE funding_total != null AND funding_total != ""',
        "SORT funding_total DESC",
        "LIMIT 50",
        "```",
        "",
    ]
    return "\n".join(lines)


# ── Export orchestration ──────────────────────────────────────


def export(dry_run: bool = False) -> None:
    """Run the full export pipeline.

    Fetches all data from Supabase and writes Obsidian markdown notes.

    Args:
        dry_run: If True, skip writing files and only log what would happen.
    """
    logger.info("Connecting to Supabase...")
    client = get_client()

    # ── Fetch all data ──
    logger.info("Fetching companies...")
    companies = fetch_all_companies(client)
    logger.info("Fetched %d companies", len(companies))

    logger.info("Fetching funding rounds...")
    funding_by_company = fetch_funding_rounds_bulk(client)

    logger.info("Fetching round investors...")
    round_investors_map = fetch_round_investors_bulk(client)

    logger.info("Fetching investors...")
    investors_map = fetch_investors_bulk(client)

    logger.info("Fetching people...")
    company_people_map = fetch_company_people_bulk(client)
    people_map = fetch_people_bulk(client)

    logger.info("Fetching company relations...")
    company_relations_map = fetch_company_relations_bulk(client)

    # ── Build lookup indexes ──
    slug_to_company: dict[str, dict] = {c["slug"]: c for c in companies if c.get("slug")}
    sub_category_index = build_sub_category_index(companies)

    # ── Create output directories ──
    if not dry_run:
        COMPANIES_DIR.mkdir(parents=True, exist_ok=True)
        logger.info("Output directory: %s", COMPANIES_DIR)
    else:
        logger.info("[DRY RUN] Would create: %s", COMPANIES_DIR)

    # ── Write index ──
    index_content = build_index_note(companies)
    index_path = STARTUPS_DIR / "_index.md"
    if dry_run:
        logger.info("[DRY RUN] Would write index: %s", index_path)
    else:
        index_path.write_text(index_content, encoding="utf-8")
        logger.info("Wrote index: %s", index_path)

    # ── Write company notes ──
    exported = 0
    skipped = 0
    total_wikilinks = 0

    for company in companies:
        slug = company.get("slug", "").strip()
        name = company.get("name", "").strip()

        if not slug:
            logger.warning("Skipping company with no slug: %r", name)
            skipped += 1
            continue

        company_id = company.get("id", "")
        funding_rounds = funding_by_company.get(company_id, [])

        try:
            note_content = build_company_note(
                company=company,
                funding_rounds=funding_rounds,
                round_investors_map=round_investors_map,
                investors_map=investors_map,
                company_people_map=company_people_map,
                people_map=people_map,
                company_relations_map=company_relations_map,
                slug_to_company=slug_to_company,
                sub_category_index=sub_category_index,
            )
        except Exception:
            logger.exception("Failed to build note for %s (%s)", name, slug)
            skipped += 1
            continue

        # Count wikilinks generated in this note
        wikilink_count = note_content.count("[[")
        total_wikilinks += wikilink_count

        note_path = COMPANIES_DIR / f"{slug}.md"
        if dry_run:
            logger.debug("[DRY RUN] Would write %s (%d wikilinks)", note_path.name, wikilink_count)
        else:
            note_path.write_text(note_content, encoding="utf-8")

        exported += 1

    # ── Summary ──
    logger.info("=" * 50)
    if dry_run:
        logger.info("[DRY RUN] Export preview complete")
    else:
        logger.info("Export complete")
    logger.info("  Companies exported : %d", exported)
    logger.info("  Companies skipped  : %d", skipped)
    logger.info("  Wikilinks generated: %d", total_wikilinks)
    if not dry_run:
        logger.info("  Output directory   : %s", COMPANIES_DIR)


# ── Entry point ───────────────────────────────────────────────


def main() -> None:
    """Parse CLI arguments and run the export."""
    parser = argparse.ArgumentParser(
        description="Export startup-db companies to Obsidian markdown notes."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview export without writing any files.",
    )
    args = parser.parse_args()

    export(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
