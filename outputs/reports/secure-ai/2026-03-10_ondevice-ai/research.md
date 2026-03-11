---
topic: OnDevice AI — sLM 경량화 & 실시간 화자분할
date: 2026-03-10
agent: research-deep
confidence: medium
status: completed
sources_used: [websearch, webfetch]
prior_report: 2026-03-03_secure-ai-v2/final.md
prior_verdict: Conditional Go (120/200)
focus: [sLM 성능/경량화, 프라이버시 보장, 단말 제약(메모리/전력), 실시간 추론, 실시간 화자분할(2인)]
---

# Research Report: OnDevice AI — sLM 경량화 & 실시간 화자분할

## Executive Summary (경영진 요약)

> **이전 분석(2026-03-03) 대비 핵심 변화 3가지:**
> 1. **sLM 추론 성능 급등 확인** — Qualcomm Snapdragon 8 Elite Gen 5에서 3B 모델 기준 220 tokens/sec 달성 [G-03]. 이전 분석 시점(commodity화 판정) 이후 HW 가속이 한 세대 더 진화해, 실시간 통화 요약·추론의 기술적 장벽이 사실상 소멸했다.
> 2. **삼성 Galaxy S26 on-device sLM(3~7B, Gauss 2.x) 정식 출시 확인** [G-05, E-01] — 보이스피싱 탐지 외에도 "hot-swap" 전문 어댑터(통화 요약·번역·프라이버시 처리)가 NPU에서 동작. 경쟁사 단말 차원의 sLM 인프라가 완성 단계.
> 3. **실시간 화자분할(2인) TRL 7 진입 확인** — NVIDIA Streaming Sortformer(2025.08) [G-09] + Picovoice Falcon(완전 온디바이스) [G-10] 출시로 서버·클라우드 없이 단말에서 2인 화자분할 실시간 처리가 기술적으로 가능해짐. 단, 잡음 환경 DER 상승 및 배터리 소모가 제약 요인.
>
> **전략적 시사점**: OnDevice sLM + 실시간 화자분할 조합은 통신사가 "통화 분석 허브" 역할을 수행할 수 있는 기술적 기반이 마련됐다. 그러나 삼성·Apple이 단말 OS 레벨에서 동일 기능을 무료 제공하는 속도가 통신사 서비스 론칭 속도보다 빠르다는 구조적 위협이 유지된다. 신뢰도: Medium (화자분할 온디바이스 실측 벤치마크, 배터리 소모, 한국어 화자분할 정확도 데이터 부재).

---

## 연구 질문

> "통신사 관점에서 OnDevice sLM(경량화·추론 성능)과 실시간 화자분할(2인) 기술의 현재 성숙도(TRL), 주요 플레이어 동향, 학술·특허 트렌드를 조사하고, 이전 분석(2026-03-03 Conditional Go 120/200)에서 부족했던 sLM 경량화 벤치마크, 화자분할 학술 동향, 글로벌 벤치마크를 보완하라."

---

## 1. 기술 현황

### OnDevice sLM — 성숙도 및 핵심 파라미터

**TRL 평가**

| L3 기술 | TRL | 근거 |
|---------|-----|------|
| OnDevice sLM (3B 이하, 영어) | **8~9** | Snapdragon 8 Elite Gen 5 220 tok/s [G-03]; Apple AFM 3B 양산 [E-02]; Galaxy S26 배포 완료 [E-01] |
| OnDevice sLM (한국어 특화) | **7~8** | KT 믿:음 2.3B Mini 오픈소스 [E-03]; ETRI Eagle 3B 공개 [G-13]; 실서비스 적용 단계 |
| 실시간 화자분할 (2인, 서버) | **8~9** | NVIDIA Streaming Sortformer DER~10% [G-09]; pyannoteAI DER 9.9%(2인) [G-11] |
| 실시간 화자분할 (2인, 온디바이스) | **7** | Picovoice Falcon SDK 상용 출시 [G-10]; SpeakerKit 9.6× 속도 [G-11]; 배터리·DER 실측 부재 |
| sLM 기반 통화 요약 (온디바이스) | **7~8** | SKT 에이닷전화 통화요약 월 30건(클라우드 혼합) [N-01]; 온디바이스 전용 상용화 미확인 |

**핵심 기술 제약 (이전 분석 대비 업데이트)**

**메모리 제약**
- 고급 스마트폰 가용 RAM: 4GB 이하 (실질적 모델 적재 한도) [G-01]
- INT4 양자화 기준: 3B 모델 → 1.5GB, 7B 모델 → 3.5GB (배포 가능 범위) [G-04]
- Apple AFM 3B: 2bit 양자화 → 37.5% KV 캐시 절감 [E-02]

**추론 속도 (2026년 현행 HW)**
- Qualcomm Snapdragon 8 Elite Gen 5 (NPU 60 TOPS): 3B 모델 **220 tok/s** (INT2/FP8) [G-03]
- Apple A19 Pro Neural Engine (~35 TOPS): ~50~80 tok/s (추정, 공식 미공개)
- Samsung Exynos 2600 (2nm GAA): NPU 성능 전세대 대비 ~113% 향상 (독립 벤치마크 미확인) [G-05]
- Phi-3-mini 3.8B (INT4): iPhone 14 A16 기준 12 tok/s [G-08] — 구세대 대비 격차 확인

**양자화 표준 수렴**
- 2026년 업계 기본: FP16 학습 → INT4 배포 (4× 메모리 감소, 품질 손실 ~1~3%) [G-04]
- GPTQ, AWQ가 사실상 표준으로 수렴 [G-04]
- Microsoft Olive 0.9.0 (2025.05): NPU INT4 공식 지원 [G-04]

**온디바이스 메모리 병목 (이전 분석 보완)**
- 모바일 메모리 대역폭: 50~90 GB/s (데이터센터 GPU 대비 30~50× 열위) [G-01]
- 디코딩 단계는 메모리 대역폭 바운드 → 모델 크기 제한이 속도의 실질적 병목 [G-01]
- MoE on-edge: EdgeMoE 메모리 5~18% 감소 가능하나 "모바일에서 실용적인 MoE 아키텍처 미존재" [G-01]

### 실시간 화자분할 — 성숙도 및 핵심 파라미터

**아키텍처 발전 방향**

2025~2026년 핵심 트렌드는 **통합 엔드투엔드 모델**(화자분할 + 음성분리 + ASR 통합)으로의 수렴이다. 기존 모듈형(VAD → 임베딩 → 클러스터링) 파이프라인 대비 정확도와 지연시간 모두 개선됐다 [P-04].

**현행 최고 성능 (DER 기준)**

| 시스템 | DER (2인) | 처리 방식 | 비고 |
|--------|-----------|----------|------|
| pyannoteAI (상용) | **9.9%** | 서버/클라우드 | 최고 성능 [G-11] |
| DiariZen (오픈소스) | 13.3% | 서버 | 경쟁력 있는 오픈소스 [G-11] |
| NVIDIA Streaming Sortformer | ~10%+ | 서버/GPU | 실시간 스트리밍 [G-09] |
| Picovoice Falcon (온디바이스) | 공개 정보 없음 | 완전 온디바이스 | SDK 상용화 완료 [G-10] |
| SpeakerKit (Argmax) | pyannote v3 동급 | 온디바이스(Apple Silicon) | **9.6× 속도** [G-11] |

**실시간 처리 (RTF)**
- Lightweight 시스템: CPU 처리, RTF **0.1 이하**, 지연 **~5.5초 고정** [G-02] — 통화 실시간에 적합
- NVIDIA Streaming Sortformer: 20~40ms 프레임 단위 처리, 밀리초 수준 정밀도 [G-09]
- Picovoice Falcon: 완전 온디바이스, 네트워크 의존 없음 [G-10]

**온디바이스 화자분할 핵심 제약**
- 배터리 소모: 연속 통화 시 실측 데이터 공개 없음 (공개 정보 없음)
- 한국어 화자분할 정확도: 전용 벤치마크 부재 (공개 정보 없음)
- 배경 잡음 환경: 잡음 조건에서 DER 급등 경향 [P-02]

---

## 2. 시장 동향

**OnDevice AI 시장 규모 (복수 출처 필요 — 이하 참고 수준)**

| 출처 | 2025 추정 | 2030/2032/2033 전망 | CAGR |
|------|-----------|---------------------|------|
| Grand View Research | $10.8B | 공개 정보 없음 | 27.8% |
| Coherent Market Insights | $26.6B | $124.1B(2032) | 24.6% |
| 360iResearch | 공개 정보 없음 | $75.5B(2033) | 공개 정보 없음 |

> 주의: 시장 리서치 수치는 리서치사별 정의 범위가 상이하며 단일 출처 검증. 수치는 [C] 수준.

**sLM 전용 시장**
- 글로벌 SLM 시장: 2023년 $7.8B → 2030년 $20.7B (CAGR 15.1%) [G-06]
- 온디바이스 AI 스마트폰 채택: 2026년 기준 **20억대 이상** 로컬 sLM 실행 중 [G-12]

**통신사 관련 시장 드라이버**
- 온디바이스 처리의 통신사 비용 절감 효과: 클라우드 추론 비용 대비 사용자 단말 이전으로 서비스 원가 절감 가능 [G-12]
- 프라이버시 규제 강화(GDPR, 국내 개인정보보호법): 온디바이스 처리 수요 확대 [G-12]
- 2026 Deloitte TMT 예측: "AI 약속과 현실 간 격차 좁히기" — 온디바이스 sLM이 핵심 [G-07]

---

## 3. 경쟁사 동향

**주요 플레이어 동향**

| 기업 | 동향 | 출처 |
|------|------|------|
| Apple | SpeechAnalyzer API(WWDC25) — 온디바이스 전사 처리, 시스템 스토리지 활용으로 앱 용량 증가 없음. AFM 3B on-device(2bit 양자화, KV 캐시 37.5% 절감). iOS 18 Live Voicemail 온디바이스 실시간 전사. | [[E-02]](#ref-e-02), [[G-14]](#ref-g-14) |
| Samsung | Galaxy S26 출시(2026.02): Gauss 2.x 기반 3~7B sLM, NPU LoRA hot-swap. 보이스피싱 탐지(경찰청/국과수 3만건) + 통화 요약·번역·프라이버시 처리 무료 제공. Exynos 2600 NPU ~113% 성능 향상. | [[E-01]](#ref-e-01), [[G-05]](#ref-g-05) |
| Qualcomm | Snapdragon 8 Elite Gen 5: 3B 모델 220 tok/s, NPU 60 TOPS, 56개 모델 5ms 이하 처리. LiteRT NeuroPilot + Google 협력으로 sLM 배포 생태계 확장. | [[G-03]](#ref-g-03), [[G-15]](#ref-g-15) |
| MediaTek | D9400+ SoC (8th-gen APU, 3nm): 50 TOPS+, Llama/Gemma 지원. AI ASIC 2026년 $1B+ 매출 목표. LiteRT NeuroPilot + Google 협력. | [[G-15]](#ref-g-15) |
| Google | Gemini 2.5 Native Audio: 다화자 전사/화자분할 지원. Pixel 기반 온디바이스 Gemini Nano — 보이스피싱 탐지·통화 스크리닝(영어/미국). 2026년 Gemini API 확장 예정. | [[G-16]](#ref-g-16) |
| SKT | MWC 2026: A.phone(에이닷전화) — 통화 요약(월 30건, 클라우드 혼합), 통역콜(한·영·일·중). A.X K1 519B (교사 모델) → 70B 이하 소형 모델로 지식 증류 연구. 에이닷 유료화 연기(2026.03). | [[E-04]](#ref-e-04), [[N-01]](#ref-n-01) |
| KT | MWC 2026: 믿:음 K 2.5 Pro 공개. 믿:음 2.0 — 11.5B Base + **2.3B Mini(온디바이스)**, 32K 컨텍스트. KoDarkBench 1위. 멀티모달(이미지+오디오) 고도화 계획. | [[E-03]](#ref-e-03) |
| NTT Docomo | MWC 2026: SyncMe — 개인 AI 에이전트, 사용자 습관 학습·선제 제안. AI 기반 네트워크 운영 에이전틱 시스템(2026.02 상용화). 6G AI-native RAN 시연. | [[N-02]](#ref-n-02) |
| ETRI | Eagle 3B 한국어 특화 sLM 오픈소스 공개(2024.11). 글로벌 빅테크 대비 한국어 처리 효율 우위. 2025년 7B 모델 추가 공개 예정. | [[G-13]](#ref-g-13) |

---

## 4. 제품/서비스 스펙 비교

**OnDevice sLM 스펙 비교 (통화 관련 기능 중심)**

| 기업 | 모델/파라미터 | 추론 속도(tok/s) | 가격(정책) | 출처 |
|------|--------------|-----------------|-----------|------|
| Apple | AFM 3B (2bit 양자화) | 공개 정보 없음 | 무료 (iOS 내장) | [[E-02]](#ref-e-02) |
| Samsung (Gauss 2.x) | 3B~7B (NPU LoRA) | 공개 정보 없음 | 무료 (Galaxy 내장) | [[E-01]](#ref-e-01) |
| Qualcomm (참조 HW) | 3B 기준 | **220 tok/s** (Snapdragon 8 Elite Gen 5) | SoC 라이선스 | [[G-03]](#ref-g-03) |
| KT (믿:음 2.0 Mini) | 2.3B (오픈소스) | 공개 정보 없음 | 오픈소스 무료 | [[E-03]](#ref-e-03) |
| ETRI (Eagle) | 3B (오픈소스) | 공개 정보 없음 | 오픈소스 무료 | [[G-13]](#ref-g-13) |
| SKT (에이닷 전화) | 클라우드 혼합 (온디바이스 비율 미공개) | 공개 정보 없음 | 기본 무료, 통화요약 월 30건 | [[N-01]](#ref-n-01) |

**실시간 화자분할 솔루션 스펙 비교**

| 솔루션 | DER (2인) | 처리 방식 | 가격(정책) | 출처 |
|--------|-----------|----------|-----------|------|
| pyannoteAI | 9.9% | 클라우드/서버 | 유료 (상용 API) | [[G-11]](#ref-g-11) |
| NVIDIA Streaming Sortformer | ~10%+ | 서버 GPU | 오픈소스 (HuggingFace) | [[G-09]](#ref-g-09) |
| Picovoice Falcon | 공개 정보 없음 | 완전 온디바이스 | 상용 SDK (가격 미공개) | [[G-10]](#ref-g-10) |
| Argmax SpeakerKit | pyannote v3 동급 | 온디바이스 (Apple Silicon) | 공개 정보 없음 | [[G-11]](#ref-g-11) |
| AssemblyAI | 잡음 환경 30% 개선 | 클라우드 | 유료 API | [[G-02]](#ref-g-02) |

---

## 5. 학술 동향

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| "Demystifying Small Language Models for Edge Deployment" (ACL 2025) | 스마트폰 HW별 sLM 지연·메모리 실측 벤치마크 최초 체계화 | [[P-01]](#ref-p-01) |
| "Edge-First Language Model Inference" (arXiv 2505.16508, 2025.05) | TGS·TTFT·전력 소모 3차원 트레이드오프 분석; 분산 에지 클러스터 확장 가능성 제시 | [[P-02]](#ref-p-02) |
| "Unifying Diarization, Separation, and ASR with Multi-Speaker Encoder" (OpenReview 2025) | UME: 화자분할+음성분리+ASR 통합 학습 → 개별 최고 성능 대비 개선 | [[P-03]](#ref-p-03) |
| "SDBench: A Comprehensive Benchmark Suite for Speaker Diarization" (arXiv 2507.16136, 2025) | 13개 데이터셋 통합 오픈벤치마크; SpeakerKit 9.6× 속도 발견 | [[P-04]](#ref-p-04) |
| "Benchmarking Diarization Models" (arXiv 2509.26177, 2025.09) | pyannoteAI 11.2% DER 1위, DiariZen 13.3% 오픈소스 최고 성능 확인 | [[P-05]](#ref-p-05) |
| "Lightweight Real-Time Speaker Diarization" (EURASIP JASMP 2024) | RTF 0.1 이하, 5.5초 고정 지연으로 CPU 온디바이스 가능성 증명 | [[P-06]](#ref-p-06) |
| "Privacy-preserving Automatic Speaker Diarization" (arXiv 2210.14995) | SMC+Secure Hashing으로 서버 노출 없이 화자분할 가능성 제시 | [[P-07]](#ref-p-07) |
| "Fast On-device LLM Inference with NPUs" (ASPLOS 2025) | NPU 특화 LLM 추론 최적화; 연산 매핑 전략 체계화 | [[P-08]](#ref-p-08) |
| "Scaling LLM Test-Time Compute with Mobile NPU on Smartphones" (arXiv 2509.23324, 2025.09) | 스마트폰 NPU에서 추론 시간 스케일링 실험; 에너지 효율 분석 | [[P-09]](#ref-p-09) |

**학술 연구 방향 요약**

**sLM 경량화 연구 흐름:**
- 지식 증류(Distillation): DeepSeek-R1에서 1.5B~70B 추론 모델 파생, Qwen3-4B가 72B 수준 추론 달성 [G-01]
- 추론 시간 스케일링(Test-Time Compute): 작은 모델이 적응형 추론으로 큰 모델 능가 [P-09]
- Speculative Decoding: Medusa 2.2~3.6×, EAGLE 유사 속도 [G-01]

**화자분할 연구 흐름:**
- 엔드투엔드 통합 모델(UME) vs 모듈형 파이프라인 경쟁 [P-03]
- 프라이버시 보존 화자분할: SMC·동형암호 결합 연구 초기 단계 [P-07]
- 벤치마크 표준화: SDBench 13개 데이터셋 통합 [P-04]

---

## 6. 특허 동향

**주요 특허**

| 출원인 | 특허번호/출원번호 | 제목 | 관할 | 출처 |
|--------|-----------------|------|------|------|
| Samsung Electronics | US20230419979A1 | Online Speaker Diarization Using Local and Global Clustering | USPTO | [[T-01]](#ref-t-01) |
| Google LLC | US12125501B2 | Face-aware Speaker Diarization for Transcripts | USPTO | [[T-02]](#ref-t-02) |
| Samsung Electronics | US11074910B2 | Electronic Device for Recognizing Speech | USPTO | [[T-03]](#ref-t-03) |

**특허 동향 분석**

**출원 트렌드:**
- USPTO 2024 AI 특허 적격성 가이드라인 업데이트(2024.07.17): AI 기반 음성신호 분석·노이즈 분리에 특허 적격성 확대 [G-17]
- Example 48 (AI 음성신호 처리): "특정 기술 문제 해결에 AI 적용" 시 특허 가능 — sLM+화자분할 결합 특허 출원 증가 예상 [G-17]
- 2025년 USPTO Director 교체 이후 AI 발명 적격성 추가 확대(Ex parte Desjardins 2025.09) [G-17]

**국내 특허 현황:**
- KIPRIS 기반 한국어 화자분할·온디바이스 sLM 특허 정보: intel-store MCP 미가동으로 수집 불가 — WebSearch 대체 시 한계. 공개 정보 없음.

**경쟁 특허 공백 (기회 영역):**
- 통신망 데이터(통화 패턴, 네트워크 신호)와 온디바이스 sLM 결합 특허: 빅테크 출원 미확인 → 통신사 선점 가능 영역

---

## 7. 기업 발언 & 보도자료

**SKT MWC 2026 CTO 발언 (2026.03)**
> "에이닷 유료화 타이밍을 다각도로 재검토 중. 현재 AI 기술로 유료 서비스에 필요한 성능 수준을 달성할 수 있는지 평가하고 있다."
> — SKT CTO, MWC Barcelona 2026 [E-04]

의미: 에이닷의 온디바이스 sLM 기반 유료 서비스 전환이 아직 기술/사업 모두 미완. 통화 요약 등 핵심 기능이 클라우드 혼합 구조에서 벗어나지 못한 상태.

**Samsung Galaxy S26 Unpacked (2026.02.25)**
> "Galaxy S26은 세계 최초 내장 프라이버시 디스플레이와 함께 온디바이스 Gauss AI로 통화 요약·번역·보이스피싱 탐지를 무료 제공. Exynos 2600 NPU에서 3~7B sLM을 LoRA hot-swap 방식으로 전문 기능 전환."
> — Samsung Global Newsroom [E-01]

**KT MWC 2026 발표 (2026.02.26)**
> "믿:음 K 2.5 Pro(32B)를 공개하며 고난도 추론 능력 강화. 2.3B Mini 온디바이스 모델은 AICC·법률·금융 도메인에서 실서비스 적용 중. 향후 멀티모달(이미지+오디오)로 고도화 계획."
> — KT 공식 보도자료 [E-03]

**Apple WWDC 2025 — SpeechAnalyzer 발표**
> "SpeechAnalyzer는 완전 온디바이스로 동작하며 앱 번들 크기를 늘리지 않는다. 시스템 스토리지에서 모델을 관리하고, 런타임 메모리를 앱 메모리 공간 밖에서 처리한다."
> — Apple Developer Documentation [E-02]

**NVIDIA Streaming Sortformer 출시 (2025.08)**
> "회의·통화·음성 앱에서 실시간으로 화자를 식별. 최대 4인 동시 추적, 밀리초 수준 정밀도. 20~40ms 프레임 단위 처리."
> — NVIDIA Technical Blog [G-09]

**NTT Docomo MWC 2026 — SyncMe**
> "SyncMe는 사용자 습관을 학습하고 선제적으로 정보·행동을 제안하는 개인 AI 에이전트. Docomo 계정 및 일상 데이터와 연동."
> — Ubergizmo / NTT Docomo [N-02]

---

## 8. 전략적 시사점

**기술 트렌드**

- sLM 추론 성능의 임계점 돌파: 220 tok/s(Snapdragon 8 Elite Gen 5)는 실시간 통화 요약·추론을 온디바이스에서 가능하게 한다 [G-03]
- 화자분할 온디바이스화 가속: Picovoice Falcon, Argmax SpeakerKit 상용화로 클라우드 의존 없이 2인 화자분할 가능 [G-10, G-11]
- 프라이버시 퍼스트 아키텍처 확산: Apple SpeechAnalyzer의 "시스템 스토리지 + 앱 외부 메모리" 패턴이 업계 표준으로 확산 예상 [E-02]

**기회**

- 통신사 고유 데이터 결합: 단말 sLM이 처리할 수 없는 "통화 패턴·네트워크 신호·가입자 프로파일" 데이터와 온디바이스 sLM 결합 → 통신사만 가능한 차별화 서비스
- 한국어 특화 화자분할: 글로벌 솔루션(NVIDIA, pyannoteAI)은 영어·만다린 최적화. 한국어 통화 환경 특화 화자분할 모델 선점 기회
- KT 믿:음 Mini 2.3B 활용: 오픈소스 기반으로 통화 특화 파인튜닝 → 빠른 온디바이스 sLM 서비스 구현 가능 [E-03]
- B2B 차별화: 기업 회의·콜센터 대상 온디바이스 화자분할+통화 요약 결합 서비스 → 클라우드 데이터 유출 우려 해소

**위협**

- 삼성·Apple의 무료 내장 속도: Galaxy S26 Gauss 3~7B sLM 무료 내장, iOS SpeechAnalyzer 무료 API — B2C 유료화 공간 지속 축소 [E-01, E-02]
- SKT 에이닷 유료화 연기: 동일 플레이어가 기술 성숙도를 "유료 전환 불충분"으로 판단 → 시장 WTP 미검증 상태 확인 [E-04]
- 글로벌 빅테크 sLM 생태계: Meta Llama, Google Gemma, Microsoft Phi 등 오픈소스 생태계가 통신사 자체 모델 개발 비용 우위를 상쇄
- 배터리·열 제약: 온디바이스 화자분할의 연속 통화 시 배터리 소모 미검증 → 실서비스 UX 리스크

**권고사항**

- 즉시: 한국어 통화 환경 화자분할 DER 자체 측정 — Picovoice Falcon/SpeakerKit SDK 기반 PoC 실시
- 단기: KT 믿:음 Mini 2.3B 또는 ETRI Eagle 3B 기반 통화 특화 sLM 파인튜닝 실험 (오픈소스 활용)
- 단기: 온디바이스 sLM + 화자분할 통합 파이프라인 배터리 영향 측정 (3세대 Snapdragon/Exynos 기기 기준)
- 중기: 통신사 고유 데이터(통화 패턴, 네트워크 신호) 결합 특허 출원 검토 — USPTO AI 적격성 확대 활용
- 중기: B2B(기업 콜센터·회의) 온디바이스 화자분할+통화 요약 패키지 — 프라이버시 우려 해소 포지셔닝

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- Qualcomm Snapdragon 8 Elite Gen 5 220 tok/s (E-01급 HW 스펙 [G-03])
- Apple AFM 3B 2bit 양자화, KV 캐시 37.5% 절감 [E-02]
- Samsung Galaxy S26 Gauss 3~7B sLM 무료 내장 확인 [E-01]
- KT 믿:음 2.3B Mini 오픈소스 공개, KoDarkBench 1위 [E-03]
- pyannoteAI DER 9.9%(2인), SpeakerKit 9.6× 속도 [P-04, P-05]
- NVIDIA Streaming Sortformer 출시(오픈소스) [G-09]
- INT4 양자화: 3B 모델 1.5GB, 7B 모델 3.5GB [G-04]

**추가 검증 필요 [C/D]:**
- On-device AI 시장 규모(리서치사별 편차 3배 이상) [C]
- Samsung Exynos 2600 NPU 113% 향상 (독립 벤치마크 미확인) [C]
- 온디바이스 화자분할 배터리 소모 (공개 정보 없음) [D]
- SKT 에이닷전화의 온디바이스 처리 비율 (공개 정보 없음) [D]

**데이터 공백:**
- 한국어 특화 화자분할 DER 벤치마크 (공개 데이터 없음)
- 통신사 통화 환경(잡음, 코덱 압축)에서의 sLM 추론 정확도
- 온디바이스 화자분할 실제 배터리 소모 데이터
- KIPRIS 한국 특허 현황 (intel-store MCP 미가동으로 수집 불가)

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | V. Chandra — On-Device LLMs: State of the Union, 2026 | [링크](https://v-chandra.github.io/on-device-llms/) | blog | 2026-01 | [B] |
| <a id="ref-g-02"></a>G-02 | AssemblyAI — Top 8 Speaker Diarization Libraries and APIs 2026 | [링크](https://www.assemblyai.com/blog/top-speaker-diarization-libraries-and-apis) | blog | 2026 | [B] |
| <a id="ref-g-03"></a>G-03 | Futurum / Findarticles — Snapdragon 8 Elite Gen 5: 220 tokens/sec | [링크](https://www.findarticles.com/new-snapdragon-chip-cracks-220-tokens-per-second/) | news | 2025 | [B] |
| <a id="ref-g-04"></a>G-04 | Microsoft / Local AI Zone — INT4 Quantization Guide 2025-2026 | [링크](https://medium.com/data-science-at-microsoft/a-practical-guide-to-int4-quantization-for-slms-gptq-vs-awq-olive-and-real-world-results-2f63d6963d1d) | blog | 2026-02 | [B] |
| <a id="ref-g-05"></a>G-05 | PR Newswire — Samsung Galaxy S26 On-Device SLM Reasoning | [링크](https://markets.financialcontent.com/prnews.pressre/article/tokenring-2025-12-25-samsungs-ghost-in-the-machine-how-the-galaxy-s26-is-redefining-privacy-with-on-device-slm-reasoning) | news | 2025-12-25 | [B] |
| <a id="ref-g-06"></a>G-06 | Grand View Research — Small Language Model Market 2023-2030 | [링크](https://www.grandviewresearch.com/industry-analysis/on-device-ai-market-report) | report | 2024 | [C] |
| <a id="ref-g-07"></a>G-07 | Deloitte — 2026 TMT Predictions | [링크](https://www.deloitte.com/global/en/about/press-room/2026-tmt-predictions.html) | report | 2025 | [B] |
| <a id="ref-g-08"></a>G-08 | ETRI Trends — 온디바이스 소형언어모델 기술개발 동향 | [링크](https://ettrends.etri.re.kr/ettrends/209/0905209009/) | paper | 2025 | [A] |
| <a id="ref-g-09"></a>G-09 | NVIDIA Technical Blog — Streaming Sortformer Real-Time Speaker Diarization | [링크](https://developer.nvidia.com/blog/identify-speakers-in-meetings-calls-and-voice-apps-in-real-time-with-nvidia-streaming-sortformer/) | news | 2025-08-21 | [A] |
| <a id="ref-g-10"></a>G-10 | Picovoice — Falcon On-Device Speaker Diarization | [링크](https://picovoice.ai/platform/falcon/) | official | 2025 | [A] |
| <a id="ref-g-11"></a>G-11 | pyannoteAI — Speaker Diarization DER Benchmark | [링크](https://www.pyannote.ai/benchmark) | official | 2025 | [A] |
| <a id="ref-g-12"></a>G-12 | Edge AI and Vision Alliance — On-Device LLMs in 2026 | [링크](https://www.edge-ai-vision.com/2026/01/on-device-llms-in-2026-what-changed-what-matters-whats-next/) | blog | 2026-01 | [B] |
| <a id="ref-g-13"></a>G-13 | AI타임스 — ETRI Eagle 3B 한국어 sLM 오픈소스 공개 | [링크](https://www.aitimes.kr/news/articleView.html?idxno=33013) | news | 2024-11 | [B] |
| <a id="ref-g-14"></a>G-14 | Apple Developer — WWDC25 SpeechAnalyzer Session 277 | [링크](https://developer.apple.com/videos/play/wwdc2025/277/) | official | 2025 | [A] |
| <a id="ref-g-15"></a>G-15 | Google Developers Blog — MediaTek NPU and LiteRT | [링크](https://developers.googleblog.com/mediatek-npu-and-litert-powering-the-next-generation-of-on-device-ai/) | official | 2025 | [A] |
| <a id="ref-g-16"></a>G-16 | Google Blog — Gemini 2.5 Native Audio Model Updates | [링크](https://blog.google/products/gemini/gemini-audio-model-updates/) | official | 2025-2026 | [A] |
| <a id="ref-g-17"></a>G-17 | Mintz / USPTO — 2024 AI Patent Eligibility Guidance Update | [링크](https://www.mintz.com/insights-center/viewpoints/2231/2024-07-24-understanding-2024-uspto-guidance-update-ai-patent) | official | 2024-07 | [A] |
| <a id="ref-n-01"></a>N-01 | 뉴시스 — SKT T전화 에이닷 탑재, 통화요약 월 30건 제한 | [링크](https://www.newsis.com/view/NISX20241015_0002919915) | news | 2024-10-15 | [B] |
| <a id="ref-n-02"></a>N-02 | Ubergizmo — NTT Docomo SyncMe Personal AI Agent at MWC 2026 | [링크](https://www.ubergizmo.com/2026/03/ntt-docomo-syncme-personal-ai-agent/) | news | 2026-03 | [B] |
| <a id="ref-e-01"></a>E-01 | Samsung Global Newsroom — Galaxy S26 Unpacked 2026 | [링크](https://news.samsung.com/global/samsung-unveils-galaxy-s26-series-the-most-intuitive-galaxy-ai-phone-yet) | official | 2026-02-25 | [A] |
| <a id="ref-e-02"></a>E-02 | Apple Machine Learning Research — Foundation Models 2025 Updates | [링크](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates) | official | 2025 | [A] |
| <a id="ref-e-03"></a>E-03 | KT 공식/파이낸셜뉴스 — 믿:음 K MWC26 공개, 믿:음 2.0 Mini 2.3B | [링크](https://www.fnnews.com/news/202602260917334750) | official | 2026-02-26 | [A] |
| <a id="ref-e-04"></a>E-04 | SKT Newsroom / AI News — MWC 2026 에이닷 유료화 재검토 | [링크](https://news.sktelecom.com/en/2742) | official | 2026-03 | [A] |
| <a id="ref-p-01"></a>P-01 | ACL 2025 — Demystifying Small Language Models for Edge Deployment | [링크](https://aclanthology.org/2025.acl-long.718.pdf) | paper | 2025 | [A] |
| <a id="ref-p-02"></a>P-02 | arXiv:2505.16508 — Edge-First Language Model Inference: Models, Metrics, and Tradeoffs | [링크](https://arxiv.org/abs/2505.16508) | paper | 2025-05 | [A] |
| <a id="ref-p-03"></a>P-03 | OpenReview — Unifying Diarization, Separation, and ASR with Multi-Speaker Encoder | [링크](https://openreview.net/forum?id=5oaUMZEjWe) | paper | 2025 | [A] |
| <a id="ref-p-04"></a>P-04 | arXiv:2507.16136 — SDBench: A Comprehensive Benchmark Suite for Speaker Diarization | [링크](https://arxiv.org/abs/2507.16136) | paper | 2025-07 | [A] |
| <a id="ref-p-05"></a>P-05 | arXiv:2509.26177 — Benchmarking Diarization Models | [링크](https://arxiv.org/abs/2509.26177) | paper | 2025-09 | [A] |
| <a id="ref-p-06"></a>P-06 | EURASIP JASMP — Lightweight Real-Time Speaker Diarization (RTF<0.1) | [링크](https://asmp-eurasipjournals.springeropen.com/articles/10.1186/s13636-024-00382-2) | paper | 2024 | [A] |
| <a id="ref-p-07"></a>P-07 | arXiv:2210.14995 — Privacy-preserving Automatic Speaker Diarization | [링크](https://arxiv.org/abs/2210.14995) | paper | 2022 | [A] |
| <a id="ref-p-08"></a>P-08 | ACM ASPLOS 2025 — Fast On-device LLM Inference with NPUs | [링크](https://dl.acm.org/doi/10.1145/3669940.3707239) | paper | 2025 | [A] |
| <a id="ref-p-09"></a>P-09 | arXiv:2509.23324 — Scaling LLM Test-Time Compute with Mobile NPU | [링크](https://arxiv.org/abs/2509.23324) | paper | 2025-09 | [A] |
| <a id="ref-t-01"></a>T-01 | Samsung Electronics — US20230419979A1 Online Speaker Diarization (Local/Global Clustering) | [링크](https://patents.google.com/patent/US20230419979A1/en) | patent | 2023 | [A] |
| <a id="ref-t-02"></a>T-02 | Google LLC — US12125501B2 Face-aware Speaker Diarization | [링크](https://patents.google.com/patent/US12125501B2/en) | patent | 2024 | [A] |
| <a id="ref-t-03"></a>T-03 | Samsung Electronics — US11074910B2 Electronic Device for Recognizing Speech | [링크](https://uspto.report/patent/grant/11,074,910) | patent | 2021 | [A] |
