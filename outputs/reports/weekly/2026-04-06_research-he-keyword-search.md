---
type: weekly-deep-research
topic: he-keyword-search
date: 2026-04-06
period: 2026-03-30 ~ 2026-04-06
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
parent: 2026-04-06_weekly-secure-ai.md
prior_report: 2026-03-30_research-he-keyword-search.md
---

# Deep 리서치: On-Device 동형암호 키워드 검색 (2026-W15)

> 기간: 2026-03-30 ~ 2026-04-06

## 이전 대비 변화

- **전주 (W14)**: "Privacy at your Fingertips" — 클라이언트 측 완전 동형암호(Fully Homomorphic Encryption, FHE) enc/dec 오버헤드 97% 감소(EuroS&P 2026), CAT GPU 가속 프레임워크 arXiv 공개(33× 가속), Zama + T-REX Network $32억 실물자산(Real World Asset, RWA) FHE 인프라 출시, Intel Heracles 기술 사양 상세 확산, FHE.org 타이페이 개최
- **금주 (W15)**: Niobium "The Fog" FHE 클라우드 플랫폼 공개 론칭(4/2), CryptoLab HEaaN Zero-Leak RAG 국내 정부품질인증(Government Software, GS) 1등급 획득(3/27), NIST 다자간 임계값(Multi-Party Threshold Schemes, MPTS) 2026 워크숍에서 임계값 FHE(Threshold FHE, Th-FHE) + 정밀 동형암호 기법(Cheon-Kim-Kim-Song, CKKS) 시연(1월, 본주 상세 확인), Intel Heracles ISSCC 발표 상세 보도 지속(3/10)
- **변화 방향**: 하드웨어 가속기 발표가 **소프트웨어 플랫폼·인증 상용화** 단계로 전환. Niobium이 암호화 시맨틱 검색(Encrypted Semantic Search)을 프리빌드 앱으로 제공하며 B2B 플랫폼 진입, CryptoLab이 공공 부문 인증을 통해 국내 정부 조달 진입로 확보. 통신(Telecom) 부문에서 LG U+가 최초 실제 배포(Proof of Concept, PoC) 고객으로 확인.

---

## 기술 동향

1. **Niobium "The Fog" — FHE 클라우드 플랫폼 공개, Encrypted Semantic Search 프리빌드 앱 포함 (4/2).**
   Niobium Microsystems가 4월 2일 프라이빗 베타를 공식 발표했다. The Fog는 FHE를 사용해 연산 중에도 데이터를 복호화하지 않는 프라이빗 클라우드 인프라다. 현재 런칭 플랫폼은 FPGA 기반 mistic Core 가속기로, GPU 대비 FHE 연산 최대 2× 빠르다고 발표했다. 세 가지 프리빌드(pre-built) 애플리케이션을 제공하며, 그 중 Encrypted Semantic Search(Secure RAG)는 쿼리와 데이터셋 모두 암호화 상태를 유지하면서 의미 기반 검색을 실행한다. 별도 컴파일러·소프트웨어 개발 키트(Software Development Kit, SDK)를 통해 암호화 비전문가도 FHE 앱을 개발할 수 있다. 공개 출시(Public Launch)는 Q2 2026 말 목표. [[G-01]](#ref-g-01), [[G-02]](#ref-g-02), [[E-01]](#ref-e-01)

2. **CryptoLab HEaaN Zero-Leak RAG — TTA GS 1등급 인증 획득 (3/27), 국내 공공 조달 진입 경로 확보.**
   한국정보통신기술협회(Telecommunications Technology Association, TTA)가 CryptoLab의 생성형 AI 보안 솔루션 "HEaaN Zero-Leak RAG"에 GS 1등급을 부여했다. 이 솔루션은 벡터 데이터베이스를 처음부터 동형암호로 암호화해, 암호문(Ciphertext) 상태에서 유사도 검색을 수행한다. 평문 대비 약 99% 정확도, 고성능 환경 기준 첫 토큰 생성 약 1.9초. 개방형 웹 애플리케이션 보안 프로젝트(Open Web Application Security Project, OWASP) 거대 언어 모델(Large Language Model, LLM) 상위 10대 취약점 중 하나인 임베딩 역변환(Embedding Inversion) 공격을 방어할 수 있는 유일 공인 솔루션으로 인정됐다. 2026년 6월 조달청 혁신 시제품 등록, 9월 CC 인증(EAL2) 취득 예정. Gartner 혁신 기술 카테고리 선정 국내 최초 동형암호 기업. [[G-03]](#ref-g-03), [[G-04]](#ref-g-04), [[E-02]](#ref-e-02)

3. **NIST MPTS 2026 워크숍 — Th-FHE from CKKS 시연, CryptoLab Damien Stehlé 발표 (2026-01).**
   NIST 다자간 임계값 체계 워크숍(MPTS 2026, 1월 26~29일)에서 CryptoLab의 Damien Stehlé가 "Threshold FHE from CKKS and Applications"를 발표했다. 임계값 FHE는 복호화 권한을 여러 참여자에게 분산하는 FHE 확장 기술로, 단일 기관이 모든 키를 보유하지 않아도 되는 분산 신뢰 모델을 구현한다. CryptoLab HEaaN 라이브러리의 근사 및 정밀 연산 성능을 함께 시연했다. 관련 논문 THED(Threshold Dilithium from FHE)도 공개됨(IACR ePrint 2026/638). [[G-05]](#ref-g-05), [[G-06]](#ref-g-06)

4. **Intel Heracles ISSCC 발표 상세 — 1,074~5,547× Xeon 대비 가속, 3nm FinFET (3/10 발표, 본주 보도 확산).**
   Intel이 ISSCC(국제 반도체 회로 학술대회, International Solid-State Circuits Conference) 2026에서 Heracles FHE 전용 칩을 공개했다. 1.2 GHz, 197mm², 176W, Intel 3(3nm FinFET) 공정. 48GB 고대역폭 메모리(High Bandwidth Memory, HBM) 819 GB/s 대역폭. 8192-way SIMD 연산 엔진(64 타일쌍, 타일쌍당 128 병렬 산술 레인, 8×8 메시 배열). BGV, BFV, CKKS 다중 FHE 스킴 지원. PCIe 가속기 카드 형태. 암호화된 유권자 데이터베이스 익명 쿼리에서 Xeon(15ms) 대비 Heracles(14μs)로 1,071× 가속. 키워드 검색 직접 적용 가능한 성능. 양산 일정은 미발표. [[G-07]](#ref-g-07), [[G-08]](#ref-g-08), [[E-03]](#ref-e-03)

5. **LG U+ + CryptoLab MWC 2026 협력 발표 — AI 에이전트 ixi-O 및 AI 컨택센터(AI Contact Center, AICC) 동형암호 탑재 (발표 3/10, 본주 추가 확인).**
   MWC 2026 바르셀로나(현지시간 3월 4일)에서 LG U+와 CryptoLab이 협력을 발표했다. LG U+는 통화 데이터를 동형암호 상태로 저장하고 복호화 없이 키워드 검색을 실행하는 계획을 제시했다. AI 에이전트 ixi-O는 음성통화를 텍스트로 변환하는 온디바이스 서비스를 운영 중이며, 해당 데이터에 동형암호를 적용한다. CryptoLab CEO 정희천은 CKKS+(4.5세대)가 "실시간 지연 없이(no real-time latency)" 작동하며 온디바이스 운용에 충분히 경량화됐다고 발표했다. [[G-09]](#ref-g-09), [[E-04]](#ref-e-04)

6. **SemiFive + Samsung Foundry — Niobium FHE ASIC 설계·제조 계약 확인 (2026-02-20, 본주 추가 확인).**
   SemiFive가 Niobium과 1,000억 원(약 USD 690만) 규모 FHE 하드웨어 가속기 ASIC 개발 계약을 체결했다. Samsung Foundry 8nm 저전력 울티메이트(8nm Low Power Ultimate, 8LPU) 공정으로 제조. SemiFive가 설계·패키징·테스트·공급망 관리 일괄(Turnkey) 담당. Niobium CEO Kevin Yoder는 "암호화된 채로 연산하는 속도가 충분히 빨라지면, 평문 상태로 민감 정보를 처리하는 것은 더 이상 수용 불가능해질 것"이라 발언. [[G-10]](#ref-g-10), [[E-01]](#ref-e-01)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| Niobium (미국) | "The Fog" FHE 클라우드 플랫폼 프라이빗 베타 개시(4/2). mistic Core FPGA 가속기(GPU 대비 2×). Encrypted Semantic Search·Federated Learning·ML Classification 프리빌드 앱 제공. SemiFive·Samsung Foundry와 ASIC 개발 중(8nm 8LPU). Q2 말 공개 출시 예정. 누적 투자 $2,300만+ | [[G-01]](#ref-g-01), [[G-02]](#ref-g-02), [[G-10]](#ref-g-10), [[E-01]](#ref-e-01) |
| CryptoLab (한국) | HEaaN Zero-Leak RAG TTA GS 1등급 취득(3/27). 평문 대비 99% 정확도, 첫 토큰 1.9초. Gartner 선정 국내 최초 동형암호 기업. LG U+ ixi-O·AICC PoC 진행. CKKS+(4.5세대) 온디바이스 경량화 달성. 6월 조달청 등록 추진 | [[G-03]](#ref-g-03), [[G-04]](#ref-g-04), [[G-09]](#ref-g-09), [[E-02]](#ref-e-02), [[E-04]](#ref-e-04) |
| Intel (미국) | Heracles FHE ASIC ISSCC 공개(3/10). 1,074~5,547× Xeon 대비 가속. 197mm², 176W, Intel 3(3nm), 48GB HBM. BGV·BFV·CKKS 지원. 양산 일정 미발표, PCIe 가속기 형태. DARPA DRIVE 프로그램 기원 | [[G-07]](#ref-g-07), [[G-08]](#ref-g-08), [[E-03]](#ref-e-03) |
| Zama (프랑스) | FHE.org 2026 타이페이(3/8) 발표 8건. TFHE 부트스트래핑 GPU 서브밀리초(sub-millisecond) 달성. T-REX Network와 $32억 RWA FHE 인프라 출시(3/26). Apple·AWS·Google 컨퍼런스 후원 유치. 유니콘($10억+ 밸류에이션) 지위 유지 | [[G-11]](#ref-g-11), [[G-12]](#ref-g-12) |
| LG U+ (한국) | MWC 2026에서 CryptoLab과 AI 에이전트 ixi-O·AICC 동형암호 협력 발표(3/4). 통화 데이터 암호화 저장·복호화 없는 키워드 검색 계획. 국내 통신사 최초 FHE 실 서비스 적용 경로 | [[G-09]](#ref-g-09), [[E-04]](#ref-e-04) |
| Apple (미국) | swift-homomorphic-encryption 오픈소스 라이브러리 운영 중. iOS 18 Live Caller ID Lookup·Enhanced Visual Search에 PIR(Private Information Retrieval) 기반 온디바이스 HE 적용. FHE.org 2026 후원. 최신 동향 추가 공개 없음 | [[G-13]](#ref-g-13) |
| Duality Technologies (미국) | 정부 Zero-Footprint Intelligence 분야 FHE 암호화 쿼리 초당 수천 건 처리 가능. 포스트 양자(Post-Quantum) FHE 보안 연구 선도. DARPA 계약 보유. 2026년 Gartner 기밀 컴퓨팅(Confidential Computing) 핵심 기술 선정 | [[G-14]](#ref-g-14) |

---

## 시장 시그널

**플랫폼 상용화 동향**

- Niobium The Fog: B2B FHE 클라우드 서비스 최초 프리빌드 앱 제공 모델로 진입. 암호화 전문 지식 없는 개발자도 FHE 앱 구축 가능한 추상화 계층 제공. Q2 2026 공개 출시 예정 [[G-01]](#ref-g-01), [[E-01]](#ref-e-01)
- CryptoLab: GS 1등급 인증으로 국내 공공 부문 조달 시장 진입 확보. 2026년 6월 조달청 혁신 시제품, 9월 CC(EAL2) 취득 로드맵 [[G-03]](#ref-g-03), [[E-02]](#ref-e-02)
- LG U+ ixi-O: 통신사 AI 에이전트에 동형암호 적용 최초 사례. 음성 통화 텍스트 변환 데이터를 암호화 채로 저장 및 키워드 검색 [[G-09]](#ref-g-09), [[E-04]](#ref-e-04)

**하드웨어 공급망**

- Samsung Foundry: SemiFive 통해 Niobium ASIC 수주(8nm 8LPU 공정). FHE 전용 칩 제조 최초 대형 파운드리 계약. 동형암호 공급망에 삼성 진입 확인 [[G-10]](#ref-g-10)
- Intel: Heracles PCIe 가속기 서버 배치 형태. 온디바이스가 아닌 서버 측 가속. 양산 일정 미발표로 실제 제품화 시점 불확실 [[G-07]](#ref-g-07), [[G-08]](#ref-g-08)

**시장 규모 전망**

- 동형암호 시장: 2024년 $12억 → 2033년 $84억, 연평균 성장률(Compound Annual Growth Rate, CAGR) 30.0% (Market Research Intellect, 2026-2033 기간 기준) [[G-15]](#ref-g-15) [추가확인 필요]
- Gartner Hype Cycle 2026: 기밀 컴퓨팅(Confidential Computing)이 핵심 아키텍처 기술 3종 중 하나로 선정. FHE 포함 프라이버시 강화 기술(Privacy Enhancing Technology, PET) 전반 기업 채택 가속화 전망 [[G-14]](#ref-g-14)

**표준화 동향**

- NIST MPTS 2026(1월): Th-FHE from CKKS 발표. 분산 키 생성 알고리즘을 통해 신뢰 딜러(Trusted Dealer) 없이 FHE 파라미터화 구현 가능. 다자간 컴퓨팅(Multi-Party Computation, MPC) + FHE 융합 표준화 진행 중 [[G-05]](#ref-g-05), [[G-06]](#ref-g-06)
- FHE.org 2026 타이페이(3/8): 55편 제출, 10편 채택, 23편 포스터. Apple·AWS·Google 후원. 학계·산업계 교류 심화 [[G-11]](#ref-g-11)

---

## 전략적 시사점

**기회**

- CryptoLab의 GS 1등급 인증은 국내 공공 부문 조달 시장 진입의 직접 경로. 통신사가 AI 컨택센터(AICC) 수요를 국내 조달로 충당할 경우 CryptoLab 경쟁력 우위
- LG U+–CryptoLab PoC는 국내 통신사 중 최초 FHE 실서비스 적용 경쟁으로 번질 가능성. KT·SKT 동향 추적 필요
- Niobium The Fog Encrypted Semantic Search는 클라우드 기반 암호화 RAG SaaS 시장을 정의하는 첫 사례. 파트너십 또는 B2B 계약 기회

**위협**

- Intel Heracles 양산 일정 미발표: 하드웨어 가속 기반 FHE 의 실제 배포 시점 지연 리스크. Heracles 상용화 이전까지 FPGA·GPU 기반 솔루션이 대안
- 시장 전망 수치($12억→$84억, CAGR 30%)는 단일 조사기관(Market Research Intellect) 출처로 독립 교차 검증 미완료. 다른 기관 수치와 편차 존재 [추가확인 필요]
- CKKS 기반 근사 암호화(Approximate Homomorphic Encryption)의 보안 정의(Differential Private Homomorphic Evaluation, DPHE)가 아직 표준화 미완료 단계. 규제 불확실성 상존

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | SiliconANGLE — Niobium brings fully encrypted AI workloads to the cloud with The Fog | [링크](https://siliconangle.com/2026/04/02/niobium-brings-fully-encrypted-ai-workloads-cloud-fog/) | news | 2026-04-02 | [B] |
| <a id="ref-g-02"></a>G-02 | ITdaily — Niobium's The Fog: new cloud platform for secure AI workloads | [링크](https://itdaily.com/news/cloud/niobium-fog/) | news | 2026-04-02 | [B] |
| <a id="ref-g-03"></a>G-03 | Seoul Economic Daily (EN) — CryptoLab Earns Top-Tier GS Certification | [링크](https://en.sedaily.com/news/2026/03/27/cryptolab-earns-top-tier-gs-certification-targets-public) | news | 2026-03-27 | [B] |
| <a id="ref-g-04"></a>G-04 | Seoul Economic Daily (EN) — Gartner-recognized encryption startup seeks to commercialize Korea's homomorphic security tech | [링크](https://en.sedaily.com/news/2026/04/04/gartner-recognized-encryption-startup-seeks-to) | news | 2026-04-04 | [B] |
| <a id="ref-g-05"></a>G-05 | NIST CSRC — Threshold FHE from CKKS and Applications (MPTS 2026 발표 슬라이드) | [링크](https://csrc.nist.gov/presentations/2026/mpts2026-2b4) | news | 2026-01-29 | [A] |
| <a id="ref-g-06"></a>G-06 | NIST CSRC — MPTS 2026 Workshop on Multi-Party Threshold Schemes | [링크](https://csrc.nist.gov/events/2026/mpts2026) | news | 2026-01-26 | [A] |
| <a id="ref-g-07"></a>G-07 | IEEE Spectrum — Intel's Heracles Chip Speeds Up FHE Computing | [링크](https://spectrum.ieee.org/fhe-intel) | news | 2026-03-10 | [A] |
| <a id="ref-g-08"></a>G-08 | Tom's Hardware — Intel's Heracles chip computes fully-encrypted data without decrypting it | [링크](https://www.tomshardware.com/tech-industry/cyber-security/intels-heracles-chip-computes-fully-encrypted-data-without-decrypting-it-chip-is-1-074-to-5-547-times-faster-than-a-24-core-intel-xeon-in-fhe-math-operations) | news | 2026-03-10 | [B] |
| <a id="ref-g-09"></a>G-09 | The Asia Business Daily — LG Uplus and Cryptolab Aim to Block Hacking Risks with Homomorphic Encryption (MWC 2026) | [링크](https://www.asiae.co.kr/en/article/2026031008212144575) | news | 2026-03-10 | [B] |
| <a id="ref-g-10"></a>G-10 | Evertiq — SemiFive secures design win with Niobium for FHE accelerator | [링크](https://evertiq.com/design/2026-02-20-semifive-secures-design-win-with-niobium-for-fhe-accelerator) | news | 2026-02-20 | [B] |
| <a id="ref-g-11"></a>G-11 | Zama — Zama at FHE.org 2026: Eight Contributions from Taipei | [링크](https://www.zama.org/post/zama-at-fhe-org-2026-eight-contributions-from-taipei) | news | 2026-03-08 | [B] |
| <a id="ref-g-12"></a>G-12 | MEXC Blog — What Is Zama FHE? The $1B Unicorn Bringing Private Smart Contracts | [링크](https://blog.mexc.com/news/what-is-zama-fhe-the-1b-unicorn-bringing-private-smart-contracts-to-ethereum-and-shibarium-2026/) | news | 2026-01 | [C] |
| <a id="ref-g-13"></a>G-13 | Apple Machine Learning Research — Combining Machine Learning and Homomorphic Encryption in the Apple Ecosystem | [링크](https://machinelearning.apple.com/research/homomorphic-encryption) | news | 2024-08 | [A] |
| <a id="ref-g-14"></a>G-14 | Duality Technologies — Securing the Future: Post-Quantum FHE for Zero-Footprint Intelligence | [링크](https://dualitytech.com/blog/securing-the-future-post-quantum-fhe-for-zero-footprint-intelligence/) | news | 2026 | [B] |
| <a id="ref-g-15"></a>G-15 | Market Research Intellect — Global Homomorphic Encryption Market Size and Forecast | [링크](https://www.marketresearchintellect.com/product/global-homomorphic-encryption-market-size-and-forecast/) | news | 2026 | [C] |
| <a id="ref-e-01"></a>E-01 | Niobium Microsystems (Kevin Yoder, CEO) — The Fog 공식 보도자료 및 CEO 발언 | [링크](http://www.prnewswire.com/news-releases/niobium-introduces-the-fog-a-new-encrypted-cloud-platform-for-private-ai-and-data-processing-302732387.html) | IR/발표 | 2026-04-02 | [A] |
| <a id="ref-e-02"></a>E-02 | CryptoLab — HEaaN Zero-Leak RAG GS 1등급 인증 보도자료 (유니콘팩토리) | [링크](https://www.unicornfactory.co.kr/article/2026032614461522253) | IR/발표 | 2026-03-26 | [A] |
| <a id="ref-e-03"></a>E-03 | Intel — Heracles FHE ASIC ISSCC 2026 발표 (Privacy Guides 커버리지) | [링크](https://www.privacyguides.org/news/2026/03/19/intels-fully-homomorphic-encryption-chip-could-revolutionize-privacy/) | IR/발표 | 2026-03-19 | [B] |
| <a id="ref-e-04"></a>E-04 | CryptoLab (정희천 CEO) — CKKS+ 온디바이스 경량화 발언 (The Asia Business Daily 인용) | [링크](https://www.asiae.co.kr/en/article/2026031008212144575) | IR/발표 | 2026-03-10 | [B] |
| <a id="ref-e-05"></a>E-05 | Niobium (Kevin Yoder, CEO) — SemiFive 계약 발언 (Evertiq 인용) | [링크](https://evertiq.com/design/2026-02-20-semifive-secures-design-win-with-niobium-for-fhe-accelerator) | IR/발표 | 2026-02-20 | [B] |
| <a id="ref-g-16"></a>G-16 | The Quantum Insider — Niobium Raises $23M+ to Advance Next-Gen FHE Hardware | [링크](https://thequantuminsider.com/2025/12/03/niobium-23m-fhe-funding/) | news | 2025-12-03 | [B] |
| <a id="ref-g-17"></a>G-17 | IACR ePrint 2026/638 — THED: Threshold Dilithium from FHE (Park, CryptoLab) | [링크](https://eprint.iacr.org/2026/638.pdf) | paper | 2026 | [A] |
| <a id="ref-g-18"></a>G-18 | TipRanks — Niobium Unveils Encrypted Cloud Platform 'The Fog' to Commercialize FHE at Scale | [링크](https://www.tipranks.com/news/private-companies/niobium-unveils-encrypted-cloud-platform-the-fog-to-commercialize-fhe-at-scale) | news | 2026-04-02 | [B] |
| <a id="ref-g-19"></a>G-19 | ITBrief Asia — Niobium taps Samsung for encrypted AI chip production | [링크](https://itbrief.asia/story/niobium-taps-samsung-for-encrypted-ai-chip-production) | news | 2026-02 | [B] |
| <a id="ref-g-20"></a>G-20 | NIST CSRC — THED Slides: Threshold Dilithium from FHE (MPTS 2026) | [링크](https://csrc.nist.gov/csrc/media/presentations/2026/mpts2026-2b4/images-media/mpts2026-2b4-slides-thfhe-ckks-stehle.pdf) | paper | 2026-01-29 | [A] |
