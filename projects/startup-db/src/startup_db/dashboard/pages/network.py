"""Network — company relationship graph visualization."""

from __future__ import annotations

import streamlit as st
from streamlit_agraph import Config, Edge, Node, agraph

from startup_db.dashboard.components import is_dark_mode
from startup_db.dashboard.data import (
    cached_all_companies_slim,
    get_repo,
)

dark = is_dark_mode()
st.title("Relationship Network")

# ── Controls ─────────────────────────────────────────────────
all_companies = cached_all_companies_slim()

RELATION_COLORS = {
    "competitor": "#EF5350",
    "partner": "#66BB6A",
    "customer": "#42A5F5",
    "supplier": "#FFA726",
}

with st.sidebar:
    st.header("Graph Settings")
    sub_categories = sorted(
        {c.get("sub_category", "") for c in all_companies if c.get("sub_category")}
    )
    selected_sub = st.selectbox("Sub-category", ["Select..."] + sub_categories)

    max_nodes = st.slider("Max nodes", 10, 200, 50)

    # Relation type filter
    relation_types = list(RELATION_COLORS.keys())
    selected_relations = st.multiselect(
        "Relation types",
        relation_types,
        default=relation_types,
    )

    show_labels = st.checkbox("Show node labels", value=True)
    physics = st.checkbox("Physics simulation", value=True)

if selected_sub == "Select...":
    st.info("Select a sub-category from the sidebar to visualize its relationship network.")
    st.stop()

# ── Fetch companies in selected sub_category ─────────────────
sub_companies = [c for c in all_companies if c.get("sub_category") == selected_sub][:max_nodes]
if not sub_companies:
    st.warning("No companies in this sub-category.")
    st.stop()

company_ids = {c["id"] for c in sub_companies}
id_to_company = {c["id"]: c for c in sub_companies}

# ── Fetch relations ──────────────────────────────────────────
client = get_repo()._client
all_relations = []
id_list = list(company_ids)

# Batch fetch in chunks of 50 (PostgREST limit)
for i in range(0, len(id_list), 50):
    chunk = id_list[i : i + 50]
    result = (
        client.table("su_company_relations")
        .select("company_id,related_company_id,relation_type")
        .in_("company_id", chunk)
        .execute()
    )
    all_relations.extend(result.data or [])

# Filter to edges where both ends are in our set + selected relation types
edges_data = [
    r
    for r in all_relations
    if r["related_company_id"] in company_ids
    and r.get("relation_type", "competitor") in selected_relations
]

# ── Header with selected category ────────────────────────────
st.subheader(f"📂 {selected_sub}")
st.caption(f"{len(sub_companies)} companies · {len(edges_data)} relations")

# ── Compute node degrees ─────────────────────────────────────
degree: dict[str, int] = {}
seen_edges = set()
for r in edges_data:
    edge_key = tuple(sorted([r["company_id"], r["related_company_id"]]))
    if edge_key in seen_edges:
        continue
    seen_edges.add(edge_key)
    degree[r["company_id"]] = degree.get(r["company_id"], 0) + 1
    degree[r["related_company_id"]] = degree.get(r["related_company_id"], 0) + 1

# Auto-hide labels when graph is dense
labels_on = (
    show_labels
    if len(sub_companies) < 30
    else st.sidebar.checkbox(
        "Force labels (30+ nodes)",
        value=False,
    )
    if show_labels
    else False
)

# ── Build graph ──────────────────────────────────────────────
STATUS_COLORS = {
    "active": "#4CAF50",
    "acquired": "#FF9800",
    "ipo": "#2196F3",
    "defunct": "#9E9E9E",
    "unknown": "#B0BEC5",
}

nodes = []
for c in sub_companies:
    color = STATUS_COLORS.get(c.get("status", "unknown"), "#B0BEC5")
    deg = degree.get(c["id"], 0)
    node_size = max(10, min(40, 10 + deg * 3))
    nodes.append(
        Node(
            id=c["id"],
            label=c["name"] if labels_on else "",
            title=(
                f"{c['name']}\n{c.get('country', '')}"
                f"\nStatus: {c.get('status', '')}\nConnections: {deg}"
            ),
            size=node_size,
            color=color,
        )
    )

edges = []
seen = set()
for r in edges_data:
    edge_key = tuple(sorted([r["company_id"], r["related_company_id"]]))
    if edge_key in seen:
        continue
    seen.add(edge_key)
    rtype = r.get("relation_type", "competitor")
    src_name = id_to_company.get(r["company_id"], {}).get("name", "")
    tgt_name = id_to_company.get(r["related_company_id"], {}).get("name", "")
    edges.append(
        Edge(
            source=r["company_id"],
            target=r["related_company_id"],
            color=RELATION_COLORS.get(rtype, "#BDBDBD"),
            label="",
            title=f"{src_name} ↔ {tgt_name}\nType: {rtype}",
        )
    )

config = Config(
    width=1200,
    height=700,
    directed=False,
    physics=physics,
    hierarchical=False,
    nodeHighlightBehavior=True,
    highlightColor="#F7DC6F",
)

agraph(nodes=nodes, edges=edges, config=config)

# ── Legend ────────────────────────────────────────────────────
st.divider()

# Node status legend
st.markdown("**Node — Status**")
status_cols = st.columns(len(STATUS_COLORS))
for col, (status, color) in zip(status_cols, STATUS_COLORS.items()):
    col.markdown(f"<span style='color:{color}'>●</span> {status}", unsafe_allow_html=True)

# Edge relation type legend
st.markdown("**Edge — Relation Type**")
rel_cols = st.columns(len(RELATION_COLORS))
for col, (rtype, color) in zip(rel_cols, RELATION_COLORS.items()):
    col.markdown(f"<span style='color:{color}'>━</span> {rtype}", unsafe_allow_html=True)
