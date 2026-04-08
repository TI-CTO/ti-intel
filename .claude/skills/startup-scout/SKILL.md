---
name: startup-scout
description: "스타트업 후보 발굴. 특정 도메인/키워드에서 신규 스타트업을 탐색하고 쇼트리스트를 생성한다."
user-invokable: true
argument-hint: "[domain or keyword]"
---

# Startup Scout — 스타트업 후보 발굴 스킬

특정 기술 도메인이나 키워드에서 유망 스타트업 후보를 탐색하고,
기존 DB 중복을 필터링한 뒤 쇼트리스트를 생성한다.
심층 분석은 하지 않는다 — 후보를 추려서 `/startup-analyst`로 넘기는 역할.

## 빠른 시작

```
/startup-scout voice AI
```

**실행 중:**
```
도메인 분석 → 키워드: TTS, ASR, voice cloning, conversational AI ...
WebSearch + intel-store 탐색 → 후보 15건
startup-db 중복 확인 → 기등록 8건 필터링
→ 신규 후보 7건 쇼트리스트 생성
```

**완료 시:**
```
신규 후보 7건 발굴 (기등록 8건 참고)
저장: outputs/reports/2026-03-13_scout-voice-ai.md

📋 Next Steps:
  → /startup-analyst {기업명} 심층 분석
```

---

## Arguments
- `domain`: 탐색할 기술 도메인 또는 키워드 (예: "voice AI", "edge AI security", "LLM infra")

## I/O Contract

### Input
| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| `domain` | yes | 자유 텍스트 | 탐색할 기술 도메인/키워드 |

### Output Files
| Artifact | Path Pattern | Description |
|----------|-------------|-------------|
| 쇼트리스트 | `outputs/reports/YYYY-MM-DD_scout-{domain-slug}.md` | 후보 리스트 + 발굴 근거 |

### Return
```yaml
status: pass
summary: "{domain} — 신규 {N}건 발굴, 기등록 {M}건"
file_path: "리포트 절대 경로"
candidates: N
domain: "{domain}"
```

## Process

### Step 1: 탐색 범위 설정
사용자가 제시한 키워드/도메인을 확인하고, 검색 전략을 수립한다.
startup-db의 기존 카테고리(7개: Service, S/W Platform, AI 산업 특화, Model/Engine, Infra, Ops, Data)와 대조하여 범위 명확화.

### Step 2: 멀티소스 탐색

**웹 검색:**
- WebSearch로 최근 6개월 내 펀딩 뉴스, 제품 출시, 수상 내역 검색
- 검색 쿼리 예시: `"{키워드}" startup funding 2026`, `"{도메인}" 스타트업 투자 유치`

**intel-store 연동 (MCP 사용 가능 시):**
- `search_intel(query="{키워드}", types=["news"], since="최근 3개월")` — 관련 뉴스에서 기업명 추출
- `collect_news(topic=..., query="{키워드}")` — 신규 수집 후 기업명 추출

**한국 스타트업 특화 소스:**
- 스타트업얼라이언스, 스타트업레시피, 플래텀, 벤처스퀘어 키워드 검색
- TheVC(thevc.kr) — 최근 투자 유치 기업 확인

### Step 3: 중복 필터링
발견한 각 후보에 대해 `search_companies(query="{기업명}")`로 기존 DB 확인.
이미 등록된 기업은 "기등록" 섹션에 표시.

### Step 4: 쇼트리스트 작성 및 저장

저장 경로: `/Users/ctoti/Project/ClaudeCode/outputs/reports/{YYYY-MM-DD}_scout-{domain-slug}.md`

## Output Format

```markdown
---
domain: {탐색 도메인/키워드}
date: {YYYY-MM-DD}
skill: startup-scout
candidates: {N}건
---

# Startup Scout: {도메인/키워드}

## 탐색 범위
- 키워드: ...
- 기간: 최근 N개월
- 소스: WebSearch, intel-store, TheVC, ...

## 후보 리스트

| # | 기업명 | 국가 | 핵심 기술/제품 | 발굴 근거 | 출처 |
|---|--------|------|---------------|----------|------|
| 1 | {name} | {country} | {1줄 요약} | {왜 주목하는가} | {URL} |

## 기등록 기업 (참고)
- {기업명} — 이미 DB에 등록됨, 최근 동향: {간단 요약}

## References
| # | 출처 | URL | 날짜 |
|---|------|-----|------|
```

## Critical Rules
- NEVER perform deep analysis — 1줄 요약과 발굴 근거만 제시. 상세 조사는 `/startup-analyst`의 역할
- 발굴된 기업은 startup-db에 자동 등록 (`upsert_company`)
- NEVER fabricate company names or funding info — 검색에서 확인된 사실만 기재
- 기등록 기업도 최근 동향이 있으면 "기등록" 섹션에 포함하여 업데이트 필요성 표시

## Success Metrics
- 후보 최소 5건 이상 (도메인이 좁으면 3건)
- 각 후보에 출처 URL 1건 이상
- 기존 DB 중복 확인 100% (전수 search_companies 호출)

## Next Steps

저장 완료 후 아래 후속 옵션을 사용자에게 제시한다:

```
📋 Next Steps:
  🔍 특정 기업 심층 분석:
    → /startup-analyst {기업명}                — 팩트 검증 + DB 입력용 JSON
  📄 PDF 변환:
    → /report-pdf {리포트 경로}                — 컨설팅 스타일 PDF
  📂 Obsidian 동기화:
    → /obsidian-bridge {리포트 경로} research   — 볼트에 동기화
```

## Notes
- MCP 서버가 응답하지 않으면 WebSearch로 대체하고 한계를 보고서에 명시
- 후보가 5건 미만이면 검색 키워드를 확장하여 재탐색
- 검색 중 발견한 투자자/VC 정보는 별도 메모하여 향후 `upsert_investor` 입력 소스로 활용
