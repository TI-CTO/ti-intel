---
globs: "projects/design-system/**/*.py"
---

# Design System Rules

## PDF 파일명
출력 파일명에 `.professional` 등 테마 접미사를 붙이지 않는다. 항상 `{stem}.pdf` / `{stem}.pptx`만 사용.

## paged.js 핵심 규칙
- body/wrapper에 절대 width 하드코딩 금지 → `width: 100%` 사용
- `:has()` 선택자: paged.js 미지원 → 포스트프로세서에서 클래스 직접 추가
- 30행 초과 테이블: `_split_large_tables()`로 분할 (paged.js 테이블 중복 렌더링 버그 우회)
- `@page` margin box: CSS가 아닌 `afterRendered()` JS로 주입
- nowrap 전면 제거: 모든 열 `white-space: normal`
- 5열+ 테이블: 포스트프로세서에서 `wide-table` 클래스 자동 부여

## Citation badge
- 마크다운 인용 형식: `[S-01](#ref-s-01)` (단일 대괄호 + 앵커 링크)
- References 앵커: `<a id="ref-s-01"></a>S-01`
- 접미사 ID 금지 (G-01-S 등): 순차 번호만 사용 (G-01, G-02, ...)
- `_preprocess()`에서 citation 패턴은 wikilink 변환 스킵

## MCP 서버 코드 수정 후
소스 수정 후 반드시 MCP 서버 프로세스 재시작 (메모리 캐싱으로 변경 미반영). `kill <PID>` → Claude Code가 자동 재시작.
