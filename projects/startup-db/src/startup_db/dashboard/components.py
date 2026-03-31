"""Shared UI components — top navbar and sidebar setup."""

from __future__ import annotations

import json
from pathlib import Path

import streamlit as st

# Page definitions: (key, label, icon, url_path)
# URL paths match what st.navigation generates from page file names.
PAGES = [
    ("overview", "Overview", "📊", "/"),
    ("companies", "Companies", "🏢", "/companies"),
    ("funding", "Funding", "💰", "/funding"),
    ("momentum", "Momentum", "🔥", "/momentum"),
    ("scores", "Scores", "⭐", "/scores"),
    ("network", "Network", "🕸️", "/network"),
    ("investors", "Investors", "🏦", "/investors"),
    ("intel", "Intel", "📡", "/intel"),
]

_THEME_FILE = Path(__file__).parent / ".theme_pref.json"


def _save_theme(dark: bool) -> None:
    """Persist dark mode preference to disk."""
    try:
        _THEME_FILE.write_text(json.dumps({"dark_mode": dark}))
    except OSError:
        pass


def _load_theme() -> bool:
    """Load dark mode preference from disk."""
    if _THEME_FILE.exists():
        try:
            return json.loads(_THEME_FILE.read_text()).get("dark_mode", False)
        except (json.JSONDecodeError, OSError):
            return False
    return False


def is_dark_mode() -> bool:
    """Return True if dark mode is enabled."""
    return st.session_state.get("dark_mode", False)


def render_sidebar_header() -> None:
    """Render common sidebar header and handle theme toggle."""
    # Initialize from disk if not in session state
    if "dark_mode" not in st.session_state:
        st.session_state["dark_mode"] = _load_theme()

    # Handle theme toggle via query param — read only, no delete/rerun
    # (modifying query_params triggers rerun and resets navigation)
    if "theme" in st.query_params:
        requested = st.query_params["theme"] == "dark"
        if st.session_state.get("dark_mode") != requested:
            st.session_state["dark_mode"] = requested
            _save_theme(requested)

    with st.sidebar:
        st.markdown(
            '<div style="text-align:center; padding: 8px 0 16px 0;">'
            '<span style="font-size:2rem;">🚀</span><br>'
            '<span style="color:white !important; font-size:1.1rem; font-weight:700;">'
            "Startup DB</span></div>",
            unsafe_allow_html=True,
        )
        st.divider()


def render_navbar(active: str) -> None:
    """Render a fixed top navigation bar with theme toggle.

    Args:
        active: Key of the currently active page (e.g. "overview", "companies").
    """
    links = []
    for key, label, icon, path in PAGES:
        cls = "nav-link active" if key == active else "nav-link"
        links.append(
            f'<a href="{path}" target="_self" class="{cls}">'
            f"{icon} {label}</a>"
        )
    links_html = "".join(links)

    dark = is_dark_mode()
    toggle_icon = "☀️" if dark else "🌙"
    toggle_target = "light" if dark else "dark"

    # Find current page path to stay on the same page after toggle
    current_path = "/"
    for key, _label, _icon, path in PAGES:
        if key == active:
            current_path = path
            break
    toggle_href = f"{current_path}?theme={toggle_target}"

    html = (
        '<div class="top-navbar">'
        '<div class="nav-brand">🚀 Startup DB</div>'
        '<div class="nav-links">'
        f"{links_html}"
        f'<a href="{toggle_href}" target="_self" '
        f'class="nav-link nav-theme-toggle">{toggle_icon}</a>'
        "</div>"
        "</div>"
    )
    st.markdown(html, unsafe_allow_html=True)
