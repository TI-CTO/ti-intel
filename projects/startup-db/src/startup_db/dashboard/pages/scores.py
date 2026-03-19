"""Scores — radar charts, heatmaps, and score distribution."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from startup_db.dashboard.components import is_dark_mode
from startup_db.dashboard.data import cached_all_companies_slim, cached_all_scores
from startup_db.dashboard.theme import CHART_COLORS, get_plotly_layout, render_countup_js, render_plotly_animated, render_styled_dataframe
from startup_db.taxonomy import L1_BY_SUBCATEGORY, L1_LABELS

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
    l1_slug = L1_BY_SUBCATEGORY.get(comp.get("sub_category", ""), "other")
    s["domain"] = L1_LABELS.get(l1_slug, l1_slug)
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
render_countup_js()

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
        st.subheader("Average Scores by Domain")
        dom_avg = df.groupby("domain")[dims].mean().reset_index()
        if not dom_avg.empty:
            dom_avg_melted = dom_avg.melt(
                id_vars="domain",
                value_vars=dims,
                var_name="dimension",
                value_name="score",
            )
            fig = px.bar(
                dom_avg_melted,
                x="domain",
                y="score",
                color="dimension",
                barmode="group",
                labels={"score": "Avg Score", "domain": "Domain"},
                color_discrete_sequence=CHART_COLORS,
            )
            fig.update_layout(**PL, height=380)
            fig.update_layout(
                margin=dict(l=50, r=20, t=50, b=60),
                xaxis_tickangle=-30,
                legend=dict(
                    title_text="",
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="center",
                    x=0.5,
                ),
            )
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
    domain_colors = {
        "Agentic AI": "#C50063",
        "Voice AI": "#06B6D4",
        "Secure AI": "#34D399",
        "other": "#9E9E9E",
    }
    # Add jitter to prevent integer stacking
    import numpy as np

    scatter_df = df.copy()
    rng = np.random.default_rng(42)
    scatter_df["tech_jitter"] = scatter_df["tech_strength"] + rng.uniform(-0.3, 0.3, len(scatter_df))
    scatter_df["market_jitter"] = scatter_df["market_potential"] + rng.uniform(-0.3, 0.3, len(scatter_df))

    fig = px.scatter(
        scatter_df,
        x="tech_jitter",
        y="market_jitter",
        color="domain",
        hover_name="company_name",
        hover_data={"tech_jitter": False, "market_jitter": False, "tech_strength": True, "market_potential": True, "overall_score": True},
        labels={
            "tech_jitter": "Tech Strength",
            "market_jitter": "Market Potential",
            "domain": "Domain",
        },
        color_discrete_map=domain_colors,
        opacity=0.6,
    )
    fig.update_traces(marker=dict(size=8))
    fig.update_layout(**PL, height=600)
    fig.update_layout(
        margin=dict(l=40, r=10, t=10, b=40),
        legend=dict(
            title_text="",
            orientation="h",
            yanchor="bottom",
            y=1.0,
            xanchor="center",
            x=0.5,
        ),
    )
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
        render_plotly_animated(fig, height=450, dark=dark)
    else:
        st.info("Select up to 5 companies above to compare their scores on a radar chart.")
