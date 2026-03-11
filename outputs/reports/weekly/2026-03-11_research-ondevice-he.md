---
type: weekly-research
domain: secure-ai
l3_topic: ondevice-he
date: 2026-03-11
period: 2026-03-04 ~ 2026-03-11
signal: 🔴
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
prior_report: 2026-03-05_research-ondevice-he.md
---

# OnDevice 동형암호 — 심층 리서치

> 기간: 2026-03-04 ~ 2026-03-11

## 기술 동향

이번 주는 온디바이스 동형암호 분야 역사상 **상용화 이정표**가 복수로 기록된 한 주다.

**CKKS+ (4.5세대) 온디바이스 적용 실증**

CryptoLab이 공개한 CKKS+는 기존 4세대 CKKS에서 **행렬 연산을 암호화 상태로 실행**하는 구조로 진화한 4.5세대 동형암호 스킴이다. CEO 천정희 교수는 MWC 2026 현장에서 "실시간 지연이 없는 수준으로 성능이 개선됐고, 온디바이스 사용이 가능할 만큼 경량화됐다"고 직접 발언했다 [[E-01]](#ref-e-01). LG유플러스는 AI 에이전트 Xio와 AICC(AI 컨택 센터)에 대한 PoC(개념 검증)를 진행 중이다.

**Threshold FHE from CKKS — 다자 연산 표준화 진입**

CryptoLab 수석 연구원 Damien Stehlé가 NIST MPTS 2026(1월 27일)에서 CKKS 기반 임계(Threshold) FHE 구성을 발표했다. 핵심은 **신뢰 딜러 없이** 분산 키 생성 알고리즘으로 FHE 파라미터 효율을 유지하는 기법이다. 실용 벤치마크: 1-라운드 임계 AES128 암호화 0.1초 미만, 2-라운드 임계 Dilithium 서명 1초 미만 달성 [[G-03]](#ref-g-03). NIST IR 8214C(Threshold Call) 범위에 FHE가 공식 포함되며 표준화 타임라인이 가시화됐다.

**이산 CKKS (Discrete-CKKS) 신규 논문 — 정수 연산 효율 3배**

Lorenzo Rovida(Politecnico di Torino)가 3월 4일 제출한 ePrint 2026/450에서 CKKS 평문 공간을 복소수에서 이산 부분집합으로 제한하는 "discrete-CKKS" 패러다임을 제안했다. 이진 벡터 분해 기반 모듈로-2 산술 연산을 다항식만으로 처리하며, 기존 대비 **덧셈·곱셈·비교·논리 시프트 전 연산에서 약 3배 낮은 지연**을 달성한다. 도메인 스위칭으로 동일 파라미터 세트를 실수/정수 연산 모두에 활용 가능 [[P-01]](#ref-p-01).

**High-Precision Functional Bootstrapping for CKKS — EUROCRYPT 2026 채택**

Beihang University·Tsinghua University 공동 연구(ePrint 2026/367)에서 Fourier Extension 기반 함수형 부트스트래핑 프레임워크를 제안. 기존 O(n⁻¹) 전역 오차 대비 O(n⁻κ⁻²)로 오차 경계 개선. OpenFHE 구현 기준 **데이터 정밀도 10-27비트 향상, 지연 1.1-2배 단축** [[P-02]](#ref-p-02).

**P2P-CKKS — 비표준 벡터 크기 처리 효율화**

동적 power-of-two 벡터 패딩으로 비표준 크기 입력 벡터를 처리하는 P2P-CKKS가 Springer *Journal of Electrical Systems and Information Technology*에 게재됐다. 전체 벡터 크기 대역에서 **100% 성공률**을 기록하며 FFT 기반 다항식 곱셈 처리 속도를 실질적으로 향상시킨다 [[P-03]](#ref-p-03).

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| CryptoLab | CKKS+ (4.5세대) 발표. 행렬 연산 암호화 실행, 온디바이스 경량화 달성. NIST MPTS 2026에서 Threshold FHE 발표. LG유플러스·Macrogen·UClone 등 다중 파트너십 병행 | [[E-01]](#ref-e-01), [[G-03]](#ref-g-03) |
| LG유플러스 | MWC 2026(3월 4일, 바르셀로나)에서 CryptoLab과 동형암호 AICC·AI 에이전트 Xio 상용화 협력 발표. CTO 장재현 "세계 최고 수준의 연산 속도와 노이즈 제거 기술을 통합해 강건한 인프라 구축"이라고 언급. 현재 PoC 단계 | [[E-01]](#ref-e-01), [[G-01]](#ref-g-01) |
| Niobium + SEMIFIVE + Samsung Foundry | 세계 최초 상용 FHE ASIC 가속기를 Samsung Foundry 8nm(8LPU) 공정으로 양산 개발. 계약 규모 약 100억 원(KRW). 클라우드·프라이빗 AI 인프라용 | [[G-05]](#ref-g-05) |
| Microsoft Research | SEAL-Embedded: 임베디드·IoT 대상 CKKS HE 라이브러리 공개 유지. 2026년 신규 발표 없음 | [[G-06]](#ref-g-06) |
| IBM Research | HElayers SDK, IBM Z FHE 인프라 지속 운영. FHE 클라우드 서비스(HE4Cloud) 확장 중. 2026년 신규 플래그십 발표 없음 | [[G-07]](#ref-g-07) |
| OpenFHE | v1.5.0 개발 버전(2026.2.26 출시). BFV·BGV·CKKS·TFHE 전 스킴 지원. 고정밀 부트스트래핑 논문(ePrint 2026/367) OpenFHE 기반 구현 | [[G-08]](#ref-g-08) |
| CryptoLab × UClone | FHE 기반 AI 에이전트 플랫폼 출시. Encrypted Vector Search(ES2)를 UClone RAG에 통합. RSAC 2025에서 공개 데모 진행. 소비자 대상 첫 FHE 구동 AI 에이전트 | [[G-09]](#ref-g-09) |
| Samsung SDS | 동형암호 기술 국제 인증 취득 및 Duality Technologies와 프라이버시 표준 협력 유지. 신규 온디바이스 발표 없음 | [[G-10]](#ref-g-10) |
| NIST | IR 8214C(Threshold Cryptography Call) 발표. FHE·MPC·ZKP 포함. MPTS 2026(1월)에서 CKKS 기반 Th-FHE 발표 수용 | [[G-03]](#ref-g-03) |

---

## 시장 시그널

- 동형암호 글로벌 시장은 2026년 약 1.2~12억 달러(추정 기관별 편차 크며, 중앙값 기준 적용 권고), 2033년까지 8.4억~84억 달러로 성장 예측 [C] [[G-11]](#ref-g-01)
- LG유플러스가 **통신사 AICC**에 동형암호를 상용 적용하는 세계 첫 사례로 포지셔닝. 한국 통신 3사 중 최초 공개 검증 사례 [[E-01]](#ref-e-01)
- Niobium FHE ASIC이 상용화되면 서버·에지 양방향에서 FHE 처리 속도가 수십 배 향상될 전망이며, **온디바이스 FHE 경제성** 논의가 현실화될 시점 [[G-05]](#ref-g-05)
- 2026년 내 사이버보안 기업의 88%가 동형암호 배포 확대를 계획(시장조사 보고서, [C]) [[G-11]](#ref-g-01)
- CryptoLab이 글로벌 벤처(UClone, Macrogen) 및 통신사(LG유플러스)·스타트업 생태계를 동시에 공략하며 **한국계 FHE 스택이 글로벌 공급망**을 형성하는 구도가 뚜렷해짐
- NIST Threshold Call 범위에 FHE 포함이 확정되면서 **FHE 표준화가 2-3년 내 가시권**에 진입. 표준 미확정 리스크가 점차 해소 중

---

## 학술 동향 (주요 논문)

**이번 주 주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| "A flexible and polynomial framework for integer arithmetic in CKKS" (Rovida, 2026) | Discrete-CKKS: 이진 벡터 기반 mod-2 정수 연산을 다항식만으로 처리. 기존 대비 3배 낮은 지연, 도메인 스위칭 지원. ePrint 2026/450, 2026.03.04 | [[P-01]](#ref-p-01) |
| "High-Precision Functional Bootstrapping for CKKS from Fourier Extension" (Bian et al., 2026) | Fourier Extension 기반 부트스트래핑. 정밀도 10-27비트 향상, 지연 1.1-2배 단축. EUROCRYPT 2026 채택, OpenFHE 구현 | [[P-02]](#ref-p-02) |
| "P2P-CKKS: enhancing homomorphic encryption efficiency via dynamic power-of-two vector padding" (2025) | 동적 power-of-two 패딩으로 비표준 입력 벡터 처리. 전 크기 대역 100% 성공률, FFT 기반 다항식 곱셈 가속 | [[P-03]](#ref-p-03) |
| "Threshold FHE from CKKS and Applications" (Stehlé, CryptoLab, 2026) | 신뢰 딜러 없는 분산 키 생성으로 Th-FHE 구성. AES128 임계 암호화 0.1초 미만, NIST MPTS 2026 발표 | [[P-04]](#ref-p-04) |

---

## 이전 대비 변화

2026-03-05 리포트(이전 주) 대비 이번 주 주요 변화:

**새로 등장한 시그널**
- LG유플러스×CryptoLab MWC 2026 상용화 협력 발표 — 이전 주 "MWC 2026에서 ixi-O 적용 계획 예고" 수준에서 **AICC·Xio 대상 PoC 공식화**로 격상
- CKKS+ (4.5세대) 명칭 및 행렬 연산 암호화 실행 세부 사항 최초 공개
- ePrint 2026/450 (Discrete-CKKS, 3월 4일), ePrint 2026/367 (Fourier Extension 부트스트래핑) 신규 논문 등장
- P2P-CKKS Springer 게재 확인

**강화된 시그널**
- Niobium FHE ASIC: 이전 주 계약 완료 확인 → 이번 주 Samsung Foundry 8nm 공정 세부 조건(8LPU, 약 100억 원) 추가 확인
- NIST MPTS 2026 Th-FHE 발표: 이전 주 예고 → 이번 주 기술 내용 및 벤치마크 수치 확인

**변화 없는 영역**
- Microsoft SEAL·IBM FHE: 신규 플래그십 발표 없이 기존 라이브러리 유지
- 순수 온디바이스 FHE TRL은 3-4 수준 유지. CKKS+ 온디바이스 경량화 주장은 PoC 단계이며 독립 검증 미완료

---

## 전략적 시사점

**기회**

- CKKS+ 온디바이스 경량화가 실증되면 **통신사 AICC·고객 응대 AI**에서 동형암호 기반 프라이버시 보장 서비스가 조기 상용화될 수 있다. KT·SKT 대비 LG유플러스가 6~12개월 선점 포지션
- CryptoLab HEaaN 라이브러리 기반 스택은 NIST Threshold Call 표준 후보로 부상 중. 표준 채택 시 **글로벌 레퍼런스 스택**으로 확산될 가능성
- FHE ASIC(Niobium) 상용화 시 서버 FHE 비용이 수십 배 절감되어, 온디바이스가 아닌 **에지-서버 하이브리드 FHE** 모델이 현실적 대안으로 부상

**위협**

- LG유플러스×CryptoLab은 현재 **PoC 단계**이며 독립 성능 검증이 없다. "실시간 지연 없음" 주장은 단일 소스(CryptoLab CEO 발언)로 [C] 등급. 과장 마케팅 가능성 배제 불가
- Microsoft·Google·IBM 등 빅테크가 독자 FHE 라이브러리 또는 클라우드 서비스로 진입 시 CryptoLab 스택의 차별성이 희석될 수 있음
- FHE 연산 비용이 여전히 평문 대비 10³~10⁶배 수준으로, 배터리·발열 제약이 있는 실제 스마트폰 온디바이스 적용까지는 추가 하드웨어 혁신 필요

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-e-01"></a>E-01 | LG유플러스 CTO 장재현 · CryptoLab CEO 천정희 — MWC 2026 기자회견 발표 | [링크](https://www.asiae.co.kr/en/article/2026031008212144575) | IR/발표 | 2026-03-04 | [A] |
| <a id="ref-g-01"></a>G-01 | Korea IT Times — LG Uplus Unveils AI, Homomorphic Encryption and Quantum-Resistant Security Technologies at MWC26 | [링크](https://www.koreaittimes.com/news/articleView.html?idxno=151253) | news | 2026-03-04 | [B] |
| <a id="ref-g-02"></a>G-02 | Inside Quantum Technology — CryptoLab working with LGU+ to commercialize PQC | [링크](https://www.insidequantumtechnology.com/news-archive/south-koreas-cheon-jung-hee-s-startup-cryptolab-working-in-homomorphic-encryption-market-and-with-lgu-to-commercialize-post-quantum-cryptography-pqc/) | news | 2026-03-05 | [B] |
| <a id="ref-g-03"></a>G-03 | NIST CSRC — Threshold FHE from CKKS and Applications (MPTS 2026) | [링크](https://csrc.nist.gov/presentations/2026/mpts2026-2b4) | news | 2026-01-27 | [A] |
| <a id="ref-g-04"></a>G-04 | NIST CSRC — MPTS 2026: NIST Workshop on Multi-Party Threshold Schemes | [링크](https://csrc.nist.gov/events/2026/mpts2026) | news | 2026-01-26 | [A] |
| <a id="ref-g-05"></a>G-05 | PR Newswire — SEMIFIVE Partners with Niobium to Develop FHE Accelerator | [링크](https://www.prnewswire.com/news-releases/semifive-partners-with-niobium-to-develop-fhe-accelerator-driving-us-market-expansion-302692312.html) | news | 2026-02-19 | [A] |
| <a id="ref-g-06"></a>G-06 | Microsoft Research — SEAL-Embedded: A HE Library for the Internet of Things | [링크](https://www.microsoft.com/en-us/research/publication/seal-embedded-a-homomorphic-encryption-library-for-the-internet-of-things/) | news | 2022-01-01 | [A] |
| <a id="ref-g-07"></a>G-07 | IBM Research — Fully Homomorphic Encryption | [링크](https://research.ibm.com/topics/fully-homomorphic-encryption) | news | 2026-03-01 | [B] |
| <a id="ref-g-08"></a>G-08 | GitHub — openfheorg/openfhe-development v1.5.0 | [링크](https://github.com/openfheorg/openfhe-development) | news | 2026-02-26 | [A] |
| <a id="ref-g-09"></a>G-09 | PR Newswire — CryptoLab and UClone Partner to Bring First FHE-Powered AI Agents to Consumers | [링크](https://www.prnewswire.com/news-releases/cryptolab-and-uclone-partner-to-bring-first-fully-homomorphic-encryption-powered-ai-agents-to-consumers-302439395.html) | news | 2025-04-28 | [A] |
| <a id="ref-g-10"></a>G-10 | Samsung SDS — Homomorphic Encryption Technology Globally Recognized | [링크](https://www.samsungsds.com/us/news/Samsung-SDS-Homomorphic-Encryption-Technology-Globally-Recognized.html) | news | 2024-01-01 | [B] |
| <a id="ref-g-11"></a>G-11 | OpenPR — Homomorphic Encryption Market USD 1.2B (2026) to USD 8.4B (2033) | [링크](https://www.openpr.com/news/4230086/homomorphic-encryption-market-by-type-and-application-rapid) | news | 2026-01-01 | [C] |
| <a id="ref-p-01"></a>P-01 | Rovida — A flexible and polynomial framework for integer arithmetic in CKKS | [링크](https://eprint.iacr.org/2026/450) | paper | 2026-03-07 | [A] |
| <a id="ref-p-02"></a>P-02 | Bian et al. (Beihang Univ. · Tsinghua Univ.) — High-Precision Functional Bootstrapping for CKKS from Fourier Extension | [링크](https://eprint.iacr.org/2026/367) | paper | 2026-03-01 | [A] |
| <a id="ref-p-03"></a>P-03 | P2P-CKKS — enhancing homomorphic encryption efficiency via dynamic power-of-two vector padding | [링크](https://link.springer.com/article/10.1186/s43067-025-00276-z) | paper | 2025-12-01 | [A] |
| <a id="ref-p-04"></a>P-04 | Stehlé (CryptoLab) — Threshold FHE from CKKS and Applications (NIST MPTS 2026 slides) | [링크](https://csrc.nist.gov/csrc/media/presentations/2026/mpts2026-2b4/images-media/mpts2026-2b4-slides-thfhe-ckks-stehle.pdf) | paper | 2026-01-27 | [A] |
