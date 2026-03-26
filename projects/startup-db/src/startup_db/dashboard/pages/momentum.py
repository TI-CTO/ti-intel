"""Funding Momentum — L3 topic funding activity over time."""

from __future__ import annotations

from datetime import date, timedelta

import pandas as pd
import plotly.express as px
import streamlit as st

from startup_db.dashboard.components import is_dark_mode
from startup_db.dashboard.data import cached_funding_momentum
from startup_db.dashboard.theme import (
    DARK,
    LIGHT,
    get_plotly_layout,
    render_countup_js,
)
from startup_db.taxonomy import L1_COLORS, L1_LABELS

dark = is_dark_mode()
PL = get_plotly_layout(dark)
C = DARK if dark else LIGHT

st.title("Funding Momentum")


def _fmt_money(amount: float) -> str:
    """Format a dollar amount as $XB, $XM, or $X.

    Args:
        amount: Dollar amount as float.

    Returns:
        Human-readable string like '$1.2B', '$500M', '$10M'.
    """
    if amount >= 1e9:
        return f"${amount / 1e9:.1f}B"
    if amount >= 1e6:
        return f"${amount / 1e6:.0f}M"
    return f"${amount:,.0f}"


# ── Time filter ──────────────────────────────────────────────
time_options = {"3M": 90, "6M": 180, "1Y": 365, "All": None}
selected_period = st.selectbox(
    "Period",
    options=list(time_options.keys()),
    index=2,
)
cutoff_days = time_options[selected_period]
cutoff_date: date | None = date.today() - timedelta(days=cutoff_days) if cutoff_days else None

# ── Load and filter data ─────────────────────────────────────
all_records = cached_funding_momentum()

if cutoff_date:
    filtered: list[dict] = []
    for rec in all_records:
        raw = rec.get("announced_date")
        if raw:
            try:
                rec_date = date.fromisoformat(str(raw)[:10])
                if rec_date >= cutoff_date:
                    filtered.append(rec)
            except ValueError:
                pass
    records = filtered
else:
    records = all_records

if not records:
    st.info("No funding data available for the selected period.")
    st.stop()

df = pd.DataFrame(records)

# ── KPI row ───────────────────────────────────────────────────
# Deduplicate per (company_id, l3_slug) to avoid double-counting when a
# company has multiple L3 topics — count each round once per company.
# For total raised: sum raised_amount once per (company_id, announced_date)
rounds_df = df.drop_duplicates(subset=["company_id", "announced_date"])
total_raised = rounds_df["raised_amount"].sum()
round_count = len(rounds_df)

# Hottest L3: most total raised in period (deduplicated by company per l3)
l3_agg = (
    df.drop_duplicates(subset=["company_id", "l3_slug"]).groupby("l3_slug")["raised_amount"].sum()
)
hottest_l3 = l3_agg.idxmax() if not l3_agg.empty else "—"
hottest_l3_label = hottest_l3.replace("-", " ").title()

col1, col2, col3 = st.columns(3)
col1.metric("Total Invested", _fmt_money(total_raised))
col2.metric("Rounds", f"{round_count:,}")
col3.metric("Hottest L3", hottest_l3_label)
render_countup_js()

st.divider()

# ── Bar chart: L3 by total raised ────────────────────────────
st.subheader("Raised by L3 Topic")

# Aggregate: one row per (company_id, l3_slug) to avoid double-counting
l3_detail = (
    df.drop_duplicates(subset=["company_id", "l3_slug"])
    .groupby(["l3_slug", "l1"])
    .agg(total_raised=("raised_amount", "sum"), rounds=("raised_amount", "count"))
    .reset_index()
    .sort_values("total_raised", ascending=True)
)

if not l3_detail.empty:
    # Map L1 to display color
    l3_detail["l1_color"] = l3_detail["l1"].map(L1_COLORS)
    l3_detail["l3_label"] = l3_detail["l3_slug"].str.replace("-", " ").str.title()

    fig = px.bar(
        l3_detail,
        x="total_raised",
        y="l3_label",
        orientation="h",
        color="l1",
        color_discrete_map=L1_COLORS,
        labels={
            "total_raised": "Total Raised (USD)",
            "l3_label": "L3 Topic",
            "l1": "Domain",
        },
        custom_data=["rounds", "l1"],
    )
    fig.update_traces(
        hovertemplate=(
            "<b>%{y}</b><br>"
            "Raised: %{x:,.0f}<br>"
            "Rounds: %{customdata[0]}<br>"
            "Domain: %{customdata[1]}<extra></extra>"
        )
    )
    # Rename legend entries to display labels
    for trace in fig.data:
        trace.name = L1_LABELS.get(trace.name, trace.name)

    chart_height = max(300, len(l3_detail) * 28)
    fig.update_layout(
        **PL,
        height=chart_height,
        legend_title_text="Domain",
        xaxis_title="Total Raised (USD)",
        yaxis_title=None,
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No L3 topic data to display.")

st.divider()

# ── Summary table ─────────────────────────────────────────────
st.subheader("L3 Breakdown")

# Build table: L3 | L1 | Total Raised | Rounds | Top Companies
l3_companies = (
    df.drop_duplicates(subset=["company_id", "l3_slug"])
    .groupby("l3_slug")["company_name"]
    .apply(lambda names: ", ".join(n for n in list(dict.fromkeys(names))[:3] if n))
    .reset_index()
    .rename(columns={"company_name": "top_companies"})
)

table_df = (
    l3_detail.merge(l3_companies, on="l3_slug", how="left")
    .sort_values("total_raised", ascending=False)
    .reset_index(drop=True)
)

table_df["L3"] = table_df["l3_slug"].str.replace("-", " ").str.title()
table_df["L1"] = table_df["l1"].map(L1_LABELS).fillna(table_df["l1"])
table_df["Total Raised"] = table_df["total_raised"].apply(_fmt_money)
table_df["Rounds"] = table_df["rounds"].astype(int)
table_df["Top Companies"] = table_df["top_companies"].fillna("—")

display_df = table_df[["L3", "L1", "Total Raised", "Rounds", "Top Companies"]]
st.dataframe(display_df, use_container_width=True, hide_index=True)
