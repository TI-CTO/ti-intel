# Command Reference

> 스킬과 MCP 도구의 파라미터 전체 레퍼런스.
> 플랫폼 개요는 [platform-guide.md](platform-guide.md) 참조.

---

## 공유 파라미터

### 토픽 슬러그

모든 MCP 서버 도구와 `/monitor` 스킬에서 `topic` 파라미터로 사용.

| 슬러그 | 의미 |
|--------|------|
| `ai-network` | AI 기반 네트워크 최적화, 자율 네트워크 |
| `6g` | 6세대 이동통신 표준 및 연구 |
| `network-slicing` | 5G/6G 네트워크 슬라이싱 기술 |
| `edge-computing` | MEC, 엣지 클라우드, 분산 컴퓨팅 |
| `quantum-comm` | 양자 통신, 양자 암호 |
| `llm-telecom` | 통신 도메인 LLM 적용 |
| `open-ran` | Open RAN 아키텍처 및 생태계 |
| `digital-twin` | 네트워크 디지털 트윈 |

### 신뢰도 태그

리서치 결과물에서 출처 신뢰도를 표시할 때 사용.

| 태그 | 설명 | 예시 |
|------|------|------|
| `[A]` | 공식 1차 출처 | 기업 IR 발표, 정부 정책 문서, 표준 기구 문서 |
| `[B]` | 공신력 있는 2차 출처 | 학술 논문, 주요 언론 (FT, NYT, 조선일보) |
| `[C]` | 지시적 자료 | 업계 블로그, 분석사 보고서, 기업 홈페이지 |
| `[D]` | 미검증 | 소셜미디어, 익명 출처, 커뮤니티 포스트 |

### 통신사 코드

telco-factbook 도구에서 `carrier` 파라미터로 사용.

| 코드 | 설명 |
|------|------|
| `SKT` | SK텔레콤 (2024~2025 데이터 보유) |
| `KT` | KT (수동 임포트 필요) |

---

## 스킬 커맨드 레퍼런스

### /wtis

LG U+ 기술전략 인텔리전스. 제안서 분석·트렌드 조사·과제 검증·기회 발굴을 수행한다.

**문법**
```
/wtis [mode] [query 또는 파일 경로]
```

**파라미터**

| 파라미터 | 타입 | 필수 | 기본값 | 설명 |
|----------|------|------|--------|------|
| `mode` | `proposal\|quick\|standard\|deep` | 선택 | 자동 판정 | 분석 모드 |
| `query` | string | 필수* | — | 질문 텍스트, 제안서 텍스트, 또는 파일 경로 |

**모드별 설명**

| 모드 | 실행 컴포넌트 | 소요 시간 | 적합한 상황 |
|------|-------------|-----------|------------|
| `proposal` | SKILL-0 → research-deep → SKILL-1 → validator | ~20분 | 과제 제안서 전체 검증 |
| `quick` | research-deep 단독 | ~5분 | 빠른 동향/현황 파악 |
| `standard` | research-deep + SKILL-1 또는 SKILL-2 + validator | ~15분 | 진행 중 과제 타당성 검증 |
| `deep` | discover + research-deep + SKILL-1 + validator | ~30분 | 신규 기술 기회 발굴 |

**자동 모드 판정 규칙**

| 입력에 포함된 단어 | 판정 모드 |
|--------------------|-----------|
| `제안서`, `proposal`, 파일 경로 (`.md`, `.txt`) | `proposal` |
| `동향`, `트렌드`, `뉴스`, `현황`, `비교` | `quick` |
| `검증`, `타당성`, `Go/No-Go`, `적합한지` | `standard` |
| `발굴`, `탐색`, `전략`, `기회` | `deep` |

**예시**
```
# 제안서 파일 전체 분석 파이프라인
/wtis proposal outputs/reports/my-proposal.md

# 제안서 텍스트 직접 입력
/wtis proposal "AI 기반 네트워크 자동화 과제 — 목표: OPEX 30% 절감..."

# 빠른 트렌드 조사
/wtis quick 2026년 국내 통신사 AI 에이전트 서비스 현황

# 모드 생략 (자동 판정)
/wtis 6G 테라헤르츠 통신 최신 동향

# 과제 타당성 검증
/wtis standard 현재 진행 중인 Open RAN 도입 과제 타당성 검토

# 전략적 기회 발굴
/wtis deep B2B AI 솔루션 시장 기회 탐색
```

**출력 파일 경로**
```
outputs/reports/{YYYY-MM-DD}_wtis-proposal-{slug}-final.md
```

---

### /discover

도메인 내 신기술 기회를 발굴하고 2×2 우선순위 매트릭스(전략가치 × 실행가능성)로 정리한다.

**문법**
```
/discover [domain]
```

**파라미터**

| 파라미터 | 타입 | 필수 | 설명 |
|----------|------|------|------|
| `domain` | string | 필수 | 탐색할 기술 도메인 (자유 텍스트) |

> 추가적인 context(포트폴리오, 경쟁사, 분류체계)는 대화 메시지로 함께 제공 가능.

**예시**
```
# 기본 발굴
/discover B2B AI 솔루션

# 구체적인 도메인
/discover 6G 엣지 컴퓨팅

# 기존 포트폴리오 언급과 함께 (중복 제외 요청)
/discover 양자 통신 기술
현재 보유 과제: AI 네트워크 최적화, 5G 슬라이싱
경쟁사 제외: SKT Cloud-Z, KT DX
```

**출력 파일 경로**
```
outputs/reports/{YYYY-MM-DD}_discover-{domain-slug}.md
```

**반환 형식**
```
status: pass | fail | uncertain
summary: 발견된 기회 수, 최우선 기회명 (200자 이내)
file_path: 결과 파일 절대 경로
```

---

### /monitor

등록된 watch_topics를 스캔하고 이전 스냅샷과 비교하여 변화를 감지한다.

**문법**
```
/monitor [topic-slug]
```

**파라미터**

| 파라미터 | 타입 | 필수 | 기본값 | 설명 |
|----------|------|------|--------|------|
| `topic-slug` | string | 선택 | (전체) | 특정 토픽만 스캔. 생략 시 watch_topics 전체 |

**신호 분류**

| 기호 | 레벨 | 의미 | 처리 |
|------|------|------|------|
| 🟢 | 정상 | 변화 없음 | 로그만 기록 |
| 🟡 | 주의 | 주목할 변화 발생 | 요약 보고서 생성 |
| 🔴 | 긴급 | 전략적 영향 가능성 | 상세 보고서 + 에스컬레이션 안내 |

**예시**
```
# 전체 토픽 스캔
/monitor

# 특정 토픽만
/monitor ai-network

# 여러 토픽 (각각 별도 호출)
/monitor 6g
/monitor open-ran
```

**출력 파일 경로** (🟡/🔴 토픽만 저장)
```
outputs/reports/{YYYY-MM-DD}_monitor-{topic-slug}.md
```

---

### /research-session

주제를 구조화된 방식으로 조사하고 Evidence Chain 기반 리서치 노트를 작성한다.

**문법**
```
/research-session [topic]
```

**파라미터**

| 파라미터 | 타입 | 필수 | 설명 |
|----------|------|------|------|
| `topic` | string | 필수 | 리서치 주제 (자유 텍스트, 한국어/영어 모두 가능) |

**MCP 데이터 소스 자동 활용 조건**

주제가 기술 트렌드/논문/특허 관련이면 MCP 소스를 병렬 호출:
- `research-hub.search_papers(topic, query)` — 학술 논문
- `patent-intel.search_patents(topic, query)` — 특허
- `trend-tracker.search_news(topic, query)` — 뉴스

topic 파라미터에는 공유 토픽 슬러그 중 가장 관련성 높은 것을 사용.

**예시**
```
# 기술 트렌드 조사 (MCP 자동 활용)
/research-session 6G 테라헤르츠 통신 최신 연구 동향

# 비교 분석
/research-session Pydantic v2 vs dataclasses 성능 비교

# 시장 분석
/research-session 국내 Private 5G 시장 현황 및 주요 플레이어

# 특정 기업/제품 조사
/research-session SKT T cloud 서비스 포트폴리오 분석
```

**출력 파일 경로**
```
outputs/reports/{YYYY-MM-DD}_{topic-slug}.md
```

---

### /slides

마크다운 파일을 디자인 테마가 적용된 PPTX로 변환한다.

**문법**
```
/slides [theme] <file-path>
```

**파라미터**

| 파라미터 | 타입 | 필수 | 기본값 | 설명 |
|----------|------|------|--------|------|
| `theme` | `professional\|minimal\|dark` | 선택 | `professional` | 디자인 테마 |
| `file-path` | string | 필수 | — | 마크다운 파일 경로 (절대 또는 workspace 상대) |

**테마 설명**

| 테마 | 스타일 | 적합한 상황 |
|------|--------|------------|
| `professional` | 마젠타 포인트, 기업 스타일 | 경영진 보고, 공식 발표 |
| `minimal` | 흑백 + 블루 포인트 | 기술 발표, 심플 보고 |
| `dark` | 다크 배경 + 밝은 텍스트 | 컨퍼런스, 데모 |

**마크다운 슬라이드 매핑 규칙**

| 마크다운 요소 | 슬라이드 타입 |
|-------------|-------------|
| `# H1` | 표지 |
| `## H2` | 섹션 구분 |
| `> 인용문` | 핵심 메시지 강조 |
| `\| 표 \|` | 데이터 표 |
| `- 리스트` | 불릿 포인트 |
| 일반 텍스트 | 본문 |

**예시**
```
# 기본 (professional 테마)
/slides outputs/reports/2026-02-25_wtis-proposal-final.md

# 테마 지정
/slides minimal outputs/reports/2026-02-25_analysis.md

# 다크 테마
/slides dark outputs/reports/2026-02-25_demo.md
```

**출력 파일**
```
# 입력 파일과 동일한 경로에 테마명 추가
{original-path}.professional.pptx
{original-path}.minimal.pptx
{original-path}.dark.pptx
```

---

### /obsidian-bridge

워크스페이스 산출물을 Obsidian 볼트로 동기화한다.

**문법**
```
/obsidian-bridge <file-path> <type>
```

**파라미터**

| 파라미터 | 타입 | 필수 | 설명 |
|----------|------|------|------|
| `file-path` | string | 필수 | 소스 파일 경로 |
| `type` | `research\|implementation\|project` | 필수 | 노트 타입 |

**타입별 대상 폴더**

| type | Obsidian 저장 경로 |
|------|-------------------|
| `research` | `70-Research/Sessions/` |
| `implementation` | `60-ClaudeCode/Implementations/` |
| `project` | `10-Projects/` |

**예시**
```
# 리서치 세션 동기화
/obsidian-bridge outputs/reports/2026-02-25_6g-analysis.md research

# 구현 기록 동기화
/obsidian-bridge docs/platform-guide.md implementation

# 프로젝트 문서 동기화
/obsidian-bridge projects/research-hub/CLAUDE.md project
```

---

### /work-log

현재 세션의 작업 내용을 Obsidian 업무일지에 기록한다.

**문법**
```
/work-log [update]
```

**파라미터**

| 파라미터 | 타입 | 필수 | 설명 |
|----------|------|------|------|
| (없음) | — | — | 오늘 일지 신규 생성 또는 새 작업만 추가 |
| `update` | flag | 선택 | 기존 일지에 이후 진행 내용만 명시적 추가 |

**예시**
```
# 오늘 작업 일지 생성/업데이트
/work-log

# 오후 작업 내용만 추가
/work-log update
```

**저장 경로**
```
Obsidian/60-ClaudeCode/WorkLogs/{YYYY-MM-DD}_daily-log.md
```

---

### /new-project

`projects/` 아래에 새 MCP 서버 프로젝트를 표준 구조로 스캐폴딩한다.

**문법**
```
/new-project <project-name>
```

**파라미터**

| 파라미터 | 타입 | 필수 | 설명 |
|----------|------|------|------|
| `project-name` | string | 필수 | 프로젝트 이름 (lowercase-kebab-case) |

**명명 규칙**
- 정식 프로젝트: `lowercase-kebab-case` (예: `startup-intel`)
- 임시/실험: `{YYYY-MM-DD}-{name}` (예: `2026-02-startup-test`)

**예시**
```
# 스타트업 정보 MCP 서버
/new-project startup-intel

# 주식 데이터 MCP 서버
/new-project stock-data

# 실험적 프로젝트
/new-project 2026-02-rag-experiment
```

**생성 구조**
```
projects/{name}/
├── CLAUDE.md
├── pyproject.toml
├── .env.example
├── src/{name_underscore}/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── mcp_server.py
│   └── db/
│       ├── client.py
│       └── repository.py
└── tests/
    ├── test_models.py
    └── test_repository.py
```

생성 후 `.mcp.json`에 수동 등록 필요.

---

## MCP 도구 레퍼런스

> MCP 도구는 Claude가 대화 중 자동 호출하거나, 사용자가 직접 지시할 수 있다.
> 예: "SKT 2025년 Q3 실적 알려줘" → Claude가 `get_financial_metrics` 자동 호출

---

### telco-factbook

SKT/KT 재무 지표 및 가입자 데이터 조회. **현재 SKT 데이터만 보유** (2024~2025 전분기).

#### get_financial_metrics

```python
get_financial_metrics(carrier?, year, quarter?)
```

| 파라미터 | 타입 | 필수 | 설명 |
|----------|------|------|------|
| `carrier` | `SKT\|KT` | 선택 | 생략 시 전체 |
| `year` | int | 필수 | 조회 연도 |
| `quarter` | int (1~4) | 선택 | 생략 시 연간 전체 |

**예시 요청**
```
"SKT 2025년 Q3 재무 지표 알려줘"
→ get_financial_metrics(carrier="SKT", year=2025, quarter=3)

"2024년 SKT/KT 연간 실적 비교"
→ get_financial_metrics(year=2024)
```

**반환 예시**
```json
{
  "metrics": [{
    "year": 2025, "quarter": 3,
    "carrier": "SKT",
    "revenue": 5312.4,
    "operating_income": 1087.2,
    "net_income": 891.5,
    "ebitda": 1621.3,
    "capex": 478.9,
    "mobile_subscribers": 21820000
  }],
  "count": 1
}
```

**주요 지표 단위**: 매출/이익 → 십억원(KRW bn), 가입자 → 명

#### compare_carriers

```python
compare_carriers(metric, year, quarter?)
```

| 파라미터 | 타입 | 필수 | 설명 |
|----------|------|------|------|
| `metric` | string | 필수 | `revenue`, `operating_income`, `net_income`, `ebitda`, `capex`, `mobile_subscribers` |
| `year` | int | 필수 | 비교 연도 |
| `quarter` | int (1~4) | 선택 | 생략 시 연간 합계 |

**예시 요청**
```
"SKT vs KT 2025년 매출 비교"
→ compare_carriers(metric="revenue", year=2025)
```

#### get_revenue_trend

```python
get_revenue_trend(carrier, year_from, year_to)
```

**예시 요청**
```
"SKT 2022~2025 매출 추이"
→ get_revenue_trend(carrier="SKT", year_from=2022, year_to=2025)
```

#### get_subscriber_data

```python
get_subscriber_data(carrier, year, quarter?)
```

**예시 요청**
```
"SKT 2025년 가입자 현황"
→ get_subscriber_data(carrier="SKT", year=2025)
```

---

### research-hub

Semantic Scholar API로 학술 논문을 검색·저장하고 조회한다.

#### search_papers

```python
search_papers(topic, query, since_year?, limit?)
```

| 파라미터 | 타입 | 필수 | 기본값 | 설명 |
|----------|------|------|--------|------|
| `topic` | string | 필수 | — | 토픽 슬러그 |
| `query` | string | 필수 | — | 검색 키워드 |
| `since_year` | int | 선택 | — | 발행 연도 하한 |
| `limit` | int (1~50) | 선택 | 10 | 최대 논문 수 |

**예시 요청**
```
"6G 테라헤르츠 통신 최신 논문 찾아줘"
→ search_papers(topic="6g", query="terahertz communication", since_year=2023, limit=10)

"AI 네트워크 최적화 논문 20편"
→ search_papers(topic="ai-network", query="network optimization reinforcement learning", limit=20)
```

**반환 예시**
```json
{
  "topic": "6g",
  "stored_count": 8,
  "papers": [{
    "external_id": "ss:abc123",
    "title": "Terahertz Channel Modeling for 6G Networks",
    "authors": ["Kim, J.", "Lee, S."],
    "published_date": "2024-03-15",
    "citation_count": 47,
    "abstract": "We present a comprehensive...",
    "raw_url": "https://api.semanticscholar.org/..."
  }]
}
```

#### get_trending_papers

```python
get_trending_papers(topic, since?, limit?)
```

| 파라미터 | 타입 | 필수 | 기본값 | 설명 |
|----------|------|------|--------|------|
| `topic` | string | 필수 | — | 토픽 슬러그 |
| `since` | YYYY-MM-DD | 선택 | — | 발행일 하한 |
| `limit` | int | 선택 | 20 | 반환 개수 |

**예시 요청**
```
"ai-network 토픽에서 올해 인용 많은 논문"
→ get_trending_papers(topic="ai-network", since="2025-01-01", limit=10)
```

#### get_paper_stats

```python
get_paper_stats(topic, year?, month?)
```

**예시 요청**
```
"6g 토픽 2025년 2월 논문 통계"
→ get_paper_stats(topic="6g", year=2025, month=2)
```

---

### patent-intel

USPTO PatentsView API로 미국 특허를 검색·저장하고 조회한다 (1976년~).

#### search_patents

```python
search_patents(topic, query, since_year?, limit?)
```

| 파라미터 | 타입 | 필수 | 기본값 | 설명 |
|----------|------|------|--------|------|
| `topic` | string | 필수 | — | 토픽 슬러그 |
| `query` | string | 필수 | — | 검색 키워드 (특허 제목/초록) |
| `since_year` | int | 선택 | — | 출원 연도 하한 |
| `limit` | int (1~50) | 선택 | 10 | 최대 특허 수 |

**예시 요청**
```
"네트워크 슬라이싱 관련 삼성 특허"
→ search_patents(topic="network-slicing", query="network slicing Samsung", since_year=2022, limit=15)

"양자 암호 통신 특허 동향"
→ search_patents(topic="quantum-comm", query="quantum key distribution telecom", limit=20)
```

**반환 예시**
```json
{
  "topic": "network-slicing",
  "stored_count": 12,
  "patents": [{
    "external_id": "uspto:US11234567B2",
    "title": "Method for network slice management in 5G",
    "applicant": "Samsung Electronics Co., Ltd.",
    "filing_date": "2023-06-15",
    "ipc_codes": ["H04W 28/02", "H04L 41/0806"],
    "abstract": "A method for dynamically allocating...",
    "raw_url": "https://patents.google.com/patent/US11234567B2"
  }]
}
```

#### get_recent_patents

```python
get_recent_patents(topic, since?, limit?)
```

**예시 요청**
```
"2025년 이후 open-ran 특허"
→ get_recent_patents(topic="open-ran", since="2025-01-01", limit=20)
```

#### get_patent_stats

```python
get_patent_stats(topic, year?, quarter?)
```

**예시 요청**
```
"edge-computing 2024년 Q4 특허 통계"
→ get_patent_stats(topic="edge-computing", year=2024, quarter=4)
```

---

### trend-tracker

뉴스·트렌드 데이터를 저장하고 시계열 비교를 제공한다.

> **참고**: 자동 수집 파이프라인 미구현. `upsert_news`로 수동 저장하거나, `/research-session`이 조사 결과를 저장할 때 활용된다.

#### search_news

```python
search_news(topic?, keyword?, since?, limit?)
```

| 파라미터 | 타입 | 필수 | 기본값 | 설명 |
|----------|------|------|--------|------|
| `topic` | string | 선택 | — | 토픽 슬러그 필터 |
| `keyword` | string | 선택 | — | 제목 검색어 |
| `since` | YYYY-MM-DD | 선택 | — | 발행일 하한 |
| `limit` | int | 선택 | 20 | 최대 결과 수 |

**예시 요청**
```
"ai-network 관련 저장된 뉴스"
→ search_news(topic="ai-network", limit=30)

"2025년 이후 6G 관련 뉴스"
→ search_news(topic="6g", since="2025-01-01")
```

#### upsert_news

```python
upsert_news(items)
```

**items 스키마**
```json
[{
  "title": "Samsung unveils 6G prototype",
  "source": "Samsung Newsroom",
  "url": "https://news.samsung.com/...",
  "topic": "6g",
  "published_date": "2025-02-20",
  "summary": "Samsung demonstrated 6G terahertz...",
  "reliability_tag": "A",
  "keywords": ["6G", "Samsung", "terahertz"]
}]
```

#### manage_watch_topics

```python
manage_watch_topics(action, topic?, keywords?, frequency?, is_active?)
```

| 파라미터 | 타입 | 필수 | 설명 |
|----------|------|------|------|
| `action` | `list\|add\|update\|remove` | 필수 | 동작 |
| `topic` | string | add/update/remove 시 필수 | 토픽 슬러그 |
| `keywords` | array[string] | 선택 | 모니터링 키워드 |
| `frequency` | `daily\|weekly\|monthly` | 선택 | 모니터링 주기 |
| `is_active` | bool | 선택 | 활성 여부 |

**예시 요청**
```
"등록된 watch_topics 목록"
→ manage_watch_topics(action="list")

"llm-telecom 토픽 주간 모니터링으로 추가"
→ manage_watch_topics(
    action="add",
    topic="llm-telecom",
    keywords=["LLM", "telecom", "GPT", "통신 AI"],
    frequency="weekly"
  )
```

---

## 자주 묻는 질문

**Q: 토픽 슬러그에 없는 기술을 조사하면?**
`/research-session`이나 `/wtis quick`은 슬러그 없이도 WebSearch로 동작한다.
MCP DB에 저장하려면 먼저 토픽을 추가해야 한다 → Supabase `topics` 테이블에 INSERT.

**Q: MCP 도구를 직접 호출하는 방법은?**
대화에서 자연어로 요청하면 Claude가 적절한 도구를 자동 호출한다.
예: "SKT 2025년 매출 알려줘" → `get_financial_metrics` 자동 호출.

**Q: 리서치 결과를 Obsidian에 저장하려면?**
스킬이 자동으로 `outputs/reports/`에 저장한다. Obsidian으로 옮기려면:
```
/obsidian-bridge outputs/reports/{파일명}.md research
```
