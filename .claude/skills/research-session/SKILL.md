---
name: research-session
description: "구조화된 리서치 세션을 시작한다. 주제를 조사하고 결과를 outputs/reports/에 저장한다."
user-invokable: true
argument-hint: "[topic to research]"
---

# Research Session

주어진 주제에 대해 체계적인 리서치 세션을 수행한다.

## 빠른 시작

```
/research-session MCP 서버 성능 최적화 방법
```

**실행 중:**
```
기존 리서치 확인: 관련 파일 없음
심층 조사: WebSearch 12건, intel-store 5건 수집 중...
```

**완료 시:**
```
리서치 완료 — 핵심 발견 6건
신뢰도: medium (WebSearch 중심)
저장: outputs/reports/2026-02-26_mcp-performance-optimization.md
→ Obsidian 동기화: /obsidian-bridge [경로] research
```

---

## Arguments
- 리서치할 주제 (자유 형식)

## I/O Contract

### Input
| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| `topic` | yes | 자유 텍스트 | 리서치할 주제 |

### Output Files
| Artifact | Path Pattern | Description |
|----------|-------------|-------------|
| 리포트 | `outputs/reports/YYYY-MM-DD_{topic-slug}.md` | 구조화된 리서치 노트 |

### Return
```yaml
status: completed | needs-followup
summary: "{topic} — 핵심 발견 {N}건, 신뢰도 {level}"
file_path: "리포트 절대 경로"
confidence: "high | medium | low"
```

## Process

### Phase 1: 기존 지식 확인
- `outputs/reports/` Glob으로 파일 목록 조회
- 파일명 kebab-case 토큰 또는 frontmatter `topic` 필드로 키워드 매칭
- 매칭 파일의 frontmatter(`topic`, `date`, `confidence`) + 경영진 요약 첫 5줄 발췌
- 발견 시: Phase 2에서 동일 결론 반복하지 않고 변화/추가 사항에 집중
- 없으면: 전체 조사 실행 (기본 흐름)

### Phase 2: 심층 조사
- 관련 소스 파일, 문서, 레퍼런스 읽기
- 선택지가 있는 주제라면 대안 비교
- 구체적인 코드 예시, 파일 경로, 라인 번호 기록
- 필요 시 WebSearch/WebFetch로 외부 정보 수집

**MCP 데이터 소스 활용 (주제가 기술 트렌드/논문/특허 관련인 경우):**
- `intel-store`: `search_intel(query=..., topic=..., mode="semantic", limit=10)` — 통합 검색 (뉴스+논문+특허)
- `intel-store`: `collect_papers(topic=..., query=..., limit=10)` — Semantic Scholar 논문 수집+저장
- `intel-store`: `collect_news(topic=..., query=..., limit=10)` — Tavily/GDELT 뉴스 수집+저장
- `intel-store`: `find_similar(text=..., limit=5)` — 시맨틱 유사 아이템 탐색
- 등록된 토픽 슬러그: `ai-network`, `6g`, `network-slicing`, `edge-computing`, `quantum-comm`, `llm-telecom`, `open-ran`, `digital-twin`

### Phase 3: 구조화된 출력
다음 형식으로 리서치 노트를 작성한다:

```markdown
---
topic: {research topic}
date: {today YYYY-MM-DD}
confidence: high|medium|low
status: completed|needs-followup
---

# Research: {topic}

## 연구 질문
> 무엇을 알아내려 했는가

## 핵심 발견
1. (번호 매긴 발견사항, 근거 포함)

## 비교 분석 (해당 시)
| 기준 | 옵션 A | 옵션 B |
|------|--------|--------|
| ...  | ...    | ...    |

## 신뢰도 평가
- 높은 확신:
- 추가 검증 필요:

## 액션 아이템
- [ ] (후속 작업)

## 참고 자료
- (파일 경로, URL, 문서 참조)
```

### Phase 4: 저장
결과를 다음 경로에 저장:
`/Users/ctoti/Project/ClaudeCode/outputs/reports/{YYYY-MM-DD}_{topic-slug}.md`

### Phase 5: Next Steps 안내

저장 완료 후 아래 후속 옵션을 사용자에게 제시한다:

```
📋 Next Steps:
  ✅ 기술 타당성 검증이 필요하면:
    → /wtis standard {주제} Go/No-Go 검증          — 200점 채점 + 3B 전략
  🔍 더 넓은 기회 탐색이 필요하면:
    → /discover {도메인}                           — 신기술 기회 발굴 + 우선순위
  📄 PDF 변환:
    → /report-pdf {리포트 경로}                    — 컨설팅 스타일 PDF
  📂 Obsidian 동기화:
    → /obsidian-bridge {리포트 경로} research        — 볼트에 동기화
  📝 작업 기록:
    → /work-log                                    — 리서치 내용 일지에 기록
```
