---
type: weekly-monitor
domain: agentic-ai
week: 2026-W13
date: 2026-03-23
l3_count: 12
deep_count: 3
---

# 주간 기술 동향: Agentic AI (2026-W13)

## Executive Summary

| 세부기술 | 신호 | 핵심 내용 | 분석 |
|----------|------|----------|------|
| Agent Orchestration | 🟡 | Google Colab MCP Server 오픈소스(3/17), MCP 2026 로드맵 공개, MS Agent Framework GA 임박, A2A 150개+ 조직 | Deep |
| GPU Orchestration | 🟡 | SkyPilot Job Groups+AI 에이전트 자율 실험 실증, Ocean Network P2P 베타(3/17), AKS DRA+vGPU GA, GTC 2026 추론 변곡점 | Deep |
| 5G SA/6G (AI-RAN) | 🟡 | SKT-에릭슨 AI-RAN MoU(3/19, 5년), NVIDIA Aerial 전면 오픈소스(Apache 2.0), OCUDU 재단 출범 | Deep |
| On-Device sLM | 🟢 | Gemma 3n GA·SmolLM3-3B SOTA 안정화, W12 대비 신규 릴리스 없음 | Quick |
| Edge AI | 🟢 | GTC 2026 'Inflection of Inference' 테마 확인, ExecuTorch 1.0 프로덕션 확산 | Quick |
| Adaptive RAG | 🟢 | Agentic RAG 57%+ 도입, CRAG 패턴 정착 유지 | Quick |
| Agentic Context Engineering | 🟢 | ACE 오픈소스 생태계 성숙 지속, 이번 주 신규 변화 없음 | Quick |
| Agent Planning | 🟢 | ReAcTree + hybrid plan-execute 산업 표준 정착 중 | Quick |
| FeedbackOps (Meta-prompt) | 🟢 | DSPy MIPROv2 안정, 이번 주 돌파구 없음 | Quick |
| EvaluationOps (KMS) | 🟢 | RAGAS 표준 정착, MLflow 프레임워크 통합 진행 | Quick |
| MLOps Pipeline | 🟢 | MLOps→LLMOps 전환 지속, 시장 $4.38B | Quick |
| Speaker Diarization | 🟢 | AssemblyAI Universal-3-Pro·Gladia Solaria-1 점진적 개선 | Quick |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음
>
> **분석** : Deep = 심층 리서치 수행 | Quick = 1줄 요약만

---

## 🟢 Quick 요약 (변화 미미)

### On-Device sLM
- W12에서 발표된 SmolLM3-3B(SOTA), Qwen3.5-9B, Gemma 3n 멀티모달이 안정화 단계에 진입. 이번 주 신규 모델 릴리스 없음. 2026형 NPU(Qualcomm X2/Samsung Exynos 2600/MediaTek) 세대교체 성과가 실제 디바이스에 적용되는 시차 단계.

### Edge AI
- GTC 2026에서 Jensen Huang이 "Inflection of Inference"를 핵심 메시지로 제시 — 추론이 전체 AI 컴퓨트의 2/3를 차지하며 에지로 이동하는 구조적 전환 확인. ExecuTorch 1.0이 Meta 플랫폼(Instagram, WhatsApp, Facebook)에서 프로덕션 사용 확산. 50KB 풋프린트, 12개+ 하드웨어 백엔드 지원.

### Adaptive RAG
- Agentic RAG 프로덕션 도입률 57%+ 유지. CRAG(Corrective RAG) 패턴이 기업 배포 표준으로 정착. 검색 품질 > 생성 품질 우선순위 역전 인식 확산 지속. 이번 주 추가 돌파구 없음.

### Agentic Context Engineering
- W11에서 ACE(ICLR 2026), CORPGEN(Microsoft 3계층 메모리)을 상세 분석한 이후 신규 발표 없음. ACE 오픈소스 생태계가 점진적으로 성숙 중.

### Agent Planning
- ReAcTree + hybrid plan-execute 패턴이 산업 표준으로 정착 중. METR 태스크 시간 14.5시간 달성(7개월마다 2배) 추세 유지. 이번 주 추가 변화 없음.

### FeedbackOps (Meta-prompt Engineering)
- DSPy MIPROv2 옵티마이저와 GEPA 기반 자동 프롬프트 최적화가 안정적으로 운영 중. 산업 적용 사례는 제한적이나 프레임워크 성숙도는 높아지는 추세.

### EvaluationOps (KMS 성능평가)
- LLM-as-judge가 인간 평가자와 80-90% 일치율 유지. RAGAS 표준 정착. MLflow에 DeepEval+RAGAS+Phoenix 통합 진행 중. 추적 가능성(traceability) 키워드 지속.

### MLOps Pipeline
- MLOps 시장 $4.38B(CAGR 39.8%), 72% 기업 자동화 도입. MLOps→LLMOps 전환 가속 추세 유지. 이번 주 신규 변화 없음.

### Speaker Diarization
- AssemblyAI Universal-3-Pro와 Gladia Solaria-1(103ms 부분 지연) 안정 운영. 점진적 개선 지속 중이나 돌파구 수준 변화 없음.

---

## 🟡 Agent Orchestration — 주목

> 상세 리서치: [2026-03-23_research-agent-orchestration.md](2026-03-23_research-agent-orchestration.md)

### 이전 대비 변화
- 전주: Claude Agent SDK 런타임 MCP, A2A v0.3 gRPC, MCP CIMD 엔터프라이즈 인증 — 프로토콜 성숙화
- 금주: Google Colab MCP Server 오픈소스(3/17), MCP 2026 로드맵 공개, Microsoft Agent Framework GA 임박 — 생태계 확장 + 도메인 수직화
- 변화 방향: Big Tech 인프라(클라우드 GPU)→MCP 표준 채택 + 금융·과학 도메인 특화 구현 가속

### 기술 동향

1. **Google Colab MCP Server 출시(3/17) — 클라우드 GPU 런타임을 MCP 표준으로 개방.**
   MCP 호환 에이전트(Claude Code, Gemini CLI 등)가 Google Colab 노트북을 원격 런타임으로 직접 제어. 셀 생성·코드 실행·의존성 설치를 에이전트가 수행. `uvx`/`npx`로 서버 기동, GitHub(`googlecolab/colab-mcp`)에서 오픈소스. [[G-01]](#ref-g-01)

2. **MCP 2026 로드맵 공개 — 엔터프라이즈 준비도 4대 축 확정.**
   HTTP transport 수평 확장, Tasks SEP-1686 재시도·만료 정책, 거버넌스 컨트리뷰터 래더, 엔터프라이즈 SSO·감사 트레일 4대 축. 표준화 속도가 채택 속도를 못 따라가는 갭을 공식 인정. [[G-02]](#ref-g-02)

3. **Microsoft Agent Framework GA 임박 — AutoGen·Semantic Kernel 통합 완료.**
   Q1 2026 말 GA 목표. Python·.NET 통합, 그래프 기반 워크플로우, A2A·MCP 프로토콜 지원. AutoGen·Semantic Kernel은 메인테넌스 모드 전환 완료. [[G-03]](#ref-g-03)

4. **MAS-Orchestra — RL 기반 10x 효율 향상.**
   MAS 오케스트레이션을 function-calling RL로 정형화. MASBENCH에서 수학·멀티홉 QA·검색 QA 전반에서 강 베이스라인 대비 10배+ 효율 달성. "어떤 모델"에서 "어떻게 조율하느냐"로 학술 트렌드 전환 재확인. [[P-01]](#ref-p-01)

### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Google | Colab MCP Server 오픈소스(3/17). A2A 파트너 150개+ 조직, Tyson Foods·Gordon Food Service 공급망 실증 | [[G-01]](#ref-g-01), [[G-04]](#ref-g-04) |
| Microsoft | Agent Framework RC1 유지, Q1 GA 목표. AutoGen·SK 메인테넌스 전환 완료 | [[G-03]](#ref-g-03) |
| Anthropic | Claude Agent SDK v0.1.48 유지. Claude Code bare mode·권한 릴레이 추가 | [[G-05]](#ref-g-05) |
| CrewAI | v1.10 A2A 지원 추가, GitHub Stars 45,900+, 인증 개발자 10만명+ | [[G-06]](#ref-g-06) |

### 시장 시그널
- Gartner: 2026년 말 엔터프라이즈 앱 **40%**에 에이전트 탑재(2025년 5% 미만 대비) [[G-07]](#ref-g-07)
- 글로벌 에이전틱 AI 시장 **$91~109억(2026)**, 전년 대비 25~49% 성장 [[G-08]](#ref-g-08)
- 기업 **57%** AI 에이전트 프로덕션 배포 완료, 배포 최우선 요구사항: 보안·감사 가능성(75%) [[G-09]](#ref-g-09)
- Gartner 경고: 에이전틱 AI 공급이 수요 초과 — 시장 조정 가능성 [[G-10]](#ref-g-10)

### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| MAS-Orchestra (Anonymous et al., 2026) | RL 기반 Holistic 오케스트레이션, 10x+ 효율 향상 | [[P-01]](#ref-p-01) |
| OrchMAS (Feng et al., 2026) | 과학 도메인 2-티어 오케스트레이션, 이종 전문가 에이전트 동적 구성 | [[P-02]](#ref-p-02) |
| AdaptOrch (dmae97 et al., 2026) | 토폴로지 선택 > 모델 선택, 12~23% 성능 향상 | [[P-03]](#ref-p-03) |

### 전략적 시사점

**기회**
- Colab MCP Server로 에이전트 기반 대규모 데이터 전처리·모델 실험 자동화 즉시 가능
- MCP Tasks SEP-1686 개선이 장기 실행 에이전트 워크플로우 신뢰성 확보의 핵심

**위협**
- 에이전틱 AI 공급 수요 초과 경고 — 투자 플랫폼 지속성 불확실 리스크
- MCP 엔터프라이즈 SSO·감사 표준 미완성 — 규제 환경에서 컴플라이언스 리스크

---

## 🟡 GPU Orchestration — 주목

> 상세 리서치: [2026-03-23_research-gpu-orchestration.md](2026-03-23_research-gpu-orchestration.md)

### 이전 대비 변화
- 전주: SkyPilot Shopify 채택, AMD ROCm 7.0+Ray — 구조적 돌파구 없음(🟢)
- 금주: AI 에이전트가 GPU 클러스터를 자율 관리하는 "에이전트 주도 오케스트레이션" 실체화, 탈중앙화 P2P 레이어 프로덕션 진입(🟡)
- 변화 방향: 오케스트레이션 주체가 인간→에이전트로 이동, 중앙화 Neocloud vs 탈중앙화 DePIN 경쟁 구도 부상

### 기술 동향

1. **SkyPilot Job Groups — 이종 하드웨어 RL 학습의 단일 YAML 오케스트레이션.**
   PPO/GRPO/RLHF의 Trainer(고성능 GPU)·Rollout Server(저가 GPU)·Replay Buffer(고메모리 CPU) 전체를 단일 YAML로 정의. DNS 기반 자동 서비스 디스커버리. 20개+ 클라우드·K8s·Slurm 지원. [[G-11]](#ref-g-11)

2. **SkyPilot + Claude Code 에이전트 자율 실험 — 910회 실험·2.87% 손실 개선.**
   Claude Code에 16-GPU K8s 클러스터 접근 부여 시 8시간 동안 약 910회 자동 제출. 순차 대비 9배 처리량. H100/H200 성능 차이를 자체 발견, 2-tier 검증 전략 구사. 비용: 컴퓨트 ~$300 + Claude API ~$9. [[G-12]](#ref-g-12)

3. **Ocean Network P2P GPU 베타(3/17) — 탈중앙화 컴퓨트 레이어 실사용 진입.**
   VS Code·Cursor·Windsurf 네이티브 통합. Aethir 파트너십으로 H200~H100 즉시 공급. Pay-Per-Use Escrow(Base/Ethereum L2). [[G-13]](#ref-g-13)

4. **Microsoft AKS DRA + vGPU GA — Kubernetes GPU 가상화 분할 프로덕션 진입.**
   K8s 1.34+ DRA로 단일 GPU를 1/6·1/3·1/2 프로파일 분할 할당. MIG+DRA 조합도 GA. [[G-14]](#ref-g-14)

5. **NVIDIA GTC 2026 — 추론·에이전트 중심 GPU 수요 구조 재편.**
   데이터센터를 "AI Factory" 재정의. Vera Rubin NVL72(3.6 exaflops/rack) 2026 H2 배포. NemoClaw 에이전트 스택 오픈소스. $1조+ 수요 전망. [[G-15]](#ref-g-15)

### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| SkyPilot | Job Groups(3/2) 출시, Claude Code 자율 910회 실험 실증(9x 처리량) | [[G-11]](#ref-g-11), [[G-12]](#ref-g-12) |
| NVIDIA | GTC 2026: Vera Rubin NVL72, NemoClaw 오픈소스, AWS 100만+ GPU 협력 | [[G-15]](#ref-g-15) |
| CoreWeave | HGX B300 GA — TTFT 4.93x, 처리량 3.42x(HGX H200 대비). Cursor 프로덕션 이전 중 | [[G-16]](#ref-g-16) |
| Microsoft | AKS DRA+vGPU GA(3/6), MIG+DRA GA(3/3). Ray on AKS 멀티리전 Private Preview | [[G-14]](#ref-g-14) |
| Ocean Network | P2P GPU 베타(3/17), IDE 네이티브 통합, Aethir H200~H100 즉시 공급 | [[G-13]](#ref-g-13) |

### 시장 시그널
- GTC 핵심 메시지: 학습 중심→추론·에이전트 중심 전환 — GPU 오케스트레이션 요구가 고빈도 저지연 추론+에이전트 작업 큐로 다변화 [[G-15]](#ref-g-15)
- AWS·Google·Azure 3사 모두 Managed Ray 통합 발표 — 오케스트레이션이 클라우드 벤더 lock-in의 새 경쟁지 [[G-17]](#ref-g-17)
- DePIN GPU 시장 캡 $52억→$190억(1년 만에 3.6x 성장) [[G-18]](#ref-g-18)
- K8s DRA GA 전환 가속 — vGPU+DRA와 MIG+DRA 3일 간격 연속 GA [[G-14]](#ref-g-14)

### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| GFS (ASPLOS '26) | GPU 클러스터 선점 인식 스케줄링, 스팟 인스턴스 예측 관리 | [[P-04]](#ref-p-04) |
| MSched (arXiv, 2025-12) | GPU 하드웨어 동기화 기반 CPU 개입 없는 멀티태스킹 | [[P-05]](#ref-p-05) |

### 전략적 시사점

**기회**
- 에이전트 주도 GPU 오케스트레이션 조기 내재화 — 인증·비용 제어·정책 프레임워크 선제 설계 필요
- DRA 기반 GPU 분할로 중소 워크로드 비용 최적화 즉시 가능

**위협**
- 하이퍼스케일러 Managed Ray lock-in 위험 — 벤더별 최적화가 이식성 제한
- 에이전트 GPU 접근의 비용 폭주 리스크 — 거버넌스 없이 자율 실행 시 예측 불가 비용

---

## 🟡 5G SA/6G (AI-RAN) — 주목

> 상세 리서치: [2026-03-23_research-5g-6g-ai-ran.md](2026-03-23_research-5g-6g-ai-ran.md)

### 이전 대비 변화
- 전주: MWC 2026 대형 발표 — NVIDIA+12사 연합, Nokia 2027 상용, T-Mobile OTA, SoftBank SRv6(🔴)
- 금주: MWC 선언→실행 전환 — SKT-에릭슨 MoU(3/19), NVIDIA Aerial 오픈소스, OCUDU 재단(🟡)
- 변화 방향: 선언→파트너십 계약·오픈소스 생태계 구축 실행 단계 진입

### 기술 동향

1. **NVIDIA Aerial 전면 오픈소스화(Apache 2.0) — AI-RAN 개발 접근성 혁명적 확대.**
   CUDA-Accelerated RAN(상용급 3GPP·O-RAN 준수), Aerial Omniverse Digital Twin(AODT), Aerial Framework(Python→CUDA 변환) 전체 공개. R&D 사이클 "개월→시간" 단축. DGX Spark 급 장비로 랩 수준 연구자도 상용급 개발 가능. [[G-19]](#ref-g-19)

2. **SKT-에릭슨 MoU 체결(3/19) — 5년간 AI-RAN·6G 5개 축 협력.**
   2031년까지 유효. (1) AI-powered RAN, (2) 5G 수익화, (3) 오픈·자율 네트워크, (4) Zero Trust 보안, (5) 6G 표준화(ISAC 포함). Ericsson ASIC 전략 + SKT ATHENA 비전 결합. NVIDIA GPU 진영(Nokia)에 대항하는 독립 아키텍처 진영 강화. [[E-01]](#ref-e-01)

3. **Linux Foundation OCUDU 재단 출범 — 오픈소스 AI-RAN 탈벤더록인.**
   창립 멤버 21개사: AMD, AT&T, Cisco, DeepSig, Ericsson, Nokia, NVIDIA, SoftBank, SRS, Verizon. 연구기관 17곳. 경쟁자인 Nokia-Ericsson이 동일 재단 참여. O-RAN 기반 CU·DU 스택 + AI 알고리즘 통합 레퍼런스 플랫폼. [[G-20]](#ref-g-20)

4. **Wind River + AMD: CPU 전용 O-RAN/AI-RAN 통합 플랫폼 상용 출시.**
   AMD EPYC + Wind River Cloud Platform. 단일 서버에서 vRAN + AI 추론 동시 구동. GPU 가속 없이 범용 CPU 기반 AI-RAN 구현의 상용 진입점. CAPEX 최대 50% 절감 주장. [[G-21]](#ref-g-21)

5. **Samsung + AMD: AI-RAN 검증→상용 배포 공식 전환.**
   EPYC 9005 기반 다중 셀 AI vRAN, 추가 가속기 없이 완전 가상화 소프트웨어 스택만으로 상용급 성능. Videotron(캐나다) 배포 레퍼런스. [[G-22]](#ref-g-22)

6. **Rakuten Mobile: 전국망 RIC 구축 완료 — 오픈 RAN AI 운영 레퍼런스.**
   세계 최초 전국 규모 RIC + 제3자 rApp 배포. 전력 소비 15~20% 절감. [[G-23]](#ref-g-23)

### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| NVIDIA | Aerial 전체 스택 Apache 2.0 오픈소스. AI-RAN Alliance 130개사 | [[G-19]](#ref-g-19) |
| SKT | 에릭슨 MoU 체결(3/19, 2031년까지). ASIC 기반 AI-RAN 진영 합류 | [[E-01]](#ref-e-01) |
| Ericsson | SKT + Chunghwa Telecom MoU. ASIC 기반 독립 아키텍처 진영 확대 | [[G-24]](#ref-g-24) |
| Samsung | AMD EPYC 기반 AI-RAN 상용 배포 전환. Videotron 레퍼런스 | [[G-22]](#ref-g-22) |
| Rakuten | 전국망 RIC + rApp 배포 완료. 전력 15~20% 절감 | [[G-23]](#ref-g-23) |
| Wind River + AMD | CPU 전용 통합 O-RAN/AI-RAN 상용 플랫폼 출시 | [[G-21]](#ref-g-21) |

### 시장 시그널
- AI-RAN Alliance 132개사 확대, Qualcomm·SKT·Vodafone 이사회 합류 [[G-25]](#ref-g-25)
- 통신사 AI 투자 ~$210억(2026), AI-RAN이 주요 수혜 분야 [[G-26]](#ref-g-26)
- Intel AI-RAN Alliance 미참여 — 칩 공급망 NVIDIA vs CPU/ASIC 양분 [[G-27]](#ref-g-27)
- 3GPP Rel-20 2026.9월 동결, Rel-21(첫 6G 스펙) 2027.3월 Full Steam [[G-28]](#ref-g-28)

### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| E2E Intelligence in 6G (Han et al., 2026) | LLM+ReAct 기반 RAN-CN 통합 지능 프레임워크 | [[P-06]](#ref-p-06) |
| AI-Native PHY-Layer (Mutescu et al., 2025) | 6G 스펙트럼 인식 AI 탐지기, 파형 판별 99.5% 정확도 | [[P-07]](#ref-p-07) |
| Transparent 6G AI-RAN (ScienceDirect, 2025) | 설명 가능한 DRL 기반 네트워크 슬라이싱 서베이 | [[P-08]](#ref-p-08) |

### 전략적 시사점

**기회**
- NVIDIA Aerial 오픈소스로 AI-RAN 프로토타입 진입 비용 대폭 하락
- SKT-에릭슨 MoU로 ISAC 공동 연구 진입점 확보, 6G 표준화 영향력
- OCUDU 초기 참여 시 오픈소스 AI-RAN 스택 방향에 영향력 행사 가능

**위협**
- Nokia(GPU) vs Ericsson(ASIC) vs Samsung(CPU-only) 전략 분기 — 장비 선택이 칩 아키텍처 종속으로
- Aerial 오픈소스로 후발 통신사도 빠르게 AI-RAN 실증 가능 — 차별화 기회 축소
- 6G 표준 확정 전 독점적 구현에 투자 시 재작업 리스크

---

## 경쟁사 동향 (SKT / KT)

> 이번 주 Agentic AI 도메인 관련 SKT·KT의 주요 움직임.

### SKT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| SKT-에릭슨 AI-RAN MoU | 3/19 체결. 5년간 AI-RAN, 5G 수익화, 6G 표준화 등 5개 축 협력 | 5g-6g-ai-ran | [[E-01]](#ref-e-01) |
| "1인 1 AI 에이전트" 전사 AX 전환 | 정재헌 부회장, 에이닷 비즈·폴라리스·플레이그라운드 플랫폼으로 전직원 에이전트 활용 목표 | agent-orchestration | [[E-02]](#ref-e-02) |
| Panmnesia CXL AI DC 협력 | CXL 기반 차세대 AI 데이터센터 아키텍처 공동 개발 | gpu-orchestration | [[E-03]](#ref-e-03) |
| MWC26 풀스택 AI 공개 | AI 인프라·모델·서비스 전범위 역량 시연 | (L3 밖) | [[E-04]](#ref-e-04) |

### KT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| 노코드 '에이전트 빌더' 공개 | MWC26 Drag&Drop 방식, 산업별 템플릿(금융·제조·공공) | agent-orchestration | [[E-05]](#ref-e-05) |
| Mi:um K 2.5 Pro 자체 AI 모델 | 4개 국어 지원, GPU 구축 부담 감소 강조 | ondevice-slm | [[E-06]](#ref-e-06) |
| 148편 AI 논문 발행 (5년간) | 49편 주요 학회(CVPR/EMNLP/NeurIPS) 채택 | (L3 밖) | [[E-07]](#ref-e-07) |
| 6G AI 네트워크 비전 | "초연결, 초신뢰, 지능형 AI 네트워크" 비전 제시 | 5g-6g-ai-ran | [[E-08]](#ref-e-08) |
| K RaaS 로봇 플랫폼 | 피지컬 AI 대중화 선언, MWC26 공개 | (L3 밖) | [[E-09]](#ref-e-09) |

### 시사점
- **SKT**: 에릭슨 MoU(3/19)로 ASIC 기반 AI-RAN 전략 파트너십을 공식화하며 6G 표준화 진영을 확정. "1인 1 에이전트" 전사 전환은 내부 에이전트 오케스트레이션 수요를 빠르게 확대시킬 전망.
- **KT**: "에이전트 빌더"로 비개발자 에이전트 생성 플랫폼을 공개하며 보다 수평적 접근. Mi:um K로 경량 자체 모델 전략도 병행. 두 사 모두 에이전트+네트워크 지능화가 핵심 방향.

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **"에이전트가 인프라를 직접 운용하는 시대" 구체화** — Agent Orchestration의 MCP 생태계 확장(Colab MCP)과 GPU Orchestration의 에이전트 자율 실험(SkyPilot+Claude)이 수렴. 에이전트가 코드 실행 환경(Colab)과 GPU 클러스터(SkyPilot)를 모두 직접 제어하는 풀스택 자율 파이프라인이 현실화되고 있다.

2. **오픈소스가 기술 진입 장벽을 빠르게 해체** — NVIDIA Aerial(AI-RAN), MCP Colab Server, NemoClaw(에이전트 스택)가 동시에 오픈소스화. 프로토콜·인프라·실행 스택 전 계층에서 오픈소스가 표준이 되면서, 기술 보유 자체보다 통합·운영 역량이 차별화 요소로 부상.

3. **표준화 vs 채택 속도의 갭** — MCP 엔터프라이즈 인증이 미완, 6G 표준이 2027년 본격화, K8s DRA가 이제 GA. 산업 현장의 채택 속도가 표준화를 앞서가는 구조적 리스크가 3개 Deep 영역 모두에서 관찰됨.

### 후속 조치 제안

- 5G/6G AI-RAN은 W12→W13 연속 🟡 이상 — SKT-에릭슨 MoU의 전략적 함의가 크므로 `/wtis standard` 검증 고려
- GPU Orchestration이 🟢→🟡로 상향 — 에이전트 주도 오케스트레이션 패턴을 내부 MLOps에 적용하는 방안 검토

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Google Developers Blog — Announcing the Colab MCP Server | [링크](https://developers.googleblog.com/announcing-the-colab-mcp-server-connect-any-ai-agent-to-google-colab/) | news | 2026-03-17 | [A] |
| <a id="ref-g-02"></a>G-02 | MCP Blog — The 2026 MCP Roadmap | [링크](http://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) | official | 2026 | [A] |
| <a id="ref-g-03"></a>G-03 | Microsoft Foundry — Agent Framework Reaches Release Candidate | [링크](https://devblogs.microsoft.com/foundry/microsoft-agent-framework-reaches-release-candidate/) | official | 2026-02-19 | [A] |
| <a id="ref-g-04"></a>G-04 | Cloud Wars — Google Advances A2A Protocol, 150+ Partners | [링크](https://cloudwars.com/ai/google-advances-agent2agent-a2a-protocol-gains-microsoft-and-sap-backing/) | news | 2026 | [B] |
| <a id="ref-g-05"></a>G-05 | Releasebot — Claude Code Release Notes March 2026 | [링크](https://releasebot.io/updates/anthropic/claude-code) | release | 2026-03 | [B] |
| <a id="ref-g-06"></a>G-06 | DEV Community — AutoGen vs LangGraph vs CrewAI 2026 | [링크](https://dev.to/synsun/autogen-vs-langgraph-vs-crewai-which-agent-framework-actually-holds-up-in-2026-3fl8) | blog | 2026 | [C] |
| <a id="ref-g-07"></a>G-07 | Gartner — 40% Enterprise Apps with AI Agents by 2026 | [링크](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025) | press-release | 2025-08-26 | [A] |
| <a id="ref-g-08"></a>G-08 | tech-insider.org — Agentic AI $9B Market Analysis 2026 | [링크](https://tech-insider.org/agentic-ai-enterprise-2026-market-analysis/) | blog | 2026 | [B] |
| <a id="ref-g-09"></a>G-09 | Arcade.dev — State of AI Agents 2026: Enterprise Trends | [링크](https://www.arcade.dev/blog/5-takeaways-2026-state-of-ai-agents-claude/) | blog | 2026 | [B] |
| <a id="ref-g-10"></a>G-10 | Gartner — Agentic AI Supply Exceeds Demand | [링크](https://www.gartner.com/en/newsroom/press-releases/2025-10-07-gartner-says-agentic-ai-supply-exceeds-demand-market-correction-looms) | press-release | 2025-10-07 | [A] |
| <a id="ref-g-11"></a>G-11 | SkyPilot Blog — Job Groups: RL on Heterogeneous Hardware | [링크](https://blog.skypilot.co/job-groups/) | blog | 2026-03-02 | [B] |
| <a id="ref-g-12"></a>G-12 | SkyPilot Blog — Scaling Autoresearch: Agent Gets a GPU Cluster | [링크](https://blog.skypilot.co/scaling-autoresearch/) | blog | 2026-03 | [B] |
| <a id="ref-g-13"></a>G-13 | GlobeNewswire — Ocean Network P2P GPU Orchestration Beta | [링크](https://www.globenewswire.com/news-release/2026/03/17/3257334/0/en/Ocean-Network-launches-beta-for-affordable-P2P-GPU-orchestration.html) | news | 2026-03-17 | [B] |
| <a id="ref-g-14"></a>G-14 | AKS Engineering Blog — DRA with vGPUs on AKS | [링크](https://blog.aks.azure.com/2026/03/06/dra-with-vGPUs-on-aks) | blog | 2026-03-06 | [A] |
| <a id="ref-g-15"></a>G-15 | NVIDIA Blog — GTC 2026 Live Updates | [링크](https://blogs.nvidia.com/blog/gtc-2026-news/) | news | 2026-03-16 | [A] |
| <a id="ref-g-16"></a>G-16 | CoreWeave — HGX B300 AI-Native Cloud Platform | [링크](https://www.coreweave.com/news/coreweave-advances-ai-native-cloud-platform-for-the-next-phase-of-production-scale-ai) | news | 2026-03-17 | [A] |
| <a id="ref-g-17"></a>G-17 | InfoQ — Running Ray at Scale on AKS | [링크](https://www.infoq.com/news/2026/03/ray-aks-ai-microsoft/) | news | 2026-03 | [B] |
| <a id="ref-g-18"></a>G-18 | BlockEden — Decentralized GPU Networks 2026 | [링크](https://blockeden.xyz/blog/2026/02/07/decentralized-gpu-networks-2026/) | blog | 2026-02-07 | [C] |
| <a id="ref-g-19"></a>G-19 | NVIDIA Blog — Open Sources Aerial for AI-Native 6G | [링크](https://blogs.nvidia.com/blog/open-source-aerial-ai-native-6g/) | news | 2026-03 | [A] |
| <a id="ref-g-20"></a>G-20 | Linux Foundation — OCUDU Ecosystem Foundation Launch | [링크](https://www.linuxfoundation.org/press/linux-foundation-announces-ocudu-ecosystem-foundation-to-accelerate-open-source-ai-ran-innovation) | news | 2026-03-01 | [A] |
| <a id="ref-g-21"></a>G-21 | BusinessWire — Wind River AMD Unified O-RAN AI-RAN | [링크](https://www.businesswire.com/news/home/20260301788558/en/Wind-River-Announces-Strategic-Collaboration-with-AMD-Delivering-Industrys-First-Unified-O-RAN-and-AI-RAN-Platform) | news | 2026-03-02 | [A] |
| <a id="ref-g-22"></a>G-22 | Samsung — Samsung AMD Commercial AI-RAN Deployment | [링크](https://news.samsung.com/global/samsung-and-amd-reinforce-strategic-collaboration-to-advance-ai-powered-network-innovations-for-commercial-deployments) | news | 2026-03-03 | [A] |
| <a id="ref-g-23"></a>G-23 | Rakuten Symphony — Nationwide RIC + rApp Deployment | [링크](https://symphony.rakuten.com/newsroom/rakuten-mobile-and-rakuten-symphony-advance-open-ran-innovation-with-third-party-rapp-integration-and-nationwide-ric-deployment) | news | 2026-02-26 | [A] |
| <a id="ref-g-24"></a>G-24 | Ericsson — Chunghwa Telecom 5G-Advanced MoU MWC 2026 | [링크](https://www.ericsson.com/en/press-releases/2026/3/cht-and-ericsson-sign-5g-advanced-and-ai-intelligent-network-mou-at-mwc-2026-to-accelerate-6g-evolution) | news | 2026-03 | [A] |
| <a id="ref-g-25"></a>G-25 | SDxCentral — AI-RAN Alliance 130+ Members MWC | [링크](https://www.sdxcentral.com/news/ai-ran-alliance-pushes-past-130-members-as-ai-native-ran-takes-center-stage-at-mwc/) | news | 2026-03 | [B] |
| <a id="ref-g-26"></a>G-26 | Juniper Research — Telecom AI Investment $21B 2026 | [링크](https://www.juniperresearch.com/press/direct-to-device-5g-advanced-ai-ran-to-redefine-global-connectivity-in-2026/) | news | 2026 | [C] |
| <a id="ref-g-27"></a>G-27 | Fierce Network — Intel Sits Out AI-RAN Alliance | [링크](https://www.fierce-network.com/wireless/mwc-2026-intel-sits-out-ai-ran-alliance-now) | news | 2026-03 | [B] |
| <a id="ref-g-28"></a>G-28 | 3GPP — Release 20 Planning and Progress | [링크](https://www.3gpp.org/news-events/3gpp-news/sa-rel20) | official | 2026 | [A] |
| <a id="ref-e-01"></a>E-01 | SK Telecom — SKT Ericsson MoU 6G Network Innovation | [링크](https://news.sktelecom.com/en/2854) | IR/발표 | 2026-03-19 | [A] |
| <a id="ref-e-02"></a>E-02 | 아시아투데이 — SKT "1인 1 AI 에이전트" 전사 AX 전환 | [링크](https://www.asiatoday.co.kr/kn/view.php?key=20260316010004523) | news | 2026-03-16 | [B] |
| <a id="ref-e-03"></a>E-03 | Yahoo Finance — SKT-Panmnesia CXL AI DC Partnership | [링크](https://finance.yahoo.com/news/sk-telecom-panmnesia-sign-partnership-230000952.html) | news | 2026-03 | [B] |
| <a id="ref-e-04"></a>E-04 | SK Telecom — MWC26 Full Stack AI | [링크](https://news.sktelecom.com/en/2742) | IR/발표 | 2026-03 | [A] |
| <a id="ref-e-05"></a>E-05 | AI타임스 — KT 노코드 에이전트 빌더 MWC26 공개 | [링크](https://www.aitimes.kr/news/articleView.html?idxno=38894) | news | 2026-03 | [B] |
| <a id="ref-e-06"></a>E-06 | 파이낸셜포스트 — KT Mi:um K 2.5 Pro GPU 부담 감소 | [링크](https://www.financialpost.co.kr/news/articleView.html?idxno=249278) | news | 2026-03 | [B] |
| <a id="ref-e-07"></a>E-07 | UPI — KT 148 AI Papers, Expanding Applications | [링크](https://www.upi.com/Top_News/World-News/2026/03/22/KT-artificial-intelligence-research-papers/4131774217655/) | news | 2026-03-22 | [B] |
| <a id="ref-e-08"></a>E-08 | 이투데이 — KT 6G 비전 "지능형 AI 네트워크" | [링크](https://www.etoday.co.kr/news/view/2561207) | news | 2026-03 | [B] |
| <a id="ref-e-09"></a>E-09 | 서울신문 — KT K RaaS 로봇 플랫폼 MWC26 | [링크](https://www.seoul.co.kr/news/economy/industry/2026/03/01/20260301500003) | news | 2026-03 | [B] |
| <a id="ref-p-01"></a>P-01 | Anonymous et al. — MAS-Orchestra: Holistic Orchestration, 10x Efficiency (arXiv:2601.14652) | [링크](https://arxiv.org/abs/2601.14652) | paper | 2026-01 | [A] |
| <a id="ref-p-02"></a>P-02 | Feng et al. — OrchMAS: Heterogeneous Scientific Expert Agents (arXiv:2603.03005) | [링크](https://arxiv.org/abs/2603.03005) | paper | 2026-03 | [A] |
| <a id="ref-p-03"></a>P-03 | dmae97 et al. — AdaptOrch: Topology > Model Selection (arXiv:2602.16873) | [링크](https://arxiv.org/abs/2602.16873) | paper | 2026-02 | [A] |
| <a id="ref-p-04"></a>P-04 | GFS — Preemption-aware GPU Scheduling (ASPLOS '26) | [링크](https://arxiv.org/html/2509.11134v1) | paper | 2026-03 | [A] |
| <a id="ref-p-05"></a>P-05 | MSched — GPU Multitasking via Proactive Memory Scheduling | [링크](https://arxiv.org/html/2512.24637v1) | paper | 2025-12 | [A] |
| <a id="ref-p-06"></a>P-06 | Han et al. — E2E Intelligence in 6G: AI Agent-Based RAN-CN Framework | [링크](https://arxiv.org/abs/2602.23623) | paper | 2026-02 | [B] |
| <a id="ref-p-07"></a>P-07 | Mutescu et al. — AI-Native PHY-Layer in 6G Spectrum-Aware Networks | [링크](https://pmc.ncbi.nlm.nih.gov/articles/PMC12694481/) | paper | 2025-11 | [A] |
| <a id="ref-p-08"></a>P-08 | ScienceDirect — Transparent 6G AI-RAN: Explainable DRL for Network Slicing | [링크](https://www.sciencedirect.com/science/article/pii/S2949715925000757) | paper | 2025 | [A] |
