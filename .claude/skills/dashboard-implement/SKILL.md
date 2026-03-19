---
name: dashboard-implement
description: "대시보드 코드 변경을 구현 + 자동 검증하는 워크플로우. implementer → CSS 검증 → dashboard-review 체이닝."
user-invokable: true
argument-hint: "<변경 요청 설명>"
---

# Dashboard Implement Skill

대시보드 UI/CSS 변경을 구현하고, 자동 검증을 통과한 후에만 결과를 반환한다.

## 빠른 시작

```
/dashboard-implement 네트워크 페이지에 줌 컨트롤 추가
/dashboard-implement 다크모드에서 범례 텍스트 안보이는 버그 수정
```

## Input
- 변경 요청 설명 (자연어)

## Process

### Phase 1: 사전 분석 (P0 분류)

변경 요청을 분석하여 우선순위를 분류한다:
- **P0**: 기존 기능 유지 (다크/라이트 모드 가시성, 기존 동작 보존)
- **P1**: 요청된 변경 사항
- **P2**: 개선/정리 사항

CSS 변경이 포함된 경우, 수정 전에 반드시:
1. `theme.py`의 관련 셀렉터와 `!important` 규칙 목록을 파악
2. 영향받는 페이지의 기존 CSS 패턴 확인
3. 명시도(specificity) 충돌 가능성 사전 확인

### Phase 2: 구현

`implementer` 에이전트 (sonnet)를 사용하여 코드를 변경한다.

implementer에게 전달할 컨텍스트:
- P0/P1/P2 분류 결과
- theme.py CSS 셀렉터 분석 결과
- `docs/spec-dashboard-ui.md`의 CSS-01~04 규칙

### Phase 2.5: 스모크 테스트 (자동)

구현 완료 후, 수정된 파일에 대해 아래 검증을 순서대로 실행한다.
하나라도 실패하면 Phase 2로 돌아가 수정한다.

1. **Lint**: `cd projects/startup-db && ~/.local/bin/uv run ruff check src/startup_db/dashboard/pages/{modified_file}.py`
2. **컴파일**: `~/.local/bin/uv run python -m py_compile src/startup_db/dashboard/pages/{modified_file}.py`
3. **런타임 패턴 검사** (코드 리뷰):
   - `**dict` 언패킹과 동일 키워드 인자 중복 사용 (`update_layout(**PL, margin=...)` 등) → 반드시 별도 호출로 분리
   - Plotly `update_layout`에 존재하지 않는 파라미터 사용
   - 정의되지 않은 변수/컬럼 참조
   - import 누락
   - `render_plotly_animated` 사용 시: 범례/라벨이 차트 영역 밖으로 나가면 잘림 (overflow:hidden). 잘릴 위험 있으면 `st.plotly_chart` 사용 (CHART-02)

### Phase 3: CSS 다크모드 검증 (자동)

구현 완료 후 아래 검증을 자동 실행한다.
`validator` 에이전트 (sonnet)에게 다음 체크리스트를 전달:

#### 검증 체크리스트

**CSS-01 (다크모드 텍스트 커버리지)**:
- 수정된 페이지의 모든 텍스트 요소가 다크모드에서 가시적 색상을 사용하는지 확인
- `unsafe_allow_html=True` 사용 부분에서 theme.py `!important` 규칙과의 충돌 확인

**CSS-02 (인라인 HTML 호환)**:
- 인라인 `style="color:..."` 만 사용한 곳이 있으면 FAIL
- `<style>` 블록 + scoped class 패턴을 사용해야 PASS

**CSS-03 (-webkit-text-fill-color 동기화)**:
- `color: X !important` 설정 시 `-webkit-text-fill-color: X !important`도 있는지 확인

**CSS-04 (셀렉터 우선순위)**:
- 페이지 scoped CSS 명시도 ≥ theme.py 대응 셀렉터 명시도

**P0 보존 검증**:
- 변경 전 존재하던 다크/라이트 모드 텍스트 가시성이 유지되는지

#### 판정 기준
- 전 항목 PASS → Phase 4로 진행
- 1건이라도 FAIL → Phase 2로 돌아가 수정 (최대 2회 반복, 초과 시 사용자에게 이슈 보고)

### Phase 4: Dashboard Review

`/dashboard-review` 스킬의 로직을 실행하여 `docs/spec-dashboard-ui.md` 전체 체크리스트 대비 회귀 검증.

- PASS → Phase 5
- FAIL → Phase 2로 돌아가 수정

### Phase 5: 결과 보고

아래 형식으로 사용자에게 보고:

```markdown
## 구현 완료 — 결정 사항 체크리스트

- [x] P0: (기존 기능 보존 항목들)
- [x] P1: (요청된 변경 항목들)
- [ ] P2: (선택적 개선 — 미구현 시 사유)

## 검증 결과

| 단계 | 상태 | 비고 |
|------|------|------|
| CSS 다크모드 검증 | PASS/FAIL | (상세) |
| Dashboard Review | PASS/FAIL | (상세) |
| 반복 횟수 | N회 | |

## 변경 파일
| 파일 | 변경 내용 |
|------|----------|
```

## Output
- 검증 통과된 코드 변경
- 결정 사항 체크리스트 + 검증 결과 테이블

## Return
구현 완료 보고 (마크다운)

## Suggested Next Steps
- 브라우저에서 다크/라이트 모드 전환하며 육안 확인
- 문제 발견 시 `/dashboard-implement` 재실행
