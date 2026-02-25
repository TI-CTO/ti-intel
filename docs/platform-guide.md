# Tech Intelligence Platform — 사용 가이드

> LG U+ 기술전략 인텔리전스를 위한 멀티 에이전트 플랫폼.
> Claude Code + MCP 서버 + Supabase로 구성된 3-레이어 아키텍처.

---

## 1. 플랫폼 개요

이 플랫폼은 **기술 동향 조사, 경쟁사 분석, 과제 제안서 검증**을 자동화한다.
Claude Code의 스킬·에이전트가 5개 MCP 데이터 서버를 오케스트레이션하여 Evidence Chain 기반 보고서를 생성한다.

### 무엇을 할 수 있나?

| 사용 목적 | 사용할 것 |
|-----------|-----------|
| 신규 과제 아이디어 발굴 | `/discover` |
| 특정 기술 동향 조사 | `/research-session` |
| 경쟁사(SKT/KT) 실적 조회 | `telco-factbook` MCP 직접 사용 |
| 학술 논문 검색·저장 | `research-hub` MCP |
| 특허 동향 파악 | `patent-intel` MCP |
| 등록 토픽 정기 모니터링 | `/monitor` |
| 과제 제안서 전체 분석 | `/wtis proposal [파일]` |
| 마크다운 → PPTX 변환 | `/slides` |
| 리서치 결과 → Obsidian 동기화 | `/obsidian-bridge` |

---

## 2. 아키텍처

```
┌──────────────────────────────────────────────────────┐
│                  Layer 3 · WTIS                      │
│          /wtis — 종합 인텔리전스 오케스트레이터         │
└──────────────────┬───────────────────────────────────┘
                   │ 위임
┌──────────────────▼───────────────────────────────────┐
│              Layer 2 · Core Capabilities             │
│                                                      │
│  스킬        discover  monitor  research-session     │
│  에이전트    research-deep  validator                │
└──────┬────────────────────────────────────┬──────────┘
       │ MCP 호출                            │ 파일 핸드오프
┌──────▼───────────────────────────────────▼──────────┐
│              Layer 1 · MCP 데이터 서버               │
│                                                      │
│  telco-factbook   trend-tracker   research-hub       │
│  patent-intel     design-system                      │
└──────────────────────┬───────────────────────────────┘
                       │
                  ┌────▼────┐
                  │Supabase │  (tech-intel 프로젝트)
                  └─────────┘
```

### 레이어 설명

**Layer 1 — MCP 데이터 서버**: 각 `projects/` 폴더가 독립 MCP 서버로 실행됨. 데이터 수집·저장·조회 담당.

**Layer 2 — Core Capabilities**: 스킬과 에이전트. 여러 MCP 서버를 조합해 분석 수행. 결과를 파일로 저장하여 다음 단계로 전달.

**Layer 3 — WTIS**: LG U+ 도메인 특화 오케스트레이터. Layer 2를 조합하여 완성된 인텔리전스 보고서 생성.

---

## 3. 컴포넌트 레퍼런스

> 파라미터 전체 레퍼런스(예시 포함): [command-reference.md](command-reference.md)

### 스킬 (사용자 직접 호출 가능)

| 스킬 | 호출 | 설명 |
|------|------|------|
| **wtis** | `/wtis [mode] [입력]` | 종합 기술 인텔리전스. 제안서 분석·과제 검증·발굴 |
| **discover** | `/discover [domain]` | 신기술 기회 발굴, 2×2 우선순위 매트릭스 |
| **monitor** | `/monitor [topic]` | 등록 토픽 모니터링, 변화 감지 리포트 |
| **research-session** | `/research-session [주제]` | 구조화된 리서치. MCP + 웹 통합 조사 |
| **slides** | `/slides [마크다운 파일]` | 마크다운 → PPTX (3가지 테마) |
| **obsidian-bridge** | `/obsidian-bridge [파일]` | 산출물을 Obsidian 볼트로 동기화 |
| **work-log** | `/work-log` | 현재 세션 작업 내용을 Obsidian 업무일지에 기록 |
| **new-project** | `/new-project [이름]` | 새 MCP 서버 프로젝트 표준 스캐폴딩 |

### 에이전트 (스킬 내부에서 자동 호출)

| 에이전트 | 모델 | 역할 |
|----------|------|------|
| **research-deep** | sonnet | 다중 소스 심층 조사. 결과를 파일로 저장 |
| **validator** | sonnet | Black-box 검증. 인용·수치·논리 독립 검증 |
| **researcher** | haiku | 빠른 탐색·비교 분석 (읽기 전용) |
| **reviewer** | sonnet | 코드 품질·보안 리뷰 (읽기 전용) |
| **implementer** | sonnet | 코드 작성·수정·테스트 |

### MCP 서버 도구

| 서버 | 주요 도구 |
|------|-----------|
| **telco-factbook** | `get_financial_metrics`, `compare_carriers`, `get_revenue_trend`, `get_subscriber_data` |
| **trend-tracker** | `search_news`, `get_trend_timeline`, `compare_snapshots`, `upsert_news`, `manage_watch_topics` |
| **research-hub** | `search_papers`, `get_trending_papers`, `get_paper_stats` |
| **patent-intel** | `search_patents`, `get_recent_patents`, `get_patent_stats` |
| **design-system** | `render_pptx`, `list_themes`, `get_theme` |

### 공유 토픽 슬러그 (Supabase `topics` 테이블)

```
ai-network  |  6g  |  network-slicing  |  edge-computing
quantum-comm  |  llm-telecom  |  open-ran  |  digital-twin
```

---

## 4. 설치 및 초기 설정

```bash
# 1. 저장소 클론
git clone git@github.com:TI-CTO/ti-intel.git
cd ti-intel

# 2. 환경 변수 설정 (각 프로젝트)
cp projects/telco-factbook/.env.example projects/telco-factbook/.env
cp projects/trend-tracker/.env.example projects/trend-tracker/.env
cp projects/research-hub/.env.example projects/research-hub/.env
cp projects/patent-intel/.env.example projects/patent-intel/.env
# 각 .env 파일에 Supabase URL과 KEY 입력

# 3. MCP 설정
cp .mcp.json.example .mcp.json
# .mcp.json의 supabase 섹션에 project_ref와 PAT 입력

# 4. 의존성 설치 (각 프로젝트)
cd projects/telco-factbook && uv sync && cd ../..
cd projects/trend-tracker && uv sync && cd ../..
cd projects/research-hub && uv sync && cd ../..
cd projects/patent-intel && uv sync && cd ../..
```

> **Supabase 연결 정보**는 팀 관리자에게 문의. `.env`와 `.mcp.json`은 `.gitignore`에 등록되어 있어 커밋되지 않는다.

---

## 5. 사용 예시 — Best Practices

### Recipe 1: 신규 기술 트렌드 빠르게 파악

```
/wtis quick 2026년 국내 통신사 AI 에이전트 서비스 현황
```

**흐름**: `research-deep` 에이전트 단독 → WebSearch + trend-tracker + research-hub → 빠른 리포트
**소요 시간**: ~5분
**결과물**: 터미널 출력 (파일 저장 선택)

---

### Recipe 2: 논문·특허 기반 심층 기술 분석

```
/research-session 6G 테라헤르츠 통신 최신 연구 동향
```

**흐름**:
1. `research-hub.search_papers(topic="6g", query="terahertz")` → Semantic Scholar 논문 수집
2. `patent-intel.search_patents(topic="6g", query="terahertz")` → USPTO 특허 검색
3. `trend-tracker.search_news(topic="6g")` → 최신 뉴스 보완
4. 종합 리서치 노트 → `outputs/reports/2026-02-25_6g-terahertz.md` 저장

**결과물**: Evidence Chain 포함 마크다운 (출처·신뢰도 태그 포함)

---

### Recipe 3: 과제 제안서 전체 검증 파이프라인

```
/wtis proposal projects/my-proposal.md
```

**흐름**:
```
SKILL-0 (파싱) → research-deep (심층 조사) → SKILL-1 (선정검증) → validator (교차검증)
```

**SKILL-1이 "부적합" 판정 시 파이프라인 자동 중단**, 사유 보고.
**결과물**: `outputs/reports/{date}_wtis-proposal-{slug}-final.md`

---

### Recipe 4: 경쟁사 실적 비교 + 장표

```
# Step 1: 데이터 조회 (MCP 직접)
"SKT와 KT의 2025년 연간 매출과 영업이익을 비교해줘"
→ telco-factbook.compare_carriers() 자동 호출

# Step 2: 조사 결과를 장표로
/slides outputs/reports/2026-02-25_carrier-comparison.md
```

**흐름**: telco-factbook → 분석 → 마크다운 → design-system.render_pptx()
**결과물**: `.pptx` 파일 (professional 테마 기본)

---

### Recipe 5: 신기술 발굴 → 전략 보고서

```
/wtis deep B2B AI 솔루션 기회 탐색
```

**흐름**:
1. `discover` 스킬: research-hub + patent-intel + WebSearch → 2×2 우선순위 매트릭스
2. `research-deep` 에이전트: 상위 후보 심층 조사
3. `SKILL-1`: LG U+ 전략 적합성 판단 (3B 전략: Build/Buy/Partner)
4. `validator`: 결론 교차검증

**결과물**: 전략 보고서 + Obsidian 동기화 안내

---

### Recipe 6: 정기 모니터링 → Obsidian 저장

```
# 모든 watch_topics 스캔
/monitor

# 특정 토픽만
/monitor open-ran
```

**흐름**: watch_topics 조회 → trend-tracker.compare_snapshots() → 변화 감지(🟢/🟡/🔴) → 스냅샷 저장
**결과물**: 변화 감지 리포트 → `/obsidian-bridge`로 볼트 동기화

---

### Recipe 7: 새 MCP 서버 추가

새로운 데이터 소스가 필요할 때 (예: 스타트업 투자 데이터):

```
/new-project startup-intel
```

**생성 구조**:
```
projects/startup-intel/
├── CLAUDE.md          ← 도메인 컨텍스트
├── pyproject.toml
├── src/startup_intel/
│   ├── mcp_server.py  ← MCP 도구 정의
│   ├── models.py
│   └── db/repository.py
└── tests/
```

이후 `.mcp.json`에 등록하면 모든 스킬에서 바로 접근 가능.

---

## 6. 데이터 흐름 및 파일 핸드오프

에이전트 간 데이터는 **파일 경로**로 전달된다 (컨텍스트 오염 방지).

```
연구 세션 파일: outputs/reports/YYYY-MM-DD_{slug}.md
WTIS 중간 산출물:
  - skill0  → outputs/reports/{date}_wtis-proposal-{slug}-skill0.md
  - research → outputs/reports/{date}_wtis-proposal-{slug}-research.md
  - skill1  → outputs/reports/{date}_wtis-proposal-{slug}-skill1.md
  - final   → outputs/reports/{date}_wtis-proposal-{slug}-final.md
```

모든 결과 파일에 포함되는 표준 필드:
```yaml
status: pass | fail | uncertain
summary: (200자 이내 요약)
file_path: (저장 경로)
```

---

## 7. 신뢰도 태그 (Evidence Chain)

모든 보고서에서 출처는 아래 태그로 분류된다:

| 태그 | 의미 | 예시 |
|------|------|------|
| `[A]` | 공식 자료 | 기업 IR, 정부 발표, 표준 문서 |
| `[B]` | 공신력 있는 2차 출처 | 학술 논문, 주요 언론 |
| `[C]` | 지시적 자료 | 업계 블로그, 분석사 보고서 |
| `[D]` | 미검증 | 소셜미디어, 익명 출처 |

`[D]` 단독 근거로 결론 도달 시 → `confidence: low` 처리.

---

## 8. 자주 쓰는 패턴 정리

```
빠른 조사        /wtis quick {질문}
구조화 조사      /research-session {주제}
신기술 발굴      /discover {도메인}  또는  /wtis deep {주제}
제안서 검증      /wtis proposal {파일경로}
정기 모니터링    /monitor  또는  /monitor {topic-slug}
결과 시각화      /slides {마크다운 파일}
Obsidian 동기화  /obsidian-bridge {파일}
작업 기록        /work-log
```

---

## 9. 파일 구조 참조

```
ti-intel/
├── .claude/
│   ├── agents/          ← 에이전트 정의 (*.md)
│   ├── skills/          ← 스킬 정의 (*/SKILL.md)
│   └── rules/           ← 코딩 컨벤션
├── docs/                ← 설계 문서 (이 파일 포함)
├── projects/            ← MCP 서버 프로젝트
│   ├── telco-factbook/
│   ├── trend-tracker/
│   ├── research-hub/
│   ├── patent-intel/
│   └── design-system/
├── outputs/
│   ├── reports/         ← 모든 스킬/에이전트 산출물
│   └── summaries/       ← 종합 정리
├── references/          ← 리포트 참조 파일 (PDF, 사내 문서)
├── .mcp.json.example    ← MCP 서버 설정 템플릿
└── CLAUDE.md            ← 전역 컨텍스트
```
