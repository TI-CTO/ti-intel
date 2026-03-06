---
name: weekly-monitor
description: "주간 기술 동향 모니터링. 2단계 파이프라인: 전체 L3 빠른 스캔 → 변화 감지된 L3 심층 리서치. 논문/특허/뉴스를 종합한다."
user-invokable: true
argument-hint: "<agentic-ai | secure-ai | axops>"
---

# Weekly Monitor — 주간 기술 동향 모니터링

3개 도메인 × 18개 L3 세부기술의 주간 모니터링.
**2단계 파이프라인**: 먼저 전체 L3를 빠르게 스캔하고, 변화가 감지된 L3에 대해서만 심층 리서치를 실행한다.

## 핵심 원칙

1. **레이더 + 망원경** — Quick(빠른 스캔)으로 신호를 감지하고, Deep(심층 리서치)으로 깊이를 확보
2. **뉴스 최대 수집** — 중복이 아닌 한 가능한 모든 뉴스를 수집. 몇 건 수준이 아닌 포괄적 수집
3. **논문/특허/뉴스 종합** — 심층 리서치는 research-deep 수준으로 3개 소스를 모두 활용
4. **WTIS quick 대체** — weekly-monitor의 Deep이 충분히 깊으므로 별도 WTIS quick 실행 불필요

## 빠른 시작

```
/weekly-monitor agentic-ai   → 월요일: Agentic AI 7개 L3
/weekly-monitor secure-ai    → 수요일: Secure AI 7개 L3
/weekly-monitor axops        → 금요일: AXOps 4개 L3
```

---

## Arguments

| 인자 | 설명 |
|------|------|
| `agentic-ai` | Agentic AI 도메인 (L3 7개) |
| `secure-ai` | Secure AI 도메인 (L3 7개) |
| `axops` | AXOps 도메인 (L3 4개) |

인자는 필수. 도메인 하나만 지정한다.

## References

- 분류체계: `.claude/skills/wtis/references/tech-taxonomy.md`
- 도메인 파라미터: `.claude/skills/wtis/references/domain-params.md`

---

## Domain → L3 매핑

### agentic-ai
| L2 | L3 | slug |
|----|----|------|
| 의도파악기술 | Adaptive RAG | `adaptive-rag` |
| Multi-Agent | Intelligent Agent Orchestration | `agent-orchestration` |
| Multi-Agent | Agent Oriented Planning | `agent-planning` |
| Self Evolving Agent | Agentic Context Engineering | `agentic-context-engineering` |
| 관계추론기술 | 페르소나 플러그인 기술 | `persona-plugin` |
| 관계추론기술 | 관계 그래프 구축 기술 | `relationship-graph` |
| 관계추론기술 | 컨텍스트 기반 액션 추천 기술 | `context-action-recommendation` |

### secure-ai
| L2 | L3 | slug |
|----|----|------|
| OnDevice AI | OnDevice sLM | `ondevice-slm` |
| OnDevice AI | 실시간 화자분할(2인) | `speaker-diarization` |
| 스팸/피싱/탐지 | 스팸피싱감지(통화전) | `spam-phishing-detection` |
| 스팸/피싱/탐지 | OCR 이미지 스팸 차단 | `ocr-image-spam` |
| 양자동형암호 | OnDevice 양자암호 | `ondevice-pqc` |
| 양자동형암호 | OnDevice 동형암호 | `ondevice-he` |
| 양자동형암호 | Secure Vector Search | `secure-vector-search` |

### axops
| L2 | L3 | slug |
|----|----|------|
| FeedBackOps/EvalOps | FeedBackOps Meta Prompt Eng. | `feedbackops-prompt` |
| FeedBackOps/EvalOps | EvalOps KMS 성능평가 | `evalops-kms` |
| ML/LLMOps | 학습 배포 통합 파이프라인 | `mlops-pipeline` |
| ML/LLMOps | 하이브리드 GPU Orchestration | `gpu-orchestration` |

---

## Process

### Step 0: 사용자 입력 (선택)

사용자에게 질문:
> "이번 주 특별히 추적할 회사나 키워드가 있나요? (없으면 Enter)"

- 입력 있으면: Quick 검색에 추가 키워드로 포함
- 입력 없으면: 기본 키워드(`tech-taxonomy.md`)로 진행

---

## Quick: 빠른 스캔 (전체 L3)

목적: 전체 L3에 대해 **신호등(🟢🟡🔴)을 판정**한다. ~5분.

### Step 1-1: 데이터 수집

`tech-taxonomy.md`에서 해당 도메인의 L3 slug + 검색 키워드를 로드한다.

각 L3 토픽에 대해:

```
intel-store: search_intel(query={keywords}, topic={slug}, since={7일전}, limit=30, mode="keyword")
intel-store: search_intel(query={keywords}, types=["paper"], since={7일전}, limit=5, mode="keyword")
WebSearch: "{L3 keywords} 2026 latest news" (intel-store 결과 부족 시)
```

### Step 1-2: 신호등 판정

수집된 데이터로 각 L3의 변화 수준을 판정:

| 신호 | 기준 | Deep |
|------|------|------|
| 🟢 평온 | 뉴스 ≤ 3건, 유의미 변화 없음 | **스킵** — 1줄 요약만 |
| 🟡 주목 | 주요 발표/논문/표준 변화 감지 | **실행** — 심층 리서치 |
| 🔴 긴급 | 경쟁사 출시, 규제 변경, 기술 돌파 | **실행** — 심층 리서치 |

### Step 1-3: 사용자 확인

신호등 결과를 사용자에게 보여주고 Deep 진행 확인:

```
Quick 스캔 완료:
  🔴 OnDevice sLM — Apple sLM 3.0 발표 + Qualcomm 대응
  🟡 ondevice-pqc — NIST PQC 마이그레이션 가이드 공개
  🟢 speaker-diarization — 특이사항 없음
  🟢 spam-phishing-detection — 특이사항 없음
  ...

Deep 심층 리서치 대상: 2개 (🔴 1, 🟡 1)
계속할까요?
```

사용자가 추가/제외할 L3를 조정할 수 있다.

---

## Deep: 심층 리서치 (🟡🔴 L3만)

목적: 변화가 감지된 L3에 대해 **논문/특허/뉴스를 종합한 심층 분석**을 수행한다.

### Step 2-1: 포괄적 데이터 수집

`research-deep` 에이전트를 호출한다. L3 토픽별로 **개별 호출** (병렬 가능):

```
research-deep 에이전트 (sonnet):
  목표: "{L3 이름}의 최근 1주 기술/시장/경쟁 동향 종합 리서치"
  도구·소스:
    - intel-store MCP: collect_papers(topic, query) — 최신 논문 전수 수집+저장
    - intel-store MCP: collect_patents(topic, query) — 최신 특허 출원 수집+저장
    - intel-store MCP: collect_news(topic, query) — 뉴스 전수 수집 (Tavily+GDELT, 중복 제거)
    - intel-store MCP: find_similar(text) — 관련 아이템 탐색
    - WebSearch: MCP 결과 보강 (최신 뉴스, 블로그, 공식 발표)
  태스크 경계:
    - Go/No-Go 판정하지 않음 (WTIS standard/proposal의 역할)
    - 전략 권고하지 않음 (팩트 수집 + 분석에 집중)
  출력 경로: outputs/reports/weekly/YYYY-MM-DD_research-{l3-slug}.md
    ⚠️ 반드시 weekly/ 폴더에 저장 (메인 리포트와 같은 위치)
  출력 내용:
    - 기술 동향 (논문/표준/오픈소스 변화)
    - 플레이어 동향 (기업별 움직임)
    - 시장 시그널 (투자/M&A/파트너십)
    - References 테이블 (전수)
```

### Step 2-2: 이전 스냅샷 대비 변화 분석

이전 주 스냅샷이 있으면:
```
trend-tracker: compare_snapshots(topic={slug}, period="1w")
```

변화 내용을 리포트에 "이전 대비 변화" 섹션으로 포함.

### Step 2-3: 플레이어 식별

Deep 대상 L3에 대해:

1. 수집된 뉴스/논문/특허에서 기업명 빈도 추출 → 상위 5~10개
2. `domain-params.md`의 `key_players` 목록과 교차
3. 사용자 지정 회사 고정 포함
4. L3별 플레이어 동향 테이블 생성

---

## Step 3: 스냅샷 저장

각 L3 토픽별로:
```
trend-tracker: upsert_snapshot(
  topic={slug},
  summary={L3 요약},
  key_signals=[주요 시그널 목록],
  news_count={수집 뉴스 수},
  sentiment={positive|neutral|negative|mixed},
  change_level={none|minor|notable|urgent}
)
```

---

## Step 4: 리포트 생성 & 저장

### 파일 경로 규칙

모든 산출물은 `weekly/` 폴더에 저장한다:
```
outputs/reports/weekly/
  YYYY-MM-DD_weekly-{domain-slug}.md              ← 메인 리포트 (Quick + Deep 요약)
  YYYY-MM-DD_weekly-{domain-slug}.professional.pdf ← PDF
  YYYY-MM-DD_research-{l3-slug}.md                ← Deep 심층 리서치 (L3별 개별 파일)
```

⚠️ **Deep research-deep 에이전트 호출 시 `file_path`를 반드시 `weekly/` 경로로 지정한다.**
잘못된 예: `outputs/reports/YYYY-MM-DD_research-xxx.md` (reports 루트에 저장 — 금지)

### Step 5: PDF 생성

```
design-system MCP → render_pdf(
  markdown_path = "<리포트 절대경로>",
  theme = "professional"
)
```

### Step 6: 후속 안내

- 🔴 긴급 L3가 있으면: `/wtis standard {L2 기술} Go/No-Go 검증` 제안
- Obsidian 동기화: `/obsidian-bridge` 안내

---

## Table Schema (고정 — 열 수/순서 변경 금지)

메인 리포트와 Deep 리서치 모두 아래 스키마를 **정확히** 따른다.
research-deep 에이전트에도 동일한 스키마가 정의되어 있다.

### T1: Executive Summary (4열)
```
| 세부기술 | 신호 | 핵심 내용 | 분석 |
```

### T2: 플레이어 동향 (3열)
```
| 기업 | 동향 | 출처 |
```
- 동향 셀에 수치·성과 포함. 별도 "성과" 컬럼 금지.
- 출처: `[[G-01]](#ref-g-01)` 앵커 링크. 복수 출처는 `, `로 구분.

### T3: 주요 논문 (3열)
```
| 논문 | 핵심 | 출처 |
```
- 논문: "제목 (저자, 연도)". 저자 3인+ → "First et al."
- 출처: `[[P-01]](#ref-p-01)` 앵커 링크.

### T4: 시장 시그널
- **테이블 금지** — 불릿 리스트로만 작성.

### T5: References (6열)
```
| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
```
- 모든 출처 유형(G/N/E/P/T)을 **하나의 테이블**에 통합. 유형별 분리 금지.
- URL: `[링크](url)` 마크다운 링크.
- #열: `<a id="ref-g-01"></a>G-01` 앵커 태그 포함.

---

## Output Format

```markdown
---
type: weekly-monitor
domain: {domain-slug}
week: {YYYY-Wnn}
date: {YYYY-MM-DD}
l3_count: {N}
deep_count: {Deep 실행된 L3 수}
---

# 주간 기술 동향: {Domain Name} ({Week})

## Executive Summary

| 세부기술 | 신호 | 핵심 내용 | 분석 |
|----------|------|----------|------|
| OnDevice sLM | 🔴 긴급 | Apple sLM 3.0 발표, 온디바이스 추론 2배 향상 | Deep |
| ondevice-pqc | 🟡 주목 | NIST PQC 마이그레이션 가이드 v2 공개 | Deep |
| speaker-diarization | 🟢 평온 | 특이사항 없음 | Quick |

---

## 🟢 Quick 요약 (변화 미미)

### {L3 이름}
- 특이사항 없음 / 1~2줄 요약

---

## 🟡🔴 Deep 심층 분석

### {세부기술 이름} — 🔴 긴급

#### 기술 동향
- 논문/표준/오픈소스 변화 상세 서술
- 출처 앵커 링크: [[G-01]](#ref-g-01)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Apple | sLM 3.0 발표, 온디바이스 추론 성능 2배 | [[G-02]](#ref-g-02) |
| Samsung | Galaxy AI 업데이트 예고 | [[N-01]](#ref-n-01) |

#### 시장 시그널
- 투자/M&A/파트너십 동향 (불릿 리스트)

#### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| Nexus (Author et al., 2025) | 단일 GPU 내 P/D 분리 | [[P-01]](#ref-p-01) |

#### 전략적 시사점

**기회**
- 항목

**위협**
- 항목

---

(Deep 세부기술별 반복)

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. 여러 세부기술에 걸친 공통 패턴, 연결점, 종합 시사점

### 후속 조치 제안

- 🔴 긴급 세부기술 → `/wtis standard` 검증 제안
- 기타 후속 액션

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | {출처명} | [링크]({url}) | news | {YYYY-MM-DD} | [B] |
| <a id="ref-p-01"></a>P-01 | {저자 — 제목} | [링크]({url}) | paper | {YYYY} | [A] |
| <a id="ref-e-01"></a>E-01 | {기업 — 발언 요약} | [링크]({url}) | IR/발표 | {YYYY-MM-DD} | [A] |
```

---

## WTIS와의 관계

```
weekly-monitor         WTIS
─────────────          ────
Quick: 신호 감지        (해당 없음)
Deep: 심층 리서치    ≈   quick (사실상 대체)
(판정 없음)             standard/proposal: Go/No-Go 판정
                       deep: 기회 발굴
```

- weekly-monitor Deep이 **WTIS quick을 대체**한다
- 🔴 긴급 시그널 발견 시 → `/wtis standard`로 Go/No-Go **의사결정** 연계
- weekly-monitor는 판정/채점을 하지 않는다 (팩트 수집 + 분석까지만)

---

## Error Handling

- **MCP 도구 오류**: 해당 L3는 WebSearch만으로 대체 수집 → 한계 명시
- **뉴스 0건**: WebSearch 대체 수집 → "DB 수집 없음, 웹 검색 기반" 표시
- **첫 실행 (스냅샷 없음)**: 변화 비교 불가 안내 + 베이스라인 스냅샷만 저장
- **전체 MCP 실패**: WebSearch만으로 최소 리포트 생성 + 경고 표시
- **Deep 대상 과다 (≥5개)**: 사용자에게 우선순위 조정 요청 (비용/시간 안내)

## Notes

- `tech-taxonomy.md`의 검색 키워드를 OR 확장하여 쿼리 구성
- Deep의 research-deep 호출 시 `domain-params.md`의 소스 우선순위 준수
- 리포트의 References는 WTIS Final Report와 동일한 앵커 링크 형식 사용
- 향후 cron 자동화: `claude -p "/weekly-monitor {domain}"` (수동 안정화 후)
