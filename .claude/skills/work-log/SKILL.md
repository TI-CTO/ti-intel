---
name: work-log
description: "현재 세션의 작업 내용을 Obsidian 업무일지에 기록한다. 신규 생성 또는 기존 일지에 추가."
user-invokable: true
argument-hint: "[update]"
---

# Work Log

현재 대화에서 수행한 작업을 Obsidian 업무일지로 기록한다.

## Arguments
- 인자 없음: 오늘 일지를 새로 생성하거나, 기존 일지가 있으면 새 작업만 추가
- `update`: 기존 일지에 이후 진행한 내용만 추가 (명시적 업데이트)

## Configuration
- **저장 경로**: `/Users/ctoti/Obsidian/Obsidian_Work/60-ClaudeCode/WorkLogs/`
- **파일명**: `{YYYY-MM-DD}_daily-log.md`
- **태그**: `claude-code`, `work-log`

## Process

### 1. 기존 일지 확인
오늘 날짜의 일지 파일이 존재하는지 Read로 확인한다:
- 경로: `/Users/ctoti/Obsidian/Obsidian_Work/60-ClaudeCode/WorkLogs/{YYYY-MM-DD}_daily-log.md`

### 2. 대화 컨텍스트 분석
현재 세션에서 수행한 작업을 분석한다:
- 어떤 파일을 수정/생성했는가
- 어떤 문제를 해결했는가
- 어떤 결정을 내렸는가
- 사용자와 어떤 논의가 있었는가

### 3-A. 신규 생성 (기존 일지 없음)
파일을 새로 생성한다:

```markdown
---
tags: [claude-code, work-log]
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
project: {주로 작업한 프로젝트명, 여러 개면 쉼표 구분}
---

# {YYYY-MM-DD} 업무일지

## 작업 요약
{1-2문장 전체 요약}

---

## 1. {작업 제목}
{작업 내용 상세}

### 수정/생성 파일
{해당하는 경우 테이블 또는 리스트}

### 개선 효과 / 해결한 이슈
{구체적인 before/after 또는 효과}

---

## 느낀점
{기술적 인사이트, 배운 점}
```

### 3-B. 기존 일지에 추가 (기존 일지 있음)
1. 기존 일지를 Read로 읽는다
2. 이미 기록된 내용과 현재 대화 컨텍스트를 비교한다
3. **아직 기록되지 않은 새 작업만** 식별한다
4. 기존 일지의 마지막 섹션 번호를 확인하고 이어서 번호를 매긴다
5. `느낀점` 섹션 위에 새 작업 섹션을 삽입한다
6. `느낀점`에도 새로운 인사이트가 있으면 추가한다
7. frontmatter의 `updated` 날짜를 오늘로 갱신한다
8. 필요시 `project` 필드에 새 프로젝트명을 추가한다

### 4. 결과 보고
- 생성/수정된 파일 경로
- 추가된 작업 항목 요약 (1줄씩)
- 신규 생성인지 업데이트인지 명시

## Writing Guidelines
- 대화/설명은 한국어, 코드/변수명은 영어
- 작업 제목은 간결하게 (예: "KT 스크래퍼 버그 수정", "Playwright 다운로더 구현")
- 수정 파일은 프로젝트 루트 기준 상대 경로 사용
- 개선 효과는 구체적으로 (before/after, 수치, 영향 범위)
- 느낀점은 기술적 인사이트 중심 (감상이 아닌 교훈)
