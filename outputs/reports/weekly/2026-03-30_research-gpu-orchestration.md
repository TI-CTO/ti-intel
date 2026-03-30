---
type: deep-research
parent: weekly-monitor
domain: agentic-ai
l3: gpu-orchestration
date: 2026-03-30
---

# Deep Research: 하이브리드 GPU Orchestration (W15)

## 이전 대비 변화 (W14 → W15)

- **W14 핵심**: NVIDIA Dynamo 1.0 GA(3/16), Vera Rubin + Groq 3 LPX 발표(GTC 2026), 추론 OS 포지셔닝
- **W15 핵심**: KubeCon Europe 2026(3/24) — GPU 오케스트레이션의 **오픈소스·커뮤니티 이관** 대규모 단행. DRA Driver CNCF 기부, Grove API 공개, KAI Scheduler CNCF Sandbox, llm-d CNCF 합류, Microsoft AI Runway 출시
- **변화 방향**: NVIDIA의 전략이 "자사 플랫폼 잠금(lock-in)"에서 "오픈 에코시스템 주도(open ecosystem stewardship)"로 전환. Kubernetes가 AI 인프라 OS로서의 지위 공식화

---

## 기술 동향

1. **NVIDIA DRA Driver CNCF 기부 — GPU 리소스 할당의 커뮤니티 표준화.**
   NVIDIA가 Dynamic Resource Allocation (DRA) Driver for GPUs를 CNCF에 기부, 벤더 단독 거버넌스에서 Kubernetes 프로젝트 산하 커뮤니티 소유로 이전. DRA Driver는 Kubernetes와 GPU 하드웨어 사이에서 컨테이너 워크로드에 컴퓨트 리소스를 할당하는 "교통 통제자" 역할. AWS, Broadcom, Canonical, Google Cloud, Microsoft, Nutanix, Red Hat, SUSE 8개 파트너가 공동 협력. CNCF CTO Chris Aniszczyk는 "GPU 오케스트레이션이 오픈 클라우드 네이티브 환경에서 표준화되는 주요 이정표"라고 평가. [[G-01]](#ref-g-01)

2. **NVIDIA Grove API 공개 — 복잡한 추론 시스템의 단일 선언형 표현.**
   NVIDIA Dynamo 생태계의 모듈형 컴포넌트로, GPU 클러스터에서 AI 워크로드를 오케스트레이션하는 오픈소스 Kubernetes API. 개발자가 특정 역할, 의존성, 다단계 스케일링 규칙, 시작 순서 등 복잡한 추론 시스템 전체를 단일 Custom Resource (CR)로 표현 가능. llm-d 추론 스택과 통합되어 더 넓은 Kubernetes 커뮤니티 채택 목표. Dynamo 독립 실행 또는 외부 고성능 추론 프레임워크와 연동도 지원. [[G-02]](#ref-g-02)

3. **KAI Scheduler CNCF Sandbox 수락 — AI 워크로드 스케줄링의 오픈 거버넌스 진입.**
   NVIDIA의 고성능 AI 워크로드 스케줄러인 KAI Scheduler가 CNCF Sandbox 프로젝트로 공식 수락. Gang-scheduling, 계층적 큐(hierarchical queues), 플러그인 기반 확장을 지원하며 GPU Operator 및 DRA Driver 위에서 고급 리소스 조율 기능 제공. Kubernetes의 선언적·동적 확장 모델을 유지하면서 AI 워크로드 특화 스케줄링 계층을 추가. NVIDIA 단독 관리에서 커뮤니티 공동 개발로 전환. [[G-03]](#ref-g-03)

4. **GPU Kata Containers 보안 확장 — GPU 가속 기밀 컴퓨팅.**
   NVIDIA가 CNCF Confidential Containers 커뮤니티와 협력하여 Kata Containers에 GPU 지원을 도입. 경량 가상머신(VM) 기반 격리를 GPU 가속 워크로드로 확장하여 하드웨어 수준의 워크로드 격리 + GPU 가속을 동시 구현. AI 추론의 데이터 보안 및 규정 준수 요구 강화 추세에 대응. [[G-04]](#ref-g-04)

5. **llm-d CNCF Sandbox 합류 — 분산 LLM 추론의 클라우드 네이티브 표준화.**
   2025년 5월 출범한 llm-d(Distributed LLM inference framework)가 CNCF Sandbox 프로젝트로 수락(3/24). Red Hat, Google Cloud, IBM Research, CoreWeave, NVIDIA가 공동 창립, AMD, Cisco, Hugging Face, Intel, Lambda, Mistral AI 지원. UC Berkeley·University of Chicago 학술 파트너십. Kubernetes Gateway API Inference Extension 구현, LeaderWorkerSet 기반 멀티노드 복제본, Prefill/Decode 분리(disaggregation), 계층형 KV 캐시 오프로딩(GPU→TPU→CPU→스토리지) 핵심 기능. [[G-05]](#ref-g-05)

6. **Microsoft AI Runway 출시 — Kubernetes 추론 워크로드 통합 관리 API.**
   Microsoft가 KubeCon에서 오픈소스 AI Runway 프로젝트 공개. Kubernetes 추론 워크로드를 위한 공통 API로 플랫폼 팀이 모델 배포와 서빙 기술 전환을 중앙에서 관리. HuggingFace 모델 검색, GPU 메모리 적합도 표시, 실시간 비용 추정, Kubernetes 비전문가 대상 웹 UI 제공. NVIDIA Dynamo, KubeRay, llm-d, KAITO 런타임 지원. Microsoft는 "Kubernetes가 단순 클라우드 네이티브 앱 컨트롤 플레인을 넘어 AI 인프라의 운영 OS"라고 선언. [[G-06]](#ref-g-06)

7. **DRA General Availability (Kubernetes 1.36) — 엔터프라이즈급 GPU 리소스 관리 성숙.**
   Dynamic Resource Allocation이 Kubernetes 1.36에서 일반 공개(GA) 달성. Workload Aware Scheduling이 DRA 지원을 Workload API에 추가, KubeRay 통합으로 분산 훈련·추론 클러스터에서 고성능 하드웨어 요청·관리 단순화. DRANet이 Azure RDMA NIC 업스트림 호환성을 포함하여 GPU-NIC 토폴로지 정렬이 성능에 직결되는 고성능 하드웨어로 네트워크 리소스 관리 확장. [[G-07]](#ref-g-07)

8. **Dynamo 1.0 + GKE Inference Gateway — 멀티클라우드 추론 오케스트레이션 심화.**
   W14에 GA된 Dynamo 1.0이 GKE Inference Gateway와 통합, 애플리케이션 레이어부터 하드웨어까지 아우르는 모듈형 오픈소스 컨트롤 플레인 구성. KV-aware 라우터 플러그인이 Inference Gateway의 엔드포인트 피커에 통합되어 Dynamo 서버 추론 풀 전체에 지능형 요청 라우팅. Blackwell GPU에서 최대 7x 처리량 향상, 멀티모달 워크로드 TTFT 30% 가속. [[G-08]](#ref-g-08)

9. **SkyPilot Shopify 사례 — 멀티클라우드 GPU 추상화 실제 적용.**
   Shopify가 SkyPilot 기반 멀티클라우드 GPU 워크플로우 사례를 공개. 단일 YAML 파일로 복수 클라우드에서 AI 훈련 잡 런칭, 팀별 `ml.shopify.io/quota-group` 레이블로 Kueue 큐 매핑 및 공정 분배 스케줄링 구현. `showback_cost_owner_ref` 레이블로 GPU 비용 팀 단위 추적. "클라우드 추가 시 사용자 YAML 변경 불필요"라는 추상화 목표 달성. [[G-09]](#ref-g-09)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| NVIDIA | KubeCon에서 DRA Driver CNCF 기부, Grove API 공개, KAI Scheduler CNCF Sandbox 수락, GPU Kata Containers 도입. W14 Dynamo 1.0 + Vera Rubin의 오픈 에코시스템 확장 전략 본격화. AWS·Broadcom·Canonical·Google·Microsoft·Nutanix·Red Hat·SUSE 8개사 협력 | [[G-01]](#ref-g-01), [[G-02]](#ref-g-02), [[G-03]](#ref-g-03) |
| Microsoft | DRA GA 달성, AI Runway 오픈소스 공개, AKS GPU 텔레메트리(Prometheus/Grafana 통합), DRANet RDMA NIC 업스트림 지원, "Kubernetes = AI 인프라 OS" 전략 선언 | [[G-06]](#ref-g-06), [[G-07]](#ref-g-07) |
| Google Cloud | GKE Inference Gateway + Dynamo 1.0 통합 심화, llm-d 공동 창립 기여, Scaling MoE 추론 on A4X 블로그 발행(3/24) | [[G-08]](#ref-g-08), [[G-05]](#ref-g-05) |
| Red Hat / IBM | llm-d + CNCF 공동 창립(Red Hat·IBM Research), CNCF에 "Kubernetes를 SOTA AI 인프라로 진화"하는 청사진 기부 | [[G-05]](#ref-g-05) |
| CoreWeave | llm-d 공동 창립 참여, Nscale $2B 경쟁 구도 속 $14.2B Meta 계약 유지. SkyPilot 멀티클라우드 오케스트레이션 백엔드 지원 지속 | [[G-10]](#ref-g-10), [[G-11]](#ref-g-11) |
| Anyscale (Ray) | KubeRay Workload API DRA 지원 통합(Microsoft 기여). Ray 클러스터 DRA 기반 GPU 요청·관리 단순화 | [[G-07]](#ref-g-07) |
| Shopify | SkyPilot 기반 멀티클라우드 GPU 플랫폼 구축 사례 공개 — Kueue 공정 분배, 팀 단위 비용 추적, 단일 YAML 추상화 달성 | [[G-09]](#ref-g-09) |
| Nscale | 유럽 최대 시리즈 C 펀딩 $2B(3월 초) 달성, 밸류에이션 $14.6B. NVIDIA·Citadel·Dell·Jane Street 투자 유치. 데이터센터 → 컴퓨트 → 오케스트레이션 수직 통합 | [[G-10]](#ref-g-10) |

---

## 시장 시그널

**투자 & M&A**
- Nscale이 $2B 시리즈 C 조달(밸류에이션 $14.6B). 유럽 최대 테크 펀딩 라운드 기록. NVIDIA, Citadel, Dell, Jane Street 참여. AI 데이터센터~오케스트레이션 수직 통합 모델 [[G-10]](#ref-g-10) [추가확인 필요]
- Nexthop AI $500M 시리즈 B(Lightspeed·a16z). AI 최적화 네트워킹 인프라 — GPU 클러스터 연결 레이어가 독립 투자 카테고리로 부상 [[G-10]](#ref-g-10) [추가확인 필요]
- NVIDIA의 $20B Groq 인수(2025 년말) 성과: GTC 2026에서 Groq 3 LPX 발표. Vera Rubin 플랫폼 내 저지연 추론 특화 이종 아키텍처로 편입 [[G-12]](#ref-g-12)

**파트너십 & 제휴**
- NVIDIA + AWS·Broadcom·Canonical·Google·Microsoft·Nutanix·Red Hat·SUSE: DRA Driver CNCF 기부 공동 협력. 업계 최초 GPU 오케스트레이션 벤더 중립 표준 협약 [[G-01]](#ref-g-01)
- IBM + Red Hat + Google + CoreWeave + NVIDIA: llm-d CNCF 공동 창립. 분산 LLM 추론 프레임워크의 오픈 표준화 추진 [[G-05]](#ref-g-05)
- Pure Storage + NVIDIA Dynamo: Pure KVA(KV 캐시 가속)가 Dynamo와 통합. 스토리지 레이어에서 추론 지연시간 단축 [[G-13]](#ref-g-13)

**시장 전망**
- GPU as a Service 시장: 2026년 $7.34B~$7.61B 추정, 전년 대비 27~29% 성장 (복수 리서치사 추정치 [[G-14]](#ref-g-14)) [추가확인 필요]
- 하이브리드 클라우드 오케스트레이션 시장: 2026년 $26.81B 추정, 2030년 $50.3B 전망(CAGR 17%). 하이브리드·멀티클라우드 세그먼트 29.44% CAGR로 최고 성장률 기록 [[G-15]](#ref-g-15) [추가확인 필요]
- AWS: 2026년부터 1백만+ NVIDIA GPU 배포 계획(Blackwell + Rubin 아키텍처) 발표 [[G-11]](#ref-g-11)

**도입 사례**
- Shopify: SkyPilot 기반 멀티클라우드 GPU 플랫폼 — 훈련 잡 런칭 소요시간 일 단위 → 분 단위로 단축, 팀별 GPU 비용 추적 자동화 [[G-09]](#ref-g-09)
- Dynamo 1.0 프로덕션 도입: AstraZeneca, Baseten, ByteDance, CoreWeave, Crusoe, DigitalOcean, Gcore, Pinterest [[G-08]](#ref-g-08)

**연구 동향**
- KubeCon Europe 2026 기준, Kubernetes 생태계의 AI 인프라화가 기술 의제 최상위로 부상. DRA·llm-d·Grove·AI Runway 4개 주요 프로젝트가 동시에 CNCF 산하 편입되어 GPU 오케스트레이션 표준화 단계 진입
- 이종 하드웨어 추상화(NVIDIA GPU + Groq LPU + AMD GPU)와 Prefill/Decode 분리 아키텍처가 차세대 추론 최적화의 핵심 연구 방향으로 수렴

---

## 전략적 시사점

**기회**
- NVIDIA의 오픈소스 전략 전환으로 DRA/KAI/Grove 스택이 벤더 중립 표준으로 진화 중. 조기 도입 시 멀티벤더 하이브리드 GPU 클러스터 구축 비용·복잡성 대폭 감소
- Microsoft AI Runway + Dynamo + llm-d 조합이 Kubernetes 네이티브 추론 플랫폼의 사실상 표준(de facto stack)으로 수렴 가능. 지금이 내부 플랫폼 아키텍처 정렬 시점
- SkyPilot 사례(Shopify)처럼 단일 YAML 추상화 + Kueue 공정 분배 + 팀별 비용 추적 패턴은 통신사 내부 AI 인프라 운영에 즉시 적용 가능한 참조 아키텍처

**위협**
- GPU 오케스트레이션 표준 경쟁(CNCF vs. 프로프라이어터리)이 단기 분열 위험. llm-d·Grove·AI Runway가 각자 "공통 API"를 표방하나 실제 통합 경로 미확정 — 잘못 선택한 플랫폼에 락인 위험
- Nscale 등 수직 통합 GPU 클라우드 스타트업의 급성장($14.6B 밸류)이 하이퍼스케일러 GPU 가격 전쟁을 심화. 자체 GPU 클러스터 구축 시 TCO 정당화 어려워지는 구조
- Groq 3 LPX(저지연) + Vera Rubin(고처리량)의 이종 조합이 실제 운영 복잡성을 대폭 높임. 오케스트레이션 레이어가 이를 투명하게 추상화하지 못하면 운영 부담 증가

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | NVIDIA Blog — Advancing Open Source AI, NVIDIA Donates DRA Driver for GPUs | [링크](https://blogs.nvidia.com/blog/nvidia-at-kubecon-2026/) | news | 2026-03-24 | [A] |
| <a id="ref-g-02"></a>G-02 | NVIDIA Developer — Grove Open-Source Kubernetes API | [링크](https://developer.nvidia.com/grove) | news | 2026-03-24 | [A] |
| <a id="ref-g-03"></a>G-03 | GitHub — KAI Scheduler CNCF Sandbox Issue #372 | [링크](https://github.com/cncf/sandbox/issues/372) | news | 2026-03-24 | [A] |
| <a id="ref-g-04"></a>G-04 | Rafay — Kubernetes Makes GPUs First-Class: Advances in Allocation, Scheduling, and Isolation | [링크](https://rafay.co/ai-and-cloud-native-blog/advancing-gpu-scheduling-and-isolation-in-kubernetes) | blog | 2026-03-24 | [B] |
| <a id="ref-g-05"></a>G-05 | CNCF Blog — Welcome llm-d to the CNCF | [링크](https://www.cncf.io/blog/2026/03/24/welcome-llm-d-to-the-cncf-evolving-kubernetes-into-sota-ai-infrastructure/) | news | 2026-03-24 | [A] |
| <a id="ref-g-06"></a>G-06 | Microsoft Open Source Blog — What's new with Microsoft at KubeCon + CloudNativeCon Europe 2026 | [링크](https://opensource.microsoft.com/blog/2026/03/24/whats-new-with-microsoft-in-open-source-and-kubernetes-at-kubecon-cloudnativecon-europe-2026/) | news | 2026-03-24 | [A] |
| <a id="ref-g-07"></a>G-07 | Windows Forum — Microsoft KubeCon 2026: Kubernetes Becomes AI Infrastructure OS with DRA, AI Runway & Cilium | [링크](https://windowsforum.com/threads/microsoft-kubecon-2026-kubernetes-becomes-ai-infrastructure-os-with-dra-ai-runway-cilium.407624/) | news | 2026-03-24 | [B] |
| <a id="ref-g-08"></a>G-08 | NVIDIA Technical Blog — How NVIDIA Dynamo 1.0 Powers Multi-Node Inference at Production Scale | [링크](https://developer.nvidia.com/blog/nvidia-dynamo-1-production-ready/) | news | 2026-03-16 | [A] |
| <a id="ref-g-09"></a>G-09 | Shopify Engineering — SkyPilot at Shopify: Multi-cloud GPUs without the pain (2026) | [링크](https://shopify.engineering/skypilot) | blog | 2026-03-01 | [B] |
| <a id="ref-g-10"></a>G-10 | Nscale Press Release — Nscale Raises $2 Billion in Series C | [링크](https://www.nscale.com/press-releases/nscale-series-c) | news | 2026-03-09 | [A] |
| <a id="ref-g-11"></a>G-11 | Virtualization Review — NVIDIA, AWS and Google Cloud Spotlight AI Infrastructure Push at GTC 2026 | [링크](https://virtualizationreview.com/articles/2026/03/20/nvidia-aws-and-google-cloud-spotlight-ai-infrastructure-push-at-gtc-2026.aspx) | news | 2026-03-20 | [B] |
| <a id="ref-g-12"></a>G-12 | NVIDIA Technical Blog — Inside NVIDIA Groq 3 LPX: The Low-Latency Inference Accelerator for the NVIDIA Vera Rubin Platform | [링크](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | news | 2026-03-16 | [A] |
| <a id="ref-g-13"></a>G-13 | Pure Storage Blog — Pure KVA Now Integrates with NVIDIA Dynamo for Scalable, Low-latency LLM Inference | [링크](https://blog.purestorage.com/news-events/pure-kva-integrates-nvidia-dynamo-for-scalable-low-latency-llm-inference/) | news | 2026-03-01 | [B] |
| <a id="ref-g-14"></a>G-14 | Fortune Business Insights — GPU as a Service Market Size, Growth Forecast [2032] | [링크](https://www.fortunebusinessinsights.com/gpu-as-a-service-market-107797) | report | 2026-01-01 | [B] |
| <a id="ref-g-15"></a>G-15 | Research and Markets — Hybrid Cloud Orchestration Market Report 2026 | [링크](https://www.researchandmarkets.com/reports/6215633/hybrid-cloud-orchestration-market-report) | report | 2026-01-01 | [B] |
| <a id="ref-g-16"></a>G-16 | SDxCentral — Nvidia unveils Grove: An open source API to help orchestrate AI inference | [링크](https://www.sdxcentral.com/news/nvidia-unveils-grove-an-open-source-api-to-help-orchestrate-ai-inference/) | news | 2026-03-24 | [B] |
| <a id="ref-g-17"></a>G-17 | Help Net Security — NVIDIA puts GPU orchestration in community hands | [링크](https://www.helpnetsecurity.com/2026/03/24/nvidia-kubernetes-gpu-driver-community/) | news | 2026-03-24 | [B] |
| <a id="ref-g-18"></a>G-18 | Canonical Blog — NVIDIA donates the GPU DRA driver to the CNCF at KubeCon Europe 2026 | [링크](https://canonical.com/blog/canonical-nvidia-kubecon-2026) | news | 2026-03-24 | [A] |
| <a id="ref-g-19"></a>G-19 | The New Stack — IBM, Red Hat, and Google donated a Kubernetes blueprint for LLM inference to the CNCF | [링크](https://thenewstack.io/llm-d-cncf-kubernetes-inference/) | news | 2026-03-24 | [B] |
| <a id="ref-g-20"></a>G-20 | Google Cloud Blog — Scaling MoE inference with NVIDIA Dynamo on Google Cloud A4X | [링크](https://cloud.google.com/blog/products/compute/scaling-moe-inference-with-nvidia-dynamo-on-google-cloud-a4x) | news | 2026-03-24 | [A] |
| <a id="ref-g-21"></a>G-21 | NVIDIA Newsroom — NVIDIA Enters Production With Dynamo, the Broadly Adopted Inference Operating System for AI Factories | [링크](https://nvidianews.nvidia.com/news/nvidia-enters-production-with-dynamo-the-broadly-adopted-inference-operating-system-for-ai-factories) | news | 2026-03-16 | [A] |
| <a id="ref-g-22"></a>G-22 | AKS Engineering Blog — Scaling multi-node LLM inference with NVIDIA Dynamo and NVIDIA GPUs on AKS (Part 3) | [링크](https://blog.aks.azure.com/2026/03/16/dynamo-on-aks-part-3) | news | 2026-03-16 | [A] |
| <a id="ref-g-23"></a>G-23 | SkyPilot GitHub Releases — skypilot-org/skypilot releases | [링크](https://github.com/skypilot-org/skypilot/releases) | blog | 2026-03-01 | [B] |
| <a id="ref-g-24"></a>G-24 | HPCwire — Microsoft Advances Open-Source AI Infrastructure on Kubernetes at KubeCon Europe 2026 | [링크](https://www.hpcwire.com/off-the-wire/microsoft-advances-open-source-ai-infrastructure-on-kubernetes-at-kubecon-europe-2026/) | news | 2026-03-24 | [B] |
