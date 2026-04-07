---
type: weekly-deep-research
domain: agentic-ai
l3: edge-ai
date: 2026-04-06
signal: 🟡
---

# Deep 리서치: Edge AI (2026-04-06)

## 이전 대비 변화
- 전주(W16): TI TinyEngine NPU 90x 저지연·120x 에너지 효율 발표, 추론 최적화 칩 시장 $50B 전망, 서브 1B 파라미터 모델 실용화 변곡점
- 금주(W17): Embedded World 2026 후속으로 주요 벤더 제품 출시 구체화 — ASUS UGen300(Hailo-10H, 40 TOPS, 2.5W) 출시 발표(4/1), Nordic Axon NPU CPU 대비 15x 추론 향상, MediaTek Genio 420 샘플링 시작(4월)
- 변화 방향: PoC·발표 단계에서 **양산 및 실구매 가능 제품으로 전환 가속** — USB 폼팩터 AI 가속기, $1 이하 AI MCU 등 가격 장벽 붕괴 시작

---

## 기술 동향

1. **ASUS UGen300 출시 — USB-C 플러그인 엣지 AI 추론 가속기.**
   2026년 4월 1일 ASUS가 발표한 UGen300은 Hailo-10H 신경 처리 장치(Neural Processing Unit, NPU)를 탑재해 40 AI TOPS 성능을 2.5W 전력으로 제공한다. 105×50×18mm 크기에 8GB LPDDR4 전용 메모리를 탑재, USB 3.1 Gen 2 Type-C 인터페이스로 Windows·Linux·Android에 바로 연결 가능하다. TensorFlow·PyTorch·ONNX 프레임워크를 지원하며, Windows 드라이버는 2026년 5월 중순 제공 예정이다. M.2 버전도 병행 출시된다. [[G-01]](#ref-g-01)

2. **Nordic nRF54LM20B Axon NPU — IoT 디바이스의 추론 속도 15x 향상.**
   Nordic Semiconductor의 nRF54LM20B 시스템온칩(System-on-Chip, SoC)은 128MHz Axon NPU를 내장해 TensorFlow Lite 모델 추론 속도를 CPU 대비 최대 15x 향상시키며, 경쟁 무선 NPU 대비 7x 성능·8x 에너지 효율을 제공한다. 2026년 Q1부터 선별 고객에게 샘플링 중이며 Q2 초 광범위 개발 키트 출시 예정이다. Edge AI Lab으로 Neuton 모델 학습부터 배포까지 통합 파이프라인을 지원한다. [[G-02]](#ref-g-02), [[G-03]](#ref-g-03)

3. **Synaptics Torq NPU + Google Coral 통합 — 웨어러블 대상 멀티모달 엣지 AI.**
   2026년 3월 10일 Synaptics와 Google Research가 공동 발표한 Coral Dev Board는 Astra SL2610 SoC에 1 TOPS Torq NPU를 탑재하며, 업계 최초로 Google Coral NPU를 구현한다. Gemma 3 270M 모델이 기본 탑재되어 즉시 개발 가능하다. MLIR 기반 오픈소스 툴체인이 PyTorch·TFLite 모델을 단일 워크플로로 배포하며, 웨어러블·스마트홈·산업 제어 시스템 시장을 타겟한다. Embedded World 2026 Hall 4-A에서 시연되었다. [[G-04]](#ref-g-04), [[G-05]](#ref-g-05)

4. **MediaTek Genio 시리즈 확장 — 3nm부터 6nm까지 로봇·IoT 풀 라인업.**
   2026년 3월 10일 MediaTek이 Embedded World에서 발표한 신규 Genio 라인업은 3개 제품군으로 구성된다. Genio Pro(TSMC 3nm, 50 TOPS+)는 로봇·드론·머신 비전 타겟으로 Q1 샘플링, Q3 양산 예정이다. Genio 420(6nm, 7.2 TOPS)은 2026년 4월 샘플링 시작, Genio 360/360P(6 TOPS/8.5 TOPS)는 현재 샘플링 중이다. Genio 360 시리즈는 최대 2B 파라미터 모델의 엣지 추론을 지원한다. [[G-06]](#ref-g-06), [[G-07]](#ref-g-07)

5. **Texas Instruments MSPM0G5187 — $1 이하 MCU에 TinyEngine NPU 탑재.**
   TI가 Embedded World 2026에서 발표한 MSPM0G5187(Arm Cortex-M0+, 80MHz)은 TinyEngine NPU를 내장해 NPU 미탑재 MCU 대비 추론 지연 90x 단축, 에너지 소비 120x 절감을 달성한다. 생산 수량 1,000개 기준 $1 이하 가격으로 공급되며, 개발 키트(LP-MSPM0G5187)는 $22이다. CCStudio Edge AI Studio로 모델 선택·학습·배포를 단일 환경에서 지원한다. [[G-08]](#ref-g-08), [[G-09]](#ref-g-09)

6. **Ambiq Atomiq SoC — 300mV 초저전압 동작 NPU SoC 공개.**
   Ambiq이 CES 2026(1월)에서 발표하고 Embedded World 2026에서 시연한 Atomiq SoC는 12nm FinFET 공정에 Arm Ethos-U85 NPU를 탑재, 200 GOPS 이상의 온디바이스 AI 성능을 제공한다. 300mV의 초저전압 동작 모드는 동사 제품군 사상 최저 전압으로, 항상 켜진(always-on) 오디오·비전·추론 AI를 실용화한다. 첫 양산 제품(Atomiq110)은 2027년 예정이다. [[G-10]](#ref-g-10)

7. **NPU 벤치마크 인사이트 — TOPS 지표의 한계, 메모리 대역폭이 실성능 결정.**
   2026년 NPU 벤치마크 분석에 따르면 TOPS 수치가 실제 추론 성능을 완전히 반영하지 않는다는 것이 확인되었다. Apple M4 Max는 상대적으로 낮은 TOPS에도 불구하고 통합 메모리 아키텍처 덕분에 LLM 추론에서 우위를 보인다. AMD Ryzen AI 300은 높은 TOPS 스펙에도 NPU 기반 이미지 생성에 70초가 소요되는 반면 동일 칩 내장 GPU는 30초 수준이다. NPU는 GPU 대비 추론 속도 60% 향상, 전력 소비 40-45% 절감을 제공한다. [[G-11]](#ref-g-11)

8. **LLM 엣지 추론 실증 논문 — 모바일 열 관리가 핵심 제약.**
   2026년 3월 24일 arXiv에 게재된 "LLM Inference at the Edge" 논문(Tummalapalli et al., 2026)은 Raspberry Pi 5+Hailo-10H NPU, Samsung Galaxy S24 Ultra, iPhone 16 Pro, RTX 4050 GPU 등 4개 플랫폼에서 Qwen 2.5 1.5B(4bit 양자화) 모델을 벤치마킹했다. RTX 4050은 131.7 tokens/sec(34.1W), Hailo-10H는 6.9 tokens/sec(2W 미만)로, 에너지 효율에서 엣지 NPU가 GPU를 크게 앞선다. 모바일 플랫폼은 열 제약으로 성능이 급감하는 반면 전용 하드웨어는 전력·메모리 대역폭이 병목이다. [[P-01]](#ref-p-01)

9. **통신사 AI-RAN + 멀티 액세스 엣지 컴퓨팅(Multi-Access Edge Computing, MEC) 연동 진전.**
   SoftBank와 Ericsson이 2026년 2월 27일 AI-RAN과 MEC 플랫폼을 연동해 로봇이 온보드 하드웨어 제약 없이 고급 AI 작업을 동적으로 오프로드하는 PoC를 완료했다. T-Mobile은 Nokia anyRAN 소프트웨어 위에 NVIDIA RTX Pro 6000 Blackwell Server 기반 AI 인프라를 모바일 스위칭 오피스에 파일럿 배포했다. 모바일 엣지 컴퓨팅(MEC) 시장은 2025년 $0.80B에서 2031년 $3.88B로 CAGR 30.1% 성장이 전망된다. [[G-12]](#ref-g-12), [[G-13]](#ref-g-13)

10. **Qualcomm 한국 AI 스타트업 프로그램 참여 — Dragonwing 엣지 AI 플랫폼 확산 추진.**
    Qualcomm이 2026년 4월 초 한국 정부 지원 AI 스타트업 프로그램 "Challenge AX for All"에 참여, Dragonwing 프로세서 라인을 기반으로 PoC에서 시장 출시까지 스타트업을 지원한다. Dragonwing Q-8750은 77 TOPS 성능에 최대 11B 파라미터 LLM 온디바이스 추론을 지원하며, Q-7790은 24 TOPS 성능으로 스마트 카메라·TV 시장을 타겟한다. [[G-14]](#ref-g-14)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| ASUS | UGen300 USB AI 가속기 발표(4/1), Hailo-10H 탑재 40 TOPS, 2.5W, 8GB LPDDR4, $가격 미공개(개발자 대상 출시) | [[G-01]](#ref-g-01) |
| Hailo | Hailo-10H 일반 공급(GA) 전환 완료, ASUS·Raspberry Pi 등 다수 OEM 채택으로 에코시스템 확장 | [[G-01]](#ref-g-01), [[G-16]](#ref-g-16) |
| Nordic Semiconductor | nRF54LM20B(Axon NPU) Q2 2026 광범위 출시, Embedded World 2026에서 Neuton 모델+Axon NPU 시연 | [[G-02]](#ref-g-02), [[G-03]](#ref-g-03) |
| Synaptics | Google Research와 Coral Dev Board 공동 출시(3/10), 업계 최초 Coral NPU 상용 구현, Gemma 3 모델 기본 탑재 | [[G-04]](#ref-g-04) |
| MediaTek | Genio Pro(3nm, 50 TOPS+), Genio 420(6nm, 7.2 TOPS), Genio 360/360P(6~8.5 TOPS) 발표(3/10), 4월 샘플링 시작 | [[G-06]](#ref-g-06), [[G-07]](#ref-g-07) |
| Texas Instruments | MSPM0G5187 및 AM13Ex MCU 즉시 양산 공급 개시, $1 이하 가격 달성, 90x 저지연·120x 에너지 효율 | [[G-08]](#ref-g-08), [[G-09]](#ref-g-09) |
| Ambiq | Atomiq SoC 발표(CES 1월, EW 2026 시연), 12nm·200 GOPS·300mV 초저전압, Atomiq110 2027년 양산 예정 | [[G-10]](#ref-g-10) |
| Qualcomm | Dragonwing Q-8750(77 TOPS, 11B LLM 지원)·Q-7790(24 TOPS) 기반 한국 스타트업 프로그램 참여(4월) | [[G-14]](#ref-g-14) |
| Samsung | Galaxy S26에 EdgeFusion(Exynos 2600 탑재) 적용, 엑시노스 2nm 공정 NPU로 온디바이스 이미지 생성 기능 차별화 | [[G-15]](#ref-g-15) |
| Ericsson | SoftBank와 AI-RAN+MEC PoC 완료(2/27), 로봇 AI 작업 동적 오프로드 시연 | [[G-12]](#ref-g-12) |

---

## 시장 시그널

**시장 전망**

- 엣지 AI 칩 시장: 2025년 $3.67B → 2026년 $4.44B → 2031년 $11.54B(CAGR 21.05%) [[G-17]](#ref-g-17)
- 장기 전망: 2036년 $80B+ 돌파 예상 — 자동차·AI 스마트폰·AI PC·휴머노이드 로봇·AI 센서 5개 세그먼트가 견인 [[G-18]](#ref-g-18)
- 온디바이스 AI(AI PC·스마트폰·산업 IoT 포함) CAGR 26%+ [[G-17]](#ref-g-17)
- 소비자 가전이 엣지 AI 칩 시장의 70% 이상 점유 유지 전망, AI 스마트폰이 최대 단일 세그먼트 [[G-18]](#ref-g-18)
- MEC 시장: 2026년 $1.04B → 2031년 $3.88B(CAGR 30.1%) [[G-13]](#ref-g-13)

**도입 사례**

- ASUS UGen300: Windows·Linux·Android 기기에 플러그인 방식으로 엣지 AI 추론 환경 구성, 100개 이상 사전 학습 모델 번들 예정 [[G-01]](#ref-g-01)
- TI MCU: $1 이하 가격 달성으로 가전·산업 자동화 기기의 AI 탑재 비용 장벽 제거 [[G-08]](#ref-g-08)
- SoftBank+Ericsson AI-RAN: 로봇이 MEC 플랫폼에 AI 작업을 동적 오프로드하여 온보드 하드웨어 한계 극복 [[G-12]](#ref-g-12)
- T-Mobile: 모바일 스위칭 오피스에 NVIDIA Blackwell 기반 AI-RAN 인프라 파일럿 배포 [[G-13]](#ref-g-13)

**연구 동향**

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| LLM Inference at the Edge (Tummalapalli et al., 2026) | 4개 플랫폼 벤치마크: Hailo-10H NPU 6.9 t/s 2W 미만, RTX 4050 131.7 t/s 34.1W. 모바일 열 관리가 핵심 제약. | [[P-01]](#ref-p-01) |
| eIQ Neutron: Edge-AI Inference with Integrated NPU (NXP 외, 2025) | 동일 TOPS 자원 대비 평균 1.8x(최대 4x) 추론 속도 향상, 컴파일러-NPU 통합 설계 중요성 강조 | [[P-02]](#ref-p-02) |
| Benchmarking Edge AI Platforms for High-Performance ML Inference (2024) | Intel AI PC(CPU+GPU+NPU 이종 플랫폼)에서 NPU가 행렬 벡터 곱 58.54% 고속화, LLM 3.2x 속도 향상 | [[P-03]](#ref-p-03) |
| Evaluating Energy Efficiency of NPU-Accelerated ML Inference on Embedded MCUs (2025) | 지연 7x~125x 단축, 에너지 최대 143x 절감, MCU NPU 가속 효과 정량화 | [[P-04]](#ref-p-04) |

**커뮤니티 시그널**

- Embedded World 2026을 계기로 개발자 커뮤니티에서 "NPU가 없는 MCU는 이제 경쟁력이 없다"는 인식이 확산되고 있음 [추가확인 필요] — 단일 관찰 소스, 정량 데이터 없음
- Nordic DevZone에서 Axon NPU 성능 스펙 문의 급증 — 샘플링 단계 개발자 수요 반영 [[G-20]](#ref-g-20)

---

## 전략적 시사점

**기회**

- **가격 장벽 붕괴**: TI $1 이하 AI MCU, ASUS $미공개 USB 가속기 등 엣지 AI 하드웨어의 대중화 시점이 2026년 H1로 앞당겨짐. 저가 센서·IoT 기기에 AI 탑재가 경제적으로 실현 가능해짐
- **멀티 벤더 에코시스템 성숙**: Hailo(가속기) + Nordic(IoT SoC) + Synaptics/Google(개발 키트) + MediaTek(IoT SoC) 생태계가 빠르게 표준화. 특정 벤더 의존 없이 솔루션 설계 가능
- **통신 인프라 엣지 AI화**: AI-RAN + MEC 연동 PoC 완료로 통신사가 네트워크 엣지를 AI 추론 플랫폼으로 운영하는 모델 가시화. SKT·KT의 MEC AI 사업 기회
- **소형·저전력 모델 실용화**: Gemma 3 270M, Qwen 2.5 1.5B(4bit) 등 서브 1B 모델이 상용 NPU에서 실시간 추론 가능 — 배터리 기기 대상 AI 서비스 적용 범위 확대

**위협**

- **성능 지표 불일치 리스크**: TOPS 수치가 실성능을 반영하지 않는 사례 증가(AMD Ryzen AI 300 사례). 도입 의사결정 시 벤치마크 기반 검증 없이 스펙만으로 판단 시 성능 미달 위험
- **모바일 플랫폼 열 제약**: 스마트폰 기반 엣지 AI는 지속 부하 시 열 스로틀링으로 성능이 급감 — 제품 SLA 설계 시 최대 성능이 아닌 지속 성능 기준 적용 필요
- **파편화 리스크**: NPU별 툴체인(TI CCStudio, Nordic nRF Connect SDK, Hailo SDK, MediaTek NeuroPilot) 난립으로 개발 리소스 분산. 표준화 전까지 멀티 플랫폼 지원 비용 증가
- **윈도우 드라이버 지연**: ASUS UGen300 Windows 드라이버 2026년 5월 중순 제공 예정 — 엔터프라이즈 Windows 환경 도입 시 타임라인 조정 필요

---

## 제품/서비스 스펙 비교

**엣지 AI 가속기/NPU SoC 비교 (2026 신규 발표)**

| 기업 | AI 성능(TOPS) | 전력(W) | 가격(정책) | 출처 |
|------|--------------|---------|-----------|------|
| ASUS UGen300 (Hailo-10H) | 40 TOPS | 2.5W | 미공개 (개발자/상업용) | [[G-01]](#ref-g-01) |
| MediaTek Genio Pro | 50 TOPS+ | 미공개 | 샘플링 중 (Q3 2026 양산) | [[G-06]](#ref-g-06) |
| MediaTek Genio 420 | 7.2 TOPS | 미공개 | 샘플링 시작(2026-04) | [[G-07]](#ref-g-07) |
| Nordic nRF54LM20B (Axon) | CPU 대비 15x 속도 향상 | 초저전력(수치 미공개) | Q2 2026 개발 키트 출시 | [[G-02]](#ref-g-02) |
| Synaptics Astra SL2610 (Torq) | 1 TOPS | 초저전력(수치 미공개) | 한정판 개발자 보드 | [[G-04]](#ref-g-04) |
| TI MSPM0G5187 (TinyEngine) | 수치 미공개 (90x 지연 단축) | 초저전력 MCU | $1 이하/1K 단위 | [[G-08]](#ref-g-08) |
| Ambiq Atomiq (Ethos-U85) | 200 GOPS | 300mV 초저전압 | 2027 양산 예정 | [[G-10]](#ref-g-10) |
| Qualcomm Dragonwing Q-8750 | 77 TOPS | 미공개 | 공개 정보 없음 | [[G-14]](#ref-g-14) |

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | ASUS Pressroom — ASUS UGen300 USB AI Accelerator 발표 | [링크](https://press.asus.com/news/press-releases/asus-ugen300-usb-ai-accelerator-generative-ai-edge/) | news | 2026-04-01 | [A] |
| <a id="ref-g-02"></a>G-02 | Nordic Semiconductor — nRF54L Series SoC with NPU and Nordic Edge AI Lab | [링크](https://www.nordicsemi.com/Nordic-news/2026/01/nRF54L-Series-SoC-with-NPU-and-Nordic-Edge-AI-Lab-make-on-device-intelligence-easily-accessible) | news | 2026-01-07 | [A] |
| <a id="ref-g-03"></a>G-03 | Electromaker.io — Nordic Axon NPU at Embedded World 2026 | [링크](https://www.electromaker.io/blog/article/nordic-demonstrates-edge-ai-with-neuton-models-and-axon-npu-at-embedded-world-2026) | news | 2026-03 | [B] |
| <a id="ref-g-04"></a>G-04 | Synaptics — Google Research and Synaptics Launch Next-Generation Coral Dev Board | [링크](https://www.synaptics.com/company/news/google-research-and-synaptics-launch-next-generation-coral-dev-board-for-developers-to-bring-multimodal-edge-ai-applications-to-life) | news | 2026-03-10 | [A] |
| <a id="ref-g-05"></a>G-05 | GlobeNewswire — Google Research and Synaptics Coral Dev Board 발표 | [링크](https://www.globenewswire.com/news-release/2026/03/10/3252447/35894/en/Google-Research-and-Synaptics-Launch-Next-Generation-Coral-Dev-Board-for-Developers-to-Bring-Multimodal-Edge-AI-Applications-to-Life.html) | news | 2026-03-10 | [A] |
| <a id="ref-g-06"></a>G-06 | MediaTek — Adds New Genio Platforms for Robotics, Drones, and Industrial IoT | [링크](https://www.mediatek.com/press-room/mediatek-adds-new-genio-platforms-to-bring-ai-processing-to-robotics-drones-and-industrial-iot) | news | 2026-03-10 | [A] |
| <a id="ref-g-07"></a>G-07 | embedsbc.com — MediaTek Genio Pro 5100 & Genio 420 Edge AI SoCs at Embedded World 2026 | [링크](https://www.embedsbc.com/mediatek-genio-pro-5100-genio-420-edge-ai/) | news | 2026-03 | [B] |
| <a id="ref-g-08"></a>G-08 | TI Newsroom — TI Expands MCU Portfolio and Software Ecosystem for Edge AI | [링크](https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-10-ti-expands-microcontroller-portfolio-and-software-ecosystem-to-enable-edge-ai-in-every-device.html) | news | 2026-03-10 | [A] |
| <a id="ref-g-09"></a>G-09 | CNX Software — Texas Instruments MSPM0G5187 and AM13Ex MCUs with TinyEngine NPU | [링크](https://www.cnx-software.com/2026/03/11/texas-instruments-mspm0g5187-and-am13ex-mcus-integrate-tinyengine-npu-for-edge-ai-applications/) | news | 2026-03-11 | [B] |
| <a id="ref-g-10"></a>G-10 | Ambiq — Unveils Atomiq, World's First Ultra-Low Power NPU SoC Built on SPOT | [링크](https://ambiq.com/news/ambiq-unveils-atomiq-the-worlds-first-ultra-low-power-npu-soc-built-on-spot/) | news | 2026-01-06 | [A] |
| <a id="ref-g-11"></a>G-11 | LocalAIMaster — NPU Comparison 2026: Intel vs Qualcomm vs AMD vs Apple | [링크](https://localaimaster.com/blog/npu-comparison-2026) | blog | 2026 | [C] |
| <a id="ref-g-12"></a>G-12 | Ericsson — SoftBank Corp. and Ericsson demonstrate network-enabled Physical AI with AI-RAN | [링크](https://www.ericsson.com/en/press-releases/2026/2/softbank-corp-and-ericsson-demonstrate-network-enabled-physical-ai-with-ai-ran) | news | 2026-02-27 | [A] |
| <a id="ref-g-13"></a>G-13 | Fierce Network — NVIDIA, T-Mobile and Partners Integrate Physical AI Applications on AI-RAN | [링크](https://www.fierce-network.com/broadband/nvidia-gtc-t-mobile-and-nvidia-push-physical-ai-network-edge-0) | news | 2026-03 | [B] |
| <a id="ref-g-14"></a>G-14 | IBTimes.sg — Qualcomm Joins South Korea's AI Startup Program to Expand Edge AI Push | [링크](https://www.ibtimes.sg/qualcomm-joins-south-koreas-ai-startup-program-expand-edge-ai-push-amid-smartphone-slowdown-85006) | news | 2026-04 | [B] |
| <a id="ref-g-15"></a>G-15 | Android Authority — Galaxy S26 Exynos On-Device AI Image Generation (EdgeFusion) | [링크](https://www.androidauthority.com/galaxy-s26-exynos-2600-on-device-ai-image-generation-3638116/) | news | 2026 | [B] |
| <a id="ref-g-16"></a>G-16 | Hailo — General Availability of Hailo-10H Edge AI Accelerator | [링크](https://hailo.ai/company-overview/newsroom/news/hailo-announces-general-availability-of-hailo-10h-edge-ai-accelerator-with-generative-ai-capabilities/) | news | 2026 | [A] |
| <a id="ref-g-17"></a>G-17 | Mordor Intelligence — Edge AI Chips Market Size, Trends, Share & Growth Report 2031 | [링크](https://www.mordorintelligence.com/industry-reports/edge-artificia-intelligence-chips-market) | report | 2026 | [B] |
| <a id="ref-g-18"></a>G-18 | GlobeNewswire — Edge AI Chips Markets, Technologies, and Forecasts Report 2026-2036 | [링크](https://www.globenewswire.com/news-release/2026/03/11/3253565/0/en/Edge-AI-Chips-Markets-Technologies-and-Forecasts-Report-2026-2036-Architectures-Applications-Competitive-Dynamics-Geographic-Forecasts-and-54-Detailed-Company-Profiles.html) | report | 2026-03-11 | [B] |
| <a id="ref-g-19"></a>G-19 | Moor Insights & Strategy — Embedded World 2026: 10 Strategic Trends Driving Embedded Systems | [링크](https://moorinsightsstrategy.com/embedded-world-2026-10-strategic-trends-driving-embedded-systems/) | report | 2026-03 | [B] |
| <a id="ref-g-20"></a>G-20 | Nordic DevZone — nRF54LM20B AXON NPU Performance Specs Q&A | [링크](https://devzone.nordicsemi.com/f/nordic-q-a/127431/nrf54lm20b-axon-npu-performance-specs/563412) | blog | 2026 | [B] |
| <a id="ref-g-21"></a>G-21 | Electronics Weekly — TI adds to edge-AI MCUs (Embedded World 2026) | [링크](https://www.electronicsweekly.com/news/business/embedded-ti-2026-03/) | news | 2026-03 | [B] |
| <a id="ref-g-22"></a>G-22 | Hailo AI — ASUS UGen300 Powered by Hailo-10H On-Device AI Anywhere | [링크](https://hailo.ai/resources/industries/personal-compute/asus-ugen300-powered-by-hailo-10h-on-device-ai-anywhere/) | news | 2026-04 | [A] |
| <a id="ref-g-23"></a>G-23 | Qualcomm — Dragonwing Q-8750 processor and Q-7790 for AIoT launch | [링크](https://www.eenewseurope.com/en/qualcomm-dragonwing-q-8750-processor-q-7790-aiot/) | news | 2026-01 | [A] |
| <a id="ref-g-24"></a>G-24 | Synaptics Blog — Embedded World 2026: Bringing Edge AI into the Real World | [링크](https://www.synaptics.com/company/blog/embedded-world-2026-bringing-edge-ai-into-the-real-world) | news | 2026-03 | [A] |
| <a id="ref-g-25"></a>G-25 | Ambiq — Showcases Ultra-Low Power Edge AI SoCs at Embedded World 2026 | [링크](https://ambiq.com/news/ambiq-showcases-ultra-low-power-edge-ai-socs-and-npu-innovation-at-embedded-world-2026/) | news | 2026-03 | [A] |
| <a id="ref-p-01"></a>P-01 | Tummalapalli et al. — LLM Inference at the Edge: Mobile, NPU, and GPU Performance Efficiency Trade-offs Under Sustained Load | [링크](https://arxiv.org/abs/2603.23640) | paper | 2026-03-24 | [A] |
| <a id="ref-p-02"></a>P-02 | NXP et al. — eIQ Neutron: Redefining Edge-AI Inference with Integrated NPU and Compiler Innovations | [링크](https://arxiv.org/abs/2509.14388) | paper | 2025 | [A] |
| <a id="ref-p-03"></a>P-03 | arXiv — Benchmarking Edge AI Platforms for High-Performance ML Inference | [링크](https://arxiv.org/html/2409.14803v1) | paper | 2024 | [A] |
| <a id="ref-p-04"></a>P-04 | arXiv — Evaluating the Energy Efficiency of NPU-Accelerated Machine Learning Inference on Embedded Microcontrollers | [링크](https://arxiv.org/abs/2509.17533) | paper | 2025 | [A] |
