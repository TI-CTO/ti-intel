---
type: weekly-monitor
domain: agentic-ai
week: 2026-W15
date: 2026-04-06
l3_count: 12
deep_count: 2
---

# 주간 기술 동향: Agentic AI (2026-W15)

## Executive Summary

> **이번 주 핵심**: Microsoft Agent Framework 1.0 GA(General Availability)(4/3)를 기점으로 주요 에이전트 오케스트레이션 프레임워크의 프로덕션 진입이 완료되었고, Embedded World 2026 후속으로 ASUS UGen300(40 TOPS/2.5W), TI $1 AI MCU(Microcontroller Unit) 등 엣지 AI 가속기가 PoC(Proof of Concept)에서 양산 가능 제품으로 전환 가속 중이다.

| Layer 2 | 세부기술 | 신호 | 핵심 내용 |
|---------|----------|------|----------|
| Trusted Multi-Agent Orchestration | Intelligent Agent Orchestration | 🟡 | [제품출시] MS Agent Framework 1.0 GA(4/3), Copilot Studio 멀티에이전트 GA · [생태계] MCP Dev Summit 종료, SDK v2 로드맵 공개 · [제품출시] Google Gemma 4 온디바이스 에이전트 |
| | Agent Oriented Orchestration | 🟢 | Plan-and-Act 하이브리드 패턴 안정 유지 |
| Hybrid AI Infra | Edge AI | 🟡 | [제품출시] ASUS UGen300(Hailo-10H, 40 TOPS, 2.5W) · [기술돌파] Nordic Axon NPU(Neural Processing Unit) 15x 추론 향상 · [제품출시] TI $1 이하 AI MCU 양산 |
| | On-Device sLM | 🟢 | FunctionGemma/Qwen 3.5/Gemma 3 정착 유지, sLM-First 비용 절감 지속 |
| | 5G SA/6G (AI-RAN/SRv6) | 🟢 | MWC·P.I. Works-TELUS 후속 정착, NVIDIA Aerial 오픈소스 |
| | 실시간 화자분할(2인) | 🟢 | Voxtral sub-200ms, AssemblyAI Universal-3-Pro 안정 유지 |
| Model & Delta Foundry | GPU Orchestration | 🟢 | SkyPilot Agent Skills 에코시스템 성숙, 추가 발표 없음 |
| | FeedbackOps: Meta-prompt Engineering | 🟢 | DSPy MIPROv2 안정, 신규 릴리스 없음 |
| | EvaluationOps: KMS 성능평가 | 🟢 | RAGAS 에이전트 워크플로우 평가 확장, 도구 생태계 성숙 |
| | 데이터-학습-배포 파이프라인 | 🟢 | AgentOps 개념 정착, 보안/거버넌스 프레임워크 공식화 |
| Self Evolving Architecture | Agentic Context Engineering | 🟢 | ACE(Agentic Context Engineering) ICLR 2026 생태계 성숙 지속 |
| 의도 파악 기술 | Adaptive RAG | 🟢 | Router Pattern 표준 유지, Hybrid RAG 프로덕션 베이스라인 |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음
> **태그** : [기술돌파] [제품출시] [경쟁사] [규제] [투자] [논문] [생태계]

---

## 🟢 Quick 요약 (변화 미미)

### Agent Oriented Orchestration
- Plan-and-Act 하이브리드 패턴(고추론 DAG(Directed Acyclic Graph) 분해 → 경량 실행 → 재계획)이 엔터프라이즈 배포 주류 유지. LATS(Language Agent Tree Search) 참조 증가. 이번 주 추가 변화 없음.

### On-Device sLM
- FunctionGemma 270M, Qwen 3.5 4B, Gemma 3 1B 기존 정착 유지. sLM-First 아키텍처 60-70% 비용 절감 패턴 지속. Google Gemma 4 E2B(1.5GB 미만)가 에이전트 특화 온디바이스 모델로 출시되었으나 Edge AI 섹션에서 별도 분석.

### 5G SA/6G (AI-RAN/SRv6)
- MWC 2026 후속 정착 단계. NVIDIA Aerial 오픈소스 6G AI-native 스택, P.I. Works-TELUS AI-RAN 자동화 파트너십(4/1) 후속. 3GPP 6G 스펙 2029년 목표 유지. CSP(Communication Service Provider) 65%가 AI 팩토리 배포/시범 중.

### Speaker Diarization
- Mistral Voxtral Realtime sub-200ms, AssemblyAI Universal-3-Pro 30% 노이즈 개선 안정 유지. Gladia Solaria-1 103ms 다국어 지원. 돌파구 수준 변화 없음.

### GPU Orchestration
- KubeCon Europe 후속 정착. SkyPilot Agent Skills(GPU 접근·잡 관리), CoreWeave 통합(7 GB/s), Shopify 프로덕션 채택 등 에코시스템 성숙. 이번 주 추가 발표 없음.

### FeedbackOps (Meta-prompt Engineering)
- DSPy MIPROv2 옵티마이저 안정 운영 지속. GEPA(Genetic-Pareto Reflective Optimizer), BetterTogether 등 학술 연구 진행 중. 이번 주 신규 릴리스 없음.

### EvaluationOps (KMS 성능평가)
- RAGAS v0.2+ 에이전트 워크플로우 평가 확장 지속. LLM-as-judge 80-90% 인간 일치율 유지. MIRAGE-Bench 다국어 RAG(Retrieval-Augmented Generation) 평가 등장. 이번 주 돌파구 없음.

### MLOps Pipeline
- MLOps→LLMOps→AgentOps 전환 가속 중. AgentOps(장기 실행·다단계 에이전트 관리) 개념이 정착. DevSecMLOps(보안 통합 파이프라인) 프레임워크 공식화 진행. 구체적 신규 제품 출시 없음.

### Agentic Context Engineering
- ACE(ICLR 2026) 프레임워크: AppWorld +17.1%, MCE(Meta Context Engineering) 논문 5.6-53.8% 개선 보고 등 생태계 성숙 지속. GitHub Agent-Skills-for-Context-Engineering 툴킷 등장. 프로덕션 적용 사례는 아직 미확인.

### Adaptive RAG
- Router Pattern이 2026 표준으로 정착. Hybrid RAG(밀집+희소 검색 조합) 프로덕션 베이스라인. 프로덕션 LLM 앱 85%가 RAG 사용(2024년 30%에서 상승). 이번 주 변화 없음.

---

## 🟡🔴 Deep 심층 분석

### Intelligent Agent Orchestration — 🟡 주목

> 상세 리서치: [2026-04-06_research-agent-orchestration.md](2026-04-06_research-agent-orchestration.md)

#### 이전 대비 변화
- 전주: MCP Dev Summit 개막(4/2-3 NYC), AG-UI(Agent-User Interaction Protocol) 3대 프로토콜 스택 형성, MS Agent Framework .NET RC5 출하
- 금주: Microsoft Agent Framework 1.0 GA(4/3), Google Gemma 4 온디바이스 에이전트(4/2), MCP SDK v2 로드맵 최초 공개, Copilot Studio 멀티에이전트 GA(4/1)
- 변화 방향: **RC → GA 전환 완료 국면** — 에이전트 프레임워크 프로덕션 진입 확정. 온디바이스 에이전트·멀티모델 라우팅이 새 경쟁 축으로 부상.

#### 기술 동향

1. **Microsoft Agent Framework 1.0 GA(4/3) — 멀티에이전트 오케스트레이션 프레임워크 정식 출하.**
   Python·.NET 양쪽 SDK가 동시에 1.0 정식 버전으로 전환. AutoGen과 Semantic Kernel의 통합 결과물로, 단일 에이전트 추상화·미들웨어 훅·플러그형 메모리·그래프 기반 워크플로우·멀티에이전트 패턴(순차·동시·핸드오프·그룹 채팅·Magentic-One)이 안정 API로 확정. MCP 지원 포함, A2A(Agent-to-Agent)는 "coming soon" [[G-01]](#ref-g-01).

2. **MCP Dev Summit 종료(4/2-3, NYC) — MCP SDK v2 로드맵 최초 공개.**
   AAIF(Agentic AI Foundation) 주관 95개 세션. Anthropic Max Isbey가 Python SDK v2 로드맵을 공식화, 인증 아키텍처(`mcp.server.auth`) 재설계 가능성 언급. OAuth 2.1 명세 저자 Aaron Parecki와 Anthropic Paul Carleton이 "에이전트를 위한 SSO(Single Sign-On)" 세션 공동 진행 [[G-02]](#ref-g-02), [[G-03]](#ref-g-03).

3. **Google Gemma 4 출시(4/2) — 온디바이스 에이전트 특화 오픈 모델.**
   Apache 2.0 라이선스, E2B(1.5GB 미만)·E4B 버전. 다단계 계획·자율 행동·오프라인 코드 생성·멀티모달 처리 특화. Agent Skills API로 외부 지식·다른 모델 통합. 128K 컨텍스트, 140+ 언어. GKE(Google Kubernetes Engine) Agent Sandbox 초당 300 샌드박스 보안 격리 [[G-04]](#ref-g-04), [[G-05]](#ref-g-05).

4. **Copilot Studio 멀티에이전트 GA(4/1) — A2A 지원, 멀티벤더 모델 개방.**
   A2A 프로토콜로 외부 에이전트 직접 통신·위임. Microsoft Fabric 연동 엔터프라이즈 데이터 추론. Claude Opus 4.6·Sonnet 4.5, Grok 4.1, GPT-5.3/5.4 등 다중 공급자 모델 확장 [[G-06]](#ref-g-06).

5. **LangGraph 1.1.5~1.1.6(4/3) — 실행 정보·원격 빌드 안정화.**
   4월 첫 주 두 개 패치 연속 출하. W16의 타입 안전 스트리밍·Pydantic 강제 변환 기능 후속 안정화 [[G-07]](#ref-g-07).

6. **IBM watsonx Orchestrate 보이스 확장(4/1) — Deepgram·ElevenLabs 파트너십.**
   음성 인식(Deepgram) + TTS(Text-to-Speech)(ElevenLabs) 통합으로 브랜드 음성 에이전트·다국어 더빙·커스텀 음성 클로닝 지원. Elsewedy Electric 엔터프라이즈 에이전트 AI 전략 협력 발표 [[G-08]](#ref-g-08), [[E-01]](#ref-e-01).

7. **AWS AgentCore Policy GA — 에이전트-도구 거버넌스 레이어.**
   에이전트-도구 상호작용에 대한 세분화된 중앙 제어를 에이전트 코드 외부에서 적용. Stateful MCP 서버 기능(elicitation, sampling, progress notifications) 추가 [[G-10]](#ref-g-10), [[G-11]](#ref-g-11).

8. **멀티모델 라우팅 — 에이전트 오케스트레이션 필수 역량으로 부상.**
   각 서브에이전트·태스크 유형에 최적 모델을 동적 배정하는 아키텍처가 "nice-to-have"에서 "must-have"로 격상. 특정 LLM 종속 탈피 설계 필요성 증가 [[G-12]](#ref-g-12).

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Microsoft | Agent Framework 1.0 GA(4/3): Python·.NET 동시 정식, MCP 지원, A2A "coming soon"; Copilot Studio 멀티에이전트 GA(4/1): A2A·Fabric·다중 모델 | [[G-01]](#ref-g-01), [[G-06]](#ref-g-06) |
| Google | Gemma 4(4/2): 온디바이스 에이전트 오픈 모델 E2B/E4B, Apache 2.0; GKE Agent Sandbox 초당 300 샌드박스 | [[G-04]](#ref-g-04), [[G-05]](#ref-g-05) |
| LangChain | LangGraph 1.1.5-1.1.6(4/3): CLI 원격 빌드·실행 정보 안정화; 28.5k GitHub 스타 | [[G-07]](#ref-g-07) |
| IBM | watsonx Orchestrate(4/1): Deepgram·ElevenLabs 보이스 파트너십; Elsewedy Electric 전략 협력 | [[G-08]](#ref-g-08), [[E-01]](#ref-e-01) |
| AWS | AgentCore Policy GA: 중앙 거버넌스; Stateful MCP 서버 기능 추가 | [[G-10]](#ref-g-10), [[G-11]](#ref-g-11) |
| Anthropic | MCP SDK v2 로드맵 공개(Dev Summit); 에이전트용 SSO 세션; Claude Haiku 3 은퇴(4/20) 임박 | [[G-02]](#ref-g-02) |
| OpenAI | SDK 0.13.4 이후 추가 릴리스 미확인; MCP x MCP 키노트(Dev Summit 4/3, Nick Cooper) | [[G-09]](#ref-g-09), [[G-03]](#ref-g-03) |
| CrewAI | 1.1.0: 멀티공급자 LLM·Qdrant Vector Search 개선; 이번 주 추가 릴리스 미확인 | [[G-13]](#ref-g-13) |

#### 시장 시그널

**투자 & M&A**
- 에이전트 AI 섹터 누적 투자 $4.4억+, 2024년 피크 $20.18억; 에이전트 인에이블러(플랫폼·오케스트레이션)가 총 투자의 55%+ 차지 [[G-14]](#ref-g-14) [추가확인 필요]

**파트너십 & 제휴**
- Copilot Studio ↔ A2A: 외부 에이전트 직접 통신·위임 공식 지원 [[G-06]](#ref-g-06)
- IBM watsonx ↔ Deepgram·ElevenLabs: 음성 에이전트 인프라 확장 [[G-08]](#ref-g-08)
- Gemma 4 ↔ NVIDIA RTX/Spark: 온디바이스 에이전트 AI 가속 [[G-05]](#ref-g-05)

**시장 전망**
- 에이전트 스프롤(Agent Sprawl)이 2026년 엔터프라이즈 AI 거버넌스 최대 과제로 부상 [[G-12]](#ref-g-12)
- 멀티모델 라우팅이 에이전트 아키텍처 새 표준 — 특정 LLM 종속 탈피 설계 필요 [[G-12]](#ref-g-12)

**도입 사례**
- Microsoft Ask Microsoft: 멀티에이전트 아키텍처 제품 도메인별 서브에이전트 분산 처리 [원문 미확인] [[G-06]](#ref-g-06)
- IBM Elsewedy Electric: watsonx 기반 엔터프라이즈 에이전트 AI 도입 [[E-01]](#ref-e-01)

**연구 동향**
- "Hierarchical Memory Orchestration for Personalized Persistent Agents" (Liu et al., 2026) — 3단계 계층형 메모리로 온디바이스 에이전트 개인화 장기 기억 구현 [[P-01]](#ref-p-01)
- "ClinicalAgents: Multi-Agent Orchestration with Dual-Memory" (2026) — MCTS(Monte Carlo Tree Search) 기반 동적 오케스트레이터·이중 메모리 아키텍처 [[P-02]](#ref-p-02)

**커뮤니티 시그널**
- MCP Dev Summit 95개 세션 녹화 공개 — MCP SDK v2 인증 변경에 대한 개발자 대응 논의 시작 [[G-02]](#ref-g-02)
- HN "MCPlexor": MCP 멀티툴 환경에서 요청당 40-50k 토큰 낭비 문제 — 시맨틱 라우팅으로 500 토큰 수준 오버헤드 절감 시도 [[C-01]](#ref-c-01)

#### 시장 수요 (voice-of-market)

> Harrison Chase(LangChain) Interrupt 2025 키노트, Douwe Kiela(Contextual AI) AI Engineer Summit, HN 실무자 쓰레드 기반.

**고객 페인포인트**
- **프로토타입→프로덕션 신뢰성 격차** — "쉽게 작동하는 것을 만들 수 있지만, 비즈니스에서 레버를 움직일 만큼 신뢰할 수 있게 만들기는 어렵다" — Harrison Chase (LangChain) [[C-02]](#ref-c-02)
- **MCP 멀티툴 토큰 낭비** — 여러 MCP 서버 연결 시 요청당 40-50k 토큰 주입, 200k 컨텍스트의 25% 소진. 실제 사용 툴은 1-2개 [[C-01]](#ref-c-01)
- **프로덕션 무성 실패** — Prosus 7,949개 에이전트 배포, 성공률 15% [[C-03]](#ref-c-03)

**도입 장벽**
- **다학제적 전문성 요구** — prompting + engineering + product sense + ML 복합 역량의 "agent engineer" 인재 극히 희소 [[C-02]](#ref-c-02)
- **MCP 생태계 품질 파편화** — 서버 구현 품질 편차 극심, 인증 시스템 불안정 [[C-04]](#ref-c-04)
- **파일럿→프로덕션 전환** — 수만~수백만 건 문서, 20,000+ 유스케이스 확장 시 기존 도구 불가 — Douwe Kiela (Contextual AI) [[C-05]](#ref-c-05)

**시장 니즈**
- 프로덕션급 에이전트 배포 플랫폼 (long-running, bursty, stateful 네이티브)
- 멀티모달 AI 전용 관찰가능성 스택
- 비개발자용 노코드 에이전트 빌더
- MCP 컨텍스트 효율화 (시맨틱 라우팅 기반 멀티플렉서)
- 도메인 특화 RAG 에이전트 ("specialization over AGI")

#### 전략적 시사점

**기회**
- Agent Framework 1.0 GA = 도입 최적 타이밍 — RC 불안정성 없이 파일럿 시작 가능
- 온디바이스 에이전트: Gemma 4 E2B(1.5GB 미만)로 망 엣지 에이전트 실행 현실화
- MCP SDK v2 인증 표준화 선점: v2 스펙 확정 전 추상화 레이어 설계로 마이그레이션 비용 절감
- 멀티공급자 오케스트레이터: Copilot Studio의 Claude·GPT·Grok 동시 지원이 표준화 — LLM 종속 탈피 설계

**위협**
- Claude Haiku 3 은퇴(4/20) **2주 남음** — 서브에이전트 파이프라인 즉시 마이그레이션 필요
- A2A 지원 공백: MS Agent Framework 1.0 GA에 A2A 미포함("coming soon") — 크로스런타임 협업 계획 시 주의
- MCP SDK v2 인증 breaking change 리스크: 현재 FastAPI+MCP 인증 코드 동결 권고

---

### Edge AI — 🟡 주목

> 상세 리서치: [2026-04-06_research-edge-ai.md](2026-04-06_research-edge-ai.md)

#### 이전 대비 변화
- 전주: TI TinyEngine NPU 90x 저지연·120x 에너지 효율 발표, 추론칩 시장 $50B 전망, 서브 1B 모델 실용화 변곡점
- 금주: ASUS UGen300(Hailo-10H, 40 TOPS(Tera Operations Per Second), 2.5W) 출시(4/1), Nordic Axon NPU 15x 추론 향상, TI $1 이하 MCU 양산, MediaTek Genio 420 4월 샘플링
- 변화 방향: **PoC·발표 → 양산·실구매 가능 제품 전환 가속** — USB 폼팩터 AI 가속기, $1 이하 AI MCU 등 가격 장벽 붕괴 시작

#### 기술 동향

1. **ASUS UGen300 출시(4/1) — USB-C 플러그인 엣지 AI 가속기.**
   Hailo-10H NPU 탑재, 40 TOPS / 2.5W / 8GB LPDDR4(Low Power Double Data Rate 4). USB 3.1 Gen 2로 Windows·Linux·Android 바로 연결. TensorFlow·PyTorch·ONNX(Open Neural Network Exchange) 지원. Windows 드라이버 5월 중순 예정 [[G-15]](#ref-g-15).

2. **Nordic nRF54LM20B Axon NPU — IoT 추론 속도 15x 향상.**
   128MHz Axon NPU 내장 SoC(System-on-Chip). TFLite(TensorFlow Lite) 추론 CPU 대비 15x, 경쟁 무선 NPU 대비 7x 성능·8x 효율. Q2 광범위 개발 키트 출시 예정 [[G-16]](#ref-g-16).

3. **Synaptics+Google Coral — 업계 최초 Coral NPU 상용 구현.**
   Astra SL2610 SoC에 1 TOPS Torq NPU 탑재. Gemma 3 270M 기본 탑재. MLIR(Multi-Level Intermediate Representation) 기반 오픈소스 툴체인으로 PyTorch·TFLite 단일 워크플로 배포 [[G-17]](#ref-g-17).

4. **MediaTek Genio 시리즈 — 3nm~6nm 풀 라인업.**
   Genio Pro(3nm, 50 TOPS+), Genio 420(6nm, 7.2 TOPS, 4월 샘플링), Genio 360/360P(6~8.5 TOPS). 최대 2B 파라미터 엣지 추론 지원 [[G-18]](#ref-g-18).

5. **TI MSPM0G5187 — $1 이하 AI MCU 양산.**
   Arm Cortex-M0+ 80MHz, TinyEngine NPU로 추론 90x 저지연·120x 에너지 절감. 1,000개 기준 $1 이하 [[G-19]](#ref-g-19).

6. **Ambiq Atomiq SoC — 300mV 초저전압 NPU.**
   12nm FinFET, Arm Ethos-U85 NPU, 200 GOPS(Giga Operations Per Second). 항상 켜진 오디오·비전·추론 AI 실용화. 양산(Atomiq110) 2027년 예정 [[G-20]](#ref-g-20).

7. **NPU 벤치마크 — TOPS 지표의 한계 확인.**
   Apple M4 Max가 낮은 TOPS에도 통합 메모리로 LLM 추론 우위. NPU는 GPU 대비 추론 60% 향상, 전력 40-45% 절감. 메모리 대역폭이 실성능 결정 인자 [[G-21]](#ref-g-21).

8. **LLM 엣지 추론 논문 — 모바일 열 관리가 핵심 제약.**
   Hailo-10H: 6.9 t/s / 2W 미만 vs RTX 4050: 131.7 t/s / 34.1W. 에너지 효율에서 엣지 NPU 우위, 모바일 열 스로틀링이 병목 (Tummalapalli et al., 2026) [[P-03]](#ref-p-03).

9. **통신사 AI-RAN + MEC 연동 진전.**
   SoftBank-Ericsson PoC 완료: 로봇 AI 작업 MEC 동적 오프로드. T-Mobile NVIDIA Blackwell 파일럿 배포. MEC 시장 2031년 $3.88B(CAGR 30.1%) [[G-22]](#ref-g-22), [[G-23]](#ref-g-23).

10. **Qualcomm 한국 AI 스타트업 프로그램 참여(4월).**
    Dragonwing Q-8750(77 TOPS, 11B LLM 온디바이스) 기반 "Challenge AX for All" 프로그램 참여 [[G-24]](#ref-g-24).

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| ASUS | UGen300 USB AI 가속기(4/1), Hailo-10H 40 TOPS, 2.5W, 8GB LPDDR4 | [[G-15]](#ref-g-15) |
| Hailo | Hailo-10H GA 전환 완료, ASUS·Raspberry Pi 등 다수 OEM(Original Equipment Manufacturer) 채택 | [[G-26]](#ref-g-26) |
| Nordic | nRF54LM20B Axon NPU Q2 광범위 출시, Edge AI Lab 통합 파이프라인 | [[G-16]](#ref-g-16) |
| Synaptics | Google Research와 Coral Dev Board 공동 출시, Gemma 3 270M 기본 탑재 | [[G-17]](#ref-g-17) |
| MediaTek | Genio Pro(50 TOPS+)·420·360/360P 발표, 4월 샘플링 시작 | [[G-18]](#ref-g-18) |
| TI | MSPM0G5187 $1 이하 AI MCU 즉시 양산 공급, 90x 저지연·120x 효율 | [[G-19]](#ref-g-19) |
| Samsung | Galaxy S26 EdgeFusion(Exynos 2600 2nm NPU) 온디바이스 이미지 생성 | [[G-25]](#ref-g-25) |
| Qualcomm | Dragonwing Q-8750(77 TOPS) 한국 스타트업 프로그램 참여(4월) | [[G-24]](#ref-g-24) |
| Ericsson | SoftBank와 AI-RAN+MEC PoC 완료, 로봇 AI 동적 오프로드 시연 | [[G-22]](#ref-g-22) |

#### 시장 시그널

**시장 전망**
- 엣지 AI 칩 시장: 2025년 $3.67B → 2031년 $11.54B(CAGR(Compound Annual Growth Rate) 21%) [[G-27]](#ref-g-27)
- 장기: 2036년 $80B+ — 자동차·AI 스마트폰·AI PC·휴머노이드 로봇·AI 센서 견인 [[G-28]](#ref-g-28)
- MEC 시장: 2026년 $1.04B → 2031년 $3.88B(CAGR 30.1%) [[G-23]](#ref-g-23)

**도입 사례**
- ASUS UGen300: 플러그인 방식 엣지 AI, 100개+ 사전 학습 모델 번들 예정 [[G-15]](#ref-g-15)
- TI MCU: $1 이하로 가전·산업 자동화 AI 탑재 비용 장벽 제거 [[G-19]](#ref-g-19)
- SoftBank+Ericsson: MEC 플랫폼에 로봇 AI 작업 동적 오프로드 [[G-22]](#ref-g-22)

**연구 동향**
- "LLM Inference at the Edge" (Tummalapalli et al., 2026) — 4개 플랫폼 벤치마크, 열 관리가 핵심 제약 [[P-03]](#ref-p-03)
- "eIQ Neutron" (NXP 외, 2025) — 컴파일러-NPU 통합 설계로 동일 TOPS 대비 1.8x(최대 4x) 추론 향상 [[P-04]](#ref-p-04)

**커뮤니티 시그널**
- HN "AI PCs Aren't Good at AI": NPU 소프트웨어 생태계 미성숙, 메모리 대역폭 병목 활발 논의 [[C-06]](#ref-c-06)
- Nordic DevZone Axon NPU 성능 스펙 문의 급증 — 샘플링 단계 개발자 수요 반영 [[G-29]](#ref-g-29)

#### 시장 수요 (voice-of-market)

> Embedded World 2026 키노트(Microchip COO Rich Simoncic), GTC 2026 리캡, HN 개발자 커뮤니티 기반.

**고객 페인포인트**
- **NPU 소프트웨어 생태계 미성숙** — 하드웨어 출시 시 runtime 미동시 제공, 개발자가 직접 inference 코드 작성 강요 — HN 커뮤니티 [[C-06]](#ref-c-06)
- **NPU-LLM 구조적 불일치** — NPU는 CNN(Convolutional Neural Network) 스타일 weight 스트리밍에 강하나, LLM 워크로드에서 메모리 대역폭 병목 심화 — HN 커뮤니티 [[C-06]](#ref-c-06)
- **분산 엣지 배포 관리 복잡성** — 수백~수천 노드에 "cloud-like simplicity" 부재, 70% Industry 4.0 프로젝트 파일럿 단계 중단 — GTC 2026 (Zededa)

**도입 장벽**
- **NPU 벤더별 프로그래밍 모델 파편화** — 통일 프로그래밍 모델 없음, 여러 코드 경로 유지 비용 [[C-06]](#ref-c-06)
- **모델 변환 품질 불안정** — 커스텀 PyTorch→On-device 변환 시 출력 불일치 빈발 [[C-07]](#ref-c-07)
- **최신 모델 아키텍처 공식 지원 부재** — SAM2, Whisper, Kokoro 등 TFLite/LiteRT 포팅 없음 [[C-07]](#ref-c-07)

**시장 니즈**
- "Build Once, Run Anywhere" 크로스플랫폼 소프트웨어 스택
- 분산 엣지 노드 중앙 통합 관리 플랫폼
- 저전력·컴팩트 추론 하드웨어 (ASUS UGen300이 이 니즈 정면 대응)
- 개방형 프레임워크 및 벤더 중립 툴체인

#### 전략적 시사점

**기회**
- 가격 장벽 붕괴: TI $1 이하 AI MCU, ASUS USB 가속기로 엣지 AI 하드웨어 대중화 시점 2026 H1으로 앞당겨짐
- 멀티벤더 에코시스템 성숙: Hailo+Nordic+Synaptics/Google+MediaTek 생태계 표준화 — 벤더 종속 없이 솔루션 설계 가능
- 통신 인프라 엣지 AI화: AI-RAN+MEC PoC 완료로 네트워크 엣지를 AI 추론 플랫폼으로 운영하는 모델 가시화
- 소형·저전력 모델 실용화: Gemma 3 270M, Qwen 2.5 1.5B(4bit) 등 상용 NPU에서 실시간 추론 가능

**위협**
- TOPS 지표 불일치: 스펙만으로 판단 시 성능 미달 위험 — 벤치마크 기반 검증 필수
- 모바일 열 제약: 지속 부하 시 열 스로틀링 → 제품 SLA(Service Level Agreement)는 최대가 아닌 지속 성능 기준 적용
- NPU 툴체인 파편화: TI CCStudio, Nordic nRF Connect, Hailo SDK, MediaTek NeuroPilot 난립
- Windows 드라이버 지연: ASUS UGen300 Windows 드라이버 5월 중순 → 엔터프라이즈 타임라인 조정 필요

---

## 경쟁사 동향 (SKT / KT)

> 이번 주 해당 도메인과 관련된 SKT·KT의 주요 움직임.

### SKT

이번 주(3/30~4/6) 해당 도메인 관련 SKT 신규 뉴스 없음. 기존 동향 유지:
- 1인 1 AI 에이전트 전환(3/16), SK AX Agent Builder Platform, 에이닷 조직 전면 배치 등 W16 보도 지속.

### KT

이번 주(3/30~4/6) 해당 도메인 관련 KT 신규 뉴스 없음. 기존 동향 유지:
- 노코드 에이전트 빌더(MWC 3/4), K 인텔리전스 스튜디오, 산업별 AI 템플릿 등 W16 보도 지속.

### 시사점
- 양사 모두 MWC 발표(3월 초) 이후 신규 뉴스 없이 내부 실행 단계로 전환한 것으로 추정. 글로벌 생태계가 GA 전환(MS Agent Framework, Copilot Studio)으로 빠르게 움직이는 반면, 양사의 프로토콜 전략(MCP/A2A/AG-UI 대응)은 여전히 미공개 상태.

---

## 규제 & 거버넌스

> 해당 도메인에 영향을 미치는 국내외 규제·표준·가이드라인 동향.

### 시행 임박 / 카운트다운

| 규제 | 시행일 | D-day |
|------|--------|-------|
| 한국 AI 기본법 (인공지능 발전과 신뢰 기반 조성 등에 관한 기본법) | 2026-01-22 | 시행 중 |
| EU AI Act Article 6-49 (고위험 AI 시스템 전면 적용) | 2026-08-02 | D-118 |
| EU AI Act Article 50 (합성 콘텐츠 투명성) | 2026-08-02 | D-118 |
| Colorado AI Act (고위험 AI 공개 요건) [[G-33]](#ref-g-33) | 2026-06-01 | D-56 |

### 신규 발의 & 가이드라인

- **NIST AI Agent Standards Initiative 퍼블릭 코멘트 마감(4/2)**: 3대 축 — 산업 주도 표준, 오픈소스 프로토콜, 보안·ID 연구. 4월부터 섹터별 리스닝 세션 시작. 에이전트 상호운용성·보안을 위한 미국 최초 연방 프레임워크 [[G-30]](#ref-g-30)
- **NIST NCCoE — AI Agent Identity & Authorization 콘셉트 페이퍼(2/5 발행)**: OAuth 2.0 확장, SP 800-207(Zero Trust), SP 800-63-4(디지털 ID) 기반 에이전트 인가·검증 체계 제안 [[G-30]](#ref-g-30)
- **McKinsey AI Agent 거버넌스 로드맵(3월)**: 6단계 — 에이전트 ID·범위 정의 → 인간 감독 → 최소 권한 접근 → 모니터링·감사 → 멀티에이전트 거버넌스 → 라이프사이클 관리 [[G-31]](#ref-g-31)
- **CFPB(Consumer Financial Protection Bureau)·SEC(Securities and Exchange Commission) 규제 공백**: Regulation E(소비자 결제)에 AI 에이전트 인가 분쟁 조항 없음. SOX Section 302(내부 통제)에 AI 모델 파라미터 감사 추적 미포함 [[G-32]](#ref-g-32)

### 시사점
- EU AI Act 고위험 전면 적용까지 D-118. 에이전트 오케스트레이션이 "고위험 AI"로 분류될 경우 리스크 관리·투명성·인간 감독 의무 발생
- NIST가 4/2 코멘트 마감 후 섹터별 리스닝 세션을 시작하면서 미국도 에이전트 전용 규제 프레임워크 구축 가속
- Colorado AI Act(6/1 시행, D-56)이 신규 카운트다운 항목으로 추가 — 고위험 AI 공개 요건이 에이전트 배포에 영향

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **에이전트 프레임워크 GA 완료 = 프로덕션 진입 시점**: MS Agent Framework 1.0(4/3), Copilot Studio 멀티에이전트(4/1), AWS AgentCore Policy(GA) — 주요 3사가 같은 주에 GA 전환을 완료. 파일럿 시작 시 RC 불안정성 리스크가 해소된 창(window).

2. **온디바이스 에이전트 + 엣지 NPU 수렴**: Google Gemma 4 E2B(1.5GB 미만 에이전트 모델)와 ASUS UGen300(40 TOPS USB 가속기)의 동시 출현은 클라우드 의존 없는 엣지 에이전트 실행 시나리오를 현실화. 통신사 MEC 플랫폼에서 에이전트 호스팅 가능성 검토 가치.

3. **거버넌스 레이어 정착**: AWS AgentCore Policy GA + NIST AI Agent Standards Initiative + McKinsey 6단계 거버넌스 로드맵이 같은 시기에 수렴. "에이전트 배포 전 거버넌스 필수"라는 업계 합의 형성.

### 후속 조치 제안

- ⚠️ **Claude Haiku 3 은퇴(4/20) 2주 남음** — 서브에이전트 파이프라인 즉시 마이그레이션 (`claude-haiku-4-5-20251001`)
- 🟡 agent-orchestration 지속 모니터링: MS Agent Framework GA 후속·MCP SDK v2 진행 상황 추적
- 🟡 edge-ai 지속 모니터링: ASUS UGen300 Windows 드라이버(5월)·MediaTek Genio 420 샘플링 후속
- 📂 Obsidian 동기화: `/obsidian-bridge` 실행
- 📅 다음 도메인: `/weekly-monitor voice-ai`

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Microsoft DevBlogs — Agent Framework Version 1.0 | [링크](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/) | release | 2026-04-03 | [A] |
| <a id="ref-g-02"></a>G-02 | DEV Community — MCP Dev Summit 2026: What Python Developers Should Pay Attention To | [링크](https://dev.to/peytongreen_dev/mcp-dev-summit-2026-what-python-developers-should-actually-pay-attention-to-5ald) | blog | 2026-04-02 | [B] |
| <a id="ref-g-03"></a>G-03 | Linux Foundation — MCP Dev Summit Schedule | [링크](https://events.linuxfoundation.org/mcp-dev-summit-north-america/program/schedule/) | event | 2026-04-02 | [A] |
| <a id="ref-g-04"></a>G-04 | Google Developers Blog — Gemma 4 Agentic Skills at the Edge | [링크](https://developers.googleblog.com/bring-state-of-the-art-agentic-skills-to-the-edge-with-gemma-4/) | blog | 2026-04-02 | [A] |
| <a id="ref-g-05"></a>G-05 | NVIDIA Blog — RTX to Spark: Gemma 4 Local Agentic AI | [링크](https://blogs.nvidia.com/blog/rtx-ai-garage-open-models-google-gemma-4/) | blog | 2026-04-02 | [B] |
| <a id="ref-g-06"></a>G-06 | Microsoft Copilot Blog — Multi-agent Orchestration GA | [링크](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/new-and-improved-multi-agent-orchestration-connected-experiences-and-faster-prompt-iteration/) | release | 2026-04-01 | [A] |
| <a id="ref-g-07"></a>G-07 | GitHub — langchain-ai/langgraph Releases | [링크](https://github.com/langchain-ai/langgraph/releases) | release | 2026-04-03 | [A] |
| <a id="ref-g-08"></a>G-08 | IBM — watsonx Orchestrate Deepgram·ElevenLabs Partnership | [링크](https://www.ibm.com/new/announcements/how-watsonx-orchestrate-is-helping-modernize-customer-care) | release | 2026-04-01 | [A] |
| <a id="ref-g-09"></a>G-09 | GitHub — openai/openai-agents-python Releases | [링크](https://github.com/openai/openai-agents-python/releases) | release | 2026-04-01 | [A] |
| <a id="ref-g-10"></a>G-10 | The New Stack — AWS AgentCore Policy GA | [링크](https://thenewstack.io/aws-new-policy-layer-in-bedrock-agentcore-makes-sure-ai-agents-cant-give-away-the-store/) | news | 2026-04 | [B] |
| <a id="ref-g-11"></a>G-11 | AWS — AgentCore Runtime Stateful MCP | [링크](https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-bedrock-agentcore-runtime-stateful-mcp/) | release | 2026-03 | [A] |
| <a id="ref-g-12"></a>G-12 | ABNewswire — Multi-Model Routing Must-Have 2026 | [링크](https://markets.financialcontent.com/stocks/article/abnewswire-2026-4-3-2026-agentic-ai-era-why-multi-model-routing-has-become-a-must-have-not-a-nice-to-have) | news | 2026-04-03 | [B] |
| <a id="ref-g-13"></a>G-13 | CrewAI Community — Release 1.1.0 | [링크](https://community.crewai.com/t/new-release-crewai-1-1-0-is-out/7142) | release | 2025-10 | [B] |
| <a id="ref-g-14"></a>G-14 | New Market Pitch — Agentic AI Funding Trends | [링크](https://newmarketpitch.com/blogs/news/agentic-ai-funding-trends) | report | 2026 | [B] |
| <a id="ref-g-15"></a>G-15 | ASUS Pressroom — UGen300 USB AI Accelerator | [링크](https://press.asus.com/news/press-releases/asus-ugen300-usb-ai-accelerator-generative-ai-edge/) | news | 2026-04-01 | [A] |
| <a id="ref-g-16"></a>G-16 | Nordic Semiconductor — nRF54L Series SoC with Axon NPU | [링크](https://www.nordicsemi.com/Nordic-news/2026/01/nRF54L-Series-SoC-with-NPU-and-Nordic-Edge-AI-Lab-make-on-device-intelligence-easily-accessible) | news | 2026-01 | [A] |
| <a id="ref-g-17"></a>G-17 | Synaptics — Coral Dev Board with Torq NPU | [링크](https://www.synaptics.com/company/news/google-research-and-synaptics-launch-next-generation-coral-dev-board-for-developers-to-bring-multimodal-edge-ai-applications-to-life) | news | 2026-03-10 | [A] |
| <a id="ref-g-18"></a>G-18 | MediaTek — Genio Platforms for Robotics, Drones, IoT | [링크](https://www.mediatek.com/press-room/mediatek-adds-new-genio-platforms-to-bring-ai-processing-to-robotics-drones-and-industrial-iot) | news | 2026-03-10 | [A] |
| <a id="ref-g-19"></a>G-19 | TI Newsroom — MCU Portfolio with TinyEngine NPU | [링크](https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-10-ti-expands-microcontroller-portfolio-and-software-ecosystem-to-enable-edge-ai-in-every-device.html) | news | 2026-03-10 | [A] |
| <a id="ref-g-20"></a>G-20 | Ambiq — Atomiq Ultra-Low Power NPU SoC | [링크](https://ambiq.com/news/ambiq-unveils-atomiq-the-worlds-first-ultra-low-power-npu-soc-built-on-spot/) | news | 2026-01 | [A] |
| <a id="ref-g-21"></a>G-21 | LocalAIMaster — NPU Comparison 2026 | [링크](https://localaimaster.com/blog/npu-comparison-2026) | blog | 2026 | [C] |
| <a id="ref-g-22"></a>G-22 | Ericsson — SoftBank AI-RAN + MEC PoC | [링크](https://www.ericsson.com/en/press-releases/2026/2/softbank-corp-and-ericsson-demonstrate-network-enabled-physical-ai-with-ai-ran) | news | 2026-02-27 | [A] |
| <a id="ref-g-23"></a>G-23 | Fierce Network — T-Mobile NVIDIA Blackwell AI-RAN | [링크](https://www.fierce-network.com/broadband/nvidia-gtc-t-mobile-and-nvidia-push-physical-ai-network-edge-0) | news | 2026-03 | [B] |
| <a id="ref-g-24"></a>G-24 | IBTimes — Qualcomm Korea AI Startup Program | [링크](https://www.ibtimes.sg/qualcomm-joins-south-koreas-ai-startup-program-expand-edge-ai-push-amid-smartphone-slowdown-85006) | news | 2026-04 | [B] |
| <a id="ref-g-25"></a>G-25 | Android Authority — Galaxy S26 EdgeFusion On-Device AI | [링크](https://www.androidauthority.com/galaxy-s26-exynos-2600-on-device-ai-image-generation-3638116/) | news | 2026 | [B] |
| <a id="ref-g-26"></a>G-26 | Hailo — Hailo-10H GA | [링크](https://hailo.ai/company-overview/newsroom/news/hailo-announces-general-availability-of-hailo-10h-edge-ai-accelerator-with-generative-ai-capabilities/) | news | 2026 | [A] |
| <a id="ref-g-27"></a>G-27 | Mordor Intelligence — Edge AI Chips Market 2031 | [링크](https://www.mordorintelligence.com/industry-reports/edge-artificia-intelligence-chips-market) | report | 2026 | [B] |
| <a id="ref-g-28"></a>G-28 | GlobeNewswire — Edge AI Chips Forecast 2026-2036 | [링크](https://www.globenewswire.com/news-release/2026/03/11/3253565/0/en/Edge-AI-Chips-Markets-Technologies-and-Forecasts-Report-2026-2036-Architectures-Applications-Competitive-Dynamics-Geographic-Forecasts-and-54-Detailed-Company-Profiles.html) | report | 2026-03-11 | [B] |
| <a id="ref-g-29"></a>G-29 | Nordic DevZone — Axon NPU Specs Q&A | [링크](https://devzone.nordicsemi.com/f/nordic-q-a/127431/nrf54lm20b-axon-npu-performance-specs/563412) | blog | 2026 | [B] |
| <a id="ref-g-30"></a>G-30 | NIST — AI Agent Standards Initiative | [링크](https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure) | policy | 2026-02-17 | [A] |
| <a id="ref-g-31"></a>G-31 | McKinsey — AI Agent Governance Roadmap | [링크](https://www.mckinsey.com/capabilities/quantumblack/our-insights/why-agents-are-the-next-frontier-of-generative-ai) | report | 2026-03 | [B] |
| <a id="ref-g-32"></a>G-32 | Data Innovation — Agentic Commerce Regulation Gap | [링크](https://datainnovation.org/2026/03/agentic-commerce-is-coming-but-regulation-meant-for-humans-will-slow-it-down/) | report | 2026-03 | [B] |
| <a id="ref-g-33"></a>G-33 | Baker Donelson — 2026 AI Legal Forecast | [링크](https://www.bakerdonelson.com/2026-ai-legal-forecast-from-innovation-to-compliance) | report | 2026 | [B] |
| <a id="ref-e-01"></a>E-01 | IBM — Elsewedy Electric Agentic AI with watsonx | [링크](https://mena-fintech.org/news/elsewedy-electric-and-ibm-advance-enterprise-scale-agentic-ai-adoption-using-watsonx-portfolio/) | IR/발표 | 2026-04-01 | [A] |
| <a id="ref-p-01"></a>P-01 | Liu et al. — Hierarchical Memory Orchestration for Persistent Agents | [링크](https://arxiv.org/abs/2604.01670) | paper | 2026-04-02 | [A] |
| <a id="ref-p-02"></a>P-02 | ClinicalAgents: Multi-Agent Orchestration with Dual-Memory | [링크](https://arxiv.org/abs/2603.26182) | paper | 2026-03-27 | [A] |
| <a id="ref-p-03"></a>P-03 | Tummalapalli et al. — LLM Inference at the Edge | [링크](https://arxiv.org/abs/2603.23640) | paper | 2026-03-24 | [A] |
| <a id="ref-p-04"></a>P-04 | NXP et al. — eIQ Neutron: Edge-AI Inference with Integrated NPU | [링크](https://arxiv.org/abs/2509.14388) | paper | 2025 | [A] |
| <a id="ref-c-01"></a>C-01 | HN — MCPlexor: MCP Multiplexer Token Waste | [링크](https://news.ycombinator.com/item?id=46942466) | community | 2025-12 | [C] |
| <a id="ref-c-02"></a>C-02 | Harrison Chase — LangChain Interrupt 2025 Keynote | [링크](https://www.youtube.com/watch?v=DrygcOI-kG8) | community | 2025-05 | [B] |
| <a id="ref-c-03"></a>C-03 | MLOps × Prosus — AI Agents in Production Conference | [링크](https://home.mlops.community/home/content/agents-in-production-2025) | community | 2025-11 | [B] |
| <a id="ref-c-04"></a>C-04 | HN — Show HN: mcp-agent (MCP Ecosystem Quality) | [링크](https://news.ycombinator.com/item?id=42867050) | community | 2025-01 | [C] |
| <a id="ref-c-05"></a>C-05 | Douwe Kiela — RAG Agents in Production (AI Engineer Summit) | [링크](https://www.youtube.com/watch?v=kPL-6-9MVyA) | community | 2025-02 | [B] |
| <a id="ref-c-06"></a>C-06 | HN — AI PCs Aren't Good at AI: CPU Beats NPU | [링크](https://news.ycombinator.com/item?id=41863061) | community | 2024-10 | [C] |
| <a id="ref-c-07"></a>C-07 | HN — Google AI Edge: On-device AI Deployment | [링크](https://news.ycombinator.com/item?id=40511391) | community | 2025-06 | [C] |
