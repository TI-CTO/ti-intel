---
type: deep-research
parent: weekly-monitor
domain: agentic-ai
l3: agent-orchestration
date: 2026-04-02
week: W16
signal: 🟡 주목
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
---

# Deep Research: Intelligent Agent Orchestration (W16)
**기간: 2026-03-26 ~ 2026-04-02**

---

## Executive Summary

이번 주 Intelligent Agent Orchestration (IAO) 분야는 **프로토콜 완성 → 런타임 거버넌스 성숙** 전환 기조를 뚜렷하게 확인할 수 있었다. OpenAI Agents SDK 0.13.3~0.13.4(3/31~4/1)가 MCP 리소스 API와 RealtimeRunner Session Initiation Protocol (SIP) 지원을 추가하고, AWS AgentCore Evaluations(3/31 GA)·Microsoft Agent Framework .NET RC5(4/1)가 잇따라 출하되었다. MCP Dev Summit (Linux Foundation 주관, 4/2~3 NYC)이 오늘 개막하여 Auth·Observability·수평 확장 등 프로덕션 격차를 집중 논의한다. AG-UI(Agent-User Interaction Protocol)라는 신규 프로토콜이 AWS AgentCore(3/13)·Microsoft Agent Framework·Oracle에 채택되며 MCP/A2A와 함께 3대 에이전트 프로토콜 스택을 형성하고 있다. 전반적 신뢰도는 [A]~[B] 수준이며, 7일 이내 공식 발표 기반으로 작성되었다.

---

## 연구 질문

> 2026-03-26~04-02 기간 내 IAO 분야에서 발생한 기술/제품/시장 시그널을 식별하고, W15 대비 새로운 변화 방향을 분석한다. 특히 프로토콜 표준화 이후 거버넌스·런타임 효율화 단계 전환 여부를 검토한다.

---

## 기술 동향

1. **OpenAI Agents SDK 0.13.3 (3/31) & 0.13.4 (4/1) — MCP 리소스 API 공개, RealtimeRunner SIP 지원.**
   0.13.3(3/31)은 서버 대화 추적기의 stale hydrated 입력 ID 해소, raw `image_url` 콘텐츠 파트 수용, 비OpenAI 공급자 문서 개선을 포함한다. 0.13.4(4/1)는 AnyLLM 응답 재생 입력 검증 전처리 추가, feature label 매핑 수정이 주 내용이다 [[G-01]](#ref-g-01). 별도로, 0.13.0에서 이미 추가된 MCPServer에 `list_resources()`, `list_resource_templates()`, `read_resource()` 메서드가 이번 주 문서화·안정화되었고, RealtimeRunner에 SIP attach flow(`OpenAIRealtimeSIPModel`)가 추가되어 전화 에이전트 시나리오(Realtime Calls API → `call_id` 연결)를 공식 지원한다 [[G-02]](#ref-g-02). W15의 WebSocket transport 기반(0.13.2) 위에 리소스 조회·음성통화 바인딩이 추가되는 형태다.

2. **Microsoft Agent Framework .NET RC5 (4/1) — 영속 워크플로우·MCP 도구 노출 추가.**
   `dotnet-1.0.0-rc5`(4/1 릴리스)는 .NET에 durable workflow 지원, Azure Functions 호스팅 시 워크플로우를 MCP 도구로 노출, 에이전트 스킬 다중 소스 아키텍처(breaking change), 인라인 스킬 API, 관찰성 강화를 포함한다. `ReasoningEncryptedContent`가 기본 포함으로 변경되었고, Python RC는 W15(3/20 RC5) 이후 추가 릴리스 미확인 상태다 [[G-03]](#ref-g-03). GA 발표는 이번 주 기준 미발생 — GA는 Q1 말(3월 말) 목표였으나 .NET RC5로 보아 Q2 초 실현 가능성이 높다 [추가확인 필요].

3. **LangGraph 1.1 출시 (3월) — 타입 안전 스트리밍·Pydantic 강제 변환.**
   LangGraph v1.1은 `stream()·astream()`에 `version="v2"` 파라미터를 추가하여 타입 안전 스트리밍(StreamPart 통합 출력)·타입 안전 invoke(GraphOutput 객체)를 도입했다. Pydantic 모델·데이터클래스에 대한 자동 강제 변환도 포함하며, 하위 호환성을 유지(`version="v2"` 옵트인 방식)한다 [[G-04]](#ref-g-04). LangSmith Sandboxes(3/17 Private Preview)는 에이전트가 실행하는 코드를 하드웨어 가상화 microVM으로 격리하여 커널 수준 보안을 확보한다. Authentication Proxy가 외부 서비스 호출을 라우팅하여 시크릿이 런타임에 노출되지 않도록 설계되었다. LangSmith 3월 뉴스레터 발표에 따르면 LangChain 내부 GTM 에이전트 활용 결과 리드-퀄리파이드 상담 전환율이 250% 향상되었다고 보고했다 [[G-05]](#ref-g-05).

4. **AWS AgentCore Evaluations GA (3/31) & AG-UI 프로토콜 지원 (3/13) — 품질 평가·UI 연동 표준화.**
   AgentCore Evaluations(3/31 GA)는 온라인(프로덕션 트래픽 상시 모니터링)·온디맨드(CI/CD 통합 테스트) 2가지 평가 유형, 13개 내장 평가기(응답 품질·안전·태스크 완료·도구 사용), 커스텀 Python/JavaScript Lambda 평가기를 제공한다. 9개 AWS 리전에 제공되며 AgentCore Observability와 통합된다 [[G-06]](#ref-g-06). AG-UI 프로토콜 지원(3/13)은 별도 시그널로, AgentCore Runtime이 에이전트-UI 간 실시간 스트리밍 표준 프로토콜(SSE·WebSocket)을 채택한 것이다 [[G-07]](#ref-g-07).

5. **AG-UI 프로토콜 — 에이전트-UI 상호작용 표준화 가속.**
   CopilotKit이 제안한 AG-UI(Agent-User Interaction Protocol)는 에이전트가 프런트엔드 애플리케이션과 통신하는 방식을 표준화하는 오픈 이벤트 기반 프로토콜이다. 텍스트 청크·추론 단계·도구 결과를 프런트엔드로 실시간 스트리밍하고, 진행 표시줄·대시보드 등 UI 요소를 에이전트가 직접 업데이트할 수 있다 [[G-08]](#ref-g-08). AWS(3/13), Microsoft Agent Framework, Oracle, Google이 채택하면서 MCP(도구 컨텍스트)·A2A(에이전트 간 통신)·AG-UI(에이전트-사용자 인터페이스)로 구성되는 3대 에이전트 프로토콜 스택 구도가 뚜렷해졌다 [[G-09]](#ref-g-09).

6. **MCP Dev Summit 개막 (4/2~3, NYC) — 프로덕션 격차 논의 공식화.**
   Linux Foundation Agentic AI Foundation (AAIF) 주관으로 오늘(4/2) 개막한 MCP Dev Summit North America는 근 50명 연사(Anthropic, OpenAI, Google, Docker, Datadog 등)가 참여하는 최대 규모 MCP 커뮤니티 행사다 [[G-10]](#ref-g-10). 심층 기술 세션은 ① 엔터프라이즈 MCP 확장, ② 보안 오케스트레이션, ③ 에이전트 시스템 관찰성, ④ 엔터프라이즈 통합 패턴에 집중한다. MCP 월간 SDK 다운로드 9,700만 건(론칭 16개월 만에 4,750% 성장) 배경 하에, 2026 로드맵은 Auth·Observability·HTTP transport 수평 확장을 핵심 과제로 설정했다 [[G-11]](#ref-g-11).

7. **Anthropic Claude Haiku 3 deprecated 예고 (4/20 은퇴) — 오케스트레이션 런타임 마이그레이션 영향.**
   Anthropic이 `claude-3-haiku-20240307`의 은퇴일을 4월 20일로 확정했다. 대체 모델은 `claude-haiku-4-5-20251001`이다 [[G-12]](#ref-g-12). 별도로, Sonnet 4.5·Sonnet 4의 1M 컨텍스트 윈도우 베타 헤더(`context-1m-2025-08-07`)가 4/30 이후 효력 상실된다 — 이후 1M 컨텍스트 사용은 Sonnet 4.6 또는 Opus 4.6으로 마이그레이션이 필요하다 [[G-12]](#ref-g-12). 에이전트 오케스트레이션에서 서브에이전트 모델을 Haiku 3로 사용하는 팀은 즉시 대응이 필요하다.

8. **CrewAI 0.175.0 (3/25) — Qdrant Edge 메모리·에이전트 스킬·네이티브 OpenAI 호환 공급자.**
   Qdrant Edge 스토리지 백엔드로 메모리 시스템 로컬 실행이 가능해졌다. 에이전트 스킬 기능, 계층형 메모리 격리를 위한 `root_scope` 자동 설정, OpenRouter·DeepSeek·Ollama·vLLM·Cerebras·Dashscope를 네이티브 OpenAI 호환 공급자로 지원한다. HITL(Human-In-The-Loop) 플로우 버그 다수 수정이 포함되었다 [[G-13]](#ref-g-13).

---

## 플레이어 동향

**주요 플레이어 동향**

| 기업 | 동향 | 출처 |
|------|------|------|
| OpenAI | Agents SDK 0.13.3(3/31): stale ID 버그 수정, 0.13.4(4/1): AnyLLM 재생 입력 검증; MCPServer 리소스 API·RealtimeRunner SIP 안정화 | [[G-01]](#ref-g-01), [[G-02]](#ref-g-02) |
| Microsoft | Agent Framework .NET RC5(4/1): durable workflow·MCP 도구 노출·인라인 스킬; GA는 Q2 초 예상 [추가확인 필요]; Foundry Agent Service GA(3/16): BYO VNet·Voice Live·평가 GA | [[G-03]](#ref-g-03), [[E-01]](#ref-e-01) |
| LangChain | LangGraph 1.1 타입 안전 스트리밍; LangSmith Sandboxes(3/17 Private Preview) microVM 격리; Polly AI 어시스턴트 GA; ABAC·감사 로그; GTM 에이전트 전환율 250%↑ | [[G-04]](#ref-g-04), [[G-05]](#ref-g-05) |
| AWS | AgentCore Evaluations GA(3/31): 13개 내장 평가기·온라인/온디맨드 평가; AG-UI 지원(3/13); 관리형 세션 스토리지 Preview; WebRTC 지원; Step Functions 통합 | [[G-06]](#ref-g-06), [[G-07]](#ref-g-07) |
| Anthropic | Claude Haiku 3 은퇴(4/20), Sonnet 4.5·4의 1M 컨텍스트 베타 종료(4/30); Opus 4.6 에이전트 팀 기능 활성 유지; MCP Dev Summit 공동 주최 | [[G-12]](#ref-g-12), [[E-02]](#ref-e-02) |
| Google | A2A v0.3 gRPC·카드 서명·SDK 확장 안정화 진행 중; MCP Dev Summit 참여(플래티넘 AAIF 회원) | [[G-14]](#ref-g-14) |
| CrewAI | v0.175.0(3/25): Qdrant Edge 메모리·에이전트 스킬·OpenAI 호환 6개 공급자; HITL 버그 수정; 월 4.5억 워크플로우 실행 | [[G-13]](#ref-g-13) |
| CopilotKit | AG-UI 오픈 프로토콜 주도; AWS·Microsoft·Oracle·Google 채택으로 MCP/A2A와 함께 3대 프로토콜 스택 형성 | [[G-08]](#ref-g-08), [[G-09]](#ref-g-09) |

---

## 시장 시그널

**투자 & M&A**

- Tracxn 기준 에이전트 AI 섹터 총 펀딩 $186억, 2023년 이후 연 60%+ 성장률 지속; 에이전트 인에이블러(플랫폼·오케스트레이션 레이어)가 총 투자의 55%+ 차지 [[G-15]](#ref-g-15)
- Automation Anywhere 섹터 최대 펀딩액 $840M [[G-15]](#ref-g-15)

**파트너십 & 제휴**

- Microsoft Foundry Agent Service — Responses API 기반 런타임, OpenAI 에이전트와 wire-compatible 설계로 다중 공급자 전략 확정 [[E-01]](#ref-e-01)
- AG-UI 프로토콜 — Oracle, Google, CopilotKit 공동 통합 발표; AWS AgentCore·Microsoft Agent Framework 채택으로 프런트엔드 표준화 가속 [[G-09]](#ref-g-09)
- MCP Dev Summit — Duolingo(180개 MCP 도구 Slack봇), Docker(MCP Platform 전략), Datadog(엔터프라이즈 에이전트 가관찰성) 등 실사용 기업 참여 [[G-10]](#ref-g-10)

**시장 전망**

- Deloitte 2026 TMT 예측: 에이전트 AI 시장 2026년 $85억 → 2030년 $350억 전망; 오케스트레이션 거버넌스 개선 시 최대 30% 업사이드 [[G-16]](#ref-g-16)
- BCG: 에이전트 AI로 Tech Services TAM 향후 5년간 최대 $2,000억 순증, CAGR 6~8% [[G-17]](#ref-g-17)
- Gartner: 2026년 말까지 엔터프라이즈 애플리케이션의 40%에 태스크별 AI 에이전트 내장 전망 [[G-18]](#ref-g-18)
- 현재 42% 기업이 에이전트 AI 프로덕션 단계, 72%가 프로덕션+파일럿 병행 운영 [[G-18]](#ref-g-18)

**도입 사례**

- LangChain 내부 GTM 에이전트: 리드-퀄리파이드 상담 전환율 250% 향상 (단일 소스) [[G-05]](#ref-g-05) [추가확인 필요]
- CrewAI Fortune 500 고객: IBM, PwC, DocuSign, PepsiCo, Johnson & Johnson; 월 4.5억 에이전트 워크플로우 처리 [[G-13]](#ref-g-13)
- Duolingo: MCP 도구 180개 통합 AI Slack봇 운영 (MCP Dev Summit 발표 예정) [[G-10]](#ref-g-10)

**연구 동향**

- 에이전트 오케스트레이션 평가 자동화 영역 급성장 — AgentCore Evaluations GA, Foundry 평가 GA가 동시 출하되며 "에이전트 품질 측정"이 프로덕션 필수 레이어로 정착
- 멀티에이전트 거버넌스("guardian agent" 아키텍처) 개념 확산 — 에이전트 스프롤 관리, 규정 준수 오케스트레이션을 단일 거버넌스 레이어가 담당하는 패턴 [[G-19]](#ref-g-19)
- 소형 언어 모델(SLM, Small Language Model) 기반 온디바이스 에이전트 실행으로 비용 70~85% 절감 사례 보고 [[G-19]](#ref-g-19)

**커뮤니티 시그널**

- MCP Dev Summit 4/2~3 NYC 개막 — Linux Foundation AAIF 주관 첫 대규모 공식 이벤트; 프로덕션 격차(Auth·Observability·서버 관리) 해소가 2026 로드맵 핵심 [[G-10]](#ref-g-10)
- MCP 월간 SDK 다운로드 9,700만 건(론칭 16개월, +4,750%) [[G-11]](#ref-g-11)
- AG-UI GitHub 저장소(`ag-ui-protocol/ag-ui`) 및 CopilotKit 커뮤니티 중심 빠른 확산 중 [[G-08]](#ref-g-08)

---

## 전략적 시사점

**기회**

- **3대 프로토콜 스택 조기 채택**: MCP(도구 컨텍스트)·A2A(에이전트 간 통신)·AG-UI(에이전트-사용자 인터페이스)가 동시 성숙하고 있다. 세 프로토콜을 모두 지원하는 오케스트레이션 계층을 선점하는 것이 2026년 인프라 차별화 포인트가 될 것이다.
- **에이전트 평가·관찰성 내재화**: AgentCore Evaluations GA, Foundry 평가 GA, LangSmith ABAC·감사 로그가 동시 출하되었다. 에이전트 품질 측정·감사 로그를 내재화하는 팀이 엔터프라이즈 신뢰성 검증에서 유리해진다.
- **에이전트 SIP/음성 연동 기회**: OpenAI RealtimeRunner SIP, Microsoft Voice Live Preview가 안정화 단계에 진입했다. 음성 에이전트와 기존 통신 인프라(SIP 트렁크)의 통합 시나리오가 현실화되고 있어, 통신사 관점에서 선행 검토 가치가 있다.
- **서브에이전트 모델 비용 최적화**: CrewAI의 Qdrant Edge·로컬 메모리 백엔드, 온디바이스 SLM(Small Language Model) 에이전트 실행이 가시화됨에 따라 클라우드 토큰 비용 70~85% 절감 아키텍처 설계가 가능해지고 있다.

**위협**

- **모델 은퇴 일정 압박**: Anthropic Claude Haiku 3(4/20 은퇴), Sonnet 4.5·4의 1M 컨텍스트 베타 종료(4/30)가 목전에 있다. 서브에이전트 모델로 Haiku 3를 사용하거나 대용량 컨텍스트 파이프라인을 구성한 경우 즉각 마이그레이션이 필요하다.
- **프로토콜 분화 리스크**: MCP·A2A·AG-UI·A2UI(Google) 등 표준 후보가 난립하고 있다. 특정 프로토콜에 강하게 결합된 아키텍처는 생태계 분화 리스크에 노출된다 — 추상화 레이어 설계가 필요하다.
- **에이전트 스프롤 거버넌스 공백**: 엔터프라이즈 에이전트 배포가 40%에 육박하는 가운데, 중앙화된 에이전트 레지스트리·감사 로그·ABAC 정책 없이 무분별한 에이전트 확산이 진행될 경우 규정 준수 및 보안 리스크가 증가한다.
- **Microsoft GA 지연 불확실성**: Agent Framework .NET RC5(4/1) 릴리스 이후에도 GA 미발표 상태다. AutoGen·Semantic Kernel 통합 체계에 의존하는 전략 계획의 타이밍 조정이 필요할 수 있다 [추가확인 필요].

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | GitHub — openai-agents-python Releases | [링크](https://github.com/openai/openai-agents-python/releases) | release | 2026-04-01 | [A] |
| <a id="ref-g-02"></a>G-02 | OpenAI Agents SDK — Release Changelog | [링크](https://openai.github.io/openai-agents-python/release/) | docs | 2026-04-01 | [A] |
| <a id="ref-g-03"></a>G-03 | GitHub — microsoft/agent-framework Releases | [링크](https://github.com/microsoft/agent-framework/releases) | release | 2026-04-01 | [A] |
| <a id="ref-g-04"></a>G-04 | LangChain Changelog — LangGraph 1.1 | [링크](https://docs.langchain.com/oss/python/releases/changelog) | release | 2026-03 | [A] |
| <a id="ref-g-05"></a>G-05 | LangChain Blog — March 2026 Newsletter | [링크](https://blog.langchain.com/march-2026-langchain-newsletter/) | blog | 2026-03-31 | [B] |
| <a id="ref-g-06"></a>G-06 | AWS — AgentCore Evaluations Generally Available | [링크](https://aws.amazon.com/about-aws/whats-new/2026/03/agentcore-evaluations-generally-available/) | release | 2026-03-31 | [A] |
| <a id="ref-g-07"></a>G-07 | AWS — AgentCore Runtime AG-UI Protocol Support | [링크](https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-bedrock-agentcore-runtime-ag-ui-protocol/) | release | 2026-03-13 | [A] |
| <a id="ref-g-08"></a>G-08 | CopilotKit — Introducing AG-UI Protocol | [링크](https://www.copilotkit.ai/blog/introducing-ag-ui-the-protocol-where-agents-meet-users) | blog | 2026-03 | [B] |
| <a id="ref-g-09"></a>G-09 | Medium — A2A, MCP, AG-UI, A2UI: The Essential 2026 AI Agent Protocol Stack | [링크](https://medium.com/@visrow/a2a-mcp-ag-ui-a2ui-the-essential-2026-ai-agent-protocol-stack-ee0e65a672ef) | blog | 2026-03 | [C] |
| <a id="ref-g-10"></a>G-10 | Linux Foundation Events — MCP Dev Summit North America | [링크](https://events.linuxfoundation.org/mcp-dev-summit-north-america/) | event | 2026-04-02 | [A] |
| <a id="ref-g-11"></a>G-11 | MCP Blog — MCP joins the Agentic AI Foundation | [링크](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/) | blog | 2025-12-09 | [A] |
| <a id="ref-g-12"></a>G-12 | Anthropic Docs — Model Deprecations | [링크](https://platform.claude.com/docs/en/about-claude/model-deprecations) | docs | 2026-04-02 | [A] |
| <a id="ref-g-13"></a>G-13 | CrewAI Community — Release 0.175.0 | [링크](https://community.crewai.com/t/new-release-0-175-0/6989) | release | 2026-03-25 | [B] |
| <a id="ref-g-14"></a>G-14 | Google Cloud Blog — Agent2Agent Protocol is Getting an Upgrade | [링크](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade) | blog | 2026-03 | [A] |
| <a id="ref-g-15"></a>G-15 | Tracxn — Agentic AI 2026 Market & Investment Trends | [링크](https://tracxn.com/d/sectors/agentic-ai/__oyRAfdUfHPjf2oap110Wis0Qg12Gd8DzULlDXPJzrzs) | report | 2026-03 | [B] |
| <a id="ref-g-16"></a>G-16 | Deloitte — Unlocking Exponential Value with AI Agent Orchestration | [링크](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/ai-agent-orchestration.html) | report | 2026-01 | [B] |
| <a id="ref-g-17"></a>G-17 | BCG — The $200 Billion Agentic AI Opportunity for Tech Service Providers | [링크](https://www.bcg.com/publications/2026/the-200-billion-dollar-ai-opportunity-in-tech-services) | report | 2026 | [B] |
| <a id="ref-g-18"></a>G-18 | Joget — AI Agent Adoption 2026: What the Data Shows (Gartner, IDC) | [링크](https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/) | report | 2026-03 | [B] |
| <a id="ref-g-19"></a>G-19 | AetherLink — Agentic AI & Multi-Agent Systems: Enterprise Governance in 2026 | [링크](https://aetherlink.ai/en/blog/agentic-ai-multi-agent-systems-enterprise-governance-in-2026) | blog | 2026-03 | [C] |
| <a id="ref-e-01"></a>E-01 | Microsoft Foundry Blog — Foundry Agent Service is GA | [링크](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/) | IR/발표 | 2026-03-16 | [A] |
| <a id="ref-e-02"></a>E-02 | Anthropic — Model Deprecation Commitments Update | [링크](https://www.anthropic.com/research/deprecation-updates-opus-3) | IR/발표 | 2026-02 | [A] |
