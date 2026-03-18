"""Company Detail — 4-tier profile inspired by Crunchbase/PitchBook."""

from __future__ import annotations

import html as _html

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from startup_db.dashboard.components import is_dark_mode
from startup_db.dashboard.data import (
    cached_all_companies_slim,
    cached_company_detail,
    cached_company_relations,
)
from startup_db.dashboard.theme import (
    CHART_COLORS,
    DARK,
    LIGHT,
    PRIMARY,
    PRIMARY_GRADIENT,
    STATUS_BADGE_COLORS,
    STATUS_BADGE_COLORS_DARK,
    _glass_css,
    get_plotly_layout,
    render_countup_js,
    render_plotly_animated,
)
from startup_db.taxonomy import L1_COLORS, L1_LABELS, get_l1_for_l3, get_l2_for_l3

dark = is_dark_mode()
PL = get_plotly_layout(dark)
C = DARK if dark else LIGHT
BADGE = STATUS_BADGE_COLORS_DARK if dark else STATUS_BADGE_COLORS

# ── Company selector (sidebar + query param) ─────────────────
all_companies = cached_all_companies_slim()
slug_name_map = {c["slug"]: c["name"] for c in all_companies}
slug_list = sorted(slug_name_map.keys())

# Priority: query param > session state > first in list
default_slug = st.query_params.get("slug", st.session_state.get("selected_company_slug", ""))
if default_slug and default_slug in slug_list:
    st.session_state["selected_company_slug"] = default_slug

default_idx = 0
if default_slug in slug_list:
    default_idx = slug_list.index(default_slug)

with st.sidebar:
    selected = st.selectbox(
        "Select company",
        slug_list,
        index=default_idx,
        format_func=lambda s: slug_name_map.get(s, s),
    )

if selected:
    st.session_state["selected_company_slug"] = selected

if not selected:
    st.info("Select a company from the sidebar.")
    st.stop()

company = cached_company_detail(selected)
if not company:
    st.error(f"Company '{selected}' not found.")
    st.stop()

score = company.get("latest_score")
rounds = company.get("funding_rounds", [])
people = company.get("people", [])
topics = company.get("topics", [])

# ── Computed highlights ──────────────────────────────────────
# Use pre-computed total_raised if available, else SUM from rounds
total_raised = company.get("total_raised") or sum(
    r.get("raised_amount") or 0 for r in rounds
)
round_count = len(rounds)
people_count = len(people)
overall_score = score.get("overall_score", 0) if score else 0
growth_stage = company.get("growth_stage") or ""
employee_range = company.get("employee_range") or ""


def _safe(val: object) -> str:
    s = str(val) if val else ""
    return "" if s in ("None", "nan", "") else _html.escape(s)


def _fmt_money(amount: float) -> str:
    if amount >= 1_000_000_000:
        return f"${amount / 1_000_000_000:.1f}B"
    if amount >= 1_000_000:
        return f"${amount / 1_000_000:.1f}M"
    if amount >= 1_000:
        return f"${amount / 1_000:.0f}K"
    if amount > 0:
        return f"${amount:,.0f}"
    return "—"


# ══════════════════════════════════════════════════════════════
# TIER 1 — Hero Header
# ══════════════════════════════════════════════════════════════
status = _safe(company.get("status")) or "unknown"
status_fg, status_bg = BADGE.get(status, ("#6B7280", "rgba(107,114,128,0.15)"))

name = _safe(company.get("name"))
category = _safe(company.get("main_category"))
sub_category = _safe(company.get("sub_category"))
country = _safe(company.get("country"))
city = _safe(company.get("city"))
website = company.get("website") or ""
founded = _safe(company.get("founded_date"))

location = ", ".join(filter(None, [city, country]))

glass = _glass_css(C)

# Build subtitle parts
subtitle_parts = category
if sub_category:
    subtitle_parts += f" / {sub_category}"
if location:
    subtitle_parts += f" &middot; {location}"
if founded:
    subtitle_parts += f" &middot; Founded {founded[:4]}"
if growth_stage:
    subtitle_parts += f" &middot; {growth_stage.title()}"
if employee_range:
    subtitle_parts += f" &middot; {employee_range} employees"

# Website link
website_html = ""
if website and website not in ("None", "nan"):
    safe_url = _html.escape(website, quote=True)
    safe_label = _html.escape(website)
    website_html = (
        f'<a href="{safe_url}" target="_blank" '
        f'style="font-size:0.85rem; color:{PRIMARY}; text-decoration:none;">'
        f"{safe_label}</a>"
    )

# Hero identity
st.markdown(
    f'<div style="{glass} border-radius:20px; padding:28px 32px; margin-bottom:4px;">'
    f'<div style="display:flex; align-items:center; gap:12px; margin-bottom:8px; flex-wrap:wrap;">'
    f'<span style="font-size:1.6rem; font-weight:700; color:{C["text"]}; letter-spacing:-0.02em;">{name}</span>'
    f'<span style="font-size:0.75rem; font-weight:600; padding:4px 12px; border-radius:10px; '
    f'color:{status_fg}; background:{status_bg};">{status.upper()}</span>'
    f"</div>"
    f'<div style="font-size:0.9rem; color:{C["text_secondary"]}; margin-bottom:6px;">{subtitle_parts}</div>'
    f"{website_html}"
    f"</div>",
    unsafe_allow_html=True,
)

# ── Topic badges ──────────────────────────────────────────────
if topics:
    topic_badges = []
    for t in topics:
        l3 = t["l3_slug"]
        l1 = get_l1_for_l3(l3)
        l2 = get_l2_for_l3(l3)
        color = L1_COLORS.get(l1 or "", "#6B7280")
        l1_label = L1_LABELS.get(l1 or "", "")
        badge_label = _html.escape(l3)
        topic_badges.append(
            f'<span style="display:inline-block; font-size:0.75rem; padding:3px 10px; border-radius:10px; '
            f'margin:2px 4px; background:{color}18; color:{color}; border:1px solid {color}40; '
            f'font-weight:500;">{badge_label}</span>'
        )
    st.markdown(
        f'<div style="margin-bottom:12px; line-height:2;">{"".join(topic_badges)}</div>',
        unsafe_allow_html=True,
    )

# Highlight KPI badges — use st.columns + st.metric
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Total Raised", _fmt_money(total_raised))
kpi2.metric("Rounds", str(round_count))
kpi3.metric("Team", str(people_count))
score_label = f"{overall_score:.0f} / 100" if overall_score else "—"
kpi4.metric("Score", score_label)
render_countup_js()


# ══════════════════════════════════════════════════════════════
# TIER 2 — About & Technology (glass cards side by side)
# ══════════════════════════════════════════════════════════════
description = _safe(company.get("description"))
technology = _safe(company.get("technology"))
main_product = _safe(company.get("main_product"))

has_about = description or main_product
has_tech = technology

if has_about or has_tech:
    cols = st.columns(2 if (has_about and has_tech) else 1)

    if has_about:
        with cols[0]:
            about_parts = []
            if description:
                about_parts.append(
                    f'<p style="font-size:0.88rem; color:{C["text"]}; line-height:1.65;">'
                    f"{description[:600]}</p>"
                )
            if main_product:
                about_parts.append(
                    f'<div style="margin-top:12px;">'
                    f'<span style="font-size:0.72rem; font-weight:600; text-transform:uppercase; '
                    f'letter-spacing:0.05em; color:{C["text_secondary"]};">Main Product</span>'
                    f'<p style="font-size:0.85rem; color:{C["text"]}; margin-top:4px;">{main_product}</p>'
                    f"</div>"
                )

            st.markdown(
                f'<div style="{glass} border-radius:16px; padding:20px 24px;">'
                f'<div style="font-size:0.95rem; font-weight:600; color:{C["text"]}; margin-bottom:12px;">About</div>'
                f'{"".join(about_parts)}'
                f"</div>",
                unsafe_allow_html=True,
            )

    if has_tech:
        col_idx = 1 if has_about else 0
        with cols[col_idx]:
            st.markdown(
                f'<div style="{glass} border-radius:16px; padding:20px 24px;">'
                f'<div style="font-size:0.95rem; font-weight:600; color:{C["text"]}; margin-bottom:12px;">Technology</div>'
                f'<p style="font-size:0.88rem; color:{C["text"]}; line-height:1.65;">{technology[:600]}</p>'
                f"</div>",
                unsafe_allow_html=True,
            )


# ══════════════════════════════════════════════════════════════
# TIER 3 — Tabbed detail sections
# ══════════════════════════════════════════════════════════════
tab_labels = []
tab_keys = []

if rounds:
    tab_labels.append(f"💰 Funding ({round_count})")
    tab_keys.append("funding")
if people:
    tab_labels.append(f"👥 People ({people_count})")
    tab_keys.append("people")
if score and any(score.get(d, 0) for d in ["tech_strength", "market_potential", "team_quality", "business_fit", "traction"]):
    tab_labels.append("📊 Score")
    tab_keys.append("score")

# Relations
relations = []
if company.get("id"):
    relations = cached_company_relations(company["id"])
if relations:
    tab_labels.append(f"🔗 Relations ({len(relations)})")
    tab_keys.append("relations")

if tab_labels:
    tabs = st.tabs(tab_labels)
    tab_map = dict(zip(tab_keys, tabs))

    # ── Funding tab ──────────────────────────────────────
    if "funding" in tab_map:
        with tab_map["funding"]:
            rounds_df = pd.DataFrame(rounds)
            display_cols = ["round_type", "raised_amount", "currency", "announced_date"]
            display_cols = [c for c in display_cols if c in rounds_df.columns]
            rounds_df = rounds_df[display_cols].sort_values(
                "announced_date", ascending=False, na_position="last"
            )
            rounds_df["raised_amount"] = rounds_df["raised_amount"].apply(
                lambda x: f"${x:,.0f}" if pd.notna(x) and x else "—"
            )
            rounds_df.columns = ["Round", "Amount", "Currency", "Date"][:len(display_cols)]
            st.dataframe(rounds_df, hide_index=True, use_container_width=True)

            # Funding timeline mini-chart
            timeline_df = pd.DataFrame(rounds)
            if "raised_amount" in timeline_df.columns and "announced_date" in timeline_df.columns:
                timeline_df = timeline_df.dropna(subset=["raised_amount", "announced_date"])
                if not timeline_df.empty:
                    timeline_df = timeline_df.sort_values("announced_date")
                    timeline_df["label"] = timeline_df["round_type"].fillna("Unknown")
                    fig = go.Figure()
                    fig.add_trace(go.Bar(
                        x=timeline_df["announced_date"],
                        y=timeline_df["raised_amount"],
                        text=timeline_df["label"],
                        textposition="outside",
                        marker_color=CHART_COLORS[0],
                        hovertemplate="<b>%{text}</b><br>$%{y:,.0f}<br>%{x}<extra></extra>",
                    ))
                    fig.update_layout(
                        **PL,
                        height=280,
                        yaxis_title="Amount (USD)",
                        xaxis_title="",
                        showlegend=False,
                    )
                    render_plotly_animated(fig, height=280, dark=dark)

    # ── People tab ───────────────────────────────────────
    if "people" in tab_map:
        with tab_map["people"]:
            people_df = pd.DataFrame(people)
            display_cols = ["name", "role", "title", "organization"]
            display_cols = [c for c in display_cols if c in people_df.columns]
            people_show = people_df[display_cols].copy()
            people_show.columns = [c.title() for c in display_cols]
            st.dataframe(people_show, hide_index=True, use_container_width=True)

    # ── Score tab ────────────────────────────────────────
    if "score" in tab_map:
        with tab_map["score"]:
            dims = ["tech_strength", "market_potential", "team_quality", "business_fit", "traction"]
            labels = ["Tech", "Market", "Team", "Fit", "Traction"]
            values = [score.get(d) or 0 for d in dims]

            col_radar, col_detail = st.columns([1, 1])
            with col_radar:
                fig = go.Figure()
                fig.add_trace(
                    go.Scatterpolar(
                        r=values + [values[0]],
                        theta=labels + [labels[0]],
                        fill="toself",
                        name=company["name"],
                        line=dict(color=CHART_COLORS[0], width=2),
                        fillcolor="rgba(197, 0, 99, 0.15)",
                    )
                )
                fig.update_layout(
                    **PL,
                    polar=dict(
                        radialaxis=dict(range=[0, 10], showticklabels=True),
                        bgcolor="rgba(0,0,0,0)",
                    ),
                    height=300,
                    showlegend=False,
                )
                render_plotly_animated(fig, height=300, dark=dark)

            with col_detail:
                for label, dim, val in zip(labels, dims, values):
                    pct = val / 10 * 100
                    bar_color = CHART_COLORS[0] if val >= 7 else (C["warning"] if val >= 4 else C["danger"])
                    st.markdown(
                        f'<div style="margin-bottom:12px;">'
                        f'<div style="display:flex; justify-content:space-between; margin-bottom:4px;">'
                        f'<span style="font-size:0.82rem; font-weight:500; color:{C["text"]};">{label}</span>'
                        f'<span style="font-size:0.82rem; font-weight:600; color:{C["text"]};">{val:.1f}</span>'
                        f"</div>"
                        f'<div style="height:8px; background:{C["input_bg"]}; border-radius:4px; overflow:hidden;">'
                        f'<div class="score-bar-fill" style="height:100%; width:{pct}%; background:{bar_color}; border-radius:4px;"></div>'
                        f"</div></div>",
                        unsafe_allow_html=True,
                    )

    # ── Relations tab ────────────────────────────────────
    if "relations" in tab_map:
        with tab_map["relations"]:
            # Build a lookup for company names
            id_name_map = {c["id"]: c["name"] for c in all_companies}
            cid = company["id"]

            rel_rows = []
            for rel in relations:
                rel_type = rel.get("relation_type", "unknown")
                other_id = rel["related_company_id"] if rel["company_id"] == cid else rel["company_id"]
                other_name = id_name_map.get(other_id, other_id[:8])
                rel_rows.append({"Relation": rel_type.title(), "Company": other_name})

            if rel_rows:
                rel_df = pd.DataFrame(rel_rows)
                # Group by relation type
                for rel_type in rel_df["Relation"].unique():
                    subset = rel_df[rel_df["Relation"] == rel_type]
                    names = subset["Company"].tolist()
                    # Render as tag cloud
                    tags_html = " ".join(
                        f'<span style="display:inline-block; font-size:0.8rem; padding:4px 12px; '
                        f'border-radius:10px; margin:3px; background:{C["input_bg"]}; '
                        f'color:{C["text"]}; border:1px solid {C["glass_border"]};">{_html.escape(n)}</span>'
                        for n in sorted(names)[:30]
                    )
                    remaining = len(names) - 30
                    if remaining > 0:
                        tags_html += (
                            f'<span style="font-size:0.78rem; color:{C["text_secondary"]}; margin-left:8px;">'
                            f"+{remaining} more</span>"
                        )
                    st.markdown(
                        f'<div style="margin-bottom:16px;">'
                        f'<div style="font-size:0.82rem; font-weight:600; color:{C["text_secondary"]}; '
                        f'text-transform:uppercase; letter-spacing:0.04em; margin-bottom:8px;">'
                        f"{rel_type} ({len(names)})</div>"
                        f'<div style="line-height:2;">{tags_html}</div></div>',
                        unsafe_allow_html=True,
                    )


# ══════════════════════════════════════════════════════════════
# TIER 4 — Metadata footer
# ══════════════════════════════════════════════════════════════
tags = company.get("tags")
discovery_source = _safe(company.get("discovery_source"))
created_at = _safe(company.get("created_at"))

meta_items = []
if tags and isinstance(tags, list) and tags:
    tags_html = " ".join(
        f'<span style="font-size:0.75rem; padding:3px 10px; border-radius:8px; '
        f'background:{C["input_bg"]}; color:{C["text_secondary"]}; '
        f'border:1px solid {C["glass_border"]};">{_html.escape(t)}</span>'
        for t in tags
    )
    meta_items.append(f'<span style="font-size:0.78rem; color:{C["text_secondary"]}; margin-right:8px;">Tags:</span>{tags_html}')

if discovery_source:
    meta_items.append(
        f'<span style="font-size:0.78rem; color:{C["text_secondary"]};">Source: {discovery_source}</span>'
    )

if created_at:
    meta_items.append(
        f'<span style="font-size:0.78rem; color:{C["text_secondary"]};">Added: {created_at[:10]}</span>'
    )

if meta_items:
    st.markdown(
        f'<div style="{glass} border-radius:14px; padding:14px 20px; margin-top:24px; '
        f'display:flex; align-items:center; gap:20px; flex-wrap:wrap;">'
        f'{"&nbsp;&middot;&nbsp;".join(meta_items)}'
        f"</div>",
        unsafe_allow_html=True,
    )
