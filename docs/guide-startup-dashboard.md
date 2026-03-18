# Startup Dashboard — 설계 가이드

> 807개 스타트업 데이터를 열람·시각화·평가하는 플랫폼.
> Obsidian 그래프 뷰 + Streamlit 대시보드 이중 인터페이스.

---

## 1. 현황 (2026-03-18)

### 데이터 현황

| 테이블 | 건수 | 비고 |
|--------|------|------|
| su_companies | 807 | 회사 마스터 |
| su_funding_rounds | 627 | 통화: USD |
| su_people | 602 | 창업자·임원 |
| su_company_relations | 13,354 | competitor 6,631쌍 + partner 46쌍 |
| su_scores | 806 | 5차원 + overall 백필 완료 |
| su_investors | 188 | TheVC/Crunchbase 수집 완료 |
| su_round_investors | 977 | 투자자-라운드 매핑 완료 |
| su_company_topics | — | L3 기술 토픽 매핑 (taxonomy.py 기반) |
| su_collections | 0 | 워치리스트 미생성 |
| su_signals | 0 | intel-store 연동 미구현 |

### MCP 도구 (15개)

**Phase 1** (6개): search_companies, get_company, upsert_company, get_company_stats, add_funding_round, upsert_investor

**Phase 2** (7개): score_company, add_company_relation, search_investors, get_investor_portfolio, get_funding_stats, manage_collection, search_people

**Phase 3** (2개): assign_company_topics, remove_company_topics

---

## 2. Streamlit 대시보드 (완료)

### 프로젝트 구조

```
projects/startup-db/
  src/startup_db/
    dashboard/
      app.py               Streamlit 엔트리포인트 (st.navigation SPA)
      components.py         공통 UI 컴포넌트 (navbar, sidebar, 카드 등)
      data.py               캐싱 데이터 함수 (cached_company_stats 등)
      theme.py              Dark/Light 테마 시스템 + CSS 주입
      pages/
        overview.py          통계 + Plotly 차트 + Countup 애니메이션
        companies.py         목록 + L1/L2/L3 필터 + 카드 렌더링
        company_detail.py    상세 (펀딩, 인물, 스코어, 관계)
        funding.py           펀딩 트렌드 (연도별/라운드별 분석)
        scores.py            레이더 차트 / 히트맵
        network.py           관계 그래프 (streamlit-agraph)
        investors.py         투자자 포트폴리오
```

### 기술 스택

- **Streamlit** — Python-only SPA (st.navigation)
- **Plotly** — 인터랙티브 차트
- **streamlit-agraph** — 관계 그래프 시각화
- **Supabase 직접 연결** — 읽기용 (anon key, RLS 허용)
- **Dark/Light 테마** — theme.py에서 CSS 주입

### 실행

```bash
cd projects/startup-db
uv pip install -e ".[dashboard]"
uv run streamlit run src/startup_db/dashboard/app.py
```

---

## 3. Obsidian 연동 (완료)

### 폴더 구조

```
Obsidian_Work/
  50-Startups/
    _index.md                 Dataview 테이블 (전체 목록)
    companies/
      {slug}.md               회사별 노트 (807건)
    investors/                 (미생성)
      {investor-slug}.md
    collections/               (수동 큐레이션)
      voice-ai.md
```

### 회사 노트 형식

- YAML frontmatter: name, status, category, sub_category, country, funding_total, latest_round
- `## 기술` — 기술 설명
- `## 펀딩` — 라운드별 금액 + 투자자 wikilink
- `## 인물` — 핵심 인물
- `## 관계` — 경쟁/파트너 wikilink (sub_category 기반 자동 + DB 명시적 관계)

### 핵심 메커니즘

- `[[slug]]` wikilink → Obsidian 그래프 뷰에서 자동 노드·엣지 생성
- 같은 sub_category + country 회사들이 자동으로 경쟁사 wikilink 연결
- Dataview 플러그인으로 카테고리/국가/펀딩 필터 테이블

---

## 4. 스크립트

```bash
cd projects/startup-db

# Obsidian 노트 생성 (807건)
uv run python scripts/export_to_obsidian.py
uv run python scripts/export_to_obsidian.py --dry-run  # 미리보기

# 데이터 보강
uv run python scripts/backfill_relations.py        # competitor + partner 관계
uv run python scripts/backfill_scores.py            # tech_strength 초기값
uv run python scripts/backfill_scores_full.py       # 5차원 + overall 스코어
uv run python scripts/backfill_enrichment.py        # 파생 필드 (one_liner, total_raised 등)
uv run python scripts/backfill_topics.py            # sub_category→L1 토픽 할당

# 투자자 데이터
uv run python scripts/collect_investors.py          # TheVC/Crunchbase 수집
uv run python scripts/upsert_investors_from_json.py # JSON → DB 적재
```

---

## 5. 데이터 보강 전략

### 자동 보강 (완료)

| 소스 | 대상 | 방법 |
|------|------|------|
| sub_category + country | su_company_relations (competitor) | `backfill_relations.py` |
| metadata.bigtech_collaboration | su_company_relations (partner) | `backfill_relations.py` |
| metadata.tech_competitiveness | su_scores (tech_strength) | `backfill_scores.py` |
| sub_category → L1 매핑 | su_company_topics | `backfill_topics.py` |

### 외부 수집

| 대상 | 방법 | 우선순위 | 상태 |
|------|------|---------|------|
| su_investors + su_round_investors | TheVC/Crunchbase 배치 수집 | P1 | **완료** (188 / 977) |
| su_scores (5차원 + overall) | `backfill_scores_full.py` 백필 | P2 | **완료** |
| su_signals | intel-store 연동 (Phase 4 MCP 도구) | P3 | 미착수 |

---

## 6. 운영 워크플로우

```
[수집] startup-scout로 스타트업 발굴
  → upsert_company + add_funding_round

[분류] assign_company_topics로 L3 토픽 할당
  → taxonomy.py 기반 L1/L2 자동 파생

[분석] startup-analyst로 심층 분석
  → score_company (5차원 평가)
  → add_company_relation (관계 추가)

[동기화] export_to_obsidian.py 재실행
  → Obsidian 노트 갱신 + 그래프 뷰 반영

[열람] Streamlit 대시보드 / Obsidian 그래프 뷰
  → 팀원 열람 + 큐레이션
```

---

## 7. Phase 로드맵

| Phase | 내용 | 상태 |
|-------|------|------|
| **Phase 0** | Obsidian 연동 — 807건 회사 노트 + Dataview + 그래프 뷰 | **완료** |
| **Phase 1** | 데이터 보강 — 투자자 수집 (188건), 스코어 백필 (5차원+overall) | **완료** |
| **Phase 2** | Streamlit 대시보드 — 7개 페이지 (통계·목록·상세·펀딩·스코어·네트워크·투자자) | **완료** |
| **Phase 3** | Taxonomy 연동 — L3 토픽 할당/제거 MCP 도구 | **완료** |
| **Phase 4** | intel-store 연동 — su_signals MCP 도구 + 기술 동향 연결 | 미착수 |
