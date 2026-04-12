# Weekly Writing Rules

주간 리포트의 형식 품질을 일관되게 유지하기 위한 공통 작성 규칙이다.  
특히 ClaudeCode와 Codex 결과를 비교할 때, 구조 차이보다 실행 엔진 차이만 드러나게 하는 것이 목적이다.

## 목적

- 기존 팀 산출물과 형식을 맞춘다
- 같은 주제의 Claude/Codex 결과를 공정하게 비교 가능하게 만든다
- 생성 후 수작업 교정을 줄인다

## 적용 범위

- `outputs/reports/weekly/*.md`
- 도메인별 weekly report
- ClaudeCode 기반 weekly
- Codex 기반 weekly

## 최우선 원칙

1. 새 포맷을 만들지 않는다
2. 같은 도메인의 최신 weekly 리포트를 구조 템플릿으로 삼는다
3. 내용보다 먼저 형식 호환성을 맞춘다
4. 확실하지 않은 항목은 빼더라도 형식은 깨지지 않게 유지한다

## frontmatter 규칙

다음 키 구조를 우선 유지한다.

```yaml
---
type: weekly-monitor
domain: <domain>
week: <YYYY-Www>
date: <YYYY-MM-DD>
l3_count: <number>
deep_count: <number>
tags:
  - <engine>
  - weekly
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---
```

규칙:
- `type`은 항상 `weekly-monitor`
- `domain`은 폴더/파일명과 일치
- `created`, `updated`는 생성일 기준으로 채운다
- 비교 실험이면 `tags`에 엔진 표기(`claude-code` 또는 `codex`)를 넣는다

## 섹션 순서 규칙

같은 도메인의 최신 weekly 리포트와 같은 순서를 우선 사용한다.

기본 구조:

1. `## Executive Summary`
2. `## 🟢 Quick 요약 (변화 미미)`
3. `## 🟡🔴 Deep 심층 분석`
4. `## 경쟁사 동향 (SKT / KT)` 또는 도메인 맞춤 경쟁사 섹션
5. `## 규제 & 거버넌스`
6. `## 종합 시사점 및 후속 조치`
7. `## References`

규칙:
- 섹션명을 불필요하게 영어/한글로 바꾸지 않는다
- 기존 weekly에서 쓰는 제목 스타일을 그대로 따른다
- deep section 수가 달라져도 최소 2개 이상의 핵심 심층 섹션을 유지하는 방향을 우선 검토한다

## References 규칙

이 규칙은 반드시 지킨다.

References 표 기본 형식:

```md
| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | 출처명 | [링크](https://example.com) | news | 2026-04-01 | [A] |
```

세부 규칙:
- `URL` 컬럼에는 원문 URL 문자열을 직접 넣지 않는다
- 항상 `[링크](URL)` 형식을 사용한다
- 식별자는 `G-`, `P-`, `E-`, `C-` 등 기존 체계를 따른다
- 본문 인라인 인용 `[[G-01]](#ref-g-01)`과 References anchor id가 일치해야 한다
- `출처` 컬럼은 사이트명만 쓰지 말고 문서/발표명을 함께 적는다
- `유형`, `날짜`, `신뢰도` 컬럼을 비우지 않는다

## 본문 인용 규칙

- 본문에서는 `[[G-01]](#ref-g-01)` 형태를 사용한다
- References에 없는 인용 코드를 본문에 쓰지 않는다
- 약한 출처는 본문에서 단정적으로 쓰지 않는다

## 비교 실험 규칙

Claude/Codex 비교 시:

- 같은 날짜 범위
- 같은 도메인
- 같은 출력 형식
- 같은 파일명 규칙
- 같은 섹션 순서
- 같은 References 표 구조

만 다르고, 엔진만 달라야 한다.

## 생성 전 체크리스트

- 최신 same-domain weekly를 열었는가
- frontmatter 키 순서를 맞췄는가
- 섹션 순서를 복제했는가
- References 표 컬럼 순서를 맞췄는가
- URL 컬럼이 모두 `[링크](...)` 형식인가

## 생성 후 체크리스트

- 파일명 규칙이 맞는가
- 본문 인용 코드와 References anchor가 일치하는가
- raw URL이 References URL 컬럼에 남아 있지 않은가
- `## References` 표가 기존 weekly와 같은 형식인가
- PDF 변환 전 표/헤딩 구조를 한 번 더 점검했는가

## 금지 사항

- References의 URL 컬럼에 raw URL 직접 삽입
- 기존 weekly 구조와 다른 임의 섹션명 추가
- anchor 없는 인용 코드 사용
- 출처를 만들거나, 확인되지 않은 수치를 사실처럼 서술
