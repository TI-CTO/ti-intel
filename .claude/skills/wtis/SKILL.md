---
name: wtis
description: "Winning Tech Intelligence System v4.0 — LG U+ 기술전략 인텔리전스. 과제 제안서 분석, 기술 모니터링, 선정/진행 검증을 수행한다."
user-invokable: true
argument-hint: "[proposal|quick|standard|deep] [query or file path]"
---

# WTIS v4.0 Orchestrator

LG U+ Winning Tech Intelligence System의 오케스트레이터.
v4.0: SKILL-3/4/5를 Tech Intelligence Platform Layer 2 핵심 역량에 위임한다.
도메인 전용 로직(SKILL-0/1/2)은 내부 유지, 범용 역량(발굴/리서치/검증)은 외부 위임.

## 빠른 시작 — 모드별 치트시트

| 모드 | 언제 쓰나 | 호출 예시 | 소요 시간 |
|------|-----------|-----------|----------|
| **quick** | 동향/뉴스 파악 | `/wtis 6G mmWave 최신 동향` | ~2분 |
| **standard** | 과제 타당성 검증 | `/wtis AI-RAN 과제 Go/No-Go 검증` | ~5분 |
| **deep** | 신규 기회 발굴 | `/wtis edge AI 기회 탐색 및 전략 비교` | ~10분 |
| **proposal** | 제안서 전체 분석 | `/wtis proposal.md` | ~15분 |

**자동 모드 감지 키워드:**
- `동향 / 트렌드 / 뉴스` → quick
- `검증 / 타당성 / Go/No-Go` → standard
- `발굴 / 탐색 / 전략 / 비교` → deep
- `제안서` 또는 `.md` 파일 경로 → proposal

**PDF 자동 생성:** 모든 모드에서 최종 리포트 완료 후 PDF가 함께 생성됩니다.

---

## v3.0 → v4.0 변경점

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
| **quick** | 단순 현황/트렌드 질문 | research-deep 단독 (빠른 수집) |
| **standard** | 과제 검증 요청, 정기 보고 | research-deep + SKILL-1 or 2 + validator |
| **deep** | 신규 과제 발굴, 전략적 의사결정 | discover + research-deep + SKILL-1 + validator |

사용자가 모드를 지정하지 않으면 입력 내용으로 자동 판정한다:
- "제안서", "proposal", 파일 경로 포함 → **proposal**
- "동향", "트렌드", "뉴스", 단순 질문 → **quick**
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
- 기존 리서치: `/Users/ctoti/Project/ClaudeCode/outputs/reports/`

---

## Phase 0: 기존 리서치 확인 (모든 모드 공통 선행 단계)

모든 모드 실행 전, `outputs/reports/`에서 관련 기존 분석을 검색한다.

### 검색 대상 파일
```
outputs/reports/*-final.md          # WTIS 최종 리포트
outputs/reports/*_research-*.md     # research-deep 결과
outputs/reports/*_discover-*.md     # discover 결과
```
(*-skill0, -skill1, -validator 파일은 제외 — 중간 산출물)

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
  ✓ 관련 리포트 2건 발견
    - 2026-02-26_wtis-proposal-secure-ai-final.md  (0일 전 | Conditional Go | 128/200)
    - 2026-02-25_research-secure-ai.md             (1일 전 | medium)
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
    ├─ [1] SKILL-0 실행 (subagent_type: researcher, model: sonnet)
    │   └─ 프롬프트: skill-0-proposal.md 로드
    │   └─ 제안서 파싱 → Analysis Brief 생성
    │   └─ 결과 파일: outputs/reports/{date}_wtis-proposal-{slug}-skill0.md
    │
    ├─ [2] research-deep 에이전트 호출 (Layer 2 위임)
    │   └─ 입력: SKILL-0 결과 파일 경로 + 도메인 파라미터
    │   └─ 지시: "WTIS 제안서 분석을 위한 심층 리서치. domain-params.md의 소스 우선순위 준수"
    │   └─ 결과 파일: outputs/reports/{date}_wtis-proposal-{slug}-research.md
    │
    ├─ [3] SKILL-1 실행 (subagent_type: researcher, model: opus)
    │   └─ 프롬프트: skill-1-selection.md 로드
    │   └─ 입력: SKILL-0 Brief 파일 + research-deep 결과 파일 (경로 2개 전달)
    │   └─ 선정검증 + 3B 전략 제언
    │   └─ 결과 파일: outputs/reports/{date}_wtis-proposal-{slug}-skill1.md
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
    │   └─ 결과: 기존 research 파일에 보강 섹션 추가 (별도 파일 아님)
    │   └─ SKILL-1 재실행하지 않음 (보강 데이터는 다음 파이프라인에서 반영)
    │   └─ 최대 1회만 실행 (무한 루프 방지)
    │
    └─ [5] 최종 보고서 생성 + PDF 변환
        └─ 경로: outputs/reports/{date}_wtis-proposal-{slug}-final.md
        └─ design-system MCP → render_pdf(markdown_path=위 경로) 자동 실행
        └─ PDF: outputs/reports/{date}_wtis-proposal-{slug}-final.professional.pdf
```

### Quick Mode

```
사용자: 트렌드/현황 질문
    │
    ├─ [0] Phase 0: 기존 리서치 확인
    │   └─ prior_reports 있으면 "변화점 집중" 지시 추가
    │
    ├─ research-deep 에이전트 호출 (Layer 2 위임)
    │   └─ 입력: 질문 + 도메인 파라미터 + prior_reports (있으면)
    │   └─ 결과 파일 저장
    │
    └─ [자동] design-system MCP → render_pdf(결과 파일 경로)
```

### Standard Mode

```
사용자: 과제 검증 요청
    │
    ├─ [0] Phase 0: 기존 리서치 확인
    │   └─ prior_reports 있으면 SKILL-1/2에 이전 판정 컨텍스트 전달
    │
    ├─ research-deep 에이전트 호출 (Layer 2 위임)
    │   └─ 입력: 검증 대상 + 도메인 파라미터 + prior_reports (있으면)
    │
    ├─ SKILL-1 또는 SKILL-2 실행 (선정 또는 진행 검증)
    │
    ├─ validator 에이전트 호출 (Layer 2 위임)
    │
    ├─ 최종 보고서 생성
    │
    └─ [자동] design-system MCP → render_pdf(최종 보고서 경로)
```

### Deep Mode

```
사용자: 전략적 발굴/분석 요청
    │
    ├─ [0] Phase 0: 기존 리서치 확인
    │   └─ prior_reports 있으면 discover에 "이미 파악된 기회 중복 제외" 지시
    │
    ├─ [1] discover 스킬 호출 (Layer 2 위임) — SKILL-3 대체
    │   └─ 입력: 도메인 + domain-params.md의 competitors, taxonomy 전달
    │   └─ prior_reports 있으면: "기존 포트폴리오" 파라미터로 전달 (중복 방지)
    │   └─ 결과 파일: outputs/reports/{date}_discover-{domain}.md
    │
    ├─ [2] research-deep 에이전트 호출 (Layer 2 위임) — SKILL-4 대체
    │   └─ 입력: discover 결과 파일 + 도메인 파라미터 + prior_reports (있으면)
    │   └─ 결과 파일: outputs/reports/{date}_research-{topic}.md
    │
    ├─ [3] SKILL-1 실행 (subagent_type: researcher, model: opus)
    │   └─ discover + research-deep 결과를 입력으로 전달
    │
    ├─ [4] validator 에이전트 호출 (Layer 2 위임) — SKILL-5 대체
    │
    ├─ [5] 최종 보고서 생성
    │
    └─ [6] [자동] design-system MCP → render_pdf(최종 보고서 경로)
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

## Final Report Template

```markdown
---
topic: {analysis topic}
date: {YYYY-MM-DD}
wtis_version: v4.0
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
> (핵심 발견, 추천 방향, 신뢰도를 3~5문장으로)

## 상세 분석
(각 스킬/에이전트 결과를 통합 — 반복하지 않고 핵심만 연결)

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

## 교차검증 결과
(validator 요약: PASS/PARTIAL/FAIL + 주요 발견)

## 권고 및 Next Action
- [ ] (구체적 후속 조치 with 담당자/기한)

## References
(research-deep의 레퍼런스 테이블 전체 포함)
| # | 출처 | URL | 발행일 | 신뢰도 |
|---|------|-----|--------|--------|
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

### Step A: PDF 자동 생성 (필수)
최종 보고서 마크다운을 PDF로 변환한다.

```
design-system MCP → render_pdf(
  markdown_path = "<최종 보고서 절대경로>",
  theme = "professional"
)
```

- 성공 시: `{date}_wtis-*-final.professional.pdf` 생성, 경로 사용자에게 보고
- 실패 시: 오류 메시지 출력 후 마크다운 파일 경로를 대신 안내 (파이프라인 중단 없음)

### Step B: 후속 안내 (선택)
1. Obsidian 동기화 필요 시 `/obsidian-bridge` 안내
2. 후속 모니터링 필요 시 `/monitor [topic]` 사용 제안
3. 이전 WTIS 세션이 있으면 (`outputs/reports/` 검색) 변화 추이 언급

## Announcement
실행 시작 전 사용자에게 판정 결과를 먼저 보여준다:
```
[WTIS v4.0] 모드: {mode} | 실행: {components}
데이터 소스: {MCP 서버 목록} + WebSearch
기존 리포트: {N건 발견 → 변화 추이 비교 모드 | 없음 → 신규 분석}
분석을 시작합니다.
```
