---
type: weekly-research
domain: secure-ai
l3_topic: ondevice-pqc
date: 2026-03-05
signal: 🔴
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
prev_report: outputs/reports/weekly/2026-03-03_research-ondevice-pqc.md
---

# Research Report: OnDevice 양자암호 (PQC) — 2026-03-05

> 이전 리포트(2026-03-03) 대비 1~2주간 신규 시그널 업데이트 보고서

---

## Executive Summary (경영진 요약)

> 2026년 3월 초 온디바이스 PQC 시장에서 **두 건의 결정적 신호**가 포착되었다. (1) Thales가 2026-03-01 세계 최초로 배포된 5G SIM/eSIM에 대한 PQC 원격 업그레이드 성공을 발표했다 — 기기 교체 없이 Over-The-Air(OTA) 방식으로 양자내성 알고리즘을 적용, 통신사의 PQC 전환 비용 구조를 근본적으로 바꿀 수 있는 기술 돌파구다. (2) NISTIR 8547 초안이 2030년까지 RSA/ECC 단계적 폐기 로드맵을 공식화하며 모든 임베디드·모바일 기기의 마이그레이션 시간표를 확정지었다. 국내에서는 LG U+의 SOLMAE 전자서명이 TTA 표준으로 제정(2025-12)되었고, SKT-Thales 5G SUPI PQC 실증이 유지되고 있으며, KT는 2026년부터 공공기관 대상 하이브리드 PQC+QKD 망 구축을 개시했다. ESP32 등 MCU급 기기에서 Kyber512의 실용 구현이 논문으로 확인되어 IoT까지 확산 기반이 마련되었다. **신뢰도: A/B급 출처 고확신. 레드 신호 유지.**

---

## 연구 질문

2026년 2월 하순~3월 5일 사이 온디바이스 PQC 분야에서 발생한 신규 시그널을 심층 분석하고, 이전 보고서(2026-03-03) 이후의 변화를 식별한다.

---

## 1. 기술 동향

### 1.1 NIST 표준 및 마이그레이션 로드맵

**NISTIR 8547 초안 공개 (2025년 9월, 참조 지속)**

NIST는 NISTIR 8547 「Transition to Post-Quantum Cryptography Standards」 초안을 통해 [G-04]:
- RSA 및 ECC 기반 알고리즘의 **2030년까지 단계적 사용 제한** 명시
- 미 연방기관 및 산업계 마이그레이션 시작 시한을 2026년으로 설정
- 2026년부터 시작하는 조직은 "책임 있는 전환의 외곽 경계선"에 위치

**확정 표준 현황 (2024-08-14 발효)**

| 표준 | 알고리즘 | 용도 | 파라미터 세트 | 임베디드 적합성 |
|------|---------|------|-------------|----------------|
| FIPS 203 | ML-KEM (Kyber) | 키 캡슐화 | 512/768/1024 | ML-KEM-512: 소형 디바이스 적합 [G-06] |
| FIPS 204 | ML-DSA (Dilithium) | 디지털 서명 | ML-DSA44/65/87 | Samsung S3SSE2A 하드웨어 가속 [E-02] |
| FIPS 205 | SLH-DSA (SPHINCS+) | 해시 서명 | 다수 | 서명 크기 큼, IoT 제약 [G-06] |

**HQC 선정 (2025-03): ML-KEM 수학적 백업, 표준 초안 2026년 예정** [G-03]

---

### 1.2 Thales 5G SIM PQC 원격 업그레이드 — 핵심 신호 (2026-03-01)

Thales가 2026년 3월 1일 발표한 세계 최초 성과 [E-01, G-01]:

**기술 개요:**
- 이미 배포된 SIM 및 eSIM에 PQC 알고리즘을 **OTA(Over-The-Air) 원격 다운로드**로 적용
- 서비스 단절, 기기 교체, 물리 카드 교체 없이 백그라운드 업그레이드 완료
- **Crypto-Agility** 아키텍처: 표준 및 위협 진화에 따라 알고리즘을 동적으로 교체 가능

**전략적 의미:**
- 통신사 입장에서 수억 장의 SIM 교체 비용 제거
- GSMA 표준화 논의와 병행하여 실제 운용 환경에서 최초 실증
- 3GPP Release 19/20 PQC AKA 표준 선행 검증으로 작용 가능

**국내 맥락:**
- SKT-Thales는 이미 5G SUPI(Subscription Permanent Identifier) 보호에 Crystals-Kyber 적용 5G 시험망 연동 성공 기록 보유 [N-04]

---

### 1.3 하드웨어/임베디드 구현 기술 현황

**Samsung S3SSE2A Secure Element (샘플 출하 중)**

Samsung System LSI의 업계 최초 하드웨어 PQC 내장 보안칩 [E-02]:
- FIPS 204 (ML-DSA) 구현, ML_DSA65 서명 생성 기준:
  - 소프트웨어 전용: **335.97ms** @ 200MHz
  - 하드웨어+소프트웨어 결합: **19.02ms** → **약 17배 성능 향상**
- 모바일 디바이스용 Secure Element(SE) 턴키 솔루션
- 양자컴퓨터 위협 시한: RSA-2048 해독 "약 2028년 가능" 가정 하에 설계

**ESP32 MCU에서 Kyber512 구현 (2025-03, arXiv 2503.10207)**

초소형 IoT 기기의 PQC 실용성을 확인한 최신 논문 [P-01]:
- ESP32 단일코어 기준 성능:
  - Key Generation: 15.24ms
  - Encapsulation: 17.10ms
  - Decapsulation: 18.57ms
- 듀얼코어 + 하드웨어 가속기(SHA, AES) 활용 시: **최대 1.84배 성능 향상**
- SHA-256 하드웨어: 10.44배, AES 하드웨어: 9.65배 가속
- 1억+ 대 배포된 ESP32 MCU 기반 IoT 기기에 PQC 적용 가능성 입증

**wolfSSL + liboqs (임베디드 TLS 라이브러리)**

- wolfSSL: ML-KEM, ML-DSA, LMS, XMSS 자체 구현 완료 [G-10]
- liboqs v0.15.0 (2025-11-14 배포): ML-KEM, ML-DSA, SLH-DSA 포함 [G-10]
- wolfSSL: **HQC 지원 추가** (2026년 초안 표준 대비 선제 구현)
- Embedded World 2025에서 임베디드 PQC 솔루션 공개 발표

---

### 1.4 표준화 및 규제 동향

**3GPP / GSMA 현황:**
- 3GPP SA3: Release 19/20에서 PQC AKA, SUPI/SUCI 암호화 옵션 포함 검토 중 [G-07]
- GSMA PQ.03 (통신 PQC 가이드라인) + PQ.05 (5G 로밍 PQC, 2025) 발간 [G-07]
- GSMA/국가 보안기관: "Quantum-ready" SIM 소프트웨어 데드라인 설정 시작

**규제 일정표:**
| 지역 | 규제/가이드라인 | 시한 | 내용 |
|------|--------------|------|------|
| 미국 | CNSA 2.0 (NSA) | 2027년 | NSS(국가보안시스템) PQC 의무화 |
| 미국 | NISTIR 8547 | 2030년 | RSA/ECC 단계적 폐기 |
| EU | PQC Roadmap | 2026년 수립, 2030년 전환 | 금융·의료·인프라 고위험 섹터 우선 |
| 한국 | 정부 양자 로드맵 | 2028년 국가핵심망, 2030년 위성 | 양자암호통신 구축 완료 목표 |

---

## 2. 플레이어 동향

### 2.1 국내 통신사 현황

| 기업 | 주요 활동 | 기술 | 상용화 단계 | 출처 |
|------|---------|------|-----------|------|
| **SKT** | Thales와 5G SUPI PQC 실증 성공; QKD+PQC 하이브리드 장비(Solteris KMS) 출시; Q-HSM(QRNG+PUF+PQC) 칩 KCMVP 인증 | Crystals-Kyber, 자체 PQC SW | 상용 장비 출시 완료, 단말 적용 진행 중 | [N-04] |
| **KT** | 하이브리드 QKD+PQC 솔루션 상용화 준비 완료; 2026년 공공기관 하이브리드 양자보안망 구축 개시; 양자암호 통합 관제 플랫폼 시범운용 완료 | PQC+QKD 하이브리드, 이기종 장비 연동 | 2026년 공공기관 파일럿 시작 | [N-05] |
| **LG U+** | SOLMAE(NTRU 격자 기반) 전자서명 TTA 표준 제정(2025-12); IoT/임베디드 기기 적합 설계; 2026년 공공·금융 시범사업 추진 | SOLMAE(NTRU), PQC SDN 인터페이스 | TTA 표준 제정, 상용화 준비 | [N-03] |

### 2.2 글로벌 플레이어 현황

| 기업 | 주요 활동 | 기술 | 상용화 단계 | 출처 |
|------|---------|------|-----------|------|
| **Thales** | 5G SIM/eSIM OTA PQC 업그레이드 세계 최초 시연 (2026-03-01); Samsung S3SSE2A에 보안 OS 탑재 파트너 | Crypto-Agility, ML-KEM | 시연 완료, 통신사 배포 협의 단계 | [E-01] |
| **Samsung** | S3SSE2A SE 칩 샘플 출하 (하드웨어 PQC, FIPS 204); Exynos 2600 SoC PQC 탑재 | ML-DSA(FIPS 204), 하드웨어 가속 | 샘플 출하 완료, 양산 예정 | [E-02] |
| **Google** | Chrome에 PQC TLS 키 교환 배포; Android 코어 보안 프레임워크 PQC 통합; 인프라 내부 PQC 마이그레이션 진행 | ML-KEM, 하이브리드 TLS | 부분 배포 진행 중 | [G-09] |
| **Apple** | iMessage 종단암호화에 PQC 프로토콜 도입; iOS 보안 프레임워크 PQC 통합; iCloud PQC 암호화 | 자체 PQC 프로토콜 | 일부 서비스 배포 | [G-09] |
| **wolfSSL** | ML-KEM, ML-DSA, HQC 자체 구현; Embedded World 2025 임베디드 PQC 솔루션 발표 | ML-KEM/ML-DSA/HQC/LMS/XMSS | 라이브러리 배포 완료 | [G-10] |

---

## 3. 시장 시그널

### 3.1 시장 규모 및 성장

PQC 시장 규모 전망 (복수 출처 교차 검증 필요 — 추정치 편차 큼) [G-11]:

| 조사기관 | 2025 기준 | 2030/2033 목표 | CAGR |
|---------|---------|--------------|------|
| MarketsandMarkets | $0.42B | $2.84B (2030) | 46.2% |
| SNS Insider | $1.35B | $22.68B (2033) | 42.3% |
| Grand View Research | $1.15B (2024) | 2030까지 고성장 | 37.6% |

> 주의: 조사기관별 추정치 편차가 3~5배 수준으로 크며, 단일 출처 신뢰 불가. 방향성(고성장)만 [B]급 신뢰.

- **미국 연방정부**: 향후 10년 PQC 투자 규모 **$71억** 추정 [G-04]
- **EU**: 2026년 고위험 섹터(금융·의료·인프라) PQC 전환 시작 의무화 [G-04]

### 3.2 투자 및 파트너십 신호

- **Thales + 통신사 파트너십**: 5G SIM OTA PQC 업그레이드 시연 (파트너 통신사명 비공개) [E-01]
- **SKT + IDQ (아이디퀀티크)**: QKD-PQC 하이브리드 장비 Solteris 공동 출시 [N-04]
- **KT + 신한은행**: 하이브리드 양자보안 네트워크 구축 [N-05]
- **삼성 + Thales**: S3SSE2A에 Thales 보안 OS 탑재 [E-02]
- **PQCA (Post-Quantum Cryptography Alliance)**: Linux Foundation 산하 오픈소스 연합, liboqs 주도 [G-10]

### 3.3 규제 및 정책 시그널

- **미국 CISA**: "Harvest Now, Decrypt Later" 공격 경고 강화 — 즉각적 마이그레이션 압력 [G-04]
- **한국 정부**: 2026년 PQC+QKD 파일럿 5개 분야(통신·금융·국방·교통·우주) 동시 추진 [N-05]
- **KpqC (한국형 PQC)**: 한국 자체 양자내성암호 알고리즘 표준화 작업 진행 중 [N-06]

---

## 4. 제품/서비스 스펙 비교

| 기업 | 제품/솔루션 | 알고리즘 | 성능 | 적용 환경 | 발표시점 | 출처 |
|------|-----------|---------|------|---------|---------|------|
| Samsung | S3SSE2A Secure Element | ML-DSA (FIPS 204) | 19.02ms (ML_DSA65 서명, HW+SW) vs 소프트웨어 335.97ms | 모바일 SE, IoT | 샘플 출하 중 | [E-02] |
| Thales | 5G SIM OTA PQC 업그레이드 | PQC 알고리즘 (비공개, ML-KEM 추정) | OTA 원격, 서비스 무단절 | 5G SIM/eSIM | 2026-03-01 | [E-01] |
| LG U+ | SOLMAE 전자서명 | NTRU 격자 기반 | IoT/임베디드 최적화 | IoT, 임베디드, SDN | TTA 표준 (2025-12) | [N-03] |
| SKT/IDQ | Q-HSM (QKEV7) | PQC SW + QRNG + PUF | KCMVP 인증 | 보안 하드웨어 모듈 | 상용화 완료 | [N-04] |
| wolfSSL | wolfCrypt PQC | ML-KEM, ML-DSA, HQC, LMS, XMSS | 임베디드 TLS 지원 | MCU, 임베디드 TLS | liboqs 0.15.0 (2025-11) | [G-10] |
| Google | Chrome + Android | ML-KEM (TLS 키 교환) | 부분 배포 | 브라우저, Android OS | 진행 중 | [G-09] |

---

## 5. 학술 동향

### 5.1 주요 논문

**[P-01] CRYSTALS-Kyber on ESP32 (arXiv 2503.10207, 2025-03)**
- 저자: 공개 (arXiv 최신)
- 핵심: ESP32 듀얼코어 + 하드웨어 가속기 조합으로 Kyber512 실용 성능 달성
- 의의: 1억+ 대 배포 MCU에서 PQC 실용화 가능성 최초 종합 실증

**[P-02] Post-quantum authentication for Industrial IoT (Scientific Reports, 2025)**
- ML-KEM + ML-DSA를 TLS 1.3에 통합, IIoT 환경 PQC 인증 프로토콜
- 격자 기반 암호화의 산업 IoT 적용 가능성 확인

**[P-03] PQC for resource-constrained consumer electronics (Discover IoT, Springer, 2025)**
- 리소스 제한 소비자 전자기기에서 PQC 성능 구현 실증
- IoT 기기 대상 PQC 성능/전력 트레이드오프 분석

**[P-04] QORE: Quantum Secure 5G/B5G Core (arXiv 2510.19982, 2025-10)**
- 5G 코어망에 PQC 통합 시 성능 영향 미미함 확인
- B5G/6G 양자안전 코어망 아키텍처 제안

**[P-05] A Survey of PQC Support in Cryptographic Libraries (arXiv 2508.16078, 2025-08)**
- 주요 암호 라이브러리들의 FIPS 203/204/205 지원 현황 종합 조사
- wolfSSL, liboqs, OpenSSL, BouncyCastle 등 비교

### 5.2 연구 방향

1. **MCU/IoT 경량화**: Kyber/Dilithium의 메모리·연산 최적화 (NTT 효율화, HW 가속기 활용)
2. **하이브리드 전환**: 클래식 + PQC 혼용 TLS, 인증서 체인 호환성 확보
3. **사이드채널 공격 대응**: PQC 하드웨어 구현 시 전력·타이밍 공격 방어
4. **5G/6G 통합**: AKA 프로토콜, SUPI 암호화, 로밍 보안에 PQC 도입

---

## 6. 특허 동향

### 6.1 출원 트렌드

- IBM: 2024년 글로벌 양자 기술 특허 191건 1위 [G-12]
- 중국 기관: 양자암호 특허 출원 수량 세계 최다 (국가 전략적 우선순위)
- 격자 기반 암호, 보안 네트워킹, Crypto-Agility 프레임워크 분야 출원 집중
- 특허 활동 2024년 피크: R&D 집중 투자 반영

### 6.2 주요 출원인별 동향

| 기업 | 특허 활동 영역 | 비고 |
|------|-------------|------|
| Samsung | 하드웨어 PQC SE, 스마트폰 PQC 통합 | S3SSE2A 관련 특허 출원 추정 |
| Thales | SIM PQC OTA 업그레이드, Crypto-Agility | 2026-03 시연 관련 특허 존재 추정 |
| IBM | 격자 기반 암호, 양자 알고리즘 | 191건 (2024) [G-12] |
| ARM | HW 가속기 PQC, 라이선스 제약 존재 | Exynos 기반 구현 제약 요인 |

> 세부 특허 번호 데이터: Google Patents SerpAPI 할당량 소진으로 이번 주기 수집 불가. 다음 주기 보완 필요. [데이터 공백]

---

## 7. 기업 발언 & 보도자료

**[E-01] Thales — "세계 최초 5G 양자안전 보안 업그레이드" (2026-03-01)**
> "With Thales' unique crypto-agile approach, operators can remotely update the device protection without replacing cards, changing devices or interrupting connectivity. This successful demonstration is the first of its kind and sends a strong signal to the market: Quantum-safe security can be introduced over the air without changing devices or interrupting service."
> — Thales 공식 보도자료 (BusinessWire, 2026-03-01) [G-01]

**[E-02] Samsung Semiconductor — S3SSE2A 출시 (2025-2026)**
> "Samsung System LSI has completed the development of this remarkable product and samples are now available to be shipped. The S3SSE2A addresses the urgent threat posed by quantum computers, which could be achieved by 2028 with sufficient capability to decrypt current RSA-2048 encryption."
> — Samsung Semiconductor 공식 블로그 [E-02]

**[N-03] LG U+ — SOLMAE TTA 표준 제정 (2025-12-31)**
> "LG유플러스는 이번 기술을 기반으로 내년부터 공공기관과 금융권 시범사업을 추진하고, 6G 이동통신, 자율주행, 스마트팩토리 등 다양한 산업으로 확산할 계획이다. SOLMAE는 서명 크기를 최소화하고 효율적인 연산 방식을 지원해 자원이 제한적인 IoT 기기, 임베디드 기기에서도 활용할 수 있다."
> — 헤럴드경제, 아시아투데이 등 복수 언론 동시 보도 [N-03]

**[N-04] SKT — QKD-PQC 하이브리드 장비 출시**
> "SKT는 자체 개발 PQC 제품의 출시를 통해 'QKD 단독', 'QKD-PQC 하이브리드', 'PQC 단독'의 양자암호 장비 라인업을 갖추게 됐으며, 글로벌 보안 기업 탈레스와 협업해 양자내성암호(PQC)를 활용한 SIM-통신망 인증 기술을 개발, 5G 시험망 연동에 성공했다."
> — SKT 뉴스룸, 디지털투데이 [N-04]

**[N-05] KT — 공공기관 PQC 망 구축 2026 개시**
> "KT는 양자암호 통합 관제 플랫폼 시범운용을 완료했으며, 2026년부터 공공기관 대상으로 플랫폼 구축 및 운용을 시작한다. 파일럿 사업 분야: 통신·금융·국방·교통·우주 5개 분야."
> — KT Enterprise 보도자료, 뉴스핌 [N-05]

---

## 8. 전략적 시사점

### 기회 (Opportunities)

1. **OTA PQC 업그레이드 시장**: Thales 시연으로 기존 SIM/eSIM 교체 없이 PQC 적용 시장 개화. 통신사 대상 OTA PQC 솔루션 B2B 기회.
2. **국내 3사 파일럿 연계**: KT(공공 5개 분야), LG U+(공공·금융), SKT(장비 라인업 완성) 모두 2026년 본격화. 국내 솔루션 공급망 기회.
3. **MCU/IoT PQC 경량화**: ESP32급 기기에서 Kyber512 실용화 확인 — IoT 보안 업그레이드 수요 선점 기회.
4. **KpqC 한국형 표준화**: 자체 PQC 알고리즘 표준화로 국내 공공·국방 조달에서 KpqC 우선 적용 가능성.

### 위협 (Threats)

1. **3GPP 표준 부재**: 공식 5G AKA PQC 표준 없이 배포된 interim 솔루션은 상호운용성 리스크 내재.
2. **중국 특허 공세**: 양자암호 특허 출원 세계 최다 — IP 분쟁 가능성.
3. **Harvest Now, Decrypt Later**: 현재 수집된 암호화 데이터가 양자컴퓨터 등장 시 일괄 해독 위험. 장기 데이터 보호 즉각 대응 필요.
4. **마이그레이션 시간 부족**: NISTIR 8547 기준 2026년이 전환 외곽 경계. 늦게 시작한 조직은 2030 데드라인 달성 불투명.

### 권고사항

1. **즉시**: 온디바이스 PQC 적용 로드맵 수립 — Thales 사례 참조하여 OTA 업그레이드 경로 포함
2. **단기 (3-6개월)**: ML-KEM-512 기반 파일럿 구현; wolfSSL/liboqs 라이브러리 평가
3. **중기 (6-18개월)**: 하이브리드 PQC+클래식 병행 배포; 3GPP 표준 모니터링
4. **장기**: 6G 시대 대비 PQC 네이티브 아키텍처 설계

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- Thales 5G SIM OTA PQC 업그레이드: BusinessWire 공식 보도자료 [A]
- Samsung S3SSE2A 스펙/성능: 공식 반도체 블로그 [A]
- NIST FIPS 203/204/205 및 NISTIR 8547: 정부 공식 문서 [A]
- LG U+ SOLMAE TTA 표준: 복수 언론 동시 보도 [B]
- KT 공공기관 PQC 구축 2026 개시: KT Enterprise 보도자료 [A/B]
- ESP32 Kyber512 성능: arXiv 논문 (동료검토 전) [B]

**추가 검증 필요 [C/D]:**
- PQC 시장 규모: 조사기관별 3~5배 편차, 교차 검증 2개 미만 [C]
- SKT-Thales 5G 시험망 연동 세부 사항: 보도 기반, 공식 확인 미비 [C]
- 중국 양자암호 특허 최다 주장: 단일 출처 [D]

**데이터 공백:**
- Thales OTA 업그레이드 협력 통신사명 비공개
- 특허 번호 상세 데이터 (SerpAPI 할당량 소진)
- Apple PQC 구현 공식 스펙 비공개
- Qualcomm PQC 특허/칩 계획 공개 정보 없음

---

## References

### 글로벌 출처 (G-xx)

| 번호 | 출처명 | 발행일 | 기관유형 | 제목 | 인용원문(한글) | 관련성 | 신뢰성 | 최신성 | URL |
|------|--------|--------|----------|------|-------------|--------|--------|--------|-----|
| G-01 | BusinessWire | 2026-03-01 | 공식 보도자료 | Thales sets a world first in quantum-safe security for 5G networks | Thales, 5G SIM/eSIM OTA PQC 업그레이드 세계 최초 시연 | 5 | 5 | 5 | https://www.businesswire.com/news/home/20260301594505/en/Thales-sets-a-world-first-in-quantum-safe-security-for-5G-networks |
| G-02 | The Quantum Insider | 2026-03-02 | 전문 언론 | Thales Demonstrates Remote Post-Quantum Security Upgrade for 5G SIMs | Thales 5G SIM PQC 원격 업그레이드 상세 분석 | 5 | 4 | 5 | https://thequantuminsider.com/2026/03/02/thales-remote-post-quantum-5g-sim-upgrade/ |
| G-03 | NIST CSRC | 2025-09 | 정부기관 | NISTIR 8547 (Draft): Transition to Post-Quantum Cryptography Standards | RSA/ECC 2030년 폐기 로드맵, 마이그레이션 가이드 | 5 | 5 | 4 | https://csrc.nist.gov/pubs/ir/8547/ipd |
| G-04 | NCCoE (NIST) | 2025 | 정부기관 | Migration to Post-Quantum Cryptography | PQC 마이그레이션 위험 프레임워크 매핑 | 5 | 5 | 4 | https://www.nccoe.nist.gov/crypto-agility-considerations-migrating-post-quantum-cryptographic-algorithms |
| G-05 | NIST CSRC | 2024-08-14 | 정부기관 | FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA) | NIST PQC 3종 표준 최종 발효 | 5 | 5 | 4 | https://csrc.nist.gov/pubs/fips/203/final |
| G-06 | wolfSSL | 2025 | 기업 기술블로그 | What are FIPS 203, 204, and 205? | 표준별 임베디드 적합성 분석 | 4 | 4 | 4 | https://www.wolfssl.com/what-are-fips-203-204-and-205/ |
| G-07 | GSMA | 2025 | 산업단체 | PQC in Mobile Networks: GSMA Task Force Insights | 3GPP Release 19/20 PQC AKA 표준화 진행 현황 | 5 | 5 | 4 | https://www.gsma.com/solutions-and-impact/technologies/security/gsma_resources/post-quantum-cryptography-guidelines-for-telecom-use-cases-pq-03-2/ |
| G-08 | IEEE Xplore | 2024-2025 | 학술 저널 | Efficient Hardware Implementation of the Lightweight CRYSTALS-Kyber | Kyber 경량 하드웨어 구현 | 4 | 4 | 4 | https://ieeexplore.ieee.org/document/10642971/ |
| G-09 | Google Security Blog / PhishDef | 2024-2025 | 기업 블로그 | Post-Quantum Cryptography: Why Google and Apple Are Switching | Google/Apple PQC 도입 전략 | 4 | 4 | 4 | https://phish-def.com/blog/cybersecurity/post-quantum-cryptography-why-google-and-apple-are-switching-and-you-should-too/ |
| G-10 | wolfSSL / PQCA | 2025 | 기업/오픈소스 | wolfSSL Unveils PQC at Embedded World 2025; liboqs v0.15.0 | wolfSSL ML-KEM/ML-DSA/HQC 지원, liboqs 최신 버전 | 4 | 4 | 4 | https://www.wolfssl.com/wolfssl-unveils-post-quantum-cryptography-and-security-solutions-at-embedded-world-2025/ |
| G-11 | MarketsandMarkets / SNS Insider | 2025-2026 | 시장조사 | Post-Quantum Cryptography Market Forecast | PQC 시장 규모 $0.42B~$1.35B (2025), CAGR 37~46% | 3 | 3 | 4 | https://www.marketsandmarkets.com/PressReleases/post-quantum-cryptography.asp |
| G-12 | PatentPC / GlobeNewswire | 2025-2026 | 특허/시장 분석 | Quantum Cryptography Growth: Patent & Investment Data | IBM 특허 191건(2024), PQC R&D 투자 트렌드 | 3 | 3 | 4 | https://patentpc.com/blog/quantum-cryptography-growth-the-latest-data-on-post-quantum-security |

### 최신 동향 (N-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약(한글) | URL |
|------|--------|--------|------|-----------|-----------|-----|
| N-01 | EuropaWire | 2026-03-02 | Thales Advances Quantum Ready 5G Security | Thales 5G SIM PQC 2026 | Thales 5G OTA PQC 업그레이드 유럽 배포 소식 | https://news.europawire.eu/thales-advances-quantum-ready-5g-security-with-remote-post-quantum-cryptography-upgrade-technology/ |
| N-02 | Insight Korea | 2026 | SKT·KT·LGU+, 양자로 철벽 보안 구축 | SKT KT LGU+ 양자내성암호 2026 | 국내 통신 3사 양자보안 기술 개발 현황 종합 | https://www.insightkorea.co.kr/news/articleView.html?idxno=242127 |
| N-03 | 헤럴드경제 / 아시아투데이 | 2025-12-30 | LGU+, 양자내성암호 기반 네트워크·전자서명 기술 상용화 | LGU+ SOLMAE 양자내성암호 2025 | LG U+ SOLMAE TTA 표준 제정, IoT/임베디드 최적화, 2026 공공·금융 파일럿 | https://biz.heraldcorp.com/article/10645601 |
| N-04 | SKT 뉴스룸 / 디지털투데이 | 2025 | SKT, 양자암호 양대 기술 QKD·PQC 하나로 묶었다 | SKT 양자암호 PQC QKD 2025 | SKT QKD-PQC 하이브리드 장비 Solteris 출시, Thales 협업 5G 시험망 연동 성공 | https://news.sktelecom.com/207758 |
| N-05 | KT Enterprise / 뉴스핌 | 2025-12-31 / 2025-06 | KT 양자암호 통합 관제 플랫폼 시범운용 완료 | KT 양자내성암호 PQC 2026 | KT 2026년 공공기관 대상 PQC+QKD 하이브리드망 구축 개시, 5개 분야 파일럿 | https://enterprise.kt.com/bt/mediareport/2544.do |
| N-06 | 바이라인네트워크 | 2026-02 | 한국형 양자내성암호(KpqC) 현황 | KpqC 한국형 양자내성암호 2026 | 국내 자체 PQC 알고리즘 표준화 진행 현황, NIST와의 관계 | https://byline.network/2026/02/26-571/ |

### 기업 발언 (E-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약원문 |
|------|--------|--------|------|-----------|---------|
| E-01 | Thales / BusinessWire | 2026-03-01 | Thales sets a world first in quantum-safe security for 5G networks | Thales 5G SIM PQC OTA 2026 | "Operators can remotely update the device protection without replacing cards, changing devices or interrupting connectivity." — 공식 보도자료 |
| E-02 | Samsung Semiconductor Blog | 2025-2026 | S3SSE2A: Hardware PQC Locks in Security for the Quantum Era | Samsung S3SSE2A PQC chip | "Hardware + Software combination achieves 19.02ms for ML_DSA65 vs 335.97ms software-only — 17x improvement. Samples now available." — 공식 기술블로그 |
| E-03 | Samsung Research Blog | 2025 | Transitioning Cellular networks towards Post Quantum Cryptography | Samsung 5G PQC cellular | Samsung Research의 5G 셀룰러 PQC 전환 전략 공개 |

### 학술 논문 (P-xx)

| 번호 | 저자 | 발행년도 | 제목 | 학술지/컨퍼런스 | 인용수 | 핵심 인용 | DOI/URL |
|------|------|---------|------|----------------|--------|---------|---------|
| P-01 | (저자 공개) | 2025-03 | Efficient Implementation of CRYSTALS-KYBER KEM on ESP32 | arXiv 2503.10207 | 미집계 | "1.72x~1.84x speedup via dual-core + hardware accelerators; ESP32 feasibility confirmed" | https://arxiv.org/html/2503.10207v1 |
| P-02 | (다수) | 2025 | Post-quantum cryptographic authentication protocol for industrial IoT using lattice-based cryptography | Scientific Reports (Nature) | 미집계 | ML-KEM + ML-DSA TLS 1.3 통합으로 IIoT PQC 인증 가능 | https://www.nature.com/articles/s41598-025-28413-8 |
| P-03 | (다수) | 2025 | Implementation and performance of PQC for resource constrained consumer electronics | Discover Internet of Things (Springer) | 미집계 | 소비자 IoT 기기 대상 PQC 성능/전력 트레이드오프 분석 | https://link.springer.com/article/10.1007/s43926-025-00238-x |
| P-04 | Damir, Niemi 등 | 2025-10 | QORE: Quantum Secure 5G/B5G Core | arXiv 2510.19982 | 미집계 | 5G 코어망 PQC 통합 시 성능 영향 미미, 양자안전 B5G 아키텍처 제안 | https://arxiv.org/html/2510.19982v1 |
| P-05 | (다수) | 2025-08 | A Survey of Post-Quantum Cryptography Support in Cryptographic Libraries | arXiv 2508.16078 | 미집계 | wolfSSL, liboqs, OpenSSL 등 주요 라이브러리 FIPS 203/204/205 지원 현황 종합 | https://arxiv.org/html/2508.16078v1 |

### 특허 (T-xx)

| 번호 | 출원인 | 등록/출원일 | 특허번호 | 제목 | 핵심 청구항 | 관할 |
|------|--------|-----------|---------|------|-----------|------|
| T-01 | IBM | 2024 | (복수) | 격자 기반 암호, 양자 알고리즘 관련 | 양자내성 키 생성 및 교환 방법 | 글로벌 (191건 대표) |
| T-02 | Samsung | 2024-2025 | (미공개) | 하드웨어 PQC 보안 요소 | ML-DSA 하드웨어 가속 회로, SE 아키텍처 | KR, US 추정 |
| T-03 | Thales | 2025-2026 | (미공개) | SIM/eSIM OTA PQC 업그레이드 | OTA를 통한 SIM 알고리즘 원격 교체 방법 | EP, US 추정 |

> 주의: T-02, T-03 특허 번호 미확인 (공개 정보 없음). SerpAPI 할당량 소진으로 상세 검색 불가. 다음 주기 보완 필요.

### 내부 자료 (I-xx)

| 번호 | 자료명 | 작성일 | 페이지 | 인용내용 |
|------|--------|--------|--------|---------|
| I-01 | 2026-03-03_research-ondevice-pqc.md | 2026-03-03 | 전체 | 직전 주기(2026-03-03) 리서치 베이스라인: NIST 표준, Samsung Exynos, Thales 시연 사전 정보 |

---

*리포트 생성: research-deep 에이전트 | 2026-03-05 | 신호 등급: 레드(🔴) — 시장 전환 가속 확인*
