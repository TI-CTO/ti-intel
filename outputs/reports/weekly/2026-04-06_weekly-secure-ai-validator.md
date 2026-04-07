---
validator_status: partial
target_file: outputs/reports/weekly/2026-04-06_weekly-secure-ai.md
verified_at: 2026-04-06
---

# Validation Report — 2026-04-06_weekly-secure-ai.md

## 요약
- **상태**: PARTIAL (조건부 통과)
- **주요 이슈**:
  - Critical 4건: (1) Google 논문 "9분" 표현 원문 불일치, (2) 캐나다 PQC 의무화 "법적 의무" 과장 표현, (3) Adaptive Security 누적 조달액 불일치($146.5M vs. 원본 $136M), (4) G-15 CRQC 큐비트 하향 추이 수치 불일치
  - Minor 5건: G-01 Ethereum Foundation 공동 저술 표현 과대, P-01 저자명 오기재(Janssen et al.→Chhetri 외), Oratomic 출범 날짜 오기재(3/31→3/30), G-13 Justin Drake 접근 불가, G-32 Security Boulevard 403 오류
  - 고아 소스: G-28(Zama $1B MEXC 블로그)이 본문에서 직접 인용되지 않음

---

## 1. 인용 검증

| 항목 | 결과 | 비고 |
|------|------|------|
| References 테이블 존재 | ✅ | G/P/E계열 통합 테이블 |
| 모든 [N] 인용 매칭 | ✅ | 본문 인용 코드 전수 교차 확인: G-01~G-46, P-01~P-05, E-01~E-09 모두 References 등재 확인 |
| 고아 소스 (References 등재 → 본문 미인용) | ⚠️ | G-28(MEXC Zama $1B) — 본문에서 직접 인용 없음. 플레이어 테이블에 "유니콘 지위"만 언급되어 출처 표기 필요 |
| 미인용 주장 | ⚠️ | "Apple·AWS·Google FHE.org 후원 진입"(전략적 시사점) — 인용 코드 없음. G-27(Zama 블로그)에 스폰서 정보 없음 |

---

## 2. 수치 검증

| 수치 | 소스 수 | 판정 | 비고 |
|------|---------|------|------|
| PQC 시장 2026년 $12억 → 2035년 $130억, CAGR 30% | 1 (G-12 Juniper) | [B] | 원본 확인: $1.2B→$13B, CAGR 30% 일치 |
| FHE 시장 2024년 $12억 → 2033년 $84억, CAGR 30% | 1 (G-31 MRI) | [C] | 원본 확인: $1.2B→$8.4B, CAGR 30% 일치. 단, 종료 연도가 본문 "2033년"으로 정확함 |
| INTERPOL $442B 사기 손실, 47개국 행동계획 | 2 (G-36, G-37) | [A] | 양쪽 공식 출처 확인. GASA 추정치 기준 명시됨 |
| 딥페이크 비싱 사건당 평균 $600K, 10%+ $1M 초과 | 1 (G-43) | [C] | G-43(CX Today) 원본 확인. Group-IB/Regula Forensics 설문 재인용 수치 |
| AI 사기 손실 2023년 $12.3B → 2027년 $40B(Deloitte) | 1 (G-38) | [B] | Help Net Security 원본 확인. Deloitte 출처 명시됨 |
| ML-KEM-512 키 교환 35.7ms·2.83mJ, ECDH P-256 대비 17배 | 1 (P-01) | [A] | arXiv 원본 확인. 수치 일치. 단, 저자 Janssen et al. 오기재 (아래 상세) |
| ML-DSA 서명 99퍼센타일 최대 1,125ms | 1 (P-01) | [A] | arXiv 원본 확인. 수치 일치 |
| RAG 사기 탐지 정확도 97.98%, F1 97.44% | 1 (P-03) | [A] | arXiv 원본 확인. 수치 일치 |
| Pindrop: 2초 탐지, 99% 정확도, 370+ TTS, 2,000만+ 오디오 | 1 (G-34) | [B] | Pindrop 제품 페이지 원본 확인. 수치 일치 |
| Adaptive Security $81M Series B, 누적 $146.5M | 1 (G-44) | ❌ | G-44(BankInfoSecurity) 원본은 누적 $136M. WebSearch로 확인한 공식 보도자료(PR Newswire)는 $146.5M. G-44가 $136M으로 잘못 계산한 것으로 추정. 공식 출처 교체 필요 |
| Zama 유니콘 지위 | 1 (G-28 MEXC 블로그) | [C] | G-28(MEXC 블로그) 원본 확인: $57M+로 유니콘 주장하나 [C] 등급 출처. 본문 직접 인용 없이 플레이어 테이블에만 언급 |
| Niobium 누적 $2,300만+ | 미인용 주장 | ⚠️ | SiliconANGLE(G-17)에 펀딩 정보 없음. E-06(PR Newswire) 원본에도 조달액 미기재 |
| Naoris Protocol 시총 $36M | 1 (G-08) | ⚠️ | G-08(The Quantum Insider) 원본에 시총 미기재 |
| Google ECDLP 20배 감소(Litinski 900만 큐비트 기준) | 1 (G-01) | [B] | G-01 원본: "approximately 20-fold reduction" 확인. 단, Litinski 900만 큐비트 기준은 G-01에 없음 |
| CRQC 큐비트 추이 900만→100만→50만/1만 | 1 (G-15) | ❌ | G-15 원본 실제 추이: 2천만(2019)→100만 미만(2025-05)→10만 미만(2026-02)→50만 미만(2026-03, ECC 기준). 본문의 "900만→100만→50만/1만" 수치가 원본과 전면 불일치 |
| 40% 조직 PQC 전환 진행 중, 실제 배포 5% | 1 (G-14, Security Boulevard 403) | ⚠️ | G-14 접근 불가(403). WebSearch로 Entrust/Ponemon 2026 보고서 존재 확인: 미국 40% 준비 중 수치 부합. 단, 5% 배포 완료는 DigiCert 조사 수치이며 Entrust/Ponemon과 혼용 가능성 |

---

## 보강 필요 항목 (reinforcement_needed)

```yaml
reinforcement_needed:
  - claim: "CRQC 필요 자원 추정치 3개월 내 3편 논문으로 연속 하향: 900만 → 100만 → 50만/1만 큐비트"
    current_sources: 1 (G-15)
    issue: "수치 불일치. G-15 원본의 실제 추이는 2천만(2019)→100만 미만(2025-05)→10만 미만(2026-02)→50만 미만(2026-03)임. 900만은 원본에 없는 수치."
    suggested_keywords: ["Litinski 2023 qubit estimate", "Iceberg Quantum 100000 qubits", "three quantum papers 2025 2026 CRQC timeline"]

  - claim: "Adaptive Security 누적 $146.5M 조달"
    current_sources: 1 (G-44 BankInfoSecurity)
    issue: "G-44 원본은 $136M. 공식 PR Newswire 보도자료(adaptivesecurity.com/blog/adaptive-raises-series-b)는 $146.5M. G-44를 공식 보도자료 URL로 교체 필요."
    suggested_keywords: ["Adaptive Security Series B $81M total raised 146.5 million"]

  - claim: "Naoris Protocol 시총 $36M"
    current_sources: 0 (G-08에 없음)
    issue: "인용 출처(G-08)에 해당 수치 없음."
    suggested_keywords: ["Naoris Protocol NAORIS token market cap 36 million"]

  - claim: "Niobium 누적 $2,300만+"
    current_sources: 0 (G-17, E-06 모두 해당 수치 없음)
    issue: "References 어디에도 이 수치의 근거가 없음."
    suggested_keywords: ["Niobium Microsystems funding raised million"]

  - claim: "Apple·AWS·Google FHE.org 후원 진입"
    current_sources: 0 (인용 코드 없음)
    issue: "전략적 시사점 섹션에 인용 코드 없음. G-27(Zama 블로그)에 스폰서 정보 없음."
    suggested_keywords: ["FHE.org 2026 Taipei conference sponsors Apple AWS Google"]

  - claim: "4/1 이후 체결하는 디지털 요소 포함 계약 전체에 PQC 조달 조항 의무화"
    current_sources: 1 (E-04 CCCS)
    issue: "E-04(CCCS 공식 문서) 원본은 권장 로드맵이며 의무 조달은 조건부 기술. G-04(PQShield) 403 접근 불가로 대조 미확인."
    suggested_keywords: ["Canada CCCS ITSM.40.001 PQC procurement mandatory April 2026"]
```

---

## 5. URL-Content 검증

| # | URL 상태 | 본문 주장 | 판정 | 비고 |
|---|---------|---------|------|------|
| G-01 | 200 OK | Google 논문: <50만 큐비트, 9분 내 개인키 복원, 20배 감소, Ethereum Foundation·Stanford 공동 저술 | ⚠️ 부분 일치 | "fewer than 500,000 qubits"와 "20-fold reduction"은 확인. 단, "9분"은 원문 "a few minutes"이며 구체적 시간 미기재. "Ethereum Foundation·Stanford 공동 저술"은 과장 — 원문은 협력기관, 공동저자 아님 |
| G-02 | 200 OK | Oratomic 출범 3/31, 10,000 중성원자 큐비트, qLDPC 아키텍처, Bluvstein·Preskill·Endres 창업팀 | ⚠️ 부분 일치 | 창업팀·10,000 큐비트 확인. qLDPC 미언급. 날짜는 G-02(The Quantum Insider)에서 3/31로 기재했으나 E-05(공식 보도자료)는 3/30 — 날짜 오기재 가능성 |
| G-04 | 200 OK (PQShield 블로그) | 캐나다 2031/2035 의무화, 4/1 이후 PQC 조달 조항 의무화 | ⚠️ 부분 일치 | 2031/2035 타임라인 확인. PQC 조달 조항 의무화는 블로그 원문에 명시 없음 |
| G-06 | 200 OK (NIST 메타페이지) | RSA/ECDSA 2030 deprecated, 2035 disallowed, FIPS 203/204/205 대체 표준 | 🔗 접근 불가 (내용) | NIST CSRC 페이지는 메타데이터만 반환. 실제 PDF 내용 확인 불가. 주장은 NIST 공식 입장과 부합하므로 [A] 유지 가능하나 직접 검증 불가 |
| G-07 | 403 | Cisco IOS XE 26 전체 스택 PQC | 🔗 접근 불가 | E-02(Cisco 공식 블로그)로 대체 검증: 4계층 PQC 구조 전면 확인 |
| G-08 | 200 OK | Naoris ML-DSA 메인넷, 1억600만 트랜잭션, 6억300만 위협 차단, $36M 시총 | ⚠️ 부분 일치 | 트랜잭션·위협 차단 수치 확인. FIPS 204(ML-DSA) 구체 알고리즘 미기재(NIST-approved만 언급). $36M 시총 없음 |
| G-09 | 200 OK | Quantum XChange Phio TX 2026 PQC 금상 | ✅ 일치 | 상 내용 및 크립토-어질리티 인정 확인 |
| G-10 | 200 OK | BTQ BIP-360 테스트넷 v0.3.0, P2MR 합의, Dilithium opcode 활성화 | ✅ 일치 | 전부 확인 |
| G-11 | 404 | BIP-360 공동 저자 "비트코인 완전 양자내성 전환에 7년 소요" | 🔗 접근 불가 | CoinTelegraph 404. WebSearch 대체 확인 필요 |
| G-12 | 200 OK | PQC 시장 2026년 $12억 → 2035년 $130억, CAGR 30% | ✅ 일치 | Juniper Research 원본 수치 일치 |
| G-13 | 403 | Justin Drake "기념비적인 날" 발언 | 🔗 접근 불가 | CoinDesk 403. 발언 출처 독립 검증 불가 |
| G-14 | 403 | 40% PQC 전환 진행 중, 5% 배포 완료, 40% 웹사이트 하이브리드 지원 | 🔗 접근 불가 | Security Boulevard 403. WebSearch로 Entrust/Ponemon 40% 확인, 5%는 DigiCert 출처로 Entrust와 혼용 가능성 |
| G-15 | 200 OK | CRQC 큐비트 3개월 3편 연속 하향: 900만→100만→50만/1만 | ❌ 불일치 | 원본 실제 추이: 2천만(2019)→100만 미만(2025-05)→10만 미만(2026-02)→50만 미만(2026-03). 본문 "900만"은 원문에 없는 수치. "1만"은 Oratomic 큐비트 수치로 동일 추이에 혼입된 것으로 추정 |
| G-17 | 200 OK | Niobium The Fog: 4/2 베타, mistic Core FPGA GPU 2×, 3개 프리빌드 앱, Samsung 8nm ASIC, Q2 공개 목표 | ⚠️ 부분 일치 | 베타·가속기·프리빌드 앱·Samsung 협력 확인. 8nm 공정 명시는 SiliconANGLE에 없음(E-06에도 없음, G-26에서 확인). $2,300만 누적 조달액 G-17·E-06 어디에도 없음 |
| G-19 | 200 OK | CryptoLab GS 1등급, ~99% 정확도, 1.9초 TTFT, 6월 조달청, CC EAL2 | ✅ 일치 | 7/8 항목 확인. Gartner 선정만 해당 기사에 없음 (G-20 별도 기사에 있음) |
| G-21 | 200 OK | NIST MPTS 2026 Threshold FHE from CKKS, Damien Stehlé, 분산 키 생성 | ✅ 일치 | 전부 확인 |
| G-23 | 200 OK (IEEE Spectrum) | Intel Heracles 1,074~5,547×, 197mm², 176W, 3nm, 48GB HBM | ⚠️ 부분 일치 | 칩 이름·가속 수치는 G-24(Tom's Hardware)에서 확인. IEEE Spectrum 페이지에 세부 스펙 미포함. Tom's Hardware(G-24) WebFetch에서도 수치 확인(헤드라인 기준 1,074~5,547× 확인) |
| G-25 | 200 OK | LG U+·CryptoLab MWC, ixi-O AICC 동형암호, CKKS+ 온디바이스, "실시간 지연 없이" | ⚠️ 부분 일치 | "ixi-O" 명칭 직접 언급 없음(기사는 "Xio"와 "AICC"를 분리 기술). 나머지 확인 |
| G-26 | 200 OK | SemiFive·Niobium FHE ASIC 수주, Samsung Foundry 8nm | ✅ 일치 | Samsung 8nm(8LPU) 확인. 계약 규모 $6.86M 기재 |
| G-27 | 200 OK | Zama FHE.org 2026 8건 발표, TFHE GPU 서브밀리초 | ✅ 일치 | 3 talks + 5 posters = 8건. Sub-Millisecond TFHE Bootstrapping on GPU 확인. 유니콘 지위는 미언급 |
| G-28 | 200 OK (MEXC 블로그) | Zama $1B 유니콘 (플레이어 테이블 주석) | ⚠️ 부분 일치 | 블로그 유니콘 주장 존재. 단, [C] 등급 소스 + 본문 직접 인용 없음 (G-28 고아 소스) |
| G-31 | 200 OK | FHE 시장 2024년 $12억→2033년 $84억, CAGR 30% | ✅ 일치 | 수치 일치. 종료 연도 2033년으로 정확 |
| G-33 | 200 OK (Experian) | Agentic AI 사기 독립 위협 범주, Identity Farm 800점대 신용점수 | ⚠️ 부분 일치 | Agentic AI 위협 범주화 확인. Identity Farm 800점대 생성 미언급. Sardine AI 미언급 |
| G-34 | 200 OK | Pindrop Pulse 2초 99% 탐지, 370+ TTS, 2,000만+ 오디오, 오탐 1% | ✅ 일치 | 전부 확인 |
| G-36 | 200 OK | INTERPOL $442B, 47개국, GASA 추정치 | ✅ 일치 | 전부 확인. AI 사기 4.5x 수익성은 미언급 |
| G-37 | 404 | UNODC $442B, 47개국 | 🔗 접근 불가 | UNODC 404. G-36으로 동일 이벤트 내용 검증 가능 |
| G-38 | 200 OK | ABA 20개 권고안, FIDO 패스키, 디지털 여권, IRS/USPS 신원 검증, Deloitte $12.3B→$40B | ✅ 일치 | 전부 확인 |
| G-43 | 200 OK | 딥페이크 비싱 평균 $600K, 10%+ $1M 초과 | ✅ 일치 | Group-IB/Regula 설문 수치로 재인용 확인 |
| G-44 | 200 OK | Adaptive Security $81M Series B, Bain Capital·NVIDIA·OpenAI·a16z, 누적 $146.5M | ⚠️ 부분 일치 | G-44(BankInfoSecurity) 원본은 누적 $136M. NVIDIA NVentures는 G-44에 미기재. WebSearch로 공식 보도자료(PR Newswire) 기준 $146.5M, NVIDIA NVentures 참여 확인. G-44가 불완전 소스 |
| E-01 | 접근 불가 (PDF binary) | Google 논문 공동 저술팀 및 핵심 주장 | 🔗 PDF binary | PDF 내용 직접 확인 불가 |
| E-02 | 200 OK | Cisco IOS XE 26 전체 스택 PQC 4계층, C9000, IPsec/MACsec, "업계 최초" | ✅ 일치 | 전부 확인 |
| E-03 | 200 OK | PQShield CRQC 4단계 프레임워크, Google·Oratomic 상호보완 평가 | ✅ 일치 | 확인 |
| E-04 | 200 OK | CCCS ITSM.40.001, 2031/2035 타임라인 | ⚠️ 부분 일치 | 2031/2035 확인. "법적 의무화" 표현은 원문이 권장 로드맵 성격임을 명시 (TBS 정책 수단 별도 발급 예정) |
| E-05 | 200 OK (Oratomic 공식) | Oratomic 출범 날짜 3/31 | ❌ 불일치 | 공식 보도자료 날짜: "March 30, 2026" (3/30). 본문은 3/31로 기재 |
| E-06 | 200 OK (PR Newswire) | Niobium The Fog: Kevin Yoder CEO 발언, mistic Core FPGA 2×, Q2 2026 목표 | ✅ 일치 | 8nm 명시 없음은 앞서 확인. CEO 발언·가속기·일정 확인 |
| E-07 | 200 OK (유니콘팩토리) | CryptoLab GS 1등급, OWASP LLM Top 10 방어, 조달청 진입 | ✅ 일치 | Gartner 미언급은 G-20에서 별도 확인 |
| E-09 | 200 OK | LG U+·CryptoLab CKKS+ 온디바이스, "실시간 지연 없이" | ✅ 일치 | CEO 발언 및 협력 내용 확인 |
| P-01 | 200 OK | Janssen et al., ML-KEM-512 35.7ms·2.83mJ, ECDH 17배, ML-DSA 99p 1,125ms | ⚠️ 부분 일치 | 수치 전부 확인. 저자명이 "Janssen et al."로 표기되었으나 arXiv 원본 첫 번째 저자는 "Rojin Chhetri". References 테이블에도 "Janssen et al."로 표기됨 — 저자명 오기재 |
| P-02 | 403 | Park et al. THED: Threshold Dilithium from FHE | 🔗 접근 불가 | IACR ePrint PDF 403. 논문 제목·저자 직접 확인 불가 |
| P-03 | 200 OK | Singh et al., RAG 97.98% 정확도, F1 97.44%, 재학습 불필요 | ✅ 일치 | 전부 확인 |
| P-04 | 200 OK | Bhatti et al., 37.5% 구분 능력, 75% 오분류, 철회 상태 | ✅ 일치 | 전부 확인 |
| P-05 | 418 | IEEE 2026 에이전트형 AI 보이스피싱 탐지 | 🔗 접근 불가 | IEEE Xplore 418 오류 |

---

## 3. 논리 검증

**PASS 항목:**
- On-Device PQC 섹션: Google 논문 → CRQC 위협 가속화 → 통신사 대응 시급성의 논리 흐름 타당
- FHE 섹션: Niobium·CryptoLab·Intel Heracles의 소프트웨어/인증/하드웨어 3축 동시화를 "플랫폼 시대 개막"으로 서술 — 근거-결론 부합
- 스팸/피싱 섹션: INTERPOL 공조 + ABA 정책 + IEEE 2026 → 규제 국제화 결론 타당

**이슈:**
- "대기업 마이그레이션 12~15년 이상 소요" — 인용 코드 없음(출처 표기가 인라인 텍스트로만 "postquantum.com" 기재). References 테이블 미등재 소스
- "LLM 피싱 자동화로 공격 비용 95% 절감" — 인용 코드 없음. 수치 근거 불명확

---

## 4. 편향 검증

**PASS:**
- PQC 섹션: Google·Oratomic 논문의 위협 가속화를 기술하면서, ML-DSA 서명 99p 지연 1,125ms 등 실용화 리스크도 함께 서술
- FHE 섹션: Intel Heracles 양산 미발표 리스크, CKKS 표준화 미완료 등 균형 있게 기술
- 스팸/피싱 섹션: 탐지-생성 군비경쟁 문제를 커뮤니티 시그널로 포함, 방어 한계 인정

**소주의:**
- Naoris Protocol 시총 $36M 및 Niobium $2,300만 조달액이 인용 근거 없이 수치로만 제시됨 — 신뢰도 판단 어려운 수치의 독립 확인 표시 필요

---

## 결론

이 리포트는 전반적으로 복수의 공식 출처(INTERPOL, NIST, Cisco 공식 블로그, arXiv 논문 등)를 적절히 활용했으며, 주요 수치의 상당수가 원본과 일치한다. 다만 4건의 Critical 이슈가 발견되었다: (1) Google 논문의 "9분" 개인키 복원은 원문 "a few minutes"의 수치 구체화로 원문 미지지, (2) CRQC 큐비트 하향 추이 "900만"은 G-15 원본에 없는 수치, (3) Adaptive Security 누적 조달액이 인용 출처($136M)와 공식 보도자료($146.5M) 간 불일치, (4) 캐나다 PQC "법적 의무화" 표현이 원문 권장 로드맵 성격을 과장함. 추가로 P-01 저자 "Janssen et al."이 실제 첫 번째 저자 "Chhetri"와 불일치하며, Oratomic 출범 날짜가 3/31(본문)→3/30(공식 보도자료)로 오기재되어 있다. G-37·G-11(404), G-07·G-13·G-14·G-32(403), P-02·P-05(403/418) 등 접근 불가 URL 8건이 검증 공백으로 남았으나, 동일 이벤트를 인용하는 대체 소스들을 통해 주요 주장은 교차 검증되었다.
