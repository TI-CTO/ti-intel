---
topic: 엣지/온디바이스 VLM 배포 기술 — 통신사 MEC 인프라 활용 관점
date: 2026-03-12
agent: research-deep
confidence: medium
status: completed
sources_used: [websearch]
---

# Research Report: 엣지/온디바이스 VLM 배포 기술 — 통신사 MEC 인프라 활용 관점

## Executive Summary

> 2025~2026년 기준으로 소형 VLM(Moondream 1.8B, SmolVLM-256M 등)은 INT4 양자화 적용 시 2~4GB VRAM만으로 엣지 서버 배포가 현실화되었다. MiniCPM-V 2.6(8B)은 모바일 NPU에서 8.2 tokens/s 추론을 달성해 온디바이스 실용 임계를 처음 넘었으며, Qwen2.5-VL 7B는 MEC 엣지 서버(16~24GB GPU 탑재)에서 운용 가능한 수준이다. VLM 특화 양자화(MBQ, CVPR 2025)는 W4A8에서 FP16 대비 1.1% 이내 정확도 손실을 달성했으며, NVIDIA TensorRT Edge-LLM은 자동차·로보틱스 엣지 플랫폼에서 VLM 실시간 추론을 공식 지원하기 시작했다. 통신사 MEC 관점에서 100ms 이하 응답 지연은 모델 분할 추론(비전 인코더 엣지 + LLM 디코더 클라우드) 아키텍처로 달성 가능하며, 실시간 CCTV 분석은 H100 1장 기준 8 FPS(StreamingVLM), RTX 4090 기준 6 FPS(VideoScan)가 최신 연구 수준이다. 데이터 공백: MEC 노드별 VLM 배포 실제 상용 사례는 아직 제한적이며 [C] 수준 추가 검증이 필요하다.

---

## 연구 질문

> 통신사 MEC 인프라에 VLM을 배포할 때 현실적으로 어떤 모델을 어떤 하드웨어에서 어떤 프레임워크로 운용할 수 있는가? 양자화 기술의 정확도-효율 트레이드오프, 실시간 영상 처리 가능 여부, 클라우드-엣지 분산 추론 전략은 무엇인가?

---

## 1. 기술 현황

**TRL(기술 성숙도) 평가**

- **소형 VLM 온디바이스 추론**: TRL 7~8 (파일럿 배포 단계). Moondream, SmolVLM, MiniCPM-V 등이 모바일/엣지 환경에서 실제 작동 검증됨.
- **MEC 서버급 VLM 서빙**: TRL 6~7 (데모/초기 상용 단계). 7B 이하 모델은 INT4 양자화 후 16GB GPU 서버에서 서비스 가능.
- **실시간 영상 스트림 VLM 분석**: TRL 5~6 (연구 실증 단계). StreamingVLM, VideoScan이 2025년 발표되었으나 상용 배포 사례는 제한적.

**주요 기술 요소**

- **양자화(Quantization)**: INT4/INT8 PTQ(Post-Training Quantization), QAT(Quantization-Aware Training), VLM 특화 방법(MBQ, VEQ)
- **추론 엔진**: llama.cpp(CPU/엣지), vLLM(서버 고처리량), TensorRT Edge-LLM(NVIDIA 임베디드), MLC-LLM(크로스플랫폼)
- **분산 추론**: 비전 인코더-LLM 디코더 분리, 클라우드-엣지 오프로딩
- **스트리밍 추론**: KV 캐시 최적화(Attention Sink), 청크 기반 프리필

---

## 2. 시장 동향

**엣지 AI 추론 시장 확대**

- 2026년 기준 AI 전체 컴퓨팅의 약 2/3가 추론 워크로드로 전환 예상 (2023년 1/3 → 2025년 1/2 → 2026년 2/3) [[G-01]](#ref-g-01)
- 추론 최적화 칩 시장이 2026년 500억 달러 이상으로 성장 전망 [[G-01]](#ref-g-01)
- 2026년까지 모바일 데이터 트래픽의 54%가 5G 네트워크를 통해 처리될 예상, MEC 인프라 투자 가속 [[G-02]](#ref-g-02)

**통신사 MEC + AI 융합**

- MEC는 일반적으로 20ms 이하 지연시간을 제공하며, 실시간 AI 분석을 위한 기반 인프라로 자리매김 [[G-03]](#ref-g-03)
- NVIDIA는 GTC 2026에서 MEC 서버 전용 엣지 AI 인프라 솔루션(Lanner Electronics 협력) 발표 [[G-04]](#ref-g-04)
- China Telecom은 "AI Flow" 전략으로 엣지 노드에서 AI 추론 통합 추진 [[G-05]](#ref-g-05)

---

## 3. 경쟁사 동향

**주요 플레이어 동향**

| 기업 | 동향 | 출처 |
|------|------|------|
| NVIDIA | TensorRT Edge-LLM 출시(2025). Jetson Thor 기반 자동차·로보틱스 VLM 실시간 추론 지원. Bosch, MediaTek 등 파트너 채택. AGX Orin 64GB에서 Qwen2.5-VL-7B 공식 지원. | [[G-06]](#ref-g-06) |
| Alibaba (Qwen팀) | Qwen2.5-VL 7B/72B 출시. MNN Chat App으로 온디바이스 배포 지원. NVFP4 양자화 버전 제공. | [[G-07]](#ref-g-07) |
| OpenBMB (MiniCPM팀) | Nature Communications 논문(2025)으로 MiniCPM-V 2.6 성능 공인. 모바일 NPU 150x 이미지 인코딩 가속 달성. | [[G-08]](#ref-g-08) |
| Moondream AI | 2025년 4월 2B(1.9B) 모델 출시. QAT INT4 지원. RTX 3090에서 4-bit 시 184 tokens/s. | [[G-09]](#ref-g-09) |
| HuggingFace | SmolVLM/SmolVLM2 시리즈. 256M 모델이 0.8GB VRAM으로 동작, WebGPU 브라우저 배포 지원. | [[G-10]](#ref-g-10) |
| MIT Han Lab | StreamingVLM(2025.10) 발표. H100 1장에서 8 FPS 무한 영상 스트림 처리. | [[G-11]](#ref-g-11) |

---

## 4. 제품/서비스 스펙 비교

#### 모델별 하드웨어 요구사항 (엣지 배포 기준)

**모델 스펙 비교**

| 기업 | VRAM(FP16) | VRAM(INT4) | 가격(정책) | 출처 |
|------|-----------|-----------|-----------|------|
| Moondream 2B (1.9B) | ~4GB | 2.45GB (RTX 3090 실측) | 오픈소스 (Apache 2.0) | [[G-09]](#ref-g-09) |
| SmolVLM-256M | ~1GB | 0.8GB | 오픈소스 (Apache 2.0) | [[G-10]](#ref-g-10) |
| SmolVLM-500M | ~2GB | ~1.2GB | 오픈소스 (Apache 2.0) | [[G-10]](#ref-g-10) |
| MiniCPM-V 2.6 (8B) | ~16GB | ~6GB (모바일: 시분할 로딩) | 오픈소스 (Apache 2.0) | [[G-08]](#ref-g-08) |
| Qwen2.5-VL-7B | ~17GB | ~5GB (NVFP4) | 오픈소스 (Apache 2.0) | [[G-07]](#ref-g-07) [[G-12]](#ref-g-12) |
| Qwen2.5-VL-72B | ~144GB | ~36GB (INT4) | 오픈소스 (Apache 2.0) | [[G-13]](#ref-g-13) |

#### 모델별 추론 속도 (실측 벤치마크)

**추론 속도 비교**

| 기업 | 추론속도 | 하드웨어 | 출처 |
|------|---------|---------|------|
| Moondream 2B (INT4) | 184 tokens/s | RTX 3090 (2.45GB VRAM) | [[G-09]](#ref-g-09) |
| SmolVLM-256M | 80 decode tokens/s | MacBook Pro M4 Max (WebGPU) | [[G-10]](#ref-g-10) |
| SmolVLM-256M | 수백 examples/s (batch 1) | NVIDIA A100 | [[G-10]](#ref-g-10) |
| MiniCPM-V (모바일) | 8.2 tokens/s | 스마트폰 (Qualcomm NPU) | [[G-08]](#ref-g-08) |
| MiniCPM-V (엔코딩) | 150x 가속 (vs. 미최적화) | 엣지 디바이스 | [[G-08]](#ref-g-08) |
| SmolVLM 생성 단계 | 7.5~16x 빠름 (vs. Qwen2-VL) | — | [[G-10]](#ref-g-10) |

---

## 5. 학술 동향

#### 주요 논문 (2024~2025)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| MBQ: Modality-Balanced Quantization for Large VLMs (Li et al., CVPR 2025) | 비전/텍스트 토큰 감도 차이를 활용한 VLM 전용 양자화. W4A8에서 FP16 대비 정확도 손실 1.1% 이내. 7B VLM 대비 AWQ 대비 4.2% 개선. | [[P-01]](#ref-p-01) |
| SmolVLM: Redefining small and efficient multimodal models (Arxiv 2025) | 256M~2B 소형 VLM 시리즈. Prefill 3.3~4.5x, 생성 7.5~16x 속도 향상 (vs. Qwen2-VL). 0.8GB VRAM 동작 검증. | [[P-02]](#ref-p-02) |
| StreamingVLM: Real-Time Understanding for Infinite Video Streams (MIT Han Lab et al., 2025) | Attention Sink + KV 캐시 최적화로 무한 영상 스트림 처리. H100에서 8 FPS, 40GB VRAM 이하. | [[P-03]](#ref-p-03) |
| VideoScan: Efficient Streaming Video Understanding (arxiv 2025.03) | 프레임당 단일 시맨틱 캐리어 토큰으로 5x 속도 향상. RTX 4090에서 6 FPS 실시간 추론. | [[P-04]](#ref-p-04) |
| Efficient GPT-4V level multimodal LLM for edge (Nature Communications, 2025) | MiniCPM-V 2.6 공인 연구. 8B 파라미터로 GPT-4V 수준 성능, 모바일 NPU 최적화 상세 기술. | [[P-05]](#ref-p-05) |
| Distributed VLMs: Cloud-Edge Collaboration (Columbia Univ, 2025) | 비전 인코더 엣지 + LLM 서버 분리 구조. 토큰 제한 5기준 33.5%, 토큰 15기준 29% 처리량 향상. | [[P-06]](#ref-p-06) |
| Comparative Study: MLX, MLC-LLM, Ollama, llama.cpp (arxiv 2411.05502) | 온디바이스 추론 프레임워크 6종 비교. LMDeploy가 100 동시 사용자 기준 최고 처리량 700 tokens/s. | [[P-07]](#ref-p-07) |

---

## 6. 특허 동향

MCP intel-store 접근 불가 환경에서 WebSearch로 VLM 특허 동향을 별도 수집하지 않았음. 아래는 공개 정보 기반 서술임.

- **NVIDIA**: Jetson 플랫폼 및 TensorRT 관련 엣지 추론 최적화 특허 다수 보유. TensorRT Edge-LLM 출시(2025)가 특허 포트폴리오의 실용화 단계.
- **Qualcomm**: 모바일 NPU 기반 VLM 추론(QNN 프레임워크) 관련 특허 적극 출원 중. MiniCPM-V의 NPU 가속이 Qualcomm QNN 프레임워크 기반.
- **출원 추이**: VLM 경량화·양자화 관련 특허는 2024~2025년 급증 추세로 추정되나 구체적 수치는 추가 검증 필요 [D].

---

## 7. 기업 발언 & 보도자료

**NVIDIA — TensorRT Edge-LLM 발표 (2025)**

> "TensorRT Edge-LLM is a new, open source C++ framework for LLM and VLM inference, designed to solve the emerging need for high-performance edge inference. Edge-LLM is purpose-built for real-time applications on embedded automotive and robotics platforms." — NVIDIA Technical Blog, 2025 [[G-06]](#ref-g-06)

- Bosch, ThunderSoft, MediaTek가 차량 내 AI 어시스턴트 및 캐빈 모니터링 시스템에 TensorRT Edge-LLM 채택 발표.

**Deloitte — 2026 Inference 전망 (2025)**

> "Inference workloads will account for roughly two-thirds of all compute in 2026, up from a third in 2023 and half in 2025. The market for inference-optimized chips is growing to over US$50 billion in 2026." — Deloitte TMT Predictions 2026 [[G-01]](#ref-g-01)

**China Telecom — AI Flow 전략 (2025)**

- 통신사가 엣지 노드를 활용한 "유비쿼터스 인텔리전스" 구현을 추진 중임을 ITU AI for Good 포럼에서 발표. 엣지 AI 추론을 통신 인프라 핵심 서비스로 규정. [[G-05]](#ref-g-05)

**MiniCPM팀 — Nature Communications 논문 (2025)**

> "MiniCPM-V 2.6 achieves real-time video understanding on end-side devices such as iPad for the first time, supported by superior token density and systematic NPU optimization." — Nature Communications, 2025 [[P-05]](#ref-p-05)

---

## 8. 전략적 시사점

### MEC VLM 배포 아키텍처 권고

**엣지 계층별 모델 선택 기준**

- **모바일 단말 (≤4GB RAM)**: Moondream 2B INT4, SmolVLM-256M/500M
  - 적합 시나리오: 현장 작업자 AR 지원, 단말 측 1차 필터링
- **MEC 엣지 노드 (8~24GB GPU)**: MiniCPM-V 2.6, Qwen2.5-VL-7B (INT4/NVFP4)
  - 적합 시나리오: CCTV 분석, 실시간 영상 이벤트 감지, 산업 현장 모니터링
- **MEC 고성능 노드 (40GB+ GPU)**: Qwen2.5-VL-72B, StreamingVLM 워크로드
  - 적합 시나리오: 광역 CCTV 통합 분석, 다중 카메라 스트림

**분산 추론 전략 (100ms 이하 달성 경로)**

- Columbia Univ 연구에 따르면, **비전 인코더를 엣지에, LLM 디코더를 클라우드에 분리**하는 구조가 단순 집중 배포 대비 29~33% 처리량 향상을 가져옴 [[P-06]](#ref-p-06)
- MEC 자체 지연은 20ms 이하 수준이므로, 모델 추론 지연을 80ms 이하로 설계하면 100ms 목표 달성 가능
- INT4 양자화 적용 시 처리량 2~3x 향상, KV 캐시 최적화(StreamingVLM 방식) 추가 시 연속 스트림에서 안정적 지연 유지

**기술 트렌드**

- VLM 전용 양자화(MBQ)로 W4A8에서 정확도 손실 1.1% 이내 달성 → INT4 배포가 품질 타협 없이 가능한 수준에 도달
- llama.cpp의 VLM 지원(2025.05 libmtmd 병합)으로 CPU-only 엣지 서버에서도 소형 VLM 운용 가능
- NVIDIA TensorRT Edge-LLM이 오픈소스 공개 → 엣지 VLM 배포 표준 프레임워크로 자리잡을 가능성

**기회**

- 국내 통신사(SKT/KT)의 MEC 인프라에 Qwen2.5-VL-7B (INT4) 또는 MiniCPM-V 2.6 배포로 CCTV 이벤트 분석 서비스 조기 상용화 가능
- SmolVLM 계열의 초소형 모델을 단말에 탑재하여 프라이버시-보호형 온디바이스 비전 AI 서비스 차별화 가능
- 엣지-클라우드 분산 추론 아키텍처를 5G 네트워크 슬라이싱과 결합하여 SLA 기반 AI 추론 서비스 출시 가능

**위협**

- NVIDIA Jetson 플랫폼 생태계가 엣지 VLM 추론 표준을 선점하면 비 NVIDIA 하드웨어 기반 통신사 인프라에서 경쟁력 저하
- 실시간 CCTV 분석(8 FPS)은 H100 급 GPU 필요 → MEC 노드 GPU 업그레이드 비용 부담
- VLM 특화 양자화 기술의 급속한 발전으로 오픈소스 기반 자체 최적화 없이는 상용 솔루션에 종속 위험

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- Moondream 2B INT4의 RTX 3090 실측 수치 (184 tokens/s, 2.45GB) — HuggingFace 공개 모델 카드 기반 [A]
- SmolVLM-256M의 0.8GB VRAM, 80 tokens/s (M4 Max) — ArXiv 논문 + HuggingFace [A]
- MBQ의 W4A8 정확도 손실 1.1% — CVPR 2025 peer-reviewed 논문 [A]
- StreamingVLM 8 FPS on H100 — MIT Han Lab 논문 [A]
- MEC 기본 지연 20ms 이하 — ETSI 표준 기반 IBM/RedHat 문서 [B]
- 2026년 추론 칩 시장 500억 달러 — Deloitte TMT 2026 Predictions [B]

**추가 검증 필요 [C/D]:**
- Qwen2.5-VL-7B FP16 기준 17GB VRAM 수치 — 비공식 블로그/포럼 원본, 공식 문서 교차 검증 필요 [C]
- 분산 추론 29~33% 처리량 향상 — 학술 논문이나 소규모 실험 기반, 실제 MEC 환경 검증 필요 [C]
- China Telecom AI Flow 전략 구체적 배포 현황 — ITU 발표 수준, 상용 성과 미확인 [C]

**데이터 공백:**
- 국내 통신사(SKT/KT) MEC 노드의 GPU 사양 및 현재 AI 워크로드 현황 — 비공개
- MEC 환경에서 VLM 실시간 추론의 실제 종단간 지연 측정값
- VideoScan/StreamingVLM의 실제 CCTV 환경(다중 카메라) 배포 사례

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Deloitte — 2026 AI Compute Predictions | [링크](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/compute-power-ai.html) | report | 2025 | [B] |
| <a id="ref-g-02"></a>G-02 | Stellarix — The Rise of MEC | [링크](https://stellarix.com/insights/articles/the-rise-of-multi-access-edge-computing-mec/) | news | 2025 | [B] |
| <a id="ref-g-03"></a>G-03 | IBM — What is MEC | [링크](https://www.ibm.com/think/topics/multi-access-edge-computing) | blog | 2025 | [B] |
| <a id="ref-g-04"></a>G-04 | Lanner Electronics — GTC 2026 Edge AI | [링크](https://www.lannerinc.com/news-and-events/latest-news/gtc-2026-purpose-built-edge-ai-for-infrastructure) | news | 2026 | [B] |
| <a id="ref-g-05"></a>G-05 | ITU AI for Good — China Telecom AI Flow | [링크](https://aiforgood.itu.int/china-telecom-drives-ubiquitous-intelligence-through-ai-flow/) | news | 2025 | [B] |
| <a id="ref-g-06"></a>G-06 | NVIDIA Technical Blog — TensorRT Edge-LLM | [링크](https://developer.nvidia.com/blog/accelerating-llm-and-vlm-inference-for-automotive-and-robotics-with-nvidia-tensorrt-edge-llm) | blog | 2025 | [A] |
| <a id="ref-g-07"></a>G-07 | vLLM Recipes — Qwen2.5-VL Usage Guide | [링크](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen2.5-VL.html) | blog | 2025 | [B] |
| <a id="ref-g-08"></a>G-08 | Nature Communications — MiniCPM-V 2.6 | [링크](https://www.nature.com/articles/s41467-025-61040-5) | paper | 2025 | [A] |
| <a id="ref-g-09"></a>G-09 | Moondream Blog — 2025-04-14 Release | [링크](https://moondream.ai/blog/moondream-2025-04-14-release) | blog | 2025-04-14 | [B] |
| <a id="ref-g-10"></a>G-10 | OpenReview — SmolVLM Paper | [링크](https://openreview.net/forum?id=qMUbhGUFUb) | paper | 2025 | [A] |
| <a id="ref-g-11"></a>G-11 | arXiv — StreamingVLM (abs) | [링크](https://arxiv.org/abs/2510.09608) | paper | 2025-10 | [A] |
| <a id="ref-g-12"></a>G-12 | Novita AI — Qwen2.5-VL VRAM Guide | [링크](https://blogs.novita.ai/qwen2-5-vl-72b-vram/) | blog | 2025 | [C] |
| <a id="ref-g-13"></a>G-13 | HuggingFace — Qwen2.5-VL-72B VRAM Discussion | [링크](https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct/discussions/3) | forum | 2025 | [C] |
| <a id="ref-g-14"></a>G-14 | NVIDIA Developer — Jetson Edge AI Getting Started | [링크](https://developer.nvidia.com/blog/getting-started-with-edge-ai-on-nvidia-jetson-llms-vlms-and-foundation-models-for-robotics) | blog | 2025 | [A] |
| <a id="ref-g-15"></a>G-15 | NVIDIA Developer — Jetson Benchmarks | [링크](https://developer.nvidia.com/embedded/jetson-benchmarks) | blog | 2025 | [A] |
| <a id="ref-g-16"></a>G-16 | LearnOpenCV — VLM on Edge Devices | [링크](https://learnopencv.com/vlm-on-edge-devices/) | blog | 2025 | [B] |
| <a id="ref-g-17"></a>G-17 | Jarvislabs — LLM Quantization Complete Guide | [링크](https://docs.jarvislabs.ai/blog/vllm-quantization-complete-guide-benchmarks) | blog | 2025 | [B] |
| <a id="ref-g-18"></a>G-18 | ionio.ai — GGUF vs AWQ vs GPTQ | [링크](https://www.ionio.ai/blog/llms-on-cpu-the-power-of-quantization-with-gguf-awq-gptq) | blog | 2025 | [B] |
| <a id="ref-g-19"></a>G-19 | LocalAIMaster — Quantization Comparison 2026 | [링크](https://localaimaster.com/blog/quantization-explained) | blog | 2026 | [C] |
| <a id="ref-g-20"></a>G-20 | GPUStack — Impact of Quantization on vLLM | [링크](https://docs.gpustack.ai/2.0/performance-lab/references/the-impact-of-quantization-on-vllm-inference-performance/) | blog | 2025 | [B] |
| <a id="ref-g-21"></a>G-21 | Red Hat Developer — vLLM vs llama.cpp | [링크](https://developers.redhat.com/articles/2025/09/30/vllm-or-llamacpp-choosing-right-llm-inference-engine-your-use-case) | blog | 2025-09 | [B] |
| <a id="ref-g-22"></a>G-22 | BentoML — Benchmarking LLM Inference Backends | [링크](https://www.bentoml.com/blog/benchmarking-llm-inference-backends) | blog | 2025 | [B] |
| <a id="ref-g-23"></a>G-23 | NVIDIA Technical Blog — NVIDIA Dynamo | [링크](https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/) | blog | 2025 | [A] |
| <a id="ref-g-24"></a>G-24 | Simon Willison — llama.cpp vision support (May 2025) | [링크](https://simonwillison.net/2025/May/10/llama-cpp-vision/) | blog | 2025-05 | [B] |
| <a id="ref-g-25"></a>G-25 | arxiv — 5G Edge Architecture for CV Offloading | [링크](https://arxiv.org/html/2501.04267v1) | paper | 2025-01 | [A] |
| <a id="ref-g-26"></a>G-26 | RD World — 2026 AI: Inference at the Edge | [링크](https://www.rdworldonline.com/2026-ai-story-inference-at-the-edge-not-just-scale-in-the-cloud/) | news | 2026 | [B] |
| <a id="ref-p-01"></a>P-01 | Li et al. — MBQ: Modality-Balanced Quantization for Large VLMs | [링크](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_MBQ_Modality-Balanced_Quantization_for_Large_Vision-Language_Models_CVPR_2025_paper.pdf) | paper | 2025 | [A] |
| <a id="ref-p-02"></a>P-02 | HuggingFace et al. — SmolVLM: Redefining small efficient multimodal models | [링크](https://arxiv.org/html/2504.05299v1) | paper | 2025-04 | [A] |
| <a id="ref-p-03"></a>P-03 | MIT Han Lab et al. — StreamingVLM: Real-Time Understanding for Infinite Video Streams | [링크](https://arxiv.org/abs/2510.09608) | paper | 2025-10 | [A] |
| <a id="ref-p-04"></a>P-04 | VideoScan et al. — Enabling Efficient Streaming Video Understanding | [링크](https://arxiv.org/abs/2503.09387) | paper | 2025-03 | [A] |
| <a id="ref-p-05"></a>P-05 | OpenBMB team — Efficient GPT-4V level MLLM for edge (Nature Communications) | [링크](https://www.nature.com/articles/s41467-025-61040-5) | paper | 2025 | [A] |
| <a id="ref-p-06"></a>P-06 | Columbia Univ — Distributed VLMs: Cloud-Edge Collaboration | [링크](https://wimnet.ee.columbia.edu/wp-content/uploads/2025/04/DistributedVLMs_Efficient_Vision-Language_Processing_through_Cloud-Edge_Collaboration.pdf) | paper | 2025-04 | [A] |
| <a id="ref-p-07"></a>P-07 | Comparative Study: MLX, MLC-LLM, Ollama, llama.cpp (arXiv 2411.05502) | [링크](https://arxiv.org/pdf/2511.05502) | paper | 2024-11 | [A] |
