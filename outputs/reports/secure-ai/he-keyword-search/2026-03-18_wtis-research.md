---
type: wtis-research
topic: he-keyword-search
domain: secure-ai
l2_topic: quantum-he
date: 2026-03-18
parent: 2026-03-18_wtis-he-keyword-search
---

# WTIS 심층 리서치: On-Device 동형암호 키워드 검색

## Executive Summary

> On-Device FHE 키워드 검색은 2026년 초 기준 TRL 3~4로 상향 재평가된다. Intel Heracles ASIC(1,074~5,547× 가속)과 Niobium 2세대 ASIC(삼성 8nm, 2026년 양산 전환 중)이 하드웨어 장벽을 빠르게 낮추고 있으며, 클라이언트-사이드 경량화(97% enc/dec 비용 절감, Aikata et al. 2026)와 키워드 PIR 구현(HET-PIR, BKPIR)이 "구현 가능 단계"를 공식화했다. DESILO GL 스킴(5세대)과 CryptoLab CKKS+(4.5세대)는 행렬 연산 병목을 개선해 AICC·음성 데이터 검색 실시간화 가능성을 높였다. LG유플러스-CryptoLab 협력(MWC 2026)이 통신사 PoC 단계를 공식화했고, 국내에서는 HomomorphicEncryption.org 9차 표준 회의(2026-03 서울)와 NIST Threshold Call(2026-04-20 마감)이 표준화 모멘텀을 강화하고 있다. 신뢰도: 기술 벤치마크 [A/B], 시장 규모 [B/C], 상용화 일정 [C].

---

## 연구 질문

> On-Device 동형암호 키워드 검색(he-keyword-search)의 2026년 기술 성숙도·시장 잠재력·경쟁 구도를 종합 분석하고, 2026-03-03 이전 판정(TRL 2~3, Watch) 대비 달라진 시그널을 정량화한다.

---

## 1. 시장 분석

### TAM/SAM/SOM

**글로벌 FHE 시장 (TAM)**

동형암호 글로벌 시장에 대해 복수 리서치 기관 간 추정치 편차가 크다. 보수적 시나리오(CAGR ~8%)와 적극적 시나리오(CAGR ~20%)가 공존한다. [[G-01]](#ref-g-01) [[G-02]](#ref-g-02) [[G-03]](#ref-g-03)

| 기관 | 2024/2025 기준값 | 2030 전망 | CAGR | 신뢰도 |
|------|-----------------|-----------|------|--------|
| NextMSC | $189.5M (2022) | $358.9M | ~8.3% | [C] |
| GM Insights / Roots Analysis | $234.7M (2025) | $351.5M (2030) | ~8.4% | [C] |
| Data Bridge / Verified | $321.4M (2024) | $594.9M (2032) | ~8.0% | [C] |
| 360 Research Reports | $251.2M (2026) | $1,319M (2035) | **20.2%** | [C] |
| 비고 | $3B (2030) FHE 단독 전망도 존재 | — | — | [D] |

> **교차 검증 결론**: 보수 기준 2030년 $350~600M, 적극 기준 $1~3B. 기관별 FHE 정의 범위 차이가 주요 원인. 단일 수치 인용 금지, 범위로 표기.

**AICC·음성 데이터 보안 시장 (SAM)**

AICC(AI Contact Center) 시장이 FHE 키워드 검색의 1차 SAM이다. [[G-09]](#ref-g-09)

| 기관 | 2025 규모 | 2033/2034 전망 | CAGR |
|------|-----------|----------------|------|
| Archive Market Research | ~$55B (2025) | — | ~22% |
| Data Insights Market | $5.7B (2023) | $28.2B (2033) | ~17.6% |
| Fortune Business Insights | $2.4B (Call Center AI, 2025) | $13.5B (2034) | 20.8% |

> 통신사 AICC는 AICC 전체 시장의 약 20%로 추산되므로 SAM ~$480M (2025, 보수 기준) ~ $2B (2025, 적극 기준). [[G-09]](#ref-g-09)

**한국 SOM (Service Obtainable Market)**

한국 시장은 글로벌 대비 약 2~3% 규모로 추산된다. LG유플러스·KT·SKT 통신 3사 AICC 음성 데이터 보안 수요가 주요 SOM이다. 추정 한국 FHE SOM: 연간 $7~15M (2026~2028 누적 PoC/파일럿 계약 기준). [[G-09]](#ref-g-09) [[E-01]](#ref-e-01)

> 공개 데이터 없음 — 위 추정치는 단일 소스 기반 계산이므로 [D] 수준 정밀도.

### 연도별 시장 전망

**동형암호 글로벌 시장 규모 전망 (보수/적극 시나리오)**

| 연도 | 보수 ($M, CAGR 8%) | 적극 ($M, CAGR 20%) | 키 드라이버 |
|------|--------------------|---------------------|-------------|
| 2024 | 321 | 321 | FHE 라이브러리 성숙, 클라우드 파일럿 |
| 2026 | 374 | 463 | ASIC 하드웨어 등장, AICC 통합 |
| 2028 | 437 | 666 | ISO/IEC 18033-8 표준 예상 확정 |
| 2030 | 510 | 960 | On-Device FHE 본격 양산 |
| 2032 | 595 | 1,382 | PQC-FHE 하이브리드 인프라 확산 |

출처: [[G-01]](#ref-g-01) [[G-02]](#ref-g-02) [[G-03]](#ref-g-03) 기반 추정.

### 인접 시장 기회

- **통신사 음성·AICC 보안**: LG유플러스-CryptoLab PoC 진행 중 [[E-01]](#ref-e-01) [[N-01]](#ref-n-01)
- **Nokia Bell Labs QRYPT**: 암호화 음성 통화 (압축 128×, RWC 2025) [[G-10]](#ref-g-10)
- **금융 음성 데이터**: CryptoLab — 카카오엔터프라이즈, 토스 EFR(얼굴 특징 보호) 배포 중 [[G-11]](#ref-g-11)
- **프라이버시 AI 추론**: Cornami+DESILO FHE LLM 배포 선언 (2025-09) [[E-03]](#ref-e-03)
- **블록체인 기밀 컴퓨팅**: Zama unicorn ($1B 밸류에이션, 2025-06) [[G-12]](#ref-g-12)

---

## 2. 기술 성숙도

### TRL 현황

**이전 판정 (2026-03-03)**: TRL 2~3 — TFHE 32ms/8xH100, ITU-T 150ms 초과, 불가 → Watch

**현재 재평가 (2026-03-18)**: TRL 3~4

재평가 근거:
- Intel Heracles ASIC: FHE 수학 연산 1,074~5,547× 가속, 3nm FinFET, 48GB HBM (819 GB/s) [[G-04]](#ref-g-04) [[G-05]](#ref-g-05)
- Niobium 2세대 ASIC: 삼성 8nm LPU, SEMIFIVE 파트너십 (2026-02-19), KRW 10B 계약, 고객 파일럿 단계 진입 [[G-06]](#ref-g-06) [[E-04]](#ref-e-04)
- Aikata et al. (2026): 클라이언트-사이드 enc/dec 비용 97% 절감, 76× FPGA 가속 [[P-01]](#ref-p-01)
- HET-PIR (2026, Springer Cybersecurity): 32비트 비교 3.9ms, 16비트 batch 0.01ms/건 [[G-08]](#ref-g-08) [[P-03]](#ref-p-03)
- BKPIR (NDSS 2026): FHE 기반 PIR 처리량 10× 향상 [[P-04]](#ref-p-04)
- DESILO GL 스킴 (FHE.org 2026, 3월): 행렬 곱셈 특화 5세대 FHE, Craig Gentry 공동 저자 [[E-02]](#ref-e-02) [[G-07]](#ref-g-07)
- CryptoLab CKKS+ (4.5세대): 행렬 연산 지원, CEO "실시간 레이턴시 없음, On-Device 충분히 경량" 발언 [[E-01]](#ref-e-01)

TRL 4 도달 조건 (아직 미충족): 실제 On-Device(스마트폰급) 엔드-투-엔드 키워드 검색 지연시간 ≤150ms (ITU-T G.114 기준) 공개 검증.

### 성능 벤치마크

**하드웨어 가속기 비교**

| 솔루션 | 공정 | 메모리 | FHE 가속비 | 상태 | 출처 |
|--------|------|--------|-----------|------|------|
| Intel Heracles ASIC | 3nm FinFET | 48GB HBM (819 GB/s) | 1,074~5,547× vs Xeon | 발표 완료 (ISSCC) | [[G-04]](#ref-g-04) [[G-05]](#ref-g-05) |
| Niobium Gen2 ASIC | Samsung 8nm LPU | — | 공개 미공개 | 고객 파일럿 준비 중 | [[G-06]](#ref-g-06) [[E-04]](#ref-e-04) |
| CryptoLab HEaaN GPU | — | GPU 가속 | 100×+ (단일 스레드 대비) | 상용 배포 중 | [[G-13]](#ref-g-13) |
| Zama TFHE-rs v1.0 | CPU x86 | — | 20 TPS → 500~1000 TPS (GPU, 2026 예정) | 블록체인 mainnet 배포 | [[G-12]](#ref-g-12) |
| Aikata et al. FPGA | FPGA | — | 76× vs 선행 연구 | ASIC 합성 결과 포함 | [[P-01]](#ref-p-01) |

**키워드 PIR 레이턴시 비교**

| 시스템 | 쿼리 유형 | 레이턴시 / 처리량 | DB 규모 | 출처 |
|--------|-----------|------------------|---------|------|
| HET-PIR (2026) | 32비트 단일 비교 | 3.9ms | — | [[P-03]](#ref-p-03) |
| HET-PIR (2026) | 16비트 배치 (32,768건) | 0.01ms/건 (amortized) | — | [[P-03]](#ref-p-03) |
| BKPIR (NDSS 2026) | 불리언 키워드 PIR | 10× 처리량 개선 | 대형 payload | [[P-04]](#ref-p-04) |
| Faster Spiral (2025) | 인덱스 PIR | Spiral 대비 1.7× | — | [[P-05]](#ref-p-05) |
| Aikata et al. (2026) | Client-side enc/dec | -97% 비용, 76× FPGA | — | [[P-01]](#ref-p-01) |

> **참고**: On-Device (스마트폰급) 엔드-투-엔드 키워드 검색의 공개 벤치마크는 아직 없음. 위 수치는 서버-사이드 또는 FPGA 기준. 공개 정보 없음.

### 핵심 기술 진전 (이전 대비 변화)

**이전(2026-03-03)에 없었던 신규 시그널:**

1. **DESILO GL 스킴 공개** (2026-03-08, FHE.org 2026 Taipei): FHE 창시자 Craig Gentry 공동 저자, 행렬 곱셈 특화 5세대 스킴. AI LLM 워크로드 대상 최적화. [[E-02]](#ref-e-02)
2. **Niobium Gen2 ASIC → 고객 파일럿** (2026-02-19): SEMIFIVE-삼성 8nm 파트너십, KRW 10B 계약 체결. "세계 최초 상업용 FHE 가속기" 목표. [[E-04]](#ref-e-04) [[G-06]](#ref-g-06)
3. **Aikata et al. 클라이언트 경량화** (2026-03, IACR ePrint 2026/515): 97% enc/dec 절감, FPGA 76× — On-Device FHE의 핵심 병목인 클라이언트 비용 문제에 직접 답변. [[P-01]](#ref-p-01)
4. **LG유플러스-CryptoLab MWC 2026 발표** (2026-03-10): 익시오(ixi-O) AICC에 CKKS+ 적용 PoC 공식화. CEO "실시간 레이턴시 없음" 주장. [[E-01]](#ref-e-01) [[N-01]](#ref-n-01)
5. **HomomorphicEncryption.org 9차 회의 서울 개최** (2026-03-05/06, LG 사이언스파크): NIST 업데이트, Craig Gentry 기조연설, 워킹그룹 3개 병행. [[G-14]](#ref-g-14)
6. **BKPIR & HET-PIR 논문** (NDSS 2026, Springer Cybersecurity 2026): 키워드 PIR이 학술 구현 단계 진입 확인. [[P-03]](#ref-p-03) [[P-04]](#ref-p-04)
7. **Cornami-DESILO FHE LLM 배포** (2025-09): AI Infra Summit 2025에서 "Plaintext 속도에 근접한 암호화 AI 추론" 발표. HARVEST 플랫폼 2025-12 출시. [[E-03]](#ref-e-03)

### 표준화 현황

- **ISO/IEC WD 18033-8**: BGV, BFV, CKKS, CGGI/TFHE 4개 스킴 규정 예정. 현재 의견 수렴 단계, 수년 내 통과 예상. [[G-15]](#ref-g-15)
- **NIST Threshold Call (NISTIR 8214C)**: FHE S5 카테고리 포함. 2026-04-20 Preview Writeup 마감. 2026-01-27 FHE 전용 세션 개최 (3개 T-FHE 발표). [[G-16]](#ref-g-16)
- **HomomorphicEncryption.org 9차 서울 (2026-03-05/06)**: NIST 업데이트, 보안/벤치마킹/FHE 시스템 3개 워킹그룹 병행. Intel Gold 스폰서. [[G-14]](#ref-g-14)
- **ISO/IEC 18033-6:2019**: Paillier, ElGamal 수준의 부분 동형암호만 커버. FHE는 18033-8에서 별도 처리. [[G-15]](#ref-g-15)

---

## 3. 경쟁 환경

### 글로벌 플레이어

**글로벌 주요 플레이어 동향**

| 기업 | 동향 | 출처 |
|------|------|------|
| Apple | iOS 18 Live Caller ID Lookup에 BFV 기반 PIR 배포. Enhanced Visual Search에 PNNS 적용. swift-homomorphic-encryption 오픈소스 공개. | [[G-17]](#ref-g-17) [[G-18]](#ref-g-18) |
| Google | Jaxite(GPU/TPU FHE), HEIR 컴파일러 오픈소스. 2025-11 비디오 FHE 처리 발표. | [[G-19]](#ref-g-19) |
| Microsoft | SEAL 4,500+ 앱 통합, SEAL-Embedded(IoT). ARM 아키텍처 지원 업데이트. | [[G-20]](#ref-g-20) |
| IBM | HElib 지속 개선, 30개+ 엔터프라이즈 프로젝트 배포. FHE+MPC 복합 솔루션 제공. | [[G-20]](#ref-g-20) |
| Intel | Heracles ASIC 발표 (3nm, 48GB HBM, 5,547× 가속). US Army 계약 기반 5년 개발. | [[G-04]](#ref-g-04) [[G-05]](#ref-g-05) |
| Niobium | Gen2 ASIC 파일럿 (삼성 8nm, SEMIFIVE). $23M+ 추가 펀딩. | [[G-06]](#ref-g-06) [[G-21]](#ref-g-21) |
| Zama | TFHE 유니콘 ($1B, 2025-06), mainnet 배포. TFHE-rs v1.0 안정화. | [[G-12]](#ref-g-12) |
| Nokia Bell Labs | QRYPT: 암호화 음성 통화 HE 적용, 128× 압축. RWC 2025 발표. | [[G-10]](#ref-g-10) |
| Duality Technologies | OpenFHE 공동 기여. DARPA 계약. Fortune 500 금융사 배포. | [[G-22]](#ref-g-22) |
| Cornami | DESILO 협력 FHE LLM 배포. Craig Gentry(Chief Scientist). HARVEST 플랫폼 2025-12 출시. | [[E-03]](#ref-e-03) |

### 국내 플레이어

**국내 주요 플레이어 동향**

| 기업 | 동향 | 출처 |
|------|------|------|
| CryptoLab | CKKS 원천 특허 보유. CKKS+(4.5세대, 행렬 연산 지원). LG유플러스 PoC. MWC 2026 발표. CEO: "실시간 레이턴시 없음, On-Device 경량 충분" | [[E-01]](#ref-e-01) [[G-13]](#ref-g-13) |
| DESILO | GL 스킴(5세대, Craig Gentry 공동) FHE.org 2026 발표. Cornami와 FHE LLM 배포. HomomorphicEncryption.org 9차 서울 공동 주최. | [[E-02]](#ref-e-02) [[E-03]](#ref-e-03) |
| LG유플러스 | MWC 2026에서 익시오(ixi-O)+AICC 동형암호 PoC 공식화. CryptoLab 협력. CTO Jaehyun Jang 직접 발언. | [[E-01]](#ref-e-01) [[N-01]](#ref-n-01) |
| SKT | QKD+PQC 하이브리드 양자암호 출시. IonQ, ID Quantique 지분 교환. 동형암호 직접 추진 공식 발표 없음. | [[N-02]](#ref-n-02) |
| KT | 2025 해킹 사고 이후 5년간 1조 원 정보보호 투자 발표. AI 기반 보안 청사진. 동형암호 직접 추진 미확인. | [[N-03]](#ref-n-03) |
| Samsung SDS | FHE 기반 금융·의료 분석 서비스 기술 검증 완료. HomomorphicEncryption.org 표준화 참여. | [[G-23]](#ref-g-23) |
| SEMIFIVE | Niobium Gen2 ASIC 설계 파트너 (삼성 8nm). US 시장 진출 드라이버. | [[E-04]](#ref-e-04) |

### Gap Analysis

**글로벌-국내 경쟁 포지션 비교**

| 역량 | 국내 (CryptoLab/DESILO) | 글로벌 (Apple/Google/Intel) | 격차 방향 |
|------|------------------------|----------------------------|----------|
| 알고리즘 원천 기술 | CKKS 원천 특허 (CryptoLab), GL 스킴 (DESILO) | BFV(Apple), TFHE(Zama), HEIR 컴파일러(Google) | 대등 (CKKS는 한국 우위) |
| On-Device 배포 | PoC 단계 (LGU+ 실증 중) | iOS 18 Live Caller ID 실 배포 | Apple 선행 1~2년 |
| 하드웨어 가속기 | SEMIFIVE-Niobium 파트너십 (설계 단계) | Intel Heracles (발표 완료) | Intel 선행 |
| 표준화 참여 | CryptoLab(정정희 교수 운영위), DESILO (서울 9차 주최) | Intel(Gold 스폰서), Google, Microsoft | 국내 적극 참여 |
| 통신 특화 적용 | LGU+ AICC PoC, Nokia Bell Labs QRYPT | 아직 통신사 메이저 배포 없음 | 국내 통신 분야 잠재 우위 |
| 오픈소스 생태계 | HEaaN (상용), 제한적 공개 | SEAL, HEIR, swift-HE, Jaxite 전면 공개 | 글로벌 생태계 우위 |

---

## 4. 규제·정책 동향

**NIST 표준화**

- NISTIR 8214C Threshold Call: FHE S5 카테고리 포함. 2026-04-20 Preview Writeup 마감. 미제출 팀은 마감 후 참여 불가. 2026-01-27 MPTC 워크숍 FHE 전용 세션 (T-FHE 3개 발표). [[G-16]](#ref-g-16)
- 배경: PQC와 달리 FHE는 아직 NIST 정식 표준 미완료. NIST는 FHE를 Privacy-Enhancing Cryptography 로드맵에 포함. [[G-15]](#ref-g-15)

**ISO/IEC 표준화**

- ISO/IEC WD 18033-8: BGV, BFV, CKKS, CGGI/TFHE 규정 예정. NWI(신규 작업 항목) 승인, 3년 타임라인. 이후 키 관리, FHE-VM, 인터롭 표준화 예정. [[G-15]](#ref-g-15)
- ISO/IEC 18033-6:2019: Paillier/ElGamal 부분 동형암호만 커버. 현행 표준 갭 존재. [[G-15]](#ref-g-15)

**한국 규제 환경**

- 개인정보보호법(PIPA) 개정 시행 (2025-10): 데이터 이동 청구권 신설(2025-03~). PIPC가 동형암호를 프라이버시 강화 기술(PET)로 공식 R&D 확대 방침 명시. [[G-24]](#ref-g-24)
- AI기본법 시행 (2026-01): 한국 최초 AI 프레임워크법. 고위험 AI 시스템 규제. 음성 데이터 처리 AI(AICC)는 고위험 분류 가능성 → 동형암호 기반 프라이버시 강화 수요 직접 연결. [[G-24]](#ref-g-24)
- PIPC 생성형 AI 가이드라인 (2025-08): 개인정보 처리 최소화, 암호화 처리 권고. [[G-24]](#ref-g-24)
- 국가 핵심 인프라 양자암호통신망 구축: 2028년까지 행정·국방·금융 구간 목표. 통신사 수혜. [[N-02]](#ref-n-02)

**글로벌 규제 트렌드**

- EU AI Act (2025~): 고위험 AI 시스템 데이터 보호 강화. FHE가 컴플라이언스 솔루션으로 주목. [[G-24]](#ref-g-24)
- GDPR Article 25 (Privacy by Design): FHE가 기술적 수단으로 인정 가능성 논의 중. [[G-24]](#ref-g-24)
- 미국 FedRAMP·CMMC: 암호화 처리 표준 강화 방향. Intel Heracles의 US Army 계약이 정부 수요를 반증. [[G-05]](#ref-g-05)

---

## 5. 전략적 시사점

**기술 트렌드**

- ASIC 가속기 등장(Intel, Niobium)이 FHE의 최대 장벽인 연산 오버헤드를 2026~2028년 임계점 이하로 낮출 전망
- 클라이언트-사이드 경량화(97%, Aikata 2026)는 스마트폰 온디바이스 키워드 검색의 기술적 전제 조건 해소 방향으로 진화 중
- Apple iOS 18 실 배포가 "On-Device FHE PIR은 불가능하지 않다"는 시장 증거가 됨

**기회**

- AICC·음성 AI 통신 특화: LG유플러스-CryptoLab PoC는 국내 통신사 중 최선두. SKT·KT가 아직 동형암호 직접 배포 미확인 → 선점 가능 창구
- CKKS 원천 기술 보유 국가(한국)의 표준화 주도권: 9차 서울 회의 + NIST 참여 시너지
- AI기본법·PIPA 개정이 "암호화 상태 AI 처리" 수요를 법제도 레벨에서 창출
- 통신사 AICC 파일럿 → 금융(Toss, Kakao)·의료 확장 가능한 레퍼런스 구축 기회

**위협**

- Apple이 이미 BFV 기반 PIR을 iOS 18에 실 배포: On-Device FHE의 첫 대중 배포 주체가 빅테크
- Intel Heracles 가속 효과가 서버-사이드에 집중: On-Device(스마트폰) 적용에는 별도 소형화 필요
- ISO 표준 확정 전 CKKS 우선 채택 여부 불확실 (BFV, BGV, TFHE 경쟁 스킴 존재)
- 단일 소스 시장 수치 의존 위험: 기관별 CAGR 편차(8%~20%)가 투자 근거 산정 어렵게 함

**이전 분석 대비 핵심 변화 (2026-03-03 → 2026-03-18)**

| 항목 | 이전 (2026-03-03) | 현재 (2026-03-18) | 변화 |
|------|------------------|------------------|------|
| TRL 평가 | 2~3 (실험실 단계) | 3~4 (검증/파일럿 진입) | 상향 |
| 핵심 병목 | 연산 속도 (32ms/8xH100) | 클라이언트 경량화 진전(97% 절감) | 부분 해소 |
| 하드웨어 가속기 | FPGA 연구 수준 | Intel ASIC 발표, Niobium 파일럿 | 임박 상용화 |
| 키워드 PIR 구현 | 학술 프로토타입 | BKPIR(NDSS2026), HET-PIR(Springer2026) | 구현 단계 공식화 |
| 통신사 PoC | 없음 | LGU+-CryptoLab MWC 2026 공식 발표 | 신규 |
| 표준화 일정 | 모호 | NIST 2026-04-20 마감, ISO 3년 타임라인 | 구체화 |
| 한국 클러스터 | CryptoLab 독립 존재 | CryptoLab+DESILO+SEMIFIVE+LGU+ 에코시스템 | 확장 |

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | NextMSC — Homomorphic Encryption Market Size and Share 2023-2030 | [링크](https://www.nextmsc.com/report/homomorphic-encryption-market) | report | 2024 | [C] |
| <a id="ref-g-02"></a>G-02 | GM Insights / Roots Analysis — Homomorphic Encryption Market Size Forecasts 2035 | [링크](https://www.gminsights.com/industry-analysis/homomorphic-encryption-market) | report | 2025 | [C] |
| <a id="ref-g-03"></a>G-03 | 360 Research Reports — Homomorphic Encryption Market CAGR 20.2% | [링크](https://www.360researchreports.com/market-reports/homomorphic-encryption-market-206111) | report | 2025 | [C] |
| <a id="ref-g-04"></a>G-04 | Tom's Hardware — Intel Heracles Chip 1,074~5,547× Faster | [링크](https://www.tomshardware.com/tech-industry/cyber-security/intels-heracles-chip-computes-fully-encrypted-data-without-decrypting-it-chip-is-1-074-to-5-547-times-faster-than-a-24-core-intel-xeon-in-fhe-math-operations) | news | 2025 | [B] |
| <a id="ref-g-05"></a>G-05 | IEEE Spectrum — Intel Heracles Chip Speeds Up Encrypted Computing | [링크](https://spectrum.ieee.org/fhe-intel) | news | 2025 | [B] |
| <a id="ref-g-06"></a>G-06 | PR Newswire — SEMIFIVE Partners with Niobium to Develop FHE Accelerator | [링크](https://www.prnewswire.com/news-releases/semifive-partners-with-niobium-to-develop-fhe-accelerator-driving-us-market-expansion-302692312.html) | press | 2026-02-19 | [B] |
| <a id="ref-g-07"></a>G-07 | CybersecAsia — DESILO and FHE Inventor Craig Gentry Introduce 5th-Generation GL FHE Scheme | [링크](https://cybersecasia.net/pr-newswire/desilo-and-fhe-inventor-craig-gentry-introduce-5th-generation-gl-fhe-scheme-for-private-ai/) | news | 2026-03-08 | [B] |
| <a id="ref-g-08"></a>G-08 | Springer Cybersecurity — HET-PIR: Practical Keyword PIR via Novel Homomorphic Equality Test | [링크](https://link.springer.com/article/10.1186/s42400-025-00506-x) | paper | 2026-01 | [A] |
| <a id="ref-g-09"></a>G-09 | Fortune Business Insights — Call Center AI Market Size $2.41B (2025) to $13.52B (2034) | [링크](https://www.fortunebusinessinsights.com/call-center-ai-market-109249) | report | 2025 | [C] |
| <a id="ref-g-10"></a>G-10 | Nokia Bell Labs — QRYPT End-to-End Encrypted Audio Conferencing (RWC 2025) | [링크](https://www.nokia.com/bell-labs/collaboration-opportunities/entrepreneurs-in-residence/end-to-end-encrypted-audio-conferencing/) | research | 2025 | [B] |
| <a id="ref-g-11"></a>G-11 | Unicorn Factory — 동형암호 기술 급부상 (CryptoLab, 카카오, Toss) | [링크](https://www.unicornfactory.co.kr/article/2025093015561341705) | news | 2025-09-30 | [B] |
| <a id="ref-g-12"></a>G-12 | BlockEden — Zama Protocol: FHE Unicorn $1B Valuation (2025-06) | [링크](https://blockeden.xyz/blog/2026/01/05/zama-protocol/) | news | 2026-01-05 | [B] |
| <a id="ref-g-13"></a>G-13 | CryptoLab Official — HEaaN Library GPU 100× Acceleration | [링크](https://www.cryptolab.co.kr/en/products-en/heaan-he/) | official | 2025 | [B] |
| <a id="ref-g-14"></a>G-14 | HomomorphicEncryption.org — 9th Standards Meeting Seoul (2026-03-05/06) | [링크](https://homomorphicencryption.org/9th-homomorphicencryption-org-standards-meeting/) | official | 2026-03-05 | [A] |
| <a id="ref-g-15"></a>G-15 | ISO/IEC 18033 & IAPP — FHE Standardization ISO WD 18033-8 Progress | [링크](https://iapp.org/news/a/the-latest-in-homomorphic-encryption-a-game-changer-shaping-up) | news | 2025 | [B] |
| <a id="ref-g-16"></a>G-16 | NIST CSRC — Multi-Party Threshold Cryptography FHE S5 / 2026-04-20 Deadline | [링크](https://csrc.nist.gov/projects/threshold-cryptography) | official | 2026 | [A] |
| <a id="ref-g-17"></a>G-17 | Apple ML Research — Combining Machine Learning and Homomorphic Encryption | [링크](https://machinelearning.apple.com/research/homomorphic-encryption) | official | 2024 | [A] |
| <a id="ref-g-18"></a>G-18 | Swift.org — Announcing Swift Homomorphic Encryption (iOS 18 PIR) | [링크](https://www.swift.org/blog/announcing-swift-homomorphic-encryption/) | official | 2024 | [A] |
| <a id="ref-g-19"></a>G-19 | Google Developers Blog — Expanding FHE Offering (Jaxite, HEIR) | [링크](https://developers.googleblog.com/en/expanding-our-fully-homomorphic-encryption-offering/) | official | 2025-11 | [A] |
| <a id="ref-g-20"></a>G-20 | Dialzara — Homomorphic Encryption Libraries Guide 2024-2025 (SEAL, HElib) | [링크](https://dialzara.com/blog/homomorphic-encryption-securing-ai-privacy) | blog | 2025 | [C] |
| <a id="ref-g-21"></a>G-21 | The Quantum Insider — Niobium Raises $23M+ for FHE Hardware | [링크](https://thequantuminsider.com/2025/12/03/niobium-23m-fhe-funding/) | news | 2025-12-03 | [B] |
| <a id="ref-g-22"></a>G-22 | Samsung SDS — Duality Technologies Convene Industry Leaders Privacy Standards | [링크](https://www.prnewswire.com/news-releases/samsung-sds-and-duality-technologies-convene-industry-leaders-to-advance-privacy-standards-301006434.html) | press | 2020 | [B] |
| <a id="ref-g-23"></a>G-23 | Samsung SDS — Homomorphic Encryption Technology Globally Recognized | [링크](https://www.samsungsds.com/us/news/Samsung-SDS-Homomorphic-Encryption-Technology-Globally-Recognized.html) | official | 2024 | [B] |
| <a id="ref-g-24"></a>G-24 | Securiti — South Korea AI Safe Use Guidance / PIPA Amendments 2025 | [링크](https://securiti.ai/south-korea-safe-use-of-personal-information-in-ai/) | analysis | 2025 | [B] |
| <a id="ref-g-25"></a>G-25 | Data Bridge Market Research — Fully Homomorphic Encryption Market Forecast 2032 | [링크](https://www.databridgemarketresearch.com/reports/global-fully-homomorphic-encryption-market) | report | 2024 | [C] |
| <a id="ref-g-26"></a>G-26 | eprint.iacr.org — CKKS Low-Latency Bootstrapping Using Roots of Unity (2025) | [링크](https://eprint.iacr.org/2025/651.pdf) | paper | 2025 | [A] |
| <a id="ref-g-27"></a>G-27 | NDSS 2026 — BKPIR: Keyword PIR for Private Boolean Retrieval (paper page) | [링크](https://www.ndss-symposium.org/ndss-paper/bkpir-keyword-pir-for-private-boolean-retrieval/) | paper | 2026-02-12 | [A] |
| <a id="ref-g-28"></a>G-28 | FHE.org 2026 Conference Taipei — 5th Annual FHE.org Conference | [링크](https://fhe.org/conferences/conference-2026/) | official | 2026-03-08 | [A] |
| <a id="ref-g-29"></a>G-29 | Investing.com — Beyond Theoretical: 5th-gen FHE scheme GL aims to make Private AI a reality | [링크](https://www.investing.com/news/company-news/beyond-theoretical-5thgen-fhe-scheme-aims-to-make-private-ai-a-reality-4548552) | news | 2026-03-08 | [B] |
| <a id="ref-g-30"></a>G-30 | Cornami — Post-Quantum Private LLM Whitepaper | [링크](https://cornami.com/wp-content/uploads/2025/09/Post-Quantum-Private-LLM-From-Cornami-and-Desilo.pdf) | whitepaper | 2025-09 | [B] |
| <a id="ref-g-31"></a>G-31 | New Electronics — Niobium Moves FHE Accelerator ASIC Closer to Production | [링크](https://www.newelectronics.co.uk/content/news/niobium-moves-fhe-accelerator-asic-closer-to-production) | news | 2026-02 | [B] |
| <a id="ref-g-32"></a>G-32 | Insight Korea — SKT·KT·LGU+ 양자로 철벽 보안 구축 | [링크](https://www.insightkorea.co.kr/news/articleView.html?idxno=242127) | news | 2025 | [B] |
| <a id="ref-g-33"></a>G-33 | eprint.iacr.org — Towards Lightweight CKKS: On Client Cost Efficiency (2025/720) | [링크](https://eprint.iacr.org/2025/720) | paper | 2025 | [A] |
| <a id="ref-g-34"></a>G-34 | Springer Nature — A Comparative Performance Analysis of FHE and ABE Schemes (2025) | [링크](https://www.nature.com/articles/s41598-025-19404-w) | paper | 2025 | [A] |
| <a id="ref-g-35"></a>G-35 | HEProfiler — In-Depth Profiler of Approximate HE Libraries (2025, Springer) | [링크](https://link.springer.com/article/10.1007/s13389-025-00377-5) | paper | 2025 | [A] |
| <a id="ref-n-01"></a>N-01 | Asia Business Daily — LG Uplus and Cryptolab Aim to Block Hacking Risks (MWC 2026) | [링크](https://www.asiae.co.kr/en/article/2026031008212144575) | news | 2026-03-10 | [B] |
| <a id="ref-n-02"></a>N-02 | SKT Newsroom — SKT QKD-PQC 하이브리드 양자암호 출시 | [링크](https://news.sktelecom.com/207758) | official | 2025 | [A] |
| <a id="ref-n-03"></a>N-03 | Global Economic — KT, 1조 투자 보안 청사진 (AI기반) | [링크](https://www.g-enews.com/article/ICT/2025/07/2025071511020968510b8d776efa_1) | news | 2025-07-15 | [B] |
| <a id="ref-e-01"></a>E-01 | CryptoLab CEO 전정희 + LGU+ CTO 장재현 — MWC 2026 발언 (ixi-O AICC 동형암호 PoC) | [링크](https://www.asiae.co.kr/en/article/2026031008212144575) | IR/발표 | 2026-03-10 | [A] |
| <a id="ref-e-02"></a>E-02 | DESILO PR Newswire — GL Scheme 5th Generation FHE Announcement | [링크](https://www.prnewswire.com/news-releases/desilo-and-fhe-inventor-craig-gentry-introduce-5th-generation-gl-fhe-scheme-for-private-ai-302707060.html) | press | 2026-03-08 | [B] |
| <a id="ref-e-03"></a>E-03 | Cornami & DESILO PR Newswire — Deployable FHE-Based LLM (AI Infra Summit 2025) | [링크](https://www.prnewswire.com/news-releases/cornami-and-desilo-bring-encrypted-ai-to-scale-with-deployable-fhe-based-llm-302557181.html) | press | 2025-09-16 | [B] |
| <a id="ref-e-04"></a>E-04 | SEMIFIVE PR Newswire — SEMIFIVE Partners with Niobium FHE Accelerator | [링크](https://www.prnewswire.com/news-releases/semifive-partners-with-niobium-to-develop-fhe-accelerator-driving-us-market-expansion-302692312.html) | press | 2026-02-19 | [B] |
| <a id="ref-e-05"></a>E-05 | Herald Korea — CryptoLab-LGU+ 협력 익시오 동형암호 보안 탑재 | [링크](https://biz.heraldcorp.com/article/10690901) | news | 2026-03 | [B] |
| <a id="ref-p-01"></a>P-01 | Aikata, Krieger, Roy (Graz Univ.) — Privacy at your Fingertips: Enabling Rapid Client-Side Operations in FHE (97% enc/dec 절감, 76× FPGA) | [링크](https://eprint.iacr.org/2026/515) | paper | 2026-03 | [A] |
| <a id="ref-p-02"></a>P-02 | IACR ePrint 2025/1935 — GL Scheme (Gentry-Lee) Technical Paper | [링크](https://eprint.iacr.org/2025/1935) | paper | 2025 | [A] |
| <a id="ref-p-03"></a>P-03 | HET-PIR Authors — Practical Keyword PIR via Novel Homomorphic Equality Test Algorithm (Springer Cybersecurity, 2026) | [링크](https://link.springer.com/article/10.1186/s42400-025-00506-x) | paper | 2026-01 | [A] |
| <a id="ref-p-04"></a>P-04 | Song et al. — BKPIR: Keyword PIR for Private Boolean Retrieval (NDSS 2026) | [링크](https://www.ndss-symposium.org/ndss-paper/bkpir-keyword-pir-for-private-boolean-retrieval/) | paper | 2026-02-12 | [A] |
| <a id="ref-p-05"></a>P-05 | MDPI Cryptography — Faster Spiral: Low-Communication High-Rate PIR (2025-02) | [링크](https://www.mdpi.com/2410-387X/9/1/13) | paper | 2025-02 | [A] |
| <a id="ref-p-06"></a>P-06 | eprint.iacr.org — Bridging Keyword PIR and Index PIR via MPHF (2025/2252) | [링크](https://eprint.iacr.org/2025/2252.pdf) | paper | 2025 | [A] |

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- Intel Heracles ASIC 1,074~5,547× 가속비 (IEEE Spectrum, Tom's Hardware 교차 확인)
- Apple iOS 18 Live Caller ID BFV PIR 실 배포 (Apple 공식 블로그)
- Niobium-SEMIFIVE 파트너십 KRW 10B 계약 (PR Newswire 공식 발표)
- LGU+-CryptoLab MWC 2026 PoC 공식 발표 (Asia Business Daily, Herald Korea 교차 확인)
- NIST Threshold Call 2026-04-20 마감 (NIST CSRC 공식)
- Aikata et al. 97% 절감 (IACR ePrint 2026/515, Graz 공식)
- HET-PIR 3.9ms / BKPIR 10× (Springer 저널, NDSS peer-reviewed)
- HomomorphicEncryption.org 9차 서울 (공식 사이트)
- Zama $1B 유니콘 (다수 출처 교차)

**추가 검증 필요 [C/D]:**
- 시장 규모 수치 전반: 기관별 CAGR 편차(8%~20%) — 정의 범위 차이 원인 불명
- CryptoLab CEO "실시간 레이턴시 없음" — 수치 미공개, 단일 인터뷰 발언
- GL 스킴 구체적 성능 수치 — 보도자료에 정량 벤치마크 없음, 기술 논문(IACR 2025/1935) 직접 검토 필요
- 한국 SOM 추정 ($7~15M) — 공개 데이터 없어 계산 기반 추정 ([D] 수준)
- On-Device(스마트폰) 엔드-투-엔드 키워드 검색 레이턴시 — 공개 벤치마크 없음

**데이터 공백:**
- SKT·KT의 동형암호 직접 추진 여부 — 공식 발표 미확인 (SKT는 QKD+PQC 집중)
- Intel Heracles 실제 출하 일정 및 가격 — 공개 정보 없음
- 스마트폰급 On-Device FHE 키워드 검색 실증 데이터 — 현재 공개 없음
- DESILO GL 스킴 CKKS 대비 정량 성능 비교 — 기술 논문 미공개 벤치마크
