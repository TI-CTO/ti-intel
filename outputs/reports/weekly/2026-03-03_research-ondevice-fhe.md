---
topic: OnDevice 동형암호 (Homomorphic Encryption on Device)
date: 2026-03-03
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
domain: Secure AI (LG U+ tech strategy)
tier: 2 (deep research)
---

# Research Report: OnDevice 동형암호 (Homomorphic Encryption on Device)

## Executive Summary (경영진 요약)

> 2025~2026년 초는 동형암호(FHE)의 연구-상용화 전환점이다. GPU 마이크로아키텍처 최적화(FHECore, 2.41x 명령어 감소), 멀티-GPU LLM 암호화 추론 프레임워크(Cerium: Llama3-8B를 134초에 처리), 그리고 DESILO+Cornami의 배포 가능한 FHE-LLM 출시(행렬 연산 80x 가속)가 상용화 임계점 진입을 가리킨다. 국내에서는 LG유플러스가 CryptoLab과 협업해 MWC 2026에서 익시오(ixi-O) 동형암호 적용 계획을 발표했고, 제9회 HomomorphicEncryption.org 표준화 회의가 서울 LG사이언스파크에서 개최(2026.3.5-6)됨으로써 한국이 글로벌 표준화의 중심지로 부상하고 있다. 온디바이스 순수 FHE는 아직 연구 단계이나, 하이브리드 HE(클라이언트 경량 암호화+서버 FHE 연산) 방식으로 에지 디바이스 적용 가능성이 열리고 있다. 신뢰도: 하드웨어 성능 수치 [A/B], 시장 규모 전망 [C] (보고사마다 큰 편차).

---

## 연구 질문

> OnDevice 동형암호 기술의 현재 기술 성숙도(TRL), 주요 플레이어 동향, 상용화 경로, 그리고 통신 산업(특히 LG U+)에서의 적용 가능성은 어떠한가?

---

## 1. 기술 현황

### 1.1 전반적 TRL 평가

| 적용 영역 | TRL | 비고 |
|----------|-----|------|
| 서버사이드 FHE (클라우드 AI) | TRL 7-8 | Cornami+DESILO 배포 가능 LLM 출시 (2025.9) |
| GPU 가속 FHE | TRL 6-7 | Cerium 프레임워크, BERT-Base 8초 (2025.12) |
| ASIC/칩 FHE 가속기 | TRL 4-6 | DARPA DPRIVE Phase 2, Niobium ASIC 개발 중 |
| 에지/하이브리드 HE | TRL 5-6 | HHEML FPGA 50x 지연 감소 (2025.10) |
| **순수 온디바이스 FHE** | **TRL 3-4** | **연구 단계, 스마트폰 직접 실행 미검증** |

### 1.2 핵심 기술 요소

**FHE 스킴 비교:**
- **CKKS**: 실수 근사 연산, AI/ML 추론에 최적. 가장 활발히 연구됨
- **TFHE**: 비트 연산, 부트스트래핑 빠름, 에지 디바이스 로직 연산에 유리
- **BGV/BFV**: 정수 연산, Microsoft SEAL이 BFV 지원

**연산 오버헤드 현황 (2025-2026 기준):**
- CPU 기준: 암호화되지 않은 연산 대비 수천~수만 배 오버헤드
- GPU 가속: CPU 대비 200x 이상 개선 (EncryptedLLM 2026) [G-02]
- ASIC: GPU 대비 에너지 효율 10x 목표 (DARPA DPRIVE) [G-17]
- 최신 멀티-GPU: Llama3-8B 암호화 추론 134초 (Cerium, 2025.12) [G-10]

**핵심 병목 해소 기술:**
- **Number Theoretic Transform (NTT)**: FHE 연산의 90% 이상 차지, GPU/ASIC 가속의 주 타겟
- **부트스트래핑(Bootstrapping)**: CKKS의 핵심 병목 — FHECore 50% 감소 [G-01]
- **행렬 연산(Matrix Multiplication)**: LLM 연산의 90% 이상 — DESILO+Cornami PCMM 기법으로 80x 가속 [E-01]
- **Softmax/GeLU 근사**: Transformer 비선형 함수를 다항식으로 근사 (ELLMo, Powerformer 등) [G-13]

---

## 2. 시장 동향

### 2.1 시장 규모

시장조사 기관마다 편차가 크며 [C] 수준으로 인용:

| 조사기관 | 2025/2026 규모 | 목표연도 규모 | CAGR |
|---------|--------------|------------|------|
| Industry Research Co. | USD 1.2B (2026) | USD 8.4B (2033) | 30%+ |
| Verified Market Reports | — | USD 29B (2032) | 31.8% |
| Market Research Future | USD 234M (2025) | USD 526M (2035) | 8.4% |
| Global Growth Insights | — | USD 8.4B (IT/통신 특화, 2031) | 30% |

> 주의: 시장 정의(부분 vs. 완전 동형암호, 응용 범위)에 따라 수치 편차 큼. ≥2개 독립 출처 교차 확인 필요.

### 2.2 주요 성장 드라이버

- **AI 프라이버시 규제 강화**: GDPR, 한국 개인정보보호법 강화 → 암호화 상태 처리 수요 증가
- **의료·금융 데이터 협업**: 복호화 없이 분석 가능한 FHE의 핵심 가치
- **생성형 AI 보안 우려**: LLM 서비스에서 사용자 쿼리 유출 방지 수요
- **양자내성암호(PQC)와 융합**: FHE는 본질적으로 격자 기반 → 포스트-퀀텀 보안 내포

---

## 3. 경쟁사 동향

### 3.1 한국 기업

**CryptoLab (크립토랩)**
- 세계 최초 4세대 FHE 스킴 CKKS 원천특허 보유 (천정희 서울대 교수 창업)
- 핵심 제품: **HEaaN Library** — 세계 최고 속도의 CKKS 구현체 [G-05]
- 최신 동향: LG유플러스와 협업, MWC 2026에서 익시오(ixi-O) 동형암호 적용 발표 [E-03]
- **Samsung Electronics**: HEaaN Library를 활용한 Smart SSD용 동형암호 하드웨어 개발 중 [G-05]
- **Macrogen 계약 (2024)**: 유전체 데이터 분석을 위한 3년 공급 계약 체결 [E-05]
- **IBM HElayers 탑재**: IBM AI 분석 소프트웨어에 HEaaN 탑재 확인 [E-06]
- **Niobium 파트너십 (2024.10)**: HEaaN CKKS 소프트웨어 + Niobium FHE ASIC 결합, 암호화 AI 추론 상용화 목표 [E-07]

**DESILO (디사일로)**
- Python 기반 FHE 라이브러리 **Liberate.FHE** 독자 개발
- 2021년 네이버·KB투자·하나은행 참여 Series A 60억원 유치 [G-09]
- **Cornami와 전략적 협업** (가장 중요한 최근 동향):
  - 2025.9: 배포 가능한 FHE 기반 LLM 출시 (AI Infra Summit 2025) [E-01]
  - 2025.11: Craig Gentry(FHE의 아버지)와 공동 연구 발표 — 행렬 연산 80x 가속 논문 발표 [E-01, G-11]
- 핵심 기술: **PCMM(Plaintext-Ciphertext Matrix Multiplication)** — LLM 연산 90% 이상을 최소 오버헤드로 처리

### 3.2 글로벌 기업

**Cornami (미국)**
- 재구성 가능한 Many-Core Compute Fabric 기반 FHE 가속기 개발
- DESILO와 협업, HARVEST Platform (의료 데이터 협업) 2025.12 출시 예정 발표 [E-01]
- DARPA DPRIVE 프로그램 비참여, 독자 기술 경로

**Zama (프랑스)**
- 2025.6: **Series B $57M 유치**, FHE 공간 최초 유니콘 달성 ($1B 밸류에이션) [G-08]
- 총 누적 투자 $150M+
- 주력 방향: FHE를 활용한 블록체인 스마트 컨트랙트 (Confidential Blockchain Protocol)
- TFHE 스킴 특화, 오픈소스 라이브러리 Concrete 유지

**Niobium (미국, 오하이오)**
- 2025.12: **$23M+ 후속 투자 유치** (누적 $28M+) [G-07]
- 투자자: Fusion Fund, Morgan Creek Capital, Analog Devices Ventures (ADVentures), Korea Development Bank (KDB), Blockchange Ventures 등
- 목표: 2세대 FHE ASIC 칩 개발, prototype → 생산용 silicon 전환

**Duality Technologies (미국)**
- OpenFHE 오픈소스 라이브러리 기여자
- 2025.11: Google Cloud Confidential Computing 포트폴리오 지원 발표 (NVIDIA GPU confidential VM) [G-16]
- DARPA DPRIVE Phase II 선정 (Phase I $14.5M 계약)
- LG Technology Ventures로부터 투자 유치 이력

**Intel (미국)**
- Intel HE Toolkit, Intel AVX-512 최적화 HE Acceleration Library 운영
- DARPA DPRIVE 참여 (Phase I 완료)
- 목표: CPU 대비 5 오더 오브 매그니튜드 성능 개선 ASIC [G-17]
- 2025 FHE.org Hardware Day 패널 참여 (Rosario Cammarota)

**Microsoft (미국)**
- **Microsoft SEAL**: BFV/CKKS 지원 오픈소스 라이브러리, 2025 벤치마크에서 CKKS 암호화 최고 속도 기록 [G-21]
- 기업용 암호화 컴퓨팅 플랫폼 통합 제공

**Apple (미국)**
- 2024.7: **Swift Homomorphic Encryption** 오픈소스 패키지 공개 (Apache 2.0) [G-22]
- iOS 18 Live Caller ID Lookup 기능에 BFV 동형암호 적용 — 스마트폰 최초 실사용 사례
- Enhanced Visual Search 등 온디바이스 프라이버시 보호에 적용

---

## 4. 제품/서비스 스펙 비교

| 기업 | 주요 제품 | 핵심 스킴 | 성능 지표 | 적용 사례 | 발표시점 | 출처 |
|------|---------|---------|----------|---------|---------|------|
| CryptoLab | HEaaN Library | CKKS (4세대) | 세계 최고 속도 (자체 주장) | 유전체 분석, LG유플러스, IBM | 계속 업데이트 | [G-05, E-05] |
| DESILO | Liberate.FHE | CKKS | 행렬 연산 80x (PCMM) | FHE-LLM 배포 | 2025.9~11 | [E-01] |
| Cornami | Compute Fabric | 다중 | 공개 정보 없음 (칩 명칭 미공개) | DESILO 협업 LLM | 2025.9 | [E-01] |
| Niobium | FHE ASIC (2세대) | CKKS | 공개 정보 없음 (개발 중) | CryptoLab 협업 | 2025.12 | [G-07] |
| Zama | Concrete Library | TFHE | 공개 정보 없음 | 블록체인 스마트 컨트랙트 | 2025.6 | [G-08] |
| Apple | Swift HE | BFV | Caller ID Lookup 실시간 | iOS 18 (Live Caller ID) | 2024.7 | [G-22] |
| Microsoft | SEAL | BFV, CKKS | CKKS 암호화 최고 속도 | 클라우드/연구 | 지속 | [G-21] |
| Intel | HE Toolkit + ASIC | 다중 | 목표: 5 OoM 개선 | 클라우드 엔터프라이즈 | 계속 | [G-17] |

---

## 5. 학술 동향

### 5.1 2025-2026 핵심 논문 (시계열 정렬)

**[2025년]**

1. **"Leveraging ASIC AI Chips for Homomorphic Encryption" (CROSS)**
   - 저자: Jianming Tong et al. (Georgia Tech, MIT, Google, Cornell)
   - arXiv:2501.07047 (2025.1)
   - 핵심: TPU 등 AI ASIC을 FHE 가속에 재활용하는 CROSS 컴파일러 프레임워크
   - TPUv4 기준 CPU 대비 161x, GPU(V100) 대비 5x 속도 개선 [P-01]

2. **"MetaKernel: Enabling Efficient Encrypted Neural Network Inference through Unified MVM and Convolution"**
   - ACM Programming Languages 게재 (2025)
   - 핵심: MVM과 Conv 연산을 통합 최적화하는 FHE 컴파일러
   - 개별 커널 10~185x, 종단간 추론 1.75~11.84x 속도 개선 [P-02]

3. **"HHEML: Hybrid Homomorphic Encryption for Privacy-Preserving Machine Learning on Edge"**
   - arXiv:2510.20243 (2025.10)
   - 핵심: 클라이언트 사이드 경량 대칭 암호화 + 서버 FHE 연산 결합
   - FPGA(PYNQ-Z2) 기준 기존 HHE 대비 클라이언트 지연 50x 감소, 처리량 2x [P-03]

4. **"FHE-Agent: Automating CKKS Configuration for Practical Encrypted Inference via an LLM-Guided Agentic Framework"**
   - arXiv:2511.18653 (2025.11)
   - 핵심: CKKS 파라미터 설정(링 차원, 모듈러스 체인, 패킹) 자동화 에이전트 [P-04]

5. **"Fully Homomorphic Encryption for Matrix Arithmetic"**
   - IACR ePrint 2025/1935 (2025.10)
   - 저자: Craig Gentry, Yongwoo Lee (DESILO CTO) 공저
   - 핵심: 암호화 행렬 연산 80x 가속하는 새로운 방법론 [P-05]

6. **"A Scalable Multi-GPU Framework for Encrypted Large-Model Inference" (Cerium)**
   - arXiv:2512.11269 (2025.12)
   - 핵심: 멀티-GPU FHE 추론 프레임워크
   - 성과: 부트스트래핑 7.5ms (최초 10ms 미만), BERT-Base 8초, Llama3-8B 134초 암호화 추론 [P-06]

**[2026년]**

7. **"FHECore: Rethinking GPU Microarchitecture for Fully Homomorphic Encryption"**
   - arXiv:2602.22229 (2026.2)
   - 저자: Boston University, Northeastern University, KAIST, Univ. of Murcia 공동 연구
   - 핵심: GPU Streaming Multiprocessor 내 전용 FHE 함수 유닛(FHECore) 설계
   - 성과: CKKS 명령어 수 2.41x 감소, 성능 최대 2.12x 향상, 부트스트래핑 50% 감소, 면적 오버헤드 2.4% [P-07]

8. **"Privacy-Preserving LLM Inference in Practice"**
   - IACR ePrint 2026/105 (2026)
   - 핵심: FHE 기반 LLM 추론 실용화 현황 종합 서베이 [P-08]

9. **"ELLMo: Packing- and Depth-Aware Encrypted Transformer Inference"**
   - IACR ePrint 2026/198 (2026)
   - 핵심: Statistical-max Softmax, DelayNorm으로 부트스트래핑 46% 감소
   - BERT-Tiny 기준 SOTA 대비 1.4x 속도 향상, 정확도 손실 0~1.5% [P-09]

10. **"Cachemir: Fully Homomorphic Encrypted Inference of Generative Large Language Model with KV Cache"**
    - arXiv:2602.11470 (2026.2)
    - 핵심: KV Cache를 FHE에 통합하여 자기회귀 디코딩 효율 극대화
    - MOAI(ICML'25) 대비 48.83x, THOR(CCS'25) 대비 67.16x 속도 향상
    - GPU에서 Llama-3-8B 토큰 당 100초 미만 [P-10]

11. **"Efficient Softmax Reformulation for Homomorphic Encryption via Moment Generating Function"**
    - arXiv:2602.01621 (2026.2)
    - 핵심: Transformer의 Softmax를 FHE 친화적으로 재설계 [P-11]

### 5.2 연구 트렌드 요약

- **방향 1**: GPU/ASIC 하드웨어 최적화 — NTT, 부트스트래핑, 행렬 연산 병목 해소
- **방향 2**: 암호화 친화적 모델 설계 (FHE-Friendly Architecture) — Softmax, LayerNorm, GeLU 근사
- **방향 3**: 멀티-GPU 분산 추론 — 테라바이트급 메모리 문제 해결
- **방향 4**: KV Cache 통합 — 생성형 LLM의 자기회귀 디코딩 효율화
- **방향 5**: 하이브리드 HE (에지) — 클라이언트 경량화로 온디바이스 가능성 확대

---

## 6. 특허 동향

### 6.1 주요 특허 활동

| 출원인 | 특허번호 | 등록일 | 내용 | 관할 |
|--------|---------|--------|------|------|
| Samsung Electronics | US 12,231,531 | 2025.2.18 | 초월함수 근사 연산 지원 동형암호 시스템 (이진 트리 구조 동형 곱셈) | USPTO |
| Samsung Electronics | US 12,362,904 | 확인 필요 | 동형암호 연산 가속기 및 동작 방법 | USPTO |
| CryptoLab | 원천특허 다수 | — | CKKS 스킴 원천특허 보유 | 다국가 |

### 6.2 특허 트렌드 분석

- 2024-2025년 FHE 특허 출원이 급격히 증가하고 있으나 USPTO PatentsView 실시간 데이터 미수집 (MCP 미연동 상태)
- 삼성전자: 하드웨어 가속기, 근사 연산 최적화 특허 지속 출원
- 대기업(Google, Microsoft, IBM, Apple): 라이브러리/오픈소스 전략을 특허보다 선호하는 경향
- DARPA DPRIVE 계약 기업들: 정부 계약으로 상당 기술이 비공개

> 특허 데이터 공백: patent-intel MCP 미연동으로 상세 출원 데이터 수집 불가. 위 정보는 웹 검색 기반 [B/C] 신뢰도.

---

## 7. 기업 발언 & 보도자료

### 7.1 LG유플러스 (MWC 2026, 2026.3.1 기준)

**공식 발표 내용** [E-03, E-04]:
- "동형암호를 AI 통화앱 익시오(ixi-O), AICC 등 AI 서비스에 적용해 데이터가 탈취되더라도 암호화된 개인정보에 대한 접근을 원천적으로 낮추는 방향으로 보안을 강화할 계획"
- 보안 브랜드 **'익시 가디언 2.0(Xci Guardian 2.0)'** 론칭
- **4종 보안 기술**: ①동형암호, ②알파키(AlphaKey, AI 이상감지 통합계정관리), ③PQC 기반 광전송장비, ④U+SASE
- CryptoLab과의 협업으로 "데이터 저장·전송·처리 전 과정에서 암호화 형태 유지" 구현

### 7.2 DESILO & Cornami

**2025.9.16 보도자료** (PR Newswire) [E-01]:
- "배포 가능한 FHE 기반 LLM 출시" (AI Infra Summit 2025 발표)
- PCMM(Plaintext Ciphertext Matrix Multiplication) 기술로 LLM 연산의 90%+ 처리
- HARVEST 플랫폼 (의료 데이터 협업) 2025.12 출시 예정 발표

**2025.11.13 보도자료** (PR Newswire) [E-02]:
- Craig Gentry(FHE의 아버지, Gödel상 수상)와 Yongwoo Lee(DESILO 암호기술 총괄) 공동 연구
- "대표적 최신 기준 대비 암호화 행렬 곱셈 80x 더 빠른 방법 도입"

### 7.3 Niobium

**2025.12 자금 조달 발표** [E-08]:
- "$23M+ 초과 인수 후속 투자 완료"
- "2세대 FHE 플랫폼의 생산 실리콘 아키텍처 완성, 생산용 ASIC 개발 시작"
- 전략적 투자자 **한국산업은행(KDB)** 포함

### 7.4 Zama

**2025.6.25 발표** [G-08]:
- "FHE 분야 최초 유니콘 달성, $57M Series B 유치"
- "총 $150M 이상 누적 투자"

---

## 8. 이벤트 & 표준화 동향

### 8.1 제9회 HomomorphicEncryption.org 표준화 회의

- **일시**: 2026년 3월 5~6일
- **장소**: 서울 LG사이언스파크 ISC 빌딩
- **키노트**: Craig Gentry, "Encrypted LLM Inference with Batching Across Users" [N-01]
- **주요 세션**: NIST 업데이트, 보안, 유스케이스·벤치마킹, FHE 시스템 병렬 분과
- 등록 마감 완료 (얼리버드: 2026.2.11)

### 8.2 FHE.org 2026 컨퍼런스 (제5회)

- **일시**: 2026년 3월 8일 (Real World Crypto 2026 공동 개최)
- **장소**: 대만 타이베이 Marriott Hotel
- **주최**: FHE.org (IACR ICW-IACR 협력) [N-02]
- 세션: 발표, 포스터, 초청 연사, 네트워킹

### 8.3 표준화 현황

- **ISO/IEC JTC1 SC27**: FHE 표준화 진행 중 (ISO/IEC 18033-6:2019 부분 HE 기존 표준)
- **NIST PEC 프로젝트**: FHE 포함한 Privacy-Enhancing Cryptography 표준화 추진
- **NIST Multi-Party Threshold Schemes 공모 (2023 초안, 2025 제출)**: C2.6 항목 FHE 포함
- 제8회 회의 (2025.3.23, 이스탄불) → 제9회 회의 (2026.3.5-6, 서울) 연속 진행

---

## 9. 전략적 시사점

> 주의: 이 섹션은 팩트 정리이며, Go/No-Go 판단은 WTIS 영역입니다.

### 9.1 확인된 기회 신호

1. **한국의 글로벌 FHE 중심지화**: CryptoLab(CKKS 원천특허), DESILO(Cornami 협업), 제9회 표준화 회의 서울 개최 — 한국이 FHE 기술 및 표준화의 글로벌 허브로 자리매김
2. **LG유플러스의 선제적 포지셔닝**: MWC 2026에서 CryptoLab 협업 동형암호를 익시오 적용 계획 발표 — 통신 AI 서비스에 FHE 도입 공식화
3. **하이브리드 HHE의 에지 실현 가능성**: HHEML이 FPGA에서 50x 클라이언트 지연 감소 달성 → 온디바이스-서버 하이브리드 구조가 현실적 경로
4. **Craig Gentry의 "Multi-User 배칭" 연구**: 여러 사용자 요청을 배칭 처리하는 암호화 LLM 추론 → 통신 서비스 규모에 적합한 서버사이드 FHE-LLM 가능성

### 9.2 확인된 리스크/제약

1. **순수 온디바이스 FHE는 아직 TRL 3-4**: 스마트폰에서 직접 FHE 연산 수행은 배터리·처리능력 제약으로 미달
2. **성능 오버헤드 여전히 큼**: Llama3-8B 암호화 추론 134초 → 실시간 음성통화 등 저지연 응용에 미적합
3. **시장 전망치 신뢰도 낮음**: 기관마다 최대 100배 차이나는 시장 규모 — $234M vs $29B (2025/2032)
4. **Apple의 온디바이스 레퍼런스**: iOS 18 Live Caller ID Lookup이 스마트폰 BFV 적용 최초 사례이나, 복잡한 AI 추론과는 난이도 차이 큼

---

## 신뢰도 평가

### 높은 확신 [A/B]

- FHECore (arXiv:2602.22229): 2.41x 명령어 감소, 50% 부트스트래핑 감소 — 동료 심사 전이나 공개 arXiv 논문, 수치 명확 [B]
- Cerium (arXiv:2512.11269): Llama3-8B 134초, 부트스트래핑 7.5ms — 동일 [B]
- DESILO+Cornami PR Newswire 보도자료 (2025.9, 2025.11): 공식 보도자료, 80x 수치 포함 [B]
- LG유플러스 MWC 2026 발표: 복수 한국 언론 보도, 내용 일치 [B]
- Zama $57M Series B: CoinDesk, TechEU 등 복수 독립 매체 확인 [A]
- Niobium $23M 투자: SecurityWeek, The Quantum Insider 등 복수 확인 [A]
- 제9회 표준화 회의 (서울, 2026.3.5-6): 공식 homomorphicencryption.org 페이지 확인 [A]
- Apple Swift HE, iOS 18 적용: Apple 공식 발표 [A]

### 추가 검증 필요 [C/D]

- 시장 규모 전망 ($1.2B→$8.4B 등): 보고서마다 편차 큼, 방법론 불명확 [C]
- Samsung Smart SSD 동형암호 개발 현황: 공식 발표 없음, CryptoLab 홈페이지 언급만 확인 [C]
- DARPA DPRIVE 2025-2026 최신 진행 상황: 업데이트된 공식 발표 미확인 [C]
- Cornami 칩 상용화 시점: "2025년 중 출시" 언급이나 실제 제품 출시 확인 불가 [C]

### 데이터 공백

- **특허 상세 데이터**: patent-intel MCP 미연동으로 출원 트렌드, 주요 청구항 세부 분석 불가
- **한국 정부(과기부) FHE 지원 사업**: 한국어 정부 자료 검색 결과 부재
- **Desilo-Konami 파트너십**: 검색 결과 없음 (Tier 1 신호의 "코나미"는 Cornami의 오기일 가능성 높음)
- **CryptoLab 2025-2026 매출/투자 최신 정보**: 공개 재무 데이터 없음
- **Cerium, ELLMo 등 최신 논문 인용수**: 너무 최신이라 인용 데이터 없음

---

## References

### 글로벌 출처 (G-xx)

| 번호 | 출처명 | 발행일 | 기관유형 | 제목 | 인용원문(한글) | 관련성 | 신뢰성 | 최신성 | URL |
|------|--------|-------|----------|------|-------------|--------|--------|--------|-----|
| G-01 | Semiconductor Engineering | 2026.2 | 기술 미디어 | A GPU Microarchitecture Optimized for Fully Homomorphic Encryption | FHECore: 2.41x 명령어 감소, 부트스트래핑 50% 감소 | 5 | 4 | 5 | https://semiengineering.com/a-gpu-microarchitecture-optimized-for-fully-homomorphic-encryption/ |
| G-02 | OpenReview | 2026 | 학술 플랫폼 | Privacy-Preserving Large Language Model Inference via GPU-Accelerated FHE | GPU 가속 FHE로 CPU 대비 200x+ 개선, GPT-2 추론 구현 | 5 | 4 | 5 | https://openreview.net/forum?id=Rs7h1od6ov |
| G-03 | Cornami 공식 | 2025.9 | 기업 | Cornami and DESILO Bring Encrypted AI to Scale with Deployable FHE-Based LLM | 배포 가능한 FHE-LLM, PCMM 기술, HARVEST 플랫폼 | 5 | 4 | 5 | https://cornami.com/cornami-and-desilo-bring-encrypted-ai-to-scale-with-deployable-fhe-based-llm/ |
| G-04 | Duality Technologies 블로그 | 2024 | 기업 | Hardware Acceleration of Fully Homomorphic Encryption | FHE 하드웨어 가속 현황, DARPA DPRIVE 배경 | 4 | 4 | 3 | https://dualitytech.com/blog/hardware-acceleration-of-fully-homomorphic-encryption-making-privacy-preserving-machine-learning-practical/ |
| G-05 | CryptoLab 공식 | 2025 | 기업 | HEaaN Library | HEaaN 4세대 CKKS, Samsung Smart SSD 협업, IBM 탑재 | 5 | 5 | 4 | https://www.cryptolab.co.kr/en/products-en/heaan-he/ |
| G-06 | arXiv | 2026.2 | 학술 | FHECore: Rethinking GPU Microarchitecture for Fully Homomorphic Encryption | FHECore 상세 기술 사양, 2D systolic array PE, Barrett reduction 내장 | 5 | 4 | 5 | https://arxiv.org/abs/2602.22229 |
| G-07 | The Quantum Insider | 2025.12 | 기술 미디어 | Niobium Raises $23M+ to Advance Next-Gen FHE Hardware | $23M+ 투자, 2세대 ASIC, KDB 한국산업은행 투자 포함 | 5 | 4 | 5 | https://thequantuminsider.com/2025/12/03/niobium-23m-fhe-funding/ |
| G-08 | CoinDesk | 2025.6 | 미디어 | FHE Pioneer Zama Raises $57M, Becomes First Fully Homomorphic Encryption Unicorn | Zama $57M Series B, FHE 분야 최초 유니콘, $1B 밸류에이션 | 4 | 4 | 4 | https://www.coindesk.com/tech/2025/06/25/zama-raises-57m-becomes-first-unicorn-involved-with-fully-homomorphic-encryption |
| G-09 | 머니투데이 | 2024.3 | 언론 | 네이버·LG가 찜한 동형암호 스타트업 '디사일로', 추가 투자유치 | 디사일로 시리즈 A 60억원, 네이버·KB투자 참여 | 4 | 4 | 3 | https://news.mt.co.kr/mtview.php?no=2024032710240092113 |
| G-10 | arXiv | 2025.12 | 학술 | A Scalable Multi-GPU Framework for Encrypted Large-Model Inference (Cerium) | Cerium: 부트스트래핑 7.5ms, BERT-Base 8초, Llama3-8B 134초 | 5 | 4 | 5 | https://arxiv.org/abs/2512.11269 |
| G-11 | IACR ePrint | 2025.10 | 학술 | Fully Homomorphic Encryption for Matrix Arithmetic (Craig Gentry, Yongwoo Lee) | 암호화 행렬 연산 80x 가속 방법론 | 5 | 5 | 5 | https://eprint.iacr.org/2025/1935 |
| G-12 | arXiv | 2025.10 | 학술 | HHEML: Hybrid Homomorphic Encryption for Privacy-Preserving Machine Learning on Edge | FPGA HHEML: 클라이언트 지연 50x 감소, 처리량 2x | 5 | 4 | 5 | https://arxiv.org/abs/2510.20243 |
| G-13 | IACR ePrint | 2026 | 학술 | ELLMo: Packing- and Depth-Aware Encrypted Transformer Inference | Statistical-max Softmax, DelayNorm, 부트스트래핑 46% 감소 | 5 | 4 | 5 | https://eprint.iacr.org/2026/198 |
| G-14 | arXiv | 2026.2 | 학술 | Cachemir: Fully Homomorphic Encrypted Inference of Generative LLM with KV Cache | KV Cache 통합 FHE-LLM, Llama-3-8B 토큰당 100초 미만 | 5 | 4 | 5 | https://arxiv.org/abs/2602.11470 |
| G-15 | arXiv | 2025.1 | 학술 | Leveraging ASIC AI Chips for Homomorphic Encryption (CROSS) | TPUv4 기준 CPU 대비 161x, GPU 대비 5x 속도 | 5 | 4 | 4 | https://arxiv.org/abs/2501.07047 |
| G-16 | Duality Tech 발표 | 2025.11 | 기업 | Duality supports Google Cloud Confidential Computing | NVIDIA GPU confidential VM, 암호화 LLM 학습·추론 | 4 | 4 | 4 | https://dualitytech.com/ |
| G-17 | DARPA/IntelCapital | 2021~현재 | 정부/기업 | DARPA DPRIVE program, Intel Completes Phase One | 4개 팀 계약, 목표 5 OoM 성능 개선 | 4 | 5 | 3 | https://community.intel.com/t5/Blogs/Products-and-Solutions/HPC/Intel-Completes-DARPA-DPRIVE-Phase-One-Milestone-for-a-Fully/post/1411021 |
| G-18 | Swift.org | 2024.7 | 기업 공식 | Announcing Swift Homomorphic Encryption | Apple BFV 기반 온디바이스 HE, iOS 18 Live Caller ID 적용 | 5 | 5 | 4 | https://www.swift.org/blog/announcing-swift-homomorphic-encryption/ |
| G-19 | ACM DL | 2025 | 학술 | MetaKernel: Enabling Efficient Encrypted Neural Network Inference through Unified MVM and Convolution | 커널 10~185x, 종단간 1.75~11.84x 속도 개선 | 5 | 4 | 5 | https://dl.acm.org/doi/10.1145/3763095 |
| G-20 | arXiv | 2025.11 | 학술 | FHE-Agent: Automating CKKS Configuration via LLM-Guided Agentic Framework | CKKS 파라미터 설정 자동화 에이전트 | 4 | 4 | 5 | https://arxiv.org/abs/2511.18653 |
| G-21 | ACM DL | 2025 | 학술 | Performance Analysis: SEAL, HElib, OpenFHE, Lattigo Benchmark | SEAL CKKS 최고 속도, HElib BGV 최고 | 4 | 4 | 4 | https://dl.acm.org/doi/10.1145/3729706.3729711 |
| G-22 | Apple Machine Learning Research | 2024 | 기업 공식 | Combining Machine Learning and Homomorphic Encryption in the Apple Ecosystem | Enhanced Visual Search, Live Caller ID 등 실제 적용 | 5 | 5 | 4 | https://machinelearning.apple.com/research/homomorphic-encryption |
| G-23 | IACR ePrint | 2026 | 학술 | Privacy-Preserving LLM Inference in Practice | FHE-LLM 추론 실용화 현황 종합 서베이 | 5 | 4 | 5 | https://eprint.iacr.org/2026/105.pdf |
| G-24 | openpr.com | 2025 | 시장조사 | Homomorphic Encryption Market: USD 1.2B (2026) to USD 8.4B (2033) | IT/통신 분야 동형암호 시장 전망 | 3 | 2 | 4 | https://www.openpr.com/news/4230086/homomorphic-encryption-market-by-type-and-application-rapid |
| G-25 | arXiv | 2026.2 | 학술 | Efficient Softmax Reformulation for HE via Moment Generating Function | Softmax FHE 재설계 | 4 | 4 | 5 | https://arxiv.org/abs/2602.01621 |

### 최신 동향 (N-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약(한글) | URL |
|------|--------|-------|------|-----------|----------|-----|
| N-01 | HomomorphicEncryption.org | 2026.3 | 9th HomomorphicEncryption.org Standards Meeting | standards meeting Seoul 2026 | 2026.3.5-6 서울 LG사이언스파크, Craig Gentry 키노트, NIST 업데이트 세션 | https://homomorphicencryption.org/9th-homomorphicencryption-org-standards-meeting/ |
| N-02 | FHE.org | 2026.3 | FHE.org 2026 Conference - Taipei | FHE.org conference Taipei 2026 | 2026.3.8 대만 타이베이, Real World Crypto 2026 공동 개최 | https://fhe.org/conferences/conference-2026/ |
| N-03 | fheorg.substack.com | 2026.2 | FHE.org digest #38: FHE.org 2026 Conference, Upcoming Events | FHE.org digest 38 | 2026 컨퍼런스 상세, 9회 표준화 회의 안내 | https://fheorg.substack.com/p/fheorg-digest-38-fheorg-2026-conference |
| N-04 | 머니투데이 | 2025.10 | 대기업도 연이어 털렸다…해킹 원천차단 '동형암호' 기술 뜬다 | 동형암호 통신 텔레콤 2025 | 동형암호 기술 주목도 상승 배경, 국내 사이버 침해 사례 증가 | https://www.mt.co.kr/future/2025/10/09/2025093015561341705 |

### 기업 발언 (E-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약원문 |
|------|--------|-------|------|-----------|---------|
| E-01 | PR Newswire | 2025.9.16 | Cornami and DESILO Bring Encrypted AI to Scale with Deployable FHE-Based LLM | Cornami Desilo FHE LLM 2025 | "At the AI Infra Summit 2025, Cornami and DESILO announced the deployment of a fully homomorphic encryption (FHE) based LLM... PCMM allows these operations to be executed securely with extremely low overhead." |
| E-02 | PR Newswire | 2025.11.13 | DESILO and Cornami Announce Breakthrough in Encrypted AI Computation | DESILO Cornami Craig Gentry 80x | "co-authored by Craig Gentry... and Yongwoo Lee... introduces a new method... delivers up to 80× faster encrypted matrix multiplication compared to representative state-of-the-art baselines." |
| E-03 | Korea IT Times | 2026.2 | LG Uplus Unveils AI, Homomorphic Encryption and Quantum-Resistant Security Technologies at MWC26 | LG Uplus MWC 2026 homomorphic encryption | "LG Uplus will present its plan to apply homomorphic encryption to its AI calling app, ixi-O... In collaboration with CryptoLab, the company has developed homomorphic encryption technology." |
| E-04 | 이비엔(EBN) | 2026.3 | [MWC 2026] LG유플러스, '익시 가디언 2.0' 공개 | LG유플러스 MWC 2026 동형암호 | "동형암호를 익시오(ixi-O), AICC 등 AI 서비스에 적용해 데이터가 탈취되더라도 암호화된 개인정보 접근을 원천적으로 낮추는 방향으로 보안을 강화할 계획" |
| E-05 | PR Newswire | 2024.3 | CryptoLab Signs a Contract to Supply Homomorphic Encryption Technology to Macrogen | CryptoLab HEaaN 2024 | "signing of a three-year supply contract with Macrogen, Korea's largest genetic data analysis company... HEaaN Genome Analysis Solution based on CKKS scheme." |
| E-06 | CryptoLab 공식 | 2024 | IBM installs CryptoLab HEaaN Library in HElayers | CryptoLab IBM HElayers | "IBM has installed and launched CryptoLab's HEaaN Library in HElayers, a homomorphic encryption-based AI analysis software." |
| E-07 | Niobium/PR Newswire | 2024.10.10 | CryptoLab and Niobium Partner to Bring Guaranteed Privacy to LLM and Generative AI | CryptoLab Niobium partnership | "integrating CryptoLab's industry-leading HE software with Niobium's FHE acceleration hardware... goal: fully encrypted GenAI/LLM inferencing at speeds comparable to unencrypted operations." |
| E-08 | AccessNewswire | 2025.12 | Niobium Secures $23M+ Oversubscribed Financing | Niobium 23M FHE hardware | "transition from prototype to production-ready silicon, ASIC development, software-hardware co-design... total funding over $28 million." |

### 학술 논문 (P-xx)

| 번호 | 저자 | 발행년도 | 제목 | 학술지/컨퍼런스 | 인용수 | 핵심 인용 | DOI/URL |
|------|------|---------|------|----------------|--------|----------|---------|
| P-01 | Jianming Tong et al. (GT, MIT, Google, Cornell) | 2025.1 | Leveraging ASIC AI Chips for Homomorphic Encryption (CROSS) | arXiv preprint | — | "CROSS (TPU v6e) achieves higher throughput per watt on NTT and HE operators... up to 161x speedup vs CPUs" | https://arxiv.org/abs/2501.07047 |
| P-02 | ACM 저자 | 2025 | MetaKernel: Enabling Efficient Encrypted Neural Network Inference through Unified MVM and Convolution | ACM Proceedings on Programming Languages | — | "inference time speedups of 10.08×–185.60× for individual kernels, 1.75×–11.84× end-to-end" | https://dl.acm.org/doi/10.1145/3763095 |
| P-03 | HHEML 저자 | 2025.10 | HHEML: Hybrid HE for Privacy-Preserving ML on Edge | arXiv:2510.20243 | — | "50× lower client-side latency, close to 2× higher throughput vs prior FPGA-based HHE" | https://arxiv.org/abs/2510.20243 |
| P-04 | arXiv 저자 | 2025.11 | FHE-Agent: Automating CKKS Configuration for Practical Encrypted Inference | arXiv:2511.18653 | — | "automates expert reasoning by coupling an LLM controller with a deterministic tool suite" | https://arxiv.org/abs/2511.18653 |
| P-05 | Craig Gentry, Yongwoo Lee (DESILO) | 2025.10 | Fully Homomorphic Encryption for Matrix Arithmetic | IACR ePrint 2025/1935 | — | "delivers up to 80× faster encrypted matrix multiplication compared to state-of-the-art baselines" | https://eprint.iacr.org/2025/1935 |
| P-06 | Cerium 저자 | 2025.12 | A Scalable Multi-GPU Framework for Encrypted Large-Model Inference (Cerium) | arXiv:2512.11269 | — | "first to execute bootstrapping under 10ms (7.5ms), encrypted inference for BERT-Base (8s) and Llama3-8B (134s)" | https://arxiv.org/abs/2512.11269 |
| P-07 | Boston Univ., Northeastern, KAIST, Univ. Murcia | 2026.2 | FHECore: Rethinking GPU Microarchitecture for Fully Homomorphic Encryption | arXiv:2602.22229 | — | "2.41× instruction count reduction, up to 2.12× speedup, 50% bootstrapping latency reduction, 2.4% area overhead" | https://arxiv.org/abs/2602.22229 |
| P-08 | ePrint 저자 | 2026 | Privacy-Preserving LLM Inference in Practice | IACR ePrint 2026/105 | — | FHE-LLM 추론 실용화 현황 서베이 | https://eprint.iacr.org/2026/105.pdf |
| P-09 | ELLMo 저자 | 2026 | ELLMo: Packing- and Depth-Aware Encrypted Transformer Inference | IACR ePrint 2026/198 | — | "Statistical-max Softmax, DelayNorm reduce bootstrapping by up to 46%, 1.4× speedup on BERT-Tiny" | https://eprint.iacr.org/2026/198 |
| P-10 | Cachemir 저자 | 2026.2 | Cachemir: Fully Homomorphic Encrypted Inference of Generative LLM with KV Cache | arXiv:2602.11470 | — | "48.83× over MOAI, 67.16× over THOR... under 100s on GPU for Llama-3-8B" | https://arxiv.org/abs/2602.11470 |
| P-11 | arXiv 저자 | 2026.2 | Efficient Softmax Reformulation for HE via Moment Generating Function | arXiv:2602.01621 | — | FHE 친화적 Softmax 재설계 | https://arxiv.org/abs/2602.01621 |

### 특허 (T-xx)

| 번호 | 출원인 | 등록/출원일 | 특허번호 | 제목 | 핵심 청구항 | 관할 |
|------|--------|-----------|---------|------|-----------|------|
| T-01 | Samsung Electronics | 2025.2.18 (등록) | US 12,231,531 | Homomorphic encryption system for supporting approximate arithmetic operation | 이진 트리 구조 동형 곱셈을 이용한 초월함수 근사 연산 | USPTO |
| T-02 | Samsung Electronics | 확인 필요 | US 12,362,904 | Homomorphic encryption operation accelerator and operating method | 동형암호 연산 가속기 하드웨어 및 동작 방법 | USPTO |

### 내부 자료 (I-xx)

해당 없음 (내부 자료 미제공)

---

*보고서 생성: 2026-03-03 | Agent: research-deep | 모델: Claude Sonnet 4.6*
*MCP 미연동 제약: research-hub (Semantic Scholar), patent-intel (USPTO PatentsView), trend-tracker 미사용 — 모든 데이터는 WebSearch/WebFetch 기반*
