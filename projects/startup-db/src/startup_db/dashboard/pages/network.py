"""Network — interactive company relationship graph (vis.js)."""

from __future__ import annotations

import json

import streamlit as st
import streamlit.components.v1 as components

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

STATUS_COLORS = {
    "active": "#4CAF50",
    "acquired": "#FF9800",
    "ipo": "#2196F3",
    "defunct": "#9E9E9E",
    "unknown": "#B0BEC5",
}

with st.sidebar:
    st.header("Graph Settings")
    sub_categories = sorted(
        {c.get("sub_category", "") for c in all_companies if c.get("sub_category")}
    )
    selected_sub = st.selectbox(
        "Sub-category",
        sub_categories if sub_categories else ["(none)"],
    )

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
    graph_height = st.slider("Graph height (px)", 400, 1000, 700, step=50)

if not sub_categories or selected_sub == "(none)":
    st.info("No sub-categories available.")
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
all_relations: list[dict] = []
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

# ── Header ───────────────────────────────────────────────────
st.subheader(f"📂 {selected_sub}")
st.caption(f"{len(sub_companies)} companies · {len(edges_data)} relations")

# ── Compute node degrees ─────────────────────────────────────
degree: dict[str, int] = {}
seen_edges: set[tuple[str, str]] = set()
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
    else st.sidebar.checkbox("Force labels (30+ nodes)", value=False)
    if show_labels
    else False
)

# ── Build vis.js data ────────────────────────────────────────
vis_nodes = []
for c in sub_companies:
    color = STATUS_COLORS.get(c.get("status", "unknown"), "#B0BEC5")
    deg = degree.get(c["id"], 0)
    node_size = max(12, min(45, 12 + deg * 4))
    vis_nodes.append(
        {
            "id": c["id"],
            "label": c["name"] if labels_on else "",
            "title": (
                f"<b>{c['name']}</b><br>"
                f"{c.get('country', '')}<br>"
                f"Status: {c.get('status', '')}<br>"
                f"Connections: {deg}"
            ),
            "size": node_size,
            "color": {
                "background": color,
                "border": color,
                "highlight": {"background": "#F7DC6F", "border": "#F1C40F"},
            },
            "font": {
                "color": "#E0E0E0" if dark else "#333333",
                "size": 11,
                "face": "Inter, -apple-system, sans-serif",
            },
            "_name": c["name"],
        }
    )

vis_edges = []
seen = set()
for r in edges_data:
    edge_key = tuple(sorted([r["company_id"], r["related_company_id"]]))
    if edge_key in seen:
        continue
    seen.add(edge_key)
    rtype = r.get("relation_type", "competitor")
    src_name = id_to_company.get(r["company_id"], {}).get("name", "")
    tgt_name = id_to_company.get(r["related_company_id"], {}).get("name", "")
    vis_edges.append(
        {
            "from": r["company_id"],
            "to": r["related_company_id"],
            "color": {"color": RELATION_COLORS.get(rtype, "#BDBDBD"), "opacity": 0.6},
            "title": f"{src_name} ↔ {tgt_name}<br>Type: {rtype}",
            "smooth": {"type": "continuous"},
        }
    )

# ── Render vis.js graph ──────────────────────────────────────
nodes_json = json.dumps(vis_nodes, ensure_ascii=False)
edges_json = json.dumps(vis_edges, ensure_ascii=False)
bg_color = "#0E1117" if dark else "#FFFFFF"
text_color = "#E0E0E0" if dark else "#333333"
physics_enabled = "true" if physics else "false"

html = f"""
<!DOCTYPE html>
<html>
<head>
<script src="https://unpkg.com/vis-network@9.1.6/standalone/umd/vis-network.min.js"></script>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: {bg_color}; overflow: hidden; }}
  #graph {{
    width: 100%;
    height: {graph_height}px;
    background: {bg_color};
    border: 1px solid {"#2A2A2A" if dark else "#E0E0E0"};
    border-radius: 8px;
  }}
  #controls {{
    position: absolute;
    bottom: 12px;
    right: 12px;
    display: flex;
    flex-direction: column;
    gap: 4px;
    z-index: 10;
  }}
  #controls button {{
    width: 32px;
    height: 32px;
    border: 1px solid {"#444" if dark else "#CCC"};
    border-radius: 6px;
    background: {"#1E1E1E" if dark else "#F5F5F5"};
    color: {text_color};
    font-size: 16px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.15s;
  }}
  #controls button:hover {{
    background: {"#333" if dark else "#E0E0E0"};
  }}
  #info {{
    position: absolute;
    top: 12px;
    left: 12px;
    padding: 8px 14px;
    border-radius: 6px;
    background: {"rgba(30,30,30,0.85)" if dark else "rgba(255,255,255,0.9)"};
    color: {text_color};
    font: 12px Inter, -apple-system, sans-serif;
    z-index: 10;
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.2s;
    max-width: 260px;
    border: 1px solid {"#333" if dark else "#DDD"};
    backdrop-filter: blur(8px);
  }}
  #info.visible {{ opacity: 1; }}
</style>
</head>
<body>
<div id="graph"></div>
<div id="controls">
  <button onclick="zoomIn()" title="Zoom in">+</button>
  <button onclick="zoomOut()" title="Zoom out">−</button>
  <button onclick="fitAll()" title="Fit all">⊙</button>
</div>
<div id="info"></div>

<script>
var nodesData = {nodes_json};
var edgesData = {edges_json};

var nodes = new vis.DataSet(nodesData);
var edges = new vis.DataSet(edgesData);

var container = document.getElementById("graph");
var data = {{ nodes: nodes, edges: edges }};

var options = {{
  physics: {{
    enabled: {physics_enabled},
    solver: "forceAtlas2Based",
    forceAtlas2Based: {{
      gravitationalConstant: -80,
      centralGravity: 0.008,
      springLength: 160,
      springConstant: 0.02,
      damping: 0.4,
      avoidOverlap: 0.3
    }},
    stabilization: {{
      enabled: true,
      iterations: 200,
      updateInterval: 25
    }},
    maxVelocity: 40,
    minVelocity: 0.5
  }},
  interaction: {{
    hover: true,
    tooltipDelay: 150,
    zoomView: true,
    dragView: true,
    dragNodes: true,
    multiselect: false,
    navigationButtons: false,
    zoomSpeed: 0.3,
    keyboard: {{
      enabled: true,
      speed: {{ x: 10, y: 10, zoom: 0.02 }}
    }}
  }},
  nodes: {{
    shape: "dot",
    borderWidth: 2,
    shadow: {{
      enabled: true,
      color: "rgba(0,0,0,0.15)",
      size: 6,
      x: 2,
      y: 2
    }},
    scaling: {{
      label: {{ enabled: true, min: 9, max: 14 }}
    }}
  }},
  edges: {{
    width: 1.5,
    selectionWidth: 2.5,
    smooth: {{
      enabled: true,
      type: "continuous",
      roundness: 0.5
    }}
  }}
}};

var network = new vis.Network(container, data, options);

// ── Zoom controls ──
function zoomIn() {{
  var scale = network.getScale();
  network.moveTo({{ scale: scale * 1.3, animation: {{ duration: 300, easingFunction: "easeInOutQuad" }} }});
}}

function zoomOut() {{
  var scale = network.getScale();
  network.moveTo({{ scale: scale / 1.3, animation: {{ duration: 300, easingFunction: "easeInOutQuad" }} }});
}}

function fitAll() {{
  network.fit({{ animation: {{ duration: 500, easingFunction: "easeInOutQuad" }} }});
}}

// ── Obsidian-like focus: click node → highlight neighbors, fade rest ──
var allNodeIds = nodes.getIds();
var highlightActive = false;

network.on("click", function(params) {{
  var info = document.getElementById("info");

  if (params.nodes.length > 0) {{
    var nodeId = params.nodes[0];
    var connectedNodes = network.getConnectedNodes(nodeId);
    var connectedEdges = network.getConnectedEdges(nodeId);
    var clickedNode = nodes.get(nodeId);

    // Show info panel
    info.innerHTML = "<b>" + (clickedNode._name || clickedNode.label || "") + "</b><br>" +
                     "Connections: " + connectedNodes.length;
    info.classList.add("visible");

    // Highlight: dim all, brighten selected + neighbors
    var updatedNodes = [];
    allNodeIds.forEach(function(id) {{
      var isConnected = connectedNodes.indexOf(id) !== -1;
      var isSelected = id === nodeId;
      if (isSelected) {{
        updatedNodes.push({{ id: id, opacity: 1.0, font: {{ color: "{text_color}", size: 13, bold: true }} }});
      }} else if (isConnected) {{
        updatedNodes.push({{ id: id, opacity: 1.0, font: {{ color: "{text_color}", size: 11 }} }});
      }} else {{
        updatedNodes.push({{ id: id, opacity: 0.12, font: {{ color: "transparent" }} }});
      }}
    }});
    nodes.update(updatedNodes);

    // Dim non-connected edges
    var allEdgeIds = edges.getIds();
    var updatedEdges = [];
    allEdgeIds.forEach(function(eid) {{
      if (connectedEdges.indexOf(eid) !== -1) {{
        updatedEdges.push({{ id: eid, hidden: false }});
      }} else {{
        updatedEdges.push({{ id: eid, hidden: true }});
      }}
    }});
    edges.update(updatedEdges);

    // Zoom to neighborhood
    var focusNodes = [nodeId].concat(connectedNodes);
    network.fit({{
      nodes: focusNodes,
      animation: {{ duration: 500, easingFunction: "easeInOutQuad" }}
    }});

    highlightActive = true;

  }} else {{
    // Click on empty space → reset
    if (highlightActive) {{
      info.classList.remove("visible");
      var resetNodes = [];
      allNodeIds.forEach(function(id) {{
        resetNodes.push({{ id: id, opacity: 1.0, font: {{ color: "{text_color}", size: 11 }} }});
      }});
      nodes.update(resetNodes);

      var allEdgeIds = edges.getIds();
      var resetEdges = [];
      allEdgeIds.forEach(function(eid) {{
        resetEdges.push({{ id: eid, hidden: false }});
      }});
      edges.update(resetEdges);

      network.fit({{ animation: {{ duration: 500, easingFunction: "easeInOutQuad" }} }});
      highlightActive = false;
    }}
  }}
}});

// ── Hover effect ──
network.on("hoverNode", function(params) {{
  container.style.cursor = "pointer";
}});

network.on("blurNode", function(params) {{
  container.style.cursor = "default";
}});

// Initial fit
network.once("stabilizationIterationsDone", function() {{
  network.fit({{ animation: false }});
}});
</script>
</body>
</html>
"""

components.html(html, height=graph_height + 30, scrolling=False)

# ── Legend ────────────────────────────────────────────────────
st.divider()
lc = "#E0E0E0" if dark else "#333333"

# Inject scoped CSS to override theme's !important rules
# CSS-02: <style> 블록 사용, 인라인 style 금지
# CSS-03: color + -webkit-text-fill-color 동기화
all_dot_colors = {**STATUS_COLORS, **RELATION_COLORS}
dot_css = "\n".join(
    f"    .network-legend span.dot-{key} {{"
    f" color: {color} !important;"
    f" -webkit-text-fill-color: {color} !important;"
    f" }}"
    for key, color in all_dot_colors.items()
)
st.markdown(
    f"""<style>
    .network-legend,
    .network-legend span,
    .network-legend b,
    .network-legend p,
    .network-legend div {{
        color: {lc} !important;
        -webkit-text-fill-color: {lc} !important;
    }}
{dot_css}
    [data-testid="stExpander"] .network-legend,
    [data-testid="stExpander"] .network-legend span,
    [data-testid="stExpander"] .network-legend b,
    [data-testid="stExpander"] .network-legend div {{
        color: {lc} !important;
        -webkit-text-fill-color: {lc} !important;
    }}
    </style>""",
    unsafe_allow_html=True,
)

# Node status legend
st.markdown(
    f'<div class="network-legend"><b>Node — Status</b></div>',
    unsafe_allow_html=True,
)
status_cols = st.columns(len(STATUS_COLORS))
for col, (status, _color) in zip(status_cols, STATUS_COLORS.items()):
    col.markdown(
        f'<div class="network-legend">'
        f'<span class="dot-{status}" style="font-size:1.1em">●</span> '
        f"{status}</div>",
        unsafe_allow_html=True,
    )

# Edge relation type legend
st.markdown(
    f'<div class="network-legend"><b>Edge — Relation Type</b></div>',
    unsafe_allow_html=True,
)
rel_cols = st.columns(len(RELATION_COLORS))
for col, (rtype, _color) in zip(rel_cols, RELATION_COLORS.items()):
    col.markdown(
        f'<div class="network-legend">'
        f'<span class="dot-{rtype}" style="font-size:1.1em">━</span> '
        f"{rtype}</div>",
        unsafe_allow_html=True,
    )

# Usage tips
with st.expander("Graph controls"):
    st.markdown(
        f"""<div class="network-legend">
<b>Scroll</b> — Zoom in/out<br>
<b>Drag background</b> — Pan<br>
<b>Drag node</b> — Move node<br>
<b>Click node</b> — Focus on connections<br>
<b>Click empty space</b> — Reset view<br>
<b>+/−/⊙ buttons</b> — Zoom in / Zoom out / Fit all<br>
<b>Arrow keys</b> — Pan (when graph focused)
</div>""",
        unsafe_allow_html=True,
    )
