---
type: weekly-monitor
domain: secure-ai
week: 2026-W14
date: 2026-03-30
l3_count: 5
deep_count: 2
---

# 주간 기술 동향: Secure AI (2026-W14)

## Executive Summary

> **이번 주 핵심**: Google이 2029 PQC 마이그레이션 데드라인을 선언하며 Android 17에 ML-DSA를 전면 탑재(3/25-26). 빅테크가 규제보다 빠른 속도로 양자안전 전환을 주도하는 구도가 공식화됨. 동형암호 측에서는 "Privacy at your Fingertips" 논문이 클라이언트 측 FHE 오버헤드 97% 감소를 달성해 온디바이스 키워드 검색 실용화 임계점에 접근.

| Layer 2 | 세부기술 | 신호 | 핵심 내용 |
|---------|----------|------|----------|
| 양자/동형 암호 | On-Device PQC | 🔴 | [제품출시] Google 2029 PQC 데드라인 선언, Android 17 ML-DSA 4계층 통합 · [생태계] IBM+Signal+Threema 대역폭 100× 증가 문제 정량화 |
| | On-Device 동형암호 | 🟡 | [논문] "Privacy at your Fingertips" 클라이언트 FHE 오버헤드 97% 감소 · [생태계] Zama+T-REX $32B RWA FHE 기밀성 레이어 |
| | Secure Vector Search | 🟢 | 구조적 변화 없음. IronCore Labs 벡터 암호화 논의 지속 |
| 스팸/피싱탐지 | 스팸/피싱 감지(통화전) | 🟡 | [생태계] Meta 안티스캠 AI 도구 출시(3월) · AI 피싱 204% 급증 보고 |
| | OCR 이미지 스팸 차단 | 🟢 | 신규 시그널 없음. Gmail RETVec 체계 유지 |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음
> **태그** : [기술돌파] [제품출시] [경쟁사] [규제] [투자] [논문] [생태계]

---

## 🟢 Quick 요약 (변화 미미)

### Secure Vector Search
- PHE 벡터 유사도 연구(arXiv 2503.05850) 지속 인용. IronCore Labs가 AI 임베딩 벡터 암호화 솔루션 논의 확산. Nature Scientific Reports에 프라이버시 보존 멀티모달 검색 논문 발표. 상용 돌파 없음.

### OCR 활용 이미지 스팸 차단
- Gmail RETVec + Gemini Nano 온디바이스 보호 체계 유지. 학계에서 XAI 기반 CNN 스팸 이미지 탐지 97.16% 정확도 달성(기존 연구). 이번 주 신규 시그널 없음.

---

## 🟡🔴 Deep 심층 분석

### On-Device PQC (양자내성암호) — 🔴 긴급

#### 이전 대비 변화
- 전주: ZeroTier Quantum RSAC 출시(3/23), Kudelski KSE3 PQC 반도체 IP, Thales 5G SIM OTA PQC 업그레이드, FIPS 140-2 D-180 카운트다운
- 금주: Google 2029 PQC 데드라인 선언(3/25) + Android 17 ML-DSA 전면 탑재(3/26). IBM+Signal+Threema 대역폭 100× 문제 정량화
- 변화 방향: 하드웨어 IP 레벨(KSE3)에서 **모바일 OS 레벨**(Android 17)로 PQC 구현이 플랫폼 전반에 확산. 빅테크가 규제보다 빠르게 전환 추진

#### 기술 동향

1. **Google 2029 PQC 마이그레이션 데드라인 — NIST 2030보다 1년, NSA 2033보다 4년 앞당김.**
   Google은 "Quantum Frontiers May Be Closer Than They Appear" 블로그(3/25)에서 Cryptographically Relevant Quantum Computer (CRQC) 조기 출현 가능성과 Store-Now-Decrypt-Later (SNDL) 공격 위협을 근거로 2029년 자체 완료를 선언. 통신사·금융 등 규제 산업 로드맵 조기화 압력 발생. [[G-01]](#ref-g-01), [[G-02]](#ref-g-02)

2. **Android 17 ML-DSA 탑재 — 모바일 OS 최초 종합 PQC 보안 아키텍처.**
   4계층 동시 업그레이드: (1) Android Verified Boot ML-DSA, (2) Keystore ML-DSA-65/ML-DSA-87 `KeyPairGenerator` API, (3) Remote Attestation PQC, (4) Play App Signing 하이브리드 서명. ML-DSA 서명 ~3,293바이트(ECDSA 대비 ~51×). [[G-03]](#ref-g-03), [[E-01]](#ref-e-01)

3. **PQShield PQMicroLib-Core — 5KB RAM 임베디드 PQC, Embedded World 2026(3/10).**
   TLS 포함, 소프트웨어 업그레이드만으로 메모리 제약 IoT·보안 통신 단말에 PQC 소급 적용 가능. 레거시 디바이스 시장 타깃. [[G-05]](#ref-g-05)

4. **IBM + Signal + Threema — ML-DSA 직접 치환 시 대역폭 100× 증가 정량화.**
   Real-World Crypto 2026 발표. 서버 측 암호화 그룹 데이터 저장 + 멤버 검증 분산 방식으로 해결 제안. 보이스 PQC 프로토콜 설계 시 핵심 제약 요인. [[G-07]](#ref-g-07)

5. **QuSecure, SEC 제출 PQFIF에서 금융 PQC 레퍼런스 공식 인용(3/19).**
   Banco Sabadell+Accenture 4개월 마이그레이션 — 대형 은행 최초 규제 기관 인정 사례. AFWERX/TACFI $3.9M 미공군 계약, MDA SHIELD $151B 계약 수주. [[G-09]](#ref-g-09), [[E-02]](#ref-e-02)

6. **CISA 연방 PQC 조달 기준 확립(1/23) — 협업 도구(메시징·보이스) 즉시 PQC 의무 범주 포함.**
   Executive Order 14306에 따른 제품 카테고리 목록. 1군(즉시 PQC 구매): 클라우드, 협업 도구, 브라우저, 엔드포인트. 2군(전환 중): 통신장비, OS, 스토리지, IAM. [[G-10]](#ref-g-10)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Google | 2029 PQC 데드라인 선언(3/25). Android 17 ML-DSA 4계층 통합(3/26). Chrome ML-KEM 기본 활성화 | [[G-01]](#ref-g-01), [[E-01]](#ref-e-01) |
| IBM | Signal·Threema와 양자안전 그룹 메시징 재설계 발표(3/10). ML-DSA 대역폭 100× 문제 확인 | [[G-07]](#ref-g-07) |
| PQShield | PQMicroLib-Core 5KB RAM PQC(3/10). 100편 연구 논문 달성 | [[G-05]](#ref-g-05) |
| QuSecure | SEC PQFIF 공식 인용(3/19). AFWERX $3.9M + MDA SHIELD 수주 | [[G-09]](#ref-g-09), [[E-02]](#ref-e-02) |
| Thales | 5G SIM OTA PQC 세계 최초 시연(3/2). SKT와 CRYSTALS-Kyber SIM 테스트 | [[G-12]](#ref-g-12), [[E-03]](#ref-e-03) |
| SKT | QKD-PQC 하이브리드 장비(세계 최초). Thales 5G SIM PQC 테스트 협력 | [[G-17]](#ref-g-17) |

#### 시장 시그널

**투자 & M&A**
- QuSecure, AFWERX/TACFI $3.9M + MDA SHIELD 계약 — 미국 방위 PQC 조달 가속 [[G-09]](#ref-g-09) [추가확인 필요]
- Axelera AI, EU Innovation Council €200M+ 조달 — Europa AIPU(KSE3 PQC 내장) 생산 재원 확보 [[G-15]](#ref-g-15)

**파트너십 & 제휴**
- IBM + Signal + Threema: 양자안전 메시징 공동 연구 — 소비자 플랫폼 PQC 전환 로드맵 영향 [[G-07]](#ref-g-07)
- Multiverse Computing + Axelera: 엣지 AI 모델 압축(최대 95%) 협력(3/18) [[G-16]](#ref-g-16)

**시장 전망**
- 기업 14%만 양자 취약 시스템 전수 조사 완료. 대기업 마이그레이션 12~15년+ 소요 추정 [[G-19]](#ref-g-19) [추가확인 필요]
- 2026년은 Pure PQC보다 Classical+PQC 하이브리드 접근 지배 전망 [[G-20]](#ref-g-20)

**도입 사례**
- Google: Android 17 종합 PQC 스택 — 모바일 OS 최초
- QuSecure + Banco Sabadell: 금융권 최초 SEC 공식 인정
- SKT + Thales: 5G SA 망 CRYSTALS-Kyber SIM — 통신사 On-Device PQC 실증

**연구 동향**
- IBM: PQC 메시징 대역폭 100× 증가 문제 정량화 + 해결책 (Real-World Crypto 2026) [[G-07]](#ref-g-07)
- MDPI Electronics: 격자 기반 암호화 하드웨어 가속기 — NTT·다항식 연산 온디바이스 오프로드 [[G-13]](#ref-g-13)

#### 시장 수요 (voice-of-market)

**고객 페인포인트**
- 크립토 하드코딩으로 마이그레이션 부담 (ABN AMRO: 팀 2~3명 × 3~4주, 수백 파일 수동 수정) — 출처: Migrating and benchmarking a banking application (Alessandro Amadori, TNO / PKI Consortium)
- ML-DSA 서명 2,420바이트(Ed25519 대비 38×) — SIEM 스토리지 50배 증가, DB 오버플로, HSM 통합 문제 — 출처: PKI Consortium PQC Conference; HN 커뮤니티
- macOS Secure Enclave 등 하드웨어 보안 요소(SE)의 PQC 미지원 — 온디바이스 구현 근본 제약 — 출처: HN 커뮤니티

**도입 장벽**
- 조직 내 암호화 인벤토리/가시성 확보 자체가 난제 — 출처: NIST Post-Quantum Cryptography Update (Bill Newhouse, NIST)
- 프로토콜 수준 표준(FIPS 203/204/205 이후) 업데이트 미완성 — 출처: NIST Update (Andrew Regenscheid)
- 경영진 설득 장벽 — 소규모 PoC부터 점진적 접근 필요 — 출처: PKI Consortium Conference

**시장 니즈**
- 크립토 애질리티 설계 패턴 및 구현 가이드 (알고리즘 추상화 인터페이스) — 출처: PKI Consortium Conference
- DoD 2031 데드라인(NSS 전체 QR 전환)이 방산·연방 공급망 즉각적 PQC 수요 촉발 — 출처: NSA Morgan Stern 발표

#### 전략적 시사점

**기회**
- Android 17 ML-DSA Keystore API로 On-Device PQC 서명/인증을 표준 API로 구현 가능. 별도 HSM 없이 TrustZone 격리 보관
- Thales OTA PQC 업그레이드는 기존 5G SIM 디바이스 교체 없이 PQC 소급 적용 경로. SKT가 이미 협력 중
- PQShield 5KB RAM 라이브러리는 IoT·VoIP 단말 저비용 PQC 적용 레디메이드 솔루션

**위협**
- PQC 메시징 대역폭 100× 증가 — 실시간 보이스 통화 QoS 저하 위험. SIP/RTP 스택 재설계 필요
- Google 2029 선언으로 공급망 전체 조기화 압력 — 2030 기준 로드맵 수정 요구 가능
- 기업 14%만 전수 조사 완료 + 대기업 12~15년 소요 — 대부분 NIST 2030 충족 어려운 상황

---

### On-Device 동형암호 — 🟡 주목

#### 이전 대비 변화
- 전주: UTS FHE 기반 DRL 세계 최초 실증(Nature MI, 3/18), Intel Heracles 미디어 확산(3/19), LGU++CryptoLab AICC 동형암호(MWC)
- 금주: "Privacy at your Fingertips" 클라이언트 FHE 오버헤드 97% 감소(EuroS&P 2026), CAT GPU 프레임워크 CKKS 33× 가속(arXiv 3/28), Zama+T-REX $32B RWA FHE 실도입(3/26)
- 변화 방향: 하드웨어 단계(ASIC)에서 **생태계 확장** 단계로 이동. 금융 부문 실도입 + 클라이언트 측 최적화 논문으로 온디바이스 실용화 가속

#### 기술 동향

1. **"Privacy at your Fingertips" — 클라이언트 FHE enc/dec 오버헤드 97% 감소 (EuroS&P 2026, 3/15).**
   Boosted-Deflation 기법으로 부동소수점 산술 요구 제거 + 부트스트래핑 활용 통신 오버헤드 저감. 선행 연구 대비 76× 속도 향상. 온디바이스 키워드 검색 실용성 직접 제고. [[G-21]](#ref-g-21), [[P-01]](#ref-p-01)

2. **CAT GPU 가속 FHE 프레임워크 — CKKS 프라이빗 DB 쿼리 CPU 대비 33× (arXiv 3/28).**
   3계층 아키텍처로 CKKS/BFV/BGV 통합 지원. RTX 4090에서 최대 2,173× 가속. 1초 내 10³행 데이터셋 암호화 쿼리 가능. [[G-22]](#ref-g-22), [[P-02]](#ref-p-02)

3. **Intel Heracles 기술 사양 지속 확산.**
   1.2GHz, 197mm², Intel 3 공정. 1,074~5,547× Xeon 가속. 암호화 유권자 DB 쿼리 14μs(Xeon 15ms). BGV/BFV/CKKS 다중 스킴 지원. 양산 일정 미발표. [[G-23]](#ref-g-23), [[E-04]](#ref-e-04)

4. **Zama + T-REX Network — $32B ERC-3643 토큰화 자산에 FHE 기밀성 레이어 통합(3/26).**
   기관 금융 인프라 수준 최초 FHE 실도입. Apex Group $3.5조 자산 서비스 기반. 2027년 6월 $1,000억 목표. [[G-24]](#ref-g-24), [[E-05]](#ref-e-05)

5. **FHECore GPU 전용 마이크로아키텍처 — CKKS 부트스트래핑 50% 감소.**
   BU/Northeastern/KAIST/Murcia 공동 연구. NTT·기저 변환을 동일 WMAC 유닛으로 처리. 면적 오버헤드 2.4%. [[G-25]](#ref-g-25), [[P-03]](#ref-p-03)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Intel | Heracles FHE ASIC 1,074~5,547× 가속. DARPA DRIVE 기원. 양산 미발표 | [[G-23]](#ref-g-23), [[E-04]](#ref-e-04) |
| Zama | T-REX Network FHE 기밀성 레이어 출시(3/26). 유니콘($1B+). FHE.org Apple·AWS·Google 후원 | [[G-24]](#ref-g-24), [[E-05]](#ref-e-05) |
| CryptoLab | LGU+ ixi-O AICC 동형암호 PoC. CKKS 4세대 원천특허. Niobium ASIC 통합 추진 | [[G-26]](#ref-g-26), [[E-06]](#ref-e-06) |
| Niobium+SemiFive | Samsung 8nm FHE ASIC 개발 진행(100억 원). 세계 최초 상용 FHE 가속기 목표 | [[G-27]](#ref-g-27) |
| LGU+ | MWC 2026 '인간 중심 AI'. CryptoLab과 AICC 동형암호 탑재 PoC | [[G-26]](#ref-g-26) |

#### 시장 시그널

**파트너십 & 제휴**
- Zama + T-REX: FHE를 $32B RWA 토큰화 인프라에 통합(3/26) — 기관 금융 최초 실도입 규모 [[G-24]](#ref-g-24)
- LGU+ + CryptoLab: AICC 동형암호 PoC — 국내 통신사 최초 암호화 AI 고객센터 경로 [[G-26]](#ref-g-26)

**연구 동향**
- "Privacy at your Fingertips" (EuroS&P 2026): 클라이언트 FHE 97% 오버헤드 감소 — 온디바이스 키워드 검색 실용성 임계점 [[P-01]](#ref-p-01)
- CAT (arXiv 3/28): CKKS 프라이빗 DB 쿼리 33× 가속 [[P-02]](#ref-p-02)
- FHE.org 타이페이(3/8): Apple·AWS·Google 후원. 다수 발표·포스터 채택 [[G-28]](#ref-g-28)

**시장 전망**
- FHE 스타트업 8개사 누적 $2.79억. Zama 유니콘($1B+ 밸류에이션) [[G-29]](#ref-g-29) [추가확인 필요]

**도입 사례**
- T-REX Ledger: $32B ERC-3643 자산 FHE 통합 — FHE 사상 최초 기관급 실도입 [[G-24]](#ref-g-24)
- LGU+ AICC: 고객 개인정보 암호화 상태 비교·분석 PoC 진행 중 [[G-26]](#ref-g-26)

**커뮤니티 시그널**
- Slashdot "Intel Demos Chip" 수백 건 댓글 — FHE 주류 기술 커뮤니티 인지도 확산. 회의론과 기대감 혼재 [[C-01]](#ref-c-01)
- FHE.org Digest #38: Apple·AWS·Google 후원 → 빅테크 진입 신호로 해석 [[G-28]](#ref-g-28)

#### 시장 수요 (voice-of-market)

**고객 페인포인트**
- FHE 연산 오버헤드 — GPU 기반도 대부분 실용 배포 미달. "bootstrapping은 1,000× 이상 오버헤드 근본 한계" — 출처: FHE Hardware Day 2025 Panel (Rosario Cammarota, Intel Labs)
- 암호문 크기 평문 대비 ~1,000× — 메모리 아키텍처 병목. HBM 접근 에너지 100×+ — 출처: FHE Hardware Day (Paul Master, Cornami)

**도입 장벽**
- FHE 전문가 전세계 50인 미만 — 기업 내재화 불가 — 출처: FHE Hardware Day (Rosario Cammarota, Intel Labs)
- 킬러앱 볼륨 부재 — ASIC 제조 $1억+ 투자 회수 불확실 — 출처: FHE Hardware Day (Paul Master, Cornami)
- Apple도 완전 온디바이스 FHE 구현 못 함 — iOS 18에서 임베딩 평문 계산 + 최근접이웃만 FHE 처리 — 출처: HN 커뮤니티

**시장 니즈**
- Private LLM — 금융·의료·법률 분야 암호화 AI 추론 수요 부상 — 출처: FHE Hardware Day (Paul Master, Cornami)
- FHE 표준화 — 50인 전문가 밖으로 확산 가능한 개발자 도구 필요. 서울 9차 HE 표준화 회의(3/5-6) — 출처: HomomorphicEncryption.org

#### 전략적 시사점

**기회**
- "Privacy at your Fingertips" 97% 감소는 스마트폰급 기기에서 FHE 키워드 검색 가능 전환점. 12~18개월 내 상용 데모 가능성
- LGU++CryptoLab 성공 시 KT/SKT도 동형암호 AICC 도입 압박
- Niobium(Samsung 8nm) + Intel(Intel 3) FHE ASIC 병행 — 국내 팹리스 협력 기회

**위협**
- Intel Heracles 양산 미발표 — 소프트웨어 FHE 키워드 검색 지연 문제 지속
- Apple·AWS·Google FHE.org 후원 진입 — 자체 클라우드 FHE 서비스 출시 시 국내 솔루션 잠식 가능
- 저전력 임베디드 GPU(Jetson Nano 등) FHE 부적합 — 온디바이스 적용 범위 상위 티어 스마트폰 제한

---

### 스팸/피싱 감지(통화전) — 🟡 주목

> Deep 에이전트 미실행. Quick 스캔 기반 요약.

#### 주요 동향
- **Meta 안티스캠 AI 도구 출시(3월)**: 고급 AI로 피싱 리다이렉트 페이지 감지, 브랜드 위장 차단. 수천 브랜드 보호
- **AI 피싱 204% 급증**: 악성 이메일 19초당 1건. AI 생성 피싱 클릭률이 인간 제작 대비 4배. 12월 AI 피싱 비중 56% 도달
- **Google 3월 스팸 업데이트(3/24-25)**: 글로벌·전 언어 대상 스팸 필터 갱신 완료
- **QRishing(QR 피싱) 2026 급부상**: 전통 방어체계 탐지율 극히 낮음. 보이스 딥페이크와 결합 가능

---

## 경쟁사 동향 (SKT / KT)

### SKT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| QKD-PQC 하이브리드 장비 | 세계 최초 출시. NIST FIPS 203/204 준수 자체 개발 PQC 소프트웨어 | pqc-voice-encryption | [[G-17]](#ref-g-17) |
| Thales 5G SIM PQC 테스트 | 5G SA 망 CRYSTALS-Kyber SIM 협력 테스트 | pqc-voice-encryption | [[E-03]](#ref-e-03) |
| 위성통신 양자암호 국책과제 | PIC 기술로 QKD 장비 소형화·저비용화 추진 | pqc-voice-encryption | [[G-17]](#ref-g-17) |

### KT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| AI 보이스피싱 탐지 | 2025년 ~1,300억 원 피해 예방. 4,400만 건 분석, 3만 건 주의/경고 알림 | spam-phishing-detection | [[G-30]](#ref-g-30) |
| QKD+AI+동형암호 결합 전략 | 보안 기술 전 구간 적용 계획 발표 | pqc-voice-encryption | [[G-31]](#ref-g-31) |

### 시사점
- SKT가 PQC 분야에서 Thales 협력·자체 개발 양면으로 선두 유지. 5G SIM OTA PQC 실증은 국내 최초
- KT는 AI 보이스피싱 탐지에서 실질적 성과(1,300억 원 피해 예방) — 스팸/피싱 영역 실적 기반 경쟁력
- LGU+가 CryptoLab과 동형암호 AICC 차별화 선점 시도 중 — KT/SKT 미대응 시 프라이버시 차별화 포인트 선점당할 가능성

---

## 규제 & 거버넌스

### 시행 임박 / 카운트다운

| 규제 | 시행일 | D-day |
|------|--------|-------|
| EU AI Act Article 6 (High-Risk AI 의무) | 2026-08-02 | D-125 |
| EU CRA 보고 의무 (취약점 24시간 내 ENISA 보고) | 2026-09-11 | D-165 |
| FIPS 140-2 인증 종료 (NIST CMVP Historical 이전) | 2026-09-21 | D-175 |
| CNSA 2.0 NSS 신규 조달 의무화 | 2027-01-01 | D-276 |
| 한국 AI 기본법 Article 31 (AI 생성 표시) | 2026-01-22 | 시행 중 |
| FCC SIP 603+ Analytics-Based Blocking | 2026-03-25 | 시행 중 |

### 신규 발의 & 가이드라인
- **CISA PQC 제품 카테고리 리스트(1/23)**: 협업 도구(메시징·보이스)가 즉시 PQC 의무 범주(1군)에 포함. 통신장비는 2군(전환 중) [[G-10]](#ref-g-10)
- **트럼프 행정부 Cyber Strategy(3/6)**: 연방 네트워크 현대화에 PQC + 제로 트러스트 + AI 방어 명시 [[G-32]](#ref-g-32)
- **Google 독자 2029 데드라인**: 정부 규제(NIST 2030)보다 앞선 민간 기준 — 업계 레퍼런스로 작용 가능

### 시사점
- FIPS 140-2 종료(D-175)·CRA(D-165)·CNSA 2.0(D-276) 삼중 데드라인 하반기 집중 지속
- Google 2029 선언은 정부 규제를 앞서는 민간 표준 형성 — 통신사 로드맵 재검토 필요
- CISA 1군에 협업 도구 포함 → 보이스 통신 PQC 지원이 미국 연방 조달 기본 요건으로 공식화

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **PQC 플랫폼 확산 가속** — Google 2029 선언 + Android 17 ML-DSA + CISA 1군 분류로, PQC가 "when"에서 "how fast"로 전환. 통신사 로드맵 2030 기준이면 이미 늦을 수 있음

2. **FHE 실용화 임계점 접근** — "Privacy at your Fingertips" 97% 감소 + Intel Heracles 5,000× 가속 + Zama $32B 실도입. 하드웨어·소프트웨어·비즈니스 3축이 동시에 움직이는 첫 주

3. **국내 통신사 양극화** — SKT(PQC 선두), KT(AI 피싱 탐지 실적), LGU+(동형암호 AICC 차별화). 각사 차별화 축이 명확해지는 추세

### 후속 조치 제안

- 🔴 PQC — `/wtis standard` 검증 권고. Google 2029 선언이 국내 통신사 로드맵에 미치는 영향 평가 필요. Thales OTA PQC + Android 17 ML-DSA 조합으로 On-Device 보이스 PQC PoC 가능성 검토
- 🟡 동형암호 — LGU++CryptoLab AICC PoC 진행 상황 추적. "Privacy at your Fingertips" 후속 연구 + Intel Heracles 양산 일정 모니터링
- 🟡 스팸/피싱 — Meta 안티스캠 AI 도구 구조 분석. QRishing+보이스 딥페이크 결합 위협 대비 검토

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Google Blog — Quantum Frontiers: PQC Migration Timeline 2029 | [링크](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/) | news | 2026-03-25 | [A] |
| <a id="ref-g-02"></a>G-02 | TechSpot — Google Sets 2029 Deadline for Quantum-Safe Encryption | [링크](https://www.techspot.com/news/111856-google-sets-2029-deadline-quantum-safe-encryption-years.html) | news | 2026-03-25 | [B] |
| <a id="ref-g-03"></a>G-03 | Privacy Guides — Android 17 PQC Upgrade | [링크](https://www.privacyguides.org/news/2026/03/26/android-17-is-getting-a-post-quantum-cryptography-upgrade/) | news | 2026-03-26 | [B] |
| <a id="ref-g-05"></a>G-05 | Quantum Insider — PQShield PQMicroLib-Core 5KB RAM | [링크](https://thequantuminsider.com/2026/03/10/pqshield-ultra-small-pqc-embedded-security-embedded-world/) | news | 2026-03-10 | [B] |
| <a id="ref-g-07"></a>G-07 | Quantum Insider — IBM + Signal + Threema Quantum-Safe Messaging | [링크](https://thequantuminsider.com/2026/03/10/ibm-signal-threema-quantum-safe-research/) | news | 2026-03-10 | [B] |
| <a id="ref-g-09"></a>G-09 | Quantum Insider — SEC PQFIF QuSecure Deployment | [링크](https://thequantuminsider.com/2026/03/19/sec-submission-highlights-qusecure-deployment-real-world-post-quantum-migration-example/) | news | 2026-03-19 | [B] |
| <a id="ref-g-10"></a>G-10 | CISA — Product Categories for PQC Standards | [링크](https://www.cisa.gov/resources-tools/resources/product-categories-technologies-use-post-quantum-cryptography-standards) | news | 2026-01-23 | [A] |
| <a id="ref-g-12"></a>G-12 | Quantum Insider — Thales 5G SIM OTA PQC | [링크](https://thequantuminsider.com/2026/03/02/thales-remote-post-quantum-5g-sim-upgrade/) | news | 2026-03-02 | [B] |
| <a id="ref-g-13"></a>G-13 | MDPI Electronics — Lattice-Based Cryptographic Accelerators | [링크](https://www.mdpi.com/2079-9292/15/2/475) | paper | 2026-01 | [A] |
| <a id="ref-g-15"></a>G-15 | EE Times — Axelera Raises €200M+ | [링크](https://www.eetimes.com/axelera-raises-250m-in-largest-eu-semi-round-ever/) | news | 2026-02-24 | [B] |
| <a id="ref-g-16"></a>G-16 | Quantum Insider — Multiverse + Axelera AI Collaboration | [링크](https://thequantuminsider.com/2026/03/18/ultiverse-computing-axelera-ai-strategic-collaboration-ai-models-edge-devices/) | news | 2026-03-18 | [B] |
| <a id="ref-g-17"></a>G-17 | SK텔레콤 뉴스룸 — QKD-PQC 하이브리드 장비 | [링크](https://news.sktelecom.com/207758) | news | 2026-03-15 | [A] |
| <a id="ref-g-19"></a>G-19 | Gray Group — PQC Enterprise Guide 2026 | [링크](https://www.graygroupintl.com/blog/post-quantum-cryptography-enterprise-guide/) | blog | 2026-03 | [C] |
| <a id="ref-g-20"></a>G-20 | Security Boulevard — PQC Authentication Migration Guide | [링크](https://securityboulevard.com/2026/03/post-quantum-cryptography-for-authentication-the-enterprise-migration-guide-2026/) | news | 2026-03 | [B] |
| <a id="ref-g-21"></a>G-21 | IACR ePrint — Privacy at your Fingertips (발표 소식) | [링크](https://iacr.org/news/item/27993) | news | 2026-03-15 | [A] |
| <a id="ref-g-22"></a>G-22 | arXiv — CAT GPU-Accelerated FHE Framework | [링크](https://arxiv.org/abs/2503.22227) | paper | 2026-03-28 | [A] |
| <a id="ref-g-23"></a>G-23 | Tom's Hardware — Intel Heracles 1,074~5,547× Xeon 가속 | [링크](https://www.tomshardware.com/tech-industry/cyber-security/intels-heracles-chip-computes-fully-encrypted-data-without-decrypting-it-chip-is-1-074-to-5-547-times-faster-than-a-24-core-intel-xeon-in-fhe-math-operations) | news | 2026-03-19 | [B] |
| <a id="ref-g-24"></a>G-24 | Benzinga — T-REX + Zama FHE Institutional Confidentiality | [링크](https://www.benzinga.com/pressreleases/26/03/51479524/t-rex-network-and-zama-launch-institutional-grade-confidentiality-infrastructure-for-rwa-tokenizati) | news | 2026-03-26 | [B] |
| <a id="ref-g-25"></a>G-25 | Semi Engineering — GPU Microarchitecture for FHE (FHECore) | [링크](https://semiengineering.com/a-gpu-microarchitecture-optimized-for-fully-homomorphic-encryption/) | news | 2026-03 | [B] |
| <a id="ref-g-26"></a>G-26 | Asia Business Daily — LGU+ CryptoLab MWC26 | [링크](https://www.asiae.co.kr/en/article/2026031008212144575) | news | 2026-03-10 | [B] |
| <a id="ref-g-27"></a>G-27 | evertiq — SemiFive + Niobium FHE Accelerator | [링크](https://evertiq.com/design/2026-02-20-semifive-secures-design-win-with-niobium-for-fhe-accelerator) | news | 2026-02-20 | [B] |
| <a id="ref-g-28"></a>G-28 | FHE.org Digest #38 — 2026 Conference, Apple/AWS/Google 후원 | [링크](https://fheorg.substack.com/p/fheorg-digest-38-fheorg-2026-conference) | news | 2026-03 | [B] |
| <a id="ref-g-29"></a>G-29 | SeedTable — 8 Best FHE Startups (2026-03-24) | [링크](https://www.seedtable.com/best-homomorphic-encryption-startups) | blog | 2026-03-24 | [C] |
| <a id="ref-g-30"></a>G-30 | 전자신문 — KT AI 보이스피싱 탐지 1,300억 원 피해 예방 | [링크](https://www.etnews.com/20251223000189) | news | 2025-12-23 | [B] |
| <a id="ref-g-31"></a>G-31 | 보안뉴스 — 2026년 통신사 보안 기상도 | [링크](https://m.boannews.com/html//detail.html?idx=141650) | news | 2026-01 | [B] |
| <a id="ref-g-32"></a>G-32 | UV Cyber — PQC Federal Mandate Framework | [링크](https://www.uvcyber.com/resources/blog/post-quantum-cryptography-just-became-a-federal-mandate-a-practical-framework-for-quantum-readiness) | news | 2026-03-06 | [B] |
| <a id="ref-p-01"></a>P-01 | Aikata et al. — Privacy at your Fingertips (EuroS&P 2026) | [링크](https://eprint.iacr.org/2026/515) | paper | 2026-03-15 | [A] |
| <a id="ref-p-02"></a>P-02 | CAT: GPU-Accelerated FHE Framework (arXiv 2503.22227) | [링크](https://arxiv.org/abs/2503.22227) | paper | 2026-03-28 | [A] |
| <a id="ref-p-03"></a>P-03 | FHECore: GPU Microarchitecture for FHE (arXiv 2602.22229) | [링크](https://arxiv.org/abs/2602.22229) | paper | 2026-02 | [A] |
| <a id="ref-e-01"></a>E-01 | Google Security Blog — PQC in Android 17 | [링크](https://security.googleblog.com/2026/03/post-quantum-cryptography-in-android.html) | IR/발표 | 2026-03-26 | [A] |
| <a id="ref-e-02"></a>E-02 | QuSecure — SEC PQFIF Banking Deployment | [링크](https://www.qusecure.com/post-quantum-cryptography-banking-deployment-sec-framework/) | IR/발표 | 2026-03-19 | [A] |
| <a id="ref-e-03"></a>E-03 | Thales/Nasdaq — World First Quantum-Safe 5G SIM | [링크](https://www.nasdaq.com/press-release/thales-sets-world-first-quantum-safe-security-5g-networks-2026-03-02) | IR/발표 | 2026-03-02 | [A] |
| <a id="ref-e-04"></a>E-04 | IEEE Spectrum — Intel Heracles FHE ISSCC Demo | [링크](https://spectrum.ieee.org/fhe-intel) | IR/발표 | 2026-03-10 | [A] |
| <a id="ref-e-05"></a>E-05 | Zama — Confidentiality Layer for T-REX Ledger | [링크](https://www.zama.org/post/zama-becomes-the-confidentiality-layer-for-the-t-rex-ledger) | IR/발표 | 2026-03-26 | [A] |
| <a id="ref-e-06"></a>E-06 | Korea IT Times — LGU+ Human-Centered AI MWC 2026 | [링크](https://www.koreaittimes.com/news/articleView.html?idxno=151339) | IR/발표 | 2026-03-10 | [B] |
| <a id="ref-c-01"></a>C-01 | Slashdot — Intel Demos Chip To Compute With Encrypted Data | [링크](https://it.slashdot.org/story/26/03/10/2022201/intel-demos-chip-to-compute-with-encrypted-data) | community | 2026-03-10 | [C] |
