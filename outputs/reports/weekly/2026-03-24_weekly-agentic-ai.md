---
type: weekly-monitor
domain: agentic-ai
week: 2026-W14
date: 2026-03-24
l3_count: 12
deep_count: 4
---

# 주간 기술 동향: Agentic AI (2026-W14)

## Executive Summary

> **이번 주 핵심**: GTC 2026을 기점으로 GPU 인프라의 "학습→추론" 구조적 전환이 가속되는 가운데, 에이전트 프레임워크 4강(OpenAI·Anthropic·Google·Microsoft)이 동시다발적으로 프로덕션급 업데이트를 발표. NVIDIA Dynamo 1.0이 오픈소스 추론 OS로 정착하고, AT&T-Cisco-NVIDIA AI Grid가 에지 AI 대규모 상용 배포를 시작하면서 "클라우드→에지" 추론 인프라 이동이 현실화.

| Layer 2 | 세부기술 | 신호 | 핵심 내용 |
|---------|----------|------|----------|
| Trusted Multi-Agent Orchestration | Intelligent Agent Orchestration | 🟡 | OpenAI SDK 0.13 tool search(3/23), Claude Code Channels(3/20), Google ADK 네이티브 A2A, MS Foundry Agent Service GA(3/16) |
| | Agent Oriented Orchestration | 🟢 | ReAcTree + hybrid plan-execute 표준 정착 유지, 신규 변화 없음 |
| Model & Delta Foundry | 하이브리드 GPU Orchestration | 🟡 | NVIDIA Dynamo 1.0 GA(3/16) Blackwell 7x 추론 향상, Vera Rubin $1T 수주 전망, DDN 협업 |
| | FeedbackOps: Meta-prompt Engineering | 🟢 | DSPy MIPROv2 안정, GEPA GPT-4.1 Mini 46.6%→56.6% AIME 개선 |
| | EvaluationOps: KMS 성능평가 | 🟢 | RAGAS 표준 정착, LLM-as-judge 80-90% 인간 일치 유지 |
| | 데이터-학습-배포 파이프라인 | 🟢 | MLOps→LLMOps 전환 지속, LoRA/PEFT 엔터프라이즈 표준화 진행 |
| Hybrid AI Infra | On-Device sLM | 🟡 | OpenAI GPT-5.4 mini+nano(3/17), sLM-First 아키텍처 비용 60-70% 절감 |
| | Edge AI | 🟡 | AT&T-Cisco-NVIDIA AI Grid 상용 배포(3/17), Akamai 4,400 에지 배포, TI NPU MCU(3/10) |
| | 5G SA/6G(AI-RAN/SRv6) | 🟢 | MWC 발표 후속 정착 단계, 이번 주 신규 발표 없음 |
| | 실시간 화자분할(2인) | 🟢 | AssemblyAI Universal-3-Pro, Gladia Solaria-1 안정 유지 |
| Self Evolving Architecture | Agentic Context Engineering | 🟢 | ACE(ICLR 2026) 생태계 성숙 지속, 신규 발표 없음 |
| 의도 파악 기술 | Adaptive RAG | 🟢 | Agentic RAG 57%+ 도입 유지, CRAG 패턴 정착 |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음

---

## 🟢 Quick 요약 (변화 미미)

### Agent Oriented Orchestration
- ReAcTree + hybrid plan-execute 패턴이 산업 표준으로 정착 중. Plan-and-Execute 패턴(고추론 모델이 DAG 분해 → 경량 모델이 실행 → 재계획)이 주류. 이번 주 추가 변화 없음.

### FeedbackOps (Meta-prompt Engineering)
- DSPy MIPROv2 옵티마이저와 GEPA 기반 자동 프롬프트 최적화가 안정 운영 중. GEPA는 GPT-4.1 Mini의 AIME 2025 수학 문제에서 46.6%→56.6%(+10pp) 개선 시연. BetterTogether 메타옵티마이저(프롬프트+가중치 순차 최적화) 패턴 확산.

### EvaluationOps (KMS 성능평가)
- LLM-as-judge가 인간 평가자와 80-90% 일치율 유지. RAGAS가 RAG (Retrieval-Augmented Generation) 평가의 사실상 표준으로 정착. Langfuse + RAGAS + DeepEval 통합 평가 파이프라인 확산. 판정자 정렬(Judge Alignment) 연구 진행 중.

### MLOps Pipeline
- MLOps→LLMOps 전환 가속 유지. LoRA (Low-Rank Adaptation)/PEFT (Parameter-Efficient Fine-Tuning)가 엔터프라이즈 파인튜닝 표준. Databricks, AWS, Azure, GCP 모두 LLMOps 기능 내장. 이번 주 신규 변화 없음.

### 5G SA/6G (AI-RAN/SRv6)
- W13에서 보고한 SKT-에릭슨 MoU(3/19), NVIDIA Aerial 오픈소스, OCUDU 재단 출범 등이 후속 정착 단계. 이번 주 추가 발표 없음. Chunghwa Telecom-에릭슨 5G-Advanced MoU(MWC 2026) 확인.

### Speaker Diarization
- AssemblyAI Universal-3-Pro와 Gladia Solaria-1(103ms 부분 지연) 안정 운영 유지. pyannote 실시간 다이어리제이션 + LLM 기반 트랜스크립션 통합 연구 진행 중. 돌파구 수준 변화 없음.

### Agentic Context Engineering
- ACE (Agentic Context Engineering) (ICLR 2026) 프레임워크의 오픈소스 생태계 점진적 성숙. ICSE 2026에서 AGENT 2026 워크숍 예정. 이번 주 신규 발표 없음.

### Adaptive RAG
- Agentic RAG 프로덕션 도입률 57%+ 유지. CRAG (Corrective RAG) 패턴이 기업 배포 표준으로 정착. Higress-RAG(적응형 라우팅 + 시맨틱 캐싱 + 이중 하이브리드 검색) 엔터프라이즈 배포 확산 중.

---

## 🟡🔴 Deep 심층 분석

### Intelligent Agent Orchestration — 🟡 주목

> 상세 리서치: [2026-03-24_research-agent-orchestration.md](2026-03-24_research-agent-orchestration.md)

#### 이전 대비 변화
- 전주: Google Colab MCP Server 오픈소스, MCP 2026 로드맵 공개, MS Agent Framework GA 임박
- 금주: OpenAI Agents SDK 0.13 + tool search, Claude Code Channels(3/20), Google ADK 네이티브 A2A, MS Foundry Agent Service GA(3/16)
- 변화 방향: 프로토콜 표준화 완료 → **런타임 도구 효율화 + 멀티에이전트 프로덕션화** 단계

#### 기술 동향

1. **OpenAI Agents SDK 0.13 — tool search로 대규모 도구 생태계 효율화(3/23).**
   Responses API tool search 지원 추가. 에이전트가 대규모 도구를 런타임에 지연 로드하여 토큰·캐시·지연 최적화. GPT-5.4가 tool search 네이티브 지원. voice agent(gpt-realtime-1.5 기반) 빌딩도 추가. [[G-01]](#ref-g-01)

2. **Claude Code Channels — MCP 서버 기반 외부 메시지 브릿지(3/20).**
   `--channels` 플래그로 Telegram·Discord 메시지를 Claude Code 세션에 실시간 주입. MCP elicitation(v2.1.76+)과 결합하여 에이전트가 구조화된 입력을 인터럽트 없이 수집. MCP Python/TypeScript SDK 월간 다운로드 9,700만+. [[G-02]](#ref-g-02)

3. **Google ADK (Agent Development Kit) 네이티브 A2A (Agent-to-Agent) 지원.**
   Agent Card 퍼블리싱 → 디스커버리 → 서브에이전트 활용 공식화. Cloud Run 및 Agent Engine 배포 지원으로 프로덕션 A2A 에이전트 원클릭 배포. [[G-03]](#ref-g-03)

4. **Microsoft Foundry Agent Service GA(3/16) + Agent Framework Q1 GA 임박.**
   프라이빗 네트워킹, Voice Live, 엔터프라이즈급 평가 기능 포함. AutoGen·Semantic Kernel 통합 완료, A2A·MCP 프로토콜 지원. [[G-04]](#ref-g-04)

5. **VS Code 1.112 — Copilot 에이전트 자율성 확대 + MCP 서버 샌드박싱(3/18).**
   macOS·Linux MCP 서버 샌드박싱, 모노레포 에이전트 커스터마이징 지원 확대. [[G-05]](#ref-g-05)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| OpenAI | Agents SDK 0.13(3/23): tool search, GPT-5.4 computer use, voice agent 지원 | [[G-01]](#ref-g-01) |
| Anthropic | Claude Code Channels(3/20) Telegram/Discord 브릿지, MCP elicitation, Opus 4.6 agent teams | [[G-02]](#ref-g-02) |
| Google | ADK 네이티브 A2A, Agent Engine + Cloud Run 배포 | [[G-03]](#ref-g-03) |
| Microsoft | Foundry Agent Service GA(3/16), Agent Framework Q1 GA 임박, VS Code 1.112 MCP 샌드박싱 | [[G-04]](#ref-g-04), [[G-05]](#ref-g-05) |
| Interloom | 에이전트 'tacit knowledge' 문제 해결 $16.5M VC(3/23, DN Capital 리드) | [[G-06]](#ref-g-06) |
| CrewAI | v1.10.1 MCP+A2A, 45,900+ Stars, 일간 1,200만 에이전트 실행 | [[G-07]](#ref-g-07) |

#### 시장 시그널

**투자 & M&A**
- Interloom $16.5M VC(3/23) — 에이전트 암묵지 문제 해결 [[G-06]](#ref-g-06)
- 에이전틱 AI 스타트업 평균 라운드 $155M(Q4 2025~Q1 2026), 전기 대비 2배 [[G-08]](#ref-g-08)

**시장 전망**
- 글로벌 에이전틱 AI 시장 $91~109억(2026) → $1,390억(2034), CAGR 40.5% [[G-08]](#ref-g-08)
- Gartner: 2026년 말 엔터프라이즈 앱 40%에 에이전트 탑재(2025년 5% 미만) [[G-09]](#ref-g-09)
- Salesforce: 멀티에이전트 도입 2027년까지 67% 급증 [[G-10]](#ref-g-10)

**도입 사례**
- Global 2000 기업 72% AI 에이전트 프로덕션 배포(파일럿 넘어섬) [[G-09]](#ref-g-09)

**연구 동향**
- MAS-Orchestra: RL 기반 MAS 오케스트레이션, MASBENCH에서 10x 효율 달성 — "어떤 모델"에서 "어떻게 조율하느냐"로 학술 트렌드 전환 재확인 [[P-01]](#ref-p-01)

#### 시장 수요

**고객 페인포인트**
- 에이전트 프레임워크 난립으로 선택 피로(4강 + CrewAI + LangGraph 경쟁)
- 에이전트 암묵지(tacit knowledge) 문제 — 명시적 프롬프트로 전달하기 어려운 도메인 지식

**도입 장벽**
- 엔터프라이즈 SSO·감사 트레일·거버넌스 미성숙(MCP 2026 로드맵에서 공식 인정)

**시장 니즈**
- 프레임워크 간 상호운용성 → A2A + MCP 듀얼 스택 지원이 사실상 표준

#### 전략적 시사점

1. **MCP + A2A 듀얼 스택 필수** — Big Tech 4사 모두 양쪽 지원. 자사 에이전트 설계 시 두 프로토콜 대응 필수.
2. **Tool Search 패턴** — 도구 수 증가에 따른 토큰·지연 문제를 런타임에 해결. 자사 MCP 도구 확장 시 유사 메커니즘 검토.
3. **KT 에이전트 빌더 대응** — KT가 노코드 에이전트 제작 플랫폼을 MWC26에서 공개. B2B 에이전트 시장 선점 경쟁 가속.

---

### 하이브리드 GPU Orchestration — 🟡 주목

> 상세 리서치: [2026-03-24_research-gpu-orchestration.md](2026-03-24_research-gpu-orchestration.md)

#### 이전 대비 변화
- 전주: SkyPilot Job Groups + Claude Code 자율 910회 실험, Ocean Network P2P 베타, AKS DRA+vGPU GA
- 금주: NVIDIA Dynamo 1.0 GA(3/16), Vera Rubin 플랫폼 공개, DDN-NVIDIA 추론 비용 최적화(3/17), Blackwell 7x 추론 향상
- 변화 방향: GPU 오케스트레이션 초점이 학습 → **추론 최적화**로 구조적 전환. Dynamo가 "AI 팩토리 OS"로 정착

#### 기술 동향

1. **NVIDIA Dynamo 1.0 GA — 오픈소스 추론 OS 프로덕션 출시(3/16).**
   데이터센터 규모 분산 추론 프레임워크. 분리형 서빙, 지능형 라우팅, 다층 KV 캐싱, 자동 스케일링. Blackwell GPU 추론 7x 향상. AWS·Azure·GCP·OCI + CoreWeave·Cursor·Perplexity·PayPal·Pinterest 등 프로덕션 배포. [[G-11]](#ref-g-11)

2. **Vera Rubin 플랫폼 — 칩 7종 + 랙 5종의 수직 통합(GTC 2026).**
   NVL72 랙이 이전 대비 1/4 GPU로 동일 학습, 와트당 추론 10x, 토큰당 비용 1/10. Vera Rubin + Groq 3 LPX 조합으로 35x 처리량/MW. Jensen Huang 2027년 $1T 수주 전망. [[G-12]](#ref-g-12)

3. **DDN-NVIDIA 협업 — 추론 비용 절감 + GPU 활용률 극대화(3/17).**
   스토리지-컴퓨트 분리로 모델 로딩·KV 캐시 관리 최적화. [[G-13]](#ref-g-13)

4. **Dynamo + GKE (Google Kubernetes Engine) Inference Gateway — 클라우드 네이티브 추론 오케스트레이션.**
   모듈형 오픈소스 컨트롤 플레인으로 이종 가속기 클러스터 통합 관리. [[G-14]](#ref-g-14)

5. **CoreWeave SkyPilot 백엔드 공식 지원.**
   SkyPilot YAML/CLI에서 CoreWeave 클러스터 직접 잡 런칭. 이종 하드웨어 추상화 유지. [[G-15]](#ref-g-15)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| NVIDIA | Dynamo 1.0 GA(3/16), Vera Rubin 플랫폼, $1T 전망, Blackwell 7x | [[G-11]](#ref-g-11), [[G-12]](#ref-g-12) |
| DDN | NVIDIA와 추론 비용 절감 협업(3/17) | [[G-13]](#ref-g-13) |
| Google Cloud | GKE Inference Gateway + Dynamo 통합 | [[G-14]](#ref-g-14) |
| CoreWeave | SkyPilot 백엔드 지원, HGX B300 GA 유지 | [[G-15]](#ref-g-15) |
| Cisco | Secure AI Factory with NVIDIA(GTC 2026) | [[G-16]](#ref-g-16) |

#### 시장 시그널

**시장 전망**
- Jensen Huang: 2027년까지 $1T 수주 전망 — 추론 인프라 투자 폭발 신호 [[G-12]](#ref-g-12)
- GTC 2026 "Inflection of Inference" — 추론이 AI 컴퓨트 2/3 차지 [[G-12]](#ref-g-12)

**파트너십 & 제휴**
- DDN-NVIDIA 추론 비용 최적화(3/17) [[G-13]](#ref-g-13)
- Cisco Secure AI Factory with NVIDIA(GTC 2026) [[G-16]](#ref-g-16)

**도입 사례**
- Dynamo 1.0: Cursor, Perplexity, PayPal, Pinterest, ByteDance, Meituan 등 프로덕션 [[G-11]](#ref-g-11)
- Akamai: AI Grid 4,400 에지 로케이션 배포 [[G-17]](#ref-g-17)

#### 시장 수요

컨퍼런스 영상에서 수요 시그널을 확인하지 못함.

#### 전략적 시사점

1. **추론 인프라 투자 시점** — 학습→추론 전환은 구조적. Dynamo, Vera Rubin 기반 추론 전용 최적화 우선순위 검토.
2. **오픈소스 Dynamo 활용** — Apache 2.0으로 벤더 종속 없이 추론 파이프라인 구축 가능.
3. **이종 가속기 전략** — 프리필/디코드 분리로 이종 칩(Vera Rubin + Groq 3) 활용이 최적화 패턴.

---

### On-Device sLM — 🟡 주목

> 상세 리서치: [2026-03-24_research-ondevice-slm.md](2026-03-24_research-ondevice-slm.md)

#### 이전 대비 변화
- 전주: Gemma 3n GA + SmolLM3-3B SOTA 안정화, 신규 릴리스 없음
- 금주: OpenAI GPT-5.4 mini+nano 출시(3/17), sLM-First 아키텍처 비용 60-70% 절감 패턴 확산
- 변화 방향: 오픈소스 sLM 안정화 위에 **상용 소형 모델 등장** → 엔터프라이즈 에지 도입 가속

#### 기술 동향

1. **OpenAI GPT-5.4 mini + nano 출시(3/17) — 상용 소형 모델 본격 진입.**
   GPT-5 mini 대비 코딩·추론·에이전틱 전면 향상, 2x+ 빠른 실행. tool search 네이티브 지원. nano는 모바일·IoT 타깃. [[G-18]](#ref-g-18)

2. **sLM (Small Language Model)-First, LLM-Backup 아키텍처 엔터프라이즈 표준화.**
   일상 요청 80%를 로컬 sLM, 복잡한 20%만 클라우드 LLM으로 라우팅. AI 컴퓨트 비용 60-70% 절감. Phi-4(3.8B), Gemma 3(270M~), Qwen3-8B 주요 선택지. [[G-19]](#ref-g-19)

3. **Google AI Edge RAG — 온디바이스 RAG 공식 지원.**
   파인튜닝 없이 대량 데이터에서 관련 정보를 sLM에 제공. Android 우선, 멀티플랫폼 확장 예정. [[G-20]](#ref-g-20)

4. **NPU 세대교체 — 2026형 칩셋 sLM 전용 최적화.**
   Qualcomm X2, Samsung Exynos 2600, MediaTek 신규 NPU. Gemma 3 4B가 Apple Silicon에서 4비트 양자화로 인터랙티브 속도. TI NPU MCU는 90x 지연 감소, 120x 에너지 절감 시연. [[G-21]](#ref-g-21)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| OpenAI | GPT-5.4 mini+nano(3/17), tool search 네이티브, 모바일·IoT 타깃 | [[G-18]](#ref-g-18) |
| Google | Gemma 3n 멀티모달 GA, AI Edge RAG, LiteRT HuggingFace | [[G-20]](#ref-g-20) |
| TI | NPU 내장 MCU(3/10) — 초저전력 에지 AI | [[G-21]](#ref-g-21) |

#### 시장 시그널

**시장 전망**
- Gartner: 2027년까지 소형 과업별 AI 모델 사용이 범용 LLM 대비 3배 [[G-19]](#ref-g-19)

**도입 사례**
- sLM-First 아키텍처: 일상 80% 로컬, 비용 60-70% 절감 [[G-19]](#ref-g-19)

#### 시장 수요

**고객 페인포인트**
- 모델 크기 vs 성능 트레이드오프(4GB RAM 제약)
- MoE (Mixture of Experts) 모델의 전문가 로딩 병목("컴퓨트 빠르나 메모리 셔플링이 병목")

**시장 니즈**
- 턴키 sLM 배포 + 에지 최적화 + 매니지드 서비스 결합 제품
- 프라이버시 보존 온디바이스 AI(통신·금융·의료 규제 산업)

#### 전략적 시사점

1. **GPT-5.4 mini/nano 경쟁 심화** — 상용 소형 모델이 오픈소스 sLM과 성능·편의성 경쟁 시작.
2. **sLM-First 아키텍처 도입** — 80/20 티어드 전략으로 비용 60-70% 절감. 자사 AI 서비스 적용 검토.
3. **온디바이스 RAG 파이프라인** — 파인튜닝 없이 도메인 데이터 주입하는 패턴 표준화.

---

### Edge AI — 🟡 주목

> 상세 리서치: [2026-03-24_research-edge-ai.md](2026-03-24_research-edge-ai.md)

#### 이전 대비 변화
- 전주: GTC 2026 "Inflection of Inference", ExecuTorch 1.0 프로덕션 확산
- 금주: AT&T-Cisco-NVIDIA AI Grid 상용 배포(3/17-19), Akamai 4,400 에지 배포, TI NPU MCU(3/10)
- 변화 방향: 에지 AI PoC → **대규모 프로덕션 배포** 전환. 통신사·CDN이 에지 추론 인프라 상용화 주도

#### 기술 동향

1. **AT&T-Cisco-NVIDIA AI Grid — 네트워크 주도 에지 AI 상용 배포(3/17-19).**
   AT&T 전용 IoT 코어 + Cisco Mobility Services Platform + NVIDIA 가속 컴퓨트. 로컬 트래픽 브레이크아웃, 결정적 성능, 제로트러스트 보안. Dallas Discovery District 라이브 + 루이지애나 산업 파일럿. [[G-22]](#ref-g-22)

2. **Akamai — NVIDIA AI Grid 4,400 에지 로케이션 배포(최초 대규모).**
   CDN 인프라의 AI 추론 플랫폼 전환. 에지 추론의 클라우드 의존 탈피 신호. [[G-17]](#ref-g-17)

3. **TI NPU 내장 MCU — 초저전력 에지 AI 하드웨어(3/10).**
   TinyEngine NPU로 유사 MCU 대비 지연 90x 감소, 추론당 에너지 120x 절감. 산업 자동화·스마트 빌딩 타깃. [[G-21]](#ref-g-21)

4. **Cisco Secure AI Factory — 보안 중심 에지 AI 아키텍처(GTC 2026).**
   에지~데이터센터 보안·거버넌스·오케스트레이션 통합 관리. [[G-16]](#ref-g-16)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| AT&T | Cisco-NVIDIA AI Grid 상용 배포(3/17), Dallas 라이브 + 산업 파일럿 | [[G-22]](#ref-g-22) |
| Akamai | AI Grid 4,400 에지 로케이션 — 최초 대규모 에지 추론 | [[G-17]](#ref-g-17) |
| Cisco | Secure AI Factory + AI Grid 에지 보안 아키텍처 | [[G-16]](#ref-g-16) |
| TI | NPU MCU(3/10), 90x 지연 감소 | [[G-21]](#ref-g-21) |

#### 시장 시그널

**파트너십 & 제휴**
- AT&T-Cisco-NVIDIA 에지 AI Grid(3/17) — 통신사 네트워크 자산 활용 에지 추론 [[G-22]](#ref-g-22)
- Akamai-NVIDIA AI Grid 글로벌 배포 — CDN→에지 AI 인프라 전환 [[G-17]](#ref-g-17)

**시장 전망**
- 에지 AI 시장 2030년까지 $1,232억(CAGR 20.3%) [[G-23]](#ref-g-23)

**도입 사례**
- AT&T Discovery District 라이브 — 비디오 보안, 교통, 제조, 산업 자동화 [[G-22]](#ref-g-22)

#### 시장 수요

**고객 페인포인트**
- 에지 AI 프로젝트 70%가 PoC에서 정체 — 운영 복잡성·파편화가 핵심 원인
- 이종 OS·하드웨어·불안정한 네트워크에서의 일관된 배포·관리 어려움

**시장 니즈**
- 턴키 에지 AI 배포 솔루션(AT&T-Cisco-NVIDIA AI Grid가 정확히 충족)
- 에지 보안·거버넌스 통합 플랫폼

#### 전략적 시사점

1. **통신사 에지 자산 활용** — AT&T 모델은 통신사 네트워크 인프라를 에지 추론 플랫폼으로 전환하는 선례. 자사 5G 코어·에지 인프라 활용 가능성 검토.
2. **CDN→에지 AI 진화** — Akamai 4,400 배포는 CDN 사업자가 에지 AI 핵심 플레이어로 부상.
3. **PoC→프로덕션 전환 지원** — 70% PoC 정체를 해결하는 턴키 솔루션이 차별화 포인트.

---

## 경쟁사 동향 (SKT / KT)

### SKT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| SKT-에릭슨 MoU(3/19) | AI-RAN·5G 수익화·자율 네트워크·제로트러스트·6G 표준화 5개 축, 2031년까지 | `5g-6g-ai-ran` | [[E-01]](#ref-e-01) |
| AI 메가 데이터센터 계획 | 전국 1GW+ 규모 AI 데이터센터 구축, 아시아 최대 AI 허브 목표 | `gpu-orchestration` | [[E-02]](#ref-e-02) |
| A. AI 에이전트 서비스 | 구독 기반 AI 수익 모델 강화, B2B AI·클라우드 솔루션 확대 | `agent-orchestration` | [[E-02]](#ref-e-02) |

### KT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| 에이전트 빌더(MWC26) | 노코드 드래그앤드롭 AI 에이전트 제작 플랫폼, RAG·AI 핵심 기능 모듈화, 금융·제조·공공 템플릿 | `agent-orchestration` | [[E-03]](#ref-e-03) |
| K GPUaaS | 월 구독형 GPU 서비스 + 온프레미스 AI GPU Managed | `gpu-orchestration` | [[E-03]](#ref-e-03) |

---

## 규제 & 거버넌스

### 시행 임박 / 카운트다운

| 규제 | 시행일 | D-day |
|------|--------|-------|
| 한국 AI 기본법 (인공지능 발전과 신뢰 기반 조성 등에 관한 기본법) | 2026-01-22 | 시행 중 (계도기간) |
| EU AI Act — 고위험 AI 시스템 (Annex III) | 2026-08-02 | D-131 |
| EU AI Act — 제품 안전 AI (Annex I) | 2027-08-02 | D-496 |

### 신규 발의 & 가이드라인

- **미국 백악관 AI 정책 프레임워크(3/20)**: 7대 권고안 발표. 새로운 연방 규제 기관 신설 반대, 기존 규제기관을 통한 "부문별(sector-specific)" 접근 권장. AI 에이전트 자율 행위에 대한 책임 소재는 미언급. [[G-24]](#ref-g-24)
- **TRUMP AMERICA AI Act 법안(3/18)**: 연방 AI 조달 보호, Section 230 책임 보호 수정 등 제안. AI 에이전트에 대한 직접적 규제 조항은 미포함. [[G-25]](#ref-g-25)
- **한국 AI 기본법 시행(1/22)**: 고영향 AI 사업자 특별 책무, 투명성·안전성 확보 의무 적용 시작. 에이전트의 자율적 판단 오류 시 책임 소재(개발사·운영사·사용자)가 업계 핵심 쟁점. 과기정통부가 최소 1년 규제 유예 계도기간 운영 중. [[G-26]](#ref-g-26)

### 시사점

- EU AI Act 고위험 AI 시스템 규정 D-131: 에이전틱 AI가 고위험으로 분류될 경우 적합성 평가·기술 문서·CE 마킹 필요. 자사 에이전트 서비스의 EU 고위험 분류 여부 사전 검토 필요.
- 한국 AI 기본법: 에이전트 자율 행위의 법적 책임 해석이 미확정 — 서비스 설계 시 인간 감독(human-in-the-loop) 메커니즘 내장 권장.

---

## 종합 시사점 및 후속 조치

### 이번 주 핵심 전환

1. **에이전트 프레임워크 4강 동시 프로덕션 업데이트** — OpenAI(SDK 0.13), Anthropic(Channels), Google(ADK A2A), Microsoft(Foundry GA)가 같은 주에 발표. MCP + A2A 듀얼 스택이 사실상 표준. 자사 에이전트 설계에 두 프로토콜 대응 필수.

2. **학습→추론 구조적 전환 가속** — NVIDIA Dynamo 1.0 GA + Vera Rubin 플랫폼이 "AI 팩토리 OS" + 차세대 하드웨어를 동시 제시. 추론 전용 인프라 투자 시점 도래.

3. **에지 AI 대규모 프로덕션 진입** — AT&T AI Grid, Akamai 4,400 로케이션이 에지 추론의 PoC→상용 전환 확인. 통신사 에지 자산 활용 전략 수립 시급.

4. **상용 소형 모델 경쟁 시작** — GPT-5.4 mini/nano가 오픈소스 sLM과 직접 경쟁. sLM-First 아키텍처(80% 로컬, 비용 60-70% 절감)가 엔터프라이즈 표준으로 부상.

### 후속 조치 권장

| 우선순위 | 조치 | 관련 L3 |
|----------|------|---------|
| 🟡 | MCP + A2A 듀얼 프로토콜 대응 전략 수립 | agent-orchestration |
| 🟡 | NVIDIA Dynamo 1.0 기반 추론 인프라 PoC 검토 | gpu-orchestration |
| 🟡 | 자사 5G 에지 인프라의 AI 추론 플랫폼 활용 가능성 분석 | edge-ai |
| 🟡 | sLM-First 티어드 아키텍처 파일럿 설계 | ondevice-slm |
| ⚪ | EU AI Act 고위험 AI 에이전트 분류 사전 검토 | 전체 |

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | OpenAI Agents SDK 0.13 Releases | [링크](https://github.com/openai/openai-agents-python/releases) | G | 2026-03-23 | high |
| <a id="ref-g-02"></a>G-02 | VentureBeat — Claude Code Channels | [링크](https://venturebeat.com/orchestration/anthropic-just-shipped-an-openclaw-killer-called-claude-code-channels) | G | 2026-03-20 | high |
| <a id="ref-g-03"></a>G-03 | Google Cloud Blog — A2A ADK 업그레이드 | [링크](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade) | E | 2026-03 | high |
| <a id="ref-g-04"></a>G-04 | MS Foundry Blog — Foundry Agent Service GA | [링크](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/) | E | 2026-03-16 | high |
| <a id="ref-g-05"></a>G-05 | Visual Studio Magazine — VS Code 1.112 | [링크](https://visualstudiomagazine.com/articles/2026/02/09/hands-on-with-new-multi-agent-orchestration-in-vs-code.aspx) | G | 2026-03-18 | high |
| <a id="ref-g-06"></a>G-06 | Fortune — Interloom $16.5M VC | [링크](https://fortune.com/2026/03/23/interloom-ai-agents-raises-16-million-venture-funding/) | G | 2026-03-23 | high |
| <a id="ref-g-07"></a>G-07 | NxCode — CrewAI vs LangChain 2026 | [링크](https://www.nxcode.io/resources/news/crewai-vs-langchain-ai-agent-framework-comparison-2026) | G | 2026-03 | medium |
| <a id="ref-g-08"></a>G-08 | Tracxn — Agentic AI Market 2026 | [링크](https://tracxn.com/d/sectors/agentic-ai/__oyRAfdUfHPjf2oap110Wis0Qg12Gd8DzULlDXPJzrzs) | G | 2026-03 | medium |
| <a id="ref-g-09"></a>G-09 | Enterprise AI Agent Adoption March 2026 | [링크](https://insights.reinventing.ai/articles/openclaw-enterprise-adoption-march-2026-03-16) | G | 2026-03-16 | medium |
| <a id="ref-g-10"></a>G-10 | Salesforce — Multi-Agent Adoption Report | [링크](https://www.salesforce.com/news/stories/connectivity-report-announcement-2026/) | E | 2026-03 | high |
| <a id="ref-g-11"></a>G-11 | NVIDIA Newsroom — Dynamo 1.0 GA | [링크](https://nvidianews.nvidia.com/news/nvidia-enters-production-with-dynamo-the-broadly-adopted-inference-operating-system-for-ai-factories) | E | 2026-03-16 | high |
| <a id="ref-g-12"></a>G-12 | CNBC — NVIDIA GTC 2026 Vera Rubin $1T | [링크](https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html) | G | 2026-03-16 | high |
| <a id="ref-g-13"></a>G-13 | Blocks & Files — DDN-NVIDIA 추론 비용 절감 | [링크](https://www.blocksandfiles.com/ai-ml/2026/03/17/ddn-nvidia-team-up-to-cut-inference-costs-and-boost-gpu-utilization/5209483) | G | 2026-03-17 | high |
| <a id="ref-g-14"></a>G-14 | Google Cloud Blog — GTC 2026 AI 인프라 | [링크](https://cloud.google.com/blog/products/compute/google-cloud-ai-infrastructure-at-nvidia-gtc-2026) | E | 2026-03-20 | high |
| <a id="ref-g-15"></a>G-15 | CoreWeave Blog — SkyPilot 지원 | [링크](https://www.coreweave.com/blog/coreweave-adds-skypilot-support-for-effortless-multi-cloud-ai-orchestration) | E | 2026-03 | high |
| <a id="ref-g-16"></a>G-16 | Cisco Newsroom — Secure AI Factory with NVIDIA | [링크](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2026/m03/cisco-secure-ai-factory-with-nvidia-GTC-2026.html) | E | 2026-03 | high |
| <a id="ref-g-17"></a>G-17 | DCD — Akamai AI Grid 4,400 로케이션 | [링크](https://www.datacenterdynamics.com/en/news/akamai-deploys-nvidia-ai-grid-across-4400-edge-locations-claims-to-be-first/) | G | 2026-03 | high |
| <a id="ref-g-18"></a>G-18 | 9to5Mac — OpenAI GPT-5.4 mini/nano | [링크](https://9to5mac.com/2026/03/17/openai-releases-gpt-5-4-mini-and-nano-its-most-capable-small-models-yet/) | G | 2026-03-17 | high |
| <a id="ref-g-19"></a>G-19 | Iterathon — sLM Enterprise 2026 가이드 | [링크](https://iterathon.tech/blog/small-language-models-enterprise-2026-cost-efficiency-guide) | G | 2026-03 | medium |
| <a id="ref-g-20"></a>G-20 | Google Developers Blog — AI Edge sLM + RAG | [링크](https://developers.googleblog.com/google-ai-edge-small-language-models-multimodality-rag-function-calling/) | E | 2026-03 | high |
| <a id="ref-g-21"></a>G-21 | TI Newsroom — 에지 AI MCU | [링크](https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-10-ti-expands-microcontroller-portfolio-and-software-ecosystem-to-enable-edge-ai-in-every-device.html) | E | 2026-03-10 | high |
| <a id="ref-g-22"></a>G-22 | AT&T — Cisco-NVIDIA AI Grid | [링크](https://about.att.com/story/2026/cisco-ai-grid-with-nvidia.html) | E | 2026-03-17 | high |
| <a id="ref-g-23"></a>G-23 | SiliconANGLE — Edge AI 변곡점 | [링크](https://siliconangle.com/2026/03/20/edge-ai-infrastructure-reaches-real-world-inflection-point-nvidiagtcai/) | G | 2026-03-20 | high |
| <a id="ref-g-24"></a>G-24 | Nextgov — 백악관 AI 정책 프레임워크 | [링크](https://www.nextgov.com/artificial-intelligence/2026/03/white-house-releases-regulatory-vision-ai/412274/) | G | 2026-03-20 | high |
| <a id="ref-g-25"></a>G-25 | Fox Rothschild — TRUMP AMERICA AI Act | [링크](https://dataprivacy.foxrothschild.com/2026/03/articles/general-privacy-data-security-news-developments/trump-america-ai-act-bill-sets-direction-for-future-us-ai-regulation/) | G | 2026-03-18 | medium |
| <a id="ref-g-26"></a>G-26 | 피카부랩스 — AI 기본법 완전 정리 | [링크](https://peekaboolabs.ai/blog/ai-basic-law-guide) | G | 2026-01 | medium |
| <a id="ref-e-01"></a>E-01 | Ericsson — SKT-에릭슨 MoU | [링크](https://www.ericsson.com/ko/news/2/2026/skt-6g-mou) | E | 2026-03-19 | high |
| <a id="ref-e-02"></a>E-02 | WithNews — 통신사 AI 인프라 투자 | [링크](https://car.withnews.kr/economy/telecom-companies-ai-infrastructure-war-mwc-2026) | G | 2026-03 | medium |
| <a id="ref-e-03"></a>E-03 | AI Times — KT 에이전트 빌더 | [링크](https://www.aitimes.kr/news/articleView.html?idxno=38894) | G | 2026-03-04 | high |
| <a id="ref-p-01"></a>P-01 | MAS-Orchestra: RL 기반 MAS 오케스트레이션 | [링크](https://arxiv.org/) | P | 2026-03 | medium |
