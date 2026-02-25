---
name: discover
description: "신기술/기회 탐색. 주어진 도메인에서 신규 기술 기회를 발굴하고 우선순위를 매긴다."
user-invokable: true
argument-hint: "[domain or technology area]"
---

# Discover — 기술 기회 탐색 스킬

주어진 도메인에서 신기술/기회를 체계적으로 탐색하고 2×2 우선순위 매트릭스로 정리한다.
WTIS SKILL-3(발굴)의 범용화 버전 — 특정 도메인에 종속되지 않는다.

## Arguments
- `domain`: 탐색할 기술 도메인 (예: "edge AI", "quantum networking", "6G")
- `portfolio` (선택): 기존 보유 과제/기술 목록 (중복 방지용)
- `competitors` (선택): 비교 대상 경쟁사 목록
- `taxonomy` (선택): 기술 분류 체계

## Process

### Phase 1: 도메인 분석 (sonnet)
1. 제공된 도메인에 대한 탐색 방향과 검색 전략 수립
2. 핵심 기술 키워드 3-7개 도출
3. 기존 포트폴리오(제공 시)와 비교하여 공백 영역 파악

### Phase 2: 다중 소스 탐색
다음 소스를 **병렬**로 탐색한다:

**MCP Sources:**
- `research-hub`: `get_trending_papers(topic=..., since=..., limit=20)` — 최신 학술 동향
- `patent-intel`: `get_recent_patents(topic=..., limit=20)` — 특허 출원 동향
- `trend-tracker`: `search_news(topic=..., query=..., limit=20)` — 시장/뉴스 동향

**Web Sources (보완):**
- WebSearch로 최근 6개월 주요 뉴스/보고서 검색
- 필요 시 특정 URL WebFetch

### Phase 3: 기회 분석 (sonnet)
수집된 데이터를 바탕으로:

1. **3-Layer 니즈 분석**
   - 표면 니즈: 명시적으로 요청/언급된 것
   - 잠재 니즈: 행동/동향에서 추론 가능한 것
   - 미충족 니즈: 현재 솔루션이 없는 영역

2. **경쟁 동향 분석** (competitors 제공 시)
   - 각사 최근 움직임 요약
   - 선점/공백 영역 구분

3. **기술 성숙도 평가**
   - TRL 추정 (1~9)
   - 논문·특허 근거 제시

### Phase 4: 우선순위 매트릭스 (sonnet)
최소 5개 기회 후보에 대해:

```
우선순위 = 전략 가치 × 실행 가능성

전략 가치 (1-10): 시장 크기, 경쟁 차별화, 미래 성장성
실행 가능성 (1-10): 기술 성숙도, 내부 역량, 소요 자원

분류:
- 즉시착수 (가치≥7, 실행≥7)
- 역량확보후 (가치≥7, 실행<7)
- 검토 (가치<7, 실행≥7)
- 보류 (가치<7, 실행<7)
```

### Phase 5: 저장
결과를 저장:
`/Users/ctoti/Project/ClaudeCode/research/sessions/{YYYY-MM-DD}_discover-{domain-slug}.md`

## Output Format

```markdown
---
topic: {domain}
date: {YYYY-MM-DD}
skill: discover
confidence: high | medium | low
sources_used: [research-hub, patent-intel, trend-tracker, websearch]
---

# Discover Report: {Domain}

## Executive Summary
> (3줄: 탐색 범위, 핵심 발견, 최우선 기회)

## 탐색 도메인
> (정의, 범위, 탐색 방향)

## 기술 동향 신호
### 학술 동향 (research-hub)
### 특허 동향 (patent-intel)
### 시장/뉴스 동향 (trend-tracker + WebSearch)

## 3-Layer 니즈 분석
| 니즈 유형 | 내용 | 근거 |
|-----------|------|------|
| 표면 니즈 | | |
| 잠재 니즈 | | |
| 미충족 니즈 | | |

## 기회 후보 목록
| # | 기회명 | 전략가치 | 실행가능성 | 분류 | 근거 |
|---|--------|---------|-----------|------|------|

## 우선순위 매트릭스
```
         높은 실행가능성
              │
  역량확보후  │  즉시착수
              │
──────────────┼──────────────
              │
  보류        │  검토
              │
         낮은 실행가능성
  낮은 가치 ←──→ 높은 가치
```

## 즉시착수 기회 상세
(최우선 1-3개에 대한 상세 설명)

## References
| # | 출처명 | URL | 발행일 | 접근일 | 신뢰도 |
|---|--------|-----|--------|--------|--------|
```

## Return
```
status: pass
summary: (200자 이내 — 도메인, 발견된 기회 수, 최우선 기회명)
file_path: (절대 경로)
```

## Notes
- MCP 서버가 응답하지 않으면 WebSearch로 대체하고 한계를 보고서에 명시
- 기회 후보가 5개 미만이면 WebSearch 범위를 확장하여 재탐색
- 기존 포트폴리오(제공 시)와 중복되는 후보는 명시적으로 제외
