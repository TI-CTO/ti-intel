---
type: weekly-monitor
domain: agentic-ai
week: 2026-W16
date: 2026-04-02
l3_count: 12
deep_count: 1
---

# 주간 기술 동향: Agentic AI (2026-W16)

## Executive Summary

> **이번 주 핵심**: MCP Dev Summit(4/2-3 NYC)이 오늘 개막하면서 에이전트 프로토콜 생태계가 "표준화 완료 → 프로덕션 거버넌스" 단계로 본격 전환했다. MCP/A2A에 더해 AG-UI(Agent-User Interaction Protocol)가 AWS·Microsoft·Oracle·Google 4대 하이퍼스케일러에 동시 채택되어 3대 에이전트 프로토콜 스택이 형성. OpenAI SDK 0.13.3~4는 MCP 리소스 API와 RealtimeRunner SIP(Session Initiation Protocol)를 추가하고, AWS AgentCore Evaluations가 GA(3/31)로 "에이전트 품질 평가"를 프로덕션 필수 레이어로 정착시켰다.

| Layer 2 | 세부기술 | 신호 | 핵심 내용 |
|---------|----------|------|----------|
| Trusted Multi-Agent Orchestration | Intelligent Agent Orchestration | 🟡 | [생태계] MCP Dev Summit 개막(4/2-3 NYC), AG-UI 3대 프로토콜 스택 형성 · [제품출시] OpenAI SDK 0.13.3-4, AWS AgentCore Evaluations GA, MS AF .NET RC5 |
| | Agent Oriented Orchestration | 🟢 | Plan-and-Act 하이브리드 패턴 지배 유지, 신규 변화 없음 |
| Model & Delta Foundry | 하이브리드 GPU Orchestration | 🟢 | KubeCon 후속 정착, vMetal bare-metal AI 관리 등장 |
| | FeedbackOps: Meta-prompt Engineering | 🟢 | DSPy MIPROv2 안정, 신규 릴리스 없음 |
| | EvaluationOps: KMS (Knowledge Management System) 성능평가 | 🟢 | RAGAS+LLM-as-judge 생태계 안정 |
| | 데이터-학습-배포 파이프라인 | 🟢 | AgentOps 개념 부상 중, 구체적 신규 출시 없음 |
| Hybrid AI Infra | On-Device sLM | 🟢 | FunctionGemma 270M 디바이스 제어, Qwen 3.5 4B 등 정착 |
| | Edge AI | 🟢 | TI NPU 90x 저지연, 추론칩 $50B 전망, 정착 단계 |
| | 5G SA/6G (AI-RAN/SRv6) | 🟢 | P.I. Works-TELUS AI-RAN 파트너십(4/1), MWC 후속 정착 |
| | 실시간 화자분할(2인) | 🟢 | Voxtral Realtime sub-200ms, 안정 유지 |
| Self Evolving Architecture | Agentic Context Engineering | 🟢 | ACE(Agentic Context Engineering) ICLR 2026 생태계 성숙, 신규 발표 없음 |
| 의도 파악 기술 | Adaptive RAG | 🟢 | Router Pattern 표준화, Higress-RAG 확산 지속 |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음
> **태그** : [기술돌파] [제품출시] [경쟁사] [규제] [투자] [논문] [생태계]

---

## 🟢 Quick 요약 (변화 미미)

### Agent Oriented Orchestration
- Plan-and-Act 하이브리드 패턴(고추론 DAG 분해 → 경량 실행 → 재계획)이 엔터프라이즈 배포 주류 유지. Gartner: 2026년 말까지 엔터프라이즈 앱 40%에 태스크별 AI 에이전트 내장 전망. 이번 주 추가 변화 없음.

### GPU Orchestration
- KubeCon Europe(3/24) 후속 정착 단계. vCluster Labs가 vMetal(bare-metal GPU 관리 레이어) 출시하여 AI Factory 프로비저닝 자동화 시도. SkyPilot에 Agent Skills(GPU 접근·잡 관리) 추가(3월). KubeCon 발표들의 실 적용 기간.

### FeedbackOps (Meta-prompt Engineering)
- DSPy MIPROv2 옵티마이저 안정 운영 지속. 메타프롬프팅이 "프롬프트 엔지니어링의 기본 기법"으로 정착. Gartner: 2026년 엔터프라이즈 워크로드 80%+가 AI 시스템 활용 예상. 이번 주 신규 릴리스 없음.

### EvaluationOps (KMS(Knowledge Management System) 성능평가)
- LLM-as-judge 80-90% 인간 일치율 유지. RAGAS v0.2+ 에이전틱 워크플로우 평가 확장. 2026 신규 도구: Open Evals, EvalScope, W&B Eval. 이번 주 돌파구 없음.

### MLOps Pipeline
- MLOps→LLMOps→AgentOps 전환 가속 중. AgentOps(장기 실행·다단계 에이전트 관리) 개념이 차세대 운영 패러다임으로 부상하나 구체적 신규 제품 출시 없음. 30-40% 운영 효율 개선 보고(Intellibytes).

### On-Device sLM
- Google FunctionGemma 270M이 자연어 → 구조화 코드 변환 전문 모델로 디바이스 제어 영역 확대. Qwen 3.5 4B가 GPT-4o급 벤치마크. Gemma 3 1B 529MB가 모바일 GPU에서 2,585 tok/s 달성. sLM-First 아키텍처 60-70% 비용 절감 패턴 정착 지속.

### Edge AI
- TI TinyEngine NPU(Neural Processing Unit): 기존 MCU(Microcontroller Unit) 대비 90x 저지연, 120x 에너지 효율. 추론 최적화 칩 시장 $50B 전망(2026). 서브 1B 파라미터 모델이 실용 태스크 대응 가능 수준 도달. PoC→프로덕션 변곡점 지속.

### 5G SA/6G (AI-RAN/SRv6)
- P.I. Works-TELUS 파트너십(4/1): AI-RAN(AI-Radio Access Network) 자동화 5G SA 환경에서 실행. Open RAN이 AI-RAN의 전제조건이며, AI-RAN이 Open RAN 목표의 연장선. 3GPP 6G 스펙 2029년 목표. CSP(Communication Service Provider) 65%가 AI 팩토리 배포/시범 중.

### Speaker Diarization
- Mistral Voxtral Realtime: sub-200ms 저지연, $0.006/분. AssemblyAI Universal-3-Pro: 노이즈 환경 30% 개선, 프롬프트 다이어리제이션. pyannote 실시간 다이어리제이션 + LLM 통합 연구 진행. 돌파구 수준 변화 없음.

### Agentic Context Engineering
- ACE(ICLR 2026) 프레임워크: AppWorld 벤치마크 +17.1%, 적응 지연 86.9% 감소. MCE(Meta Context Engineering) 논문이 ACE 대비 5.6-53.8% 개선 보고. 프로덕션 적용 사례는 아직 없으며 생태계 성숙 지속.

### Adaptive RAG
- Router Pattern이 2026 표준으로 정착. Higress-RAG 프레임워크(2026.02): 적응적 라우팅 + 시맨틱 캐싱 + 듀얼 하이브리드 검색으로 엔터프라이즈 데이터셋 90%+ 리콜. Hybrid RAG가 프로덕션 베이스라인, Adaptive/Self-RAG가 비용·지연·신뢰성 동적 최적화.

---

## 🟡🔴 Deep 심층 분석

### Intelligent Agent Orchestration — 🟡 주목

> 상세 리서치: [2026-04-02_research-agent-orchestration.md](2026-04-02_research-agent-orchestration.md)

#### 이전 대비 변화
- 전주: OpenAI SDK 0.13.2 WebSocket(3/26), MS Agent Framework RC5(GA 임박), LangSmith Fleet(3/19), ADK A2A v0.3 gRPC, AWS AgentCore Stateful MCP GA, MCP 97M 다운로드
- 금주: OpenAI SDK 0.13.3-4(MCP 리소스 API·SIP), MS AF .NET RC5(durable workflow), AWS AgentCore Evaluations GA, AG-UI 3대 프로토콜 스택, MCP Dev Summit 개막, Claude Haiku 3 은퇴 예고
- 변화 방향: **프로토콜 표준화 완료 → 거버넌스·평가·런타임 효율화 단계** 전환 확정

#### 기술 동향

1. **OpenAI Agents SDK 0.13.3(3/31)~0.13.4(4/1) — MCP 리소스 API 공개, RealtimeRunner SIP 지원.**
   MCPServer에 `list_resources()`, `list_resource_templates()`, `read_resource()` 메서드가 안정화되었고, RealtimeRunner에 SIP(Session Initiation Protocol) attach flow(`OpenAIRealtimeSIPModel`)가 추가되어 전화 에이전트 시나리오를 공식 지원한다. gpt-realtime-1.5가 기본 WebSocket Realtime 모델로 설정. Python 3.14 호환성 확보 [[G-01]](#ref-g-01), [[G-02]](#ref-g-02).

2. **Microsoft Agent Framework .NET RC5(4/1) — 영속 워크플로우·MCP 도구 노출.**
   durable workflow 지원, Azure Functions 호스팅 시 워크플로우를 MCP 도구로 노출, 에이전트 스킬 다중 소스 아키텍처(breaking change), 인라인 스킬 API 추가. 별도로 Foundry Agent Service GA(3/16)에서 BYO VNet(Bring-Your-Own Virtual Network)·Voice Live Preview·평가 GA를 출하. GA는 Q2 초 예상 [추가확인 필요] [[G-03]](#ref-g-03), [[E-01]](#ref-e-01).

3. **AWS AgentCore Evaluations GA(3/31) — 에이전트 품질 평가 프로덕션 레이어 정착.**
   온라인(프로덕션 트래픽 상시 모니터링)·온디맨드(CI/CD 통합 테스트) 2가지 평가 유형, 13개 내장 평가기(응답 품질·안전·태스크 완료·도구 사용), 커스텀 Lambda 평가기. 9개 AWS 리전. AgentCore Runtime에 AG-UI 프로토콜(3/13), 관리형 세션 스토리지 Preview, WebRTC 실시간 스트리밍 지원도 추가 [[G-06]](#ref-g-06), [[G-07]](#ref-g-07).

4. **AG-UI 프로토콜 — MCP/A2A와 함께 3대 에이전트 프로토콜 스택 형성.**
   CopilotKit이 제안한 AG-UI(Agent-User Interaction Protocol)는 에이전트가 프런트엔드 앱과 실시간 통신하는 오픈 이벤트 기반 프로토콜. AWS(3/13)·Microsoft·Oracle·Google이 채택하면서 **MCP(도구 컨텍스트)·A2A(에이전트 간)·AG-UI(에이전트-사용자)** 3대 프로토콜 스택 구도가 확정 [[G-08]](#ref-g-08), [[G-09]](#ref-g-09).

5. **MCP Dev Summit 개막(4/2-3, NYC) — 프로덕션 격차 해소 공식화.**
   Linux Foundation AAIF(Agentic AI Foundation) 주관, Anthropic·OpenAI·Google·Docker·Datadog 등 50명 연사. MCP 월간 SDK 다운로드 9,700만 건(16개월 +4,750%). 2026 로드맵: Auth·Observability·HTTP transport 수평 확장 [[G-10]](#ref-g-10), [[G-11]](#ref-g-11).

6. **LangGraph 1.1 + LangSmith 3월 업데이트 — 타입 안전 스트리밍·에이전트 거버넌스.**
   LangGraph 1.1은 타입 안전 스트리밍(`StreamPart`)·invoke(`GraphOutput`)를 도입. LangSmith Sandboxes(3/17 Private Preview)는 microVM 격리로 에이전트 코드 실행 보안. Fleet(에이전트 ID/공유/권한), Deploy CLI, Polly AI 어시스턴트 GA, ABAC(Attribute-Based Access Control)·감사 로그 추가 [[G-04]](#ref-g-04), [[G-05]](#ref-g-05).

7. **Claude Haiku 3 은퇴(4/20) + 1M 컨텍스트 베타 종료(4/30) — 오케스트레이션 마이그레이션 필요.**
   `claude-3-haiku-20240307` 4/20 은퇴, 대체 모델 `claude-haiku-4-5-20251001`. Sonnet 4.5·4의 1M 컨텍스트 베타 헤더 4/30 효력 상실 → Sonnet 4.6 또는 Opus 4.6으로 마이그레이션 필요. 서브에이전트로 Haiku 3 사용 팀은 즉시 대응 필요 [[G-12]](#ref-g-12).

8. **CrewAI 0.175.0(3/25) — Qdrant Edge 메모리·에이전트 스킬·네이티브 공급자 확장.**
   Qdrant Edge 스토리지 백엔드로 로컬 메모리 실행 가능. OpenRouter·DeepSeek·Ollama·vLLM·Cerebras·Dashscope 네이티브 지원. Fortune 500 고객(IBM, PwC, DocuSign) 포함 월 4.5억 워크플로우 처리 [[G-13]](#ref-g-13).

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| OpenAI | SDK 0.13.3-4: MCP 리소스 API, RealtimeRunner SIP, gpt-realtime-1.5 기본 설정 | [[G-01]](#ref-g-01), [[G-02]](#ref-g-02) |
| Microsoft | AF .NET RC5(4/1): durable workflow·MCP 도구 노출; Foundry Agent Service GA(3/16): BYO VNet·Voice Live·평가 GA | [[G-03]](#ref-g-03), [[E-01]](#ref-e-01) |
| LangChain | LangGraph 1.1 타입 안전 스트리밍; LangSmith Sandboxes·Fleet·ABAC·Audit Logs; GTM(Go-To-Market) 에이전트 전환율 250%↑ | [[G-04]](#ref-g-04), [[G-05]](#ref-g-05) |
| AWS | AgentCore Evaluations GA(3/31): 13개 평가기; AG-UI(3/13); 세션 스토리지 Preview; WebRTC | [[G-06]](#ref-g-06), [[G-07]](#ref-g-07) |
| Anthropic | Haiku 3 은퇴(4/20), 1M context beta 종료(4/30); MCP Dev Summit 공동 주최 | [[G-12]](#ref-g-12) |
| Google | A2A v0.3 안정화; MCP Dev Summit 참여(AAIF 플래티넘) | [[G-14]](#ref-g-14) |
| CopilotKit | AG-UI 프로토콜 주도; AWS·MS·Oracle·Google 채택으로 3대 스택 형성 | [[G-08]](#ref-g-08), [[G-09]](#ref-g-09) |
| CrewAI | v0.175.0: Qdrant Edge·스킬·6개 공급자; 월 4.5억 워크플로우; IBM·PwC·DocuSign | [[G-13]](#ref-g-13) |

#### 시장 시그널

**투자 & M&A**
- 에이전트 AI 섹터 총 펀딩 $186억, 2023년 이후 연 60%+ 성장. 에이전트 인에이블러(플랫폼·오케스트레이션)가 총 투자의 55%+ 차지 [[G-15]](#ref-g-15)

**파트너십 & 제휴**
- AG-UI 프로토콜: AWS·Microsoft·Oracle·Google·CopilotKit 공동 채택으로 프런트엔드 에이전트 통신 표준화 가속 [[G-09]](#ref-g-09)
- MCP Dev Summit: Duolingo(180개 MCP 도구 Slack봇), Docker(MCP Platform), Datadog(에이전트 가관찰성) 실사용 기업 참여 [[G-10]](#ref-g-10)

**시장 전망**
- Deloitte TMT 2026: 에이전트 AI 시장 2026년 $85억 → 2030년 $350억 [[G-16]](#ref-g-16)
- BCG: 에이전트 AI로 Tech Services TAM(Total Addressable Market) 5년간 $2,000억 순증, CAGR(Compound Annual Growth Rate) 6-8% [[G-17]](#ref-g-17)
- Gartner: 2026년 말 엔터프라이즈 앱 40%에 AI 에이전트 내장; 42% 기업 프로덕션 단계, 72% 프로덕션+파일럿 병행 [[G-18]](#ref-g-18)

**도입 사례**
- LangChain 내부 GTM 에이전트: 리드-퀄리파이드 전환율 250% 향상 [[G-05]](#ref-g-05) [추가확인 필요]
- CrewAI: IBM·PwC·DocuSign·PepsiCo·J&J; 월 4.5억 에이전트 워크플로우 [[G-13]](#ref-g-13)
- Duolingo: 180개 MCP 도구 통합 AI Slack봇 운영 [[G-10]](#ref-g-10)

**연구 동향**
- "guardian agent" 아키텍처: 에이전트 스프롤 관리·규정 준수를 단일 거버넌스 레이어가 담당하는 패턴 확산 [[G-19]](#ref-g-19)
- AgentCore Evaluations GA + Foundry 평가 GA 동시 출하 → "에이전트 품질 측정"이 프로덕션 필수 레이어로 정착

**커뮤니티 시그널**
- MCP Dev Summit 4/2-3 NYC: Linux Foundation AAIF 첫 대규모 이벤트; Auth·Observability·서버 관리가 2026 로드맵 핵심 [[C-01]](#ref-c-01)
- MCP 월간 SDK 다운로드 9,700만 건(16개월 +4,750%) [[C-02]](#ref-c-02)
- HN "Multi-agent coordination: 8 production pain points" — 컨텍스트 압축 건망증, 동시 파일 충돌, idle 토큰 낭비 등 실무 이슈 활발 논의 [[C-03]](#ref-c-03)

#### 시장 수요 (voice-of-market)

> Interrupt 2025 Keynote(Harrison Chase), Andrew Ng Fireside Chat, HN 실무자 쓰레드 기반.

**고객 페인포인트**
- **프로토타입→프로덕션 신뢰성 격차** — "쉽게 작동하는 것을 만들 수 있지만, 실제 비즈니스에서 레버를 움직일 만큼 신뢰할 수 있는 것으로 만들기는 어렵다" — Harrison Chase (LangChain)
- **eval 미실행** — "사람들이 eval에 대해 이야기하지만, 어떤 이유에서인지 실제로는 하지 않는다" — Andrew Ng
- **MCP 서버 품질 불균일** — "인터넷에서 찾는 MCP 서버 대부분이 제대로 작동하지 않고, 인증 시스템이 불안정" — Andrew Ng
- **에이전트 빌드 멀티디시플린 요구** — prompting + engineering + product sense + ML을 모두 요구하는 새 직군

**도입 장벽**
- **비즈니스 워크플로우→에이전트 변환 스킬 부족** — "비즈니스에서 수행되는 작업을 에이전틱 워크플로우로 변환하는 능력이 여전히 매우 희귀" — Andrew Ng
- **에이전트 배포 인프라 미성숙** — long-running, bursty, stateful 특성 → 기존 웹 서버 모델 부적합
- **A2A 프로토콜 초기 단계** — "한 팀의 에이전트가 다른 팀의 에이전트와 성공적으로 소통한 사례가 아직 초기" — Andrew Ng

**시장 니즈**
- AI 관찰가능성 전용 툴링 (ML·product·prompt 맥락 통합)
- long-running·bursty 에이전트 전용 배포 플랫폼
- 경량 eval 프레임워크 (20분 구축, LLM-as-judge)
- Voice AI 에이전트 스택 — "대기업이 음성 애플리케이션에 매우 흥분하지만 개발자 관심은 훨씬 적다" — Andrew Ng
- No-code 에이전트 빌더 (비개발자용)

#### 전략적 시사점

**기회**
- 3대 프로토콜 스택(MCP·A2A·AG-UI) 조기 채택으로 오케스트레이션 계층 차별화
- 에이전트 SIP/음성 연동: OpenAI RealtimeRunner SIP + MS Voice Live → 통신사 SIP 트렁크 통합 시나리오 현실화
- 에이전트 평가·관찰성 내재화로 엔터프라이즈 신뢰성 검증 선점

**위협**
- Claude Haiku 3 은퇴(4/20), 1M context beta 종료(4/30) — 서브에이전트 모델 즉시 마이그레이션 필요
- 프로토콜 분화 리스크(MCP·A2A·AG-UI·A2UI(Agent-to-User Interface) 난립) — 추상화 레이어 설계 필요
- 에이전트 스프롤: 중앙 레지스트리·ABAC 정책 없이 무분별 확산 시 보안·규정 준수 리스크

---

## 경쟁사 동향 (SKT / KT)

> 이번 주 해당 도메인과 관련된 SKT·KT의 주요 움직임.

### SKT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| 1인 1 AI 에이전트 전환 | 3/16 공개, 전 구성원이 AI 에이전트 직접 설계·업무 적용. 에이닷 비즈·폴라리스·플레이그라운드 플랫폼 제공 | agent-orchestration | [[E-02]](#ref-e-02) |
| 멀티에이전트 시스템 | SK AX Agent Builder Platform으로 산업별 특화 에이전트 서비스 준비. 현장 검증 멀티에이전트 프레임워크 기반 | agent-orchestration | [[E-03]](#ref-e-03) |
| 에이닷 조직 전면 배치 | 2026 조직개편에서 AI CIC 내 에이닷 관련 부서를 사업·기획·전화로 분리, 모든 부서명에 에이닷 공통 적용 | (L3 밖) | [[E-04]](#ref-e-04) |

### KT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| 에이전트 빌더 공개 (MWC26) | 노코드 드래그앤드롭 AI 에이전트 제작 플랫폼. 업무 템플릿+대화 모듈 조합 방식 | agent-orchestration | [[E-05]](#ref-e-05) |
| K 인텔리전스 스튜디오 | 에이전트 빌더 + RAG + K GPUaaS(월 구독형 GPU) + AI GPU 매니지드 통합 플랫폼 | gpu-orchestration | [[E-05]](#ref-e-05) |
| 산업별 AI 템플릿 | 금융·제조·공공 분야 검증 에이전트 시나리오 표준화 서비스 준비 | agent-orchestration | [[E-05]](#ref-e-05) |

### 시사점
- SKT·KT 모두 **노코드 에이전트 빌더** 전략으로 수렴 — 비개발자 AI 에이전트 제작이 양사의 공통 방향
- SKT는 내부 AX(1인 1 에이전트) + 외부 B2B(SK AX Agent Builder) 투트랙, KT는 MWC에서 B2B 플랫폼 중심 전략
- 글로벌 생태계의 MCP/A2A/AG-UI 프로토콜 스택 대비 양사의 프로토콜 전략은 아직 미공개

---

## 규제 & 거버넌스

> 해당 도메인에 영향을 미치는 국내외 규제·표준·가이드라인 동향.

### 시행 임박 / 카운트다운

| 규제 | 시행일 | D-day |
|------|--------|-------|
| 한국 AI 기본법 (인공지능 발전과 신뢰 기반 조성 등에 관한 기본법) | 2026-01-22 | 시행 중 |
| EU AI Act Article 6-49 (고위험 AI 시스템 전면 적용) | 2026-08-02 | D-122 |
| EU AI Act Article 50 (합성 콘텐츠 투명성) | 2026-08-02 | D-122 |

### 신규 발의 & 가이드라인
- **EU AI Act와 AI 에이전트**: The Future Society 분석에 따르면 AI Act는 원래 에이전트를 염두에 두고 설계되지 않았으나 실제로 적용됨. GPAI(General-Purpose AI) 모델 제공자는 에이전트로부터의 시스템 리스크를 평가·완화해야 함. 다목적 에이전트는 고위험으로 간주될 수 있음 [[G-20]](#ref-g-20)
- **한국 AI 기본법**: 규제 적용 최소 1년 유예 + 계도기간 운영. 사실조사는 인명사고·인권 훼손 등 예외적 경우에만. 기업 지원 창구 개설 [[G-21]](#ref-g-21)
- **에이전트 크로스보더 거버넌스 공백**: 자율 에이전트가 다른 관할권의 도구를 실시간으로 호출하는 경우 단일 지역 규제(AI Act)만으로는 통제 불가 — 추가 가이드라인 필요 [[G-20]](#ref-g-20)

### 시사점
- EU AI Act 고위험 전면 적용(8월)까지 D-122. 에이전트 오케스트레이션 시스템이 "고위험 AI"로 분류될 경우 리스크 관리·기술 문서·투명성·인간 감독 의무 발생
- 한국 AI 기본법은 계도기간 중이나, "고영향 AI" 분류 기준이 에이전트 시스템에 어떻게 적용될지 주시 필요

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **에이전트 프로토콜 3대 스택 성립**: MCP(도구)·A2A(에이전트 간)·AG-UI(사용자 인터페이스)가 동시 성숙하면서, 이를 모두 지원하는 오케스트레이션 레이어가 2026년 인프라 차별화 핵심. 우리 에이전트 아키텍처에서 3대 프로토콜 추상화 레이어 설계를 선행 검토할 필요.

2. **에이전트 평가·거버넌스가 프로덕션 게이트로 정착**: AWS AgentCore Evaluations GA + MS Foundry 평가 GA + LangSmith ABAC/Audit Logs가 같은 주에 출하. "에이전트를 배포하려면 품질 평가+감사 로그가 필수"라는 업계 합의 형성. 내부 에이전트 파이프라인에 평가 단계 내재화 시급.

3. **SIP/음성 에이전트 통합 기회**: OpenAI RealtimeRunner SIP + MS Voice Live가 통신 인프라(SIP 트렁크)와의 연동을 공식 지원. 통신사 관점에서 음성 에이전트 시나리오(AI 컨택센터, 에이닷 통화) 선행 검토 가치 높음.

### 후속 조치 제안

- 🟡 agent-orchestration 지속 모니터링: MCP Dev Summit(4/2-3) 결과 확인, MS AF GA 발표 추적
- Claude Haiku 3(4/20)·1M context beta(4/30) 은퇴 대비 마이그레이션 검토
- 📂 Obsidian 동기화: `/obsidian-bridge` 실행
- 📅 다음 도메인: `/weekly-monitor voice-ai`

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | GitHub — openai-agents-python Releases | [링크](https://github.com/openai/openai-agents-python/releases) | release | 2026-04-01 | [A] |
| <a id="ref-g-02"></a>G-02 | OpenAI Agents SDK — Release Changelog | [링크](https://openai.github.io/openai-agents-python/release/) | docs | 2026-04-01 | [A] |
| <a id="ref-g-03"></a>G-03 | GitHub — microsoft/agent-framework Releases | [링크](https://github.com/microsoft/agent-framework/releases) | release | 2026-04-01 | [A] |
| <a id="ref-g-04"></a>G-04 | LangChain Changelog — LangGraph 1.1 | [링크](https://docs.langchain.com/oss/python/releases/changelog) | release | 2026-03 | [A] |
| <a id="ref-g-05"></a>G-05 | LangChain Blog — March 2026 Newsletter | [링크](https://blog.langchain.com/march-2026-langchain-newsletter/) | blog | 2026-03-31 | [B] |
| <a id="ref-g-06"></a>G-06 | AWS — AgentCore Evaluations Generally Available | [링크](https://aws.amazon.com/about-aws/whats-new/2026/03/agentcore-evaluations-generally-available/) | release | 2026-03-31 | [A] |
| <a id="ref-g-07"></a>G-07 | AWS — AgentCore Runtime AG-UI Protocol | [링크](https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-bedrock-agentcore-runtime-ag-ui-protocol/) | release | 2026-03-13 | [A] |
| <a id="ref-g-08"></a>G-08 | CopilotKit — Introducing AG-UI Protocol | [링크](https://www.copilotkit.ai/blog/introducing-ag-ui-the-protocol-where-agents-meet-users) | blog | 2026-03 | [B] |
| <a id="ref-g-09"></a>G-09 | Medium — A2A, MCP, AG-UI: 2026 AI Agent Protocol Stack | [링크](https://medium.com/@visrow/a2a-mcp-ag-ui-a2ui-the-essential-2026-ai-agent-protocol-stack-ee0e65a672ef) | blog | 2026-03 | [C] |
| <a id="ref-g-10"></a>G-10 | Linux Foundation — MCP Dev Summit North America | [링크](https://events.linuxfoundation.org/mcp-dev-summit-north-america/) | event | 2026-04-02 | [A] |
| <a id="ref-g-11"></a>G-11 | MCP Blog — MCP joins the Agentic AI Foundation | [링크](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/) | blog | 2025-12-09 | [A] |
| <a id="ref-g-12"></a>G-12 | Anthropic Docs — Model Deprecations | [링크](https://platform.claude.com/docs/en/about-claude/model-deprecations) | docs | 2026-04-02 | [A] |
| <a id="ref-g-13"></a>G-13 | CrewAI Community — Release 0.175.0 | [링크](https://community.crewai.com/t/new-release-0-175-0/6989) | release | 2026-03-25 | [B] |
| <a id="ref-g-14"></a>G-14 | Google Cloud Blog — A2A Protocol Upgrade | [링크](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade) | blog | 2026-03 | [A] |
| <a id="ref-g-15"></a>G-15 | Tracxn — Agentic AI 2026 Market Trends | [링크](https://tracxn.com/d/sectors/agentic-ai/__oyRAfdUfHPjf2oap110Wis0Qg12Gd8DzULlDXPJzrzs) | report | 2026-03 | [B] |
| <a id="ref-g-16"></a>G-16 | Deloitte — AI Agent Orchestration TMT Predictions 2026 | [링크](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/ai-agent-orchestration.html) | report | 2026-01 | [B] |
| <a id="ref-g-17"></a>G-17 | BCG — The $200B Agentic AI Opportunity | [링크](https://www.bcg.com/publications/2026/the-200-billion-dollar-ai-opportunity-in-tech-services) | report | 2026 | [B] |
| <a id="ref-g-18"></a>G-18 | Joget — AI Agent Adoption 2026 (Gartner, IDC) | [링크](https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/) | report | 2026-03 | [B] |
| <a id="ref-g-19"></a>G-19 | AetherLink — Agentic AI Enterprise Governance 2026 | [링크](https://aetherlink.ai/en/blog/agentic-ai-multi-agent-systems-enterprise-governance-in-2026) | blog | 2026-03 | [C] |
| <a id="ref-g-20"></a>G-20 | The Future Society — AI Agents Under the EU AI Act | [링크](https://thefuturesociety.org/aiagentsintheeu/) | report | 2026 | [B] |
| <a id="ref-g-21"></a>G-21 | 피카부랩스 — AI 기본법 완전 정리 | [링크](https://peekaboolabs.ai/blog/ai-basic-law-guide) | blog | 2026 | [B] |
| <a id="ref-e-01"></a>E-01 | Microsoft Foundry Blog — Foundry Agent Service GA | [링크](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/) | IR/발표 | 2026-03-16 | [A] |
| <a id="ref-e-02"></a>E-02 | SK텔레콤 뉴스룸 — 1인 1 AI 에이전트 전환 | [링크](https://news.sktelecom.com/223253) | IR/발표 | 2026-03 | [A] |
| <a id="ref-e-03"></a>E-03 | SK AX — 멀티에이전트 시스템이 필요한 이유 | [링크](https://www.skax.co.kr/insight/trend/3626) | blog | 2026 | [B] |
| <a id="ref-e-04"></a>E-04 | 더벨 — 2026 SKT 리빌딩 에이닷 조직 전면 배치 | [링크](https://m.thebell.co.kr/m/newsview.asp?svccode=04&newskey=202512311210233800102717) | news | 2025-12 | [B] |
| <a id="ref-e-05"></a>E-05 | 인공지능신문 — KT 노코드 에이전트 빌더 공개 | [링크](https://www.aitimes.kr/news/articleView.html?idxno=38894) | news | 2026-03-04 | [B] |
| <a id="ref-c-01"></a>C-01 | MCP Dev Summit — Linux Foundation AAIF 공식 이벤트 | [링크](https://events.linuxfoundation.org/mcp-dev-summit-north-america/) | community | 2026-04-02 | [A] |
| <a id="ref-c-02"></a>C-02 | MCP Blog — SDK 다운로드 9,700만 건 | [링크](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/) | community | 2025-12-09 | [A] |
| <a id="ref-c-03"></a>C-03 | HN — Multi-agent coordination: 8 production pain points | [링크](https://news.ycombinator.com/item?id=46929406) | community | 2025-03 | [C] |
