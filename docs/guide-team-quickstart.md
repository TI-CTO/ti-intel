# Tech Intelligence Platform — 팀 Quick Start

> 5분 안에 플랫폼을 사용할 수 있는 빠른 시작 가이드.
> 상세 도구 레퍼런스: `docs/guide-tool-reference.md`

---

## 1. 환경 설정

### 새 PC 환경 세팅 (clone부터 실행까지)

```bash
# 1. 레포 클론
git clone git@github.com:TI-CTO/ti-intel.git
cd ti-intel

# 2. uv 설치
curl -LsSf https://astral.sh/uv/install.sh | sh
# ruff (린터)
~/.local/bin/uv tool install ruff

# 3. 로컬 설정 파일 복사 후 경로 수정
cp .claude/settings.local.json.example .claude/settings.local.json
# → OBSIDIAN_VAULT_PATH, additionalDirectories 경로를 본인 환경에 맞게 수정

# 4. MCP 서버 설정 복사 후 API 키 입력
cp .mcp.json.example .mcp.json
# → .env 파일에 필요한 API 키 설정 (SUPABASE_URL, SUPABASE_ANON_KEY 등)

# 5. 각 프로젝트 의존성 설치
for proj in projects/*/; do
  (cd "$proj" && ~/.local/bin/uv sync)
done

# 6. Playwright Chromium 설치 (PDF 렌더링용)
cd projects/design-system && ~/.local/bin/uv run --extra browser playwright install chromium && cd ../..

# 7. Claude Code 실행
claude
```

### 필요 환경변수 (.env)

| 변수 | 용도 | 필수 |
|------|------|------|
| `SUPABASE_URL` | Supabase 프로젝트 URL | Y |
| `SUPABASE_ANON_KEY` | Supabase 익명 키 | Y |
| `SERPAPI_KEY` | 특허 수집 (SerpAPI) | N (특허 미사용 시) |
| `TAVILY_API_KEY` | 뉴스 수집 (Tavily) | N (GDELT/Naver 폴백) |
| `NAVER_CLIENT_ID` | 네이버 뉴스 검색 | N |
| `NAVER_CLIENT_SECRET` | 네이버 뉴스 검색 | N |

### 필수 조건
- macOS (터미널)
- Claude Code CLI (`~/.local/bin/claude`)
- 환경변수: `.env` 파일에 API 키 설정 완료

### 시작
```bash
cd /path/to/ti-intel
claude
```

---

## 2. 30초 치트시트

| 하고 싶은 일 | 명령어 |
|-------------|--------|
| "이 기술 도입해야 해?" | `/wtis standard {기술명}` |
| "이번 주 뭐 바뀌었어?" | `/weekly-monitor {도메인}` |
| "이 주제 조사해줘" | `/research-session {주제}` |
| "새 기술 기회 찾아줘" | `/discover {분야}` |
| "스타트업 찾아줘" | `/startup-scout {도메인}` |
| "이 회사 분석해줘" | `/startup-analyst {기업명}` |
| "리포트 PDF로" | `/report-pdf {파일경로}` |
| "발표자료 만들어줘" | `/slides {파일경로}` |

> 슬래시 명령어 대신 자연어로 말해도 됩니다: "PQC 기술 Go/No-Go 판정해줘"

---

## 3. 도메인 구조

3개 L1 도메인 × 10개 L2 기술영역 × 25개 L3 세부기술.
주간 모니터링은 매주 월요일 07:30에 3개 L1 도메인(Agentic AI → Voice AI → Secure AI)을 순차 실행한다.

> 전체 목록: `docs/tech-taxonomy-overview.md` (기술분류체계)

---

## 4. 역할별 워크플로우

### 전략기획 — "기술 도입 판정 + 포트폴리오 관리"

핵심 흐름: **기술 평가(Standard) → 판정 → 종합 기술 전략 제안서(Full) → CTO 보고**

```
① /wtis standard 동형암호 키워드 검색      ← 200점 정량 평가 + Go/No-Go 판정
② /wtis full he-keyword-search            ← 종합 기술 전략 제안서 (전략+기업+재무 통합)
③ 포트폴리오 확인                           ← outputs/reports/{domain}/{domain}-portfolio.md
④ /weekly-monitor secure-ai               ← 매주 기술 변화 추적 → 판정 재검토 트리거
```

> 상세: `docs/guide-strategy-analysis.md` (WTIS 2-Tier 가이드)

**자주 쓰는 질문 예시**:
- "Secure AI 포트폴리오 현황 보여줘" → portfolio.md 요약
- "PQC 기술 Go/No-Go 판정해줘" → `/wtis standard` 실행
- "이 기술 도입 전략 제안서 만들어줘" → `/wtis full` 실행 (전략+기업+재무 통합)
- "지난주 대비 변화된 기술 있어?" → `/weekly-monitor` 또는 `get_weekly_diff`
- "SKT KT 양자암호 최근 동향" → intel-store 경쟁사 토픽 검색 + 웹 서치

### 사업기획 — "시장 현황 파악 + 스타트업 발굴"

핵심 흐름: **시장 조사 → 뉴스 수집 → 스타트업 탐색 → 기업 분석**

```
① search_intel로 시장 현황 검색             ← "search_intel(query='AI AICC', mode='hybrid')"
② collect_news로 최신 뉴스 수집             ← "AICC 관련 최신 뉴스 수집해줘"
③ /startup-scout voice AI 한국             ← 해당 분야 스타트업 후보 발굴
④ /startup-analyst Hume AI                ← 관심 기업 심층 분석 + DB 저장
```

**자주 쓰는 질문 예시**:
- "에이전트 AI 시장 최신 뉴스 알려줘" → `search_intel` + `collect_news`
- "이 분야 한국 스타트업 후보 찾아줘" → `/startup-scout`
- "Hume AI 펀딩 현황과 기술력 분석해줘" → `/startup-analyst`
- "투자자별 포트폴리오 보여줘" → `get_investor_portfolio`

### 개발 — "기술 리서치 + 논문/특허 탐색"

핵심 흐름: **논문 수집 → 유사 탐색 → 심층 리서치 → 기술 보고서**

```
① collect_papers로 논문 수집               ← "PQC lattice 관련 최신 논문 수집해줘"
② find_similar로 관련 논문 확장             ← "이 논문과 비슷한 거 더 찾아줘"
③ /research-session CKKS 부트스트래핑       ← 특정 주제 심층 리서치
④ collect_arxiv로 프리프린트 추가 수집       ← "arXiv에서 CKKS 관련 최신 논문"
```

**자주 쓰는 질문 예시**:
- "동형암호 CKKS 최신 논문 수집해줘" → `collect_papers` + `collect_arxiv`
- "이 논문과 관련된 다른 연구 찾아줘" → `find_similar`
- "Edge AI 보안 기술 동향 조사해줘" → `/research-session`
- "PQC VoLTE 관련 특허 있어?" → `collect_patents`

---

## 5. 시나리오 예시

### "이번 주 기술 동향 알려줘"

```
/weekly-monitor secure-ai
```
→ 5개 L3 빠른 스캔 → 변화 감지된 L3 심층 분석 → 주간 리포트 + PDF

### "이 기술 도입할까?"

```
/wtis standard 동형암호 키워드 검색
```
→ 심층 리서치 → 200점 정량 평가 → Go/Conditional/No-Go 판정 → PDF + 포트폴리오

### "경쟁사가 뭐 하고 있어?"

```
"SKT KT 양자암호 최근 동향 알려줘"
```
→ intel-store에서 `skt-strategy`, `kt-strategy` 토픽 검색 + 웹 서치

### "특정 기업 심층 분석"

```
/startup-analyst Hume AI
```
→ 기업 조사 → 분석 리포트 + DB 입력용 정규화 데이터

---

## 6. 산출물 위치

```
outputs/reports/
  agentic-ai/                     ← Agentic AI WTIS 분석
    agentic-ai-portfolio.md       ← 포트폴리오 (L2별 점수 요약)
    2026-03-09_multi-agent/       ← WTIS 세션
  voice-ai/                       ← Voice AI WTIS 분석
    voice-ai-portfolio.md
  secure-ai/                      ← Secure AI WTIS 분석
    secure-ai-portfolio.md
  weekly/                         ← 주간 모니터링
    2026-03-18_weekly-secure-ai.md
    2026-03-18_weekly-secure-ai.pdf
    2026-03-18_research-*.md       ← Deep 리서치 (L3별)
```

---

## 7. 포트폴리오

L1 도메인별 L2 평가 결과 종합 현황판. WTIS 평가 완료 시 자동 갱신된다.

| 판정 | 점수 | 의미 |
|------|------|------|
| **Go** | 160+ | 즉시 추진 |
| **Conditional Go** | 120~159 | 조건 충족 시 추진 |
| **재검토** | 80~119 | 근본적 재설계 필요 |
| **No-Go** | ~79 | 추진 부적합 |

> 최신 현황: `outputs/reports/{domain}/{domain}-portfolio.md`

---

## 8. 주간 운영

매주 월요일 07:30에 Agentic AI → Voice AI → Secure AI → 경쟁사 브로드스캔을 순차 자동 실행.
금요일 07:30에 주간 종합 + 데이터 건강 체크. 화~목은 WTIS 검증, 리서치, 스타트업 분석 등 자유 일정.

> 상세 타임라인: `docs/guide-platform-overview.md` (주간 운영 사이클)

---

## 9. 자주 묻는 질문

**Q: 데이터가 없는 새 주제를 검색하면?**
A: 먼저 수집이 필요합니다. "PQC 논문 수집해줘" → `collect_all` 실행 → 이후 검색 가능.

**Q: MCP 도구를 직접 호출해야 하나?**
A: 아닙니다. 자연어로 말하면 Claude가 적절한 도구를 자동 선택합니다. "PQC 관련 뉴스 찾아줘"라고 하면 됩니다.

**Q: VSCode에서 사용 가능한가?**
A: MCP 도구 호출은 터미널 Claude Code에서만 가능합니다. VSCode Claude 확장에서는 일반 대화만 가능합니다.

**Q: SerpAPI 쿼터가 걱정되는데?**
A: 특허 수집(`collect_patents`)만 SerpAPI를 사용합니다. 뉴스/논문 수집은 무료 API이므로 자유롭게 사용하세요.

**Q: 리포트를 Obsidian에서 보고 싶어요**
A: `/obsidian-bridge {파일경로} {유형}`으로 동기화합니다. 유형: `wtis`, `weekly`, `research`, `reference`.

---

## 10. 장애 대응

### 빠른 진단표

| 증상 | 원인 | 대응 |
|------|------|------|
| "MCP 도구 호출 실패" | MCP 서버 미시작 | 터미널 재시작 또는 `claude` 재실행 |
| "collect 결과 0건" | API 키 만료 또는 쿼터 초과 | `.env` 키 확인, `get_intel_stats`로 현황 체크 |
| "PDF 생성 실패" | Playwright 미설치 | `uv run --extra browser playwright install chromium` |
| "Obsidian 파일 안 보여" | 동기화 미실행 | `/obsidian-bridge`로 수동 동기화 |
| "WTIS 타임아웃" | opus 에이전트 과부하 | 재실행 (2차 시도에서 성공하는 패턴) |
| "search_intel 0건" | 해당 토픽 데이터 미수집 | `collect_all(topic="...", query="...")` 먼저 실행 |
| "에이전트 무응답/hang" | 병렬 에이전트 5개+ 리소스 경합 | 최대 3~4개 동시 실행, 5개+면 2배치 분할 |

### API 쿼터 관리

| API | 월 한도 | 확인 방법 | 초과 시 영향 |
|-----|---------|----------|-------------|
| **SerpAPI** | 250회/월 | [serpapi.com](https://serpapi.com) 대시보드 | 특허 수집(`collect_patents`) 중단. 뉴스/논문은 무영향 |
| **Tavily** | 1,000회/월 | [tavily.com](https://tavily.com) 대시보드 | 뉴스 수집이 GDELT + Naver로 자동 폴백 |
| **Anthropic** | 사용량 기반 | [console.anthropic.com](https://console.anthropic.com) | 전체 Claude Code 중단. 즉시 관리자에게 보고 |

**쿼터 절약 팁**:
- `collect_news`만 필요하면 `collect_all` 대신 단독 호출 (SerpAPI 소모 방지)
- `collect_patents`는 분기 1~2회 일괄 수집으로 충분
- `search_intel(mode="keyword")`는 API 비용 없음 (DB 내부 검색)

### 수집 에러 대응

**논문 수집 실패** (`collect_papers` / `collect_arxiv`):
1. Semantic Scholar API 일시 장애 → arXiv로 자동 폴백 (별도 조치 불필요)
2. arXiv도 실패 → 수 분 후 재시도. arXiv는 3초 간격 rate limit 있음
3. 결과 0건이지만 에러 아닌 경우 → 검색어를 영어/일반 키워드로 변경

**뉴스 수집 실패** (`collect_news`):
1. `source="all"` 중 일부만 실패 → 성공한 소스 결과는 정상 저장됨
2. Naver API 키 만료 → `.env`의 `NAVER_CLIENT_ID`, `NAVER_CLIENT_SECRET` 갱신
3. 한국어 뉴스만 필요 → `source="naver"` 단독 호출

**특허 수집 실패** (`collect_patents`):
1. SerpAPI 쿼터 확인 (월 250회)
2. 쿼터 잔여 시 → 검색어 단순화 (한국어 → 영어)

### MCP 서버 점검

MCP 서버가 정상인지 확인하려면:
```
"intel-store 상태 확인해줘"    → get_intel_stats() 호출
"startup-db 상태 확인해줘"     → get_company_stats() 호출
"trend-tracker 토픽 목록"      → manage_watch_topics(action="list") 호출
```

전체 MCP 서버 목록 (6개):
| 서버 | 상태 확인 도구 |
|------|---------------|
| intel-store | `get_intel_stats()` |
| startup-db | `get_company_stats()` |
| trend-tracker | `manage_watch_topics(action="list")` |
| design-system | `list_themes()` |
| youtube-transcript | `get_transcript(url="...")` |
| context7 | 외부 문서 조회 시 자동 사용 |

---

## 11. 참고 문서

| 문서 | 위치 | 내용 |
|------|------|------|
| 도구 레퍼런스 (상세) | `docs/guide-tool-reference.md` | 전체 도구 목록, 파라미터, 사용 예시 |
| 스킬 체이닝 맵 | `docs/guide-skill-chaining.md` | 스킬 간 연결 관계 + 시나리오 |
| 기술 분류체계 | `.claude/skills/wtis/references/tech-taxonomy.md` | L1/L2/L3 전체 정의 + 검색 키워드 |
| 3주 시범운영 통계 | `outputs/reports/2026-03-18_3week-pilot-summary.md` | KPI 달성, 데이터 현황 |
