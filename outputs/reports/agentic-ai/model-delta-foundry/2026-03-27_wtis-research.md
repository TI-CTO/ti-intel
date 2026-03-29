---
topic: Model & Delta Foundry
domain: agentic-ai
l2_topic: model-delta-foundry
date: 2026-03-27
type: wtis-research
agent: research-deep
confidence: medium
status: completed
sources_used: [websearch]
---

# Research: Model & Delta Foundry

## Executive Summary

> Model & Delta Foundry는 자동 프롬프트 최적화(FeedbackOps/Prompt), LLM 평가 자동화(EvalOps/KMS), MLOps 파이프라인, GPU 오케스트레이션 등 4개 L3를 포괄하는 기술군이다. MLOps/LLMOps 글로벌 시장은 2025년 약 $2.2~3.2B에서 2030년대 초 $25~35B 규모로 고성장이 예측된다(CAGR 28~42%). NVIDIA의 Run:ai 인수($700M)와 CoreWeave의 W&B 인수($1.7B)는 GPU 오케스트레이션과 MLOps 툴체인이 인프라 레이어로 통합되는 구조적 전환을 명확히 보여준다. SKT는 Haein GPU 클러스터(1,000+ NVIDIA Blackwell) 기반 GPUaaS를 상용화하여 AI DC 매출 $354M(YoY +35%)을 달성했으나, KT는 Microsoft Azure AI와의 파트너십에 의존하는 전략 차이가 확인된다. 통신사 관점에서 내부 AI 모델 운영 효율화(프롬프트 최적화, 평가 자동화)와 GPUaaS B2B 서비스는 단기 수익화 가능한 적용 영역으로 판단되나, 하이퍼스케일러 대비 GPU 가동률(목표 60~70%+) 확보가 핵심 과제다.

---

## 연구 질문

Model & Delta Foundry 기술군(자동 프롬프트 최적화, LLM 평가 자동화, MLOps 파이프라인, GPU 오케스트레이션)의 글로벌 시장 규모와 성장성, 주요 플레이어 전략, 투자/M&A 트렌드, 그리고 국내 통신사(SKT/KT) 및 글로벌 통신사의 적용 현황을 파악한다.

---

## 1. 시장 분석

### 1.1 MLOps / LLMOps 글로벌 TAM

**MLOps 시장 규모 (복수 출처 교차 검증)**

다수의 시장 리서치 기관이 2025~2030년 MLOps 시장을 고성장 구간으로 전망하며, 수치는 기관별 정의 차이로 편차가 크다.

- Fortune Business Insights: 2025년 $2.33B → 2026년 $4.38B [[G-01]](#ref-g-01)
- MarketsandMarkets (2023 보고서): 2027년 $5.9B, CAGR 41.0% [[G-02]](#ref-g-02)
- Straits Research: 2025년 $2.23B → 2033년 $35.4B, CAGR 41.3% [[G-03]](#ref-g-03)
- Business Research Insights: 2025년 $3.18B → 2035년 $73.7B, CAGR 41.8% [[G-04]](#ref-g-04)
- GM Insights: 2025~2034년 기간 CAGR 28.9% [[G-05]](#ref-g-05)

> 기관별 수치 편차가 크므로 보수적 추정(CAGR ~30%)과 낙관적 추정(CAGR ~42%)의 중간값으로 판단 필요. 공통적으로 강한 성장 방향성은 일치 [B].

**LLMOps 소프트웨어 시장**

- Valuates Reports: 2025년 $5.2B → 2032년 $19.8B, CAGR 21.3% [[G-06]](#ref-g-06)
- MLOps와 LLMOps 시장의 경계는 흐려지고 있으며, 2026년 이후 통합 플랫폼(MLflow 3.0, Databricks Mosaic AI) 중심으로 수렴 중 [[G-07]](#ref-g-07)

### 1.2 GPU 클라우드 / 추론 최적화 시장

**GPU as a Service (GPUaaS) 시장**

- MarketsandMarkets: 2025년 $8.2B → 2030년 $26.6B, CAGR 26.5% [[G-08]](#ref-g-08)
- Fortune Business Insights: 2026년 $7.34B (전년 $5.70B) [[G-09]](#ref-g-09)

**AI 추론(Inference) 시장**

- MarketsandMarkets: 2026년 $50B 초과 예상 — 처음으로 학습(Training) 시장 규모를 추월 전망 [[G-10]](#ref-g-10)
- 추론 세그먼트가 전체 AI 컴퓨팅의 약 67% 차지(2026년 기준) [[G-10]](#ref-g-10)
- AI Data Center GPU 시장: 2025년 $10.5B → 2035년 $77.2B (Precedence Research) [[G-11]](#ref-g-11)

### 1.3 주요 성장 드라이버 및 억제 요인

**성장 드라이버**
- 엔터프라이즈 AI 프로덕션 전환 가속: 생산 AI 사용 사례 비율이 2024년 대비 2025년 31%로 2배 증가 [[G-12]](#ref-g-12)
- 에이전틱 AI(Agentic AI) 확산 — MLOps의 범위가 LLM 파인튜닝, RAG 파이프라인, 에이전트 오케스트레이션으로 확장 [[G-13]](#ref-g-13)
- GenAI 특화 클라우드 서비스 2025년 Q2 기준 YoY 140~180% 성장 [[G-12]](#ref-g-12)
- GPU 대안 클라우드(Lambda, CoreWeave 등)의 하이퍼스케일러 대비 50~70% 비용 절감 [[G-14]](#ref-g-14)

**억제 요인**
- 통신사 등 분산형 GPU 클러스터의 가동률 60~70% 이상 달성 난이도 (Utilization Trap) [[G-15]](#ref-g-15)
- 기관별 규제·데이터 주권 요건으로 멀티클라우드 관리 복잡성 증가
- MLOps 툴체인 파편화 — 평가 자동화, 프롬프트 관리, 모니터링 도구가 각각 별도 시장으로 분산

---

## 2. 기술 성숙도

### 2.1 자동 프롬프트 최적화 (FeedbackOps/Prompt)

현재 기술 성숙도 수준(Technology Readiness Level, TRL): **TRL 5~7** — 학술 검증 완료, 초기 프로덕션 적용 단계

**주요 프레임워크 비교**

| 프레임워크 | 접근 방식 | 성능 | 상태 |
|-----------|---------|------|------|
| DSPy (Stanford NLP) | 프롬프트를 코드로 추상화, 컴파일러 기반 최적화 | Math 문제 +25~65% [[G-16]](#ref-g-16) | 오픈소스 활발 |
| TextGrad (Stanford) | 텍스트 기반 역전파(backpropagation), Nature 게재 | GSM8k 82.1% (DSPy+TextGrad 결합) [[G-16]](#ref-g-16) | 오픈소스 |
| ADAS (Automated Design of Agentic Systems) | 메타 에이전트가 코드 수준에서 에이전트 자동 설계 | ICLR 2025 채택, 도메인 간 전이 성능 검증 [[G-17]](#ref-g-17) | 연구 단계 |
| AFlow | 에이전트 워크플로우 자동 설계 | ICLR 2025 채택 [[G-17]](#ref-g-17) | 연구 단계 |

- DSPy와 TextGrad는 상호 보완적: DSPy는 In-Context 예제 추가, TextGrad는 시스템 프롬프트 최적화에 강점 [[G-16]](#ref-g-16)
- 2025년 7월 연구에서 DSPy가 가드레일 강화, 환각 탐지, 코드 생성, 라우팅 에이전트 5가지 사용 사례에서 정확도 46.2% → 64.0% 향상 확인 [[G-18]](#ref-g-18)

### 2.2 LLM 평가 자동화 (EvalOps/KMS)

현재 TRL: **TRL 6~8** — 프로덕션 사용 중, 표준화 진행

**주요 평가 프레임워크**

- **HELM** (Stanford CRFM): 정확도·교정·견고성·공정성·편향·독성·효율성 7개 지표, 16개 핵심 시나리오. 오픈소스 Python 프레임워크 [[G-19]](#ref-g-19)
- **LM Evaluation Harness** (EleutherAI): 60+ 표준 학술 벤치마크, 수백 개 서브태스크. 동일 입력·코드베이스 기반 재현 가능한 평가 [[G-20]](#ref-g-20)
- **LangSmith** (LangChain): 프로덕션 에이전트 추적·평가·배포 통합. LLM-as-a-Judge, 인간 어노테이션, 휴리스틱 평가 지원. 2025년 멀티스텝 에이전트 트레이싱 강화 [[G-21]](#ref-g-21)
- **MLflow 3.0 Evaluation** (Databricks): 2025년 6월 출시, GenAI·에이전트 평가 통합, LLM-as-a-Judge 내장, OpenTelemetry 호환 [[G-07]](#ref-g-07)

**트렌드**: LLM-as-a-Judge 방식이 인간 평가를 대체하는 자동화 평가의 핵심 방법론으로 자리잡음. 단일 지표에서 다차원 평가(품질·비용·지연시간·안전성)로 확장 중.

### 2.3 MLOps 파이프라인

현재 TRL: **TRL 8~9** — 성숙, 엔터프라이즈 표준 확립

**플랫폼 진화 현황**

- **MLflow 3.0** (Databricks, 2025년 6월): 전통 ML + 딥러닝 + GenAI 단일 플랫폼 통합. Mosaic AI Agent Framework, Unity Catalog 거버넌스, MLflow Tracing(OpenTelemetry) 포함 [[G-07]](#ref-g-07)
- **Databricks Mosaic AI**: Compound AI System 전주기 관리 환경. Mosaic AI Gateway로 외부 LLM API 관리 [[G-07]](#ref-g-07)
- 2026년 MLOps 범위: 고전 ML + LLM + RAG 파이프라인 + 벡터 검색 + 에이전트 기반 애플리케이션 통합 운영으로 확장 [[G-13]](#ref-g-13)
- **AWS Bedrock AgentCore** (2025년 10월): 엔터프라이즈급 에이전트 시스템 빌더, 접근 관리·관찰성·보안 포함 [[G-22]](#ref-g-22)

### 2.4 GPU 오케스트레이션 / 추론 최적화

현재 TRL: **TRL 7~9** — 추론 프레임워크 성숙, 오케스트레이션은 빠른 발전 중

**추론 엔진 성능 비교 (H100 기준)**

| 프레임워크 | 주요 강점 | 벤치마크 지표 | 최적 사용 사례 |
|-----------|---------|------------|-------------|
| vLLM | PagedAttention, 연속 배칭, 빠른 첫 토큰(TTFT) | SGLang 대비 낮은 처리량이나 최저 TTFT [[G-23]](#ref-g-23) | 고동시성, 인터랙티브 서비스 |
| SGLang | RadixAttention, 안정적 per-token 지연시간 | 16,215 tok/s, vLLM 12,553 tok/s 대비 29% 우위 [[G-23]](#ref-g-23) | 구조화된 출력, 일관된 지연시간 |
| TensorRT-LLM (NVIDIA) | Hopper/Blackwell 아키텍처 최적화, B200에서 최상위 성능 | 모든 동시성 레벨에서 1위 (B200 기준) [[G-23]](#ref-g-23) | NVIDIA 하드웨어 최적화, 엔터프라이즈 |
| NVIDIA NIM | TensorRT-LLM 기반, 컨테이너화, 5분 이내 배포 | H100에서 1,201 tok/s (off-the-shelf 613 tok/s 대비 2.6배) [[G-24]](#ref-g-24) | 엔터프라이즈 프로덕션 |

**GPU 오케스트레이션**

- **NVIDIA Run:ai** ($700M 인수 완료): Kubernetes 기반 GPU 가상화·스케줄링. 분수 GPU 할당, 동적 리소스 배분, 기업 도입 후 유효 GPU 활용률 2~3배 향상 [[G-25]](#ref-g-25)
- Run:ai 소프트웨어 오픈소스화 계획 발표 (NVIDIA) [[G-25]](#ref-g-25)
- 기존 30~40% GPU 활용률 → 추론 프레임워크 최적화 후 70~80%로 개선 가능 [[G-10]](#ref-g-10)
- Speculative Decoding: 추론 속도 2~3배 향상 기법, 2025년 프로덕션 적용 확산 [[G-26]](#ref-g-26)

---

## 3. 경쟁사 / 플레이어 동향

**주요 플레이어 동향**

| 기업 | 동향 | 출처 |
|------|------|------|
| NVIDIA | Run:ai 인수(~$700M) 완료, NIM 마이크로서비스 160+ 모델 지원, 2025년 12월 기준 H100 대비 NIM 2.6배 처리량 향상 발표 | [[G-24]](#ref-g-24), [[G-25]](#ref-g-25) |
| Databricks | MLflow 3.0(2025년 6월) 출시, Mosaic AI로 Compound AI System 전주기 통합 플랫폼 선언 | [[G-07]](#ref-g-07) |
| CoreWeave | W&B(Weights & Biases) $1.7B 인수 완료(2025년 5월), GPU 인프라+MLOps 툴체인 수직 통합 | [[G-27]](#ref-g-27), [[G-28]](#ref-g-28) |
| Anyscale (Ray) | Ray가 PyTorch Foundation 합류, LLM 서빙에 Ray Serve + vLLM 통합, Wide-EP/Disaggregated Serving 지원 | [[G-29]](#ref-g-29) |
| AWS | Bedrock AgentCore(2025년 10월 출시), SageMaker MLOps 통합, 엔터프라이즈 에이전트 시스템 빌더 | [[G-22]](#ref-g-22) |
| Google Cloud | A2A(Agent-to-Agent) 프로토콜 창시(2025년 4월), Linux Foundation 기증, Vertex AI에 에이전트 오케스트레이션 내장 | [[G-22]](#ref-g-22) |
| Microsoft Azure | Azure AI Foundry + Microsoft Agent Framework 오픈소스 SDK 출시(2025년 10월), MCP/A2A 프로토콜 지원 | [[G-22]](#ref-g-22) |
| FriendliAI (한국) | $20M Seed Extension 조달, LG Electronics 파트너십, EXAONE 단독 API 공급, 2025년 매출 YoY 6~7배 성장 예상 | [[G-30]](#ref-g-30) |
| SambaNova | SN50 칩 공개(2025년), Intel과 멀티 이어 협업(2026년 2월), Xeon CPU+SambaNova AI 소프트웨어 스택 결합 | [[G-31]](#ref-g-31) |
| NTT DATA | NVIDIA NIM+NeMo 기반 엔터프라이즈 AI Factory 이니셔티브 발표(2026년 3월) | [[G-32]](#ref-g-32) |
| SKT | Haein GPU 클러스터(1,000+ NVIDIA Blackwell) 구축, GPUaaS 상용화, AI DC 매출 $354M(YoY +35%), MWC 2026 Best Cloud Solution 수상 | [[G-33]](#ref-g-33), [[G-34]](#ref-g-34) |
| KT | Microsoft와 Azure AI 협력(GPT-4o 커스터마이즈, Phi 소형모델 탐색), Azure AI Studio·Copilot Studio 기반 B2B 에이전트 개발 | [[G-35]](#ref-g-35) |

---

## 4. 투자 / M&A 트렌드

### 4.1 주요 M&A 사례 (최근 12개월)

| 딜 | 금액 | 시점 | 전략적 의의 |
|---|------|------|------------|
| CoreWeave → Weights & Biases | $1.7B | 2025년 5월 완료 | GPU 인프라+MLOps 툴 수직 통합 [[G-27]](#ref-g-27) |
| NVIDIA → Run:ai | ~$700M | 완료(2024~2025) | GPU 오케스트레이션 플랫폼 내재화 [[G-25]](#ref-g-25) |
| (기존) Databricks → MosaicML | $1.3B | 2023 | 엔터프라이즈 MLOps+파운데이션 모델 결합 |

### 4.2 주요 펀딩 라운드

| 기업 | 라운드 | 금액 | 시점 | 비고 |
|------|--------|------|------|------|
| FriendliAI | Seed Extension | $20M | 2025 | KDB, KB Securities 참여 [[G-30]](#ref-g-30) |
| VESSL AI | Series A | $12M | 2024년 10월 | GPU 비용 최대 80% 절감 MLOps [[G-36]](#ref-g-36) |
| DataRobot | 누적 | $1B+ | 누적 | 투자자 신뢰도 최고 [[G-14]](#ref-g-14) |

### 4.3 투자 트렌드 분석

- 2024년 MLOps 섹터 투자 $4.5B, 2025년 $6B+ 전망, 2026년 $7~8B 예측 [[G-14]](#ref-g-14)
- Microsoft, Google, Snowflake, NVIDIA가 전략적 기업 투자 주도 [[G-14]](#ref-g-14)
- 2026년 15~20건 전략적 M&A 예상, 매출 기업 대상 8~12배 ARR 멀티플 [[G-14]](#ref-g-14)
- **패턴**: GPU 클라우드 + MLOps 툴 결합(CoreWeave-W&B), GPU 오케스트레이션 내재화(NVIDIA-Run:ai), 모델 훈련+서빙 통합(Databricks) — 플랫폼 수직 통합이 M&A의 핵심 테마

---

## 5. 통신사 적용 가능성

### 5.1 SKT 현황

SKT는 국내 통신사 중 가장 적극적인 AI 인프라 투자를 진행 중이다 [[G-33]](#ref-g-33):

- **Haein GPU 클러스터**: 1,000+ NVIDIA Blackwell GPU, DASE(분리형 공유-전체) 아키텍처, Vast 스토리지, Supermicro HGX 서버
- **GPUaaS 상용화**: 멀티테넌트 환경, 대규모 AI 학습 및 실시간 추론 동시 지원
- **AI DC 매출**: 2025년 $354M (YoY +35%), 2030년 목표 KRW 1조($700M) [[G-33]](#ref-g-33)
- **MWC 2026**: GSMA Global Mobile Awards Best Cloud Solution 수상 (3년 연속 클라우드 기술 수상) [[G-34]](#ref-g-34)
- **소버린 AI**: 519B 파라미터 파운데이션 모델(국내 최대), 1조 파라미터 + 멀티모달 업그레이드 계획 [[G-33]](#ref-g-33)
- **NVIDIA-SK Group AI Factory**: NVIDIA와 한국 제조·디지털 전환 AI Factory 구축 협력 [[G-37]](#ref-g-37)

### 5.2 KT 현황

KT는 자체 GPU 인프라 구축보다 Microsoft Azure AI 파트너십 중심의 전략을 채택 [[G-35]](#ref-g-35):

- GPT-4o 및 Phi 소형모델 커스터마이즈 개발 협력
- Azure AI Studio·Copilot Studio 기반 커스텀 AI 에이전트 개발 (B2C: 교육·헬스케어·차량, B2B: 산업별 솔루션)
- 자체 MLOps 파이프라인보다 Azure 관리형 서비스 의존 구조

### 5.3 글로벌 통신사 AI 인프라 투자 규모

- 통신사 전체: 2025~2030년 AI 클라우드 인프라 누적 $770억 투자 예상 (Analysys Mason) [[G-15]](#ref-g-15)
- 아태 지역 통신사(한국 포함)가 소버린 AI, LLM 학습, AIaaS/GPUaaS 분야에서 선도 [[G-15]](#ref-g-15)
- NTT DATA: NVIDIA NIM+NeMo 기반 엔터프라이즈 AI Factory 발표(2026년 3월) [[G-32]](#ref-g-32)

### 5.4 통신사 B2B 서비스로서의 MLOps/GPU 오케스트레이션

- GPUaaS B2B 서비스: 데이터 주권 요건을 가진 금융·공공·의료 기업 대상 "소버린 GPU 클라우드" 포지셔닝 가능 [[G-15]](#ref-g-15)
- AI-as-a-Service: 네트워크 인프라(저지연) + GPU + MLOps 툴체인 번들링으로 하이퍼스케일러 대비 차별화 [[G-38]](#ref-g-38)
- **핵심 과제**: GPU 가동률 60~70%+ 확보 — 지리적으로 분산된 통신사 GPU는 하이퍼스케일러 대비 낮은 가동률이 수익성의 구조적 위협 [[G-15]](#ref-g-15)

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- CoreWeave-W&B 인수 금액($1.7B, 2025년 5월) — 복수 공식 보도 확인
- NVIDIA-Run:ai 인수(~$700M) — 공식 블로그 및 복수 미디어 확인
- MLflow 3.0 출시(2025년 6월) — Databricks 공식 블로그 확인
- SKT Haein GPU 클러스터(1,000+ Blackwell) — SKT 뉴스룸 공식 발표
- SKT AI DC 매출 $354M(YoY +35%) — 공식 발표 자료 기반
- vLLM/SGLang/TensorRT-LLM 성능 비교 — 복수 독립 벤치마크 기관 일치

**추가 검증 필요 [C/D]:**
- MLOps 시장 규모 수치 — 기관별 편차 크고 단일 보고서 기반, 교차 검증 불충분
- FriendliAI 매출 6~7배 성장 — 단일 소스(Crunchbase) [D]
- 2026년 MLOps 투자 $7~8B 전망 — 단일 분석 보고서 [D]
- KT Azure 협력 상세 진행 현황 — 2024년 발표 이후 업데이트 미확인

**데이터 공백:**
- KT 자체 GPU 인프라 규모·투자 금액 — 공개 정보 없음
- Anyscale 2025년 구체적 매출/투자 규모 — 공개 정보 없음
- DSPy/TextGrad 기업 프로덕션 채택율 — 체계적 데이터 없음
- 국내 MLOps 플랫폼 시장 규모(KR TAM) — 공개 데이터 없음

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Fortune Business Insights — MLOps Market Size | [링크](https://www.fortunebusinessinsights.com/mlops-market-108986) | report | 2025 | [B] |
| <a id="ref-g-02"></a>G-02 | GlobeNewswire — MarketsandMarkets MLOps $5.9B by 2027 | [링크](https://www.globenewswire.com/news-release/2023/04/21/2652028/0/en/MLOps-Market-Size-is-Anticipated-to-Cross-US-5-9-billion-by-2027-growing-at-a-CAGR-of-41-0-Report-by-MarketsandMarkets.html) | report | 2023-04-21 | [B] |
| <a id="ref-g-03"></a>G-03 | Straits Research — MLOps Market Size Share Trends | [링크](https://straitsresearch.com/report/mlops-market) | report | 2025 | [C] |
| <a id="ref-g-04"></a>G-04 | Business Research Insights — MLOps Market 2035 | [링크](https://www.businessresearchinsights.com/market-reports/machine-learning-operations-mlops-market-109238) | report | 2025 | [C] |
| <a id="ref-g-05"></a>G-05 | GM Insights — MLOps Market Size Share 2025-2034 | [링크](https://www.gminsights.com/industry-analysis/mlops-market) | report | 2025 | [C] |
| <a id="ref-g-06"></a>G-06 | Valuates Reports — LLMOps Software Market $19.8B 2032 | [링크](https://reports.valuates.com/market-reports/QYRE-Auto-33S18467/global-large-language-model-operationalization-llmops-software) | report | 2025 | [C] |
| <a id="ref-g-07"></a>G-07 | Databricks Blog — MLflow 3.0 Unified AI Experimentation | [링크](https://www.databricks.com/blog/mlflow-30-unified-ai-experimentation-observability-and-governance) | news | 2025-06 | [A] |
| <a id="ref-g-08"></a>G-08 | MarketsandMarkets — GPU as a Service Market $26.6B 2030 | [링크](https://www.marketsandmarkets.com/Market-Reports/gpu-as-a-service-market-153834402.html) | report | 2025 | [B] |
| <a id="ref-g-09"></a>G-09 | Fortune Business Insights — GPU as a Service Market | [링크](https://www.fortunebusinessinsights.com/gpu-as-a-service-market-107797) | report | 2025 | [B] |
| <a id="ref-g-10"></a>G-10 | MarketsandMarkets — AI Inference Market $50B 2026 | [링크](https://www.marketsandmarkets.com/Market-Reports/ai-inference-market-189921964.html) | report | 2025 | [B] |
| <a id="ref-g-11"></a>G-11 | Precedence Research — AI Data Center GPU Market $77.15B 2035 | [링크](https://www.precedenceresearch.com/ai-data-center-gpu-market) | report | 2025 | [C] |
| <a id="ref-g-12"></a>G-12 | Bloomcs / AWS.PlainEnglish — GenAI Cloud Services YoY 140-180% Q2 2025 | [링크](https://aws.plainenglish.io/aws-bedrock-sagemaker-vs-azure-ai-foundry-vs-google-vertex-ai-the-ultimate-cloud-ai-platform-2026-03bbbab919b2) | blog | 2025 | [C] |
| <a id="ref-g-13"></a>G-13 | Hatchworks — MLOps in 2026: What You Need to Know | [링크](https://hatchworks.com/blog/gen-ai/mlops-what-you-need-to-know/) | blog | 2026 | [C] |
| <a id="ref-g-14"></a>G-14 | QuickMarketPitch — Which MLOps platforms got funded? July 2025 | [링크](https://quickmarketpitch.com/blogs/news/mlops-funding) | blog | 2025-07 | [C] |
| <a id="ref-g-15"></a>G-15 | Analysys Mason — Operators $77B AI cloud infrastructure 2025-2030 | [링크](https://www.analysysmason.com/research/content/articles/telecoms-ai-cloud-rma16-rma21/) | report | 2025 | [B] |
| <a id="ref-g-16"></a>G-16 | Stanford HAI — TextGrad: AutoGrad for Text | [링크](https://hai.stanford.edu/news/textgrad-autograd-text) | news | 2024 | [A] |
| <a id="ref-g-17"></a>G-17 | ICLR 2025 / arXiv — ADAS: Automated Design of Agentic Systems | [링크](https://arxiv.org/abs/2408.08435) | paper | 2025 | [A] |
| <a id="ref-g-18"></a>G-18 | arXiv — Is It Time To Treat Prompts As Code? DSPy Multi-Use Case Study | [링크](https://arxiv.org/html/2507.03620v1) | paper | 2025-07 | [A] |
| <a id="ref-g-19"></a>G-19 | Stanford CRFM — HELM (Holistic Evaluation of Language Models) | [링크](https://crfm.stanford.edu/helm/latest/) | paper | 2022-2025 | [A] |
| <a id="ref-g-20"></a>G-20 | EleutherAI — LM Evaluation Harness GitHub | [링크](https://github.com/EleutherAI/lm-evaluation-harness) | code | 2025 | [A] |
| <a id="ref-g-21"></a>G-21 | LangChain — LangSmith AI Agent & LLM Observability Platform | [링크](https://www.langchain.com/langsmith-platform) | product | 2025 | [B] |
| <a id="ref-g-22"></a>G-22 | GoPenAI Blog — Azure AI Foundry vs AWS Bedrock vs Google Vertex AI 2025 Guide | [링크](https://blog.gopenai.com/azure-ai-foundry-vs-aws-bedrock-vs-google-vertex-ai-the-2025-guide-25a69c1d19b1) | blog | 2025 | [B] |
| <a id="ref-g-23"></a>G-23 | Spheron Blog — vLLM vs TensorRT-LLM vs SGLang H100 Benchmarks 2026 | [링크](https://www.spheron.network/blog/vllm-vs-tensorrt-llm-vs-sglang-benchmarks/) | blog | 2026 | [B] |
| <a id="ref-g-24"></a>G-24 | NVIDIA — NIM Microservices for Fast AI Inference Deployment | [링크](https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/) | product | 2025-12 | [A] |
| <a id="ref-g-25"></a>G-25 | NVIDIA Blog — NVIDIA to Acquire GPU Orchestration Software Provider Run:ai | [링크](https://blogs.nvidia.com/blog/runai/) | news | 2024-2025 | [A] |
| <a id="ref-g-26"></a>G-26 | Introl Blog — Speculative Decoding: Achieving 2-3x LLM Inference Speedup | [링크](https://introl.com/blog/speculative-decoding-llm-inference-speedup-guide-2025) | blog | 2025 | [C] |
| <a id="ref-g-27"></a>G-27 | CoreWeave — CoreWeave Completes Acquisition of Weights & Biases | [링크](https://www.coreweave.com/blog/coreweave-completes-acquisition-of-weights-biases) | news | 2025-05-07 | [A] |
| <a id="ref-g-28"></a>G-28 | TechCrunch — CoreWeave acquires AI developer platform Weights & Biases | [링크](https://techcrunch.com/2025/03/04/coreweave-acquires-ai-developer-platform-weights-biases/) | news | 2025-03-04 | [B] |
| <a id="ref-g-29"></a>G-29 | Anyscale — Ray Serve LLM Wide-EP and Disaggregated Serving with vLLM | [링크](https://www.anyscale.com/blog/ray-serve-llm-anyscale-apis-wide-ep-disaggregated-serving-vllm) | blog | 2025 | [B] |
| <a id="ref-g-30"></a>G-30 | Crunchbase News — FriendliAI Raises $20M Seed Extension | [링크](https://news.crunchbase.com/ai/inference-platform-friendliai-raises-seed-extension-chun/) | news | 2025 | [B] |
| <a id="ref-g-31"></a>G-31 | Intel Newsroom — Intel and SambaNova Multi-Year Collaboration | [링크](https://newsroom.intel.com/data-center/intel-and-sambanova-planning-multi-year-collaboration-for-xeon-based-ai-inference) | news | 2026-02 | [A] |
| <a id="ref-g-32"></a>G-32 | NTT DATA — NTT DATA unveils NVIDIA-powered enterprise AI factories | [링크](https://us.nttdata.com/en/news/press-release/2026/march/ntt-data-unveils-nvidia-powered-enterprise-ai-factories) | news | 2026-03 | [A] |
| <a id="ref-g-33"></a>G-33 | SKT Newsroom — Haein AI Infrastructure Built with 1,000 GPUs GPUaaS GLOMO Award | [링크](https://news.sktelecom.com/en/2895) | news | 2026-03 | [A] |
| <a id="ref-g-34"></a>G-34 | Telecomsinfrastructure.com — SK Telecom Builds AI Infrastructure Momentum with GPUaaS and Haein Cluster | [링크](https://www.telecomsinfrastructure.com/2026/03/sk-telecom-builds-ai-infrastructure.html) | news | 2026-03 | [B] |
| <a id="ref-g-35"></a>G-35 | Microsoft Source — KT Corporation and Microsoft Giant Step AI Innovation in Korea | [링크](https://news.microsoft.com/source/2024/09/29/kt-corporation-and-microsoft-take-giant-step-to-accelerate-ai-innovation-in-korea/) | news | 2024-09-29 | [A] |
| <a id="ref-g-36"></a>G-36 | TechCrunch — VESSL AI secures $12M for MLOps platform GPU costs 80% reduction | [링크](https://techcrunch.com/2024/10/07/vessl-ai-secures-12m-for-its-mlops-platform/) | news | 2024-10-07 | [B] |
| <a id="ref-g-37"></a>G-37 | NVIDIA Investor Relations — NVIDIA and SK Group Build AI Factory Korea | [링크](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-and-SK-Group-Build-AI-Factory-to-Drive-Koreas-Manufacturing-and-Digital-Transformation/default.aspx) | news | 2025 | [A] |
| <a id="ref-g-38"></a>G-38 | RCR Wireless — How Telcos can offer AI-as-a-Service to enterprise clients | [링크](https://www.rcrwireless.com/20251203/ai/telcos-as-ai-providers) | news | 2025-12-03 | [B] |
