---
type: weekly-research
domain: agentic-ai
l3: agent-planning
date: 2026-03-09
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
---

# Agent Planning — 심층 리서치 (2026-03-09)

## 기술 동향

Agent Planning 분야는 2026년 들어 세 가지 축으로 빠르게 수렴 중이다.

**Planner-Worker 분리 아키텍처의 정착**

Plan-and-Execute 패턴이 산업 표준으로 자리 잡고 있다. Planner LLM이 목표를 전체 계획(DAG 또는 리스트)으로 분해하고, Executor/Worker는 계획 단계를 원자적으로 실행하는 구조다 [[G-04]](#ref-g-04). 이 구조는 (1) 큰 모델을 계획에만 투입하고 하위 태스크는 경량 모델로 처리하는 비용 최적화, (2) 계획과 실행 간 명확한 감사 경로 확보, (3) 태스크 실패 시 재계획(replanning) 격리라는 세 가지 이점을 제공한다 [[G-04]](#ref-g-04).

**계층적 계획의 부상: HiPlan**

HiPlan(Li et al., 2025)은 글로벌 마일스톤 가이드(macro)와 단계별 힌트(micro)를 결합하는 계층적 계획 프레임워크다 [[P-01]](#ref-p-01). 오프라인 단계에서 전문가 시연으로 마일스톤 라이브러리를 구축하고, 실행 시 의미적으로 유사한 태스크와 마일스톤을 검색(RAG 방식)하여 구조화된 가이던스를 제공한다. 이 "검색 보강 마일스톤 라이브러리"는 장기 태스크에서 발생하는 로컬 최적 함정과 방향 이탈 문제를 완화한다.

**트랜잭셔널 보장: SagaLLM**

SagaLLM(Chang et al., 2025)은 분산 시스템의 Saga 트랜잭션 패턴을 LLM 계획에 적용한 프레임워크로, VLDB 2026에 게재되었다 [[P-02]](#ref-p-02). 핵심 구성 요소는 다음과 같다:
- `GlobalValidationAgent`: 전체 시스템 상태에 접근하는 중앙 검증 권한
- `SagaCoordinatorAgent`: 트랜잭션 시퀀싱·의존성 추적·보상 조율 담당
- 엄격한 ACID는 완화하되, 모듈식 체크포인팅과 보상 가능한 실행(compensable execution)으로 워크플로우 일관성을 보장한다 [[P-02]](#ref-p-02)

**계층적 트리 탐색: ReAcTree**

ReAcTree(2025, ICLR 2026 게재)는 ReAct 패턴을 계층적 트리 구조로 확장한다 [[P-03]](#ref-p-03). 복잡한 목표를 동적으로 구성된 에이전트 트리 내 서브 목표로 분해하고, 에피소딕 메모리(사례 검색)와 워킹 메모리(환경 관찰 공유)의 이중 메모리 시스템을 탑재한다. WAH-NL 벤치마크에서 61% 목표 성공률로 ReAct(31%)의 2배 달성 [[P-03]](#ref-p-03).

**미해결 과제: 컨텍스트 윈도우 일관성**

컨텍스트 윈도우의 약 60% 초과 시 출력 품질이 저하되는 "Context Rot" 현상이 확인되었다 [[G-10]](#ref-g-10). 크로스 컨텍스트 윈도우 일관성 유지가 장기 실행 에이전트의 핵심 미해결 과제로 부각되고 있으며, SagaLLM의 체크포인팅, Mem0의 동적 메모리 압축 등이 부분적 해법으로 등장했다 [[G-10]](#ref-g-10).

---

## 플레이어 동향

**주요 플레이어 동향**

| 기업 | 동향 | 출처 |
|------|------|------|
| Microsoft | AutoGen과 Semantic Kernel을 통합하는 **Microsoft Agent Framework** RC 출시 (2026-02-19). 그래프 기반 멀티 에이전트 워크플로우, 세션 기반 상태 관리, 미들웨어·텔레메트리 포함. GA 목표: 2026 Q1 말. AutoGen은 신규 기능 추가 없이 유지보수 전환 | [[G-05]](#ref-g-05) |
| Google DeepMind | **Intelligent AI Delegation** 프레임워크 발표(2026-02-12, arXiv). Contract-First Decomposition 도입: 검증 불가능한 태스크 위임 금지, 재귀적 서브태스크 분해 강제. 5개 핵심 기둥(동적 평가, 적응적 실행, 구조적 투명성, 확장 가능 마켓, 시스템 회복력) 정의 | [[G-06]](#ref-g-06) |
| Anthropic | **Claude Opus 4.6** 출시(2026-02-05). 14.5시간 태스크 완료 시간 지평으로 당시 최장 기록. **Agent Teams** 기능(멀티 에이전트 병렬 협업) 및 **Cowork** 제품(비개발자 대상 반자율 에이전트) 출시. 계획 수립 후 주요 단계에서 사용자 승인 요청하는 투명한 플로우 채택 | [[G-08]](#ref-g-08) [[G-09]](#ref-g-09) |
| LangChain | **Deep Agents**(LangGraph 기반) 공개. 내장 `write_todos` 툴로 태스크 자동 분해·추적, 가상 파일시스템 기반 메모리, 서브에이전트 스폰 지원. LangGraph 안정 semver 릴리스 완료, 프로덕션 환경 운용 중 | [[G-07]](#ref-g-07) |
| CrewAI | `planning=True` 플래그 하나로 AgentPlanner 활성화. 이터레이션 전 step-by-step 플랜을 각 태스크 설명에 주입. 기본 플래너 모델로 gpt-4o-mini 사용 | [[G-11]](#ref-g-11) |

---

## 시장 시그널

- **METR 시간 지평 지표**: 에이전트가 50% 신뢰도로 완료하는 코딩 태스크 시간이 7개월마다 2배 증가. 2026년 2월 현재 14.5시간 수준 달성 [[G-01]](#ref-g-01) [[G-02]](#ref-g-02)
- **가속 국면 신호**: 2024-2025 구간은 4개월마다 2배로 더 빠른 증가세. 이 추세 유지 시 2026년 말 주간 단위 자율 태스크 도달 예측 [[G-02]](#ref-g-02)
- **실패율 증가 문제**: 태스크 시간 2배 시 실패율은 4배 증가. 장기 태스크 신뢰성 확보가 상용화의 핵심 병목으로 부상 [[G-01]](#ref-g-01)
- **프레임워크 통합 가속**: AutoGen→Microsoft Agent Framework, LangGraph stable, CrewAI production-grade 등 도구 생태계가 프로덕션 단계로 이행 [[G-05]](#ref-g-05) [[G-07]](#ref-g-07)
- **검증 우선 설계로 패러다임 이동**: Google DeepMind Contract-First Decomposition이 대표하듯, "어떻게 계획할 것인가"에서 "어떻게 계획을 검증할 것인가"로 관심 이동 [[G-06]](#ref-g-06)
- **엔터프라이즈 채택 본격화**: Microsoft Agent Framework의 엔터프라이즈 인증, CrewAI 상업용 클라우드 플랫폼 등 B2B 상용화 경로가 구체화 [[G-05]](#ref-g-05)

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| HiPlan: Hierarchical Planning for LLM Agents with Adaptive Global-Local Guidance (Li et al., 2025) | 글로벌 마일스톤 + 로컬 스텝 힌트 이중 계층 구조. 전문가 시연 기반 마일스톤 라이브러리 구축 후 RAG로 검색 보강. 장기 태스크에서 로컬 최적 함정 회피 | [[P-01]](#ref-p-01) |
| SagaLLM: Context Management, Validation, and Transaction Guarantees for Multi-Agent LLM Planning (Chang et al., 2025) | Saga 트랜잭션 패턴 적용, GlobalValidationAgent + SagaCoordinatorAgent 이중 에이전트 구조. 모듈식 체크포인팅과 보상 실행으로 워크플로우 일관성 보장. VLDB 2026 게재 | [[P-02]](#ref-p-02) |
| ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning (2025) | ReAct를 계층적 동적 트리로 확장. 에피소딕+워킹 이중 메모리. WAH-NL 벤치마크 61% 성공률(ReAct 31% 대비 2배). 2026-02-10 최종 업데이트 | [[P-03]](#ref-p-03) |
| Intelligent AI Delegation (Tomašev et al., 2026) | Contract-First Decomposition: 검증 불가능한 태스크 위임 금지 원칙. 태스크 분해 vs. 위임의 개념적 구분 정립. 책임·신뢰·권한 계층화 프레임워크 | [[P-04]](#ref-p-04) |

---

## 전략적 시사점

**기회**

- Planner-Worker 분리와 계층적 계획이 표준 패턴으로 정착하는 시점에 해당 아키텍처 기반 사내 에이전트 플랫폼 구축 기회 존재
- SagaLLM의 트랜잭셔널 보장 패턴은 금융·통신 등 규제 산업의 장기 자율 워크플로우 적용에 직접 활용 가능
- METR 시간 지평 지표 기준 14.5시간 → 주간 태스크로의 전환이 1~2년 내 예상되므로, 지금부터 장기 태스크 오케스트레이션 역량 선제 확보가 유효
- Google DeepMind의 Contract-First Decomposition은 AI 에이전트 감사·거버넌스 요건이 강화되는 추세에 부합하는 설계 원칙으로 활용 가능

**위협**

- Context Rot(컨텍스트 60% 초과 시 성능 저하)은 장기 실행 에이전트의 신뢰성 확보를 구조적으로 어렵게 만들며, 해결책이 아직 부분적 수준
- 태스크 시간 2배 증가 시 실패율 4배 증가 법칙은 에이전트 기반 자동화의 SLA 보장을 어렵게 하며 운영 리스크 증가
- Microsoft Agent Framework, LangGraph, CrewAI 등 빅테크·오픈소스 플랫폼의 빠른 성숙으로 자체 프레임워크 개발보다 플랫폼 선택·통합 능력이 더 중요해지는 구조로 전환
- 검증 우선 패러다임 전환으로 계획 알고리즘뿐 아니라 독립 검증 에이전트 설계 역량도 필수 요소로 부상

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- METR 시간 지평 지표 (METR 공식 블로그, 독립 검증 복수 소스)
- SagaLLM 실험 결과 (VLDB 2026 peer-reviewed 논문)
- ReAcTree 벤치마크 수치 (arXiv + OpenReview 공개)
- Microsoft Agent Framework RC 출시 사실 (공식 발표)

**추가 검증 필요 [C/D]:**
- HiPlan 구체적 성능 수치 (arXiv 프리프린트, peer review 미완료)
- "4개월마다 2배" 가속 추세 지속 여부 (단기 관측, 추세 전환 가능성)
- Claude Opus 4.6의 14.5시간 수치 (Anthropic 자체 측정, 독립 검증 미확인)

**데이터 공백:**
- HiPlan 대비 정량적 벤치마크 비교 (다른 계층적 계획 프레임워크 대비 우위 미검증)
- CrewAI Enterprise의 실제 프로덕션 성능 지표 (공개 정보 없음)
- 국내 통신사(SKT/KT) Agent Planning 기술 내재화 현황

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | AI Digest — A new Moore's Law for AI agents | [링크](https://theaidigest.org/time-horizons) | news | 2026 | [B] |
| <a id="ref-g-02"></a>G-02 | Medium (Shivam) — Task length doubling every 7 months | [링크](https://medium.com/@shivam-b/be-ready-the-length-of-tasks-that-ai-agents-can-complete-with-50-reliability-has-been-doubling-f29257d63048) | blog | 2026-02 | [C] |
| <a id="ref-g-03"></a>G-03 | METR — Time Horizon 1.1 (2026-01-29) | [링크](https://metr.org/blog/2026-1-29-time-horizon-1-1/) | news | 2026-01-29 | [A] |
| <a id="ref-g-04"></a>G-04 | LangChain Blog — Plan-and-Execute Agents | [링크](https://blog.langchain.com/planning-agents/) | blog | 2025 | [B] |
| <a id="ref-g-05"></a>G-05 | VentureBeat — Microsoft retires AutoGen, debuts Agent Framework | [링크](https://venturebeat.com/ai/microsoft-retires-autogen-and-debuts-agent-framework-to-unify-and-govern) | news | 2026 | [B] |
| <a id="ref-g-06"></a>G-06 | MarkTechPost — Google DeepMind Intelligent AI Delegation | [링크](https://www.marktechpost.com/2026/02/15/google-deepmind-proposes-new-framework-for-intelligent-ai-delegation-to-secure-the-emerging-agentic-web-for-future-economies/) | news | 2026-02-15 | [B] |
| <a id="ref-g-07"></a>G-07 | GitHub — langchain-ai/deepagents | [링크](https://github.com/langchain-ai/deepagents) | blog | 2026 | [B] |
| <a id="ref-g-08"></a>G-08 | TechCrunch — Anthropic releases Opus 4.6 with agent teams | [링크](https://techcrunch.com/2026/02/05/anthropic-releases-opus-4-6-with-new-agent-teams/) | news | 2026-02-05 | [B] |
| <a id="ref-g-09"></a>G-09 | Anthropic — Measuring agent autonomy | [링크](https://www.anthropic.com/research/measuring-agent-autonomy) | news | 2026 | [A] |
| <a id="ref-g-10"></a>G-10 | LogRocket Blog — LLM context problem in 2026 | [링크](https://blog.logrocket.com/llm-context-problem/) | blog | 2026 | [B] |
| <a id="ref-g-11"></a>G-11 | CrewAI Docs — Planning | [링크](https://docs.crewai.com/en/concepts/planning) | blog | 2026 | [B] |
| <a id="ref-g-12"></a>G-12 | Microsoft Learn — Agent Framework Overview | [링크](https://learn.microsoft.com/en-us/agent-framework/overview/) | news | 2026 | [A] |
| <a id="ref-g-13"></a>G-13 | Semantic Kernel Blog — Migrate to Agent Framework RC | [링크](https://devblogs.microsoft.com/semantic-kernel/migrate-your-semantic-kernel-and-autogen-projects-to-microsoft-agent-framework-release-candidate/) | news | 2026-02-19 | [A] |
| <a id="ref-p-01"></a>P-01 | Li et al. — HiPlan: Hierarchical Planning for LLM Agents with Adaptive Global-Local Guidance | [링크](https://arxiv.org/abs/2508.19076) | paper | 2025-08-26 | [B] |
| <a id="ref-p-02"></a>P-02 | Chang et al. — SagaLLM: Context Management, Validation, and Transaction Guarantees for Multi-Agent LLM Planning | [링크](https://arxiv.org/abs/2503.11951) | paper | 2025-03 | [A] |
| <a id="ref-p-03"></a>P-03 | ReAcTree: Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning | [링크](https://arxiv.org/abs/2511.02424) | paper | 2025-11 | [A] |
| <a id="ref-p-04"></a>P-04 | Tomašev et al. — Intelligent AI Delegation (arXiv:2602.11865) | [링크](https://arxiv.org/abs/2602.11865) | paper | 2026-02-12 | [B] |
