# Research: Professional Startup Database UI Patterns

## 연구 질문

> 전문 스타트업/회사 데이터베이스 플랫폼들의 UI 구조, 기능, 정보 조직 방식을 조사하여, startup-db 대시보드 설계에 적용 가능한 구체적인 패턴과 베스트 프랙티스를 파악하고 싶다.

## 연구 범위

- **Crunchbase** (crunchbase.com): Company profiles, search/filter, funding data display
- **PitchBook**: Company data display, comparisons, dashboards
- **CB Insights**: Analytics dashboards, market maps, Mosaic Score
- **Tracxn**: Company profiles, analytics, deal flow tracking
- **Dealroom.co**: Startup profiles, ecosystem views, geographic benchmarking

---

## 1. 프로필 페이지 정보 구조

### 일관된 헤더-섹션-탭 패턴

모든 주요 플랫폼이 채택한 구조:

- **상단 헤더**: 회사명, 로고, 주요 지표 (Crunchbase Growth/Heat Score, CB Insights Mosaic Score) 우상단 표시
- **좌측 사이드바 네비게이션**: 깊은 계층 구조를 수직으로 정렬 (Material Design)
  - 예: Crunchbase, PitchBook, Tracxn 모두 동일 패턴
- **주요 섹션**: About, Highlights, News & Activity, Tech Details
- **태블 기반 상세 보기**: 개별 섹션 확장 가능

### 회사 프로필 콘텐츠 계층화

| **계층** | **표시 위치** | **데이터 예시** |
|---------|-------------|-----------------|
| **Tier 1: 한눈에** | 카드 상단 / 헤더 | 기업명, 로고, 상태(Active/Acquired), 지역 |
| **Tier 2: 빠른 평가** | About + Highlights | 설명, 자금, 직원수, 펀딩 라운드, 획득/IPO |
| **Tier 3: 심층 분석** | 탭 확장 | 기술 스택, 팀, 경쟁사, 유사 회사, 뉴스 |
| **Tier 4: 데이터 상세** | 테이블/차트 | 자금 내역, 밸류에이션, 투자자, 거래 흐름 |

**설계 철학**: Crunchbase 새 프로필 설계(2025~2026)는 "가장 가치 있는 정보를 먼저" 표시하는 방식으로 의사결정 속도 향상 추구. PitchBook은 AI 기반 요약(deal history + financials + leadership + recent activity)으로 시작.

---

## 2. 검색 및 필터링 UX 패턴

### Faceted Search 구현

업계 표준 패턴:

- **1차 선택**: 9개 검색 타입 (Companies, People, Investors, Funding Rounds, Acquisitions, Events 등)
- **2차 필터**: 필터 패널 우상단, 확장 가능 영역 내 카테고리
  - 위치, 직원 수, 산업, 최근 펀딩 날짜, 평가 점수, 펀딩 단계
  - **멀티셀렉트 체크박스**: 사용자가 여러 옵션 선택 시 나머지 필터 옵션 계속 표시 (UX 핵심)
  - **동적 아이템 카운트**: 각 필터 옵션 옆에 해당하는 결과 수 표시
- **3차 정렬/표시**: Edit Columns 링크로 테이블 구성 커스터마이징

### 특수 기능

| **기능** | **플랫폼** | **설명** |
|---------|----------|--------|
| **AI 검색 빌더** | Crunchbase Pro | 자연어 입력 → 자동으로 관련 필터 추출 |
| **Query Builder** | Crunchbase | 100개+ 필터 조합 가능 (고급 사용자용) |
| **저장된 검색 & 알림** | Crunchbase, Tracxn | 검색 조건 저장 → 신규 거래 시 이메일 알림 |
| **의미론적 검색** | Dealroom | 정확한 단어 일치 대신 의미 기반 해석 |
| **Mosaic 필터** | CB Insights | 점수 범위(0~1000) 또는 백분위수로 필터링 |

**UX 원칙** (Algolia 문서 기반):
- Facet 옵션이 검색 결과에 따라 동적 변경되면 사용자 이해도 증가
- 지나친 facet 수는 피하고 "Show More" 옵션으로 계층화
- 선택된 필터를 태그로 표시하여 시각적 피드백 제공

---

## 3. 데이터 시각화 전략

### 시각화 유형별 사용처

| **시각화 유형** | **플랫폼** | **용도** | **예시 축** |
|----------------|---------|--------|----------|
| **선 그래프 (시계열)** | Tracxn, PitchBook | 자금, 밸류에이션, 직원 성장 | X: 시간, Y: 금액/인원 |
| **막대/원형 차트** | PitchBook | 자본 분해, 지역별 회사 수 | 범주별 구성 비율 |
| **시장 맵 (마이크로-매크로)** | CB Insights, PitchBook, Dealroom | 산업 경쟁 구도 | X: 혁신/시장점유율, Y: 시장크기/성장률 |
| **히트맵/버블 차트** | CB Insights, Dealroom | 에코시스템 비교 | 크기: 투자 규모, 색: 성장률 |
| **비교 테이블** | PitchBook, Crunchbase | 유사 회사 비교 | 밸류에이션, 자금, 산업, 직원 |
| **지리 맵** | Dealroom | 도시/국가별 에코시스템 | 지역별 통계 패널 좌측 표시 |

### Market Map 설계 원칙

**CB Insights Market Map Maker**:
- 템플릿 클론 → 분류/카테고리 커스터마이징 가능
- 필터링 옵션: Mosaic 점수, 총 펀딩, 최신 펀딩, 알파벳 순
- 2축 조정으로 회사 위치 재배열

**Dealroom Ecosystem Benchmarking (2025)**:
- 288개 도시, 69개 국가 벤치마킹 대시보드
- 메트릭: VC 투자, 유니콘 수, 자본 밀도, 스케일업 전환율, AI 인재, 특허 활동
- 좌측 패널: 집계 통계 (분기별 펀딩, 출처 국가별)

---

## 4. 리스트 & 컬렉션 관리

### Crunchbase Lists (정적 모델)

- **특징**: 사용자가 수동으로 추가/삭제 (자동 동기화 없음)
- **생성 방법 3가지**:
  1. 검색 결과에서 행 선택 → "Save to List" 버튼
  2. 모든 결과 선택 → 기존/신규 리스트 지정 또는 Zapier 동기화
  3. 리스트 열기 → Quick Add로 개별 추가
- **알림 기능**: 리스트 내 회사에 대한 뉴스/신호 실시간 추적

### CB Insights Collections (고급 모델)

- **Tagging System**:
  - 행 일괄선택 → Action Bar에서 태그 추가/제거
  - 팀 태그 전파: 게스트가 컬렉션 클론 시 태그도 함께 복사
- **마켓 랜드스케이프 빌드**: 태그로 회사 계층화 → 차트/시장맵 자동 생성
- **데이터 관리**: 스프레드시트 뷰에서 행 편집 가능

---

## 5. 경쟁사/유사사 기능

### Crunchbase Similar Companies

- **기계학습 기반**: 자동 감지
- **UI**: 프로필 탭 추가 → "Similar Companies" 클릭 시 경쟁사 리스트

### PitchBook Comparables

- **자동 생성**: 속성 필터 (산업, 위치, 밸류에이션, 자본금, 매출 등) 적용 → 자동 생성
- **Comparisons 기능**: side-by-side 비교 → Excel/PNG로 다운로드 가능
- **Market Maps Tool**: 사용자 정의 세그먼트 추가/제거 가능
- **Charts**: 막대, 원형, 누적 막대, 히스토그램 등 선택 가능

---

## 6. 점수/지표 시스템

### 주요 지표

| **지표** | **플랫폼** | **구성 요소** | **사용처** |
|---------|---------|----------|----------|
| **Growth Score** | Crunchbase | 자금, 직원, 시장점유율, 재무, 고객 성장 | 프로필 상단 |
| **Heat Score** | Crunchbase | 실시간 관심도 (뉴스, 언급) | 프로필 상단 |
| **Mosaic Score (0~1000)** | CB Insights | 4개 요소 (아래 참조) | Collections, Search, Market Index, 프로필 |
| **Tracxn Analyst Rating** | Tracxn | 성능/자금/밸류에이션 등급 | 필터링, 프로필 표시 |

### Mosaic Score 구성 (CB Insights)

```
Mosaic Score (0~1000) = 
  ├─ Momentum (20%): 회사의 현재 추진력 - 자금 증가, 직원 성장, 언론 언급
  ├─ Market (25%): 산업 건강성 - 섹터 펀딩 트렌드, 경쟁 강도
  ├─ Money (25%): 재무 건강도 - 자본금, 유지율, 수익성 신호
  └─ Management (30%): 리더십 품질 - 팀 경험, 이전 회사 EXIT 이력
```

**검증**: 150k+ 회사 대상 연구 → 유니콘 예측 정확도 4.7배 (상위 VC 대비)

---

## 7. 네비게이션 구조

### 계층화 구조

```
┌─ Primary Navigation (수평 탭)
│  ├─ Companies
│  ├─ Investors
│  ├─ Deals
│  └─ News
│
└─ Secondary Navigation (수직, 좌측 사이드바)
   ├─ Search
   ├─ My Collections
   │  ├─ Saved Lists
   │  ├─ Recent Searches
   ├─ Alerts
   ├─ Drafts
   └─ Settings
```

### Material Design 원칙 적용

- **상단**: 가로 탭 (주요 섹션 전환)
- **좌측**: 세로 네비게이션 (카테고리, 필터, 저장된 항목)
- **우측/중앙**: 콘텐츠 (프로필, 테이블, 차트)
- **반응형**: 데스크톱 (3단 레이아웃) → 모바일 (햄버거 메뉴)

**Best Practice** (Material Design, navbar.gallery 출처):
- Supabase 사이드바: 많은 네비게이션 링크를 구분된 서브카테고리로 정렬
- 간결하고 설명적인 라벨 사용
- 유사한 콘텐츠/기능을 논리적으로 그룹화

---

## 8. 대시보드 및 보고 기능

### PitchBook Dashboards 모델

- **상단 리본**: 다중 대시보드 (Companies, Investors, Deals 등)
- **결과 탭**: Overview, Companies, Deals, Investors, Limited Partners, People, Pivot Table, Charts
- **데이터 새로고침**: 시간마다 갱신 (브라우저 새로고침으로 최신 데이터 로드)
- **커스터마이징**: Edit Columns로 출력 테이블 구성 변경

### CB Insights Analytics 기능

- **Strategy Maps**: 대규모 기업 활동 → 패턴화된 인사이트
- **Relationship Graphs**: 투자자-회사 네트워크
- **Predictive Signals**: ChatGPT + CB 데이터 연계
- **Market Index**: 산업별 자금 유입, 상위 투자자, 최근 EXIT

---

## 9. 헤더 액션 버튼 & 통합

### Crunchbase 새 설계 (2025~2026)

- **Save 버튼** (Follow 대체):
  - 커스텀 리스트나 "My Follows"에 저장
  - 알림 수신 활성화
- **Salesforce 통합** (예정):
  - 프로필 저장 → CRM 자동 동기화
  - 영업 팀 워크플로우 통합
- **Outreach 컨텍스트**:
  - 최근 뉴스/신호 표시로 "개인화된 접근" 지원

---

## 10. 성능 및 확장성 고려사항

### 데이터 제한 및 새로고침

- **Crunchbase Pro**: 검색 결과 최대 1,000개 표시
- **PitchBook**: 시간 단위 데이터 새로고침
- **성능**: 대규모 테이블 (500+행)에서 가상 스크롤 고려

### 실시간 신호 처리

- **뉴스 & Activity**: 자동 트래킹 (저장된 프로필)
- **구조화된 신호**: 펀딩, 인수, 팀 변화, 헤드라인

---

## 참고: 설계 결정 기준

| **결정** | **근거** | **플랫폼** |
|--------|--------|---------|
| 좌측 사이드바 네비게이션 | 깊은 계층 구조 수용, 모바일 반응형 | Crunchbase, PitchBook, Tracxn |
| Faceted Search 필터 | 동적 facet, 멀티셀렉트 UX 검증됨 | Algolia, Crunchbase, Tracxn |
| 시장맵 2축 시각화 | 산업 구도 이해, 비교 분석 용이 | CB Insights, PitchBook, Dealroom |
| 지역 벤치마킹 기능 | 에코시스템 비교 니즈 | Dealroom Global Index |
| 점수 지표 (Mosaic 유형) | 회사 평가 신속화 | CB Insights (검증됨) |
| 리스트 + 태그 조합 | 팀 협업 및 마켓 랜드스케이프 빌드 | CB Insights Collections |

---

## 출처

### 공식 문서
- [Crunchbase Profile Navigation](https://support.crunchbase.com/hc/en-us/articles/360052260893-Navigating-a-company-profile-on-Crunchbase)
- [Crunchbase Advanced Search](https://support.crunchbase.com/hc/en-us/articles/115010629528-Use-filters-to-build-a-search-with-Crunchbase-Pro)
- [Crunchbase New Profile Design](https://about.crunchbase.com/blog/new-crunchbase-profile-design)
- [PitchBook Platform Navigation](https://pitchbook.com/help/platform-log-in-dashboards)
- [PitchBook Comparable Companies](https://pitchbook.com/blog/how-to-find-comparable-private-and-public-companies-with-pitchbook)
- [CB Insights Market Map Maker](https://www.cbinsights.com/what-we-offer/platform/market-map-maker/)
- [CB Insights Mosaic Score](https://www.cbinsights.com/mosaic-score/)
- [Dealroom Ecosystems](https://dealroom.co/ecosystems-network/)
- [Dealroom Map Design](https://dealroom.co/blog/map-design-upgrade)

### UX 패턴
- [Algolia Faceted Search](https://www.algolia.com/blog/ux/faceted-search-and-navigation)
- [Data Table UX Patterns](https://www.pencilandpaper.io/articles/ux-pattern-analysis-enterprise-data-tables)
- [Filter UX Best Practices](https://www.pencilandpaper.io/articles/ux-pattern-analysis-enterprise-filtering)
- [Sidebar Navigation Design](https://www.navbar.gallery/blog/best-side-bar-navigation-menu-design-examples)
- [Material Design Navigation](https://m1.material.io/patterns/navigation.html)

---

*최종 업데이트: 2026-03-17*
