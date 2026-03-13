# Startup Dashboard — 설계 가이드

> 807개 스타트업 데이터를 열람·시각화·평가하는 플랫폼.
> Obsidian 그래프 뷰를 1차 인터페이스로, 향후 Streamlit 대시보드를 2차로 구축한다.

---

## 1. 현황 (2026-03-13)

### 데이터 현황

| 테이블 | 건수 | 비고 |
|--------|------|------|
| su_companies | 807 | 회사 마스터 |
| su_funding_rounds | 627 | 통화: USD |
| su_people | 602 | 창업자·임원 |
| su_company_relations | 13,354 | competitor 6,631쌍 + partner 46쌍 |
| su_scores | 806 | tech_strength 초기값 (CSV 기반) |
| su_investors | 0 | 외부 수집 필요 |
| su_round_investors | 0 | 투자자 데이터 의존 |
| su_collections | 0 | 워치리스트 미생성 |
| su_signals | 0 | intel-store 연동 미구현 |

### MCP 도구 (13개)

**Phase 1** (6개): search_companies, get_company, upsert_company, get_company_stats, add_funding_round, upsert_investor

**Phase 2** (7개): score_company, add_company_relation, search_investors, get_investor_portfolio, get_funding_stats, manage_collection, search_people

---

## 2. 접근법: Obsidian → Streamlit

| 관점 | Obsidian 그래프 뷰 | Streamlit 대시보드 |
|------|-------------------|-------------------|
| 배포 | 로컬 (Obsidian Sync 가능) | URL 공유 (Cloud 무료) |
| 그래프 | 내장 그래프 뷰 (즉시) | pyvis/agraph (코드 필요) |
| 필터/검색 | Dataview 플러그인 | SQL 기반 (자유도 높음) |
| 차트/통계 | 불가 | plotly (자유도 높음) |
| 팀 접근 | Obsidian 설치 필요 | 브라우저 URL |

**결정**: Obsidian 먼저 (즉시 사용 가능) → Streamlit은 정량 분석 필요 시

---

## 3. Obsidian 연동 (Phase 0 — 완료)

### 폴더 구조

```
Obsidian_Work/
  50-Startups/
    _index.md                 Dataview 테이블 (전체 목록)
    companies/
      {slug}.md               회사별 노트 (807건)
    investors/                 (Phase 1 이후)
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

### 스크립트

```bash
cd projects/startup-db

# Obsidian 노트 생성 (807건)
uv run python scripts/export_to_obsidian.py
uv run python scripts/export_to_obsidian.py --dry-run  # 미리보기

# 관계 데이터 보강 (competitor + partner)
uv run python scripts/backfill_relations.py

# 스코어 초기값 보강 (tech_strength)
uv run python scripts/backfill_scores.py
```

---

## 4. 데이터 보강 전략

### 자동 보강 (완료)

| 소스 | 대상 | 방법 |
|------|------|------|
| sub_category + country | su_company_relations (competitor) | `backfill_relations.py` |
| metadata.bigtech_collaboration | su_company_relations (partner) | `backfill_relations.py` |
| metadata.tech_competitiveness | su_scores (tech_strength) | `backfill_scores.py` |

### 외부 수집 필요 (미완)

| 대상 | 방법 | 우선순위 |
|------|------|---------|
| su_investors + su_round_investors | TheVC/Crunchbase 배치 수집 (상위 200개 회사) | P1 |
| su_scores (나머지 4차원) | startup-analyst 분석 리포트 → DB 저장 자동화 | P2 |
| su_signals | intel-store 연동 (Phase 3 MCP 도구) | P3 |

---

## 5. Streamlit 대시보드 (Phase 1 — 미구현)

### 프로젝트 구조 (계획)

```
projects/startup-db/
  src/startup_db/
    dashboard/
      app.py               Streamlit 엔트리포인트
      pages/
        01_overview.py      통계 + 차트
        02_companies.py     목록 + 필터
        03_company_detail.py  상세 (펀딩, 인물, 스코어)
        04_funding.py       펀딩 트렌드
        05_network.py       관계 그래프 (pyvis)
        06_scores.py        레이더 차트 / 히트맵
      components/
        charts.py           plotly 차트 함수
        filters.py          사이드바 필터
```

### 기술 스택

- **Streamlit** — Python-only, Node 불필요
- **Plotly** — 인터랙티브 차트
- **pyvis / streamlit-agraph** — 관계 그래프
- **Supabase 직접 연결** — 읽기용 (anon key, RLS 허용)

### 실행

```bash
cd projects/startup-db
uv pip install -e ".[dashboard]"
uv run streamlit run src/startup_db/dashboard/app.py
```

---

## 6. 운영 워크플로우

```
[수집] startup-scout로 스타트업 발굴
  → upsert_company + add_funding_round

[분석] startup-analyst로 심층 분석
  → score_company (5차원 평가)
  → add_company_relation (관계 추가)

[동기화] export_to_obsidian.py 재실행
  → Obsidian 노트 갱신 + 그래프 뷰 반영

[열람] Obsidian 그래프 뷰 / Dataview 필터
  → 팀원 열람 + 큐레이션
```
