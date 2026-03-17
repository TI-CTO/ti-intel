"""Investors — search, portfolio, and analysis."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from startup_db.dashboard.components import is_dark_mode
from startup_db.dashboard.data import (
    cached_investor_portfolio,
    cached_search_investors,
)
from startup_db.dashboard.theme import render_styled_dataframe

dark = is_dark_mode()
st.title("Investors")

# ── Search ───────────────────────────────────────────────────
with st.sidebar:
    st.header("Filters")
    query = st.text_input("Search investor", placeholder="Name...")
    inv_type = st.selectbox(
        "Type", ["All", "vc", "angel", "cvc", "pe", "accelerator", "government"]
    )

investors = cached_search_investors(
    query=query or None,
    investor_type=inv_type if inv_type != "All" else None,
    limit=100,
)

if not investors:
    st.info("No investors found.")
    st.stop()

st.caption(f"{len(investors)} investors found")

# ── Investor list ────────────────────────────────────────────
inv_df = pd.DataFrame(investors)
display = ["name", "investor_type", "country", "portfolio_count", "description"]
display = [c for c in display if c in inv_df.columns]

st.markdown(
    render_styled_dataframe(inv_df[display], dark=dark),
    unsafe_allow_html=True,
)

# ── Portfolio view ───────────────────────────────────────────
st.divider()
st.subheader("Investor Portfolio")

selected_inv = st.selectbox(
    "Select investor",
    [i["slug"] for i in investors],
    format_func=lambda s: next((i["name"] for i in investors if i["slug"] == s), s),
)

if selected_inv:
    inv = next((i for i in investors if i["slug"] == selected_inv), None)
    if inv:
        portfolio = cached_investor_portfolio(inv["id"])
        if portfolio:
            st.caption(f"{len(portfolio)} portfolio companies")
            port_df = pd.DataFrame(portfolio)
            display = ["name", "main_category", "sub_category", "country", "status"]
            display = [c for c in display if c in port_df.columns]
            st.markdown(
                render_styled_dataframe(port_df[display], dark=dark),
                unsafe_allow_html=True,
            )
        else:
            st.info("No portfolio data linked to this investor.")
