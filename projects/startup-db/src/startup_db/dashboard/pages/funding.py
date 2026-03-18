"""Funding — trends, breakdown, and analysis."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from startup_db.dashboard.components import is_dark_mode
from startup_db.dashboard.data import cached_funding_by_domain, cached_funding_stats
from startup_db.dashboard.theme import (
    CHART_COLORS,
    DARK,
    LIGHT,
    _glass_css,
    get_plotly_layout,
    render_countup_js,
    render_plotly_animated,
    render_styled_dataframe,
)

dark = is_dark_mode()
PL = get_plotly_layout(dark)
st.title("Funding Analysis")

funding = cached_funding_stats()

# ── KPIs ─────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)
col1.metric("Total Rounds", f"{funding['total_rounds']:,}")
col2.metric("Total Raised", f"${funding['total_raised']:,.0f}")
avg = funding["total_raised"] / max(funding["total_rounds"], 1)
col3.metric("Avg per Round", f"${avg:,.0f}")
render_countup_js()

st.divider()

# ── By Year ──────────────────────────────────────────────────
st.subheader("Funding by Year")
year_data = [
    {"year": k, "rounds": v["count"], "raised": v["total_raised"]}
    for k, v in funding["by_year"].items()
    if k != "unknown"
]
if year_data:
    year_df = pd.DataFrame(year_data).sort_values("year")

    tab1, tab2 = st.tabs(["Amount Raised", "Round Count"])
    with tab1:
        fig = px.bar(
            year_df,
            x="year",
            y="raised",
            labels={"raised": "USD", "year": "Year"},
            color_discrete_sequence=CHART_COLORS,
        )
        fig.update_layout(**PL, height=400)
        render_plotly_animated(fig, height=400, dark=dark)
    with tab2:
        fig = px.bar(
            year_df,
            x="year",
            y="rounds",
            labels={"rounds": "Rounds", "year": "Year"},
            color_discrete_sequence=[CHART_COLORS[2]],
        )
        fig.update_layout(**PL, height=400)
        render_plotly_animated(fig, height=400, dark=dark)

# ── By Round Type ────────────────────────────────────────────
st.subheader("By Round Type")
rt_data = [
    {"type": k, "count": v["count"], "raised": v["total_raised"]}
    for k, v in funding["by_round_type"].items()
]
if rt_data:
    rt_df = pd.DataFrame(rt_data)
    left, right = st.columns(2)
    with left:
        fig = px.pie(
            rt_df,
            values="count",
            names="type",
            hole=0.35,
            color_discrete_sequence=CHART_COLORS,
        )
        fig.update_layout(**PL, height=350)
        st.plotly_chart(fig, use_container_width=True)
    with right:
        rt_df["avg_raised"] = rt_df["raised"] / rt_df["count"].replace(0, 1)
        rt_df = rt_df.sort_values("avg_raised", ascending=False)
        fig = px.bar(
            rt_df,
            x="avg_raised",
            y="type",
            orientation="h",
            labels={"avg_raised": "Avg Raised (USD)", "type": "Type"},
            color_discrete_sequence=[CHART_COLORS[1]],
        )
        fig.update_layout(
            **PL,
            height=350,
            yaxis={"categoryorder": "total ascending"},
        )
        render_plotly_animated(fig, height=350, dark=dark)

# ── By Domain (L1 → L2 Treemap) ─────────────────────────────
import html as _html

from startup_db.taxonomy import L1_COLORS, L1_LABELS

st.subheader("By Domain")

domain_data = cached_funding_by_domain()
by_l2 = domain_data.get("by_l2", {})
companies_by_l2 = domain_data.get("companies_by_l2", {})

C = DARK if dark else LIGHT

if by_l2:
    def _fmt(amount: float) -> str:
        if amount >= 1e9:
            return f"${amount / 1e9:.1f}B"
        if amount >= 1e6:
            return f"${amount / 1e6:.0f}M"
        return f"${amount:,.0f}"

    tree_rows = []
    for l2, info in by_l2.items():
        l1 = info["l1"]
        tree_rows.append({
            "l1": L1_LABELS.get(l1, l1),
            "l2": l2.replace("-", " ").title(),
            "l2_slug": l2,
            "raised": info["total_raised"],
            "count": info["count"],
            "raised_label": _fmt(info["total_raised"]),
        })

    tree_df = pd.DataFrame(tree_rows)

    # Color map: L1 label → L1 color
    color_map = {L1_LABELS.get(k, k): v for k, v in L1_COLORS.items()}

    fig = px.treemap(
        tree_df,
        path=["l1", "l2"],
        values="raised",
        color="l1",
        color_discrete_map=color_map,
        custom_data=["count", "raised_label", "l2_slug"],
    )
    fig.update_traces(
        texttemplate="<b>%{label}</b><br>%{customdata[1]}<br>%{customdata[0]} rounds",
        textposition="middle center",
        textfont_size=12,
    )
    fig.update_layout(**PL, height=450, showlegend=False)

    event = st.plotly_chart(fig, use_container_width=True, on_select="rerun")

    # ── Click → show companies in selected L2 domain ─────────
    if event and event.selection and event.selection.get("points"):
        pt = event.selection["points"][0]
        label = pt.get("label", "")
        # Find matching L2 slug
        matched_l2 = None
        for row in tree_rows:
            if row["l2"] == label:
                matched_l2 = row["l2_slug"]
                break

        if matched_l2 and matched_l2 in companies_by_l2:
            companies = companies_by_l2[matched_l2]
            companies_sorted = sorted(companies, key=lambda c: -c["raised"])
            st.caption(f"{label} — {len(companies_sorted)} companies")

            comp_df = pd.DataFrame(companies_sorted)
            comp_df["raised"] = comp_df["raised"].apply(_fmt)
            display_df = comp_df[["name", "country", "raised", "rounds"]].rename(
                columns={"name": "Company", "country": "Country", "raised": "Total Raised", "rounds": "Rounds"}
            )
            st.markdown(
                render_styled_dataframe(display_df, dark=dark),
                unsafe_allow_html=True,
            )
        elif label:
            # Clicked on L1 parent — show summary
            l1_companies = []
            for l2_slug, comps in companies_by_l2.items():
                l2_info = by_l2.get(l2_slug, {})
                if L1_LABELS.get(l2_info.get("l1", ""), "") == label:
                    l1_companies.extend(comps)
            if l1_companies:
                # Deduplicate by slug
                seen = set()
                unique = []
                for c in sorted(l1_companies, key=lambda x: -x["raised"]):
                    if c["slug"] not in seen:
                        seen.add(c["slug"])
                        unique.append(c)
                st.caption(f"{label} — {len(unique)} companies")
                comp_df = pd.DataFrame(unique[:20])
                comp_df["raised"] = comp_df["raised"].apply(_fmt)
                display_df = comp_df[["name", "country", "raised", "rounds"]].rename(
                    columns={"name": "Company", "country": "Country", "raised": "Total Raised", "rounds": "Rounds"}
                )
                st.markdown(
                    render_styled_dataframe(display_df, dark=dark),
                    unsafe_allow_html=True,
                )
else:
    st.info("No domain topic data available.")
