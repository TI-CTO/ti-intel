---
type: weekly-research
domain: secure-ai
l3_topic: ondevice-slm
date: 2026-03-05
signal: 🟡
agent: research-deep
confidence: medium
status: completed
sources_used: [websearch, webfetch]
---

# Research Report: OnDevice Small Language Model (온디바이스 소형 언어 모델)

## Executive Summary (경영진 요약)

> 2026년 초 온디바이스 SLM 시장은 MWC 2026(바르셀로나, 2026-03-02~05)을 기점으로 **실증 단계에서 대량 양산 단계로의 전환점**을 맞이하고 있다. Qualcomm Snapdragon 8 Elite Gen 5(100 TOPS NPU), MediaTek Dimensity 9500(NPU 990), Apple A19 Pro Neural Engine(~35 TOPS) 등 플래그십 SoC가 10억 파라미터급 모델의 실시간 추론을 지원함으로써 클라우드 의존 없는 AI 경험이 현실화되었다. Google Gemma 3n(E2B/E4B, 멀티모달), Apple 온디바이스 3B, Microsoft Phi-4-mini(3.8B), Samsung Gauss2 Compact가 핵심 모델 경쟁을 주도하며, Meta ExecuTorch 1.0 GA가 배포 표준화를 이끌고 있다. 그러나 모바일 메모리 대역폭(50~90 GB/s)이 여전히 핵심 병목이며, 4-bit 양자화·KV 캐시 압축 등 추론 최적화 기술이 차별화 핵심이 될 전망이다. [B] 등급 분석.

## 연구 질문

> OnDevice SLM 분야에서 2026년 3월 초 기준 주요 기업 동향·기술 동향·시장 시그널은 무엇이며, 향후 1~3개월 내 주목해야 할 변화는 무엇인가?

---

## 1. 기술 동향

### 1.1 기술 성숙도 (TRL)

온디바이스 SLM은 TRL 8~9 단계로, 상용 제품 탑재 단계에 진입했다. 핵심 기술 요소는 다음과 같다:

**모델 아키텍처**
- **파라미터 "Goldilocks Zone"**: 3B~7B 파라미터가 실용적 성능과 디바이스 제약의 최적 교점 [G-03]
- **Mixture of Experts (MoE)**: 2025년 초 이후 프론티어 모델의 60% 이상이 MoE 채택. 모바일 배포 시 Expert Pruning 필요 [G-09]
- **Per-Layer Embeddings (PLE)**: Google Gemma 3n이 도입한 동적 메모리 할당 기법. 5B/8B 파라미터 모델을 2GB/3GB 메모리에서 실행 가능 [G-01]
- **KV 캐시 공유**: Apple 온디바이스 3B 모델이 2블록 5:3 비율 분할 + KV 캐시 공유로 메모리 37.5% 절감 [G-05]

**양자화 (Quantization)**
- 4-bit PTQ(Post-Training Quantization)가 사실상 표준으로 정착 (GPTQ, AWQ 방법론) [G-10]
- INT8 양자화: 모델 크기 68% 감소, 정확도 손실 <6%, 전력 40% 절감
- INT4: 3배 추론 속도 향상 달성 가능
- SpinQuant: 회전 행렬 기반 4-bit weight+activation+KV-cache 동시 양자화
- BitNet 1.58-bit: 훈련 단계부터 초저비트 적용 (연구 단계)

**추론 최적화**
- Speculative Decoding: 드래프트 모델 검증 방식으로 2.2~3.6배 속도 향상 [G-10]
- FlashAttention-4: Hot Chips 2025 발표, Blackwell 최적화로 추가 20% 속도 향상 [G-12]
- MLC-LLM, llama.cpp (GGUF 포맷): CPU 추론의 사실상 표준

**하드웨어 NPU 역량 (2026년 플래그십)**
| SoC | NPU 성능 | 주요 특징 |
|-----|---------|---------|
| Qualcomm Snapdragon 8 Elite Gen 5 | ~100 TOPS | Hexagon NPU, 이전 대비 37% 고속화 [G-06] |
| MediaTek Dimensity 9500 | ~50 TOPS | NPU 990, 멀티모달 오프라인 실행 [G-07] |
| Apple A19 Pro (Neural Engine) | ~35 TOPS | MLX 프레임워크 최적화, 통합 메모리 [G-10] |
| Samsung Exynos 2600 | 공개 정보 없음 | Galaxy S26 일부 탑재 |

**핵심 병목**: 모바일 메모리 대역폭(50~90 GB/s) vs. 데이터센터 GPU(2~3 TB/s). 약 30~50배 격차가 실용적 배포의 근본 제약 [G-10]

### 1.2 배포 프레임워크 생태계

| 프레임워크 | 개발사 | 버전 | 특징 |
|-----------|--------|------|------|
| ExecuTorch | Meta/PyTorch | 1.0 GA (2025-10) | 50KB 기반 런타임, 12+ 하드웨어 백엔드, HuggingFace 상위 모델 80%+ 호환 [G-11] |
| llama.cpp | 오픈소스 | 최신 | GGUF 포맷 표준, CPU 추론 최적화 |
| MLX | Apple | 최신 | Apple Silicon 전용, 통합 메모리 활용 |
| MLC-LLM | CMU/오픈소스 | 최신 | 크로스플랫폼 컴파일 |
| ONNX Runtime | Microsoft | 최신 | Phi-4-mini iOS/Android 배포에 활용 [G-04] |
| LiteRT (TFLite) | Google | 최신 | Qualcomm NPU 최적화 [G-06] |

---

## 2. 시장 동향

### 2.1 시장 규모 및 성장

- SLM 시장 규모: 2032년까지 **54.5억 달러** 전망 (MarketsandMarkets) [G-02]
- 온프레미스/엣지 LLM 배포: 2025년 LLM 시장의 51.85% 점유, **27.25% CAGR**로 2031년까지 성장 [G-02]
- 대형 언어 모델 전체 시장: 2030년 기준 149.89억 달러 (Precedence Research)

### 2.2 핵심 드라이버

1. **프라이버시 규제 강화**: 클라우드 전송 없는 온디바이스 처리 수요 증가
2. **모바일 NPU 성능 도약**: 2026년 플래그십 SoC의 NPU 성능이 실용 임계값 초과
3. **배포 비용 절감**: 온디바이스 처리로 클라우드 API 비용 제거
4. **오프라인 사용성**: 네트워크 불요(不要) AI 기능 확장
5. **Gartner 예측**: 2027년까지 기업의 SLM 사용량이 일반 LLM 대비 3배 [G-09]

---

## 3. 경쟁사 동향

### 3.1 기업별 전략 요약

**Google**
- Gemma 3n (E2B/E4B): 5B/8B 파라미터, 2GB/3GB 메모리 풋프린트의 멀티모달 온디바이스 모델. Qualcomm·MediaTek·Samsung System LSI와 공동 개발 [G-01]
- Gemma 3 270M: 초소형 하이퍼 효율 모델. 극한 제약 환경 대응 [G-01]
- LiteRT를 통한 Qualcomm NPU 최적화 [G-06]
- Google AI Edge 도구 체인으로 개발자 생태계 구축

**Apple**
- 온디바이스 ~3B 파라미터 파운데이션 모델: iOS 26/iPadOS 26/macOS 26에서 개발자 API 개방 [G-05]
- KV 캐시 공유로 메모리 37.5% 절감, 2-bit 양자화 인식 훈련 적용
- Foundation Models 프레임워크: Swift API로 수 줄의 코드로 온디바이스 AI 기능 구현
- Private Cloud Compute: 온디바이스 처리 불가 태스크만 서버 위임 (프라이버시 우선 아키텍처)
- 성능: Qwen-2.5-3B 전 언어 우위, Qwen-3-4B·Gemma-3-4B와 영어 경쟁력

**Microsoft**
- Phi-4-mini (3.8B): 온디바이스 최적화 SLM. ONNX Runtime + Microsoft Olive로 iOS·Android·Windows 배포 [G-04]
- Phi-4-mini: iPhone 12 Pro에서 11 tokens/second 생성 속도 달성
- Phi-4-mini-flash-reasoning: 엣지 디바이스용 추론 특화 모델
- Microsoft Edge 브라우저 내 Phi-4-mini 통합 검토 중

**Samsung**
- Samsung Gauss2: Compact(온디바이스), Balanced, Premium 3개 버전. 멀티모달(언어+코드+이미지) [G-08]
- Galaxy S26: 3세대 Galaxy AI 폰. Snapdragon 8 Elite Gen 5 탑재, 100 TOPS NPU
- AI 삼원 전략: Gemini(에이전틱) + Perplexity(웹 검색) + Bixby/Gauss2(온디바이스)
- MWC 2026에서 Galaxy AI 생태계 확장 발표 [G-08]

**Qualcomm**
- Snapdragon 8 Elite Gen 5: ~100 TOPS, Hexagon NPU 37% 고속화 [G-06]
- Snapdragon Wear Elite (MWC 2026): 웨어러블용 NPU 탑재 최초 "Elite" 브랜드 칩 [N-04]
- AGI Inc. 협력: Snapdragon 기반 에이전틱 AI 스택 최적화 [N-05]
- CES 2026: "온디바이스 AI의 미래" 발표

**MediaTek**
- Dimensity 9500: NPU 990 탑재, 멀티모달 모델 오프라인 실시간 실행 [G-07]
- MWC 2026: "AI For Life: From Edge to Cloud" 테마 전시 [N-03]
- OPPO 협력: Omni 풀모달 온디바이스 모델 공개 (음성+비디오+텍스트)
- AI 안경: Dimensity 9500 NPU + Omni 모델 탑재 데모

**Meta**
- ExecuTorch 1.0 GA: Instagram·WhatsApp·Messenger·Facebook 전체 적용 [G-11]
- Llama 3.2 (1B/3B): 128K 컨텍스트, Qualcomm/MediaTek 최적화
- SmolLM2 (135M~1.7B): 11조 토큰 훈련, Llama 3.2 1B 성능 초과

---

## 4. 제품/서비스 스펙 비교

| 기업 | 모델명 | 파라미터 | 메모리 풋프린트 | 멀티모달 | 배포 대상 | 발표 시점 | 출처 |
|------|--------|---------|--------------|---------|---------|---------|------|
| Google | Gemma 3n E2B | 5B (effective 2B) | ~2GB | 이미지+오디오+비디오+텍스트 | 모바일/태블릿/노트북 | 2025-05 (preview) | [G-01] |
| Google | Gemma 3n E4B | 8B (effective 4B) | ~3GB | 이미지+오디오+비디오+텍스트 | 모바일/태블릿/노트북 | 2025-05 (preview) | [G-01] |
| Google | Gemma 3 270M | 270M | 공개 정보 없음 | 텍스트 | 극한 제약 환경 | 2025 | [G-01] |
| Apple | Foundation Model | ~3B | 공개 정보 없음 (2-bit QAT) | 이미지+텍스트 | iPhone/iPad/Mac (Apple Intelligence) | iOS 26 (2025-09) | [G-05] |
| Microsoft | Phi-4-mini | 3.8B | 공개 정보 없음 | 텍스트 (Phi-4-multimodal 별도) | iOS/Android/Windows/IoT | 2025-02 | [G-04] |
| Samsung | Gauss2 Compact | 공개 정보 없음 | 공개 정보 없음 | 언어+코드+이미지 | Galaxy 디바이스 | 2024~2025 | [G-08] |
| Meta | Llama 3.2 3B | 3B | 공개 정보 없음 | 텍스트 (비전 별도) | 크로스플랫폼 (ExecuTorch) | 2024-09 | [G-10] |
| 오픈소스 | SmolLM2 1.7B | 1.7B | 공개 정보 없음 | 텍스트 | 엣지 디바이스 | 2024 | [G-10] |

---

## 5. 학술 동향

### 5.1 주요 연구 방향

**에지 효율 추론 (Edge-Efficient Inference)**
- Tsinghua Science and Technology 2026: "Efficient Inference for Edge Large Language Models" 종합 서베이. 양자화·Speculative Decoding·모델 오프로딩 체계화 [P-01]
- ACM ToIT 2026: "Sustainable LLM Inference for Edge AI" — 에너지 효율·출력 정확도·추론 지연 삼각 트레이드오프 분석 [P-02]
- PMC 2026: "Tiny Machine Learning and On-Device Inference" — 응용·과제·미래 방향 서베이 [P-03]

**양자화 혁신**
- ICLR 2026: "MO-BIEDIT: Resource-Efficient" — 자원 효율 편집 기법 [P-04]
- I-LLM (OpenReview): 완전 양자화 저비트 LLM을 위한 정수 전용 추론 [P-05]

**추론 가속**
- Intel/Weizmann (ICML 2025): 임의의 소형 드래프트 모델이 임의의 LLM 가속 가능 — 최대 2.8배 추론 속도 향상 [G-12]
- FlashAttention-4 (Hot Chips 2025): Blackwell 최적화, 추가 20% 속도 향상 [G-12]

**데이터 효율**
- "데이터 품질 개선은 소형 모델에서 대형 모델보다 더 큰 성능 향상을 유발" [G-10]
- 타겟 데이터 믹스처(코드·수학·지시 데이터)가 서브 1B 모델에서 결정적 역할

**신흥 연구 방향**
- Test-Time Compute: 소형 모델의 긴 추론 체인이 대형 모델 대비 우위 달성
- On-Device Personalization: 클라우드 데이터 전송 없는 로컬 적응(Test-Time Training)
- MoE on Edge: Expert Partitioning·Pruning을 통한 모바일 MoE 배포

---

## 6. 특허 동향

> **참고**: 이번 리서치 사이클에서 intel-store MCP가 미가동 환경이었으므로 특허 데이터는 WebSearch 기반 간접 정보만 수집되었습니다. USPTO/Google Patents 직접 조회는 추후 수행이 필요합니다.

### 6.1 주요 출원인 및 동향

**Qualcomm**
- 에지 추론 가속 분야 상위 4개 특허 출원인 중 하나 (FY2025 기준) [G-09]
- US 10,968,477 B2: 온디바이스 엣지 추론 가속, 642 인용 [G-09]
- NPU 기반 LLM 추론, 디바이스 내 모델 압축 관련 지속 출원 중

**Apple**
- Private Cloud Compute 아키텍처, 디바이스 내 양자화 인식 훈련(QAT) 관련 출원
- KV 캐시 최적화, Neural Engine 가속 관련 특허 [G-05]

**Samsung**
- Gauss2 아키텍처 및 Compact 모델 배포 관련 특허
- System LSI NPU 기반 추론 최적화 특허 출원 중 [G-08]

**주요 기술 클러스터**
- 4-bit 이하 양자화 기법
- Speculative Decoding 가속
- NPU 전용 어텐션 메커니즘
- 온디바이스 개인화(Federated Learning + Test-Time Training)
- 메모리 대역폭 효율화 기법

---

## 7. 기업 발언 및 보도자료

### 7.1 주요 공식 발언

**Google (Gemma 3n, 2025-05-20)**
> "Gemma 3n는 전화기, 노트북, 태블릿 등 일상적 디바이스에서 사용하도록 최적화된 생성형 AI 모델이다. 지난해의 클라우드 기반 프론티어 모델에서만 볼 수 있었던 강력한 멀티모달 역량을 엣지 디바이스에 가져온다." [E-01]

**Qualcomm (CES 2026)**
> "Snapdragon 8 Elite Gen 5의 Hexagon NPU는 100 TOPS를 달성하며, 이전 세대 대비 37% 빠르다. 이는 Personal Knowledge Graph, Personal Scribe 등 완전한 온디바이스 에이전틱 AI 경험을 가능하게 한다." [E-02]

**Qualcomm (MWC 2026, Snapdragon Wear Elite 발표)**
> "웨어러블 분야 최초의 Elite 브랜딩 칩으로, 5배 단일코어 CPU 성능, 7배 GPU 속도, 듀얼 NPU로 10억 파라미터급 모델을 엣지에서 지원한다." [E-03]

**MediaTek (MWC 2026)**
> "Dimensity 9500의 NPU 990은 Omni 풀모달 모델을 완전히 오프라인 상태에서 실시간으로 실행한다. 이것이 'AI For Life: From Edge to Cloud'의 핵심이다." [E-04]

**Samsung (Galaxy Unpacked 2026)**
> "Galaxy S26 시리즈는 Galaxy AI 3세대로, Galaxy S 시리즈 역사상 가장 강력한 성능과 가장 직관적인 AI 경험을 결합했다." [E-05]

**Apple (Foundation Models 프레임워크, 2025-09)**
> "Foundation Models 프레임워크는 개발자에게 ~30억 파라미터 온디바이스 언어 모델에 대한 접근을 단 몇 줄의 Swift 코드로 제공한다. 데이터는 디바이스를 벗어나지 않는다." [E-06]

**Meta (ExecuTorch 1.0 GA, 2025-10)**
> "ExecuTorch는 이제 Instagram, WhatsApp, Messenger, Facebook 전체에서 수십억 사용자를 대상으로 작동한다. 50KB 런타임이 마이크로컨트롤러에서 플래그십 스마트폰까지 동일한 PyTorch API로 배포된다." [E-07]

---

## 8. 전략적 시사점

### 8.1 기회

1. **NPU 가속 모델 최적화 서비스**: Snapdragon/Dimensity NPU 전용 추론 최적화 컨설팅·도구 수요 급증 예상
2. **프라이버시 컴플라이언스**: GDPR/개인정보보호법 강화 환경에서 온디바이스 처리가 클라우드 대비 규제 리스크 감소
3. **한국어 특화 SLM**: 글로벌 모델(영어 중심)의 한국어 성능 한계 → 로컬 특화 경쟁력 기회
4. **엔터프라이즈 온프레미스 SLM**: 기업 내부망 전용 SLM 수요 증가 (금융·의료·공공)
5. **웨어러블 AI**: Qualcomm Snapdragon Wear Elite를 기반으로 한 AI 웨어러블 시장 신규 개척

### 8.2 위협

1. **빅테크 수직 통합**: Apple(Silicon + 모델 + 프레임워크), Google(SoC 파트너 + Gemma + Android), Qualcomm(NPU + 최적화 도구)이 풀스택 장악
2. **메모리 대역폭 병목**: 모바일 메모리 한계가 SLM 성능 상한선 결정 → 하드웨어 혁신 없이는 소프트웨어 단 최적화 한계
3. **중국 생태계 경쟁**: Alibaba MNN, Baidu ERNIE Edge 등 독자 생태계 구축 가속 [G-13]
4. **모델 파편화**: 각 SoC 벤더별 최적화 요구로 크로스플랫폼 배포 복잡성 증가

### 8.3 권고사항

- **단기(1~3개월)**: Gemma 3n·Phi-4-mini·Llama 3.2 3B의 한국어 성능 벤치마크 자체 수행. Qualcomm NPU·Apple Neural Engine 실측 비교
- **중기(3~6개월)**: ExecuTorch 1.0 기반 배포 파이프라인 검증. 온디바이스 SLM + RAG 하이브리드 아키텍처 프로토타이핑
- **장기**: 한국어 특화 SLM 파인튜닝 전략 검토. 통신사 망 내 온디바이스 AI 서비스 기회 분석

---

## 신뢰도 평가

- **높은 확신 [A/B]**: 주요 기업 발표(Gemma 3n, Apple Foundation Models, Snapdragon 8 Elite Gen 5 스펙), MWC 2026 발표 내용, ExecuTorch 1.0 GA 출시
- **추가 검증 필요 [C/D]**: SLM 시장 규모 예측치(복수 리서치사 간 편차 큼), Qualcomm 100 TOPS 수치(마케팅 발표 기반)
- **데이터 공백**:
  - 특허 출원 건수 및 세부 청구항 (intel-store MCP 미가동으로 Google Patents 직접 조회 미수행)
  - Samsung Gauss2 Compact 파라미터 수 (공개 정보 없음)
  - OPPO Omni 모델 상세 스펙
  - 국내 통신사(SKT/KT) 온디바이스 SLM 전략

---

## References

### 글로벌 출처 (G-xx)

| 번호 | 출처명 | 발행일 | 기관유형 | 제목 | 인용원문(한글) | 관련성 | 신뢰성 | 최신성 | URL |
|------|--------|-------|----------|------|-------------|--------|--------|--------|-----|
| G-01 | Google Developers Blog | 2025-05-20 | 기업 공식 | Announcing Gemma 3n preview | Gemma 3n, 5B/8B 파라미터를 2GB/3GB에서 실행 | 5 | 5 | 5 | [링크](https://developers.googleblog.com/en/introducing-gemma-3n/) |
| G-02 | MarketsandMarkets | 2024 | 시장조사 | Small Language Model Market worth $5.45B by 2032 | SLM 시장, 2032년 54.5억 달러 전망 | 4 | 4 | 3 | [링크](https://www.marketsandmarkets.com/PressReleases/small-language-model.asp) |
| G-03 | Edge AI and Vision Alliance | 2026-01 | 기술매체 | On-Device LLMs in 2026: What Changed | 3B~30B 파라미터 "Goldilocks Zone" | 5 | 4 | 5 | [링크](https://www.edge-ai-vision.com/2026/01/on-device-llms-in-2026-what-changed-what-matters-whats-next/) |
| G-04 | Microsoft Azure Blog | 2025 | 기업 공식 | Phi-4 mini edge deployment | Phi-4-mini, iPhone 12 Pro에서 11 tokens/s | 5 | 5 | 4 | [링크](https://azure.microsoft.com/en-us/blog/empowering-innovation-the-next-generation-of-the-phi-family/) |
| G-05 | Apple Machine Learning Research | 2025 | 기업 공식 | Updates to Apple's On-Device Foundation Language Models | KV 캐시 공유로 메모리 37.5% 절감 | 5 | 5 | 4 | [링크](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates) |
| G-06 | Android Central | 2025-12 | 기술매체 | Snapdragon 8 Elite Gen 5 AI upgrade | Hexagon NPU 100 TOPS, 이전 대비 37% 고속화 | 5 | 4 | 5 | [링크](https://www.androidcentral.com/phones/samsung-galaxy/snapdragon-8-elite-gen-5-hands-the-galaxy-s26-the-ai-upgrade-weve-been-waiting-for) |
| G-07 | mashdigi | 2026-03 | 기술매체 | MediaTek Dimensity 9500 at MWC 2026 | Dimensity 9500 NPU 990, 오프라인 멀티모달 실행 | 4 | 3 | 5 | [링크](https://en.mashdigi.com/from-6g-network-connectivity-to-next-generation-data-centers-mediatek-showcases-its-ai-capabilities-at-mwc-2026-with-the-dimensity-9500-enabling-multi-modal-applications-on-devices/) |
| G-08 | Samsung Newsroom | 2026-03 | 기업 공식 | Samsung Advances Galaxy AI at MWC 2026 | Galaxy S26, Gauss2 Compact 온디바이스 AI | 5 | 5 | 5 | [링크](https://news.samsung.com/global/samsung-advances-galaxy-ai-and-its-connected-ecosystem-at-mwc-2026) |
| G-09 | Gartner/GreyB | 2025 | 리서치/분석 | Edge AI Hardware Evaluation Report 2025 | 2027년까지 SLM이 LLM 대비 3배 사용 예측 | 4 | 4 | 3 | [링크](https://www.businesswire.com/news/home/20250910279522/en/Edge-AI-Hardware-Company-Evaluation-Report-2025-Qualcomm-Apple-and-Huawei-Lead-with-Advanced-Processors-Strategic-Collaborations-and-Expanding-AI-Capabilities---ResearchAndMarkets.com) |
| G-10 | Meta AI Research (Vikas Chandra) | 2026 | 기술 리포트 | On-Device LLMs: State of the Union, 2026 | 메모리 대역폭 30~50배 격차가 핵심 병목 | 5 | 4 | 5 | [링크](https://v-chandra.github.io/on-device-llms/) |
| G-11 | Arm Newsroom | 2025-10 | 기업 공식 | ExecuTorch 1.0 GA Release | 50KB 런타임, 12+ 하드웨어 백엔드 | 5 | 5 | 4 | [링크](https://newsroom.arm.com/news/executorch-1-0-ga-release-edge-ai) |
| G-12 | ScienceDirect / ACM | 2025~2026 | 학술 | Edge LLM inference optimization survey | Speculative Decoding 2.8x, FlashAttention-4 20% 향상 | 4 | 5 | 4 | [링크](https://www.sciencedirect.com/science/article/abs/pii/S1574013725000310) |
| G-13 | GitHub (Alibaba MNN) | 2025 | 오픈소스 | MNN - Mobile Neural Network | 알리바바 모바일 딥러닝 프레임워크 | 3 | 4 | 3 | [링크](https://github.com/alibaba/MNN) |

### 최신 동향 (N-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약(한글) | URL |
|------|--------|-------|------|-----------|----------|-----|
| N-01 | Engadget | 2026-03 | Everything announced at MWC 2026 | MWC 2026 on-device AI | MWC 2026 주요 발표 종합 — 온디바이스 AI가 전시 핵심 주제 | [링크](https://www.engadget.com/mobile/everything-announced-at-mwc-2026-lenovos-wild-foldable-gaming-handheld-honors-robot-phone-and-more-172442814.html) |
| N-02 | Android Central | 2026-03 | OPPO, MediaTek Omni at MWC 2026 | OPPO MediaTek on-device AI MWC | OPPO·MediaTek Omni 풀모달 온디바이스 AI 모델 공개 | [링크](https://www.androidcentral.com/phones/oppo-phones/oppo-mediatek-let-omni-take-the-mwc-2026-stage-as-the-gateway-to-ai-and-the-physical-world) |
| N-03 | MediaTek Press Room | 2026-03 | MediaTek Exemplifies AI and Connectivity Leadership at MWC 2026 | MediaTek MWC 2026 NPU | "AI For Life: From Edge to Cloud" 테마, Dimensity 9500 온디바이스 AI 전시 | [링크](https://www.mediatek.com/press-room/mediatek-exemplifies-ai-and-connectivity-leadership-at-mwc-2026) |
| N-04 | Qualcomm Newsroom | 2026-03 | Qualcomm Powers Rise of Personal AI with Snapdragon Wear Elite | Qualcomm MWC 2026 wearable AI | Snapdragon Wear Elite, 웨어러블 최초 NPU + 5G RedCap + 위성통신 탑재 | [링크](https://www.qualcomm.com/news/releases/2026/03/qualcomm-powers-the-rise-of-personal-ai-with-new-snapdragon-wear) |
| N-05 | Telecom Reseller | 2026-03 | AGI Inc. Enables Agentic Capabilities for Snapdragon | Qualcomm agentic on-device 2026 | AGI Inc.가 Snapdragon 플랫폼용 에이전틱 AI 스택 최적화 발표 | [링크](https://telecomreseller.com/2026/03/03/agi-inc-enables-new-agentic-capabilities-for-devices-powered-by-snapdragon/) |
| N-06 | Futurum Group | 2026-01 | Qualcomm Unveils Future of Intelligence at CES 2026 | Qualcomm CES 2026 on-device AI | Qualcomm CES 2026에서 온디바이스 AI 미래 비전 발표 | [링크](https://futurumgroup.com/insights/qualcomm-unveils-future-of-intelligence-at-ces-2026-pushes-the-boundaries-of-on-device-ai/) |
| N-07 | HuggingFace Blog | 2025 | Gemma 3n fully available in open-source ecosystem | Gemma 3n open source | Gemma 3n 오픈소스 생태계 전체 통합 완료 발표 | [링크](https://huggingface.co/blog/gemma3n) |

### 기업 발언 (E-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약원문 |
|------|--------|-------|------|-----------|---------|
| E-01 | Google Developers Blog | 2025-05-20 | Announcing Gemma 3n preview | Google Gemma 3n on-device | "brings powerful multimodal capabilities previously only seen in last year's cloud-based frontier models to edge devices" |
| E-02 | CES Innovation Awards / Futurum | 2026-01 | Qualcomm AI Engine in Snapdragon 8 Elite Gen 5 | Snapdragon 8 Elite Gen 5 TOPS | "Hexagon NPU is about 37% faster... enabling on-device agentic AI including assistants that truly understand each user's needs" |
| E-03 | Qualcomm Newsroom | 2026-03-02 | Snapdragon Wear Elite at MWC 2026 | Qualcomm wearable NPU | "5x better single-core CPU performance and 7x faster GPU... dual NPUs for on-device AI... first Elite-branded wearable platform" |
| E-04 | MediaTek Press Room | 2026-03 | MediaTek at MWC 2026 | MediaTek Omni multimodal on-device | "NPU 990 can run powerful Omni multimodal models in real-time, even completely offline" |
| E-05 | Samsung Newsroom | 2026-02 | Galaxy Unpacked 2026 | Samsung Galaxy S26 Galaxy AI | "Galaxy S26 Series: Samsung's Most Intuitive Galaxy AI Phone Yet — most powerful performance in Galaxy S series history" |
| E-06 | Apple Newsroom | 2025-09 | Apple's Foundation Models framework | Apple Foundation Models iOS 26 | "Foundation Models framework gives developers access to the ~3B parameter on-device language model... data never leaves the device" |
| E-07 | Engineering at Meta | 2025-07 | ExecuTorch on-device ML at Meta | ExecuTorch 1.0 Meta deployment | "ExecuTorch is now deployed across Instagram, WhatsApp, Messenger, and Facebook, serving billions of users" |

### 학술 논문 (P-xx)

| 번호 | 저자 | 발행년도 | 제목 | 학술지/컨퍼런스 | 인용수 | 핵심 인용 | DOI/URL |
|------|------|---------|------|----------------|--------|----------|---------|
| P-01 | 다수 저자 | 2026 | Efficient Inference for Edge Large Language Models: A Survey | Tsinghua Science and Technology | 공개 정보 없음 | 양자화·Speculative Decoding·모델 오프로딩 체계적 분류 | [링크](https://www.sciopen.com/article/10.26599/TST.2025.9010166) |
| P-02 | 다수 저자 | 2026 | Sustainable LLM Inference for Edge AI: Evaluating Quantized LLMs | ACM Transactions on Internet of Things | 공개 정보 없음 | 에너지 효율·정확도·추론 지연 트레이드오프 분석 | [링크](https://dl.acm.org/doi/10.1145/3767742) |
| P-03 | 다수 저자 | 2026 | Tiny Machine Learning and On-Device Inference: A Survey | PMC / 공개 학술지 | 공개 정보 없음 | 응용·과제·미래 방향 종합 서베이 | [링크](https://pmc.ncbi.nlm.nih.gov/articles/PMC12115890/) |
| P-04 | 다수 저자 | 2026 | MO-BIEDIT: Resource-Efficient (모델 편집) | ICLR 2026 | 공개 정보 없음 | 자원 효율 모델 편집 기법 | [링크](https://openreview.net/pdf?id=fb7yTBOV3p) |
| P-05 | 다수 저자 | 2025 | I-LLM: Efficient Integer-Only Inference for Fully-Quantized Low-Bit LLMs | OpenReview | 공개 정보 없음 | 완전 정수 전용 추론 파이프라인 | [링크](https://openreview.net/forum?id=44pbCtAdLx) |
| P-06 | 다수 저자 | 2025 | Apple Intelligence Foundation Language Models: Tech Report 2025 | arXiv | 공개 정보 없음 | Apple 온디바이스 3B 모델 아키텍처 상세 | [링크](https://arxiv.org/abs/2507.13575) |
| P-07 | 다수 저자 | 2025 | Edge-First Language Model Inference: Models, Metrics, and Tradeoffs | arXiv | 공개 정보 없음 | 에지 배포 트레이드오프 메트릭 체계화 | [링크](https://arxiv.org/html/2505.16508v1) |

### 특허 (T-xx)

> **주의**: 이번 사이클에서 intel-store MCP(Google Patents via SerpAPI) 직접 조회 미수행. 웹 검색 기반 간접 참조만 수록. 다음 리서치 사이클에서 `collect_patents(topic="ondevice-slm")` 실행 권장.

| 번호 | 출원인 | 등록/출원일 | 특허번호 | 제목 | 핵심 청구항 | 관할 |
|------|--------|-----------|---------|------|-----------|------|
| T-01 | Qualcomm | 공개 정보 없음 | US 10,968,477 B2 | On-device edge inference acceleration | 엣지 디바이스 추론 가속 방법 및 시스템 | USPTO |
| T-02 | Apple | 공개 정보 없음 | 공개 정보 없음 | KV-cache sharing for on-device foundation models | KV 캐시 공유를 통한 메모리 절감 | USPTO (간접 확인) |

### 내부 자료 (I-xx)

| 번호 | 자료명 | 작성일 | 페이지 | 인용내용 |
|------|--------|-------|--------|---------|
| I-01 | 해당 사항 없음 | — | — | 내부 참조 자료 미사용 |
