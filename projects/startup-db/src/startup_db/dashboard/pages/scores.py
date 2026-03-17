"""Scores — radar charts, heatmaps, and score distribution."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from startup_db.dashboard.components import is_dark_mode
from startup_db.dashboard.data import cached_all_companies_slim, cached_all_scores
from startup_db.dashboard.theme import CHART_COLORS, get_plotly_layout, render_styled_dataframe

dark = is_dark_mode()
PL = get_plotly_layout(dark)
st.title("Score Analytics")

scores = cached_all_scores()
companies = cached_all_companies_slim()

if not scores:
    st.info("No scores data available.")
    st.stop()

# ── Join scores with company info ────────────────────────────
company_map = {c["id"]: c for c in companies}
for s in scores:
    comp = company_map.get(s.get("company_id"), {})
    s["company_name"] = comp.get("name", "Unknown")
    s["main_category"] = comp.get("main_category", "unknown")
    s["sub_category"] = comp.get("sub_category", "unknown")
    s["country"] = comp.get("country", "unknown")

df = pd.DataFrame(scores)
dims = ["tech_strength", "market_potential", "team_quality", "business_fit", "traction"]
for d in dims:
    df[d] = pd.to_numeric(df[d], errors="coerce").fillna(0)
df["overall_score"] = pd.to_numeric(df.get("overall_score", 0), errors="coerce").fillna(0)

# ── KPIs ─────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
col1.metric("Scored Companies", len(df))
col2.metric("Avg Overall", f"{df['overall_score'].mean():.1f}")
col3.metric("Top Score", f"{df['overall_score'].max():.1f}")
col4.metric("Avg Tech", f"{df['tech_strength'].mean():.1f}")

st.divider()

# ── Ribbon tabs ──────────────────────────────────────────────
tab_dist, tab_rank, tab_scatter, tab_compare = st.tabs(
    ["Distribution", "Rankings", "Scatter Plot", "Compare"]
)

with tab_dist:
    left, right = st.columns([2, 1])
    with left:
        st.subheader("Overall Score Distribution")
        # Pre-compute fixed bin edges so click filtering is exact
        import numpy as np

        score_min = df["overall_score"].min()
        score_max = df["overall_score"].max()
        n_bins = 20
        bin_edges = np.linspace(score_min, score_max, n_bins + 1)

        fig = px.histogram(
            df,
            x="overall_score",
            nbins=n_bins,
            labels={"overall_score": "Overall Score (0–100)", "count": "Companies"},
            color_discrete_sequence=[CHART_COLORS[0]],
        )
        fig.update_traces(
            marker_line_color="rgba(255,255,255,0.6)" if dark else "rgba(255,255,255,0.8)",
            marker_line_width=1.5,
            texttemplate="%{y}",
            textposition="outside",
            textfont_size=10,
        )
        fig.update_layout(
            **PL,
            height=300,
            bargap=0.08,
            yaxis_title="Companies",
        )
        event = st.plotly_chart(fig, use_container_width=True, on_select="rerun")

        # Show companies when a bar is clicked
        if event and event.selection and event.selection.get("points"):
            pt = event.selection["points"][0]
            clicked_x = pt.get("x", None)
            if clicked_x is not None:
                # Find which bin this x value falls into
                bin_idx = int(np.searchsorted(bin_edges, clicked_x, side="right") - 1)
                bin_idx = max(0, min(bin_idx, n_bins - 1))
                bin_min = bin_edges[bin_idx]
                bin_max = bin_edges[bin_idx + 1]
                # Last bin is inclusive on both sides
                if bin_idx == n_bins - 1:
                    filtered = df[
                        (df["overall_score"] >= bin_min)
                        & (df["overall_score"] <= bin_max)
                    ]
                else:
                    filtered = df[
                        (df["overall_score"] >= bin_min)
                        & (df["overall_score"] < bin_max)
                    ]
                filtered = filtered.sort_values("overall_score", ascending=False)
                if not filtered.empty:
                    st.caption(
                        f"Score {bin_min:.0f}–{bin_max:.0f} ({len(filtered)} companies)"
                    )
                    show_cols = [
                        "company_name", "main_category", "country", "overall_score",
                    ]
                    show_cols = [c for c in show_cols if c in filtered.columns]
                    st.markdown(
                        render_styled_dataframe(
                            filtered[show_cols].reset_index(drop=True), dark=dark
                        ),
                        unsafe_allow_html=True,
                    )

    with right:
        st.subheader("Average Scores by Category")
        cat_avg = df.groupby("main_category")[dims].mean().reset_index()
        if not cat_avg.empty:
            cat_avg_melted = cat_avg.melt(
                id_vars="main_category",
                value_vars=dims,
                var_name="dimension",
                value_name="score",
            )
            fig = px.bar(
                cat_avg_melted,
                x="main_category",
                y="score",
                color="dimension",
                barmode="group",
                labels={"score": "Avg Score", "main_category": "Category"},
                color_discrete_sequence=CHART_COLORS,
            )
            fig.update_layout(**PL, height=300)
            st.plotly_chart(fig, use_container_width=True)

with tab_rank:
    st.subheader("Top 20 Companies by Overall Score")
    top = df.nlargest(20, "overall_score")
    display_cols = ["company_name", "main_category", "country", "overall_score"] + dims
    display_cols = [c for c in display_cols if c in top.columns]
    st.markdown(
        render_styled_dataframe(top[display_cols].reset_index(drop=True), dark=dark),
        unsafe_allow_html=True,
    )

with tab_scatter:
    st.subheader("Tech Strength vs Market Potential")
    fig = px.scatter(
        df,
        x="tech_strength",
        y="market_potential",
        color="main_category",
        size="overall_score",
        hover_name="company_name",
        labels={
            "tech_strength": "Tech Strength",
            "market_potential": "Market Potential",
        },
        color_discrete_sequence=CHART_COLORS,
    )
    fig.update_layout(**PL, height=500)
    st.plotly_chart(fig, use_container_width=True)

with tab_compare:
    st.subheader("Compare Companies (Radar)")
    compare_names = st.multiselect(
        "Select companies to compare",
        df["company_name"].tolist(),
        max_selections=5,
    )
    if compare_names:
        labels = ["Tech", "Market", "Team", "Fit", "Traction"]
        fig = go.Figure()
        for i, name in enumerate(compare_names):
            row = df[df["company_name"] == name].iloc[0]
            values = [row[d] for d in dims]
            fig.add_trace(
                go.Scatterpolar(
                    r=values + [values[0]],
                    theta=labels + [labels[0]],
                    fill="toself",
                    name=name,
                    line=dict(color=CHART_COLORS[i % len(CHART_COLORS)]),
                )
            )
        fig.update_layout(
            **PL,
            polar=dict(radialaxis=dict(range=[0, 10])),
            height=450,
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Select up to 5 companies above to compare their scores on a radar chart.")
