---
type: weekly-monitor
domain: agentic-ai
week: 2026-W16
date: 2026-04-07
l3_count: 12
deep_count: 1
tags: [claude-code, weekly]
created: 2026-04-07
updated: 2026-04-07
---

# 주간 기술 동향: Agentic AI (2026-W16)

## Executive Summary

> **이번 주 핵심**: W15의 대규모 GA(General Availability) 출시(MS Agent Framework 1.0, Copilot Studio 멀티에이전트, Gemma 4)가 정착하는 조용한 주간이었으나, NTT DOCOMO와 SKT의 vRAN(virtualized RAN)/AI-RAN(AI-Centric RAN) 공동 백서(3/31)가 통신사 관점의 AI-RAN 3대 기술 요건을 공식 정의하며 5G/6G 인프라 전환의 표준화 의제를 선점했다.

| Layer 2 | 세부기술 | 신호 | 핵심 내용 |
|---------|----------|------|----------|
| Hybrid AI Infra | 5G SA/6G (AI-RAN/SRv6) | 🟡 | [파트너십] DOCOMO-SKT vRAN/AI-RAN 공동 백서(3/31): HW/SW 분리·리소스 풀링·xPU 3대 요건 공식화 · [제품출시] Samsung+Vodafone Intel Xeon 6 SoC vRAN 유럽 최초 콜 · [생태계] 3GPP R21 6G 스펙 일정 6월 확정 예정 |
| | Edge AI | 🟢 | W15 ASUS UGen300/Nordic Axon/TI $1 MCU 후속 정착 |
| | On-Device sLM | 🟢 | Gemma 4 E2B/E4B 정착, Gartner "2027년 SLM 3배 사용" 전망 |
| | 실시간 화자분할(2인) | 🟢 | 변화 없음 |
| Trusted Multi-Agent Orchestration | Intelligent Agent Orchestration | 🟢 | W15 GA 정착. Anthropic Conway 상시 에이전트 테스트. 기업 평균 12개 에이전트 운영 |
| | Agent Oriented Orchestration | 🟢 | Plan-and-Act 하이브리드 패턴 안정 유지 |
| Model & Delta Foundry | GPU Orchestration | 🟢 | SkyPilot Agent Skills 에코시스템 안정 |
| | FeedbackOps: Meta-prompt Engineering | 🟢 | DSPy MIPROv2 안정, 신규 릴리스 없음 |
| | EvaluationOps: KMS 성능평가 | 🟢 | RAGAS v0.2+ 안정, LLM-as-judge 성숙 |
| | 데이터-학습-배포 파이프라인 | 🟢 | LLMOps→AgentOps 전환 가속 |
| Self Evolving Architecture | Agentic Context Engineering | 🟢 | Context Engineering 독립 분야 부상, MVC 패턴 확산 |
| 의도 파악 기술 | Adaptive RAG | 🟢 | Agentic RAG 정착, GraphRAG+MCP 표준 아키텍처 |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음
> **태그** : [기술돌파] [제품출시] [경쟁사] [규제] [투자] [논문] [생태계]

---

## 🟢 Quick 요약 (변화 미미)

### Intelligent Agent Orchestration
- W15의 MS Agent Framework 1.0 GA(4/3), Copilot Studio 멀티에이전트 GA(4/1), Google Gemma 4(4/2) 프로덕션 진입이 정착하는 주간. Anthropic이 Conway 상시 에이전트(24/7 활성, 멀티스텝 자율 실행) 테스트 중. Belitsoft 조사에 따르면 기업 평균 12개 AI 에이전트 운영 중이나 50%가 사일로 운영. Microsoft Agent Governance Toolkit MIT 라이선스 오픈소스 공개(4/2).

### Agent Oriented Orchestration
- Plan-and-Act 하이브리드 패턴(고추론 DAG 분해 → 경량 실행 → 재계획)이 엔터프라이즈 배포 주류 유지. AgentOrchestra TEA(Tool-Environment-Agent) Protocol 논문 등장(OpenReview). 이번 주 추가 변화 없음.

### On-Device sLM
- Gemma 4 E2B(1.5GB 미만)/E4B 정착 유지. Gartner는 2027년까지 조직이 범용 LLM(Large Language Model) 대비 소규모 태스크 특화 AI 모델을 3배 더 사용할 것으로 전망. SLM(Small Language Model)이 대형 모델 성능의 80-90%를 달성하며 온디바이스 배포 기본 옵션으로 자리잡음.

### Edge AI
- W15 ASUS UGen300(Hailo-10H, 40 TOPS(Tera Operations Per Second), 2.5W), Nordic Axon NPU 15x 향상, TI $1 이하 AI MCU(Microcontroller Unit) 양산 후속 정착. 이번 주 추가 하드웨어 발표 없음.

### Speaker Diarization
- Voxtral Realtime sub-200ms, AssemblyAI Universal-3-Pro 30% 노이즈 개선 안정 유지. PyAnnote 3.1 10% DER(Diarization Error Rate) 달성. NVIDIA NeMo Sortformer 아키텍처 등장. 돌파구 수준 변화 없음.

### GPU Orchestration
- SkyPilot Agent Skills(GPU 접근·잡 관리), CoreWeave 통합, Shopify 프로덕션 채택 등 에코시스템 안정. Ray+SkyPilot 멀티클라우드 분산 컴퓨팅 조합 정착. 이번 주 추가 발표 없음.

### FeedbackOps (Meta-prompt Engineering)
- DSPy MIPROv2(Multi-stage Instruction PRoposal Optimizer) 옵티마이저 안정 운영 지속. 이번 주 신규 릴리스 없음.

### EvaluationOps (KMS 성능평가)
- RAGAS v0.2+ 에이전트 워크플로우 평가 확장 지속. LLM-as-judge 54개 모델 테스트 중 27개가 Tier 1 성능 달성. MemAlign(인간 피드백 기반 LLM 판사 보정) 논문 등장(2026-02). 이번 주 돌파구 없음.

### MLOps Pipeline
- LLMOps→AgentOps 전환 가속 지속. DevSecMLOps(보안 통합 파이프라인) 프레임워크 공식화 진행. ONEREACH AI "LLMOps for AI Agents" 가이드 발표. 구체적 신규 제품 출시 없음.

### Agentic Context Engineering
- Context Engineering이 독립 아키텍처 분야로 부상. Minimum Viable Context(MVC) — 에이전트에 현 단계 작업에 필요한 최소한의 정보만 제공하는 패턴이 핵심 원칙으로 확산. GitHub Agent-Skills-for-Context-Engineering 툴킷 생태계 성숙 지속.

### Adaptive RAG
- Agentic RAG(Retrieval-Augmented Generation) 패턴이 2026 표준으로 정착: Query → Plan → Tool Use → Reflect → Answer. GraphRAG+MCP 조합이 "USB-C for AI" 비유와 함께 데이터 아키텍처 주류로 부상. 프로덕션 LLM 앱 85%가 RAG 사용(2024년 30%에서 상승).

---

## 🟡🔴 Deep 심층 분석

### 5G SA/6G (AI-RAN/SRv6) — 🟡 주목

> 상세 리서치: [2026-04-07_research-5g-6g-ai-ran.md](2026-04-07_research-5g-6g-ai-ran.md)

#### 이전 대비 변화
- 전주: MWC 2026 후속 정착 단계. NVIDIA Aerial 오픈소스, P.I. Works-TELUS AI-RAN 자동화 파트너십(4/1)
- 금주: DOCOMO-SKT vRAN/AI-RAN 공동 백서(3/31) 발간, Samsung+Vodafone 유럽 최초 vRAN 콜, 3GPP Release 21 일정 가시화
- 변화 방향: **MWC 후속에서 백서·실증 기반 표준화 선점 국면으로 전환** — 통신사 주도의 AI-RAN 기술 요건 공식화가 시작됨

#### 기술 동향

1. **DOCOMO-SKT 공동 백서 발간(3/31) — 통신사 관점의 AI-RAN 3대 기술 요건 공식화.**
   NTT DOCOMO와 SKT가 "Requirements for Advancing vRAN and AI-RAN in Mobile Networks" 백서를 공동 발간했다. 양사의 실제 네트워크 구축·운영 경험을 바탕으로 3가지 핵심 기술 요건을 정의: (1) HW/SW 분리 — 소프트웨어 독립 배포, (2) 리소스 풀링 — 품질 유지하면서 용량 개선·전력 절감, (3) xPU(CPU·GPU 등 정보처리 유닛 총칭) 기반 AI 컴퓨팅 — 이동통신과 AI 서비스를 함께 제공하는 통합 플랫폼 진화. 양사는 2022년 11월 5G Evolution/6G 기술 연구 협력 이래 세 번째 공동 백서다 [[G-01]](#ref-g-01), [[E-01]](#ref-e-01).

2. **Samsung+Vodafone 유럽 최초 vRAN 상용 콜 — Intel Xeon 6 SoC 기반 단일 서버 2G/4G/5G 통합.**
   Samsung과 Vodafone이 Intel Xeon 6 SoC(System-on-Chip) 기반 vRAN으로 유럽 최초 콜을 완료했다. 2G·4G·5G를 단일 고성능 서버에서 동시 처리하며, Dell Technologies 서버 + Wind River Studio 클라우드 플랫폼과 협력 구현. 2026년 중 상용 배포 예정. 별도로 2026년 1월 미국 Tier 1 통신사에서 Intel Xeon 6700P-B(72코어) 기반 업계 최초 vRAN 상용 콜도 달성 [[G-02]](#ref-g-02), [[E-02]](#ref-e-02).

3. **Nokia-NVIDIA L1 RAN 전체 CUDA 플랫폼 설계 — GPU 기반 AI-RAN 아키텍처 확정.**
   Nokia는 MWC 2026에서 anyRAN 소프트웨어를 NVIDIA GPU 가속 AI-RAN 플랫폼에서 T-Mobile, IOH(Indosat Ooredoo Hutchison), SoftBank와 기능 테스트를 완료했다. L1(Layer 1) RAN 전체를 NVIDIA CUDA(Compute Unified Device Architecture) 플랫폼과 GPU에서 구동하는 설계를 확정. SoftBank는 AITRAS Orchestrator로 여유 AI-RAN 컴퓨팅 자원을 제3자 AI 태스크에 할당하는 수익화 모델을 제시 [[G-03]](#ref-g-03), [[E-03]](#ref-e-03).

4. **NVIDIA 12사 6G AI-native 연합 — 업계 최대 규모 공약.**
   NVIDIA가 BT Group, Cisco, Deutsche Telekom, Ericsson, Nokia, SKT, SoftBank, T-Mobile 등 11개 기관과 AI-native 개방형 6G 플랫폼 구축을 공약(2/28). AI-RAN Alliance 132개 회원사. T-Mobile은 5G 서비스와 생성형 AI 애플리케이션을 동시에 OTA(Over-the-Air) 실증 [[G-04]](#ref-g-04), [[E-04]](#ref-e-04).

5. **Ericsson ASIC 이기종 전략 vs Nokia CUDA 집중 — 벤더 전략 분기 심화.**
   Ericsson은 자체 Silicon(ASIC, Application-Specific Integrated Circuit)을 주축으로 NVIDIA·Intel·Qualcomm에 모두 연결되는 이기종 구조를 추구하며, T-Mobile과 Cloud RAN 소프트웨어의 NVIDIA AI 인프라 위 포터블 실증을 완료. "Cloud RAN 소프트웨어는 설계 자체가 포터블" 강조 [[G-06]](#ref-g-06). Nokia의 CUDA 집중 전략과 대조적 [[G-05]](#ref-g-05), [[E-05]](#ref-e-05), [[E-06]](#ref-e-06).

6. **3GPP Release 21 일정 — 6G 표준화 공식 출발선 2026년 6월 가시화.**
   3GPP는 Release 21(최초 6G 스펙) 작업 기간을 2026년 6월까지 확정 예정. ASN.1 동결 2029년 3월 전망 [추정]. Ericsson은 6G 스펙 2028년 말 완성, 2030년 첫 상용 시스템 출시를 전망. Qualcomm은 프리커머셜 2028년(LA 올림픽), 상용화 2029년 목표 제시 [[G-07]](#ref-g-07), [[G-10]](#ref-g-10).

7. **Qualcomm Agentic RAN Management Service 출시 — AI 에이전트 기반 자율 네트워크 경로.**
   Qualcomm이 Dragonwing RAN Automation Suite 내 Agentic RAN Management Service를 출시(MWC 2026). RAN AI 에이전트들이 협력하여 네트워크 상태를 모니터링하고 자율적으로 변경을 실행하는 6G급 자율 네트워크 목표. X105 5G 모뎀(세계 최초 Release 19 지원) 샘플링 시작 [[G-10]](#ref-g-10), [[E-07]](#ref-e-07).

8. **SRv6(Segment Routing over IPv6) 글로벌 확산 — 5G/6G 백홀 기본 프로토콜로 부상.**
   SoftBank-Arrcus SRv6 MUP(Mobile User Plane) 세계 최초 상용 도입. Jio는 SRv6를 AI 워크로드와 5G/6G 서비스 최적화에 활용. 트래픽 분리, 네트워크 슬라이싱, 50ms 미만 경로 복원 지원 [[G-11]](#ref-g-11).

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| NTT DOCOMO | SKT와 vRAN/AI-RAN 백서 공동 발간(3/31). 3대 기술 요건 공식화 | [[G-01]](#ref-g-01), [[E-01]](#ref-e-01) |
| SK Telecom | DOCOMO 백서 공동 발간. Ericsson 5년 MoU(3/18). AI-RAN Alliance 이사회 합류. NVIDIA 6G 연합 참여 | [[G-01]](#ref-g-01), [[E-08]](#ref-e-08) |
| Samsung | Intel Xeon 6 SoC vRAN으로 Vodafone 유럽 최초 콜. 미국 Tier 1 Xeon 6700P-B 업계 최초 콜(1월). NVIDIA AI-native 네트워크 협력 | [[G-02]](#ref-g-02), [[E-02]](#ref-e-02) |
| Nokia | L1 RAN 전체 CUDA 설계 확정. T-Mobile·IOH·SoftBank AI-RAN 테스트 완료. Red Hat AI Enterprise 통합. Doksuri 무선 신제품 | [[G-03]](#ref-g-03), [[E-03]](#ref-e-03) |
| Ericsson | T-Mobile 포터블 AI-RAN 실증. ASIC 이기종 전략. Intel·Qualcomm·MediaTek 파트너십. SKT 5년 MoU | [[E-05]](#ref-e-05), [[E-06]](#ref-e-06) |
| NVIDIA | 12사 6G AI-native 연합(2/28). Aerial Apache 2.0 오픈소스. AI-RAN Alliance 130+ 회원사 | [[G-04]](#ref-g-04), [[E-04]](#ref-e-04) |
| Qualcomm | Agentic RAN Management Service 출시. AI-RAN Alliance 이사회. X105 5G 모뎀(R19) 샘플링. 6G 3축 비전 | [[G-10]](#ref-g-10), [[E-07]](#ref-e-07) |
| Intel | AI-RAN Alliance 불참 유지. Samsung·Vodafone vRAN용 Xeon 6 SoC 공급. Ericsson AI-native 6G 협력 | [[G-09]](#ref-g-09) |

#### 시장 시그널

**투자 & M&A**
- AI-RAN 글로벌 시장 2025년 29.6억 달러 → 2035년 371.9억 달러(CAGR(Compound Annual Growth Rate) 28.79%) [[G-13]](#ref-g-13) [추가확인 필요]
- Open RAN 시장 2025년 65.3억 달러 → 2033년 450.9억 달러(CAGR 26.8%) [[G-14]](#ref-g-14) [추가확인 필요]
- AT&T-Ericsson Open RAN 5년 계약(최대 140억 달러) — 단일 오퍼레이터 역대 최대 [[G-14]](#ref-g-14)

**파트너십 & 제휴**
- DOCOMO-SKT vRAN/AI-RAN 공동 백서(3/31) — 2022년 협력 이래 세 번째 백서 [[G-01]](#ref-g-01)
- SKT-Ericsson 5년 MoU(3/18): AI-powered RAN, 5G 수익화, 오픈·자율 네트워크, Zero Trust, 6G 표준화 5개 영역 [[E-08]](#ref-e-08)
- NVIDIA-Marvell NVLink Fusion AI-RAN 인프라 파트너십 [[G-09]](#ref-g-09)
- QCT(Quanta Cloud Technology) Nokia anyRAN·NVIDIA ARC-Pro 지원 AI-RAN 서버 발표 [[G-15]](#ref-g-15)

**시장 전망**
- Omdia 2026 Open RAN 조사: 전략적 적극 배포 13% + 미래 진화 가이드 27% = 의미 있는 채택 40% [[G-08]](#ref-g-08)
- 아시아·태평양 AI-RAN 최고속 성장(CAGR 25.5%, 2026-2035), 북미 37% 점유 [[G-13]](#ref-g-13)
- 상용 6G 서비스 2030년 전후 예상. Qualcomm 프리커머셜 2028년(LA 올림픽) 목표 [[G-10]](#ref-g-10)

**도입 사례**
- Deutsche Telekom: 독일 3,000+ 사이트 Open RAN 배포 완료(Huawei→Nokia+Fujitsu 교체) [[G-14]](#ref-g-14)
- Bharti Airtel: Mavenir과 인도 농촌 2,500개 Open RAN(10,000개 확장 옵션) [[G-14]](#ref-g-14)
- SoftBank: Arrcus SRv6 MUP 세계 최초 상용 도입 [[G-11]](#ref-g-11), [[G-12]](#ref-g-12)

**연구 동향**
- IEEE INFOCOM 2026 "6G AI-RAN 2026" 워크숍: AI-native 분산 인텔리전스, 학습 기반 아키텍처, 스펙트럼 할당 [[G-16]](#ref-g-16)
- Frontiers "AI-native 6G 종합 리뷰": 시맨틱 통신, RIS(Reconfigurable Intelligent Surface), 엣지 인텔리전스 통합 [[P-01]](#ref-p-01)
- Nature Communications 광대역 실시간 스펙트럼 감지 6G 논문(2026) [[P-02]](#ref-p-02)

#### 시장 수요 (voice-of-market)

**고객 페인포인트**
- 다중 AI 유스케이스 확장성 부재 — 레거시 SON(Self-Organizing Network) 기반 자동화가 다수 AI 앱 동시 운영에서 확장 불가. "It is not really scalable with multiple AI use case" — O-RAN Alliance Summit MWC 2026 (Changsoon Choi, Deutsche Telekom)
- O-RAN 전체 가시성(Observability) 확보 불가 — O-Cloud·AI-RAN 레이어 간 통합 가시성 부재로 이상 탐지·원인 분석이 수동 처리 — O-RAN Alliance Summit (Deutsche Telekom)
- 5G SA 전환율 저조 — 253개 5G 네트워크 중 77개만 SA(Standalone) 출시. ROI(Return on Investment) 경로 불명확 — Opensignal 2025 리포트

**도입 장벽**
- 표준화 속도가 기술 발전 속도를 따라가지 못함 — O-RAN 스펙 합의에 수개월, AI 모델 출시는 3-4주 주기. "We cannot allow ourselves to spend weeks, months and years on agreeing on a specification" — O-RAN Alliance Summit (AT&T 대표)
- 동시 과제 과부하 — 스펙트럼 배포, 클라우드 전환, AI 네이티브화를 병렬 요구받는 상황 — O-RAN Alliance Summit (AT&T 대표)
- AI+RAN GPU 공유 TCO(Total Cost of Ownership) 미성숙 — 대규모 GPU 도입 CAPEX(Capital Expenditure)/OPEX(Operational Expenditure) 부담으로 오퍼레이터 신중 검토 중 — NVIDIA Blog

**시장 니즈**
- 동적 네트워크 슬라이싱을 위한 RAN 도메인 오케스트레이션 SMO(Service Management and Orchestration) 통합 — Deutsche Telekom 구체적 비즈니스 수요 접수
- Large Telco Model(LTM) — 네트워크 로그·카운터·아키텍처를 이해하는 텔코 특화 파운데이션 모델 수요 — NVIDIA (Kanika Atri)
- SRv6 기반 경험 기반 수익화(Experience-Based Monetization) — 남아프리카 사례 ARPU(Average Revenue Per User) $18→$25 상승 — Huawei MWC 2026

#### 전략적 시사점

**기회**
- SKT가 DOCOMO와 AI-RAN 기술 요건 백서를 통해 표준화 의제를 선점. Ericsson 5년 MoU와 결합하면 국내 6G 상용화 공급망 주도적 위치 확보 가능
- AI-RAN을 "이동통신 + AI 컴퓨팅 통합 플랫폼"으로 포지셔닝하면 기지국 인프라가 엣지 AI 서비스 플랫폼으로 확장 — SoftBank AITRAS 수익화 모델이 레퍼런스
- SRv6 기반 백홀 구축은 네트워크 슬라이싱·5G SA 서비스 차별화 기반. SoftBank·Jio 선행 사례 벤치마킹 가능

**위협**
- NVIDIA GPU 중심 AI-RAN 생태계 고착화 시 ASIC/CPU 진영의 벤더 다양성 제한 및 비용 경쟁력 약화 우려
- Intel AI-RAN Alliance 불참은 Xeon 기반 vRAN(Samsung 검증)과 GPU 기반 AI-RAN(NVIDIA 진영) 간 표준 충돌 가능성
- Ericsson-Nokia AI-RAN 전략 분기(ASIC 이기종 vs CUDA 집중)가 통신사 벤더 선택 불확실성 증가 요인

---

## 경쟁사 동향 (SKT / KT)

> 이번 주 해당 도메인과 관련된 SKT·KT의 주요 움직임.

### SKT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| DOCOMO-SKT AI-RAN 백서 | vRAN/AI-RAN 3대 기술 요건 공동 정의(3/31). HW/SW 분리, 리소스 풀링, xPU AI 컴퓨팅 | 5g-6g-ai-ran | [[G-01]](#ref-g-01), [[E-01]](#ref-e-01) |
| Ericsson 5년 MoU | AI-powered RAN, 5G 수익화, 자율 네트워크, Zero Trust, 6G 표준화 5개 영역(3/18) | 5g-6g-ai-ran | [[E-08]](#ref-e-08) |
| AI-RAN Alliance 이사회 | Qualcomm·Vodafone과 함께 신규 이사회 멤버 합류 | 5g-6g-ai-ran | [[G-08]](#ref-g-08) |
| 1인 1 AI 에이전트 전략 | 전사 AX(AI Transformation) 혁신 가속. 에이닷 비즈·폴라리스·플레이그라운드 플랫폼 제공. AXMS 정식 가동 | agent-orchestration | [[E-09]](#ref-e-09) |

### KT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| 에이전트 빌더 공개 | MWC26에서 노코드 AI 에이전트 제작 플랫폼 공개(3/4). 드래그앤드롭 방식, 업무 템플릿·대화 모듈 조합 | agent-orchestration | [[E-10]](#ref-e-10) |
| 회의록 자동화 에이전트 | 화자 분리 → 핵심 안건 정리 → 공문 초안 → 결재 자동처리 시연 | speaker-diarization | [[E-10]](#ref-e-10) |

### 시사점
- SKT는 DOCOMO 백서와 Ericsson MoU를 통해 5G/6G 인프라 전환의 국제 협력 축을 강화하며 표준화 의제 선점에 나섰다. 동시에 "1인 1 AI 에이전트" 전략으로 내부 AX를 가속화하고 있어, 인프라(5G/6G)와 서비스(AI 에이전트) 양면에서 동시 진행 중
- KT는 MWC에서 노코드 에이전트 빌더를 공개하며 B2B AI 에이전트 시장 진입을 본격화. 회의록 자동화 시연은 화자분할+LLM 연계의 실용적 유스케이스

---

## 규제 & 거버넌스

> 해당 도메인에 영향을 미치는 국내외 규제·표준·가이드라인 동향.

### 시행 임박 / 카운트다운

| 규제 | 시행일 | D-day |
|------|--------|-------|
| EU AI Act 전면 시행 (고위험 AI 분류·적합성 평가) | 2026-08-02 | D-117 |
| EU AI Act Article 50 (합성 콘텐츠 투명성) | 2026-08-02 | D-117 |
| EU AI Regulatory Sandbox 회원국 설치 의무 | 2026-08-02 | D-117 |
| 한국 AI 기본법 (인공지능 발전과 신뢰 기반 조성 등에 관한 기본법) | 2026-01-22 | 시행 중 |

### 신규 발의 & 가이드라인
- EU 집행위원회 "간소화(Simplification)" 제안(2025-11): AI Act 및 GDPR(General Data Protection Regulation) 주요 법률 변경안 공개. AI Act 전면 시행 일정 지연 가능성 제기 [[G-20]](#ref-g-20). 에이전트 관련 적용 범위·책임 소재 논의 진행 중 [[G-19]](#ref-g-19)
- 한국 AI 기본법 시행령 입법예고 [[G-21]](#ref-g-21): 고영향 AI 분류 기준, 범용 에이전트의 규제 범위를 두고 정부·업계·시민단체 해석 상충 지속. "과도한 컴플라이언스 비용이 사다리 걷어차기가 될 수 있다"는 스타트업계 우려
- Microsoft Agent Governance Toolkit 오픈소스(4/2, MIT 라이선스) — OWASP(Open Worldwide Application Security Project) Agentic AI 10대 리스크 전체를 커버하는 최초 툴킷 [[G-18]](#ref-g-18)

### 시사점
- EU AI Act 전면 시행(D-117)까지 4개월 미만. 고위험 AI 분류에 네트워크 자율 운영(AI-RAN 에이전트) 포함 여부가 통신사 AI 배포 전략에 영향
- 한국 AI 기본법 시행령에서 범용 에이전트의 고영향 AI 분류 결정이 에이전트 서비스 출시 일정에 직접 영향

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **인프라-서비스 양면 전환 가속**: SKT의 DOCOMO 백서(인프라)와 1인 1 에이전트(서비스), KT의 에이전트 빌더(서비스)는 통신사들이 AI-RAN 인프라와 AI 에이전트 서비스를 동시에 추진하고 있음을 보여준다. 우리도 두 축의 연계(에이전트가 AI-RAN 자원을 활용하는 구조)를 선제적으로 설계해야 함

2. **GA 정착 후 보안·거버넌스가 다음 경쟁 축**: W15의 대규모 GA 출시 이후 이번 주는 보안(88% 조직 사고 보고)과 거버넌스(Microsoft Governance Toolkit, EU AI Act)가 부각. 에이전트 배포의 양적 확장에서 질적 관리 국면으로 전환 중

3. **벤더 선택의 불확실성 증가**: Ericsson ASIC 이기종 vs Nokia CUDA 집중, Intel AI-RAN Alliance 불참 등 생태계 분열이 심화. 통신사로서 벤더 lock-in 리스크 관리와 멀티벤더 전략 수립이 시급

### 후속 조치 제안

- 🟡 5G/6G AI-RAN: DOCOMO-SKT 백서와 Ericsson MoU 내용을 우리 네트워크 전략에 반영할 포인트 검토 필요
  → `/wtis standard Hybrid AI Infra` — 5G/6G 기술 영역 Go/No-Go 검증
- 📂 Obsidian 동기화:
  → `/obsidian-bridge` — 메인 리포트 + Deep 리서치 동기화
- 📅 다른 도메인 모니터링:
  → `/weekly-monitor voice-ai` — 화요일 Voice AI 모니터링
  → `/weekly-monitor secure-ai` — 수요일 Secure AI 모니터링

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | NTT DOCOMO — DOCOMO and SK Telecom Publish White Paper on Requirements for Advancing vRAN and AI-RAN | [링크](https://www.docomo.ne.jp/english/info/media_center/pr/2026/0331_00.html) | press-release | 2026-03-31 | [A] |
| <a id="ref-g-02"></a>G-02 | Samsung Global Newsroom — Samsung and Vodafone Drive the Future of AI-Native Networks Across Europe | [링크](https://news.samsung.com/global/samsung-and-vodafone-drive-the-future-of-ai-native-networks-across-europe-with-successful-validation-of-a-new-chipset) | press-release | 2026-03 | [A] |
| <a id="ref-g-03"></a>G-03 | Nokia Newsroom — Nokia accelerates AI-RAN momentum with new partnerships driving path to AI-Native 6G | [링크](https://www.nokia.com/newsroom/nokia-accelerates-ai-ran-momentum-with-new-partnerships-driving-path-to-ai-native-6g-mwc26/) | press-release | 2026-03-01 | [A] |
| <a id="ref-g-04"></a>G-04 | NVIDIA Newsroom — NVIDIA and Global Telecom Leaders Commit to Build 6G on Open and Secure AI-Native Platforms | [링크](https://nvidianews.nvidia.com/news/nvidia-and-global-telecom-leaders-commit-to-build-6g-on-open-and-secure-ai-native-platforms) | press-release | 2026-02-28 | [A] |
| <a id="ref-g-05"></a>G-05 | Light Reading — Ericsson and Nokia are diverging like never before on AI-RAN | [링크](https://www.lightreading.com/5g/ericsson-and-nokia-are-diverging-like-never-before-on-ai-ran) | news | 2026-03 | [B] |
| <a id="ref-g-06"></a>G-06 | T-Mobile — T-Mobile and Ericsson Advance Portable AI RAN Software On NVIDIA AI Infrastructure | [링크](https://www.t-mobile.com/news/network/t-mobile-and-ericsson-advance-portable-ai-ran-software-on-nvidia-ai-infrastructure) | press-release | 2026-03 | [A] |
| <a id="ref-g-07"></a>G-07 | Ericsson — 6G standardization timeline and technology principles | [링크](https://www.ericsson.com/en/blog/2024/3/6g-standardization-timeline-and-technology-principles) | blog | 2024-03 | [B] |
| <a id="ref-g-08"></a>G-08 | AI-RAN Alliance — MWC 2026 Momentum Press Release | [링크](https://ai-ran.org/press-releases/mwc-2026-momentum) | press-release | 2026-02-26 | [A] |
| <a id="ref-g-09"></a>G-09 | Fierce Network — MWC 2026: Intel sits out AI-RAN Alliance, for now | [링크](https://www.fierce-network.com/wireless/mwc-2026-intel-sits-out-ai-ran-alliance-now) | news | 2026-03 | [B] |
| <a id="ref-g-10"></a>G-10 | Qualcomm — Qualcomm Launches Agentic RAN Management Service | [링크](https://www.qualcomm.com/news/releases/2026/03/qualcomm-launches-agentic-ran-management-service-and-ai-enhancem) | press-release | 2026-03-01 | [A] |
| <a id="ref-g-11"></a>G-11 | Light Reading — SKT and NTT Docomo define the path to vRAN and AI-RAN | [링크](https://www.lightreading.com/virtualization/skt-and-ntt-docomo-define-the-path-to-vran-and-ai-ran) | news | 2026-04-02 | [B] |
| <a id="ref-g-12"></a>G-12 | SoftBank — SRv6 MUP Commercial Deployment | [링크](https://www.softbank.jp/en/corp/news/press/sbkk/2025/20251218_01/) | press-release | 2025-12 | [A] |
| <a id="ref-g-13"></a>G-13 | Precedence Research — AI-RAN Market Size to Hit USD 37.19 Billion by 2035 | [링크](https://www.precedenceresearch.com/ai-ran-market) | market-report | 2026 | [C] |
| <a id="ref-g-14"></a>G-14 | 5G World Pro — The Real 5G Open RAN Numbers in 2026 | [링크](https://5gworldpro.com/blog/2026/03/10/the-real-5g-open-ran-numbers-in-2026) | blog | 2026-03-10 | [C] |
| <a id="ref-g-15"></a>G-15 | National Law Review — QCT Unveils QuantaEdge EGN77C-2U AI-RAN Server | [링크](https://natlawreview.com/press-releases/qct-unveils-quantaedge-egn77c-2u-new-ai-ran-server-supporting-nokia-anyran) | press-release | 2026-03 | [A] |
| <a id="ref-g-16"></a>G-16 | IEEE INFOCOM 2026 — 6G AI-RAN 2026 Workshop | [링크](https://infocom2026.ieee-infocom.org/first-workshop-ai-native-distributed-intelligence-6g-networks-6g-ai-ran-2026-call-papers) | conference | 2026 | [A] |

| <a id="ref-g-21"></a>G-21 | 한국 AI 기본법 (법령 전문) | [링크](https://www.law.go.kr/lsInfoP.do?lsiSeq=268543) | regulation | 2026-01-22 | [A] |
| <a id="ref-g-18"></a>G-18 | Belitsoft — 2026 AI Agent Trends: Enterprises Run 12 AI Agents on Average | [링크](https://markets.financialcontent.com/stocks/article/abnewswire-2026-4-6-belitsoft-report-2026-ai-agent-trends-enterprises-run-12-ai-agents-on-average-but-half-work-alone) | report | 2026-04-06 | [B] |
| <a id="ref-g-19"></a>G-19 | EU AI Act — How AI Agents Are Governed Under the EU AI Act | [링크](https://thefuturesociety.org/aiagentsintheeu/) | analysis | 2026 | [B] |
| <a id="ref-g-20"></a>G-20 | Amnesty International — EU proposals to simplify tech laws roll back our rights | [링크](https://www.amnesty.org/en/latest/news/2026/04/eu-simplification-laws/) | news | 2026-04 | [B] |
| <a id="ref-e-01"></a>E-01 | SK Telecom — Yu Takki 발언 (DOCOMO-SKT 백서 공동 발간) | [링크](https://en.acnnewswire.com/press-release/english/106047/docomo-and-sk-telecom-publish-white-paper-on-requirements-for-advancing-vran-and-ai-ran-in-mobile-networks) | press-release | 2026-03-31 | [A] |
| <a id="ref-e-02"></a>E-02 | Samsung Business — Samsung and Vodafone vRAN Validation | [링크](https://www.samsung.com/global/business/networks/insights/press-release/0303-samsung-and-vodafone-drive-the-future-of-ai-native-networks-across-europe-with-successful-validation-of-a-new-chipset/) | press-release | 2026-03-03 | [A] |
| <a id="ref-e-03"></a>E-03 | Nokia — NVIDIA and Nokia to Pioneer the AI Platform for 6G | [링크](https://www.nokia.com/newsroom/nvidia-and-nokia-to-pioneer-the-ai-platform-for-6g--powering-americas-return-to-telecommunications-leadership/) | press-release | 2026-02-28 | [A] |
| <a id="ref-e-04"></a>E-04 | NVIDIA IR — NVIDIA and Global Telecom Leaders 6G Commitment | [링크](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Global-Telecom-Leaders-Commit-to-Build-6G-on-Open-and-Secure-AI-Native-Platforms/default.aspx) | IR | 2026-02-28 | [A] |
| <a id="ref-e-05"></a>E-05 | Ericsson — Ericsson leads the 6G journey toward an intelligent fabric at MWC 2026 | [링크](https://www.ericsson.com/en/press-releases/2026/3/ericsson-leads-the-6g-journey-toward-an-intelligent-fabric-at-mwc-2026) | press-release | 2026-03 | [A] |
| <a id="ref-e-06"></a>E-06 | Ericsson — Ericsson and T-Mobile test portable AI RAN on NVIDIA platform | [링크](https://www.ericsson.com/en/news/2026/3/ericsson-t-mobile-boost-portable-ai-ran-on-nvidia-platform) | press-release | 2026-03 | [A] |
| <a id="ref-e-07"></a>E-07 | Qualcomm — Qualcomm 6G device-to-data-center transformation | [링크](https://www.qualcomm.com/news/onq/2026/03/qualcomm-6g-device-to-data-center-transformation) | blog | 2026-03 | [A] |
| <a id="ref-e-08"></a>E-08 | Ericsson Korea — SKT-Ericsson AI-RAN 및 6G 기술혁신 MoU | [링크](https://www.ericsson.com/ko/news/2/2026/skt-6g-mou) | press-release | 2026-03-18 | [A] |
| <a id="ref-e-09"></a>E-09 | SK텔레콤 뉴스룸 — 1인 1 AI 에이전트 시대로 전환 | [링크](https://news.sktelecom.com/222847) | press-release | 2026-03-16 | [A] |
| <a id="ref-e-10"></a>E-10 | KT — MWC26 에이전트 빌더 공개 | [링크](https://www.mt.co.kr/tech/2026/03/04/2026030408131578528) | news | 2026-03-04 | [A] |
| <a id="ref-p-01"></a>P-01 | Frontiers — A comprehensive review of AI-native 6G | [링크](https://www.frontiersin.org/journals/communications-and-networks/articles/10.3389/frcmn.2025.1655410/full) | paper | 2025 | [A] |
| <a id="ref-p-02"></a>P-02 | Nature Communications — Integrated photonic ultrawideband real-time spectrum sensing for 6G | [링크](https://www.nature.com/articles/s41467-026-70389-0) | paper | 2026 | [A] |
