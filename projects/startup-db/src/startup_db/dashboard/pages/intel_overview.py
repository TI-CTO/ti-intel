"""Intel Store — Overview + Topic Explorer page."""

from __future__ import annotations

import html as _html

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from startup_db.dashboard.components import is_dark_mode
from startup_db.dashboard.data import (
    cached_intel_by_topic,
    cached_intel_community_engagement,
    cached_intel_filter_options,
    cached_intel_item_detail,
    cached_intel_items_by_topic,
    cached_intel_recent,
    cached_intel_search,
    cached_intel_stats,
    cached_intel_weekly_diff,
)
from startup_db.dashboard.theme import (
    CHART_COLORS,
    DARK,
    LIGHT,
    PRIMARY,
    _glass_css,
    get_plotly_layout,
    render_countup_js,
    render_plotly_animated,
)

# ── Type label maps ──────────────────────────────────────────
TYPE_KO = {
    "news": "뉴스",
    "paper": "논문",
    "patent": "특허",
    "community": "커뮤니티",
    "statement": "기업발언",
    "report": "리포트",
    "standard": "표준",
}


def _format_item_rows(items: list[dict]) -> pd.DataFrame:
    """Convert intel item records into a compact display dataframe."""
    rows = []
    for item in items:
        rows.append(
            {
                "ID": item.get("id"),
                "제목": item.get("title", ""),
                "유형": TYPE_KO.get(item.get("item_type"), item.get("item_type")),
                "소스": item.get("source_name", ""),
                "발행일": item.get("published_date") or "",
                "수집일": item.get("collected_date") or "",
                "신뢰도": item.get("reliability") or "",
                "URL": item.get("source_url") or "",
            }
        )
    return pd.DataFrame(rows)


def _render_item_table(items: list[dict], *, key: str) -> None:
    """Render a filterable item table with URL columns."""
    if not items:
        st.info("조건에 맞는 아이템이 없습니다.")
        return

    df = _format_item_rows(items)
    st.dataframe(
        df,
        width="stretch",
        hide_index=True,
        column_config={
            "ID": st.column_config.NumberColumn("ID", width="small"),
            "제목": st.column_config.TextColumn("제목", width="large"),
            "URL": st.column_config.LinkColumn("URL", display_text="열기"),
        },
    )

    item_ids = [int(item["id"]) for item in items if item.get("id") is not None]
    selected_id = st.selectbox(
        "상세 보기",
        options=item_ids,
        index=0,
        key=f"{key}_detail_id",
        format_func=lambda item_id: _title_for_id(items, item_id),
    )
    if selected_id:
        _render_item_detail(selected_id)


def _render_item_detail(item_id: int) -> None:
    """Render raw detail for one intel item."""
    item = cached_intel_item_detail(item_id)
    if not item:
        st.warning("아이템을 찾을 수 없습니다.")
        return

    with st.expander(f"Raw detail · #{item_id}", expanded=False):
        st.markdown(f"**{item.get('title', '')}**")
        cols = st.columns(4)
        cols[0].metric("유형", TYPE_KO.get(item.get("item_type"), item.get("item_type", "")))
        cols[1].metric("신뢰도", item.get("reliability") or "—")
        cols[2].metric("발행일", item.get("published_date") or "—")
        cols[3].metric("수집일", item.get("collected_date") or "—")

        if item.get("source_url"):
            st.link_button("원문 열기", item["source_url"])

        topic_names = [
            topic.get("display_name") or topic.get("slug")
            for topic in item.get("topics", [])
        ]
        if topic_names:
            st.caption("Topics: " + ", ".join(topic_names))

        if item.get("abstract"):
            st.markdown("**Abstract / Summary**")
            st.write(item["abstract"])

        st.markdown("**Metadata**")
        st.json(item.get("metadata", {}), expanded=False)


def _title_for_id(items: list[dict], item_id: int) -> str:
    for item in items:
        if item.get("id") == item_id:
            return f"#{item_id} · {item.get('title', '')[:80]}"
    return f"#{item_id}"


def _topic_options(topics: list[dict]) -> dict[str, str]:
    return {topic["topic_name"]: topic["topic_slug"] for topic in topics}

dark = is_dark_mode()
PL = get_plotly_layout(dark)
C = DARK if dark else LIGHT
glass = _glass_css(C)

st.title("인텔리전스 저장소")

# ── Data ─────────────────────────────────────────────────────
stats = cached_intel_stats()
total = stats["total"]
by_type = stats["by_type"]
by_source = stats["by_source"]
monthly = stats["by_month"]

# ── KPI metrics ──────────────────────────────────────────────
type_count = len(by_type)
source_count = len(by_source)
community_count = by_type.get("community", 0)

col1, col2, col3, col4 = st.columns(4)
col1.metric("전체 아이템", f"{total:,}")
col2.metric("유형 수", f"{type_count}")
col3.metric("소스 수", f"{source_count}")
col4.metric("커뮤니티", f"{community_count:,}")

render_countup_js()
st.divider()

# ── Tabs ─────────────────────────────────────────────────────
tab_timeline, tab_sources, tab_recent, tab_topics, tab_search = st.tabs([
    "수집 타임라인",
    "소스 & 유형",
    "최근 수집",
    "토픽 탐색",
    "검색",
])

# ── Tab 1: 수집 타임라인 ─────────────────────────────────────
with tab_timeline:
    if monthly:
        month_df = pd.DataFrame(monthly)
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=month_df["month"],
            y=month_df["count"],
            marker_color=CHART_COLORS[0],
            text=month_df["count"],
            textposition="outside",
            hovertemplate="<b>%{x}</b><br>수집: %{y}건<extra></extra>",
        ))
        fig.update_layout(
            **PL,
            height=380,
            showlegend=False,
            yaxis_title="수집 건수",
            xaxis_title="",
        )
        render_plotly_animated(fig, height=380, dark=dark)
    else:
        st.info("수집된 데이터가 없습니다.")

    # Community engagement summary
    community_items = cached_intel_community_engagement()
    if community_items:
        st.subheader("커뮤니티 반응")
        platform_stats: dict[str, dict] = {}
        for item in community_items:
            p = item["platform"]
            platform_stats.setdefault(p, {"count": 0, "total_engagement": 0})
            platform_stats[p]["count"] += 1
            platform_stats[p]["total_engagement"] += item.get("engagement", 0)

        pcols = st.columns(len(platform_stats))
        for i, (platform, pstats) in enumerate(
            sorted(platform_stats.items(), key=lambda x: -x[1]["count"])
        ):
            with pcols[i]:
                avg_eng = (
                    pstats["total_engagement"] / pstats["count"]
                    if pstats["count"] > 0
                    else 0
                )
                st.metric(
                    platform.title(),
                    f"{pstats['count']}건",
                    f"평균 반응: {avg_eng:,.0f}",
                )

# ── Tab 2: 소스 & 유형 ──────────────────────────────────────
with tab_sources:
    left, right = st.columns(2)

    with left:
        st.subheader("유형별 분포")
        type_df = pd.DataFrame([
            {"유형": TYPE_KO.get(k, k), "건수": v}
            for k, v in sorted(by_type.items(), key=lambda x: -x[1])
        ])
        if not type_df.empty:
            fig = px.pie(
                type_df,
                values="건수",
                names="유형",
                hole=0.4,
                color_discrete_sequence=CHART_COLORS,
            )
            fig.update_layout(**PL, height=400)
            st.plotly_chart(fig, use_container_width=True)

    with right:
        st.subheader("소스별 분포")
        sorted_sources = sorted(by_source.items(), key=lambda x: -x[1])[:15]
        source_df = pd.DataFrame([
            {"소스": k, "건수": v} for k, v in sorted_sources
        ])
        if not source_df.empty:
            fig = px.bar(
                source_df,
                x="건수",
                y="소스",
                orientation="h",
                color_discrete_sequence=[CHART_COLORS[1]],
            )
            fig.update_layout(
                **PL,
                height=400,
                showlegend=False,
                yaxis={"categoryorder": "total ascending"},
            )
            render_plotly_animated(fig, height=400, dark=dark)

# ── Tab 3: 최근 수집 ────────────────────────────────────────
with tab_recent:
    recent = cached_intel_recent(limit=30)
    if recent:
        border = C["glass_border"]
        rows_html = []
        for item in recent:
            title = _html.escape(item.get("title", "")[:80])
            itype = item.get("item_type", "")
            itype_ko = TYPE_KO.get(itype, itype)
            source = _html.escape(item.get("source_name", ""))
            url = item.get("source_url", "")
            date_str = (item.get("collected_date") or "")[:10]

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

            rows_html.append(
                f'<tr style="border-bottom:1px solid {border};">'
                f'<td style="padding:8px;font-size:0.85rem;">{title_html}</td>'
                f'<td style="padding:8px;text-align:center;">'
                f'<span style="background:{badge_color};color:#fff;'
                f'padding:2px 8px;border-radius:10px;font-size:0.72rem;'
                f'font-weight:600;">{_html.escape(itype_ko)}</span></td>'
                f'<td style="padding:8px;color:{C["text_secondary"]};'
                f'font-size:0.82rem;">{source}</td>'
                f'<td style="padding:8px;color:{C["text_secondary"]};'
                f'font-size:0.82rem;">{date_str}</td>'
                f"</tr>"
            )

        st.markdown(
            f'<table style="width:100%;border-collapse:collapse;">'
            f'<thead><tr style="border-bottom:2px solid {border};">'
            f'<th style="text-align:left;padding:8px;color:{C["text_secondary"]};'
            f'font-size:0.75rem;text-transform:uppercase;">제목</th>'
            f'<th style="text-align:center;padding:8px;color:{C["text_secondary"]};'
            f'font-size:0.75rem;text-transform:uppercase;">유형</th>'
            f'<th style="text-align:left;padding:8px;color:{C["text_secondary"]};'
            f'font-size:0.75rem;text-transform:uppercase;">소스</th>'
            f'<th style="text-align:left;padding:8px;color:{C["text_secondary"]};'
            f'font-size:0.75rem;text-transform:uppercase;">수집일</th>'
            f"</tr></thead>"
            f'<tbody>{"".join(rows_html)}</tbody></table>',
            unsafe_allow_html=True,
        )
    else:
        st.info("수집된 아이템이 없습니다.")

# ── Tab 4: 토픽 탐색 ────────────────────────────────────────
with tab_topics:
    topics = cached_intel_by_topic()

    if not topics:
        st.info("토픽 데이터가 없습니다.")
    else:
        # Chart: items per topic
        topic_df = pd.DataFrame(topics)
        chart_height = max(350, len(topic_df.head(20)) * 28)

        fig = px.bar(
            topic_df.head(20),
            x="count",
            y="topic_name",
            orientation="h",
            color_discrete_sequence=[PRIMARY],
            labels={"count": "건수", "topic_name": "토픽"},
        )
        fig.update_layout(
            **{**PL, "margin": {"l": 200, "r": 20, "t": 30, "b": 20}},
            height=chart_height,
            showlegend=False,
            yaxis={"categoryorder": "total ascending"},
        )
        render_plotly_animated(fig, height=chart_height, dark=dark)

        st.divider()

        # Topic selector + drill down
        st.subheader("토픽별 상세")
        topic_options = _topic_options(topics)
        selected_name = st.selectbox(
            "토픽 선택",
            options=list(topic_options.keys()),
            index=0,
        )
        selected_slug = topic_options[selected_name]

        items = cached_intel_items_by_topic(selected_slug, limit=50)

        diff = cached_intel_weekly_diff(selected_slug)
        dcol1, dcol2 = st.columns(2)
        dcol1.metric("최근 7일", diff["this_week_count"])
        dcol2.metric("이전 7일", diff["last_week_count"])

        with st.expander("Weekly diff 아이템 보기", expanded=False):
            st.markdown("**최근 7일**")
            _render_item_table(diff["this_week"][:30], key=f"{selected_slug}_this_week")
            st.markdown("**이전 7일**")
            _render_item_table(diff["last_week"][:30], key=f"{selected_slug}_last_week")

        if not items:
            st.info(f"'{selected_name}'에 해당하는 아이템이 없습니다.")
        else:
            # Type filter
            all_types = sorted({item["item_type"] for item in items})
            type_filter = st.multiselect(
                "유형 필터",
                options=all_types,
                default=all_types,
                format_func=lambda x: TYPE_KO.get(x, x),
            )
            filtered = [
                item for item in items if item["item_type"] in type_filter
            ]

            # Stats row
            type_counts: dict[str, int] = {}
            for item in filtered:
                t = item["item_type"]
                type_counts[t] = type_counts.get(t, 0) + 1

            stat_cols = st.columns(min(len(type_counts) + 1, 5))
            stat_cols[0].metric("전체", len(filtered))
            for i, (t, c) in enumerate(
                sorted(type_counts.items(), key=lambda x: -x[1])
            ):
                if i + 1 < len(stat_cols):
                    stat_cols[i + 1].metric(TYPE_KO.get(t, t), c)

            # Items table
            border = C["glass_border"]
            rows_html = []
            for item in filtered:
                title = _html.escape(item.get("title", "")[:90])
                itype = item.get("item_type", "")
                itype_ko = TYPE_KO.get(itype, itype)
                source = _html.escape(item.get("source_name", "")[:25])
                url = item.get("source_url", "")
                date_str = (item.get("collected_date") or "")[:10]

                meta = item.get("metadata", {})
                eng_platform = meta.get("platform", "")
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
                    f' style="color:{C["text"]};text-decoration:none;">'
                    f"{title}</a>"
                    if url
                    else title
                )

                engagement_html = ""
                if eng_platform:
                    eng_str = f"{engagement:,}" if engagement else ""
                    engagement_html = (
                        f'<span style="color:{C["text_secondary"]};'
                        f'font-size:0.78rem;">'
                        f"{eng_platform} {eng_str}</span>"
                    )

                rows_html.append(
                    f'<tr style="border-bottom:1px solid {border};">'
                    f'<td style="padding:8px;font-size:0.85rem;">'
                    f"{title_html}</td>"
                    f'<td style="padding:8px;text-align:center;">'
                    f'<span style="background:{badge_color};color:#fff;'
                    f"padding:2px 8px;border-radius:10px;"
                    f'font-size:0.72rem;font-weight:600;">'
                    f"{_html.escape(itype_ko)}</span></td>"
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
                f'<th style="text-align:left;padding:8px;'
                f'color:{C["text_secondary"]};font-size:0.75rem;'
                f'text-transform:uppercase;">제목</th>'
                f'<th style="text-align:center;padding:8px;'
                f'color:{C["text_secondary"]};font-size:0.75rem;'
                f'text-transform:uppercase;">유형</th>'
                f'<th style="text-align:left;padding:8px;'
                f'color:{C["text_secondary"]};font-size:0.75rem;'
                f'text-transform:uppercase;">소스</th>'
                f'<th style="text-align:left;padding:8px;'
                f'color:{C["text_secondary"]};font-size:0.75rem;'
                f'text-transform:uppercase;">반응</th>'
                f'<th style="text-align:left;padding:8px;'
                f'color:{C["text_secondary"]};font-size:0.75rem;'
                f'text-transform:uppercase;">수집일</th>'
                f"</tr></thead>"
                f'<tbody>{"".join(rows_html)}</tbody></table>',
                unsafe_allow_html=True,
            )

            _render_item_table(filtered, key=f"{selected_slug}_topic_items")


# ── Tab 5: 검색 ──────────────────────────────────────────────
with tab_search:
    st.subheader("인텔 저장소 검색")
    options = cached_intel_filter_options()
    topics = options["topics"]
    topic_options = {"전체 토픽": None} | _topic_options(topics)

    qcol1, qcol2 = st.columns([2, 1])
    query_text = qcol1.text_input("검색어", placeholder="예: voice cloning, AICC, PQC")
    selected_topic_name = qcol2.selectbox("토픽", options=list(topic_options.keys()))

    fcol1, fcol2 = st.columns(2)
    selected_types = fcol1.multiselect(
        "유형",
        options=options["types"],
        default=[],
        format_func=lambda item_type: TYPE_KO.get(item_type, item_type),
    )
    selected_sources = fcol2.multiselect(
        "소스",
        options=options["sources"],
        default=[],
    )

    dcol1, dcol2, lcol = st.columns([1, 1, 1])
    collected_from = dcol1.date_input("수집일 시작", value=None)
    collected_to = dcol2.date_input("수집일 종료", value=None)
    limit = lcol.number_input("최대 결과", min_value=10, max_value=500, value=100, step=10)

    results = cached_intel_search(
        query_text=query_text,
        item_types=tuple(selected_types),
        source_names=tuple(selected_sources),
        topic_slug=topic_options[selected_topic_name],
        collected_from=collected_from.isoformat() if collected_from else None,
        collected_to=collected_to.isoformat() if collected_to else None,
        limit=int(limit),
    )

    st.caption(f"검색 결과 {len(results):,}건")
    _render_item_table(results, key="intel_search")
