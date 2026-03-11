---
type: weekly-research
domain: secure-ai
l3_topic: ondevice-pqc
date: 2026-03-11
signal: 🔴
agent: research-deep
confidence: high
status: completed
sources_used: [websearch]
prev_report: outputs/reports/weekly/2026-03-05_research-ondevice-pqc.md
---

# OnDevice 양자암호 (PQC) — 심층 리서치

> 기간: 2026-03-04 ~ 2026-03-11

---

## 기술 동향

### PLANTS / Merkle Tree Certificates — Google의 PQC TLS 인증서 아키텍처 혁신

2026년 2월 Google은 PQC 적용 TLS 인증서의 크기 문제를 해결하는 새로운 아키텍처 **Merkle Tree Certificates(MTC)**를 발표했으며, 이를 위한 IETF 워킹그룹 **PLANTS(PKI, Logs, And Tree Signatures)**가 공식 가동됐다 [[G-01]](#ref-g-01). 기존 X.509 인증서에 PQC 서명(ML-DSA-44)을 단순 삽입할 경우 TLS 핸드셰이크 인증 데이터가 약 **14,700바이트**로 팽창해 TCP 초기 혼잡 윈도우를 초과하고 레이턴시 60% 이상 증가를 유발한다 [[G-02]](#ref-g-02). MTC는 CA가 수백만 건의 인증서를 포함하는 단일 'Tree Head'를 서명하고, 브라우저는 736바이트의 경량 포함 증명만 수신하는 방식으로 이를 해결한다 [[G-01]](#ref-g-01).

**롤아웃 3단계:**
- Phase 1 (진행 중): Google-Cloudflare 공동 타당성 검토
- Phase 2 (Q1 2027): CT Log 운영자 초기 부트스트래핑 초청
- Phase 3 (Q3 2027): Chrome Quantum-resistant Root Store(CQRS) 온보딩 요건 확정

### NIST CMVP: FIPS 140-2 → Historical 이전 (2026-09-21)

2026년 9월 21일, NIST CMVP는 잔존하는 모든 FIPS 140-2 인증 모듈을 **Historical List**로 이동한다. 이후 신규 조달에는 FIPS 140-3 검증 모듈만 허용된다 [[G-04]](#ref-g-04). FIPS 140-3에는 FIPS 203(ML-KEM), FIPS 204(ML-DSA), FIPS 205(SLH-DSA)에 대한 자가 테스트 요건이 추가되어 있으나, 현재 PQC 알고리즘을 포함한 완전한 FIPS 140-3 CMVP 인증을 획득한 엔터프라이즈 Linux 배포판은 아직 없다 [[G-04]](#ref-g-04).

### NSA CNSA 2.0: 2027-01 신규 시스템 의무화

NSA의 CNSA 2.0(Commercial National Security Algorithm Suite 2.0)은 2027년 1월부터 모든 신규 국가 안보 시스템(NSS) 조달에 양자내성 알고리즘 준수를 의무화한다 [[G-05]](#ref-g-05). 알고리즘 세트: ML-KEM(키 캡슐화), ML-DSA(디지털 서명). 전면 의무화(레거시 제거)는 2030~2031년 목표다.

### Google 내부 트래픽 ML-KEM 전환 완료

2026년 2월 Google은 모든 내부 트래픽의 키 교환을 ML-KEM으로 완료했다고 공개했다 [[G-06]](#ref-g-06). X25519+ML-KEM-768 하이브리드(X-Wing KEM) 방식이 채택됐으며, "대규모 PQC 배포가 기술적으로 실현 가능함을 실증했다"는 메시지를 발신했다 [[G-06]](#ref-g-06).

### Cloudflare: IPsec 하이브리드 ML-KEM (2026-03)

Cloudflare는 2026년 3월, IPsec IKEv2에 하이브리드 ML-KEM을 적용해 SASE(Secure Access Service Edge) 스택 전체를 PQC화한 최초의 사업자가 됐다 [[G-07]](#ref-g-07). 2026-02-11 One Appliance v2026.2.0을 통해 자동 업그레이드가 배포됐으며, Cloudflare 네트워크 유입 인간 생성 TLS 트래픽의 **60% 이상이 하이브리드 ML-KEM 사용 중**이다 [[G-07]](#ref-g-07). IPsec은 현재 closed beta이며 2026년 6월까지 3개 기능이 추가 출시될 예정이다.

### Microsoft PQC APIs GA (Windows / .NET)

Windows Server 2025, Windows 11(24H2, 25H2), .NET 10에서 ML-KEM 및 ML-DSA API가 **정식 출시(General Availability)**됐다 [[G-08]](#ref-g-08). Active Directory Certificate Services(ADCS)의 PQC 지원은 2026년 초 GA 목표이며, Azure, Microsoft 365, AI 서비스에도 순차 적용 중이다 [[G-08]](#ref-g-08).

### HQC: NIST 5번째 PQC 표준 후보 초안 2026년 예정

HQC(Hamming Quasi-Cyclic)가 ML-KEM의 수학적 백업 알고리즘으로 NIST 5번째 표준에 선정됐다. 초안은 2026년, 최종 표준은 2027년 목표다 [[G-12]](#ref-g-12).

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| Google | ML-KEM으로 전사 내부 트래픽 키 교환 완료. PLANTS 워킹그룹 주도, MTC 아키텍처 발표(2026-02). 14,700B → 736B 인증서 경량화 | [[G-01]](#ref-g-01), [[G-02]](#ref-g-02), [[G-06]](#ref-g-06) |
| Cloudflare | 2026-02-23 세계 최초 완전 PQC SASE 달성. IPsec IKEv2 하이브리드 ML-KEM 추가(2026-03). 트래픽 60% 이상 하이브리드 ML-KEM 적용 | [[G-07]](#ref-g-07) |
| Microsoft | ML-KEM·ML-DSA API GA (Windows 11/Server 2025/.NET 10). ADCS PQC 지원 2026 초 목표. Azure·M365 순차 통합 중 | [[G-08]](#ref-g-08) |
| Samsung | S3SSE2A: 업계 최초 하드웨어 기반 PQC Secure Element. CC EAL6+ 인증, FIPS 204(ML-DSA) 하드웨어 구현으로 소프트웨어 대비 최대 17배 처리 속도. CES 2026 최우수 사이버보안 혁신상 수상. Thales가 보안 OS 공급 | [[G-09]](#ref-g-09), [[E-01]](#ref-e-01) |
| Samsung (Exynos) | 모바일 SoC 부트 ROM 단계부터 PQC 기반 보안 부트 적용. Galaxy S25 시리즈부터 ML-KEM/ML-DSA 소프트웨어 적용 시작 | [[G-10]](#ref-g-10) |
| Thales | 2026-03-02 세계 최초: 이미 배포된 5G SIM/eSIM에 OTA로 PQC 원격 업그레이드 성공 실증. 기기 교체·서비스 중단 없음. Crypto-agile 접근 방식 | [[G-11]](#ref-g-11) |
| Apple | iMessage PQ3 프로토콜 기배포(iOS 17.4+). ML-KEM+Kyber 하이브리드 방식, 50메시지마다 또는 7일마다 키 로테이션. WWDC25에서 양자내성 암호화 플랫폼 확장 발표 | [[G-03]](#ref-g-03) |
| IBM | z16 메인프레임에 ML-KEM·ML-DSA 내장. NIST PQC 표준 두 알고리즘(ML-KEM, ML-DSA)을 자사가 개발. NCCoE SP 1800-38 협력사 참여(47개사) | [[G-13]](#ref-g-13) |
| SKT | QKD+PQC 하이브리드 제품 출시(세계 최초). Q-HSM(QRNG+PUF+소프트웨어 PQC) 양산. Thales와 5G SA SUPI PQC 실증. IonQ 지분 교환으로 양자컴퓨팅-AI-통신 융합 추진 | [[G-14]](#ref-g-14) |
| KT | SKT와 공동 양자암호 전용 회선 서비스 운영. 2026년부터 공공기관 대상 하이브리드 PQC+QKD 망 구축 개시 | [[G-14]](#ref-g-14) |
| NIST | FIPS 140-2 → Historical(2026-09-21). CSWP 39(암호 민첩성 성숙도 모델) 확정(2025-12-19). HQC 초안 2026년 예정 | [[G-04]](#ref-g-04), [[G-12]](#ref-g-12) |

---

## 시장 시그널

- PQC 시장 규모는 2026년 약 5.1억 달러(Business Research Insights), 2030년까지 최소 28억~46억 달러 성장 전망(CAGR 39~46%); 조사기관별 방법론 차이로 추정치 편차가 크다 [[G-15]](#ref-g-15)
- 하이브리드(고전+PQC) 방식이 현 주류로 확립됨 — 순수 PQC 배포는 극히 드물고, 하이브리드 배포가 사실상 표준 경로로 고착화 [[G-16]](#ref-g-16)
- 기업 사이버보험 시장에서 PQC 전환 계획 부재 시 보험료 인상 또는 양자 관련 면책 조항 삽입 움직임이 관측됨 [[G-16]](#ref-g-16)
- IPO S-1 등록서류에 하이브리드 암호화 적용 여부가 중요 공시 사항으로 등장 — 양자 대비태세가 재무적 리스크 항목으로 부상 [[G-16]](#ref-g-16)
- CDN 선두권 Cloudflare: Q1 2026 완전 PQC SASE 달성. 6월까지 3개 추가 기능 출시 예정 [[G-07]](#ref-g-07)
- 금융·정부·국방·통신 분야가 PQC 조기 도입 선도; TLS, VPN, PKI, 클라우드 KMS, 펌웨어 서명 순으로 배포 [[G-15]](#ref-g-15)
- NSA CNSA 2.0 2027-01 의무화, NIST FIPS 140-2 2026-09 종료라는 이중 규제 마감이 기업 조달 전환을 압박 [[G-04]](#ref-g-04), [[G-05]](#ref-g-05)
- 5G SIM OTA PQC 업그레이드 최초 실증(Thales 2026-03-02): 수십억 대의 기배포 기기를 교체 없이 양자내성으로 전환할 수 있는 기술적 경로가 열림 [[G-11]](#ref-g-11)
- 하이브리드 모드는 단독 알고리즘 대비 네트워크 처리량을 약 절반 수준으로 감소, 레이턴시 증가 — 고성능 엔드포인트에서는 수용 가능하나 리소스 제한 IoT에서는 최적화 필요 [[G-16]](#ref-g-16)

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| Lattice-Based Cryptographic Accelerators for the Post-Quantum Era (MDPI Electronics, 2026-01) | FPGA·ASIC 기반 NTT 가속기 아키텍처 종합 리뷰. 다중 스킴(Kyber·Dilithium·Falcon·SPHINCS+) 지원 설계가 단일 스킴 대비 면적 효율 81.85% 달성 가능 | [[P-01]](#ref-p-01) |
| Performance Analysis and Industry Deployment of PQC Algorithms (arXiv:2503.12952, 2026-03) | ML-KEM+ML-DSA는 모바일에서 저레이턴시·최소 CPU 오버헤드 실증. ARM Cortex-A53: ML-KEM 150 ops/s vs. Intel i7-12700K 85,000 ops/s | [[P-02]](#ref-p-02) |
| Post-Quantum Cryptography in the 5G Core (arXiv:2512.20243) | PQC 적용 시 성능 영향이 측정 가능하나 5G 망 가용성에 실질적 영향 없음. 하이브리드 X25519+Kyber768: +2.3KB, 레이턴시 중위값 10~20ms 추가 | [[P-03]](#ref-p-03) |
| A Formal Analysis of Apple's iMessage PQ3 Protocol (Linker, USENIX Security '25) | PQ3의 순방향 비밀성·사후 침해 보안·양자내성을 형식 검증으로 확인. harvest-now-decrypt-later 위협에 대한 수학적 증명 | [[P-04]](#ref-p-04) |
| Implementation and Performance of PQC for Resource Constrained Consumer Electronics (Springer IoT, 2025) | CRYSTALS-Kyber가 메모리·에너지 지표에서 가장 균형적 성능 제공. RSA 대비 메모리 20~30%, 에너지 최대 18% 절감. ESP32 등 MCU 실용화 가능 | [[P-05]](#ref-p-05) |

---

## 이전 대비 변화

이전 리포트(2026-03-05) 이후 이번 주(2026-03-04~03-11) 신규 포착된 변화:

- **신규 [최고 임팩트]**: Google PLANTS/MTC 아키텍처 발표(2026-02 후반, 3월 초 미디어 확산). PQC 인증서 크기 문제에 대한 근본적 해법이 제시됨으로써 브라우저·CDN 생태계 전체의 전환 경로가 구체화됐다 [[G-01]](#ref-g-01), [[G-02]](#ref-g-02)
- **신규 [기반 확장]**: Cloudflare IPsec IKEv2 PQC 지원이 3월 초 InfoQ를 통해 공개됨. SASE 전 계층 완성으로 기업 WAN 트래픽 보호 범위가 확대됐다 [[G-07]](#ref-g-07)
- **지속 [강화]**: Microsoft PQC API GA 소식이 3월 초 재확산. Windows·.NET 개발자 생태계의 PQC 접근성이 공식 확인됐다 [[G-08]](#ref-g-08)
- **지속 [규제 압박 심화]**: NSA CNSA 2.0 2027-01 데드라인과 NIST FIPS 140-2 2026-09 종료 일정이 복수 분석 리포트에서 재조명됨. "관망"이 더 이상 방어 가능한 전략이 아님을 업계가 공식화하는 흐름 [[G-04]](#ref-g-04), [[G-05]](#ref-g-05)
- **지속 [디바이스 레이어]**: Samsung S3SSE2A CES 2026 수상 이후 미디어 후속 보도 지속. 하드웨어 PQC가 모바일·IoT 레이어에서 실용화 단계에 진입했다는 신호 [[G-09]](#ref-g-09)

---

## 전략적 시사점

**기회**

- Google PLANTS/MTC는 PQC 인증서 성능 장벽을 제거한다. 국내 PKI·CA 사업자와 CDN 업체는 MTC 호환 인프라 준비를 2026년 내 착수해야 Chrome CQRS Q3 2027 온보딩 윈도우를 놓치지 않는다
- Thales OTA 5G SIM PQC 업그레이드 기술은 SKT·KT에게 기배포 수천만 단말의 양자내성 전환을 기기 교체 없이 추진할 수 있는 경로를 제공한다. 상용화 협의 가속화가 필요하다
- Samsung S3SSE2A(CC EAL6+, 소프트웨어 대비 17배 속도)는 온디바이스 PQC 하드웨어 가속의 레퍼런스 아키텍처를 확립했다. Exynos SoC 통합 로드맵을 보면 Galaxy 플래그십이 2~3년 내 완전 HW-PQC 플랫폼으로 전환될 전망이다
- FIPS 140-3 CMVP 인증 공백(현재 PQC 포함 모듈 미인증)은 국내 보안 기업에게 단기적 시장 선점 기회를 제공한다. CAVP 획득 후 CMVP 인증 로드맵 가속이 유효하다
- NSA CNSA 2.0·NIST 마감 압박은 국내 공공·국방 조달 레퍼런스 확보의 시간 창이다. SKT Q-HSM, KT 하이브리드 PQC+QKD 망이 이미 포지셔닝 중이다

**위협**

- 하이브리드 모드는 처리량을 약 절반으로 감소시킨다. 리소스 제한 IoT·MCU 기기(ARM Cortex-A53 ML-KEM 150 ops/s)에서는 실제 배포 전 최적화 검증이 필수이며, 충분한 프로파일링 없이 배포 시 서비스 품질 저하 리스크가 있다
- FIPS 140-3 PQC 인증 모듈 부재는 규제 적용 산업(금융·의료·공공)의 조달 결정을 지연시킬 수 있다. 미국 연방기관 납품을 위한 한국 기업의 인증 확보 경로가 아직 불투명하다
- Google MTC/CQRS는 기존 X.509 PKI 생태계를 우회하는 새로운 신뢰 체계다. 기존 인증서 발급·관리 비즈니스 모델에 대한 중장기 파괴 리스크가 존재한다
- NSA CNSA 2.0은 ML-KEM과 ML-DSA를 의무화하지만, 향후 NIST HQC 표준화(초안 2026년, 확정 2027년) 이후 알고리즘 세트가 변경될 경우 초기 배포 조직의 재마이그레이션 비용이 발생한다

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | The Hacker News — Google Develops Merkle Tree Certificates for Quantum-Resistant HTTPS | [링크](https://thehackernews.com/2026/03/google-develops-merkle-tree.html) | news | 2026-03 | [B] |
| <a id="ref-g-02"></a>G-02 | Google Security Blog — Cultivating a robust and efficient quantum-safe HTTPS | [링크](https://security.googleblog.com/2026/02/cultivating-robust-and-efficient.html) | blog/official | 2026-02 | [A] |
| <a id="ref-g-03"></a>G-03 | Apple Security Research — iMessage with PQ3 | [링크](https://security.apple.com/blog/imessage-pq3/) | official | 2024-02 | [A] |
| <a id="ref-g-04"></a>G-04 | postquantum.com — The Complete US PQC Regulatory Framework in 2026 | [링크](https://postquantum.com/quantum-policies/us-pqc-regulatory-framework-2026/) | news | 2026 | [B] |
| <a id="ref-g-05"></a>G-05 | NSA — CSA CNSA 2.0 Algorithms | [링크](https://media.defense.gov/2025/May/30/2003728741/-1/-1/0/CSA_CNSA_2.0_ALGORITHMS.PDF) | official | 2022-09 (2025 rev) | [A] |
| <a id="ref-g-06"></a>G-06 | Kiteworks — Google Warns Quantum Threats to Encryption Are Imminent (2026) | [링크](https://www.kiteworks.com/cybersecurity-risk-management/google-quantum-computing-encryption-threat-post-quantum-cryptography/) | news | 2026-02 | [B] |
| <a id="ref-g-07"></a>G-07 | InfoQ — Standardizing Post-Quantum IPsec: Cloudflare Adopts Hybrid ML-KEM | [링크](https://www.infoq.com/news/2026/03/cloudflare-post-quantum-ipsec/) | news | 2026-03 | [B] |
| <a id="ref-g-08"></a>G-08 | Microsoft Tech Community — Post-Quantum Cryptography APIs Now Generally Available | [링크](https://techcommunity.microsoft.com/blog/microsoft-security-blog/post-quantum-cryptography-apis-now-generally-available-on-microsoft-platforms/4469093) | official | 2026 | [A] |
| <a id="ref-g-09"></a>G-09 | Samsung Semiconductor — S3SSE2A: Industry's First Hardware-Based PQC | [링크](https://semiconductor.samsung.com/news-events/tech-blog/ces-innovations-awards-2026-honoree-interview-s3sse2a/) | official | 2026-01 | [A] |
| <a id="ref-g-10"></a>G-10 | Samsung Semiconductor — Exynos Anchors Post-Quantum Security at the Root of Mobile SoCs | [링크](https://semiconductor.samsung.com/news-events/tech-blog/where-trust-begins-exynos-anchors-post-quantum-security-at-the-root-of-mobile-socs/) | official | 2026 | [A] |
| <a id="ref-g-11"></a>G-11 | The Quantum Insider — Thales Demonstrates Remote Post-Quantum Security Upgrade for 5G SIMs | [링크](https://thequantuminsider.com/2026/03/02/thales-remote-post-quantum-5g-sim-upgrade/) | news | 2026-03-02 | [B] |
| <a id="ref-g-12"></a>G-12 | Utimaco — NIST announces HQC as fifth algorithm to be standardized | [링크](https://utimaco.com/news/blog-posts/pqc-news-nist-announces-hqc-fifth-algorithm-be-standardized) | news | 2025 | [B] |
| <a id="ref-g-13"></a>G-13 | IBM Newsroom — IBM-Developed Algorithms as NIST's First PQC Standards | [링크](https://newsroom.ibm.com/2024-08-13-ibm-developed-algorithms-announced-as-worlds-first-post-quantum-cryptography-standards) | official | 2024-08-13 | [A] |
| <a id="ref-g-14"></a>G-14 | SKT Newsroom — Path towards a quantum-safe future | [링크](https://news.sktelecom.com/en/853) | official | 2024 | [A] |
| <a id="ref-g-15"></a>G-15 | GlobeNewswire — Post-Quantum Cryptography Industry Research Report 2026 | [링크](https://www.globenewswire.com/news-release/2026/02/23/3242432/28124/en/Post-Quantum-Cryptography-Industry-Research-Report-2026-PQC-Transitions-from-Research-Concept-to-Core-Cybersecurity-Pillar-Amid-Rising-Quantum-Computing-Breakthroughs.html) | news | 2026-02-23 | [C] |
| <a id="ref-g-16"></a>G-16 | Graygroup — Post-Quantum Cryptography in 2026: The Enterprise Guide | [링크](https://www.graygroupintl.com/blog/post-quantum-cryptography-enterprise-guide/) | blog | 2026 | [C] |
| <a id="ref-e-01"></a>E-01 | BusinessWire — Thales Powers CES-Winning Post-Quantum Chip From Samsung Electronics | [링크](https://www.businesswire.com/news/home/20260106145232/en/Thales-Powers-CES-Winning-Post-Quantum-Chip-From-Samsung-Electronics) | 보도자료 | 2026-01-06 | [A] |
| <a id="ref-p-01"></a>P-01 | Bathen et al. — Lattice-Based Cryptographic Accelerators for the Post-Quantum Era (MDPI Electronics 15(2):475) | [링크](https://www.mdpi.com/2079-9292/15/2/475) | paper | 2026-01 | [A] |
| <a id="ref-p-02"></a>P-02 | (arXiv:2503.12952) — Performance Analysis and Industry Deployment of Post-Quantum Cryptography Algorithms | [링크](https://arxiv.org/html/2503.12952v1) | paper | 2026-03 | [A] |
| <a id="ref-p-03"></a>P-03 | (arXiv:2512.20243) — Post-Quantum Cryptography in the 5G Core | [링크](https://arxiv.org/html/2512.20243v1) | paper | 2025-12 | [A] |
| <a id="ref-p-04"></a>P-04 | Linker — A Formal Analysis of Apple's iMessage PQ3 Protocol (USENIX Security '25) | [링크](https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-595-linker.pdf) | paper | 2025 | [A] |
| <a id="ref-p-05"></a>P-05 | Springer IoT — Implementation and performance of PQC for resource constrained consumer electronics | [링크](https://link.springer.com/article/10.1007/s43926-025-00238-x) | paper | 2025 | [A] |
