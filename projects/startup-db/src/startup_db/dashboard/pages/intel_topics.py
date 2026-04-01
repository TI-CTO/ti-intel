"""Intel Store — Topic Explorer page."""

from __future__ import annotations

import html as _html

import pandas as pd
import plotly.express as px
import streamlit as st

from startup_db.dashboard.components import is_dark_mode
from startup_db.dashboard.data import (
    cached_intel_by_topic,
    cached_intel_items_by_topic,
)
from startup_db.dashboard.theme import (
    CHART_COLORS,
    DARK,
    LIGHT,
    PRIMARY,
    _glass_css,
    get_plotly_layout,
    render_plotly_animated,
)

dark = is_dark_mode()
PL = get_plotly_layout(dark)
C = DARK if dark else LIGHT
glass = _glass_css(C)

st.title("Topic Explorer")

# ── Topic distribution ───────────────────────────────────────
topics = cached_intel_by_topic()

if not topics:
    st.info("No topic data available.")
    st.stop()

# ── Chart: items per topic ───────────────────────────────────
topic_df = pd.DataFrame(topics)

fig = px.bar(
    topic_df.head(20),
    x="count",
    y="topic_name",
    orientation="h",
    color_discrete_sequence=[PRIMARY],
    labels={"count": "Items", "topic_name": "Topic"},
)
chart_height = max(350, len(topic_df.head(20)) * 28)
fig.update_layout(
    **{**PL, "margin": {"l": 200, "r": 20, "t": 30, "b": 20}},
    height=chart_height,
    showlegend=False,
    yaxis={"categoryorder": "total ascending"},
)
render_plotly_animated(fig, height=chart_height, dark=dark)

st.divider()

# ── Topic selector ───────────────────────────────────────────
st.subheader("Drill Down")

topic_options = {t["topic_name"]: t["topic_slug"] for t in topics}
selected_name = st.selectbox(
    "Select a topic",
    options=list(topic_options.keys()),
    index=0,
)
selected_slug = topic_options[selected_name]

# ── Items for selected topic ─────────────────────────────────
items = cached_intel_items_by_topic(selected_slug, limit=50)

if not items:
    st.info(f"No items found for '{selected_name}'.")
    st.stop()

# Type filter
all_types = sorted({item["item_type"] for item in items})
type_filter = st.multiselect(
    "Filter by type",
    options=all_types,
    default=all_types,
)
filtered = [item for item in items if item["item_type"] in type_filter]

# Stats row
type_counts = {}
for item in filtered:
    t = item["item_type"]
    type_counts[t] = type_counts.get(t, 0) + 1

cols = st.columns(min(len(type_counts) + 1, 5))
cols[0].metric("Total", len(filtered))
for i, (t, c) in enumerate(sorted(type_counts.items(), key=lambda x: -x[1])):
    if i + 1 < len(cols):
        cols[i + 1].metric(t.title(), c)

# Items table
border = C["glass_border"]
rows_html = []
for item in filtered:
    title = _html.escape(item.get("title", "")[:90])
    itype = _html.escape(item.get("item_type", ""))
    source = _html.escape(item.get("source_name", "")[:25])
    url = item.get("source_url", "")
    date_str = (item.get("collected_date") or "")[:10]

    meta = item.get("metadata", {})
    platform = meta.get("platform", "")
    engagement = meta.get("engagement", 0)

    type_colors = {
        "news": CHART_COLORS[0],
        "paper": CHART_COLORS[1],
        "patent": CHART_COLORS[2],
        "community": CHART_COLORS[3],
    }
    badge_color = type_colors.get(itype, C["text_secondary"])

    title_html = (
        f'<a href="{_html.escape(url)}" target="_blank"'
        f' style="color:{C["text"]};text-decoration:none;">{title}</a>'
        if url
        else title
    )

    engagement_html = ""
    if platform:
        eng_str = f"{engagement:,}" if engagement else ""
        engagement_html = (
            f'<span style="color:{C["text_secondary"]};font-size:0.78rem;">'
            f"{platform} {eng_str}</span>"
        )

    rows_html.append(
        f'<tr style="border-bottom:1px solid {border};">'
        f'<td style="padding:8px;font-size:0.85rem;">{title_html}</td>'
        f'<td style="padding:8px;text-align:center;">'
        f'<span style="background:{badge_color};color:#fff;'
        f'padding:2px 8px;border-radius:10px;font-size:0.72rem;'
        f'font-weight:600;">{itype}</span></td>'
        f'<td style="padding:8px;color:{C["text_secondary"]};'
        f'font-size:0.82rem;">{source}</td>'
        f'<td style="padding:8px;">{engagement_html}</td>'
        f'<td style="padding:8px;color:{C["text_secondary"]};'
        f'font-size:0.82rem;">{date_str}</td>'
        f"</tr>"
    )

st.markdown(
    f'<table style="width:100%;border-collapse:collapse;">'
    f'<thead><tr style="border-bottom:2px solid {border};">'
    f'<th style="text-align:left;padding:8px;color:{C["text_secondary"]};'
    f'font-size:0.75rem;text-transform:uppercase;">Title</th>'
    f'<th style="text-align:center;padding:8px;color:{C["text_secondary"]};'
    f'font-size:0.75rem;text-transform:uppercase;">Type</th>'
    f'<th style="text-align:left;padding:8px;color:{C["text_secondary"]};'
    f'font-size:0.75rem;text-transform:uppercase;">Source</th>'
    f'<th style="text-align:left;padding:8px;color:{C["text_secondary"]};'
    f'font-size:0.75rem;text-transform:uppercase;">Engagement</th>'
    f'<th style="text-align:left;padding:8px;color:{C["text_secondary"]};'
    f'font-size:0.75rem;text-transform:uppercase;">Date</th>'
    f"</tr></thead>"
    f'<tbody>{"".join(rows_html)}</tbody></table>',
    unsafe_allow_html=True,
)
