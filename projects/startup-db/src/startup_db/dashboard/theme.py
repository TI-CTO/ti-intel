"""Dashboard theme — glassmorphism / dark glassmorphism."""

from __future__ import annotations

# ── Signature color ─────────────────────────────────────────
PRIMARY = "#C50063"
PRIMARY_DARK = "#8B0042"
PRIMARY_LIGHT = "#FFE5F0"
PRIMARY_GRADIENT = f"linear-gradient(135deg, {PRIMARY} 0%, {PRIMARY_DARK} 100%)"

# ── Light Glassmorphism palette (Soft Sand) ─────────────────
LIGHT = {
    "bg": "linear-gradient(135deg, #f5f0e8 0%, #e8d5c4 50%, #f0dbd8 100%)",
    "bg_solid": "#F5F0E8",  # fallback for elements that need a solid color
    "card": "rgba(255, 255, 255, 0.5)",
    "card_solid": "#FFFFFF",
    "glass_border": "rgba(255, 255, 255, 0.65)",
    "glass_blur": "16px",
    "glass_shadow": "0 8px 32px rgba(90, 60, 50, 0.08)",
    "sidebar_bg": "linear-gradient(180deg, rgba(197,0,99,0.85) 0%, rgba(64,43,58,0.92) 100%)",
    "sidebar_text": "rgba(255,255,255,0.75)",
    "sidebar_active": "#FFFFFF",
    "primary": PRIMARY,
    "primary_light": "rgba(197,0,99,0.08)",
    "secondary": "#D63484",
    "success": "#10B981",
    "warning": "#F59E0B",
    "danger": "#EF4444",
    "text": "#3D2B1F",
    "text_secondary": "#7A6558",
    "border": "rgba(255, 255, 255, 0.55)",
    "shadow": "rgba(90, 60, 50, 0.08)",
    "input_bg": "rgba(255, 255, 255, 0.4)",
}

# ── Dark Glassmorphism palette ──────────────────────────────
DARK = {
    "bg": "linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%)",
    "bg_solid": "#13111C",
    "card": "rgba(255, 255, 255, 0.06)",
    "card_solid": "#1E1B2E",
    "glass_border": "rgba(255, 255, 255, 0.12)",
    "glass_blur": "20px",
    "glass_shadow": "0 8px 32px rgba(0, 0, 0, 0.35)",
    "sidebar_bg": "linear-gradient(180deg, rgba(15,12,41,0.95) 0%, rgba(59,28,50,0.9) 100%)",
    "sidebar_text": "rgba(255,255,255,0.6)",
    "sidebar_active": "#FFFFFF",
    "primary": PRIMARY,
    "primary_light": "rgba(197,0,99,0.15)",
    "secondary": "#A64D79",
    "success": "#10B981",
    "warning": "#F59E0B",
    "danger": "#EF4444",
    "text": "#E8E0F0",
    "text_secondary": "#A89BBF",
    "border": "rgba(255, 255, 255, 0.1)",
    "shadow": "rgba(0, 0, 0, 0.4)",
    "input_bg": "rgba(255, 255, 255, 0.07)",
}

# Active palette (set by inject_css)
COLORS = LIGHT.copy()

# Chart color sequence
CHART_COLORS = [
    "#C50063",
    "#D63484",
    "#A64D79",
    "#FF9BD2",
    "#10B981",
    "#F59E0B",
    "#06B6D4",
    "#8B5CF6",
    "#E8337F",
    "#14B8A6",
    "#34D399",
    "#FBBF24",
    "#A78BFA",
    "#F472B6",
    "#22D3EE",
]

PLOTLY_LAYOUT = dict(
    font_family="Inter, -apple-system, sans-serif",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=20, r=20, t=30, b=20),
    colorway=CHART_COLORS,
)


def get_plotly_layout(dark: bool = False) -> dict:
    """Return Plotly layout dict with correct font color for current mode."""
    c = DARK if dark else LIGHT
    grid_color = "rgba(255,255,255,0.08)" if dark else "rgba(0,0,0,0.06)"
    return {
        **PLOTLY_LAYOUT,
        "font_color": c["text"],
        "legend_font_color": c["text"],
        "xaxis_tickfont_color": c["text"],
        "xaxis_gridcolor": grid_color,
        "yaxis_tickfont_color": c["text"],
        "yaxis_gridcolor": grid_color,
        "transition": {"duration": 500, "easing": "cubic-in-out"},
    }


def _glass_css(c: dict) -> str:
    """Return reusable glass panel CSS properties."""
    return (
        f"background: {c['card']}; "
        f"backdrop-filter: blur({c['glass_blur']}); "
        f"-webkit-backdrop-filter: blur({c['glass_blur']}); "
        f"border: 1px solid {c['glass_border']}; "
        f"box-shadow: {c['glass_shadow']}; "
    )


def render_styled_dataframe(
    df: "pd.DataFrame", dark: bool = False, link_columns: list[str] | None = None
) -> str:
    """Return HTML table styled for current theme.

    Args:
        df: DataFrame to render.
        dark: If True, use dark mode colors.
        link_columns: Column names to render as clickable links.
    """
    c = DARK if dark else LIGHT
    link_columns = link_columns or []

    header_bg = "rgba(255,255,255,0.08)" if dark else "rgba(255,255,255,0.5)"
    row_bg = "rgba(255,255,255,0.03)" if dark else "rgba(255,255,255,0.35)"
    row_alt_bg = "rgba(255,255,255,0.07)" if dark else "rgba(255,255,255,0.55)"
    hover_bg = "rgba(197,0,99,0.12)" if dark else "rgba(197,0,99,0.08)"
    border = c["glass_border"]
    text = c["text"]
    text_sec = c["text_secondary"]

    style = (
        f"<style>"
        f".styled-table {{ width:100%; border-collapse:collapse; border-radius:16px; overflow:hidden; "
        f"border:1px solid {border}; font-size:0.88rem; font-family:Inter,-apple-system,sans-serif; "
        f"backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px); }}"
        f".styled-table th {{ background:{header_bg}; color:{text_sec}; font-weight:600; "
        f"text-transform:uppercase; font-size:0.75rem; letter-spacing:0.04em; "
        f"padding:12px 16px; text-align:left; border-bottom:1px solid {border}; }}"
        f".styled-table td {{ padding:10px 16px; color:{text}; border-bottom:1px solid {border}; }}"
        f".styled-table tr:nth-child(even) td {{ background:{row_alt_bg}; }}"
        f".styled-table tr:nth-child(odd) td {{ background:{row_bg}; }}"
        f".styled-table tr:hover td {{ background:{hover_bg}; }}"
        f".styled-table a {{ color:{PRIMARY}; text-decoration:none; }}"
        f".styled-table a:hover {{ text-decoration:underline; }}"
        f"</style>"
    )

    rows = []
    headers = "".join(f"<th>{col}</th>" for col in df.columns)
    for _, row in df.iterrows():
        cells = []
        for col in df.columns:
            val = row[col]
            if col in link_columns and val and str(val) not in ("None", "nan", ""):
                cells.append(f'<td><a href="{val}" target="_blank">Link</a></td>')
            else:
                display_val = "" if str(val) in ("None", "nan") else str(val)
                cells.append(f"<td>{display_val}</td>")
        rows.append(f"<tr>{''.join(cells)}</tr>")

    return f"{style}<table class='styled-table'><thead><tr>{headers}</tr></thead><tbody>{''.join(rows)}</tbody></table>"


STATUS_BADGE_COLORS = {
    "active": ("#10B981", "rgba(16,185,129,0.15)"),
    "acquired": ("#F59E0B", "rgba(245,158,11,0.15)"),
    "ipo": ("#3B82F6", "rgba(59,130,246,0.15)"),
    "defunct": ("#6B7280", "rgba(107,114,128,0.15)"),
}

STATUS_BADGE_COLORS_DARK = {
    "active": ("#34D399", "rgba(16,185,129,0.2)"),
    "acquired": ("#FBBF24", "rgba(245,158,11,0.2)"),
    "ipo": ("#60A5FA", "rgba(59,130,246,0.2)"),
    "defunct": ("#9CA3AF", "rgba(107,114,128,0.2)"),
}


def render_company_cards(
    companies: list[dict],
    dark: bool = False,
    detail_path: str = "/company_detail",
) -> str:
    """Return HTML grid of uniform-height clickable company cards.

    Args:
        companies: List of company dicts with name, main_category, etc.
        dark: If True, use dark mode colors.
        detail_path: URL path for company detail page.
    """
    import html as _html

    c = DARK if dark else LIGHT
    badge_colors = STATUS_BADGE_COLORS_DARK if dark else STATUS_BADGE_COLORS

    card_bg = c["card"]
    border = c["glass_border"]
    blur = c["glass_blur"]
    shadow = c["glass_shadow"]
    text = c["text"]
    text2 = c["text_secondary"]
    input_bg = c["input_bg"]

    style = (
        "<style>"
        ".cc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;}"
        f".cc-card{{background:{card_bg};backdrop-filter:blur({blur});-webkit-backdrop-filter:blur({blur});"
        f"border:1px solid {border};box-shadow:{shadow};"
        "border-radius:14px;padding:18px 20px;height:160px;"
        "display:flex;flex-direction:column;justify-content:space-between;"
        "text-decoration:none;cursor:pointer;"
        f"transition:transform 0.25s ease,box-shadow 0.25s ease,border-color 0.25s ease;}}"
        f".cc-card:hover{{transform:translateY(-4px);box-shadow:0 12px 32px {c['shadow']},0 0 0 1px {PRIMARY}40;"
        f"border-color:{PRIMARY};}}"
        f".cc-name{{font-size:0.95rem;font-weight:600;color:{text};white-space:nowrap;"
        "overflow:hidden;text-overflow:ellipsis;}}"
        f".cc-cat{{font-size:0.78rem;color:{text2};margin-top:4px;"
        "white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}}"
        ".cc-badges{display:flex;gap:6px;margin-top:auto;padding-top:10px;flex-wrap:wrap;}"
        f".cc-badge{{font-size:0.68rem;padding:2px 8px;border-radius:8px;font-weight:500;}}"
        f".cc-tech{{font-size:0.73rem;color:{text2};margin-top:8px;"
        "display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;}}"
        "</style>"
    )

    def _safe(val: object) -> str:
        s = str(val) if val else ""
        return "" if s in ("None", "nan") else _html.escape(s)

    cards = []
    for comp in companies:
        name = _safe(comp.get("name", ""))
        slug = _safe(comp.get("slug", ""))
        cat = _safe(comp.get("main_category", ""))
        sub = _safe(comp.get("sub_category", ""))
        country = _safe(comp.get("country", ""))
        status = _safe(comp.get("status", "unknown")) or "unknown"
        tech = _safe(comp.get("technology", ""))

        fg, bg = badge_colors.get(status, ("#6B7280", "rgba(107,114,128,0.15)"))
        status_badge = f'<span class="cc-badge" style="color:{fg};background:{bg};">{status}</span>'
        country_badge = (
            f'<span class="cc-badge" style="color:{text2};background:{input_bg};">{country}</span>'
            if country else ""
        )

        cat_label = f"{cat} / {sub}" if sub else cat
        tech_html = f'<div class="cc-tech">{tech[:100]}</div>' if tech else ""
        href = f"{detail_path}?slug={slug}"

        cards.append(
            f'<a class="cc-card" href="{href}" target="_self">'
            "<div>"
            f'<div class="cc-name">{name}</div>'
            f'<div class="cc-cat">{cat_label}</div>'
            f"{tech_html}"
            "</div>"
            f'<div class="cc-badges">{status_badge}{country_badge}</div>'
            "</a>"
        )

    return f'{style}<div class="cc-grid">{"".join(cards)}</div>'


def inject_css(dark: bool = False) -> str:
    """Return custom CSS for the dashboard.

    Args:
        dark: If True, apply dark mode colors.
    """
    c = DARK if dark else LIGHT
    # Update module-level COLORS for external use
    COLORS.update(c)

    glass = _glass_css(c)
    sidebar_bg_css = c["sidebar_bg"]

    css = f"""
<style>
    /* ── Import font ──────────────────────────────────── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* ── Root overrides — gradient background ──────────── */
    .stApp {{
        background: {c["bg"]} !important;
        background-attachment: fixed !important;
        font-family: 'Inter', -apple-system, sans-serif;
        min-height: 100vh;
    }}

    /* ── Global text color (main area only, NOT sidebar) ── */
    .stApp h1, .stApp h2, .stApp h3, .stApp h4,
    .main h1, .main h2, .main h3, .main h4,
    [data-testid="stAppViewBlockContainer"] h1,
    [data-testid="stAppViewBlockContainer"] h2,
    [data-testid="stAppViewBlockContainer"] h3 {{
        color: {c["text"]} !important;
    }}
    .main p, .main span, .main label, .main li,
    .main .stMarkdown, .main .stMarkdown p, .main .stMarkdown span,
    [data-testid="stAppViewBlockContainer"] p,
    [data-testid="stAppViewBlockContainer"] span,
    [data-testid="stAppViewBlockContainer"] label {{
        color: {c["text"]} !important;
    }}
    /* Ensure sidebar text is NOT overridden by stApp rules */
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {{
        color: {c["sidebar_active"]} !important;
    }}
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label {{
        color: {c["sidebar_text"]} !important;
    }}
    /* Caption — secondary color */
    .stApp [data-testid="stCaptionContainer"],
    .stApp [data-testid="stCaptionContainer"] * {{
        color: {c["text_secondary"]} !important;
    }}

    /* ── Sidebar — frosted glass ─────────────────────── */
    section[data-testid="stSidebar"] {{
        background: {sidebar_bg_css};
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border-right: 1px solid {c["glass_border"]};
    }}
    section[data-testid="stSidebar"] * {{
        color: {c["sidebar_text"]} !important;
    }}
    section[data-testid="stSidebar"] .stSelectbox label,
    section[data-testid="stSidebar"] .stTextInput label,
    section[data-testid="stSidebar"] .stSlider label,
    section[data-testid="stSidebar"] .stMultiSelect label,
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {{
        color: {c["sidebar_active"]} !important;
    }}
    section[data-testid="stSidebar"] .stSelectbox > div > div,
    section[data-testid="stSidebar"] .stMultiSelect > div > div {{
        background: rgba(255,255,255,0.1) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        border-color: rgba(255,255,255,0.2) !important;
        color: white !important;
        border-radius: 12px !important;
    }}
    /* Selectbox selected value text */
    section[data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] span,
    section[data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] div {{
        color: white !important;
    }}
    /* Selectbox dropdown arrow */
    section[data-testid="stSidebar"] .stSelectbox svg,
    section[data-testid="stSidebar"] .stMultiSelect svg {{
        fill: white !important;
        color: white !important;
    }}
    section[data-testid="stSidebar"] input {{
        background: rgba(255,255,255,0.1) !important;
        backdrop-filter: blur(8px) !important;
        border-color: rgba(255,255,255,0.2) !important;
        color: white !important;
        border-radius: 12px !important;
    }}
    /* Hide sidebar page navigation (already in top navbar) */
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"],
    section[data-testid="stSidebar"] nav {{
        display: none !important;
    }}
    /* Sidebar toggle button */
    button[data-testid="stSidebarCollapsedControl"] {{
        color: {c["text"]} !important;
    }}

    /* ── Main heading ─────────────────────────────────── */
    h1 {{
        font-weight: 700 !important;
        font-size: 1.75rem !important;
        letter-spacing: -0.02em;
    }}
    h2 {{
        font-weight: 600 !important;
        font-size: 1.15rem !important;
    }}

    /* ── Metric cards — glass panels ─────────────────── */
    [data-testid="stMetric"] {{
        {glass}
        border-radius: 16px;
        padding: 20px 24px;
        border-top: 3px solid transparent;
        border-image: {PRIMARY_GRADIENT} 1;
        border-image-slice: 1;
    }}
    [data-testid="stMetricLabel"] {{
        color: {c["text_secondary"]} !important;
        font-size: 0.82rem !important;
        font-weight: 500 !important;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }}
    [data-testid="stMetricValue"] {{
        color: {c["text"]} !important;
        font-size: 1.6rem !important;
        font-weight: 700 !important;
    }}

    /* ── Cards / containers — glass panels ────────────── */
    [data-testid="stVerticalBlock"] > div:has(> [data-testid="stPlotlyChart"]),
    [data-testid="stVerticalBlock"] > div:has(> [data-testid="stDataFrame"]) {{
        {glass}
        border-radius: 16px;
        padding: 16px;
    }}

    /* ── Dataframe ────────────────────────────────────── */
    .stDataFrame {{
        border-radius: 16px;
        overflow: hidden;
    }}
    .stDataFrame thead th {{
        background: {c["input_bg"]} !important;
        font-weight: 600 !important;
        color: {c["text_secondary"]} !important;
        text-transform: uppercase;
        font-size: 0.75rem !important;
        letter-spacing: 0.04em;
    }}

    /* ── Tabs — underline style ─────────────────────── */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 4px;
        border-bottom: 1px solid {c["glass_border"]};
        background: transparent !important;
    }}
    .stTabs [data-baseweb="tab"] {{
        background: transparent !important;
        border: none !important;
        border-radius: 0 !important;
        padding: 10px 20px;
        font-size: 1.4rem !important;
        font-weight: 500;
        color: {c["text_secondary"]} !important;
        opacity: 0.5;
        border-bottom: 2px solid transparent !important;
        backdrop-filter: none !important;
        -webkit-backdrop-filter: none !important;
        transition: all 0.2s;
    }}
    .stTabs [data-baseweb="tab"]:hover {{
        opacity: 0.8;
        color: {c["text"]} !important;
    }}
    .stTabs [aria-selected="true"] {{
        background: transparent !important;
        border-bottom: 2px solid {PRIMARY} !important;
        opacity: 1;
    }}
    .stTabs [data-baseweb="tab"] p,
    .stTabs [data-baseweb="tab"] span,
    .stTabs [data-baseweb="tab"] div {{
        font-size: 1.4rem !important;
    }}
    .stTabs [aria-selected="true"] * {{
        color: {c["text"]} !important;
        -webkit-text-fill-color: {c["text"]} !important;
        font-weight: 600;
    }}
    .stTabs [data-baseweb="tab-highlight"] {{
        display: none !important;
    }}
    .stTabs [data-baseweb="tab-border"] {{
        display: none !important;
    }}

    /* ── Buttons — glass ─────────────────────────────── */
    .stButton > button {{
        border-radius: 12px;
        font-weight: 500;
        border: 1px solid {c["glass_border"]};
        background: {c["card"]} !important;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        transition: all 0.2s;
        color: {c["text"]} !important;
    }}
    .stButton > button:hover {{
        border-color: {PRIMARY};
        color: {PRIMARY} !important;
        box-shadow: 0 4px 16px rgba(197,0,99,0.15);
    }}

    /* ── Divider ──────────────────────────────────────── */
    hr {{
        border-color: {c["glass_border"]} !important;
        opacity: 0.5;
    }}

    /* ── Selectbox / Input (main area) ────────────────── */
    .main .stSelectbox > div > div,
    .main .stTextInput > div > div > input,
    .main .stMultiSelect > div > div {{
        border-radius: 12px !important;
        border-color: {c["glass_border"]} !important;
        background: {c["input_bg"]} !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        color: {c["text"]} !important;
    }}
    /* Selectbox dropdown arrow (main area) */
    .main .stSelectbox svg {{
        fill: {c["text_secondary"]} !important;
        color: {c["text_secondary"]} !important;
    }}

    /* ── Page links ───────────────────────────────────── */
    a[data-testid="stPageLink-NavLink"] {{
        border-radius: 12px !important;
    }}

    /* ── Top Navbar — glass panel ─────────────────────── */
    .top-navbar {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        {glass}
        border-radius: 16px;
        padding: 10px 28px;
        margin: -1rem -1rem 1.5rem -1rem;
        position: sticky;
        top: 0;
        z-index: 999;
    }}
    .nav-brand {{
        font-size: 1.5rem;
        font-weight: 700;
        background: {PRIMARY_GRADIENT};
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.02em;
        white-space: nowrap;
    }}
    .nav-links {{
        display: flex;
        gap: 4px;
        align-items: center;
        flex-wrap: wrap;
    }}
    .nav-link {{
        padding: 8px 18px;
        border-radius: 12px;
        font-size: 0.88rem;
        font-weight: 500;
        color: {c["text_secondary"]} !important;
        text-decoration: none !important;
        transition: all 0.2s;
        white-space: nowrap;
    }}
    .nav-link:hover {{
        background: {c["input_bg"]};
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        color: {c["text"]} !important;
    }}
    .nav-link.active {{
        background: {PRIMARY_GRADIENT};
        color: white !important;
        font-weight: 600;
        box-shadow: 0 2px 12px rgba(197,0,99,0.25);
    }}
    /* Theme toggle inside navbar */
    .nav-theme-toggle {{
        font-size: 1.15rem !important;
        padding: 6px 12px !important;
        margin-left: 8px;
        border-left: 1px solid {c["glass_border"]};
        cursor: pointer;
    }}
    .nav-theme-toggle:hover {{
        background: {c["input_bg"]} !important;
    }}

    /* ── Info / Warning / Error alerts ────────────────── */
    .stAlert {{
        border-radius: 16px;
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
    }}

    /* ── Hide default Streamlit branding ──────────────── */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}

    /* ══ ANIMATIONS ═══════════════════════════════════ */

    /* ── Keyframes ────────────────────────────────── */
    @keyframes fadeSlideUp {{
        from {{ opacity: 0; transform: translateY(16px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}
    @keyframes growWidth {{
        from {{ transform: scaleX(0); }}
        to {{ transform: scaleX(1); }}
    }}

    /* ── Page load — content fade-in + slide-up ───── */
    .main .block-container {{
        animation: fadeSlideUp 0.45s ease-out;
    }}

    /* ── KPI metric stagger reveal ────────────────── */
    [data-testid="stMetric"] {{
        animation: fadeSlideUp 0.5s ease-out both;
        transition: transform 0.25s ease, box-shadow 0.25s ease,
                    border-color 0.25s ease;
        cursor: default;
    }}
    [data-testid="column"]:nth-child(1) [data-testid="stMetric"] {{ animation-delay: 0.0s; }}
    [data-testid="column"]:nth-child(2) [data-testid="stMetric"] {{ animation-delay: 0.08s; }}
    [data-testid="column"]:nth-child(3) [data-testid="stMetric"] {{ animation-delay: 0.16s; }}
    [data-testid="column"]:nth-child(4) [data-testid="stMetric"] {{ animation-delay: 0.24s; }}
    [data-testid="column"]:nth-child(5) [data-testid="stMetric"] {{ animation-delay: 0.32s; }}
    [data-testid="column"]:nth-child(6) [data-testid="stMetric"] {{ animation-delay: 0.40s; }}

    /* ── KPI hover lift + glow ────────────────────── */
    [data-testid="stMetric"]:hover {{
        transform: translateY(-4px) !important;
        box-shadow: 0 12px 40px rgba(197,0,99,0.15) !important;
    }}

    /* ── Tab content fade on switch ────────────────── */
    .stTabs [data-baseweb="tab-panel"] {{
        animation: fadeSlideUp 0.3s ease-out;
    }}

    /* ── Plotly chart fade-in ──────────────────────── */
    [data-testid="stPlotlyChart"] {{
        animation: fadeIn 0.5s ease-out;
    }}

    /* ── Score progress bar grow ───────────────────── */
    .score-bar-fill {{
        transform-origin: left;
        animation: growWidth 0.8s cubic-bezier(0.22, 0.61, 0.36, 1) both;
    }}
    .score-bar-fill:nth-of-type(1) {{ animation-delay: 0.0s; }}
    .score-bar-fill:nth-of-type(2) {{ animation-delay: 0.08s; }}
    .score-bar-fill:nth-of-type(3) {{ animation-delay: 0.16s; }}
    .score-bar-fill:nth-of-type(4) {{ animation-delay: 0.24s; }}
    .score-bar-fill:nth-of-type(5) {{ animation-delay: 0.32s; }}

    /* ── Company card stagger ─────────────────────── */
    .cc-card {{
        animation: fadeSlideUp 0.35s ease-out both;
    }}
    .cc-card:nth-child(1)  {{ animation-delay: 0.00s; }}
    .cc-card:nth-child(2)  {{ animation-delay: 0.03s; }}
    .cc-card:nth-child(3)  {{ animation-delay: 0.06s; }}
    .cc-card:nth-child(4)  {{ animation-delay: 0.09s; }}
    .cc-card:nth-child(5)  {{ animation-delay: 0.12s; }}
    .cc-card:nth-child(6)  {{ animation-delay: 0.15s; }}
    .cc-card:nth-child(7)  {{ animation-delay: 0.18s; }}
    .cc-card:nth-child(8)  {{ animation-delay: 0.21s; }}
    .cc-card:nth-child(9)  {{ animation-delay: 0.24s; }}
    .cc-card:nth-child(10) {{ animation-delay: 0.27s; }}
    .cc-card:nth-child(11) {{ animation-delay: 0.30s; }}
    .cc-card:nth-child(12) {{ animation-delay: 0.33s; }}
    .cc-card:nth-child(n+13) {{ animation-delay: 0.36s; }}

    /* ── Table row stagger ────────────────────────── */
    .styled-table tbody tr {{
        animation: fadeIn 0.3s ease-out both;
    }}
    .styled-table tbody tr:nth-child(1)  {{ animation-delay: 0.02s; }}
    .styled-table tbody tr:nth-child(2)  {{ animation-delay: 0.04s; }}
    .styled-table tbody tr:nth-child(3)  {{ animation-delay: 0.06s; }}
    .styled-table tbody tr:nth-child(4)  {{ animation-delay: 0.08s; }}
    .styled-table tbody tr:nth-child(5)  {{ animation-delay: 0.10s; }}
    .styled-table tbody tr:nth-child(6)  {{ animation-delay: 0.12s; }}
    .styled-table tbody tr:nth-child(7)  {{ animation-delay: 0.14s; }}
    .styled-table tbody tr:nth-child(8)  {{ animation-delay: 0.16s; }}
    .styled-table tbody tr:nth-child(9)  {{ animation-delay: 0.18s; }}
    .styled-table tbody tr:nth-child(10) {{ animation-delay: 0.20s; }}
    .styled-table tbody tr:nth-child(n+11) {{ animation-delay: 0.22s; }}
</style>
"""
    # ── Dark-mode-only overrides ─────────────────────────────
    if dark:
        css += f"""
<style>
    /* Streamlit header bar (Deploy button area) */
    header[data-testid="stHeader"] {{
        background: rgba(15,12,41,0.8) !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        border-bottom: 1px solid {c["glass_border"]};
    }}
    header[data-testid="stHeader"] * {{
        color: {c["text_secondary"]} !important;
    }}

    /* Dataframe / table dark styling */
    .stDataFrame {{
        border: 1px solid {c["glass_border"]} !important;
        border-radius: 16px !important;
        overflow: hidden;
    }}
    .stDataFrame [data-testid="stDataFrameResizable"],
    .stDataFrame > div {{
        background-color: {c["card_solid"]} !important;
    }}
    [data-testid="stDataFrame"] > div > div {{
        background-color: {c["card_solid"]} !important;
    }}
    .stDataFrame thead th,
    .stDataFrame [role="columnheader"] {{
        background-color: rgba(255,255,255,0.05) !important;
        color: {c["text_secondary"]} !important;
    }}
    .stDataFrame td, .stDataFrame [role="gridcell"] {{
        color: {c["text"]} !important;
    }}
    .stDataFrame iframe {{
        background-color: {c["card_solid"]} !important;
    }}
    /* Selectbox and inputs in main area */
    .stSelectbox > div > div {{
        background: {c["input_bg"]} !important;
        color: {c["text"]} !important;
    }}
    /* Buttons */
    .stButton > button {{
        background: {c["card"]} !important;
    }}

    /* Navbar brand — lighter gradient for dark bg */
    .nav-brand {{
        background: linear-gradient(135deg, #FF9BD2 0%, {PRIMARY} 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
    }}
</style>
"""

    return css


def render_plotly_animated(
    fig: "go.Figure",
    height: int = 400,
    dark: bool = False,
    direction: str = "auto",
) -> None:
    """Render a Plotly figure with CSS clip-path reveal animation.

    Replaces st.plotly_chart() for charts that need a 'drawing' effect.
    Uses CSS clip-path to reveal the fully-rendered chart.

    Args:
        fig: Plotly figure object.
        height: Chart height in pixels.
        dark: Dark mode flag (unused, kept for API compat).
        direction: 'up', 'right', or 'auto' (detects from orientation).
    """
    import streamlit.components.v1 as components

    # Auto-detect direction from chart data
    if direction == "auto":
        direction = "up"
        for trace in fig.data:
            if getattr(trace, "orientation", None) == "h":
                direction = "right"
                break

    chart_html = fig.to_html(
        full_html=False,
        include_plotlyjs="cdn",
        config={"responsive": True, "displayModeBar": False},
    )

    anim_name = "revealRight" if direction == "right" else "revealUp"
    clip_from = "0 100% 0 0" if direction == "right" else "100% 0 0 0"

    html = f"""<!DOCTYPE html>
<html>
<head>
<style>
body {{ margin:0; padding:0; background:transparent; overflow:hidden; }}
@keyframes {anim_name} {{
    from {{ clip-path: inset({clip_from}); }}
    to   {{ clip-path: inset(0 0 0 0); }}
}}
.anim-wrap .plot-container {{
    opacity: 0;
}}
.anim-wrap.reveal .plot-container {{
    opacity: 1;
    animation: {anim_name} 1.2s cubic-bezier(0.22, 0.61, 0.36, 1) both;
}}
</style>
</head>
<body>
<div class="anim-wrap">
{chart_html}
</div>
<script>
setTimeout(function() {{
    document.querySelector('.anim-wrap').classList.add('reveal');
}}, 200);
</script>
</body>
</html>"""

    components.html(html, height=height + 5)


def render_countup_js() -> None:
    """Inject JS that animates metric values with a count-up effect.

    Uses streamlit.components.v1.html to access parent DOM from an iframe.
    Call this after all st.metric() calls on a page.
    """
    import streamlit.components.v1 as components

    components.html(
        """
        <script>
        (function() {
            const doc = window.parent.document;
            function animateCountUp() {
                const metrics = doc.querySelectorAll(
                    '[data-testid="stMetricValue"] > div'
                );
                metrics.forEach(function(el) {
                    if (el.dataset.counted) return;
                    el.dataset.counted = '1';
                    const text = el.textContent.trim();
                    // Match patterns: "$2.3B", "807", "45.2", "$150M", "4.8 / 100"
                    const m = text.match(/^([^\\d]*?)(\\d[\\d,]*\\.?\\d*)(.*)$/);
                    if (!m) return;
                    const prefix = m[1];
                    const numStr = m[2].replace(/,/g, '');
                    const suffix = m[3];
                    const target = parseFloat(numStr);
                    if (isNaN(target) || target === 0) return;
                    const hasDec = numStr.includes('.');
                    const decimals = hasDec ? (numStr.split('.')[1] || '').length : 0;
                    const hasComma = m[2].includes(',');
                    const duration = 800;
                    const start = performance.now();
                    function tick(now) {
                        const t = Math.min((now - start) / duration, 1);
                        const eased = 1 - Math.pow(1 - t, 3);  // ease-out cubic
                        const cur = target * eased;
                        var formatted;
                        if (hasDec) {
                            formatted = cur.toFixed(decimals);
                        } else {
                            var rounded = Math.round(cur);
                            formatted = hasComma
                                ? rounded.toLocaleString()
                                : rounded.toString();
                        }
                        el.textContent = prefix + formatted + suffix;
                        if (t < 1) requestAnimationFrame(tick);
                    }
                    requestAnimationFrame(tick);
                });
            }
            // Wait for Streamlit to render metrics
            setTimeout(animateCountUp, 150);
        })();
        </script>
        """,
        height=0,
    )
