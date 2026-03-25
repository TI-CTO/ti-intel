---
type: weekly-monitor
domain: secure-ai
week: 2026-W14
date: 2026-03-25
l3_count: 5
deep_count: 2
---

# 주간 기술 동향: Secure AI (2026-W14)

## Executive Summary

> **이번 주 핵심**: RSAC 2026(3/23-24)에서 ZeroTier Quantum이 세계 최초 E2E 양자안전 네트워킹 플랫폼을 출시하고, Kudelski Labs가 PQC 반도체 IP(KSE3)를 공개하며 하드웨어·네트워킹 레이어의 PQC 실용화가 가속. 동형암호에서는 UTS가 FHE 기반 딥강화학습(Deep Reinforcement Learning, DRL)을 세계 최초로 실증해 Nature Machine Intelligence에 게재(3/18). FIPS 140-2 종료(D-180)·EU CRA 보고 의무(D-170)·CNSA 2.0(D-281) 삼중 규제 데드라인이 동시 압박.

| Layer 2 | 세부기술 | 신호 | 핵심 내용 |
|---------|----------|------|----------|
| 양자/동형 암호 | On-Device 양자암호(PQC) | 🟡 | RSAC 2026 ZeroTier Quantum E2E PQC 출시(3/24), Kudelski KSE3 PQC 반도체 IP, FIPS 140-2 D-180 |
| | On-Device 동형암호 | 🟡 | UTS FHE DRL 세계 최초 실증(Nature MI, 3/18), Intel Heracles 일반 미디어 커버리지 확산 |
| | Secure Vector Search | 🟢 | PHE 벡터 유사도 연구 지속, 상용 돌파 없음 |
| 스팸/피싱탐지 | 스팸/피싱 감지(통화전) | 🟢 | FCC SIP 603+ 시행 완료(3/25). 전주 대비 신규 돌파 없음 |
| | OCR 활용 이미지 스팸 차단 | 🟢 | 구조적 변화 없음 |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음

---

## 🟢 Quick 요약 (변화 미미)

### 스팸/피싱 감지(통화전)
- FCC SIP 603+ (Session Initiation Protocol 603+) 의무화가 3/25 시행 완료. 미국 모든 Voice Service Provider가 analytics-based call blocking 시 "Network Blocked" 코드를 반환해야 한다. 전주 SKT 에이닷 성문 탐지 출시(3/18), Adaptive Security $81M Series B 등 주요 이벤트 후 소강 상태. C2PA(Coalition for Content Provenance and Authenticity) 표준의 통신사 채택이 진행 중이나 구체적 신규 발표 없음.

### OCR 활용 이미지 스팸 차단
- Gmail TensorFlow 이미지 스팸 탐지(일 1억건 추가 차단), RETVec(Resilient & Efficient Text Vectorizer) 조작 텍스트 탐지, Gemini Nano 온디바이스 보호 지속. 이번 주 구조적 변화 없음.

### Secure Vector Search: B2B AICC 동형암호 적용
- PHE(Partially Homomorphic Encryption) 기반 벡터 유사도 연구(arXiv 2503.05850)가 FHE 대안으로 주목 지속. 사이퍼텍스트·키 크기 경량화 이점. UTS의 FHE DRL 돌파(아래 Deep 참조)가 간접적으로 암호화 AI 추론의 가능성을 넓히나, 벡터 검색 특화 상용 돌파는 없음.

---

## 🟡🔴 Deep 심층 분석

### On-Device 양자암호(PQC) — 🟡 주목

#### 이전 대비 변화
- 전주: 중국 PQC 독자 표준 3년 내 선언(3/19), 트럼프 사이버 전략 PQC 명시(3/6), SEALSQ 블록체인 PQC 배포(3/20), HNDL 위협 경고 강화
- 금주: RSAC 2026서 ZeroTier Quantum 출시(3/24), Kudelski KSE3 PQC 반도체 IP, Axelera Europa+KSE3 엣지 AI 결합, 삼중 규제 데드라인 가시화
- 변화 방향: 하드웨어(반도체 IP)·네트워킹(E2E 플랫폼)·통신(SIM OTA) 전 레이어에서 PQC 실용화가 동시 진행. 기술 배포 → 규제·표준 제도화로 무게 중심 이동

#### 기술 동향

1. **ZeroTier Quantum 출시(3/24) — RSAC 2026에서 CNSA 2.0 준수 E2E 양자안전 네트워킹 플랫폼 공개.**
   ZeroTier Transport Protocol(ZTP)에 Hybrid FIPS-compliant PQC를 전송 계층에 직접 내장. NSA Commercial National Security Algorithm Suite 2.0 (CNSA 2.0) 준수. Rust로 전체 재작성, SaaS·소버린 격리·에어갭 3가지 배포 옵션. 방산·정부·의료·금융 타깃. [[G-01]](#ref-g-01), [[G-02]](#ref-g-02)

2. **Kudelski Labs KSE3 — NIST 표준 PQC + 보안 엔클레이브 반도체 IP, CRA 준수.**
   Embedded World 2026에서 공개. NIST ML-KEM(FIPS 203, Module-Lattice-Based Key-Encapsulation Mechanism) 및 ML-DSA(FIPS 204, Module-Lattice-Based Digital Signature Algorithm)를 하드웨어 엔클레이브에 통합. 사이드채널·폴트 공격 보호. 모듈형 구조로 PQC 알고리즘 교체 시 펌웨어 업데이트만으로 크립토-어질리티(Crypto-agility) 지원. EU Cyber Resilience Act(CRA) Important Products 분류 준수. [[G-03]](#ref-g-03)

3. **Axelera AI + Kudelski Labs(3/10) — Europa Edge AI 칩에 KSE3 PQC-ready 보안 엔클레이브 통합.**
   On-Device AI 추론 워크로드에 양자내성 암호화, 보안 부팅, 키 관리, 불변 신원(Immutable Identity)을 동시 제공하는 최초의 엣지 AI 칩 사례. SESIP/PSA Level 3(AVA_VAN.3) 인증 목표. 스마트 인프라·산업 자동화·자율 로봇 타깃. [[G-04]](#ref-g-04), [[G-05]](#ref-g-05)

4. **Thales 5G SIM OTA PQC 업그레이드 세계 최초 시연(3/2).**
   SIM 및 eSIM 카드에 PQC 알고리즘을 원격(Over-the-Air)으로 다운로드해 양자안전 보안으로 전환. 디바이스 교체 없이 수십억 기존 단말에 PQC 소급 적용 경로 실증. 크립토-어질리티 개념의 통신 단말 레벨 실용화. [[E-01]](#ref-e-01)

5. **SEALSQ 블록체인 PQC 배포(3/20) — CRYSTALS-Kyber + Dilithium TPM 통합.**
   ML-KEM(키 캡슐화) 및 ML-DSA(디지털 서명)를 TPM-class 칩에 직접 내장. 스위스 블록체인 금융 플랫폼 WeCan과 협력해 실 서비스 적용. Secure Multi-Party Computation(MPC)+Zero-Knowledge Proof(ZKP) 결합. [[G-06]](#ref-g-06)

6. **FIPS 140-2 종료 D-180(2026-09-21) — FIPS 140-3 전환 구조적 병목.**
   NIST Cryptographic Module Validation Program(CMVP)이 잔존 FIPS 140-2 인증 모듈을 Historical로 이전. 이후 신규 연방 조달은 FIPS 140-3만 허용. FIPS 140-3 검증 평균 542일(FIPS 140-2 대비 +42%)로, PQC 완전 인증 모듈의 2027년 이전 광범위 공급이 어려운 구조적 공백(Acquisition Gap) 발생. [[G-07]](#ref-g-07)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| ZeroTier | RSAC 2026(3/24): ZeroTier Quantum 출시. ZTP+Hybrid FIPS PQC, CNSA 2.0, Rust 재작성 | [[G-01]](#ref-g-01) |
| Kudelski Labs | Embedded World 2026: KSE3 PQC 반도체 IP. ML-KEM+ML-DSA 하드웨어 엔클레이브, CRA 준수 | [[G-03]](#ref-g-03) |
| Axelera AI | Europa AIPU+KSE3 통합(3/10). 최초 Edge AI+PQC 결합 칩. SESIP/PSA L3 목표 | [[G-04]](#ref-g-04) |
| Thales | 5G SIM OTA PQC 세계 최초 시연(3/2). 기존 단말 소급 적용 경로 실증 | [[E-01]](#ref-e-01) |
| SEALSQ | 블록체인 PQC 배포(3/20). ML-KEM/ML-DSA TPM 내장, WeCan 실 서비스 | [[G-06]](#ref-g-06) |
| LG유플러스 | ixi-Guardian 2.0: NIST+KpqC 이중 알고리즘 광전송 장비. GSMA GLOMO 수상 | [[G-08]](#ref-g-08) |

#### 시장 시그널

**파트너십 & 제휴**
- Axelera AI + Kudelski Labs: 엣지 AI 칩+PQC 반도체 IP 결합. On-Device PQC 추론 보안 레퍼런스 아키텍처로 확산 가능 [[G-04]](#ref-g-04)
- Ciena + QCi OFC 2026 시연(3/12): 광통신 인프라에 PQC+QKD(Quantum Key Distribution) 통합, 1.6 Tb/s 실용화 [[G-09]](#ref-g-09)

**시장 전망**
- PQC 글로벌 시장: MarketsandMarkets 추정 2025년 $4.2억 → 2030년 $28.4억(CAGR 46.2%) [추정] [[G-10]](#ref-g-10)
- 하이브리드 방식(고전+PQC)이 2026년 표준 전환 경로로 확립. 순수 PQC 단독 배포는 여전히 희소 [[G-11]](#ref-g-11)

**도입 사례**
- SEALSQ + WeCan: ML-KEM/ML-DSA TPM 통합, 스위스 블록체인 금융 실 서비스 보호. PQC 하드웨어+금융 서비스 최초 상용 사례 [[G-06]](#ref-g-06)
- LGU+ ixi-Guardian 2.0: NIST+KpqC 광전송 장비, 알고리즘 교체 시 서비스 무중단. 국내 통신사 PQC 광전송 첫 상용화 [[G-08]](#ref-g-08)
- SoftBank: 4G/5G 라이브 트래픽 하이브리드 PQC 파일럿 완료. 레이턴시 추가 최소화 확인 [[G-12]](#ref-g-12)

**연구 동향**
- "Post-Quantum Cryptography in the 5G Core" (arXiv:2512.20243, 2025) — 5G 코어에 PQC 알고리즘(BIKE, FrodoKEM, ML-DSA 등) 적용 시 성능 영향 분석. 하이브리드 적용이 실용적 경로로 제시 [[P-01]](#ref-p-01)
- "Harvest-Now, Decrypt-Later: A Temporal Cybersecurity Risk" (Ehlen et al., MDPI 2026) — 통신 인프라 HNDL(Harvest Now, Decrypt Later) 위협을 시계열 리스크로 분석. 고보존 분야의 노출 기간이 수십 년임을 실증 [[P-02]](#ref-p-02)

#### 시장 수요 (voice-of-market)

**고객 페인포인트**
- 암호화 자산 가시성 부재 — 조직 내 암호화 자산 규모를 파악하지 못해 우선순위 결정 불가. 실제 발견 자산은 사전 추정의 3~5배. 출처: NIST PQC Update (Andrew Regenscheid, Bill Newhouse / NIST)
- 소스코드 RSA 하드코딩으로 마이그레이션 공수 폭증 — ABN AMRO 은행 사례: 64개 파일 수작업 수정, 팀 2~3명 풀타임 3~4주 소요. 출처: Migrating a Banking Application (Alessandro Amadori / Dutch TNO)
- PQC 서명 크기 오버헤드 — SLH-DSA(Stateless Hash-Based Digital Signature Algorithm) 7.8kB+, ML-DSA 수 kB로 기존 ECDSA 대비 수십~수백 배. 출처: Hacker News 커뮤니티

**도입 장벽**
- 경영진 "Wait-and-See" — 전사 마이그레이션 예산 승인 저항. 소규모 PoC → 내부 인식 확산 전략 필요. 출처: Migrating a Banking Application (Amadori / Dutch TNO)
- 프로덕션용 PQC 라이브러리 신뢰성 부족 — Open Quantum Safe 라이브러리 자체가 프로덕션 비권장. NIST도 TLS/SSH/HSM PQC 지원 미완성 인정. 출처: NIST PQC Update (Regenscheid / NIST)
- CNSA 2.0 타이트한 데드라인 — 2027 신규 조달 QR 의무화 vs DoD 5년 예산 주기 충돌. 출처: NSA PQC Transition (Morgan Stern / NSA)

**시장 니즈**
- Crypto Agility 설계 가이드라인 — NIST Lily Chen 주도 공식 정의 문서 초안 공개 예정. 출처: NIST PQC Update (Newhouse / NCCoE)
- Discovery & Inventory 툴링 — 조직 내 암호화 자산 자동 탐색+위험 우선순위 도출 도구 수요 긴급. 출처: NIST PQC Update (Newhouse / NCCoE)
- 실세계 마이그레이션 케이스 스터디 — Google, Signal 등 선도 기업 과정·병목 공개 부족. 출처: PQC Conference Austin (Amadori / Dutch TNO)

#### 전략적 시사점

**기회**
- 하드웨어(KSE3, SEALSQ)·네트워킹(ZeroTier)·통신(Thales SIM OTA) 세 레이어가 동시에 PQC 실용화 이정표 기록 — On-Device PQC 통화 암호화의 설계 참조 아키텍처가 ML-KEM/ML-DSA 중심으로 수렴
- Thales SIM OTA PQC는 기존 단말 소급 적용 경로를 열어, 신규 단말 출시 없이도 양자안전 전환 가능성 시사

**위협**
- FIPS 140-3 검증 542일 병목 → 규제 준수 시장 진입 장벽. 2026~2027 Acquisition Gap 불가피
- 중국 비구조 격자 표준이 NIST 표준과 비호환 시, 글로벌 통신 인프라의 이중 표준 부담

---

### On-Device 동형암호: 키워드 검색 — 🟡 주목

#### 이전 대비 변화
- 전주: Intel Heracles 후속 기사(3/19) 외 소강. GPU FHE 가속 CUDA 논문 게재
- 금주: UTS FHE DRL Nature Machine Intelligence 게재(3/18) — 세계 최초 실증. Intel Heracles 일반 미디어 커버리지 확산. IACR Vaikuntanathan FHE 공헌 Fellow 선정(3/23)
- 변화 방향: 학술·기초연구에서 "암호화 데이터 AI 학습" 가능성이 처음 실증됨. 실용화 로드맵은 아직 멀지만 기초 연구 돌파 단계

#### 기술 동향

1. **UTS — 세계 최초 FHE 기반 딥강화학습(DRL) 프레임워크, Nature Machine Intelligence 게재(3/18).**
   호주 시드니공대(UTS) Associate Professor Hoang Dinh 팀이 완전 동형암호(Fully Homomorphic Encryption, FHE) 상태에서 딥강화학습을 가능하게 하는 프레임워크를 발표. 핵심 혁신: 역제곱근(inverse square root) 고차 다항식 근사 없이 동작하는 HE 호환 Adam 옵티마이저. 암호화 DRL 모델이 비암호화 기준 대비 10% 이내 성능 격차 유지. 공동연구: Meta AI Research Dr. Kristin Lauter, 한양대 Miran Kim. [[G-13]](#ref-g-13), [[P-03]](#ref-p-03)

2. **Intel Heracles 커버리지 일반 미디어 확산(3/19).**
   Privacy Guides, Tom's Hardware 등 일반 기술 미디어로 확장. DARPA DRIVE(Data Protection in Virtual Environments) 프로그램 기원 서사 강조. 8,192-way SIMD, Intel 3 공정, 197mm², 176W TDP, 48GB HBM3(819 GB/s). 24코어 Xeon 대비 1,074~5,547× 가속. BGV/BFV/CKKS 지원. 양산 일정 미발표. [[G-14]](#ref-g-14), [[G-15]](#ref-g-15)

3. **FHECore — GPU FHE 전용 마이크로아키텍처(BU/Northeastern/KAIST/Murcia).**
   GPU Streaming Multiprocessor에 FHE 전용 연산 유닛 통합. Built-in Barrett reduction으로 모듈로 연산 명령어 시퀀스 제거. CKKS 기본 연산 명령어 수 기하평균 2.41× 감소, 엔드투엔드 최대 2.12× 향상, 부트스트래핑 50% 감소, 면적 오버헤드 2.4%. Semiengineering 상세 기술 분석 게재. [[G-16]](#ref-g-16), [[P-04]](#ref-p-04)

4. **IACR — Vinod Vaikuntanathan MIT 교수, FHE 공헌으로 IACR Fellows 선정(3/23).**
   Learning With Errors(LWE) 기반 FHE 이론의 핵심 설계자. FHE, Secure Multi-Party Computation, 양자 암호학 등 근본적 기여. FHE 학술 커뮤니티 위상 강화 상징. [[G-17]](#ref-g-17)

5. **EUROCRYPT 2026 — 준선형 서버 시간 PIR(Private Information Retrieval) 달성.**
   Henzinger & Ragavan의 "Two-Server PIR in Sublinear Time and Quasilinear Space". 압축 선형 동형암호 활용, 통신 복잡도 n^0.31 수준. 정보 이론적 PIR 중 최초로 준선형 서버 저장+다항식 준선형 서버 시간 동시 달성. HE 키워드 검색의 이론적 효율성 상한 확장. [[G-18]](#ref-g-18)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Intel | Heracles FHE ASIC 일반 미디어 확산(3/19). 1,074~5,547× Xeon 가속. 양산 미발표 | [[G-14]](#ref-g-14) |
| UTS (호주) | FHE DRL Nature MI 게재(3/18). Meta AI Research·한양대 공동. 암호화 AI 학습 첫 실증 | [[G-13]](#ref-g-13) |
| LGU+ + CryptoLab | MWC 2026: ixi-O AI 에이전트+AICC에 CKKS 동형암호 탑재 협력. 국내 통신사 FHE 상용화 최근접 사례 | [[E-02]](#ref-e-02) |
| Niobium + SEMIFIVE | Samsung 8nm FHE ASIC 계약(2/19). 세계 최초 상용 FHE 가속기 목표. 설계 진행 중 | [[G-19]](#ref-g-19) |
| Zama (프랑스) | FHE.org 2026(타이베이, 3/8)에서 8편 기여. TFHE 부트스트래핑 가속, NIST 제출 준비 | [[G-20]](#ref-g-20) |

#### 시장 시그널

**파트너십 & 제휴**
- LGU+ + CryptoLab: ixi-O AI 에이전트 및 AICC에 CKKS 동형암호 적용. 국내 통신사 최초 FHE 상용화 경로 [[E-02]](#ref-e-02)
- Niobium + SEMIFIVE + Samsung Foundry: 세계 최초 상용 FHE ASIC 양산 계약(Samsung 8nm 8LPU) [[G-19]](#ref-g-19)

**시장 전망**
- HE 시장 규모: 2024년 $1.2B → 2031년 $8.4B(CAGR ~33%) [추정] [[G-21]](#ref-g-21)
- Niobium $23M+ 펀딩으로 세계 최초 상용 FHE ASIC 개발 가속(Samsung 8nm) [[G-22]](#ref-g-22)

**연구 동향**
- "Empowering AI with Homomorphic Encryption for Secure DRL" (Nguyen et al., Nature MI 2026) — FHE 상태 DRL 세계 최초 실증, 성능 격차 10% 이내 [[P-03]](#ref-p-03)
- "FHECore: Rethinking GPU Microarchitecture for FHE" (Jiang et al., arXiv 2026) — CKKS 2.41× 명령어 감소, 부트스트래핑 50% 감소 [[P-04]](#ref-p-04)
- "Two-Server PIR in Sublinear Time" (Henzinger & Ragavan, EUROCRYPT 2026) — 통신 복잡도 n^0.31, HE PIR 이론 한계 돌파 [[G-18]](#ref-g-18)

#### 시장 수요 (voice-of-market)

**고객 페인포인트**
- 성능 오버헤드 — GPU 대비 1,000배+ 느린 연산이 실서비스 배포를 차단. 출처: Panel on Hardware for FHE (Rosario Cammarota, Intel Labs / FHE.org Hardware Day 2025)
- FHE 애플리케이션 프로그래밍 극단적 난이도 — HEIR 등 컴파일러 없이 일반 프로그래머 접근 불가. 출처: Panel on Hardware for FHE (Cammarota / FHE.org Hardware Day 2025)
- 기존 데이터 파이프라인 통합 불가 — FHE를 실무 시스템에 편입하는 방법론 미정립. 출처: Panel on Hardware for FHE (Cammarota / FHE.org Hardware Day 2025)

**도입 장벽**
- 칩 제조 투자($100M) 대비 볼륨 시장 미성숙 — "킬러 애플리케이션"을 아직 발굴 중. 출처: Panel on Hardware for FHE (Paul Master, Cornami / FHE.org Hardware Day 2025)
- FHE 전문가 풀 전 세계 50명 미만. 출처: Panel on Hardware for FHE (Cammarota / FHE.org Hardware Day 2025)
- CKKS/BFV/TFHE 스키마별 하드웨어 최적화 단편화 — 상호운용성 표준 부재. 출처: Panel on Hardware for FHE (Master / FHE.org Hardware Day 2025)

**시장 니즈**
- Private LLM / 암호화 AI 추론 — 패널 전원이 FHE 볼륨 시장 1순위 후보로 지목. 출처: Panel on Hardware for FHE (Master / FHE.org Hardware Day 2025)
- FHE 친화적 자동 컴파일러 — 비전문가 접근성 확보 핵심 니즈. HEIR(Google), FHE on Cloud 등. 출처: Panel on Hardware for FHE (Master / FHE.org Hardware Day 2025)
- FHE-as-a-Service — Belfort가 AWS FPGA에 FHE 가속기 무료 배포, 2줄 코드 변경으로 FPGA 가속 전환. 출처: Belfort (Van Beirendonck / FHE.org Hardware Day 2025)

#### 전략적 시사점

**기회**
- UTS의 FHE DRL 실증은 "암호화 데이터에서 AI 학습"이라는 새로운 패러다임의 첫 증거. 중장기적으로 온디바이스 프라이버시 보존 AI 키워드 검색의 기초 기술
- LGU++CryptoLab의 ixi-O AICC 동형암호 적용은 국내 통신사 FHE 상용화의 최근접 사례 — 경쟁 벤치마크 필요

**위협**
- 성능 오버헤드(1,000×+)와 전문가 부족(50명 미만)이 단기 상용화의 근본 장벽
- Intel Heracles ASIC이 양산되면 하드웨어 가속 경쟁이 본격화, SW-only 접근의 경쟁력 약화 가능

---

## 경쟁사 동향 (SKT / KT)

> 이번 주 Secure AI 도메인과 관련된 SKT·KT의 주요 움직임.

### SKT

이번 주 해당 도메인 관련 SKT 신규 뉴스 없음. (전주: 에이닷 '위험 목소리 탐지' 성문 분석 출시 3/18, 정확도 96%, ICT 규제 샌드박스 승인)

### KT

이번 주 해당 도메인 관련 KT 신규 뉴스 없음. (MWC 2026서 6G Quantum-Safe 전략 발표: QKD+AI 침해탐지+동형암호 전 구간 적용 계획, 초당 30만 양자키 생성 장비 공개)

### 시사점
- 이번 주는 SKT·KT 모두 Secure AI 도메인 관련 신규 발표 없음. MWC 2026 및 전주 발표의 후속 이행 모니터링 필요
- LGU+의 ixi-Guardian 2.0(PQC+동형암호+SASE 통합)과 CryptoLab 협력이 경쟁사 대비 차별화 포인트로 부상 — SKT·KT의 대응 관심

---

## 규제 & 거버넌스

> Secure AI 도메인에 영향을 미치는 국내외 규제·표준·가이드라인 동향.

### 시행 임박 / 카운트다운

| 규제 | 시행일 | D-day |
|------|--------|-------|
| FCC SIP 603+ Analytics-Based Blocking 의무화 (미국) | 2026-03-25 | 시행 (금일) |
| EU AI Act Article 6 (High-Risk AI 의무) | 2026-08-02 | D-130 |
| EU CRA 보고 의무 (취약점 24시간 내 ENISA 보고) | 2026-09-11 | D-170 |
| FIPS 140-2 인증 종료 (NIST CMVP Historical 이전) | 2026-09-21 | D-180 |
| CNSA 2.0 NSS 신규 조달 의무화 | 2027-01-01 | D-281 |
| 한국 AI 기본법 Article 31 (AI 생성 표시) | 2026-01-22 | 시행 중 |

### 신규 발의 & 가이드라인

- **RSAC 2026 AI 에이전트 보안 이슈 부상(3/23-24)**: MCP(Model Context Protocol) 기반 에이전트-에이전트 통신의 보안 모니터링 공백 지적. Cisco DefenseClaw(에이전트 보안 프레임워크) 공개. IDC 2028년 13억 AI 에이전트 운영 전망 — 비인간 ID(Non-Human Identity) 거버넌스 수요 [[G-23]](#ref-g-23)
- **EU CRA 보고 의무 2026-09-11 시행**: 디지털 요소 포함 제품 제조사는 적극 악용 취약점을 ENISA에 24시간 내 조기 경보, 72시간 내 완전 통보 의무. On-Device PQC 디바이스 제조사에 직접 영향 [[G-24]](#ref-g-24)

### 시사점
- FCC 603+ 시행으로 analytics-based blocking 투명성 제도화 완료. 한국 통신 규제에 유사 프레임워크 논의 가능성
- FIPS 140-2 종료(D-180)·EU CRA(D-170)·CNSA 2.0(D-281) 삼중 데드라인이 2026년 하반기에 집중. PQC 솔루션 공급사와 수요 조직 모두에 구체적 일정 기반 대응 필요
- RSAC 2026의 AI 에이전트 보안 논의는 아직 초기 단계이나, 스팸/피싱 탐지용 AI 에이전트 자체의 보안도 고려해야 할 시점 도래

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **PQC와 FHE의 수렴** — Kudelski KSE3의 PQC 반도체 IP와 Niobium+SEMIFIVE의 FHE ASIC이 동일한 격자(Lattice) 기반 수학 구조를 공유. 중장기적으로 PQC+FHE 통합 칩 설계가 가능하며, "양자안전 암호화 데이터에서 AI 연산"이라는 궁극 비전에 수렴

2. **규제 삼중 데드라인 효과** — FIPS 140-2 종료(9/21)·EU CRA 보고(9/11)·CNSA 2.0(1/1/2027)이 동시 압박. 통신사와 디바이스 제조사는 PQC 마이그레이션 + 인증 체계 전환 + 보안 사고 보고 체계를 동시에 구축해야 하는 상황

3. **하드웨어 가속 경쟁 본격화** — Intel Heracles(ASIC), FHECore(GPU 확장), Niobium+Samsung(ASIC), Belfort(FPGA)가 각각 다른 아키텍처로 FHE 가속 경쟁. 2026년이 하드웨어 전쟁의 원년

### 후속 조치 제안

- 🟡 PQC — ZeroTier Quantum의 통신사 채택 가능성 추적. FIPS 140-2 종료(D-180) 대비 내부 인증 모듈 현황 점검. Crypto-agility 역량 자체 평가(NIST CSWP 39) 검토
- 🟡 동형암호 — LGU++CryptoLab ixi-O AICC 동형암호 적용 진행 상황 모니터링. UTS FHE DRL 후속 연구 추적
- 🟢 스팸/피싱 — FCC 603+ 시행 후 미국 통신사 실제 적용 현황 추적. C2PA 통신사 채택 진행 모니터링

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | The Quantum Insider — ZeroTier Launches ZeroTier Quantum | [링크](https://thequantuminsider.com/2026/03/24/zerotier-launches-zerotier-quantum-a-secure-networking-platform/) | news | 2026-03-24 | [B] |
| <a id="ref-g-02"></a>G-02 | BusinessWire — RSAC 2026: ZeroTier Quantum E2E Quantum-Secure Platform | [링크](https://www.morningstar.com/news/business-wire/20260322114599/rsac-2026-zerotier-launches-zerotier-quantum-the-worlds-first-end-to-end-quantum-secure-networking-platform) | 보도자료 | 2026-03-22 | [A] |
| <a id="ref-g-03"></a>G-03 | design-reuse.com — Kudelski Labs at Embedded World 2026: PQC + Edge AI + CRA | [링크](https://www.design-reuse.com/news/202530178-kudelski-labs-addresses-device-lifecycle-security-edge-ai-post-quantum-cryptography-and-regulatory-compliance-at-embedded-world-2026/) | news | 2026-03 | [B] |
| <a id="ref-g-04"></a>G-04 | EE Journal — Axelera AI Adds Kudelski KSE3 to Europa Edge AI Chip | [링크](https://www.eejournal.com/industry_news/axelera-ai-adds-kudelski-labs-security-ip-to-europa-chip-to-enable-secure-high-performance-edge-ai/) | news | 2026-03-10 | [B] |
| <a id="ref-g-05"></a>G-05 | New Electronics — Axelera AI Integrates Kudelski Secure Enclave into Europa | [링크](https://www.newelectronics.co.uk/content/news/axelera-ai-integrates-kudelski-secure-enclave-into-europa-edge-ai-chip) | news | 2026-03-10 | [B] |
| <a id="ref-g-06"></a>G-06 | GlobeNewswire — SEALSQ Deploys PQC for Blockchain Infrastructure | [링크](https://www.globenewswire.com/news-release/2026/03/20/3259796/0/en/SEALSQ-Deploys-Post-Quantum-Cryptography-to-Secure-Blockchain-and-Digital-Transaction-Infrastructures-Through-the-Deployment-of-Post-Quantum-Cryptographic-PQC-Technologies.html) | 보도자료 | 2026-03-20 | [A] |
| <a id="ref-g-07"></a>G-07 | SafeLogic — What Happens on September 21, 2026? FIPS 140-2 Sunset | [링크](https://www.safelogic.com/blog/what-happens-on-september-21-2026) | blog | 2026 | [B] |
| <a id="ref-g-08"></a>G-08 | EBN — LG유플러스 MWC 2026 ixi-Guardian 2.0 공개 | [링크](https://www.ebn.co.kr/news/articleView.html?idxno=1700902) | news | 2026-02 | [B] |
| <a id="ref-g-09"></a>G-09 | PR Newswire — QCi + Ciena PQC+QKD at OFC 2026 (1.6 Tb/s) | [링크](https://www.prnewswire.com/news-releases/quantum-computing-inc-and-ciena-demonstrate-next-generation-quantum-secured-communications-with-high-speed-encryption-using-pqc-and-qkd-at-ofc-2026-302710416.html) | 보도자료 | 2026-03-12 | [A] |
| <a id="ref-g-10"></a>G-10 | MarketsandMarkets — PQC Market 2025 $0.42B → 2030 $2.84B (CAGR 46.2%) | [링크](https://www.marketsandmarkets.com/PressReleases/post-quantum-cryptography.asp) | report | 2025 | [C] |
| <a id="ref-g-11"></a>G-11 | Security Boulevard — PQC Enterprise Migration Guide 2026 | [링크](https://securityboulevard.com/2026/03/post-quantum-cryptography-for-authentication-the-enterprise-migration-guide-2026/) | news | 2026-03 | [B] |
| <a id="ref-g-12"></a>G-12 | postquantum.com — Telecom's Quantum-Safe Imperative: SoftBank PQC Pilot | [링크](https://postquantum.com/post-quantum/telecom-pqc-challenges/) | news | 2026 | [B] |
| <a id="ref-g-13"></a>G-13 | UTS News — UTS Researchers Achieve Breakthrough in Privacy-Preserving AI | [링크](https://www.uts.edu.au/news/2026/03/uts-researchers-achieve-breakthrough-in-privacy-preserving-ai) | news | 2026-03-18 | [A] |
| <a id="ref-g-14"></a>G-14 | Privacy Guides — Intel's FHE Chip Could Revolutionize Privacy | [링크](https://www.privacyguides.org/news/2026/03/19/intels-fully-homomorphic-encryption-chip-could-revolutionize-privacy/) | news | 2026-03-19 | [B] |
| <a id="ref-g-15"></a>G-15 | Tom's Hardware — Intel Heracles 1,074-5,547× Faster Than Xeon | [링크](https://www.tomshardware.com/tech-industry/cyber-security/intels-heracles-chip-computes-fully-encrypted-data-without-decrypting-it-chip-is-1-074-to-5-547-times-faster-than-a-24-core-intel-xeon-in-fhe-math-operations) | news | 2026-03-18 | [B] |
| <a id="ref-g-16"></a>G-16 | Semiengineering — A GPU Microarchitecture Optimized for FHE | [링크](https://semiengineering.com/a-gpu-microarchitecture-optimized-for-fully-homomorphic-encryption/) | news | 2026-03-18 | [B] |
| <a id="ref-g-17"></a>G-17 | IACR — Vinod Vaikuntanathan Selected as IACR Fellow 2026 | [링크](https://iacr.org/news/item/28062) | news | 2026-03-23 | [A] |
| <a id="ref-g-18"></a>G-18 | GitHub — Two-Server PIR (Henzinger & Ragavan, EUROCRYPT 2026) | [링크](https://github.com/ahenzinger/finite-diffs-pir) | paper | 2026-03 | [A] |
| <a id="ref-g-19"></a>G-19 | PR Newswire — SEMIFIVE + Niobium FHE Accelerator (Samsung 8nm) | [링크](https://www.prnewswire.com/news-releases/semifive-partners-with-niobium-to-develop-fhe-accelerator-driving-us-market-expansion-302692312.html) | news | 2026-02-19 | [A] |
| <a id="ref-g-20"></a>G-20 | Zama — FHE.org 2026: Eight Contributions from Taipei | [링크](https://www.zama.org/post/zama-at-fhe-org-2026-eight-contributions-from-taipei) | news | 2026-03-08 | [A] |
| <a id="ref-g-21"></a>G-21 | OpenPR — Homomorphic Encryption Market $1.2B (2024) → $8.4B (2031) | [링크](https://www.openpr.com/news/4230086/homomorphic-encryption-market-by-type-and-application-rapid) | report | 2026 | [C] |
| <a id="ref-g-22"></a>G-22 | The Quantum Insider — Niobium Raises $23M+ for FHE Hardware | [링크](https://thequantuminsider.com/2025/12/03/niobium-23m-fhe-funding/) | news | 2025-12 | [B] |
| <a id="ref-g-23"></a>G-23 | SiliconANGLE — RSAC 2026: AI Agents Quantum Cybersecurity Challenges | [링크](https://siliconangle.com/2026/03/19/agents-quantum-cybersecurity-ai-security-challenges-rsac26/) | news | 2026-03-19 | [B] |
| <a id="ref-g-24"></a>G-24 | ComplianceHub.Wiki — EU CRA Reporting Deadlines June/September 2026 | [링크](https://compliancehub.wiki/eu-cyber-resilience-act-june-and-september-2026-reporting-deadlines-loom-for-manufacturers-of-products-with-digital-elements/) | news | 2026 | [B] |
| <a id="ref-e-01"></a>E-01 | BusinessWire / Thales — World First Quantum-Safe Security for 5G Networks | [링크](https://www.businesswire.com/news/home/20260301594505/en/Thales-sets-a-world-first-in-quantum-safe-security-5G-networks) | 보도자료 | 2026-03-02 | [A] |
| <a id="ref-e-02"></a>E-02 | Korea IT Times — LG Uplus + CryptoLab HE for ixi-O and AICC at MWC26 | [링크](https://www.koreaittimes.com/news/articleView.html?idxno=151253) | IR/발표 | 2026-03-10 | [A] |
| <a id="ref-p-01"></a>P-01 | arXiv:2512.20243 — Post-Quantum Cryptography in the 5G Core | [링크](https://arxiv.org/html/2512.20243v1) | paper | 2025-12 | [A] |
| <a id="ref-p-02"></a>P-02 | Ehlen et al. — Harvest-Now, Decrypt-Later: Temporal Risk in Quantum Transition (MDPI 2026) | [링크](https://www.mdpi.com/2673-4001/6/4/100) | paper | 2026 | [A] |
| <a id="ref-p-03"></a>P-03 | Nguyen et al. — Empowering AI with HE for Secure DRL (Nature MI, 2026) | [링크](https://www.nature.com/articles/s42256-025-01135-2) | paper | 2026-03-18 | [A] |
| <a id="ref-p-04"></a>P-04 | Jiang et al. — FHECore: Rethinking GPU Microarchitecture for FHE (arXiv:2602.22229) | [링크](https://arxiv.org/abs/2602.22229) | paper | 2026-02 | [A] |
