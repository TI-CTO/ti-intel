"""Startup Dashboard — SPA entry point using st.navigation."""

from __future__ import annotations

import streamlit as st

from startup_db.dashboard.components import is_dark_mode, render_navbar, render_sidebar_header
from startup_db.dashboard.theme import inject_css

st.set_page_config(
    page_title="Startup Dashboard",
    page_icon="🚀",
    layout="wide",
)

# Theme setup (runs once, shared across all pages)
render_sidebar_header()
dark = is_dark_mode()
st.markdown(inject_css(dark), unsafe_allow_html=True)

# Define pages
pages = st.navigation(
    [
        st.Page("pages/overview.py", title="Overview", icon="📊", default=True),
        st.Page("pages/companies.py", title="Companies", icon="🏢"),
        st.Page("pages/company_detail.py", title="Company Detail", icon="🔍"),
        st.Page("pages/funding.py", title="Funding", icon="💰"),
        st.Page("pages/scores.py", title="Scores", icon="⭐"),
        st.Page("pages/network.py", title="Network", icon="🕸️"),
        st.Page("pages/investors.py", title="Investors", icon="🏦"),
    ]
)

# Render navbar with active page detection
# Map page title to navbar key
page_key_map = {
    "Overview": "overview",
    "Companies": "companies",
    "Company Detail": "companies",
    "Funding": "funding",
    "Scores": "scores",
    "Network": "network",
    "Investors": "investors",
}
active = page_key_map.get(pages.title, "overview")
render_navbar(active)

pages.run()
