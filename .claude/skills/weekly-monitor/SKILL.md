---
name: weekly-monitor
description: "주간 기술 동향 모니터링. 2단계 파이프라인: 전체 L3 빠른 스캔 → 변화 감지된 L3 심층 리서치. 논문/특허/뉴스를 종합한다."
user-invokable: true
argument-hint: "<agentic-ai | voice-ai | secure-ai>"
---

# Weekly Monitor — 주간 기술 동향 모니터링

3개 도메인 × 25개 L3 세부기술의 주간 모니터링.
**2단계 파이프라인**: 먼저 전체 L3를 빠르게 스캔하고, 변화가 감지된 L3에 대해서만 심층 리서치를 실행한다.

## 핵심 원칙

1. **레이더 + 망원경** — Quick(빠른 스캔)으로 신호를 감지하고, Deep(심층 리서치)으로 깊이를 확보
2. **뉴스 최대 수집** — 중복이 아닌 한 가능한 모든 뉴스를 수집. 몇 건 수준이 아닌 포괄적 수집
3. **논문/특허/뉴스 종합** — 심층 리서치는 research-deep 수준으로 3개 소스를 모두 활용
4. **WTIS quick 대체** — weekly-monitor의 Deep이 충분히 깊으므로 별도 WTIS quick 실행 불필요
5. **7일 이내 소식만 포함** — 모든 섹션(기술 동향, 플레이어, 시장 시그널, 경쟁사 동향 포함)에서 최근 7일 이내 발행된 소식만 사용. WebSearch 결과도 동일 기준 적용. 오래된 뉴스가 섞이면 "주간 delta" 원칙이 훼손됨

## 빠른 시작

```
/weekly-monitor agentic-ai   → 월요일: Agentic AI 12개 L3
/weekly-monitor voice-ai     → 화요일: Voice AI 8개 L3
/weekly-monitor secure-ai    → 수요일: Secure AI 5개 L3
```

---

## Arguments

| 인자 | 설명 |
|------|------|
| `agentic-ai` | Agentic AI 도메인 (L3 12개) |
| `voice-ai` | Voice AI 도메인 (L3 8개) |
| `secure-ai` | Secure AI 도메인 (L3 5개) |

인자는 필수. 도메인 하나만 지정한다.

## I/O Contract

### Input
| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| `domain` | yes | `agentic-ai` \| `voice-ai` \| `secure-ai` | 모니터링 대상 도메인 |
| 추가 키워드 | no | 자유 텍스트 | Step 0에서 대화로 수집 |

### Output Files
| Artifact | Path Pattern | Description |
|----------|-------------|-------------|
| 메인 리포트 | `outputs/reports/weekly/YYYY-MM-DD_weekly-{domain}.md` | Quick + Deep 종합 |
| PDF | `outputs/reports/weekly/YYYY-MM-DD_weekly-{domain}.pdf` | 메인 리포트 PDF |
| Deep 리서치 | `outputs/reports/weekly/YYYY-MM-DD_research-{l3-slug}.md` | L3별 심층 분석 (🟡🔴만) |

### Return
```yaml
status: pass | partial    # partial: MCP 일부 실패 시
summary: "{domain} W{nn} — Deep {N}건, 🔴 {N} 🟡 {N} 🟢 {N}"
file_path: "메인 리포트 절대 경로"
deep_files: ["Deep 리서치 파일 경로 목록"]
```

## References

- 분류체계: `.claude/skills/wtis/references/tech-taxonomy.md`
- 도메인 파라미터: `.claude/skills/wtis/references/domain-params.md`

---

## Domain → L3 매핑

### agentic-ai
| L2 | L3 | slug |
|----|----|------|
| Self Evolving Architecture | Agentic Context Engineering | `agentic-context-engineering` |
| Model & Delta Foundry | FeedbackOps: 자율형 Meta-prompt Engineering PoC | `feedbackops-prompt` |
| Model & Delta Foundry | EvaluationOps: KMS 성능평가 자동화 PoC | `evalops-kms` |
| Model & Delta Foundry | 데이터-학습-배포 통합 자동화 파이프라인 | `mlops-pipeline` |
| Model & Delta Foundry | 하이브리드 GPU Orchestration | `gpu-orchestration` |
| Trusted Multi-Agent Orchestration | Intelligent Agent Orchestration | `agent-orchestration` |
| Trusted Multi-Agent Orchestration | Agent Oriented Orchestration | `agent-oriented-orchestration` |
| Hybrid AI Infra | On-Device sLM | `ondevice-slm` |
| Hybrid AI Infra | 실시간 화자분할(2인) 기술 확보 | `speaker-diarization` |
| Hybrid AI Infra | Edge AI | `edge-ai` |
| Hybrid AI Infra | 5G SA/6G(AI-RAN/SRv6) | `5g-6g-ai-ran` |
| 의도 파악 기술 | Adaptive RAG | `adaptive-rag` |

### voice-ai
| L2 | L3 | slug |
|----|----|------|
| Speech Perception & Interaction | Emotional Analysis | `emotional-analysis` |
| Speech Perception & Interaction | Context Recognition | `context-recognition` |
| Speech Perception & Interaction | Interrupt & Turn-Taking | `interrupt-turn-taking` |
| Personal Intelligence | 페르소나 플러그인 기술 고도화 | `persona-plugin` |
| Personal Intelligence | 관계 그래프 구축 기술 확보 | `relationship-graph` |
| Personal Intelligence | 컨텍스트 기반 액션 추천 기술 확보 | `context-action-recommendation` |
| Speech Generation | Voice Cloning | `voice-cloning` |
| Speech Generation | Voice Synthesis | `voice-synthesis` |

### secure-ai
| L2 | L3 | slug |
|----|----|------|
| 스팸/피싱탐지 | 스팸/피싱 감지(통화전) | `spam-phishing-detection` |
| 스팸/피싱탐지 | OCR 활용 이미지 스팸 차단 | `ocr-image-spam` |
| 양자/동형 암호 | On-Device 양자암호: 통화 녹음 파일 암호화 | `pqc-voice-encryption` |
| 양자/동형 암호 | On-Device 동형암호: 키워드 검색 | `he-keyword-search` |
| 양자/동형 암호 | Secure Vector Search: B2B AICC 동형암호 적용 | `secure-vector-search` |

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

### Step 1-0: 이전 주 데이터 로드

Executive Summary의 `전주` 열과 Deep의 "이전 대비 변화" 섹션에 사용할 이전 데이터를 로드한다.

**소스 우선순위**:
1. `trend-tracker: get_topic_summary(topic={slug})` — 최근 스냅샷의 `change_level`, `summary` 사용
2. 이전 주 리포트 파일 (`outputs/reports/weekly/` 에서 같은 도메인의 가장 최근 `_weekly-{domain}.md`) — Executive Summary 테이블 파싱
3. 둘 다 없으면: `전주` 열에 `—` 표시, "이전 대비 변화" 섹션 생략

**로드 결과**: L3별 `{prev_signal, prev_summary}` 딕셔너리를 Step 1-2, Step 2-1에서 참조.

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

### Step 1-2b: 경쟁사 동향 수집

Quick 스캔과 병행하여 해당 도메인 관련 경쟁사(SKT/KT) 뉴스를 수집한다.
**7일 이내 소식만 포함** — 경쟁사 동향도 다른 섹션과 동일하게 주간 delta 원칙 적용.

```
intel-store: search_intel(query="{도메인 L2 키워드}", topic="skt-strategy", since={7일전}, limit=15, mode="keyword")
intel-store: search_intel(query="{도메인 L2 키워드}", topic="kt-strategy", since={7일전}, limit=15, mode="keyword")
WebSearch: "SKT {도메인 키워드} site:news.sktelecom.com" (7일 이내 결과만 사용)
WebSearch: "KT {도메인 키워드} site:corp.kt.com" (7일 이내 결과만 사용)
```

- 도메인별 L2 키워드 예시:
  - agentic-ai: "AI 에이전트", "sLM", "RAG", "GPU"
  - voice-ai: "음성", "TTS", "AI 스피커", "보이스"
  - secure-ai: "보안", "피싱", "양자암호", "동형암호"
- 수집된 뉴스를 기업별(SKT/KT)로 그룹핑하여 리포트 경쟁사 섹션에 사용
- 7일 이내 신규 뉴스 없으면 "이번 주 해당 도메인 관련 경쟁사 뉴스 없음" 표기

### Step 1-2c: 규제 & 거버넌스 수집

해당 도메인 관련 규제·표준·가이드라인 동향을 수집한다.

```
WebSearch: "{도메인 키워드} regulation OR 규제 OR AI Act OR 기본법 2026"
WebSearch: "{도메인 키워드} standard OR guideline OR compliance 2026"
```

- 이전 주 리포트의 카운트다운 테이블을 로드하여 D-day 갱신
- 신규 규제 발의/가이드라인 공개가 있으면 추가
- 도메인과 무관한 일반 AI 규제는 제외

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

L3 토픽별로 **2개 에이전트를 병렬 호출**한다:

```
┌─ research-deep 에이전트 (sonnet) ─────────────────────────┐
│  목표: "{L3 이름}의 최근 1주 기술/시장/경쟁 동향 종합 리서치"  │
│  도구·소스:                                                │
│    - intel-store MCP: collect_papers, collect_patents,      │
│      collect_news, find_similar                            │
│    - WebSearch: MCP 결과 보강                               │
│  태스크 경계:                                               │
│    - Go/No-Go 판정하지 않음 (WTIS의 역할)                    │
│    - 전략 권고하지 않음 (팩트 수집 + 분석에 집중)              │
│  출력: outputs/reports/weekly/YYYY-MM-DD_research-{slug}.md │
└──────────────────────────────────────────────────────────┘
                        ↕ 병렬
┌─ voice-of-market 에이전트 (sonnet) ───────────────────────┐
│  목표: "{L3 이름} 관련 컨퍼런스 영상에서 수요 시그널 추출"     │
│  도구·소스:                                                │
│    - WebSearch: 관련 컨퍼런스 영상 탐색                      │
│    - youtube-transcript MCP: 트랜스크립트 추출 (최대 3개)     │
│  출력: 고객 페인포인트, 도입 장벽, 시장 니즈 (구조화 반환)     │
│  ⚠️ 영상 없으면 skip 반환 (실패 아님)                        │
└──────────────────────────────────────────────────────────┘
```

**병렬 실행 제한**: research-deep + voice-of-market 합산으로 동시 에이전트 최대 6개 (L3 3개 × 2 에이전트). L3 4개 이상이면 2배치로 분할.

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
  YYYY-MM-DD_weekly-{domain-slug}.pdf ← PDF
  YYYY-MM-DD_research-{l3-slug}.md                ← Deep 심층 리서치 (L3별 개별 파일)
```

⚠️ **Deep research-deep 에이전트 호출 시 `file_path`를 반드시 `weekly/` 경로로 지정한다.**
잘못된 예: `outputs/reports/YYYY-MM-DD_research-xxx.md` (reports 루트에 저장 — 금지)

### Step 4.5: 출처 검증 (validator)

메인 리포트 생성 후, PDF 변환 전에 `validator` 에이전트를 호출하여 References URL-Content 전수 검증을 실행한다.

```
validator 에이전트 (sonnet):
  입력: 메인 리포트 절대경로
  검증 범위: URL-Content 전수 검증 (References 테이블의 모든 URL)
  출력: 검증 리포트 (같은 폴더에 저장)
```

- ❌ 불일치 발견 시: 본문의 출처 인용을 수정하거나 올바른 URL로 교체한 후 PDF 진행
- ⚠️ 부분 일치: 경고만 출력, PDF 진행
- 🔗 접근 불가: 경고만 출력, PDF 진행

### Step 5: PDF 생성 + 품질 검증

```
design-system MCP → render_pdf(
  markdown_path = "<리포트 절대경로>",
  theme = "professional"
)
```

`render_pdf` 응답에 `validation` 필드가 포함된다:
```json
{
  "status": "success",
  "output_path": "...",
  "validation": {
    "passed": true,
    "summary": "18/18 PASS",
    "errors": [],
    "warnings": []
  }
}
```

#### 검증 실패 시 재시도 플로우

1. **errors가 있으면** (M-05~M-11 마크다운 구조 문제):
   - 에러 메시지를 분석하여 마크다운 소스를 수정
   - 수정 후 `render_pdf` 재호출 (최대 2회 재시도)
   - 대표적 수정: citation 앵커 누락(M-05), References 열 수(M-07), 시장 시그널 테이블(M-10)

2. **HTML 에러 (H-01, H-02)**:
   - 렌더러 코드 버그이므로 사용자에게 경고만 출력
   - 마크다운 수정으로 해결 불가

3. **warnings만 있으면**:
   - 경고 목록을 사용자에게 출력하되 재시도 없이 진행

### Step 6: Next Steps 안내

리포트 완료 후 아래 후속 옵션을 사용자에게 제시한다:

```
📋 Next Steps:
  🔴 긴급 L3 발견 시:
    → /wtis standard {L2 기술} Go/No-Go 검증    — 의사결정이 필요한 기술의 타당성 검증
  📊 프레젠테이션 필요 시:
    → /slides {리포트 경로}                      — PPTX 슬라이드 변환
  📂 Obsidian 동기화:
    → /obsidian-bridge {리포트 경로} weekly       — 메인 리포트 동기화
    → /obsidian-bridge {research 경로} research   — 심층 리서치 개별 동기화
  🔍 특정 L3 심화 조사:
    → /research-session {L3 주제}                — 자유 형식 심층 리서치
  📅 다른 도메인 모니터링:
    → /weekly-monitor {다른 도메인}               — 월:agentic-ai / 화:voice-ai / 수:secure-ai
```

---

## Heading Level Rules (엄격 — 변경 금지)

메인 리포트의 헤더 계층은 아래를 **정확히** 따른다. 한 단계 올리거나 내리지 않는다.

```
## Executive Summary                    ← h2
## 🟢 Quick 요약 (변화 미미)              ← h2
### {L3 이름}                            ← h3
## 🟡🔴 Deep 심층 분석                    ← h2 (컨테이너)
### {세부기술 이름} — 🔴 긴급              ← h3
#### 이전 대비 변화                        ← h4
#### 기술 동향                            ← h4
#### 플레이어 동향                         ← h4
#### 시장 시그널                           ← h4
#### 시장 수요                            ← h4
#### 학술 동향 (주요 논문)                  ← h4
#### 전략적 시사점                         ← h4
## 경쟁사 동향 (SKT / KT)                 ← h2
### SKT / ### KT                         ← h3
## 규제 & 거버넌스                         ← h2
### 시행 임박 / 카운트다운                   ← h3
### 신규 발의 & 가이드라인                   ← h3
### 시사점                                ← h3
## 종합 시사점 및 후속 조치                 ← h2
## References                            ← h2
```

⚠️ Deep L3를 `##`(h2)로 시작하면 하위 섹션이 h3이 되어 Quick의 L3 헤더와 같은 레벨이 되고, PDF에서 목차·스타일이 깨진다.

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

### T3: 주요 논문 (3열)
```
| 논문 | 핵심 | 출처 |
```

### T4: 시장 시그널
- **테이블 금지** — 불릿 리스트로만 작성.

### T4b: 시장 수요
- **테이블 금지** — 불릿 리스트로만 작성.
- 고객 페인포인트 / 도입 장벽 / 시장 니즈를 **볼드 소제목**으로 구분.
- 섹션 항상 포함. 결과 없으면 "컨퍼런스 영상에서 수요 시그널을 확인하지 못함" 표기.

### T-C: 경쟁사 동향 (4열)
```
| 항목 | 내용 | 관련 L3 | 출처 |
```
- SKT/KT 별도 테이블. 해당 도메인 관련 뉴스만 포함.
- 관련 L3: 우리 L3 slug 매핑. 해당 없으면 `(L3 밖)` 표기.
- 출처: 앵커 링크 (`[[E-01]](#ref-e-01)`).

### T-R: 규제 & 거버넌스
- **시행 임박 / 카운트다운**: 테이블 (3열)
```
| 규제 | 시행일 | D-day |
```
- D-day는 리포트 발행일 기준 자동 계산.
- **신규 발의 & 가이드라인**: 불릿 리스트.
- **시사점**: 불릿 리스트 (우리 사업 영향 1~2줄).
- 이번 주 규제 뉴스 없으면 카운트다운 테이블만 갱신하고 신규 섹션은 "이번 주 신규 규제 동향 없음" 표기.

### T5: References (6열)
```
| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
```
- 인용·앵커·ID 규칙은 `.claude/rules/report-writing.md` 참조.

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
| OnDevice sLM | 🔴 | Apple sLM 3.0 발표, 온디바이스 추론 2배 향상 | Deep |
| ondevice-pqc | 🔴 | NIST PQC 마이그레이션 가이드 v2 공개 | Deep |
| speaker-diarization | 🟢 | 특이사항 없음 | Quick |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음
>
> **분석** : Deep = 심층 리서치 수행 | Quick = 1줄 요약만

---

## 🟢 Quick 요약 (변화 미미)

### {L3 이름}
- 특이사항 없음 / 1~2줄 요약

---

## 🟡🔴 Deep 심층 분석

### {세부기술 이름} — 🔴 긴급

#### 이전 대비 변화
- 전주: {이전 주 핵심 상황 1줄}
- 금주: {이번 주 핵심 변화 1줄}
- 변화 방향: {실증→상용화 가속 / 신규 진입 / 규제 강화 등}

※ 이전 데이터 없으면(첫 실행) 이 섹션 생략.

#### 기술 동향

1. **제목 — 한 줄 요약.**
   상세 설명 텍스트. 출처 앵커 링크: [[G-01]](#ref-g-01)

2. **제목 — 한 줄 요약.**
   상세 설명 텍스트. [[G-02]](#ref-g-02)

※ 기술 동향은 반드시 순서 리스트(`1.` `2.`)로 작성. 볼드 제목과 설명은 줄바꿈으로 분리.

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Apple | sLM 3.0 발표, 온디바이스 추론 성능 2배 | [[G-02]](#ref-g-02) |
| Samsung | Galaxy AI 업데이트 예고 | [[N-01]](#ref-n-01) |

#### 시장 시그널
- 투자/M&A/파트너십 동향 (불릿 리스트)

#### 시장 수요 (voice-of-market)

> voice-of-market 에이전트 결과를 통합. 이 섹션은 항상 포함한다.

**고객 페인포인트**
- {페인포인트} — 출처: {영상 제목} ({발표자})

**도입 장벽**
- {장벽} — 출처: {영상 제목} ({발표자})

**시장 니즈**
- {니즈} — 출처: {영상 제목} ({발표자})

※ 에이전트가 `skip` 반환 시: "이번 주 해당 기술 관련 컨퍼런스 영상에서 수요 시그널을 확인하지 못함." 으로 표기.

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

---

## 경쟁사 동향 (SKT / KT)

> 이번 주 해당 도메인과 관련된 SKT·KT의 주요 움직임.

### SKT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| AI 에이전트 서비스 출시 | A. 서비스 상용화 발표 | agent-orchestration | [[E-01]](#ref-e-01) |

### KT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| AICC 동형암호 적용 | B2B AICC에 FHE 검색 도입 | secure-vector-search | [[E-02]](#ref-e-02) |

### 시사점
- 경쟁사 대비 우리의 포지션, 기회/위협 요약 (2~3줄)

※ 해당 도메인과 관련 없는 경쟁사 뉴스는 제외. 관련 뉴스 없으면 "이번 주 해당 도메인 관련 경쟁사 뉴스 없음" 표기.

---

## 규제 & 거버넌스

> 해당 도메인에 영향을 미치는 국내외 규제·표준·가이드라인 동향.

### 시행 임박 / 카운트다운

| 규제 | 시행일 | D-day |
|------|--------|-------|
| EU AI Act Article 50 (합성 콘텐츠 투명성) | 2026-08-02 | D-{N} |
| 한국 AI 기본법 Article 31 (AI 생성 표시) | 2026-01-22 | 시행 중 |

※ 도메인에 관련 없는 규제는 제외. 카운트다운 테이블은 매주 D-day를 갱신한다. 시행 완료된 항목은 "시행 중"으로 표기하고, 시행 후 4주가 지나면 테이블에서 제거한다.

### 신규 발의 & 가이드라인
- {이번 주 새로 발의/공개된 규제·표준·가이드라인} — 출처: [[G-xx]](#ref-g-xx)

※ 이번 주 신규 규제 동향 없으면 "이번 주 신규 규제 동향 없음" 표기.

### 시사점
- 우리 사업에 미치는 영향 (1~2줄)

---

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
