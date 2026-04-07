---
type: weekly-monitor
domain: secure-ai
week: 2026-W15
date: 2026-04-06
l3_count: 5
deep_count: 3
---

# 주간 기술 동향: Secure AI (2026-W15)

## Executive Summary

> **이번 주 핵심**: Google·Oratomic이 Cryptographically Relevant Quantum Computer (CRQC) 필요 물리 큐비트를 동시에 20배/900배 하향 조정(3/31)하며 Q-Day 위협이 최고조에 달했다. 동시에 Cisco IOS XE 26 전체 스택 Post-Quantum Cryptography (PQC) 상용화(4/1), 캐나다 연방 PQC 이행계획 의무화(4/1), Naoris Protocol Module-Lattice-Based Digital Signature Algorithm (ML-DSA) 블록체인 메인넷 출시(4/1) — "선언"에서 "실행"으로 전환이 동시 다발적으로 가속. 동형암호(Fully Homomorphic Encryption, FHE) 측에서는 Niobium "The Fog" 클라우드 플랫폼 출시(4/2)로 B2B FHE 서비스 시대 개막, CryptoLab HEaaN Zero-Leak RAG GS 1등급 인증(3/27)으로 국내 공공 조달 진입 확보. 스팸/피싱 영역은 INTERPOL-UNODC가 $442B 글로벌 사기 손실을 공식화하며 국제 공조 격상.

| Layer 2 | 세부기술 | 신호 | 핵심 내용 |
|---------|----------|------|----------|
| 양자/동형 암호 | On-Device PQC | 🔴 | [기술돌파] Google ECDLP <50만 큐비트·9분 해독(20배↓) · [제품출시] Cisco IOS XE 26 전체 스택 PQC · [규제] 캐나다 4/1 이행계획 의무화 |
| | On-Device 동형암호 | 🟡 | [제품출시] Niobium "The Fog" FHE 클라우드 프라이빗 베타(4/2) · [생태계] CryptoLab GS 1등급 인증, 공공 조달 진입 |
| | Secure Vector Search | 🟢 | Niobium Encrypted Semantic Search 연관이나 독립 돌파 없음 |
| 스팸/피싱탐지 | 스팸/피싱 감지(통화전) | 🟡 | [규제] INTERPOL $442B·47개국 행동계획 · [기술돌파] Agentic AI 사기 공식 위협 범주화 |
| | OCR 이미지 스팸 차단 | 🟢 | 신규 시그널 없음. Gmail RETVec+Gemini Nano 체계 유지 |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음
> **태그** : [기술돌파] [제품출시] [경쟁사] [규제] [투자] [논문] [생태계]

---

## 🟢 Quick 요약 (변화 미미)

### Secure Vector Search
- Niobium "The Fog"에 Encrypted Semantic Search(Secure RAG) 프리빌드 앱이 포함되어 FHE 벡터 검색 상용화 경로가 열렸으나, secure-vector-search 자체의 독립적 돌파는 없음. IronCore Labs 벡터 암호화 논의 지속. Apple BFV 기반 PIR 적용(iOS 18) 체계 유지.

### OCR 활용 이미지 스팸 차단
- 신규 시그널 없음. Gmail RETVec + Gemini Nano 온디바이스 보호 체계 유지. AI 기반 CAPTCHA 우회·프로필 사진 생성 등 공격 고도화 보고는 있으나 OCR 이미지 스팸 특화 돌파 없음.

---

## 🟡🔴 Deep 심층 분석

### On-Device PQC (양자내성암호) — 🔴 긴급

#### 이전 대비 변화
- 전주: Google 2029 PQC 데드라인 선언(3/25), Android 17 ML-DSA 4계층 통합(3/26), IBM+Signal 대역폭 100× 문제 정량화
- 금주: Google·Oratomic CRQC 필요 큐비트 20배 하향(3/31), 캐나다 4/1 이행계획 의무화, Cisco IOS XE 26 전체 스택 PQC(4/1), Naoris ML-DSA 메인넷(4/1)
- 변화 방향: 위협 가속(CRQC 자원 추정치 연속 하향) + 실행 전환(네트워크 장비·정부·블록체인 동시 PQC 구현) — "when"에서 "how fast"로 완전 전환

#### 기술 동향

1. **Google ECDLP 논문 — <50만 물리 큐비트로 Elliptic Curve Digital Signature Algorithm (ECDSA)-256 수분 내 해독, 종전 대비 20배 감소.**
   Google Quantum AI가 "Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities" 논문(arXiv:2603.28846, 3/31)을 공개했다. 표면 코드 기반 초전도체 아키텍처에서 <50만 물리 큐비트로 secp256k1 Elliptic Curve Discrete Logarithm Problem (ECDLP)-256 해독이 가능하며, 공개키 노출 후 수분(a few minutes) 내 개인키 복원이 핵심 주장이다. 이전 추정치 대비 약 20배 감소. Ethereum Foundation·Stanford 공동 저술. [[G-01]](#ref-g-01), [[E-01]](#ref-e-01)

2. **Oratomic 출범(3/31) — 10,000 중성원자 큐비트로 Shor's 알고리즘 실행 가능한 아키텍처.**
   Caltech 협력 스타트업 Oratomic이 quantum Low-Density Parity-Check (qLDPC) 코드 기반 아키텍처를 발표했다. 창업팀: Dolev Bluvstein(CEO), John Preskill, Manuel Endres(Caltech·Harvard·Google 출신). PQShield는 두 논문을 "CRQC 구현 4단계 중 서로 다른 계층을 동시에 해결하는 상호보완 연구"로 평가했다. [[G-02]](#ref-g-02), [[E-05]](#ref-e-05)

3. **캐나다 연방정부 PQC 이행계획 제출 마감(4/1) — 2031 고우선순위·2035 전면 완료 행정 지침 의무화.**
   캐나다 사이버보안센터(Canadian Centre for Cyber Security, CCCS) ITSM.40.001에 따라 연방 각 부처가 초기 PQC 이행계획을 제출했다. 4/1 이후 체결하는 디지털 요소 포함 계약 전체에 PQC 조달 조항이 의무화. Five Eyes 파트너(미 NSA·영 NCSC)와 조율된 일정. [[G-04]](#ref-g-04), [[E-04]](#ref-e-04)

4. **Cisco IOS XE 26 전체 스택 PQC — 네트워크 장비 계층 최초 NIST 표준 통합(4/1).**
   Cisco Live Amsterdam에서 발표. 부팅(C9000 Secure Boot), 이미지 무결성, 네트워크 트래픽(IPsec·MACsec), 관리 세션의 4계층을 모두 NIST 승인 알고리즘으로 보호. "업계 최초 전체 스택 PQC 아키텍처" 포지셔닝. [[G-07]](#ref-g-07), [[E-02]](#ref-e-02)

5. **Naoris Protocol ML-DSA 메인넷 출시(4/1) — NIST 승인 PQC 기반 최초 Layer 1 블록체인.**
   FIPS 204(ML-DSA)를 모든 트랜잭션 서명에 사용. 테스트 기간 1억600만 트랜잭션·6억300만 보안 위협 차단 검증. 한번 양자내성 키 채택 시 전통 암호화로 되돌릴 수 없는 비가역 전환 정책. [[G-08]](#ref-g-08)

6. **arXiv:2603.19340 — ARM Cortex-M0+ ML-KEM·ML-DSA 최초 체계적 벤치마크, IoT PQC 실용성 입증.**
   ML-KEM-512 완전 키 교환 35.7ms·2.83mJ(ECDH P-256 동일 하드웨어 대비 17배 빠름). 반면 ML-DSA 서명은 rejection sampling으로 99퍼센타일 최대 1,125ms — 실시간 보이스 프로토콜 설계 시 지연 버스트 고려 필수. [[P-01]](#ref-p-01)

7. **NIST IR 8547 — RSA/ECDSA 2030 deprecated, 2035 disallowed 기준 재확인.**
   초기 공개 초안(2024-11-12) 상태. 112비트 이하 레거시 알고리즘(RSA-2048, ECC P-256 포함)은 2030년 후 deprecated, 2035년 후 disallowed. FIPS 203(Module-Lattice-Based Key-Encapsulation Mechanism, ML-KEM), FIPS 204(ML-DSA), FIPS 205(Stateless Hash-Based Digital Signature Algorithm, SLH-DSA)를 핵심 대체 표준으로 지정. [[G-06]](#ref-g-06)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Google Quantum AI | ECDLP-256 <50만 큐비트 논문(3/31). 자체 2029 PQC 마감 재확인. Ethereum Foundation·Stanford 공동 저술 | [[G-01]](#ref-g-01), [[E-01]](#ref-e-01) |
| Oratomic | Caltech 협력 스텔스→공식 출범(3/31). 10K 중성원자 qLDPC 아키텍처. Bluvstein·Preskill·Endres 창업팀 | [[G-02]](#ref-g-02), [[E-05]](#ref-e-05) |
| Cisco | IOS XE 26 전체 스택 PQC 발표(4/1). C9000·IPsec·MACsec 4계층 NIST 알고리즘 | [[G-07]](#ref-g-07), [[E-02]](#ref-e-02) |
| Naoris Protocol | ML-DSA 레이어1 블록체인 메인넷(4/1). 1억600만 트랜잭션 검증. 시총 $36M | [[G-08]](#ref-g-08) |
| Quantum XChange | Phio TX 2026 Cybersecurity Excellence Awards PQC 금상(3/26). 크립토-어질리티 아키텍처 인정 | [[G-09]](#ref-g-09) |
| PQShield | Google·Oratomic 논문 공식 분석 리포트(4/1). "4단계 CRQC 프레임워크" 제시 | [[E-03]](#ref-e-03) |
| 캐나다 CCCS | 연방 PQC 이행계획 4/1 마감. 2031/2035 법적 의무. PQC 조달 조항 의무화 | [[G-04]](#ref-g-04), [[E-04]](#ref-e-04) |

#### 시장 시그널

**투자 & M&A**
- Oratomic, Caltech 협력 스텔스에서 공식 출범(3/31) — 투자 규모 미공개 [[G-02]](#ref-g-02)
- PQC 시장: 2026년 $12억 → 2035년 $130억(Juniper Research, CAGR 30%) [[G-12]](#ref-g-12)

**시장 전망**
- CRQC 필요 자원 추정치 연속 하향: 2천만(2019) → 100만 미만(2025-05) → 10만 미만(2026-02) → 50만 미만(2026-03, Google) [[G-15]](#ref-g-15)
- 2026 Entrust/Ponemon 조사: 40% 조직이 PQC 전환 "진행 중"이라 응답하나 실제 배포 완료 5% — 계획-실행 격차 35%p [[G-14]](#ref-g-14) [추가확인 필요]
- 상위 40% 웹사이트가 하이브리드 PQ 키 교환 지원. 퓨어 PQC보다 하이브리드 접근이 지배적 [[G-14]](#ref-g-14)

**도입 사례**
- Cisco IOS XE 26: 엔터프라이즈 스위칭 인프라 첫 전체 스택 PQC 상용화 [[G-07]](#ref-g-07)
- 캐나다 연방: 4/1 이후 신규 계약 전체에 PQC 조달 조항 의무화 [[G-04]](#ref-g-04)
- Naoris Protocol: ML-DSA 단독 서명, 레거시 알고리즘 강제 배제 — 블록체인 최초 [[G-08]](#ref-g-08)
- BTQ Technologies: BIP-360 비트코인 테스트넷 v0.3.0 구현(3/20). P2MR 합의, Dilithium 서명 opcode 활성화 [[G-10]](#ref-g-10)

**연구 동향**
- arXiv 2603.19340: ARM Cortex-M0+ ML-KEM-512 키 교환 35.7ms·2.83mJ(ECDH P-256 대비 17배 빠름) — IoT PQC 실용성 정량 확인 [[P-01]](#ref-p-01)
- PQShield 분석: Google·Oratomic 논문이 CRQC 4단계(물리→논리→알고리즘→공격) 중 2단계·3단계를 동시 진전 [[E-03]](#ref-e-03)

**커뮤니티 시그널**
- Ethereum 연구자 Justin Drake(논문 공동 저자): "양자컴퓨팅과 암호학에서 기념비적인 날" [[G-13]](#ref-g-13)
- BIP-360 공동 저자: "비트코인 완전 양자내성 전환에 7년 소요" 경고 [[G-11]](#ref-g-11)

#### 시장 수요 (voice-of-market)

**고객 페인포인트**
- 인터넷 인프라 미준비 — TLS 핸드셰이크에서 인증서 크기 1KB 증가 시 응답 시간 1.5% 증가. 프로토콜 ossification 문제 — 출처: PKI Consortium PQC Conference Austin 2025
- 암호화 자산 인벤토리 규모 — macOS 단말 25만 개, Windows 단말 36.9만 개 암호키. Operational Technology (OT) 인벤토리 도구 부재 — 출처: PKI Consortium 2025
- Hardware Security Module (HSM) FIPS 인증 병목 — PQC 알고리즘 검증 대기로 컴플라이언트 배포 자체 불가 — 출처: RSA Conference 2025 (PQShield 패널)

**도입 장벽**
- 대기업 마이그레이션 12~15년 이상 소요 예상. 2035년 마감 감안 시 지금 시작해도 빠듯 — 출처: Enterprise PQC Migration Study (postquantum.com)
- 국가별 규제 단편화 — 프랑스 ANSSI는 하이브리드 권고, 미국 NSA는 하이브리드 금지 — 출처: PKI Consortium Kuala Lumpur 2025
- PQC 전문 인력 68% 조직이 확보 어려움 — 출처: ISACA 2025

**시장 니즈**
- Crypto-Agility 플랫폼 — 알고리즘 교체 시 운용 중단 없는 아키텍처 — 출처: RSA 2025 (PQShield)
- 암호화 자산 자동 발견/인벤토리 도구 (특히 OT 환경) — 출처: PKI Consortium 2025
- Harvest Now, Decrypt Later (SNDL) 대응 즉시 키 교환 마이그레이션 — 출처: HN 커뮤니티

#### 전략적 시사점

**기회**
- Cisco IOS XE 26 상용화로 코어 네트워크 조달 기준이 PQC 지원으로 이동. 국내 스위칭·라우팅 교체 로드맵에 PQC 조달 기준 반영 시점
- arXiv 벤치마크(ML-KEM-512 35.7ms)로 온디바이스 보이스 단말 키 교환이 실용 수준임을 정량 확인. Voice over Long-Term Evolution (VoLTE)/Voice over New Radio (VoNR) PQC 프로토콜 설계에 직접 참조 가능
- 캐나다·미국 정부 조달 PQC 의무화 동시 구체화 — 공공기관 대상 PQC 솔루션·컨설팅 선점 기회

**위협**
- Google·Oratomic 논문으로 Store-Now-Decrypt-Later (SNDL) 위험 현실화 가속. 현재 VoLTE/VoNR 트래픽의 ECDSA/ECDH 보호가 CRQC 등장 후 무력화 가능
- ML-DSA 서명 99퍼센타일 지연 1,125ms — Session Initiation Protocol (SIP) INVITE/200 OK 과정에서 체감 품질 저하 가능성. 하이브리드 방식에서도 PQC 서명이 최대 성능 병목
- BIP-360 "7년 전환 경고"는 통신사에도 적용 — 2026년 시작 기준 NIST 2030 데드라인 달성 빠듯

---

### 스팸/피싱 감지(통화전) — 🟡 주목

#### 이전 대비 변화
- 전주: Meta 안티스캠 AI, AI 피싱 204% 급증, Google 3월 스팸 업데이트, QRishing 급부상
- 금주: INTERPOL-UNODC $442B 공식화(3/16–17), ABA 등 금융권 연방 정책 20개 권고안(4/1), Agentic AI 사기 독립 위협 범주화
- 변화 방향: ① 규제 프레임이 산업 자율→국제 공조·정부 입법으로 격상 ② 공격이 딥페이크 음성→완전 자율 AI 에이전트로 진화 ③ 방어도 RAG 기반 정책 검증, Pindrop 2초 탐지 등 고도화

#### 기술 동향

1. **Agentic AI 사기 — 완전 자율화 공격 벡터 공식화.**
   Experian과 Security Boulevard가 '에이전트형 AI 사기'를 독립 위협 범주로 명명. 신원 팜(Identity Farm)이 AI 에이전트로 800점대 신용점수를 프로그래매틱 생성. Sardine AI에 따르면 은행·핀테크·크립토에서 실손해 발생 중. [[G-32]](#ref-g-32), [[G-33]](#ref-g-33)

2. **Retrieval-Augmented Generation (RAG) 기반 실시간 통화 사기 탐지.**
   Singh et al.이 통화를 실시간 전사 후 RAG로 발신자의 개인정보 요청을 정책 문서와 대조 검증하는 프레임워크 제안. 정확도 97.98%, F1 97.44%. 모델 재학습 없이 정책 업데이트 가능. [[P-03]](#ref-p-03)

3. **인간의 AI 음성 구분 능력 — 우연 수준 이하(37.5%) 확인.**
   Bhatti et al. 실험(arxiv, 철회 상태 참고용)에서 AI 생성 클립의 75%가 인간으로 오분류. "인간 판단" 기반 방어선 사실상 붕괴. [[P-04]](#ref-p-04)

4. **Pindrop Pulse — 2초 발화로 99% 딥페이크 탐지.**
   370+ Text-to-Speech (TTS) 시스템 데이터, 2,000만+ 오디오 파일 학습. 오탐율 1% 미만. [[G-34]](#ref-g-34)

5. **IEEE 2026 — 에이전트형 AI 보이스피싱 탐지 프레임워크.**
   공격에서 쓰이는 에이전트형 AI를 방어에도 동일하게 적용하는 대칭 접근. [[P-05]](#ref-p-05)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| INTERPOL / UNODC | 비엔나 정상회담(3/16–17). $442B 손실 공식화, 47개국 행동계획. AI 사기 4.5x 수익성 의제 [원문 미확인] | [[G-36]](#ref-g-36), [[G-37]](#ref-g-37) |
| ABA / Better Identity Coalition | 연방 정책 20개 권고안(4/1): Fast Identity Online (FIDO) 패스키 의무화, 디지털 여권, IRS/USPS 신원 검증 강화 | [[G-38]](#ref-g-38) |
| Pindrop | Pulse: 2초 탐지, 99% 딥페이크 엔진 탐지율. 370+ TTS 시스템 대상 | [[G-34]](#ref-g-34) |
| Adaptive Security | $81M Series B(Bain Capital, NVIDIA NVentures, OpenAI Fund, a16z). 누적 $146.5M | [[G-44]](#ref-g-44) |
| KT | '후후' 실시간 보이스피싱 탐지: 문맥+화자+딥보이스 삼중 체계. Q4 정확도 97.2% | [[G-39]](#ref-g-39) |
| AT&T | 자율 AI 에이전트 배포로 사기 탐지·네트워크 이상 관리 실시간화 | [[G-40]](#ref-g-40) |

#### 시장 시그널

**피해 규모**
- 글로벌 조직화 사기 손실: $442B (Global Anti-Scam Alliance (GASA) 추정) [[G-36]](#ref-g-36)
- AI 사기 손실(미국): 2023년 $12.3B → 2027년 $40B 전망 (Deloitte) [[G-38]](#ref-g-38)
- 딥페이크 비싱 사건당 평균 $600K, 10%+ 사건 $1M 초과 [[G-43]](#ref-g-43) [추가확인 필요]

**투자 & M&A**
- Adaptive Security $81M Series B — NVIDIA·OpenAI·a16z 참여. 총 $146.5M 조달. 딥페이크 방어 특화 [[G-44]](#ref-g-44)

**규제·정책**
- INTERPOL-UNODC 47개국 공동 행동 계획(3/16–17) [[G-36]](#ref-g-36)
- ABA 연방 정책: 디지털 여권, FIDO 패스키 의무화, IRS/USPS 신원 검증 신설 [[G-38]](#ref-g-38)

**연구 동향**
- Singh et al.: RAG 기반 실시간 사기 탐지 97.98% 정확도 (arXiv 2501.15290) [[P-03]](#ref-p-03)
- IEEE 2026: 에이전트형 AI 보이스피싱 탐지 대칭 접근 프레임워크 [[P-05]](#ref-p-05)

**커뮤니티 시그널**
- HN 실무자: "딥페이크 탐지는 딥페이크 생성보다 느리다. 탐지 API 공개 시 공격자 피드백 루프" — 탐지-생성 군비경쟁 근본 문제 지적
- HN 실무자: "HSM이 도난을 암호학적으로 서명한다. 서명은 유효하고 의도는 가짜" — 현행 암호 인프라 공백 지적

#### 시장 수요 (voice-of-market)

**고객 페인포인트**
- 실시간 탐지 불가 — 화상회의 중 피해 발생 후에야 인식. 사후 분석 중심 — 출처: RSAC 2025 CISO 인터뷰 (Pindrop)
- 콘택트센터 사기 46초마다 1건. 2024년 보험 +475%, 은행 +149%, 소매 +107% — 출처: Pindrop 2025 Voice Intelligence Report
- 딥페이크 채용 후보자 — 2차 기술면접 6~8% 프록시 사기, 4명 중 1명 북한 IT 인력 위장 — 출처: Pindrop RSAC 2025

**도입 장벽**
- 탐지-생성 군비경쟁 — 탐지 API 공개 시 공격자 피드백 루프 악용 — 출처: HN Reality Defender 쓰레드
- 블랙박스 거부감 — CISO들은 설명 가능하고 워크플로우 통합 가능한 솔루션 요구 — 출처: RSAC 2025 (Pindrop)
- 인간 판별 능력 ~50% 수준 — 교육만으로는 탐지 불가 — 출처: Pindrop 2025

**시장 니즈**
- 실시간 딥페이크 탐지(라이브 화상회의/콜센터) — 출처: RSAC 2025 (Pindrop Pulse for Meetings)
- 연속 신원 아키텍처 — ① 진짜인가? ② 이 사람인가? ③ 우리 고객인가? — 모든 상호작용 지점 검증 — 출처: RSAC 2025
- 통신사 네트워크 레이어 AI 사기 콜 자동 차단 — 출처: TADSummit 2025

#### 전략적 시사점

**기회**
- INTERPOL-UNODC 공조 프레임과 ABA 정책이 국내 규제 설계 레퍼런스로 활용 가능
- Agentic AI 사기 대응에 에이전트형 방어(IEEE 2026)를 선제 적용하면 기술 차별화 가능
- RAG 기반 실시간 정책 검증은 통화 중 컴플라이언스 확인에 재학습 없이 적용 가능 — 부가서비스 제품화 기회

**위협**
- 인간 판단 37.5% 정확도 — 2차 검증 의존 체계 근본 한계 노출
- Agentic Fraud: 합성 신원 800점대 자동 생성 → 기존 신원 검증 전면 무력화
- Large Language Model (LLM) 피싱 자동화로 공격 비용 95% 절감 — 사기 규모 급확대 압력

---

### On-Device 동형암호 키워드 검색 — 🟡 주목

#### 이전 대비 변화
- 전주: "Privacy at your Fingertips" FHE 97% 감소, CAT GPU 33× 가속, Zama+T-REX $32B RWA FHE, Intel Heracles
- 금주: Niobium "The Fog" FHE 클라우드 프라이빗 베타(4/2), CryptoLab HEaaN Zero-Leak RAG GS 1등급(3/27), LG U++CryptoLab AICC 동형암호 PoC 상세 확인
- 변화 방향: 하드웨어 발표 → **소프트웨어 플랫폼·인증 상용화** 전환. B2B FHE 서비스 시대 개막

#### 기술 동향

1. **Niobium "The Fog" — FHE 클라우드 플랫폼 프라이빗 베타 개시(4/2).**
   암호화된 채로 AI 워크로드를 실행하는 프라이빗 클라우드 인프라. Field-Programmable Gate Array (FPGA) 기반 mistic Core 가속기(GPU 대비 2×). Encrypted Semantic Search(Secure RAG)·Federated Learning·ML Classification 프리빌드 앱 제공. SemiFive·Samsung Foundry 8nm Application-Specific Integrated Circuit (ASIC) 개발 중. Q2 2026 말 공개 출시 목표. [[G-17]](#ref-g-17), [[E-06]](#ref-e-06)

2. **CryptoLab HEaaN Zero-Leak RAG — TTA GS 1등급 인증(3/27), 공공 조달 진입 확보.**
   벡터 DB를 처음부터 동형암호로 암호화해 암호문 상태에서 유사도 검색. 평문 대비 ~99% 정확도, 첫 토큰 ~1.9초. Open Web Application Security Project (OWASP) LLM Top 10 중 임베딩 역변환 공격 방어 유일 공인 솔루션. 6월 조달청 혁신 시제품, 9월 Common Criteria (CC) 인증(EAL2) 예정. Gartner 혁신 기술 선정 국내 최초 동형암호 기업. [[G-19]](#ref-g-19), [[E-07]](#ref-e-07)

3. **NIST Multi-Party Threshold Schemes (MPTS) 2026 워크숍 — Threshold FHE from Cheon-Kim-Kim-Song (CKKS) 시연(1월).**
   CryptoLab Damien Stehlé 발표. 분산 키 생성으로 신뢰 딜러 없이 FHE 파라미터화 구현. Multi-Party Computation (MPC) + FHE 융합 표준화 진행 중. [[G-21]](#ref-g-21)

4. **Intel Heracles ISSCC — 1,074~5,547× Xeon 대비 가속, 3nm FinFET(3/10 발표, 본주 보도 확산).**
   197mm², 176W, Intel 3 공정. 48GB High Bandwidth Memory (HBM) 819 GB/s. 8192-way Single Instruction Multiple Data (SIMD). BGV·BFV·CKKS 다중 스킴 지원. PCIe 가속기 형태. 양산 일정 미발표. [[G-23]](#ref-g-23), [[E-08]](#ref-e-08)

5. **LG U+ + CryptoLab MWC 2026 — ixi-O AI Contact Center (AICC) 동형암호 탑재 협력 상세 확인.**
   통화 데이터를 동형암호 상태로 저장, 복호화 없이 키워드 검색. CKKS+(4.5세대) "실시간 지연 없이" 온디바이스 경량화 달성. 국내 통신사 최초 FHE 실서비스 적용 경로. [[G-25]](#ref-g-25), [[E-09]](#ref-e-09)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Niobium | "The Fog" 프라이빗 베타(4/2). mistic Core FPGA(GPU 2×). Encrypted Semantic Search 프리빌드. SemiFive·Samsung ASIC 개발 중. 누적 $2,300만+ | [[G-17]](#ref-g-17), [[E-06]](#ref-e-06) |
| CryptoLab | HEaaN Zero-Leak RAG GS 1등급(3/27). Gartner 선정 국내 최초. LG U+ AICC PoC. CKKS+ 온디바이스 경량화. 6월 조달청 등록 | [[G-19]](#ref-g-19), [[E-07]](#ref-e-07), [[E-09]](#ref-e-09) |
| Intel | Heracles ISSCC 공개(3/10). 1,074~5,547× 가속. 3nm, 48GB HBM. 양산 미발표 | [[G-23]](#ref-g-23), [[E-08]](#ref-e-08) |
| Zama | FHE.org 2026 타이페이 발표 8건. TFHE 부트스트래핑 GPU 서브밀리초. T-REX $32B RWA. 유니콘 지위 | [[G-27]](#ref-g-27) |
| LG U+ | CryptoLab과 ixi-O·AICC 동형암호 협력(MWC 3/4). 국내 통신사 최초 FHE 실서비스 경로 | [[G-25]](#ref-g-25), [[E-09]](#ref-e-09) |

#### 시장 시그널

**플랫폼 상용화**
- Niobium The Fog: B2B FHE 클라우드 최초 프리빌드 앱 모델. 암호화 비전문가도 FHE 앱 구축 가능 [[G-17]](#ref-g-17)
- CryptoLab: GS 1등급으로 국내 공공 조달 시장 진입. 6월 조달청, 9월 CC(EAL2) [[G-19]](#ref-g-19)

**하드웨어 공급망**
- Samsung Foundry: SemiFive 통해 Niobium FHE ASIC 수주(8nm). FHE 전용 칩 최초 대형 파운드리 계약 [[G-26]](#ref-g-26)

**시장 전망**
- FHE 시장: 2024년 $12억 → 2033년 $84억, CAGR 30% (Market Research Intellect) [[G-31]](#ref-g-31) [추가확인 필요]
- Gartner Hype Cycle 2026: 기밀 컴퓨팅(Confidential Computing) 핵심 아키텍처 기술 선정 [[G-30]](#ref-g-30)

**연구 동향**
- NIST MPTS 2026: Threshold FHE from CKKS — 분산 키 생성으로 다자간 FHE 표준화 진행 [[G-21]](#ref-g-21)
- THED(Threshold Dilithium from FHE) IACR ePrint 2026/638 공개 [[P-02]](#ref-p-02)

#### 시장 수요 (voice-of-market)

**고객 페인포인트**
- FHE 배포 시 주변 인프라(키관리·TEE·메시징)가 FHE 자체보다 구현 비용 대부분 차지 — 출처: FHE.org 2025 Sofia (Bergamaschi, Intel Labs)
- 암호문 쿼리 시 전체 DB 순회 강제(O(n)) — 대용량 환경 성능 병목 — 출처: 동일
- 부트스트래핑 ~1,000× 오버헤드 물리적 하한 — 출처: HN 실무자 커뮤니티

**도입 장벽**
- GPU 백엔드 미완성 — OpenFHE GPU 지원 ETA 미정 — 출처: FHE.org 2025 (Polyakov, Duality Technologies)
- 파라미터 선정 자동화 부재 — HEIR 컴파일러 CKKS 노이즈 모델 미구현. "We don't have a good answer" — 출처: FHE.org 2025 (Jeremy Kun, Google)
- LLM 추론 FHE 적용 불가 — 6개월 내 지원 불가 공식 인정 — 출처: 동일

**시장 니즈**
- 하드웨어 가속기 통합 — Google, Intel, FPGA 벤더 동시 작업 중 — 출처: FHE.org 2025 (Google HEIR)
- Python 고수준 프론트엔드 — HEIR "most requested feature" — 출처: 동일
- 금융·헬스케어 프라이빗 쿼리 서비스 — 복수 금융기관 공유 DB에 쿼리 미노출 조회 PoC 검증 — 출처: FHE.org 2025 (Bergamaschi)

#### 전략적 시사점

**기회**
- CryptoLab GS 1등급은 국내 공공 조달 직접 경로. AICC 수요를 조달로 충당 시 경쟁 우위
- LG U+–CryptoLab PoC 성공 시 KT/SKT 동형암호 AICC 도입 압박 발생
- Niobium Encrypted Semantic Search는 클라우드 기반 Secure RAG SaaS 시장 정의 첫 사례

**위협**
- Intel Heracles 양산 미발표 — 실제 배포 시점 지연 리스크 지속
- Apple·AWS·Google FHE.org 후원 진입 — 자체 클라우드 FHE 서비스 시 국내 솔루션 잠식 가능
- CKKS 근사 암호화 보안 정의(Differential Private Homomorphic Evaluation, DPHE) 표준화 미완료 — 규제 불확실성

---

## 경쟁사 동향 (SKT / KT)

> 이번 주 해당 도메인 관련 SKT·KT의 주요 움직임.

### SKT

이번 주(3/30~4/6) secure-ai 도메인 관련 SKT 신규 뉴스 없음.

참고(기존 현황): Quantum Key Distribution (QKD)-PQC 하이브리드 장비(세계 최초), 위성 탑재 QKD 국책과제(IITP, 2028년까지), 에이닷 '위험 목소리 탐지' + 2025년 11억 건 AI 스팸/피싱 차단(+35% YoY).

### KT

이번 주(3/30~4/6) secure-ai 도메인 관련 KT 신규 뉴스 없음.

참고(기존 현황): MWC 2026 6G 비전에 Quantum Safe Security 핵심 기술 포함. QKD+AI 침입탐지+동형암호 전 구간 적용 계획. '후후' 보이스피싱 탐지 Q4 97.2% 정확도 달성.

### 시사점
- 이번 주 경쟁사 secure-ai 관련 신규 발표 없음. 전주까지의 포지셔닝 유지: SKT(PQC 하드웨어 선두), KT(AI 피싱 탐지 실적 기반)
- LG U+가 CryptoLab과 동형암호 AICC 차별화를 선점 중 — KT/SKT 미대응 시 프라이버시 차별화 포인트 선점당할 가능성 지속

---

## 규제 & 거버넌스

> 해당 도메인에 영향을 미치는 국내외 규제·표준·가이드라인 동향.

### 시행 임박 / 카운트다운

| 규제 | 시행일 | D-day |
|------|--------|-------|
| EU AI Act Article 6 (High-Risk AI 의무) | 2026-08-02 | D-118 |
| EU Cyber Resilience Act (CRA) 보고 의무 (취약점 24시간 내 ENISA 보고) | 2026-09-11 | D-158 |
| FIPS 140-2 인증 종료 (NIST CMVP Historical 이전) | 2026-09-21 | D-168 |
| Commercial National Security Algorithm (CNSA) 2.0 National Security Systems (NSS) 신규 조달 의무화 | 2027-01-01 | D-269 |
| NIST IR 8547 RSA/ECDSA deprecated (초안) | 2030 | D-~1,365 |
| NIST IR 8547 RSA/ECDSA disallowed (초안) | 2035 | D-~3,192 |
| 캐나다 PQC 고우선순위 시스템 완료 | 2031 | D-~1,730 |
| 한국 AI 기본법 Article 31 (AI 생성 표시) | 2026-01-22 | 시행 중 |
| FCC SIP 603+ Analytics-Based Blocking | 2026-03-25 | 시행 중 |
| 캐나다 PQC 이행계획 제출·PQC 조달 조항 | 2026-04-01 | 시행 중 |

### 신규 발의 & 가이드라인

- **캐나다 CCCS ITSM.40.001(4/1)**: 연방 부처 PQC 이행계획 의무 제출. 4/1 이후 신규 계약 전체에 PQC 조달 조항 의무화. 2031 고우선순위·2035 전면 완료 [[G-04]](#ref-g-04), [[E-04]](#ref-e-04)
- **ABA·Better Identity Coalition 연방 정책 20개 권고안(4/1)**: 딥페이크 대응, FIDO 패스키 의무화, 디지털 여권, IRS/USPS 신원 검증 강화. 130명+ 전문가 18개월 작업 [[G-38]](#ref-g-38)
- **INTERPOL-UNODC 47개국 행동계획(3/17)**: AI 사기 국제 공조 프레임 구축. $442B 손실 공식화 [[G-36]](#ref-g-36)
- **EU PQC 로드맵**: 회원국 2026년 말까지 종합 PQC 이행계획 수립 의무

### 시사점
- 캐나다 4/1 마감이 Five Eyes 국가 최초의 구속력 있는 PQC 조달 의무화 사례 — 미국·영국·호주 후속 조치 촉매 역할
- ABA 디지털 여권·FIDO 패스키 권고는 국내 금융권 딥페이크 대응 규제 설계 레퍼런스
- NIST 2030/2035 타임라인과 Google 2029 민간 데드라인이 동시에 구체화 — 통신사 PQC 로드맵 2030 기준이면 이미 늦을 수 있음

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **PQC "실행" 국면 진입** — Google ECDLP 20배 하향 + Cisco IOS XE 26 전체 스택 + 캐나다 4/1 의무화가 같은 주에 발생. "선언→실행" 전환이 공식화됐으며, 통신사 로드맵 2030 기준이면 대기업 12~15년 마이그레이션 소요를 감안할 때 이미 빠듯함

2. **FHE 플랫폼 시대 개막** — Niobium "The Fog"가 FHE를 SaaS 형태로 제공하는 최초 사례. CryptoLab GS 인증으로 공공 조달 진입. 하드웨어(Intel Heracles, Samsung ASIC) + 소프트웨어(The Fog, HEaaN) + 인증(GS, Gartner) 3축이 동시에 움직이는 두 번째 연속 주

3. **AI 사기 규제 국제화** — INTERPOL $442B + ABA 정책 20개 + FIDO 패스키 의무화 흐름은 통신사의 AI 피싱 방어가 단순 부가서비스에서 규제 컴플라이언스 의무로 격상되는 시그널

### 후속 조치 제안

- 🔴 PQC — `/wtis standard` 검증 권고. Cisco IOS XE 26 상용화가 국내 네트워크 장비 조달 기준에 미치는 영향 평가. ML-DSA 서명 지연(99p 1,125ms)이 VoLTE/VoNR에 미치는 영향 PoC 검토
- 🟡 동형암호 — CryptoLab GS 1등급 + LG U+ PoC 진행 상황 추적. Niobium "The Fog" 공개 출시(Q2) 모니터링
- 🟡 스팸/피싱 — ABA 정책 20개 권고안 국내 규제 매핑 검토. Agentic AI 사기 대응 에이전트형 방어(IEEE 2026) 기술 타당성 평가

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Google Research Blog — Safeguarding cryptocurrency by disclosing quantum vulnerabilities responsibly | [링크](https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/) | news | 2026-03-31 | [A] |
| <a id="ref-g-02"></a>G-02 | The Quantum Insider — Oratomic Launches to Build Utility-Scale Quantum Computers | [링크](https://thequantuminsider.com/2026/03/31/oratomic-launches-to-build-utility-scale-quantum-computers/) | news | 2026-03-31 | [B] |
| <a id="ref-g-04"></a>G-04 | PQShield — Canada publishes new PQC migration roadmap | [링크](https://pqshield.com/canada-publishes-new-pqc-migration-roadmap/) | news | 2026-04-01 | [B] |
| <a id="ref-g-06"></a>G-06 | NIST CSRC — IR 8547 Transition to Post-Quantum Cryptography Standards (IPD) | [링크](https://csrc.nist.gov/pubs/ir/8547/ipd) | news | 2024-11-12 | [A] |
| <a id="ref-g-07"></a>G-07 | Security Boulevard — PQC: Moving From Awareness to Execution (Cisco IOS XE 26) | [링크](https://securityboulevard.com/2026/04/post-quantum-cryptography-moving-from-awareness-to-execution/) | news | 2026-04-01 | [B] |
| <a id="ref-g-08"></a>G-08 | The Quantum Insider — Naoris Protocol Launches Mainnet, Introducing Post-Quantum Layer 1 Blockchain | [링크](https://thequantuminsider.com/2026/04/01/naoris-protocol-launches-mainnet-introducing-post-quantum-layer-1-blockchain/) | news | 2026-04-01 | [B] |
| <a id="ref-g-09"></a>G-09 | National Law Review — Quantum XChange Wins Gold for PQC in 2026 Cybersecurity Excellence Awards | [링크](https://natlawreview.com/press-releases/quantum-xchange-wins-gold-post-quantum-cryptography-2026-cybersecurity) | news | 2026-03-26 | [B] |
| <a id="ref-g-10"></a>G-10 | The Quantum Insider — BTQ Technologies Implements BIP-360 Quantum-Resistant Bitcoin Transactions on Testnet | [링크](https://thequantuminsider.com/2026/03/20/btq-technologies-implements-bip-360-quantum-resistant-bitcoin-transactions-testnet/) | news | 2026-03-20 | [B] |
| <a id="ref-g-11"></a>G-11 | CoinTelegraph — Bitcoin may take 7 years to upgrade to post-quantum: BIP-360 co-author | [링크](https://cointelegraph.com/magazine/bitcoin-7-years-upgrade-post-quantum-bip-360-co-author/) | news | 2026-04-01 | [B] |
| <a id="ref-g-12"></a>G-12 | Juniper Research — Post-quantum Cryptography Market to Exceed $13 Billion by 2035 | [링크](https://www.juniperresearch.com/press/post-quantum-cryptography-market-to-exceed-13-billion-by-2035-as-q-day-awareness-accelerates/) | news | 2026 | [B] |
| <a id="ref-g-13"></a>G-13 | CoinDesk — BTC bulls scramble for post-quantum protection as Google drops bombshell paper | [링크](https://www.coindesk.com/tech/2026/03/31/bitcoin-bulls-scramble-for-post-quantum-protection-as-google-drops-bombshell-paper) | news | 2026-03-31 | [B] |
| <a id="ref-g-14"></a>G-14 | Security Boulevard — PQC: Moving From Awareness to Execution (enterprise adoption stats) | [링크](https://securityboulevard.com/2026/04/post-quantum-cryptography-moving-from-awareness-to-execution/) | news | 2026-04-01 | [B] |
| <a id="ref-g-15"></a>G-15 | The Quantum Insider — Q-Day Just Got Closer: Three Papers in Three Months | [링크](https://thequantuminsider.com/2026/03/31/q-day-just-got-closer-three-papers-in-three-months-are-rewriting-the-quantum-threat-timeline/) | news | 2026-03-31 | [B] |
| <a id="ref-g-17"></a>G-17 | SiliconANGLE — Niobium brings fully encrypted AI workloads to the cloud with The Fog | [링크](https://siliconangle.com/2026/04/02/niobium-brings-fully-encrypted-ai-workloads-cloud-fog/) | news | 2026-04-02 | [B] |
| <a id="ref-g-19"></a>G-19 | Seoul Economic Daily — CryptoLab Earns Top-Tier GS Certification | [링크](https://en.sedaily.com/news/2026/03/27/cryptolab-earns-top-tier-gs-certification-targets-public) | news | 2026-03-27 | [B] |
| <a id="ref-g-21"></a>G-21 | NIST CSRC — Threshold FHE from CKKS and Applications (MPTS 2026 발표) | [링크](https://csrc.nist.gov/presentations/2026/mpts2026-2b4) | news | 2026-01-29 | [A] |
| <a id="ref-g-23"></a>G-23 | IEEE Spectrum — Intel's Heracles Chip Speeds Up FHE Computing | [링크](https://spectrum.ieee.org/fhe-intel) | news | 2026-03-10 | [A] |
| <a id="ref-g-25"></a>G-25 | The Asia Business Daily — LG Uplus and CryptoLab Aim to Block Hacking with Homomorphic Encryption (MWC 2026) | [링크](https://www.asiae.co.kr/en/article/2026031008212144575) | news | 2026-03-10 | [B] |
| <a id="ref-g-26"></a>G-26 | Evertiq — SemiFive secures design win with Niobium for FHE accelerator | [링크](https://evertiq.com/design/2026-02-20-semifive-secures-design-win-with-niobium-for-fhe-accelerator) | news | 2026-02-20 | [B] |
| <a id="ref-g-27"></a>G-27 | Zama — Zama at FHE.org 2026: Eight Contributions from Taipei | [링크](https://www.zama.org/post/zama-at-fhe-org-2026-eight-contributions-from-taipei) | news | 2026-03-08 | [B] |
| <a id="ref-g-30"></a>G-30 | Duality Technologies — Post-Quantum FHE for Zero-Footprint Intelligence | [링크](https://dualitytech.com/blog/securing-the-future-post-quantum-fhe-for-zero-footprint-intelligence/) | news | 2026 | [B] |
| <a id="ref-g-31"></a>G-31 | Market Research Intellect — Global Homomorphic Encryption Market | [링크](https://www.marketresearchintellect.com/product/global-homomorphic-encryption-market-size-and-forecast/) | news | 2026 | [C] |
| <a id="ref-g-32"></a>G-32 | Security Boulevard — The Rise of Agentic Fraud: How AI Agents Are Reshaping Security | [링크](https://securityboulevard.com/2026/03/the-rise-of-agentic-fraud-how-ai-agents-are-reshaping-security/) | news | 2026-03 | [B] |
| <a id="ref-g-33"></a>G-33 | Experian — Fraud Forecast: Agentic AI-Driven Financial Fraud 2026 | [링크](https://www.experianplc.com/newsroom/press-releases/2026/experian-s-new-fraud-forecast-warns-agentic-ai--deepfake-job-can) | 보도자료 | 2026-01-13 | [A] |
| <a id="ref-g-34"></a>G-34 | Pindrop — Pindrop Pulse for Audio Deepfake Detection | [링크](https://www.pindrop.com/product/pindrop-pulse/) | 제품 | 2026 | [B] |
| <a id="ref-g-36"></a>G-36 | INTERPOL — INTERPOL-UNODC global summit ends with call to action against fraud surge | [링크](https://www.interpol.int/en/News-and-Events/News/2026/INTERPOL-UNODC-global-summit-ends-with-call-to-action-against-fraud-surge) | 공식 | 2026-03-17 | [A] |
| <a id="ref-g-37"></a>G-37 | UNODC — UNODC-INTERPOL global summit mobilizes action against fraud surge | [링크](https://www.unodc.org/unodc/en/press/releases/2026/March/unodc-interpol-global-summit-mobilizes-action-against-fraud-surge.html) | 공식 | 2026-03-17 | [A] |
| <a id="ref-g-38"></a>G-38 | Help Net Security — Financial groups lay out a plan to fight AI identity attacks | [링크](https://www.helpnetsecurity.com/2026/04/01/fight-ai-identity-fraud/) | news | 2026-04-01 | [B] |
| <a id="ref-g-39"></a>G-39 | Mobile World Live — KT trials voice phishing detection | [링크](https://www.mobileworldlive.com/asia-pacific/kt-trials-voice-phishing-detection/) | news | 2026 | [B] |
| <a id="ref-g-40"></a>G-40 | PYMNTS — AI Takes On the Spam Call Epidemic | [링크](https://www.pymnts.com/artificial-intelligence-2/2026/ai-takes-on-the-spam-call-epidemic/) | news | 2026 | [B] |
| <a id="ref-g-43"></a>G-43 | CX Today — Deepfake Voice Fraud is Fueling the Voice Trust Collapse | [링크](https://www.cxtoday.com/security-privacy-compliance/the-voice-trust-collapse-and-deepfake-voice-fraud/) | news | 2026 | [C] |
| <a id="ref-g-44"></a>G-44 | Bank Info Security — Adaptive Security Gets $81M Series B for AI Deepfake Defense | [링크](https://www.bankinfosecurity.com/adaptive-security-gets-81m-series-b-for-ai-deepfake-defense-a-30332) | news | 2026 | [B] |
| <a id="ref-p-01"></a>P-01 | Janssen et al. — Benchmarking ML-KEM and ML-DSA on ARM Cortex-M0+ (arXiv:2603.19340) | [링크](https://arxiv.org/abs/2603.19340) | paper | 2026-03-30 | [A] |
| <a id="ref-p-02"></a>P-02 | Park et al. — THED: Threshold Dilithium from FHE (IACR ePrint 2026/638) | [링크](https://eprint.iacr.org/2026/638.pdf) | paper | 2026 | [A] |
| <a id="ref-p-03"></a>P-03 | Singh et al. — Advanced Real-Time Fraud Detection Using RAG-Based LLMs (arXiv:2501.15290) | [링크](https://arxiv.org/abs/2501.15290) | paper | 2025-01-25 | [A] |
| <a id="ref-p-04"></a>P-04 | Bhatti et al. — Human Perception of Synthetic Voices in Vishing (arXiv:2602.20061) [철회] | [링크](https://arxiv.org/abs/2602.20061) | paper | 2026-02-23 | [C] |
| <a id="ref-p-05"></a>P-05 | IEEE 2026 — Efficient Voice Phishing Detection using the Agentic AI Approach | [링크](https://ieeexplore.ieee.org/document/11263515) | paper | 2026 | [A] |
| <a id="ref-e-01"></a>E-01 | Google Quantum AI — ECDLP Cryptocurrency Whitepaper (arXiv:2603.28846) | [링크](https://quantumai.google/static/site-assets/downloads/cryptocurrency-whitepaper.pdf) | IR/발표 | 2026-03-31 | [A] |
| <a id="ref-e-02"></a>E-02 | Cisco Blogs — Why full-stack PQC cannot wait (Han Lee, Cisco Live EMEA) | [링크](https://blogs.cisco.com/networking/why-full-stack-post-quantum-cryptography-cannot-wait) | IR/발표 | 2026-04-01 | [A] |
| <a id="ref-e-03"></a>E-03 | PQShield — Improved Quantum Attacks on Elliptic Curves Analysis | [링크](https://pqshield.com/improved-quantum-attacks-on-elliptic-curves-is-the-pqc-transition-moving-fast-enough/) | IR/발표 | 2026-04-01 | [A] |
| <a id="ref-e-04"></a>E-04 | Canadian Centre for Cyber Security — ITSM.40.001 Roadmap for Migration to PQC | [링크](https://www.cyber.gc.ca/en/guidance/roadmap-migration-post-quantum-cryptography-government-canada-itsm40001) | IR/발표 | 2026-04-01 | [A] |
| <a id="ref-e-05"></a>E-05 | Oratomic — Launch Announcement (공식 보도자료) | [링크](https://www.oratomic.com/news/launch-announcement) | IR/발표 | 2026-03-31 | [A] |
| <a id="ref-e-06"></a>E-06 | Niobium Microsystems — The Fog 공식 보도자료 (Kevin Yoder, CEO) | [링크](http://www.prnewswire.com/news-releases/niobium-introduces-the-fog-a-new-encrypted-cloud-platform-for-private-ai-and-data-processing-302732387.html) | IR/발표 | 2026-04-02 | [A] |
| <a id="ref-e-07"></a>E-07 | CryptoLab — HEaaN Zero-Leak RAG GS 1등급 인증 (유니콘팩토리) | [링크](https://www.unicornfactory.co.kr/article/2026032614461522253) | IR/발표 | 2026-03-26 | [A] |
| <a id="ref-e-08"></a>E-08 | Intel — Heracles FHE ASIC ISSCC 2026 발표 (Privacy Guides) | [링크](https://www.privacyguides.org/news/2026/03/19/intels-fully-homomorphic-encryption-chip-could-revolutionize-privacy/) | IR/발표 | 2026-03-19 | [B] |
| <a id="ref-e-09"></a>E-09 | CryptoLab CEO 정희천 — CKKS+ 온디바이스 경량화 발언 (Asia Business Daily 인용) | [링크](https://www.asiae.co.kr/en/article/2026031008212144575) | IR/발표 | 2026-03-10 | [B] |
