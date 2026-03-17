"""Startup Dashboard — Overview page content."""

from __future__ import annotations

import html as _html
from collections import defaultdict

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from startup_db.dashboard.components import is_dark_mode
from startup_db.dashboard.data import (
    cached_company_stats,
    cached_company_topics_bulk,
    cached_funding_stats,
    get_repo,
)
from startup_db.dashboard.theme import (
    CHART_COLORS,
    DARK,
    LIGHT,
    PRIMARY,
    _glass_css,
    get_plotly_layout,
)
from startup_db.taxonomy import L1_COLORS, L1_LABELS, get_l1_for_l3

dark = is_dark_mode()
PL = get_plotly_layout(dark)
C = DARK if dark else LIGHT
glass = _glass_css(C)

st.title("Startup Dashboard")

# ── Data ─────────────────────────────────────────────────────
repo = get_repo()
stats = cached_company_stats()
funding = cached_funding_stats()
topics_map = cached_company_topics_bulk()

# Compute L1 domain counts
l1_counts: dict[str, int] = {}
_seen: dict[str, set[str]] = {}
for cid, slugs in topics_map.items():
    for slug in slugs:
        l1 = get_l1_for_l3(slug)
        if l1:
            _seen.setdefault(l1, set())
            if cid not in _seen[l1]:
                _seen[l1].add(cid)
                l1_counts[l1] = l1_counts.get(l1, 0) + 1

# Compute funding-derived stats
funded_companies = sum(
    1 for v in funding.get("by_round_type", {}).values()
    for _ in range(v.get("count", 0))
)
total_raised = funding.get("total_raised", 0)

# Recent funding by year
year_data = {
    k: v for k, v in funding.get("by_year", {}).items()
    if k not in ("unknown", "")
}
sorted_years = sorted(year_data.keys())


def _fmt_money(amount: float) -> str:
    if amount >= 1_000_000_000:
        return f"${amount / 1_000_000_000:.1f}B"
    if amount >= 1_000_000:
        return f"${amount / 1_000_000:.0f}M"
    if amount >= 1_000:
        return f"${amount / 1_000:.0f}K"
    return f"${amount:,.0f}"


# ── KPI metrics ──────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
col1.metric("Companies", f"{stats['total']:,}")
col2.metric("Total Raised", _fmt_money(total_raised))

# YoY trend
if len(sorted_years) >= 2:
    latest_yr = sorted_years[-1]
    prev_yr = sorted_years[-2]
    latest_raised = year_data[latest_yr]["total_raised"]
    prev_raised = year_data[prev_yr]["total_raised"]
    if prev_raised > 0:
        yoy_pct = ((latest_raised - prev_raised) / prev_raised) * 100
        col3.metric(
            f"Funding {latest_yr}",
            _fmt_money(latest_raised),
            f"{yoy_pct:+.0f}% YoY",
        )
    else:
        col3.metric(f"Funding {latest_yr}", _fmt_money(latest_raised))
else:
    col3.metric("Countries", len(stats.get("by_country", {})))

col4.metric("Investors", str(len(
    (repo._client.table("su_investors")
     .select("id", count="exact").execute()).data or []
)))

st.divider()

# ── Tabs ─────────────────────────────────────────────────────
tab_trend, tab_domain, tab_fund = st.tabs([
    "Funding Trends",
    "Domain & Country",
    "Round Types",
])

# ── Tab 1: Funding Trends (주력 탭) ─────────────────────────
with tab_trend:
    # Funding timeline chart
    if sorted_years:
        year_df = pd.DataFrame([
            {
                "year": k,
                "rounds": year_data[k]["count"],
                "raised": year_data[k]["total_raised"],
            }
            for k in sorted_years
        ])
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=year_df["year"],
            y=year_df["raised"],
            name="Raised",
            marker_color=CHART_COLORS[0],
            text=year_df["raised"].apply(_fmt_money),
            textposition="outside",
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Raised: %{text}<br>"
                "<extra></extra>"
            ),
        ))
        fig.update_layout(
            **PL,
            height=380,
            showlegend=False,
            yaxis_title="Total Raised (USD)",
            xaxis_title="",
        )
        st.plotly_chart(fig, use_container_width=True)

    # Top funded companies by period
    from datetime import date, timedelta

    st.subheader("Top Funded Companies")

    period_options = {
        "1W": 7,
        "1M": 30,
        "3M": 90,
        "6M": 180,
        "12M": 365,
        "All": 0,
    }
    period_cols = st.columns(len(period_options))
    if "overview_period" not in st.session_state:
        st.session_state.overview_period = "All"

    for i, (label, _days) in enumerate(period_options.items()):
        with period_cols[i]:
            is_active = st.session_state.overview_period == label
            if st.button(
                label,
                key=f"period_{label}",
                use_container_width=True,
                type="primary" if is_active else "secondary",
            ):
                st.session_state.overview_period = label
                st.rerun()

    selected_days = period_options[st.session_state.overview_period]
    today = date.today()

    if selected_days > 0:
        cutoff = (today - timedelta(days=selected_days)).isoformat()
        # Get rounds in period, sum by company
        recent_rounds = (
            repo._client.table("su_funding_rounds")
            .select("company_id,raised_amount,announced_date,round_type")
            .gte("announced_date", cutoff)
            .order("announced_date", desc=True)
            .execute()
        )
        rounds_data = recent_rounds.data or []
        # Aggregate by company
        company_raised: dict[str, dict] = {}
        for r in rounds_data:
            cid = r["company_id"]
            amt = float(r.get("raised_amount") or 0)
            if cid not in company_raised:
                company_raised[cid] = {
                    "total": 0,
                    "latest_date": r.get("announced_date"),
                    "latest_type": r.get("round_type"),
                }
            company_raised[cid]["total"] += amt

        if company_raised:
            # Get company details
            top_cids = sorted(
                company_raised.keys(),
                key=lambda x: -company_raised[x]["total"],
            )[:10]
            companies_result = (
                repo._client.table("su_companies")
                .select("id,name,slug,country,sub_category")
                .in_("id", top_cids)
                .execute()
            )
            cid_to_company = {
                c["id"]: c for c in (companies_result.data or [])
            }
            top_list = []
            for cid in top_cids:
                comp = cid_to_company.get(cid)
                if comp:
                    top_list.append({
                        **comp,
                        "raised": company_raised[cid]["total"],
                        "date": company_raised[cid]["latest_date"],
                        "round": company_raised[cid]["latest_type"],
                    })
        else:
            top_list = []
    else:
        # All time — use pre-computed total_raised
        result = (
            repo._client.table("su_companies")
            .select(
                "id,name,slug,total_raised,"
                "country,sub_category,last_funding_type"
            )
            .gt("total_raised", 0)
            .order("total_raised", desc=True)
            .limit(10)
            .execute()
        )
        top_list = [
            {
                **c,
                "raised": float(c.get("total_raised") or 0),
                "round": c.get("last_funding_type"),
            }
            for c in (result.data or [])
        ]

    if top_list:
        border = C["glass_border"]
        rows_html = []
        for i, c in enumerate(top_list, 1):
            name = _html.escape(c.get("name") or "")
            slug = _html.escape(c.get("slug") or "")
            country = _html.escape(c.get("country") or "")
            sub = _html.escape(c.get("sub_category") or "")
            rd = _html.escape(
                (c.get("round") or "").replace("_", " ").title()
            )
            raised = c.get("raised", 0)
            href = f"/company_detail?slug={slug}"
            rows_html.append(
                f'<tr style="border-bottom:1px solid {border};">'
                f'<td style="padding:10px 8px;color:{C["text_secondary"]};'
                f'font-size:0.82rem;">{i}</td>'
                f'<td style="padding:10px 8px;">'
                f'<a href="{href}" target="_self"'
                f' style="color:{C["text"]};text-decoration:none;'
                f'font-weight:500;">{name}</a></td>'
                f'<td style="padding:10px 8px;'
                f'color:{C["text_secondary"]};'
                f'font-size:0.85rem;">{sub}</td>'
                f'<td style="padding:10px 8px;'
                f'color:{C["text_secondary"]};'
                f'font-size:0.85rem;">{country}</td>'
                f'<td style="padding:10px 8px;'
                f'color:{C["text_secondary"]};'
                f'font-size:0.85rem;">{rd}</td>'
                f'<td style="padding:10px 8px;text-align:right;'
                f'font-weight:600;color:{C["text"]};">'
                f'{_fmt_money(raised)}</td>'
                f'</tr>'
            )
        st.markdown(
            f'<table style="width:100%;border-collapse:collapse;'
            f'font-size:0.88rem;">'
            f'<thead><tr style="border-bottom:2px solid {border};">'
            f'<th style="text-align:left;padding:8px;width:30px;'
            f'color:{C["text_secondary"]};font-size:0.75rem;'
            f'text-transform:uppercase;">#</th>'
            f'<th style="text-align:left;padding:8px;'
            f'color:{C["text_secondary"]};font-size:0.75rem;'
            f'text-transform:uppercase;">Company</th>'
            f'<th style="text-align:left;padding:8px;'
            f'color:{C["text_secondary"]};font-size:0.75rem;'
            f'text-transform:uppercase;">Category</th>'
            f'<th style="text-align:left;padding:8px;'
            f'color:{C["text_secondary"]};font-size:0.75rem;'
            f'text-transform:uppercase;">Country</th>'
            f'<th style="text-align:left;padding:8px;'
            f'color:{C["text_secondary"]};font-size:0.75rem;'
            f'text-transform:uppercase;">Round</th>'
            f'<th style="text-align:right;padding:8px;'
            f'color:{C["text_secondary"]};font-size:0.75rem;'
            f'text-transform:uppercase;">Raised</th>'
            f'</tr></thead>'
            f'<tbody>{"".join(rows_html)}</tbody></table>',
            unsafe_allow_html=True,
        )
    else:
        period_label = st.session_state.overview_period
        st.info(f"No funding rounds found in the last {period_label}.")

# ── Tab 2: Domain & Country ──────────────────────────────────
with tab_domain:
    left, right = st.columns(2)
    with left:
        st.subheader("By L1 Domain")
        other_count = stats["total"] - len(topics_map)
        if other_count > 0:
            l1_counts["other"] = other_count

        l1_labels_map = {**L1_LABELS, "other": "Other"}
        l1_color_map = {**L1_COLORS, "other": "#9CA3AF"}
        domain_df = pd.DataFrame([
            {"domain": l1_labels_map.get(k, k), "count": v}
            for k, v in sorted(
                l1_counts.items(), key=lambda x: -x[1]
            )
        ])
        if not domain_df.empty:
            colors = [
                l1_color_map.get(k, "#9CA3AF")
                for k in sorted(
                    l1_counts.keys(),
                    key=lambda x: -l1_counts[x],
                )
            ]
            fig = px.bar(
                domain_df,
                x="count",
                y="domain",
                orientation="h",
                color="domain",
                color_discrete_sequence=colors,
            )
            fig.update_layout(
                **PL,
                height=400,
                showlegend=False,
                yaxis={"categoryorder": "total ascending"},
            )
            st.plotly_chart(fig, use_container_width=True)

    with right:
        st.subheader("By Country")
        country_df = pd.DataFrame(
            [{"country": k, "count": v}
             for k, v in stats["by_country"].items()]
        )
        if not country_df.empty:
            fig = px.pie(
                country_df.head(10),
                values="count",
                names="country",
                hole=0.4,
                color_discrete_sequence=CHART_COLORS,
            )
            fig.update_layout(**PL, height=400)
            st.plotly_chart(fig, use_container_width=True)

# ── Tab 3: Round Types ───────────────────────────────────────
with tab_fund:
    left2, right2 = st.columns(2)
    with left2:
        st.subheader("By Round Type")
        rt_df = pd.DataFrame([
            {
                "round_type": k,
                "count": v["count"],
                "raised": v["total_raised"],
            }
            for k, v in funding["by_round_type"].items()
        ])
        if not rt_df.empty:
            fig = px.bar(
                rt_df.head(10),
                x="count",
                y="round_type",
                orientation="h",
                labels={"count": "Rounds", "round_type": "Type"},
                color_discrete_sequence=[CHART_COLORS[1]],
            )
            fig.update_layout(
                **PL,
                height=350,
                showlegend=False,
                yaxis={"categoryorder": "total ascending"},
            )
            st.plotly_chart(fig, use_container_width=True)

    with right2:
        st.subheader("By Status")
        status_df = pd.DataFrame([
            {"status": k, "count": v}
            for k, v in stats["by_status"].items()
        ])
        if not status_df.empty:
            fig = px.pie(
                status_df,
                values="count",
                names="status",
                hole=0.4,
                color_discrete_sequence=CHART_COLORS,
            )
            fig.update_layout(**PL, height=350)
            st.plotly_chart(fig, use_container_width=True)
