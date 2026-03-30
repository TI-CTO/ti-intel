---
type: wtis-research
topic: 양자/동형 암호
domain: secure-ai
l2_topic: he-keyword-search
date: 2026-03-30
agent: research-deep
confidence: high
status: completed
prior_report: 2026-03-18_wtis-he-keyword-search.md
sources_used: [websearch, prior-reports, weekly-deep]
---

# WTIS 심층 리서치: 양자/동형 암호 (2026-03-30)

> 이전 판정(2026-03-18): Conditional Go, 125/200, Borrow(CryptoLab)+Build(AICC)+Watch(HW/GL)
> 분석 범위: PQC(양자내성암호), FHE(완전 동형암호) 키워드 검색, Secure Vector Search (3개 L3)
> 이전 대비 주요 변화: Google 2029 데드라인·Android 17 ML-DSA(3/25~26), "Privacy at your Fingertips" 클라이언트 97% 경량화(EuroS&P 2026), Zama+T-REX $32B RWA 기관 실도입(3/26), CryptoLab HEaaN Zero-Leak RAG GS 1등급 획득(3/26~27)

---

## 이전 분석 대비 변화 요약

| 항목 | 이전 (2026-03-18) | 현재 (2026-03-30) | 변화 |
|------|-------------------|-------------------|------|
| **FHE TRL** | 3~4 (서버 사이드 ASIC 발표) | 3~4 → **4 임박** (클라이언트 97% 경량화 검증 + 기관 실도입) | ↑ 조건 단축 |
| **PQC 마이그레이션 데드라인** | NIST 2030 / NSA 2033 기준 | Google **2029** 독자 선언 (업계 기준점 조기화) | ↑ 압박 강화 |
| **On-Device PQC** | Android 계획 단계 | Android 17 **ML-DSA 네이티브 탑재** 공식 발표 | ↑ 플랫폼 지원 현실화 |
| **FHE 클라이언트 오버헤드** | 97% 감소 논문 공개(ePrint) | EuroS&P 2026 **피어리뷰 확정** + CAT GPU 33× | ↑ 신뢰도 [A]로 상향 |
| **FHE 실도입 규모** | T-REX RWA 발표 전 | Zama+T-REX $32B 자산에 기관 FHE 인프라 **공식 출시** | 신규 |
| **국내 제품 인증** | CryptoLab PoC 단계 | HEaaN Zero-Leak RAG **TTA GS 1등급** (3/26) | ↑ 상용화 단계 진입 |
| **Secure Vector Search** | CryptoLab ES2 발표 수준 | GS 인증 후 **공공 조달 등록 계획** (6월 예정) | ↑ 조달 경로 확보 |
| **통신사 경쟁 구도** | LGU+만 PoC | LGU+ PoC 지속 + KT QENC 공공 배포 준비 | ↑ 경쟁 개시 |
| **글로벌 PQC 규제** | CISA 조달 가이드 | **NSA CNSA 2.0** 2027-01 신규 시스템 의무화 [[G-18]](#ref-g-18) | ↑ 규제 현실화 |

> **핵심 판정 변화 방향**: PQC는 "준비 → 실행" 전환 압박이 Google 2029 데드라인으로 가속. FHE는 서버 사이드 가속(Intel Heracles)에 이어 클라이언트 사이드 97% 경량화가 피어리뷰로 확정되며 TRL 4 도달 조건이 단축됨. Conditional Go 판정은 **유지**되나, 실행 긴박도가 이전 대비 상향 조정이 필요함.

---

## 1. PQC (양자내성암호) 동향

### 기술 현황

**NIST 표준 및 플랫폼 지원 현황**

- Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM, FIPS 203), Module-Lattice-Based Digital Signature Algorithm (ML-DSA, FIPS 204), Stateless Hash-Based Digital Signature Standard (SLH-DSA, FIPS 205) 3종이 2024년 8월 확정, 연방 사용 승인 발효 [[G-03]](#ref-g-03)
- Android 17: ML-DSA-65·ML-DSA-87 KeyPairGenerator API 네이티브 지원, Android Verified Boot(AVB), Remote Attestation, Google Play 앱 서명(Classical+PQC 하이브리드)까지 4계층 통합 [[G-04]](#ref-g-04), [[E-01]](#ref-e-01)
- ML-DSA 서명 크기 ~3,293 bytes — Elliptic Curve Digital Signature Algorithm(ECDSA) ~64 bytes 대비 51배. 보안 격리(TrustZone)에서 처리, 사용자 경험 영향 미미 [[E-01]](#ref-e-01)
- 실시간 보이스 통신 프로토콜에서 ML-DSA 직접 적용 시 **대역폭 최대 100배 증가** 문제 IBM·Signal·Threema 공동 연구로 정량화 [[G-06]](#ref-g-06), [[E-03]](#ref-e-03)

**5G 통신망 PQC 적용 현황**

- SKT+Thales: CRYSTALS-Kyber 기반 5G Standalone(SA) 실 상용 환경 PQC SIM 테스트 완료 [[G-07]](#ref-g-07), [[E-04]](#ref-e-04)
- Thales Over-the-Air(OTA) 업그레이드: 기기 교체 없이 SIM/eSIM에 PQC 소급 적용 경로 확립 [[G-07]](#ref-g-07)
- PQShield PQMicroLib-Core: 5KB RAM 임베디드 PQC 구현, Embedded World 2026(3/10) 발표. TLS 지원 포함 [[G-09]](#ref-g-09)
- 3GPP Release 20/21: PQC를 5G 라이프사이클 내 단계적 도입, 6G는 기본 탑재 목표 [[G-10]](#ref-g-10)

**핵심 병목 — PQC 메시징 대역폭 문제**

IBM Research가 Real-World Crypto 2026에서 Signal·Threema와 공동 발표한 연구에 따르면, 기존 Signal 그룹 프로토콜을 ML-DSA로 직접 교체 시 대역폭 100배 증가가 발생한다. IBM은 서버 측 암호화 그룹 데이터 저장+멤버 검증 분산 방식으로 해결을 제안했다 [[G-06]](#ref-g-06), [[E-03]](#ref-e-03). 보이스 암호화 프로토콜 설계 시 이 수치가 직접 참조 가능한 정량 근거다.

### 플레이어 동향

**PQC 주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| Google | 2026-03-25: 2029 PQC 마이그레이션 데드라인 독자 선언(NIST 2030보다 1년 앞당김). 2026-03-26: Android 17 ML-DSA 4계층 통합 공식 발표 | [[G-01]](#ref-g-01), [[E-01]](#ref-e-01) |
| IBM | Real-World Crypto 2026: Signal·Threema와 PQC 그룹 메시징 재설계 발표. ML-DSA 직접 적용 시 대역폭 100배 증가 문제 정량화 후 서버 분산 검증 방식 제안 | [[G-06]](#ref-g-06), [[E-03]](#ref-e-03) |
| SKT | QKD+PQC 하이브리드 장비 출시(2024-10, 세계 최초). Thales와 5G SA 망 CRYSTALS-Kyber SIM 테스트 협력. NIST FIPS 203/204 준수 자체 소프트웨어 통합 | [[G-07]](#ref-g-07), [[E-04]](#ref-e-04) |
| KT | PQC 솔루션 탑재 QENC 장비 보안기능확인 시험 완료(2024-05). 2026년부터 공공기관 대상 QKD+PQC 하이브리드 망 구축 추진. MWC 2026에서 6G 핵심 기술로 '퀀텀 세이프 보안' 제시 | [[G-11]](#ref-g-11), [[G-12]](#ref-g-12) |
| LGU+ | PQC 기반 네트워크·전자서명 기술 상용화 발표. 공공기관·금융 파일럿 착수 계획. AICC에 동형암호 탑재 PoC 병행 | [[G-13]](#ref-g-13) |
| PQShield | PQMicroLib-Core(5KB RAM, TLS 포함) 임베디드 PQC 라이브러리 출시(Embedded World 2026, 3/10). 100편 연구 논문 달성 | [[G-09]](#ref-g-09) |
| QuSecure | SEC 제출 PQFIF에서 PQC 금융 레퍼런스로 공식 인용(3/19). AFWERX $3.9M·MDA SHIELD 계약 수주 | [[G-08]](#ref-g-08) |

### 시장 시그널

- 2026년은 Pure PQC보다 Classical+PQC 하이브리드 접근법이 지배 전망 [[G-15]](#ref-g-15)
- 기업의 14% 만이 양자 취약 시스템 전수 조사 완료 — 중소기업 5~7년, 대기업 12~15년+ 마이그레이션 소요 예상 [[G-16]](#ref-g-16) [추가확인 필요]
- NSA CNSA 2.0: 신규 시스템에 대해 2027-01 PQC 의무화 발효 예정 [[G-18]](#ref-g-18)
- CISA 조달 가이드(2026-01-23): 클라우드·협업 도구·엔드포인트 보안 1군(즉시 PQC 구매 의무). 통신 장비·OS·스토리지·Identity and Access Management(IAM)는 2군(전환 진행 중) [[G-17]](#ref-g-17)

### 통신사 적용 시사점

**기회**

- Android 17 ML-DSA Keystore API: 통신사·단말 앱이 별도 Hardware Security Module(HSM) 없이 스마트폰 TrustZone에서 PQC 키 격리 보관 가능 → 스마트폰 보안 앱·VoIP 단말 즉시 적용 경로
- Thales OTA PQC 업그레이드: 수십억 개 기존 5G SIM에 디바이스 교체 없이 PQC 소급 적용. SKT 선발 협력, KT·LGU+ 추격 경쟁 개시

**위협**

- PQC 메시징 대역폭 100배 증가: 실시간 VoIP 인프라(Session Initiation Protocol/Real-time Transport Protocol 스택) PQC 전환 시 Quality of Service(QoS) 저하 위험
- Google 2029 데드라인 선언으로 공급망 전체에 조기화 압력 — 통신사가 2030 기준 로드맵 설정 시 고객·파트너 조기화 요구 직면 가능

---

## 2. 동형암호 (FHE) 키워드 검색 동향

### 기술 현황 (TRL 업데이트)

**이전 판정(3/18): TRL 3~4 → 현재 재평가: TRL 3~4 (4 도달 조건 단축)**

이번 주 추가 근거:

1. **"Privacy at your Fingertips" EuroS&P 2026 피어리뷰 확정** (이전: ePrint 공개 상태): Aikata, Krieger, Sinha Roy의 "Boosted-Deflation" 기법이 Fully Homomorphic Encryption(FHE) 클라이언트 측 enc/dec 오버헤드 97% 감소를 IEEE EuroS&P 2026에서 피어리뷰 확정. 이전 분석의 [A] 신뢰도 평가가 학회 검증으로 강화됨 [[P-01]](#ref-p-01)

2. **CAT GPU 가속 프레임워크 arXiv 공개(3/28)**: CKKS, BFV, BGV 통합 지원. Nvidia RTX 4090에서 CPU 대비 최대 2,173×, CKKS 기반 Private Information Retrieval(PIR) 쿼리 33×, 1초 내 10³행 쿼리 가능 [[P-02]](#ref-p-02)

3. **Intel Heracles 기술 사양 추가 확산**: 암호화 유권자 데이터베이스 익명 쿼리 14μs(vs Xeon 15ms, 1,071×). BGV·BFV·CKKS 다중 FHE 스킴 지원. PCIe 가속기 카드 형태 서버 병치 운용 [[G-20]](#ref-g-20), [[E-05]](#ref-e-05)

TRL 4 도달 조건(여전히 미충족): On-Device(스마트폰급) 엔드-투-엔드 키워드 검색 지연시간 ≤150ms (ITU-T G.114 기준) 공개 검증

**성능 벤치마크 업데이트**

| 솔루션 | 주요 수치 | 상태 | 출처 |
|--------|-----------|------|------|
| Intel Heracles ASIC | 1,071~5,547× vs Xeon, 14μs 쿼리(DB 익명), 1.2GHz, 197mm², 48GB HBM | 발표 완료(ISSCC). 양산 미정 | [[G-20]](#ref-g-20), [[E-05]](#ref-e-05) |
| CAT (arXiv 2503.22227) | CPU 대비 2,173×, CKKS PIR 33×, 1초/10³행 | arXiv 공개(3/28) [A] | [[P-02]](#ref-p-02) |
| Aikata et al. "Privacy at your Fingertips" | enc/dec 97% 감소, 76× FPGA | EuroS&P 2026 피어리뷰 확정 [A] | [[P-01]](#ref-p-01) |
| HET-PIR (Springer 2026) | 3.9ms/32비트 비교, 0.01ms/건 (배치) | 피어리뷰 [A] | [[P-03]](#ref-p-03) |
| FHECore (arXiv 2602.22229) | CKKS 연산 2.41× 명령어 감소, 부트스트래핑 50% 감소 | arXiv [A] | [[P-04]](#ref-p-04) |
| CryptoLab HEaaN GPU | 100×+ 가속 (단일 스레드 대비) | 상용 배포 중 | [[E-06]](#ref-e-06) |

### 플레이어 동향

**FHE 주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| Intel | Heracles ASIC(Intel 3 공정, 48GB HBM3): 1,074~5,547× 가속. 암호화 DB 쿼리 14μs 실증. PCIe 카드 형태. 양산 일정 미발표. DARPA DRIVE 프로그램 기원 | [[G-20]](#ref-g-20), [[E-05]](#ref-e-05) |
| Zama | T-REX Network와 FHE 기반 기관급 기밀 인프라 출시(3/26). ERC-3643 표준 $32B 토큰화 자산에 FHE 기밀성 레이어 통합. Apple·AWS·Google FHE.org 후원 확보. 유니콘($1B+ 밸류에이션) | [[G-22]](#ref-g-22), [[E-07]](#ref-e-07) |
| CryptoLab | HEaaN Zero-Leak RAG TTA GS 1등급 획득(3/26). LGU+ ixi-O AICC 동형암호 PoC 진행 중. UClone과 Encrypted Vector Search(ES2) RAG 통합. 공공 조달 등록 6월 계획, CC 인증(EAL2) 9월 목표 | [[G-14]](#ref-g-14), [[E-06]](#ref-e-06) |
| Niobium + SemiFive | Samsung Foundry 8nm 공정 FHE ASIC 개발 진행(2/19 KRW 10B 계약). 세계 최초 상용 FHE 가속기 목표. 설계 단계 | [[G-21]](#ref-g-21) |
| LGU+ | MWC 2026에서 CryptoLab과 ixi-O AICC 동형암호 탑재 PoC 공식화. 상용화 시점 미발표 | [[G-13]](#ref-g-13), [[E-06]](#ref-e-06) |

### 시장 시그널

- FHE 스타트업 8개사 누적 투자 $2억 7,890만(평균 사당 $3,490만, 2026-03-24 기준) [[G-23]](#ref-g-23) [추가확인 필요]
- Zama 유니콘 달성($1B+ 밸류에이션), Series A+B 합산 $1.5억+ — FHE 단일 기업 최고 밸류에이션 [[G-22]](#ref-g-22)
- FHE 글로벌 시장: $251~310M(2026) → $1,319M(2035), Compound Annual Growth Rate(CAGR) 20.2% 전망 [[G-25]](#ref-g-25) [추가확인 필요]
- Zama+T-REX: $32B 실물 자산(Real World Asset, RWA) 기관 인프라에 FHE 최초 실 운용 규모 통합(3/26) [[G-22]](#ref-g-22), [[E-07]](#ref-e-07)
- FHE.org 2026 컨퍼런스(타이페이, 3/8): Apple·AWS·Google 후원 진입 — 빅테크 FHE 생태계 진입 신호 [[G-24]](#ref-g-24)

### 통신사 적용 시사점

**기회**

- CryptoLab HEaaN Zero-Leak RAG GS 1등급 획득으로 공공 조달 경로 열림 → 통신사 공공 사업 참여 시 기성 인증 솔루션 Borrow 즉시 가능
- CAT GPU 33× 가속 + Aikata 97% 클라이언트 경량화 결합 시, AICC 서버-클라이언트 구조에서 On-Device FHE 키워드 검색 실용성 임계점 접근
- LGU+ PoC 성공 시 SKT·KT에 암호화 AICC 도입 압박 확산 — 2026년 하반기 경쟁 개시 가능성

**위협**

- Intel Heracles 양산 일정 불확실: PCIe 카드 양산 전까지 소프트웨어 FHE 키워드 검색의 지연 문제 지속
- Apple·AWS·Google의 FHE.org 후원 진입 → 자체 클라우드 통합 FHE 검색 서비스 선점 시 국내 솔루션 시장 잠식 가능
- 소비자급 저전력 GPU(Jetson Nano 등) FHE 연산 부적합 판정 — On-Device 적용 범위 상위 티어 스마트폰으로 제한될 가능성

---

## 3. Secure Vector Search 동향

### 기술 현황

Secure Vector Search는 벡터 임베딩(고차원 유사도 벡터)을 암호화 상태 그대로 유사도 검색하는 기술로, Retrieval-Augmented Generation(RAG) AI 파이프라인의 프라이버시 보호에 직접 적용된다. 동형암호 기반 Approximate k-Nearest Neighbor(ANN) 검색이 핵심이다.

**주요 기술 개발 현황**

- **CryptoLab ES2(Encrypted Vector Search)**: HEaaN CKKS 기반. UClone AI 에이전트 플랫폼과 통합(2025-04 파트너십 발표). RAG 파이프라인에서 쿼리 벡터·문서 벡터 모두 암호화 상태에서 내적(inner product) 유사도 연산. 2026-03-26 HEaaN Zero-Leak RAG로 TTA GS 1등급 획득 [[G-14]](#ref-g-14), [[E-06]](#ref-e-06)

- **Panther(IACR ePrint 2024/1774)**: Private Approximate Nearest Neighbor Search(ANNS) 전용 프로토콜. 1,000만 점 데이터셋에서 ANNS 쿼리 18초, 284 MB 통신 오버헤드 [[G-26]](#ref-g-26)

- **CKKS 기반 FPGA k-Nearest Neighbor(k-NN)**: 암호화 데이터 k-NN 연산 41.72ms — 평문 k-NN(0.518ms) 대비 80배 느림. 1백만 포인트 이상 스케일 시 현실적 병목 [[G-27]](#ref-g-27)

- **Additive Homomorphic Encryption(AHE) 접근**: CKKS 대신 부분 동형암호(덧셈·스칼라 곱만 지원)로 내적 유사도 연산 — 완전 FHE 대비 오버헤드 10~100× 낮으나 쿼리 확장 불가 [[G-28]](#ref-g-28)

- **HEaaN Zero-Leak RAG 아키텍처**: 벡터 DB를 최초부터 동형암호로 암호화, 암호문 상태에서 유사도 검색 수행. 복호화 없이 검색→추론 전 과정 암호화 유지 [[G-14]](#ref-g-14)

**현재 성능 한계(공개 데이터 기준)**

| 시나리오 | 지연시간 | 비고 |
|----------|----------|------|
| Panther(10M 포인트 ANNS) | 18초 | 전용 프로토콜 |
| CKKS k-NN(FPGA, 평문 대비) | 80× 느림 | 공개 벤치마크 |
| CAT CKKS DB 쿼리(10³행) | <1초 | GPU(RTX 4090) 기준 |
| HEaaN Zero-Leak RAG | 공개 정보 없음 | GS 인증 시 성능 기준 미공개 |

### 통신사 적용 시사점

**기회**

- CryptoLab HEaaN Zero-Leak RAG GS 1등급: 통신사가 공공기관 AI 보안 프로젝트 입찰 시 즉시 활용 가능한 인증 솔루션. KT·SKT는 자체 개발 없이 Borrow(CryptoLab) 전략으로 공공 조달 선점 가능
- AICC·개인화 추천 AI 파이프라인: 고객 개인정보(상담 이력, 통화 내용)를 암호화 상태에서 RAG 검색 — AI기본법 고위험 AI 분류 대응 가능
- RAG 보안 시장 성장: Enterprise RAG 배포 확산 + 개인정보 보호 규제 강화 → 암호화 벡터 DB 수요 증가 예상

**위협**

- 성능 병목: 대규모(100만+ 건) 벡터 DB에서 FHE ANN 검색은 현재 초 단위 지연. 실시간 추천·검색에는 부적합 (배치 처리·비실시간 유스케이스가 현실적)
- TEE 대체재: Intel SGX, AMD SEV 기반 Trusted Execution Environment(TEE)는 유사한 보안 보증을 10~100× 낮은 오버헤드로 제공 — 단기 대체재로 채택 가능성 존재

---

## 4. 경쟁사 동향 (SKT/KT)

### SKT

- **QKD+PQC 하이브리드**: 2024-10 세계 최초 출시. IDQ Solteris Key Management System(KMS) 기반. NIST FIPS 203/204 준수 자체 PQC 소프트웨어 통합 [[G-07]](#ref-g-07)
- **Thales 5G PQC SIM 협력**: CRYSTALS-Kyber 기반 SIM을 5G SA 실 상용 환경에서 테스트 완료. OTA 업그레이드 경로 확보 [[G-07]](#ref-g-07), [[E-04]](#ref-e-04)
- **동형암호**: 공식 추진 발표 없음. FHE 관련 공개 파트너십·특허 부재 [추가확인 필요]
- **포지션**: PQC 선도(국내 1위) — FHE는 미추진 → KT 추격·LGU+ 선행 가능성

### KT

- **QENC 장비**: PQC 솔루션(CRYSTALS-Dilithium, CRYSTALS-Kyber 적용) 탑재 자체 개발 양자암호화 통신 장비. 보안기능확인 시험 완료(2024-05) [[G-11]](#ref-g-11)
- **QKD+PQC 하이브리드 망**: 초당 30만 개 암호키 생성 QKD 장비 개발. 2026년부터 공공기관 대상 하이브리드 양자보안망 구축 착수 계획 [[G-11]](#ref-g-11), [[G-12]](#ref-g-12)
- **MWC 2026**: 6G 핵심 기술로 '퀀텀 세이프 보안' 제시. QKD·AI 침해탐지·동형암호 결합 계획 언급(구체적 일정 미발표) [[G-12]](#ref-g-12)
- **2025 해킹 사고 후속**: 5년간 1조 원 정보보호 투자 발표. AI 기반 보안 청사진 제시
- **포지션**: PQC 독자 장비 확보, 공공 조달 준비 완료 — FHE는 계획 언급 수준. SKT와 격차 없음에 가까움

### LGU+

- AICC·ixi-O에 CryptoLab CKKS+ 동형암호 탑재 Proof of Concept(PoC) — 국내 통신사 최초 FHE AICC 공식화 [[G-13]](#ref-g-13), [[E-06]](#ref-e-06)
- PQC 기반 네트워크·전자서명 기술 상용화 발표. 공공기관·금융 파일럿 착수 계획 [[G-13]](#ref-g-13)
- **포지션**: FHE 실행 선두(통신사 유일 PoC). PQC는 SKT·KT 대비 후발 — 종합 보안 기술에서 차별화 전략

---

## 5. 규제·표준 환경

**주요 규제 이벤트 (이번 주 업데이트 포함)**

| 규제·표준 | 기관 | 상태 / 시점 | 출처 |
|-----------|------|-------------|------|
| FIPS 203/204/205(ML-KEM/ML-DSA/SLH-DSA) | NIST | 2024-08 확정, 연방 발효 | [[G-03]](#ref-g-03) |
| CNSA 2.0 신규 시스템 PQC 의무화 | NSA | **2027-01 발효** | [[G-18]](#ref-g-18) |
| CISA PQC 제품 카테고리 조달 가이드 | CISA | 2026-01-23 발표 | [[G-17]](#ref-g-17) |
| Google 독자 2029 PQC 마이그레이션 데드라인 | Google | 2026-03-25 선언 | [[G-01]](#ref-g-01) |
| ISO/IEC 18033-8 (BGV/BFV/CKKS/CGGI) | ISO/IEC JTC 1 | 초안 단계, 3년 타임라인 | [이전 리서치] |
| NIST Threshold FHE Call (S5 카테고리) | NIST | 2026-04-20 Preview 마감 | [이전 리서치] |
| TTA GS 인증 1등급 | TTA (한국) | CryptoLab HEaaN Zero-Leak RAG, 2026-03-26 | [[G-14]](#ref-g-14) |
| AI기본법(한국) | 과기정통부 | 2026-01 시행. AICC 고위험 AI 분류 가능성 | [이전 리서치] |
| 개인정보보호법(PIPA) 개정 | PIPC | 프라이버시 강화 기술(PET) R&D 예산 확대 | [이전 리서치] |

**핵심 규제 시사점**

- NSA CNSA 2.0 2027-01 신규 시스템 의무화는 국내 공공·방산 분야에 간접 영향 — 방산·공공 통신 장비 납품 통신사에 PQC 탑재 의무 확산 가능
- CISA 1군(즉시 PQC 의무): 클라우드·협업 도구·협업 플랫폼 포함 → 통신사 기업 서비스 부문 PQC 의무 납품 요건 조기화
- TTA GS 1등급은 한국 공공기관 나라장터 등록 전제 조건 — CryptoLab이 6월 조달 등록 완료 시 통신사 공공 사업의 선택지로 확정됨

---

## 6. TAM/SAM/SOM 업데이트

**이전 대비 변화 포인트**: 시장 규모 수치 자체는 이전 분석과 동일 출처 기반. 신규 확인 사항은 FHE 시장 CAGR 20.2% 추정치가 복수 리서치 기관(360 Research, Business Research Insights)에서 재확인됨 [[G-25]](#ref-g-25).

**FHE/PQC 시장 전망 (업데이트)**

| 구분 | 규모(현재) | 전망 | CAGR | 출처 |
|------|-----------|------|------|------|
| FHE 글로벌 TAM | $251~310M (2026) | $1,319M (2035) | 20.2% | [[G-25]](#ref-g-25) [C] |
| FHE 글로벌 TAM (보수) | $234~321M (2025~26) | $350~600M (2030) | ~8% | [이전 리서치] [C] |
| AICC 글로벌 SAM | $2.4B (Call Center AI, 2025) | $13.5B (2034) | 20.8% | [이전 리서치] |
| PQC 글로벌 시장 | $321M (2024) | $597M (2032) | ~8% | [이전 리서치] [C] |
| 한국 FHE SOM | $7~15M (PoC 단계) | — | — | [추정, D] |

**신규 시그널 — 실도입 규모 기준점 형성**

- Zama+T-REX: $32B ERC-3643 자산 FHE 기밀성 레이어. "FHE가 $10B+ 기관 금융 인프라에서 실사용 가능함을 증명한 최초 사례" [[G-22]](#ref-g-22), [[E-07]](#ref-e-07)
- 이 사례는 FHE 시장 전망의 실현 가능성을 높이는 앵커 레퍼런스로 기능하나, 금융 블록체인과 통신 AICC 도메인이 다르므로 직접 외삽 금지

**통신 도메인 한국 SOM 보완 추정**

KT·SKT 공공 PQC 장비 납품 시장: 국내 공공기관 양자보안망 구축 예산 추정값 공개 정보 없음 — "공개 정보 없음" 명시. KT QENC 장비가 2026년부터 공공기관 조달 시작 시 단일 계약 규모는 수억~수십억 원 단위 예상 [추정, D].

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Google Blog — Quantum Frontiers: PQC Migration Timeline 2029 | [링크](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/) | news | 2026-03-25 | [A] |
| <a id="ref-g-02"></a>G-02 | TechSpot — Google Sets 2029 Deadline for Quantum-Safe Encryption | [링크](https://www.techspot.com/news/111856-google-sets-2029-deadline-quantum-safe-encryption-years.html) | news | 2026-03-25 | [B] |
| <a id="ref-g-03"></a>G-03 | NIST CSRC — FIPS 203/204/205 Post-Quantum Cryptography Standards Finalized | [링크](https://csrc.nist.gov/news/2024/postquantum-cryptography-fips-approved) | news | 2024-08-14 | [A] |
| <a id="ref-g-04"></a>G-04 | Android Authority — Android 17 is Getting Post-Quantum Cryptography | [링크](https://www.androidauthority.com/android-post-quantum-cryptography-3651834/) | news | 2026-03-26 | [B] |
| <a id="ref-g-05"></a>G-05 | Privacy Guides — Android 17 is Getting a Post Quantum Cryptography Upgrade | [링크](https://www.privacyguides.org/news/2026/03/26/android-17-is-getting-a-post-quantum-cryptography-upgrade/) | news | 2026-03-26 | [B] |
| <a id="ref-g-06"></a>G-06 | The Quantum Insider — IBM Works With Signal and Threema on Quantum-Safe Messaging | [링크](https://thequantuminsider.com/2026/03/10/ibm-signal-threema-quantum-safe-research/) | news | 2026-03-10 | [B] |
| <a id="ref-g-07"></a>G-07 | Thales — Thales and SK Telecom: Pioneering Quantum-Resistant Cryptography for 5G Networks | [링크](https://www.thalesgroup.com/en/markets/digital-identity-and-security/mobile/5G-skt-post-quantum-user-case) | news | 2026-03-02 | [B] |
| <a id="ref-g-08"></a>G-08 | The Quantum Insider — SEC Submission Highlights QuSecure PQC Deployment | [링크](https://thequantuminsider.com/2026/03/19/sec-submission-highlights-qusecure-deployment-real-world-post-quantum-migration-example/) | news | 2026-03-19 | [B] |
| <a id="ref-g-09"></a>G-09 | The Quantum Insider — PQShield Ultra-Small PQC Embedded Library (Embedded World 2026) | [링크](https://thequantuminsider.com/2026/03/10/pqshield-ultra-small-pqc-embedded-security-embedded-world/) | news | 2026-03-10 | [B] |
| <a id="ref-g-10"></a>G-10 | P1 Security — Post-Quantum Cryptography for Mobile Networks | [링크](https://www.p1sec.com/blog/post-quantum-cryptography-for-mobile-networks) | blog | 2026 | [B] |
| <a id="ref-g-11"></a>G-11 | AI Times Korea — KT 양자내성암호 솔루션 상용화 준비 완료·하이브리드 양자보안망 구축 가능 | [링크](https://www.aitimes.kr/news/articleView.html?idxno=31327) | news | 2024-06 | [B] |
| <a id="ref-g-12"></a>G-12 | The Lec — KT, 양자암호 PQC+QKD 하이브리드 대세될 것 | [링크](https://www.thelec.kr/news/articleView.html?idxno=28391) | news | 2024 | [B] |
| <a id="ref-g-13"></a>G-13 | Korea IT Times — LG Uplus Unveils AI, Homomorphic Encryption and Quantum-Resistant Security at MWC26 | [링크](https://www.koreaittimes.com/news/articleView.html?idxno=151253) | news | 2026-03-10 | [B] |
| <a id="ref-g-14"></a>G-14 | Seoul Economic Daily (영문) — CryptoLab Earns Top-Tier GS Certification, Targets Public Sector AI Security | [링크](https://en.sedaily.com/news/2026/03/27/cryptolab-earns-top-tier-gs-certification-targets-public) | news | 2026-03-27 | [B] |
| <a id="ref-g-15"></a>G-15 | Security Boulevard — PQC for Authentication: Enterprise Migration Guide 2026 | [링크](https://securityboulevard.com/2026/03/post-quantum-cryptography-for-authentication-the-enterprise-migration-guide-2026/) | news | 2026-03 | [B] |
| <a id="ref-g-16"></a>G-16 | Gray Group Intl — Post-Quantum Cryptography Enterprise Guide 2026 | [링크](https://www.graygroupintl.com/blog/post-quantum-cryptography-enterprise-guide/) | blog | 2026-03 | [C] |
| <a id="ref-g-17"></a>G-17 | CISA — Product Categories for Technologies That Use PQC Standards | [링크](https://www.cisa.gov/resources-tools/resources/product-categories-technologies-use-post-quantum-cryptography-standards) | news | 2026-01-23 | [A] |
| <a id="ref-g-18"></a>G-18 | CyberArk Blog — NIST's New Timeline for Post-Quantum Encryption | [링크](https://www.cyberark.com/resources/blog/nist-s-new-timeline-for-post-quantum-encryption) | blog | 2026 | [B] |
| <a id="ref-g-19"></a>G-19 | IACR ePrint 2026/515 — Privacy at your Fingertips (공개 소식) | [링크](https://iacr.org/news/item/27993) | news | 2026-03-15 | [A] |
| <a id="ref-g-20"></a>G-20 | Tom's Hardware — Intel Heracles 1,074~5,547× Xeon 가속 | [링크](https://www.tomshardware.com/tech-industry/cyber-security/intels-heracles-chip-computes-fully-encrypted-data-without-decrypting-it-chip-is-1-074-to-5-547-times-faster-than-a-24-core-intel-xeon-in-fhe-math-operations) | news | 2026-03-19 | [B] |
| <a id="ref-g-21"></a>G-21 | evertiq — SemiFive secures design win with Niobium for FHE accelerator | [링크](https://evertiq.com/design/2026-02-20-semifive-secures-design-win-with-niobium-for-fhe-accelerator) | news | 2026-02-20 | [B] |
| <a id="ref-g-22"></a>G-22 | Decrypt — T-REX Network and Zama Launch Institutional-Grade Confidentiality Infrastructure | [링크](https://decrypt.co/362436/t-rex-network-and-zama-launch-institutional-grade-confidentiality-infrastructure-for-rwa-tokenization) | news | 2026-03-26 | [B] |
| <a id="ref-g-23"></a>G-23 | SeedTable — 8 Best Homomorphic Encryption Startups (2026-03-24 기준) | [링크](https://www.seedtable.com/best-homomorphic-encryption-startups) | blog | 2026-03-24 | [C] |
| <a id="ref-g-24"></a>G-24 | FHE.org Digest #38 — 2026 Conference, Apple/AWS/Google 후원 | [링크](https://fheorg.substack.com/p/fheorg-digest-38-fheorg-2026-conference) | news | 2026-03 | [B] |
| <a id="ref-g-25"></a>G-25 | 360 Research Reports — Homomorphic Encryption Market CAGR 20.2% | [링크](https://www.360researchreports.com/market-reports/homomorphic-encryption-market-206111) | blog | 2026 | [C] |
| <a id="ref-g-26"></a>G-26 | IACR ePrint 2024/1774 — Panther: Private Approximate Nearest Neighbor Search | [링크](https://eprint.iacr.org/2024/1774.pdf) | paper | 2024 | [A] |
| <a id="ref-g-27"></a>G-27 | ResearchGate — FPGA-Based Acceleration of k-NN on Fully Homomorphic Encrypted Data | [링크](https://www.researchgate.net/publication/378538778_FPGA-Based_Acceleration_of_K-Nearest_Neighbor_Algorithm_on_Fully_Homomorphic_Encrypted_Data) | paper | 2024 | [A] |
| <a id="ref-g-28"></a>G-28 | arXiv 2502.14291 — Efficient Privacy-Preserving Similarity Search for Encrypted Vectors | [링크](https://arxiv.org/html/2502.14291) | paper | 2025-02 | [A] |
| <a id="ref-p-01"></a>P-01 | Aikata, Krieger, Sinha Roy — Privacy at your Fingertips: Enabling Rapid Client-Side Operations in FHE (EuroS&P 2026) | [링크](https://eprint.iacr.org/2026/515) | paper | 2026-03-15 | [A] |
| <a id="ref-p-02"></a>P-02 | CAT: A GPU-Accelerated FHE Framework with Its Application to High-Precision Private Dataset Query (arXiv 2503.22227) | [링크](https://arxiv.org/abs/2503.22227) | paper | 2026-03-28 | [A] |
| <a id="ref-p-03"></a>P-03 | HET-PIR — Homomorphic Encryption Enabled Keyword PIR (Springer Cybersecurity 2026) | [링크](https://link.springer.com/journal/42400) | paper | 2026 | [A] |
| <a id="ref-p-04"></a>P-04 | FHECore: Rethinking GPU Microarchitecture for Fully Homomorphic Encryption (arXiv 2602.22229) | [링크](https://arxiv.org/abs/2602.22229) | paper | 2026-02 | [A] |
| <a id="ref-e-01"></a>E-01 | Google Security Blog — Security for the Quantum Era: Implementing PQC in Android 17 | [링크](https://security.googleblog.com/2026/03/post-quantum-cryptography-in-android.html) | IR/발표 | 2026-03-26 | [A] |
| <a id="ref-e-02"></a>E-02 | QuSecure — SEC Framework Highlights QuSecure Post-Quantum Banking Deployment | [링크](https://www.qusecure.com/post-quantum-cryptography-banking-deployment-sec-framework/) | IR/발표 | 2026-03-19 | [A] |
| <a id="ref-e-03"></a>E-03 | IBM Research Blog — Securing communication from tomorrow's quantum risks (Signal+Threema) | [링크](https://research.ibm.com/blog/signal-threema-quantum-safe) | IR/발표 | 2026-03-10 | [A] |
| <a id="ref-e-04"></a>E-04 | Thales / Nasdaq — Thales sets world first in quantum-safe security for 5G networks | [링크](https://www.nasdaq.com/press-release/thales-sets-world-first-quantum-safe-security-5g-networks-2026-03-02) | IR/발표 | 2026-03-02 | [A] |
| <a id="ref-e-05"></a>E-05 | IEEE Spectrum — Intel Heracles Chip Speeds Up FHE Computing (ISSCC 2026) | [링크](https://spectrum.ieee.org/fhe-intel) | IR/발표 | 2026-03-10 | [A] |
| <a id="ref-e-06"></a>E-06 | CryptoLab / Moneytoday — 크립토랩 HEaaN 제로릭 RAG GS 1등급 획득 | [링크](https://www.mt.co.kr/future/2026/03/26/2026032614461522253) | IR/발표 | 2026-03-26 | [A] |
| <a id="ref-e-07"></a>E-07 | Zama Official — Zama Becomes the Confidentiality Layer for the T-REX Ledger | [링크](https://www.zama.org/post/zama-becomes-the-confidentiality-layer-for-the-t-rex-ledger) | IR/발표 | 2026-03-26 | [A] |
| <a id="ref-e-08"></a>E-08 | PR Newswire — CryptoLab and UClone Partner to Bring First FHE-Powered AI Agents to Consumers | [링크](https://www.prnewswire.com/news-releases/cryptolab-and-uclone-partner-to-bring-first-fully-homomorphic-encryption-powered-ai-agents-to-consumers-302439395.html) | IR/발표 | 2025-04-28 | [A] |
