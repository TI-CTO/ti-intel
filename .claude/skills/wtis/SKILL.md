---
name: wtis
description: "Winning Tech Intelligence System v4.1 — LG U+ 기술전략 인텔리전스. L2 기술 단위 분석, 포트폴리오 관리, 선정/진행 검증을 수행한다."
user-invokable: true
argument-hint: "[proposal|quick|standard|deep] [query or file path]"
---

# WTIS v4.1 Orchestrator

LG U+ Winning Tech Intelligence System의 오케스트레이터.
v4.1: L2 단위 분석 + 포트폴리오 구조 전환.
- 분석 단위를 L1(도메인) → L2(기술)로 전환. "하나의 판정 = 하나의 의사결정"
- L1 도메인별 포트폴리오로 L2 평가 결과를 종합
- 파이프라인 흐름(SKILL-0→research-deep→SKILL-1→validator→final)은 유지
- 바뀌는 것: 입력 범위(L2), 폴더 구조(도메인 계층), 후처리(포트폴리오 자동 갱신)

## 빠른 시작 — 모드별 치트시트

| 모드 | 언제 쓰나 | 호출 예시 | 소요 시간 |
|------|-----------|-----------|----------|
| **standard** | 과제 타당성 검증 | `/wtis AI-RAN 과제 Go/No-Go 검증` | ~10분 |
| **deep** | 신규 기회 발굴 | `/wtis edge AI 기회 탐색 및 전략 비교` | ~15분 |
| **proposal** | 제안서 전체 분석 | `/wtis proposal.md` | ~20분 |

> **동향/트렌드 파악**은 `/weekly-monitor {domain}`을 사용하세요 (quick 모드 대체).

**자동 모드 감지 키워드:**
- `동향 / 트렌드 / 뉴스` → `/weekly-monitor`로 안내
- `검증 / 타당성 / Go/No-Go` → standard
- `발굴 / 탐색 / 전략 / 비교` → deep
- `제안서` 또는 `.md` 파일 경로 → proposal

**PDF 자동 생성:** 모든 모드에서 최종 리포트 완료 후 PDF가 함께 생성됩니다.

---

## 변경 이력

### v4.0 → v4.1 변경점

| 항목 | v4.0 | v4.1 |
|------|------|------|
| 분석 단위 | L1 도메인 전체 | **L2 기술 단위** |
| 폴더 구조 | `{date}_{slug}/` | `{domain}/{date}_{slug}/` |
| 포트폴리오 | 없음 | **L1 도메인별 portfolio.md 자동 갱신** |
| SKILL-0 | 도메인만 식별 | **L1 도메인 + L2 기술 식별** |
| Post-Report | PDF만 생성 | **포트폴리오 갱신 → PDF 생성** |
| Final Report | domain 필드 없음 | `domain`, `l2_topic` frontmatter 추가 |

### v3.0 → v4.0 변경점

| 스킬 | v3.0 | v4.0 |
|------|------|------|
| SKILL-0 파서 | 내부 실행 | **내부 유지** (도메인 전용) |
| SKILL-1 선정검증 | 내부 실행 | **내부 유지** (도메인 전용) |
| SKILL-2 진행검증 | 내부 실행 | **내부 유지** (도메인 전용) |
| SKILL-3 발굴 | 내부 실행 | → **`discover` 스킬** 위임 + 도메인 파라미터 전달 |
| SKILL-4 데이터수집 | 내부 실행 | → **`research-deep` 에이전트** 위임 + 도메인 파라미터 전달 |
| SKILL-5 교차검증 | 내부 실행 | → **`validator` 에이전트** 위임 |

## Modes

| Mode | Trigger | Description |
|------|---------|-------------|
| **proposal** | 과제 제안서 입력 (텍스트 or 파일 경로) | 제안서 파싱 → 심층 리서치 → 선정검증 → 교차검증 |
| **standard** | 과제 검증 요청, 정기 보고 | research-deep + SKILL-1 or 2 + validator |
| **deep** | 신규 과제 발굴, 전략적 의사결정 | discover + research-deep + SKILL-1 + validator |

> **quick 모드 폐지 (v4.1)**: 기존 quick의 역할(동향/현황 파악)은 `/weekly-monitor`의 Tier 2 심층 리서치가 대체한다. "동향", "트렌드" 질문은 → `/weekly-monitor {domain}` 안내.

사용자가 모드를 지정하지 않으면 입력 내용으로 자동 판정한다:
- "제안서", "proposal", 파일 경로 포함 → **proposal**
- "동향", "트렌드", "뉴스", 단순 질문 → `/weekly-monitor`로 안내
- "검증", "타당성", "Go/No-Go" → **standard**
- "발굴", "탐색", "전략", "비교" → **deep**

## Core Principles

1. **오케스트레이터는 라우팅만 한다** — 직접 분석하지 않고 Layer 2 또는 내부 스킬에 위임
2. **결과는 파일로 저장** — 모든 서브에이전트는 결과를 파일에 쓰고, 오케스트레이터는 요약만 수신
3. **레퍼런스 체인 유지** — 모든 주장은 출처까지 추적 가능해야 한다
4. **검증 독립성** — validator는 분석 컨텍스트 없이 독립 실행 (Black-box)
5. **도메인 파라미터** — Layer 2 호출 시 항상 LG U+ 도메인 설정 전달

## Domain Parameters
LG U+ 도메인 설정: `/Users/ctoti/Project/ClaudeCode/.claude/skills/wtis/references/domain-params.md`

## Internal Subagent Prompts (SKILL-0/1/2)
- SKILL-0: `/Users/ctoti/Project/ClaudeCode/.claude/skills/wtis/subprompts/skill-0-proposal.md`
- SKILL-1: `/Users/ctoti/Project/ClaudeCode/.claude/skills/wtis/subprompts/skill-1-selection.md`
- SKILL-2: `/Users/ctoti/Project/ClaudeCode/.claude/skills/wtis/subprompts/skill-2-progress.md`

## Layer 2 Capabilities (SKILL-3/4/5 대체)
- `discover` 스킬 → `.claude/skills/discover/SKILL.md`
- `research-deep` 에이전트 → `.claude/agents/research-deep.md`
- `validator` 에이전트 → `.claude/agents/validator.md`

## Reference Documents
- 기존 리서치: `/Users/ctoti/Project/ClaudeCode/outputs/reports/{domain}/`
- 기술 분류체계: `/Users/ctoti/Project/ClaudeCode/.claude/skills/wtis/references/tech-taxonomy.md`

---

## Phase 0: 기존 리서치 확인 (모든 모드 공통 선행 단계)

모든 모드 실행 전, `outputs/reports/{domain}/`에서 관련 기존 분석을 검색한다.

### 폴더 계층 구조
```
outputs/reports/
  {domain}/                         ← L1 도메인 (secure-ai / agentic-ai / axops)
    portfolio.md                    ← 포트폴리오 (L2 분석 후 자동 갱신)
    portfolio.professional.pdf
    {date}_{slug}/                  ← L2 분석 세션
      final.md                     # 최종 보고서
      final.professional.pdf       # PDF 변환
      skill0.md                    # SKILL-0 결과 (중간 산출물)
      research.md                  # research-deep 결과 (중간 산출물)
      skill1.md                    # SKILL-1 결과 (중간 산출물)
      validator.md                 # validator 결과 (중간 산출물)
      discover.md                  # discover 결과 (deep mode, 중간 산출물)
  weekly/                           ← 주간 모니터링 (기존 유지)
```

### 검색 대상 파일
```
outputs/reports/{domain}/*/final.md         # WTIS 최종 리포트
outputs/reports/{domain}/*/research.md      # research-deep 결과
outputs/reports/{domain}/*/discover.md      # discover 결과
outputs/reports/{domain}/portfolio.md       # 포트폴리오 종합
```
(skill0, skill1, validator 파일은 제외 — 중간 산출물)

### 키워드 매칭 방법
1. 사용자 쿼리에서 핵심 키워드 2~4개 추출
2. 각 후보 파일에 대해:
   - **파일명** kebab-case 토큰과 키워드 겹침 확인
   - **frontmatter `topic`** 필드에 키워드 포함 여부 확인
3. 하나라도 매칭되면 후보로 선정

### 결과 분류 및 처리
```
매칭 없음 → prior_reports = []  → 전체 분석 실행 (기본 흐름)

매칭 있음 (최근 ≤ 30일):
  → prior_reports에 추가
  → Announcement에 표시
  → research-deep 지시: "이전 분석 대비 변화점에 집중, 동일 결론 반복 불필요"
  → Final Report에 ## 이전 분석 대비 변화 섹션 추가

매칭 있음 (31~180일):
  → prior_reports에 추가 (참조용)
  → research-deep 지시: "이전 분석 결과를 선행 지식으로 활용"
  → Final Report에 ## 이전 분석 대비 변화 섹션 추가
```

### 관련 파일 로딩
매칭 파일은 frontmatter만 읽어 요약한다 (전체 내용 읽기 불필요):
- `topic`, `date`, `confidence`, `verdict`(있으면), `score`(있으면) 값 추출
- `## 경영진 요약` 섹션 앞 5줄만 발췌

### 빠른 시작

```
기존 리포트 스캔 결과:
  ✓ 관련 리포트 2건 발견 (secure-ai 도메인)
    - secure-ai/2026-03-03_secure-ai-v2/final.md  (0일 전 | Conditional Go | 120/200)
    - secure-ai/2026-02-26_secure-ai-v1/final.md  (5일 전 | Conditional Go | 128/200)
  → 변화 추이 비교 모드 활성화
```

---

## Execution Flows

### Proposal Mode (핵심 파이프라인)

```
사용자: 과제 제안서 입력
    │
    ├─ [0] Phase 0: 기존 리서치 확인 (위 "Phase 0" 섹션 절차 실행)
    │   └─ prior_reports 목록 구성
    │   └─ 있으면 → Announcement에 건수 표시, research-deep 지시에 반영
    │
    ├─ [0.5] 세션 폴더 생성
    │   └─ {domain}은 SKILL-0이 식별하거나, 사용자가 명시
    │   └─ mkdir -p outputs/reports/{domain}/{date}_{slug}/
    │
    ├─ [1] SKILL-0 실행 (subagent_type: researcher, model: sonnet)
    │   └─ 프롬프트: skill-0-proposal.md 로드
    │   └─ 제안서 파싱 → Analysis Brief 생성 (domain, l2_topic 필드 포함)
    │   └─ 결과 파일: outputs/reports/{domain}/{date}_{slug}/skill0.md
    │
    ├─ [2] research-deep 에이전트 호출 (Layer 2 위임)
    │   └─ 입력: SKILL-0 결과 파일 경로 + 도메인 파라미터
    │   └─ 지시: "WTIS 제안서 분석을 위한 심층 리서치. domain-params.md의 소스 우선순위 준수"
    │   └─ 결과 파일: outputs/reports/{domain}/{date}_{slug}/research.md
    │
    ├─ [3] SKILL-1 실행 (subagent_type: researcher, model: opus)
    │   └─ 프롬프트: skill-1-selection.md 로드
    │   └─ 입력: SKILL-0 Brief 파일 + research-deep 결과 파일 (경로 2개 전달)
    │   └─ 선정검증 + 3B 전략 제언
    │   └─ 결과 파일: outputs/reports/{domain}/{date}_{slug}/skill1.md
    │   └─ status: fail → 파이프라인 중단, "부적합" 사유 보고
    │
    ├─ [4] validator 에이전트 호출 (Layer 2 위임)
    │   └─ 입력: SKILL-1 결과 파일 경로 (독립 검증, Black-box)
    │   └─ status: fail → SKILL-1 1회 재실행 후 재검증
    │
    ├─ [4-1] 보강 루프 (Reinforcement Loop) — 조건부 실행
    │   └─ 조건: validator status가 "partial" 또는 "uncertain"이고 "단일 소스" 항목 존재
    │   └─ research-deep 재호출: validator가 식별한 단일 소스 주장만 타겟 검색
    │   └─ 지시: "다음 주장들에 대해 독립 소스 1개 이상 추가 확보: {claims list}"
    │   └─ 결과: 기존 research.md에 보강 섹션 추가 (별도 파일 아님)
    │   └─ SKILL-1 재실행하지 않음 (보강 데이터는 다음 파이프라인에서 반영)
    │   └─ 최대 1회만 실행 (무한 루프 방지)
    │
    ├─ [5] 최종 보고서 생성
    │   └─ 경로: outputs/reports/{domain}/{date}_{slug}/final.md
    │
    ├─ [5.5] 포트폴리오 갱신 (자동)
    │   └─ outputs/reports/{domain}/portfolio.md 읽기 (없으면 신규 생성)
    │   └─ 현재 L2의 점수/판정/전략을 해당 행에 업데이트
    │   └─ 종합 권고 섹션 재생성
    │   └─ 평가 이력 행 추가
    │
    └─ [6] PDF 생성
        └─ design-system MCP → render_pdf(final.md) → final.professional.pdf
        └─ design-system MCP → render_pdf(portfolio.md) → portfolio.professional.pdf
```

### Quick Mode — 폐지 (v4.1)

> `/weekly-monitor {domain}`의 Tier 2 심층 리서치로 대체됨.
> 사용자가 "동향", "트렌드" 질문 시 `/weekly-monitor`로 안내한다.

### Standard Mode

```
사용자: 과제 검증 요청
    │
    ├─ [0] Phase 0: 기존 리서치 확인 (outputs/reports/{domain}/ 검색)
    │   └─ prior_reports 있으면 SKILL-1/2에 이전 판정 컨텍스트 전달
    │
    ├─ [0.5] 세션 폴더 생성
    │   └─ mkdir -p outputs/reports/{domain}/{date}_{slug}/
    │
    ├─ research-deep 에이전트 호출 (Layer 2 위임)
    │   └─ 입력: 검증 대상 + 도메인 파라미터 + prior_reports (있으면)
    │   └─ 결과 파일: outputs/reports/{domain}/{date}_{slug}/research.md
    │
    ├─ SKILL-1 또는 SKILL-2 실행 (선정 또는 진행 검증)
    │   └─ 결과 파일: outputs/reports/{domain}/{date}_{slug}/skill1.md
    │
    ├─ validator 에이전트 호출 (Layer 2 위임)
    │   └─ 결과 파일: outputs/reports/{domain}/{date}_{slug}/validator.md
    │
    ├─ 최종 보고서 생성
    │   └─ 경로: outputs/reports/{domain}/{date}_{slug}/final.md
    │
    ├─ [5.5] 포트폴리오 갱신 (자동)
    │
    └─ [자동] design-system MCP → render_pdf(final.md + portfolio.md)
```

### Deep Mode

```
사용자: 전략적 발굴/분석 요청
    │
    ├─ [0] Phase 0: 기존 리서치 확인 (outputs/reports/{domain}/ 검색)
    │   └─ prior_reports 있으면 discover에 "이미 파악된 기회 중복 제외" 지시
    │
    ├─ [0.5] 세션 폴더 생성
    │   └─ mkdir -p outputs/reports/{domain}/{date}_{slug}/
    │
    ├─ [1] discover 스킬 호출 (Layer 2 위임) — SKILL-3 대체
    │   └─ 입력: 도메인 + domain-params.md의 competitors, taxonomy 전달
    │   └─ prior_reports 있으면: "기존 포트폴리오" 파라미터로 전달 (중복 방지)
    │   └─ 결과 파일: outputs/reports/{domain}/{date}_{slug}/discover.md
    │
    ├─ [2] research-deep 에이전트 호출 (Layer 2 위임) — SKILL-4 대체
    │   └─ 입력: discover 결과 파일 + 도메인 파라미터 + prior_reports (있으면)
    │   └─ 결과 파일: outputs/reports/{domain}/{date}_{slug}/research.md
    │
    ├─ [3] SKILL-1 실행 (subagent_type: researcher, model: opus)
    │   └─ discover + research-deep 결과를 입력으로 전달
    │   └─ 결과 파일: outputs/reports/{domain}/{date}_{slug}/skill1.md
    │
    ├─ [4] validator 에이전트 호출 (Layer 2 위임) — SKILL-5 대체
    │   └─ 결과 파일: outputs/reports/{domain}/{date}_{slug}/validator.md
    │
    ├─ [5] 최종 보고서 생성
    │   └─ 경로: outputs/reports/{domain}/{date}_{slug}/final.md
    │
    ├─ [5.5] 포트폴리오 갱신 (자동)
    │
    └─ [6] design-system MCP → render_pdf(final.md + portfolio.md)
```

---

## Layer 2 호출 시 도메인 파라미터 전달 방법

`discover` 또는 `research-deep` 호출 시 아래를 항상 포함:

```
## WTIS 도메인 컨텍스트
참조: /Users/ctoti/Project/ClaudeCode/.claude/skills/wtis/references/domain-params.md

주요 제약:
- 경쟁사: SKT, KT (국내 직접), NTT/Verizon/AT&T (글로벌 벤치마크)
- MCP 토픽 우선 사용 (ai-network, 6g, network-slicing, edge-computing 등)
- 데이터 소스 우선순위: telco-factbook > research-hub > patent-intel > trend-tracker > WebSearch
- 분석 결과는 LG U+ 전략 관점에서 해석

## 이전 분석 컨텍스트 (prior_reports가 있는 경우에만 포함)
prior_reports:
  - path: {파일 절대경로}
    date: {YYYY-MM-DD}
    topic: {frontmatter topic}
    verdict: {판정결과 — 있으면}      # e.g. "Conditional Go", "Go", "No-Go"
    score: {점수 — 있으면}             # e.g. "128/200"
    confidence: {신뢰도}
    summary_excerpt: |
      {## 경영진 요약 섹션 첫 3~5줄}

지시 (최근 ≤ 30일):
  - 이전 분석 결과를 선행 지식으로 활용한다
  - 동일한 결론을 반복하지 말고, 달라진 것에 집중한다
  - 이전 판정이 뒤집혔거나 강화된 근거가 있으면 명확히 표시한다

지시 (31~180일):
  - 이전 분석을 참조 배경으로만 활용한다
  - 시간 경과에 따른 변화(기술 성숙도, 시장 상황, 경쟁 동향)를 업데이트한다
```

---

## Subagent Invocation Contract

모든 서브에이전트 호출 시 다음 4요소 포함:

```
## 목표 (Objective)
> 구체적이고 범위가 명확한 분석 목표
> GOOD: "2025~2026 국내 통신사의 AI 에이전트 서비스 현황 비교 (WTIS Proposal Mode)"

## 출력 포맷
> 해당 스킬/에이전트의 포맷 명세에 따름
> 필수: status (pass|fail|uncertain), summary (200자 이내), file_path

## 도구·소스
> 사용할 MCP 서버, WebSearch, 파일 참조 경로

## 태스크 경계
> 이 서브에이전트가 하지 말아야 할 것
```

---

## Final Report — 데이터 보존 규칙

최종 보고서 생성 시 아래 5개 규칙을 **반드시** 준수한다. 중간 산출물의 데이터를 요약·압축하되 **삭제하지 않는다**.

1. **References 전수 보존** — research-deep 레퍼런스 테이블의 모든 행을 그대로 포함한다. validator 이슈는 레퍼런스 삭제가 아닌 본문 인용 추가로 해소한다.
2. **200점 채점 근거 보존** — 대분류 × 세부지표 × 점수 × 판정 이유(1줄) 테이블 전체를 포함한다. 합산만 남기지 않는다.
3. **수치 테이블 보존** — 연도별 통계, TAM/SAM/SOM 편의 계산, 성능 벤치마크 등 데이터 테이블은 원본 그대로 포함한다.
4. **의사결정 로직 보존** — 3B 판단 경로(왜 Buy/Borrow/Build인지), SMART Test(5기준별 충족/미충족 + 근거), TRL 4사분면 매핑을 포함한다.
5. **직접 인용 보존** — 기업 발언(E-xx) 핵심 3개 이상, 정부/표준기관 발표 핵심 인용을 본문에 포함한다.

### 인용 앵커 링크 형식

본문에서 레퍼런스를 인용할 때 클릭 가능한 앵커 링크를 사용한다:

**본문:**
```markdown
PQC 표준은 2025년 확정되었다 [[G-01]](#ref-g-01).
```

**References 테이블:**
```markdown
| <a id="ref-g-01"></a>G-01 | postquantum.com | https://... | 2025-03 | high |
```

이 형식은 Obsidian, GitHub, PDF 렌더러(design-system)에서 모두 클릭 → 점프 동작한다.

---

## Final Report Template

```markdown
---
topic: {analysis topic}
domain: {L1 도메인 slug — secure-ai / agentic-ai / axops}
l2_topic: {L2 기술 slug — tech-taxonomy.md 참조}
date: {YYYY-MM-DD}
wtis_version: v4.1
wtis_mode: proposal|quick|standard|deep
skills_executed: [SKILL-0, research-deep, SKILL-1, validator]
confidence: high|medium|low
status: completed|needs-followup
total_references: {N}
prior_report: {이전 분석 파일명 — 없으면 생략}
prior_report_date: {이전 분석 날짜 — 없으면 생략}
---

# WTIS Report: {topic}

## 경영진 요약
> 판정(Go/Conditional Go/No-Go), 종합 점수(N/200), 3B 전략(Buy/Borrow/Build),
> 핵심 리스크를 3~5문장으로 요약한다.

## 이전 분석 대비 변화 (prior_report가 있을 때만 포함)
> 이전 분석: `{prior_report}` ({prior_report_date})

| 항목 | 이전 ({prior_report_date}) | 현재 ({date}) | 변화 |
|------|--------------------------|--------------|------|
| 핵심 판정 | {이전 verdict} | {현재 verdict} | ↑/↓/→ |
| 신뢰도 | {이전 confidence} | {현재 confidence} | |
| 주요 위험 | {이전 top risk} | {현재 top risk} | |
| 기술 성숙도 | {이전 TRL 요약} | {현재 TRL 요약} | |

**변화 주요 원인:**
- (이전 분석 이후 달라진 시장/기술/경쟁 요인)

## 1. 시장 분석
- TAM/SAM/SOM 편의 계산 (research-deep + SKILL-1 데이터 통합)
- 연도별 통계 테이블 전수 포함 (축소·생략 금지)
- 시장매력도 채점 근거 (항목 × 점수 × 판정 이유 1줄)

## 2. 기술 성숙도 분석
- TRL 매트릭스 + 4사분면 맵
- SMART Test (5기준별 충족/미충족 + 근거)
- 성능 벤치마크 수치 테이블

## 3. 경쟁 환경
- Gap Analysis 비교표 전수 (경쟁사별 지표)
- 기업 발언 직접 인용 (E-xx) 핵심 3개 이상

## 4. 전략 권고
- 3B 의사결정 경로 (왜 Buy/Borrow/Build인지 판단 트리)
- 200점 채점표 전체 (대분류 × 세부지표 × 점수 × 근거 1줄)
- 후속 조건 체크리스트
- [ ] (구체적 후속 조치 with 담당자/기한)

## 5. 교차검증 결과
- validator 전체 이슈 목록 + 각 이슈의 처리 방식 (해소/잔존/보강)
- 최종 판정: PASS | PARTIAL | FAIL

## References
(research-deep 레퍼런스 테이블 **전수** 포함 — 삭제 금지)
(앵커 링크 형식 사용: `<a id="ref-{id}"></a>{id}`)
| # | 출처 | URL | 발행일 | 신뢰도 |
|---|------|-----|--------|--------|
| <a id="ref-g-01"></a>G-01 | {source} | {url} | {date} | {confidence} |
```

---

## Early Termination

| Condition | Action |
|-----------|--------|
| SKILL-0: 입력 파싱 불가 | 사용자에게 재입력 요청 |
| SKILL-1: "부적합" 판정 | 파이프라인 중단, 사유 보고 |
| research-deep: 유의미한 데이터 없음 | 사용자에게 키워드 조정 요청 |
| validator: 2회 연속 FAIL | 사용자에게 판단 위임 |
| validator: partial + 단일 소스 ≤ 3건 | 보강 루프 [4-1] 실행 |
| validator: partial + 단일 소스 > 3건 | 보강 루프 [4-1] 실행 + 최종 보고서에 경고 |

## Post-Report

보고서 저장 완료 후 **자동으로** 다음 순서로 실행한다:

### Step A: 포트폴리오 갱신 (필수)

1. `outputs/reports/{domain}/portfolio.md` 읽기 (없으면 아래 템플릿으로 신규 생성)
2. L2 기술 테이블에서 현재 `l2_topic` 행 찾기 (없으면 행 추가)
3. 해당 행의 최근 평가일, 점수, 판정, 전략, 세션 링크 업데이트
4. 종합 권고 섹션 재생성 (Go/Conditional/No-Go/미평가 분류)
5. 평가 이력 테이블에 행 추가
6. `updated` frontmatter 날짜 갱신

#### 포트폴리오 템플릿
```markdown
---
domain: {L1 도메인 slug}
domain_name: {L1 도메인 한글명}
updated: {YYYY-MM-DD}
wtis_version: v4.1
total_l2: {N}
evaluated: {M}
---

# {domain_name} 포트폴리오

| L2 기술 | 최근 평가일 | 점수 | 판정 | 전략 | 세션 링크 |
|---------|-----------|------|------|------|----------|
| {l2_name} | {date} | {score}/200 | Go/Conditional/No-Go | Buy/Borrow/Build/Watch | [[{session}/final]] |
| ... | — | — | 미평가 | — | — |

## 종합 권고
- **우선 추진**: {Go 판정 L2 목록}
- **조건부**: {Conditional 판정 L2 + 조건}
- **보류**: {No-Go 판정 L2}
- **미평가**: {미분석 L2 → 평가 우선순위 권고}

## 평가 이력
| 날짜 | L2 | 점수 | 판정 | 비고 |
|------|-----|------|------|------|
```

L2 목록은 `tech-taxonomy.md`에서 해당 L1 도메인의 L2 기술을 가져온다:
- secure-ai: OnDevice AI, 스팸/피싱/탐지, 양자동형암호
- agentic-ai: 의도파악기술, Multi-Agent, Self Evolving Agent, 관계추론기술
- axops: FeedBackOps/EvalOps, ML/LLMOps

### Step B: PDF 자동 생성 (필수)
최종 보고서 + 포트폴리오를 PDF로 변환한다.

```
design-system MCP → render_pdf(
  markdown_path = "<최종 보고서 절대경로>",
  theme = "professional"
)
design-system MCP → render_pdf(
  markdown_path = "<포트폴리오 절대경로>",
  theme = "professional"
)
```

- 성공 시: `{domain}/{date}_{slug}/final.professional.pdf` + `{domain}/portfolio.professional.pdf` 생성
- 실패 시: 오류 메시지 출력 후 마크다운 파일 경로를 대신 안내 (파이프라인 중단 없음)

### Step C: 후속 안내 (선택)
1. Obsidian 동기화 필요 시 `/obsidian-bridge` 안내
2. 후속 모니터링 필요 시 `/monitor [topic]` 사용 제안
3. 동일 도메인의 다른 L2 미평가 기술이 있으면 다음 분석 대상 제안

## Announcement
실행 시작 전 사용자에게 판정 결과를 먼저 보여준다:
```
[WTIS v4.1] 모드: {mode} | 도메인: {domain} | L2: {l2_topic}
실행: {components}
데이터 소스: {MCP 서버 목록} + WebSearch
기존 리포트: {N건 발견 → 변화 추이 비교 모드 | 없음 → 신규 분석}
세션 폴더: outputs/reports/{domain}/{date}_{slug}/
분석을 시작합니다.
```
