---
name: dashboard-review
description: 대시보드 UI/UX 체크리스트를 검증하여 회귀(regression)를 감지한다. 구현 변경 후 자동 점검용.
invocation: "/dashboard-review"
---

# Dashboard Review Skill

대시보드 코드가 `docs/spec-dashboard-ui.md`의 UI/UX 규칙을 준수하는지 자동 검증한다.

## Input
없음 (자동으로 spec 파일과 소스 코드를 비교)

## Process

### Step 1: Spec 로드
`docs/spec-dashboard-ui.md`를 읽어 체크리스트 항목을 파싱한다.

### Step 2: 소스 코드 검증
각 체크리스트 항목에 대해 해당 소스 파일을 읽고 규칙 준수 여부를 확인한다.

검증 대상 파일:
- `projects/startup-db/src/startup_db/dashboard/theme.py`
- `projects/startup-db/src/startup_db/dashboard/components.py`
- `projects/startup-db/src/startup_db/dashboard/pages/*.py`

검증 방법:
- **THEME-***: `theme.py`에서 팔레트 값, CSS 규칙 존재 여부 확인
- **CSS-***: `theme.py` + 페이지 CSS에서 다크모드 텍스트 커버리지, 셀렉터 우선순위, `-webkit-text-fill-color` 동기화 확인
- **NAV-***: `components.py`에서 네비게이션 구현 확인
- **TABLE-***: 페이지 파일에서 `render_styled_dataframe` 사용 여부 확인
- **NETWORK-***: `network.py`에서 그래프 설정 확인
- **CHART-***: 차트 관련 페이지에서 스타일 파라미터 확인

### Step 3: 결과 보고

아래 형식으로 결과를 출력한다:

```
## Dashboard UI Review Report

### Summary
- Total: N checks
- ✅ Pass: X
- ❌ Fail: Y
- ⚠️ Warning: Z

### Details
| ID | Rule | Status | Note |
|----|------|--------|------|
| THEME-01 | 라이트 모드 텍스트 가시성 | ✅ | LIGHT["text"] == "#402B3A" |
| THEME-02 | 사이드바 셀렉트박스 텍스트 | ❌ | `!important` 누락 |
| ... | ... | ... | ... |
```

## Output
- 콘솔에 체크리스트 검증 결과 테이블 출력
- 실패 항목이 있으면 수정 방법 제안

## Return
검증 결과 테이블 (마크다운)

## Suggested Next Steps
- 실패 항목 수정 후 `/dashboard-review` 재실행
- 새 UI 규칙 추가 시 `docs/spec-dashboard-ui.md`에 항목 추가
