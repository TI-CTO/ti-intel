---
topic: multimodal-vlm
date: 2026-03-12
confidence: high
status: completed
sources_used: [websearch]
---

# Research: 멀티모달 VLM — 통신사 적용 심층 분석

## 연구 질문

> Discover에서 도출한 즉시착수 3건(고객 서비스 비전 AI, B2B 문서 AI, 네트워크 비전 모니터링)의 기술적 실현 가능성, 비용 구조, 경쟁 상황을 심층 검증한다.

---

## 핵심 발견

### 1. 글로벌 통신사의 이미지 VLM 고객 서비스는 아직 파일럿 단계

Deutsche Telekom(Sprinklr CCaaS, 41,000 상담원), Verizon(Project 624, AI 이탈방지 10만 명), SKT(A.X K1 이미지 멀티모달 2026H1) 모두 텍스트 AI 중심이며, **이미지 기반 VLM 자동 진단의 공개 FCR(1차 해결율) 수치는 아직 없다.** 즉 선점 기회가 열려 있다.

### 2. 온프레미스 VLM은 일 10만 건 이상에서 API 대비 TCO 우위

- GPT-4o 이미지 처리: 월 $8,500~25,000 (일 10만 건)
- 온프레미스 A100: 월 $2,000~4,500 (전력·유지 포함)
- **손익분기**: 월 ~9,500만 토큰(일 315만 토큰) 이상에서 온프레미스 유리
- 초기 GPU CapEx $15K~60K + 엔지니어링 비용 고려 필요

### 3. 한국어 VLM 성능은 상용 API 대비 11점 격차

CC-OCR 벤치마크 한국어: Gemini-1.5-Pro **80.0점** > GPT-4o 74.2점 > Qwen-VL-Max **69.1점**(온프레미스 최강). 라틴계 언어 대비 전반적으로 낮으며, 한국어 특화 파인튜닝이 차별화 포인트.

### 4. 엣지 VLM 배포는 INT4 양자화로 현실화

MBQ(CVPR 2025)로 W4A8 정확도 손실 1.1% 이내. Moondream 2B INT4는 2.45GB VRAM에서 184 tokens/s 달성. MEC 100ms 목표는 비전 인코더-엣지 / LLM 디코더-클라우드 분리 아키텍처로 달성 가능.

### 5. OCR-free 문서 AI는 PaddleOCR-VL이 SOTA

PaddleOCR-VL 1.5(0.9B): OmniDocBench 94.5점 SOTA, 109개 언어(한국어 포함), 오픈소스. Mistral OCR 3: $2/1,000페이지. 한국어 특화 1위는 **업스테이지**($45M 투자, 삼성·보험사 납품).

### 6. 실시간 영상 처리는 H100에서 8 FPS 수준

StreamingVLM(MIT): H100 1장에서 8 FPS, 3시간+ 무한 스트림 처리. VideoScan: RTX 4090에서 6 FPS. CCTV 전수 분석(25 FPS)은 불가 → **경량 비전 모델 1차 필터링 + VLM 이벤트 분석** 캐스케이드가 현실적.

---

## 기술 아키텍처 비교

### 고객 서비스 VLM 파이프라인

```
고객 사진 전송 → 전처리(EXIF 제거, 마스킹, 리사이즈)
             → VLM 추론(Qwen2.5-VL 7B, vLLM)
             → 신뢰도 게이팅(≥0.85 자동응답, <0.85 에스컬레이션)
             → AICC 연동(CRM 티켓 생성)
```

### MEC 엣지 배포 아키텍처

```
[엣지 단말] → [MEC 노드: 비전 인코더 + 경량 추론]
                    ↓ (복잡 쿼리만)
             [클라우드: 대형 VLM 디코더]
```

- MEC 자체 지연: 20ms 이하 → 모델 추론 예산 80ms
- 5G 네트워크 슬라이싱으로 AI 추론 우선순위 보장 가능

---

## 모델 선정 가이드

### 용도별 최적 모델

| 용도 | 모델 | 파라미터 | VRAM (INT4) | 추론 속도 | 근거 |
|------|------|---------|-------------|----------|------|
| 고객 서비스 (서버) | Qwen2.5-VL 7B | 7B | ~5GB | ~21 req/s (A100) | DocVQA 96.4%, 한국어 69.1점 |
| 문서 AI (서버) | PaddleOCR-VL 1.5 | 0.9B | <2GB | 고속 | OmniDocBench 94.5 SOTA |
| CCTV 분석 (서버) | StreamingVLM | 7B+ | ~17GB | 8 FPS (H100) | 무한 스트림 안정 처리 |
| 엣지 경량 | Moondream 2B | 2B | 2.45GB | 184 tok/s | RTX 3090급 엣지 서버 |
| 모바일/IoT | SmolVLM-256M | 0.26B | ~0.8GB | 80 tok/s | 브라우저 실행 가능 |

### 양자화 방법 선정

| 방법 | 메모리 절감 | 정확도 유지 | 최적 환경 |
|------|-----------|-----------|----------|
| AWQ INT4 | ~75% | 95% | 저지연 엣지 GPU |
| MBQ W4A8 | ~75% | 98.9% (VLM 특화) | VLM 전용 배포 |
| GGUF Q4_K_M | ~75% | 92% | CPU+GPU 혼합 엣지 |
| NVFP4 | ~75% | INT4보다 우수 | H100/A100 MEC |

### 추론 프레임워크 선정

| 프레임워크 | 최적 용도 | 처리량 |
|-----------|---------|--------|
| vLLM | 멀티유저 MEC 서버 | 120~160 req/s |
| TensorRT Edge-LLM | NVIDIA Jetson 엣지 | 최고 성능 |
| llama.cpp | CPU/GPU 혼합 엣지 | 단일 스트림 |
| MLC-LLM | iOS/Android/브라우저 | 크로스플랫폼 |

---

## 국내 경쟁 환경

### 통신사

| 통신사 | 멀티모달 전략 | 강점 | 약점 |
|--------|-------------|------|------|
| **SKT** | A.X K1 → 이미지(2026H1) → 음성·영상 → 1000B | 자체 모델, MAU 1,000만 | 멀티모달 아직 미출시 |
| **KT** | 믿:음 K 문서 인식 + 에이전틱 패브릭 | B2B 실증 경험, MS 파트너십 | VLM 독립 서비스 미발표 |

### 문서 AI 플레이어

| 플레이어 | 포지션 | 한국어 | 비고 |
|---------|--------|--------|------|
| **업스테이지** | 한국어 문서 AI 1위 | 최강 | $45M 투자, 삼성·보험사 |
| **NAVER CLOVA OCR** | 네이버 클라우드 생태계 | 강함 | 영수증·명함 특화 |
| **PaddleOCR-VL** | 글로벌 SOTA | 지원(109개 언어) | 한국어 특화 부족 |
| **Mistral OCR 3** | 가격 경쟁력 | 라틴 대비 열위 | $2/1,000페이지 |

---

## 비용 분석 상세

### 고객 서비스 VLM — 일 10만 건 시나리오

| 항목 | 상용 API (GPT-4o) | 온프레미스 (Qwen 7B) |
|------|-------------------|---------------------|
| 월 API/추론 비용 | $8,500~25,000 | $0 (자체 GPU) |
| GPU 인프라 | 불필요 | A100 80GB × 2: $30,000~60,000 (CapEx) |
| 월 운영 비용 | API 비용만 | $2,000~4,500 (전력·유지·엔지니어링) |
| 연간 TCO | $102,000~300,000 | $54,000~84,000 (2년차~) |
| **프라이버시** | 국외 이전 동의 필요 | 온프레미스 처리, 동의 불요 |
| **한국어 성능** | 74.2~80.0점 | 69.1점 (11점 격차) |

**판단**: 일 10만 건 이상이면 온프레미스가 비용·프라이버시 모두 우위. 한국어 성능 격차(11점)는 파인튜닝으로 축소 가능.

---

## 프라이버시/규제

개인정보보호위원회 2025.8. 생성형 AI 안내서 기준:
- 고객 제출 이미지: **서비스 계약 수행 목적**으로 처리 가능 (동의 재취득 불요)
- AI 모델 **학습 재사용**: 별도 동의 또는 가명처리 필수
- **해외 API**(GPT-4V, Gemini): 국외 이전 고지·동의 필요 → 온프레미스 우위
- 원본 이미지 즉시 삭제(90일 이내) 권장
- 전처리 필수: EXIF 메타데이터 제거, 얼굴/배경 마스킹

---

## 신뢰도 평가

### 높은 확신
- **엣지 VLM 하드웨어 요구사항**: Nature Communications 논문 + NVIDIA 공식 벤치마크 + 다중 오픈소스 실측 데이터
- **양자화 성능**: CVPR 2025 MBQ 논문 — 피어리뷰 완료
- **비용 분석**: arXiv 손익분기 분석 + 복수 벤더 가격표 교차 검증
- **한국어 OCR 벤치마크**: CC-OCR 벤치마크(arXiv) — 16개 모델 체계적 비교
- **개인정보보호 규제**: 개인정보보호위원회 공식 안내서 (2025.8)

### 추가 검증 필요
- **통신사 이미지 VLM FCR 수치**: 어떤 통신사도 공식 발표 없음 → 자체 파일럿 필요
- **한국어 파인튜닝 효과**: Qwen 69.1 → 목표 75+ 달성 가능 여부 실험 필요
- **MEC 실배포 지연시간**: 이론 100ms 가능하나 실환경(네트워크 변동, 동시 접속) 검증 필요
- **KT 멀티모달 전략**: 공개 정보 부족, 에이전틱 패브릭과의 통합 방향 추가 확인

---

## 액션 아이템

- [ ] **고객 서비스 VLM 파일럿**: Qwen2.5-VL 7B + vLLM으로 모뎀 LED 진단 PoC 구축 → FCR 측정
- [ ] **한국어 파인튜닝**: Qwen2.5-VL 7B에 통신 장비 이미지 + 한국어 라벨 데이터셋으로 파인튜닝 → CC-OCR 75+ 목표
- [ ] **문서 AI PoC**: PaddleOCR-VL 1.5로 통신사 내부 계약서/청구서 자동 처리 파일럿
- [ ] **MEC 배포 테스트**: Moondream 2B INT4를 MEC 노드에 배포, 100ms 이하 지연시간 실측
- [ ] **CCTV 캐스케이드 설계**: YOLO 1차 필터링 + StreamingVLM 이벤트 분석 아키텍처 PoC
- [ ] **개인정보 영향평가**: 고객 이미지 처리에 대한 DPIA(Data Protection Impact Assessment) 수행

---

## 참고 자료

### 고객 서비스 VLM
| # | 출처명 | URL | 유형 | 날짜 |
|---|--------|-----|------|------|
| CS-01 | Deutsche Telekom × Sprinklr CCaaS | [링크](https://www.sprinklr.com/stories/deutsche-telekom/) | case | 2025 |
| CS-02 | Verizon Project 624 AI Overhaul | [링크](https://blog.tmcnet.com/blog/rich-tehrani/ai/verizon-unveils-project-624-ai-powered-overhaul-of-customer-support.html) | news | 2025 |
| CS-03 | SKT CEO MWC 2026 AI Native Strategy | [링크](https://www.prnewswire.com/news-releases/sk-telecom-ceo-unveils-ai-native-strategy-at-mwc26-302700470.html) | IR | 2026-03 |
| CS-04 | CC-OCR Benchmark (한국어 OCR 비교) | [링크](https://arxiv.org/html/2412.02210v2) | paper | 2024-12 |
| CS-05 | On-Premise LLM Break-Even Analysis | [링크](https://arxiv.org/html/2509.18101v3) | paper | 2025-09 |
| CS-06 | 개인정보보호위원회 생성형 AI 안내서 | [링크](https://www.privacy.go.kr/front/bbs/bbsView.do?bbsNo=BBSMSTR_000000000049&bbscttNo=20836) | gov | 2025-08 |

### 엣지 VLM 배포
| # | 출처명 | URL | 유형 | 날짜 |
|---|--------|-----|------|------|
| EV-01 | MBQ: VLM 양자화 (CVPR 2025) | [링크](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_MBQ_Modality-Balanced_Quantization_for_Large_Vision-Language_Models_CVPR_2025_paper.pdf) | paper | 2025 |
| EV-02 | StreamingVLM (MIT Han Lab) | [링크](https://arxiv.org/abs/2510.09608) | paper | 2025-10 |
| EV-03 | VideoScan | [링크](https://arxiv.org/abs/2503.09387) | paper | 2025-03 |
| EV-04 | MiniCPM-V 2.6 (Nature Communications) | [링크](https://www.nature.com/articles/s41467-025-61040-5) | paper | 2025 |
| EV-05 | Columbia Distributed VLMs | [링크](https://wimnet.ee.columbia.edu/wp-content/uploads/2025/04/DistributedVLMs_Efficient_Vision-Language_Processing_through_Cloud-Edge_Collaboration.pdf) | paper | 2025-04 |
| EV-06 | NVIDIA Jetson Edge AI Guide | [링크](https://developer.nvidia.com/blog/getting-started-with-edge-ai-on-nvidia-jetson-llms-vlms-and-foundation-models-for-robotics) | doc | 2025 |
| EV-07 | SmolVLM (HuggingFace) | [링크](https://huggingface.co/blog/smolvlm) | blog | 2025 |
| EV-08 | NVIDIA TensorRT Edge-LLM | [링크](https://developer.nvidia.com/blog/accelerating-llm-and-vlm-inference-for-automotive-and-robotics-with-nvidia-tensorrt-edge-llm) | doc | 2025 |

### 문서 AI B2B
| # | 출처명 | URL | 유형 | 날짜 |
|---|--------|-----|------|------|
| DA-01 | PaddleOCR-VL 1.5 | [링크](https://arxiv.org/html/2601.21957v1) | paper | 2026-01 |
| DA-02 | OmniDocBench (CVPR 2025) | [링크](https://github.com/opendatalab/OmniDocBench) | repo | 2025 |
| DA-03 | Mistral OCR 3 | [링크](https://mistral.ai/news/mistral-ocr) | product | 2026 |
| DA-04 | Upstage $45M Series B | [링크](https://www.prnewswire.com/news-releases/upstage-completes-45m-series-b-bridge-302534044.html) | news | 2025-08 |
| DA-05 | Grand View Research — IDP Market 2030 | [링크](https://www.grandviewresearch.com/industry-analysis/intelligent-document-processing-market-report) | report | 2025 |
| DA-06 | Precedence Research — IDP Market $43.9B | [링크](https://www.precedenceresearch.com/intelligent-document-processing-market) | report | 2025 |
| DA-07 | KT MWC 2026 에이전틱 패브릭 | [링크](https://www.youthdaily.co.kr/news/article.html?no=214413) | news | 2026-03 |
| DA-08 | NAVER CLOVA OCR | [링크](https://www.ncloud.com/v2/product/aiService/ocr) | product | 2026 |
