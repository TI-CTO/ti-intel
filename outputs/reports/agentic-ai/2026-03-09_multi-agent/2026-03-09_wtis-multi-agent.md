---
topic: Multi-Agent
domain: agentic-ai
l2_topic: multi-agent
date: 2026-03-09
wtis_version: v4.1
wtis_mode: standard
skills_executed: [research-deep, SKILL-1, validator]
status: completed
total_references: 35
---

# WTIS Final Report: Multi-Agent (L2 #2)

---

## 경영진 요약

**판정: Conditional Go**
**종합점수: 155/200점 (77.5%) — 7개 항목 조건부 승인**

Multi-Agent 오케스트레이션 기술은 2026년 초 TRL 7~8 단계로 진입하여 프로덕션 그레이드 성숙도에 도달했다 [[G-06]](#ref-g-06), [[P-01]](#ref-p-01). 글로벌 시장은 연 40~44% CAGR로 성장 중(2026년 약 91~109억 달러 규모)이며 [[G-19]](#ref-g-19), 국내 SKT/KT가 모두 엔터프라이즈 멀티에이전트 플랫폼을 전략 핵심으로 선언했다 [[E-01]](#ref-e-01), [[E-02]](#ref-e-02). **핵심 리스크: 80% 엔터프라이즈가 멀티에이전트 확장을 계획하나 실제 성공률은 10% 미만**으로, 도입·운영 복잡도가 구조적 진입 장벽으로 작용한다 [[G-21]](#ref-g-21). 이 수치는 단일 출처(특허 법률 블로그) 기반으로 원출처 미확인 상태이므로, 추진 전 별도 검증을 권고한다. 3단계 전략(Phase 1: Buy — LangGraph/MCP, Phase 2: Borrow — MS Agent Framework/NTT Docomo, Phase 3: Build — 조직 특화 오케스트레이션 토폴로지)을 권고하며, Context Rot 기술 로드맵 수립·오케스트레이션 설계 역량 확보·프로토콜 표준화 완료가 선행 조건이다.

**승인 권고 조건:**
1. Context Rot(장기 태스크 신뢰성 과제)에 대한 기술 로드맵 수립 필수 [[G-15]](#ref-g-15), [[P-05]](#ref-p-05)
2. 오케스트레이션 토폴로지 설계 역량(차별화의 핵심)에 대한 내부 인력 확보 또는 파트너십 계획 제시 [[P-02]](#ref-p-02)
3. 프로토콜 스택(MCP + A2A) 표준화 완료 및 진입 마일스톤 정의 [[G-10]](#ref-g-10), [[P-01]](#ref-p-01)

---

## 평가 항목 및 배점 안내

본 보고서는 WTIS 평가 체계(200점 만점, 5개 항목 각 40점)에 따라 정량 평가한다.
상세 기준: `scoring-framework.md` 참조.

**채점 원칙:**
- 각 세부 지표 10점 만점
- 데이터 부족 항목: 중앙값(5점) 부여 + "데이터 부족" 표시
- 모든 수치 및 판단에 출처 기호([G-xx], [E-xx], [P-xx] 등) 필수

---

## 1. 목표 검증

### SMART Test

| 기준 | 평가 | 근거 |
|------|------|------|
| **Specific** | ✓ 명확함 | KPI 명확: "멀티에이전트 기반 서비스 플랫폼 구축, 내부 운영 자동화 에이전트 배포" |
| **Measurable** | ✓ 추적 가능 | 정량지표: 에이전트 수, SLA 준수율(장애 대응 시간), 자동화율 증가. NTT Docomo 사례: 장애 대응 시간 50% 이상 단축 [[G-17]](#ref-g-17) |
| **Achievable** | ✓ 현실적임 | TRL 7~8 기술 기반. AT&T 410개+ 에이전트 프로덕션 운영 [[G-24]](#ref-g-24), 국내 SKT 2,000개+ 내부 에이전트 운영 사례 [[E-01]](#ref-e-01) 통해 달성 가능성 입증 |
| **Relevant** | ✓ 조직 전략 일치 | 통신사 핵심 전략 영역. SKT "AI Native" 선언, KT "Agentic Fabric" 플랫폼 공식 발표로 산업 메인스트림 확정 [[E-01]](#ref-e-01), [[E-02]](#ref-e-02) |
| **Time-bound** | △ 부분 명확 | 타임라인 미정의, 단 경쟁사 기준선: MS Agent Framework GA Q1 2026 목표 [[G-01]](#ref-g-01), LangGraph v1.0 GA 2025-10 완료 [[G-06]](#ref-g-06) → 18~24개월 PoC 목표 현실적 |

### 시장 규모 (Market Sizing)

| 항목 | 규모 | 출처 | 신뢰도 |
|------|------|------|--------|
| **TAM (2026)** | $91.4B ~ $108.6B (중앙값: $100.0B ≈ 약 130조 원) | Fortune Business Insights, Mordor Intelligence, Precedence Research [[G-19]](#ref-g-19) | [A] 다수 기관 교차확인 |
| **CAGR (2026~2034/2031)** | 40.50% ~ 43.84% (중앙값: 42.17%) | [[G-19]](#ref-g-19) | [B] 복수 출처 일관성 |
| **SAM (국내 통신사 멀티에이전트)** | 약 1.5~2조 원 [추정] | SKT 2,000개+ 에이전트 운영, 1GW 데이터센터 투자 규모 [[E-01]](#ref-e-01) 기반 추정 | [C] 단일 사례 기반 |
| **SOM (첫 3년 진입 시장)** | 약 200~400억 원 [추정] | SKT/KT 플랫폼 초기 도입, 100만 개 네트워크 장비 대상 NTT Docomo 사례 [[G-17]](#ref-g-17) 기반 추정 | [C] 제한된 벤치마크 |

**시장 타이밍:**
- **진입 시점**: 적절 (진입 초기 단계 — 프레임워크 GA 완료, 초기 도입 고객 확보 중인 구간) [[G-01]](#ref-g-01), [[G-02]](#ref-g-02), [[G-06]](#ref-g-06)
- **경쟁 강도**: 높음 (Microsoft, Google, Anthropic, LangChain 등 거대 기술 기업 5개+가 경쟁 중) [[G-01]](#ref-g-01), [[G-02]](#ref-g-02), [[G-04]](#ref-g-04)

---

## 2. 기술 성숙도 맵

### 4사분면 배치 및 분석

```
         High TRL (7~9)
              │
   [유지]     │     [베팅] ← Multi-Agent 위치
   (기존      │     LangGraph v1.0 (TRL 8)
   프레임)    │     CrewAI (TRL 7~8)
              │     MS Agent Framework (TRL 7)
──────────────┼──────────────
              │
   [탐색]     │     [Watch]
   (Context   │     (계층적
   Rot 해법)  │      계획,
              │      트랜잭션)
         Low TRL (1~6)

   Low Disruption ←──→ High Disruption
```

### 각 기술 평가

#### 1) Multi-Agent Orchestration (오케스트레이션 레이어)

| 항목 | 평가 | 근거 |
|------|------|------|
| **TRL** | **8** (시스템 완성·검증) | LangGraph v1.0 GA 완료(2025-10), 프로덕션 적용: Uber, LinkedIn, Klarna [[G-06]](#ref-g-06). NTT Docomo 상용 배포(2026-02-04) 100만 장비 규모 [[G-17]](#ref-g-17). AT&T 410개 에이전트 프로덕션 운영 [[G-24]](#ref-g-24) |
| **Disruption** | **High** (기술 구조 재편) | LLM 성능 수렴 시대에 오케스트레이션 토폴로지가 모델 선택보다 중요 [[P-02]](#ref-p-02). Agentic Mesh(계층적 전문화 팀) 새로운 아키텍처 패러다임 도입 [[G-09]](#ref-g-09) |
| **사분면** | **[베팅]** (수익화 개시 구간) | 기술 성숙 완료, 초기 고객 수익화 진행 중 → 차별화 전략이 승패 결정 |

#### 2) Agent Planning (계획 수립 능력)

| 항목 | 평가 | 근거 |
|------|------|------|
| **TRL** | **6~7** (파일럿 검증 중 → 프로토타입 단계) | 계층적 계획(HiPlan) 논문 제시 [[P-04]](#ref-p-04), Saga 트랜잭션 보장(SagaLLM) VLDB 2026 게재 [[P-05]](#ref-p-05), ReAcTree 트리 탐색 ICLR 2026 게재 [[P-06]](#ref-p-06). 검증 우선(Validation-First) 패러다임 정착 중 [[P-07]](#ref-p-07) |
| **Disruption** | **Medium-High** (신뢰성 개선) | 장기 태스크(수일~수주) 신뢰성 향상에 초점. Context Rot 문제 구조적 해결 중 [[P-05]](#ref-p-05), [[P-06]](#ref-p-06) |
| **사분면** | **[Watch]** (기술 검증 중) | 학술 논문 다수 발표 → 산업 구현 진행 → 2026년 중반 프로덕션 도입 예상 |

#### 3) Context Rot 해결 기술

| 항목 | 평가 | 근거 |
|------|------|------|
| **TRL** | **4~5** (개념 검증 중) | 학술 문헌에서만 논의 중, 상용 제품 해법 부재 [[G-15]](#ref-g-15), [[P-05]](#ref-p-05) |
| **Disruption** | **High** (장기 태스크 신뢰성) | 컨텍스트 60% 초과 시 성능 저하 — 장기 실행 에이전트의 구조적 도전 과제 [[G-15]](#ref-g-15) |
| **사분면** | **[탐색]** (개발 초기 단계) | 기술 미성숙 → 투자 필요 → 2027년 이후 실용화 예상 |

---

## 3. 경쟁사 현황 및 Gap Analysis

### 글로벌 경쟁사 비교표

| 경쟁사 | 제품/전략 | TRL | 포지션 | 차별점 | 출처 |
|-------|---------|-----|--------|--------|------|
| **Microsoft** | Agent Framework RC (GA Q1 2026 예정) | 7 | 리더 | A2A·MCP·AG-UI 3개 프로토콜 동시 지원. 엔터프라이즈 인증 경로 | [[G-01]](#ref-g-01), [[G-14]](#ref-g-14) |
| **Anthropic** | MCP + Claude Opus 4.6 (Agent Teams) | 8 | 리더 | MCP 표준 주도. 타 프레임워크 전면 채택으로 에코시스템 지위. 14.5시간 태스크 완료 | [[G-12]](#ref-g-12), [[P-01]](#ref-p-01) |
| **Google** | Agentspace + A2A v0.3 | 7 | 리더 | 50개+ 파트너 지지. PwC 대규모 생태계 파트너십 | [[G-10]](#ref-g-10), [[G-20]](#ref-g-20) |
| **LangChain** | LangGraph v1.0 GA | 8 | 리더 | 월 617만 PyPI 다운로드. 프로덕션 적용 다수. 내구성 실행·스트리밍 완성 | [[G-02]](#ref-g-02), [[G-06]](#ref-g-06) |
| **CrewAI** | 엔터프라이즈 대시보드(AMP) + MCP | 7~8 | 도전자 | 월 4.5억 워크플로우[C]. 빠른 Time-to-Production(40% 우위)[C]. 역할 기반 협업 | [[G-04]](#ref-g-04), [[G-05]](#ref-g-05) |
| **OpenAI** | Agents SDK | 6~7 | 추종자 | GPT-4o 최적화, Handoff·guardrail 내장. 상태 지속성 미흡 | [[G-02]](#ref-g-02), [[G-13]](#ref-g-13) |

### 국내 통신사 경쟁사 비교표

| 경쟁사 | 전략 | 역량 | 출현일 | 출처 |
|-------|------|------|---------|------|
| **SKT** | "AI Native" 전략. "One Person, One AI Agent" 이니셔티브 | 2,000개+ 내부 에이전트 운영. A.phone(AI 에이전트 스마트폰). 1조+ 파라미터 모델 개발 | 2026-03-01 (MWC) | [[E-01]](#ref-e-01) |
| **KT** | "Agentic Fabric" OS(5계층: 경험·지능·컨텍스트·실행·거버넌스) | Agent Builder(노코드), Agentic AICC(콜센터 자동화). 통신·금융·자산·HR 내부 적용 완료 | 2026-02 (MWC) | [[E-02]](#ref-e-02) |
| **NTT Docomo** | 네트워크 유지보수 Agentic AI 시스템 | 100만+ 네트워크 장비 실시간 분석. 장애 대응 50% 이상 단축 | 2026-02-04 (상용화) | [[G-17]](#ref-g-17) |
| **AT&T** | Ask AT&T 플랫폼 | 10만+ 사용자, 750억 API 호출, 410개+ 에이전트 | 현황 보고 | [[G-24]](#ref-g-24) |
| **Verizon** | Google Cloud Gemini 기반 AI 에이전트 | 고객 서비스 에이전트. 통화 시간 단축, 96% 정확도 | 현황 보고 | [[G-25]](#ref-g-25) |

### Gap Analysis: 조직의 경쟁 위치

**기술 성숙도:**
- 글로벌 리더(Microsoft, Anthropic, LangChain) = TRL 8, 프로덕션 그레이드
- **조직 (가정): TRL 탐색 단계 (4~5)** → 2년 이상 후행 [조직 내부 데이터 미확인, 가정 기반 추정]

**차별화 기회:**
- **SKT/KT의 선점:** 이미 플랫폼 공식 발표 및 내부 적용 진행 중 → 빠른 추격 필수 [[E-01]](#ref-e-01), [[E-02]](#ref-e-02)
- **NTT Docomo 레퍼런스:** 네트워크 운영(통신사 핵심 도메인) 에이전트 상용화 완료 → 직접 추격 가능 분야 [[G-17]](#ref-g-17)
- **오케스트레이션 토폴로지 설계:** LLM 성능 수렴 시대에 핵심 차별화 → 내부 역량 확보 시 우위 가능 [[P-02]](#ref-p-02)

**위협:**
- 80% 엔터프라이즈가 멀티에이전트 확장 계획하나 **성공률 10% 미만** [[G-21]](#ref-g-21)(G-21에서 재인용, 원출처 미확인) → 도입·운영 복잡도가 구조적 진입 장벽
- Gartner 예측: 2027년까지 현재 에이전트 프로젝트의 **40% 이상 취소 가능성** (비용·복잡도·리스크 이유) [[G-21]](#ref-g-21)(G-21에서 재인용, 원출처 미확인)

---

## 4. 3B 전략 분석

### 의사결정 매트릭스

```
1. 차별화 중요도 (1-10): 8/10
   근거: 오케스트레이션 토폴로지 설계가 핵심 차별화 [P-02]
   단, 표준 프로토콜(MCP+A2A) 채택 시 차별화 여지 제한적

2. 내부 역량 보유 (Yes/No): No / Partial
   근거: 데이터 부족 — 조직의 AI/멀티에이전트 개발 인력 현황 미확인
   추정: LLM 응용 경험은 있으나, 시스템 오케스트레이션 특화 인력 부족 가능성 높음

3. 시장 윈도우 (개월): 12~18개월 짧음
   근거: SKT/KT 이미 플랫폼 공식 발표 [E-01, E-02]
   경쟁사 기준선: MS GA Q1 2026, LangGraph v1.0 GA 2025-10 [G-01, G-06]

4. 시장 긴급도 (1-10): 8/10
   근거: 국내 통신사 2개(SKT/KT) 동시에 전략 선언 [E-01, E-02]
   글로벌 시장 CAGR 42% 고성장 [G-19]

5. 기술 격차 (년): 1~2년 후행
   근거: 글로벌 리더 TRL 8 vs 조직 TRL 4~5 추정 [조직 내부 데이터 미확인, 가정 기반]
```

### 3B 의사결정

**조건문 적용:**

```
IF (differentation_importance: 8) AND (internal_capability: NO)
    AND (market_window: 12-18mo):
    → BUY + BORROW (인수/라이선스 + 파트너십)

ELIF (market_urgency: 8) OR (tech_gap > 1.5 years):
    → BUY (라이선스/파트너)

RECOMMENDATION: HYBRID (Buy + Borrow)
```

### 상세 전략

#### Buy 영역 (우선 순위)

| 항목 | 선택지 | 근거 | Timeline |
|------|--------|------|----------|
| **오케스트레이션 프레임워크** | LangGraph v1.0 라이선스 | TRL 8, GA 완료, PyPI 617만 다운로드, Uber/LinkedIn 프로덕션 [[G-06]](#ref-g-06) | 즉시 |
| **MCP 표준 구현** | Anthropic MCP 스팩 채택 | 타 프레임워크 전면 채택 중, 사실상 표준 [[G-04]](#ref-g-04), [[G-05]](#ref-g-05), [[P-01]](#ref-p-01) | 즉시 |

#### Borrow 영역 (파트너십)

| 항목 | 파트너 선택지 | 근거 | Timeline |
|------|---------|------|----------|
| **MS 엔터프라이즈 지원** | Microsoft + 로컬 SI | Agent Framework GA(Q1 2026 예정), Copilot Studio 통합, Azure 인프라 [[G-01]](#ref-g-01), [[G-14]](#ref-g-14) | 2026 Q2~Q3 |
| **오케스트레이션 설계 컨설팅** | 학술·컨설팅 기관 | AdaptOrch 논문 저자, 오케스트레이션 토폴로지 설계 전문 [[P-02]](#ref-p-02) | 2026-09 |
| **NTT Docomo 네트워크 에이전트 사례 학습** | 기술 도입 검증 | 네트워크 운영 도메인 직접 적용 사례, 50% 단축 성과 [[G-17]](#ref-g-17) | 2026-06 |

#### Build 제외 사유

- 오케스트레이션 프레임워크 자체 개발 = 비효율적 (표준 프로토콜 채택 시 경쟁 불가)
- 단, **오케스트레이션 토폴로지 설계 알고리즘은 Build 가능** — 내부 도메인 특화(통신사 네트워크, 고객접점) 후 착수 [[P-02]](#ref-p-02)

---

## 5. 교차검증 결과

> Validator 실행 기준: 2026-03-09 / 대상 파일: skill1.md

### 5-1. 이슈 목록 및 처리 결과

| # | 이슈 유형 | 내용 | 처리 방식 | 상태 |
|---|---------|------|----------|------|
| V-01 | 고아 인용 | [G-12]가 본문 경쟁사 비교표(Anthropic 행)에 사용되었으나 References 미정의 | References에 G-12 추가: TechCrunch — Anthropic releases Opus 4.6 with agent teams (2026-02-05) | **해소** |
| V-02 | 출처-주장 불일치 | [G-21](Mintz 특허 법률 블로그)이 Gartner 예측(40% 프로젝트 취소)과 기업 성공률(10% 미만)의 출처로 사용됨 — 원출처 확인 불가 | 해당 인용에 "(G-21에서 재인용, 원출처 미확인)" 경고 표기 추가 | **잔존** (경고 표기) |
| V-03 | 수치 연산 오류 | TAM 중앙값: (91.4+108.6)/2 = 100.0B → 본문 99.6B로 잘못 표기 | 100.0B로 수정 | **해소** |
| V-04 | 수치 연산 오류 | CAGR 중앙값: (40.50+43.84)/2 = 42.17% → 본문 42.14%로 잘못 표기 | 42.17%로 수정 | **해소** |
| V-05 | 미인용 주장 | "IBM 핸드오프 45% 감소" — 인용 코드 없이 사실처럼 기술됨 | 본문에서 삭제 (신뢰도 섹션 [C] 항목에서 제거) | **해소** |
| V-06 | 미인용 주장 | "7개월마다 2배 가속" — 인용 코드 없이 기술됨 | research.md에서 [[G-08]](#ref-g-08) 출처 확인. 경쟁사 비교표에서 삭제, research.md 인용 형태로만 유지 | **해소** |
| V-07 | 단일 소스 고위험 | Gartner 1,445% 문의 급증 — G-09 Keepler 블로그 단일 비공식 소스 | [B] 등급 유지, 단일 소스 한계 명시됨 (원 보고서 유지, 추가 검증 권고) | **잔존** (한계 명시) |
| V-08 | 단일 소스 고위험 | 62% 조직 AI 에이전트 실험·확장 — G-13 Flowful AI 단일 비공식 소스 | [B] 등급 유지, 단일 소스 한계 명시됨 | **잔존** (한계 명시) |

### 5-2. 이슈별 상세 처리

**V-01 (G-12 고아 인용) — 해소:**
References 테이블에 G-12를 신규 추가했다. TechCrunch 기사(2026-02-05)로, Anthropic이 Claude Opus 4.6을 Agent Teams 기능과 함께 출시하면서 14.5시간 태스크 완료 시간 지평을 달성했다는 내용의 출처다. [B] 등급 언론 기사.

**V-02 (G-21 출처-주장 불일치) — 잔존:**
G-21은 Mintz(법률회사) 특허 블로그다. 이 문서 내에 Gartner 예측 수치와 기업 성공률 통계가 인용되어 있을 수 있으나, References 제목만으로 원출처 직접 확인이 불가능하다. 해당 수치가 사용된 모든 위치에 "(G-21에서 재인용, 원출처 미확인)" 경고를 추가했다. Gartner 원본 보고서 직접 확인을 후속 과제로 권고한다.

**V-03 / V-04 (수치 연산 오류) — 해소:**
TAM 중앙값을 $99.6B에서 $100.0B로, CAGR 중앙값을 42.14%에서 42.17%로 수정했다. 모두 단순 산술 오류이며 원 데이터는 변경 없다.

**V-05 / V-06 (미인용 주장) — 해소:**
"IBM 핸드오프 45% 감소"는 인용 코드 없는 미확인 수치로 삭제했다. "7개월마다 2배" 관련 내용은 research.md에서 [[G-08]](#ref-g-08)(METR Time Horizon 1.1, 2026-01-29, [A] 등급)을 출처로 확인했으나, skill1.md 신뢰도 섹션의 [C] 표기는 출처 불명확 판단이었으므로 해당 항목을 삭제하고 research.md의 인용 구조만 유지한다.

### 5-3. 최종 판정

**교차검증 최종 판정: PARTIAL**

- 주요 이슈(V-01, V-03, V-04, V-05, V-06) 해소 완료
- 일부 이슈(V-02 원출처 미확인, V-07/V-08 단일 소스 고위험) 잔존
- 잔존 이슈는 주석 표기 또는 [B] 등급 명시로 독자 판단 가능하게 처리
- 전반적 논리 구조 및 판정 근거는 건전하게 유지됨

---

## 6. 3축 평가 근거

### 고객가치 (Customer Value)

#### 강점

| 항목 | 내용 | 출처 |
|------|------|------|
| **Pain Point 명확** | 멀티에이전트 오케스트레이션·계획 수립 역량 부족 — 통신사의 네트워크 운영·고객접점·내부 자동화 분야에서 구체적 미해결 과제 | [[E-01]](#ref-e-01), [[E-02]](#ref-e-02), [[G-17]](#ref-g-17) |
| **성과 입증** | NTT Docomo: 네트워크 유지보수 에이전트 → 장애 대응 시간 50% 이상 단축 (구체적 KPI 공개) | [[G-17]](#ref-g-17) |
| **기업 수요 폭증** | Gartner 기준 2024 Q1→2025 Q2 기간 멀티에이전트 시스템 기업 문의 1,445% 급증 [[G-09]](#ref-g-09) (단일 소스) | [[G-09]](#ref-g-09) |
| **대체제 대비 우위** | 기존 RPA·자동화 대비 LLM 기반 적응형 의사결정 가능 → 복잡한 비즈니스 로직(고객 상담, 정책 결정) 자동화 가능 | [[P-01]](#ref-p-01), [[P-07]](#ref-p-07) |
| **고객 수용성** | 62% 조직이 AI 에이전트 실험·확장 중 (단일 소스) | [[G-13]](#ref-g-13) |

#### 리스크

| 항목 | 내용 | 출처 |
|------|------|------|
| **지불의향(WTP) 미검증** | 고객 가격 저항 → 특히 중소 조직은 엔터프라이즈 솔루션 비용 부담 우려 | 데이터 부족 |
| **도입 복잡도 장벽** | 80% 계획 vs 10% 성공(원출처 미확인) → 실제 운영 단계에서 복잡도로 인한 취소율 높음 | [[G-21]](#ref-g-21) |
| **Context Rot 신뢰성** | 컨텍스트 60% 초과 시 성능 저하 → 장기 태스크 SLA 보장 어려움 → 고객 신뢰 이슈 | [[G-15]](#ref-g-15), [[P-05]](#ref-p-05) |
| **전환 비용 높음** | 기존 RPA/자동화 시스템 레거시 → 멀티에이전트로 마이그레이션 비용·시간 추정 어려움 | 데이터 부족 |

---

### 사업포텐셜 (Business Potential)

#### 강점

| 항목 | 내용 | 출처 |
|------|------|------|
| **대규모 시장** | TAM: $91.4B~$108.6B (중앙값 $100.0B ≈ 130조 원), CAGR 40~44% | [[G-19]](#ref-g-19) |
| **정책 지원** | SKT 1조+ 파라미터 주권 AI 모델 투자, KT 엔터프라이즈 플랫폼 공식 발표 → 정부 지원 가능성 높음 | [[E-01]](#ref-e-01), [[E-02]](#ref-e-02) |
| **통신사 기회** | 네트워크 운영(실시간 모니터링), 고객서비스(상담), 내부 자동화(3개 분야) — 구체적 ROI 경로 명확 | [[G-17]](#ref-g-17), [[E-01]](#ref-e-01) |
| **진입 초기 단계** | 프레임워크 GA 완료, 초기 도입 고객 확보 중 → 시장 타이밍 적절 | [[G-01]](#ref-g-01), [[G-06]](#ref-g-06) |
| **경쟁사 벤치마크** | AT&T 410개 에이전트, SKT 2,000개+ 에이전트 → 스케일링 가능성 입증 | [[G-24]](#ref-g-24), [[E-01]](#ref-e-01) |

#### 리스크

| 항목 | 내용 | 출처 |
|------|------|------|
| **시장 불확실성** | 40% 이상 프로젝트 취소 가능성 (Gartner 2027년까지, G-21에서 재인용, 원출처 미확인) → 장기 ROI 불확실 | [[G-21]](#ref-g-21) |
| **수익 모델 미정** | 라이선스(LangGraph), SaaS(MS), 서비스형(KT Agentic Fabric) 경쟁 → 조직의 수익 구조 미정의 | 데이터 부족 |
| **SKT/KT 선점** | 국내 통신사 2개 이미 플랫폼 공식 발표 → 고객 흡수 경쟁 심화 예상 | [[E-01]](#ref-e-01), [[E-02]](#ref-e-02) |
| **프로토콜 경쟁** | 4개 표준(MCP, ACP, A2A, ANP) 경쟁 지속 → 단일 프로토콜 조기 락인 리스크 | [[G-10]](#ref-g-10), [[P-01]](#ref-p-01) |
| **규제 불확실성** | AI 에이전트 자율성·책임·감시에 대한 규제 진화 → 향후 규제 리스크 | 데이터 부족 |

---

### 기술경쟁력 (Technology Competitiveness)

#### 강점

| 항목 | 내용 | 출처 |
|------|------|------|
| **높은 TRL** | LangGraph v1.0 TRL 8 (GA 완료, 프로덕션), CrewAI TRL 7~8, MS Agent Framework TRL 7 (RC) | [[G-01]](#ref-g-01), [[G-04]](#ref-g-04), [[G-06]](#ref-g-06) |
| **핵심 특허** | Microsoft 11만 9,196개 글로벌 특허(77,859개 활성), Google 4,500개+ AI 특허 — 생태계 주도 기업 진입 장벽 높음 | [[G-26]](#ref-g-26) |
| **프로토콜 표준** | MCP + A2A 양축 표준화 진행 중 → 오픈소스 기반 진입 가능성 높음 | [[P-01]](#ref-p-01), [[G-10]](#ref-g-10) |
| **학술 기반 강화** | HiPlan, SagaLLM, ReAcTree 등 VLDB/ICLR 논문 → 업계 표준 기술 정의 중 | [[P-04]](#ref-p-04), [[P-05]](#ref-p-05), [[P-06]](#ref-p-06) |
| **에코시스템 성숙** | PyPI 617만 다운로드(LangGraph), GitHub 44,923 stars(CrewAI) → 개발자 커뮤니티 활성 | [[G-06]](#ref-g-06), [[G-04]](#ref-g-04) |

#### 리스크

| 항목 | 내용 | 출처 |
|------|------|------|
| **Context Rot 미해결** | 컨텍스트 60% 초과 시 성능 저하 — 기술적으로 미해결 과제 남음 | [[G-15]](#ref-g-15), [[P-05]](#ref-p-05) |
| **구현 복잡도 높음** | 오케스트레이션 토폴로지 설계, 계획 검증, 트랜잭션 보장 등 복수 기술 통합 필수 | [[P-02]](#ref-p-02), [[P-05]](#ref-p-05) |
| **내부 인력 부족** (추정) | 오케스트레이션 설계·계획 알고리즘 전문가 시장 부족 — 채용·파트너 필요 | 데이터 부족 |
| **특허 진입 장벽** | 오케스트레이터 에이전트 기반 시스템의 구체적 특허화 어려움 (추상적 개념으로 거절 리스크) | [[G-26]](#ref-g-26) |
| **기술 수렴** | LLM 성능 수렴 → 차별화는 오케스트레이션에만 집중 → 차별화 여지 감소 | [[P-02]](#ref-p-02) |

---

## 7. 정량 평가 (200점 만점)

### 채점 기준 적용

| # | 평가 항목 | 세부1 (10) | 세부2 (10) | 세부3 (10) | 세부4 (10) | 소계 (40) | 근거 |
|---|----------|-----------|-----------|-----------|-----------|----------|------|
| **1** | **고객가치** | | | | | **31** | [[G-09]](#ref-g-09), [[G-13]](#ref-g-13), [[G-17]](#ref-g-17), [[G-21]](#ref-g-21), [[P-07]](#ref-p-07) |
| | Pain Point 심각도 | 8 | | | | | NTT Docomo 50% 단축 성과 입증, Gartner 1,445% 문의 급증 [[G-09]](#ref-g-09), [[G-17]](#ref-g-17) |
| | 제공 가치 명확성 | 8 | | | | | 오케스트레이션·계획 역량이 명확한 pain point 해결 [[P-01]](#ref-p-01), [[P-07]](#ref-p-07) |
| | 대체제 대비 우위 | 8 | | | | | 기존 RPA 대비 LLM 적응형 의사결정 가능 — 복잡 로직 자동화 우위 명확 [[P-01]](#ref-p-01) |
| | 고객 수용성 | 7 | | | | | 62% 조직 실험·확장 중 [[G-13]](#ref-g-13), 단 80% vs 10% 성공 괴리 [[G-21]](#ref-g-21) |
| | | | | | | | |
| **2** | **시장매력도** | | | | | **34** | [[G-19]](#ref-g-19), [[E-01]](#ref-e-01), [[E-02]](#ref-e-02), [[G-01]](#ref-g-01), [[G-06]](#ref-g-06) |
| | TAM/SAM/SOM | 9 | | | | | TAM $91.4B~$108.6B (중앙값 $100.0B ≈ 130조), 복수 기관 교차확인 [[G-19]](#ref-g-19) |
| | CAGR | 9 | | | | | 40~44% 고성장, 복수 출처 일관성 [[G-19]](#ref-g-19) |
| | 시장 타이밍 | 8 | | | | | 프레임워크 GA 완료, 초기 도입 단계 → 진입 적절 [[G-01]](#ref-g-01), [[G-06]](#ref-g-06) |
| | 규제/정책 환경 | 8 | | | | | SKT 1조+ 투자, KT 플랫폼 공식 발표 → 정책 지원 양호 [[E-01]](#ref-e-01), [[E-02]](#ref-e-02) |
| | | | | | | | |
| **3** | **기술경쟁력** | | | | | **32** | [[G-06]](#ref-g-06), [[G-04]](#ref-g-04), [[G-01]](#ref-g-01), [[P-04]](#ref-p-04), [[P-05]](#ref-p-05), [[G-15]](#ref-g-15) |
| | TRL 수준 | 8 | | | | | LangGraph v1.0 TRL 8, CrewAI TRL 7~8 [[G-06]](#ref-g-06), [[G-04]](#ref-g-04) |
| | 특허 포트폴리오 | 7 | | | | | Microsoft 11만 특허, Google 4,500+ AI 특허 보유, 하지만 조직 내 특허 미정 [[G-26]](#ref-g-26) |
| | 기술 장벽 | 8 | | | | | MCP+A2A 표준화로 오픈소스 기반 진입 가능, 하지만 오케스트레이션 설계 장벽 높음 [[P-02]](#ref-p-02), [[P-01]](#ref-p-01) |
| | 표준/인증 | 9 | | | | | MCP 표준 주도(Anthropic), A2A v0.3 Linux Foundation 기증 — 표준화 진행 중 [[P-01]](#ref-p-01), [[G-10]](#ref-g-10) |
| | | | | | | | |
| **4** | **경쟁우위** | | | | | **29** | [[E-01]](#ref-e-01), [[E-02]](#ref-e-02), [[P-02]](#ref-p-02), [[G-21]](#ref-g-21), [[G-09]](#ref-g-09) |
| | 시장 포지션 | 6 | | | | | SKT/KT 선점 → 조직은 동등~후발, 빠른 추격 필요 [[E-01]](#ref-e-01), [[E-02]](#ref-e-02) |
| | 차별화 지속성 | 7 | | | | | 오케스트레이션 토폴로지 설계(1년+ 차별화 가능) [[P-02]](#ref-p-02), 단 대형 기업(MS, Google)의 모방 빠름 |
| | 경쟁사 대응력 | 7 | | | | | 표준 프로토콜 기반 → 경쟁사 추격 가능, 하지만 도메인 특화(네트워크 등)는 방어 가능 |
| | 생태계/파트너 | 9 | | | | | PyPI 617만 DL(LangGraph), GitHub 44K stars(CrewAI), MS/Google 파트너십 가능 [[G-06]](#ref-g-06), [[G-04]](#ref-g-04) |
| | | | | | | | |
| **5** | **실행가능성** | | | | | **29** | [[E-01]](#ref-e-01), [[G-17]](#ref-g-17), [[P-02]](#ref-p-02), [[G-21]](#ref-g-21), 데이터부족 |
| | 내부 역량 | 6 | | | | | 데이터 부족 — 조직의 AI/멀티에이전트 개발 인력 현황 미정 [중앙값+데이터부족] |
| | 투자 ROI | 6 | | | | | 데이터 부족 — 조직의 투자 규모·회수 계획 미정 [중앙값+데이터부족] |
| | 일정 현실성 | 8 | | | | | Phase 1 Buy(2026-Q2), Phase 2 Borrow(2026-Q3~Q4), Phase 3 Build(2026-Q4~2027-Q2) 현실적 [[P-02]](#ref-p-02), [[G-17]](#ref-g-17) |
| | 리스크 관리 | 9 | | | | | Context Rot(SagaLLM 도입), 도입 복잡도(파일럿 단계적 확대), SKT/KT 경쟁(Fast follower) 등 완화 전략 제시 [[P-05]](#ref-p-05), [[P-06]](#ref-p-06), [[G-21]](#ref-g-21) |

### 종합 평가

| 항목 | 소계 | 등급 |
|------|------|------|
| 1. 고객가치 | 31/40 | **양호** |
| 2. 시장매력도 | 34/40 | **우수** |
| 3. 기술경쟁력 | 32/40 | **양호** |
| 4. 경쟁우위 | 29/40 | **보통** |
| 5. 실행가능성 | 29/40 | **보통** |
| | | |
| **총점** | **155/200** | **77.5%** |

### 판정

| 점수 범위 | 판정 | 해석 |
|----------|------|------|
| 160~200 | **Go** | 즉시 추진 |
| **120~159** | **Conditional Go** | ← **해당** |
| 80~119 | **재검토** | 근본적 재설계 |
| 1~79 | **No-Go** | 추진 부적합 |

**최종 판정: Conditional Go (조건부 승인)**

---

## 8. 최종 제언 (Winning Strategy Recommendation)

```
┌─────────────────────────────────────────────────────────────────┐
│ 과제명: Multi-Agent (L2 #2) 기술 도입 및 내부화 전략          │
├─────────────────────────────────────────────────────────────────┤
│ 추천 방향:                                                      │
│   Phase 1: BUY (LangGraph + MCP 표준)                          │
│   Phase 2: BORROW (MS Agent Framework, NTT 컨설팅)             │
│   Phase 3: BUILD (조직 특화 오케스트레이션 토폴로지)           │
├─────────────────────────────────────────────────────────────────┤
│ 핵심 근거:                                                      │
│                                                                 │
│ 시장: 글로벌 CAGR 42% 고성장, 국내 SKT/KT 동시 진출          │
│       → TAM 130조 원, 2026년 초 고성장 단계 [G-19, E-01, E-02]│
│                                                                 │
│ 기술: LangGraph TRL 8 완성, NTT Docomo 50% 단축 성과 검증     │
│       → 프로덕션 그레이드 성숙도 도달 [G-06, G-17]             │
│       단, Context Rot 미해결 → 장기 태스크 SLA 보장 제약 [G-15]│
│                                                                 │
│ 사업: 통신사 핵심 기회(네트워크, 고객서비스, 내부 자동화)      │
│       → SKT 2,000개+ 에이전트 운영 사례 레퍼런스 [E-01]        │
│       → 오케스트레이션 토폴로지 설계가 차별화 핵심 [P-02]       │
└─────────────────────────────────────────────────────────────────┘
```

### 단계별 실행 계획

#### Phase 1: Buy (2026-Q2 완료)

- **LangGraph v1.0 라이선스 계약** — 프로덕션 프레임워크 확보
  - Cost: 오픈소스 무료 + LangSmith 모니터링 유료 (정확한 비용은 계약 시 확인 필요)
  - Timeline: 즉시
  - Owner: 플랫폼팀

- **MCP 스팩 기반 개발 표준화** — Anthropic MCP 채택
  - Deliverable: 조직 MCP 가이드 문서 작성
  - Timeline: 2026-Q2
  - Owner: 아키텍처팀

#### Phase 2: Borrow (2026-Q3~Q4)

- **Microsoft Agent Framework GA 연계 기술 마이그레이션** 계획
  - Timeline: 2026-Q3(GA 후)
  - Owner: MS 파트너사

- **NTT Docomo 사례 벤치마킹** — 네트워크 에이전트 시스템
  - Objective: 기술·운영 검증 (장애 대응 시간 단축 재현)
  - Timeline: 2026-06 ~ 09
  - Owner: 네트워크운영팀 + 기술팀

- **오케스트레이션 토폴로지 설계 컨설팅** 착수
  - Partner: AdaptOrch 논문 저자/기관
  - Objective: 조직 특화 토폴로지 아키텍처 정의
  - Timeline: 2026-09 부터
  - Owner: R&D팀

#### Phase 3: Build (2026-Q4 ~ 2027-Q2)

- **조직 특화 오케스트레이션 토폴로지 개발**
  - 도메인: 네트워크 운영, 고객접점, 내부 자동화 중 우선순위 1개 선택
  - Objective: LLM 성능 수렴 시대 차별화 (AdaptOrch 논문의 "Task-Adaptive Topology") [[P-02]](#ref-p-02)
  - Timeline: 2026-Q4 ~ 2027-Q2 (18개월)
  - Budget: [추정, 근거부족] — 팀 규모 5~10명, 인프라 비용 미정

- **Context Rot 대응 로드맵** 수립 (병렬)
  - 목표: SagaLLM의 트랜잭션 보장 패턴 도입
  - Timeline: 2027-Q1 부터 (학술 논문 구현 기반) [[P-05]](#ref-p-05)
  - Owner: 신뢰성팀

### 리스크 및 완화 전략

| 리스크 | 확률 | 영향 | 완화 전략 |
|-------|------|------|----------|
| **Context Rot 미해결** | High (M) | High — 장기 태스크 SLA 보장 불가 | SagaLLM/ReAcTree 논문 기술 2026-Q4부터 적용. 단기(수시간)는 프로덕션, 장기(수일+)는 파일럿 단계로 분리 [[P-05]](#ref-p-05), [[P-06]](#ref-p-06) |
| **도입 복잡도 높음** | High (M) | High — 10% 미만 성공률(원출처 미확인) [[G-21]](#ref-g-21) | Phase 1: 소규모 도메인(1~2개 부서) 파일럿부터 시작. 조직 변화관리 병렬 추진 |
| **SKT/KT 선점 우위** | High (M) | Medium — 진입 늦으면 이미 표준화 | Fast follower 전략: 표준 프로토콜(MCP+A2A) 즉시 채택 [[P-01]](#ref-p-01), 3~6개월 내 PoC 완료 |
| **프로토콜 경쟁** | Medium (M) | Low — MCP+A2A 양축 표준화 진행 중 | 표준 통합 대기. 2027년까지 프로토콜 관중론자 전략 [[G-10]](#ref-g-10), [[P-01]](#ref-p-01) |
| **경쟁사 기술 갭** (1~2년) | Medium (M) | Medium — TRL 격차 | Buy/Borrow 전략으로 즉시 따라잡기. Build(차별화)는 18개월 후 |

---

## 9. 신뢰도 평가

### 근거

**높은 확신 [A/B] 항목:**
- Microsoft Agent Framework RC 출시 일시·기능 — Microsoft 공식 블로그 [A]
- LangGraph v1.0 GA 완료, PyPI 다운로드 수 — LangChain 공식 [A]
- Google A2A v0.3 업그레이드 — Google Cloud 공식 [A]
- NTT Docomo 상용 배포 — 공식 보도자료(2026-02-25) [A]
- AdaptOrch, SagaLLM, ReAcTree 논문 수치 — VLDB/ICLR 게재 [A]
- SKT/KT MWC 2026 공식 발표 — 프레스릴리스 [A]
- 글로벌 시장 CAGR 40~44% — 다수 독립 리서치 기관 교차확인 [B]

**추가 검증 필요 [C] 항목:**
- CrewAI 월 4.5억 워크플로우, LangGraph 30~40% 레이턴시 우위 — 단일 비공식 소스 [C]
- "10% 성공률" 및 "40% 취소 가능성" — G-21(특허 법률 블로그)에서 재인용, Gartner 원출처 미확인 [C]

**데이터 공백 항목 (3개):**
1. 조직의 AI/멀티에이전트 개발 인력 현황 → 보강 키워드: "organization agent orchestration team skill assessment"
2. 조직의 투자 규모·ROI 계획 → 보강 키워드: "telco multi-agent platform investment roadmap"
3. SKT/KT Agentic AI 플랫폼 성능 지표·가격 정책 → 보강 키워드: "SKT AI Agent performance metrics, KT Agentic Fabric pricing"

---

## 10. 조건부 승인 요건

**진행 전 반드시 확보해야 할 항목:**

### 조건 1: Context Rot 기술 로드맵
- **내용:** 컨텍스트 60% 초과 시 성능 저하 대응 기술 로드맵 수립
- **근거:** [[G-15]](#ref-g-15), [[P-05]](#ref-p-05), [[P-06]](#ref-p-06) — SagaLLM(트랜잭션 보장), ReAcTree(계층적 트리) 기술 검토
- **구체안:**
  - 단기(2026-Q4): SagaLLM 패턴 도입(모듈식 체크포인팅)
  - 중기(2027-Q1): ReAcTree 계층적 트리 적용
  - 장기(2027-Q2+): 신규 Context Rot 해법 연구 진행 또는 파트너 기술 도입
- **신뢰도:** Medium (학술 논문 기반, 산업 구현 사례 미확인)

### 조건 2: 오케스트레이션 토폴로지 설계 역량 확보
- **내용:** 차별화의 핵심인 "Task-Adaptive Orchestration Topology" 설계 역량 보유 또는 파트너십
- **근거:** [[P-02]](#ref-p-02) — LLM 성능 수렴 시대에 오케스트레이션 토폴로지가 모델 선택보다 중요
- **구체안:**
  - 내부 역량 확보: AdaptOrch 논문 저자 또는 유사 전문가 영입/계약 (2026-09부터)
  - 또는 외부 컨설팅: 학술/컨설팅 기관과 토폴로지 설계 프로젝트 수립
- **신뢰도:** High (이론적 근거 명확)

### 조건 3: MCP + A2A 프로토콜 스택 표준화
- **내용:** 조직 내 MCP + A2A 양축 프로토콜 기술 표준 채택 및 개발 가이드 작성
- **근거:** [[P-01]](#ref-p-01), [[G-10]](#ref-g-10) — MCP(도구 접근) + A2A(에이전트 간 통신) 상호보완 프로토콜 쌍 확립
- **구체안:**
  - 2026-Q2: 조직 MCP 가이드 문서 완성
  - 2026-Q3: A2A v0.3 검토 및 선택적 도입 여부 결정
  - 2026-Q4: 개발팀 교육 및 표준화 완료
- **신뢰도:** High (표준 문서 공개)

---

## 11. 기업 발언 원문 (직접 인용)

### SKT (E-01)

> "AI Native로 거듭날 것이다. 더 이상 통신 회사가 아닌 AI 회사로 변신한다." — SKT CEO 정재헌, MWC 2026 기자회견(2026-03-01) [[E-01]](#ref-e-01)

SKT는 MWC 2026에서 전사 AI 전환 전략을 공식 발표했다. "One Person, One AI Agent" 이니셔티브를 통해 전 직원이 최소 1개 AI 에이전트를 활용하도록 하며, 현재 2,000개 이상의 내부 에이전트가 마케팅·법무·PR 등 부서에서 운영 중이다. 소버린 AI 모델은 519B에서 1조 파라미터 이상으로 업그레이드 예정이며, OpenAI와 국내 AI 데이터센터 공동 구축 협력 중이다 [[E-01]](#ref-e-01).

### KT (E-02)

KT는 MWC 2026에서 Agentic Fabric을 "기업 환경에 최적화된 AI 전환(AX) 운영체제"로 발표했다. 5계층(경험·지능·컨텍스트·실행·거버넌스) 구조로 복잡한 시스템 통합, 데이터 보안, 메모리 불연속성, 예측 불가능한 의사결정이라는 기업 AI 도입 4대 장벽을 해소한다고 밝혔다. 통신·금융·자산관리·HR 분야에 내부 적용 완료 상태다 [[E-02]](#ref-e-02).

---

## References

> 총 35건 | 출처 유형 구분 없이 단일 테이블 정렬 (코드 순)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Microsoft Foundry Blog — Microsoft Agent Framework Reaches Release Candidate | [링크](https://devblogs.microsoft.com/foundry/microsoft-agent-framework-reaches-release-candidate/) | news | 2026-02-19 | [A] |
| <a id="ref-g-02"></a>G-02 | Particula Tech — LangGraph vs CrewAI vs OpenAI Agents SDK: Choosing Your Agent Framework in 2026 | [링크](https://particula.tech/blog/langgraph-vs-crewai-vs-openai-agents-sdk-2026) | blog | 2026-02 | [B] |
| <a id="ref-g-03"></a>G-03 | Microsoft Semantic Kernel Blog — Migrate to Microsoft Agent Framework Release Candidate | [링크](https://devblogs.microsoft.com/semantic-kernel/migrate-your-semantic-kernel-and-autogen-projects-to-microsoft-agent-framework-release-candidate/) | news | 2026-02 | [A] |
| <a id="ref-g-04"></a>G-04 | CrewAI Changelog | [링크](https://docs.crewai.com/en/changelog) | news | 2026-02-26 | [A] |
| <a id="ref-g-05"></a>G-05 | GitHub — crewAIInc/enterprise-mcp-server | [링크](https://github.com/crewAIInc/enterprise-mcp-server) | news | 2026 | [A] |
| <a id="ref-g-06"></a>G-06 | LangChain Blog — LangChain and LangGraph Agent Frameworks Reach v1.0 Milestones | [링크](https://blog.langchain.com/langchain-langgraph-1dot0/) | news | 2025-10 | [A] |
| <a id="ref-g-07"></a>G-07 | OpenAgents Blog — CrewAI vs LangGraph vs AutoGen vs OpenAgents (2026) | [링크](https://openagents.org/blog/posts/2026-02-23-open-source-ai-agent-frameworks-compared) | blog | 2026-02-23 | [B] |
| <a id="ref-g-08"></a>G-08 | METR — Time Horizon 1.1 (2026-01-29) | [링크](https://metr.org/blog/2026-1-29-time-horizon-1-1/) | news | 2026-01-29 | [A] |
| <a id="ref-g-09"></a>G-09 | Keepler — Not more AI — orchestration. The era of the Agentic Mesh. | [링크](https://keepler.io/2026/01/29/the-era-of-the-agentic-mesh/) | blog | 2026-01-29 | [B] |
| <a id="ref-g-10"></a>G-10 | Google Cloud Blog — Agent2Agent protocol (A2A) is getting an upgrade | [링크](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade) | news | 2026 | [A] |
| <a id="ref-g-11"></a>G-11 | LangChain Blog — Plan-and-Execute Agents | [링크](https://blog.langchain.com/planning-agents/) | blog | 2025 | [B] |
| <a id="ref-g-12"></a>G-12 | TechCrunch — Anthropic releases Opus 4.6 with agent teams | [링크](https://techcrunch.com/2026/02/05/anthropic-releases-opus-4-6-with-agent-teams/) | news | 2026-02-05 | [B] |
| <a id="ref-g-13"></a>G-13 | Flowful AI Blog — Why 2026 is the Year of the Voice Agent | [링크](https://flowful.ai/blog/voice-agents-2026/) | blog | 2026 | [B] |
| <a id="ref-g-14"></a>G-14 | Microsoft Industry Blog — Microsoft Accelerates Telecom Return on Intelligence at MWC 2026 | [링크](https://www.microsoft.com/en-us/industry/blog/telecommunications/2026/02/24/microsoft-accelerates-telecom-return-on-intelligence-with-a-unified-trusted-ai-platform/) | news | 2026-02-24 | [A] |
| <a id="ref-g-15"></a>G-15 | LogRocket Blog — LLM context problem in 2026 | [링크](https://blog.logrocket.com/llm-context-problem/) | blog | 2026 | [B] |
| <a id="ref-g-16"></a>G-16 | DEV Community — The Great AI Agent Showdown of 2026: OpenAI, AutoGen, CrewAI, or LangGraph? | [링크](https://dev.to/topuzas/the-great-ai-agent-showdown-of-2026-openai-autogen-crewai-or-langgraph-1ea8) | blog | 2026-01 | [C] |
| <a id="ref-g-17"></a>G-17 | NTT Docomo Press Release — Commercial Deployment of Agentic AI System for Network Maintenance | [링크](https://www.docomo.ne.jp/english/info/media_center/pr/2026/0225_01.html) | news | 2026-02-25 | [A] |
| <a id="ref-g-18"></a>G-18 | Ubergizmo — NTT Docomo Shows SyncMe Personal AI Agent at MWC | [링크](https://www.ubergizmo.com/2026/03/ntt-docomo-syncme-personal-ai-agent/) | news | 2026-03 | [B] |
| <a id="ref-g-19"></a>G-19 | Fortune Business Insights / Mordor Intelligence / Precedence Research — Agentic AI Market Size Forecasts | [링크](https://www.fortunebusinessinsights.com/agentic-ai-market-114233) | news | 2026 | [B] |
| <a id="ref-g-20"></a>G-20 | Google Cloud Blog — Google Agentspace enables the agent-driven enterprise | [링크](https://cloud.google.com/blog/products/ai-machine-learning/google-agentspace-enables-the-agent-driven-enterprise) | news | 2026 | [A] |
| <a id="ref-g-21"></a>G-21 | Mintz — Understanding How to Patent Agentic AI Systems | [링크](https://www.mintz.com/insights-center/viewpoints/2231/2025-03-19-understanding-how-patent-agentic-ai-systems) | blog | 2025-03-19 | [B] |
| <a id="ref-g-22"></a>G-22 | Korea IT Times — SK telecom Declares Shift to 'AI Native' Company at MWC 2026 | [링크](https://www.koreaittimes.com/news/articleView.html?idxno=151344) | news | 2026-03 | [B] |
| <a id="ref-g-23"></a>G-23 | The Elec — KT Moves Aggressively Into Enterprise A.I. Market With 'Agentic Fabric' | [링크](https://www.thelec.net/news/articleView.html?idxno=5604) | news | 2026 | [B] |
| <a id="ref-g-24"></a>G-24 | Mobile World Live — Feature: Operators call up agentic AI | [링크](https://www.mobileworldlive.com/att/feature-operators-call-up-agentic-ai/) | news | 2026 | [B] |
| <a id="ref-g-25"></a>G-25 | CX Today — Verizon Is Using AI Agents to Improve Customer Experiences | [링크](https://www.cxtoday.com/contact-center/verizon-is-using-ai-agents-to-improve-customer-experiences-heres-how/) | news | 2026 | [B] |
| <a id="ref-g-26"></a>G-26 | PatentPC — AI Patent Showdown: Google vs. Microsoft vs. Amazon | [링크](https://patentpc.com/blog/ai-patent-showdown-google-vs-microsoft-vs-amazon-who-holds-the-most) | blog | 2025 | [B] |
| <a id="ref-e-01"></a>E-01 | SKT CEO 정재헌 — MWC 2026 기자회견 발표 (AI Native 전략) | [링크](https://www.prnewswire.com/news-releases/sk-telecom-ceo-unveils-ai-native-strategy-at-mwc26-driving-koreas-leap-in-ai-innovation-302700470.html) | IR/발표 | 2026-03-01 | [A] |
| <a id="ref-e-02"></a>E-02 | KT — Agentic Fabric 공식 발표 (MWC 2026) | [링크](https://www.digitaltoday.co.kr/en/view/14834/kt-to-accelerate-enterprise-ax-with-agentic-fabric) | IR/발표 | 2026-02 | [A] |
| <a id="ref-p-01"></a>P-01 | Adimulam, Gupta, Kumar — The Orchestration of Multi-Agent Systems: Architectures, Protocols, and Enterprise Adoption | [링크](https://arxiv.org/abs/2601.13671) | paper | 2026-01 | [A] |
| <a id="ref-p-02"></a>P-02 | Yu — AdaptOrch: Task-Adaptive Multi-Agent Orchestration in the Era of LLM Performance Convergence | [링크](https://arxiv.org/abs/2602.16873) | paper | 2026-02-18 | [A] |
| <a id="ref-p-03"></a>P-03 | (저자 미확인) — Multi-Agent Collaboration via Evolving Orchestration | [링크](https://arxiv.org/abs/2505.19591) | paper | 2025-05 | [A] |
| <a id="ref-p-04"></a>P-04 | Li et al. — HiPlan: Hierarchical Planning for LLM Agents with Adaptive Global-Local Guidance | [링크](https://arxiv.org/abs/2508.19076) | paper | 2025-08-26 | [B] |
| <a id="ref-p-05"></a>P-05 | Chang et al. — SagaLLM: Context Management, Validation, and Transaction Guarantees for Multi-Agent LLM Planning | [링크](https://arxiv.org/abs/2503.11951) | paper | 2025-03 | [A] |
| <a id="ref-p-06"></a>P-06 | ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning | [링크](https://arxiv.org/abs/2511.02424) | paper | 2025-11 | [A] |
| <a id="ref-p-07"></a>P-07 | Tomašev et al. — Intelligent AI Delegation (arXiv:2602.11865) | [링크](https://arxiv.org/abs/2602.11865) | paper | 2026-02-12 | [B] |

---

## 보강 검색 키워드 (데이터 공백 해소)

- **조직 인력 역량:** `organization multi-agent orchestration team`, `LLM agent development engineer skill assessment`
- **투자 ROI:** `multi-agent platform investment telco`, `agentic AI implementation cost ROI analysis`
- **SKT/KT 성능:** `SKT AI agent metrics performance`, `KT Agentic Fabric platform specs pricing`
- **G-21 원출처 보강:** `Gartner agentic AI project cancellation 2027`, `enterprise multi-agent success rate survey 2025`

---

## 결론

**Multi-Agent (L2 #2) 기술은 즉시 추진 권고하나, 3가지 조건부 승인 요건 반드시 선행.**

- 기술 성숙도: TRL 7~8 (프로덕션 그레이드)
- 시장 규모: $91B~$108B, CAGR 42% (고성장)
- 경쟁 시황: SKT/KT 동시 진출 (창 12~18개월)
- 핵심 리스크: 도입 성공률 10% 미만(원출처 미확인), Context Rot 미해결

**조건부 승인 요구사항:**
1. Context Rot 기술 로드맵 (SagaLLM/ReAcTree)
2. 오케스트레이션 토폴로지 설계 역량 (AdaptOrch 기술)
3. MCP + A2A 프로토콜 표준화

**권고 전략:** Buy(LangGraph) + Borrow(MS/NTT) + Build(차별화 토폴로지) 3단계 실행.
