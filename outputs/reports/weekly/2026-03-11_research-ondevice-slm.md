---
type: weekly-research
domain: secure-ai
l3_topic: ondevice-slm
period: 2026-03-04 ~ 2026-03-11
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
prev_report: 2026-03-05_research-ondevice-slm.md
---

# OnDevice sLM — 심층 리서치

> 기간: 2026-03-04 ~ 2026-03-11

---

## 기술 동향

이번 주(2026-03-04~03-11)는 **두 가지 주요 기술 이벤트**가 동시에 발생했다: Gemma 3n 오픈소스 정식 출시(2026-02-27 발표, 이번 주 생태계 통합 완료)와 Alibaba Qwen3.5 Small 시리즈 오픈소스 공개(2026-03-02). 두 사건 모두 "모바일 온디바이스 멀티모달 sLM의 오픈소스화"라는 동일한 방향을 가리키고 있다.

**Gemma 3n 오픈소스 생태계 통합 완료** [[G-01]](#ref-g-01)

Google이 I/O 2025에서 프리뷰로 공개한 Gemma 3n(E2B/E4B)가 HuggingFace Transformers, MLX, llama.cpp, Transformers.js, Ollama, Google AI Edge 등 주요 오픈소스 라이브러리에 전체 통합되었다. 이번 주 시점에서 개발자가 별도 설정 없이 기존 워크플로우에서 바로 활용 가능한 상태로 진입했다.

핵심 아키텍처 혁신 두 가지가 온디바이스 sLM 설계 철학의 전환점을 나타낸다:

- **MatFormer (Matryoshka Transformer)**: 하나의 대형 모델 안에 중첩된 소형 서브모델을 포함한 탄성 추론(elastic inference) 아키텍처. E4B(총 8B 파라미터) 훈련 중 E2B(총 5B 파라미터) 서브모델이 동시 최적화됨. 요청 복잡도에 따라 동적으로 활성화할 파라미터를 선택해 에너지 효율을 극대화한다 [[G-02]](#ref-g-02).
- **Per-Layer Embeddings (PLE)**: 각 레이어에 연관된 임베딩 파라미터를 GPU/TPU 가속기 외부(CPU + 빠른 스토리지)에서 처리·캐시하는 기법. 결과적으로 E2B(실효 2B)는 ~2GB, E4B(실효 4B)는 ~3GB의 메모리만 가속기에 상주시킨다. 총 파라미터 대비 메모리 풋프린트를 약 60% 절감하면서 모델 품질을 유지한다 [[G-02]](#ref-g-02).

MediaTek Dimensity 9500 NPU 기반 실측에서 Gemma 3n E2B가 **prefill 1,600 tokens/sec, decode 28 tokens/sec** (4K 컨텍스트, NPU)를 달성했다 [[G-03]](#ref-g-03). CPU 대비 12배, GPU 대비 10배 가속이다.

**Qwen3.5 Small 시리즈 오픈소스 공개 (2026-03-02)** [[G-04]](#ref-g-04)

Alibaba가 Qwen3.5-0.8B, 2B, 4B, 9B 전 시리즈를 Apache 2.0으로 공개했다. 아키텍처 특징:

- **네이티브 멀티모달 Early Fusion**: 기존 방식처럼 비전 인코더를 사후 결합하는 대신, 텍스트·이미지·비디오 토큰을 훈련 초기부터 통합 학습. 단일 백본으로 텍스트+이미지+비디오 처리가 가능하다.
- **하이브리드 Attention (Gated DeltaNet + Full Attention)**: 4개 Transformer 블록 중 3개는 Gated DeltaNet(선형 어텐션)을 사용해 긴 컨텍스트를 효율적으로 처리하고, 1개만 전통적인 이차(quadratic) 어텐션을 유지해 정밀한 정보 검색을 담당한다 [[G-05]](#ref-g-05). 262K 네이티브 컨텍스트 윈도우를 지원한다.
- **0.8B 모델이 최초로 온디바이스 비디오 처리**: 60초 분량(8 FPS) 비디오 오프라인 요약 및 공간 추론 지원. 2~3GB 메모리 기기에서 실행 가능 [[G-04]](#ref-g-04).
- 성능: 9B 모델이 GPQA Diamond에서 81.7점 — OpenAI GPT-OSS-120B(71.5점)를 13.5배 작은 크기로 상회 [[G-05]](#ref-g-05).

**에지 추론 논문 신규 시그널** [[P-01]](#ref-p-01)

2026-03 arXiv에 "Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices"가 게재되었다. 핵심 기여: 멀티에이전트 환경에서 각 에이전트의 KV 캐시를 4-bit 양자화하여 디스크에 영속 저장하고, 필요 시 Attention 레이어에 직접 복원하는 방식으로 O(n) Prefill 재연산을 제거한다. Apple M4 Pro에서 Gemma 3 12B 기준 TTFT(Time to First Token)를 **22~136배** 단축(4K~32K 컨텍스트). Q4 양자화로 메모리를 FP16 대비 4배 절감하며, 퍼플렉시티 손실은 -0.7%~+3.0% 수준이다.

**NVIDIA Nemotron-H 기술적 방향성 확인** [[G-06]](#ref-g-06)

NVIDIA가 2025-12에 공개한 Nemotron-H는 하이브리드 Mamba-Transformer MoE 아키텍처로, 4개 Transformer 블록 중 일부만 Full Attention을 사용하고 나머지는 Mamba-2로 대체한다. Nemotron 3 Nano(30B 총 파라미터, 3B 활성)가 이미 출시 상태이며, 2026년 상반기에 Super/Ultra 버전이 나온다. 이 아키텍처는 에지 배포 대상이 아닌 서버(DGX Spark, H100, B200)를 타겟으로 하지만, **하이브리드 Attention 설계 패턴이 Qwen3.5와 함께 주류로 자리잡는 추세**를 반증한다.

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| Google | Gemma 3n E2B/E4B 오픈소스 전체 생태계 통합 완료(2026-02-27). HuggingFace Transformers, MLX, llama.cpp, Ollama 등 주요 라이브러리 즉시 사용 가능. Gemma 3 1B는 모바일 GPU에서 2,585 tokens/sec prefill 달성 | [[G-01]](#ref-g-01) |
| Alibaba (Qwen) | Qwen3.5-0.8B/2B/4B/9B Apache 2.0 오픈소스 공개(2026-03-02). 0.8B 모델이 최초로 온디바이스 비디오 처리(60초, 8FPS) 지원. 9B가 GPT-OSS-120B GPQA Diamond 점수 초과 | [[G-04]](#ref-g-04), [[G-05]](#ref-g-05) |
| Apple | iOS 26/macOS 26 Foundation Models 프레임워크에서 ~3B 온디바이스 모델을 개발자에게 공개. Qwen-2.5-3B 전 언어 성능 초과. 2-bit QAT 및 KV 캐시 공유로 메모리 최적화. 2026년 LLM 기반 Siri 전면 교체 예정 | [[G-07]](#ref-g-07) |
| Samsung | Galaxy S26 + Gauss2 Compact 온디바이스 전략 3원 구도(Gemini 에이전틱/Perplexity 웹/Bixby+Gauss2 온디바이스) 운영 중. MWC 2026에서 Galaxy AI 생태계 확장 발표 | [[G-08]](#ref-g-08) |
| Qualcomm | MWC 2026: Snapdragon 8 Elite Gen 5 NPU(~100 TOPS)로 13B 파라미터 모델 완전 온디바이스 실행 실증. Snapdragon Wear Elite로 웨어러블 최초 전용 NPU 탑재(2B 모델, 10 tokens/sec) | [[G-09]](#ref-g-09) |
| MediaTek | Dimensity 9500 NPU(~50 TOPS)에서 Gemma 3n E2B 1,600 tokens/sec prefill 달성. Google LiteRT NeuroPilot Stack으로 NPU-LLM 통합 표준화. 대상 모델: Qwen3-0.6B, Gemma-3-270M/1B, Gemma-3n-E2B | [[G-03]](#ref-g-03) |
| Meta | ExecuTorch 1.0(GA 2025-10)이 Instagram·WhatsApp·Messenger·Facebook 전체에서 수십억 사용자 대상 작동 중. React Native ExecuTorch 공개로 모바일 앱 개발 생태계 확장 | [[G-10]](#ref-g-10) |
| Hugging Face | SmolLM2(135M~1.7B) 배포 활성화. SmolVLM-256M이 300배 큰 모델을 1GB 미만 메모리로 초과하는 성능 달성 | [[G-11]](#ref-g-11) |
| SKT | MWC 2026에서 "풀스택 AI 컴퍼니" 선언. 42dot이 온디바이스 AI 기술 강화. A.X 모델(519B)의 트릴리언 파라미터급 확장 및 Edge AI 3대 축(AIDC, GPUaaS, Edge AI) 전략 발표 | [[G-12]](#ref-g-12) |
| KT | MWC 2026 포커스는 "AI for networks, networks for AI". Agentic Fabric(멀티에이전트 오케스트레이션 기업 AI OS) 강조. 온디바이스 직접 전략은 미공개 | [[G-12]](#ref-g-12) |

---

## 시장 시그널

- **오픈소스화 가속**: 이번 주 Gemma 3n 생태계 통합 완료 + Qwen3.5 Small Apache 2.0 공개로, 멀티모달 온디바이스 모델이 사실상 무료·상업 허용으로 진입 장벽이 제거되었다 [[G-01]](#ref-g-01)[[G-04]](#ref-g-04).
- **0.8B 파라미터 멀티모달의 임계값 돌파**: Qwen3.5-0.8B가 최초로 온디바이스 비디오 처리를 지원하면서, "서브 1B 모델 = 텍스트 전용"이라는 암묵적 한계가 깨졌다 [[G-04]](#ref-g-04).
- **MWC 2026 칩 벤더 실증**: Qualcomm과 MediaTek 모두 MWC 2026에서 13B 및 7B급 모델을 각각 온디바이스로 실행하는 실증을 공개 시연. "클라우드 폴백 없는 AI"가 마케팅에서 실제 스펙으로 전환되었다 [[G-09]](#ref-g-09)[[G-03]](#ref-g-03).
- **웨어러블 AI 첫 파도**: Qualcomm Snapdragon Wear Elite가 웨어러블용 전용 NPU를 최초로 도입(2B 모델, 10 tokens/sec). 스마트워치급 온디바이스 LLM 실용화의 시작점 [[G-09]](#ref-g-09).
- **통신사 Edge AI 진입**: SKT가 MWC 2026에서 Edge AI를 3대 인프라 축 중 하나로 명시 선언. 기존 클라우드 AI 데이터센터 중심에서 엣지로의 전략 전환 신호 [[G-12]](#ref-g-12).
- **SLM 시장 성장률**: 온프레미스/엣지 LLM 배포가 LLM 시장의 51.85%를 점유하며 27.25% CAGR로 성장 중(2031년까지). Gartner는 2027년까지 기업의 SLM 사용량이 LLM 대비 3배가 될 것으로 예측 [[G-13]](#ref-g-13).
- **하이브리드 Attention 아키텍처 주류화**: Qwen3.5(Gated DeltaNet 혼합)와 NVIDIA Nemotron-H(Mamba-2 혼합) 등 선형+이차 어텐션 혼합 아키텍처가 에지 효율 설계의 공통 패턴으로 자리잡고 있다 [[G-05]](#ref-g-05)[[G-06]](#ref-g-06).
- **비용 효율 수치**: 7B SLM 서빙 비용이 70B~175B LLM 대비 10~30배 저렴하며, GPU·클라우드·에너지 비용을 최대 75% 절감 가능 [[G-13]](#ref-g-13).

---

## 학술 동향 (주요 논문)

**이번 주 신규 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices (익명 저자, 2026-03) | 에지 기기의 멀티에이전트 LLM 추론 시 KV 캐시를 Q4로 양자화해 디스크 영속 저장. Gemma 3 12B에서 TTFT 22~136배 단축(4K~32K 컨텍스트). Apple M4 Pro에서 FP16 대비 4배 메모리 절감 | [[P-01]](#ref-p-01) |
| Sometimes Painful but Promising: Feasibility and Trade-offs of On-Device Language Model Inference (arXiv 2503.09114, 2026-03) | CPU 기반(Raspberry Pi 5)과 GPU 가속(NVIDIA Jetson Orin Nano) 에지 기기에서 10B 미만 모델의 메모리·속도·에너지 실측 평가. 양자화가 병목을 줄이지만 완전히 제거하지 못함을 확인 | [[P-02]](#ref-p-02) |
| Feasibility and Trade-Offs of On-Device Language Model Inference (ACM TECS, 2026-03) | 컨텍스트 크기 증가 시 KV 캐시가 모델 가중치 메모리를 초과하는 현상 실증. 모바일 장기 컨텍스트 사용의 근본 제약 정량화 | [[P-03]](#ref-p-03) |
| Oaken: Online-Offline Hybrid KV Cache Quantization (ISCA 2026) | 온라인·오프라인 혼합 KV 캐시 양자화로 NVIDIA A100 대비 최대 1.58배 처리량 향상. 평균 정확도 손실 0.54% | [[P-04]](#ref-p-04) |

**이전 주요 논문 (맥락용)**

| 논문 | 핵심 | 출처 |
|------|------|------|
| Efficient Inference for Edge Large Language Models: A Survey (Tsinghua Science and Technology, 2026) | 양자화·Speculative Decoding·모델 오프로딩 체계적 분류. 에지 LLM 추론 최적화 종합 서베이 | [[P-05]](#ref-p-05) |
| Apple Intelligence Foundation Language Models Tech Report 2025 (arXiv 2507.13575) | Apple 온디바이스 3B 모델 아키텍처 상세. 2-bit QAT, KV 캐시 공유 기법 공개 | [[P-06]](#ref-p-06) |

---

## 이전 대비 변화

이번 주(03-04~03-11) 신규 시그널 vs. 직전 리포트(2026-03-05):

**신규 확인된 사항**
- Gemma 3n 오픈소스 생태계 통합 완료 (프리뷰 → 정식 사용 가능 전환). 직전 리포트에서는 "출시 임박"이었으나 이번 주 사용 가능 상태 확인 [[G-01]](#ref-g-01).
- Qwen3.5 Small(0.8B~9B) Apache 2.0 공개(2026-03-02). 직전 리포트에는 미포함. 0.8B 온디바이스 비디오 처리가 신규 임계값 돌파 시그널 [[G-04]](#ref-g-04).
- Persistent Q4 KV Cache 논문(arXiv 2603.04428) — 멀티에이전트 에지 추론의 실용적 병목 해결 방안 첫 실증 [[P-01]](#ref-p-01).
- MediaTek Dimensity 9500 실측 벤치마크 수치 확보: Gemma 3n E2B에서 NPU 1,600 tokens/sec prefill [[G-03]](#ref-g-03).
- MWC 2026 Qualcomm 발표: Snapdragon 8 Elite Gen 5에서 13B 파라미터 완전 온디바이스 실행 실증 공개 [[G-09]](#ref-g-09).

**직전 리포트에서 지속되는 시그널**
- Apple Foundation Models 3B 파라미터 온디바이스 모델 (iOS 26 일정 유지).
- ExecuTorch 1.0 GA 배포 확대 중 (수십억 사용자 대상 Meta 앱).
- 4-bit 양자화 표준화 추세 지속.
- 모바일 메모리 대역폭(50~90 GB/s) 병목 근본 미해결.

**이전 데이터 공백 → 이번 주 일부 해소**
- Samsung Gauss2 Compact 파라미터 수: 여전히 공개 정보 없음.
- 국내 통신사(SKT) 온디바이스 SLM 전략: MWC 2026에서 Edge AI 축 언급 확인(간접), 구체적 모델·스펙 미공개.

---

## 전략적 시사점

**기회**

- 멀티모달 오픈소스 sLM의 상업화 허용으로 엔터프라이즈 내부망 특화 파인튜닝 기회가 현실화되었다. Gemma 3n(Apache 2.0에 준하는 조건)과 Qwen3.5(Apache 2.0)가 무료 상업 허용으로 사용 가능하다 [[G-01]](#ref-g-01)[[G-04]](#ref-g-04).
- 0.8B 비디오 처리 지원으로 웨어러블·IoT·스마트홈 기기의 AI 파이프라인 설계 가능성이 열렸다. 저전력 에지 단말 대상 서비스 기회 [[G-04]](#ref-g-04).
- Persistent KV Cache 기법이 멀티에이전트 에지 추론의 실용 임계를 돌파함에 따라, 에지에서 복잡한 에이전틱 태스크를 수행하는 서비스 아키텍처 설계가 가능해지고 있다 [[P-01]](#ref-p-01).
- SKT의 Edge AI 인프라 투자 선언은 통신사 망 기반 온디바이스 AI 서비스 협력 채널 가능성을 시사한다 [[G-12]](#ref-g-12).

**위협**

- Qwen3.5 0.8B의 비디오 처리 지원은 Alibaba가 서브 1B 파라미터 시장에서도 Google(Gemma 3 270M)과 함께 주도권을 쥐기 시작했음을 의미한다. 중국 오픈소스 생태계가 글로벌 표준을 선점할 리스크가 증가한다 [[G-04]](#ref-g-04).
- 하이브리드 Attention 아키텍처(Gated DeltaNet, Mamba-2 혼합)가 복수 플레이어(Qwen3.5, NVIDIA Nemotron-H)에서 동시에 채택되며 빠르게 표준화되고 있다. 아키텍처 차별화 기간이 단축되고 있다 [[G-05]](#ref-g-05)[[G-06]](#ref-g-06).
- Qualcomm과 MediaTek이 각각 Snapdragon과 Dimensity NPU에 Google LiteRT를 통합함으로써 칩-프레임워크-모델 수직 통합을 강화하고 있다. 비벤더 독립 배포 솔루션의 입지가 좁아진다 [[G-03]](#ref-g-03)[[G-09]](#ref-g-09).
- 모바일 메모리 대역폭 병목은 하드웨어 혁신 없이 소프트웨어 단 최적화만으로는 해결이 불가능하다. 현재 50~90 GB/s vs. 데이터센터 2~3 TB/s의 30~50배 격차가 모바일 추론 상한선을 규정한다 [[G-14]](#ref-g-14).

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | HuggingFace Blog — Gemma 3n fully available in the open-source ecosystem | [링크](https://huggingface.co/blog/gemma3n) | news | 2026-02-27 | [A] |
| <a id="ref-g-02"></a>G-02 | Google Developers Blog — Introducing Gemma 3n (developer guide) | [링크](https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/) | news | 2025-05-20 | [A] |
| <a id="ref-g-03"></a>G-03 | Google Developers Blog — MediaTek NPU and LiteRT: Powering the next generation of on-device AI | [링크](https://developers.googleblog.com/mediatek-npu-and-litert-powering-the-next-generation-of-on-device-ai/) | news | 2025-12 | [A] |
| <a id="ref-g-04"></a>G-04 | MarkTechPost — Alibaba just released Qwen 3.5 Small Models | [링크](https://www.marktechpost.com/2026/03/02/alibaba-just-released-qwen-3-5-small-models-a-family-of-0-8b-to-9b-parameters-built-for-on-device-applications/) | news | 2026-03-02 | [B] |
| <a id="ref-g-05"></a>G-05 | StableLearn — Qwen3.5: 9B Beats 120B, 0.8B Runs Video on Phones | [링크](https://stable-learn.com/en/qwen35-native-multimodal-agent-model/) | news | 2026-03 | [B] |
| <a id="ref-g-06"></a>G-06 | NVIDIA Research — Nemotron-H: Hybrid Mamba-Transformer Models | [링크](https://research.nvidia.com/labs/adlr/nemotronh/) | news | 2025-12 | [A] |
| <a id="ref-g-07"></a>G-07 | Apple Machine Learning Research — Updates to Apple's On-Device and Server Foundation Language Models | [링크](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates) | news | 2025 | [A] |
| <a id="ref-g-08"></a>G-08 | Samsung Newsroom — Samsung Advances Galaxy AI and Its Connected Ecosystem at MWC 2026 | [링크](https://news.samsung.com/global/samsung-advances-galaxy-ai-and-its-connected-ecosystem-at-mwc-2026) | news | 2026-03 | [A] |
| <a id="ref-g-09"></a>G-09 | DEV Community — MWC 2026: What Every Developer Building AI Features Should Know | [링크](https://dev.to/giolaq/mwc-2026-what-every-developer-building-ai-features-should-know-1a45) | news | 2026-03 | [B] |
| <a id="ref-g-10"></a>G-10 | Arm Newsroom — ExecuTorch 1.0 GA Release | [링크](https://newsroom.arm.com/news/executorch-1-0-ga-release-edge-ai) | news | 2025-10 | [A] |
| <a id="ref-g-11"></a>G-11 | VentureBeat — Hugging Face SmolLM2 brings powerful models to smartphones | [링크](https://venturebeat.com/ai/ai-on-your-smartphone-hugging-faces-smollm2-brings-powerful-models-to-the-palm-of-your-hand) | news | 2025 | [B] |
| <a id="ref-g-12"></a>G-12 | Korea Tech Today — Korea's AI-Telco Moment: Strategic Signaling at MWC 2026 | [링크](https://koreatechtoday.com/koreas-ai-telco-moment-strategic-signaling-at-mwc-2026/) | news | 2026-03 | [B] |
| <a id="ref-g-13"></a>G-13 | Calmops — Small Language Models (SLMs) Complete Guide 2026: The Edge AI Revolution | [링크](https://calmops.com/ai/small-language-models-slm-complete-guide-2026/) | news | 2026 | [C] |
| <a id="ref-g-14"></a>G-14 | Meta AI Research (Vikas Chandra) — On-Device LLMs: State of the Union, 2026 | [링크](https://v-chandra.github.io/on-device-llms/) | news | 2026-01 | [B] |
| <a id="ref-g-15"></a>G-15 | Google DeepMind — Gemma 3n model page | [링크](https://deepmind.google/models/gemma/gemma-3n/) | news | 2026 | [A] |
| <a id="ref-g-16"></a>G-16 | InfoQ — Gemma 3n Introduces Novel Techniques for Enhanced Mobile AI Inference | [링크](https://www.infoq.com/news/2025/07/gemma-3n-architecture/) | news | 2025-07 | [B] |
| <a id="ref-g-17"></a>G-17 | VentureBeat — NVIDIA Nemotron 3 with hybrid MoE and Mamba-Transformer | [링크](https://venturebeat.com/ai/nvidia-debuts-nemotron-3-with-hybrid-moe-and-mamba-transformer-to-drive) | news | 2025-12 | [B] |
| <a id="ref-g-18"></a>G-18 | Edge AI and Vision Alliance — On-Device LLMs in 2026: What Changed, What Matters, What's Next | [링크](https://www.edge-ai-vision.com/2026/01/on-device-llms-in-2026-what-changed-what-matters-whats-next/) | news | 2026-01 | [B] |
| <a id="ref-g-19"></a>G-19 | PyTorch Blog — Introducing ExecuTorch 1.0 | [링크](https://pytorch.org/blog/introducing-executorch-1-0/) | news | 2025-10 | [A] |
| <a id="ref-g-20"></a>G-20 | Apple Newsroom — Apple's Foundation Models framework unlocks new intelligent app experiences | [링크](https://www.apple.com/newsroom/2025/09/apples-foundation-models-framework-unlocks-new-intelligent-app-experiences/) | news | 2025-09 | [A] |
| <a id="ref-p-01"></a>P-01 | 익명 저자 — Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices | [링크](https://arxiv.org/abs/2603.04428) | paper | 2026-03 | [B] |
| <a id="ref-p-02"></a>P-02 | 익명 저자 — Sometimes Painful but Promising: Feasibility and Trade-offs of On-Device Language Model Inference | [링크](https://arxiv.org/abs/2503.09114) | paper | 2026-03 | [B] |
| <a id="ref-p-03"></a>P-03 | 익명 저자 — Feasibility and Trade-Offs of On-Device Language Model Inference (ACM TECS) | [링크](https://dl.acm.org/doi/pdf/10.1145/3788870) | paper | 2026-03 | [A] |
| <a id="ref-p-04"></a>P-04 | 익명 저자 — Oaken: Fast and Efficient LLM Serving with Online-Offline Hybrid KV Cache Quantization (ISCA 2026) | [링크](https://dl.acm.org/doi/10.1145/3695053.3731019) | paper | 2026 | [A] |
| <a id="ref-p-05"></a>P-05 | 다수 저자 — Efficient Inference for Edge Large Language Models: A Survey | [링크](https://www.sciopen.com/article/10.26599/TST.2025.9010166) | paper | 2026 | [A] |
| <a id="ref-p-06"></a>P-06 | Apple — Apple Intelligence Foundation Language Models Tech Report 2025 | [링크](https://arxiv.org/abs/2507.13575) | paper | 2025 | [A] |
