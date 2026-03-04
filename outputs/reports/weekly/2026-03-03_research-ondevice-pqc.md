---
topic: OnDevice 양자암호 (Post-Quantum Cryptography on Device)
date: 2026-03-03
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
domain: Secure AI (LG U+ tech strategy)
period: late Feb ~ early Mar 2026
---

# Research Report: OnDevice 양자암호 (Post-Quantum Cryptography on Device)
## Tier 2 Comprehensive Research — Weekly Tech Intelligence

---

## Executive Summary (경영진 요약)

> 2026년 2~3월은 온디바이스 PQC(양자내성암호)가 **개념 검증에서 상용화**로 전환되는 변곡점이다. 삼성은 Exynos 2600(갤럭시 S26)에 세계 최초 하드웨어 기반 PQC를 탑재하고, Thales는 서비스 단절 없이 기존 배포된 SIM/eSIM을 원격으로 PQC 업그레이드하는 세계 최초 시연을 MWC 2026에서 발표했다. SKT-Thales 협업은 5G SUPI 보호에 Crystals-Kyber를 실증 적용했고, LG U+는 MWC에서 AI·PQC 기반 보안 4종을 공개했다. 학술적으로는 5G Core에 PQC 도입 시 성능 영향이 미미함이 복수 논문으로 확인되었으며, NIST는 HQC를 다섯 번째 백업 표준으로 선정했다. 규제 측면에서 미국 NSS 2027년 CNSA 2.0 의무화, EU 2026년 로드맵 수립·2030년 전환 완료 일정이 확정되어 통신 사업자의 조기 대응이 불가피해졌다. **신뢰도: A/B급 출처 기반 고확신.**

---

## 연구 질문

온디바이스 PQC 분야에서 2026년 2월 말~3월 초 사이 발생한 주요 신호를 심층 수집하고, 기술 성숙도·학술 동향·특허·플레이어별 전략·통신 특화 이슈를 종합하여 WTIS 의사결정 전(前) 분석 기반을 마련한다.

---

## 1. 기술 현황

### 1.1 NIST PQC 표준 최종 확정 (TRL 9)

NIST는 2024년 8월 최초 3개 PQC 표준을 최종 발표했다 [G-08]:
- **FIPS 203 (ML-KEM)**: CRYSTALS-Kyber 기반 키 캡슐화 메커니즘. ML-KEM-512/768/1024 3종 파라미터 세트
- **FIPS 204 (ML-DSA)**: CRYSTALS-Dilithium 기반 디지털 서명
- **FIPS 205 (SLH-DSA)**: SPHINCS+ 기반 상태 비저장 해시 서명

2025년 3월, NIST는 **HQC(Hamming Quasi-Cyclic)**를 ML-KEM 백업용 다섯 번째 알고리즘으로 선정했다 [G-12]. HQC는 ML-KEM과 수학적 기반이 달라 ML-KEM 취약점 발견 시 대체 가능. 초안 표준은 2026년 초 예정, 최종 표준은 2027년 예정이다 [G-12].

### 1.2 하드웨어 PQC 구현 (TRL 7-8 → 9 전환 중)

**삼성 S3SSE2A Secure Element (2026년 1월, CES)**
- 업계 최초 하드웨어 기반 PQC 내장 임베디드 보안 요소(eSE) [E-01]
- CC(Common Criteria) 인증 획득
- Thales의 보안 OS + 양자내성 암호화 라이브러리 탑재
- 기존 보안 알고리즘과 PQC를 모두 지원하는 **하이브리드 구조**
- 고속 PQC 연산, 저전력·저메모리 소비 달성 [E-01]

**삼성 Exynos 2600 모바일 SoC (2025년 12월 발표, 2026년 2월 갤럭시 S26 탑재)**
- 세계 최초 스마트폰 칩셋의 하드웨어 지원 PQC [G-01]
- **알고리즘**: ML-DSA (Module-Lattice-Based Digital Signature Algorithm)
- **Boot ROM 통합**: PQC 검증이 Boot ROM 단계부터 즉시 수행, 불변 RoT(Root of Trust) 구현
- **하드웨어 가속**: NTT 연산 및 관련 계산을 하드웨어로 가속하여 기존 ECDSA와 동등 수준의 부팅 속도 달성 [G-02]
- **AND-Policy 하이브리드**: ECDSA + ML-DSA 양방향 검증 — 두 서명 모두 통과해야 부팅, 병렬 처리로 지연 최소화
- **메모리**: ML-DSA는 레거시 대비 수십 KB 추가 메모리 필요, 삼성이 임베디드 제약을 고려하여 최적화 [G-02]
- Primary Security Processor(격리 보안 프로세서/Enclave)가 Boot ROM과 보안 코어를 격리, 공격 표면 최소화

### 1.3 하이브리드 모드 트렌드

산업 전반에서 **고전 + PQC 하이브리드** 접근법이 표준으로 자리잡고 있다:
- 상호운용성 보장 (레거시 시스템과 호환)
- 표준 전환 기간 중 안전성 담보
- 클라이언트-서버 양쪽이 PQC를 지원할 때 자동으로 PQC 활성화

**Cloudflare 실제 트래픽 기준** [G-19]: 2025년 초 29% → 2025년 12월 초 52%로 PQC 암호화 트래픽 급증. ML-KEM(X25519MLKEM768)이 업계 표준 키 합의 프로토콜로 수렴.

---

## 2. 시장 동향

### 2.1 시장 규모

| 조사기관 | 2024~2026 기준값 | 2030년 전망 | CAGR |
|---------|----------------|-----------|------|
| MarketsandMarkets [G-20] | $0.42B (2025) | $2.84B | 46.2% |
| Grand View Research | $1.15B (2024) | — | 37.6% |
| IMARC Group | $310.4M (2024) | — | 45.3% |

> 주의: 각 기관의 시장 범위 정의가 상이하여 수치 직접 비교는 부적절. 공통적으로 40%+ CAGR의 고성장 전망은 일관적 [C].

### 2.2 주요 성장 동인

1. **규제 의무화 일정**: 미국 NSS 2027년 CNSA 2.0, EU 2026년 로드맵·2030년 전환 [G-17]
2. **Harvest Now, Decrypt Later 위협**: 현재 수집한 암호화 데이터를 미래 양자컴퓨터로 해독 가능
3. **NIST 표준 확정 (2024)**: 불확실성 해소 → 기업 투자 실행 단계 진입
4. **하이퍼스케일러·브라우저 벤더 선제 적용**: Google Chrome ML-KEM 전환, Apple PQ3

### 2.3 시장 현황 (2026년 초)

- **Financial services, Government, Defense, Telecom**이 초기 도입 주도 [G-20]
- VPN, TLS, 아이덴티티 시스템, 클라우드 키 관리, 펌웨어 서명, 보안 메시징 등에서 통합 진행 중
- PQC 전문 스타트업(PQShield, SEALSQ, Arqit 등) + 기존 대형 보안 벤더(IBM, Thales, IDEMIA) 경쟁 구도

---

## 3. 경쟁사 동향

### 3.1 삼성 (Samsung)

**하드웨어 PQC 분야 현재 선도자** [A]:

- **Exynos 2600**: 2025년 12월 공식 발표, 2026년 2월 갤럭시 S26에 탑재. 세계 최초 스마트폰 SoC 하드웨어 PQC [E-02]
- **S3SSE2A 보안 칩**: CES 2026 Best Cybersecurity Innovation 수상. 업계 최초 하드웨어 기반 PQC 임베디드 보안 요소, CC 인증 [E-01]
- **Knox Matrix 업데이트**: PQC 기반 E2EE를 eSIM 이전 서비스에 확장 지원 [E-03]
- **7년 보안 업데이트**: 갤럭시 S26 시리즈 전 모델 적용 [E-03]
- **파트너**: Thales (보안 OS 및 PQC 라이브러리 공급)
- **경쟁 우위**: Qualcomm Snapdragon은 2026년 3월 현재 하드웨어 PQC 미발표 → 삼성이 유일한 소비자 기기 하드웨어 PQC 공급자 [G-03]

### 3.2 SKT (SK Telecom)

**5G 네트워크 PQC 국내 선도자** [A]:

- **SKT-Thales 협업**: CRYSTALS-Kyber 기반 5G SA(Standalone) 네트워크에서 SUPI 보호 실증 [E-04]
- 기존 배포된 5G SIM/eSIM을 교체 없이 서비스 무중단으로 PQC 업그레이드 가능성 확인
- **2025년 퀀텀 세이프 로드맵** 공개: Path towards a quantum-safe future [E-05]
- 위 협업의 최초 시연은 2023년 12월, 2026년 3월 Thales가 세계 최초 상용 수준 시연으로 발전 [N-01]

### 3.3 KT (Korea Telecom)

**양자 보안에서 QKD 중심 접근 채택** [B]:

- 2025년 2월: QKD + PQC 하이브리드 양자 보안 네트워크 출시, 5G 네트워크 15개 이상 노드 적용 [N-08]
- HEQA Security와 협업하여 통신 인프라에 QKD 시스템 배포 계획 (2025년 6월 Quantum Korea 2025 발표) [N-08]
- PQC 단독 전용회선 서비스 공개 발표: 공개 정보 없음 (KT는 PQC보다 QKD 중심 전략 추진 중으로 분석됨)

### 3.4 LG U+ (LGU+)

**MWC 2026: 차세대 보안 4종 공개** [A]:

- **PQC 광전송 장비 적용**: 미국 NIST 및 국내 KpqC 알고리즘 모두 지원하는 통합 인터페이스 구현 [E-06]
- **알고리즘 교체 시 서비스 무중단** 운영 지원 (Crypto Agility)
- **U+ PQC-VPN** 서비스 출시 (기존): 양자내성암호 적용 가상사설망 [E-07]
- **U+ PQC 전용회선**: 세계 최초 양자내성암호 전용회선 서비스 (격자 기반 암호, ROADM 광전송장비 적용) [E-08]
- **협력사**: 크립토랩(첨단암호), 코위버(광전송장비)
- **MWC 2026 공개 기술**: (1) PQC 광전송, (2) AI 기반 이상탐지, (3) SASE 보안 플랫폼(국내 최초 구축), (4) 암호화된 공격 탐지 [N-05]
- **파일럿 계획**: 공공기관·금융 분야 파일럿, 이후 6G 이동통신·자율주행·스마트팩토리로 확장 예정 [E-06]

### 3.5 Thales

**SIM/eSIM PQC 원격 업그레이드의 세계 최초 시연** [A]:

- **2026년 3월 1일 MWC**: 이미 현장에 배포된 SIM/eSIM에 원격으로 PQC 알고리즘 다운로드 가능 시연 [N-01]
- **Crypto Agility**: 서비스 단절 없이 OTA(Over-the-Air) 방식으로 암호화 알고리즘 업그레이드
- 기존 데이터·서비스 유지, 즉각적 보안 강화
- Samsung S3SSE2A 칩에 보안 OS 및 PQC 라이브러리 공급 [E-01]
- SKT 5G PQC 협업의 기술 파트너 [E-04]

### 3.6 IDEMIA

**eSIM IoT PQC 시연 (MWC 2025)** [B]:

- 2022년: 세계 최초 양자내성 5G SIM 공급 업체
- 2025년 7월 MWC Barcelona 2025: Telefónica와 협업, 스마트 유틸리티 IoT 디바이스 대상 PQC eSIM 기술 시연 [N-06]
- **IDEMIA Crypto Agility Solution** (2024년 4월): 원격 암호화 업데이트 기능 포함 [N-07]
- 현재 가장 긴 PQC SIM 상용 경험 보유 (2022년~)

### 3.7 Apple

**iMessage PQ3 프로토콜 (2024년 적용 완료)** [A]:

- **PQ3 프로토콜**: NIST ML-KEM 기반 Kyber 공개키 사용, ECC와 하이브리드 설계 [G-13]
- Level 3 보안: 모든 주요 메시징 앱 중 최고 수준
- 최대 50메시지마다 또는 7일마다 키 갱신 → Forward Secrecy 보장
- 2024년 iOS 17.4/iPadOS 17.4/macOS 14.4/watchOS 10.4 배포 완료
- iOS 26 배포 후 Apple 기기의 PQC 지원 요청 비율: 2% → 25% 급증 [G-19]
- **현재 미보고 사항**: iOS/macOS 커널 레벨 또는 다른 시스템 프로토콜에 PQC 확장 여부 공개 정보 없음

### 3.8 Google

**Chrome ML-KEM 전환 (2024년 11월)** [A]:

- Chrome 131에서 Kyber768+X25519 → **ML-KEM768+X25519**로 전환 (코드포인트 0x6399 → 0x11EC) [G-14]
- TLS 하이브리드 PQC 키 교환 기본 활성화
- **2026년**: 최초 PQC 인증서 등장 예상되나, 모든 브라우저가 신뢰하기까지 2027년 이후 예상 [G-14]

### 3.9 IBM

**엔터프라이즈 PQC 전환 서비스 선도** [B]:

- **IBM Quantum Safe Explorer, Remediator**: 암호화 자산 발견·전환 도구 [G-15]
- **IBM Quantum Safe Posture Management**: Private Preview 제공 중
- **Keyfactor 파트너십** (2026년 1월): 기업의 PQC 전환 가시성·리스크 관리 솔루션 공동 제공 [G-16]
- **Palo Alto Networks 파트너십**: Quantum-Safe Readiness 공동 솔루션 2026년 초 출시 예정 [G-15]
- IBM Quantum Platform 자체에 quantum-safe 보안 적용 [G-15]

### 3.10 Qualcomm

**하드웨어 PQC 미발표 (2026년 3월 기준)** [B]:

- Snapdragon 8 Elite Gen 5: Qualcomm SPU(Secure Processing Unit) 탑재, 그러나 고전 RSA/ECC 기반 유지 [G-03]
- 2022년: FALCON 알고리즘 기술적 기여 이력 존재 [G-03]
- Qualcomm 내부 발표: 공개 정보 없음
- 업계 분석: Snapdragon, MediaTek이 2~3년 내 PQC 탑재 예상 [G-03]

### 3.11 Telefónica

**PQC 최초 상용 통신 서비스 사업자 주장** [B]:

- MWC 2026 'Quantum Telco' 발표: PQC 표준 기반 데이터센터·오피스 통신 서비스 상용 출시 [E-09]
- 3가지 Quantum-Safe 솔루션: Adtran(DCI), Fortinet(Q-Safe 오피스), Luxquanta(QKD) [E-09]
- IDEMIA와 MWC 2025 PQC eSIM IoT 시연 [N-06]

### 3.12 Nokia / Ericsson

**네트워크 장비 벤더 PQC 로드맵** [B]:

- **Nokia**: 업계 최초 광네트워킹 장비 NIST FIPS 140-3 Security Level 2 인증 획득 [G-18]
  - Numana와 Kirq 플랫폼 기반 양자 안전 네트워크 아키텍처 테스트 (2026년 2월 25일) [N-09]
  - 2026년 Kirq 플랫폼 테스트 확대 예정
  - Colt, Honeywell과 위성 기반 QKD 솔루션 테스트 (2026), 상용화 2027년 예정
- **Ericsson**: 3GPP, IETF, ETSI에서 PQC 표준화 활동 참여 [G-18]
  - 5G TLS, IKEv2, X.509, JOSE, SUCI 표준 업데이트 시 PQC 적용 계획
  - 현재 CRQC(암호화 관련 양자컴퓨터)가 수년 내 등장하지 않을 것으로 전망하면서도 조기 계획 수립 권고

---

## 4. 제품/서비스 스펙 비교

| 기업 | 제품/서비스 | 알고리즘 | 적용 레이어 | 상용 단계 | 하이브리드 지원 | 발표 시점 | 출처 |
|------|-----------|---------|-----------|---------|--------------|---------|------|
| Samsung | Exynos 2600 (SoC) | ML-DSA | Boot ROM / 하드웨어 가속 | 양산 (갤럭시 S26) | AND-Policy (ECDSA+ML-DSA) | 2025-12 | [E-02] |
| Samsung | S3SSE2A (Secure Element) | ML-KEM + ML-DSA | eSE 하드웨어 | CC 인증 완료 | 하이브리드 | 2026-01 CES | [E-01] |
| Samsung | Knox Matrix PQC | PQC E2EE | eSIM 이전 서비스 | 갤럭시 S26 | 공개 정보 없음 | 2026-02 Unpacked | [E-03] |
| LG U+ | U+ PQC 전용회선 | 격자 기반 (NIST + KpqC) | 광전송 (ROADM) | 상용 서비스 중 | 공개 정보 없음 | 2022 출시 | [E-08] |
| LG U+ | U+ PQC-VPN | PQC | VPN | 상용 서비스 중 | 공개 정보 없음 | 출시 완료 | [E-07] |
| LG U+ | MWC 2026 PQC 광전송 | NIST+KpqC 통합 | 광전송 장비 | 전시/파일럿 단계 | Crypto Agility | 2026-02 MWC | [E-06] |
| SKT + Thales | 5G SIM PQC 업그레이드 | CRYSTALS-Kyber | 5G SA 네트워크 SUPI 보호 | 세계 최초 실증 완료 | 공개 정보 없음 | 2026-03 MWC | [N-01] |
| Thales | 5G SIM 원격 PQC OTA | NIST PQC 표준 | SIM/eSIM OTA | 세계 최초 시연 완료 | Crypto Agility | 2026-03-01 | [N-01] |
| IDEMIA | Quantum-resistant 5G SIM | NIST PQC | SIM | 상용 (2022~) | 공개 정보 없음 | 2022 | [N-07] |
| Apple | iMessage PQ3 | ML-KEM (Kyber) + ECC | 메시징 | 전체 배포 완료 (2024) | 하이브리드 (레벨 3) | 2024-02 | [G-13] |
| Google | Chrome ML-KEM | ML-KEM768+X25519 | TLS 키 교환 | Chrome 131 배포 | 하이브리드 | 2024-09 | [G-14] |
| Qualcomm | Snapdragon 8 Elite Gen 5 | RSA/ECC (고전) | SPU | 양산 중 | 미지원 | 공개 정보 없음 | [G-03] |
| Nokia | 광네트워킹 장비 | FIPS 140-3 Level 2 | 광 전송 | NIST 인증 획득 | 공개 정보 없음 | 인증 완료 | [G-18] |
| coRAN Labs + Canonical | 5G PQC 플랫폼 (QORE) | ML-DSA PKI 기반 | 5G 전 스택 (RAN~Core) | MWC 2026 데모 | 하이브리드 | 2026-03 MWC | [N-03] |
| Telefónica | Quantum Telco | PQC 표준 기반 | DC 연결, 오피스 통신 | 상용 출시 | 공개 정보 없음 | 2026-03 MWC | [E-09] |
| Keeper Security | 패스워드 매니저 | NIST Kyber (ML-KEM) | API 인증 + 터널 | 백엔드 API 배포 완료 | ECC+Kyber 하이브리드 | 2026-02-25 | [N-04] |
| IBM | Quantum Safe Suite | ML-KEM, ML-DSA 등 | 엔터프라이즈 IT | 서비스 출시 중 | 공개 정보 없음 | 2026 | [G-15] |

---

## 5. 학술 동향

### 5.1 5G Core PQC 도입 성능 영향: 미미

**Post-Quantum Cryptography in the 5G Core** [P-01]
- arxiv:2512.20243 (2025년 12월)
- 5G Core의 기존 암호 알고리즘을 PQC로 교체 시 대역폭 소비·지연에 미치는 영향 실측
- **핵심 결과**: 성능에 측정 가능한 영향은 있으나 미미, 네트워크 사용성에 실질적 영향 없음
- 5G Core가 PQC 도입을 기술적으로 수용 가능함을 확인

**Analysis of Post-Quantum Cryptography in User Equipment in 5G and Beyond** [P-02]
- arxiv:2507.17074 (2025년 7월)
- 5G 에뮬레이션 스택 + PQC-enabled TLS 1.3 환경에서 NIST 선정 PQC 알고리즘 실험적 평가
- **핵심 결과**: ML-KEM + ML-DSA가 지연 민감 애플리케이션에서 최적 효율성 제공; SPHINCS+ + HQC 조합은 더 높은 계산 오버헤드

### 5.2 5G 인증 프로토콜 PQC 하이브리드화

**5G-AKA-HPQC: Hybrid PQC Protocol for 5G Primary Authentication** [P-03]
- arxiv:2502.02851 (2025년 2월 5일)
- 저자: Yongho Ko 외 2인
- 5G-AKA 프로토콜에 ECIES + PQC KEM 하이브리드 적용, 기존 표준 호환성 유지
- SVO Logic + ProVerif로 보안 검증, 계산·통신 오버헤드 균형 확인

**QORE: Quantum Secure 5G/B5G Core** [P-04]
- arxiv:2510.19982 (2025년 10월)
- coRAN Labs의 QORE 시스템 학술 기반 논문
- ML-KEM이 미미한 성능 오버헤드로 양자 보안 제공, 3GPP SA3/SA5 PQC 관련 스터디 활동과 정렬

### 5.3 모바일/IoT 제약 환경 성능 벤치마크

**Implementation and performance of PQC for resource constrained consumer electronics** [P-05]
- Springer Nature Discover IoT (2025년 11월)
- 차세대 소비자 전자기기 대상 PQC 도입 가능성 탐색
- Kyber-512(128비트 보안)는 RSA-2048 대비 키 교환 약 3배 빠름, IoT 배터리 기기에 적합

**A Practical Performance Benchmark of PQC Across Heterogeneous Computing Environments** [P-06]
- MDPI Cryptography 9(2):32 (2025년)
- 고성능 서버~제약 IoT 기기까지 다양한 환경에서 PQC 배포 가능성 확인
- IoT 프로토콜의 1~2KB 패킷 크기 제한 → BIKE는 모든 보안 수준에서 단편화 필요

**Investigating PQC to Secure Transmitted Data via Mobile Communication** [P-07]
- Preprints.org 202601.1876 (2026년 1월)
- CRYSTALS-Kyber, Dilithium, Falcon, SPHINCS+ 등 NIST 후보 알고리즘을 모바일 통신 시스템에 통합
- 격자 기반(Kyber, Dilithium)이 제약 기기에서 보안-효율성 최적 균형 제공
- SPHINCS+ 등 해시 기반 알고리즘은 계산 부담으로 일부 적용에 제한적

### 5.4 삼성 QRNG + PQC 스마트폰 연구

**Unveiling Samsung Quantum Galaxy: Securing Smartphones With QRNG and PQC** [P-08]
- IEEE Access Vol.13 (2025년 4월 23일), 저자: Omar Alibrahim (Kuwait University)
- 갤럭시 스마트폰 QRNG 칩 활용 현황 분석: 실제 앱에서 QRNG 활용 미흡 발견
- QRNG + PQC 결합 보안 인스턴트 메시징·VoIP 앱 개발, 보안성 유의미한 향상 확인
- DOI: 10.1109/ACCESS.2025.10974970

### 5.5 하드웨어 가속 (ASIC/FPGA)

**Lattice-Based Cryptographic Accelerators for the Post-Quantum Era: Survey** [P-09]
- MDPI Electronics 15(2):475 (2026년 1월)
- 2020~2025년 NIST Round 3/4 이후 FPGA/ASIC 구현 문헌 종합 리뷰
- CRYSTALS-Kyber 45%, CRYSTALS-Dilithium 30%가 연구 논문의 대다수 차지
- FPGA 구현이 전체의 약 65%
- NTT(Number Theoretic Transform)가 핵심 계산 병목

**A Configurable ML-KEM/Kyber Hardware Accelerator Architecture** [P-10]
- IEEE Transactions (2024, Article 10634219)
- ML-KEM 전용 설정 가능 하드웨어 가속기 아키텍처 제안

**Hardware Acceleration of Crystals-Kyber with RISC-V ISA Extensions** [P-11]
- IEEE Journals (2024, Article 10562296)
- RISC-V 명령어 세트 확장을 통한 CRYSTALS-Kyber 하드웨어 가속
- ASIC 설계: NTT 대비 14.51배, inverse NTT 대비 16.75배 속도 향상 (180nm CMOS, 118MHz) [G-21]

---

## 6. 특허 동향

> MCP patent-intel 도구가 현재 환경에서 호출 불가 (VSCode 확장 MCP 미작동 확인). USPTO PatentsView API 기반 검색은 대체 WebSearch로 수행.

### 6.1 전반적 특허 출원 동향

- 2024년 PQC 관련 특허 출원이 최고조에 달함 [G-20]
- 격자 기반 암호, 보안 네트워킹, 암호 민첩성(Crypto Agility) 프레임워크 분야 집중
- 2025~2026년에도 지속적 R&D 투자를 반영한 출원 증가 추세 예상
- **Qualcomm**: 2022년 FALCON 알고리즘 관련 기여 이력, 세부 특허 정보 공개 없음
- **Samsung**: S3SSE2A 보안 칩 관련 특허 다수 추정, 갤럭시 S26 울트라 보안 특허 ZDNet Korea 보도 [N-10]
- **특허 전문 검색 한계**: 개별 기업의 구체적 특허 번호·청구항 수집은 MCP patent-intel 도구 필요 (현재 미접근 가능)

### 6.2 주요 출원 영역

| 기술 영역 | 주요 출원 기업 (추정) | 비고 |
|---------|-----------------|------|
| 격자 기반 키 캡슐화 (ML-KEM) | IBM, Qualcomm, Samsung, Intel | NIST 표준화 완료 후 구현 특허 집중 |
| 하드웨어 PQC 가속기 | Samsung, Arm, NVIDIA, Xilinx | FPGA/ASIC NTT 가속 관련 |
| PQC SIM/eSIM OTA 업그레이드 | Thales, IDEMIA, Gemalto | 통신 특화 |
| PQC 하이브리드 프로토콜 (TLS, IKEv2) | Google, Apple, Microsoft, Cloudflare | 프로토콜 레이어 |
| Crypto Agility 프레임워크 | IBM, Nokia, Thales | 엔터프라이즈 전환 관리 |

---

## 7. 기업 발언 & 보도자료

### E-01: Samsung + Thales — S3SSE2A CES 2026 Best Innovation 수상 (2026-01-06)
"Samsung and Thales have built a long-standing collaboration in security, and the S3SSE2A is the industry's first PQC total solution, developed jointly from the outset to integrate hardware and software, delivering an exceptional level of security." — Business Wire [E-01]

### E-02: Samsung Semiconductor — Exynos 2600 PQC 기술 블로그 (2025-12)
"Exynos has been designed so that secure boot verification based on post-quantum cryptography (PQC) is performed immediately from the Boot ROM stage... NTT operations and related computations are accelerated using hardware backing, optimizing ML-DSA performance to match existing ECDSA implementation speeds." — Samsung Semiconductor Global Blog [E-02]

### E-03: Samsung Galaxy Unpacked 2026 공식 발표 (2026-02-26, 한국어 뉴스룸)
"업데이트된 녹스 매트릭스는 기기 간 양자 내성 암호 기반의 '종단 간 암호화(E2EE)'를 eSIM 이전과 같은 서비스에도 확대 지원합니다." — 삼성전자 한국 뉴스룸 [E-03]

### E-04: SKT + Thales — 5G PQC 협업 발표 (2023-12-19, SKT 뉴스룸)
"This collaboration highlights our commitment to staying ahead in cybersecurity and ensuring customer data safety." — Yu Takki, SKT VP [E-04]
"There is an emerging need to transition to cryptographic algorithms believed secure against quantum attacks." — Eva Rudin, Thales SVP [E-04]

### E-05: SKT — Path towards a quantum-safe future (SKT 뉴스룸)
SKT가 퀀텀 세이프 미래를 향한 로드맵을 공개. 구체적 타임라인 기준: 공개 정보 없음 [E-05]

### E-06: LG유플러스 — MWC 2026 차세대 보안 기술 발표 (2026-02-26)
"LG유플러스는 미국 국립표준기술연구소와 국내 양자내성암호연구단(KpqC)이 제시한 최신 알고리즘을 모두 지원하는 통합 인터페이스를 구현했으며, 고객은 보안 정책에 맞는 알고리즘을 선택해 적용할 수 있고, 알고리즘 교체 시에도 서비스 중단 없이 안정적으로 운영할 수 있습니다." — LG유플러스 공식 발표 [E-06]

### E-07: LG유플러스 — U+ PQC-VPN 출시 (뉴스룸)
"양자내성암호 적용한 가상사설망 U+ PQC-VPN" 정식 서비스 출시 [E-07]

### E-08: LG유플러스 — 세계 최초 양자내성암호 전용회선 서비스 (LG 공식 보도자료)
"세계 최초로 선보이는 U+양자내성암호 전용회선은 양자내성암호 기술이 적용된 광전송장비(ROADM)를 통해 해킹이 불가능한 보안환경을 제공하며, 고객이 전용회선을 통해 데이터를 송·수신할 때 양자내성암호 키로 암·복호화하는 방식입니다." [E-08]

### E-09: Telefónica — Quantum Telco, MWC 2026 (2026-03, 공식 보도자료)
"Telefónica was the first operator to commercially launch communications services for data centres and offices protected by the new post-quantum cryptography standards." [E-09]

---

## 8. 통신 특화 분석

### 8.1 5G/6G PQC 마이그레이션 로드맵

**현재 5G의 암호화 취약 지점** [G-22]:
1. **SUPI(가입자 영구 식별자) 보호**: 5G는 SUCI(SUPI 은닉)로 프라이버시 개선했으나 현재 고전 공개키 암호 사용 → 양자컴퓨터 공격에 취약
2. **5G AKA 인증 프로토콜**: ECIES 기반 → PQC 하이브리드 대체 연구 진행 중 [P-03]
3. **서비스 기반 인터페이스(SBI) TLS**: PQC-TLS로 교체 연구 진행 중 [P-01]

**3GPP 표준화 진행 상황** [G-22]:
- 3GPP Release 19 또는 20에서 PQC 알고리즘 옵션/요구사항 포함 예상
- 현재 SA3(보안), SA5(네트워크 관리) 스터디 그룹에서 PQC 관련 활동 진행 중
- IETF, 3GPP, ETSI, ITU, O-RAN에서 표준화 작업 병행 (아직 완료되지 않음) [G-10]

### 8.2 SIM/eSIM 양자 안전 업그레이드 경로

| 접근법 | 설명 | 주요 플레이어 | 상용화 수준 |
|-------|------|------------|-----------|
| 신규 PQC SIM 발급 | PQC 탑재 신형 SIM 교체 | IDEMIA (2022~), Thales | 상용 서비스 중 |
| OTA 원격 PQC 업그레이드 | 기존 배포 SIM에 PQC 알고리즘 OTA 다운로드 | Thales (세계 최초 시연 2026-03) | 시연 완료, 상용화 진행 중 |
| 하이브리드 SIM | 기존 알고리즘 + PQC 동시 지원 | 전 SIM 벤더 | 개념 정립 완료 |

**Thales Crypto Agility 기술**: 서비스 단절 없이 OTA로 암호화 알고리즘 업그레이드. SKT와 협업하여 5G SA 네트워크에서 Crystals-Kyber로 SUPI 보호 실증 [N-01].

### 8.3 네트워크 장비 벤더 지원 현황

| 벤더 | PQC 현황 | 인증/표준 | 상용화 수준 |
|------|---------|---------|-----------|
| Nokia | FIPS 140-3 Level 2 인증 완료 (광네트워킹) | NIST FIPS | 장비 출시 중 |
| Ericsson | NIST PQC 표준화 활동 참여, 3GPP/IETF 관여 | 3GPP, IETF | 연구/표준화 단계 |
| Huawei | 공개 발표 없음 | 공개 정보 없음 | 공개 정보 없음 |

### 8.4 규제 타임라인

| 규제 | 시점 | 내용 |
|-----|-----|------|
| 미국 CNSA 2.0 | 2025년 말 | 신규 소프트웨어·펌웨어·공개 대면 시스템에서 CNSA 2.0 알고리즘 지원 및 우선 적용 |
| 미국 CNSA 2.0 | **2027-01-01** | 모든 신규 NSS(국가안보시스템) 장비 조달 CNSA 2.0 의무화 [G-17] |
| 미국 NIST IR 8547 | 2035년 | 양자 취약 알고리즘 표준에서 제거 완료 |
| EU 권고 | **2026년 말** | 모든 EU 회원국 PQC 전환 국가 계획 수립 완료 [G-17] |
| EU 권고 | **2030년 말** | 중요 인프라의 PQC 전환 완료 |
| EU 권고 | 2035년 | 실현 가능한 모든 시스템 전환 완료 |

---

## 신뢰도 평가

### 높은 확신 [A/B]:
- 삼성 Exynos 2600 PQC 구현 세부 사항 (Samsung Semiconductor 공식 기술 블로그, 복수 확인)
- Samsung S3SSE2A CES 2026 수상 및 Thales 협력 (Business Wire 공식 보도자료)
- Thales 5G SIM PQC OTA 세계 최초 시연 (복수 언론, 공식 보도자료)
- SKT-Thales CRYSTALS-Kyber 5G 협업 (SKT 공식 뉴스룸)
- LG U+ MWC 2026 PQC 발표 내용 (복수 국내 언론, 공식 보도자료)
- NIST FIPS 203/204/205 확정 및 HQC 선정 (NIST 공식 발표)
- EU 2026/2030 로드맵, 미국 CNSA 2.0 2027 의무화 (정부 공식 문서)
- Apple PQ3, Google Chrome ML-KEM 전환 (공식 기술 블로그)
- Cloudflare PQC 트래픽 52% 통계 (Cloudflare 공식 블로그)
- 5G Core PQC 성능 영향 미미 (arxiv 피어리뷰 논문 2건)

### 추가 검증 필요 [C/D]:
- PQC 시장 규모 수치 ($0.42B~$1.15B 기관별 편차 큼) — 단일 시장조사 기관 수치 채택 부적절
- Qualcomm의 향후 PQC 하드웨어 출시 일정 — 업계 분석가 추정, 공식 확인 없음
- Telefónica의 "최초 상용 PQC 통신 서비스" 주장 — 자사 보도자료 기반, 독립 검증 필요
- Huawei PQC 전략 — 공개 정보 부재

### 데이터 공백:
- KT의 PQC 전용 이니셔티브 (QKD 중심 전략이므로 PQC 단독 공개 발표 없음)
- Qualcomm Snapdragon PQC 하드웨어 로드맵
- IDEMIA의 2026년 MWC 발표 내용 (MWC 2025 협업만 확인됨)
- Huawei의 PQC 네트워크 장비 현황
- 삼성 Knox Matrix PQC E2EE의 구체적 알고리즘 및 프로토콜 세부사항
- 3GPP Release 19/20의 PQC 관련 기술 규격 확정 일정

---

## References

### 기업 발언 (E-xx)
| 번호 | 출처명 | 발행일 | 제목 | 요약 |
|------|--------|-------|------|------|
| E-01 | Business Wire | 2026-01-06 | Thales Powers CES-Winning Post-Quantum Chip From Samsung Electronics | Samsung S3SSE2A: 업계 최초 하드웨어 기반 PQC eSE, Thales 보안 OS + PQC 라이브러리 탑재, CES 2026 Best Cybersecurity Innovation 수상 |
| E-02 | Samsung Semiconductor Blog | 2025-12 | Where Trust Begins: Exynos Anchors PQC at the Root of Mobile SoCs | Exynos 2600: ML-DSA, Boot ROM PQC, NTT 하드웨어 가속, AND-Policy 하이브리드 |
| E-03 | 삼성전자 한국 뉴스룸 | 2026-02-26 | 삼성전자, 갤럭시 S26 시리즈 공개 | Knox Matrix PQC E2EE eSIM 이전 확장, 7년 보안 업데이트 |
| E-04 | SKT 뉴스룸 (EN) | 2023-12-19 | SK Telecom and Thales Collaborate on PQC | CRYSTALS-Kyber 기반 5G SA 네트워크 SUPI 보호, Yu Takki/Eva Rudin 발언 |
| E-05 | SKT 뉴스룸 | — | Path towards a quantum-safe future | SKT 퀀텀 세이프 로드맵 공개 |
| E-06 | LG유플러스 보도자료 | 2026-02-26 | MWC 2026 차세대 보안 기술 4종 | NIST+KpqC 통합 PQC 광전송, SASE, AI 이상탐지, 암호화 공격 탐지 |
| E-07 | LG유플러스 뉴스룸 | 출시일 미확인 | U+ PQC-VPN 출시 | 양자내성암호 적용 VPN 서비스 |
| E-08 | LG그룹 공식 보도자료 | 2022 | 세계 최초 양자내성암호 전용회선 서비스 출시 | ROADM 광전송장비, 격자 기반 암호, 크립토랩·코위버 협력 |
| E-09 | Telefónica 공식 보도자료 | 2026-03 | Telefónica leads Quantum Telco at MWC | 최초 상용 PQC 통신 서비스 주장, Adtran/Fortinet/Luxquanta 협력 |

### 최신 동향 (N-xx)
| 번호 | 출처명 | 발행일 | 제목 | 요약 |
|------|--------|-------|------|------|
| N-01 | The Quantum Insider / Yahoo Finance / Morningstar | 2026-03-02 | Thales sets a world first in quantum-safe security for 5G networks | Thales, 기존 배포 SIM/eSIM OTA PQC 업그레이드 세계 최초 시연. Crypto Agility로 서비스 단절 없음 |
| N-02 | Ubuntu Blog / Canonical | 2026-03 | Building quantum-safe telecom infrastructure for 5G and beyond | coRAN Labs + Canonical, MWC 2026에서 ML-DSA PKI 기반 양자 안전 5G 전 스택 데모 |
| N-03 | MWC Barcelona 공식 | 2026-03 | Post Quantum Cryptography: Readiness, Standardisation and Migration (세션) | MWC 2026 PQC 세션 개최, 2026-03-03 15:00~17:15 |
| N-04 | PR Newswire / The Quantum Insider | 2026-02-25 | Keeper Security Introduces Quantum-Resistant Encryption | Kyber(ML-KEM) + ECC 하이브리드, 백엔드 API·Keeper Commander 배포 완료, 모바일 후속 예정 |
| N-05 | 인사이트코리아 / EZY경제 등 | 2026-02-26 | LG유플러스 MWC 2026 보안 기술 4종 공개 | PQC 광전송, SASE, AI 이상탐지, 암호화 트래픽 공격 탐지 |
| N-06 | IDEMIA / Milipol | 2025-07-18 | IDEMIA and Telefónica showcase Post-Quantum eSIM technology | IoT 스마트 유틸리티 네트워크 대상 PQC eSIM PoC, MWC 2025 |
| N-07 | IDEMIA 보도자료 | 2024-04-22 | IDEMIA Secure Transactions unveils Crypto Agility Solution for PQC | 원격 암호화 업데이트 기능 포함 Crypto Agility 솔루션 |
| N-08 | Quantum Zeitgeist / PR Newswire | 2025-06 | Korea Telecom & HEQA Security Deploy QKD | KT, QKD + PQC 하이브리드 네트워크, 5G 15개 이상 노드, Quantum Korea 2025 |
| N-09 | The Quantum Insider | 2026-02-25 | Numana and Nokia Test Quantum-Safe Network Architecture on Kirq Platform | Nokia, 2026년 Kirq 플랫폼 양자 안전 아키텍처 테스트 확대 |
| N-10 | ZDNet Korea | 2026-03-01 | 갤S26 울트라, 특허로 쌓은 보안 성벽 | 갤럭시 S26 울트라 보안 특허 기술 분석 |

### 글로벌 출처 (G-xx)
| 번호 | 출처명 | 발행일 | 제목 | 관련성 | 신뢰성 | 최신성 | URL |
|------|--------|-------|------|--------|--------|--------|-----|
| G-01 | Technosports | 2026-02 | Exynos 2600 Is the World's First Smartphone Chip With Quantum-Proof Encryption | 5/5 | 3/5 | 5/5 | https://technosports.co.in/exynos-2600-quantum-proof-encryption/ |
| G-02 | Samsung Semiconductor | 2025-12 | Where Trust Begins: Exynos Anchors PQC at Root of Mobile SoCs | 5/5 | 5/5 | 5/5 | https://semiconductor.samsung.com/news-events/tech-blog/where-trust-begins-exynos-anchors-post-quantum-security-at-the-root-of-mobile-socs/ |
| G-03 | The Quantum Space / Futurum | 2025-09 | Post-Quantum Readiness in Semiconductors: Key Industry Insights | 4/5 | 3/5 | 4/5 | https://thequantumspace.org/2025/09/30/quantum-hardware-roundup-september-2025/ |
| G-08 | NIST | 2024-08 | NIST Releases First 3 Finalized Post-Quantum Encryption Standards | 5/5 | 5/5 | 5/5 | https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards |
| G-09 | NIST CSRC | 2024 | FIPS 203 Federal Information Processing Standards Publication | 5/5 | 5/5 | 5/5 | https://csrc.nist.gov/pubs/fips/203/final |
| G-10 | 5G Americas | — | Post Quantum Computing Security | 4/5 | 4/5 | 3/5 | https://www.5gamericas.org/post-quantum-computing-security/ |
| G-11 | postquantum.com | 2025 | Telecom's Quantum-Safe Imperative: Challenges in Adopting PQC | 4/5 | 3/5 | 4/5 | https://postquantum.com/post-quantum/telecom-pqc-challenges/ |
| G-12 | NIST | 2025-03 | NIST Selects HQC as Fifth Algorithm for Post-Quantum Encryption | 5/5 | 5/5 | 5/5 | https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption |
| G-13 | Apple Security Research | 2024-02 | iMessage with PQ3: The new state of the art in quantum-secure messaging | 5/5 | 5/5 | 4/5 | https://security.apple.com/blog/imessage-pq3 |
| G-14 | Google Security Blog | 2024-09 | A new path for Kyber on the web (Chrome ML-KEM 전환) | 5/5 | 5/5 | 4/5 | https://security.googleblog.com/2024/09/a-new-path-for-kyber-on-web.html |
| G-15 | IBM | 2026-01 | IBM and Keyfactor Partner for Enterprise PQC Security | 4/5 | 5/5 | 5/5 | https://thequantuminsider.com/2026/01/22/ibm-keyfactor-partner-enterprise-post-quantum-security/ |
| G-16 | IBM | 2026 | Empowering CIOs to accelerate crypto-agility with IBM Quantum Safe Explorer | 4/5 | 5/5 | 5/5 | https://www.ibm.com/new/product-blog/empowering-cios-to-accelerate-crypto-agility-with-ibm-quantum-safe-explorer |
| G-17 | European Commission | 2025 | A Coordinated Implementation Roadmap for the Transition to PQC | 5/5 | 5/5 | 4/5 | https://digital-strategy.ec.europa.eu/en/library/coordinated-implementation-roadmap-transition-post-quantum-cryptography |
| G-18 | Nokia / Ericsson | 2025-2026 | Embracing PQC in the Quantum Era (Nokia); Quantum technology and mobile network security (Ericsson) | 4/5 | 5/5 | 4/5 | https://www.nokia.com/cybersecurity/post-quantum-cryptography/ |
| G-19 | Cloudflare Blog | 2025-12 | State of the post-quantum Internet in 2025 | 5/5 | 5/5 | 5/5 | https://blog.cloudflare.com/pq-2025/ |
| G-20 | MarketsandMarkets | 2025 | Post-Quantum Cryptography Market ($2.84B by 2030) | 3/5 | 3/5 | 4/5 | https://www.marketsandmarkets.com/PressReleases/post-quantum-cryptography.asp |
| G-21 | IEEE Journals | 2024 | Hardware Acceleration of Crystals-Kyber with RISC-V ISA Extensions | 5/5 | 5/5 | 4/5 | https://ieeexplore.ieee.org/document/10562296/ |
| G-22 | p1sec Blog | — | Post Quantum Cryptography for Mobile Networks | 4/5 | 3/5 | 3/5 | https://www.p1sec.com/blog/post-quantum-cryptography-for-mobile-networks |
| G-23 | Telecom Lead | 2026-03 | Telefonica Unveils 'Quantum Telco' at MWC 2026 | 4/5 | 3/5 | 5/5 | https://telecomlead.com/telecom-services/telefonica-unveils-quantum-telco-at-mwc-2026-to-drive-real-world-quantum-security-and-innovation-124899 |
| G-24 | GitHub (coRAN Labs) | 2025-10 | QORE: Quantum Secure Core — arxiv/GitHub | 5/5 | 4/5 | 5/5 | https://github.com/coranlabs/QORE |
| G-25 | NSA | 2022-09 | Commercial National Security Algorithm Suite 2.0 (CNSA 2.0) | 5/5 | 5/5 | 4/5 | https://media.defense.gov/2025/May/30/2003728741/-1/-1/0/CSA_CNSA_2.0_ALGORITHMS.PDF |

### 학술 논문 (P-xx)
| 번호 | 저자 | 발행년도 | 제목 | 학술지/컨퍼런스 | 인용수 | 핵심 인용 | DOI/URL |
|------|------|---------|------|----------------|--------|----------|---------|
| P-01 | Attema, de Kock 외 | 2025-12 | Post-Quantum Cryptography in the 5G Core | arXiv | — | "The deployment of PQC has a measurable effect on performance, but that this effect is small" | https://arxiv.org/abs/2512.20243 |
| P-02 | (미확인) | 2025-07 | Analysis of PQC in User Equipment in 5G and Beyond | arXiv | — | "ML-KEM with ML-DSA offers the best efficiency for latency-sensitive applications" | https://arxiv.org/abs/2507.17074 |
| P-03 | Yongho Ko 외 2인 | 2025-02-05 | 5G-AKA-HPQC: Hybrid PQC Protocol for 5G Primary Authentication with Forward Secrecy | arXiv | — | ECIES + PQC KEM 하이브리드, SVO Logic + ProVerif 검증 | https://arxiv.org/abs/2502.02851 |
| P-04 | coRAN Labs 팀 | 2025-10 | QORE: Quantum Secure 5G/B5G Core | arXiv | — | "ML-KEM delivers quantum security with only minor performance overhead" | https://arxiv.org/abs/2510.19982 |
| P-05 | (미확인) | 2025-11 | Implementation and performance of PQC for resource constrained consumer electronics | Springer Discover IoT | — | Kyber-512: RSA-2048 대비 키 교환 3배 빠름 | https://link.springer.com/article/10.1007/s43926-025-00238-x |
| P-06 | (미확인) | 2025 | A Practical Performance Benchmark of PQC Across Heterogeneous Computing Environments | MDPI Cryptography 9(2):32 | — | IoT 1~2KB 패킷 제한 → BIKE 단편화 필요 | https://www.mdpi.com/2410-387X/9/2/32 |
| P-07 | (미확인) | 2026-01 | Investigating PQC to Secure Transmitted Data via Mobile Communication | Preprints.org 202601.1876 | — | 격자 기반(Kyber, Dilithium)이 제약 기기에서 최적 균형 | https://www.preprints.org/manuscript/202601.1876 |
| P-08 | Omar Alibrahim (Kuwait University) | 2025-04-23 | Unveiling Samsung Quantum Galaxy: Securing Smartphones With QRNG and PQC | IEEE Access Vol.13 | — | QRNG 활용 미흡, QRNG+PQC 결합 시 보안성 유의미한 향상 | DOI: 10.1109/ACCESS.2025.10974970 |
| P-09 | (미확인) | 2026-01 | Lattice-Based Cryptographic Accelerators for the Post-Quantum Era: Survey | MDPI Electronics 15(2):475 | — | CRYSTALS-Kyber 45%, Dilithium 30%, FPGA 65% 차지 | https://www.mdpi.com/2079-9292/15/2/475 |
| P-10 | (미확인) | 2024 | A Configurable ML-KEM/Kyber Key-Encapsulation Hardware Accelerator Architecture | IEEE Transactions | — | ML-KEM 전용 설정 가능 하드웨어 가속기 | https://ieeexplore.ieee.org/document/10634219/ |
| P-11 | (미확인) | 2024 | Hardware Acceleration of Crystals-Kyber with RISC-V Instruction Set Extensions | IEEE Journals | — | NTT 14.51배, iNTT 16.75배 속도 향상 (180nm CMOS) | https://ieeexplore.ieee.org/document/10562296/ |

### 특허 (T-xx)
> MCP patent-intel 서비스 현재 접근 불가 (VSCode 확장 환경 MCP 미작동). 특허 DB 직접 검색 미수행.
> 향후 patent-intel MCP 활성화 시 재수집 권장: Samsung(S3SSE2A, Exynos PQC), Thales(OTA PQC SIM), IDEMIA(PQC eSIM), LG U+(PQC 광전송) 관련 특허

---

*보고서 작성 기준일: 2026-03-03*
*수집 소스: WebSearch (Google), WebFetch (Samsung Semiconductor Blog, Canonical Blog, SKT Newsroom)*
*MCP 도구 미사용 (research-hub, patent-intel, trend-tracker — 현재 환경 미작동)*
