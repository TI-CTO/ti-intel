---
name: startup-analyst
description: "스타트업 심층 분석. 특정 기업을 조사하여 팩트 기반 분석 리포트와 DB 입력용 정규화 데이터를 산출한다."
user-invokable: true
argument-hint: "[company name]"
---

# Startup Analyst — 스타트업 심층 분석 스킬

특정 기업을 심층 조사하여 팩트 기반 분석 리포트를 생성하고,
리포트 생성 후 startup-db MCP에 정규화 데이터를 저장한다.
VC/투자 관점의 분석과 DB 입력을 동시에 수행하는 하이브리드 역할.

## 빠른 시작

```
/startup-analyst SIM2REAL
```

**실행 중:**
```
기존 DB 확인 → SIM2REAL (slug: sim2real) 이미 등록됨, 기준선 확인
멀티소스 수집 → TheVC, 혁신의숲, WebSearch, intel-store ... (18개 소스)
팩트 검증 → 투자 금액 교차 확인, 직원 수 검증
5차원 스코어링 → 기술(7), 시장(6), 팀(5), 적합도(8), 견인력(6)
```

**완료 시:**
```
분석 완료 (confidence: high, sources: 18)
저장: outputs/reports/startups/2026-03-13_startup-sim2real.md

📋 Next Steps:
  → startup-db에 자동 저장
  → /wtis standard {핵심 기술} Go/No-Go 검증
```

---

## Arguments
- `company`: 조사할 기업명 (예: "SIM2REAL", "XL8 Inc.")

## I/O Contract

### Input
| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| `company` | yes | 자유 텍스트 | 조사 대상 기업명 |

### Output Files
| Artifact | Path Pattern | Description |
|----------|-------------|-------------|
| 분석 리포트 | `outputs/reports/startups/YYYY-MM-DD_startup-{slug}.md` | 심층 분석 + DB JSON |

### Return
```yaml
status: pass
summary: "{기업명} — {confidence}, {N}개 소스, overall {score}/100"
file_path: "리포트 절대 경로"
confidence: high | medium | low
sources_count: N
company_slug: "{slug}"
```

## Process

### Step 1: 기존 데이터 확인
startup-db에 이미 등록된 기업인지 확인:
- `search_companies(query="{기업명}")` 또는 `get_company(slug="{slug}")`
- 이미 있으면 기존 데이터를 기준선으로 사용, 변경사항 중심으로 조사

### Step 2: 멀티소스 수집 (최소 15개 소스)

**한국 비상장 스타트업 필수 소스:**
- **TheVC (thevc.kr)**: 투자 라운드, 누적 투자액, 투자사 명단
- **혁신의숲 (innoforest.co.kr)**: MAU, 소비자 결제 추이, 고용/퇴사율
- **잡플래닛 (jobplanet.co.kr)**: 기업 평점, 경영진 평가, 조직 문화
- **원티드 (wanted.co.kr)**: 채용 직무, 기술 스택, 사업 확장 방향

**글로벌 소스:**
- Crunchbase, PitchBook 공개 프로필
- TechCrunch, VentureBeat 등 기술 미디어
- 기업 공식 웹사이트, 블로그, 보도자료

**intel-store 연동 (MCP 사용 가능 시):**
- `search_intel(query="{기업명}")` — 관련 뉴스/논문/특허 검색
- `collect_news(query="{기업명}")` — 최신 뉴스 수집

**특허/논문:**
- Google Patents, KIPRIS — 보유 특허 확인
- Google Scholar — 핵심 인력 논문 확인

### Step 3: 팩트 검증

**출처 분류:**
```
[A] Official   — 기업 공시, IR 자료, 정부 통계, peer-reviewed 논문
[B] Reputable  — 주요 언론(TechCrunch, 한경 등), TheVC, 혁신의숲
[C] Indicative — 블로그, 미검증 보도자료, 개인 리뷰
[D] Unverified — 단일 소스, 루머, 비공식 채널
```

**교차 검증 규칙:**
- 투자 금액/라운드: TheVC + 기사 2건 이상 교차 확인
- 직원 수/MAU: 혁신의숲 + 채용 공고 수로 간접 검증
- 기술 스택: 채용 공고(원티드) + GitHub/기술 블로그
- 단일 소스 정보: [D] 태그 명시, 확정 사실로 기술 금지

### Step 4: 분석 리포트 + 스코어링 작성

5차원 스코어를 산출한다:
- tech_strength (1-10): 기술 경쟁력 (특허, 논문, 핵심기술 차별성)
- market_potential (1-10): 시장성 (TAM, 성장률, 타이밍)
- team_quality (1-10): 팀 역량 (경험, 도메인 전문성)
- business_fit (1-10): 사업 적합도 (우리 회사와의 시너지)
- traction (1-10): 견인력 (매출, 고객 수, 성장률)
- overall_score (0-100): 가중합

### Step 5: 저장

저장 경로: `/Users/ctoti/Project/ClaudeCode/outputs/reports/startups/{YYYY-MM-DD}_startup-{slug}.md`

## Output Format

```markdown
---
company: {기업명}
date: {YYYY-MM-DD}
skill: startup-analyst
confidence: high | medium | low
sources_count: {N}
---

# {기업명} 심층 분석

## 0. 한 줄 요약
> {기업의 핵심 가치와 미션을 1문장으로}

## 1. 기업 개요

**기본 정보:**
| 항목 | 내용 | 출처 |
|------|------|------|
| 설립일 | {YYYY-MM-DD} | {[A-01]} |
| 소재지 | {국가, 도시} | {[A-01]} |
| 대표자 | {이름} | {[B-01]} |
| 직원 수 | {N명 (시점)} | {[B-02]} |
| 상태 | {active/acquired/ipo/defunct} | {[B-01]} |
| 웹사이트 | {URL} | |

**핵심 인력:**
| 이름 | 직함 | 주요 경력 | 출처 |
|------|------|----------|------|
| {name} | {CEO/CTO/...} | {경력 요약} | {[B-xx]} |

**인력 동향:**
- 최근 1년 고용/퇴사 트렌드 (혁신의숲 참조)
- 현재 채용 중인 핵심 직무 (원티드 참조)

## 2. 기술력 및 IP

**핵심 기술:**
- 기술적 작동 원리 및 기존 방식 대비 차별성

**IP 현황:**
| 구분 | 내용 | 출처 |
|------|------|------|
| 특허 수 | {N건} | {[A-xx]} |
| 핵심 특허 | {제목/요약} | {[A-xx]} |

**기술 스택** (채용 공고 기반):
- {언어/프레임워크/인프라}

## 3. 제품/서비스 및 비즈니스 모델

**주요 서비스:**
- 서비스명, 핵심 기능, 해결하는 Pain Point

**수익 모델:**
- {B2B 구독 / 수수료 / 라이선스 / ...}

**성장 지표 (Traction):**
| 지표 | 수치 | 기간 | 출처 |
|------|------|------|------|
| MAU | {N} | {시점} | {[B-xx]} |
| 매출/GMV | {N} | {시점} | {[B-xx]} |

## 4. 투자 이력

| 라운드 | 금액 | 통화 | 리드 투자사 | 일자 | 출처 |
|--------|------|------|-----------|------|------|
| {Seed/Series A/...} | {N} | {KRW/USD} | {투자사명} | {YYYY-MM-DD} | {[B-xx]} |

**누적 투자금:** {총액} ({출처})
**주요 투자사:** {리스트}

## 5. 시장 및 경쟁 우위

**경쟁사 분석:**
| 기업 | 핵심 강점 | 핵심 약점 | 출처 |
|------|----------|----------|------|
| {경쟁사1} | {강점} | {약점} | {[B-xx]} |

**차별화 포인트 (Moat):**
- 기술적 해자 / 네트워크 효과 / 선점 효과 / 데이터 자산

## 6. 파트너십 및 최근 동향

**전략적 제휴 (최근 3년):**
- {파트너사 — 제휴 내용 — 시점}

**최근 1년 주요 이슈:**
- {투자 유치, 수상, 제품 출시, 해외 진출 등}

## 7. 종합 평가

**5차원 스코어:**
| 차원 | 점수 (1-10) | 근거 |
|------|------------|------|
| 기술 경쟁력 (tech_strength) | {N} | {1줄 근거} |
| 시장성 (market_potential) | {N} | {1줄 근거} |
| 팀 역량 (team_quality) | {N} | {1줄 근거} |
| 사업 적합도 (business_fit) | {N} | {1줄 근거} |
| 견인력 (traction) | {N} | {1줄 근거} |
| **종합 (overall)** | **{0-100}** | |

**투자 매력도:**
- VC 관점에서의 성장 잠재력 및 Exit 가능성

**리스크 요인:**
- 시장 규제, 경쟁 심화, 번레이트, 핵심 인력 이탈 등

## References
| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| A-01 | {출처명} | [링크]({url}) | {유형} | {날짜} | [A] |
```

## Critical Rules
- NEVER fabricate sources, URLs, statistics, or funding amounts — 허위 출처는 전체 분석을 무효화한다
- NEVER present single-source claims as confirmed facts — 반드시 [D] 태그 명시
- NEVER skip the References table — 출처 없는 주장은 삭제한다
- NEVER guess financial data — 투자 금액, 밸류에이션, 매출은 확인된 수치만 기재. 불확실하면 "공개 정보 없음"
- 리포트 생성 완료 후 startup-db MCP 도구로 자동 저장 (upsert_company + add_funding_round)
- "성장세가 가파르다" 같은 정성적 표현 금지 — "최근 6개월간 MAU 150% 증가 [B-03]" 같이 수치 + 출처로 기술
- 한국 비상장 스타트업은 TheVC + 혁신의숲 필수 조회 — 스킵하면 데이터 품질 보증 불가

## Success Metrics
- References 최소 15건 (한국 비상장은 국내 소스 5건+)
- 단일 소스([D]) 비율 20% 미만
- 투자 금액: 2건+ 교차 검증 완료
- DB 저장 시 startup-db 스키마와 100% 호환
- 5차원 스코어 전 항목에 1줄 이상 근거 명시
- 정보 부재 항목은 "공개 정보 없음" 명시 (빈 칸 방치 금지)

## Next Steps

저장 완료 후 아래 후속 옵션을 사용자에게 제시한다:

```
📋 Next Steps:
  💾 DB 저장 (자동):
    → 리포트 데이터로 upsert_company + add_funding_round 실행
  🔬 핵심 기술 검증:
    → /wtis standard {핵심 기술}               — Go/No-Go 200점 채점
  📄 PDF 변환:
    → /report-pdf {리포트 경로}                — 컨설팅 스타일 PDF
  📂 Obsidian 동기화:
    → /obsidian-bridge {리포트 경로} research   — 볼트에 동기화
  📝 작업 기록:
    → /work-log
```

## Notes
- MCP 서버가 응답하지 않으면 WebSearch로 대체하고 한계를 보고서에 명시
- 글로벌 기업은 한국 특화 소스(TheVC, 혁신의숲 등) 스킵 가능
- startup-scout에서 넘어온 초기 정보가 있으면 Step 2에서 재활용 (중복 검색 방지)
