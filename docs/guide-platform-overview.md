# Tech Intelligence Platform — 사용 가이드

> AI 기반 기술 인텔리전스 시스템.
> 주간 동향 모니터링부터 과제 Go/No-Go 판정까지, 일관된 파이프라인으로 의사결정을 지원한다.

---

## 1. 시스템 전체 구조

```
                    ┌─────────────────────────┐
                    │   기술 분류 체계 (L1/L2/L3)  │
                    └────────┬────────────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
    Agentic AI          Voice AI              Secure AI
    (L2 5개, L3 12개)   (L2 3개, L3 8개)      (L2 2개, L3 5개)
         │                   │                   │
         ▼                   ▼                   ▼
  ┌──────────────────────────────────────────────────┐
  │              Weekly Monitor (주간 동향)             │
  │  L1 도메인 단위로 L3 25개를 매주 스캔               │
  │  "이번 주 무슨 일이 있었나?"                        │
  └──────────────────┬───────────────────────────────┘
                     │ 🔴 긴급 시그널 발견 시
                     ▼
  ┌──────────────────────────────────────────────────┐
  │                  WTIS v4.1 (과제 검증)              │
  │  L2 기술 단위로 Go/No-Go 판정 + 200점 채점          │
  │  "이 과제를 해야 하나? 어떤 전략으로?"                │
  └──────────────────┬───────────────────────────────┘
                     │
                     ▼
  ┌──────────────────────────────────────────────────┐
  │              포트폴리오 (L1 도메인별)                │
  │  L2 평가 결과를 종합한 기술 투자 현황판               │
  └──────────────────────────────────────────────────┘
```

### 기술 분류 체계

| L1 도메인 | L2 기술 | L3 세부기술 |
|-----------|---------|------------|
| **Agentic AI** (12) | Self Evolving Architecture | Agentic Context Engineering |
| | Model & Delta Foundry | FeedbackOps, EvaluationOps, 학습-배포 파이프라인, GPU Orchestration |
| | Trusted Multi-Agent | Agent Orchestration, Agent Oriented Orchestration |
| | Hybrid AI Infra | On-Device sLM, 실시간 화자분할, Edge AI, 5G SA/6G |
| | 의도 파악 기술 | Adaptive RAG |
| **Voice AI** (8) | Speech Perception | Emotional Analysis, Context Recognition, Interrupt & Turn-Taking |
| | Personal Intelligence | 페르소나 플러그인, 관계 그래프, 컨텍스트 액션 추천 |
| | Speech Generation | Voice Cloning, Voice Synthesis |
| **Secure AI** (5) | 스팸/피싱탐지 | 스팸/피싱 감지(통화전), OCR 이미지 스팸 |
| | 양자/동형 암호 | PQC 통화녹음 암호화, 동형암호 키워드 검색, Secure Vector Search |

---

## 2. Weekly Monitor — 주간 기술 동향

### 목적

매주 3개 도메인의 L3 세부기술을 스캔하여 **변화를 감지**한다.
판정(Go/No-Go)은 하지 않고, **팩트 수집과 신호 감지**에 집중한다.

### 2단계 파이프라인

```
Tier 1: 빠른 스캔 (~5분)
  전체 L3에 대해 뉴스·논문을 빠르게 검색
  → 신호등 판정: 🟢 평온 / 🟡 주목 / 🔴 긴급

Tier 2: 심층 리서치 (~10분, 🟡🔴만)
  변화가 감지된 L3에 대해 논문·특허·뉴스를 종합 수집
  → L3별 개별 심층 리서치 파일 생성
```

### 주간 스케줄

| 요일 | 도메인 | L3 수 |
|------|--------|-------|
| **월** | Agentic AI | 12개 |
| **화** | Voice AI | 8개 |
| **수** | Secure AI | 5개 |

### 호출 방법

```
/weekly-monitor agentic-ai
/weekly-monitor voice-ai
/weekly-monitor secure-ai
```

### 산출물

```
outputs/reports/weekly/
  YYYY-MM-DD_weekly-{domain}.md                ← 메인 리포트 (전체 L3 요약)
  YYYY-MM-DD_weekly-{domain}.professional.pdf  ← PDF 버전
  YYYY-MM-DD_research-{l3-slug}.md             ← Tier 2 심층 (해당 L3만)
```

---

## 3. WTIS v4.1 — 과제 검증 시스템

### 목적

특정 L2 기술에 대해 **Go/No-Go 판정**, **200점 채점**, **3B 전략(Buy/Borrow/Build)**을 산출한다.
"하나의 판정 = 하나의 의사결정" 원칙.

### 3가지 모드

| 모드 | 언제 쓰나 | 입력 | 산출물 |
|------|-----------|------|--------|
| **proposal** | 과제 제안서가 있을 때 | 제안서 텍스트 또는 파일 | Go/No-Go + 200점 채점 + 전략 |
| **standard** | 과제 타당성 검증 | 검증 대상 기술/주제 | Go/No-Go + 200점 채점 + 전략 |
| **deep** | 신규 기회 발굴 | 도메인 + 탐색 방향 | 기회 목록 + 선정검증 |

### 파이프라인 (proposal 기준)

```
제안서 입력
  → SKILL-0: 파싱 → Analysis Brief (L1 도메인 + L2 기술 자동 식별)
  → research-deep: 논문·특허·뉴스 심층 수집
  → SKILL-1: 200점 채점 + Go/No-Go 판정 + 3B 전략
  → validator: 독립 교차검증 (Black-box)
  → 최종 보고서 → 포트폴리오 자동 갱신 → PDF
```

### 200점 채점 기준

| 대분류 | 배점 |
|--------|------|
| 고객가치 | 40점 |
| 시장매력도 | 40점 |
| 기술경쟁력 | 40점 |
| 경쟁우위 | 40점 |
| 실행가능성 | 40점 |
| **합계** | **200점** |

### 판정 기준

| 점수 | 판정 | 의미 |
|------|------|------|
| 140+ | **Go** | 추진 권고 |
| 100~139 | **Conditional Go** | 조건부 추진 (리스크 해소 필요) |
| ~99 | **No-Go** | 보류 또는 재검토 |

### 포트폴리오

L1 도메인별로 L2 평가 결과를 종합한 현황판:

```
outputs/reports/{domain}/portfolio.md

| L2 기술 | 최근 평가일 | 점수 | 판정 | 전략 |
|---------|-----------|------|------|------|
| 양자동형암호 | 2026-03-05 | 128/200 | Conditional Go | Borrow |
| OnDevice AI | — | — | 미평가 | — |
```

---

## 4. Weekly Monitor ↔ WTIS 연결

```
weekly-monitor                       WTIS
──────────────                       ────
L1 도메인 전체 스캔                    L2 기술 하나에 집중
팩트 수집 + 신호 감지                  Go/No-Go 판정 + 전략
매주 정기 실행                        필요 시 수시 실행
판정 없음                            200점 채점 + 3B

         🔴 긴급 시그널 발견
         ─────────────────→    /wtis standard {L2} 검증
                               (주간 리서치를 선행 지식으로 재활용)
```

---

## 5. 데이터 소스

| 소스 | 데이터 | 역할 |
|------|--------|------|
| **intel-store** | 논문(Semantic Scholar/arXiv) + 특허(Google Patents) + 뉴스(Tavily/GDELT/Naver) | 통합 수집·검색·저장 |
| **WebSearch** | 실시간 웹 검색 | 최신 뉴스, 기업 발표, 블로그 |
| **trend-tracker** | 트렌드 스냅샷 | 주간 비교, 변화 감지 |
| **design-system** | PDF/PPTX 렌더링 | 컨설팅 스타일 리포트 생성 |

---

## 6. 설치 및 초기 설정

```bash
# 1. 저장소 클론
git clone <your-repo-url>
cd ti-intel

# 2. 환경 변수 설정 (각 프로젝트)
cp projects/intel-store/.env.example projects/intel-store/.env
cp projects/trend-tracker/.env.example projects/trend-tracker/.env
# 각 .env 파일에 Supabase URL과 KEY 입력

# 3. MCP 설정
cp .mcp.json.example .mcp.json

# 4. 의존성 설치 (각 프로젝트)
cd projects/intel-store && ~/.local/bin/uv sync && cd ../..
cd projects/trend-tracker && ~/.local/bin/uv sync && cd ../..
cd projects/design-system && ~/.local/bin/uv sync && cd ../..
```

> **Supabase 연결 정보**는 팀 관리자에게 문의. `.env`와 `.mcp.json`은 `.gitignore`에 등록되어 있어 커밋되지 않는다.

---

## 7. 자주 쓰는 패턴 정리

```
구조화 조사      /research-session {주제}
신기술 발굴      /discover {도메인}  또는  /wtis deep {주제}
제안서 검증      /wtis proposal {파일경로}
정기 모니터링    /weekly-monitor {domain}
결과 시각화      /slides {마크다운 파일}
PDF 변환        /report-pdf {마크다운 파일}
Obsidian 동기화  /obsidian-bridge {파일}
작업 기록        /work-log
```

---

## 8. 스킬 체이닝

스킬 간 연결 관계와 데이터 흐름은 별도 가이드 참조:
→ `docs/guide-skill-chaining.md` — 전체 체이닝 맵, I/O Contract 요약, 워크플로우 시나리오

모든 분석 스킬은 통일된 I/O Contract(Input/Output/Return)를 갖고 있으며,
각 SKILL.md에 `## I/O Contract` 섹션과 `## Next Steps` 섹션이 정의되어 있다.

---

## 9. 파일 구조 참조

```
ti-intel/
├── .claude/
│   ├── agents/          ← 에이전트 정의 (*.md)
│   ├── skills/          ← 스킬 정의 (*/SKILL.md) — I/O Contract + Next Steps 포함
│   └── rules/           ← 코딩 컨벤션
├── docs/                ← 설계·가이드 문서 (원본, git 관리)
├── projects/            ← MCP 서버 프로젝트
│   ├── intel-store/     ← 통합 인텔리전스 (논문·특허·뉴스)
│   ├── trend-tracker/   ← 트렌드 스냅샷
│   ├── design-system/   ← PDF/PPTX 렌더링
│   └── telco-factbook/  ← SKT/KT 재무 지표 (CLI 전용)
├── outputs/
│   └── reports/         ← 모든 스킬/에이전트 산출물
├── references/          ← 리포트 참조 파일 (PDF, 사내 문서)
├── scripts/             ← 유틸리티 스크립트
├── .mcp.json.example    ← MCP 서버 설정 템플릿
└── CLAUDE.md            ← 전역 컨텍스트
```
