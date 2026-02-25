---
name: slides
description: 마크다운 파일을 디자인 테마가 적용된 PPTX 프레젠테이션으로 변환한다.
user_invocable: true
arguments: "[theme] <file_path>"
---

# /slides — Markdown to Presentation

마크다운 파일을 디자인 시스템 테마가 적용된 PPTX 프레젠테이션으로 변환합니다.

## 사용법

```
/slides                          → 테마 목록 표시 + 파일 선택 안내
/slides <file_path>              → professional 테마로 변환
/slides minimal <file_path>      → minimal 테마로 변환
/slides dark <file_path>         → dark 테마로 변환
```

## 실행 절차

### 1. 입력 파싱

인자가 없으면 사용 가능한 테마를 안내하고 파일 경로를 요청한다.
인자가 있으면:
- 첫 번째 인자가 테마 이름이면 테마로 사용, 나머지가 파일 경로
- 첫 번째 인자가 파일 경로이면 professional 테마를 기본 적용

### 2. 파일 확인

- 파일이 존재하는지 확인
- `.md` 확장자인지 확인
- 파일 내용을 Read 도구로 읽어 미리 확인

### 3. PPTX 생성

design-system MCP의 `render_pptx` 도구를 호출한다:

```json
{
  "markdown_path": "/absolute/path/to/file.md",
  "theme": "professional"
}
```

### 4. 결과 보고

생성된 파일 경로, 슬라이드 수, 적용 테마를 사용자에게 보고한다.

## 테마 목록

| 테마 | 설명 |
|------|------|
| `professional` | 기업 프레젠테이션용. 마젠타 포인트, 깔끔한 레이아웃 |
| `minimal` | 미니멀 흑백. 타이포그래피 중심, 최소 색상 |
| `dark` | 다크 배경. 밝은 텍스트, 선명한 포인트 색상 |

## 슬라이드 매핑

마크다운 요소가 자동으로 슬라이드 타입에 매핑된다:

| MD 요소 | 슬라이드 |
|---------|---------|
| `# H1` | 표지 |
| `## H2` | 섹션 구분 |
| `> 인용문` | 핵심 메시지 |
| `| 표 |` | 표 |
| `- 리스트` | 불릿 |
| 일반 텍스트 | 본문 |

## MCP 의존성

- `design-system` MCP 서버 필요 (`.mcp.json`에 등록)

## 예시

```
/slides outputs/reports/2026-02-24_wtis-proposal-self-evolving-agent-final.md
```
→ `outputs/reports/2026-02-24_wtis-proposal-self-evolving-agent-final.professional.pptx` 생성
