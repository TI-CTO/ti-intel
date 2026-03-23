---
type: weekly-deep-research
topic: gpu-orchestration
l3_name: 하이브리드 GPU Orchestration
domain: agentic-ai
week: 2026-W13
date: 2026-03-23
signal: 🟡
---

# Deep 리서치: 하이브리드 GPU Orchestration (2026-W13)

## 이전 대비 변화
- 전주: SkyPilot 멀티클라우드 확장(Shopify 프로덕션), AMD ROCm 7.0 + Ray Serve 통합, Neocloud Kubernetes 표준화 진행 — 구조적 돌파구 없음(🟢)
- 금주: AI 에이전트가 GPU 클러스터를 자율 관리하는 "에이전트 주도 GPU 오케스트레이션" 개념이 SkyPilot Agent/Job Groups·GTC 2026 기조 메시지를 통해 실체화되었고, 탈중앙화 P2P GPU 레이어(Ocean Network 베타)가 처음으로 프로덕션 접근 단계에 진입(🟡)
- 변화 방향: 오케스트레이션 추상화 레이어가 인간→에이전트로 주체가 이동하는 전환 신호; 중앙화 Neocloud 공급망과 탈중앙화 DePIN 레이어 간 경쟁 구도 부상

---

## 기술 동향

1. **SkyPilot Job Groups — 이종 하드웨어 RL 학습의 단일 YAML 오케스트레이션.**
   2026-03-02 출시. RL post-training(PPO, GRPO, RLHF)은 Trainer(고성능 GPU)·Rollout Server(저가 GPU)·Replay Buffer(고메모리 CPU)로 구성 요소마다 최적 하드웨어가 다르다. SkyPilot Job Groups는 이 이종(heterogeneous) 구성 전체를 단일 YAML로 정의하고, DNS 기반 자동 서비스 디스커버리(`trainer-0.job-name`)와 coordinated lifecycle으로 관리한다. Kubernetes·Slurm·20개+ 클라우드 지원. [[G-01]](#ref-g-01)

2. **SkyPilot + Claude Code 에이전트 자율 실험 — 910회 실험·2.87% 손실 개선 실증.**
   Claude Code에 16-GPU Kubernetes 클러스터 접근 권한을 부여했을 때, 8시간 동안 약 910회 실험을 자동 제출하여 val_bpb 1.003→0.974로 개선했다. 단순 순차 탐색 대비 처리량 9배(약 90 experiment/hr). 에이전트는 명시적 지시 없이 H100과 H200 성능 차이를 자체 발견하고 2-tier 검증 전략(H100 스크리닝→H200 확인)을 구사했다. 총 비용은 컴퓨트 약 $300 + Claude API ~$9. [[G-02]](#ref-g-02)

3. **Microsoft AKS DRA + NVIDIA vGPU — Kubernetes GPU 가상화 분할의 프로덕션 진입.**
   2026-03 AKS Engineering Blog 발표. Kubernetes 1.34+ Dynamic Resource Allocation(DRA)이 NVIDIA vGPU(NVadsA10_v5 시리즈)와 통합되어 단일 물리 GPU를 1/6·1/3·1/2 프로파일로 분할 할당 가능해졌다. MIG과 DRA 조합도 별도 GA 발표. 중소 워크로드의 GPU 비용 효율화에 직접적 영향. Kubernetes 1.34+ 필수. [[G-05]](#ref-g-05), [[G-06]](#ref-g-06)

4. **Anyscale Ray on AKS 멀티리전 — 3대 하이퍼스케일러의 Managed Ray 경쟁 전선 형성.**
   2026-03 InfoQ 보도. AKS 팀이 멀티클러스터·멀티리전 Ray 아키텍처 가이드를 공개하며 "리전 한도를 초과한 GPU 쿼터 집계"가 핵심 이점으로 제시됐다. Entra 워크로드 아이덴티티로 단기 토큰 자동 갱신, Azure BlobFuse2로 POSIX 파일 시스템 일관성 확보. AWS(EKS+SageMaker HyperPod), Google Cloud(KubeRay upstream 기여), Azure 3사가 모두 Managed Ray 경쟁에 진입. Private Preview 단계. [[G-07]](#ref-g-07)

5. **Ocean Network P2P GPU 오케스트레이션 베타 — 탈중앙화 컴퓨트 레이어의 실사용 진입.**
   2026-03-17 GlobeNewswire 공식 발표. VS Code·Cursor·Windsurf에 네이티브 통합되는 Ocean Orchestrator를 통해 개발자가 컨테이너화된 작업을 한 번의 클릭으로 분산 GPU에 제출할 수 있다. Aethir 파트너십으로 H200·H100부터 1060까지 다양한 GPU를 Pay-Per-Use Escrow(Base/Ethereum L2) 방식으로 사용. 얼리 어답터에게 $100 컴퓨트 크레딧 제공. Compute-to-Data(C2D) 아키텍처로 원시 데이터 보호. [[G-03]](#ref-g-03), [[G-04]](#ref-g-04)

6. **NVIDIA GTC 2026 — 에이전트 AI가 GPU 수요 구조를 재편하는 "인퍼런스 변곡점" 선언.**
   2026-03-16~19 산호세. Jensen Huang은 데이터센터를 "AI Factory"로 재정의하고, 추론(inference)·에이전트·물리적 AI로의 전환이 GPU 수요를 기존 학습 중심에서 다중 사용 사례로 분산시킨다고 역설했다. 2027년까지 최소 $1조 규모 수요를 전망. Vera Rubin NVL72(3.6 exaflops/rack-scale system)는 에이전트 AI를 위한 대역폭·인터커넥트 최적화 플랫폼으로 2026 H2 배포 예정. NemoClaw 오픈소스 에이전트 스택도 발표. [[G-08]](#ref-g-08), [[G-09]](#ref-g-09)

---

## 플레이어 동향

**주요 플레이어 동향**

| 기업 | 동향 | 출처 |
|------|------|------|
| SkyPilot (오픈소스) | Job Groups(2026-03-02) 출시: 이종 하드웨어 RL 학습을 단일 YAML로 오케스트레이션. Claude Code 에이전트와 통합 실증(910회 실험, 9x 처리량). 20개+ 클라우드·Kubernetes·Slurm 지원 | [[G-01]](#ref-g-01), [[G-02]](#ref-g-02) |
| NVIDIA | GTC 2026: Vera Rubin NVL72(3.6 exaflops/rack) 발표, 2026 H2 배포 예정. NemoClaw 에이전트 스택 오픈소스화. $1조+ 수요 전망. AWS 100만+ GPU 배포 협력 발표 | [[G-08]](#ref-g-08), [[G-09]](#ref-g-09) |
| CoreWeave | GTC 2026 연계(2026-03-16): NVIDIA HGX B300(HGX H200 대비 TTFT 4.93x, 처리량 3.42x) 일반 공급 개시. Cursor 이미 프로덕션 워크로드 이전 중. Vera Rubin NVL72 최초 배포 클라우드 예정(2026 H2). Weights & Biases 통합으로 RL·에이전트 개발 워크플로우 강화 | [[G-10]](#ref-g-10), [[G-11]](#ref-g-11) |
| Microsoft (AKS) | DRA + NVIDIA vGPU GA(2026-03-06): 단일 GPU 다중 프로파일 분할 할당. Anyscale Ray on AKS 멀티리전 가이드 공개(Private Preview). NVIDIA Rubin 대규모 배포를 위한 AI 데이터센터 계획 발표 | [[G-05]](#ref-g-05), [[G-06]](#ref-g-06), [[G-07]](#ref-g-07) |
| Anyscale (Ray) | AKS/EKS/GKE 3사 하이퍼스케일러 모두 Managed Ray 파트너십 체결 완료. Ray v2.49에서 label-based scheduling 및 Dynamic Resource Allocation GB200 인스턴스 지원 추가. KubeRay v1.5.1 3종 CRD 안정화 | [[G-07]](#ref-g-07), [[G-12]](#ref-g-12) |
| Nebius | KubeCon Europe 2026(2026-03-23~26 암스테르담) 참가. Soperator(Slurm-on-Kubernetes): self-healing·자동 스케일링·IaC 워크플로우 데모 발표. 400+ MW 확보, 2026년 말 1GW 목표. NVIDIA $2B 투자 수혜 | [[G-13]](#ref-g-13), [[G-14]](#ref-g-14) |
| Ocean Network (DePIN) | P2P GPU 오케스트레이션 베타 런칭(2026-03-17). IDE 네이티브 통합(VS Code·Cursor·Windsurf), Pay-Per-Use Escrow on Base. Aethir 파트너십으로 H200~H100 즉시 공급. 얼리 어답터 $100 크레딧 | [[G-03]](#ref-g-03), [[G-04]](#ref-g-04) |
| Lambda Labs | Microsoft 다년 계약 + TWG Global $1.5B 투자 확보. 2026년 IPO 목표. CoreWeave 대항마로 특화 AI 컴퓨팅 포지셔닝 강화 | [[G-15]](#ref-g-15) |

---

## 시장 시그널

- NVIDIA GTC 2026의 핵심 메시지는 "학습 중심 → 추론·에이전트 중심 전환"으로, 이는 GPU 오케스트레이션 요구사항이 대형 배치 학습 클러스터에서 고빈도 저지연 추론 및 에이전트 작업 큐 관리로 다변화됨을 의미한다. [[G-08]](#ref-g-08)
- 3대 하이퍼스케일러(AWS·Google Cloud·Azure)가 모두 GTC 2026에서 NVIDIA GPU 기반 AI 인프라 확장과 Managed Ray 통합을 발표함으로써, 오케스트레이션 레이어가 클라우드 벤더 lock-in의 새로운 경쟁지로 부상했다. [[G-09]](#ref-g-09)
- DePIN(탈중앙화 물리 인프라) GPU 시장 캡이 $52억→$190억으로 1년 만에 3.6배 성장. Ocean Network 베타·Depinfer Solana 스테이킹 거버넌스 등 사용성 중심 플레이어가 등장하여 Web2 개발자 유입 가시화. [[G-04]](#ref-g-04), [[G-16]](#ref-g-16)
- SkyPilot이 "에이전트에게 GPU 클러스터 접근 권한"을 부여하는 실제 사례를 공개하며, AI 에이전트 자체가 GPU 오케스트레이션 소비자가 되는 패러다임이 구체화되었다. 이는 기존 인간 MLOps 엔지니어 중심 워크플로우와 전혀 다른 API 설계·인증·비용 관리를 요구한다. [[G-02]](#ref-g-02)
- Kubernetes DRA(Dynamic Resource Allocation) GA 전환 흐름이 가속: AKS는 vGPU+DRA(2026-03-06)와 MIG+DRA(2026-03-03) 두 가지 GA를 3일 간격으로 연속 발표했다. 표준 API 기반 GPU 분할이 멀티테넌트 기업 환경의 기본값이 될 전망. [[G-05]](#ref-g-05), [[G-06]](#ref-g-06)
- CoreWeave HGX B300의 TTFT 4.93x 개선은 추론 지연에 민감한 에이전트 워크로드(실시간 tool-calling, multi-step reasoning)에 직접적 영향을 미치며, Neocloud가 단순 학습 공급자를 넘어 추론 인프라 공급자로 포지셔닝을 전환하고 있음을 시사한다. [[G-11]](#ref-g-11)
- ASPLOS '26(2026-03-22~26 Pittsburgh)에서 GFS(GPU 클러스터 선점 인식 스케줄링·스팟 인스턴스 관리) 논문 발표. 학계도 LLM 추론을 위한 스팟 인스턴스 활용 최적화에 집중하는 시점. [[G-17]](#ref-g-17)

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| GFS: A Preemption-aware Scheduling Framework for GPU Clusters (ASPLOS '26, 2026-03) | LLM 클러스터에서 스팟 인스턴스 예측 관리 + 선점 인식 스케줄링. 리소스 비용 절감과 SLO 준수를 동시에 달성하는 프레임워크 | [[P-01]](#ref-p-01) |
| MSched: GPU Multitasking via Proactive Memory Scheduling (arXiv, 2025-12) | GPU 하드웨어 동기화 프리미티브(GPU tracker·events)를 활용해 CPU 개입 없는 파이프라인 의존성 오케스트레이션 구현. 멀티태스킹 GPU 활용률 향상 | [[P-02]](#ref-p-02) |
| Hybrid Cloud Architectures for Research Computing (arXiv:2601.04349, 2026-01) | Kubernetes API 투명 인터셉트 + 멀티클러스터 라우팅 Admission Controller로 페더레이티드 GPU 워크로드 스케줄링 구현. 연구 컴퓨팅 환경의 하이브리드 오케스트레이션 모델 | [[P-03]](#ref-p-03) |
| Algorithmic Techniques for GPU Scheduling: A Comprehensive Survey (MDPI Algorithms, 2025-05) | GPU 스케줄링 알고리즘 체계적 분류: 그리디·DP·수학적 프로그래밍·ML 기법. LLM 추론 시대 스케줄링 평가 지표 재정의 | [[P-04]](#ref-p-04) |

---

## 전략적 시사점

**기회**

- **에이전트 주도 GPU 오케스트레이션 조기 내재화**: SkyPilot + Claude Code 조합의 "자율 실험 에이전트"가 실증 단계에 진입했다. AI 연구·개발 조직이 GPU 클러스터에 에이전트 접근 권한을 부여하는 표준 패턴이 자리잡기 전에, 내부 MLOps 팀이 인증·비용 제어·정책 프레임워크를 선제적으로 설계해야 한다.
- **DRA 기반 GPU 공유로 중소 워크로드 비용 최적화**: Kubernetes DRA + vGPU/MIG가 GA 수준으로 안정화됐다. 멀티테넌트 추론 환경에서 단일 GPU를 분할하여 fine-tuning·임베딩·소형 LLM 서빙을 동시 실행하는 아키텍처가 경제적으로 타당해졌다.
- **Neocloud 공급망 다변화**: CoreWeave HGX B300 + Lambda NVIDIA 클러스터 + Nebius Soperator 등 선택지가 성숙했다. SkyPilot 멀티클라우드 추상화를 통해 특정 Neocloud에 종속되지 않는 하이브리드 GPU 조달 전략이 실행 가능해졌다.

**위협**

- **하이퍼스케일러 Managed Ray Lock-in 위험**: AWS·Google·Azure 3사가 모두 Managed Ray 파트너십을 체결하면서, 오케스트레이션 레이어가 클라우드 에코시스템 종속의 새로운 진입점이 되고 있다. 벤더별 인증·스토리지·스케줄러 최적화가 이식성을 점차 제한할 가능성이 있다.
- **DePIN GPU 네트워크의 신뢰성·보안 미성숙**: Ocean Network 베타는 Pay-Per-Use Escrow와 Compute-to-Data 아키텍처로 신뢰 문제를 완화하려 하지만, 분산 노드의 가용성·SLA·보안 검증 체계는 여전히 미성숙하다. 기업 프로덕션 워크로드 적용 시 리스크 평가가 선행되어야 한다.
- **Vera Rubin 전환 시 오케스트레이션 재설계 부담**: NVIDIA Vera Rubin NVL72(2026 H2)는 아키텍처적으로 대역폭·인터커넥트 구조가 Blackwell과 다르다. 현재 최적화된 KV캐시 라우팅·P/D Disaggregation 파이프라인이 Rubin 전환 시 재검증이 필요할 수 있다.
- **에이전트 GPU 접근의 비용 폭주 리스크**: SkyPilot 실험에서 에이전트가 8시간 동안 910회 실험을 자율 제출했다. 비용 제한·할당량 거버넌스가 없는 환경에서 에이전트에게 GPU 접근 권한을 부여할 경우 예측 불가능한 클라우드 비용 급증이 발생할 수 있다.

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | SkyPilot Blog — Job Groups: Run RL on Heterogeneous Hardware | [링크](https://blog.skypilot.co/job-groups/) | blog | 2026-03-02 | [B] |
| <a id="ref-g-02"></a>G-02 | SkyPilot Blog — Scaling Karpathy's Autoresearch: What Happens When the Agent Gets a GPU Cluster | [링크](https://blog.skypilot.co/scaling-autoresearch/) | blog | 2026-03 | [B] |
| <a id="ref-g-03"></a>G-03 | GlobeNewswire — Ocean Network launches beta for affordable P2P GPU orchestration | [링크](https://www.globenewswire.com/news-release/2026/03/17/3257334/0/en/Ocean-Network-launches-beta-for-affordable-P2P-GPU-orchestration.html) | news | 2026-03-17 | [B] |
| <a id="ref-g-04"></a>G-04 | Chainwire — Ocean Network Launches Beta for Affordable P2P GPU Orchestration | [링크](https://chainwire.org/2026/03/16/ocean-network-launches-beta-for-affordable-p2p-gpu-orchestration/) | news | 2026-03-16 | [C] |
| <a id="ref-g-05"></a>G-05 | AKS Engineering Blog — DRA with vGPUs on AKS | [링크](https://blog.aks.azure.com/2026/03/06/dra-with-vGPUs-on-aks) | blog | 2026-03-06 | [A] |
| <a id="ref-g-06"></a>G-06 | AKS Engineering Blog — Multi-instance GPU with DRA on AKS | [링크](https://blog.aks.azure.com/2026/03/03/multi-instance-gpu-with-dra-on-aks) | blog | 2026-03-03 | [A] |
| <a id="ref-g-07"></a>G-07 | InfoQ — Running Ray at Scale on AKS | [링크](https://www.infoq.com/news/2026/03/ray-aks-ai-microsoft/) | news | 2026-03 | [B] |
| <a id="ref-g-08"></a>G-08 | NVIDIA Blog — GTC 2026 Live Updates on What's Next in AI | [링크](https://blogs.nvidia.com/blog/gtc-2026-news/) | news | 2026-03-16 | [A] |
| <a id="ref-g-09"></a>G-09 | Virtualization Review — NVIDIA, AWS and Google Cloud Spotlight AI Infrastructure Push at GTC 2026 | [링크](https://virtualizationreview.com/articles/2026/03/20/nvidia-aws-and-google-cloud-spotlight-ai-infrastructure-push-at-gtc-2026.aspx) | news | 2026-03-20 | [B] |
| <a id="ref-g-10"></a>G-10 | CoreWeave Press Release — CoreWeave Advances AI-Native Cloud Platform with NVIDIA HGX B300 | [링크](https://www.coreweave.com/news/coreweave-advances-ai-native-cloud-platform-for-the-next-phase-of-production-scale-ai) | news | 2026-03-17 | [A] |
| <a id="ref-g-11"></a>G-11 | CoreWeave Blog — Introducing NVIDIA HGX B300 on the Essential Cloud for AI | [링크](https://www.coreweave.com/blog/engineered-for-agentic-ai-nvidia-hgx-b300-on-coreweave-cloud) | blog | 2026-03 | [A] |
| <a id="ref-g-12"></a>G-12 | InfoQ — Microsoft Adds DRA-Backed NVIDIA vGPU Support to AKS | [링크](https://www.infoq.com/news/2026/03/microsoft-nvidia-gpu/) | news | 2026-03 | [B] |
| <a id="ref-g-13"></a>G-13 | Nebius — KubeCon 2026 (Soperator: Slurm on Kubernetes) | [링크](https://nebius.com/events/kube-con-2026) | blog | 2026-03-23 | [A] |
| <a id="ref-g-14"></a>G-14 | Cloud Computing News — Nvidia invests US$2 billion in AI cloud firm Nebius | [링크](https://www.cloudcomputing-news.net/news/nvidia-invests-us-2-billion-in-ai-cloud-firm-nebius/) | news | 2025 | [B] |
| <a id="ref-g-15"></a>G-15 | TechBuzz.ai — Lambda scores massive $1.5B funding after Microsoft deal | [링크](https://www.techbuzz.ai/articles/lambda-scores-massive-1-5b-funding-after-microsoft-deal) | news | 2026 | [B] |
| <a id="ref-g-16"></a>G-16 | BlockEden.xyz — Decentralized GPU Networks 2026: How DePIN is Challenging AWS for the $100B AI Compute Market | [링크](https://blockeden.xyz/blog/2026/02/07/decentralized-gpu-networks-2026/) | blog | 2026-02-07 | [C] |
| <a id="ref-g-17"></a>G-17 | arXiv — GFS: A Preemption-aware Scheduling Framework for GPU Clusters with Predictive Spot Instance Management (ASPLOS '26) | [링크](https://arxiv.org/html/2509.11134v1) | paper | 2026-03 | [A] |
| <a id="ref-g-18"></a>G-18 | CNBC — Nvidia GTC 2026: CEO Jensen Huang sees $1 trillion in orders for Blackwell and Vera Rubin through '27 | [링크](https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html) | news | 2026-03-16 | [B] |
| <a id="ref-g-19"></a>G-19 | CNBC — Nvidia GTC 2026: Agentic AI takes center stage | [링크](https://www.cnbc.com/2026/03/20/nvidia-gtc-2026-agentic-ai-chips-tech-download.html) | news | 2026-03-20 | [B] |
| <a id="ref-p-01"></a>P-01 | GFS — A Preemption-aware Scheduling Framework for GPU Clusters with Predictive Spot Instance Management | [링크](https://arxiv.org/html/2509.11134v1) | paper | 2026-03 | [A] |
| <a id="ref-p-02"></a>P-02 | MSched — GPU Multitasking via Proactive Memory Scheduling | [링크](https://arxiv.org/html/2512.24637v1) | paper | 2025-12 | [A] |
| <a id="ref-p-03"></a>P-03 | Hybrid Cloud Architectures for Research Computing (arXiv:2601.04349) | [링크](https://arxiv.org/html/2601.04349v1) | paper | 2026-01 | [A] |
| <a id="ref-p-04"></a>P-04 | Algorithmic Techniques for GPU Scheduling: A Comprehensive Survey (MDPI Algorithms) | [링크](https://www.mdpi.com/1999-4893/18/7/385) | paper | 2025-05 | [A] |
