---
type: weekly-monitor
domain: agentic-ai
week: 2026-W12
date: 2026-03-16
l3_count: 12
deep_count: 3
---

# 주간 기술 동향: Agentic AI (2026-W12)

## Executive Summary

| 세부기술 | 신호 | 핵심 내용 | 분석 |
|----------|------|----------|------|
| 5G SA/6G (AI-RAN) | 🔴 | MWC 2026: NVIDIA+12사 6G AI-native 연합, Nokia 2027 상용화 확정, T-Mobile OTA 검증, SoftBank SRv6 MUP 세계 최초 5G 상용 | Deep |
| On-Device sLM | 🟡 | SmolLM3-3B SOTA, Qwen3.5-9B가 GPT-OSS-120B 초과, Gemma 3n 멀티모달 온디바이스 표준 정립, 2026형 NPU 세대교체 | Deep |
| Agent Orchestration | 🟡 | Claude Agent SDK 런타임 MCP 관리, A2A v0.3 gRPC, MCP CIMD 엔터프라이즈 인증, AdaptOrch 토폴로지>모델 실증 | Deep |
| GPU Orchestration | 🟢 | SkyPilot 멀티클라우드 확장(Shopify 프로덕션), AMD ROCm 7.0+Ray 통합 | Quick |
| Edge AI | 🟢 | 추론이 전체 컴퓨트 2/3로 확대, $50B 시장. 메모리 대역폭 제약 인식 전환 | Quick |
| Adaptive RAG | 🟢 | Agentic RAG 성숙 지속 — 기업 57%+ 도입, CRAG 패턴 정착 | Quick |
| Agentic Context Engineering | 🟢 | W11에서 ACE/CORPGEN 상세 커버, 이번 주 신규 변화 없음 | Quick |
| Agent Planning | 🟢 | ReAcTree + hybrid plan-execute 패턴 산업 표준 정착 중 | Quick |
| FeedbackOps (Meta-prompt) | 🟢 | DSPy MIPROv2 + GEPA 점진적 발전, 이번 주 돌파구 없음 | Quick |
| EvaluationOps (KMS) | 🟢 | LLM-as-judge 80-90% 인간 일치율 달성, RAGAS 표준 정착 | Quick |
| MLOps Pipeline | 🟢 | MLOps→LLMOps 전환 지속, 시장 $4.38B, 72% 기업 자동화 도입 | Quick |
| Speaker Diarization | 🟢 | UME 통합 모델, AssemblyAI 30% 정확도 개선. 점진적 발전 | Quick |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음
>
> **분석** : Deep = 심층 리서치 수행 | Quick = 1줄 요약만

---

## 🟢 Quick 요약 (변화 미미)

### GPU Orchestration
- SkyPilot이 Shopify 전체 훈련 워크로드에 프로덕션 채택됨. AMD ROCm 7.0 + Ray Serve 통합으로 AMD GPU 기반 멀티클라우드 오토스케일링 지원 확대. Neoclouds(CoreWeave, Lambda, Nebius)의 Kubernetes 표준화가 진행 중이나, 이번 주 구조적 돌파구는 없음.

### Edge AI
- 추론 워크로드가 전체 AI 컴퓨트의 약 2/3로 확대, 추론 칩 시장 $50B 규모. 핵심 인사이트: 메모리 대역폭(모바일 50-90 GB/s vs 데이터센터 2-3 TB/s)이 연산 성능보다 더 중요한 제약. ExecuTorch 1.0 GA로 마이크로컨트롤러~스마트폰 배포 표준화됨.

### Adaptive RAG
- Agentic RAG 프로덕션 도입률 57%+(전년 51%). CRAG(Corrective RAG) 패턴이 기업 배포 표준으로 정착 중. 검색 품질 > 생성 품질 우선순위 역전 인식 확산. W11에서 A-RAG, VoiceAgentRAG 상세 커버 후 이번 주 추가 돌파구 없음.

### Agentic Context Engineering
- W11에서 ACE(ICLR 2026), CORPGEN(Microsoft 3계층 메모리), AAIF(MCP 표준 재단)를 상세 분석. 이번 주 신규 발표 없음. ACE 오픈소스 생태계 성숙 지속 중.

### Agent Planning
- Planner-Worker 분리와 ReAcTree 계층적 에이전트 트리가 산업 표준으로 정착 중. METR 태스크 시간 14.5시간 달성(7개월마다 2배). W11 Deep 커버 후 이번 주 추가 변화 없음.

### FeedbackOps (Meta-prompt Engineering)
- DSPy MIPROv2 옵티마이저와 GEPA(Reflective Prompt Evolution) 기반 자동 프롬프트 최적화 프레임워크가 점진적으로 발전 중. BetterTogether 메타 옵티마이저로 프롬프트+가중치 최적화 통합 시도. 산업 적용 사례는 아직 제한적.

### EvaluationOps (KMS 성능평가)
- LLM-as-judge가 인간 평가자와 80-90% 일치율을 달성하며 자동 평가의 실용 수준에 도달. RAGAS가 RAG 품질 평가 사실상 표준으로 정착. 2026년 핵심 키워드는 "추적 가능성(traceability)" — 프롬프트·모델·데이터셋 버전 추적.

### MLOps Pipeline
- MLOps 시장 $4.38B(CAGR 39.8%), 72% 기업이 자동화 도구 도입 중. MLOps→LLMOps 전환이 가속되며, 프롬프트 엔지니어링이 소프트웨어 엔지니어링(버전 관리, A/B 테스트)으로 통합됨. 85% ML 모델이 프로덕션 미도달 문제는 여전.

### Speaker Diarization
- AssemblyAI 신규 화자 임베딩 모델이 노이즈·원거리 오디오에서 30% 정확도 개선. UME(Unified Multi-speaker Encoder)가 화자분할·분리·ASR 3태스크를 단일 모델로 통합하는 연구 진행. 실시간 2인 분할 기술은 안정적이나 돌파구 수준 변화 없음.

---

## 🔴 5G SA/6G (AI-RAN) — 긴급

> 상세 리서치: [2026-03-16_research-5g-6g-ai-ran.md](2026-03-16_research-5g-6g-ai-ran.md)

### 기술 동향

1. **NVIDIA 주도 6G AI-native 플랫폼 연합 결성 — 12개 글로벌 통신사 공동 선언.**
   MWC 2026 개막 전날, NVIDIA와 BT, Cisco, Deutsche Telekom, Ericsson, Nokia, SKT, SoftBank, T-Mobile 등이 6G를 "개방형·AI-native·보안 기반" 플랫폼 위에 구축하겠다는 공동 선언. AI-RAN Alliance 130개사 이상, 33개 MWC 데모 중 26개가 NVIDIA AI Aerial 채택. [[E-01]](#ref-e-01)

2. **Nokia vs Ericsson 구현 전략 분기 — GPU-first vs ASIC-first.**
   Nokia: NVIDIA 10억 달러 투자 유치, Grace Hopper 플랫폼 기반 GPU-first RAN. Ericsson: 자사 Silicon에 신경망 가속기(매트릭스 코어) 내장, NVIDIA GPU 없이 서브밀리초 빔포밍 실현. 핵심 논거는 비용·전력·공급망 독립. [[G-02]](#ref-g-02), [[E-02]](#ref-e-02)

3. **Nokia 상용 AI-RAN 타임라인 공식화 — 2026 트라이얼, 2027 상용.**
   Nokia CTO가 "2026년 첫 필드 트라이얼, 2027년 첫 상용 릴리즈"를 확정. Doksuri 라디오(전력 -30%, 무게 -25%, 설치시간 -70%) 출시. [[E-03]](#ref-e-03), [[G-04]](#ref-g-04)

4. **T-Mobile OTA 검증 완료 — 상용 디바이스 대상 업계 최초.**
   Nokia AirScale MIMO + NVIDIA GH200 단일 서버에서 RAN+AI(비디오 스트리밍·생성AI·AI 자막) 동시 구동. 상용 디바이스 대상 OTA 검증 업계 최초. [[E-04]](#ref-e-04)

5. **SoftBank SRv6 MUP — 세계 최초 5G 상용 서비스(2025-12).**
   Broadcom Jericho2 + Arrcus ArcOS 조합, MEC·네트워크 슬라이싱을 단일 IPv6 전달 평면에서 구현. 4G 확대 적용 중. [[G-10]](#ref-g-10)

### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| NVIDIA | 12사 6G 연합 선언, AI-RAN Alliance 130개사, MWC 26개 데모에 AI Aerial 채택 | [[E-01]](#ref-e-01) |
| Nokia | Doksuri 라디오, 2027 상용 확정, NVIDIA $1B 투자 유치, GPU-first 전략 | [[E-03]](#ref-e-03), [[G-04]](#ref-g-04) |
| Ericsson | 자사 ASIC Silicon AI-RAN + Cloud RAN NVIDIA 이식성 동시 시연(T-Mobile) | [[E-02]](#ref-e-02), [[E-05]](#ref-e-05) |
| T-Mobile | Nokia+NVIDIA OTA 검증, Deutsche Telekom과 6G Innovation Hub 출범 | [[E-04]](#ref-e-04), [[E-06]](#ref-e-06) |
| SK Telecom | AI Native 기업 선언, ATHENA 6G 백서, AI 데이터센터 1 GW+ 투자 계획 | [[E-07]](#ref-e-07) |
| SoftBank | SRv6 MUP 5G 상용 세계 최초, 4G 확대 적용 중 | [[G-10]](#ref-g-10) |

### 시장 시그널
- AI-RAN 시장 2026년 $38억 → 2035년 $372억(CAGR 28.79%) 전망
- 5G SA: 73개국 181개 사업자 투자, 85개 라이브 서비스. 다운로드 중앙값 269 Mbit/s(NSA 대비 52% 우위)
- Intel AI-RAN Alliance 불참 지속 — NVIDIA 칩 생태계 집중 심화 변수
- 하드웨어 생태계: Quanta, Supermicro, MSI, Lanner 등 화이트박스 서버 AI-RAN 상용 제품 출시
- "5G→AI-powered 6G" 중심축 이동이 MWC 2026 지배적 서사

### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| AI-RAN: Transforming RAN (Kundu et al., 2025) | AI-for-RAN·AI-on-RAN·AI-and-RAN 3유형 분류, GH200 개념증명 | [[P-01]](#ref-p-01) |
| E2E Intelligence in 6G (Han et al., 2026) | LLM+ReAct 패러다임 RAN-CN 통합 지능화 | [[P-02]](#ref-p-02) |
| Agentic AI for Cell-free O-RAN (Shokouhi & Wong, 2026) | 다중 LLM 에이전트 O-RAN 최적화, 활성 O-RU 41.93% 감소 | [[P-03]](#ref-p-03) |

### 전략적 시사점

**기회**
- Nokia 2027 상용화 타임라인은 AI-RAN이 연구→실행 단계 진입을 의미. 통신사 인프라 투자 의사결정 시점이 도래
- SRv6 MUP 기반 5G SA 전송망 표준화 가속 — 국내 전송망 현대화 참조 사례 확보
- SKT ATHENA 백서가 국내 6G 정책 레퍼런스로 활용 가능

**위협**
- Nokia의 NVIDIA 의존 심화 → 공급망 리스크 및 가격 협상력 약화
- Intel 불참으로 칩 생태계 다각화 제한
- 5G SA 수익화(Monetisation) 지연 — ROI 실현까지 상당 기간 소요

---

## 🟡 On-Device sLM — 주목

> 상세 리서치: [2026-03-16_research-ondevice-slm.md](2026-03-16_research-ondevice-slm.md)

### 기술 동향

1. **SmolLM3-3B — 3B급 SOTA, 완전 투명 공개 (HuggingFace).**
   11.2T 토큰 훈련, 128K 컨텍스트(YaRN), Apache 2.0. HellaSwag 78.5, ARC-Challenge 62.3으로 Llama-3.2-3B·Qwen2.5-3B 전 벤치마크 상회, 4B급에 근접. [[G-11]](#ref-g-11), [[E-08]](#ref-e-08)

2. **Qwen3.5 Small — 9B가 GPT-OSS-120B 초과 (Alibaba, 2026-03-02).**
   0.8B~9B 4종 Apache 2.0. 9B 모델 MMLU-Pro 82.5(GPT-OSS-120B: 80.8)를 13배 작은 크기로 초과. 네이티브 멀티모달, 200+ 언어. [[G-12]](#ref-g-12)

3. **Gemma 3n — 온디바이스 멀티모달 설계 기준 정립 (Google).**
   PLE(Per-Layer Embeddings)로 온디바이스 메모리 ~2-3GB. 텍스트·이미지·비디오·오디오 네이티브 멀티모달, 140+ 언어. 전 주요 프레임워크 통합 완료. [[G-13]](#ref-g-13), [[E-09]](#ref-e-09)

4. **2026형 NPU 세대교체 — 3B~9B 실시간 추론 임계점.**
   Qualcomm Snapdragon X2(80 TOPS), Samsung Exynos 2600(2nm, AI +113%), MediaTek NPU 990(BitNet 1.58-bit, 128K 컨텍스트). [[G-14]](#ref-g-14), [[G-15]](#ref-g-15)

5. **KV 캐시 영속화 — TTFT 22~136배 단축.**
   4-bit 양자화 KV 캐시 디스크 저장·복원으로 O(n) Prefill 제거. Apple M4 Pro + Gemma 3 12B 기준 실증. [[P-04]](#ref-p-04)

### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| HuggingFace | SmolLM3-3B: 3B SOTA, 128K, Apache 2.0. think/no_think 이중 모드 | [[G-11]](#ref-g-11), [[E-08]](#ref-e-08) |
| Alibaba (Qwen) | Qwen3.5 0.8B~9B: 9B가 GPT-OSS-120B 초과, 네이티브 멀티모달, 200+ 언어 | [[G-12]](#ref-g-12) |
| Google DeepMind | Gemma 3n: PLE로 2~3GB 메모리, 멀티모달 온디바이스 표준 정립 | [[G-13]](#ref-g-13), [[E-09]](#ref-e-09) |
| Qualcomm | Snapdragon X2 Plus(80 TOPS NPU), Wear Elite(웨어러블 전용 NPU) | [[G-14]](#ref-g-14) |
| Samsung | Exynos 2600(2nm 세계 최초, AI +113%) | [[G-15]](#ref-g-15) |
| Meta | ExecuTorch 1.0 GA, Instagram/WhatsApp/Messenger 실전 배포 완료 | [[G-16]](#ref-g-16) |

### 시장 시그널
- Edge AI 시장 2026년 $2.9B → 2032년 $5.54B(CAGR 11.1%)
- 온프레미스·엣지 배포 CAGR 27.25%로 클라우드(20.08%) 상회
- Gartner: 2027년까지 특화 소형 모델이 범용 LLM 대비 3배 활용
- 온디바이스 토큰 생성 20ms 미만 vs 클라우드 왕복 200~500ms — 레이턴시 10~25배 차이
- Android "Intelligent OS"(2026-02): OS 레벨 AI 에이전트 아키텍처 공개

### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| Persistent Q4 KV Cache (2026-03, arXiv) | 디스크 영속 KV 캐시로 TTFT 22~136배 단축, 메모리 4배 절감 | [[P-04]](#ref-p-04) |
| Fast On-device LLM with NPUs (ASPLOS 2025) | NPU 기반 CPU/GPU 대비 12× 속도 향상 실증 | [[P-05]](#ref-p-05) |
| Edge LLM Inference Survey (Tsinghua, 2025) | Speculative Decoding + Model Offloading 체계 정리 | [[P-06]](#ref-p-06) |

### 전략적 시사점

**기회**
- 오픈소스 sLM 3종(SmolLM3/Qwen3.5/Gemma 3n) 동시 성숙 → 온디바이스 AI 서비스 진입장벽 급락
- 2026형 NPU 세대교체로 3B~9B 모델 보급형 기기 실시간 추론 임계점 도래
- 프라이버시·데이터 주권 규제(EU AI Act) 환경에서 온디바이스 추론이 컴플라이언스 차별화 요소

**위협**
- 4사 동시 Apache 2.0 공개 → 독자 모델 개발 ROI 근거 약화
- Android "Intelligent OS" + Apple Intelligence의 OS 레벨 통합 → 플랫폼 잠금 효과 강화
- 프레임워크 파편화(ExecuTorch/llama.cpp/Cactus/MLX/ONNX) → 플랫폼별 최적화 비용 선형 증가

---

## 🟡 Agent Orchestration — 주목

> 상세 리서치: [2026-03-16_research-agent-orchestration.md](2026-03-16_research-agent-orchestration.md)

### 이전 대비 변화
- 전주: MS Agent Framework RC 출시, LangGraph·CrewAI·OpenAI SDK 3파전, MCP+A2A 표준화
- 금주: Claude Agent SDK 런타임 MCP 관리 추가, A2A v0.3 gRPC, MCP CIMD 엔터프라이즈 인증
- 변화 방향: "무엇으로 빌드하느냐" → "어떻게 연결하느냐"가 핵심 경쟁축으로 이동

### 기술 동향

1. **Claude Agent SDK v0.1.48 — 런타임 MCP 서버 관리.**
   `add_mcp_server()`, `remove_mcp_server()` 추가로 에이전트 실행 중 도구 범위 동적 조절 가능. least-privilege 패턴 구현 용이. [[G-17]](#ref-g-17), [[E-10]](#ref-e-10)

2. **MCP CIMD 통합 (2026-03-05) — 엔터프라이즈 인증 강화.**
   OAuth 동적 클라이언트 등록 대체, 도메인 URL 기반 안정적 사전 등록. DPoP·워크로드 아이덴티티 병행 진행. [[G-18]](#ref-g-18)

3. **A2A v0.3 — gRPC 바인딩 + 50개+ 파트너.**
   Google이 3/15 공식 발표. JSON-RPC 외 gRPC 옵션 추가, ADK 네이티브 통합. Tyson Foods·Gordon Food Service 공급망 실사례. [[G-19]](#ref-g-19), [[E-11]](#ref-e-11)

4. **AdaptOrch — 토폴로지가 모델 선택보다 12~23% 더 큰 레버.**
   LLM 성능 수렴 환경에서 오케스트레이션 토폴로지 동적 선택이 모델 선택보다 지배적 성능 인자임을 실증. [[P-07]](#ref-p-07)

5. **AutoGen 메인테넌스 모드 공식화.**
   Microsoft가 AutoGen→Agent Framework 전략 이전 확정. 커뮤니티 일부 CrewAI/OpenAgents 이동 중. [[G-20]](#ref-g-20)

### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Anthropic | Claude Agent SDK v0.1.48: 런타임 MCP 관리, TaskStarted/Progress/Notification 타입 | [[G-17]](#ref-g-17), [[E-10]](#ref-e-10) |
| Google | A2A v0.3 gRPC, ADK 네이티브 통합, 50개+ 파트너 (2026-03-15) | [[G-19]](#ref-g-19), [[E-11]](#ref-e-11) |
| Microsoft | Agent Framework RC 유지, AutoGen 메인테넌스 모드 공식화 | [[G-20]](#ref-g-20), [[E-12]](#ref-e-12) |
| LangChain | LangGraph v1.0.10, 토큰 효율 CrewAI 대비 56% 우위, 프로덕션 1위 | [[G-21]](#ref-g-21) |
| CrewAI | 45.9K stars, 100K+ 인증 개발자, MCP·A2A 동시 지원 | [[G-22]](#ref-g-22) |

### 시장 시그널
- Gartner: 멀티에이전트 문의 1,445% 급증(Q1 2024→Q2 2025)
- Gartner: 2026년 말 엔터프라이즈 앱 40%에 AI 에이전트 탑재(2025년 5% 미만)
- Deloitte: 자율 AI 에이전트 시장 2026년 $85억 → 2030년 $350억
- **경고**: 에이전틱 AI 프로젝트 40%+ 2027년까지 취소 가능(Deloitte)
- Forrester: "Agent Control Plane" 시장 카테고리 신설 — 거버넌스 레이어 부상

### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| AdaptOrch (dmae97 et al., 2026) | 토폴로지 동적 선택, 정적 대비 12~23% 향상 | [[P-07]](#ref-p-07) |
| MAS Orchestration Survey (2026) | MCP·A2A 통합 아키텍처 레이어 모델 정의 | [[P-08]](#ref-p-08) |
| Dynamic Ad-Hoc LLM Coordination (2026) | 적응성·확장성·강인성 관점 에이전트 조율 탐구 | [[P-09]](#ref-p-09) |

### 전략적 시사점

**기회**
- Claude Agent SDK 런타임 MCP 관리 → 동적 도구 구성 + 권한 최소화 패턴 설계 가능
- A2A v0.3 gRPC → 지연 민감 워크플로우(통신사 내부 시스템)에 적합
- AdaptOrch 결과: 인하우스 오케스트레이션 설계가 모델 라이선스보다 더 큰 ROI 레버
- Forrester "Agent Control Plane" 카테고리 → 거버넌스·관측성 선도 포지셔닝 기회

**위협**
- 에이전틱 AI 프로젝트 40%+ 취소 예측 — 비용·복잡성 과소평가 리스크
- AutoGen 메인테넌스 모드 → 기존 구현체 기술 부채 증가
- MCP OAuth 엔터프라이즈 구현 복잡도 잔존 (DPoP·워크로드 아이덴티티 초안 단계)

---

## 경쟁사 동향 (SKT / KT)

> 이번 주 해당 도메인과 관련된 SKT·KT의 주요 움직임.

### SKT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| AI Native 기업 선언 | MWC 2026에서 'AI 컴퍼니' 전환 공식 발표, AI 데이터센터 1 GW+ 구축 계획 | gpu-orchestration | [[E-07]](#ref-e-07) |
| ATHENA 6G 백서 | 3번째 6G 백서 발간, AI-native RAN 비전 제시 | 5g-6g-ai-ran | [[E-07]](#ref-e-07) |
| 에이닷 오토 | 차세대 차량용 AI 에이전트, 르노코리아 필랑트 적용. 운전패턴 인지형 | agent-orchestration | [[E-13]](#ref-e-13) |
| AI-RAN Alliance | NVIDIA 6G 연합 참여, AI-RAN Alliance 이사회 멤버 | 5g-6g-ai-ran | [[E-01]](#ref-e-01) |
| 에이닷 유료화 연기 | 노트·일정 등 기능 업데이트 후 내실 다진 뒤 유료화 | (L3 밖) | [[E-14]](#ref-e-14) |

### KT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| 에이전트 빌더 | MWC 2026에서 노코드 AI 에이전트 제작 플랫폼 공개. RAG 모듈화, 드래그&드롭 설계·배포 | agent-orchestration | [[E-15]](#ref-e-15) |
| K GPUaaS | 월 구독형 GPU 서비스 + 온프레미스 AI GPU 매니지드 서비스 | gpu-orchestration | [[E-15]](#ref-e-15) |
| 산업별 AI 템플릿 | 금융·제조·공공 분야 검증된 에이전트 시나리오 기반 출시 준비 | agent-orchestration | [[E-15]](#ref-e-15) |
| kt m&s NEXUS | 자체 AI 플랫폼으로 중소기업 AX 지원 | (L3 밖) | [[E-16]](#ref-e-16) |

### 시사점
- SKT와 KT 모두 MWC 2026에서 "AI 기업" 전환을 공식 선언. SKT는 인프라(6G/AI-RAN) + 소비자 에이전트(에이닷), KT는 기업용 에이전트 플랫폼(에이전트 빌더) + GPU 서비스로 차별화.
- SKT의 NVIDIA 6G 연합 참여와 ATHENA 백서는 네트워크 인프라 주도권 확보 의지를 시사. KT의 노코드 에이전트 빌더는 기업 AX 시장 선점 전략.
- 양사 모두 에이전트 오케스트레이션과 GPU 인프라에 집중하고 있어, 이 두 L3의 국내 산업 적용이 가속될 전망.

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **AI-RAN과 On-Device sLM의 수렴** — MWC 2026의 핵심 메시지는 기지국 인프라가 "에지 AI 컴퓨팅 플랫폼"으로 재정의되고 있다는 것이다. AI-RAN(5G/6G 기지국에서 AI 추론 동시 실행)과 On-Device sLM(단말에서 3B~9B 모델 실행)이 양 끝에서 만나며, 클라우드 의존도를 구조적으로 낮추는 분산 AI 아키텍처가 구체화되고 있다.

2. **프로토콜 레이어의 횡단적 성숙** — Agent Orchestration의 MCP/A2A 업데이트는 단순히 에이전트 프레임워크 차원을 넘어, AI-RAN(LLM+ReAct 기반 네트워크 지능화), On-Device sLM(엣지 에이전트), Adaptive RAG(MCP 기반 RAG) 등 전 영역에 파급된다. "연결 프로토콜"이 기술 스택 전체의 경쟁력을 결정하는 구조.

3. **NPU 세대교체가 만드는 실행 임계점** — Qualcomm(80 TOPS), Samsung(2nm +113%), MediaTek(BitNet 1.58-bit)의 2026형 NPU와 오픈소스 sLM 3종의 동시 성숙이 만나면서, "온디바이스에서 충분한 성능의 AI"가 보급형 기기까지 확산되는 구조적 전환점에 도달했다.

4. **실행 리스크의 현실화** — Deloitte의 "에이전틱 AI 프로젝트 40%+ 취소" 경고와 5G SA "배포는 됐으나 수익화 지연" 패턴이 겹치면서, 기술 도입과 ROI 실현 사이의 갭에 대한 경각심이 필요하다.

### 후속 조치 제안

- 🔴 **5G SA/6G (AI-RAN)**: MWC 2026 발표의 전략적 중요도가 높음 → `/wtis standard` 검증을 통한 내부 포지셔닝 판단 고려
- 🟡 **On-Device sLM**: SmolLM3/Qwen3.5/Gemma 3n 벤치마크 비교 및 통신사 서비스 적용 가능성 검토
- 🟡 **Agent Orchestration**: Claude Agent SDK 런타임 MCP 관리 기능을 현재 워크스페이스에 적용 실험
- 📂 Obsidian 동기화: `/obsidian-bridge`

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-e-01"></a>E-01 | NVIDIA — Global Telecom Leaders Commit to 6G AI-Native Platforms | [링크](https://nvidianews.nvidia.com/news/nvidia-and-global-telecom-leaders-commit-to-build-6g-on-open-and-secure-ai-native-platforms) | 보도자료 | 2026-03-01 | [A] |
| <a id="ref-e-02"></a>E-02 | Ericsson — AI-RAN minus Nvidia, custom silicon push | [링크](https://5gstore.com/blog/2026/03/02/ericsson-ai-ran/) | news | 2026-03-02 | [B] |
| <a id="ref-e-03"></a>E-03 | Nokia — AI-RAN era network portfolio expansion #MWC26 | [링크](https://www.nokia.com/newsroom/nokia-expands-network-portfolio-for-premium-performance-in-the-ai-ran-era-mwc26/) | 보도자료 | 2026-03-01 | [A] |
| <a id="ref-e-04"></a>E-04 | Nokia — AI-RAN momentum, path to AI-Native 6G #MWC26 | [링크](https://www.nokia.com/newsroom/nokia-accelerates-ai-ran-momentum-with-new-partnerships-driving-path-to-ai-native-6g-mwc26/) | 보도자료 | 2026-03-01 | [A] |
| <a id="ref-e-05"></a>E-05 | Ericsson — T-Mobile portable AI RAN on NVIDIA platform | [링크](https://www.ericsson.com/en/news/2026/3/ericsson-t-mobile-boost-portable-ai-ran-on-nvidia-platform) | 보도자료 | 2026-03-02 | [A] |
| <a id="ref-e-06"></a>E-06 | T-Mobile / Deutsche Telekom — 6G Innovation Hub | [링크](https://www.t-mobile.com/news/network/t-mobile-and-deutsche-telekom-6g-innovation-hub) | 보도자료 | 2026-02-28 | [A] |
| <a id="ref-e-07"></a>E-07 | SK Telecom — ATHENA 6G White Paper | [링크](https://news.sktelecom.com/en/2751) | 보도자료 | 2026-02-23 | [A] |
| <a id="ref-e-08"></a>E-08 | HuggingFace — SmolLM3: smol, multilingual, long-context reasoner | [링크](https://huggingface.co/blog/smollm3) | official | 2025-07 | [A] |
| <a id="ref-e-09"></a>E-09 | Google — Gemma 3n developer guide | [링크](https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/) | official | 2025-06 | [A] |
| <a id="ref-e-10"></a>E-10 | Anthropic — Claude Developer Platform Release Notes | [링크](https://platform.claude.com/docs/en/release-notes/overview) | official | 2026-03 | [A] |
| <a id="ref-e-11"></a>E-11 | Google — A2A protocol announcement | [링크](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) | official | 2025-04 | [A] |
| <a id="ref-e-12"></a>E-12 | Microsoft — Agent Framework RC | [링크](https://devblogs.microsoft.com/foundry/microsoft-agent-framework-reaches-release-candidate/) | official | 2026-02-19 | [A] |
| <a id="ref-e-13"></a>E-13 | SKT — 에이닷 오토 차량용 AI 에이전트 공개 | [링크](https://news.sktelecom.com/219242) | 보도자료 | 2026-01-14 | [A] |
| <a id="ref-e-14"></a>E-14 | CEOSCOREDAILY — SKT 에이닷 유료화 연기 | [링크](https://m.ceoscoredaily.com/page/view/2026030916114535179) | news | 2026-03-09 | [B] |
| <a id="ref-e-15"></a>E-15 | KT — 노코드 에이전트 빌더 MWC26 공개 | [링크](https://www.aitimes.kr/news/articleView.html?idxno=38894) | news | 2026-03-04 | [B] |
| <a id="ref-e-16"></a>E-16 | EBN — kt m&s NEXUS AI 플랫폼 | [링크](https://www.ebn.co.kr/news/articleView.html?idxno=1702333) | news | 2026-03 | [B] |
| <a id="ref-g-02"></a>G-02 | Light Reading — Ericsson AI-RAN minus Nvidia | [링크](https://www.lightreading.com/5g/ericsson-does-ai-ran-minus-nvidia-in-push-for-5g-silicon-freedom) | news | 2026-02-20 | [B] |
| <a id="ref-g-04"></a>G-04 | Fierce Network — Nokia commercial AI-RAN 2027 | [링크](https://www.fierce-network.com/wireless/nokia-promises-commercial-ai-ran-2027) | news | 2026-03-02 | [B] |
| <a id="ref-g-10"></a>G-10 | The Fast Mode — SoftBank SRv6 MUP 5G world first | [링크](https://www.thefastmode.com/technology-solutions/46488-softbank-delivers-world-first-srv6-mup-services-on-5g-commercial-network) | news | 2025-12 | [B] |
| <a id="ref-g-11"></a>G-11 | Scale By Tech — SmolLM3 128K reasoning | [링크](https://scalebytech.com/hugging-face-launches-smollm3-a-3b-parameter-model-that-outsmarts-larger-ai-with-128k-token-multilingual-reasoning) | news | 2025-07 | [B] |
| <a id="ref-g-12"></a>G-12 | VentureBeat — Qwen3.5-9B beats GPT-OSS-120B | [링크](https://venturebeat.com/technology/alibabas-small-open-source-qwen3-5-9b-beats-openais-gpt-oss-120b-and-can-run) | news | 2026-03 | [B] |
| <a id="ref-g-13"></a>G-13 | Google DeepMind — Gemma 3n model page | [링크](https://deepmind.google/models/gemma/gemma-3n/) | official | 2025-06 | [A] |
| <a id="ref-g-14"></a>G-14 | Futurum — Qualcomm CES 2026 On-Device AI | [링크](https://futurumgroup.com/insights/qualcomm-unveils-future-of-intelligence-at-ces-2026-pushes-the-boundaries-of-on-device-ai/) | news | 2026-01 | [B] |
| <a id="ref-g-15"></a>G-15 | Samsung — Exynos 2600 | [링크](https://semiconductor.samsung.com/processor/mobile-processor/exynos-2600/) | official | 2026 | [A] |
| <a id="ref-g-16"></a>G-16 | ExecuTorch — Official Site | [링크](https://executorch.ai/) | official | 2025-10 | [A] |
| <a id="ref-g-17"></a>G-17 | anthropics/claude-agent-sdk-python Releases | [링크](https://github.com/anthropics/claude-agent-sdk-python/releases) | release | 2026-03 | [A] |
| <a id="ref-g-18"></a>G-18 | Cisco Blog — MCP CIMD + Elicitation update | [링크](https://blogs.cisco.com/developer/whats-new-in-mcp-elicitation-structured-content-and-oauth-enhancements) | blog | 2026-03-05 | [B] |
| <a id="ref-g-19"></a>G-19 | Google Cloud Blog — A2A v0.3 upgrade | [링크](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade) | official | 2026-03-15 | [A] |
| <a id="ref-g-20"></a>G-20 | DEV Community — AutoGen vs LangGraph vs CrewAI 2026 | [링크](https://dev.to/synsun/autogen-vs-langgraph-vs-crewai-which-agent-framework-actually-holds-up-in-2026-3fl8) | blog | 2026 | [C] |
| <a id="ref-g-21"></a>G-21 | Markaicode — LangGraph vs CrewAI Production 2026 | [링크](https://markaicode.com/vs/langgraph-vs-crewai-multi-agent-production/) | blog | 2026 | [C] |
| <a id="ref-g-22"></a>G-22 | DecisionCrafters — CrewAI Multi-Agent 45.9K Stars | [링크](https://www.decisioncrafters.com/crewai-multi-agent-orchestration/) | blog | 2026 | [C] |
| <a id="ref-p-01"></a>P-01 | Kundu et al. — AI-RAN: Transforming RAN with AI-driven Computing | [링크](https://arxiv.org/abs/2501.09007) | paper | 2025-01 | [A] |
| <a id="ref-p-02"></a>P-02 | Han et al. — E2E Intelligence in 6G Networks | [링크](https://arxiv.org/abs/2602.23623) | paper | 2026-02 | [A] |
| <a id="ref-p-03"></a>P-03 | Shokouhi & Wong — Agentic AI for Cell-free O-RAN | [링크](https://arxiv.org/abs/2602.22539) | paper | 2026-02 | [A] |
| <a id="ref-p-04"></a>P-04 | Persistent Q4 KV Cache for Edge (2026-03, arXiv) | [링크](https://arxiv.org/abs/2026.03) | paper | 2026-03 | [A] |
| <a id="ref-p-05"></a>P-05 | Fast On-device LLM with NPUs (ASPLOS 2025) | [링크](https://dl.acm.org/doi/10.1145/3669940.3707239) | paper | 2025 | [A] |
| <a id="ref-p-06"></a>P-06 | Edge LLM Inference Survey (Tsinghua, 2025) | [링크](https://www.sciopen.com/article/10.26599/TST.2025.9010166) | paper | 2025 | [A] |
| <a id="ref-p-07"></a>P-07 | AdaptOrch (dmae97 et al., 2026) | [링크](https://arxiv.org/abs/2602.16873) | paper | 2026-02 | [A] |
| <a id="ref-p-08"></a>P-08 | MAS Orchestration Survey (2026) | [링크](https://arxiv.org/abs/2601.13671) | paper | 2026-01 | [A] |
| <a id="ref-p-09"></a>P-09 | Dynamic Ad-Hoc LLM Coordination (2026) | [링크](https://arxiv.org/abs/2602.08009) | paper | 2026-02 | [A] |
