---
topic: Multi-Agent (L2) — Intelligent Agent Orchestration & Agent Oriented Planning
domain: agentic-ai
l2: multi-agent
l2_number: 2
date: 2026-03-09
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch, existing-weekly-research]
---

# Research Report: Multi-Agent — Intelligent Agent Orchestration & Agent Oriented Planning

## Executive Summary (경영진 요약)

> Multi-Agent 기술은 2026년 초 TRL 7~8 수준으로 진입했다. Microsoft Agent Framework RC(2026-02-19), LangGraph v1.0 GA, CrewAI 엔터프라이즈화 등 주요 프레임워크가 프로덕션 그레이드에 도달했으며, MCP + A2A 이중 프로토콜이 사실상 표준으로 자리잡고 있다. 시장 규모는 2026년 약 91~109억 달러로 추정되며[추정] CAGR 40~44%로 성장 중이다. 국내에서는 SKT와 KT가 각각 MWC 2026에서 "One Person One AI Agent" 이니셔티브와 "Agentic Fabric" 플랫폼을 공개하며 통신사 AI 에이전트 경쟁이 본격화됐다. 글로벌 통신사 중 NTT Docomo는 네트워크 유지보수 에이전트 시스템 상용화를 완료하여 장애 대응 시간 50% 이상 단축이라는 구체적 성과를 기록했다. LLM 성능 수렴 시대에 오케스트레이션 토폴로지 설계 역량이 핵심 차별화 요소로 부상하고 있으며, Context Rot(컨텍스트 60% 초과 시 성능 저하)은 장기 태스크 신뢰성의 구조적 도전 과제로 상존한다.

## 연구 질문

> Multi-Agent 기술(L2)의 기술 성숙도·시장 동향·경쟁사(통신사 포함) 전략·학술 동향·특허 동향을 파악하여 WTIS 판정을 위한 팩트 베이스를 구축한다. 하위 L3 기술인 Intelligent Agent Orchestration(agent-orchestration)과 Agent Oriented Planning(agent-planning)을 통합 분석한다.

---

## 1. 기술 현황

### 1-1. TRL 및 성숙도

**TRL 판단**

Multi-Agent 오케스트레이션 기술은 2026년 초 기준 TRL 7~8 구간에 위치한다. 주요 근거:

- **TRL 8 (시스템 완성·검증)**: LangGraph v1.0 GA(2025-10), Uber·LinkedIn·Klarna 프로덕션 적용. NTT Docomo 네트워크 유지보수 에이전트 상용 배포(2026-02-04). AT&T 410개 GenAI 에이전트 프로덕션 운영 [[G-06]](#ref-g-06), [[G-17]](#ref-g-17)
- **TRL 7 (시스템 프로토타입)**: Microsoft Agent Framework RC(2026-02-19), Q1 2026 GA 목표. CrewAI 엔터프라이즈 대시보드(AMP) 공개 [[G-01]](#ref-g-01), [[G-04]](#ref-g-04)
- **TRL 6 (파일럿 검증 중)**: Agent Planning 고도화 기술(계층적 트리 탐색, 트랜잭셔널 보장). NTT Docomo SyncMe 개인 에이전트 파일럿(2026 봄 예정) [[G-18]](#ref-g-18)

**기술 성숙 패턴**

오케스트레이션 레이어 기술은 단일 에이전트 → 멀티에이전트 → "Agentic Mesh"(전문화 에이전트 팀의 계층적 오케스트레이션) 방향으로 진화 중이다 [[G-09]](#ref-g-09). 동시에 "어떻게 계획할 것인가"에서 "어떻게 계획을 검증하고 보장할 것인가"로 패러다임이 이동하는 중이다 [[P-07]](#ref-p-07).

### 1-2. 핵심 기술 요소

**프레임워크 3파전 포지셔닝**

- **LangGraph**: 그래프 기반 상태 머신 워크플로우. 체크포인팅·human-in-the-loop 내장. 월간 PyPI 다운로드 약 617만 건. v1.0 GA(2025-10) 이후 제로 브레이킹 체인지 정책 [[G-06]](#ref-g-06), [[G-02]](#ref-g-02)
- **CrewAI**: 역할 기반 멀티에이전트 협업. GitHub stars 44,923개, 월간 4.5억 워크플로우 처리[C]. MCP first-class 지원(2026-02-26), enterprise-mcp-server 공개 [[G-04]](#ref-g-04), [[G-05]](#ref-g-05)
- **Microsoft Agent Framework**: AutoGen + Semantic Kernel 통합. A2A·MCP·AG-UI 동시 지원. RC(2026-02-19), Q1 2026 GA 목표 [[G-01]](#ref-g-01)

**Agent Planning 핵심 패턴**

- **Planner-Worker 분리**: Plan-and-Execute 패턴이 산업 표준으로 정착. 대형 LLM을 계획에만 투입하고 하위 태스크는 경량 모델로 처리하는 비용 최적화 패턴 [[G-11]](#ref-g-11)
- **계층적 계획(HiPlan)**: 글로벌 마일스톤(macro) + 단계별 힌트(micro) 이중 계층. RAG 방식 마일스톤 라이브러리 검색 [[P-04]](#ref-p-04)
- **트랜잭셔널 보장(SagaLLM)**: Saga 트랜잭션 패턴 적용. 모듈식 체크포인팅 + 보상 가능한 실행(compensable execution). VLDB 2026 게재 [[P-05]](#ref-p-05)

**상호운용성 프로토콜**

- **MCP (Anthropic)**: 도구·컨텍스트 접근 표준화. CrewAI·Microsoft Agent Framework 전면 채택
- **A2A (Google)**: 피어 간 에이전트 조율·위임. Linux Foundation 기증, 50개 이상 기업 지지. v0.3: gRPC 지원, security card 서명 [[G-10]](#ref-g-10)
- MCP(도구 접근) + A2A(에이전트 간 통신) 상호보완 프로토콜 쌍 확립

**미해결 과제**

- **Context Rot**: 컨텍스트 윈도우 약 60% 초과 시 출력 품질 저하 현상. 장기 실행 에이전트의 핵심 도전 과제 [[G-15]](#ref-g-15)
- **장기 태스크 신뢰성**: 태스크 완료 시간 2배 증가 시 실패율 4배 증가 법칙. SLA 보장 어려움 [[G-08]](#ref-g-08)
- **80% → 10% 괴리**: 80%의 엔터프라이즈가 멀티에이전트로의 확장을 계획하나, 실제 성공한 비율은 10% 미만 [[G-21]](#ref-g-21)

---

## 2. 시장 동향

### 2-1. 시장 규모 및 성장률

**Agentic AI 시장 규모 (복수 출처 교차 검증)**

| 조사기관 | 2026 시장규모 | 목표연도 규모 | CAGR | 출처 |
|---------|--------------|--------------|------|------|
| Fortune Business Insights | $91.4억[추정] | $1,391.9억(2034) | 40.50% | [[G-19]](#ref-g-19) |
| Mordor Intelligence | $98.9억[추정] | $574.2억(2031) | 42.14% | [[G-19]](#ref-g-19) |
| Precedence Research | $108.6억[추정] | $1,990억(2034) | 43.84% | [[G-19]](#ref-g-19) |
| Market.us | — | — | 49.6%(2026-2033) | [[G-19]](#ref-g-19) |

**시장 드라이버**

- **기술 성숙**: LangGraph·CrewAI·Microsoft Agent Framework 프로덕션 그레이드 도달로 도입 장벽 하락 [[G-02]](#ref-g-02), [[G-01]](#ref-g-01)
- **기업 수요 폭증**: Gartner 기준 2024 Q1→2025 Q2 기간 멀티에이전트 시스템 기업 문의 1,445% 급증 [[G-09]](#ref-g-09)
- **성과 입증**: IBM 리서치 — 멀티에이전트 오케스트레이션 시 핸드오프 45% 감소, 의사결정 속도 3배 향상[C] [[G-21]](#ref-g-21)
- **엔터프라이즈 채택**: 62%의 조직이 AI 에이전트를 실험·확장 중 [[G-13]](#ref-g-13)

### 2-2. 채택 패턴

- **프레임워크 마이그레이션**: CrewAI(프로토타입) → LangGraph(프로덕션) 전환이 가장 빈번한 경로 [[G-02]](#ref-g-02)
- **"Agentic Mesh" 하이브리드**: LangGraph 오케스트레이터 + CrewAI 팀의 복합 아키텍처 등장 [[G-02]](#ref-g-02), [[G-07]](#ref-g-07)
- **에이전트 시간 지평 확장**: 에이전트가 50% 신뢰도로 완료하는 코딩 태스크 시간이 7개월마다 2배 증가. 2026년 2월 현재 14.5시간 수준 [[G-08]](#ref-g-08)

---

## 3. 경쟁사 동향

### 3-1. 주요 플레이어 동향

**주요 플레이어 동향**

| 기업 | 동향 | 출처 |
|------|------|------|
| Microsoft | Agent Framework RC(2026-02-19): AutoGen + Semantic Kernel 통합. A2A·MCP·AG-UI 3개 프로토콜 동시 지원. Q1 2026 GA 목표. Copilot Studio에 멀티에이전트 오케스트레이션 기능 통합, MCP GA 포함. | [[G-01]](#ref-g-01), [[G-14]](#ref-g-14) |
| Google | A2A Protocol v0.3 공개, Linux Foundation 기증. 50개+ 파트너 지지. Agentspace → Gemini Enterprise로 통합, Agent Designer(no-code) 공개. PwC 대규모 AI 에이전트 생태계 파트너십 체결. | [[G-10]](#ref-g-10), [[G-20]](#ref-g-20) |
| Anthropic | MCP 표준 주도. 타 프레임워크 전면 채택으로 생태계 표준 지위 확고. Claude Opus 4.6(2026-02-05): 14.5시간 태스크 완료 시간 지평. Agent Teams(병렬 협업) + Cowork(비개발자 반자율 에이전트) 출시. | [[G-10]](#ref-g-10), [[G-12]](#ref-g-12) |
| LangChain (LangGraph) | v1.0 GA(2025-10): 체크포인팅·내구성 실행·스트리밍 완성. 월 617만 PyPI 다운로드. Deep Agents(내장 `write_todos` 툴) 공개. Uber·LinkedIn·Klarna 프로덕션 적용. | [[G-02]](#ref-g-02), [[G-06]](#ref-g-06) |
| CrewAI | GitHub stars 44,923개. MCP first-class 지원(2026-02-26), enterprise-mcp-server 공개. `planning=True` 플래그로 AgentPlanner 활성화. 엔터프라이즈 대시보드(AMP) 출시. | [[G-04]](#ref-g-04), [[G-05]](#ref-g-05) |
| OpenAI | Agents SDK: Handoff·guardrail 내장. GPT-4o Realtime API로 음성 에이전트 연계. 상태 지속성(persistence) 미내장이 한계. | [[G-02]](#ref-g-02), [[G-13]](#ref-g-13) |

### 3-2. 통신사 경쟁사 동향

**통신사 AI 에이전트 동향**

| 기업 | 동향 | 출처 |
|------|------|------|
| SKT | MWC 2026(2026-03-01): "AI Native" 전략 발표. "One Person, One AI Agent" 이니셔티브 — 전 직원 AI 에이전트 1개 이상 사용 목표. 내부 2,000개+ AI 에이전트 운영 중(마케팅·법무·PR 등). A.phone(AI 에이전트 통합 스마트폰), 통합 AI 에이전트(T world·T Direct Shop 접점 연결). 1GW 규모 하이퍼스케일 AI 데이터센터 구축, 주권 AI 모델 1조 파라미터 이상 업그레이드 예정. | [[G-22]](#ref-g-22), [[E-01]](#ref-e-01) |
| KT | MWC 2026: "Agentic Fabric" 플랫폼 공개 — 기업 AI 전환(AX) 전용 OS. 5개 계층(경험·지능·컨텍스트·실행·거버넌스). Agent Builder(노코드 에이전트 생성), Agentic AICC(멀티에이전트 콜센터 자동화) 발표. 통신·금융·자산관리·HR 분야 내부 적용 완료. SaaS·온프레미스·하이브리드 지원. | [[G-23]](#ref-g-23), [[E-02]](#ref-e-02) |
| NTT Docomo | 2026-02-04 네트워크 유지보수용 Agentic AI 시스템 상용 배포 — 100만+ 네트워크 장비(기지국·코어망) 실시간 트래픽·알람 분석. 복잡 장애 대응 시간 50% 이상 단축. Amazon Bedrock AgentCore 기반. SyncMe 개인 AI 에이전트 MWC 2026 시연, 2026년 여름 상업 출시 목표. | [[G-17]](#ref-g-17), [[G-18]](#ref-g-18) |
| AT&T | Ask AT&T 플랫폼: 10만+ 사용자, 750억 API 호출 누적. 410개+ GenAI 에이전트 프로덕션 운영. Ask AT&T Workflows 프레임워크로 에이전트 개발. Ask Operations으로 네트워크 자동화(human oversight 포함). | [[G-24]](#ref-g-24) |
| Verizon | Google Cloud Gemini 기반 AI 에이전트 고객 서비스 도입 — 평균 통화 시간 단축, 에이전트 지원 정확도 96%. NVIDIA GPU 엣지 플랫폼 + 5G 프라이빗 네트워크 파트너십. | [[G-25]](#ref-g-25) |

---

## 4. 제품/서비스 스펙 비교

**주요 프레임워크 스펙 비교**

| 기업 | 지표①: 워크플로우 처리 규모 | 지표②: 개발 생산성 | 가격(정책) | 출처 |
|------|--------------------------|------------------|-----------|------|
| LangGraph (LangChain) | 월 617만 PyPI 다운로드. 프로덕션 적용 다수(Uber·LinkedIn·Klarna). 30~40% 낮은 레이턴시[C] | 표준 워크플로우 대비 40% 느린 초기 개발 속도[C]. 복잡 워크플로우 최적화 | 오픈소스 무료, LangSmith(모니터링) 유료 | [[G-02]](#ref-g-02), [[G-16]](#ref-g-16) |
| CrewAI | 월 4.5억 워크플로우 처리[C]. GitHub stars 44,923 | 표준 비즈니스 워크플로우 Time-to-Production 40% 빠름[C] | 오픈소스 무료, Enterprise(AMP 대시보드) 별도 유료 | [[G-02]](#ref-g-02), [[G-04]](#ref-g-04) |
| Microsoft Agent Framework | 프로덕션 그레이드 엔터프라이즈 인증 예정(GA 이후). AutoGen 기존 워크로드 마이그레이션 지원 | .NET/Python 양쪽 지원. A2A·MCP·AG-UI 3개 프로토콜 동시 지원 | 오픈소스(GitHub 공개), Azure 연동 시 Azure 요금 | [[G-01]](#ref-g-01), [[G-03]](#ref-g-03) |
| OpenAI Agents SDK | GPT-4o 모델 최적화. Handoff·guardrail 내장. 상태 지속성 미지원 | 100라인 이하 구현 가능. 빠른 프로토타이핑 | 오픈소스, GPT 모델 API 사용료 별도 | [[G-02]](#ref-g-02) |
| Google Agentspace (Gemini Enterprise) | 100만+ 기업 사용자[추정]. Agent Marketplace — Accenture·Deloitte 등 파트너 에이전트 제공 | Agent Designer(노코드). Deep Research 에이전트(GA). OneDrive·SharePoint·Salesforce 등 통합 | 공개 정보 없음 (Gemini Enterprise 구독 포함 추정[추정]) | [[G-20]](#ref-g-20) |
| KT Agentic Fabric | 5계층 아키텍처. SaaS·온프레미스·하이브리드 지원 | Agent Builder(노코드 드래그앤드롭). 산업별 표준 에이전트 템플릿 제공 | 공개 정보 없음 | [[E-02]](#ref-e-02) |

---

## 5. 학술 동향

### 5-1. Agent Orchestration 주요 논문

**주요 논문 — Agent Orchestration**

| 논문 | 핵심 | 출처 |
|------|------|------|
| "The Orchestration of Multi-Agent Systems: Architectures, Protocols, and Enterprise Adoption" (Adimulam et al., 2026) | 계획·정책집행·상태관리·품질운영 통합 오케스트레이션 레이어 아키텍처 제시. MCP + A2A 상호보완 프로토콜 체계 분석 | [[P-01]](#ref-p-01) |
| "AdaptOrch: Task-Adaptive Multi-Agent Orchestration in the Era of LLM Performance Convergence" (Yu, 2026) | LLM 성능 수렴 시대에 오케스트레이션 토폴로지(병렬/순차/계층/하이브리드)가 모델 선택보다 중요. 작업 의존성 그래프 기반 동적 토폴로지 선택으로 정적 기준 대비 12~23% 향상 | [[P-02]](#ref-p-02) |
| "Multi-Agent Collaboration via Evolving Orchestration" (2025) | 중앙 오케스트레이터 강화학습 기반 진화. 퍼펫티어(puppeteer) 패러다임 제안 | [[P-03]](#ref-p-03) |

### 5-2. Agent Planning 주요 논문

**주요 논문 — Agent Planning**

| 논문 | 핵심 | 출처 |
|------|------|------|
| "HiPlan: Hierarchical Planning for LLM Agents with Adaptive Global-Local Guidance" (Li et al., 2025) | 글로벌 마일스톤 + 로컬 스텝 힌트 이중 계층. RAG 방식 마일스톤 라이브러리. 장기 태스크 로컬 최적 함정 회피 | [[P-04]](#ref-p-04) |
| "SagaLLM: Context Management, Validation, and Transaction Guarantees for Multi-Agent LLM Planning" (Chang et al., 2025) | Saga 트랜잭션 패턴 적용. GlobalValidationAgent + SagaCoordinatorAgent. 모듈식 체크포인팅과 보상 실행. VLDB 2026 게재 | [[P-05]](#ref-p-05) |
| "ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning" (2025) | ReAct를 계층적 동적 트리로 확장. 에피소딕+워킹 이중 메모리. WAH-NL 벤치마크 61% 성공률(ReAct 31% 대비 2배). ICLR 2026 게재 | [[P-06]](#ref-p-06) |
| "Intelligent AI Delegation" (Tomašev et al., 2026) | Contract-First Decomposition: 검증 불가능한 태스크 위임 금지 원칙. 태스크 분해 vs. 위임 개념적 구분. 책임·신뢰·권한 계층화 프레임워크 | [[P-07]](#ref-p-07) |

### 5-3. 연구 방향 요약

- **LLM 성능 수렴 시대의 오케스트레이션 우위**: 모델 선택보다 토폴로지 설계가 성능을 결정하는 시대로 전환 중 [[P-02]](#ref-p-02)
- **검증 우선(Validation-First) 패러다임**: 단순 계획 알고리즘에서 독립 검증 에이전트 설계로 연구 초점 이동 [[P-07]](#ref-p-07)
- **장기 태스크 신뢰성**: Context Rot, 트랜잭셔널 보장, 계층적 트리 탐색이 공통 연구 주제로 수렴 [[P-05]](#ref-p-05), [[P-06]](#ref-p-06)

---

## 6. 특허 동향

### 6-1. 주요 특허 출원 현황

**공개된 주요 특허**

- **Google** `US12316753B1` (2025-05-27 공개): Secure multi-agent system for privacy-preserving distributed computation — 프라이버시 보존 분산 컴퓨팅용 보안 멀티에이전트 시스템 [[G-26]](#ref-g-26)
- **Google** `US12111859B2`: Enterprise generative AI architecture — 오케스트레이터가 멀티모달 LLM 프롬프트를 에이전트별 지시로 변환하는 엔터프라이즈 GenAI 아키텍처 [[G-26]](#ref-g-26)
- **국제출원** `WO2021084510A1`: Executing artificial intelligence agents in an operating environment — 운영 환경 내 AI 에이전트 실행 (선행 기술, 2021) [[G-26]](#ref-g-26)

### 6-2. 특허 트렌드

- **빅테크 AI 특허 경쟁**: Google 4,500개+ AI 특허 보유(헬스케어 포함). Microsoft 11만 9,196개 글로벌 특허(전 기술 영역, 77,859개 활성) [[G-26]](#ref-g-26)
- **에이전트 시스템 특허화 과제**: 오케스트레이터 에이전트 기반 시스템의 구성 요소·데이터 흐름·훈련 프로세스를 구체적으로 정의하지 않으면 추상적 개념으로 거절 리스크 존재 [[G-21]](#ref-g-21)
- **특허 출원 가속**: USPTO AI 특허 데이터셋 기준 에이전트 시스템 관련 출원이 2024~2025년 급증 추세[B] [[G-26]](#ref-g-26)

**데이터 공백**: Multi-agent orchestration/planning에 특화된 한국 특허(KIPRIS) 출원 현황은 공개 정보 미확인.

---

## 7. 기업 발언 & 보도자료

### 7-1. SKT (E-01)

> "AI Native로 거듭날 것이다. 더 이상 통신 회사가 아닌 AI 회사로 변신한다." — SKT CEO 정재헌, MWC 2026 기자회견(2026-03-01) [[E-01]](#ref-e-01)

SKT는 MWC 2026에서 전사 AI 전환 전략을 공식 발표했다. "One Person, One AI Agent" 이니셔티브를 통해 전 직원이 최소 1개 AI 에이전트를 활용하도록 하며, 현재 2,000개 이상의 내부 에이전트가 마케팅·법무·PR 등 부서에서 운영 중이다. 소버린 AI 모델은 519B에서 1조 파라미터 이상으로 업그레이드 예정이며, OpenAI와 국내 AI 데이터센터 공동 구축 협력 중이다 [[E-01]](#ref-e-01).

### 7-2. KT (E-02)

KT는 MWC 2026에서 Agentic Fabric을 "기업 환경에 최적화된 AI 전환(AX) 운영체제"로 발표했다. 5계층(경험·지능·컨텍스트·실행·거버넌스) 구조로 복잡한 시스템 통합, 데이터 보안, 메모리 불연속성, 예측 불가능한 의사결정이라는 기업 AI 도입 4대 장벽을 해소한다고 밝혔다. 통신·금융·자산관리·HR 분야에 내부 적용 완료 상태다 [[E-02]](#ref-e-02).

### 7-3. NTT Docomo

NTT Docomo는 2026-02-25 공식 보도자료에서 네트워크 유지보수 Agentic AI 시스템의 상용 배포 시작을 발표했다. 100만 개 이상의 네트워크 장비에서 실시간 데이터를 분석하여 복잡 장애 대응 시간 50% 이상 단축이라는 구체적 성과를 공개했다. Amazon Bedrock AgentCore를 기반으로 하며 세계 최대 규모 데이터셋 기반 Agentic AI 시스템 중 하나라고 밝혔다 [[G-17]](#ref-g-17).

### 7-4. Microsoft

Microsoft는 Copilot Studio 블로그(2026)에서 "2025년에 확장 가능한 에이전트 기반 업무의 토대를 마련했으며, 2026년에는 그 기반 위에 구축하는 조직이 가장 큰 혜택을 얻을 것"이라고 밝혔다. 또한 MWC 2026에서 통신사 대상 AI ROI 가속화를 위한 통합 신뢰 AI 플랫폼을 발표하며 통신 산업 특화 포지셔닝을 강화했다 [[G-14]](#ref-g-14).

### 7-5. AT&T

AT&T는 Ask AT&T 플랫폼이 10만+ 사용자, 750억 API 호출, 일 평균 50억 토큰 처리에 도달했다고 공개했다. 현재 410개+ GenAI 에이전트가 프로덕션 환경에서 운영 중이며, Ask AT&T Workflows 프레임워크로 소프트웨어 개발 사이클 내에서 에이전트를 개발하고 있다 [[G-24]](#ref-g-24).

---

## 8. 전략적 시사점

**기술 트렌드**

- LLM 모델 성능 수렴 → 오케스트레이션 토폴로지 설계 역량이 차별화 핵심으로 이동 (AdaptOrch 논문 근거)
- MCP + A2A 이중 프로토콜 스택이 사실상 표준으로 확립되는 중
- 검증 우선(Validation-First) 패러다임 전환: 계획 알고리즘 + 독립 검증 에이전트 설계 역량이 동시 필수화
- 에이전트 시간 지평 확장(7개월마다 2배)이 지속되면 2026년 말 주간 단위 자율 태스크 도달 예측[추정]

**기회**

- SKT/KT가 모두 멀티에이전트 플랫폼을 전략 핵심으로 선언한 상황에서, 통신사 특화 Agentic AI(네트워크 운영·고객접점·내부 자동화) 기술 확보 시 차별화 포인트 확보 가능
- NTT Docomo 사례(네트워크 유지보수 에이전트 상용화)는 통신사 Agentic AI의 구체적 ROI 레퍼런스로 활용 가능
- SagaLLM의 트랜잭셔널 보장 패턴은 통신·금융 등 규제 산업의 장기 자율 워크플로우 적용에 직접 활용 가능
- Microsoft Agent Framework GA(Q1 2026 예정) 시점 맞춰 엔터프라이즈 마이그레이션 가이드 선점 가능

**위협**

- 80% 엔터프라이즈가 멀티에이전트 확장을 계획하나 성공률 10% 미만 — 도입·운영 복잡도가 구조적 진입 장벽
- Context Rot은 장기 실행 에이전트 SLA 보장을 어렵게 하는 미해결 기술 과제
- 4개 거버넌스 프로토콜(MCP, ACP, A2A, ANP) 경쟁 지속 → 단일 프로토콜 조기 락인 리스크
- OpenAI Agents SDK의 GPT 락인 구조 — 모델 중립(model-agnostic) 아키텍처 선택이 전략적으로 중요
- Gartner 예측: 2027년까지 현재 에이전트 프로젝트의 40% 이상이 비용·복잡도·리스크 이유로 취소될 수 있음 [[G-21]](#ref-g-21)

---

## 신뢰도 평가

**높은 확신 [A/B]:**

- Microsoft Agent Framework RC 출시 일시(2026-02-19) 및 기능 명세 — 공식 Microsoft 블로그 [A]
- LangGraph v1.0 출시 및 PyPI 다운로드 수 — LangChain 공식 changelog [A]
- Google A2A v0.3 기능 — Google 공식 개발자 블로그 [A]
- NTT Docomo Agentic AI 상용 배포 — 공식 보도자료(2026-02-25) [A]
- AdaptOrch, SagaLLM, ReAcTree 논문 핵심 수치 — arXiv/VLDB/ICLR 게재 [A]
- SKT MWC 2026 공식 발표 — 프레스릴리즈 [A]
- KT Agentic Fabric 아키텍처 — 공식 발표 기사 다수 교차 확인 [B]
- 시장 CAGR 40~44% — 다수 독립 리서치 기관 교차 확인 [B]

**추가 검증 필요 [C/D]:**

- LangGraph 레이턴시 30~40% 우위, CrewAI Time-to-Production 40% 빠름 — 단일 비공식 블로그 소스 [C]
- IBM 핸드오프 45% 감소·의사결정 3배 속도 수치 — 출처 구체성 불명확 [C]
- CrewAI 월간 4.5억 워크플로우 수치 — 자사 발표, 측정 기준 불명확 [C]
- "4개월마다 2배" 가속 추세 지속 여부 — 단기 관측, 추세 전환 가능성 [C]

**데이터 공백:**

- Multi-agent orchestration 관련 국내(KIPRIS) 특허 출원 현황
- SKT/KT Agentic AI 플랫폼의 구체적 성능 지표·가격 정책 (공개 정보 없음)
- LangGraph vs CrewAI 실제 엔터프라이즈 계약 수·매출 비교 (공개 정보 없음)
- Anthropic 자체 멀티에이전트 오케스트레이션 프레임워크 로드맵 (공개 정보 없음)

---

## References

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
| <a id="ref-g-12"></a>G-12 | TechCrunch — Anthropic releases Opus 4.6 with agent teams | [링크](https://techcrunch.com/2026/02/05/anthropic-releases-opus-4-6-with-new-agent-teams/) | news | 2026-02-05 | [B] |
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
