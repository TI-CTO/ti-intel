---
type: weekly-deep-research
topic: pqc-voice-encryption
date: 2026-03-30
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
parent: 2026-03-30_weekly-secure-ai.md
prev_report: outputs/reports/weekly/2026-03-25_research-pqc-voice-encryption.md
---

# Deep 리서치: On-Device PQC (양자내성암호) (2026-W14)

> 기간: 2026-03-23 ~ 2026-03-30
> 이전 대비: W13에서 ZeroTier Quantum 출시(3/23), Kudelski KSE3 반도체 IP 공개, Axelera Europa+KSE3 결합(3/10), FIPS 140-2 D-180·EU Cyber Resilience Act (CRA) D-170·CNSA 2.0 D-281 삼중 데드라인 압박 이후 이번 주 주요 변화 추적

---

## 이전 대비 변화

- **전주 (W13, 2026-03-25)**: ZeroTier Quantum RSAC 출시(3/23), Kudelski KSE3 반도체 IP 공개, Axelera Europa+KSE3 엣지 AI 결합(3/10), Thales 5G SIM OTA PQC 업그레이드 시연, FIPS 140-2/CRA/CNSA 2.0 삼중 데드라인 카운트다운
- **금주 (W14, 2026-03-30)**: Google이 2029 Post-Quantum Cryptography (PQC) 마이그레이션 데드라인 선언(3/25) — NIST 2030보다 1년 앞당김; Android 17에 Module-Lattice-Based Digital Signature Algorithm (ML-DSA) 탑재 및 Keystore Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) 지원 공개(3/26); IBM이 Signal·Threema와 양자안전 메시징 연구 협력 발표(3/10); PQShield가 5KB RAM 임베디드 PQC 라이브러리 출시(3/10); QuSecure가 미국 SEC 제출 문서에서 PQC 실제 적용 사례로 공식 인용(3/19)
- **변화 방향**: 하드웨어 IP 레벨(KSE3)에서 OS 레벨(Android 17)로 PQC 구현이 플랫폼 전반에 확산. Google의 독자적 2029 데드라인 선언은 민간 빅테크가 정부 규제보다 빠른 속도로 양자안전 전환을 추진하는 신호이며, 통신사에게 공급망 전반의 PQC 준비도 점검을 앞당기는 압력으로 작용

---

## 기술 동향

1. **Google 2029 PQC 마이그레이션 데드라인 선언 — NIST 2030보다 1년, NSA 2033보다 4년 앞당김.**
   Google은 2026-03-25 공식 블로그에서 "Quantum Frontiers May Be Closer Than They Appear"를 발표하며 2029년을 자체 PQC 마이그레이션 완료 시점으로 명시했다. Cryptographically Relevant Quantum Computer (CRQC)의 조기 출현 가능성과 "Store-Now-Decrypt-Later (SNDL)" 공격 위협이 근거다. Google의 자체 마감이 업계 레퍼런스 포인트로 작용할 경우 통신사·금융·헬스케어 등 규제 산업의 로드맵 조기화 압력이 생긴다. [[G-01]](#ref-g-01), [[G-02]](#ref-g-02)

2. **Android 17 ML-DSA 탑재 — 모바일 OS 최초 종합 PQC 보안 아키텍처.**
   Google은 2026-03-26 Security Blog를 통해 Android 17의 PQC 통합 세부 내용을 공개했다. 구현 범위는 4개 계층이다: (1) Android Verified Boot(AVB) 라이브러리에 ML-DSA 통합, (2) Android Keystore가 ML-DSA-65·ML-DSA-87을 네이티브 지원 — 표준 `KeyPairGenerator` API로 접근 가능, (3) Remote Attestation 업그레이드, (4) Google Play App Signing에 Classical+PQC 하이브리드 서명 블록 도입. ML-DSA 서명은 약 3,293 바이트로 ECDSA(~64 바이트) 대비 약 51배 크기가 증가하나, 보안 격리 환경에서 처리되어 사용자 경험에 미치는 영향은 미미하다고 Google은 설명했다. [[G-03]](#ref-g-03), [[G-04]](#ref-g-04), [[E-01]](#ref-e-01)

3. **PQShield PQMicroLib-Core — 5KB RAM 임베디드 PQC 구현, Embedded World 2026 발표(3/10).**
   PQShield는 Embedded World 2026(뉘른베르크)에서 PQMicroLib-Core를 공개했다. 5KB RAM 풋프린트로 TLS 지원이 포함된 양자내성 암호화를 메모리 제약 임베디드 디바이스에서 소프트웨어 업그레이드만으로 구현 가능하다. IoT·산업 제어 시스템·보안 통신 단말 등 하드웨어 교체 없이 PQC를 소급 적용해야 하는 레거시 디바이스 시장을 직접 타깃한다. [[G-05]](#ref-g-05), [[G-06]](#ref-g-06)

4. **IBM + Signal + Threema — 양자안전 그룹 메시징 프로토콜 연구 발표(3/10).**
   IBM Research는 Signal, Threema와 협력하여 NIST 표준 ML-DSA·ML-KEM을 프라이빗 그룹 메시징 프로토콜에 통합하는 방법론을 Real-World Crypto 2026에서 발표했다. 기존 Signal 그룹 프로토콜을 그대로 ML-DSA로 교체할 경우 대역폭이 최대 100배 증가하는 문제가 발견됐으며, IBM은 서버 측 암호화 그룹 데이터 저장 + 멤버 검증 분산 방식으로 이를 해결하는 재설계를 제안했다. Signal 측은 구현 검토 의사를 밝혔고, Threema는 ML-KEM 통합 평가 중이다. 보이스 암호화 프로토콜에도 동일한 대역폭 증가 문제가 적용될 수 있어 On-Device PQC 보이스 통신 설계 시 핵심 고려 사항이다. [[G-07]](#ref-g-07), [[G-08]](#ref-g-08)

5. **QuSecure, SEC 제출 문서에서 PQC 실제 적용 사례 공식 인용(3/19) — 금융권 레퍼런스 확립.**
   미국 포스트-퀀텀 금융 인프라 프레임워크(Post-Quantum Financial Infrastructure Framework, PQFIF)가 미국 증권거래위원회(SEC)에 제출됐으며, 문서 내에서 QuSecure가 Banco Sabadell·Accenture와 4개월간 수행한 PQC 배포가 "대형 은행이 기존 시스템을 중단 없이 PQC로 전환 가능함을 증명한 유일한 실사례"로 인용됐다. 또한 QuSecure는 미국 공군 Global Strike Command 핵 폭격기(B-52) 분류 망 보호를 위한 $3.9M AFWERX/TACFI 계약, 미사일 방어청(Missile Defense Agency, MDA) SHIELD 계약($151B 규모)도 수주했다. [[G-09]](#ref-g-09), [[E-02]](#ref-e-02)

6. **CISA PQC 제품 카테고리 리스트 발표(1/23) — 미국 연방 조달 기준 확립.**
   CISA는 2026-01-23 트럼프 행정부 Executive Order 14306에 따라 PQC-capable 제품 카테고리 목록을 발표했다. 즉시 PQC 제품만 구매해야 하는 범주(1군)에 클라우드 서비스, 협업 도구(채팅·메시징), 핵심 웹 소프트웨어(브라우저·서버), 엔드포인트 보안이 포함됐다. 전환 진행 중(2군)에 통신 장비·OS·스토리지·IAM 솔루션이 포함됐다. 이는 보이스 통신을 포함한 협업 플랫폼 공급자에게 PQC 지원이 연방 조달의 기본 요건임을 공식화한 것이다. [[G-10]](#ref-g-10), [[G-11]](#ref-g-11)

7. **Thales 5G SIM Over-the-Air PQC 업그레이드 세계 최초 시연(3/2) — 전주에서 이어지는 핵심 신호.**
   이번 주도 Thales의 3/2 시연이 업계 레퍼런스로 계속 인용되고 있다. 주목할 점은 SKT와 Thales가 국내 5G 독립형(Standalone) 망에서 CRYSTALS-Kyber 암호화를 적용한 SIM을 테스트한 사례가 함께 부각되고 있다는 점이다. Thales의 접근법은 크립토-어질리티(Crypto-agility) 원칙을 실제 통신 네트워크에 구현한 선구적 사례로, 기기 교체 없는 PQC 전환 경로를 제시한다. [[G-12]](#ref-g-12), [[E-03]](#ref-e-03)

8. **격자 기반 암호화 하드웨어 가속기 논문 부상 — 온디바이스 연산 오버헤드 해결 연구 집중.**
   2026년 1월 MDPI Electronics에 발표된 "Lattice-Based Cryptographic Accelerators for the Post-Quantum Era"(Lattice-Based Cryptographic Accelerators et al., 2026) 논문은 Number Theoretic Transform (NTT) 및 다항식 곱셈 등 격자 기반 연산의 온디바이스 오버헤드를 하드웨어 가속으로 해결하는 아키텍처를 다룬다. PQC 알고리즘이 보이스/영상 통화처럼 지연에 민감한 응용에서 약 1.5% 응답 시간 증가를 유발한다는 점에서, 전용 가속 IP의 필요성이 커지고 있다. [[G-13]](#ref-g-13)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| Google | 2026-03-25: 2029 PQC 마이그레이션 데드라인 선언. 2026-03-26: Android 17 ML-DSA 탑재 공식 발표. AVB·Keystore·Remote Attestation·App Signing 4계층 PQC 통합. ML-DSA-65/87 KeyPairGenerator API 지원. Play 앱 서명에 Classical+PQC 하이브리드 서명 블록 도입 | [[G-01]](#ref-g-01), [[E-01]](#ref-e-01) |
| IBM | 2026-03-10: Signal·Threema와 Real-World Crypto 2026에서 양자안전 그룹 메시징 재설계 발표. ML-DSA 직접 적용 시 대역폭 100배 증가 문제 확인 후 서버 분산 검증 방식 제안. Threema는 ML-KEM 통합 평가 중 | [[G-07]](#ref-g-07), [[G-08]](#ref-g-08) |
| PQShield | 2026-03-10 Embedded World 2026: PQMicroLib-Core 공개. 5KB RAM 풋프린트, TLS 지원 포함. 하드웨어 교체 없이 소프트웨어 업그레이드로 임베디드 PQC 구현. 100편 연구 논문 달성 발표 | [[G-05]](#ref-g-05), [[G-06]](#ref-g-06) |
| QuSecure | 2026-03-19: SEC 제출 PQFIF에서 PQC 실제 적용 금융 레퍼런스로 공식 인용. $3.9M AFWERX/TACFI 미공군 B-52 핵폭격기 분류망 보호 계약. MDA SHIELD $151B 계약 수주 | [[G-09]](#ref-g-09), [[E-02]](#ref-e-02) |
| Thales | 2026-03-02(전주 발표, 이번 주 지속 인용): SIM/eSIM OTA PQC 업그레이드 세계 최초 시연. SKT와 5G SA 망에서 CRYSTALS-Kyber SIM 테스트. 크립토-어질리티 기반 디바이스 교체 없는 전환 경로 증명 | [[G-12]](#ref-g-12), [[E-03]](#ref-e-03) |
| ZeroTier | 전주 RSAC 출시(3/23) 이후 이번 주 업계 레퍼런스로 계속 인용. ZTP+Hybrid FIPS PQC, CNSA 2.0 준수. 에어갭 배포 지원. 경쟁사 대비 차별점으로 "소프트웨어 정의 E2E 양자안전 네트워킹" 강조 | [[G-14]](#ref-g-14) |
| Axelera AI + Kudelski Labs | 전주 발표(3/10) 지속: Europa AIPU에 KSE3(ML-KEM+ML-DSA) 통합. 2026-03-18: Multiverse Computing과 엣지 AI 모델 압축 협력 추가. Europa H1 2026 출하 시작 예정 | [[G-15]](#ref-g-15), [[G-16]](#ref-g-16) |
| SKT | QKD-PQC 하이브리드형 장비 출시(2024-10, 세계 최초). NIST FIPS 203/204 준수 자체 개발 PQC 소프트웨어 통합. IDQ Solteris KMS 기반. Thales와 5G SA 망 CRYSTALS-Kyber SIM 테스트 협력 | [[G-17]](#ref-g-17), [[E-03]](#ref-e-03) |

---

## 시장 시그널

**투자 & M&A**

- QuSecure, AFWERX/TACFI $3.9M 계약 및 MDA SHIELD 계약 수주 — 미국 방위·국가안보 분야 PQC 조달 가속화 신호 [[G-09]](#ref-g-09)
- Axelera AI, EU Innovation Council 지원 하에 €200M+ 조달 완료(2/24) — Europa AIPU 생산 본격화 재원 확보 [[G-15]](#ref-g-15)
- Quantum Computing Inc., Luminar Semiconductor 인수(2/26) — PQC+양자 기술 공급망 수직 통합 가속 [[G-18]](#ref-g-18)

**파트너십 & 제휴**

- IBM + Signal + Threema: 양자안전 메시징 프로토콜 공동 연구 — 소비자 메시징 플랫폼의 PQC 전환 로드맵에 직접 영향 [[G-07]](#ref-g-07)
- Multiverse Computing + Axelera AI: 엣지 AI 모델 압축(최대 95%) + PQC 보안 엔클레이브(KSE3) 결합 — 엣지 AI 보안 단말 시장 진입 협력(3/18) [[G-16]](#ref-g-16)
- Quantum Computing Inc. + Ciena: OFC 2026에서 PQC+QKD 결합 고속 암호화 통신 시연(3/11) [[G-18]](#ref-g-18)

**시장 전망**

- 2026년 기업의 14%만이 양자 취약 시스템에 대한 전수 조사를 완료한 상태 [[G-19]](#ref-g-19) [추가확인 필요]
- 기업 마이그레이션 완료 소요 기간: 중소기업 5~7년, 대기업 12~15년+ 추정 — 2026년 시작 기업은 NIST 2030 데드라인 충족이 빠듯한 상황 [[G-19]](#ref-g-19) [추가확인 필요]
- 2026년은 Pure PQC 배포보다 Classical+PQC 하이브리드 접근법 지배 전망 [[G-20]](#ref-g-20)

**도입 사례**

- Google: Chrome에 ML-KEM 기본 활성화, Android 17에 ML-DSA 통합 — 모바일 OS 최초 종합 PQC 스택
- QuSecure + Banco Sabadell + Accenture: 4개월 PQC 마이그레이션 — 금융권 최초 규제 기관 공식 인정 사례
- SKT + Thales: 5G SA 망 CRYSTALS-Kyber SIM 테스트 — 통신사 On-Device PQC 실증 사례

**연구 동향**

- IBM, Signal 그룹 프로토콜의 PQC 전환 시 대역폭 100배 증가 문제 정량화 및 해결책 제시 — 실시간 보이스 암호화 프로토콜 설계 시 직접 참조 가능한 데이터 [[G-07]](#ref-g-07)
- MDPI Electronics: 격자 기반 암호화 하드웨어 가속기 — NTT·다항식 연산 온디바이스 오프로드 아키텍처 [[G-13]](#ref-g-13)

---

## 전략적 시사점

**기회**

- Google Android 17 ML-DSA Keystore API 공개는 통신사·단말 앱 개발자에게 On-Device PQC 서명/인증을 표준 API로 구현할 수 있는 직접 경로를 제공한다. 별도 HSM 없이도 스마트폰 TrustZone에서 PQC 키를 격리 보관 가능
- Thales OTA PQC 업그레이드 기술은 수십억 개의 기존 5G SIM에 디바이스 교체 없이 PQC를 소급 적용할 수 있는 경로를 열었다. 국내 통신사 입장에서 SKT가 이미 Thales와 협력 중임은 선발 우위 확보 지점
- PQShield 5KB RAM 라이브러리는 제약된 IoT·보안 통신 단말에 소프트웨어 업데이트만으로 PQC를 적용하는 저비용 경로. VoIP 단말·스마트폰 보안 앱 등에 즉시 적용 가능한 레디-메이드 솔루션

**위협**

- IBM의 연구가 확인한 PQC 메시징 대역폭 100배 증가 문제는 실시간 보이스 통화 프로토콜에도 동일하게 적용될 수 있다. 기존 VoIP 인프라(SIP/RTP 스택)의 PQC 전환 시 QoS 저하 위험
- Google이 2029 데드라인을 선언함으로써 공급망 전체(단말 제조사, 앱 개발자, 네트워크 장비사)에 PQC 준비 가속 압력이 가해진다. 통신사가 PQC 마이그레이션 로드맵을 2030 기준으로 설정한 경우 고객 및 파트너사로부터 조기화 요구 직면 가능
- 중국 독자 PQC 표준(S-Cloud+ 계열, 2028~2029 확정 예정)이 현실화될 경우 국내 통신사의 China-sourced 장비 및 대중 로밍 서비스에서 듀얼 알고리즘 지원 요건 발생 가능 [추가확인 필요]

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Google Blog — Quantum Frontiers: PQC Migration Timeline 2029 | [링크](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/) | news | 2026-03-25 | [A] |
| <a id="ref-g-02"></a>G-02 | TechSpot — Google Sets 2029 Deadline for Quantum-Safe Encryption | [링크](https://www.techspot.com/news/111856-google-sets-2029-deadline-quantum-safe-encryption-years.html) | news | 2026-03-25 | [B] |
| <a id="ref-g-03"></a>G-03 | Privacy Guides — Android 17 is Getting a Post Quantum Cryptography Upgrade | [링크](https://www.privacyguides.org/news/2026/03/26/android-17-is-getting-a-post-quantum-cryptography-upgrade/) | news | 2026-03-26 | [B] |
| <a id="ref-g-04"></a>G-04 | Android Authority — Android 17 is getting Post-Quantum Cryptography | [링크](https://www.androidauthority.com/android-post-quantum-cryptography-3651834/) | news | 2026-03-26 | [B] |
| <a id="ref-g-05"></a>G-05 | The Quantum Insider — PQShield Releases Lightweight PQC Library for Embedded Systems | [링크](https://thequantuminsider.com/2026/03/10/pqshield-ultra-small-pqc-embedded-security-embedded-world/) | news | 2026-03-10 | [B] |
| <a id="ref-g-06"></a>G-06 | Quantum Computing Report — PQShield Launches Ultra-Compact PQC Implementation | [링크](https://quantumcomputingreport.com/pqshield-launches-ultra-compact-pqc-implementation-for-embedded-systems/) | news | 2026-03-10 | [B] |
| <a id="ref-g-07"></a>G-07 | IBM Research — IBM Works With Signal and Threema on Quantum-Safe Messaging | [링크](https://thequantuminsider.com/2026/03/10/ibm-signal-threema-quantum-safe-research/) | news | 2026-03-10 | [B] |
| <a id="ref-g-08"></a>G-08 | IBM Research Blog — Securing communication from tomorrow's quantum risks | [링크](https://research.ibm.com/blog/signal-threema-quantum-safe) | news | 2026-03-10 | [A] |
| <a id="ref-g-09"></a>G-09 | The Quantum Insider — SEC Submission Highlights QuSecure PQC Deployment | [링크](https://thequantuminsider.com/2026/03/19/sec-submission-highlights-qusecure-deployment-real-world-post-quantum-migration-example/) | news | 2026-03-19 | [B] |
| <a id="ref-g-10"></a>G-10 | CISA — Product Categories for Technologies That Use PQC Standards | [링크](https://www.cisa.gov/resources-tools/resources/product-categories-technologies-use-post-quantum-cryptography-standards) | news | 2026-01-23 | [A] |
| <a id="ref-g-11"></a>G-11 | The Quantum Insider — CISA Issues Federal Buying Guidance for PQC | [링크](https://thequantuminsider.com/2026/01/27/cisa-issues-federal-buying-guidance-for-post-quantum-cryptography/) | news | 2026-01-27 | [B] |
| <a id="ref-g-12"></a>G-12 | The Quantum Insider — Thales Demonstrates Remote Post-Quantum Security Upgrade for 5G SIMs | [링크](https://thequantuminsider.com/2026/03/02/thales-remote-post-quantum-5g-sim-upgrade/) | news | 2026-03-02 | [B] |
| <a id="ref-g-13"></a>G-13 | MDPI Electronics — Lattice-Based Cryptographic Accelerators for the Post-Quantum Era | [링크](https://www.mdpi.com/2079-9292/15/2/475) | paper | 2026-01 | [A] |
| <a id="ref-g-14"></a>G-14 | Security Boulevard — ZeroTier Launches Quantum-Secure Networking Platform at RSAC 2026 | [링크](https://securityboulevard.com/2026/03/zerotier-launches-quantum-secure-networking-platform-at-rsac-2026/) | news | 2026-03-23 | [B] |
| <a id="ref-g-15"></a>G-15 | EE Times — Axelera Raises $250M in Largest EU Semi Funding Round Ever | [링크](https://www.eetimes.com/axelera-raises-250m-in-largest-eu-semi-round-ever/) | news | 2026-02-24 | [B] |
| <a id="ref-g-16"></a>G-16 | The Quantum Insider — Multiverse Computing and Axelera AI Launch Strategic Collaboration | [링크](https://thequantuminsider.com/2026/03/18/ultiverse-computing-axelera-ai-strategic-collaboration-ai-models-edge-devices/) | news | 2026-03-18 | [B] |
| <a id="ref-g-17"></a>G-17 | SK텔레콤 뉴스룸 — SKT, 양자암호 양대 기술 하나로 묶었다 | [링크](https://news.sktelecom.com/207758) | news | 2026-03-15 | [A] |
| <a id="ref-g-18"></a>G-18 | Quantum Computing Inc. — PQC and QKD Demonstration at OFC 2026 | [링크](https://quantumcomputinginc.com/news/press-releases/2026/quantum-computing-inc.-and-ciena-demonstrate-next-generation-quantum-secured-communications-with-high-speed-encryption-using-pqc-and-qkd-at-ofc-2026) | news | 2026-03-11 | [B] |
| <a id="ref-g-19"></a>G-19 | Gray Group Intl — Post-Quantum Cryptography Enterprise Guide 2026 | [링크](https://www.graygroupintl.com/blog/post-quantum-cryptography-enterprise-guide/) | blog | 2026-03 | [C] |
| <a id="ref-g-20"></a>G-20 | Security Boulevard — PQC for Authentication: Enterprise Migration Guide 2026 | [링크](https://securityboulevard.com/2026/03/post-quantum-cryptography-for-authentication-the-enterprise-migration-guide-2026/) | news | 2026-03 | [B] |
| <a id="ref-e-01"></a>E-01 | Google Security Blog — Security for the Quantum Era: Implementing PQC in Android | [링크](https://security.googleblog.com/2026/03/post-quantum-cryptography-in-android.html) | IR/발표 | 2026-03-26 | [A] |
| <a id="ref-e-02"></a>E-02 | QuSecure — SEC Framework Highlights QuSecure Post-Quantum Banking Deployment | [링크](https://www.qusecure.com/post-quantum-cryptography-banking-deployment-sec-framework/) | IR/발표 | 2026-03-19 | [A] |
| <a id="ref-e-03"></a>E-03 | Thales / Nasdaq — Thales sets a world first in quantum-safe security for 5G networks | [링크](https://www.nasdaq.com/press-release/thales-sets-world-first-quantum-safe-security-5g-networks-2026-03-02) | IR/발표 | 2026-03-02 | [A] |
