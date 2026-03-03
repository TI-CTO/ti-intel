---
name: weekly-monitor
description: "주간 기술 동향 모니터링. L1 도메인별 L3 세부기술의 기술 동향 + 플레이어 동향을 수집·분석하여 주간 리포트를 생성한다."
user-invokable: true
argument-hint: "<agentic-ai | secure-ai | axops>"
---

# Weekly Monitor — 주간 기술 동향 모니터링

LG U+ 기술전략 3개 도메인 × 18개 L3 세부기술의 주간 모니터링.
도메인별 요일 분산으로 컨텍스트 부담을 줄인다.

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
> "이번 주 특별히 추적할 회사가 있나요? (없으면 Enter)"

- 입력 있으면: 해당 회사를 고정 추적 대상에 추가
- 입력 없으면: Step 2에서 자동 식별

### Step 1: 데이터 수집

`tech-taxonomy.md`에서 해당 도메인의 L3 slug + 검색 키워드를 로드한다.

각 L3 토픽에 대해:

```
trend-tracker: search_news(topic={slug}, keyword={OR-expanded-keywords}, since={7일전}, limit=20)
research-hub: search_papers(topic={slug}, query={keywords}, since_year=2026, limit=5)
```

**주의:** `search_news`로 기존 DB 조회, 결과가 부족하면 `collect_news`로 외부 수집.
뉴스와 논문을 통합 수집하되, 기술 관련 / 플레이어 관련은 분석 단계에서 분리한다.

### Step 2: 플레이어 식별

수집된 뉴스/논문에서 가장 많이 언급된 기업을 추출한다.

1. **사용자 지정 회사** → 고정 포함
2. **뉴스 본문에서 기업명 빈도 추출** → 상위 5개
3. **첫 실행 or 데이터 부족 시**: `WebSearch "{L3 이름} top companies 2026"` 으로 보강
4. **도메인별 Top 5 플레이어 목록** 확정 (사용자 확인 없이 진행)

### Step 3: 분석 & 리포트 생성

`researcher` 에이전트 (sonnet)를 사용하여 분석한다.

각 L3 토픽에 대해 두 섹션을 작성:

**기술 동향:**
- 핵심 뉴스 요약 (출처 포함)
- 주요 논문/표준/규제 변화
- 이전 스냅샷 대비 변화 (있을 경우)

**플레이어 동향:**
- Top 5 회사별 이번 주 움직임
- 출처 링크 포함 테이블

**변화 수준 판정:**
- 🟢 평온: 특이사항 없음
- 🟡 주목: 주요 발표/논문/표준 변화
- 🔴 긴급: 경쟁사 출시, 규제 변경, 기술 돌파

### Step 4: 스냅샷 저장

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

### Step 5: 리포트 저장

파일 경로:
```
/Users/ctoti/Project/ClaudeCode/outputs/reports/weekly/YYYY-MM-DD_weekly-{domain-slug}.md
```

---

## Output Format

```markdown
---
type: weekly-monitor
domain: {domain-slug}
week: {YYYY-Wnn}
date: {YYYY-MM-DD}
l3_count: {N}
---

# 주간 기술 동향: {Domain Name} ({Week})

## Executive Summary

| L3 | 변화 | 핵심 내용 |
|----|------|----------|
| 🔴 Adaptive RAG | urgent | 핵심 변화 1줄 |
| 🟡 Agent Orchestration | notable | ... |
| 🟢 Agent Planning | none | 특이사항 없음 |

---

## {L2 이름}

### {L3 이름}

**기술 동향**
- 뉴스/논문/표준 변화 요약 (출처 포함)
- [출처제목](URL) — 날짜

**플레이어 동향**

| 회사 | 동향 | 출처 |
|------|------|------|
| LangChain | ... | [링크](URL) |
| Cohere | ... | [링크](URL) |

**변화 수준**: 🟡 주목 — 근거 1줄

---

(L3별 반복)

## References

| # | 출처명 | URL | 유형 | 날짜 |
|---|--------|-----|------|------|
| [1] | ... | ... | news | ... |
| [2] | ... | ... | paper | ... |
```

---

## Error Handling

- **MCP 도구 오류**: 해당 L3 스킵 + 오류 로그, 나머지 계속 처리
- **뉴스 0건**: WebSearch 대체 수집 → 한계 명시 ("DB 수집 없음, 웹 검색 기반")
- **첫 실행 (스냅샷 없음)**: 변화 비교 불가 안내 + 베이스라인 스냅샷만 저장
- **전체 MCP 실패**: WebSearch만으로 최소 리포트 생성 + 경고 표시

## Notes

- `tech-taxonomy.md`의 검색 키워드를 OR 확장하여 쿼리 구성
- 리포트 생성 후 `/obsidian-bridge` 동기화 안내 출력
- 향후 cron 자동화: `claude -p "/weekly-monitor {domain}"` (수동 안정화 후)
