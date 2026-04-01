# Tech Intelligence Platform 가이드

> 스킬(명령어) → 에이전트(자동 실행) → MCP 프로젝트(데이터/렌더링) 3계층으로 구성된 기술 인텔리전스 플랫폼.

---

## 한눈에 보기

```
┌─────────────────── 사용자가 직접 호출 ───────────────────┐
│  /wtis          기술 도입 판정 (Go/No-Go)                 │
│  /weekly-monitor 주간 기술 동향 모니터링                    │
│  /research-session 자유 주제 심층 리서치                    │
│  /discover       신기술/기회 탐색                          │
│  /monitor        등록 토픽 변화 감지                       │
│  /report-pdf     마크다운 → PDF                           │
│  /slides         마크다운 → PPTX                          │
│  /obsidian-bridge 옵시디언 동기화                          │
│  /work-log       업무일지                                 │
│  /new-project    프로젝트 스캐폴딩                         │
└───────────────────────────────────────────────────────────┘
          │ 내부적으로 호출                │
          ▼                              ▼
┌─── 에이전트 조직 (자동) ──────┐  ┌─── MCP 프로젝트 (데이터) ───┐
│ 분석팀                        │  │ intel-store (13 도구)       │
│  research-deep  수석 분석관    │  │ trend-tracker (5 도구)      │
│  researcher     리서치 어소시  │  │ design-system (4 도구)      │
│  voice-of-market 시장 분석관  │  │ startup-db (15 도구)        │
│ 품질팀                        │  │ youtube-transcript (1 도구) │
│  fact-checker   감사역        │  │ context7 (외부 문서 조회)    │
│  validator      품질 검증관    │  └────────────────────────────┘
│ 엔지니어링팀                   │
│  implementer    스태프 엔지니어 │
│  reviewer       코드 리뷰 리드 │
└───────────────────────────────┘
```

---

## 외부 API 현황

### 수집 소스

| API | 용도 | 비용 | Rate Limit | 인증 | 상태 |
|-----|------|------|------------|------|------|
| **Semantic Scholar** | 학술 논문 검색 | 무료 | 1 req/sec | 선택: `SEMANTIC_SCHOLAR_API_KEY` | 정상 |
| **arXiv** | 프리프린트 논문 | 무료 | 3초 간격 | 불필요 | 정상 |
| **Google Patents (SerpAPI)** | 글로벌 특허 | 무료 250회/월 | - | `SERPAPI_API_KEY` | 정상 |
| **Tavily** | AI 뉴스 검색 | 무료 1,000회/월 | 0.5초 간격 | `TAVILY_API_KEY` | 정상 |
| **GDELT** | 글로벌 뉴스 | 완전 무료 | 1초 간격 | 불필요 | 정상 |
| **Naver News** | 한국어 뉴스 | 무료 | API 키 필요 | `NAVER_CLIENT_ID` + `SECRET` | 정상 |

### 인프라

| 서비스 | 용도 | 비용 | 인증 |
|--------|------|------|------|
| **Supabase** | PostgreSQL + pgvector DB | 무료 티어 | `SUPABASE_URL` + `SUPABASE_KEY` |
| **multilingual-e5-large** | 임베딩 (1024차원, 한영) + 관련성 필터링 | 무료 (로컬) | 불필요 |
| **Playwright Chromium** | PDF 렌더링 | 무료 (로컬) | 불필요 |

### 폐기된 API

| API | 이유 | 대체 |
|-----|------|------|
| ~~USPTO PatentsView~~ | HTTP 410 서비스 종료 (2026-03) | Google Patents (SerpAPI) |
| ~~research-hub MCP~~ | intel-store로 통합 | intel-store `collect_papers` |
| ~~patent-intel MCP~~ | intel-store로 통합 | intel-store `collect_patents` |
| ~~telco-factbook MCP~~ | MCP 제거 (2026-03) | CLI 직접 실행 또는 intel-store 경쟁사 토픽 |
| ~~supabase MCP~~ | VSCode 확장 미작동 | Management API 직접 사용 |

### 월간 쿼터 관리

| API | 월 한도 | 예상 사용량 | 여유 |
|-----|---------|-----------|------|
| SerpAPI | 250회 | ~80회 (20토픽 × ~4회/월) | 충분 |
| Tavily | 1,000회 | ~200회 (주간 모니터링 + 수동) | 충분 |

> 쿼터 초과 시: SerpAPI → 특허 수집 중단 (뉴스/논문은 무영향), Tavily → GDELT + Naver 자동 폴백

---

## 1. 스킬 (사용자 직접 호출)

### 핵심 분석 스킬

| 스킬 | 호출 | 한 줄 설명 | 산출물 |
|------|------|-----------|--------|
| **WTIS** | `/wtis` 또는 자연어 | 기술 도입 Go/No-Go 판정 | 200점 리포트 + PDF + 포트폴리오 |
| **Weekly Monitor** | `/weekly-monitor {domain}` 또는 자연어 | 주간 기술 동향 2단계 스캔 | 주간 리포트 + 심층 리서치 + PDF |
| **Research Session** | `/research-session {주제}` 또는 자연어 | 자유 주제 구조화 리서치 | 리서치 노트 |
| **Discover** | `/discover {분야}` 또는 자연어 | 신기술/기회 탐색 | 2×2 매트릭스 + 발굴 리포트 |
| **Monitor** | `/monitor {topic}` 또는 자연어 | 등록 토픽 변화 감지 | 변화 알림 |
| **Startup Scout** | `/startup-scout {도메인}` 또는 자연어 | 스타트업 후보 발굴 | 쇼트리스트 |
| **Startup Analyst** | `/startup-analyst {기업명}` 또는 자연어 | 스타트업 심층 분석 + DB JSON | 분석 리포트 |

### 출력/동기화 스킬

| 스킬 | 호출 | 한 줄 설명 |
|------|------|-----------|
| **Report PDF** | `/report-pdf {파일}` 또는 자연어 | 마크다운 → 컨설팅 스타일 PDF |
| **Slides** | `/slides {파일}` 또는 자연어 | 마크다운 → 테마 적용 PPTX |
| **Obsidian Bridge** | `/obsidian-bridge {파일} {유형}` 또는 자연어 | 산출물 → 옵시디언 볼트 동기화 |
| **Work Log** | `/work-log` 또는 자연어 | 오늘 작업 → 업무일지 기록 |
| **New Project** | `/new-project {이름}` 또는 자연어 | 표준 구조 프로젝트 생성 |

### 스킬 I/O Contract

모든 분석 스킬은 통일된 입출력 계약(`## I/O Contract`)을 가진다:
- **Input**: 필수/선택 파라미터 테이블
- **Output Files**: 생성되는 파일 경로 패턴
- **Return**: 표준화된 반환값 (`status`, `summary`, `file_path` + 스킬별 추가 필드)

스킬 완료 후에는 `## Next Steps` 섹션이 후속 가능한 스킬을 명시적으로 제안한다.
전체 연결 관계는 `docs/guide-skill-chaining.md` 참조.

---

## 2. 스킬 상세

### `/wtis` — 기술 도입·제휴 의사결정 시스템 (v4.1)

**목적**: "이 기술 도입해야 해?" — 200점 만점 정량 평가 → Go / Conditional / No-Go 판정

**사용법**:
```
/wtis "PQC VoLTE 사업화 검증"         ← 제안서 분석 (proposal 모드)
/wtis "온디바이스 sLM 기술 검증"        ← 기술 검증 (standard 모드)
/wtis "6G 보안 신기술 탐색"            ← 신기술 발굴 (deep 모드)
```

**내부 파이프라인**: 주제식별 → 심층조사 → 정량평가 → 검증 → 최종리포트 → PDF → 포트폴리오 갱신

**산출물**:
- 최종 리포트: `outputs/reports/{domain}/{날짜}_{slug}/{날짜}_wtis-{slug}.md`
- PDF: `outputs/reports/{domain}/{날짜}_{slug}/{날짜}_wtis-{slug}.pdf`
- 포트폴리오: `outputs/reports/{domain}/{domain}-portfolio.md`

---

### `/weekly-monitor` — 주간 기술 동향

**목적**: 매주 기술 변화를 자동 감지하고 심층 분석이 필요한 영역을 식별

**사용법**:
```
/weekly-monitor agentic-ai     ← 에이전틱AI 도메인 (12개 L3 기술 스캔)
/weekly-monitor voice-ai       ← 보이스AI 도메인 (8개 L3)
/weekly-monitor secure-ai      ← 보안AI 도메인 (5개 L3)
```

**2단계 파이프라인**:
- **Tier 1**: 모든 L3 기술을 빠르게 스캔 → 🟢(안정) / 🟡(주의) / 🔴(변화감지) 분류
- **Tier 2**: 🔴 기술만 심층 리서치 (research-deep 에이전트 사용)

**스케줄**: 매주 월 07:30 순차 실행 (agentic-ai → voice-ai → secure-ai → 경쟁사 브로드스캔)

**산출물**: `outputs/reports/weekly/`

---

### `/research-session` — 자유 주제 리서치

```
/research-session "CKKS 부트스트래핑 최적화 동향"
/research-session "Samsung S26 AI 보안 기능 분석"
```

산출물: `outputs/reports/{날짜}_{주제}.md`

### `/discover` — 신기술 탐색

```
/discover "edge AI security"
/discover "quantum networking"
```

산출물: 2×2 매트릭스 (즉시착수 / 역량확보후 / 검토 / 보류)

### `/monitor` — 토픽 변화 감지

```
/monitor pqc-voice-encryption    ← 특정 토픽
/monitor all             ← 전체 토픽 스캔
```

### `/report-pdf` — PDF 변환

```
/report-pdf /path/to/report.md              ← 기본 professional 테마
/report-pdf /path/to/report.md minimal      ← minimal 테마
```

### `/slides` — PPTX 변환

```
/slides /path/to/presentation.md            ← 기본 professional 테마
```

### `/obsidian-bridge` — 옵시디언 동기화

```
/obsidian-bridge /path/to/file.md reference      ← 10-Reference/
/obsidian-bridge /path/to/file.md research       ← 30-Reports/
/obsidian-bridge /path/to/file.md weekly          ← 30-Reports/weekly/
/obsidian-bridge /path/to/file.md devlog          ← 40-DevLog/
```

### `/work-log` — 업무일지

```
/work-log          ← 오늘 일지 생성 또는 추가
/work-log update   ← 기존 일지에 새 작업만 추가
```

### `/new-project` — 프로젝트 생성

```
/new-project auth-api-refactor
```

---

## 3. 에이전트 조직 (자동 실행)

> 에이전트는 직접 호출하지 않음. 스킬(Orchestrator)이 필요할 때 자동으로 투입.
> 각 에이전트는 직함·팀·보고라인을 가진 조직 구성원이다.

```
ctoti (Board)
  └── Orchestrator (Skills)
        ├── 분석팀 (Analysis)
        │     ├── research-deep — 수석 분석관
        │     ├── researcher — 리서치 어소시에이트
        │     └── voice-of-market — 시장 분석관
        ├── 품질팀 (Quality)
        │     ├── fact-checker — 감사역
        │     └── validator — 품질 검증관
        └── 엔지니어링팀 (Engineering)
              ├── implementer — 스태프 엔지니어
              └── reviewer — 코드 리뷰 리드
```

| 에이전트 | 직함 | 팀 | 호출하는 스킬 | 읽기/쓰기 |
|----------|------|-----|-------------|-----------|
| **research-deep** | 수석 분석관 | Analysis | wtis, weekly-monitor | 쓰기 가능 |
| **researcher** | 리서치 어소시에이트 | Analysis | (범용) | 읽기 전용 |
| **voice-of-market** | 시장 분석관 | Analysis | weekly-monitor | 쓰기 가능 |
| **fact-checker** | 감사역 | Quality | wtis full, biz-case | 쓰기 가능 |
| **validator** | 품질 검증관 | Quality | wtis | 읽기 전용 |
| **implementer** | 스태프 엔지니어 | Engineering | (범용) | 쓰기 가능 |
| **reviewer** | 코드 리뷰 리드 | Engineering | (범용) | 읽기 전용 |

### 핸드오프 흐름

```
분석팀 워크플로우:
  researcher (빠른 탐색) → research-deep (심층 종합)
  voice-of-market (수요 시그널) → research-deep (공급+수요 통합)

품질팀 워크플로우:
  research-deep 산출물 → fact-checker (외부 사실 검증) → validator (내부 일관성)

엔지니어링팀 워크플로우:
  implementer (구현) → reviewer (코드 리뷰)
```

---

## 4. MCP 프로젝트 (데이터 계층)

### intel-store — 통합 인텔리전스 저장소

> 뉴스·논문·특허를 **한곳에 모으고**, 키워드+AI 검색으로 **즉시 꺼내 쓰는** 저장소.

**13개 도구**:

| 구분 | 도구 | 설명 | 예시 |
|------|------|------|------|
| 검색 | `search_intel` | 통합 검색 (keyword/semantic/hybrid, 기본 keyword) | `search_intel(query="PQC", mode="hybrid")` |
| | `find_similar` | 유사 아이템 탐색 (ID 또는 텍스트) | `find_similar(item_id=128)` / `find_similar(text="실시간 AI 사기 탐지")` |
| | `get_weekly_diff` | 이번 주 vs 지난 주 신규·변경 아이템 비교 | `get_weekly_diff(topic="pqc-voice-encryption", week_date="2026-03-04")` |
| | `get_item_detail` | 단건 상세 조회 (ID 또는 external_id) | `get_item_detail(item_id=42)` / `get_item_detail(external_id="gp:US123")` |
| 수집 | `collect_papers` | Semantic Scholar 수집 (빈 결과 시 arXiv 자동 폴백) | `collect_papers(topic="pqc-voice-encryption", query="post-quantum")` |
| | `collect_arxiv` | arXiv 직접 수집 | `collect_arxiv(topic="he-keyword-search", query="all:CKKS")` |
| | `collect_patents` | Google Patents 수집 (SerpAPI, 250회/월) | `collect_patents(topic="pqc-voice-encryption", query="PQC")` |
| | `collect_news` | Tavily/GDELT/Naver 수집 (source별 또는 all) | `collect_news(topic="spam-phishing-detection", source="naver")` |
| | `collect_all` | 전체 소스 일괄 수집 (papers+arxiv+patents+news) | `collect_all(topic="pqc-voice-encryption", query="PQC")` |
| 저장 | `upsert_items` | 아이템 저장 (content_hash 자동 중복 체크) | |
| | `link_topics` | 아이템 ↔ 토픽 연결 | |
| | `link_relation` | 아이템 간 관계 (cites/updates/contradicts 등) | |
| 통계 | `get_intel_stats` | 토픽/유형별 실시간 집계 | `get_intel_stats(topic="secure-ai", period=90)` |

**`collect_all` 고급 사용법** — 소스별 쿼리를 다르게 지정:
```
collect_all(
  topic="pqc-voice-encryption",
  query="post-quantum cryptography",          ← 기본 쿼리
  queries={"arxiv": "all:ML-KEM lattice", "news": "양자암호 상용화"}  ← 소스별 오버라이드
)
```

**사용 흐름**:
```
[처음] collect_all → 관심 주제 데이터를 수집해서 DB에 쌓기
[이후] search_intel / find_similar → 쌓인 데이터에서 즉시 검색
[정기] get_weekly_diff → 이번 주 신규 아이템 변화 감지
```

**관련성 필터링**: `collect_papers`, `collect_arxiv`는 임베딩 코사인 유사도 기반 필터링 적용 (기본 임계값 0.8). 토픽과 무관한 수집물이 자동 제거됨.

**기술 스택**: Supabase PostgreSQL + pgvector(HNSW) + multilingual-e5-large(1024차원) + RRF 하이브리드 검색

---

### trend-tracker — 트렌드 모니터링

> 기술 트렌드 스냅샷을 시계열로 저장하고 시점 간 비교.

| 도구 | 설명 |
|------|------|
| `manage_watch_topics` | 모니터링 대상 CRUD |
| `upsert_snapshot` | 트렌드 스냅샷 저장 |
| `get_trend_timeline` | 시계열 트렌드 조회 |
| `get_topic_summary` | 토픽 최신 요약 |
| `compare_snapshots` | 두 시점 비교 |

### 경쟁사 모니터링

> 경쟁사 전략 방향·임원 발언은 **intel-store**의 경쟁사 토픽으로 수집·검색한다.

```
# 경쟁사 전략 뉴스 검색
search_intel(query="competitor AI strategy", topic="competitor-strategy", mode="hybrid")

# 뉴스 추가 수집
collect_news(topic="competitor-strategy", query="경쟁사 AI 투자", source="all")
```

> 재무 지표(매출, 가입자 등)가 필요한 경우: `projects/telco-factbook/` CLI로 직접 실행 (MCP 미등록)

### design-system — 디자인 시스템

> 마크다운을 컨설팅 스타일 PDF/PPTX로 변환.

**4개 도구**:

| 도구 | 설명 |
|------|------|
| `render_pdf` | 마크다운 → A4 PDF (Playwright Chromium) |
| `render_pptx` | 마크다운 → PPTX (python-pptx) |
| `list_themes` | 사용 가능한 테마 목록 |
| `get_theme` | 특정 테마의 디자인 토큰 상세 |

테마: professional / minimal / dark

---

### startup-db — 스타트업 데이터베이스

> 한국/글로벌 스타트업의 회사정보, 펀딩, 인물, 평가 데이터 저장·검색. `su_` 접두사 12개 테이블.

**15개 도구 (Phase 1~3)**:

| 구분 | 도구 | 설명 | 예시 |
|------|------|------|------|
| 검색 | `search_companies` | 이름/카테고리/국가/태그/L1/L2/L3 필터 검색 | `search_companies(query="AI", country="한국")` |
| | `get_company` | slug로 상세 조회 (라운드, 인물, 스코어 포함) | `get_company(slug="sim2real")` |
| | `get_company_stats` | 카테고리별/국가별/상태별 통계 | `get_company_stats()` |
| 저장 | `upsert_company` | 스타트업 추가/업데이트 (slug 기준) | `upsert_company(name="NewCo", country="한국")` |
| | `add_funding_round` | 펀딩 라운드 + 투자자 연결 | `add_funding_round(company_slug="newco", round_type="seed")` |
| | `upsert_investor` | 투자자 추가/업데이트 | `upsert_investor(name="Y Combinator", investor_type="accelerator")` |
| Phase 2 | `score_company` | 5차원 스코어 기록 (1-10점 × 5 + 종합 0-100) | `score_company(slug="newco", tech_strength=8, market_potential=7)` |
| | `add_company_relation` | 회사 간 관계 (competitor/partner) | `add_company_relation(slug_a="a", slug_b="b", type="competitor")` |
| | `search_investors` | 투자자 검색 | `search_investors(query="Sequoia")` |
| | `get_investor_portfolio` | 투자자별 포트폴리오 | `get_investor_portfolio(slug="sequoia")` |
| | `get_funding_stats` | 펀딩 집계 | `get_funding_stats()` |
| | `manage_collection` | 컬렉션 CRUD | `manage_collection(action="create", name="watchlist")` |
| | `search_people` | 인물 검색 | `search_people(query="CEO")` |
| Phase 3 | `assign_company_topics` | L3 토픽 할당 | `assign_company_topics(slug="newco", topics=["adaptive-rag"])` |
| | `remove_company_topics` | L3 토픽 제거 | `remove_company_topics(slug="newco", topics=["adaptive-rag"])` |

**데이터 현황**: 807개 스타트업, 689건 펀딩, 602명 인물, L3 토픽 매핑 567건
**카테고리**: Service(275), S/W Platform(212), AI 산업 특화(116), Model/Engine(69), Infra(57), Ops(48), Data(30)

**L1/L2/L3 필터 검색**:
```
search_companies(l1="agentic-ai")                    ← L1 도메인 전체
search_companies(l2="hybrid-ai-infra")                ← L2 영역
search_companies(l3_slug="adaptive-rag", country="한국")  ← L3 기술 + 국가
```

**사용 흐름**:
```
[발굴] /startup-scout {도메인} (또는 자연어) → 후보 쇼트리스트
[분석] /startup-analyst {기업명} (또는 자연어) → 심층 리포트 + DB 입력용 JSON
[저장] 사용자 승인 → upsert_company + add_funding_round
[조회] search_companies / get_company → 대시보드 또는 즉석 검색
```

### youtube-transcript — 유튜브 자막 추출

> 유튜브 영상 URL에서 자막(transcript)을 추출하여 텍스트로 반환.

| 도구 | 설명 |
|------|------|
| `get_transcript` | 유튜브 URL → 자막 텍스트 (lang 파라미터로 언어 선택, 기본 en) |

```
get_transcript(url="https://youtube.com/watch?v=...", lang="ko")
```

### context7 — 외부 라이브러리 문서 조회

> 외부 오픈소스 라이브러리/프레임워크의 최신 공식 문서를 실시간 조회. 코딩 작업 시 API 레퍼런스 확인에 활용.

---

## 5. 전체 리서치 사이클

### 단일 분석 사이클 (도구 체인)

어떤 기술 주제든 아래 4단계를 거쳐 의사결정 근거가 만들어진다:

```
① 수집 (Collect)          ② 탐색 (Search)           ③ 분석 (Analyze)         ④ 산출 (Output)
━━━━━━━━━━━━━━━         ━━━━━━━━━━━━━━━          ━━━━━━━━━━━━━━━        ━━━━━━━━━━━━━━━

collect_all ─────────▶ search_intel ──────────▶ /wtis ───────────▶ render_pdf
  │                     (hybrid 검색)            (200점 평가)        (PDF 보고서)
  ├─ collect_papers                                 │                   │
  ├─ collect_arxiv     find_similar ──────────▶ /weekly-monitor ──▶ render_pptx
  ├─ collect_patents     (유사 탐색)             (Tier 1+2)          (발표 자료)
  └─ collect_news                                   │                   │
                       get_weekly_diff ────────▶ /discover ────────▶ obsidian-bridge
                         (주간 변화)              (신기술 탐색)        (옵시디언)
                                                    │                   │
                       get_intel_stats ────────▶ /research-session ─▶ portfolio.md
                         (통계 현황)              (자유 리서치)        (포트폴리오)

     DB에 쌓기              DB에서 꺼내기           판단 + 평가           공유 + 기록
```

### 데이터 흐름 (소스 → DB → 분석 → 산출물)

```
외부 API                    Supabase DB                  분석 엔진                산출물
━━━━━━━━                   ━━━━━━━━━━                  ━━━━━━━━                ━━━━━━

Semantic Scholar ─┐                                  ┌─ /weekly-monitor ──▶ weekly/*.md
                  │     ┌──────────────────┐         │    (Tier 1+2)         weekly/*.pdf
arXiv ────────────┤     │                  │         │
                  ├────▶│   intel_items    │────────▶├─ /wtis ────────────▶ {domain}/final.md
Google Patents ───┤     │   (pgvector +    │         │    (200점 평가)       {domain}/final.pdf
                  │     │    tsvector)     │         │                      portfolio.md
Tavily ───────────┤     │                  │         ├─ /discover ────────▶ discover-*.md
                  │     └──────────────────┘         │    (2×2 매트릭스)
GDELT ────────────┤              │                   ├─ /research-session ▶ {topic}.md
                  │              │                   │    (자유 리서치)
Naver News ───────┘              ▼                   └─ search_intel ─────▶ (즉석 응답)
                        ┌────────────────┐                (실시간 검색)
                        │ trend_snapshots│
                        │ (시계열 비교)   │
                        └────────────────┘
```

---

## 6. 제약 사항

| 제약 | 영향 | 대응 |
|------|------|------|
| **수집해야 검색 가능** | 새 주제는 바로 검색 안 됨 | `collect_all`로 먼저 데이터 수집 |
| **abstract까지만 저장** | 논문/뉴스 전문 열람 불가 | source_url로 원문 이동 |
| **SerpAPI 월 250건** | Google Patents 쿼터 제한 | 필요시 유료 플랜 ($50/5,000건) |
| **Tavily 월 1,000건** | 뉴스 수집 쿼터 제한 | GDELT(무료) + Naver로 자동 보완 |
| **한국어 키워드 검색 한계** | 조사 분리 안 됨 | `mode="hybrid"` → AI 검색이 보완 |
| **실시간이 아님** | 수집 시점 기준 데이터 | 주기적 수집 (weekly-monitor 자동화) |
| **MCP 도구는 터미널 전용** | VSCode 확장에서 MCP 호출 불가 | 터미널 Claude Code 사용 |
