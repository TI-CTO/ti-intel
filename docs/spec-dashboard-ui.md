# Startup DB Dashboard — UI/UX Specification

이 문서는 대시보드 UI/UX 규칙의 원본(Single Source of Truth)이다.
`/dashboard-review` 스킬이 이 문서를 기준으로 회귀(regression)를 검증한다.

## Color Palettes

### Signature
- PRIMARY: `#C50063`
- PRIMARY_DARK: `#8B0042`
- PRIMARY_GRADIENT: `linear-gradient(135deg, #C50063 0%, #8B0042 100%)`

### Light Mode — Glassmorphism (Soft Sand)
| Role | Value | Usage |
|------|-------|-------|
| bg | gradient `#f5f0e8 → #e8d5c4 → #f0dbd8` | 페이지 배경 (베이지+로즈+웜그레이) |
| card | `rgba(255, 255, 255, 0.5)` | 카드/컨테이너 배경 (반투명 글래스) |
| glass_border | `rgba(255, 255, 255, 0.65)` | 글래스 패널 테두리 |
| glass_blur | `16px` | backdrop-filter blur 값 |
| text | `#3D2B1F` | 본문 텍스트 (다크 브라운) |
| text_secondary | `#7A6558` | 보조 텍스트 |
| sidebar_bg | gradient `rgba(197,0,99,0.85) → rgba(64,43,58,0.92)` | 사이드바 배경 |

### Dark Mode — Dark Glassmorphism
| Role | Value | Usage |
|------|-------|-------|
| bg | gradient `#0f0c29 → #302b63 → #24243e` | 페이지 배경 (딥 퍼플 그라데이션) |
| card | `rgba(255, 255, 255, 0.06)` | 카드/컨테이너 배경 (다크 글래스) |
| glass_border | `rgba(255, 255, 255, 0.12)` | 글래스 패널 테두리 |
| glass_blur | `20px` | backdrop-filter blur 값 |
| text | `#E8E0F0` | 본문 텍스트 (라이트 라벤더) |
| text_secondary | `#A89BBF` | 보조 텍스트 |
| sidebar_bg | gradient `rgba(15,12,41,0.95) → rgba(59,28,50,0.9)` | 사이드바 배경 |

### Glassmorphism 핵심 속성
모든 카드/패널/컨테이너에 일관 적용:
- `backdrop-filter: blur(Npx)` — 뒤 배경 흐림 효과
- 반투명 `rgba()` 배경색
- 미세한 흰색 테두리 (`glass_border`)
- 소프트 그림자 (`glass_shadow`)
- `border-radius: 16px` (카드), `12px` (입력/탭)

---

## Checklist

### THEME-01: 라이트 모드 텍스트 가시성
- **규칙**: 메인 영역 모든 텍스트는 `#3D2B1F` (다크 브라운)
- **검증**: `theme.py`에서 LIGHT["text"] == "#3D2B1F"
- **위험**: `.stApp` 루트에 color를 넣으면 사이드바까지 오염됨 → `.main` 스코프로 제한

### THEME-02: 사이드바 셀렉트박스 텍스트
- **규칙**: 사이드바 셀렉트박스는 반투명 배경 + 흰색 텍스트
- **검증**: CSS에 `section[data-testid="stSidebar"] .stSelectbox > div > div`에 `background: rgba(255,255,255,0.1) !important` + `color: white !important`
- **위험**: 메인 영역의 `.stSelectbox` 규칙이 `!important`로 사이드바까지 덮어씀 → 사이드바 규칙도 `!important` 필수

### THEME-03: 사이드바 드롭다운 화살표
- **규칙**: 사이드바 셀렉트박스의 SVG 아이콘(chevron)이 보여야 함
- **검증**: CSS에 `section[data-testid="stSidebar"] .stSelectbox svg { fill: white }` 존재

### THEME-04: 선택된 탭 텍스트
- **규칙**: 선택된 탭은 underline 스타일 (`border-bottom: 2px solid PRIMARY`) + **테마 텍스트 색상** + `font-weight: 600`
- **검증**: `[aria-selected="true"] *`에 `color: {c["text"]} !important` + `-webkit-text-fill-color: {c["text"]} !important`

### THEME-05: 다크 모드 헤더 영역
- **규칙**: Deploy 버튼이 있는 Streamlit 헤더도 다크 글래스 배경
- **검증**: 다크 전용 CSS에 `header[data-testid="stHeader"] { background: rgba(15,12,41,0.8) }` + `backdrop-filter: blur(16px)`

### THEME-06: 다크 모드 내비바 브랜드
- **규칙**: "Startup DB" 텍스트가 다크 배경에서 밝은 그라데이션
- **검증**: 다크 전용 CSS에 `.nav-brand { background: linear-gradient(135deg, #FF9BD2 0%, #C50063 100%) }`

### THEME-07: 사이드바 페이지 네비게이션 숨김
- **규칙**: Streamlit 기본 사이드바 페이지 링크는 숨김 (내비바와 중복)
- **검증**: CSS에 `section[data-testid="stSidebar"] nav { display: none !important }`

### THEME-08: 글래스모피즘 일관성
- **규칙**: 카드/메트릭/네비바/탭/버튼에 `backdrop-filter: blur()` + 반투명 배경 적용
- **검증**: `_glass_css()` 헬퍼 함수가 inject_css, render_company_cards에서 사용됨
- **위험**: `backdrop-filter`는 Safari에서 `-webkit-` 접두사 필수

---

### NAV-01: 다크 모드 전환 위치
- **규칙**: 내비바 우측 끝에 🌙/☀️ 아이콘 (HTML `<a>` 링크)
- **검증**: `render_navbar`에서 `nav-theme-toggle` 클래스 링크 존재

### NAV-02: 다크 모드 설정 영속성
- **규칙**: 페이지 이동 시에도 다크 모드 유지
- **검증**: `components.py`에 `_save_theme()` / `_load_theme()` 존재, `.theme_pref.json` 파일 사용

### NAV-03: SPA 네비게이션
- **규칙**: 페이지 전환 시 전체 리로드 없이 컨텐츠만 교체
- **검증**: `app.py`에서 `st.navigation` + `st.Page` 사용, 개별 페이지 파일에 `st.set_page_config` 없음

---

### TABLE-01: 스타일드 HTML 테이블
- **규칙**: Companies, Investors 페이지의 테이블은 `render_styled_dataframe()` 사용. 리스트뷰 등 특화 기능(L1 뱃지, 행 링크)이 필요한 경우 별도 구현 허용하되, 테마 색상(`row_bg`, `row_alt_bg` 등)은 동일 값 사용
- **검증**: 해당 페이지에서 `st.dataframe` 대신 `render_styled_dataframe` 또는 동일 테마 값 적용 커스텀 테이블 사용
- **이유**: `st.dataframe`(glide-data-grid)은 캔버스 기반으로 다크 모드 CSS 적용 불가

### TABLE-02: 테이블 교차행 색상
- **규칙**: 라이트 — `rgba(255,255,255,0.35)` / `rgba(255,255,255,0.55)`, 다크 — `rgba(255,255,255,0.03)` / `rgba(255,255,255,0.07)`
- **검증**: `render_styled_dataframe`의 `row_bg` / `row_alt_bg` 값

---

### NETWORK-01: 선택된 서브카테고리 표시
- **규칙**: 서브카테고리 선택 시 `st.subheader(f"📂 {selected_sub}")` + 회사/관계 수 캡션
- **검증**: `network.py`에 `st.subheader` 호출 존재

### NETWORK-02: 엣지 라벨 숨김
- **규칙**: 엣지 라벨은 표시하지 않음, hover tooltip으로 대체
- **검증**: vis.js Edge 딕셔너리에 `label` 키 미설정 (vis.js 기본값 = 라벨 없음) 또는 `label: ""`, `title=` 에 관계 정보

### NETWORK-03: 노드 크기 차등화
- **규칙**: 연결 수(degree) 기반 노드 크기 12~45px
- **검증**: `node_size = max(12, min(45, 12 + deg * 4))`

### NETWORK-04: 관계 유형 필터
- **규칙**: 사이드바에 멀티셀렉트로 관계 유형 필터
- **검증**: `st.multiselect("Relation types", ...)` 존재

### NETWORK-05: 엣지/노드 범례
- **규칙**: 노드 상태 색상 + 엣지 관계 유형 색상 범례 분리 표시
- **검증**: "Node — Status" + "Edge — Relation Type" 범례 섹션 존재

---

### CSS-01: 다크모드 텍스트 커버리지
- **규칙**: Streamlit 메인 영역의 **모든** 텍스트 요소(h1-h4, p, span, label, summary, details, expander)에 다크모드 텍스트 색상 적용
- **검증**: `theme.py`에 아래 셀렉터가 `{c["text"]} !important`로 존재:
  - `.main h1~h4`, `.main p`, `.main span`, `.main label`
  - `.main [data-testid="stExpander"] summary`, `.main [data-testid="stExpander"] summary *`
  - `.main [data-testid="stExpander"] [data-testid="stExpanderDetails"]`, `... *`
- **위험**: 새 Streamlit 컴포넌트 추가 시 텍스트 셀렉터 누락 가능

### CSS-02: 인라인 HTML 다크모드 호환
- **규칙**: `st.markdown(unsafe_allow_html=True)`로 삽입하는 HTML에 `theme.py`의 `!important` 규칙이 적용됨. 인라인 `style="color:..."` 만으로는 `!important`를 이길 수 없음
- **검증 방법**:
  1. 페이지에서 `unsafe_allow_html=True` 사용 부분을 모두 찾는다
  2. 해당 HTML 내 텍스트가 theme.py의 전역 규칙으로 커버되는지 확인
  3. 커버 안 되면 `<style>` 블록으로 scoped class를 주입하되, `color` + `-webkit-text-fill-color` 모두 `!important`로 설정
- **위험**: Streamlit이 인라인 style의 `!important`를 제거할 수 있음 → 반드시 `<style>` 블록 사용

### CSS-03: -webkit-text-fill-color 동기화
- **규칙**: `color: X !important` 설정 시 반드시 `-webkit-text-fill-color: X !important`도 함께 설정
- **검증**: theme.py 및 페이지 CSS에서 `color:.*!important` 패턴이 있으면 같은 블록에 `-webkit-text-fill-color`도 존재하는지 확인
- **이유**: Chrome/Safari에서 `-webkit-text-fill-color`가 `color`를 덮어씀. gradient text (`-webkit-background-clip: text`)가 적용된 요소의 하위 DOM에 전파될 수 있음

### CSS-04: CSS 셀렉터 우선순위 충돌 방지
- **규칙**: 페이지에서 커스텀 CSS를 추가할 때, theme.py의 전역 셀렉터보다 **높은 명시도(specificity)**를 사용해야 함
- **검증**: 페이지 scoped CSS의 셀렉터 명시도 ≥ theme.py 대응 셀렉터 명시도
- **theme.py 기준 셀렉터**: `.main .stMarkdown span` (명시도: 0,3,0), `[data-testid="stAppViewBlockContainer"] span` (명시도: 0,1,1)
- **안전한 패턴**: `.custom-class span` (0,2,0) 이상 사용

---

### CHART-01: 히스토그램 막대 구분
- **규칙**: 막대에 흰색 테두리 + gap
- **검증**: `marker_line_width=1.5`, `bargap=0.08`

### CHART-02: render_plotly_animated는 overflow:hidden
- **규칙**: `render_plotly_animated`는 `overflow:hidden` + 고정 height iframe으로 렌더링한다. 차트 영역 밖(negative y 범례, 긴 x축 라벨 등)은 **잘린다**
- **대응**: 범례/라벨이 잘릴 위험이 있으면 `st.plotly_chart(fig, use_container_width=True)` 사용 (Streamlit 자동 리사이징)
- **`render_plotly_animated` 사용 조건**: 범례가 차트 영역 내부에 완전히 포함되고, x/y축 라벨이 margin 안에 수용될 때만
- **검증**: `render_plotly_animated` 호출 시 legend y값이 0 미만이면 FAIL

---

## 파일 위치
| 파일 | 역할 |
|------|------|
| `theme.py` | CSS 생성, 팔레트 정의, `_glass_css`, `render_styled_dataframe` |
| `components.py` | 내비바, 사이드바, 다크모드 토글 |
| `pages/network.py` | 네트워크 그래프 |
| `pages/companies.py` | 회사 목록 (카드뷰/리스트뷰) |
| `pages/investors.py` | 투자자 목록 + 포트폴리오 테이블 |
| `pages/scores.py` | 점수 분석 차트 |
