---
type: weekly-monitor
domain: agentic-ai
week: 2026-W15
date: 2026-03-30
l3_count: 12
deep_count: 2
---

# 주간 기술 동향: Agentic AI (2026-W15)

## Executive Summary

> **이번 주 핵심**: KubeCon Europe 2026(3/24)에서 GPU 오케스트레이션의 대규모 오픈소스 이관이 단행되었다. NVIDIA가 DRA Driver를 CNCF에 기부하고, Grove API·KAI Scheduler를 공개하면서 "자사 플랫폼 잠금"에서 "오픈 에코시스템 주도"로 전략을 전환. 동시에 에이전트 프레임워크 진영에서는 OpenAI SDK 0.13.2의 WebSocket transport, Google ADK A2A v0.3 gRPC 지원, AWS AgentCore Stateful MCP GA 등 프로토콜 표준화가 완료되고 거버넌스·런타임 효율화 단계로 전환.

| Layer 2 | 세부기술 | 신호 | 핵심 내용 |
|---------|----------|------|----------|
| Trusted Multi-Agent Orchestration | Intelligent Agent Orchestration | 🟡 | [제품출시] OpenAI SDK 0.13.2 WebSocket(3/26) · [생태계] MS Agent Framework GA 임박, ADK A2A v0.3 gRPC, MCP 97M 다운로드 |
| | Agent Oriented Orchestration | 🟢 | PlanReAct 표준 정착 유지, 신규 변화 없음 |
| Model & Delta Foundry | 하이브리드 GPU Orchestration | 🟡 | [생태계] KubeCon: NVIDIA DRA→CNCF, Grove API, KAI Scheduler Sandbox, llm-d CNCF 합류 · [파트너십] MS AI Runway |
| | FeedbackOps: Meta-prompt Engineering | 🟢 | DSPy MIPROv2 안정, GEPA 유지 |
| | EvaluationOps: KMS 성능평가 | 🟢 | RAGAS 표준 정착, LLM-as-judge 80-90% 인간 일치 유지 |
| | 데이터-학습-배포 파이프라인 | 🟢 | LLMOps→AgentOps 전환 언급, 신규 이벤트 없음 |
| Hybrid AI Infra | On-Device sLM | 🟢 | GPT-5.4 mini/nano 후속 정착, 신규 발표 없음 |
| | Edge AI | 🟢 | AT&T-Cisco-NVIDIA AI Grid 후속 정착 단계 |
| | 5G SA/6G(AI-RAN/SRv6) | 🟢 | MWC 후속 정착, 이번 주 신규 발표 없음 |
| | 실시간 화자분할(2인) | 🟢 | AssemblyAI/Gladia 안정 유지 |
| Self Evolving Architecture | Agentic Context Engineering | 🟢 | MCE 논문 존재, ACE 생태계 성숙 지속 |
| 의도 파악 기술 | Adaptive RAG | 🟢 | Agentic RAG 57%+ 유지, CRAG 정착 |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음
> **태그** : [기술돌파] [제품출시] [경쟁사] [규제] [투자] [논문] [생태계]

---

## 🟢 Quick 요약 (변화 미미)

### Agent Oriented Orchestration
- ReAcTree + hybrid plan-execute(PlanReAct) 패턴이 산업 표준으로 정착 유지. Plan-and-Execute(고추론 모델 DAG 분해 → 경량 모델 실행 → 재계획) 패턴이 프로덕션 배포 주류. 이번 주 추가 변화 없음.

### FeedbackOps (Meta-prompt Engineering)
- DSPy MIPROv2 옵티마이저와 GEPA (Generative Evolution of Prompts and Artifacts) 기반 자동 프롬프트 최적화 안정 운영 중. BetterTogether 메타옵티마이저(프롬프트+가중치 순차 최적화) 패턴 확산 지속. 신규 릴리스 없음.

### EvaluationOps (KMS 성능평가)
- LLM-as-judge가 인간 평가자와 80-90% 일치율 유지. RAGAS (Retrieval-Augmented Generation Assessment)가 RAG 평가 사실상 표준. Langfuse + RAGAS + DeepEval 통합 평가 파이프라인 확산 지속. 이번 주 돌파구 없음.

### MLOps Pipeline
- MLOps→LLMOps→AgentOps 전환 가속. LoRA (Low-Rank Adaptation)/PEFT (Parameter-Efficient Fine-Tuning) 엔터프라이즈 파인튜닝 표준 유지. AgentOps(장기 실행·다단계·도구 사용 에이전트 관리) 개념이 차세대 운영 패러다임으로 부상 중이나 구체적 신규 제품 출시는 없음.

### On-Device sLM
- W14에 보고한 OpenAI GPT-5.4 mini/nano(3/17), sLM-First LLM-Backup 아키텍처(비용 60-70% 절감) 후속 정착 단계. Google AI Edge RAG 공식 지원 확산 지속. 이번 주 신규 발표 없음.

### Edge AI
- AT&T-Cisco-NVIDIA AI Grid 상용 배포(3/17-19), Akamai 4,400 에지 로케이션 AI Grid가 후속 정착 중. 에지 AI가 PoC→프로덕션 전환 변곡점 도달 확인. 이번 주 추가 발표 없음.

### 5G SA/6G (AI-RAN/SRv6)
- MWC 2026에서 보고한 SKT-에릭슨 MoU, NVIDIA Aerial 오픈소스, OCUDU 재단, 12개 통신사 6G 연합 등 후속 정착 단계. 90개 통신사 5G SA 코어 배포 완료. 이번 주 추가 발표 없음.

### Speaker Diarization
- AssemblyAI Universal-3-Pro와 Gladia Solaria-1(103ms 부분 지연) 안정 운영 유지. pyannote 실시간 다이어리제이션 + LLM 통합 연구 진행 중. 돌파구 수준 변화 없음.

### Agentic Context Engineering
- ACE (Agentic Context Engineering) (ICLR 2026) 프레임워크 오픈소스 생태계 성숙 지속. Meta Context Engineering (MCE) 논문이 ACE 대비 5.6-53.8% 상대 개선을 보고했으나, 아직 프로덕션 적용 사례는 없음. 이번 주 신규 발표 없음.

### Adaptive RAG
- Agentic RAG 프로덕션 도입률 57%+ 유지. CRAG (Corrective RAG) 패턴 기업 배포 표준 정착. Higress-RAG 엔터프라이즈 확산 지속. 주요 벡터 DB 벤더(Pinecone, Weaviate, Milvus)가 라우팅 기능을 플랫폼에 직접 내장하는 추세. 이번 주 변화 없음.

---

## 🟡🔴 Deep 심층 분석

### Intelligent Agent Orchestration — 🟡 주목

> 상세 리서치: [2026-03-30_research-agent-orchestration.md](2026-03-30_research-agent-orchestration.md)

#### 이전 대비 변화
- 전주: OpenAI SDK 0.13 tool search(3/23), Claude Code Channels(3/20), Google ADK 네이티브 A2A, MS Foundry Agent Service GA(3/16)
- 금주: OpenAI SDK 0.13.2 WebSocket transport(3/26), MS Agent Framework RC5(GA 임박), LangSmith Fleet 출시(3/19), ADK A2A v0.3 gRPC, AWS AgentCore Stateful MCP GA
- 변화 방향: 프로토콜 표준화 완료 → **거버넌스·런타임 효율화 + 엔터프라이즈 운영 플랫폼화** 단계

#### 기술 동향

1. **OpenAI Agents SDK 0.13.2 — WebSocket transport 추가 및 런타임 요건 상향(3/26).**
   Responses API에 WebSocket transport 지원 추가(opt-in, HTTP 기본 유지). `responses_websocket_session()` 헬퍼로 멀티턴 런에서 공유 WebSocket 세션 재사용 가능. Python 3.9 지원 종료, openai v2.x 필수화. Realtime API 기본 모델 `gpt-realtime-1.5`로 업그레이드. 음성·실시간 멀티에이전트 시나리오 기반 확충. [[G-01]](#ref-g-01)

2. **Microsoft Agent Framework RC5(3/20) — GA 임박, AutoGen+Semantic Kernel 통합 완성.**
   Python 1.0.0rc5(3/20)와 .NET RC4(3/11) 출시로 GA 직전 단계 진입. Q1 2026 말 GA 목표이나 공식 GA 발표는 미확인 [추가확인 필요]. A2A·MCP 프로토콜 네이티브 지원, .NET/Python 공통 프로그래밍 모델 제공. Foundry Agent Service(3/16 GA)와 연계하여 엔터프라이즈 배포 스택 완성도 상승. [[G-02]](#ref-g-02)

3. **LangSmith Fleet 출시(3/19) — 엔터프라이즈 에이전트 거버넌스 플랫폼.**
   에이전트 레지스트리, 계층형 권한(편집/실행/복제), 두 가지 에이전트 유형(개인화 Assistants vs. 고정 자격증명 Claws) 지원. NVIDIA Agent Toolkit 파트너십(3/20)으로 LangGraph + NVIDIA 통합 플랫폼 구성. 조직 내 수십 개 에이전트 중앙 관리 수요 겨냥. [[G-03]](#ref-g-03)

4. **Google ADK 2.0 Alpha + A2A v0.3 — gRPC 지원으로 엔터프라이즈급 상호운용성.**
   ADK Python 2.0 Alpha에 그래프 기반 워크플로우 추가. A2A v0.3(3/26)은 gRPC 지원, 에이전트 카드 서명(보안 강화), Python/Go/JavaScript/Java/.NET SDK 확장. 기업 환경의 고성능·보안 요건 충족 전환점. [[G-04]](#ref-g-04)

5. **Amazon Bedrock AgentCore — Stateful MCP 서버 지원 GA.**
   elicitation(실행 중 사용자 입력 수집), sampling(LLM 추론 연쇄), progress notification(장기 태스크 알림) 지원. Policy Controls GA로 에이전트 행동 제한 외부 검증 신뢰 계층 추가. OpenAI 공동 개발 Stateful Runtime 기반. [[G-05]](#ref-g-05)

6. **MCP 97M 다운로드 돌파 — Anthropic "madcap March" 14+ 릴리스.**
   MCP 월간 SDK 다운로드 9,700만 건(론칭 16개월 만에 4,750% 성장). AAIF (Agentic AI Foundation, Linux Foundation 산하) 기증 후 지속 확산. Claude Code 사용량 300% 증가. [[G-06]](#ref-g-06)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| OpenAI | Agents SDK 0.13.2(3/26): WebSocket transport, Python 3.9 드롭, openai v2.x 필수, gpt-realtime-1.5 | [[G-01]](#ref-g-01) |
| Microsoft | Agent Framework RC5(3/20), GA 임박; Foundry Agent Service GA(3/16) 프라이빗 네트워킹·Voice Live | [[G-02]](#ref-g-02) |
| LangChain | LangSmith Fleet(3/19) 에이전트 거버넌스; NVIDIA Agent Toolkit 파트너십(3/20) | [[G-03]](#ref-g-03) |
| Google | ADK 2.0 Alpha 그래프 워크플로우, A2A v0.3 gRPC(3/26), Agent Engine 배포 지원 | [[G-04]](#ref-g-04) |
| AWS | AgentCore Stateful MCP GA, Policy Controls GA, OpenAI Stateful Runtime 통합 | [[G-05]](#ref-g-05) |
| Anthropic | "madcap March" 14+ 릴리스, MCP 9,700만 다운로드, Computer Use research preview(3/23) | [[G-06]](#ref-g-06) |
| IBM | watsonx Orchestrate AgentOps 거버넌스, Agent Catalog 수백 개, Finance·Supply Chain 도메인 에이전트 | [[G-07]](#ref-g-07) |
| DeepSeek | V3.2 agent-first 모델 — tool-use + thinking 통합, 1,800개 환경 85k+ 에이전트 훈련 데이터 | [[G-08]](#ref-g-08) |

#### 시장 시그널

**투자 & M&A**
- 에이전틱 AI 스타트업 평균 라운드 $155M(Q4 2025~Q1 2026), 전기 대비 2배 [[G-09]](#ref-g-09) [추가확인 필요]
- 에이전트 투자 기업 92%가 향후 12개월 내 예산 증액 계획 [[G-09]](#ref-g-09) [추가확인 필요]
- Tess AI $5M 라운드(3/2) — 엔터프라이즈 에이전트 오케스트레이션 확장 [[G-10]](#ref-g-10)

**파트너십 & 제휴**
- LangChain × NVIDIA(3/20): LangSmith Fleet + NVIDIA Agent Toolkit 통합 엔터프라이즈 플랫폼 [[G-03]](#ref-g-03)
- AAIF 생태계 확장: AWS·Google·Microsoft·Cloudflare·Bloomberg 플래티넘 회원 참여 [[G-06]](#ref-g-06)

**시장 전망**
- 글로벌 에이전틱 AI 시장 $91~109억(2026) → $1,390억(2034), CAGR 40.5% [[G-09]](#ref-g-09) [추가확인 필요]
- Gartner: 2026년 말 엔터프라이즈 앱 40%에 에이전트 탑재(2025년 12%) [[G-09]](#ref-g-09) [추가확인 필요]
- 40%+ 에이전트 프로젝트가 2027년까지 실패 예상(런어웨이 비용, 정책 위반) [[G-09]](#ref-g-09) [추가확인 필요]

**도입 사례**
- Global 2000 기업 72% AI 에이전트 프로덕션 배포 운영 중(파일럿 초월) [[G-09]](#ref-g-09)
- Talkdesk CXA Operations Center(3/10): AI·인간 에이전트 단일 운영 거버넌스 [[G-11]](#ref-g-11)

**연구 동향**
- DeepSeek V3.2: "thinking with tools" — 도구 사용 중 추론 통합, agent-first 아키텍처 최초 적용 [[G-08]](#ref-g-08)
- LangChain Deep Agents v0.5.0 Alpha(3/24): 비동기 서브에이전트 + 멀티모달(PDF·오디오·비디오) 도구 지원 [[G-03]](#ref-g-03)

#### 시장 수요 (voice-of-market)

> 이번 주 해당 기술 관련 컨퍼런스 영상에서 수요 시그널을 확인하지 못함.

#### 전략적 시사점

**기회**
- 프로토콜 표준화(MCP AAIF 기증 + A2A v0.3 gRPC)로 벤더 중립 멀티에이전트 인프라 구축이 현실화. 통신사 맞춤 MCP 서버 개발 적기.
- 에이전트 거버넌스 요구 급증(LangSmith Fleet, IBM AgentOps, Talkdesk CXA) — 관찰성·정책 제어가 차별화 포인트.
- MS Agent Framework GA 임박 시 AutoGen → Agent Framework 마이그레이션 가이드 공개 예정. 내부 AutoGen 프로젝트 마이그레이션 사전 검토 시점.

**위협**
- OpenAI SDK Python 3.9 드롭 + openai v2.x 필수화로 의존성 요건 급격 상향. SDK 버전 잠금 전략 부재 시 업그레이드 단절 위험.
- Gartner 2027년 40%+ 에이전트 프로젝트 실패 예측 — 거버넌스 없는 빠른 배포는 역효과.
- AAIF 내 MCP(HTTP+SSE) vs. A2A(gRPC) 역할 분담 재조정 가능성.

---

### 하이브리드 GPU Orchestration — 🟡 주목

> 상세 리서치: [2026-03-30_research-gpu-orchestration.md](2026-03-30_research-gpu-orchestration.md)

#### 이전 대비 변화
- 전주: NVIDIA Dynamo 1.0 GA(3/16), Vera Rubin + Groq 3 LPX 발표(GTC 2026), 추론 OS 포지셔닝
- 금주: KubeCon Europe 2026(3/24) — GPU 오케스트레이션의 **오픈소스 대규모 이관**. DRA Driver CNCF 기부, Grove API 공개, KAI Scheduler Sandbox, llm-d CNCF 합류, MS AI Runway 출시
- 변화 방향: "자사 플랫폼 잠금(lock-in)" → "오픈 에코시스템 주도(open ecosystem stewardship)" 전환. Kubernetes가 AI 인프라 OS로 공식 격상

#### 기술 동향

1. **NVIDIA DRA Driver CNCF 기부(3/24) — GPU 리소스 할당의 커뮤니티 표준화.**
   Dynamic Resource Allocation Driver를 CNCF에 기부, 벤더 단독 거버넌스에서 Kubernetes 커뮤니티 소유로 이전. AWS·Broadcom·Canonical·Google·Microsoft·Nutanix·Red Hat·SUSE 8개사 공동 협력. CNCF CTO: "GPU 오케스트레이션이 오픈 클라우드 네이티브 환경에서 표준화되는 주요 이정표". [[G-12]](#ref-g-12)

2. **NVIDIA Grove API 공개(3/24) — 복잡한 추론 시스템의 단일 선언형 표현.**
   Dynamo 생태계의 오픈소스 Kubernetes API. 역할·의존성·다단계 스케일링·시작 순서 등 복잡한 추론 시스템 전체를 단일 Custom Resource로 표현. llm-d 추론 스택과 통합. [[G-13]](#ref-g-13)

3. **KAI Scheduler CNCF Sandbox(3/24) — AI 워크로드 스케줄링 오픈 거버넌스.**
   Gang-scheduling, 계층적 큐, 플러그인 기반 확장 지원. GPU Operator + DRA Driver 위에서 고급 리소스 조율. 커뮤니티 공동 개발로 전환. [[G-14]](#ref-g-14)

4. **llm-d CNCF Sandbox 합류(3/24) — 분산 LLM 추론 클라우드 네이티브 표준화.**
   Red Hat·Google Cloud·IBM Research·CoreWeave·NVIDIA 공동 창립. Kubernetes Gateway API Inference Extension, Prefill/Decode 분리, 계층형 KV 캐시 오프로딩(GPU→TPU→CPU→스토리지) 핵심 기능. AMD·Cisco·HuggingFace·Intel·Lambda·Mistral AI 지원. [[G-15]](#ref-g-15)

5. **Microsoft AI Runway 출시(3/24) — Kubernetes 추론 워크로드 통합 관리 API.**
   모델 배포·서빙 기술 전환을 중앙 관리. HuggingFace 모델 검색, GPU 메모리 적합도, 실시간 비용 추정, 비전문가 웹 UI. NVIDIA Dynamo·KubeRay·llm-d·KAITO 런타임 지원. "Kubernetes = AI 인프라 OS" 선언. [[G-16]](#ref-g-16)

6. **GPU Kata Containers 보안 확장(3/24) — GPU 가속 기밀 컴퓨팅.**
   Kata Containers(경량 VM 격리)에 GPU 지원 도입. 하드웨어 수준 워크로드 격리 + GPU 가속 동시 구현. 규제 산업 AI 추론 보안 대응. [[G-17]](#ref-g-17)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| NVIDIA | KubeCon: DRA→CNCF 기부, Grove API, KAI Scheduler Sandbox, GPU Kata. 오픈 에코시스템 전략 본격화. 8개사 협력 | [[G-12]](#ref-g-12), [[G-13]](#ref-g-13) |
| Microsoft | AI Runway 오픈소스, DRA GA(K8s 1.36), AKS GPU 텔레메트리(Prometheus/Grafana), DRANet RDMA NIC | [[G-16]](#ref-g-16) |
| Google Cloud | GKE Inference Gateway + Dynamo 1.0 통합, llm-d 공동 창립 | [[G-15]](#ref-g-15), [[G-18]](#ref-g-18) |
| Red Hat / IBM | llm-d CNCF 공동 창립, "Kubernetes를 SOTA AI 인프라로 진화" 청사진 기부 | [[G-15]](#ref-g-15) |
| CoreWeave | llm-d 공동 창립, SkyPilot 멀티클라우드 백엔드 지원 지속 | [[G-15]](#ref-g-15) |
| Nscale | 유럽 최대 시리즈 C $2B(밸류에이션 $14.6B). NVIDIA·Citadel·Dell·Jane Street 투자 | [[G-19]](#ref-g-19) [추가확인 필요] |
| Shopify | SkyPilot 기반 멀티클라우드 GPU — 훈련 잡 일→분 단축, 팀별 비용 추적 자동화 | [[G-20]](#ref-g-20) |

#### 시장 시그널

**투자 & M&A**
- Nscale $2B 시리즈 C(밸류에이션 $14.6B) — 유럽 최대 테크 펀딩. 데이터센터→컴퓨트→오케스트레이션 수직 통합 [[G-19]](#ref-g-19) [추가확인 필요]
- NVIDIA $20B Groq 인수(2025년 말) 성과: Groq 3 LPX(저지연 추론 가속기)가 Vera Rubin 플랫폼 내 편입 [[G-21]](#ref-g-21), [[G-24]](#ref-g-24)

**파트너십 & 제휴**
- NVIDIA + 8개사(AWS·Broadcom·Canonical·Google·Microsoft·Nutanix·Red Hat·SUSE): DRA Driver CNCF 공동 협력. 업계 최초 GPU 오케스트레이션 벤더 중립 표준 [[G-12]](#ref-g-12)
- IBM + Red Hat + Google + CoreWeave + NVIDIA: llm-d CNCF 공동 창립 [[G-15]](#ref-g-15)
- Pure Storage + NVIDIA Dynamo: KV 캐시 가속(Pure KVA) 통합 [[G-22]](#ref-g-22)

**시장 전망**
- GPU as a Service 시장: 2026년 $7.3~7.6B, 전년 대비 27-29% 성장 [[G-23]](#ref-g-23) [추가확인 필요]
- AWS: 2026년부터 1M+ NVIDIA GPU 배포 계획(Blackwell + Rubin) [[G-24]](#ref-g-24)

**도입 사례**
- Shopify: SkyPilot 멀티클라우드 GPU — 훈련 잡 런칭 일→분 단축, Kueue 공정 분배, 팀별 비용 추적 자동화 [[G-20]](#ref-g-20)
- Dynamo 1.0 프로덕션: AstraZeneca, Baseten, ByteDance, CoreWeave, Crusoe, DigitalOcean, Gcore, Pinterest [[G-18]](#ref-g-18)

**연구 동향**
- KubeCon 2026: DRA·llm-d·Grove·AI Runway 4개 프로젝트가 동시에 CNCF 편입 — GPU 오케스트레이션 표준화 단계 공식 진입
- Prefill/Decode 분리 + 이종 하드웨어 추상화(NVIDIA GPU + Groq LPU + AMD GPU)가 차세대 추론 최적화 핵심 방향

#### 시장 수요 (voice-of-market)

> GTC 2026·KubeCon Europe 2026 커버리지 기반 수요 시그널.

**고객 페인포인트**
- 단일 GPU 아키텍처의 워크로드 부적합 — 훈련·추론·에이전트 오케스트레이션 혼용으로 활용률 저하 — 출처: Cloud News GTC 2026 보도
- 추론 비용 시그널 단절 — 전용 추론 하드웨어 분리 시 FinOps 가시성 소실 — 출처: Rack2Cloud GTC 2026 분석
- Device Plugin 기반 스케줄링의 토폴로지(NUMA, NVLink) 인식 불가 — 출처: Rafay, KubeCon 2026 커버리지
- AI 실무자와 클라우드 네이티브 엔지니어 간 조직 문화 격차(CNCF 조사: 최대 장벽) — 출처: CNCF Blog(3/26)

**도입 장벽**
- NVIDIA/CUDA 생태계 락인 — 대안 하드웨어 전환 시 오케스트레이터 미지원
- FinOps 방법론이 토큰 소비 기반 추론 비용 추적 미지원
- AI 특화 메트릭(TTFT, 큐 깊이)이 기존 Prometheus/Grafana 스택과 미통합

**시장 니즈**
- 선언적 GPU 오케스트레이션 인터페이스(Grove 방식) — 인프라 세부사항 없이 추론 파이프라인 선언
- DRA 기반 토폴로지 인식 세밀 GPU 할당(NUMA/NVLink 지원)
- 하이브리드(온프레미스+클라우드) 이식성을 갖춘 단일 오케스트레이션 레이어

#### 전략적 시사점

**기회**
- NVIDIA의 오픈소스 전환(DRA/KAI/Grove)으로 벤더 중립 하이브리드 GPU 클러스터 구축 비용·복잡성 감소. 조기 도입 시 선점 우위.
- MS AI Runway + Dynamo + llm-d 조합이 K8s 네이티브 추론 플랫폼의 de facto stack으로 수렴 가능. 내부 플랫폼 아키텍처 정렬 시점.
- SkyPilot 패턴(단일 YAML + Kueue + 팀별 비용 추적)은 통신사 내부 AI 인프라 운영에 즉시 적용 가능한 참조 아키텍처.

**위협**
- GPU 오케스트레이션 표준 경쟁(llm-d vs. Grove vs. AI Runway)이 단기 분열 위험. 잘못된 플랫폼 선택 시 새로운 형태의 락인.
- Nscale 등 수직 통합 GPU 클라우드($14.6B 밸류)가 가격 전쟁 심화 — 자체 GPU 클러스터 TCO 정당화 어려워지는 구조.
- Groq 3 LPX + Vera Rubin 이종 조합의 운영 복잡성이 오케스트레이션 레이어의 투명한 추상화 없이 증가.

---

## 경쟁사 동향 (SKT / KT)

> 이번 주 Agentic AI 도메인 관련 SKT·KT 신규 뉴스 없음. MWC 2026(3월 초) 발표의 후속 정착 단계.

### SKT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| MWC26 풀스택 AI 전시 (3월 초) | AI-RAN, 온디바이스 AI 안테나 최적화, 에이전틱 AI 서비스 시연 | agent-orchestration, 5g-6g-ai-ran | [[E-01]](#ref-e-01) |
| A.X K1 519B 모델 | 한국 최초 519B 파라미터 LLM, 정부 자율형 AI 기반모델 2단계 진출 | ondevice-slm | [[E-02]](#ref-e-02) |

### KT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| 에이전트 빌더 공개 (MWC26, 3/3) | 노코드 AI 에이전트 제작 플랫폼. RAG 모듈화, 드래그앤드롭 설계·배포 | agent-orchestration, adaptive-rag | [[E-03]](#ref-e-03) |
| K GPUaaS 구독형 서비스 | 월 구독형 GPU 서비스 + 온프레미스 AI GPU Managed 서비스 | gpu-orchestration | [[E-03]](#ref-e-03) |

### 시사점
- SKT·KT 모두 MWC26에서 에이전틱 AI 전략을 공개했으나, 이번 주(W15) 추가 발표 없음. 글로벌 프레임워크 4강(OpenAI·MS·Google·Anthropic)의 프로덕션 업데이트 속도 대비 국내 통신사의 자체 플랫폼 개발 속도 격차 모니터링 필요.

---

## 규제 & 거버넌스

### 시행 임박 / 카운트다운

| 규제 | 시행일 | D-day |
|------|--------|-------|
| 한국 AI 기본법 (인공지능 발전과 신뢰 기반 조성 등에 관한 기본법) | 2026-01-22 | 시행 중 (계도기간) |
| EU AI Act — GPAI (General-Purpose AI) 모델 투명성·기술 문서 의무 | 2026-03-01 | **시행 중** (3월부터 집행 개시) |
| EU AI Act — 고위험 AI 시스템 (Annex III) | 2026-08-02 | D-125 |
| EU AI Act — 제품 안전 AI (Annex I) | 2027-08-02 | D-490 |

### 신규 발의 & 가이드라인

- **EU AI Act GPAI 투명성 의무 집행 개시(3월)**: 2026년 3월이 GPAI 모델 제공자의 투명성·기술 문서 의무가 실제 집행되는 첫 달. 합성 콘텐츠 마킹·라벨링 실행 규범 2차 초안(3/3) 공개. [[G-25]](#ref-g-25)
- **EU Council AI Act 간소화 합의(3/13)**: EU 이사회가 AI Act 규정 간소화에 합의. 고위험 AI 시스템 적용 기한을 최대 16개월 연장 가능성 — 위원회가 필요 표준·도구 준비 완료를 확인한 후 적용 시점 조정. [[G-26]](#ref-g-26)
- **한국 AI 기본법 시행령 제정안 입법예고**: 고영향 AI 범위, 영향 평가 절차, 해외 빅테크 국내 대리인 지정 등 세부 규정 마련 중. 범용 에이전트의 고영향 분류 여부를 둘러싼 정부·업계·시민단체 해석 상충 지속. 실제 과태료 부과는 2027년 이후 예상. [[G-27]](#ref-g-27)

### 시사점
- EU AI Act GPAI 투명성 의무가 3월부터 활성화되어 에이전틱 AI 서비스의 모델 문서화 의무가 현실화. 자사 서비스가 EU 시장 대상인 경우 즉시 대응 필요.
- EU 이사회의 고위험 AI 기한 연장 가능성은 준비 시간 확보라는 점에서 긍정적이나, 불확실성 증가로 오히려 투자 결정 지연 위험.

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **GPU 오케스트레이션 + 에이전트 오케스트레이션의 수렴**: KubeCon에서 NVIDIA가 "에이전트 오케스트레이션 병목이 GPU 연산이 아닌 태스크 조율에서 발생"한다고 지적. Grove API의 "복잡한 추론 시스템 단일 선언형 표현"은 멀티에이전트 추론 파이프라인의 GPU 자원 관리 문제를 직접 해결하려는 시도. 두 레이어의 통합 설계가 차세대 AI 인프라 핵심.

2. **오픈 표준화의 동시 진행**: GPU 레이어(DRA→CNCF, llm-d→CNCF)와 에이전트 레이어(MCP→AAIF, A2A v0.3 gRPC)가 같은 주에 오픈 표준화를 완료. 벤더 중립 인프라 구축의 현실성이 한 단계 높아짐. 다만 표준 경쟁(Grove vs. llm-d vs. AI Runway / MCP vs. A2A) 정리에는 시간 필요.

3. **거버넌스 레이어의 부상**: 에이전트(LangSmith Fleet, IBM AgentOps, Talkdesk CXA)와 GPU(KAI Scheduler, AI Runway 비용 추정) 모두에서 관찰성·정책 제어·비용 추적이 핵심 기능으로 부상. Gartner의 "40%+ 에이전트 프로젝트 실패" 경고와 맞물려 거버넌스 없는 배포는 리스크.

### 후속 조치 제안

- 🟡 NVIDIA DRA/Grove/KAI 스택 내부 검토 — 자사 K8s 클러스터 적용 가능성 평가 → gpu-orchestration
- 🟡 MCP + A2A 듀얼 프로토콜 아키텍처 설계 — MS Agent Framework GA 시점에 맞춰 내부 에이전트 인프라 정렬 → agent-orchestration
- ⚪ EU AI Act GPAI 투명성 의무 대응 검토 — 모델 문서화·합성 콘텐츠 마킹 요건 파악 → 전체

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | OpenAI Agents SDK Release Changelog — v0.13.2 | [링크](https://openai.github.io/openai-agents-python/release/) | release | 2026-03-26 | [A] |
| <a id="ref-g-02"></a>G-02 | Microsoft Foundry Blog — Agent Framework RC | [링크](https://devblogs.microsoft.com/foundry/microsoft-agent-framework-reaches-release-candidate/) | blog | 2026-02-19 | [A] |
| <a id="ref-g-03"></a>G-03 | LangChain Blog — Introducing LangSmith Fleet | [링크](https://blog.langchain.com/introducing-langsmith-fleet/) | blog | 2026-03-19 | [A] |
| <a id="ref-g-04"></a>G-04 | Google Cloud Blog — A2A Protocol Getting Upgrade (gRPC) | [링크](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade) | blog | 2026-03 | [A] |
| <a id="ref-g-05"></a>G-05 | AWS What's New — Bedrock AgentCore Stateful MCP | [링크](https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-bedrock-agentcore-runtime-stateful-mcp/) | release | 2026-03 | [A] |
| <a id="ref-g-06"></a>G-06 | The New Stack — Anthropic's Madcap March: 14+ launches | [링크](https://thenewstack.io/anthropic-march-2026-roundup/) | news | 2026-03 | [B] |
| <a id="ref-g-07"></a>G-07 | IBM — watsonx Orchestrate Agentic Workflows & Domain Agents | [링크](https://www.ibm.com/new/announcements/new-agentic-workflows-and-domain-agents-in-ibm-watsonx-orchestrate) | press | 2026-03 | [A] |
| <a id="ref-g-08"></a>G-08 | DeepSeek API Docs — V3.2 Release | [링크](https://api-docs.deepseek.com/news/news251201) | release | 2025-12 | [A] |
| <a id="ref-g-09"></a>G-09 | Axis Intelligence — Agentic AI Adoption Statistics 2026 | [링크](https://axis-intelligence.com/agentic-ai-adoption-statistics-2026/) | report | 2026-03 | [B] |
| <a id="ref-g-10"></a>G-10 | SiliconAngle — Tess AI $5M Enterprise Agent Orchestration | [링크](https://siliconangle.com/2026/03/02/tess-ai-raises-5m-expand-enterprise-agent-orchestration-platform/) | news | 2026-03-02 | [B] |
| <a id="ref-g-11"></a>G-11 | GlobeNewswire — Talkdesk CXA Operations Center | [링크](https://www.globenewswire.com/news-release/2026/03/10/3253040/0/en/Talkdesk-enables-enterprises-to-confidently-manage-AI-and-human-agents-as-one-workforce.html) | press | 2026-03-10 | [A] |
| <a id="ref-g-12"></a>G-12 | NVIDIA Blog — Advancing Open Source AI, DRA Driver CNCF | [링크](https://blogs.nvidia.com/blog/nvidia-at-kubecon-2026/) | news | 2026-03-24 | [A] |
| <a id="ref-g-13"></a>G-13 | NVIDIA Developer — Grove Open-Source Kubernetes API | [링크](https://developer.nvidia.com/grove) | news | 2026-03-24 | [A] |
| <a id="ref-g-14"></a>G-14 | GitHub — KAI Scheduler CNCF Sandbox | [링크](https://github.com/cncf/sandbox/issues/372) | news | 2026-03-24 | [A] |
| <a id="ref-g-15"></a>G-15 | CNCF Blog — Welcome llm-d to the CNCF | [링크](https://www.cncf.io/blog/2026/03/24/welcome-llm-d-to-the-cncf-evolving-kubernetes-into-sota-ai-infrastructure/) | news | 2026-03-24 | [A] |
| <a id="ref-g-16"></a>G-16 | Microsoft Open Source Blog — KubeCon Europe 2026 AI Runway | [링크](https://opensource.microsoft.com/blog/2026/03/24/whats-new-with-microsoft-in-open-source-and-kubernetes-at-kubecon-cloudnativecon-europe-2026/) | news | 2026-03-24 | [A] |
| <a id="ref-g-17"></a>G-17 | Rafay — Kubernetes GPUs First-Class: DRA, Scheduling, Isolation | [링크](https://rafay.co/ai-and-cloud-native-blog/advancing-gpu-scheduling-and-isolation-in-kubernetes) | blog | 2026-03-24 | [B] |
| <a id="ref-g-18"></a>G-18 | NVIDIA Technical Blog — Dynamo 1.0 Production Ready | [링크](https://developer.nvidia.com/blog/nvidia-dynamo-1-production-ready/) | news | 2026-03-16 | [A] |
| <a id="ref-g-19"></a>G-19 | Nscale Press Release — Series C $2B | [링크](https://www.nscale.com/press-releases/nscale-series-c) | news | 2026-03-09 | [A] |
| <a id="ref-g-20"></a>G-20 | Shopify Engineering — SkyPilot Multi-cloud GPUs | [링크](https://shopify.engineering/skypilot) | blog | 2026-03-01 | [B] |
| <a id="ref-g-21"></a>G-21 | NVIDIA Technical Blog — Inside Groq 3 LPX | [링크](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | news | 2026-03-16 | [A] |
| <a id="ref-g-22"></a>G-22 | Pure Storage Blog — KVA + NVIDIA Dynamo Integration | [링크](https://blog.purestorage.com/news-events/pure-kva-integrates-nvidia-dynamo-for-scalable-low-latency-llm-inference/) | news | 2026-03-01 | [B] |
| <a id="ref-g-23"></a>G-23 | Fortune Business Insights — GPU as a Service Market | [링크](https://www.fortunebusinessinsights.com/gpu-as-a-service-market-107797) | report | 2026-01 | [B] |
| <a id="ref-g-24"></a>G-24 | Virtualization Review — NVIDIA, AWS, Google Cloud at GTC 2026 | [링크](https://virtualizationreview.com/articles/2026/03/20/nvidia-aws-and-google-cloud-spotlight-ai-infrastructure-push-at-gtc-2026.aspx) | news | 2026-03-20 | [B] |
| <a id="ref-g-25"></a>G-25 | Kennedys Law — EU AI Act Implementation Timeline Next Deadline | [링크](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-eu-ai-act-implementation-timeline-understanding-the-next-deadline-for-compliance/) | news | 2026-03 | [B] |
| <a id="ref-g-26"></a>G-26 | EU Council — Agrees Position to Streamline AI Rules (3/13) | [링크](https://www.consilium.europa.eu/en/press/press-releases/2026/03/13/council-agrees-position-to-streamline-rules-on-artificial-intelligence/) | press | 2026-03-13 | [A] |
| <a id="ref-g-27"></a>G-27 | 김·장 법률사무소 — 인공지능기본법 최신 동향 | [링크](https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=33598) | news | 2026-03 | [B] |
| <a id="ref-e-01"></a>E-01 | SKT 뉴스룸 — AI 인프라·모델·서비스 풀스택 AI MWC26 | [링크](https://news.sktelecom.com/221927) | press | 2026-03 | [A] |
| <a id="ref-e-02"></a>E-02 | SKT 뉴스룸 — 5천억 파라미터 A.X K1 | [링크](https://news.sktelecom.com/217811) | press | 2026-03 | [A] |
| <a id="ref-e-03"></a>E-03 | EBN — KT MWC26 에이전트 빌더·K GPUaaS 공개 | [링크](https://www.ebn.co.kr/news/articleView.html?idxno=1701419) | news | 2026-03-04 | [B] |
