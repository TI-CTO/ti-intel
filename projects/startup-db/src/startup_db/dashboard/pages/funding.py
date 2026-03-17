"""Funding — trends, breakdown, and analysis."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from startup_db.dashboard.components import is_dark_mode
from startup_db.dashboard.data import cached_funding_stats
from startup_db.dashboard.theme import CHART_COLORS, get_plotly_layout

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
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        fig = px.bar(
            year_df,
            x="year",
            y="rounds",
            labels={"rounds": "Rounds", "year": "Year"},
            color_discrete_sequence=[CHART_COLORS[2]],
        )
        fig.update_layout(**PL, height=400)
        st.plotly_chart(fig, use_container_width=True)

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
        st.plotly_chart(fig, use_container_width=True)

# ── By Category ──────────────────────────────────────────────
st.subheader("By Category")
cat_data = [
    {"category": k, "count": v["count"], "raised": v["total_raised"]}
    for k, v in funding["by_category"].items()
]
if cat_data:
    cat_df = pd.DataFrame(cat_data).sort_values("raised", ascending=False)
    cat_df["raised_label"] = cat_df["raised"].apply(
        lambda x: f"${x / 1e9:.1f}B" if x >= 1e9 else f"${x / 1e6:.0f}M"
    )
    fig = px.treemap(
        cat_df.head(20),
        path=["category"],
        values="raised",
        color="category",
        color_discrete_sequence=CHART_COLORS,
        custom_data=["count", "raised_label"],
    )
    fig.update_traces(
        texttemplate="<b>%{label}</b><br>%{customdata[1]}<br>%{customdata[0]} rounds",
        textposition="middle center",
        textfont_size=13,
    )
    fig.update_layout(**PL, height=450, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
