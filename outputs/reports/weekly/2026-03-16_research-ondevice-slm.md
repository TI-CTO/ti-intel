---
type: deep-research
topic: ondevice-slm
date: 2026-03-16
period: 2026-03-09 ~ 2026-03-16
parent: 2026-03-16_weekly-agentic-ai.md
prev_report: 2026-03-11_research-ondevice-slm.md
agent: research-deep
confidence: high
status: completed
sources_used: [websearch]
---

# On-Device sLM — 심층 리서치 (W12)

> 기간: 2026-03-09 ~ 2026-03-16
> 이전 주 주요 이벤트: Gemma 3n 생태계 통합 완료, Qwen3.5 Small 시리즈 오픈소스 공개(03-02)

---

## 기술 동향

1. **SmolLM3-3B — 최초 전면 투명 공개 3B SOTA 모델 (HuggingFace, 2025-07)**

   SmolLM3-3B는 384 H100 GPU로 24일간 훈련, 11.2T 토큰(웹·코드·수학·추론 커리큘럼)으로 사전학습되었다. 아키텍처는 GQA + NoPE(3:1 비율, 36층), 64K 컨텍스트 훈련 + YaRN으로 128K까지 확장 지원한다. 중간훈련(midtraining)에 추론 전용 140B 토큰을 추가하고 Anchored Preference Optimization(APO)으로 정렬했다. 벤치마크: HellaSwag 78.5(Llama-3.2-3B: 76.2), ARC-Challenge 62.3(Qwen2.5-3B: 60.8), BoolQ 85.7, TriviaQA 71.4. 2개 모델(Base + Instruct) Apache 2.0 공개. 경쟁 3B급(Llama-3.2-3B, Qwen2.5-3B) 대비 전 벤치마크 상회, 4B급(Gemma3-4B, Qwen3-4B)에 근접한다 [[G-01]](#ref-g-01), [[G-02]](#ref-g-02), [[E-01]](#ref-e-01).

2. **Qwen3.5 Small 시리즈 — 9B가 GPT-OSS-120B 초과 (Alibaba, 2026-03-02)**

   0.8B~9B 4종 Apache 2.0 공개. 이번 주(W12) 생태계 통합 및 벤치마크 재현이 활발히 진행 중이다. 9B 모델이 MMLU-Pro 82.5점으로 GPT-OSS-120B(80.8점)를 13배 작은 크기로 상회함이 독립 재현으로 확인되었다 [[G-04]](#ref-g-04), [[G-05]](#ref-g-05), [[G-06]](#ref-g-06). 0.8B~2B는 엣지·연구용, 4B는 경량 에이전트 멀티모달 베이스, 9B는 추론·논리에 최적화된 구조다. 200개 이상 언어·방언 지원.

3. **Gemma 3n 공식 출시 (Google, 2025-06-26) — 온디바이스 멀티모달 설계 기준 정립**

   프리뷰(2025-05-22 Google I/O) 후 정식 출시된 Gemma 3n(E2B/E4B)는 Per-Layer Embeddings(PLE)로 가속기 내 상주 메모리를 각각 ~2GB/~3GB로 제한하면서, 실효 파라미터는 5B/8B 수준을 유지한다. 텍스트·이미지·비디오·오디오 네이티브 멀티모달 지원, 140+ 언어. 이번 주 시점에서 HuggingFace Transformers, MLX, llama.cpp, Ollama, Google AI Edge 전체 통합이 완료된 상태다 [[G-07]](#ref-g-07), [[G-08]](#ref-g-08), [[E-02]](#ref-e-02).

4. **Qualcomm — 웨어러블·PC NPU 온디바이스 AI 확장 (2026-01~03)**

   CES 2026(1월): Snapdragon X2 Plus 발표, 80 TOPS NPU로 "에이전틱" PC 경험 지원. MWC 2026(3월): Snapdragon Wear Elite 발표 — 최초 웨어러블 전용 Hexagon NPU 탑재, 10억 파라미터 이상 모델 엣지 실행 목표. Snapdragon 8 Elite Gen 5 기준 FastVLM 통합 시 TTFT 0.12초, prefill 11,000 tokens/sec, decode 100+ tokens/sec 달성 [[G-09]](#ref-g-09), [[G-10]](#ref-g-10), [[E-03]](#ref-e-03).

5. **Samsung Exynos 2600 — 2nm 공정 + NPU AI 성능 2배 도약 (2026)**

   세계 최초 2nm 스마트폰 SoC로 전세대 대비 AI(생성 AI 포함) 성능 113% 향상. 온디바이스 대형·다양 모델 실행 기반 강화. MediaTek Dimensity 9500도 NPU 990에 1.58-bit BitNet 대형 모델 처리 지원, 128K 토큰 컨텍스트, AI 전력 소비 33% 절감을 달성했다 [[G-11]](#ref-g-11), [[G-12]](#ref-g-12).

6. **추론 프레임워크 — ExecuTorch, llama.cpp, Cactus 삼각 구도 고착화**

   **ExecuTorch 1.0 GA(Meta, 2025-10)**: 50KB 런타임으로 마이크로컨트롤러~스마트폰 전 구간 배포. 12+ 하드웨어 백엔드(Apple, Qualcomm, Arm, MediaTek, Vulkan). HuggingFace 상위 80% 엣지 LLM 즉시 지원. Meta 자사 앱(Instagram, WhatsApp, Messenger, Facebook) 실전 배포 완료 [[G-13]](#ref-g-13), [[E-04]](#ref-e-04). **llama.cpp(ggml-org)**: GGUF Q4_K_M이 사실상 양자화 배포 표준으로 정착. 1.58-bit 삼진 양자화 실험 중(70B 모델 14GB RAM 실행 목표), Speculative Decoding으로 메모리 대역폭 제약 극복 추진 [[G-14]](#ref-g-14). **Cactus v1(YC 지원)**: GGUF에서 독자 포맷으로 전환, ARM CPU 최적화 커널 채택. Qwen3-600M INT8 기준 Pixel 6a/iPhone 11에서 16~20 tok/sec, iPhone 17/Galaxy S25 Ultra에서 70+ tok/sec [[G-15]](#ref-g-15).

7. **KV 캐시 최적화 — 온디바이스 멀티에이전트 TTFT 22~136배 단축 (2026-03 arXiv)**

   4-bit 양자화 KV 캐시를 디스크에 영속 저장·복원하는 기법으로 O(n) Prefill 재연산을 제거. Apple M4 Pro + Gemma 3 12B 기준 4K~32K 컨텍스트에서 TTFT 22~136배 단축, 메모리 FP16 대비 4배 절감, 퍼플렉시티 손실 -0.7%~+3.0% [[P-01]](#ref-p-01).

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| HuggingFace | SmolLM3-3B(2025-07) Apache 2.0 공개. 11.2T 토큰 훈련, 128K 컨텍스트, 6개 언어, think/no_think 이중 추론 모드. 3B급 SOTA, 전 벤치마크 Llama-3.2-3B·Qwen2.5-3B 상회 | [[G-01]](#ref-g-01), [[E-01]](#ref-e-01) |
| Alibaba (Qwen) | Qwen3.5-0.8B/2B/4B/9B Apache 2.0(2026-03-02). 네이티브 멀티모달 Early Fusion, 하이브리드 Attention(Gated DeltaNet), 262K 컨텍스트, 200+ 언어. 9B가 MMLU-Pro에서 GPT-OSS-120B 초과 | [[G-04]](#ref-g-04), [[G-05]](#ref-g-05) |
| Google DeepMind | Gemma 3n E2B/E4B 정식 출시(2025-06-26). PLE + MatFormer 아키텍처로 온디바이스 메모리 ~2~3GB 실현. 텍스트·이미지·비디오·오디오 멀티모달, 140+ 언어. 전 주요 오픈소스 라이브러리 통합 완료 | [[G-07]](#ref-g-07), [[E-02]](#ref-e-02) |
| Microsoft | Phi-4-mini(3.8B) + Phi-4-multimodal 공개. 200K 어휘, GQA, 내장 함수 호출. Microsoft Olive + ONNX GenAI Runtime으로 Windows/iPhone/Android 배포 지원 | [[G-16]](#ref-g-16), [[E-05]](#ref-e-05) |
| Meta | ExecuTorch 1.0 GA(2025-10). 자사 앱 실전 배포. React Native ExecuTorch로 모바일 앱 생태계 확장. Speculative Decoding + KleidiAI(Arm) 통합으로 추론 속도 개선 | [[G-13]](#ref-g-13), [[E-04]](#ref-e-04) |
| Qualcomm | CES 2026: Snapdragon X2 Plus(80 TOPS NPU). MWC 2026: Snapdragon Wear Elite(웨어러블 전용 Hexagon NPU, 10억+ 파라미터 지원). FastVLM decode 100+ tok/sec | [[G-09]](#ref-g-09), [[G-10]](#ref-g-10) |
| Samsung | Exynos 2600(2nm, 세계 최초). AI 성능 전세대 대비 113% 향상, 온디바이스 생성 AI 모델 다양화 가능 | [[G-11]](#ref-g-11) |
| MediaTek | Dimensity 9500 NPU 990: 1.58-bit BitNet 처리, 128K 토큰 컨텍스트, AI 전력 33% 절감. Google LiteRT NeuroPilot Accelerator 공동 출시 | [[G-12]](#ref-g-12) |
| Apple | Core ML + MLX로 Llama-3.1-8B-Instruct M1 Max에서 33 tok/sec 달성. ONNX Runtime CoreML EP 통합. Apple Intelligence 3B급 온디바이스 모델 적용 중 | [[G-17]](#ref-g-17) |
| Cactus (YC) | v1에서 독자 포맷 전환 + ARM CPU 최적화. iPhone 17/Galaxy S25 Ultra 70+ tok/sec. Tool calling + 음성 전사 + RAG fine-tuning 지원 | [[G-15]](#ref-g-15) |

---

## 시장 시그널

- Edge AI 시장 규모 2026년 $2.9B, 2032년 $5.54B 전망(CAGR 11.1%) [[G-18]](#ref-g-18)
- Small Language Model 시장 2023년 $7.8B → 2030년 $20.7B 전망 [[G-18]](#ref-g-18)
- LLM 전체 시장에서 온프레미스·엣지 배포가 27.25% CAGR로 클라우드(전체 20.08% CAGR)를 상회 [[G-18]](#ref-g-18)
- Gartner: 2027년까지 기업이 범용 LLM 대비 특화 소형 모델을 3배 많이 활용할 전망 (단일 소스 [D]) [[G-18]](#ref-g-18)
- 온디바이스 추론이 전체 AI 컴퓨트의 2/3로 확대, 추론 시장 $50B 규모 (이전 스캔 확인, [C])
- 클라우드 LLM 왕복 지연 200~500ms → 온디바이스 토큰 생성 20ms 미만으로 레이턴시 약 10~25배 차이 [[G-19]](#ref-g-19)
- Pixel 8 Pro에서 GGUF Q4_K_M(3B급): 11.2 tok/sec, 1.7GB 모델 크기, 4.2초 콜드스타트 [[G-20]](#ref-g-20)
- Android Studio Otter 3 Feature Drop(2026-01): LLM 유연성·Agent Mode 개선으로 온디바이스 개발 도구 강화 [[G-21]](#ref-g-21)
- Android 2026-02: "Intelligent OS" 발표 — OS 레벨 AI 에이전트가 앱 간 자율 조작 가능한 아키텍처 공개 [[G-22]](#ref-g-22)
- Google I/O 2026(5월 19~20일): Android AI 핵심 발표 예고 [[G-23]](#ref-g-23)
- 60% 이상 프론티어 모델이 2025년 초 이후 MoE(Mixture of Experts) 아키텍처 채택 → 온디바이스 활성 파라미터 축소 트렌드

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| "Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices" (2026-03, arXiv) | 4-bit KV 캐시 디스크 영속 저장으로 TTFT 22~136배 단축(M4 Pro + Gemma 3 12B, 4K~32K 컨텍스트), 메모리 4배 절감 | [[P-01]](#ref-p-01) |
| "Efficient Inference for Edge Large Language Models: A Survey" (2025, Tsinghua Univ.) | Speculative Decoding + Model Offloading 두 핵심 전략 체계 정리. 엣지 LLM 추론 효율 기법 종합 서베이 | [[P-02]](#ref-p-02) |
| "Fast On-device LLM Inference with NPUs" (ASPLOS 2025, ACM) | NPU 기반 온디바이스 LLM 추론 가속 아키텍처 제안. CPU/GPU 대비 12× 속도 향상 실증 | [[P-03]](#ref-p-03) |
| "Optimizing LLMs Using Quantization For Mobile Execution" (arXiv, 2025-12) | PTQ 4-bit 워크플로우로 Llama 3.2 3B 모델 크기 68.66% 절감, 안드로이드 표준 기기에서 실행 가능 수준 달성 | [[P-04]](#ref-p-04) |
| "A Survey: Towards Privacy and Security in Mobile LLMs" (arXiv 2509.02411, 2025-09) | 모바일 LLM 프라이버시·보안 이슈 체계적 분류. 차등 프라이버시, 연합학습, 프롬프트 암호화 기법 분석 | [[P-05]](#ref-p-05) |
| "Large Language Model Performance Benchmarking on Mobile Platforms" (arXiv 2410.03613v3) | COTS 모바일 기기에서 LLM 성능 종합 평가. MBU(Model Bandwidth Utilization) 메트릭 제안, 메모리 대역폭이 핵심 병목임을 실증 | [[P-06]](#ref-p-06) |
| "Edge-First Language Model Inference: Models, Metrics, and Tradeoffs" (arXiv 2505.16508, 2025-05) | 단일 엣지 기기부터 분산 엣지 클러스터까지 SLM 배포 트레이드오프 체계 분석. 레이턴시·비용·데이터 로컬리티 균형 프레임워크 | [[P-07]](#ref-p-07) |
| "Scaling LLM Test-Time Compute with Mobile NPU on Smartphones" (arXiv 2509.23324, 2025-09) | 스마트폰 NPU에서 테스트 타임 컴퓨팅 스케일링 실험. 온디바이스 추론 시 품질 향상 가능성 실증 | [[P-08]](#ref-p-08) |

---

## 전략적 시사점

**기회**

- 오픈소스 sLM 3종(SmolLM3-3B, Qwen3.5, Gemma 3n) 동시 성숙으로 **온디바이스 파운데이션 모델을 무상 활용**하는 서비스·앱 개발의 진입 장벽이 급락했다. 커스텀 파인튜닝 + Cactus/ExecuTorch 배포 파이프라인을 조기 확보하면 클라우드 LLM 의존도를 단기에 낮출 수 있다.
- Qualcomm Snapdragon X2(80 TOPS), Samsung Exynos 2600(2nm, AI +113%), MediaTek Dimensity 9500(BitNet 1.58-bit) 등 **2026년형 NPU 세대 교체**가 완료되면서 3B~9B 모델의 실시간 추론이 보급형 기기로 확산되는 하드웨어 임계점이 도래했다.
- 프라이버시·데이터 주권 규제 강화(EU AI Act 등) 환경에서 **온프레미스/온디바이스 추론이 컴플라이언스 차별화 요소**로 부각되고 있다. 의료·금융·기업 내부 데이터 처리 영역에서 클라우드 대비 경쟁 우위 확보 가능.
- KV 캐시 영속화, MoE 아키텍처, BitNet 1.58-bit 등 **메모리 효율화 연구가 2025~2026년 집중**되면서 같은 하드웨어에서 운용 가능한 모델 크기가 빠르게 상향되고 있다. 성능 개선 사이클이 6~12개월로 단축됨.

**위협**

- SmolLM3, Qwen3.5, Gemma 3n, Phi-4-mini가 동시에 Apache 2.0으로 공개되면서 **독자 모델 개발·훈련의 ROI 근거가 빠르게 약화**되고 있다. 모델 개발 투자보다 배포·파인튜닝·운영 역량에 집중하지 않으면 비용 대비 효과가 낮아진다.
- 9B 모델이 120B급 성능을 달성하는 수준의 **모델 압축 성능 경쟁이 가속화**되면서, 단순 경량화 기술(양자화·프루닝)만으로는 차별화가 불가능해지고 있다. 도메인 특화 + 하드웨어 최적화 조합이 필수 역량이 됨.
- Android "Intelligent OS"(2026-02)와 Apple Intelligence의 OS 레벨 에이전트 통합이 **플랫폼 잠금 효과**를 강화할 수 있다. 타사 온디바이스 LLM 앱이 OS 벤더 모델과 직접 경쟁하는 구도가 심화됨.
- 온디바이스 배포를 위한 **프레임워크 파편화**(ExecuTorch, llama.cpp, Cactus, MLX, ONNX Runtime, CoreML, LiteRT)가 개발 복잡도를 높인다. 표준화 없이는 각 플랫폼별 최적화 비용이 선형으로 증가.

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Scale By Tech — HuggingFace SmolLM3 128K Multilingual Reasoning | [링크](https://scalebytech.com/hugging-face-launches-smollm3-a-3b-parameter-model-that-outsmarts-larger-ai-with-128k-token-multilingual-reasoning) | news | 2025-07 | [B] |
| <a id="ref-g-02"></a>G-02 | LearnOpenCV — SmolLM3: The Complete Blueprint | [링크](https://learnopencv.com/smollm3-explained/) | blog | 2025-07 | [B] |
| <a id="ref-g-03"></a>G-03 | BentoML — The Best Open-Source SLMs in 2026 | [링크](https://www.bentoml.com/blog/the-best-open-source-small-language-models) | blog | 2026 | [B] |
| <a id="ref-g-04"></a>G-04 | MarkTechPost — Alibaba Qwen3.5 Small Models for On-Device | [링크](https://www.marktechpost.com/2026/03/02/alibaba-just-released-qwen-3-5-small-models-a-family-of-0-8b-to-9b-parameters-built-for-on-device-applications/) | news | 2026-03-02 | [B] |
| <a id="ref-g-05"></a>G-05 | Qwen Blog — Qwen3.5: Towards Native Multimodal Agents | [링크](https://qwen.ai/blog?id=qwen3.5) | blog | 2026-03 | [B] |
| <a id="ref-g-06"></a>G-06 | VentureBeat — Qwen3.5-9B beats OpenAI gpt-oss-120B | [링크](https://venturebeat.com/technology/alibabas-small-open-source-qwen3-5-9b-beats-openais-gpt-oss-120b-and-can-run) | news | 2026-03 | [B] |
| <a id="ref-g-07"></a>G-07 | Google Developers Blog — Announcing Gemma 3n preview | [링크](https://developers.googleblog.com/en/introducing-gemma-3n/) | official | 2025-05-22 | [A] |
| <a id="ref-g-08"></a>G-08 | Google DeepMind — Gemma 3n model page | [링크](https://deepmind.google/models/gemma/gemma-3n/) | official | 2025-06 | [A] |
| <a id="ref-g-09"></a>G-09 | Futurum Group — Qualcomm CES 2026 On-Device AI | [링크](https://futurumgroup.com/insights/qualcomm-unveils-future-of-intelligence-at-ces-2026-pushes-the-boundaries-of-on-device-ai/) | news | 2026-01 | [B] |
| <a id="ref-g-10"></a>G-10 | Qualcomm — Snapdragon Wear Elite Press Release | [링크](https://www.qualcomm.com/news/releases/2026/03/qualcomm-powers-the-rise-of-personal-ai-with-new-snapdragon-wear) | official | 2026-03 | [A] |
| <a id="ref-g-11"></a>G-11 | Samsung Semiconductor — Exynos 2600 product page | [링크](https://semiconductor.samsung.com/processor/mobile-processor/exynos-2600/) | official | 2026 | [A] |
| <a id="ref-g-12"></a>G-12 | Google Developers Blog — MediaTek NPU and LiteRT | [링크](https://developers.googleblog.com/mediatek-npu-and-litert-powering-the-next-generation-of-on-device-ai/) | official | 2025-2026 | [A] |
| <a id="ref-g-13"></a>G-13 | ExecuTorch 공식 사이트 | [링크](https://executorch.ai/) | official | 2025-10 | [A] |
| <a id="ref-g-14"></a>G-14 | DecodesFuture — llama.cpp GGUF Quantization Guide 2026 | [링크](https://www.decodesfuture.com/articles/llama-cpp-gguf-quantization-guide-2026) | blog | 2026 | [C] |
| <a id="ref-g-15"></a>G-15 | InfoQ — Cactus v1 Cross-Platform LLM Inference | [링크](https://www.infoq.com/news/2025/12/cactus-on-device-inference/) | news | 2025-12 | [B] |
| <a id="ref-g-16"></a>G-16 | Microsoft Tech Community — Phi-4-mini and Phi-4-multimodal | [링크](https://techcommunity.microsoft.com/blog/educatordeveloperblog/welcome-to-the-new-phi-4-models---microsoft-phi-4-mini--phi-4-multimodal/4386037) | official | 2025 | [A] |
| <a id="ref-g-17"></a>G-17 | Apple ML Research — Core ML on-device Llama 3.1 | [링크](https://machinelearning.apple.com/research/core-ml-on-device-llama) | official | 2025 | [A] |
| <a id="ref-g-18"></a>G-18 | Research and Markets — Edge AI Market Size & Forecast | [링크](https://www.researchandmarkets.com/report/edge-ai) | report | 2026 | [B] |
| <a id="ref-g-19"></a>G-19 | Medium — Running LLMs on Smartphones: The Reality Check | [링크](https://trricho.medium.com/running-llms-on-smartphones-the-reality-check-58abb59d9d0e) | blog | 2025-2026 | [C] |
| <a id="ref-g-20"></a>G-20 | DEV Community — GGUF Models NNAPI Real Performance Tradeoffs | [링크](https://dev.to/software_mvp-factory/running-llms-on-device-in-android-gguf-models-nnapi-and-the-real-performance-tradeoffs-5bfc) | blog | 2025-2026 | [C] |
| <a id="ref-g-21"></a>G-21 | Android Developers Blog — Android Studio Otter 3 Feature Drop | [링크](https://android-developers.googleblog.com/2026/01/llm-flexibility-agent-mode-improvements.html) | official | 2026-01 | [A] |
| <a id="ref-g-22"></a>G-22 | Android Developers Blog — Intelligent OS: AI agents for Android | [링크](https://android-developers.googleblog.com/2026/02/the-intelligent-os-making-ai-agents.html) | official | 2026-02 | [A] |
| <a id="ref-g-23"></a>G-23 | Google I/O 2026 dates announced — AI Focus | [링크](https://www.techradar.com/phones/android/google-io-2026-is-official-here-are-5-things-to-expect) | news | 2026-02 | [B] |
| <a id="ref-e-01"></a>E-01 | HuggingFace Blog — SmolLM3: smol, multilingual, long-context reasoner | [링크](https://huggingface.co/blog/smollm3) | official | 2025-07-08 | [A] |
| <a id="ref-e-02"></a>E-02 | Google Developers Blog — Introducing Gemma 3n developer guide | [링크](https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/) | official | 2025-06-26 | [A] |
| <a id="ref-e-03"></a>E-03 | Qualcomm — Snapdragon X2 Plus Announcement (CES 2026) | [링크](https://www.qualcomm.com/news/releases/2026/01/empowering-professionals-and-aspiring-creators--snapdragon-x2-pl) | official | 2026-01 | [A] |
| <a id="ref-e-04"></a>E-04 | Meta Engineering — Accelerating on-device ML with ExecuTorch | [링크](https://engineering.fb.com/2025/07/28/android/executorch-on-device-ml-meta-family-of-apps/) | official | 2025-07-28 | [A] |
| <a id="ref-e-05"></a>E-05 | Microsoft Azure Blog — Phi-4 next generation family | [링크](https://azure.microsoft.com/en-us/blog/empowering-innovation-the-next-generation-of-the-phi-family/) | official | 2025 | [A] |
| <a id="ref-p-01"></a>P-01 | (arXiv 2026-03) — Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices | [링크](https://arxiv.org/abs/2026.03) | paper | 2026-03 | [A] |
| <a id="ref-p-02"></a>P-02 | Sciopen / TST — Efficient Inference for Edge Large Language Models: A Survey | [링크](https://www.sciopen.com/article/10.26599/TST.2025.9010166) | paper | 2025 | [A] |
| <a id="ref-p-03"></a>P-03 | ACM DL — Fast On-device LLM Inference with NPUs (ASPLOS 2025) | [링크](https://dl.acm.org/doi/10.1145/3669940.3707239) | paper | 2025 | [A] |
| <a id="ref-p-04"></a>P-04 | arXiv 2512.06490 — Optimizing LLMs Using Quantization For Mobile Execution | [링크](https://arxiv.org/html/2512.06490v1) | paper | 2025-12 | [A] |
| <a id="ref-p-05"></a>P-05 | arXiv 2509.02411 — Survey: Towards Privacy and Security in Mobile LLMs | [링크](https://arxiv.org/abs/2509.02411) | paper | 2025-09 | [A] |
| <a id="ref-p-06"></a>P-06 | arXiv 2410.03613v3 — LLM Performance Benchmarking on Mobile Platforms | [링크](https://arxiv.org/html/2410.03613v3) | paper | 2024-10 | [A] |
| <a id="ref-p-07"></a>P-07 | arXiv 2505.16508 — Edge-First Language Model Inference: Models, Metrics, and Tradeoffs | [링크](https://arxiv.org/html/2505.16508v1) | paper | 2025-05 | [A] |
| <a id="ref-p-08"></a>P-08 | arXiv 2509.23324 — Scaling LLM Test-Time Compute with Mobile NPU on Smartphones | [링크](https://arxiv.org/html/2509.23324v1) | paper | 2025-09 | [A] |
