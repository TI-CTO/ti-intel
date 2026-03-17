"""Companies — searchable list with filters."""

from __future__ import annotations

import html as _html

import streamlit as st

from startup_db.dashboard.components import is_dark_mode
from startup_db.dashboard.data import (
    cached_company_stats,
    cached_company_topics_bulk,
    cached_search_companies,
    cached_search_companies_by_topic,
)
from startup_db.dashboard.theme import (
    DARK,
    LIGHT,
    PRIMARY,
    PRIMARY_DARK,
    _glass_css,
    render_company_cards,
)
from startup_db.taxonomy import (
    L1_COLORS,
    L1_LABELS,
    get_l1_for_l3,
    get_l2_slugs_for_l1,
    get_l3_slugs_for_l1,
    get_l3_slugs_for_l2,
)


def _fmt_money_short(amount: float | int | str | None) -> str:
    """Format money amount compactly."""
    if amount is None:
        return ""
    try:
        amount = float(amount)
    except (ValueError, TypeError):
        return ""
    if amount <= 0:
        return ""
    if amount >= 1_000_000_000:
        return f"${amount / 1_000_000_000:.1f}B"
    if amount >= 1_000_000:
        return f"${amount / 1_000_000:.1f}M"
    if amount >= 1_000:
        return f"${amount / 1_000:.0f}K"
    return f"${amount:,.0f}"


def _render_list_table(
    companies: list[dict],
    topics_map: dict[str, list[str]],
    *,
    dark: bool = False,
    detail_path: str = "/company_detail",
) -> str:
    """Render company list as an HTML table with clickable names."""
    c = DARK if dark else LIGHT

    header_bg = "rgba(255,255,255,0.08)" if dark else "rgba(255,255,255,0.5)"
    row_bg = "rgba(255,255,255,0.03)" if dark else "rgba(255,255,255,0.35)"
    row_alt = "rgba(255,255,255,0.07)" if dark else "rgba(255,255,255,0.55)"
    hover_bg = "rgba(197,0,99,0.12)" if dark else "rgba(197,0,99,0.08)"
    border = c["glass_border"]
    text = c["text"]
    text2 = c["text_secondary"]

    style = (
        "<style>"
        f".cl-table{{width:100%;border-collapse:collapse;border-radius:16px;overflow:hidden;"
        f"border:1px solid {border};font-size:0.85rem;font-family:Inter,-apple-system,sans-serif;"
        f"backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);}}"
        f".cl-table th{{background:{header_bg};color:{text2};font-weight:600;"
        f"text-transform:uppercase;font-size:0.72rem;letter-spacing:0.04em;"
        f"padding:12px 16px;text-align:left;border-bottom:1px solid {border};}}"
        f".cl-table td{{padding:0;border-bottom:1px solid {border};}}"
        f".cl-table tr:nth-child(even) td{{background:{row_alt};}}"
        f".cl-table tr:nth-child(odd) td{{background:{row_bg};}}"
        f".cl-table tr:hover td{{background:{hover_bg};}}"
        f".cl-table td a{{display:block;padding:10px 16px;color:{text};text-decoration:none;}}"
        f".cl-table td:first-child a{{font-weight:500;}}"
        f".cl-badge{{font-size:0.68rem;padding:2px 8px;border-radius:8px;font-weight:500;}}"
        "</style>"
    )

    def _safe(val: object) -> str:
        s = str(val) if val else ""
        if s in ("None", "nan"):
            return ""
        # Remove newlines that break HTML table structure
        s = s.replace("\n", " ").replace("\r", "")
        return _html.escape(s)

    rows = []
    for comp in companies:
        name = _safe(comp.get("name", ""))
        slug = _safe(comp.get("slug", ""))
        one_liner = _safe(comp.get("one_liner", ""))
        country = _safe(comp.get("country", ""))
        stage = _safe(comp.get("growth_stage", ""))
        raised = _fmt_money_short(comp.get("total_raised"))
        last_fund = _safe(comp.get("last_funding_date", ""))
        if last_fund:
            last_fund = last_fund[:10]  # YYYY-MM-DD only

        href = f"{detail_path}?slug={slug}"

        # L1 domain badge
        cid = comp.get("id", "")
        comp_topics = topics_map.get(cid, [])
        l1_set: set[str] = set()
        for t in comp_topics:
            l1 = get_l1_for_l3(t)
            if l1:
                l1_set.add(l1)
        l1_html = ""
        for l1_slug in sorted(l1_set):
            color = L1_COLORS.get(l1_slug, "#6B7280")
            label = L1_LABELS.get(l1_slug, l1_slug)
            l1_html += (
                f'<span class="cl-badge" style="color:{color};'
                f'background:{color}20;">{_html.escape(label)}</span> '
            )

        # Truncate one_liner
        if len(one_liner) > 120:
            one_liner = one_liner[:117] + "..."

        rows.append(
            f'<tr>'
            f'<td><a href="{href}" target="_self">{name}</a></td>'
            f'<td><a href="{href}" target="_self">{l1_html}</a></td>'
            f'<td><a href="{href}" target="_self">{one_liner}</a></td>'
            f'<td><a href="{href}" target="_self">{country}</a></td>'
            f'<td><a href="{href}" target="_self">{stage}</a></td>'
            f'<td><a href="{href}" target="_self">{raised}</a></td>'
            f'<td><a href="{href}" target="_self">{last_fund}</a></td>'
            f'</tr>'
        )

    header = (
        "<tr>"
        '<th style="width:11%">Name</th>'
        '<th style="width:9%">Domain</th>'
        '<th style="width:34%">기업 개요</th>'
        '<th style="width:7%">Country</th>'
        '<th style="width:7%">Stage</th>'
        '<th style="width:8%">Raised</th>'
        '<th style="width:9%">Last Funded</th>'
        "</tr>"
    )
    body = "".join(rows)
    return (
        f'{style}<table class="cl-table">'
        f"<thead>{header}</thead><tbody>{body}</tbody></table>"
    )

dark = is_dark_mode()
_c = DARK if dark else LIGHT
glass = _glass_css(_c)
st.title("Companies")

# ── Sidebar filters ──────────────────────────────────────────
stats = cached_company_stats()
topics_map = cached_company_topics_bulk()

with st.sidebar:
    st.header("Filters")
    query = st.text_input("Search", placeholder="Name, tech, description...")

    categories = ["All"] + list(stats["by_category"].keys())
    selected_cat = st.selectbox("Category", categories)

    countries = ["All"] + list(stats["by_country"].keys())
    selected_country = st.selectbox("Country", countries)

    statuses = ["All"] + list(stats["by_status"].keys())
    selected_status = st.selectbox("Status", statuses)

    # ── Tech Domain filters ──
    st.markdown("---")
    st.subheader("Tech Domain")

    l1_options = ["All"] + list(L1_LABELS.values())
    selected_l1_label = st.selectbox("L1 Domain", l1_options)

    # Reverse lookup label → slug
    _label_to_l1 = {v: k for k, v in L1_LABELS.items()}
    selected_l1 = _label_to_l1.get(selected_l1_label)

    selected_l2 = None
    selected_l3 = None

    if selected_l1:
        l2_slugs = get_l2_slugs_for_l1(selected_l1)
        l2_options = ["All"] + l2_slugs
        selected_l2_raw = st.selectbox("L2 Capability", l2_options)
        if selected_l2_raw != "All":
            selected_l2 = selected_l2_raw

    if selected_l2:
        l3_slugs = get_l3_slugs_for_l2(selected_l2)
        l3_options = ["All"] + l3_slugs
        selected_l3_raw = st.selectbox("L3 Technology", l3_options)
        if selected_l3_raw != "All":
            selected_l3 = selected_l3_raw

    page_size = st.selectbox("Per page", [20, 40, 60, 80], index=0)

# ── State ────────────────────────────────────────────────────
if "companies_page" not in st.session_state:
    st.session_state.companies_page = 0
if "companies_view" not in st.session_state:
    st.session_state.companies_view = "list"

is_list = st.session_state.companies_view == "list"

# ── Data fetch ───────────────────────────────────────────────
offset = st.session_state.companies_page * page_size

# Determine if topic-based filtering
topic_filter_slugs: list[str] | None = None
if selected_l3:
    topic_filter_slugs = [selected_l3]
elif selected_l2:
    topic_filter_slugs = get_l3_slugs_for_l2(selected_l2)
elif selected_l1:
    topic_filter_slugs = get_l3_slugs_for_l1(selected_l1)

if topic_filter_slugs:
    # Topic-based search, then filter in memory
    all_topic_companies = cached_search_companies_by_topic(tuple(topic_filter_slugs))
    # Apply additional filters
    filtered = all_topic_companies
    if query:
        q_lower = query.lower()
        filtered = [
            c for c in filtered
            if q_lower in (c.get("name") or "").lower()
            or q_lower in (c.get("description") or "").lower()
            or q_lower in (c.get("technology") or "").lower()
        ]
    if selected_cat != "All":
        filtered = [c for c in filtered if c.get("main_category") == selected_cat]
    if selected_country != "All":
        filtered = [c for c in filtered if c.get("country") == selected_country]
    if selected_status != "All":
        filtered = [c for c in filtered if c.get("status") == selected_status]
    companies = filtered[offset : offset + page_size]
else:
    companies = cached_search_companies(
        query=query or None,
        main_category=selected_cat if selected_cat != "All" else None,
        country=selected_country if selected_country != "All" else None,
        status=selected_status if selected_status != "All" else None,
        limit=page_size,
        offset=offset,
    )

# ── Toolbar: segmented toggle + page info ────────────────────
list_sel = is_list
card_sel = not is_list

seg_bg = _c["input_bg"]
seg_active_bg = f"linear-gradient(135deg, {PRIMARY}, {PRIMARY_DARK})"
seg_active_fg = "#FFFFFF"
seg_inactive_fg = _c["text_secondary"]
seg_border = _c["glass_border"]

start = offset + 1
end = offset + len(companies)
page_num = st.session_state.companies_page + 1

st.markdown(
    f'<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">'
    # Segmented toggle
    f'<div style="display:inline-flex; border-radius:10px; border:1px solid {seg_border}; '
    f'background:{seg_bg}; overflow:hidden;">'
    # List option
    f'<a href="?view=list" target="_self" style="padding:6px 16px; font-size:0.82rem; font-weight:500; '
    f'text-decoration:none; transition:all 0.2s; '
    f'{"background:" + seg_active_bg + "; color:" + seg_active_fg if list_sel else "color:" + seg_inactive_fg}'
    f';">List</a>'
    # Card option
    f'<a href="?view=card" target="_self" style="padding:6px 16px; font-size:0.82rem; font-weight:500; '
    f'text-decoration:none; transition:all 0.2s; '
    f'{"background:" + seg_active_bg + "; color:" + seg_active_fg if card_sel else "color:" + seg_inactive_fg}'
    f';">Cards</a>'
    f"</div>"
    # Page info
    f'<span style="font-size:0.8rem; color:{_c["text_secondary"]};">'
    f"Showing {start}–{end} (page {page_num})</span>"
    f"</div>",
    unsafe_allow_html=True,
)

# Handle view toggle via query param
if "view" in st.query_params:
    new_view = st.query_params["view"]
    if new_view in ("list", "card") and new_view != st.session_state.companies_view:
        st.session_state.companies_view = new_view
        del st.query_params["view"]
        st.rerun()
    elif "view" in st.query_params:
        del st.query_params["view"]

# ── Content ──────────────────────────────────────────────────
DETAIL_PATH = "/company_detail"

if companies:
    if st.session_state.companies_view == "card":
        st.markdown(
            render_company_cards(companies, dark=dark, detail_path=DETAIL_PATH),
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            _render_list_table(companies, topics_map, dark=dark, detail_path=DETAIL_PATH),
            unsafe_allow_html=True,
        )

    # ── Pagination ───────────────────────────────────────────
    pag_left, _, pag_right = st.columns([1, 8, 1])
    with pag_left:
        if st.button(
            "← Prev",
            disabled=st.session_state.companies_page == 0,
            use_container_width=True,
        ):
            st.session_state.companies_page -= 1
            st.rerun()
    with pag_right:
        if st.button("Next →", use_container_width=True):
            st.session_state.companies_page += 1
            st.rerun()
else:
    st.info("No companies found with the current filters.")
