---
type: weekly-monitor
domain: agentic-ai
week: 2026-W11
date: 2026-03-09
l3_count: 7
deep_count: 4
---

# 주간 기술 동향: Agentic AI (2026-W11)

## Executive Summary

| 세부기술 | 신호 | 핵심 내용 | 분석 |
|----------|------|----------|------|
| Agentic Context Engineering | 🔴 긴급 | ACE 프레임워크 ICLR 2026 정식 발표, AppWorld +17.1%, GitHub 오픈소스 공개 | Deep |
| Agent Orchestration | 🟡 주목 | MS Agent Framework RC 출시, Agentic Mesh 패턴 부상, MCP+A2A 표준화 | Deep |
| Agent Planning | 🟡 주목 | METR 자율 태스크 14.5시간 달성, Planner-Worker 표준화, SagaLLM VLDB 2026 | Deep |
| Adaptive RAG | 🟡 주목 | A-RAG Agentic 3원칙 정형화, VoiceAgentRAG 레이턴시 316배 감소 | Deep |
| 페르소나 플러그인 | 🟢 평온 | PersonaKG + PersonaAgent/GraphRAG 점진적 진전 | Quick |
| 관계 그래프 구축 | 🟢 평온 | KG+LLM 통합 트렌드 지속, 돌파구 없음 | Quick |
| 컨텍스트 액션 추천 | 🟢 평온 | 특이사항 없음 | Quick |

---

## 🟢 Quick 요약 (변화 미미)

### 페르소나 플러그인
- PersonaKG(페르소나 상식 지식그래프) 구축 연구 및 PersonaAgent+GraphRAG 프레임워크 제안. 커뮤니티 기반 개인화 접근이나 산업 적용 사례는 아직 제한적.

### 관계 그래프 구축
- KG+LLM 통합 트렌드 지속. GraphRAG 기술 성숙, Neo4j 활용 확대. 이번 주 특이 돌파구 없음.

### 컨텍스트 기반 액션 추천
- 특이사항 없음. Agentic AI 전체 흐름 속에서 점진 발전 중.

---

## 🔴 Agentic Context Engineering — 긴급

> 상세 리서치: [2026-03-09_research-agentic-context-engineering.md](2026-03-09_research-agentic-context-engineering.md)

### 기술 동향

**ACE 프레임워크 ICLR 2026 정식 발표**가 이번 주 최대 사건이다. SambaNova·Stanford·UC Berkeley 공동 개발한 ACE는 LLM 에이전트의 컨텍스트를 "진화하는 플레이북"으로 취급하며, **Generator-Reflector-Curator** 3역할 분업으로 기존 접근의 구조적 결함(brevity bias, context collapse)을 해결한다 [[G-01]](#ref-g-01).

핵심 메커니즘은 전체 컨텍스트를 매번 재작성하는 대신, 의미적 유사도 기반 항목 단위 **델타 업데이트(grow-and-refine)**를 수행하는 것이다. 오프라인(시스템 프롬프트 최적화)과 온라인(에이전트 실시간 메모리) 두 모드 모두에서 작동한다 [[G-02]](#ref-g-02).

Microsoft Research는 2026-02-26 **CORPGEN** 프레임워크를 발표했다. 기업 환경의 다중 동시 태스크(MHTE)를 다루며, Working/Structured LTM/Semantic **3계층 메모리** 아키텍처로 베이스라인 대비 최대 **3.5배 성능 향상**을 달성했다 [[G-03]](#ref-g-03).

### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| SambaNova / Stanford / UC Berkeley | ACE ICLR 2026 채택. AppWorld +10.6%, 금융 +8.6%, 적응 레이턴시 86.9% 감소. DeepSeek-V3.1로 IBM GPT-4.1 기반 에이전트와 동등 성능 달성. GitHub 오픈소스 공개 | [[G-01]](#ref-g-01), [[G-02]](#ref-g-02) |
| Microsoft Research | CORPGEN(2026-02-26) 3계층 메모리 아키텍처, MHTE 3.5배 성능 향상. Azure Foundry Agent Service에 장기 메모리 프리뷰 출시 | [[G-03]](#ref-g-03) |
| Anthropic | Context Engineering 가이드 50만 뷰. Context rot 대응 전략(요약, 서브에이전트, just-in-time retrieval) 공개. MCP 표준 재단(AAIF) 설립 | [[G-04]](#ref-g-04) |
| Google DeepMind | Gemini 3.1 Pro(1M 토큰) + Interactions API 베타. 서버사이드 컨텍스트 관리 | [[G-05]](#ref-g-05) |
| OpenAI | Agents SDK에 Sessions + Memory 모듈 공개. 2026-03 메모리 업데이트(workspace-scoped) | [[G-06]](#ref-g-06) |
| LangChain | CEO "Context Engineering이 새로운 AI 해자". Deep Agents(가상 파일시스템, 토큰 관리, 스킬·메모리 내장) 공개 | [[G-07]](#ref-g-07) |

### 시장 시그널
- Gartner: 12~18개월 내 context engineering이 기업 AI 인프라 **기반 요소**로 전환 전망 [[G-08]](#ref-g-08)
- Sequoia Capital: AI 에이전트의 "agentic leverage" 반영 투자 평가 모델 조정 시작 [[G-08]](#ref-g-08)
- Anthropic·Block·OpenAI 공동 설립 **AAIF**(리눅스 재단 산하), MCP 산업 표준 확산 [[G-09]](#ref-g-09)
- Magic LTM-2-Mini(1억 토큰) 등 초장문 컨텍스트 모델 등장, 실제 유효 용량은 광고의 60~70% [[G-10]](#ref-g-10)

### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| ACE: Evolving Contexts for Self-Improving LMs (Zhang et al., 2026) | Generator-Reflector-Curator 3역할, AppWorld +10.6%, ICLR 2026 | [[P-01]](#ref-p-01) |
| CORPGEN (Microsoft Research, 2026-02) | 기업 MHTE 3계층 메모리, 3.5배 성능 향상 | [[P-02]](#ref-p-02) |
| Codified Context (2026-02) | 복잡한 코드베이스에서 AI 에이전트를 위한 컨텍스트 인프라 코드화 | [[P-03]](#ref-p-03) |

### 전략적 시사점

**기회**
- ACE 오픈소스(ace-agent/ace)로 즉시 적용 가능. 내부 에이전트에 Generator-Reflector-Curator 패턴 도입 시 레이블 없이 운영 피드백만으로 컨텍스트 자동 개선
- MCP 표준화와 현재 intel-store MCP 기반 파이프라인의 높은 정합성
- CORPGEN의 3계층 메모리 아키텍처는 현재 플랫폼 메모리 설계에 직접 적용 가능

**위협**
- 대형 4사(Anthropic, OpenAI, Google, MS)가 모두 컨텍스트 관리 기능을 플랫폼 수준에서 내재화 → 서드파티 차별화 공간 축소
- 1M 토큰 확장에도 실제 유효 용량 60~70%, "Lost in the Middle" 지속 → 크기 확대만으로는 불충분

---

## 🟡 Agent Orchestration — 주목

> 상세 리서치: [2026-03-09_research-agent-orchestration.md](2026-03-09_research-agent-orchestration.md)

### 기술 동향

**프레임워크 3파전 포지셔닝이 확립**되었다. LangGraph(그래프 기반 상태 머신, 월 617만 PyPI DL), CrewAI(역할 기반 협업, 44.9K GitHub stars, MCP first-class), OpenAI Agents SDK(100라인 이하 구현, GPT 네이티브) [[G-11]](#ref-g-11).

**Microsoft Agent Framework RC**(2026-02-19)가 AutoGen + Semantic Kernel을 단일 프레임워크로 통합하며 A2A·MCP·AG-UI 3개 표준을 동시 지원한다. Q1 2026 GA 목표 [[G-12]](#ref-g-12).

**프로토콜 표준화**: MCP(도구·컨텍스트 접근) + A2A(에이전트 간 통신)가 상호보완 쌍으로 자리잡았다. A2A는 Linux Foundation 기증, 50개+ 기업 지지, v0.3에서 gRPC 추가 [[G-13]](#ref-g-13).

**Agentic Mesh** 패턴: 단일 범용 에이전트 → 전문 에이전트 팀 오케스트레이션. LangGraph 브레인이 CrewAI 팀을 지휘하는 하이브리드 구조 등장. Gartner: 멀티에이전트 문의 1,445% 급증(Q1 2024→Q2 2025) [[G-14]](#ref-g-14).

### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Microsoft | Agent Framework RC(2026-02-19): AutoGen + Semantic Kernel 통합, A2A·MCP·AG-UI 동시 지원, Q1 GA 목표 | [[G-12]](#ref-g-12) |
| Google | A2A v0.3 공개, Linux Foundation 기증, 50개+ 파트너 | [[G-13]](#ref-g-13) |
| LangChain | LangGraph v1.0 GA, 월 617만 PyPI DL, Uber·LinkedIn·Klarna 프로덕션 | [[G-11]](#ref-g-11) |
| CrewAI | 44.9K stars, MCP first-class(2026-02-26), enterprise-mcp-server 공개, 월 4.5억 워크플로우 | [[G-15]](#ref-g-15) |
| Anthropic | MCP 표준 주도, 타 프레임워크 전면 채택으로 생태계 표준 지위 확고 | [[G-13]](#ref-g-13) |

### Voice Agent x 멀티에이전트

음성 에이전트 end-to-end 레이턴시가 **300ms 이하**로 단축되며 인간 반응속도 수준에 도달했다 [[G-16]](#ref-g-16). MCP를 통해 음성 에이전트, 웹 챗봇, Slack 봇이 동일한 도구·데이터를 공유하는 **"Build once, deploy everywhere"** 패턴이 확산 중이다 [[G-16]](#ref-g-16). Deepgram(STT)·ElevenLabs(TTS)와 LangGraph/CrewAI 연동 스택이 구체화되고 있으며, Microsoft Teams 통합 음성 에이전트 플랫폼도 등장했다 [[G-17]](#ref-g-17).

### 시장 시그널
- 멀티에이전트 아키텍처: 단일 에이전트 대비 문제 해결 속도 45% 향상, 정확도 60% 개선 보고 [[G-14]](#ref-g-14)
- 62%의 조직이 AI 에이전트를 실험·확장 중 [[G-16]](#ref-g-16)
- 거버넌스 프로토콜 4파전: MCP, ACP, A2A, ANP — A2A가 50개+ 기업 지지로 우세 [[G-14]](#ref-g-14)

### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| AdaptOrch (Yu, 2026) | LLM 성능 수렴 시대, 오케스트레이션 토폴로지가 모델 선택보다 중요. 정적 대비 12-23% 향상 | [[P-04]](#ref-p-04) |
| MAS Orchestration Survey (Adimulam et al., 2026) | 계획·정책집행·상태관리·품질운영 통합 아키텍처, MCP+A2A 분석 | [[P-05]](#ref-p-05) |

### 전략적 시사점

**기회**
- Agentic Mesh 기반 복합 아키텍처(LangGraph 오케스트레이터 + CrewAI 팀) 레퍼런스 구축 기회
- 음성 에이전트와 멀티에이전트 통합(MCP 기반)은 통신사 고객접점 자동화 차별화 포인트

**위협**
- OpenAI Agents SDK GPT 락인 + 벤더 의존 리스크
- 거버넌스 프로토콜 4파전 → 표준 분열 가능성, 조기 단일 락인 위험

---

## 🟡 Agent Planning — 주목

> 상세 리서치: [2026-03-09_research-agent-planning.md](2026-03-09_research-agent-planning.md)

### 기술 동향

**Planner-Worker 분리 아키텍처**가 산업 표준으로 정착했다. Planner LLM이 목표를 DAG로 분해하고, Worker가 원자적으로 실행하는 구조로, 비용 최적화·감사 경로 확보·실패 격리 3가지 이점을 제공한다 [[G-18]](#ref-g-18).

4개 핵심 패턴으로 수렴 중이다:
- **HiPlan**: 글로벌 마일스톤 + 로컬 힌트, RAG 기반 마일스톤 라이브러리 [[P-06]](#ref-p-06)
- **SagaLLM**: 분산 Saga 트랜잭션 패턴 적용, 보상 가능한 실행으로 워크플로우 일관성 보장. VLDB 2026 게재 [[P-07]](#ref-p-07)
- **ReAcTree**: ReAct를 계층적 트리로 확장, 에피소딕+워킹 이중 메모리. WAH-NL 61% 성공률(ReAct 31% 대비 2배). ICLR 2026 게재 [[P-08]](#ref-p-08)
- **Contract-First Decomposition** (Google DeepMind): 검증 불가능한 태스크 위임 금지 원칙 [[P-09]](#ref-p-09)

**METR 시간 지평**: 에이전트 자율 태스크 지속시간이 7개월마다 2배 증가, 현재 **14.5시간** 달성. 2024-2025 구간은 4개월마다 2배로 가속. 이 추세 유지 시 2026년 말 주간 태스크 도달 예측 [[G-19]](#ref-g-19).

### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Microsoft | Agent Framework RC로 AutoGen 대체. 그래프 기반 멀티에이전트 워크플로우, 세션 상태 관리 | [[G-20]](#ref-g-20) |
| Google DeepMind | Intelligent AI Delegation 프레임워크. Contract-First Decomposition 도입 | [[G-21]](#ref-g-21) |
| Anthropic | Claude Opus 4.6 14.5시간 태스크 시간 지평, Agent Teams + Cowork 출시 | [[G-22]](#ref-g-22) |
| LangChain | Deep Agents — write_todos 자동 분해, 가상 파일시스템 메모리, 서브에이전트 스폰 | [[G-23]](#ref-g-23) |

### 시장 시그널
- METR: 태스크 시간 2배 시 실패율 **4배 증가** — 장기 태스크 신뢰성이 상용화 핵심 병목 [[G-19]](#ref-g-19)
- "어떻게 계획할 것인가" → "어떻게 계획을 **검증**할 것인가"로 패러다임 이동 [[G-21]](#ref-g-21)
- 프레임워크 생태계가 프로덕션 단계로 이행 (MS AF GA, LangGraph stable, CrewAI production-grade)

### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| HiPlan (Li et al., 2025) | 계층적 계획, RAG 보강 마일스톤 라이브러리 | [[P-06]](#ref-p-06) |
| SagaLLM (Chang et al., 2025) | Saga 트랜잭션 패턴, 보상 가능한 실행, VLDB 2026 | [[P-07]](#ref-p-07) |
| ReAcTree (2025) | 계층적 트리 탐색, 이중 메모리, WAH-NL 61%, ICLR 2026 | [[P-08]](#ref-p-08) |
| Intelligent AI Delegation (Tomašev et al., 2026) | Contract-First Decomposition, 검증 우선 위임 | [[P-09]](#ref-p-09) |

### 전략적 시사점

**기회**
- Planner-Worker + SagaLLM 트랜잭셔널 보장은 통신·금융 등 규제 산업 장기 자율 워크플로우에 직접 활용 가능
- METR 14.5시간→주간 태스크 전환이 1~2년 내 예상 — 장기 오케스트레이션 역량 선제 확보 유효

**위협**
- Context Rot(60% 초과 시 성능 저하) 미해결 — 장기 에이전트 신뢰성 구조적 병목
- 태스크 시간 2배 시 실패율 4배 법칙 — SLA 보장 어려움

---

## 🟡 Adaptive RAG — 주목

> 상세 리서치: [2026-03-09_research-adaptive-rag.md](2026-03-09_research-adaptive-rag.md)

### 기술 동향

**패러다임 전환이 가속**되고 있다. Classic RAG의 고정 파이프라인(인덱싱→검색→생성)에서 LLM이 검색 전략을 스스로 결정하는 **제어 루프(Agentic RAG)**로 전환 중이다 [[G-24]](#ref-g-24).

**A-RAG**(arXiv 2602.03442)가 Agentic RAG의 3원칙을 최초 정형화했다: Autonomous Strategy, Iterative Execution, Interleaved Tool Use. 계층적 검색 인터페이스(keyword/semantic/chunk_read)를 LLM에 직접 노출하여 **HotpotQA 94.5%**, 2WikiMultiHop 89.7% 달성(GPT-4o-mini 기준) [[P-10]](#ref-p-10).

**VoiceAgentRAG**(Salesforce AI Research, 2026-03-02)가 음성 에이전트 RAG의 레이턴시 문제를 구조적으로 해결했다. Slow Thinker(예측적 프리페치) + Fast Talker(캐시 전용) 이중 에이전트 구조로 캐시 히트 시 **316배 속도 향상**, 전체 히트율 75% [[P-11]](#ref-p-11).

### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Google | Vertex AI Adaptive Benchmarks — RAG Day-2 운영 평가 갭 해소 집중 | [[G-25]](#ref-g-25) |
| OpenAI | Responses API 기반 agentic RAG 표준화. file_search+web_search+code_interpreter 단일 루프. Assistants API 2026-08-26 폐기 | [[G-26]](#ref-g-26) |
| Anthropic | Contextual Retrieval(Contextual Embeddings + BM25) 검색 실패율 49% 감소, 리랭킹 결합 시 67% 감소 | [[G-27]](#ref-g-27) |
| AWS | SageMaker AI agentic RAG 파이프라인 자동화, Bedrock AgentCore $1억 투자 | [[G-28]](#ref-g-28) |
| Salesforce | VoiceAgentRAG 오픈소스 — 음성 RAG 레이턴시 316배 감소 | [[P-11]](#ref-p-11) |

### Voice Agent x RAG

음성 에이전트에서 RAG 통합의 핵심 과제는 **레이턴시**다. 자연스러운 대화를 위해 총 응답 시간 800ms 미만, 최고 수준 플랫폼은 ASR+LLM+TTS 전체를 500ms 이내로 처리한다. 벡터DB 쿼리가 50~300ms를 추가하므로, 200ms 예산 내에서 RAG를 작동시키는 것이 구조적 난제다 [[G-29]](#ref-g-29).

**VoiceAgentRAG의 해법**: Slow Thinker가 대화 스트림을 모니터링하며 후속 토픽을 예측, 관련 청크를 FAISS 캐시에 선제 프리페치. Fast Talker는 캐시에서만 검색하여 벡터DB를 완전 우회한다. 캐시 히트율 75%(웜 턴 79%), 150회 캐시 히트에서 16.5초 누적 레이턴시 절감 [[P-11]](#ref-p-11).

NVIDIA는 CES 2026에서 Nemotron 기반 음성 RAG 에이전트 레퍼런스 아키텍처를 공개했다 [[G-30]](#ref-g-30).

**시사점**: 음성 에이전트 RAG는 "온디맨드 검색"이 아니라 **"예측적 프리페칭 + 캐시 라우팅"**의 구조적 혁신이 필요하다.

### 시장 시그널
- Agentic RAG 프로덕션 도입률 **57%+** (전년도 51%에서 상승) [[G-24]](#ref-g-24)
- LlamaIndex: RAG 프레임워크 → 멀티에이전트 오케스트레이션 플랫폼으로 전환 [[G-24]](#ref-g-24)
- 검색 품질 > 생성 품질의 우선순위 역전 — 리트리벌 품질이 핵심 KPI로 인식 [[G-31]](#ref-g-31)

### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| A-RAG (Ayanami et al., 2026) | 계층적 검색 인터페이스, Agentic 3원칙 정형화, HotpotQA 94.5% | [[P-10]](#ref-p-10) |
| VoiceAgentRAG (Salesforce, 2026) | Slow Thinker + Fast Talker, 캐시 히트 316배 속도 향상 | [[P-11]](#ref-p-11) |
| Higress-RAG (2026) | MCP 기반 엔터프라이즈 RAG, Adaptive Routing + CRAG, 90%+ 리콜 | [[P-12]](#ref-p-12) |

### 전략적 시사점

**기회**
- VoiceAgentRAG의 예측적 프리페칭 패턴은 통신사 음성 AI 서비스에 직접 차별화 포인트 창출 가능
- 한국어 특화 Adaptive RAG: Naver HyperCLOVA X SEED 32B 멀티모달 확장 시점에 계층적 검색 인터페이스 결합 선점 효과

**위협**
- OpenAI Responses API + file_search로 진입 장벽 낮추면서 에코시스템 의존성 심화. Assistants API 2026-08 폐기로 마이그레이션 부담
- 프로덕션 agentic RAG는 벡터DB/시맨틱캐시/적응형라우터/CRAG/오케스트레이터 모두 필요 — 파일럿 성공 ≠ 프로덕션 성공(2024년 실패율 90%)

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **"컨텍스트가 새로운 해자"**: ACE(Context Engineering) + Adaptive RAG + Agent Planning 세 분야 모두 **컨텍스트 관리 품질**이 에이전트 성능의 핵심 차별화 요소로 수렴하고 있다. ACE의 델타 업데이트, RAG의 제어 루프, Planning의 Context Rot 문제가 같은 본질을 공유한다.

2. **MCP 프로토콜의 횡단적 영향**: Agent Orchestration(CrewAI/MS AF의 MCP first-class 지원), Adaptive RAG(Higress-RAG MCP 기반), Voice Agent(MCP 기반 "Build once, deploy everywhere") 등 모든 영역에서 MCP가 핵심 연결 고리로 작용한다. 현재 워크스페이스의 MCP 기반 아키텍처는 이 흐름과 높은 정합성을 보인다.

3. **Voice Agent의 교차 진출**: 음성 에이전트가 단순 인터페이스를 넘어 멀티에이전트 오케스트레이션(MCP 기반 통합)과 RAG(VoiceAgentRAG 예측적 프리페칭)에서 구조적 혁신을 주도하고 있다. 통신사 음성 AI 서비스에 직접 적용 가능한 패턴이 다수 등장했다.

4. **검증 우선 패러다임**: Agent Planning의 Contract-First Decomposition, Orchestration의 AdaptOrch, RAG의 CRAG — 모두 "실행 전 검증"을 강조하는 방향으로 수렴 중이다.

### 후속 조치 제안

- 🔴 **Agentic Context Engineering**: ACE 프레임워크의 전략적 중요도가 높음 → `/wtis standard` 검증을 통한 Go/No-Go 판정 고려
- 🟡 **VoiceAgentRAG**: Salesforce 오픈소스 Slow Thinker+Fast Talker 패턴을 통신사 음성 AI에 적용 가능성 검토
- 🟡 **Microsoft Agent Framework**: Q1 GA 출시 예정 — 엔터프라이즈 템플릿 선점 기회 모니터링 지속
- 📊 Obsidian 동기화: `/obsidian-bridge`

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | OpenReview — ACE ICLR 2026 | [링크](https://openreview.net/forum?id=eC4ygDs02R) | paper | 2026 | [A] |
| <a id="ref-g-02"></a>G-02 | SambaNova Blog — ACE Open-Sourced | [링크](https://sambanova.ai/blog/ace-open-sourced-on-github) | news | 2025-11 | [B] |
| <a id="ref-g-03"></a>G-03 | Microsoft Research Blog — CORPGEN | [링크](https://www.microsoft.com/en-us/research/blog/corpgen-advances-ai-agents-for-real-work/) | news | 2026-02-26 | [A] |
| <a id="ref-g-04"></a>G-04 | Anthropic — Effective Context Engineering | [링크](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | blog | 2025-09 | [A] |
| <a id="ref-g-05"></a>G-05 | AI Gazette — Gemini Interactions API Beta | [링크](https://aigazette.com/industry/google-deepmind-expands-gemini-interactions-api-beta-with-2026-agent-roadmap--s) | news | 2026 | [B] |
| <a id="ref-g-06"></a>G-06 | OpenAI Agents SDK — Memory Reference | [링크](https://openai.github.io/openai-agents-python/ref/memory/) | docs | 2026 | [A] |
| <a id="ref-g-07"></a>G-07 | Sequoia Capital Podcast — LangChain's Harrison Chase | [링크](https://sequoiacap.com/podcast/context-engineering-our-way-to-long-horizon-agents-langchains-harrison-chase/) | news | 2026 | [B] |
| <a id="ref-g-08"></a>G-08 | The New Stack — Memory for AI Agents: Context Engineering | [링크](https://thenewstack.io/memory-for-ai-agents-a-new-paradigm-of-context-engineering/) | news | 2026-01 | [B] |
| <a id="ref-g-09"></a>G-09 | Anthropic — Donating MCP, establishing AAIF | [링크](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) | news | 2025-12 | [A] |
| <a id="ref-g-10"></a>G-10 | Zylos Research — LLM Context Management 2026 | [링크](https://zylos.ai/research/2026-01-19-llm-context-management) | blog | 2026-01 | [C] |
| <a id="ref-g-11"></a>G-11 | Particula Tech — LangGraph vs CrewAI vs OpenAI Agents SDK 2026 | [링크](https://particula.tech/blog/langgraph-vs-crewai-vs-openai-agents-sdk-2026) | blog | 2026-02 | [B] |
| <a id="ref-g-12"></a>G-12 | Microsoft Foundry Blog — Agent Framework RC | [링크](https://devblogs.microsoft.com/foundry/microsoft-agent-framework-reaches-release-candidate/) | news | 2026-02-19 | [A] |
| <a id="ref-g-13"></a>G-13 | Google Cloud Blog — A2A Protocol Upgrade | [링크](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade) | news | 2026 | [A] |
| <a id="ref-g-14"></a>G-14 | Keepler — The era of the Agentic Mesh | [링크](https://keepler.io/2026/01/29/the-era-of-the-agentic-mesh/) | blog | 2026-01 | [B] |
| <a id="ref-g-15"></a>G-15 | CrewAI Changelog — MCP first-class support | [링크](https://docs.crewai.com/en/changelog) | docs | 2026-02-26 | [A] |
| <a id="ref-g-16"></a>G-16 | Flowful AI — Why 2026 is the Year of the Voice Agent | [링크](https://flowful.ai/blog/voice-agents-2026/) | blog | 2026 | [B] |
| <a id="ref-g-17"></a>G-17 | Viirtue — Enterprise AI Voice Agent Platforms for Teams 2026 | [링크](https://viirtue.com/top-4-enterprise-ai-voice-agent-platforms-for-voip-and-microsoft-teams-calling-in-2026/) | blog | 2026 | [C] |
| <a id="ref-g-18"></a>G-18 | LangChain Blog — Plan-and-Execute Agents | [링크](https://blog.langchain.com/planning-agents/) | blog | 2025 | [B] |
| <a id="ref-g-19"></a>G-19 | METR — Time Horizon 1.1 | [링크](https://metr.org/blog/2026-1-29-time-horizon-1-1/) | news | 2026-01-29 | [A] |
| <a id="ref-g-20"></a>G-20 | VentureBeat — Microsoft retires AutoGen, debuts Agent Framework | [링크](https://venturebeat.com/ai/microsoft-retires-autogen-and-debuts-agent-framework-to-unify-and-govern) | news | 2026 | [B] |
| <a id="ref-g-21"></a>G-21 | MarkTechPost — Google DeepMind Intelligent AI Delegation | [링크](https://www.marktechpost.com/2026/02/15/google-deepmind-proposes-new-framework-for-intelligent-ai-delegation-to-secure-the-emerging-agentic-web-for-future-economies/) | news | 2026-02-15 | [B] |
| <a id="ref-g-22"></a>G-22 | TechCrunch — Anthropic Opus 4.6 with Agent Teams | [링크](https://techcrunch.com/2026/02/05/anthropic-releases-opus-4-6-with-new-agent-teams/) | news | 2026-02-05 | [B] |
| <a id="ref-g-23"></a>G-23 | GitHub — langchain-ai/deepagents | [링크](https://github.com/langchain-ai/deepagents) | code | 2026 | [B] |
| <a id="ref-g-24"></a>G-24 | Data Nucleus — Agentic RAG Enterprise Guide 2026 | [링크](https://datanucleus.dev/rag-and-agentic-ai/agentic-rag-enterprise-guide-2026) | blog | 2026 | [B] |
| <a id="ref-g-25"></a>G-25 | Google — Adaptive Benchmarks for RAG on Vertex AI | [링크](https://discuss.google.dev/t/introducing-adaptive-benchmarks-for-evaluating-your-rag-systems-on-vertex-ai/318189) | news | 2026 | [A] |
| <a id="ref-g-26"></a>G-26 | OpenAI — New tools for building agents (Responses API) | [링크](https://openai.com/index/new-tools-for-building-agents/) | news | 2025-03 | [A] |
| <a id="ref-g-27"></a>G-27 | Anthropic — Contextual Retrieval | [링크](https://www.anthropic.com/news/contextual-retrieval) | news | 2024 | [A] |
| <a id="ref-g-28"></a>G-28 | AWS — Agentic RAG pipeline with SageMaker AI | [링크](https://aws.amazon.com/blogs/machine-learning/automate-advanced-agentic-rag-pipeline-with-amazon-sagemaker-ai/) | news | 2026 | [A] |
| <a id="ref-g-29"></a>G-29 | Fish Audio — Ultimate Voice Agents Guide 2026 | [링크](https://fish.audio/blog/ultimate-voice-agents-guide-2026/) | blog | 2026 | [B] |
| <a id="ref-g-30"></a>G-30 | NVIDIA — Voice Agent with RAG and Safety Guardrails | [링크](https://developer.nvidia.com/blog/how-to-build-a-voice-agent-with-rag-and-safety-guardrails/) | news | 2026-01 | [A] |
| <a id="ref-g-31"></a>G-31 | kore.ai — Corrective RAG (CRAG) | [링크](https://www.kore.ai/blog/corrective-rag-crag) | blog | 2026 | [B] |
| <a id="ref-p-01"></a>P-01 | Zhang et al. — ACE: Evolving Contexts for Self-Improving LMs | [링크](https://arxiv.org/abs/2510.04618) | paper | ICLR 2026 | [A] |
| <a id="ref-p-02"></a>P-02 | Microsoft Research — CORPGEN | [링크](https://arxiv.org/abs/2602.14229) | paper | 2026-02 | [A] |
| <a id="ref-p-03"></a>P-03 | Codified Context: Infrastructure for AI Agents | [링크](https://arxiv.org/html/2602.20478v1) | paper | 2026-02 | [B] |
| <a id="ref-p-04"></a>P-04 | Yu — AdaptOrch: Task-Adaptive Multi-Agent Orchestration | [링크](https://arxiv.org/abs/2602.16873) | paper | 2026-02 | [A] |
| <a id="ref-p-05"></a>P-05 | Adimulam et al. — Orchestration of Multi-Agent Systems | [링크](https://arxiv.org/abs/2601.13671) | paper | 2026-01 | [A] |
| <a id="ref-p-06"></a>P-06 | Li et al. — HiPlan: Hierarchical Planning | [링크](https://arxiv.org/abs/2508.19076) | paper | 2025-08 | [B] |
| <a id="ref-p-07"></a>P-07 | Chang et al. — SagaLLM | [링크](https://arxiv.org/abs/2503.11951) | paper | VLDB 2026 | [A] |
| <a id="ref-p-08"></a>P-08 | ReAcTree: Hierarchical LLM Agent Trees | [링크](https://arxiv.org/abs/2511.02424) | paper | ICLR 2026 | [A] |
| <a id="ref-p-09"></a>P-09 | Tomašev et al. — Intelligent AI Delegation | [링크](https://arxiv.org/abs/2602.11865) | paper | 2026-02 | [B] |
| <a id="ref-p-10"></a>P-10 | Ayanami et al. — A-RAG: Hierarchical Retrieval Interfaces | [링크](https://arxiv.org/abs/2602.03442) | paper | 2026-02 | [A] |
| <a id="ref-p-11"></a>P-11 | Salesforce — VoiceAgentRAG: Dual-Agent Architecture | [링크](https://arxiv.org/abs/2603.02206) | paper | 2026-03 | [A] |
| <a id="ref-p-12"></a>P-12 | Higress-RAG: Enterprise RAG Optimization | [링크](https://arxiv.org/abs/2602.23374) | paper | 2026-02 | [A] |
