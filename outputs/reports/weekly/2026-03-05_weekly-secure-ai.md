---
type: weekly-monitor
domain: secure-ai
week: 2026-W10
date: 2026-03-05
l3_count: 7
deep_count: 5
---

# 주간 기술 동향: Secure AI (2026-W10)

## Executive Summary

| 세부기술 | 신호 | 핵심 내용 | 분석 |
|----|------|----------|------|
| OnDevice 양자암호 (PQC) | 🔴 긴급 | Thales 5G SIM PQC OTA 업그레이드 세계 최초 시연, NISTIR 8547 RSA/ECC 2030 폐기 로드맵 | Deep |
| 스팸피싱감지(통화전) | 🔴 긴급 | Google Scam Detection Samsung 확대, Syntelligence $37.5M JV, KT 1300억 피해예방 | Deep |
| OnDevice sLM | 🟡 주목 | MWC 2026 기점 양산 단계 전환, Gemma 3n/Apple 3B/Phi-4-mini 경쟁 본격화 | Deep |
| OnDevice 동형암호 (HE) | 🟡 주목 | 서울 FHE 표준화 회의, Niobium-SEMIFIVE-Samsung ASIC 계약, LGU+ ixi-Guardian 2.0 | Deep |
| Secure Vector Search | 🟡 주목 | OSDI/CCS/ICDE 최정상 학회 논문 다수, IronCore/Zama 실용화 가속 | Deep |
| 실시간 화자분할(2인) | 🟢 평온 | 특이사항 없음 | Quick |
| OCR 이미지 스팸 차단 | 🟢 평온 | 특이사항 없음 | Quick |

---

## 🟢 Quick 요약 (변화 미미)

### 실시간 화자분할(2인) — speaker-diarization
- 유의미한 신규 시그널 없음. 기존 기술 안정기 유지.

### OCR 이미지 스팸 차단 — ocr-image-spam
- 유의미한 신규 시그널 없음. 기존 탐지 체계 정상 운영 중.

---

## 🟡🔴 Deep 심층 분석

---

### OnDevice 양자암호 (PQC) — 🔴 긴급

2026년 3월 초 **두 건의 결정적 신호**: (1) Thales가 세계 최초로 배포된 5G SIM/eSIM에 PQC 원격 업그레이드 성공 (2026-03-01) — OTA 방식으로 기기 교체 없이 양자내성 알고리즘 적용, 통신사 PQC 전환 비용 구조를 근본적으로 변경. (2) NISTIR 8547이 2030년까지 RSA/ECC 단계적 폐기 로드맵을 공식화. 국내에서는 LG U+ SOLMAE 전자서명 TTA 표준 제정(2025-12), SKT-Thales 5G SUPI PQC 실증, KT 공공기관 하이브리드 PQC+QKD 망 구축 개시.

#### 기술 동향

**NIST 표준 및 마이그레이션 로드맵**

NISTIR 8547은 RSA/ECC의 **2030년 단계적 사용 제한**을 명시하고, 미 연방기관 마이그레이션 시한을 2026년으로 설정 [[pqc-G-03]](#ref-pqc-g-03). 확정 표준 3종:

| 표준 | 알고리즘 | 용도 | 임베디드 적합성 |
|------|---------|------|----------------|
| FIPS 203 | ML-KEM (Kyber) | 키 캡슐화 | ML-KEM-512: 소형 디바이스 적합 |
| FIPS 204 | ML-DSA (Dilithium) | 디지털 서명 | Samsung S3SSE2A HW 가속 [[pqc-E-02]](#ref-pqc-e-02) |
| FIPS 205 | SLH-DSA (SPHINCS+) | 해시 서명 | 서명 크기 큼, IoT 제약 |

HQC가 ML-KEM 수학적 백업으로 선정(2025-03), 표준 초안 2026년 예정.

**Thales 5G SIM PQC 원격 업그레이드 (2026-03-01)**

세계 최초 성과 [[pqc-E-01]](#ref-pqc-e-01)[[pqc-G-01]](#ref-pqc-g-01):
- 배포된 SIM/eSIM에 PQC 알고리즘을 **OTA 원격 다운로드**로 적용
- 서비스 단절, 기기 교체, 물리 카드 교체 없이 백그라운드 업그레이드
- **Crypto-Agility** 아키텍처: 표준/위협 진화에 따라 알고리즘 동적 교체 가능
- 전략적 의미: 수억 장의 SIM 교체 비용 제거, 3GPP Release 19/20 PQC AKA 선행 검증

**Samsung S3SSE2A Secure Element**

업계 최초 하드웨어 PQC 내장 보안칩 [[pqc-E-02]](#ref-pqc-e-02):
- FIPS 204 (ML-DSA) 구현: SW 전용 335.97ms → HW+SW **19.02ms** (**17배** 향상)
- 모바일 SE 턴키 솔루션, 샘플 출하 중
- RSA-2048 해독 "약 2028년 가능" 가정 하에 설계

**ESP32 MCU에서 Kyber512 구현** [[pqc-P-01]](#ref-pqc-p-01):
- ESP32 단일코어: Key Gen 15.24ms, Encaps 17.10ms, Decaps 18.57ms
- 듀얼코어 + HW 가속기: **최대 1.84배** 성능 향상
- 1억+ 대 배포 ESP32 MCU 기반 IoT PQC 적용 가능성 입증

**규제 일정표**

| 지역 | 규제/가이드라인 | 시한 | 내용 |
|------|--------------|------|------|
| 미국 | CNSA 2.0 (NSA) | 2027년 | NSS PQC 의무화 |
| 미국 | NISTIR 8547 | 2030년 | RSA/ECC 단계적 폐기 |
| EU | PQC Roadmap | 2030년 전환 | 고위험 섹터 우선 |
| 한국 | 정부 양자 로드맵 | 2028~2030년 | 국가핵심망·위성 양자암호 |

#### 플레이어 동향

| 기업 | 주요 활동 | 상용화 단계 | 출처 |
|------|---------|-----------|------|
| **Thales** | 5G SIM OTA PQC 업그레이드 세계 최초 시연, Samsung S3SSE2A 보안 OS 파트너 | 시연 완료, 통신사 배포 협의 | [[pqc-E-01]](#ref-pqc-e-01) |
| **Samsung** | S3SSE2A SE칩 샘플 출하 (HW PQC, FIPS 204), Exynos 2600 PQC 탑재 | 샘플 출하 완료, 양산 예정 | [[pqc-E-02]](#ref-pqc-e-02) |
| **SKT** | Thales와 5G SUPI PQC 실증, Q-HSM(QRNG+PUF+PQC) KCMVP 인증, Solteris KMS 출시 | 상용 장비 출시 완료 | [[pqc-N-04]](#ref-pqc-n-04) |
| **KT** | 하이브리드 QKD+PQC 솔루션, 2026년 공공기관 5개 분야 파일럿 | 2026년 파일럿 시작 | [[pqc-N-05]](#ref-pqc-n-05) |
| **LG U+** | SOLMAE(NTRU 격자) 전자서명 TTA 표준 제정(2025-12), IoT/임베디드 최적화 | TTA 표준 제정, 상용화 준비 | [[pqc-N-03]](#ref-pqc-n-03) |
| **Google** | Chrome PQC TLS 키 교환 배포, Android 코어 PQC 통합 진행 | 부분 배포 진행 중 | [[pqc-G-09]](#ref-pqc-g-09) |
| **Apple** | iMessage PQC 프로토콜 도입, iCloud PQC 암호화 | 일부 서비스 배포 | [[pqc-G-09]](#ref-pqc-g-09) |
| **wolfSSL** | ML-KEM, ML-DSA, HQC 자체 구현, Embedded World 2025 임베디드 PQC 솔루션 | 라이브러리 배포 완료 | [[pqc-G-10]](#ref-pqc-g-10) |

#### 시장 시그널

- PQC 시장 CAGR 37~46% 성장 전망 (조사기관별 3~5배 편차, 방향성만 [B]급 신뢰) [[pqc-G-11]](#ref-pqc-g-11)
- 미국 연방정부 향후 10년 PQC 투자 **$71억** 추정 [[pqc-G-04]](#ref-pqc-g-04)
- 한국 정부: 2026년 PQC+QKD 파일럿 5개 분야(통신·금융·국방·교통·우주) 동시 추진 [[pqc-N-05]](#ref-pqc-n-05)
- CISA "Harvest Now, Decrypt Later" 경고 강화 — 즉각적 마이그레이션 압력

**투자/파트너십**:
- Thales + 통신사 OTA PQC 파트너십 [[pqc-E-01]](#ref-pqc-e-01)
- SKT + IDQ: Solteris QKD-PQC 하이브리드 공동 출시 [[pqc-N-04]](#ref-pqc-n-04)
- KT + 신한은행: 하이브리드 양자보안 네트워크 [[pqc-N-05]](#ref-pqc-n-05)
- PQCA (Post-Quantum Cryptography Alliance): Linux Foundation 산하 오픈소스 연합 [[pqc-G-10]](#ref-pqc-g-10)

#### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| Kyber on ESP32 (arXiv 2503.10207) | 1억+ MCU에서 PQC 실용화 최초 종합 실증 | [[pqc-P-01]](#ref-pqc-p-01) |
| PQC for Industrial IoT (Scientific Reports) | ML-KEM + ML-DSA TLS 1.3 통합 IIoT 인증 | [[pqc-P-02]](#ref-pqc-p-02) |
| QORE: Quantum Secure 5G/B5G Core | 5G 코어망 PQC 통합 시 성능 영향 미미 | [[pqc-P-04]](#ref-pqc-p-04) |
| PQC in Cryptographic Libraries Survey | wolfSSL, liboqs, OpenSSL FIPS 203/204/205 지원 비교 | [[pqc-P-05]](#ref-pqc-p-05) |

#### 전략적 시사점

**기회**
- OTA PQC 업그레이드 시장 개화
- 국내 3사 파일럿 연계
- MCU/IoT PQC 경량화
- KpqC 한국형 표준화

**위협**
- 3GPP 표준 부재로 상호운용성 리스크
- 중국 특허 공세
- HNDL 공격 시급성
- 마이그레이션 시간 부족(NISTIR 2026 외곽 경계)

---

### 스팸피싱감지(통화전) — 🔴 긴급

스팸·보이스피싱 감지 기술은 **온디바이스 AI**와 **네트워크 레벨 사전 차단** 두 축으로 고도화. Google이 Gemini Nano 온디바이스 AI를 Galaxy S26에 탑재(2026-02-25), SKT·KT·LG U+ 3사가 각각 에이닷·후후·익시오 앱으로 통화 중 실시간 탐지 상용화. Syntelligence(5개 통신사 JV, $37.5M)가 네트워크 데이터 기반 사전 차단 시스템 개발 중. 학술 분야에서는 KoBERT+CNN-BiLSTM 멀티모달 융합(F1=0.994), RAG 기반 LLM(정확도 97.98%) 등 고성능 모델 확인.

#### 기술 동향

**기술 성숙도 (TRL)**

| 기술 계층 | TRL | 비고 |
|-----------|-----|------|
| 네트워크 레벨 사전 차단 (메타데이터 분석) | 8–9 | T-Mobile, KT 등 상용화 |
| 온디바이스 AI (통화중 실시간 텍스트 분석) | 7–8 | SKT 에이닷, Google Gemini Nano |
| 딥보이스 탐지 (음성 위변조 감지) | 6–7 | KT 3중 체계, 상용화 시작 |
| 멀티모달 (텍스트+음성 융합) | 5–6 | 연구 단계, 2025 논문 발표 |
| RAG 기반 LLM 실시간 탐지 | 4–5 | 연구 단계 (~98% 정확도) |

**통화전(Pre-Call) 사전 차단**:
- 메타데이터 기반 행동 시그니처 분석 — T-Mobile은 6분마다 모델 업데이트 [[sp-G-06]](#ref-sp-g-06)
- STIR/SHAKEN 발신번호 인증 — FCC 2025-09 3자 서명자 규제 강화 [[sp-G-14]](#ref-sp-g-14)
- Syntelligence: 5개 통신사 수십억 건 호 패턴으로 훈련 [[sp-G-07]](#ref-sp-g-07)

**통화중(In-Call) 실시간 탐지**:
- 온디바이스 LLM: Gemini Nano, 에이닷 자체 모델 — 서버 미전송 [[sp-G-02]](#ref-sp-g-02)[[sp-E-01]](#ref-sp-e-01)
- KT 3중 체계: AI 문맥 탐지 + 화자인식(범죄자 음성DB) + 딥보이스 탐지 [[sp-E-02]](#ref-sp-e-02)
- SKT 에이닷 전화: '의심/위험' 2단계 팝업·알림음·진동 [[sp-E-01]](#ref-sp-e-01)

#### 플레이어 동향

**글로벌**

| 기업 | 동향 | 출처 |
|------|------|------|
| **Google** | Gemini Nano Scam Detection → Galaxy S26 확대 (2026-02-25), Android 생태계 전반 확대 전략 | [[sp-G-02]](#ref-sp-g-02)[[sp-G-03]](#ref-sp-g-03) |
| **Samsung** | Galaxy S26에 Google Scam Detection 네이티브 통합 (Phone by Google 앱 불필요) | [[sp-G-03]](#ref-sp-g-03) |
| **T-Mobile** | Scam Shield: 네트워크 레이어 6분 간격 AI 업데이트, 타사 대비 30% 우위 | [[sp-G-06]](#ref-sp-g-06) |
| **Syntelligence** | DT·e&·Singtel·SKT·SoftBank 5사 JV, $37.5M, Security Shield 개발 중 | [[sp-G-07]](#ref-sp-g-07)[[sp-G-15]](#ref-sp-g-15) |

**국내**

| 기업 | 동향 | 성과 | 출처 |
|------|------|------|------|
| **SKT** | 에이닷 전화 AI 보이스피싱 탐지 (2025-12-01), 온디바이스 AI 처리, Syntelligence 의장사 | — | [[sp-E-01]](#ref-sp-e-01) |
| **KT** | 후후 기반 AI 보이스피싱 탐지 (2025-01), 2025-07 v2.0 3중 체계, 국무조정실 최우수 | 44백만 건 분석, 1,300억 피해예방, 정확도 93%+ | [[sp-E-02]](#ref-sp-e-02)[[sp-E-03]](#ref-sp-e-03) |
| **LG U+** | 익시오(ixi-O) 통화 중 탐지, 안티딥보이스, 국내 유일 악성 앱 서버 추적 | 800개 악성 서버 추적, 3.3만명 보호, 1.8조 피해예방 추산 | [[sp-E-04]](#ref-sp-e-04)[[sp-E-05]](#ref-sp-e-05) |
| **과기정통부** | AI 보이스피싱 공동대응 플랫폼 2026~2027 구축 추진 | — | [[sp-E-07]](#ref-sp-e-07) |

#### 시장 시그널

- 글로벌 모바일 피싱 방어 시장: $2.67B(2024) → $15.99B(2034), CAGR 19.6% [[sp-G-08]](#ref-sp-g-08)
- 전 세계 스팸 피해: $41.8B 손실(2024), 미국 성인 92% 스팸 전화 수신 [[sp-G-07]](#ref-sp-g-07)
- 한국 보이스피싱: 건당 평균 4,100~5,384만원 피해 [[sp-E-02]](#ref-sp-e-02)[[sp-E-04]](#ref-sp-e-04)
- 플랫폼 통합 경쟁: Google이 Android OS 레벨에서 탐지 흡수 → 독립 앱 서비스 위협
- FCC STIR/SHAKEN 확대 + 과기정통부 공동플랫폼 → 시장 의무 참여 수요

#### 학술 동향 (주요 논문)

| 논문 | 핵심 결과 | 출처 |
|------|---------|------|
| Multimodal Voice Phishing (MDPI Applied Sciences, 2025-10) | KoBERT+CNN-BiLSTM 8:2 융합, **F1=0.994** | [[sp-G-10]](#ref-sp-g-10) |
| RAG-Based LLM Fraud Detection (arXiv, 2025-01) | 정확도 **97.98%**, F1 97.44%, 정책 재훈련 불필요 | [[sp-P-02]](#ref-sp-p-02) |
| SpaLLM-Guard (arXiv, 2025-01) | Mixtral Fine-tuning **98.61%** 정확도 | [[sp-G-11]](#ref-sp-g-11) |
| Vishing Survey (ScienceDirect, 2025) | 미국 30만+/년 vishing 피해, 최초 종합 로드맵 | [[sp-G-12]](#ref-sp-g-12) |
| LLM Spam Detection Vulnerability (arXiv, 2025-04) | GPT2/BERT 탐지기 적대적 공격 취약성 | [[sp-G-11]](#ref-sp-g-11) |

#### 전략적 시사점

**기술 트렌드**
- 탐지 레이어 이원화(네트워크+온디바이스)
- 딥보이스 탐지 필수화
- 멀티모달 연구 성숙(F1=0.994)
- 공격자-방어자 군비경쟁 구도

**기회**
- 온디바이스 프라이버시 우위
- 멀티모달 탐지 상용화 문턱 근접

**위협**
- Google Android OS 레벨 탐지 흡수가 독립 앱 기반 사업자에 위협
- Syntelligence 네트워크 데이터 독점

---

### OnDevice sLM — 🟡 주목

MWC 2026을 기점으로 온디바이스 SLM 시장이 **실증→양산 단계 전환점**을 맞이. Qualcomm Snapdragon 8 Elite Gen 5(100 TOPS), MediaTek Dimensity 9500(NPU 990), Apple A19 Pro(~35 TOPS) 등 NPU 성능 도약. Google Gemma 3n(E2B/E4B 멀티모달), Apple ~3B(KV 캐시 공유 메모리 37.5% 절감), Microsoft Phi-4-mini(3.8B, iPhone 12 Pro 11 tok/s) 경쟁 본격화. Meta ExecuTorch 1.0 GA가 배포 표준화. 핵심 병목: 모바일 메모리 대역폭(50~90 GB/s) vs 데이터센터(2~3 TB/s) 30~50배 격차 [[slm-G-10]](#ref-slm-g-10).

#### 기술 동향

**모델 아키텍처 혁신**
- 파라미터 "Goldilocks Zone": 3B~7B가 성능-제약 최적 교점 [[slm-G-03]](#ref-slm-g-03)
- Google Gemma 3n PLE(Per-Layer Embeddings): 5B/8B 모델을 2GB/3GB에서 실행 [[slm-G-01]](#ref-slm-g-01)
- Apple KV 캐시 공유: 2블록 5:3 분할로 메모리 37.5% 절감 [[slm-G-05]](#ref-slm-g-05)
- 4-bit PTQ 사실상 표준(GPTQ, AWQ), INT8 정확도 손실 <6%, SpinQuant, BitNet 1.58-bit(연구단계)
- Speculative Decoding: 2.2~3.6배 속도 향상 [[slm-G-10]](#ref-slm-g-10)

**하드웨어 NPU 역량 (2026 플래그십)**

| SoC | NPU 성능 | 특징 | 출처 |
|-----|---------|------|------|
| Qualcomm Snapdragon 8 Elite Gen 5 | ~100 TOPS | Hexagon NPU, 37% 고속화 | [[slm-G-06]](#ref-slm-g-06) |
| MediaTek Dimensity 9500 | ~50 TOPS | NPU 990, 멀티모달 오프라인 | [[slm-G-07]](#ref-slm-g-07) |
| Apple A19 Pro (Neural Engine) | ~35 TOPS | MLX 최적화, 통합 메모리 | [[slm-G-10]](#ref-slm-g-10) |

**배포 프레임워크**

| 프레임워크 | 개발사 | 특징 | 출처 |
|-----------|--------|------|------|
| ExecuTorch 1.0 GA | Meta | 50KB 런타임, 12+ HW 백엔드, Instagram/WhatsApp/Messenger 전체 적용 | [[slm-G-11]](#ref-slm-g-11) |
| LiteRT (TFLite) | Google | Qualcomm NPU 최적화 | [[slm-G-06]](#ref-slm-g-06) |
| ONNX Runtime | Microsoft | Phi-4-mini iOS/Android 배포 | [[slm-G-04]](#ref-slm-g-04) |
| llama.cpp | 오픈소스 | GGUF 포맷 표준, CPU 추론 | — |

#### 플레이어 동향

| 기업 | 모델/제품 | 핵심 스펙 | 출처 |
|------|---------|---------|------|
| **Google** | Gemma 3n E2B/E4B | 5B/8B, 2-3GB, 멀티모달(이미지+오디오+비디오+텍스트) | [[slm-G-01]](#ref-slm-g-01) |
| **Apple** | Foundation Model ~3B | KV 캐시 공유, 2-bit QAT, iOS 26 개발자 API 개방 | [[slm-G-05]](#ref-slm-g-05) |
| **Microsoft** | Phi-4-mini (3.8B) | iPhone 12 Pro 11 tok/s, ONNX 크로스플랫폼 | [[slm-G-04]](#ref-slm-g-04) |
| **Samsung** | Gauss2 Compact | 멀티모달(언어+코드+이미지), Galaxy S26 탑재 | [[slm-G-08]](#ref-slm-g-08) |
| **Qualcomm** | Snapdragon 8 Elite Gen 5 + Wear Elite | 100 TOPS NPU, 웨어러블 최초 Elite NPU | [[slm-G-06]](#ref-slm-g-06)[[slm-N-04]](#ref-slm-n-04) |
| **MediaTek** | Dimensity 9500 | OPPO Omni 풀모달 온디바이스, AI 안경 데모 | [[slm-G-07]](#ref-slm-g-07)[[slm-N-03]](#ref-slm-n-03) |
| **Meta** | ExecuTorch 1.0 + Llama 3.2 (1B/3B) | 50KB 런타임, 수십억 사용자 대상 배포 | [[slm-G-11]](#ref-slm-g-11) |

#### 시장 시그널

- SLM 시장: 2032년 **$54.5B** 전망 (MarketsandMarkets) [[slm-G-02]](#ref-slm-g-02)
- 온프레미스/엣지 LLM: LLM 시장의 51.85% 점유, CAGR 27.25% [[slm-G-02]](#ref-slm-g-02)
- Gartner: 2027년까지 SLM 사용량 일반 LLM 대비 **3배** [[slm-G-09]](#ref-slm-g-09)
- 핵심 드라이버: 프라이버시 규제 강화, NPU 성능 도약, 배포 비용 절감, 오프라인 사용성

#### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| Efficient Inference for Edge LLMs (Tsinghua Sci. Tech., 2026) | 양자화·Speculative Decoding·오프로딩 체계적 분류 | [[slm-P-01]](#ref-slm-p-01) |
| Sustainable LLM Inference for Edge AI (ACM ToIT, 2026) | 에너지 효율·정확도·지연 삼각 트레이드오프 | [[slm-P-02]](#ref-slm-p-02) |
| Apple Foundation Language Models (arXiv, 2025) | 3B 모델 아키텍처 상세 | [[slm-P-06]](#ref-slm-p-06) |

#### 전략적 시사점

**기회**
- NPU 가속 모델 최적화 서비스 수요
- 한국어 특화 SLM
- 엔터프라이즈 온프레미스 SLM
- 웨어러블 AI

**위협**
- 빅테크 수직 통합(Apple/Google/Qualcomm 풀스택)
- 메모리 대역폭 병목
- 중국 생태계 경쟁(Alibaba MNN)
- 모델 파편화

---

### OnDevice 동형암호 (HE) — 🟡 주목

동형암호(FHE)가 연구·표준화·상용화 세 축에서 동시 가속. **표준화**: 제9회 HomomorphicEncryption.org 표준화 회의(서울, 2026.3.5-6) + FHE.org 컨퍼런스(타이페이, 2026.3.8) 연달아 개최. **하드웨어**: Niobium-SEMIFIVE-Samsung Foundry 삼각 파트너십(2026.2.19, ~$6.86M)으로 세계 최초 상용 FHE ASIC 개발 공식화. **소프트웨어**: OpenFHE 1.5.0 + FHECore GPU 논문 2주 내 연달아 발표. **산업 적용**: LG U+ ixi-Guardian 2.0에 CryptoLab 동형암호 적용 계획(MWC 2026).

#### 기술 동향

**TRL 현황 (2026.3)**

| 적용 영역 | TRL | 주요 근거 | 변화 |
|----------|-----|---------|------|
| 서버사이드 FHE (클라우드 AI) | 7-8 | Cerium: Llama3-8B 암호화 추론 134초 | 유지 |
| GPU 가속 FHE | 6-7 | FHECore 2.41x 명령어 감소 [[he-P-01]](#ref-he-p-01) | 상승 |
| ASIC/칩 FHE 가속기 | 5-6 | Niobium-SEMIFIVE 설계 계약 [[he-E-03]](#ref-he-e-03) | 상승 |
| 에지/하이브리드 HE | 5-6 | HHEML FPGA 구현 [[he-P-03]](#ref-he-p-03) | 유지 |
| 온디바이스 FHE (스마트폰) | 3-4 | Apple BFV (iOS 18), 82% 효율 감소 | 유지 |

**FHECore GPU 마이크로아키텍처 (2026.2.10)** [[he-P-01]](#ref-he-p-01):
- BU·Northeastern·KAIST·U.Murcia 공동연구. GPU SM에 FHE 전용 유닛 통합
- CKKS 명령어 **2.41x 감소**, 연산 **1.57x 향상**, E2E **2.12x 가속**, 부트스트래핑 **50% 감소**, 면적 오버헤드 **2.4%**

**Cerium: 최초 Llama3-8B FHE 추론** [[he-P-02]](#ref-he-p-02):
- 멀티 GPU 프레임워크, Llama3-8B 암호화 추론 **134초**, 부트스트래핑 **7.5ms** (CraterLake ASIC 수준)

**표준화 동향**:
- 제9회 HE.org 표준화 회의 (서울, 2026.3.5-6): Craig Gentry 기조연설 "Encrypted LLM Inference with Batching Across Users", NIST 업데이트 [[he-G-01]](#ref-he-g-01)
- FHE.org 컨퍼런스 (타이페이, 2026.3.8): Real World Crypto 2026 공동 [[he-G-03]](#ref-he-g-03)
- NIST MPTS 2026: FHE 명세·구현·평가 제출 수신 예정 [[he-G-09]](#ref-he-g-09)

#### 플레이어 동향

| 기업 | 역할 | 최근 동향 | 출처 |
|------|------|---------|------|
| **Niobium** | FHE ASIC 스타트업 | $23M+ 조달, SEMIFIVE-Samsung 8nm 설계 계약 | [[he-E-03]](#ref-he-e-03)[[he-N-01]](#ref-he-n-01) |
| **SEMIFIVE** | ASIC 설계 서비스 | Niobium 설계 수주(~$6.86M), Samsung Foundry 8LPU | [[he-E-03]](#ref-he-e-03) |
| **Zama** | FHE 소프트웨어 | $57M Series B, FHE 최초 유니콘($1B+), TFHE-rs/Concrete ML | [[he-G-04]](#ref-he-g-04) |
| **LG U+** | 통신사 | MWC 2026 ixi-Guardian 2.0, CryptoLab과 동형암호 ixi-O 적용 | [[he-E-04]](#ref-he-e-04)[[he-N-03]](#ref-he-n-03) |
| **CryptoLab** | FHE 솔루션 | LG U+ 협력, HEaan 기반 통화 데이터 암호화 AI 처리 | [[he-E-04]](#ref-he-e-04) |
| **Apple** | 소비자 기기 | swift-HE 오픈소스, iOS 18 Caller ID (BFV) | [[he-G-05]](#ref-he-g-05) |
| **Intel** | 반도체/클라우드 | DARPA DPRIVE ASIC 개발 중, FHE 표준화 주도 | [[he-G-10]](#ref-he-g-10) |
| **Duality** | FHE 플랫폼 | Google Cloud Confidential Computing 지원, GPU LLM 추론 | [[he-G-11]](#ref-he-g-11) |

#### 시장 시그널

- Niobium $23M 투자 + SEMIFIVE 설계 계약: 연구→설계→제조 밸류체인 완성 [[he-E-03]](#ref-he-e-03)
- Zama $57M Series B: FHE 최초 유니콘 — 블록체인+AI 이중 전략 [[he-G-04]](#ref-he-g-04)
- FHE 시장: $234M(2025) → CAGR 8~20% (기관별 편차 큼) [[he-G-12]](#ref-he-g-12)

#### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| FHECore: GPU Microarchitecture (2026.2) | 2.12x E2E, 50% 부트스트래핑 감소, 2.4% 면적 오버헤드 | [[he-P-01]](#ref-he-p-01) |
| Cerium: Multi-GPU Encrypted Inference (2025.12) | 최초 Llama3-8B FHE 추론 134초 | [[he-P-02]](#ref-he-p-02) |
| FHE-Agent: CKKS 자동 설정 (2025.11) | LLM 에이전트 기반 파라미터 자동화 | [[he-P-05]](#ref-he-p-05) |
| Low Communication ThFHE (KDDI Research) | 노이즈 패딩, 에지 분산 FHE | [[he-P-04]](#ref-he-p-04) |
| HHEML: Hybrid HE on Edge (2025.10) | 에지 오버헤드 50x 감소, FPGA 구현 | [[he-P-03]](#ref-he-p-03) |

#### 전략적 시사점

**기회**
- 한국이 FHE 표준화 중심지로 부상(서울 회의+SEMIFIVE)
- LG U+ ixi-O 최초 통신사 온디바이스 FHE
- 하이브리드 HE가 단기 진입점
- GPU FHE 가속 실용 임계점 도달

**위협**
- 온디바이스 FHE 81% 효율 감소/1,600J/+7°C
- IBM/MS/CryptoLab 원천 특허
- 표준화 2-4년 소요 가능

---

### Secure Vector Search — 🟡 주목

암호화 벡터 검색은 TRL 4~5 수준으로 실용화 가능성이 본격 검증. Compass(OSDI'25), PANTHER(CCS'25), PP-ANNS(ICDE'25) 등 최정상 학회 논문이 한꺼번에 등장. IronCore Labs(Cloaked AI, Gartner Cool Vendor 2025), Zama($57M 유니콘), Pinecone BYOC(2026.2)가 실질적 제품 출시. 임베딩 역추론 공격 92% 성공률 확인으로 벡터 DB 암호화 필수성 대두 [[sv-G-09]](#ref-sv-g-09).

#### 기술 동향

**TRL 현황**

| 구분 | TRL | 핵심 |
|------|-----|------|
| 거리보존암호화(DCPE) 기반 ANN | 5-6 | PP-ANNS: 기존 대비 **1,000배** 성능 향상 [[sv-P-02]](#ref-sv-p-02) |
| ORAM + HNSW 그래프 | 5 | Compass: 체감 지연 ~1초, 서버 메모리 3-7배 [[sv-P-01]](#ref-sv-p-01) |
| TEE 기반 | 6-7 | Azure Confidential AI, Google Private AI Compute 상용 |
| FHE 벡터 검색 | 3-4 | FRAG(arXiv'24), 실용 속도 미달 |
| 단일 서버 PIR/MPC | 5 | PANTHER: 1천만 포인트 18초, 7.8배 속도 [[sv-P-04]](#ref-sv-p-04) |

**핵심 기술**:
- **DCPE**: 거리 순서 유지하며 암호화 → PP-ANNS(ICDE'25) + HNSW 결합 [[sv-P-02]](#ref-sv-p-02)
- **ORAM + HNSW**: Compass(OSDI'25) 방향성 필터링·예측 프리페치 [[sv-P-01]](#ref-sv-p-01)
- **PANTHER**: PIR+비밀공유+가블드서킷+HE 혼합, 1천만 포인트 18초/284MB [[sv-P-04]](#ref-sv-p-04)
- **ppRAG**: DCPE + 차분프라이버시, RAG 파이프라인 통합 [[sv-G-01]](#ref-sv-g-01)

#### 플레이어 동향

| 기업 | 핵심 암호화 기술 | 최근 동향 | 출처 |
|------|----------------|---------|------|
| **IronCore Labs** | Scale & Perturb (속성보존암호화) | Gartner Cool Vendor 2025, 암호화 학습 확장 | [[sv-G-04]](#ref-sv-g-04) |
| **Zama** | FHE (TFHE/CKKS) | $57M Series B, 유니콘, Concrete ML v1.9 | [[sv-G-03]](#ref-sv-g-03) |
| **Microsoft Azure** | Intel SGX / AMD SEV-SNP (TEE) | Confidential AI Inferencing, Whisper 암호화 | [[sv-G-05]](#ref-sv-g-05) |
| **Google** | TEE (Titanium Intelligence Enclave) | Private AI Compute (2025-11), TPU 보호 | [[sv-G-06]](#ref-sv-g-06) |
| **Pinecone** | 고객 VPC 격리 | BYOC 런칭 (2026-02), zero-access 모델 | [[sv-G-07]](#ref-sv-g-07) |

#### 시장 시그널

- HIPAA 암호화 의무화 추진 검토 (2026 목표) [[sv-G-08]](#ref-sv-g-08) → 의료 벡터 DB 암호화 수요 급증
- EU AI Act 고위험 AI 데이터 거버넌스 강화
- 임베딩 역추론 공격 92% 성공률 [[sv-G-09]](#ref-sv-g-09) → 벡터 DB 암호화 필수화

#### 학술 동향 (주요 논문)

| 논문 | 학회 | 핵심 | 출처 |
|------|------|------|------|
| Compass: Encrypted Semantic Search | OSDI'25 | ORAM+HNSW, 체감 지연 ~1초 | [[sv-P-01]](#ref-sv-p-01) |
| PP-ANNS: Privacy-Preserving ANN | ICDE'25 | DCPE+HNSW, 1,000배 속도 향상 | [[sv-P-02]](#ref-sv-p-02) |
| PANTHER: Private ANN Search | CCS'25 | PIR+HE 혼합, 1천만 포인트 18초 | [[sv-P-04]](#ref-sv-p-04) |
| FRAG: Federated Vector DB for RAG | arXiv | 단일 키 HE, 연합 환경 ANN | [[sv-P-03]](#ref-sv-p-03) |
| ppRAG: Privacy-Preserving RAG | arXiv 2026-01 | DCPE+차분프라이버시, RAG 통합 | [[sv-P-05]](#ref-sv-p-05) |

#### 전략적 시사점

**기회**
- 국내 금융·의료 프라이빗 RAG 수요
- TEE 기반 단기 솔루션
- DCPE SDK 통합
- 산학협력 R&D 선점

**위협**
- FHE 수십~수백배 속도 저하
- 글로벌 학술 격차(미국 중심)
- 벤더 락인
- 표준화 부재

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **온디바이스 AI 보안의 수렴**: PQC(양자암호) + HE(동형암호) + sLM(소형언어모델)이 온디바이스에서 수렴. Samsung S3SSE2A(PQC) + Gauss2(sLM) + Apple swift-HE 등이 동일 디바이스 통합 추세
2. **통신사 보안 경쟁 격화**: SKT(Syntelligence JV + PQC), KT(보이스피싱 탐지 + PQC+QKD), LG U+(SOLMAE + ixi-Guardian) — 3사 모두 보안을 핵심 차별화 축으로 추진
3. **표준화 가속**: PQC(NIST FIPS 203/204/205), FHE(HE.org 서울 회의), 스팸 탐지(Syntelligence 네트워크 레벨) 모두 2026년 표준화 본격 진행
4. **프라이버시 규제가 시장 창출**: HIPAA 암호화 의무화, EU AI Act, NISTIR 8547 — 규제가 PQC/HE/Secure Search 시장 성장의 직접 동인

### 후속 조치 제안

- 🔴 **ondevice-pqc**: Thales OTA PQC 기술이 SIM 전환 비용 구조를 근본적으로 변경. `/wtis standard 양자동형암호` Go/No-Go 검증 권장
- 🔴 **spam-phishing-detection**: Syntelligence JV에 SKT 참여 + Google Scam Detection 확대. 경쟁 구도 변화 모니터링 필요

---

## References

> 전수 포함 — 삭제 금지. 각 L3 토픽별로 구분.

### OnDevice 양자암호 (PQC)

#### 글로벌 출처 (G-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-pqc-g-01"></a>pqc-G-01 | BusinessWire — Thales 5G SIM PQC OTA | https://www.businesswire.com/news/home/20260301594505/en/Thales-sets-a-world-first-in-quantum-safe-security-for-5G-networks | 공식 보도자료 | 2026-03-01 | A |
| <a id="ref-pqc-g-02"></a>pqc-G-02 | The Quantum Insider — Thales 5G SIM PQC 상세 | https://thequantuminsider.com/2026/03/02/thales-remote-post-quantum-5g-sim-upgrade/ | 전문 언론 | 2026-03-02 | B |
| <a id="ref-pqc-g-03"></a>pqc-G-03 | NIST CSRC — NISTIR 8547 (Draft) PQC 전환 표준 | https://csrc.nist.gov/pubs/ir/8547/ipd | 정부기관 | 2025-09 | A |
| <a id="ref-pqc-g-04"></a>pqc-G-04 | NCCoE (NIST) — PQC 마이그레이션 위험 프레임워크 | https://www.nccoe.nist.gov/crypto-agility-considerations-migrating-post-quantum-cryptographic-algorithms | 정부기관 | 2025 | A |
| <a id="ref-pqc-g-05"></a>pqc-G-05 | NIST CSRC — FIPS 203/204/205 PQC 3종 표준 | https://csrc.nist.gov/pubs/fips/203/final | 정부기관 | 2024-08-14 | A |
| <a id="ref-pqc-g-06"></a>pqc-G-06 | wolfSSL — FIPS 203/204/205 임베디드 적합성 분석 | https://www.wolfssl.com/what-are-fips-203-204-and-205/ | 기업 기술블로그 | 2025 | B |
| <a id="ref-pqc-g-07"></a>pqc-G-07 | GSMA — PQC in Mobile Networks 가이드라인 | https://www.gsma.com/solutions-and-impact/technologies/security/gsma_resources/post-quantum-cryptography-guidelines-for-telecom-use-cases-pq-03-2/ | 산업단체 | 2025 | A |
| <a id="ref-pqc-g-08"></a>pqc-G-08 | IEEE Xplore — Efficient HW Implementation of Kyber | https://ieeexplore.ieee.org/document/10642971/ | 학술 저널 | 2024-2025 | B |
| <a id="ref-pqc-g-09"></a>pqc-G-09 | PhishDef — Google/Apple PQC 전략 | https://phish-def.com/blog/cybersecurity/post-quantum-cryptography-why-google-and-apple-are-switching-and-you-should-too/ | 기업 블로그 | 2024-2025 | B |
| <a id="ref-pqc-g-10"></a>pqc-G-10 | wolfSSL/PQCA — ML-KEM/ML-DSA/HQC, liboqs v0.15.0 | https://www.wolfssl.com/wolfssl-unveils-post-quantum-cryptography-and-security-solutions-at-embedded-world-2025/ | 기업/오픈소스 | 2025 | B |
| <a id="ref-pqc-g-11"></a>pqc-G-11 | MarketsandMarkets/SNS Insider — PQC 시장 전망 | https://www.marketsandmarkets.com/PressReleases/post-quantum-cryptography.asp | 시장조사 | 2025-2026 | C |
| <a id="ref-pqc-g-12"></a>pqc-G-12 | PatentPC — Quantum Cryptography Patent & Investment Data | https://patentpc.com/blog/quantum-cryptography-growth-the-latest-data-on-post-quantum-security | 특허/시장 분석 | 2025-2026 | C |

#### 최신 동향 (N-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-pqc-n-01"></a>pqc-N-01 | EuropaWire — Thales 5G OTA PQC 유럽 배포 | https://news.europawire.eu/thales-advances-quantum-ready-5g-security-with-remote-post-quantum-cryptography-upgrade-technology/ | 뉴스 | 2026-03-02 | B |
| <a id="ref-pqc-n-02"></a>pqc-N-02 | Insight Korea — 국내 통신 3사 양자보안 종합 | https://www.insightkorea.co.kr/news/articleView.html?idxno=242127 | 뉴스 | 2026 | B |
| <a id="ref-pqc-n-03"></a>pqc-N-03 | 헤럴드경제 — LGU+ SOLMAE TTA 표준 제정 | https://biz.heraldcorp.com/article/10645601 | 뉴스 | 2025-12-30 | B |
| <a id="ref-pqc-n-04"></a>pqc-N-04 | SKT 뉴스룸 — QKD-PQC 하이브리드 Solteris 출시 | https://news.sktelecom.com/207758 | 공식 보도 | 2025 | A |
| <a id="ref-pqc-n-05"></a>pqc-N-05 | KT Enterprise — 공공기관 PQC 망 구축 2026 개시 | https://enterprise.kt.com/bt/mediareport/2544.do | 공식 보도 | 2025-12-31 | A |
| <a id="ref-pqc-n-06"></a>pqc-N-06 | 바이라인네트워크 — KpqC 한국형 양자내성암호 현황 | https://byline.network/2026/02/26-571/ | 뉴스 | 2026-02 | B |

#### 기업 발언 (E-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-pqc-e-01"></a>pqc-E-01 | Thales/BusinessWire — "Operators can remotely update device protection without replacing cards" | https://www.businesswire.com/news/home/20260301594505/en/ | 공식 보도자료 | 2026-03-01 | A |
| <a id="ref-pqc-e-02"></a>pqc-E-02 | Samsung Semiconductor — S3SSE2A "HW+SW 19.02ms vs SW 335.97ms — 17x improvement" | — | 공식 기술블로그 | 2025-2026 | A |
| <a id="ref-pqc-e-03"></a>pqc-E-03 | Samsung Research — 5G 셀룰러 PQC 전환 전략 | — | 공식 블로그 | 2025 | B |

#### 학술 논문 (P-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-pqc-p-01"></a>pqc-P-01 | Kyber on ESP32 — 듀얼코어+HW가속 1.84x | https://arxiv.org/html/2503.10207v1 | arXiv | 2025-03 | B |
| <a id="ref-pqc-p-02"></a>pqc-P-02 | PQC Authentication for Industrial IoT (Scientific Reports) | https://www.nature.com/articles/s41598-025-28413-8 | 학술지 | 2025 | B |
| <a id="ref-pqc-p-03"></a>pqc-P-03 | PQC for Resource-Constrained Consumer Electronics (Springer) | https://link.springer.com/article/10.1007/s43926-025-00238-x | 학술지 | 2025 | B |
| <a id="ref-pqc-p-04"></a>pqc-P-04 | QORE: Quantum Secure 5G/B5G Core (arXiv) | https://arxiv.org/html/2510.19982v1 | arXiv | 2025-10 | B |
| <a id="ref-pqc-p-05"></a>pqc-P-05 | PQC Support in Cryptographic Libraries Survey (arXiv) | https://arxiv.org/html/2508.16078v1 | arXiv | 2025-08 | B |

#### 특허 (T-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-pqc-t-01"></a>pqc-T-01 | IBM — 격자 기반 양자 알고리즘 특허 191건(2024) | — | 특허 | 2024 | C |
| <a id="ref-pqc-t-02"></a>pqc-T-02 | Samsung — 하드웨어 PQC SE 특허 (미공개) | — | 특허 | 2024-2025 | D |
| <a id="ref-pqc-t-03"></a>pqc-T-03 | Thales — SIM OTA PQC 업그레이드 특허 (미공개) | — | 특허 | 2025-2026 | D |

---

### 스팸피싱감지(통화전)

#### 글로벌 출처 (G-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-sp-g-01"></a>sp-G-01 | Kymatio Blog — Phishing Trends 2026 | https://kymatio.com/blog/phishing-trends-ai-phishing-qrishing-and-voice-attacks | 보안 전문 | 2026 | B |
| <a id="ref-sp-g-02"></a>sp-G-02 | Android Authority — Google Scam Detection Galaxy S26 | https://www.androidauthority.com/google-scam-detection-samsung-galaxy-s26-3643942/ | 기술 미디어 | 2026-02-25 | A |
| <a id="ref-sp-g-03"></a>sp-G-03 | Jetstream Blog — Scam Detection Samsung 확장 | https://jetstream.blog/en/phone-by-google-scam-detection-expands-samsung/ | 기술 미디어 | 2026-02 | B |
| <a id="ref-sp-g-04"></a>sp-G-04 | Android Central — Galaxy S26 Scam Detection 상세 | https://www.androidcentral.com/phones/samsung-galaxy/galaxy-s26-steps-up-its-android-defenses-with-scam-detection-and-this-is-exactly-what-i-needed | 기술 미디어 | 2026-03 | B |
| <a id="ref-sp-g-05"></a>sp-G-05 | Google Security Blog — Android AI Scam Detection | https://security.googleblog.com/2025/03/new-ai-powered-scam-detection-features.html | 기업 공식 | 2025-03 | A |
| <a id="ref-sp-g-06"></a>sp-G-06 | T-Mobile — Scam Shield App | https://www.t-mobile.com/benefits/scam-shield | 이통사 공식 | 운영 중 | A |
| <a id="ref-sp-g-07"></a>sp-G-07 | Trending Topics EU — Syntelligence JV $37.5M | https://www.trendingtopics.eu/syntelligence-5-telecom-giants-launch-ai-joint-venture-to-combat-spam-calls/ | 기술 미디어 | 2025 | B |
| <a id="ref-sp-g-08"></a>sp-G-08 | Market.us — Mobile Phishing Protection $2.67B→$15.99B | https://market.us/report/mobile-phishing-protection-market/ | 시장조사 | 2024-2034 | C |
| <a id="ref-sp-g-09"></a>sp-G-09 | Group-IB Blog — Deepfake Voice Phishing Anatomy | https://www.group-ib.com/blog/voice-deepfake-scams/ | 보안기업 | 2025 | B |
| <a id="ref-sp-g-10"></a>sp-G-10 | MDPI Applied Sciences — KoBERT+CNN-BiLSTM F1=0.994 | https://www.mdpi.com/2076-3417/15/20/11170 | 학술지 | 2025-10-18 | A |
| <a id="ref-sp-g-11"></a>sp-G-11 | arXiv — SpaLLM-Guard / LLM Spam Vulnerability | https://arxiv.org/html/2501.04985v1 | 프리프린트 | 2025-01 | B |
| <a id="ref-sp-g-12"></a>sp-G-12 | ScienceDirect — Vishing Survey & Roadmap | https://www.sciencedirect.com/science/article/pii/S0885230825000270 | 학술지 | 2025 | A |
| <a id="ref-sp-g-13"></a>sp-G-13 | Gearbrain — Apple 스팸 통화 사전 차단 특허 | https://www.gearbrain.com/iphone-spam-call-blocking-2611717625.html | 기술 미디어 | 2017+ | C |
| <a id="ref-sp-g-14"></a>sp-G-14 | Sangoma/FCC — STIR/SHAKEN 2025 규제 강화 | https://sangoma.com/blog/the-new-fcc-stir-shaken-rules-and-why-they-matter-for-your-business-in-2025/ | 규제/기업 | 2025-09 | A |
| <a id="ref-sp-g-15"></a>sp-G-15 | TelecomTV — Syntelligence $37.5M 투자 확인 | https://www.telecomtv.com/content/ai/five-major-telcos-pump-37-5m-into-ai-venture-54939/ | 통신 전문 | 2025 | B |

#### 최신 동향 (N-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-sp-n-01"></a>sp-N-01 | 아시아에이 — SKT 에이닷 전화 보이스피싱 탐지 | https://www.asiaa.co.kr/news/articleView.html?idxno=232111 | 뉴스 | 2025-12 | B |
| <a id="ref-sp-n-02"></a>sp-N-02 | 전자신문 — KT 2025년 1300억 피해 예방 | https://www.etnews.com/20251223000189 | 뉴스 | 2025-12-23 | A |
| <a id="ref-sp-n-03"></a>sp-N-03 | 정책브리핑 — AI로 통화 중 보이스피싱 잡는다 | https://www.korea.kr/news/policyNewsView.do?newsId=148959497 | 정부 | 2026 | A |
| <a id="ref-sp-n-04"></a>sp-N-04 | 전자신문 — 과기정통부 공동대응 플랫폼 2026-2027 | https://www.etnews.com/20260212000065 | 뉴스 | 2026-02-12 | A |
| <a id="ref-sp-n-05"></a>sp-N-05 | The Mobile Network — Syntelligence→GTAA 리브랜딩 | https://the-mobile-network.com/2026/02/syntelligence-ai-is-the-global-telco-ai-alliance-now/ | 통신 전문 | 2026-02 | B |
| <a id="ref-sp-n-06"></a>sp-N-06 | 이지이코노미 — LGU+ 악성 서버 추적 3만명 보호 | https://www.ezyeconomy.com/news/articleView.html?idxno=231337 | 뉴스 | 2026 | B |

#### 기업 발언 (E-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-sp-e-01"></a>sp-E-01 | SKT 뉴스룸 — "통화 데이터가 서버를 거치지 않고... 안전한 탐지" | — | 공식 보도 | 2025-12-01 | A |
| <a id="ref-sp-e-02"></a>sp-E-02 | KT/전자신문 — "1,300억 피해 예방, 정확도 90.3%→93%+" | — | 공식 보도 | 2025-12-23 | A |
| <a id="ref-sp-e-03"></a>sp-E-03 | 경향신문 — "국내 최초 3중 보이스피싱 예방 체계" | — | 언론 | 2025-07-29 | B |
| <a id="ref-sp-e-04"></a>sp-E-04 | LGU+ 뉴스룸 — "악성 서버 800개 추적, 3.3만명 보호, 1.8조 예방" | — | 공식 보도 | 2026-02~03 | A |
| <a id="ref-sp-e-05"></a>sp-E-05 | LGU+ 뉴스룸 — "스팸 위험도 수치화, 안티딥보이스" | — | 공식 보도 | 2025 | B |
| <a id="ref-sp-e-06"></a>sp-E-06 | Google/Android Authority — "Gemini Nano monitors calls for speech patterns" | — | 기업 공식 | 2026-02-25 | A |
| <a id="ref-sp-e-07"></a>sp-E-07 | 전자신문/정책브리핑 — "공동대응 플랫폼 2026~2027 구축" | — | 정부 | 2026-02 | A |

#### 학술 논문 (P-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-sp-p-01"></a>sp-P-01 | Multimodal Voice Phishing (MDPI) — F1=0.994 | https://www.mdpi.com/2076-3417/15/20/11170 | 학술지 | 2025-10-18 | A |
| <a id="ref-sp-p-02"></a>sp-P-02 | RAG-Based LLM Fraud Detection — 정확도 97.98% | https://arxiv.org/html/2501.15290v1 | arXiv | 2025-01 | B |
| <a id="ref-sp-p-03"></a>sp-P-03 | SpaLLM-Guard — Mixtral 98.61% | https://arxiv.org/html/2501.04985v1 | arXiv | 2025-01 | B |
| <a id="ref-sp-p-04"></a>sp-P-04 | LLM Spam Detection Vulnerability | https://arxiv.org/abs/2504.09776 | arXiv | 2025-04 | B |
| <a id="ref-sp-p-05"></a>sp-P-05 | Vishing Survey & Roadmap (ScienceDirect) | https://www.sciencedirect.com/science/article/pii/S0885230825000270 | 학술지 | 2025 | A |
| <a id="ref-sp-p-06"></a>sp-P-06 | Early-stage Voice Phishing Detection | https://www.sciencedirect.com/science/article/abs/pii/S0167404825000537 | 학술지 | 2025 | B |

#### 특허 (T-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-sp-t-01"></a>sp-T-01 | Apple — Detection of Spoofed Call Information (2017+) | — | 특허 | 2017+ | C |

---

### OnDevice sLM

#### 글로벌 출처 (G-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-slm-g-01"></a>slm-G-01 | Google Developers Blog — Gemma 3n preview | https://developers.googleblog.com/en/introducing-gemma-3n/ | 기업 공식 | 2025-05-20 | A |
| <a id="ref-slm-g-02"></a>slm-G-02 | MarketsandMarkets — SLM Market $5.45B by 2032 | https://www.marketsandmarkets.com/PressReleases/small-language-model.asp | 시장조사 | 2024 | C |
| <a id="ref-slm-g-03"></a>slm-G-03 | Edge AI Vision Alliance — On-Device LLMs 2026 | https://www.edge-ai-vision.com/2026/01/on-device-llms-in-2026-what-changed-what-matters-whats-next/ | 기술매체 | 2026-01 | B |
| <a id="ref-slm-g-04"></a>slm-G-04 | Microsoft Azure Blog — Phi-4 mini edge | https://azure.microsoft.com/en-us/blog/empowering-innovation-the-next-generation-of-the-phi-family/ | 기업 공식 | 2025 | A |
| <a id="ref-slm-g-05"></a>slm-G-05 | Apple ML Research — Foundation Language Models 2025 | https://machinelearning.apple.com/research/apple-foundation-models-2025-updates | 기업 공식 | 2025 | A |
| <a id="ref-slm-g-06"></a>slm-G-06 | Android Central — Snapdragon 8 Elite Gen 5 | https://www.androidcentral.com/phones/samsung-galaxy/snapdragon-8-elite-gen-5-hands-the-galaxy-s26-the-ai-upgrade-weve-been-waiting-for | 기술매체 | 2025-12 | B |
| <a id="ref-slm-g-07"></a>slm-G-07 | mashdigi — MediaTek Dimensity 9500 MWC 2026 | https://en.mashdigi.com/from-6g-network-connectivity-to-next-generation-data-centers-mediatek-showcases-its-ai-capabilities-at-mwc-2026-with-the-dimensity-9500-enabling-multi-modal-applications-on-devices/ | 기술매체 | 2026-03 | B |
| <a id="ref-slm-g-08"></a>slm-G-08 | Samsung Newsroom — Galaxy AI MWC 2026 | https://news.samsung.com/global/samsung-advances-galaxy-ai-and-its-connected-ecosystem-at-mwc-2026 | 기업 공식 | 2026-03 | A |
| <a id="ref-slm-g-09"></a>slm-G-09 | Gartner/GreyB — Edge AI HW Evaluation 2025 | https://www.businesswire.com/news/home/20250910279522/en/Edge-AI-Hardware-Company-Evaluation-Report-2025-Qualcomm-Apple-and-Huawei-Lead-with-Advanced-Processors-Strategic-Collaborations-and-Expanding-AI-Capabilities---ResearchAndMarkets.com | 리서치 | 2025 | B |
| <a id="ref-slm-g-10"></a>slm-G-10 | Meta AI Research — On-Device LLMs State of Union 2026 | https://v-chandra.github.io/on-device-llms/ | 기술 리포트 | 2026 | B |
| <a id="ref-slm-g-11"></a>slm-G-11 | Arm Newsroom — ExecuTorch 1.0 GA Release | https://newsroom.arm.com/news/executorch-1-0-ga-release-edge-ai | 기업 공식 | 2025-10 | A |
| <a id="ref-slm-g-12"></a>slm-G-12 | ScienceDirect/ACM — Edge LLM Inference Optimization | https://www.sciencedirect.com/science/article/abs/pii/S1574013725000310 | 학술 | 2025-2026 | A |
| <a id="ref-slm-g-13"></a>slm-G-13 | GitHub — Alibaba MNN | https://github.com/alibaba/MNN | 오픈소스 | 2025 | B |

#### 최신 동향 (N-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-slm-n-01"></a>slm-N-01 | Engadget — Everything at MWC 2026 | https://www.engadget.com/mobile/everything-announced-at-mwc-2026-lenovos-wild-foldable-gaming-handheld-honors-robot-phone-and-more-172442814.html | 기술 미디어 | 2026-03 | B |
| <a id="ref-slm-n-02"></a>slm-N-02 | Android Central — OPPO MediaTek Omni MWC | https://www.androidcentral.com/phones/oppo-phones/oppo-mediatek-let-omni-take-the-mwc-2026-stage-as-the-gateway-to-ai-and-the-physical-world | 기술 미디어 | 2026-03 | B |
| <a id="ref-slm-n-03"></a>slm-N-03 | MediaTek Press Room — AI at MWC 2026 | https://www.mediatek.com/press-room/mediatek-exemplifies-ai-and-connectivity-leadership-at-mwc-2026 | 기업 공식 | 2026-03 | A |
| <a id="ref-slm-n-04"></a>slm-N-04 | Qualcomm Newsroom — Snapdragon Wear Elite | https://www.qualcomm.com/news/releases/2026/03/qualcomm-powers-the-rise-of-personal-ai-with-new-snapdragon-wear | 기업 공식 | 2026-03 | A |
| <a id="ref-slm-n-05"></a>slm-N-05 | Telecom Reseller — AGI Inc. Agentic on Snapdragon | https://telecomreseller.com/2026/03/03/agi-inc-enables-new-agentic-capabilities-for-devices-powered-by-snapdragon/ | 통신 전문 | 2026-03 | B |
| <a id="ref-slm-n-06"></a>slm-N-06 | Futurum Group — Qualcomm CES 2026 on-device AI | https://futurumgroup.com/insights/qualcomm-unveils-future-of-intelligence-at-ces-2026-pushes-the-boundaries-of-on-device-ai/ | 기술 미디어 | 2026-01 | B |
| <a id="ref-slm-n-07"></a>slm-N-07 | HuggingFace Blog — Gemma 3n open-source | https://huggingface.co/blog/gemma3n | 오픈소스 | 2025 | A |

#### 기업 발언 (E-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-slm-e-01"></a>slm-E-01 | Google — "powerful multimodal capabilities to edge devices" | — | 기업 공식 | 2025-05-20 | A |
| <a id="ref-slm-e-02"></a>slm-E-02 | Qualcomm — "Hexagon NPU ~37% faster, 100 TOPS" | — | 기업 공식 | 2026-01 | A |
| <a id="ref-slm-e-03"></a>slm-E-03 | Qualcomm — "Snapdragon Wear Elite: 5x CPU, 7x GPU, dual NPU" | — | 기업 공식 | 2026-03-02 | A |
| <a id="ref-slm-e-04"></a>slm-E-04 | MediaTek — "NPU 990 runs Omni in real-time, offline" | — | 기업 공식 | 2026-03 | A |
| <a id="ref-slm-e-05"></a>slm-E-05 | Samsung — "Galaxy S26: most powerful + intuitive Galaxy AI" | — | 기업 공식 | 2026-02 | A |
| <a id="ref-slm-e-06"></a>slm-E-06 | Apple — "Foundation Models: ~3B on-device, data never leaves device" | — | 기업 공식 | 2025-09 | A |
| <a id="ref-slm-e-07"></a>slm-E-07 | Meta — "ExecuTorch: billions of users, 50KB runtime" | — | 기업 공식 | 2025-07 | A |

#### 학술 논문 (P-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-slm-p-01"></a>slm-P-01 | Efficient Inference for Edge LLMs: Survey (Tsinghua Sci.Tech.) | https://www.sciopen.com/article/10.26599/TST.2025.9010166 | 학술지 | 2026 | A |
| <a id="ref-slm-p-02"></a>slm-P-02 | Sustainable LLM Inference for Edge AI (ACM ToIT) | https://dl.acm.org/doi/10.1145/3767742 | 학술지 | 2026 | A |
| <a id="ref-slm-p-03"></a>slm-P-03 | Tiny ML and On-Device Inference Survey (PMC) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12115890/ | 학술지 | 2026 | B |
| <a id="ref-slm-p-04"></a>slm-P-04 | MO-BIEDIT: Resource-Efficient (ICLR 2026) | https://openreview.net/pdf?id=fb7yTBOV3p | 학술 컨퍼런스 | 2026 | B |
| <a id="ref-slm-p-05"></a>slm-P-05 | I-LLM: Integer-Only Inference for Low-Bit LLMs | https://openreview.net/forum?id=44pbCtAdLx | 프리프린트 | 2025 | B |
| <a id="ref-slm-p-06"></a>slm-P-06 | Apple Intelligence Foundation Language Models (arXiv) | https://arxiv.org/abs/2507.13575 | arXiv | 2025 | B |
| <a id="ref-slm-p-07"></a>slm-P-07 | Edge-First Language Model Inference (arXiv) | https://arxiv.org/html/2505.16508v1 | arXiv | 2025 | B |

#### 특허 (T-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-slm-t-01"></a>slm-T-01 | Qualcomm — US 10,968,477 B2 On-device edge inference | — | 특허 | — | C |
| <a id="ref-slm-t-02"></a>slm-T-02 | Apple — KV-cache sharing for on-device models | — | 특허 | — | D |

---

### OnDevice 동형암호 (HE)

#### 글로벌 출처 (G-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-he-g-01"></a>he-G-01 | HomomorphicEncryption.org — 9th Standards Meeting Seoul | https://homomorphicencryption.org/9th-homomorphicencryption-org-standards-meeting/ | 표준화 기관 | 2026.3 | A |
| <a id="ref-he-g-02"></a>he-G-02 | FHE.org Digest #38 | https://fheorg.substack.com/p/fheorg-digest-38-fheorg-2026-conference | 커뮤니티 | 2026.3 | B |
| <a id="ref-he-g-03"></a>he-G-03 | FHE.org 2026 Conference Taipei | https://fhe.org/conferences/conference-2026/ | 학술 커뮤니티 | 2026.3 | A |
| <a id="ref-he-g-04"></a>he-G-04 | tech.eu — Zama $57M Series B, First FHE Unicorn | https://tech.eu/2025/06/25/zama-becomes-1st-i-fhe-unicorn-with-57m-raise-led-by-pantera-and-blockchange/ | 언론 | 2025.6 | B |
| <a id="ref-he-g-05"></a>he-G-05 | Apple ML Research — HE in Apple Ecosystem | https://machinelearning.apple.com/research/homomorphic-encryption | 기업 공식 | 2024.8 | A |
| <a id="ref-he-g-06"></a>he-G-06 | The Quantum Insider — Niobium $23M+ FHE Funding | https://thequantuminsider.com/2025/12/03/niobium-23m-fhe-funding/ | 전문 미디어 | 2025.12 | B |
| <a id="ref-he-g-07"></a>he-G-07 | GitHub — OpenFHE 1.5.0 development release | https://github.com/openfheorg/openfhe-development | 오픈소스 | 2026.2.26 | A |
| <a id="ref-he-g-08"></a>he-G-08 | NIST CSRC — FHE Privacy-Enhancing Cryptography | https://csrc.nist.gov/projects/pec/fhe | 정부기관 | 2025 | A |
| <a id="ref-he-g-09"></a>he-G-09 | NIST CSRC — MPTS 2026 Workshop | https://csrc.nist.gov/events/2026/mpts2026 | 정부기관 | 2026 | A |
| <a id="ref-he-g-10"></a>he-G-10 | InsideHPC/DARPA — Intel DPRIVE FHE ASIC | https://insidehpc.com/2021/03/intel-developing-asic-accelerator-for-darpa-holy-grail-cybersecurity-project/ | 산업 미디어 | 2021- | B |
| <a id="ref-he-g-11"></a>he-G-11 | Duality Technologies — HW Acceleration of FHE | https://dualitytech.com/blog/hardware-acceleration-of-fully-homomorphic-encryption-making-privacy-preserving-machine-learning-practical/ | 기업 블로그 | 2025.11 | B |
| <a id="ref-he-g-12"></a>he-G-12 | Market Research Future — HE Market Forecast | https://www.marketresearchfuture.com/reports/homomorphic-encryption-market-1144 | 시장조사 | 2025 | C |
| <a id="ref-he-g-13"></a>he-G-13 | ScienceDirect — HE for ML with CKKS: Survey | https://www.sciencedirect.com/org/science/article/pii/S1546221825007702 | 학술 저널 | 2025 | A |
| <a id="ref-he-g-14"></a>he-G-14 | IEEE Spectrum — Homomorphic Encryption LLM | https://spectrum.ieee.org/homomorphic-encryption-llm | 기술 미디어 | 2025 | B |
| <a id="ref-he-g-15"></a>he-G-15 | Nature Sci. Reports — Quantum Resilient Framework Apple MM1 | https://www.nature.com/articles/s41598-025-22056-5 | 학술 저널 | 2025 | A |

#### 최신 동향 (N-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-he-n-01"></a>he-N-01 | PR Newswire/TQI — Niobium $23M+ Oversubscribed | https://thequantuminsider.com/2025/12/03/niobium-23m-fhe-funding/ | 뉴스 | 2025.12.3 | B |
| <a id="ref-he-n-02"></a>he-N-02 | Evertiq — SEMIFIVE-Niobium FHE Accelerator | https://evertiq.com/design/2026-02-20-semifive-secures-design-win-with-niobium-for-fhe-accelerator | 뉴스 | 2026.2.19 | B |
| <a id="ref-he-n-03"></a>he-N-03 | Korea IT Times — LGU+ ixi-Guardian 2.0 MWC 2026 | https://www.koreaittimes.com/news/articleView.html?idxno=151339 | 뉴스 | 2026.3 | B |
| <a id="ref-he-n-04"></a>he-N-04 | Dailian — LGU+ 보안 기술 4종 MWC 2026 | https://dailian.co.kr/news/view/1614870/ | 뉴스 | 2026.3 | B |
| <a id="ref-he-n-05"></a>he-N-05 | QuantumZeitgeist — Cerium Multi-GPU FHE | https://quantumzeitgeist.com/gpu-multi-framework-enables-encrypted-large-model-inference-addressing/ | 뉴스 | 2025.12 | B |
| <a id="ref-he-n-06"></a>he-N-06 | SemiEngineering — FHECore GPU 논문 해설 | https://semiengineering.com/a-gpu-microarchitecture-optimized-for-fully-homomorphic-encryption/ | 기술 미디어 | 2026.2 | B |

#### 기업 발언 (E-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-he-e-01"></a>he-E-01 | LGU+/Dailian — "동형암호는 암호화 상태에서 데이터 저장·연산" | — | MWC 발표 | 2026.3 | A |
| <a id="ref-he-e-02"></a>he-E-02 | BusinessKorea — "LGU+ ixi-O + Physical AI + HE" | — | 기업 뉴스 | 2026.3 | B |
| <a id="ref-he-e-03"></a>he-E-03 | SEMIFIVE PR — "strategic milestone for US market expansion" (~$6.86M) | — | 공식 보도 | 2026.2.19 | A |
| <a id="ref-he-e-04"></a>he-E-04 | Korea Herald/Korea IT Times — "LGU+ MWC 2026 ixi-Guardian 2.0" | — | 언론 | 2026.3 | B |
| <a id="ref-he-e-05"></a>he-E-05 | Intel Community Blog — "DPRIVE FHE standardization" | — | 기업 블로그 | 2024.2 | B |

#### 학술 논문 (P-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-he-p-01"></a>he-P-01 | FHECore: GPU Microarchitecture for FHE (arXiv) | https://arxiv.org/abs/2602.22229 | arXiv | 2026.2 | B |
| <a id="ref-he-p-02"></a>he-P-02 | Cerium: Multi-GPU Encrypted LLM Inference (arXiv) | https://arxiv.org/abs/2512.11269 | arXiv | 2025.12 | B |
| <a id="ref-he-p-03"></a>he-P-03 | HHEML: Hybrid HE for ML on Edge (arXiv) | https://arxiv.org/abs/2510.20243 | arXiv | 2025.10 | B |
| <a id="ref-he-p-04"></a>he-P-04 | Low Communication ThFHE (KDDI/도쿄대, IACR) | https://eprint.iacr.org/2025/409 | ePrint | 2025 | B |
| <a id="ref-he-p-05"></a>he-P-05 | FHE-Agent: CKKS Auto Configuration (arXiv) | https://arxiv.org/abs/2511.18653 | arXiv | 2025.11 | B |
| <a id="ref-he-p-06"></a>he-P-06 | CAT: GPU-Accelerated FHE Framework (arXiv) | https://arxiv.org/abs/2503.22227 | arXiv | 2025.3 | B |
| <a id="ref-he-p-07"></a>he-P-07 | Efficient Keyset Design for NN using HE (PMC) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12298995/ | 학술지 | 2025 | B |

#### 특허 (T-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-he-t-01"></a>he-T-01 | IBM (Craig Gentry) — US9083526B2 FHE 원천 | — | 특허 | 2015 | A |
| <a id="ref-he-t-02"></a>he-T-02 | 2025-2026 신규 출원 — SerpAPI 한도로 수집 불가 | — | — | — | — |

---

### Secure Vector Search

#### 글로벌 출처 (G-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-sv-g-01"></a>sv-G-01 | arXiv — ppRAG: Privacy-Preserving RAG with DCPE | https://arxiv.org/abs/2601.12331 | 프리프린트 | 2026-01 | B |
| <a id="ref-sv-g-02"></a>sv-G-02 | Microsoft Research — SEAL HE Library | https://github.com/microsoft/SEAL | 기업 연구소 | 상시 | A |
| <a id="ref-sv-g-03"></a>sv-G-03 | Zama — Concrete ML, $57M Series B, Unicorn | https://www.zama.org/ | 스타트업 | 2025-06 | A |
| <a id="ref-sv-g-04"></a>sv-G-04 | IronCore Labs — Cloaked AI, Gartner Cool Vendor 2025 | https://ironcorelabs.com/products/cloaked-ai/ | 기업 보도 | 2025-07 | B |
| <a id="ref-sv-g-05"></a>sv-G-05 | Microsoft Learn — Azure Confidential AI | https://learn.microsoft.com/en-us/azure/confidential-computing/confidential-ai | 공식 기술문서 | 2024-2025 | A |
| <a id="ref-sv-g-06"></a>sv-G-06 | Google Blog — Private AI Compute | https://blog.google/innovation-and-ai/products/google-private-ai-compute/ | 기업 공식 | 2025-11 | A |
| <a id="ref-sv-g-07"></a>sv-G-07 | rahulkolekar.com — Pinecone BYOC 2026, Weaviate HIPAA 비교 | https://rahulkolekar.com/vector-db-pricing-comparison-pinecone-weaviate-2026/ | 기술 블로그 | 2026-02 | C |
| <a id="ref-sv-g-08"></a>sv-G-08 | Security Boulevard — HIPAA 암호화 의무화 추진 | https://securityboulevard.com/2026/02/10-encrypted-email-solutions-for-healthcare-providers-in-2026/ | 보안 미디어 | 2026-02 | B |
| <a id="ref-sv-g-09"></a>sv-G-09 | Medium — Embedding Inversion 92% 원본 재구성 | https://medium.com/@himansusaha/embedding-inversion-encrypted-vector-db-the-future-of-privacy-aware-rag-e0caf0985ee1 | 기술 블로그 | 2025-12 | C |
| <a id="ref-sv-g-10"></a>sv-G-10 | Cisco Security — Securing Vector Databases | https://sec.cloudapps.cisco.com/security/center/resources/securing-vector-databases | 기업 보안 | 상시 | B |
| <a id="ref-sv-g-11"></a>sv-G-11 | IACR ePrint — Compass: Encrypted Semantic Search | https://eprint.iacr.org/2024/1255 | 암호학 프리프린트 | 2024-08 | A |
| <a id="ref-sv-g-12"></a>sv-G-12 | arXiv — PP-ANNS: Privacy-Preserving ANN | https://arxiv.org/pdf/2508.10373 | 프리프린트 | 2025-08 | A |

#### 최신 동향 (N-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-sv-n-01"></a>sv-N-01 | SitePoint — Browser-Based Privacy-Preserving RAG | https://www.sitepoint.com/browser-based-rag-private-docs/ | 기술 블로그 | 2025 | C |
| <a id="ref-sv-n-02"></a>sv-N-02 | NSF PAR — D-RAG: Decentralized RAG with Blockchain | https://par.nsf.gov/biblio/10578004-rag-privacy-preserving-framework-decentralized-rag-using-blockchain | 연구 자금 | 2024 | B |
| <a id="ref-sv-n-03"></a>sv-N-03 | MEXC Blog — Zama FHE $1B Unicorn | https://blog.mexc.com/news/what-is-zama-fhe-the-1b-unicorn-bringing-private-smart-contracts-to-ethereum-and-shibarium-2026/ | 블록체인 미디어 | 2026 | C |
| <a id="ref-sv-n-04"></a>sv-N-04 | Hacker News — Google Private AI Compute Launch | https://thehackernews.com/2025/11/google-launches-private-ai-compute.html | 보안 뉴스 | 2025-11 | B |
| <a id="ref-sv-n-05"></a>sv-N-05 | LessWrong — Private AI Clouds are Future of Inference | https://www.lesswrong.com/posts/dEGEC9bDwE4mHfdbF/private-ai-clouds-are-the-future-of-inference | 커뮤니티 | 2025 | C |

#### 기업 발언 (E-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-sv-e-01"></a>sv-E-01 | IronCore Labs — "train models using encrypted data" | — | 기업 보도 | 2025-07 | B |
| <a id="ref-sv-e-02"></a>sv-E-02 | Microsoft — "encrypted prompts decrypted only within TEEs" | — | 공식 기술문서 | 2024-2025 | A |
| <a id="ref-sv-e-03"></a>sv-E-03 | Google — "privacy of on-device AI to the cloud" | — | 기업 공식 | 2025-11 | A |
| <a id="ref-sv-e-04"></a>sv-E-04 | Pinecone — "zero-access operating model" | — | 기업 발표 | 2026-02 | B |
| <a id="ref-sv-e-05"></a>sv-E-05 | Gartner — "Cool Vendors in Data Security 2025" | — | 리서치 | 2025 | A |

#### 학술 논문 (P-xx)

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-sv-p-01"></a>sv-P-01 | Compass: Encrypted Semantic Search (OSDI'25) | https://eprint.iacr.org/2024/1255 | 학술 컨퍼런스 | 2025 | A |
| <a id="ref-sv-p-02"></a>sv-P-02 | PP-ANNS: Privacy-Preserving ANN (ICDE'25) | https://arxiv.org/pdf/2508.10373 | 학술 컨퍼런스 | 2025 | A |
| <a id="ref-sv-p-03"></a>sv-P-03 | FRAG: Federated Vector DB for RAG (arXiv) | https://arxiv.org/abs/2410.13272 | arXiv | 2024 | B |
| <a id="ref-sv-p-04"></a>sv-P-04 | PANTHER: Private ANN Search (CCS'25) | https://dl.acm.org/doi/10.1145/3719027.3765190 | 학술 컨퍼런스 | 2025 | A |
| <a id="ref-sv-p-05"></a>sv-P-05 | ppRAG: Privacy-Preserving RAG with DCPE (arXiv) | https://arxiv.org/abs/2601.12331 | arXiv | 2026-01 | B |
