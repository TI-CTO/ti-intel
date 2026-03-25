---
type: weekly-research
topic: pqc-voice-encryption
date: 2026-03-25
parent: 2026-03-25_weekly-secure-ai
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
prev_report: outputs/reports/weekly/2026-03-18_research-pqc-voice-encryption.md
---

# Deep 리서치: On-Device 양자암호 (PQC Voice Encryption) (2026-W14)

> 기간: 2026-03-18 ~ 2026-03-25
> 이전 대비: W13에서 중국 PQC 독자 표준 3년 내 확정(3/19), 트럼프 사이버 전략 PQC 명시, SEALSQ 블록체인 PQC 배포, CISA PQC 제품 카테고리 리스트, HNDL 위협 경고 강화, FIPS 140-2 종료 D-181 확인 이후 이번 주 주요 변화 추적

---

## 기술 동향

1. **ZeroTier Quantum 출시 — RSAC 2026에서 CNSA 2.0 준수 E2E 양자안전 네트워킹 플랫폼 공개.**
   ZeroTier는 2026-03-23 RSAC 2026에서 ZeroTier Quantum을 발표했다. ZTP(ZeroTier Transport Protocol)라는 새로운 패킷 기반 프로토콜에 Hybrid FIPS-compliant Post-Quantum Cryptography (PQC)를 전송 계층에 직접 내장했으며, NSA의 Commercial National Security Algorithm Suite 2.0 (CNSA 2.0) 기준을 충족한다고 주장했다. 소프트웨어는 메모리 안전 언어인 Rust로 전체 재작성됐으며, SaaS 클라우드·소버린 격리·완전 에어갭(air-gapped) 세 가지 배포 옵션을 지원한다. 방산·정부·의료·금융·산업 IoT 등 규제 산업을 1차 타깃으로 명시했다. 출처: [[G-01]](#ref-g-01), [[G-02]](#ref-g-02)

2. **Kudelski Labs Embedded World 2026 — NIST 표준 PQC + 보안 엔클레이브 반도체 IP, CRA 준수.**
   Kudelski Labs는 Embedded World 2026(2026-03 뉘른베르크)에서 KSE3(Kudelski Secure Enclave 3) 반도체 IP를 공개했다. NIST 표준 ML-KEM(FIPS 203) 및 ML-DSA(FIPS 204) 알고리즘을 하드웨어 엔클레이브에 통합하고, 사이드채널·폴트 공격 보호 기능을 포함했다. 모듈형 구조로 PQC 알고리즘 교체 없이 펌웨어 업데이트만으로 크립토-어질리티(Crypto-agility)를 지원한다. EU Cyber Resilience Act (CRA) Important Products 분류에 맞춰 설계됐으며, SESIP/PSA Level 3(AVA_VAN.3 포함) 인증을 목표로 한다. keySTREAM SaaS로 OTA 업데이트 및 수명주기 관리를 제공한다. 출처: [[G-03]](#ref-g-03), [[G-04]](#ref-g-04)

3. **Axelera AI + Kudelski Labs — Europa Edge AI 칩에 KSE3 PQC-ready 보안 엔클레이브 통합(3/10).**
   Axelera AI는 2026-03-10 Europa AI Processing Unit(AIPU)에 Kudelski Labs의 KSE3를 통합했다. On-Device AI 추론 워크로드에 양자내성 암호화, 보안 부팅, 키 관리, 불변 신원(Immutable Identity)을 동시에 제공하는 최초의 엣지 AI 칩 사례다. 스마트 인프라·산업 자동화·자율 로봇 분야 타깃이며, CRA Important Products 준수를 공시했다. 출처: [[G-05]](#ref-g-05), [[G-06]](#ref-g-06)

4. **Thales 5G SIM 원격 PQC 업그레이드 세계 최초 시연(3/2) — 크립토-어질리티 개념 실용화.**
   Thales는 2026-03-02 SIM 및 eSIM 카드에 PQC 알고리즘을 원격(Over-the-Air)으로 다운로드해 양자안전 보안으로 즉시 전환하는 기술을 세계 최초로 시연했다. 주요 이동통신사와 협력해 수행됐으며, 기존 디바이스 교체 없이 보안 업그레이드가 가능함을 입증했다. On-Device PQC 관점에서 수십억 개의 기존 디바이스에 PQC를 소급 적용할 수 있는 경로를 열었다는 점에서 의미가 크다. 출처: [[G-07]](#ref-g-07), [[E-01]](#ref-e-01)

5. **SEALSQ 블록체인 PQC 배포 — CRYSTALS-Kyber + Dilithium 보안 하드웨어 통합(3/20).**
   SEALSQ(NASDAQ: LAES)는 2026-03-20 블록체인·디지털 트랜잭션 인프라 보안을 위한 PQC 기술 배포를 발표했다. CRYSTALS-Kyber(ML-KEM, 키 캡슐화) 및 CRYSTALS-Dilithium(ML-DSA, 디지털 서명)을 자사 보안 요소 및 TPM-class 칩에 직접 내장하여, 블록체인 프라이빗 키를 하드웨어 신뢰 루트(Root of Trust)에 앵커링한다. 스위스 블록체인 금융 플랫폼 WeCan과 협력해 실 서비스에 적용 중이며, 보안 멀티파티 연산(MPC)·영지식 증명(ZKP) 프레임워크를 결합했다. 출처: [[G-08]](#ref-g-08), [[E-02]](#ref-e-02)

6. **FIPS 140-2 종료 D-180(2026-09-21) — FIPS 140-3 전환 병목 구조적 심화.**
   2026-09-21은 NIST CMVP가 잔존 FIPS 140-2 인증 모듈 전체를 Historical 목록으로 이전하는 날이다. 이후 신규 연방 조달에는 FIPS 140-3 검증 모듈만 허용된다. 문제는 FIPS 140-3 검증에 평균 542일이 소요되어(FIPS 140-2 대비 42% 증가), PQC 알고리즘(ML-KEM/ML-DSA)을 포함한 완전한 FIPS 140-3 인증 모듈이 2027년 이전에 광범위하게 공급되기 어렵다는 점이다. 이 구조적 공백은 2026~2027년 조달 불일치(Acquisition Gap)를 만들어낸다. 출처: [[G-09]](#ref-g-09), [[G-10]](#ref-g-10)

7. **EU CRA 보고 의무 2026-09-11 시행 — IoT/임베디드 디바이스 제조사 직접 영향.**
   EU CRA(Cyber Resilience Act) 보고 의무가 2026-09-11부터 시행된다. 이 날부터 EU 시장에 디지털 요소가 포함된 제품을 출시하는 모든 제조사는 적극적으로 악용되는 취약점이나 심각한 보안 사고를 ENISA 및 지정 국가 CSIRT에 24시간 내 조기 경보, 72시간 내 완전 통보해야 한다. On-Device PQC를 탑재한 스마트폰·보안 통신 디바이스 제조사에게 CRA Important Products 분류 여부가 조달 결정 요인으로 부상하고 있다. 출처: [[G-11]](#ref-g-11), [[G-12]](#ref-g-12)

8. **CNSA 2.0 마감 2027-01-01 — NSS 신규 조달 양자안전 알고리즘 의무화 100일 전.**
   NSA의 CNSA 2.0 기준에 따라 2027-01-01부터 모든 신규 국가안보시스템(NSS) 장비 조달 시 CNSA 2.0 알고리즘(ML-KEM, ML-DSA, AES-256, SHA-384 등)이 기본 요건이 된다. ZeroTier Quantum이 CNSA 2.0 준수를 전면에 내세운 이유이며, Kudelski KSE3 역시 국방·정부 조달을 겨냥하고 있다. 실질적으로 2026년이 방산·정부 고객군의 PQC 솔루션 결정 시점이다. 출처: [[G-13]](#ref-g-13)

9. **중국 PQC 독자 표준 3년 내 확정 선언(3/19) — 글로벌 표준 분절화 현실화.**
   중국 전문가들이 2026-03-19 향후 3년 내(2028~2029년) 국가 PQC 표준을 확정하겠다고 선언했다. 중국은 NIST 중심의 국제 표준(격자 기반 알고리즘 ML-KEM)과 달리, "구조 없는 격자(Structureless Lattice)" 계열 알고리즘인 S-Cloud+를 우선시하는 독자 노선을 택했다. 국내 통신사의 China-sourced 장비 및 대중 수출 제품에 듀얼 PQC 표준 지원이 중장기 요건으로 부상할 가능성이 있다. 출처: [[G-14]](#ref-g-14), [[G-15]](#ref-g-15)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| ZeroTier | RSAC 2026(2026-03-23): ZeroTier Quantum 출시. ZTP 프로토콜에 Hybrid FIPS PQC 내장, CNSA 2.0 준수. Rust 재작성, 에어갭 배포 지원. 방산·정부·의료·금융 타깃 | [[G-01]](#ref-g-01), [[G-02]](#ref-g-02) |
| Kudelski Labs | Embedded World 2026: KSE3 반도체 IP 공개. ML-KEM + ML-DSA 하드웨어 엔클레이브, 크립토-어질리티 설계, CRA Important Products 준수, keySTREAM OTA 관리 | [[G-03]](#ref-g-03), [[G-04]](#ref-g-04) |
| Axelera AI | 2026-03-10: Europa AIPU에 KSE3 통합. 최초 On-Device AI + PQC-ready 보안 엔클레이브 결합 엣지 칩. CRA 준수, SESIP/PSA Level 3 목표 | [[G-05]](#ref-g-05), [[G-06]](#ref-g-06) |
| Thales | 2026-03-02: SIM/eSIM OTA PQC 업그레이드 세계 최초 시연. 디바이스 교체 없이 크립토-어질리티 구현. 이동통신사 협력 완료 | [[G-07]](#ref-g-07), [[E-01]](#ref-e-01) |
| SEALSQ | 2026-03-20: ML-KEM + ML-DSA를 TPM-class 칩에 통합해 블록체인 배포. WeCan 스위스 금융 플랫폼 실 서비스 적용 중 | [[G-08]](#ref-g-08), [[E-02]](#ref-e-02) |
| LG유플러스 | MWC 2026(2026-02): ixi-Guardian 2.0 공개. 광전송 장비에 NIST + KpqC 알고리즘 통합 인터페이스 탑재. GSMA 글로모 2026 모바일 기술 보안·사기방지 부문 수상 | [[G-16]](#ref-g-16), [[G-17]](#ref-g-17) |
| CISA | 2026-01-23: PQC 제품 카테고리 초기 리스트 발표(EO 14306 이행). 클라우드·웹·네트워킹 장비·엔드포인트 보안 등 FIPS 203/204/205 요건 명시 | [[G-18]](#ref-g-18), [[G-19]](#ref-g-19) |
| Linphone | 오픈소스 VoIP 최초로 CRYSTALS-KYBER를 ZRTP 프로토콜에 통합(KEM 방식). 음성·영상 통화 PQC 암호화 구현 세계 최초 사례 | [[G-20]](#ref-g-20) |

---

## 시장 시그널

**규제 & 정책**
- CISA, EO 14306(트럼프 사이버 전략) 이행으로 PQC 제품 카테고리 리스트 발표(2026-01-23). FIPS 203/204/205 준수 제품만 연방 조달 허용 기준 설정 — [[G-18]](#ref-g-18)
- EU CRA 2026-09-11 보고 의무 시행: 24시간 내 취약점 보고 의무가 On-Device PQC 솔루션 제조사의 인증 전략을 바꾸고 있다 — [[G-11]](#ref-g-11)
- 미국 CNSA 2.0 신규 NSS 조달 의무화 D-280(2027-01-01). 연방 수요 창출로 ZeroTier Quantum 등 CNSA 2.0 준수 솔루션 수요 선행 증가 — [[G-13]](#ref-g-13)

**파트너십 & 제휴**
- Axelera AI + Kudelski Labs(2026-03-10): 엣지 AI 칩과 PQC 반도체 IP의 결합. 향후 PQC On-Device 추론 보안 레퍼런스 아키텍처로 확산 가능성 — [[G-05]](#ref-g-05)
- Ciena + QCi OFC 2026 시연(2026-03-12): 광통신 인프라에 PQC+QKD 통합, 1.6 Tb/s 규모 실용화 단계. 통신사 백본에서 엔드포인트까지 PQC 체인 완성 경로 — [[G-21]](#ref-g-21)

**시장 전망**
- PQC 글로벌 시장: MarketsandMarkets 추정 2025년 4.2억 달러 → 2030년 28.4억 달러(CAGR 46.2%), Grand View Research 추정 2024년 11.5억 달러 → 2030년 78.2억 달러(CAGR 37.6%). 두 기관 간 큰 편차, 추정치로 취급 요 — [[G-22]](#ref-g-22), [[G-23]](#ref-g-23)
- FIPS 140-3 검증 시간 평균 542일(FIPS 140-2 대비 +42%)로, PQC 포함 완전 인증 모듈이 2027년 이전 광범위 공급 어렵다. 공급 병목이 규제 준수 시장 진입 장벽으로 작용 — [[G-09]](#ref-g-09)
- 하이브리드 방식(고전+PQC) 2026년 표준 전환 경로로 확립됨. 순수 PQC 단독 배포는 여전히 희소 — [[G-24]](#ref-g-24)

**도입 사례**
- SEALSQ + WeCan: ML-KEM/ML-DSA를 TPM-class 칩에 통합해 스위스 블록체인 금융 거래 실 서비스 보호. PQC 하드웨어 + 금융 서비스 결합 최초 상용 사례 중 하나 — [[E-02]](#ref-e-02)
- LG유플러스 ixi-Guardian 2.0: NIST + KpqC 이중 알고리즘을 광전송 장비에 통합, 알고리즘 교체 시 서비스 무중단 보장. 국내 통신사 PQC 광전송 첫 상용화 — [[G-16]](#ref-g-16)
- SoftBank: 4G/5G 라이브 트래픽에 하이브리드 PQC 암호화 파일럿 완료. 고전 타원곡선+격자 기반 알고리즘 결합으로 레이턴시 추가 최소화 확인 — [[G-25]](#ref-g-25)

**연구 동향**
- Harvest-Now, Decrypt-Later: A Temporal Cybersecurity Risk in the Quantum Transition (MDPI, 2026) — 통신 인프라의 HNDL(Harvest Now, Decrypt Later) 위협을 시계열 리스크로 분석. 고보존 분야(위성·의료)의 노출 기간이 수십 년임을 실증. 하이브리드·포워드 시크리시(Forward Secrecy) 적용 시 리스크 지평 2/3 단축 — [[P-01]](#ref-p-01)
- Decoherence and quantum threats in voice biometric authentication with PQC countermeasures (Springer QIP, 2025) — 음성 생체인증 시스템에 대한 양자 위협과 PQC 대응책 분석. 음성 보안 도메인에서 드문 PQC 특화 연구 — [[P-02]](#ref-p-02)
- Post-Quantum Cryptography in the 5G Core (arXiv:2512.20243, 2025) — 하이브리드 X25519+Kyber768 적용 시 +2.3KB, 레이턴시 중위값 10~20ms 추가. 음성 QoS에 실질적 영향 없음 확인 — [[P-03]](#ref-p-03)

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | The Quantum Insider — ZeroTier Launches ZeroTier Quantum | [링크](https://thequantuminsider.com/2026/03/24/zerotier-launches-zerotier-quantum-a-secure-networking-platform/) | news | 2026-03-24 | [B] |
| <a id="ref-g-02"></a>G-02 | Morningstar/BusinessWire — RSAC 2026: ZeroTier Launches ZeroTier Quantum | [링크](https://www.morningstar.com/news/business-wire/20260322114599/rsac-2026-zerotier-launches-zerotier-quantum-the-worlds-first-end-to-end-quantum-secure-networking-platform) | 보도자료 | 2026-03-22 | [A] |
| <a id="ref-g-03"></a>G-03 | design-reuse.com — Kudelski Labs at Embedded World 2026 | [링크](https://www.design-reuse.com/news/202530178-kudelski-labs-addresses-device-lifecycle-security-edge-ai-post-quantum-cryptography-and-regulatory-compliance-at-embedded-world-2026/) | news | 2026-03 | [B] |
| <a id="ref-g-04"></a>G-04 | Kudelski Labs — KSE Embedded Security IP | [링크](https://www.kudelskilabs.com/embedded-security-solutions/security-ip) | official | 2026 | [A] |
| <a id="ref-g-05"></a>G-05 | EE Journal — Axelera AI Adds Kudelski Labs Security IP to Europa Chip | [링크](https://www.eejournal.com/industry_news/axelera-ai-adds-kudelski-labs-security-ip-to-europa-chip-to-enable-secure-high-performance-edge-ai/) | news | 2026-03-10 | [B] |
| <a id="ref-g-06"></a>G-06 | New Electronics — Axelera AI integrates Kudelski Secure Enclave into Europa | [링크](https://www.newelectronics.co.uk/content/news/axelera-ai-integrates-kudelski-secure-enclave-into-europa-edge-ai-chip) | news | 2026-03-10 | [B] |
| <a id="ref-g-07"></a>G-07 | The Quantum Insider — Thales Demonstrates Remote Post-Quantum Security Upgrade for 5G SIMs | [링크](https://thequantuminsider.com/2026/03/02/thales-remote-post-quantum-5g-sim-upgrade/) | news | 2026-03-02 | [B] |
| <a id="ref-g-08"></a>G-08 | GlobeNewswire — SEALSQ Deploys PQC to Secure Blockchain | [링크](https://www.globenewswire.com/news-release/2026/03/20/3259796/0/en/SEALSQ-Deploys-Post-Quantum-Cryptography-to-Secure-Blockchain-and-Digital-Transaction-Infrastructures-Through-the-Deployment-of-Post-Quantum-Cryptographic-PQC-Technologies.html) | 보도자료 | 2026-03-20 | [A] |
| <a id="ref-g-09"></a>G-09 | SafeLogic — What Happens on September 21, 2026? | [링크](https://www.safelogic.com/blog/what-happens-on-september-21-2026) | blog | 2026 | [B] |
| <a id="ref-g-10"></a>G-10 | postquantum.com — The Complete US PQC Regulatory Framework in 2026 | [링크](https://postquantum.com/quantum-policies/us-pqc-regulatory-framework-2026/) | news | 2026 | [B] |
| <a id="ref-g-11"></a>G-11 | EU Digital Strategy — CRA Reporting Obligations | [링크](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting) | official | 2026 | [A] |
| <a id="ref-g-12"></a>G-12 | ComplianceHub.Wiki — EU CRA June and September 2026 Reporting Deadlines | [링크](https://compliancehub.wiki/eu-cyber-resilience-act-june-and-september-2026-reporting-deadlines-loom-for-manufacturers-of-products-with-digital-elements/) | news | 2026 | [B] |
| <a id="ref-g-13"></a>G-13 | SafeLogic — CNSA 2.0 Compliance Requirements & Timelines | [링크](https://www.safelogic.com/compliance/cnsa-2) | blog | 2026 | [B] |
| <a id="ref-g-14"></a>G-14 | The Quantum Insider — China Expects PQC Standards Within Three Years | [링크](https://thequantuminsider.com/2026/03/19/china-expects-post-quantum-cryptography-standards-within-three-years/) | news | 2026-03-19 | [B] |
| <a id="ref-g-15"></a>G-15 | Quantum Zeitgeist — China Forecasts National PQC Standards Within Three Years | [링크](https://quantumzeitgeist.com/post-quantum-cryptography-china-forecasts/) | news | 2026-03-19 | [B] |
| <a id="ref-g-16"></a>G-16 | EBN — LG유플러스 ixi-Guardian 2.0 공개 (MWC 2026) | [링크](https://www.ebn.co.kr/news/articleView.html?idxno=1701212) | news | 2026-02 | [B] |
| <a id="ref-g-17"></a>G-17 | 전자신문 — SKT·LGU+ 글로모 2026 수상 | [링크](https://www.etnews.com/20260305000196) | news | 2026-03-05 | [B] |
| <a id="ref-g-18"></a>G-18 | CISA — Product Categories for Technologies That Use PQC Standards | [링크](https://www.cisa.gov/resources-tools/resources/product-categories-technologies-use-post-quantum-cryptography-standards) | official | 2026-01-23 | [A] |
| <a id="ref-g-19"></a>G-19 | Infosecurity Magazine — CISA Releases List of PQC Product Categories | [링크](https://www.infosecurity-magazine.com/news/cisa-post-quantum-cryptography/) | news | 2026-01 | [B] |
| <a id="ref-g-20"></a>G-20 | Linphone — Voice and video communication over IP secured with post-quantum encryption | [링크](https://www.linphone.org/en/resources/secure-voice-video-ip-post-quantum-encryption/) | official | 2025 | [A] |
| <a id="ref-g-21"></a>G-21 | PR Newswire / Ciena — QCi and Ciena Demonstrate Quantum-Secured Communications at OFC 2026 | [링크](https://www.prnewswire.com/news-releases/quantum-computing-inc-and-ciena-demonstrate-next-generation-quantum-secured-communications-with-high-speed-encryption-using-pqc-and-qkd-at-ofc-2026-302710416.html) | 보도자료 | 2026-03-12 | [A] |
| <a id="ref-g-22"></a>G-22 | MarketsandMarkets — Post-Quantum Cryptography Market (USD 0.42B → USD 2.84B by 2030, CAGR 46.2%) [추정] | [링크](https://www.marketsandmarkets.com/PressReleases/post-quantum-cryptography.asp) | report | 2025 | [C] |
| <a id="ref-g-23"></a>G-23 | Grand View Research — Post-Quantum Cryptography Market (USD 1.15B in 2024 → USD 7.82B by 2030, CAGR 37.6%) [추정] | [링크](https://www.grandviewresearch.com/industry-analysis/post-quantum-cryptography-market-report) | report | 2025 | [C] |
| <a id="ref-g-24"></a>G-24 | Security Boulevard — Post-Quantum Cryptography for Authentication: Enterprise Migration Guide 2026 | [링크](https://securityboulevard.com/2026/03/post-quantum-cryptography-for-authentication-the-enterprise-migration-guide-2026/) | news | 2026-03 | [B] |
| <a id="ref-g-25"></a>G-25 | postquantum.com — Telecom's Quantum-Safe Imperative: Challenges in Adopting PQC | [링크](https://postquantum.com/post-quantum/telecom-pqc-challenges/) | news | 2026 | [B] |
| <a id="ref-e-01"></a>E-01 | BusinessWire / Thales — Thales sets a world first in quantum-safe security for 5G networks | [링크](https://www.businesswire.com/news/home/20260301594505/en/Thales-sets-a-world-first-in-quantum-safe-security-5G-networks) | 보도자료 | 2026-03-02 | [A] |
| <a id="ref-e-02"></a>E-02 | SEALSQ / GlobeNewswire — SEALSQ Deploys PQC Technologies for Blockchain | [링크](https://www.sealsq.com/investors/news-releases/sealsq-deploys-post-quantum-cryptography-to-secure-blockchain-and-digital-transaction-infrastructures-through-the-deployment-of-post-quan-1774014626476) | 보도자료 | 2026-03-20 | [A] |
| <a id="ref-p-01"></a>P-01 | Ehlen et al. — Harvest-Now, Decrypt-Later: A Temporal Cybersecurity Risk in the Quantum Transition (MDPI, 2026) | [링크](https://www.mdpi.com/2673-4001/6/4/100) | paper | 2026 | [A] |
| <a id="ref-p-02"></a>P-02 | Springer QIP — Decoherence and quantum threats in voice biometric authentication with PQC countermeasures | [링크](https://link.springer.com/article/10.1007/s11128-025-04980-7) | paper | 2025 | [A] |
| <a id="ref-p-03"></a>P-03 | arXiv:2512.20243 — Post-Quantum Cryptography in the 5G Core | [링크](https://arxiv.org/html/2512.20243v1) | paper | 2025-12 | [A] |
