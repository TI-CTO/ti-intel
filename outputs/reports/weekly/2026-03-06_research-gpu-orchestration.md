---
type: weekly-deep-research
topic: gpu-orchestration
date: 2026-03-06
domain: axops
agent: research-deep
confidence: high
status: completed
sources_used: [websearch]
---

# 심층 리서치: 하이브리드 GPU Orchestration

> **Executive Summary**: 2026년 GPU 오케스트레이션 시장은 인퍼런스 효율화 경쟁이 최전선으로 부상하며 급속도로 성숙해지고 있다. NVIDIA는 Run:ai + Dynamo 이중 레이어로 GPU 활용률 2배·first-token 지연 61배 감소를 달성했고, 오픈소스 진영(SkyPilot, Kthena, vLLM)은 멀티클라우드·이종 GPU·KV캐시 인식 라우팅으로 벤더 종속 탈출을 가속하고 있다. 통신 인프라에서는 Nokia·Samsung이 MWC 2026에서 GPU 기반 AI-RAN 상용화를 선언했으며, LG는 파주 AIDC(GPU 12만 장, 200MW, 2027 준공)와 Trusted Orchestration 아키텍처를 K-엑사원 전략의 핵심 인프라로 제시했다. GPU-as-a-Service 시장은 2026년 $73억, 2031년 $259억(CAGR 28.7%) 규모로 성장 예고. [B]

---

#### 기술 동향

**오케스트레이션 레이어 기술 성숙**

2026년 기준 GPU 오케스트레이션은 단순 스케줄링을 넘어 인퍼런스 서빙 최적화로 중심축이 이동했다. Kubernetes DRA(Dynamic Resource Allocation)가 v1.35에서 stable 승격·기본 활성화되면서 GPU를 first-class 스케줄링 자원으로 처리하는 기반이 완성됐다 [[G-06]](#ref-g-06). 그러나 실제 운영 환경에서는 well-run 클러스터도 GPU 평균 활용률이 20~30%에 머문다는 문제가 지속 보고된다 [[G-05]](#ref-g-05).

**Prefill-Decode 분리(P/D Disaggregation) 패러다임**

2025~2026년 인퍼런스 아키텍처의 핵심 혁신은 Prefill(프롬프트 처리)과 Decode(토큰 생성) 단계를 물리적으로 분리하여 각각 독립 최적화하는 P/D Disaggregation이다 [[G-07]](#ref-g-07). NVIDIA Dynamo는 이 패턴을 프로덕션 스케일로 구현한 오픈소스 프레임워크로, KV캐시 인식 라우터·GPU Resource Planner를 포함하며 DeepSeek-R1 기준 처리량 30배 향상을 달성했다 [[G-08]](#ref-g-08). 2026년 1월 Azure Kubernetes Service 상에서 다중 노드 배포가 실증됐다 [[G-08]](#ref-g-08).

**vLLM 생태계 심화**

- **LMCache**: KV 캐시를 GPU 메모리 외부에 오프로드·엔진 간 공유하는 오픈소스 솔루션. Prefill-Decode 분리를 지원하며 멀티턴 대화에서 재연산 제거 효과가 크다 [[G-13]](#ref-g-13).
- **vLLM AMD ROCm 지원**: 2026년 2월 AMD ROCm 전용 어텐션 백엔드 최적화가 공개됐다 [[G-14]](#ref-g-14). CUDA 워크로드의 AMD MI300X 이전이 실용적 수준에 진입.
- **llm-d (Red Hat)**: KV캐시 인식 라우팅으로 분산 스케줄링을 구현하는 프레임워크 [[G-13]](#ref-g-13).

**Kthena: Kubernetes-Native 인퍼런스 오케스트레이션**

Volcano 커뮤니티가 2026년 1월 CNCF를 통해 공개한 Kthena는 Kubernetes 네이티브 LLM 인퍼런스 오케스트레이션 플랫폼이다 [[G-11]](#ref-g-11). vLLM·SGLang·Triton·TorchServe를 지원하며 KV캐시 인식 라우팅, P/D 분리, 토폴로지 인식 스케줄링을 내장한다. 기존 인퍼런스 엔진을 대체하지 않고 인텔리전트 오케스트레이션 레이어로 동작하는 것이 특징이다.

**NVIDIA KAI Scheduler + Ray 통합**

NVIDIA KAI Scheduler가 KubeRay에 네이티브 통합되어 Ray 클러스터에 Gang Scheduling·우선순위 큐·워크로드 선점 기능을 제공한다 [[G-10]](#ref-g-10). 이는 Run:ai의 스케줄링 엔진을 Ray 생태계로 확장한 것으로, 학습과 인퍼런스가 동일 GPU 풀을 공유하는 멀티워크로드 환경에서 효율을 높인다.

**AMD ROCm 7.0 + SkyPilot 멀티클라우드 이종 GPU**

AMD ROCm 7.0은 엔터프라이즈급 클러스터 관리 도구를 포함하며, SkyPilot과의 통합으로 CUDA 기반 워크로드를 AMD Instinct MI300X로 최소 변경 이전하는 경로를 제공한다 [[G-12]](#ref-g-12). SkyPilot은 AWS, GCP, Azure, CoreWeave, Nebius, Lambda, RunPod, Vast.ai 등 20개 이상 클라우드를 단일 YAML로 추상화한다.

---

#### 플레이어 동향

**주요 플레이어 동향 테이블**

| 기업 | 동향 | 출처 |
|------|------|------|
| NVIDIA | Run:ai v2.24: GPU Fractioning + Bin Packing으로 인퍼런스 GPU 활용률 2x, 처리량 1.4x, TTFT 44~61x 개선. Dynamo 오픈소스 출시(P/D Disaggregation, KV캐시 라우터). GTC 2026 발표 예정 | [[G-01]](#ref-g-01), [[G-02]](#ref-g-02), [[G-08]](#ref-g-08) |
| NVIDIA (AI-RAN) | Nokia와 NVIDIA Grace Hopper 200 단일 서버에서 AI+RAN 동시 처리 실증. 2026 상용 시험, 2027 상용 출시 목표 | [[G-15]](#ref-g-15), [[G-16]](#ref-g-16) |
| Samsung | MWC 2026: NVIDIA Aerial 플랫폼 기반 AI-RAN 멀티셀 테스트 완료. AI 빔포밍으로 스펙트럼 효율 향상 실증. GPU Lock-In 탈피 CPU 옵션도 검증 | [[G-17]](#ref-g-17) |
| Nokia | MWC 2026: AI-RAN SMO 플랫폼에 rApp 마켓플레이스 출시. BT·Elisa·NTT DoCoMo·Vodafone·Indosat과 AI-RAN 배포. NVIDIA와 단일 GPU 플랫폼 전략 확정 | [[G-15]](#ref-g-15), [[G-16]](#ref-g-16) |
| LG (LG U+/AI Research) | MWC 2026: K-엑사원 로드맵 발표. 4대 아키텍처 중 "Trusted Orchestration" 포함 — 다수 AI(Planning·Execution·Evaluation·Review AI) 협업 조율. 파주 AIDC GPU 12만 장·200MW·2027 준공 | [[N-01]](#ref-n-01), [[N-02]](#ref-n-02), [[N-03]](#ref-n-03) |
| CoreWeave | IPO 후 2026년 NVIDIA로부터 $20억 추가 투자 유치. NVIDIA Rubin 플랫폼 최초 배포 클라우드 예정(2026 H2). Perplexity와 GB200 NVL72 전용 클러스터 계약(2026-03-04). 2026년 매출 $120억 예상(YoY +134~138%) | [[G-18]](#ref-g-18) |
| SkyPilot (오픈소스) | v0.11 출시(2025-12): 멀티클라우드 풀, 빠른 Managed Jobs, 엔터프라이즈 스케일. CoreWeave 공식 지원(InfiniBand·오브젝트 스토리지·오토스케일링). AMD ROCm 7.0 + Ray 통합. Vast.ai Secure Cloud 필터링 지원 | [[G-03]](#ref-g-03), [[G-19]](#ref-g-19) |
| VAST Data | 2026-02-25: Polaris 발표 — 퍼블릭 클라우드·네오클라우드·온프레미스 AI 인프라를 단일 API로 프로비저닝·오케스트레이션하는 글로벌 컨트롤 플레인 | [[G-20]](#ref-g-20) |
| Volcano/Kthena | 2026-01-28 CNCF 출시: Kubernetes-native LLM 인퍼런스 오케스트레이션. KV캐시 인식 라우팅·P/D 분리·토폴로지 인식 스케줄링 | [[G-11]](#ref-g-11) |
| AMD | ROCm 7.0: 엔터프라이즈 클러스터 관리 강화. vLLM AMD 어텐션 백엔드 최적화(2026-02-27). SkyPilot 통합으로 NVIDIA 대안 포지셔닝 | [[G-12]](#ref-g-12), [[G-14]](#ref-g-14) |
| Google | Ironwood TPU(7세대, 인퍼런스 특화·FP8 네이티브) 공개. Pathways 런타임 JetStream 통합으로 멀티호스트 인퍼런스·P/D 분리 지원. Anthropic에 Trillium TPU 수십만 개 계약 | [[G-21]](#ref-g-21) |

---

#### 시장 시그널

**시장 규모**

- GPU-as-a-Service 시장: 2026년 **$73.4억**, 2031년 **$259.4억** (CAGR 28.7%) [[G-22]](#ref-g-22)
- 멀티/하이브리드 클라우드 세그먼트 CAGR 29.4%로 최고 성장 — 오케스트레이션 소프트웨어가 핵심 드라이버 [[G-22]](#ref-g-22)
- AI 데이터센터 GPU 시장: 2026년 $128.3억 → 2035년 $771.5억 (CAGR 22.1%) [[G-23]](#ref-g-23)
- 인퍼런스 세그먼트가 시장 최대 점유 — 실시간 AI 애플리케이션 수요 주도 [[G-23]](#ref-g-23)

**투자 & 파트너십**

- **CoreWeave**: NVIDIA $20억 투자(2026-01), Meta $142억 계약(~2031), OpenAI $224억 계약, Perplexity 전용 GB200 클러스터(2026-03-04) [[G-18]](#ref-g-18)
- **VAST Data Polaris**: 퍼블릭·네오클라우드·온프레미스 통합 컨트롤 플레인 출시(2026-02-25) [[G-20]](#ref-g-20)
- **Nokia + NVIDIA**: 6G AI-Native 플랫폼 공동 개발 — 미국 통신 리더십 목표 [[G-15]](#ref-g-15)
- **LG 파주 AIDC**: GPU 12만 장·200MW·2027년 수도권 최대 규모 준공. "One Team LG" 전략(LG전자·LG CNS·LG에너지솔루션 역량 통합) [[N-01]](#ref-n-01)
- **Shopify**: SkyPilot으로 전사 학습 워크로드 운영 (멀티클라우드 YAML 정의 방식) [[G-03]](#ref-g-03)

**표준화·오픈소스 모멘텀**

- CNCF Kthena 채택: 클라우드 네이티브 인퍼런스 오케스트레이션 표준화 추진
- NVIDIA KAI Scheduler: Ray·KubeRay 네이티브 통합으로 오케스트레이션 생태계 확장
- Kubernetes DRA stable 승격(v1.35): GPU fractional 할당·토폴로지 인식 스케줄링 표준화

---

#### 학술 동향

**주요 논문 테이블**

| 논문 | 핵심 기여 | 연도 | 출처 |
|------|----------|------|------|
| Nexus: Proactive Intra-GPU Disaggregation of Prefill and Decode | 단일 엔진 내 Prefill·Decode를 별도 배치로 분리 실행, SM 동적 재할당으로 워크로드 변화 적응 | 2025 | [[P-01]](#ref-p-01) |
| RAPID-Serve: Resource-efficient Accelerated P/D Intra-GPU Disaggregation | 동일 GPU에서 Prefill·Decode 동시 실행, Adaptive Resource Management로 SLO 준수+고처리량 달성 | 2026-01 | [[P-02]](#ref-p-02) |
| FlowPrefill: Decoupling Preemption from Prefill Scheduling | 연산자 레벨 Fine-grained Preemption으로 Head-of-Line Blocking 완화, 멀티-SLO 굿풋 최적화 | 2026-02 | [[P-03]](#ref-p-03) |
| Disaggregated Prefill-Decode for Multi-Vendor GPUs | 이종 GPU(다중 벤더) 환경에서 P/D 분리 인퍼런스 시스템 구현, 리소스 활용 최대화 | 2025-09 | [[P-04]](#ref-p-04) |
| HeteroScale: Coordinated Autoscaling for Disaggregated LLM Inference | 토폴로지 인식 스케줄러 + 단일 메트릭 기반 Prefill·Decode 풀 공동 오토스케일링 | 2025-08 | [[P-05]](#ref-p-05) |
| Disaggregated Multi-Stage MLLM Inference via GPU-Internal Scheduling | 멀티모달 LLM의 비전 인코더·LLM 프리필·디코딩 3단계 분리 파이프라인, 스테이지 간 블로킹 제거 | 2025-12 | [[P-06]](#ref-p-06) |
| Token Management in Multi-Tenant AI Inference Platforms | 멀티테넌트 인퍼런스 플랫폼의 토큰 관리 최적화 (arXiv 2603.00356) | 2026-03 | [[P-07]](#ref-p-07) |

**연구 방향 요약**

**P/D 분리 최적화**: 인트라-GPU(동일 GPU 내 분리)와 인터-GPU(노드 간 분리) 두 방향으로 동시 연구 진행. 이종 GPU 환경 지원이 주요 이슈.

**KV캐시 효율화**: 캐시 오프로드, 엔진 간 공유, 인식 라우팅이 트리오를 이루며 인퍼런스 비용 절감의 핵심 경로로 부상.

**멀티모달 확장**: 비전 인코더 등 비LLM 스테이지를 포함한 이종 연산 파이프라인 오케스트레이션으로 연구 범위 확장.

---

#### 전략적 시사점

**기회**

- GPU 평균 활용률 20~30%라는 업계 공통 과제는 오케스트레이션 솔루션의 명확한 ROI 근거. Run:ai 벤치마크(활용률 2x)는 도입 비즈니스 케이스를 실증함
- P/D Disaggregation + KV캐시 인식 라우팅은 동일 GPU 투자로 처리량을 수배 향상시키는 검증된 아키텍처 패턴. NVIDIA Dynamo(오픈소스)·Kthena(CNCF)로 즉시 채택 가능
- SkyPilot + AMD ROCm 7.0 통합은 NVIDIA 종속 해소를 위한 실용적 경로. CoreWeave·Vast.ai 같은 네오클라우드 활용으로 비용 절감 여지 확보
- 통신 영역(AI-RAN)에서 GPU 오케스트레이션 수요 신규 창출 — Nokia·Samsung이 MWC 2026에서 상용화 타임라인 확정(2026 시험, 2027 출시)

**위협**

- NVIDIA의 수직 통합(H/W → Run:ai 스케줄러 → Dynamo 서빙 → NIM 마이크로서비스) 심화로 단일 벤더 의존도 경로 고착화 위험
- GPU 공급 병목 지속 — CoreWeave $300억+ 백로그, Anthropic 수십만 TPU 선점 사례가 보여주듯 컴퓨트 확보 경쟁 격화
- 오픈소스 분열(vLLM·SGLang·TorchServe·Triton·Dynamo·Kthena 등) — 오케스트레이션 레이어 표준 미확립으로 기술 선택 복잡도 상승
- 한국 AI 데이터센터 투자(LG 파주 200MW)는 2027 준공 예정 — 현재 국내 GPU 인프라 gap이 글로벌 대비 1~2년 지연 구조

---

## References

**글로벌 출처 (G-xx)**

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | NVIDIA Technical Blog — Maximizing GPU Utilization with Run:ai and NIM | [링크](https://developer.nvidia.com/blog/maximizing-gpu-utilization-with-nvidia-runai-and-nvidia-nim/) | 공식 블로그 | 2026-02 | [A] |
| <a id="ref-g-02"></a>G-02 | NVIDIA Technical Blog — GPU Fractioning: 77% Throughput at Half Allocation | [링크](https://developer.nvidia.com/blog/unlock-massive-token-throughput-with-gpu-fractioning-in-nvidia-runai/) | 공식 블로그 | 2026-02 | [A] |
| <a id="ref-g-03"></a>G-03 | CoreWeave Blog — SkyPilot Multi-Cloud AI Orchestration | [링크](https://www.coreweave.com/blog/coreweave-adds-skypilot-support-for-effortless-multi-cloud-ai-orchestration) | 기업 블로그 | 2026 | [B] |
| <a id="ref-g-04"></a>G-04 | SkyPilot Blog — v0.11 Multi-Cloud Pools, Fast Managed Jobs | [링크](https://blog.skypilot.co/announcing-skypilot-0.11.0/) | 오픈소스 공식 | 2025-12 | [B] |
| <a id="ref-g-05"></a>G-05 | ScaleOps — Kubernetes GPU Resource Management New Approach | [링크](https://scaleops.com/blog/ai-infra-for-production-why-gpu-resource-management-in-kubernetes-demands-a-new-approach/) | 전문 블로그 | 2026 | [B] |
| <a id="ref-g-06"></a>G-06 | AceCloud — Multi GPU Orchestration in Kubernetes 2026: Kueue, Volcano, DRA | [링크](https://acecloud.ai/blog/multi-gpu-orchestration-kubernetes/) | 전문 블로그 | 2026 | [B] |
| <a id="ref-g-07"></a>G-07 | vLLM Docs — Disaggregated Prefilling (experimental) | [링크](https://docs.vllm.ai/en/latest/features/disagg_prefill/) | 공식 문서 | 2026 | [A] |
| <a id="ref-g-08"></a>G-08 | NVIDIA Developer — Introducing NVIDIA Dynamo Distributed Inference Framework | [링크](https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/) | 공식 블로그 | 2025 | [A] |
| <a id="ref-g-09"></a>G-09 | NVIDIA Developer — Smart Multi-Node Scheduling with Run:ai and Dynamo | [링크](https://developer.nvidia.com/blog/smart-multi-node-scheduling-for-fast-and-efficient-llm-inference-with-nvidia-runai-and-nvidia-dynamo) | 공식 블로그 | 2026 | [A] |
| <a id="ref-g-10"></a>G-10 | NVIDIA Developer — Gang Scheduling and Workload Prioritization in Ray with KAI Scheduler | [링크](https://developer.nvidia.com/blog/enable-gang-scheduling-and-workload-prioritization-in-ray-with-nvidia-kai-scheduler) | 공식 블로그 | 2026 | [A] |
| <a id="ref-g-11"></a>G-11 | CNCF Blog — Introducing Kthena: LLM Inference for the Cloud Native Era | [링크](https://www.cncf.io/blog/2026/01/28/introducing-kthena-llm-inference-for-the-cloud-native-era/) | CNCF 공식 | 2026-01-28 | [A] |
| <a id="ref-g-12"></a>G-12 | AMD ROCm Blog — Autoscaling with Ray, ROCm 7.0, and SkyPilot | [링크](https://rocm.blogs.amd.com/ecosystems-and-partners/ray-rocm7/README.html) | 공식 블로그 | 2026 | [A] |
| <a id="ref-g-13"></a>G-13 | llm-d.ai — KV-Cache Wins: From Prefix Caching in vLLM to Distributed Scheduling | [링크](https://llm-d.ai/blog/kvcache-wins-you-can-see) | 공식 블로그 | 2026 | [B] |
| <a id="ref-g-14"></a>G-14 | vLLM Blog — High-Performance Inference on AMD ROCm | [링크](https://blog.vllm.ai/2026/02/27/rocm-attention-backend.html) | 공식 블로그 | 2026-02-27 | [A] |
| <a id="ref-g-15"></a>G-15 | Nokia Newsroom — AI-RAN Momentum with NVIDIA, Path to AI-Native 6G #MWC26 | [링크](https://www.nokia.com/newsroom/nokia-accelerates-ai-ran-momentum-with-new-partnerships-driving-path-to-ai-native-6g-mwc26/) | 공식 보도자료 | 2026-03-01 | [A] |
| <a id="ref-g-16"></a>G-16 | NVIDIA Blog — Software-Defined AI-RAN Is the Next Wireless Generation | [링크](https://blogs.nvidia.com/blog/software-defined-ai-ran/) | 공식 블로그 | 2026 | [A] |
| <a id="ref-g-17"></a>G-17 | The Meridiem — Samsung AI-RAN Validation Breaks GPU Lock-In | [링크](https://www.themeridiem.com/ai/2026/3/2/samsung-s-ai-ran-validation-breaks-gpu-lock-in-as-operators-choose-cpus) | 전문 언론 | 2026-03-02 | [B] |
| <a id="ref-g-18"></a>G-18 | CoreWeave — Extends Cloud Platform with NVIDIA Rubin Platform | [링크](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Extends-Its-Cloud-Platform-with-NVIDIA-Rubin-Platform/default.aspx) | 공식 IR | 2026 | [A] |
| <a id="ref-g-19"></a>G-19 | Vast.ai — January & February 2026 Product Updates | [링크](https://vast.ai/article/january-february-2026-product-update) | 공식 블로그 | 2026-02 | [B] |
| <a id="ref-g-20"></a>G-20 | GlobeNewswire — VAST Data Introduces Polaris for Hybrid Multicloud AI Infrastructure | [링크](https://www.globenewswire.com/news-release/2026/02/25/3244908/0/en/VAST-Data-Introduces-Polaris-to-Orchestrate-Globally-Distributed-AI-Data-Infrastructure-Across-Hybrid-Multicloud-Environments.html) | 공식 보도자료 | 2026-02-25 | [A] |
| <a id="ref-g-21"></a>G-21 | Google Blog — Ironwood: First Google TPU for the Age of Inference | [링크](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/) | 공식 블로그 | 2026 | [A] |
| <a id="ref-g-22"></a>G-22 | Mordor Intelligence — GPU as a Service Market Size 2026–2031 | [링크](https://www.mordorintelligence.com/industry-reports/gpu-as-a-service-market) | 시장조사 | 2026 | [B] |
| <a id="ref-g-23"></a>G-23 | Precedence Research — AI Data Center GPU Market to $77.15B by 2035 | [링크](https://www.precedenceresearch.com/ai-data-center-gpu-market) | 시장조사 | 2026 | [B] |

**최신 동향 (N-xx)**

| # | 출처명 | 발행일 | 제목 | 요약(한글) | URL |
|---|--------|-------|------|-----------|-----|
| <a id="ref-n-01"></a>N-01 | 인사이트코리아 | 2026-03 | LGU+, 파주에 GPU 12만 장 채운 데이터센터 구축 | LG U+가 파주에 GPU 12만 장·200MW 규모 AI 데이터센터 구축 계획 발표. 'AI 퀀텀점프' 전략의 핵심 인프라 | [링크](https://www.insightkorea.co.kr/news/articleView.html?idxno=242033) |
| <a id="ref-n-02"></a>N-02 | 아주경제 | 2026-03-02 | LG그룹 역량 한데 모은다…파주 AIDC 2027년 준공 | LG전자·LG CNS·LG에너지솔루션 역량을 파주 AIDC에 집결하는 "One Team LG" 전략 | [링크](https://www.ajunews.com/view/20260302010905149) |
| <a id="ref-n-03"></a>N-03 | 전자신문 | 2026-03-05 | 정숙경 LG유플러스 담당 "파주 AIDC, 비욘드 AI 시대 열 것" | LG U+ MWC 바르셀로나 포럼에서 파주 AIDC 전략 구체화 발언 | [링크](https://www.etnews.com/20260305000231) |
| <a id="ref-n-04"></a>N-04 | The Korea Herald | 2026-03 | LG eyes global AI leadership with Exaone 4.5 launch | EXAONE 4.5 상반기 출시, 동급 오픈웨이트 모델 최고 성능 목표 | [링크](https://www.koreaherald.com/article/10685061) |
| <a id="ref-n-05"></a>N-05 | Digital Today (EN) | 2026-03 | LG steps up One Team AI strategy with EXAONE upgrade and 200-MW data centre | LG 원팀 AI 전략 — Trusted Orchestration이 4대 핵심 기술 중 하나 | [링크](https://www.digitaltoday.co.kr/en/view/14819/lg-steps-up-one-team-lg-ai-strategy-with-exaone-upgrade-and-200mw-data-centre) |
| <a id="ref-n-06"></a>N-06 | telecoms.com | 2026-03 | Nokia charts course to AI-native 6G at MWC 2026 | Nokia MWC 2026 AI-native 6G 전략, SMO rApp 마켓플레이스, NVIDIA 단일 플랫폼 | [링크](https://www.telecoms.com/5g-6g/nokia-charts-course-to-ai-native-6g-) |
| <a id="ref-n-07"></a>N-07 | Samsung+NVIDIA/TechBuzz | 2026-03 | Samsung and Nvidia Push AI-RAN to Commercial Reality | Samsung+NVIDIA AI-RAN 멀티셀 검증 완료, MWC 2026 AI 빔포밍 시연 | [링크](https://www.techbuzz.ai/articles/samsung-and-nvidia-push-ai-ran-to-commercial-reality) |

**기업 발언 (E-xx)**

| # | 출처명 | 발행일 | 내용 요약 |
|---|--------|-------|---------|
| <a id="ref-e-01"></a>E-01 | LG AI Research / LG U+ MWC 2026 공동 발표 | 2026-03-01 | "Trusted Orchestration은 Planning AI·Execution AI·Evaluation AI·Review-and-Revision AI가 각각 역할을 수행하면서 협업을 조율하는 아키텍처" — K-엑사원 4대 핵심 기술 중 하나 |
| <a id="ref-e-02"></a>E-02 | NVIDIA Data Center (X/Twitter 공식 계정) | 2026-02 | "Most teams running LLM inference are overprovisioning GPUs 'just in case.' We benchmarked NIM + Run:ai on dramatically fewer GPUs — with minimal throughput loss." |
| <a id="ref-e-03"></a>E-03 | Nokia 공식 보도자료 (GlobeNewswire) | 2026-03-01 | "2026 is where we will do our first commercial trial, and 2027 is where we will have our first commercial release out." — Nokia-NVIDIA AI-RAN 상용화 타임라인 |
| <a id="ref-e-04"></a>E-04 | CoreWeave 투자자 IR | 2026-03-04 | CoreWeave-Perplexity 멀티연 전략적 파트너십 체결, Perplexity가 GB200 NVL72 전용 클러스터에서 차세대 AI 인퍼런스 워크로드 운영 |

**학술 논문 (P-xx)**

| # | 저자/그룹 | 연도 | 제목 | DOI/URL |
|---|-----------|------|------|---------|
| <a id="ref-p-01"></a>P-01 | — | 2025 | Nexus: Proactive Intra-GPU Disaggregation of Prefill and Decode in LLM Serving | [arxiv.org/abs/2507.06608](https://arxiv.org/abs/2507.06608) |
| <a id="ref-p-02"></a>P-02 | — | 2026-01 | RAPID-Serve: Resource-efficient and Accelerated P/D Intra-GPU Disaggregation | [arxiv.org/abs/2601.11822](https://arxiv.org/abs/2601.11822) |
| <a id="ref-p-03"></a>P-03 | — | 2026-02 | FlowPrefill: Decoupling Preemption from Prefill Scheduling Granularity | [arxiv.org/html/2602.16603](https://arxiv.org/html/2602.16603) |
| <a id="ref-p-04"></a>P-04 | — | 2025-09 | Disaggregated Prefill and Decoding Inference System for Large Language Model Serving on Multi-Vendor GPUs | [arxiv.org/abs/2509.17542](https://arxiv.org/abs/2509.17542) |
| <a id="ref-p-05"></a>P-05 | — | 2025-08 | Taming the Chaos: Coordinated Autoscaling for Heterogeneous and Disaggregated LLM Inference | [arxiv.org/abs/2508.19559](https://arxiv.org/abs/2508.19559) |
| <a id="ref-p-06"></a>P-06 | — | 2025-12 | Enabling Disaggregated Multi-Stage MLLM Inference via GPU-Internal Scheduling and Resource Sharing | [arxiv.org/abs/2512.17574](https://arxiv.org/abs/2512.17574) |
| <a id="ref-p-07"></a>P-07 | — | 2026-03 | Token Management in Multi-Tenant AI Inference Platforms | [arxiv.org/abs/2603.00356](https://arxiv.org/abs/2603.00356) |
