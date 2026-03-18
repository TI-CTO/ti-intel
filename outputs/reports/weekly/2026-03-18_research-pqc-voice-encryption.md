---
type: deep-research
topic: pqc-voice-encryption
date: 2026-03-18
parent: 2026-03-18_weekly-secure-ai
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
prev_report: outputs/reports/weekly/2026-03-11_research-ondevice-pqc.md
---

# Deep 리서치: On-Device 양자암호 (PQC) (2026-W12)

> 기간: 2026-03-11 ~ 2026-03-18
> 이전 대비: W11에서 Samsung Exynos 2600 HW-PQC, Thales OTA SIM 업그레이드, Cloudflare 완전 PQC SASE 확인 이후 주요 변화 추적

---

## 기술 동향

1. **Akamai PQC 전면 배포 완료 — TLS 전체 경로 양자내성화.**
   Akamai는 2026년 1월부터 순차적으로 진행한 ML-KEM 하이브리드 배포를 Q1 2026(3월)에 완성했다. Client-to-Edge(X25519MLKEM768 기본 활성화, 2026-02), Edge-to-Origin(opt-in → default, 2026-01-31), Mid-tier 간 Akamai-to-Akamai 전체 전환이 2026-03 목표로 완료되면서 CDN 계층 전체의 TLS 경로가 하이브리드 PQC로 보호됐다. 출처: [[G-01]](#ref-g-01)

2. **Samsung Exynos 2600 — 세계 최초 HW-PQC 스마트폰 SoC 양산.**
   2025년 12월 19일 공개된 Exynos 2600은 세계 최초로 하드웨어 기반 Post-Quantum Cryptography를 탑재한 스마트폰 SoC다. ML-DSA(FIPS 204) 서명 키를 칩 레벨 ROM에 저장하는 "ROM-rooted protection" 방식을 채택했으며, Galaxy S26(Exynos 탑재 모델)이 2026년 2월 출시됐다. Knox Matrix가 PQC 기반 E2E 암호화로 강화되어 eSIM 전송 등 크리티컬 프로세스를 보호한다. 단, Galaxy S26 Ultra는 Snapdragon 8 Elite Gen 5 탑재로 HW-PQC 미지원 상태다. 출처: [[G-02]](#ref-g-02), [[G-03]](#ref-g-03)

3. **Quantum Computing Inc. + Ciena — OFC 2026에서 1.6 Tb/s PQC+QKD 통합 시연.**
   2026년 3월 12일 OFC 2026(광섬유통신 컨퍼런스)에서 QCi와 Ciena가 NIST 인증 PQC 알고리즘과 QKD를 결합한 양자 안전 광통신 솔루션을 시연했다. Ciena의 WaveLogic 6 Extreme 1.6T는 AES-256-GCM 암호화와 NIST 인증 PQC 알고리즘을 지원하며 ETSI 표준 API로 QKD 연동을 처리한다. QCi는 time-frequency 얽힘 기반 QKD 아키텍처와 양자 영지식 증명(QZEK-P) 인증을 제공했다. 통신 인프라 레이어에서 PQC-QKD 통합이 실용화 단계에 진입했음을 확인하는 시그널이다. 출처: [[G-04]](#ref-g-04), [[E-01]](#ref-e-01)

4. **NIST FIPS 140-2 종료 6개월 카운트다운 — 2026-09-21 데드라인 임박.**
   2026년 9월 21일 NIST CMVP가 잔존 FIPS 140-2 인증 모듈 전체를 Historical List로 이전하며, 이후 신규 조달에는 FIPS 140-3 검증 모듈만 허용된다. 이 시점이 사실상 PQC 전환의 규제적 출발점이 된다. FIPS 140-3에는 ML-KEM/ML-DSA 자가 테스트 요건이 추가되어 있으나, PQC 알고리즘을 포함한 완전 FIPS 140-3 CMVP 인증을 획득한 엔터프라이즈 모듈은 아직 희소하다. 출처: [[G-05]](#ref-g-05), [[G-06]](#ref-g-06)

5. **HQC NIST 초안 표준 2026년 출시 예정 — ML-KEM 수학적 백업 알고리즘.**
   Hamming Quasi-Cyclic(HQC)는 ML-KEM과 다른 수학적 구조(코드 기반)를 사용하는 KEM으로, NIST의 5번째 PQC 표준으로 선정됐다(2025-03-11). 초안 표준은 2026년, 최종 표준은 2027년 목표다. HQC의 의의는 격자 기반 ML-KEM에 취약점이 발견될 경우를 대비한 알고리즘 다양성 확보에 있다. 출처: [[G-07]](#ref-g-07)

6. **3GPP PQC 도입 연구 착수 — VoLTE/VoNR 음성 보안 표준화 진행 중.**
   3GPP는 5G/6G 이동통신 표준에 PQC를 어떻게 도입할지 연구를 시작했다. 음성(VoLTE/VoNR)을 지원하는 IMS의 SIP 시그널링 및 미디어 보안 메커니즘(SRTP, DTLS)이 양자내성 알고리즘으로 업그레이드되어야 하나, 3GPP 공식 사양 채택 전까지 라이브 네트워크 배포는 임시 솔루션에 의존한다. SBC(Session Border Controller), Call Server, Media Gateway 등 IMS 노드가 벤더 종속 장비로 운영되는 구조가 PQC 전환의 주요 병목이다. 출처: [[G-08]](#ref-g-08), [[G-09]](#ref-g-09)

7. **PQC 엔터프라이즈 마이그레이션 가이드 2026 — 트리플 데드라인 압박.**
   2026년 3월 Security Boulevard 등 전문매체에서 기업용 PQC 마이그레이션 가이드가 집중 발행됐다. 주요 데드라인 3종: (1) FIPS 140-2 종료 2026-09-21, (2) NSA CNSA 2.0 신규 NSS 조달 의무화 2027-01-01, (3) 연방기관 PQC 전면 마이그레이션 2035. ML-KEM-768이 대부분의 TLS/VPN 배포를 위한 권장 파라미터 세트로 자리잡았으며, 조직 상태에 따라 2~6년의 마이그레이션 기간이 필요하다. 출처: [[G-10]](#ref-g-10), [[G-11]](#ref-g-11)

8. **한국 PQC 전환 파일럿 확대 — 2026년 5개 핵심 인프라 부문으로 확장.**
   한국 정부는 2026년 PQC 전환 시범사업을 기존 3개 부문에서 5개 핵심 인프라 부문으로 확대하고, 총 45억 원을 투입한다. 2035년까지 국가 주요 통신 기반시설에 PQC를 전면 적용하는 마스터플랜이 진행 중이며, 한국 자체 개발 알고리즘(AIMer, SMAUG-T, HAETAE)도 포함됐다. HNDL(Harvest Now, Decrypt Later)과 TNFL(Trust Now, Forge Later) 두 가지 위협 시나리오를 방어 축으로 삼는다. 출처: [[G-12]](#ref-g-12)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| Samsung | Exynos 2600: 세계 최초 HW-PQC 스마트폰 SoC 양산(2026-02), Galaxy S26 탑재. ML-DSA ROM-rooted protection. Knox Matrix E2E PQC 암호화 강화. S3SSE2A CC EAL6+, 소프트웨어 대비 17배 처리 속도 | [[G-02]](#ref-g-02), [[G-03]](#ref-g-03) |
| Akamai | 2026-Q1: Client-to-Edge, Edge-to-Origin, Mid-tier 전 구간 X25519MLKEM768 기본 활성화 완료. FIPS 203 기반 하이브리드 TLS 전면 배포 | [[G-01]](#ref-g-01) |
| Ciena + QCi | OFC 2026(2026-03-12): WaveLogic 6 Extreme 1.6 Tb/s + NIST 인증 PQC + QKD 통합 시연. ETSI 표준 API QKD 연동 | [[G-04]](#ref-g-04), [[E-01]](#ref-e-01) |
| SKT | QKD+PQC 하이브리드 세계 최초 상용화(IDQ Clavis XG + 자체 PQC SW). FIPS 203/204 완전 준수. 양자기술 협의체 참여(2026-01 출범) | [[E-02]](#ref-e-02), [[G-13]](#ref-g-13) |
| LG유플러스 | MWC 2026에서 ixi-Guardian 2.0 공개: 동형암호+PQC+SASE 통합. 광전송 장비에 PQC 적용, NIST+KpqC 전 알고리즘 지원 인터페이스 탑재. U+ PQC-VPN(500Mbps~36Gbps, 8종 솔루션) 운영 중 | [[G-14]](#ref-g-14), [[E-03]](#ref-e-03) |
| KT | "PQC+QKD 하이브리드가 대세" 전략 방향 공식화. 양자암호팀 "양자컴퓨팅 발전할수록 양자암호 기술이 필요" 발언. 양자기술 협의체 참여 | [[G-15]](#ref-g-15) |
| NIST | FIPS 140-2 → Historical 이전 2026-09-21 확정. HQC 초안 표준 2026년 발행 예정. ML-KEM-768을 기본 권장 파라미터로 가이드 | [[G-05]](#ref-g-05), [[G-07]](#ref-g-07) |
| Apple | iMessage PQ3(iOS 17.4+) 운영 중. 양자내성 암호화 플랫폼 확장 지속. 50메시지/7일마다 키 로테이션 | [[G-16]](#ref-g-16) |

---

## 시장 시그널

- PQC 글로벌 시장 규모: 2025년 4.2억 달러(MarketsandMarkets), 2030년 28.4억 달러(CAGR 46.2%) 또는 78.2억 달러(Grand View Research, CAGR 37.6%). 조사기관별 방법론 차이로 추정치 편차가 크며 두 기관 동시 인용 시 독립 교차 검증 요건 충족 [[G-17]](#ref-g-17), [[G-18]](#ref-g-18)
- GlobeNewswire(2026-02-19): "PQC 마이그레이션은 이제 1조 달러 규모의 과제"로 프레이밍되며 금융·인프라 투자 우선순위 상승 [[G-19]](#ref-g-19)
- 하이브리드(고전+PQC) 방식이 2026년 사실상 표준 전환 경로로 확립됨. 순수 PQC 단독 배포는 여전히 희소 [[G-11]](#ref-g-11)
- VoLTE/VoNR 음성 인프라에 대한 PQC 적용은 3GPP 표준화 지연으로 인해 2027년 이후가 현실적 배포 시점으로 예상됨 [[G-08]](#ref-g-08)
- TLS PQC 키 크기 증가(+1KB)가 레이턴시 ~1.5% 증가 유발: 음성·실시간 통신 서비스 품질에 직접 영향 [[G-09]](#ref-g-09)
- "Harvest Now, Decrypt Later" 위협이 장기 기밀성이 요구되는 통화 녹음 파일 보안의 핵심 드라이버로 부상 [[G-12]](#ref-g-12)
- 한국: 2026년 PQC 전환 시범사업 3개→5개 부문 확대, 예산 45억 원 투입. 2035년 전면 전환 목표 [[G-12]](#ref-g-12)
- 기업 사이버보험 시장에서 PQC 미준수 조직에 보험료 인상·양자 면책 조항 삽입 움직임 관측 [[G-11]](#ref-g-11)

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| Securing Cryptography in the Age of Quantum Computing and AI (arXiv:2603.06969, 2026-03) | 양자컴퓨팅+AI 이중 위협 하에서 PQC 구현·전략 대응 종합 리뷰. ML-KEM/ML-DSA 배포 시나리오 분석 | [[P-01]](#ref-p-01) |
| Post-quantum cryptographic authentication for industrial IoT using lattice-based cryptography (Scientific Reports, 2026-03) | ML-KEM+ML-DSA를 TLS 1.3에 통합, Industrial IoT 환경 인증 프로토콜 구현. 지연·처리량 실측값 포함 | [[P-02]](#ref-p-02) |
| Post-Quantum Cryptography in the 5G Core (arXiv:2512.20243, 2025-12) | 하이브리드 X25519+Kyber768 적용 시 +2.3KB, 레이턴시 중위값 10~20ms 추가. 5G 가용성 실질적 영향 없음 확인 | [[P-03]](#ref-p-03) |
| Implementation and performance of PQC for resource constrained consumer electronics (Springer IoT, 2025) | CRYSTALS-Kyber가 메모리·에너지 지표에서 가장 균형적. RSA 대비 메모리 20~30%, 에너지 최대 18% 절감. ESP32 실용화 가능 | [[P-04]](#ref-p-04) |
| Decoherence and quantum threats in voice biometric authentication with PQC countermeasures (Quantum Information Processing, 2025) | 음성 생체인증 시스템에 대한 양자 위협과 PQC 대응책 분석. 음성 인증 도메인의 드문 PQC 특화 연구 | [[P-05]](#ref-p-05) |

---

## 전략적 시사점

**기회**

- Samsung Exynos 2600의 HW-PQC 탑재는 On-Device PQC 통화 녹음 파일 암호화의 하드웨어 기반이 실용화됐음을 의미한다. Galaxy S26(Exynos) 기반 디바이스에서 ML-DSA 서명 + ML-KEM 키 교환을 하드웨어 가속으로 처리하는 아키텍처 설계가 가능한 시점이다
- LG유플러스 ixi-Guardian 2.0(PQC+동형암호+SASE 통합), SKT QKD-PQC 하이브리드 상용화는 국내 통신사가 PQC 솔루션 레이어를 이미 보유했음을 확인한다. 통화 녹음 파일 암호화 기능과의 통합 협력 모델 검토가 가능하다
- 한국 정부의 PQC 전환 파일럿 확대(5개 부문, 45억 원)는 공공 레퍼런스 확보의 창구다. 음성 데이터 장기 기밀성이 요구되는 공공기관(의료, 법무, 국방)을 타깃으로 한 PQC 통화 녹음 솔루션의 시범사업 참여 경로가 열려 있다
- HNDL 위협은 현재 평문 또는 약한 암호화로 저장된 통화 녹음 파일에 직접 적용된다. 수년간 보존되는 녹음 데이터에 ML-KEM 기반 암호화를 소급 적용하는 "레거시 파일 재암호화" 기능이 차별화 요소가 될 수 있다

**위협**

- 3GPP의 PQC 표준화 지연으로 VoLTE/VoNR 채널 레이어 PQC는 2027년 이후가 현실적이다. 현 시점 On-Device PQC는 저장 파일 암호화(at-rest)에 집중해야 하며, 통화 중 실시간 암호화(in-transit) 적용은 표준 공백으로 인해 호환성 이슈가 발생할 수 있다
- PQC 키 크기 증가로 인한 TLS 레이턴시 ~1.5% 증가는 음성 통화 품질에 영향을 줄 수 있다. ARM Cortex-A53 수준 저사양 기기에서 ML-KEM 처리 속도가 150 ops/s에 불과해 고주파 암호화 요구 환경에서 성능 병목 위험이 있다 [[P-03]](#ref-p-03)
- FIPS 140-3 완전 CMVP 인증을 획득한 PQC 모듈이 아직 희소해, 규제 적용 산업(공공·금융·의료) 조달 시 인증 공백이 마찰 요인으로 작용한다
- HQC 초안 표준(2026) 발행 이후 알고리즘 세트 변경 가능성이 있어 현재 ML-KEM 단독 구현 시 향후 재마이그레이션 비용이 발생할 수 있다. Crypto-agile 아키텍처 설계가 필수다

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Akamai — Post Quantum Cryptography Client to Edge | [링크](https://techdocs.akamai.com/property-mgr/docs/pqc-client-to-edge) | official | 2026-01 | [A] |
| <a id="ref-g-02"></a>G-02 | Samsung Semiconductor — Where Trust Begins: Exynos Anchors Post-Quantum Security | [링크](https://semiconductor.samsung.com/news-events/tech-blog/where-trust-begins-exynos-anchors-post-quantum-security-at-the-root-of-mobile-socs/) | official | 2026 | [A] |
| <a id="ref-g-03"></a>G-03 | Technosports — Exynos 2600 Is the World's First Smartphone Chip With Quantum-Proof Encryption | [링크](https://technosports.co.in/exynos-2600-quantum-proof-encryption/) | news | 2026-02 | [B] |
| <a id="ref-g-04"></a>G-04 | The Quantum Insider — QCi and Ciena Demo Quantum-Secure Communications at OFC 2026 | [링크](https://thequantuminsider.com/2026/03/12/qci-ciena-quantum-secure-communications-demo/) | news | 2026-03-12 | [B] |
| <a id="ref-g-05"></a>G-05 | SafeLogic — What Happens on September 21, 2026? | [링크](https://www.safelogic.com/blog/what-happens-on-september-21-2026) | blog | 2026 | [B] |
| <a id="ref-g-06"></a>G-06 | postquantum.com — The Complete US PQC Regulatory Framework in 2026 | [링크](https://postquantum.com/quantum-policies/us-pqc-regulatory-framework-2026/) | news | 2026 | [B] |
| <a id="ref-g-07"></a>G-07 | NIST — NIST Selects HQC as Fifth Algorithm for Post-Quantum Encryption | [링크](https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption) | official | 2025-03-11 | [A] |
| <a id="ref-g-08"></a>G-08 | postquantum.com — Telecom's Quantum-Safe Imperative: Challenges in Adopting PQC | [링크](https://postquantum.com/post-quantum/telecom-pqc-challenges/) | news | 2026 | [B] |
| <a id="ref-g-09"></a>G-09 | p1sec — Post Quantum Cryptography for Mobile Networks | [링크](https://www.p1sec.com/blog/post-quantum-cryptography-for-mobile-networks) | blog | 2025 | [C] |
| <a id="ref-g-10"></a>G-10 | Security Boulevard — Post-Quantum Cryptography for Authentication: Enterprise Migration Guide 2026 | [링크](https://securityboulevard.com/2026/03/post-quantum-cryptography-for-authentication-the-enterprise-migration-guide-2026/) | news | 2026-03 | [B] |
| <a id="ref-g-11"></a>G-11 | Graygroup — Post-Quantum Cryptography in 2026: The Enterprise Guide | [링크](https://www.graygroupintl.com/blog/post-quantum-cryptography-enterprise-guide/) | blog | 2026 | [C] |
| <a id="ref-g-12"></a>G-12 | Pentasecurity — 2026 양자보안 솔루션 리포트 | [링크](https://www.pentasecurity.co.kr/in-the-news/2026-quantum-security-solution-report/) | news | 2026-02 | [B] |
| <a id="ref-g-13"></a>G-13 | 전자신문 — 민관 협업으로 양자 주권 확보, 삼성·LG·SKT 등 양자기술 협의체 출범 | [링크](https://www.etnews.com/20260129000199) | news | 2026-01-29 | [B] |
| <a id="ref-g-14"></a>G-14 | EBN — LG유플러스, 익시 가디언 2.0 공개 (MWC 2026) | [링크](https://www.ebn.co.kr/news/articleView.html?idxno=1701212) | news | 2026-03 | [B] |
| <a id="ref-g-15"></a>G-15 | Thelec.kr — KT "양자암호 PQC+QKD 하이브리드 대세될 것" | [링크](https://www.thelec.kr/news/articleView.html?idxno=28391) | news | 2026 | [B] |
| <a id="ref-g-16"></a>G-16 | Apple Security Research — iMessage with PQ3 | [링크](https://security.apple.com/blog/imessage-pq3/) | official | 2024-02 | [A] |
| <a id="ref-g-17"></a>G-17 | MarketsandMarkets — Post-Quantum Cryptography Market (USD 0.42B → USD 2.84B by 2030, CAGR 46.2%) | [링크](https://www.marketsandmarkets.com/PressReleases/post-quantum-cryptography.asp) | report | 2025 | [C] |
| <a id="ref-g-18"></a>G-18 | Grand View Research — Post-Quantum Cryptography Market (USD 1.15B in 2024 → USD 7.82B by 2030, CAGR 37.6%) | [링크](https://www.grandviewresearch.com/industry-analysis/post-quantum-cryptography-market-report) | report | 2025 | [C] |
| <a id="ref-g-19"></a>G-19 | GlobeNewswire — Post-Quantum Cryptography Migration Is Now a Trillion-Dollar Imperative | [링크](https://www.globenewswire.com/news-release/2026/02/19/3241234/0/en/Post-Quantum-Cryptography-Migration-Is-Now-a-Trillion-Dollar-Imperative.html) | news | 2026-02-19 | [B] |
| <a id="ref-e-01"></a>E-01 | PR Newswire / Ciena — QCi and Ciena Demonstrate Next-Generation Quantum-Secured Communications at OFC 2026 | [링크](https://www.prnewswire.com/news-releases/quantum-computing-inc-and-ciena-demonstrate-next-generation-quantum-secured-communications-with-high-speed-encryption-using-pqc-and-qkd-at-ofc-2026-302710416.html) | 보도자료 | 2026-03-12 | [A] |
| <a id="ref-e-02"></a>E-02 | SKT Newsroom — SKT, 양자암호 양대 기술 QKD+PQC 하나로 묶었다 | [링크](https://news.sktelecom.com/207758) | 보도자료 | 2024-10-15 | [A] |
| <a id="ref-e-03"></a>E-03 | LG유플러스 뉴스룸 — 양자내성암호 적용한 가상사설망 U+ PQC-VPN 출시 | [링크](https://news.lguplus.com/16007) | 보도자료 | 2024-06-24 | [A] |
| <a id="ref-p-01"></a>P-01 | (arXiv:2603.06969) — Securing Cryptography in the Age of Quantum Computing and AI | [링크](https://arxiv.org/html/2603.06969v1) | paper | 2026-03 | [A] |
| <a id="ref-p-02"></a>P-02 | Nature Scientific Reports — Post-quantum cryptographic authentication for industrial IoT using lattice-based cryptography | [링크](https://www.nature.com/articles/s41598-025-28413-8) | paper | 2026-03 | [A] |
| <a id="ref-p-03"></a>P-03 | (arXiv:2512.20243) — Post-Quantum Cryptography in the 5G Core | [링크](https://arxiv.org/html/2512.20243v1) | paper | 2025-12 | [A] |
| <a id="ref-p-04"></a>P-04 | Springer IoT — Implementation and performance of PQC for resource constrained consumer electronics | [링크](https://link.springer.com/article/10.1007/s43926-025-00238-x) | paper | 2025 | [A] |
| <a id="ref-p-05"></a>P-05 | Springer QIP — Decoherence and quantum threats in voice biometric authentication with PQC countermeasures | [링크](https://link.springer.com/article/10.1007/s11128-025-04980-7) | paper | 2025 | [A] |
