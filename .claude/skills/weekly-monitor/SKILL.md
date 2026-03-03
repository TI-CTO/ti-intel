---
name: weekly-monitor
description: "주간 기술 동향 모니터링. 2단계 파이프라인: 전체 L3 빠른 스캔 → 변화 감지된 L3 심층 리서치. 논문/특허/뉴스를 종합한다."
user-invokable: true
argument-hint: "<agentic-ai | secure-ai | axops>"
---

# Weekly Monitor — 주간 기술 동향 모니터링

LG U+ 기술전략 3개 도메인 × 18개 L3 세부기술의 주간 모니터링.
**2단계 파이프라인**: 먼저 전체 L3를 빠르게 스캔하고, 변화가 감지된 L3에 대해서만 심층 리서치를 실행한다.

## 핵심 원칙

1. **레이더 + 망원경** — Tier 1(빠른 스캔)으로 신호를 감지하고, Tier 2(심층 리서치)로 깊이를 확보
2. **뉴스 최대 수집** — 중복이 아닌 한 가능한 모든 뉴스를 수집. 몇 건 수준이 아닌 포괄적 수집
3. **논문/특허/뉴스 종합** — 심층 리서치는 research-deep 수준으로 3개 소스를 모두 활용
4. **WTIS quick 대체** — weekly-monitor의 Tier 2가 충분히 깊으므로 별도 WTIS quick 실행 불필요

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

- 입력 있으면: Tier 1 검색에 추가 키워드로 포함
- 입력 없으면: 기본 키워드(`tech-taxonomy.md`)로 진행

---

## Tier 1: 빠른 스캔 (전체 L3)

목적: 전체 L3에 대해 **신호등(🟢🟡🔴)을 판정**한다. ~5분.

### Step 1-1: 데이터 수집

`tech-taxonomy.md`에서 해당 도메인의 L3 slug + 검색 키워드를 로드한다.

각 L3 토픽에 대해:

```
trend-tracker: search_news(topic={slug}, keyword={OR-expanded-keywords}, since={7일전}, limit=30)
research-hub: search_papers(topic={slug}, query={keywords}, since_year=2026, limit=5)
WebSearch: "{L3 keywords} 2026 latest news" (trend-tracker 결과 부족 시)
```

### Step 1-2: 신호등 판정

수집된 데이터로 각 L3의 변화 수준을 판정:

| 신호 | 기준 | Tier 2 |
|------|------|--------|
| 🟢 평온 | 뉴스 ≤ 3건, 유의미 변화 없음 | **스킵** — 1줄 요약만 |
| 🟡 주목 | 주요 발표/논문/표준 변화 감지 | **실행** — 심층 리서치 |
| 🔴 긴급 | 경쟁사 출시, 규제 변경, 기술 돌파 | **실행** — 심층 리서치 |

### Step 1-3: 사용자 확인

신호등 결과를 사용자에게 보여주고 Tier 2 진행 확인:

```
Tier 1 스캔 완료:
  🔴 OnDevice sLM — Apple sLM 3.0 발표 + Qualcomm 대응
  🟡 ondevice-pqc — NIST PQC 마이그레이션 가이드 공개
  🟢 speaker-diarization — 특이사항 없음
  🟢 spam-phishing-detection — 특이사항 없음
  ...

Tier 2 심층 리서치 대상: 2개 (🔴 1, 🟡 1)
예상 소요: ~10분
계속할까요?
```

사용자가 추가/제외할 L3를 조정할 수 있다.

---

## Tier 2: 심층 리서치 (🟡🔴 L3만)

목적: 변화가 감지된 L3에 대해 **논문/특허/뉴스를 종합한 심층 분석**을 수행한다.

### Step 2-1: 포괄적 데이터 수집

`research-deep` 에이전트를 호출한다. L3 토픽별로 **개별 호출** (병렬 가능):

```
research-deep 에이전트 (sonnet):
  목표: "{L3 이름}의 최근 1주 기술/시장/경쟁 동향 종합 리서치"
  도구·소스:
    - research-hub MCP: 최신 논문 (limit 없이 관련 논문 전수 수집)
    - patent-intel MCP: 최신 특허 출원
    - trend-tracker MCP: 뉴스 전수 수집 (중복 제거, limit 없이)
    - WebSearch: MCP 결과 보강 (최신 뉴스, 블로그, 공식 발표)
  태스크 경계:
    - Go/No-Go 판정하지 않음 (WTIS standard/proposal의 역할)
    - LG U+ 전략 권고하지 않음 (팩트 수집 + 분석에 집중)
  출력:
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

Tier 2 대상 L3에 대해:

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

파일 경로:
```
/Users/ctoti/Project/ClaudeCode/outputs/reports/weekly/YYYY-MM-DD_weekly-{domain-slug}.md
```

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

## Output Format

```markdown
---
type: weekly-monitor
domain: {domain-slug}
week: {YYYY-Wnn}
date: {YYYY-MM-DD}
l3_count: {N}
tier2_count: {Tier 2 실행된 L3 수}
---

# 주간 기술 동향: {Domain Name} ({Week})

## Executive Summary

| L3 | 신호 | 핵심 내용 | Tier |
|----|------|----------|------|
| OnDevice sLM | 🔴 긴급 | Apple sLM 3.0 발표, 온디바이스 추론 2배 향상 | Tier 2 |
| ondevice-pqc | 🟡 주목 | NIST PQC 마이그레이션 가이드 v2 공개 | Tier 2 |
| speaker-diarization | 🟢 평온 | 특이사항 없음 | Tier 1 |
| spam-phishing-detection | 🟢 평온 | 특이사항 없음 | Tier 1 |

---

## 🟢 Tier 1 요약 (변화 미미)

### {L3 이름}
- 특이사항 없음 / 1~2줄 요약

---

## 🟡🔴 Tier 2 심층 분석

### {L3 이름} — 🔴 긴급

**기술 동향**
- 논문/표준/오픈소스 변화 상세 서술
- 출처 앵커 링크: [[G-01]](#ref-g-01)

**플레이어 동향**

| 회사 | 동향 | 출처 |
|------|------|------|
| Apple | sLM 3.0 발표, 온디바이스 추론 성능 2배 | [[G-02]](#ref-g-02) |
| Samsung | Galaxy AI 업데이트 예고 | [[N-01]](#ref-n-01) |

**시장 시그널**
- 투자/M&A/파트너십 동향

**이전 대비 변화** (스냅샷 있을 때만)
- 지난주 대비 달라진 점

---

(Tier 2 L3별 반복)

## References

(전수 포함 — 삭제 금지)
| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | {source} | {url} | news | {date} | {confidence} |
| <a id="ref-p-01"></a>P-01 | {source} | {url} | paper | {date} | {confidence} |
| <a id="ref-t-01"></a>T-01 | {source} | {url} | patent | {date} | {confidence} |
```

---

## WTIS와의 관계

```
weekly-monitor         WTIS
─────────────          ────
Tier 1: 신호 감지       (해당 없음)
Tier 2: 심층 리서치  ≈   quick (사실상 대체)
(판정 없음)             standard/proposal: Go/No-Go 판정
                       deep: 기회 발굴
```

- weekly-monitor Tier 2가 **WTIS quick을 대체**한다
- 🔴 긴급 시그널 발견 시 → `/wtis standard`로 Go/No-Go **의사결정** 연계
- weekly-monitor는 판정/채점을 하지 않는다 (팩트 수집 + 분석까지만)

---

## Error Handling

- **MCP 도구 오류**: 해당 L3는 WebSearch만으로 대체 수집 → 한계 명시
- **뉴스 0건**: WebSearch 대체 수집 → "DB 수집 없음, 웹 검색 기반" 표시
- **첫 실행 (스냅샷 없음)**: 변화 비교 불가 안내 + 베이스라인 스냅샷만 저장
- **전체 MCP 실패**: WebSearch만으로 최소 리포트 생성 + 경고 표시
- **Tier 2 대상 과다 (≥5개)**: 사용자에게 우선순위 조정 요청 (비용/시간 안내)

## Notes

- `tech-taxonomy.md`의 검색 키워드를 OR 확장하여 쿼리 구성
- Tier 2의 research-deep 호출 시 `domain-params.md`의 소스 우선순위 준수
- 리포트의 References는 WTIS Final Report와 동일한 앵커 링크 형식 사용
- 향후 cron 자동화: `claude -p "/weekly-monitor {domain}"` (수동 안정화 후)
