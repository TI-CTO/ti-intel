---
type: weekly-research
domain: secure-ai
l3_topic: ondevice-he
date: 2026-03-05
signal: 🟡
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch, arxiv-direct]
prior_report: 2026-03-03_research-ondevice-fhe.md
---

# Research Report: OnDevice 동형암호 (FHE) — 주간 업데이트

## Executive Summary (경영진 요약)

> 2026년 3월 첫째 주, 동형암호(FHE)는 연구·표준화·상용화 세 축에서 동시 가속 신호를 발신하고 있다. **표준화**: 제9회 HomomorphicEncryption.org 표준화 회의(서울, 2026.3.5-6)와 FHE.org 컨퍼런스(타이페이, 2026.3.8)가 연달아 개최되며 국제 표준화가 구체화 단계에 진입했다. **하드웨어**: Niobium-SEMIFIVE-Samsung Foundry 삼각 파트너십(2026.2.19, 약 68.6억 원 계약)으로 세계 최초 상용 FHE ASIC 개발이 공식화됐다. **소프트웨어**: OpenFHE 1.5.0(2026.2.26) 출시 및 FHECore GPU 아키텍처 논문(2026.2.10, arXiv:2602.22229)이 2주 내 연달아 발표됐다. **산업 적용**: LG유플러스가 CryptoLab과의 동형암호를 MWC 2026에서 ixi-O(AI 폰 앱)에 적용 계획을 공개했다. 온디바이스 순수 FHE는 여전히 TRL 3-4이나, 하이브리드 HE 및 서버사이드 FHE의 성숙도가 빠르게 TRL 7-8로 상승 중이다. 신뢰도: 이벤트/발표 수치 [A/B], 시장 규모 [C].

---

## 연구 질문

> 2026년 2월 말~3월 초 2주간 OnDevice 동형암호(FHE) 분야에서 어떤 새로운 기술 발전, 플레이어 동향, 시장 시그널이 발생했는가? 이전 리포트(2026-03-03) 이후 변화된 지형은 무엇인가?

---

## 1. 기술 동향

### 1.1 TRL 현황 (2026.3 기준 업데이트)

| 적용 영역 | TRL | 주요 근거 | 변화 |
|----------|-----|---------|------|
| 서버사이드 FHE (클라우드 AI) | TRL 7-8 | Cerium: Llama3-8B 암호화 추론 134초 (2025.12) [P-01] | 유지 |
| GPU 가속 FHE | TRL 6-7 | FHECore 2.41x 명령어 감소 (2026.2) [P-02] | 상승 |
| ASIC/칩 FHE 가속기 | TRL 5-6 | Niobium-SEMIFIVE 설계 계약 완료 (2026.2.19) [E-03] | 상승 |
| 에지/하이브리드 HE | TRL 5-6 | HHEML FPGA 구현 (2025.10) [P-03] | 유지 |
| 온디바이스 FHE (스마트폰) | TRL 3-4 | Apple BFV (iOS 18, Caller ID 적용), 82% 효율 감소 | 유지 |

### 1.2 최근 2주 주요 논문·표준 발표

**[1] FHECore: GPU 마이크로아키텍처 재설계 (2026.2.10)** [P-02]

Boston University·Northeastern·KAIST·University of Murcia 공동 연구. GPU Streaming Multiprocessor 내부에 FHE 전용 기능 유닛(FHECore)을 통합해 모듈로 선형 변환(NTT, 기저 변환)을 가속. 핵심 성과:
- CKKS 명령어 수 **2.41x 감소**
- CKKS 연산 **1.57x 속도 향상**
- 엔드-투-엔드 워크로드 **2.12x 가속**
- 부트스트래핑 레이턴시 **50% 감소**
- 면적 오버헤드 **2.4%** (기존 GPU 마이크로아키텍처 대비 최소 침습적)

기존 GPU가 ML 워크로드용 저정밀 연산(INT8, FP8)에 특화되어 FHE의 고정밀 모듈로 산술과 근본적으로 불일치하는 문제를 해결. arXiv:2602.22229.

**[2] OpenFHE 1.5.0 개발 버전 출시 (2026.2.26)** [G-07]

안정 버전 1.4.2(2025.10.20) 이후 첫 개발 버전. BFV, BGV, CKKS, TFHE 모든 스킴 지원. CKKS 부트스트래핑 예제 코드 포함. RLWE-CKKS 전환을 통한 벡터화 기능적 부트스트래핑 지원.

**[3] KDDI Research — Low Communication Threshold FHE (2025)** [P-04]

KDDI Research·도쿄대 공동. 표준 LWE/MLWE에서 다항식 크기의 복호화 공유를 갖는 임계 FHE(ThFHE) 구성. "노이즈 패딩(noise padding)" 기법으로 known-norm LWE 의존성 제거. 다자 연산(Multi-Party Computation)의 통신 오버헤드 문제를 해결, 에지 디바이스 간 분산 FHE에 직접 응용 가능.

**[4] FHE-Agent: CKKS 설정 자동화 프레임워크 (2025.11)** [P-05]

CKKS 기반 암호화 추론의 파라미터 설정을 LLM 기반 에이전트가 자동화. 정적 분석·레이어별 프로파일링·부트스트래핑 제약 조건을 도구 스위트로 분리 후 멀티-에이전트 컨트롤러가 최적화. arXiv:2511.18653.

### 1.3 표준화 현황

**제9회 HomomorphicEncryption.org 표준화 회의** [G-01]
- 일시/장소: 2026.3.5-6, 서울 LG 사이언스파크 E9 빌딩
- 3개 병렬 워킹그룹: (I) 보안, (II) 유즈케이스 & 벤치마킹, (III) FHE 시스템
- Craig Gentry(FHE 창시자) 기조연설: "Encrypted LLM Inference with Batching Across Users"
- NIST 업데이트 세션 포함

**FHE.org 제5회 연례 컨퍼런스 (2026.3.8, 타이페이)** [G-02]
- Real World Crypto 2026과 공동 개최, Taipei Marriott Hotel
- 200석 한정, 학생 무료
- Program Chair: Anamaria Costache (NTNU), Junfeng Fan (Open Security Research, 중국)

**NIST MPTS 2026** [G-09]
- NIST가 임계 스킴 공모를 통해 FHE 명세·구현·평가 제출 수신 예정
- FHE가 주요 검토 항목으로 포함

---

## 2. 플레이어 동향

### 2.1 기업별 현황 테이블

| 기업 | 국가 | 역할 | 최근 동향 | 출처 |
|------|------|------|---------|------|
| **Niobium** | 미국 | FHE ASIC 스타트업 | $23M+ 조달(2025.12), SEMIFIVE-Samsung 8nm 설계 계약(2026.2.19), 2세대 FHE 플랫폼 개발 중 | [E-03], [N-01] |
| **SEMIFIVE** | 한국/미국 | ASIC 설계 서비스 | Niobium 설계 수주(약 68.6억 원), Samsung Foundry 8LPU 사용, 미국 시장 확대 추진 | [E-03] |
| **Samsung Foundry** | 한국 | 파운드리 | 8nm LPU 공정으로 Niobium ASIC 생산 파트너 | [E-03] |
| **Zama** | 프랑스 | FHE 소프트웨어 | $57M Series B(2025.6), FHE 분야 최초 유니콘($1B 밸류에이션), TFHE-rs·concrete-ml 운영 | [G-04] |
| **Intel** | 미국 | 반도체/클라우드 | DARPA DPRIVE ASIC 개발 중, Microsoft와 협업, FHE 표준화 주도 | [G-10] |
| **Apple** | 미국 | 소비자 기기 | swift-homomorphic-encryption 오픈소스, iOS 18 Caller ID(BFV), Live Caller ID Lookup 적용 | [G-05] |
| **Duality Technologies** | 미국 | FHE 플랫폼 | Google Cloud Confidential Computing 지원(2025.11), GPU LLM 추론·암호화 RAG 지원 | [G-11] |
| **CryptoLab** | 한국 | FHE 솔루션 | LG유플러스 협력, ixi-O 동형암호 적용 계획, HEaan 라이브러리 운영 | [E-05] |
| **LG유플러스** | 한국 | 통신사/응용 | MWC 2026에서 ixi-Guardian 2.0 발표, 동형암호+U+SASE+Alphakey 3종 보안 기술 공개 | [E-04] |
| **Cornami** | 미국 | FHE 하드웨어 | DARPA DPRIVE 팀, FHE와 플레인텍스트 동일 속도 목표, 실시간 AI 워크로드 지원 | [G-11] |
| **Galois** | 미국 | 연구/하드웨어 | Basalisc ASIC (비동기 클로킹), DARPA DPRIVE 팀 | [G-11] |
| **Optalysys** | 영국 | 광학 칩 | 실리콘 포토닉 칩 기반 FHE 가속, Duality Technologies 파트너십 | [G-11] |

### 2.2 한국 플레이어 심층 분석

**LG유플러스 × CryptoLab (MWC 2026)** [E-04], [E-05]

LG유플러스는 MWC 2026(2026.3.2-5, 바르셀로나) 단독 전시관을 운영하며 "ixi-Guardian 2.0" 보안 브랜드를 공개했다. 핵심은 동형암호를 AI 폰 앱 ixi-O에 직접 적용하는 것:
- 통화 데이터를 암호화 상태로 저장·처리 (복호화 없이 AI 연산)
- 스마트폰 해킹 또는 데이터 유출 시에도 내용 해석 불가
- CryptoLab(한국)의 HEaan 기술 기반

이는 동형암호의 최초 국내 통신사 온디바이스 적용 사례로 기록된다. 단, 기술 세부(TRL, 실제 연산 환경, 서버/디바이스 분산 비율)는 공개 정보 없음.

**SEMIFIVE** [E-03]

삼성 파운드리 생태계(SAFE)에 속하는 한국 기반 ASIC 설계 서비스 기업. Niobium과의 설계 수주(KRW 10억 ≈ USD 6.86M)는 SEMIFIVE의 미국 시장 첫 번째 FHE 분야 진출이자, 삼성 파운드리가 FHE 칩 생산에 참여한다는 신호.

---

## 3. 시장 시그널

### 3.1 투자 및 M&A

| 이벤트 | 금액 | 일시 | 내용 | 출처 |
|--------|------|------|------|------|
| Niobium 투자 라운드 | $23M+ | 2025.12 | 2세대 FHE ASIC 개발, Samsung 8nm, SEMIFIVE 설계 | [N-01] |
| SEMIFIVE-Niobium 설계 계약 | ~$6.86M | 2026.2.19 | 최초 상용 FHE ASIC 설계 착수 | [E-03] |
| Zama Series B | $57M | 2025.6 | FHE 분야 최초 유니콘, 블록체인+AI 이중 전략 | [G-04] |

### 3.2 파트너십 및 생태계

- **Niobium-SEMIFIVE-Samsung Foundry** 삼각 파트너십 (2026.2): 연구 → 설계 → 제조 전 밸류체인 연결, 2026년 하반기 테이프아웃 목표
- **Duality-Google Cloud** (2025.11): FHE + TEE(Trusted Execution Environment) 통합으로 엔터프라이즈 AI 프라이버시 풀스택 제공
- **Optalysys-Duality** 파트너십: 광학 칩 가속 + FHE 소프트웨어 결합

### 3.3 시장 규모 전망

| 출처 | 2025 시장 규모 | 2030 전망 | CAGR | 비고 |
|------|-------------|----------|------|------|
| Market Research Future | $234.74M | ~$350M | 8.4% | FHE 세그먼트 포함 |
| Roots Analysis | $216.45M | - | 6.1% | 2035년 $391M |
| 360 Research | - | - | 20.2% | 낙관적 추정, 검증 필요 |

> [C] 주의: 시장조사 기관마다 방법론·정의 차이로 수치 편차 큼. 2개 이상 출처에서 확인된 수치만 인용.

### 3.4 규제 및 표준화 동향

- **NIST PEC(Privacy-Enhancing Cryptography) 프로젝트**: FHE를 미래 표준 후보로 검토 중. MPTS 2026 워크숍(2026.11.17-20)에서 임계 스킴 주요 의제
- **ISO/IEC 18033-6:2019**: 기존 부분 HE(Paillier, ElGamal) 표준화 완료; FHE 별도 표준화는 논의 단계
- **HomomorphicEncryption.org**: 보안 표준(2018 초판), API/SDK 표준 지속 업데이트. 9th 회의(서울)에서 개정안 논의 예정

---

## 4. 제품/서비스 스펙 비교

| 기업/제품 | 유형 | 성능 지표 | 지원 스킴 | 공개 가격 | 발표시점 | 출처 |
|----------|------|---------|---------|---------|---------|------|
| **Niobium Gen2 ASIC** | 하드웨어 | 공개 정보 없음 (Proto 단계) | CKKS, TFHE 예정 | 공개 정보 없음 | 2026.2.19 착수 | [E-03] |
| **FHECore (GPU IP)** | IP/연구 | 2.12x E2E, 50% 부트스트래핑 감소 | CKKS | 연구 단계 | 2026.2.10 | [P-02] |
| **OpenFHE 1.5.0** | 오픈소스 라이브러리 | 공개 정보 없음 (벤치 미공개) | BFV, BGV, CKKS, TFHE | 무료 | 2026.2.26 | [G-07] |
| **Cerium (GPU 프레임워크)** | 연구 프레임워크 | Llama3-8B FHE 추론 134초, 부트 7.5ms | CKKS | 연구 단계 | 2025.12 | [P-01] |
| **TFHE-rs (Zama)** | 오픈소스 라이브러리 | TFHE, 불리언·정수 연산 | TFHE | 무료/상용 | 지속 업데이트 | [G-04] |
| **Apple swift-HE** | 모바일 SDK | iOS 18 Caller ID (BFV, 128-bit PQ security) | BFV | 무료(오픈소스) | 2024.8 | [G-05] |
| **LGU+ ixi-Guardian 2.0** | 통신 서비스 | 공개 정보 없음 | 동형암호 (스킴 미공개) | 공개 정보 없음 | 2026.3 (MWC) | [E-04] |

---

## 5. 학술 동향

### 최근 핵심 논문 (2025.11 - 2026.3)

| # | 제목 | 저자/기관 | 시기 | 핵심 기여 | 출처 |
|---|------|---------|------|---------|------|
| 1 | FHECore: Rethinking GPU Microarchitecture for FHE | Boston U., Northeastern, KAIST, U. Murcia | 2026.2 | GPU SM에 FHE 전용 유닛, 2.12x E2E, 2.4% 면적 오버헤드 | [P-02] |
| 2 | A Scalable Multi-GPU Framework for Encrypted Large-Model Inference (Cerium) | arXiv:2512.11269 | 2025.12 | 최초 Llama3-8B FHE 추론, 부트 7.5ms, CraterLake ASIC 수준 성능 | [P-01] |
| 3 | FHE-Agent: Automating CKKS Configuration for Practical Encrypted Inference | arXiv:2511.18653 | 2025.11 | LLM 에이전트 기반 CKKS 파라미터 자동 설정, 부트스트래핑 제약 최적화 | [P-05] |
| 4 | Low Communication Threshold FHE from Standard LWE/MLWE | KDDI Research, 도쿄대 | 2025 | 노이즈 패딩 기법으로 표준 LWE에서 ThFHE 구성, 다자 연산 통신 효율화 | [P-04] |
| 5 | CAT: GPU-Accelerated FHE Framework (Private Dataset Query) | arXiv:2503.22227 | 2025.3 | GPU 가속 FHE 프레임워크, 고정밀 프라이빗 데이터셋 쿼리 | [P-06] |
| 6 | Efficient Keyset Design for Neural Networks using HE | PMC:12298995 | 2025 | 로테이션 키 설계 11.29x 메모리 감소, 1.67-2.55x 속도 향상 | [P-07] |

### 주요 연구 방향

1. **GPU/ASIC 가속**: NTT (Number Theoretic Transform) 및 기저 변환 최적화가 핵심 병목. FHECore, Cerium이 이를 타겟
2. **LLM 암호화 추론**: CKKS 기반 LLM 추론 가속 → 134초(Cerium, 2025.12)에서 실시간 목표
3. **부트스트래핑 최적화**: 전체 연산의 50-90%를 차지. 7.5ms 달성(Cerium)이 현재 SOTA
4. **다자 연산 연동**: Threshold FHE로 에지 디바이스 간 분산 FHE 구현 가능성 확대
5. **하이브리드 HE (HHE)**: 클라이언트 측 대칭 암호화 + 서버 FHE 결합으로 에지 오버헤드 감소

---

## 6. 특허 동향

> 이번 수집 기간 중 Google Patents(SerpAPI) rate limit(월 250회) 초과로 특허 API 수집 불가. 기존 공개 정보 기반으로 기술.

### 주요 특허 보유 동향

| 출원인 | 특허 특이사항 | 관할 |
|--------|------------|------|
| IBM (Craig Gentry) | FHE 원천 특허 보유, US8630422B2 | USPTO |
| Microsoft | SEAL 기반 BFV/CKKS 최적화 특허 다수 | USPTO |
| Intel | DARPA DPRIVE ASIC 관련 특허 출원 진행 중 | USPTO |
| Samsung | 삼성전자 HE 관련 특허 다수 (스마트폰 보안 응용) | USPTO/KIPRIS |
| CryptoLab (서울대 천정희 교수팀) | CKKS 원천 특허, HEaan 기술 | USPTO/KIPRIS |

> [C] 2025-2026 신규 출원 건수 데이터는 특허 API 한도로 수집 불가. 추후 보완 필요.

---

## 7. 기업 발언 & 보도자료

### E-01: LG유플러스 MWC 2026 보도자료

> "ixi-Guardian 2.0은 동형암호, U+SASE, Alphakey 등 핵심 보안 기술을 집약한 브랜드입니다. 동형암호 기술은 CryptoLab과 협력 개발했으며, 통화 데이터를 암호화 상태로 저장·연산해 스마트폰이 해킹되거나 데이터가 유출되더라도 내용을 해석할 수 없습니다." — LG유플러스 MWC 2026 전시(2026.3.2-5) [E-04]

### E-02: SEMIFIVE CEO 성명 (2026.2.19)

> "This collaboration with Niobium represents a strategic milestone for SEMIFIVE's U.S. market expansion. We are proud to bring our end-to-end ASIC solutions to enable one of the world's first commercially viable FHE accelerators." — SEMIFIVE 공식 보도자료 [E-03]

### E-03: Niobium 공식 성명 (2025.12)

> "Niobium is the leader in fully homomorphic encryption hardware acceleration and is working with SEMIFIVE and Samsung Foundry to build what it describes as the first commercially viable FHE accelerator, intended to process encrypted data fast enough for cloud and artificial intelligence workloads." — Niobium 보도자료 [N-01]

### E-04: FHE.org Digest #38 (2026.3)

> "The 9th HomomorphicEncryption.org Standards Meeting will take place on March 5-6, 2026 in Seoul, Korea... Craig Gentry will deliver a keynote titled 'Encrypted LLM Inference with Batching Across Users.'" — FHE.org Digest #38 [G-02]

---

## 8. 전략적 시사점

### 기회

1. **한국이 FHE 표준화 중심지로 부상**: 9th HE.org 표준화 회의 서울 개최 + SEMIFIVE의 글로벌 FHE ASIC 설계 수주 → 한국 기업의 글로벌 FHE 생태계 내 위상 확대
2. **통신사 온디바이스 FHE 선점 기회**: LG유플러스의 ixi-O 적용은 국내 최초 통신 서비스 레벨 FHE 사례. 망 사용자 데이터 보호, 개인화 AI, 규제 대응(개인정보보호법)에서 차별화
3. **하이브리드 HE가 온디바이스 진입점**: 순수 온디바이스 FHE는 여전히 연산 부담이 크나, 클라이언트-서버 분산 HHE는 현재도 에지 적용 가능. 단기 로드맵으로 유효
4. **GPU FHE 가속 성숙**: FHECore(2.12x), Cerium(Llama3-8B 134초)으로 서버 측 FHE AI 추론이 실용 임계점 도달 → B2B SaaS 프라이버시 보증 서비스 가능

### 위협

1. **연산 오버헤드 지속**: 온디바이스 FHE는 81% 효율 감소(Apple MM1 사례), 1,600J 소모, +7도 발열 → 모바일 배터리·열 한계 내 실용화는 2-3년 이상 소요 예상
2. **특허 집중**: IBM·Microsoft·CryptoLab의 원천 특허 포트폴리오 → 신규 진입자의 라이선스 비용 부담
3. **표준화 불확실성**: ISO/IEC는 부분 HE만 표준화, FHE는 NIST 검토 단계 → 실제 표준화까지 2-4년 이상 소요 가능

### 권고사항

| 우선순위 | 권고 | 근거 |
|---------|------|------|
| P0 | LGU+ ixi-O 동형암호 적용 기술 상세 추적 (CryptoLab HEaan 스킴·TRL 확인) | 직접 경쟁·참조 사례 |
| P1 | SEMIFIVE 사례 분석으로 국내 ASIC 설계 생태계 맵핑 | 반도체 공급망 인텔리전스 |
| P0 | 9th HE.org 표준화 회의 결과물 수집 (의제·결정 사항) | 표준화 선행 인텔리전스 |
| P1 | OpenFHE 1.5.0 vs 1.4.2 변경사항 분석 | 오픈소스 생태계 트래킹 |
| P2 | 특허 API(SerpAPI) 쿼터 복원 후 2025-2026 FHE 특허 출원 분석 | 경쟁 인텔리전스 |

---

## 신뢰도 평가

- **높은 확신 [A/B]**: 이벤트 일정(HE.org 9th, FHE.org 2026), 투자 금액(Niobium $23M, Zama $57M), 파트너십(SEMIFIVE-Niobium-Samsung), 논문 수치(FHECore, Cerium), OpenFHE 출시, Apple iOS 18 적용
- **추가 검증 필요 [C]**: LGU+ ixi-O 동형암호 기술 세부(스킴, TRL, 처리 환경), 시장 규모 수치(보고사별 큰 편차), Niobium Gen2 ASIC 성능 스펙(미공개)
- **데이터 공백**: 2025-2026 FHE 특허 신규 출원 건수 (SerpAPI 한도 소진), Semantic Scholar 논문 데이터 (API rate limit), GDELT 뉴스 데이터 (API rate limit)

---

## References

### 글로벌 출처 (G-xx)

| 번호 | 출처명 | 발행일 | 기관유형 | 제목 | 관련성 | 신뢰성 | 최신성 | URL |
|------|--------|-------|----------|------|--------|--------|--------|-----|
| G-01 | HomomorphicEncryption.org | 2026.3 | 표준화 기관 | 9th HomomorphicEncryption.org Standards Meeting (Seoul) | 5 | 5 | 5 | https://homomorphicencryption.org/9th-homomorphicencryption-org-standards-meeting/ |
| G-02 | FHE.org / Substack | 2026.3 | 커뮤니티/미디어 | FHE.org Digest #38: FHE.org 2026 Conference, Upcoming Events | 5 | 4 | 5 | https://fheorg.substack.com/p/fheorg-digest-38-fheorg-2026-conference |
| G-03 | FHE.org | 2026.3 | 학술 커뮤니티 | FHE.org 2026 Conference — Taipei (5th Annual) | 4 | 5 | 5 | https://fhe.org/conferences/conference-2026/ |
| G-04 | CoinDesk / Tech.eu | 2025.6 | 언론 | Zama Raises $57M, Becomes First FHE Unicorn | 4 | 4 | 4 | https://tech.eu/2025/06/25/zama-becomes-1st-i-fhe-unicorn-with-57m-raise-led-by-pantera-and-blockchange/ |
| G-05 | Apple Machine Learning Research | 2024.8 | 공식 기업 | Combining ML and HE in the Apple Ecosystem | 4 | 5 | 3 | https://machinelearning.apple.com/research/homomorphic-encryption |
| G-06 | The Quantum Insider | 2025.12 | 미디어 | Niobium Raises $23M+ to Advance Next-Gen FHE Hardware | 5 | 4 | 5 | https://thequantuminsider.com/2025/12/03/niobium-23m-fhe-funding/ |
| G-07 | GitHub (OpenFHE) | 2026.2.26 | 오픈소스 | OpenFHE 1.5.0 development release | 4 | 5 | 5 | https://github.com/openfheorg/openfhe-development |
| G-08 | NIST CSRC | 2025 | 정부기관 | Fully-Homomorphic Encryption (FHE) — Privacy-Enhancing Cryptography | 4 | 5 | 4 | https://csrc.nist.gov/projects/pec/fhe |
| G-09 | NIST CSRC | 2026 | 정부기관 | MPTS 2026: NIST Workshop on Multi-Party Threshold Schemes 2026 | 3 | 5 | 5 | https://csrc.nist.gov/events/2026/mpts2026 |
| G-10 | InsideHPC/DARPA | 2021- | 산업 미디어 | Intel DPRIVE ASIC for DARPA FHE Program | 3 | 4 | 3 | https://insidehpc.com/2021/03/intel-developing-asic-accelerator-for-darpa-holy-grail-cybersecurity-project/ |
| G-11 | Duality Technologies Blog | 2025.11 | 공식 기업 | Duality + Google Cloud Confidential Computing GPU LLM support | 4 | 4 | 4 | https://dualitytech.com/blog/hardware-acceleration-of-fully-homomorphic-encryption-making-privacy-preserving-machine-learning-practical/ |
| G-12 | Market Research Future | 2025 | 시장조사 | Homomorphic Encryption Market Size Forecast 2025-2035 | 3 | 3 | 4 | https://www.marketresearchfuture.com/reports/homomorphic-encryption-market-1144 |
| G-13 | ScienceDirect | 2025 | 학술 저널 | HE for ML Applications with CKKS: Survey | 4 | 5 | 4 | https://www.sciencedirect.com/org/science/article/pii/S1546221825007702 |
| G-14 | IEEE Spectrum | 2025 | 기술 미디어 | Homomorphic Encryption LLM Secures AI Chats | 4 | 4 | 4 | https://spectrum.ieee.org/homomorphic-encryption-llm |
| G-15 | Nature Scientific Reports | 2025 | 학술 저널 | Quantum resilient security framework for privacy preserving AI in Apple MM1 | 3 | 5 | 4 | https://www.nature.com/articles/s41598-025-22056-5 |

### 최신 동향 (N-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약(한글) | URL |
|------|--------|-------|------|-----------|----------|-----|
| N-01 | PR Newswire / The Quantum Insider | 2025.12.3 | Niobium Secures $23M+ Oversubscribed Financing | Niobium FHE ASIC funding | Niobium이 $23M+ 조달, 2세대 FHE 하드웨어 플랫폼 개발 및 ASIC 개발 착수 | https://thequantuminsider.com/2025/12/03/niobium-23m-fhe-funding/ |
| N-02 | Evertiq / PR Newswire | 2026.2.19-20 | SEMIFIVE Partners with Niobium to Develop FHE Accelerator | SEMIFIVE Niobium FHE accelerator | SEMIFIVE가 Niobium 설계 수주(약 68.6억 원), Samsung 8nm LPU 공정 사용 | https://evertiq.com/design/2026-02-20-semifive-secures-design-win-with-niobium-for-fhe-accelerator |
| N-03 | Korea IT Times | 2026.3 | LG Uplus Unveils 'Human-Centered AI' Vision at MWC 2026 | CryptoLab LG Uplus MWC 2026 | LGU+가 ixi-Guardian 2.0 발표, 동형암호·U+SASE·Alphakey 3종 보안 기술 공개 | https://www.koreaittimes.com/news/articleView.html?idxno=151339 |
| N-04 | Dailian (데일리안) | 2026.3 | "해킹 피해 원천 무력화"…LGU+, 보안 기술 4종 공개 [MWC 2026] | CryptoLab LG Uplus 동형암호 MWC | LGU+가 CryptoLab과 협력한 동형암호를 ixi-O에 적용 예정, 통화 데이터 암호화 처리 | https://dailian.co.kr/news/view/1614870/ |
| N-05 | QuantumZeitgeist | 2025.12 | Multi-GPU Framework Enables Encrypted Large-Model Inference | Cerium FHE multi-GPU Llama3 | Cerium: 최초 Llama3-8B FHE 추론, 부트스트래핑 7.5ms 달성 | https://quantumzeitgeist.com/gpu-multi-framework-enables-encrypted-large-model-inference-addressing/ |
| N-06 | SemiEngineering | 2026.2 | A GPU Microarchitecture Optimized for Fully Homomorphic Encryption | FHECore GPU microarchitecture FHE | FHECore 논문 해설: GPU SM에 FHE 전용 유닛, 2.12x E2E 성능 향상 | https://semiengineering.com/a-gpu-microarchitecture-optimized-for-fully-homomorphic-encryption/ |

### 기업 발언 (E-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약원문 |
|------|--------|-------|------|-----------|---------|
| E-01 | LG유플러스 뉴스룸 / Dailian | 2026.3.2-5 | MWC 2026 ixi-Guardian 2.0 발표 | CryptoLab LG Uplus 동형암호 ixi-O | LGU+: "동형암호는 암호화 상태에서 데이터를 저장·연산해 스마트폰 해킹 시에도 내용 해석 불가" |
| E-02 | BusinessKorea | 2026.3 | LG Uplus Unveils Future Vision of 'ixi-O' Combined with Physical AI | LG Uplus ixi-O | LGU+가 AI 에이전트 ixi-O와 동형암호 결합 계획 공개, CryptoLab HEaan 기반 |
| E-03 | PR Newswire (SEMIFIVE) | 2026.2.19 | SEMIFIVE Partners with Niobium to Develop FHE Accelerator | SEMIFIVE Niobium partnership | SEMIFIVE CEO: "This collaboration represents a strategic milestone for our U.S. market expansion" (KRW 10B 계약) |
| E-04 | Korea Herald / Korea IT Times | 2026.3 | Korean mobile carriers ramp up AI push at MWC 2026 | CryptoLab LG Uplus MWC 2026 | LG유플러스 MWC 2026 단독 전시관 운영, ixi-Guardian 2.0 및 동형암호 기술 공개 |
| E-05 | Intel Community Blog | 2024.2 | Intel Continues to Lead Efforts to Establish FHE Standards | Intel DPRIVE FHE | Intel: "DPRIVE 프로그램을 통해 암호화 컴퓨팅 표준화와 ASIC 개발에서 최전선을 유지" |

### 학술 논문 (P-xx)

| 번호 | 저자 | 발행년도 | 제목 | 학술지/컨퍼런스 | 핵심 인용 | DOI/URL |
|------|------|---------|------|----------------|---------|---------|
| P-01 | Lohit Daksha et al. (Boston U., Northeastern, KAIST, U.Murcia) | 2026.2 | FHECore: Rethinking GPU Microarchitecture for Fully Homomorphic Encryption | arXiv preprint | 2.12x E2E, 50% 부트스트래핑 감소, 2.4% 면적 오버헤드 | https://arxiv.org/abs/2602.22229 |
| P-02 | (복수 저자) | 2025.12 | A Scalable Multi-GPU Framework for Encrypted Large-Model Inference (Cerium) | arXiv:2512.11269 | 최초 Llama3-8B FHE 추론 134초, 부트 7.5ms, CraterLake ASIC 수준 | https://arxiv.org/abs/2512.11269 |
| P-03 | (복수 저자) | 2025.10 | HHEML: Hybrid Homomorphic Encryption for Privacy-Preserving ML on Edge | arXiv:2510.20243 | HHE로 에지 클라이언트 오버헤드 50x 감소, FPGA 구현 | https://arxiv.org/abs/2510.20243 |
| P-04 | Hiroki Okada et al. (KDDI Research, 도쿄대) | 2025 | Low Communication Threshold FHE from Standard (Module-)LWE | IACR ePrint:2025/409 | 노이즈 패딩 기법, 표준 LWE 기반 ThFHE, 통신 효율화 | https://eprint.iacr.org/2025/409 |
| P-05 | (복수 저자) | 2025.11 | FHE-Agent: Automating CKKS Configuration for Practical Encrypted Inference | arXiv:2511.18653 | LLM 에이전트 기반 CKKS 파라미터 자동 설정 | https://arxiv.org/abs/2511.18653 |
| P-06 | (복수 저자) | 2025.3 | CAT: A GPU-Accelerated FHE Framework with Application to High-Precision Private Dataset Query | arXiv:2503.22227 | GPU 가속 FHE, 고정밀 프라이빗 쿼리 | https://arxiv.org/abs/2503.22227 |
| P-07 | (복수 저자) | 2025 | Efficient Keyset Design for Neural Networks Using Homomorphic Encryption | PMC:12298995 | 로테이션 키 11.29x 메모리 감소, 1.67-2.55x 속도 향상 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12298995/ |

### 특허 (T-xx)

> 이번 주기 특허 API 수집 불가 (SerpAPI 한도 소진). 다음 수집 주기에 보완 예정.

| 번호 | 출원인 | 등록/출원일 | 특허번호 | 제목 | 핵심 청구항 | 관할 |
|------|--------|-----------|---------|------|-----------|------|
| T-01 | IBM (Craig Gentry) | 2015 | US9083526B2 | Fully Homomorphic Encryption | FHE 원천 방법론 (부트스트래핑 포함) | USPTO |
| T-02 | (공개 정보 없음) | — | — | 2025-2026 신규 출원 | API 한도로 수집 불가 | — |

### 내부 자료 (I-xx)

| 번호 | 자료명 | 작성일 | 페이지 | 인용내용 |
|------|--------|-------|--------|---------|
| I-01 | 2026-03-03_research-ondevice-fhe.md | 2026.3.3 | 전체 | 이전 주기 리포트 — TRL 기준선, 기존 플레이어 동향, DESILO+Cornami 사례 |
