---
type: weekly-monitor
domain: axops
week: 2026-W10
date: 2026-03-06
l3_count: 4
deep_count: 2
---

# 주간 기술 동향: AXOps (2026-W10)

## Executive Summary

| 세부기술 | 신호 | 핵심 내용 | 분석 |
|----------|------|----------|------|
| FeedBackOps Meta Prompt Eng. | 🟢 평온 | DSPy 생태계 안정적 발전, 신규 돌파 없음 | Quick |
| EvalOps KMS 성능평가 | 🟢 평온 | LLM-as-Judge 80-90% 인간 수준 합의, 플랫폼 성숙 중 | Quick |
| 학습 배포 통합 파이프라인 | 🟡 주목 | AgentOps 등장(MLOps 진화형), Policy-as-Code 트렌드, CoreWeave-W&B $1.7B 인수 | Deep |
| 하이브리드 GPU Orchestration | 🟡 주목 | LG MWC Trusted Orchestration + 파주 AIDC 12만장 GPU, NVIDIA Run:ai 2x 활용률, P/D Disaggregation 패러다임 | Deep |

---

## 🟢 Quick 요약 (변화 미미)

### FeedBackOps Meta Prompt Eng.

DSPy 프레임워크(Stanford NLP)가 프롬프트 자동 최적화 분야의 사실상 표준으로 안정화. MIPROv2(Bayesian Optimization), COPRO(Coordinate Ascent), SIMBA(Stochastic Mini-Batch) 등 옵티마이저가 운영 안정 단계. Meta prompt-ops(오픈소스), Microsoft PromptWizard(피드백 기반 자기진화), FIPO(Nature 발표, 피드백 통합 최적화) 등 연구가 지속되나 급격한 패러다임 전환 시그널은 미감지.

### EvalOps KMS 성능평가

LLM-as-Judge가 인간 평가자와 80-90% 합의 수준에 도달하며 실용 단계 진입. RAGAS가 reference-free faithfulness/relevance 메트릭을 도입하여 수동 큐레이션 부담을 90% 절감. Amazon Bedrock에서 RAG 평가 + LLM-as-Judge가 GA 전환. 5대 평가 플랫폼(Maxim AI, LangSmith, Arize Phoenix, Ragas, DeepEval)이 생태계를 형성하며 시장 성숙 단계. 2026년 2월 "Case-Aware LLM-as-Judge for Enterprise RAG"(arXiv) 논문이 엔터프라이즈 RAG 환경의 맞춤형 평가 방법론을 제시.

---

## 🟡 Deep 심층 분석

### 학습 배포 통합 파이프라인 — 🟡 주목

#### 기술 동향

**패러다임 진화: MLOps → LLMOps → AgentOps**

2026년 AI 운영 프레임워크는 세 계층의 병렬 성숙 구조를 형성하고 있다 [[G-01]](#ref-g-01).

- **MLOps (성숙)**: 피처 스토어, 모델 훈련/튜닝, CI/CD for models, 모니터링(드리프트·지연·정확도), 자동 재훈련 워크플로우. MLflow, TFX, SageMaker Pipelines 등 도구 안정화.
- **LLMOps (부상)**: "프롬프트는 새로운 코드지만 버전 관리되지 않는다"는 문제를 핵심으로, 프롬프트 버전 관리, RAG 파이프라인 오케스트레이션, LLM 특화 평가 프레임워크, 토큰 비용 최적화가 핵심 컴포넌트 [[G-02]](#ref-g-02).
- **AgentOps (초기)**: 자율 에이전트의 비결정론적 행동 특성으로 인해 전통 MLOps로는 관리 불가. 모니터링→이상탐지→근본원인분석→해결의 4단계 프레임워크 제시 [[G-03]](#ref-g-03).

**5대 최신 MLOps 기법 (2026)**

- **Policy-as-Code**: 공정성, 데이터 계보, 규제 준수를 CI/CD에 실행 가능한 코드로 자동 임베딩. EU AI Act, SOC2, GDPR 대응 [[G-04]](#ref-g-04), [[G-05]](#ref-g-05)
- **AgentOps**: LLM 기반 자율 에이전트 전용 운영 프레임워크
- **운영 설명가능성(XAI)**: 런타임 설명기를 MLOps 라이프사이클 전반에 통합
- **분산 MLOps**: 엣지·TinyML·연합 학습 파이프라인으로 프라이버시·지연 요구사항 대응
- **Green MLOps**: 에너지 메트릭, 탄소 추적, 효율 KPI를 운영 체계에 통합 [[G-06]](#ref-g-06)

**MLflow 3.0 출시 (2025년 중반)**

GenAI 특화 기능 대폭 강화 [[E-01]](#ref-e-01): 계층적 트레이싱, LLM Judge 기반 평가, 피드백 수집 API, 애플리케이션 버전 관리(프롬프트·RAG·오케스트레이션 코드를 원자적 아티팩트로 관리). AWS SageMaker에 완전 관리형으로 제공 중 [[E-03]](#ref-e-03).

**오픈소스 업데이트**

- **KServe**: HuggingFace Transformer v4.51.0, vLLM V1 지원, OpenAI 프로토콜 호환 [[G-07]](#ref-g-07)
- **Kubeflow 1.9**: Ray, Seldon, BentoML, KServe 통합 강화, LLM GPU 최적화

#### 플레이어 동향

**주요 플레이어 테이블**

| 기업 | 동향 | 출처 |
|------|------|------|
| CoreWeave | W&B를 $1.7B에 인수(2025-05). 컴퓨트+AI 개발자 플랫폼 수직 통합 | [[E-02]](#ref-e-02) |
| Databricks | MLflow 3.0 출시. ISG 2025 Buyers Guide 4개 카테고리 Leader | [[E-01]](#ref-e-01), [[G-09]](#ref-g-09) |
| Oracle | ISG 2025 ML/LLM Operations 전체 1위. 7개 카테고리 전부 Leader | [[G-09]](#ref-g-09) |
| AWS | SageMaker AI에 MLflow 3.0 완전 관리형 제공(2025-07) | [[E-03]](#ref-e-03) |
| Google Cloud | ISG 3개 카테고리 Leader. AI 특허 세계 1위(1,837건) | [[G-09]](#ref-g-09), [[G-10]](#ref-g-10) |
| W&B (AgentOps) | 1,400+ 기업 고객. AgentOps SDK: 400+ LLM 추적, 파인튜닝 비용 25배 절감 주장 | [[G-08]](#ref-g-08) |

#### 시장 시그널

- MLOps 시장 2026년 $3~5B, CAGR 37~42% (기관별 편차 큼) [[G-11]](#ref-g-11)
- 2024년 MLOps 투자 $4.5B, 2026년 $7~8B 예상 [[G-12]](#ref-g-12)
- Gartner: AI 에이전트 플랫폼 기업 관심 1,445% 급증 [[G-13]](#ref-g-13)
- 85%의 ML 모델이 프로덕션 미도달 — 이 격차 해소가 시장 성장 핵심 동인
- **핵심 딜**: CoreWeave → W&B $1.7B (2025-05), Databricks → Tecton 통합 발표(2025) [[E-02]](#ref-e-02)

#### 학술 동향 (주요 논문)

**주요 논문 테이블**

| 논문 | 핵심 | 출처 |
|------|------|------|
| A Survey on AgentOps (Wang et al., 2025) | AgentOps 최초 종합 조사. intra/inter-agent 이상 분류, 4단계 프레임워크 | [[P-01]](#ref-p-01) |
| Navigating MLOps (Stone et al., 2025) | 9단계 통합 MLOps 라이프사이클, 5개 성숙도 모델 비교, 50개 도구 정리 | [[P-02]](#ref-p-02) |
| Transitioning from MLOps to LLMOps (MDPI, 2025) | MLOps↔LLMOps 구조적 차이 규명, GPU/TPU 의존성, RLHF 요건 분석 | [[P-03]](#ref-p-03) |
| Green MLOps to Green GenOps (MDPI, 2025) | 판별형 AI vs 생성형 AI 에너지 소비 실증 비교 | [[P-06]](#ref-p-06) |

#### 전략적 시사점

**기회**
- Policy-as-Code 기반 자동 규제 준수(EU AI Act, GDPR)를 CI/CD에 내재화하면 속도와 안전성 동시 확보 가능
- AgentOps 도구 생태계 초기 단계 — 조기 도입 시 표준화 주도권 확보 가능
- CoreWeave-W&B "컴퓨트+관측성" 수직 통합이 새 경쟁 공식 제시. 유사 번들링 전략 후발 적용 가능
- Green MLOps는 탄소 중립 목표 기업에서 MLOps 도입 정당화 신규 비즈니스 케이스

**위협**
- 클라우드 빅3의 수직 통합 심화 → 독립 MLOps 벤더 생존 공간 축소
- AgentOps 성숙도 부족: 비결정론적 행동의 프로덕션 디버깅 난이도 여전히 높음
- MLOps, LLMOps, AgentOps 도구 스택 병렬 증식 → 통합 전까지 기술 부채 축적 위험
- LLM 추론 비용이 전통 ML 대비 최대 100배 — 비용 최적화 없이는 프로덕션 확장 불가

---

### 하이브리드 GPU Orchestration — 🟡 주목

#### 기술 동향

**오케스트레이션 레이어 성숙: 스케줄링 → 인퍼런스 서빙 최적화**

GPU 오케스트레이션이 단순 스케줄링을 넘어 인퍼런스 서빙 최적화로 중심축 이동. Kubernetes DRA가 v1.35에서 stable 승격·기본 활성화되어 GPU를 first-class 스케줄링 자원으로 처리하는 기반 완성 [[G-06b]](#ref-g-06b). 그러나 well-run 클러스터도 GPU 평균 활용률 20~30% 문제 지속 [[G-05b]](#ref-g-05b).

**P/D Disaggregation (Prefill-Decode 분리) 패러다임**

2025~2026년 인퍼런스 핵심 혁신. Prefill(프롬프트 처리)과 Decode(토큰 생성)를 물리적으로 분리하여 독립 최적화 [[G-07b]](#ref-g-07b). NVIDIA Dynamo가 이를 프로덕션 스케일로 구현한 오픈소스 프레임워크로, KV캐시 인식 라우터·GPU Resource Planner를 포함하며 DeepSeek-R1 기준 **처리량 30배 향상** 달성 [[G-08b]](#ref-g-08b).

**vLLM 생태계 심화**

- **LMCache**: KV 캐시 GPU 외부 오프로드·엔진 간 공유. P/D 분리 지원 [[G-13b]](#ref-g-13b)
- **vLLM AMD ROCm 지원**: 2026-02 AMD ROCm 전용 어텐션 백엔드 최적화 공개 [[G-14b]](#ref-g-14b)
- **llm-d (Red Hat)**: KV캐시 인식 라우팅 분산 스케줄링 프레임워크 [[G-13b]](#ref-g-13b)

**Kthena: Kubernetes-Native 인퍼런스 오케스트레이션**

Volcano 커뮤니티가 2026-01 CNCF 통해 공개. vLLM·SGLang·Triton·TorchServe 지원, KV캐시 인식 라우팅, P/D 분리, 토폴로지 인식 스케줄링 내장 [[G-11b]](#ref-g-11b).

**NVIDIA KAI Scheduler + Ray 통합**

KubeRay에 네이티브 통합 — Gang Scheduling·우선순위 큐·워크로드 선점 기능 제공. 학습과 인퍼런스가 동일 GPU 풀 공유하는 멀티워크로드 환경 효율화 [[G-10b]](#ref-g-10b).

**AMD ROCm 7.0 + SkyPilot 멀티클라우드**

AMD ROCm 7.0이 엔터프라이즈급 클러스터 관리 도구를 포함하며 SkyPilot 통합으로 CUDA 워크로드의 AMD Instinct MI300X 이전 경로 제공. 20개+ 클라우드를 단일 YAML로 추상화 [[G-12b]](#ref-g-12b).

#### 플레이어 동향

**주요 플레이어 테이블**

| 기업 | 동향 | 출처 |
|------|------|------|
| NVIDIA | Run:ai v2.24 — GPU 활용률 2x, TTFT 44~61x 개선. Dynamo 오픈소스(P/D, 처리량 30x). KAI Scheduler→Ray 통합 | [[G-01b]](#ref-g-01b), [[G-08b]](#ref-g-08b), [[G-10b]](#ref-g-10b) |
| NVIDIA (AI-RAN) | Nokia와 Grace Hopper 200에서 AI+RAN 동시 처리 실증. 2026 시험, 2027 상용 출시 | [[G-15b]](#ref-g-15b) |
| Samsung | MWC 2026: NVIDIA Aerial 기반 AI-RAN 멀티셀 검증. GPU Lock-In 탈피 CPU 옵션도 검증 | [[G-17b]](#ref-g-17b) |
| Nokia | MWC 2026: SMO rApp 마켓플레이스 출시. BT·Elisa·NTT DoCoMo·Vodafone과 AI-RAN 배포 | [[G-15b]](#ref-g-15b) |
| LG (LG U+/AI Research) | K-엑사원 4대 핵심 중 "Trusted Orchestration" — Planning·Execution·Evaluation·Review AI 협업 조율. 파주 AIDC GPU 12만장·200MW·2027 준공 | [[N-01b]](#ref-n-01b), [[N-02b]](#ref-n-02b) |
| CoreWeave | IPO 후 NVIDIA $20억 추가 투자. Rubin 플랫폼 최초 배포 클라우드(2026 H2). 2026 매출 $120억(YoY +134%) | [[G-18b]](#ref-g-18b) |
| SkyPilot | v0.11: 멀티클라우드 풀, CoreWeave 공식 지원(InfiniBand), AMD ROCm 7.0+Ray 통합 | [[G-03b]](#ref-g-03b) |
| Google | Ironwood TPU(7세대, 인퍼런스 특화 FP8 네이티브). Anthropic에 Trillium TPU 수십만 개 계약 | [[G-21b]](#ref-g-21b) |

#### 시장 시그널

- GPU-as-a-Service: 2026년 **$73.4억** → 2031년 **$259.4억** (CAGR 28.7%) [[G-22b]](#ref-g-22b)
- 멀티/하이브리드 클라우드 세그먼트 CAGR 29.4%로 최고 성장 — 오케스트레이션 S/W가 핵심 드라이버
- AI 데이터센터 GPU 시장: 2026년 $128.3억 → 2035년 $771.5억 (CAGR 22.1%) [[G-23b]](#ref-g-23b)
- 인퍼런스 세그먼트가 시장 최대 점유 — 실시간 AI 앱 수요 주도
- **핵심 딜**: CoreWeave — NVIDIA $20억 투자, Meta $142억 계약, OpenAI $224억 계약, Perplexity GB200 전용 클러스터(2026-03-04) [[G-18b]](#ref-g-18b)
- **LG 파주 AIDC**: GPU 12만장·200MW·2027 준공. "One Team LG" 전략 [[N-01b]](#ref-n-01b)

#### 학술 동향 (주요 논문)

**주요 논문 테이블**

| 논문 | 핵심 | 출처 |
|------|------|------|
| Nexus: Proactive Intra-GPU Disaggregation (2025) | 단일 GPU 내 P/D 분리, SM 동적 재할당 | [[P-01b]](#ref-p-01b) |
| RAPID-Serve (2026-01) | 동일 GPU P/D 동시 실행, Adaptive Resource Mgmt | [[P-02b]](#ref-p-02b) |
| FlowPrefill (2026-02) | 연산자 레벨 Fine-grained Preemption, 멀티-SLO 최적화 | [[P-03b]](#ref-p-03b) |
| Disaggregated P/D for Multi-Vendor GPUs (2025-09) | 이종 GPU 환경 P/D 분리 인퍼런스 | [[P-04b]](#ref-p-04b) |
| HeteroScale (2025-08) | 토폴로지 인식 오토스케일러, P/D 풀 공동 스케일링 | [[P-05b]](#ref-p-05b) |
| Disaggregated Multi-Stage MLLM (2025-12) | 멀티모달 LLM 3단계(비전·프리필·디코딩) 분리 파이프라인 | [[P-06b]](#ref-p-06b) |
| Token Management in Multi-Tenant (2026-03) | 멀티테넌트 인퍼런스 플랫폼 토큰 관리 최적화 | [[P-07b]](#ref-p-07b) |

#### 전략적 시사점

**기회**
- GPU 평균 활용률 20~30% 문제 → 오케스트레이션 솔루션의 명확한 ROI. Run:ai 벤치마크(2x)가 비즈니스 케이스 실증
- P/D Disaggregation + KV캐시 라우팅은 동일 GPU 투자로 처리량 수배 향상하는 검증된 아키텍처. Dynamo(오픈소스)·Kthena(CNCF)로 즉시 채택 가능
- SkyPilot + AMD ROCm 7.0 → NVIDIA 종속 해소 실용적 경로. 네오클라우드 활용 비용 절감
- 통신 AI-RAN에서 GPU 오케스트레이션 수요 신규 창출 — Nokia·Samsung MWC 2026 상용화 타임라인 확정

**위협**
- NVIDIA 수직 통합(H/W → Run:ai → Dynamo → NIM) 심화로 단일 벤더 의존 고착화 위험
- GPU 공급 병목 지속 — CoreWeave $300억+ 백로그, Anthropic TPU 선점 사례
- 오픈소스 분열(vLLM·SGLang·Triton·Dynamo·Kthena 등) — 표준 미확립으로 기술 선택 복잡도 상승
- LG 파주 AIDC 2027 준공 예정 — 국내 GPU 인프라가 글로벌 대비 1~2년 지연

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **MLOps↔GPU Orchestration 수렴**: MLOps의 AgentOps 진화와 GPU Orchestration의 인퍼런스 최적화가 동일한 문제("복합 AI 시스템의 효율적 프로덕션 배포")를 양쪽에서 접근 중. CoreWeave-W&B 인수($1.7B)가 이 수렴을 상징하는 대표 사례.

2. **P/D Disaggregation이 전 스택에 파급**: GPU 레벨의 P/D 분리(Dynamo, Kthena)가 상위 MLOps/LLMOps 파이프라인의 서빙 아키텍처를 근본적으로 재설계 요구. 기존 단일 모델 엔드포인트 기반 배포 파이프라인이 분산 인퍼런스 파이프라인으로 전환.

3. **통신 인프라의 GPU 수요 신규 창출**: Nokia·Samsung의 AI-RAN 상용화(2026 시험, 2027 출시)와 LG 파주 AIDC(GPU 12만장)가 통신+AI 인프라 융합을 가속. GPU Orchestration이 데이터센터를 넘어 네트워크 인프라로 확장되는 시그널.

4. **Green MLOps와 GPU 효율화의 교차점**: IEA 예측(데이터센터 전력 수요 2배 증가)과 GPU 활용률 20~30% 문제가 만나는 지점에서, 탄소 인식 스케줄링 + GPU fractional 할당이 비용과 지속가능성을 동시에 해결하는 경로로 부상.

### 후속 조치 제안

- LG 파주 AIDC Trusted Orchestration 전략의 L2 기술별 영향도 분석 필요 시 → `/wtis standard` 검증 제안
- 다음 주 모니터링: NVIDIA GTC 2026 발표 내용 (Dynamo/Run:ai 업데이트 예상)

---

## References

### MLOps Pipeline 출처

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Covasant — MLOps, LLMOps, & AgentOps Guide | [링크](https://www.covasant.com/blogs/mlops-llmops-agentops-the-essential-ai-pipeline-guide) | 업계 블로그 | 2025~2026 | [B] |
| <a id="ref-g-02"></a>G-02 | Medium/CodeX — MLOps in 2026: From MLflow to LLMOps | [링크](https://medium.com/codex/mlops-in-2026-from-mlflow-to-llmops-the-complete-guide-to-shipping-ai-in-production-0024955b70c4) | 블로그 | 2026-02 | [C] |
| <a id="ref-g-03"></a>G-03 | XenonStack — AgentOps: Next Evolution in AI Lifecycle | [링크](https://www.xenonstack.com/blog/agentops-ai) | 업계 블로그 | 2025~2026 | [B] |
| <a id="ref-g-04"></a>G-04 | KDnuggets — 5 Cutting-Edge MLOps Techniques 2026 | [링크](https://www.kdnuggets.com/5-cutting-edge-mlops-techniques-to-watch-in-2026) | 전문 미디어 | 2025~2026 | [B] |
| <a id="ref-g-05"></a>G-05 | TechTarget — MLOps Governance Strategies | [링크](https://www.techtarget.com/searchenterpriseai/tip/Understand-key-MLOps-governance-strategies) | 전문 미디어 | 2025~2026 | [B] |
| <a id="ref-g-06"></a>G-06 | DevOps.com — MLOps for Green AI | [링크](https://devops.com/mlops-for-green-ai-building-sustainable-machine-learning-in-the-cloud/) | 전문 미디어 | 2025 | [B] |
| <a id="ref-g-07"></a>G-07 | KServe GitHub Releases | [링크](https://github.com/kserve/kserve/releases) | 오픈소스 공식 | 2025 | [A] |
| <a id="ref-g-08"></a>G-08 | Softcery — 8 AI Observability Platforms Compared | [링크](https://softcery.com/lab/top-8-observability-platforms-for-ai-agents-in-2025) | 업계 분석 | 2025 | [B] |
| <a id="ref-g-09"></a>G-09 | ISG — ML/LLM Operations 2025 Buyers Guide | [링크](https://research.isg-one.com/buyers-guide/artificial-intelligence/generative-ai/machine-learning-and-large-language-model-operations/2025) | 애널리스트 | 2025 | [A] |
| <a id="ref-g-10"></a>G-10 | Axios — Google Dominates AI Patent Applications | [링크](https://www.axios.com/2025/05/15/ai-patents-google-agents) | 주요 언론 | 2025-05 | [B] |
| <a id="ref-g-11"></a>G-11 | Precedence Research — MLOps Market Size | [링크](https://www.precedenceresearch.com/mlops-market) | 시장조사 | 2025~2026 | [C] |
| <a id="ref-g-12"></a>G-12 | Quick Market Pitch — MLOps Platforms Funded (July 2025) | [링크](https://quickmarketpitch.com/blogs/news/mlops-funding) | 업계 분석 | 2025-07 | [C] |
| <a id="ref-g-13"></a>G-13 | Getmaxim.ai — Top 5 AI Agent Observability 2026 | [링크](https://www.getmaxim.ai/articles/top-5-ai-agent-observability-platforms-in-2026/) | 업계 블로그 | 2026 | [C] |
| <a id="ref-g-14"></a>G-14 | Conf42 MLOps 2026 | [링크](https://www.conf42.com/mlops2026) | 컨퍼런스 | 2026 | [B] |
| <a id="ref-e-01"></a>E-01 | Databricks — MLflow 3.0 | [링크](https://www.databricks.com/blog/mlflow-30-unified-ai-experimentation-observability-and-governance) | 기업 공식 | 2025 | [A] |
| <a id="ref-e-02"></a>E-02 | CoreWeave IR — W&B Acquisition Complete | [링크](https://investors.coreweave.com/news/news-details/2025/CoreWeave-Completes-Acquisition-of-Weights--Biases/default.aspx) | 공식 IR | 2025-05-05 | [A] |
| <a id="ref-e-03"></a>E-03 | AWS — MLflow 3.0 on SageMaker AI | [링크](https://aws.amazon.com/about-aws/whats-new/2025/07/fully-managed-mlflow-3-0-amazon-sagemaker-ai/) | 공식 발표 | 2025-07 | [A] |
| <a id="ref-p-01"></a>P-01 | Wang et al. — A Survey on AgentOps | [arXiv:2508.02121](https://arxiv.org/abs/2508.02121) | 학술 논문 | 2025-08 | [A] |
| <a id="ref-p-02"></a>P-02 | Stone et al. — Navigating MLOps | [arXiv:2503.15577](https://arxiv.org/html/2503.15577v1) | 학술 논문 | 2025-03 | [A] |
| <a id="ref-p-03"></a>P-03 | MDPI — Transitioning from MLOps to LLMOps | [링크](https://www.mdpi.com/2078-2489/16/2/87) | 동료 심사 | 2025-01 | [A] |
| <a id="ref-p-04"></a>P-04 | Joshi — LLMOps, AgentOps, and MLOps Review | [ResearchGate](https://www.researchgate.net/publication/393122731) | 학술 리뷰 | 2025 | [B] |
| <a id="ref-p-05"></a>P-05 | Chernigovskaya et al. — Standardized LLMOps Process Model | [링크](https://www.scitepress.org/Papers/2025/133777/133777.pdf) | 컨퍼런스 논문 | 2025 | [A] |
| <a id="ref-p-06"></a>P-06 | MDPI — Green MLOps to Green GenOps | [링크](https://www.mdpi.com/2078-2489/16/4/281) | 동료 심사 | 2025 | [A] |

### GPU Orchestration 출처

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01b"></a>G-01b | NVIDIA — Maximizing GPU Utilization with Run:ai and NIM | [링크](https://developer.nvidia.com/blog/maximizing-gpu-utilization-with-nvidia-runai-and-nvidia-nim/) | 공식 블로그 | 2026-02 | [A] |
| <a id="ref-g-02b"></a>G-02b | NVIDIA — GPU Fractioning: 77% Throughput at Half Allocation | [링크](https://developer.nvidia.com/blog/unlock-massive-token-throughput-with-gpu-fractioning-in-nvidia-runai/) | 공식 블로그 | 2026-02 | [A] |
| <a id="ref-g-03b"></a>G-03b | CoreWeave — SkyPilot Multi-Cloud Orchestration | [링크](https://www.coreweave.com/blog/coreweave-adds-skypilot-support-for-effortless-multi-cloud-ai-orchestration) | 기업 블로그 | 2026 | [B] |
| <a id="ref-g-05b"></a>G-05b | ScaleOps — Kubernetes GPU Resource Management | [링크](https://scaleops.com/blog/ai-infra-for-production-why-gpu-resource-management-in-kubernetes-demands-a-new-approach/) | 전문 블로그 | 2026 | [B] |
| <a id="ref-g-06b"></a>G-06b | AceCloud — Multi GPU Orchestration in K8s 2026 | [링크](https://acecloud.ai/blog/multi-gpu-orchestration-kubernetes/) | 전문 블로그 | 2026 | [B] |
| <a id="ref-g-07b"></a>G-07b | vLLM Docs — Disaggregated Prefilling | [링크](https://docs.vllm.ai/en/latest/features/disagg_prefill/) | 공식 문서 | 2026 | [A] |
| <a id="ref-g-08b"></a>G-08b | NVIDIA — Introducing Dynamo Distributed Inference | [링크](https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/) | 공식 블로그 | 2025 | [A] |
| <a id="ref-g-10b"></a>G-10b | NVIDIA — Gang Scheduling in Ray with KAI Scheduler | [링크](https://developer.nvidia.com/blog/enable-gang-scheduling-and-workload-prioritization-in-ray-with-nvidia-kai-scheduler) | 공식 블로그 | 2026 | [A] |
| <a id="ref-g-11b"></a>G-11b | CNCF — Introducing Kthena | [링크](https://www.cncf.io/blog/2026/01/28/introducing-kthena-llm-inference-for-the-cloud-native-era/) | CNCF 공식 | 2026-01-28 | [A] |
| <a id="ref-g-12b"></a>G-12b | AMD ROCm — Autoscaling with Ray, ROCm 7.0, SkyPilot | [링크](https://rocm.blogs.amd.com/ecosystems-and-partners/ray-rocm7/README.html) | 공식 블로그 | 2026 | [A] |
| <a id="ref-g-13b"></a>G-13b | llm-d.ai — KV-Cache Wins | [링크](https://llm-d.ai/blog/kvcache-wins-you-can-see) | 공식 블로그 | 2026 | [B] |
| <a id="ref-g-14b"></a>G-14b | vLLM — High-Performance Inference on AMD ROCm | [링크](https://blog.vllm.ai/2026/02/27/rocm-attention-backend.html) | 공식 블로그 | 2026-02-27 | [A] |
| <a id="ref-g-15b"></a>G-15b | Nokia — AI-RAN Momentum #MWC26 | [링크](https://www.nokia.com/newsroom/nokia-accelerates-ai-ran-momentum-with-new-partnerships-driving-path-to-ai-native-6g-mwc26/) | 공식 보도자료 | 2026-03-01 | [A] |
| <a id="ref-g-17b"></a>G-17b | The Meridiem — Samsung AI-RAN Breaks GPU Lock-In | [링크](https://www.themeridiem.com/ai/2026/3/2/samsung-s-ai-ran-validation-breaks-gpu-lock-in-as-operators-choose-cpus) | 전문 언론 | 2026-03-02 | [B] |
| <a id="ref-g-18b"></a>G-18b | CoreWeave IR — Extends Cloud with NVIDIA Rubin | [링크](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Extends-Its-Cloud-Platform-with-NVIDIA-Rubin-Platform/default.aspx) | 공식 IR | 2026 | [A] |
| <a id="ref-g-20b"></a>G-20b | GlobeNewswire — VAST Data Polaris | [링크](https://www.globenewswire.com/news-release/2026/02/25/3244908/0/en/VAST-Data-Introduces-Polaris-to-Orchestrate-Globally-Distributed-AI-Data-Infrastructure-Across-Hybrid-Multicloud-Environments.html) | 공식 보도자료 | 2026-02-25 | [A] |
| <a id="ref-g-21b"></a>G-21b | Google — Ironwood TPU for the Age of Inference | [링크](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/) | 공식 블로그 | 2026 | [A] |
| <a id="ref-g-22b"></a>G-22b | Mordor Intelligence — GPU as a Service Market 2026-2031 | [링크](https://www.mordorintelligence.com/industry-reports/gpu-as-a-service-market) | 시장조사 | 2026 | [B] |
| <a id="ref-g-23b"></a>G-23b | Precedence Research — AI Data Center GPU Market | [링크](https://www.precedenceresearch.com/ai-data-center-gpu-market) | 시장조사 | 2026 | [B] |
| <a id="ref-n-01b"></a>N-01b | 인사이트코리아 — LGU+ 파주 GPU 12만장 DC | [링크](https://www.insightkorea.co.kr/news/articleView.html?idxno=242033) | 한국 언론 | 2026-03 | [B] |
| <a id="ref-n-02b"></a>N-02b | 아주경제 — LG그룹 파주 AIDC 2027 준공 | [링크](https://www.ajunews.com/view/20260302010905149) | 한국 언론 | 2026-03-02 | [B] |
| <a id="ref-n-03b"></a>N-03b | 전자신문 — 정숙경 LG유플러스 파주 AIDC 전략 | [링크](https://www.etnews.com/20260305000231) | 한국 언론 | 2026-03-05 | [B] |
| <a id="ref-p-01b"></a>P-01b | Nexus: Proactive Intra-GPU P/D Disaggregation | [arXiv:2507.06608](https://arxiv.org/abs/2507.06608) | 학술 논문 | 2025 | [A] |
| <a id="ref-p-02b"></a>P-02b | RAPID-Serve: P/D Intra-GPU Disaggregation | [arXiv:2601.11822](https://arxiv.org/abs/2601.11822) | 학술 논문 | 2026-01 | [A] |
| <a id="ref-p-03b"></a>P-03b | FlowPrefill: Decoupling Preemption from Prefill | [arXiv:2602.16603](https://arxiv.org/html/2602.16603) | 학술 논문 | 2026-02 | [A] |
| <a id="ref-p-04b"></a>P-04b | Disaggregated P/D for Multi-Vendor GPUs | [arXiv:2509.17542](https://arxiv.org/abs/2509.17542) | 학술 논문 | 2025-09 | [A] |
| <a id="ref-p-05b"></a>P-05b | HeteroScale: Coordinated Autoscaling for Disaggregated LLM | [arXiv:2508.19559](https://arxiv.org/abs/2508.19559) | 학술 논문 | 2025-08 | [A] |
| <a id="ref-p-06b"></a>P-06b | Disaggregated Multi-Stage MLLM Inference | [arXiv:2512.17574](https://arxiv.org/abs/2512.17574) | 학술 논문 | 2025-12 | [A] |
| <a id="ref-p-07b"></a>P-07b | Token Management in Multi-Tenant AI Inference | [arXiv:2603.00356](https://arxiv.org/abs/2603.00356) | 학술 논문 | 2026-03 | [A] |
