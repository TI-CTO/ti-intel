---
type: deep-research
topic: he-keyword-search
date: 2026-03-18
parent: 2026-03-18_weekly-secure-ai
period: 2026-03-11 ~ 2026-03-18
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
prior_report: 2026-03-11_research-ondevice-he.md
---

# Deep 리서치: On-Device 동형암호 키워드 검색 (2026-W12)

> 기간: 2026-03-11 ~ 2026-03-18

## 기술 동향

1. **DESILO×Cornami GL 스킴 — 5세대 FHE 공식 발표 (FHE.org 2026 타이베이).**
   DESILO 수석과학자 Yongwoo Lee와 FHE 발명자 Craig Gentry(Cornami Chief Scientist)가 3월 8일 FHE.org 2026 컨퍼런스에서 "GL" 스킴을 발표했다. GL은 LLM의 핵심 연산인 행렬 곱셈을 FHE 상태에서 재설계한 5세대 FHE 프레임워크다. 이전 발표(2025년 11월)에서 확인된 80× 암호화 행렬 곱셈 가속 대비, 이번 FHE.org 발표에서는 Private AI — 즉 프롬프트·입력·출력이 암호화된 상태로 LLM이 추론하는 구조 — 를 실증 시연했다. Gentry는 "GL 스킴으로 암호화 행렬 연산의 근본적 구조를 재설계해, 현대 AI 아키텍처 지원에 한 단계 더 가까워졌다"고 발언했다. [[G-01]](#ref-g-01), [[E-01]](#ref-e-01)

2. **Intel Heracles FHE ASIC — ISSCC 2026에서 3nm 칩 실물 시연.**
   Intel이 2월 ISSCC 2026(샌프란시스코)에서 Heracles FHE 전용 ASIC을 실물 데모했다. 3nm FinFET(Intel 3 공정), 197mm² 다이, 176W TDP, 48GB HBM3(819 GB/s 대역폭). 8192-way SIMD 엔진으로 BGV·BFV·CKKS 세 스킴을 지원하며, 24코어 Intel Xeon 대비 **1,074~5,547배 빠른** FHE 처리 성능을 달성한다. DARPA 5년 프로그램의 결과물로, 오픈소스 컴파일러 SDK(Polynomial ISA)를 GitHub에 공개했다. 3월 10일 IEEE Spectrum이 상세 기술 분석 기사를 게재하며 업계 주목을 받았다. [[G-02]](#ref-g-02), [[G-03]](#ref-g-03)

3. **클라이언트-사이드 FHE 연산 최적화 — FPGA·ASIC 76배 가속 논문 발표 (EuroS&P).**
   Graz University of Technology의 Aikata et al.이 3월 15일 ePrint 2026/515에 게재한 논문 "Privacy at your Fingertips"에서 클라이언트 측 FHE 암호화·복호화를 **부트스트래핑으로 재구성**하는 방법론을 제안했다. 결과: 암호화·복호화 연산량 97% 감소, 통신 오버헤드 97% 감소. FPGA 프로토타입 및 ASIC 합성에서 **선행 연구 대비 76배 속도 향상**. 마이크로컨트롤러(임베디드) 구현도 포함해 온디바이스 적용 가능성을 직접 검증했다. 키워드 검색용 PIR 클라이언트의 연산 부담 해소에 직접 응용 가능하다. [[P-01]](#ref-p-01)

4. **FHE.org 2026 컨퍼런스 — 10편 논문·23편 포스터 발표, 타이베이 개최.**
   3월 8일 타이베이 마리어트에서 Real World Crypto 2026과 공동 개최된 FHE.org 2026 컨퍼런스에서 총 10개의 구두 발표와 23개의 포스터가 수용됐다. GL 스킴 발표 외에 Zama의 TFHE·ZHEnith·Nexus 묶음 표준 제안, Apple의 on-device PIR 개선, 그리고 FHE Hardware Day에서 소개된 오픈소스 HPU(FPGA 기반 TFHE 가속기) 등이 발표됐다. 이 컨퍼런스는 산학 FHE 동향을 집약하는 연간 기준점으로 자리잡았다. [[G-04]](#ref-g-04)

5. **NIST Threshold Call — FHE 표준화 검토 기간 확정.**
   NIST가 1월 20일 NISTIR 8214C(Final)를 공개하면서, FHE 포함 S5 카테고리 미리보기 제출 마감을 **2026년 4월 20일**로 확정했다. 이 시점 이후 FHE 제안서 공개 검토가 개시된다. Zama(TFHE/ZHEnith/Nexus), CryptoLab(Threshold CKKS)이 제출을 공개 선언한 상태다. [[G-05]](#ref-g-05)

6. **HomomorphicEncryption.org 9차 표준화 회의 — LG사이언스파크 서울 개최.**
   3월 5~6일 서울 LG사이언스파크 ISC 빌딩에서 9번째 HE 표준화 회의가 열렸다. LG유플러스·CryptoLab 홈 그라운드에서 열린 이 회의는 CKKS 기반 파라미터 선택·키 관리 표준안 논의를 중심으로 진행됐다. ISO·NIST 양 트랙 진행 상황이 함께 공유됐다. [[G-06]](#ref-g-06)

7. **Mirror Security×NVIDIA — GPU 가속 FHE AI 추론 인프라 출시.**
   Mirror Security(아일랜드)가 NVIDIA CUDA·cuBLAS·NeMo·TensorRT-LLM을 활용한 GPU 가속 FHE 추론 플랫폼을 출시했다. 데이터가 추론 전 과정에서 복호화되지 않는 "Secure AI Inference + Secure AI Memory" 구조를 구현했으며, 정부·의료·금융 등 규제 산업을 주요 타깃으로 삼는다. 2025년 12월 Intel과 €2.1M 공동연구 계약 이후 후속 행보다. [[G-07]](#ref-g-07), [[E-02]](#ref-e-02)

8. **키워드 PIR 연구 가속 — HET-PIR·BCPIR 논문 2편 연속 발표.**
   동형암호 기반 키워드 PIR 분야에서 두 편의 주목할 논문이 연속 발표됐다. HET-PIR(Cybersecurity/Springer)는 FHE 기반 동치 테스트 알고리즘을 최적화해 단일 서버 키워드 PIR을 실용적 수준으로 구현했다. BCPIR(Springer LNCS)는 블록 코드 기반 코드워드를 사용해 키워드 PIR의 통신 복잡도를 추가로 감소시켰다. 두 논문 모두 온디바이스 클라이언트가 서버에 검색어를 노출하지 않고 암호화 상태로 조회하는 핵심 기술 경로를 확장한다. [[P-02]](#ref-p-02), [[P-03]](#ref-p-03)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| DESILO (한국) | Craig Gentry와 공동 개발한 5세대 GL FHE 스킴을 FHE.org 2026 타이베이에서 공식 발표 (3월 7~8일). Private AI(암호화 LLM 추론) 데모 시연. IACR ePrint 2025/1935 논문 공개. | [[G-01]](#ref-g-01), [[E-01]](#ref-e-01) |
| Cornami (미국) | Craig Gentry Chief Scientist로서 GL 스킴 공동 저자. FHE 기반 LLM PCMM(Plaintext-Ciphertext Matrix Multiplication) 상용화 추진 중. Niobium과 무관하게 자체 실시간 FHE 칩 개발 병행 | [[G-01]](#ref-g-01) |
| Intel (미국) | Heracles FHE ASIC을 ISSCC 2026에서 실물 시연. 3nm, 5,547× 성능, CKKS 포함 3대 스킴 지원. 오픈소스 컴파일러 SDK 공개. 양산 일정 미공개 | [[G-02]](#ref-g-02), [[G-03]](#ref-g-03) |
| Niobium + SEMIFIVE + Samsung Foundry (미국·한국) | 2월 19일 발표된 계약(100억 원, Samsung 8nm 8LPU)으로 세계 최초 상용 FHE ASIC 설계 진행 중. 이번 주 추가 발표 없음 — 설계 진행 단계 | [[G-08]](#ref-g-08), [[E-03]](#ref-e-03) |
| Mirror Security (아일랜드) | NVIDIA 협력으로 GPU 가속 FHE 추론 플랫폼 출시. Intel과 €2.1M 공동연구 병행. 헬스케어·금융·정부 시장 공략 | [[G-07]](#ref-g-07), [[E-02]](#ref-e-02) |
| CryptoLab (한국) | CKKS+ (4.5세대) 상용화 계속 진행 중. 9차 HE 표준화 회의 주최지(LG사이언스파크)와 연계. LG유플러스 AICC PoC 지속. 이번 주 신규 플래그십 발표 없음 | [[G-06]](#ref-g-06) |
| Zama (프랑스) | FHE.org 2026에서 TFHE·ZHEnith·Nexus 3종 NIST 제출 패키지 공개 발표. 오픈소스 HPU(FPGA TFHE 가속기) 출시. NIST 4월 20일 마감 준비 중 | [[G-05]](#ref-g-05), [[G-09]](#ref-g-09) |
| Apple (미국) | swift-homomorphic-encryption 라이브러리(BFV 기반 SWHE) 유지. iOS 18 Live Caller ID에 PIR 적용. on-device 완전 FHE는 하드웨어 가속 이후로 유보 중 | [[G-10]](#ref-g-10) |

---

## 시장 시그널

- FHE.org 2026(타이베이, 3월 8일)에서 하드웨어·소프트웨어·표준화 3개 트랙이 동시에 성숙 단계로 진입했음을 확인. "컨퍼런스 규모 > 행사 > 워크숍" 수준으로 격상 [B]
- Intel Heracles(ISSCC), Niobium ASIC 설계 착수, Mirror Security NVIDIA 협력이 **같은 분기 내** 발표되며 FHE 하드웨어 가속이 기술 레이스 구도로 전환
- Private AI 프레임 부상: "암호화 추론" → "암호화된 데이터에서 직접 LLM 서비스" 방향으로 시장 내러티브가 이동. DESILO GL 스킴이 이 전환점의 기술적 근거 제공
- 키워드 검색·PIR 전용 논문(HET-PIR, BCPIR)이 주요 학술지에 게재되며, **온디바이스 암호화 검색**이 이론에서 구현 단계로 이행 중
- NIST Threshold Call 4월 마감이 임박하면서 표준화 불확실성 리스크가 단기 내 해소 시작 전망. 이후 6~12개월 내 초안 공개 예상
- 동형암호 글로벌 시장 2026년 기준 약 1.2억~12억 달러(추정치, 기관별 편차 큼) [C] [[G-11]](#ref-g-11)
- 한국 생태계 — CryptoLab·DESILO·Samsung Foundry·LG유플러스가 FHE 핵심 공급망에 동시 참여하며 글로벌 FHE 공급망 내 한국 비중 확대 중

---

## 학술 동향 (주요 논문)

**이번 주 주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| "Privacy at your Fingertips: Enabling Rapid Client-Side Operations in FHE" (Aikata et al., Graz Univ. of Tech., 2026) | 부트스트래핑으로 클라이언트 FHE 연산을 재설계. 암호화·복호화 97% 경량화, FPGA/ASIC에서 76× 가속. EuroS&P 2026 게재. 임베디드·온디바이스 PIR 클라이언트 직접 응용 가능 | [[P-01]](#ref-p-01) |
| "HET-PIR: practical Keyword PIR via a Novel homomorphic equality test Algorithm" (2026) | FHE 동치 테스트 최적화로 단일 서버 키워드 PIR 실용화. 1라운드 프로토콜로 암호화 DB 쿼리 지원. Cybersecurity/Springer 게재 | [[P-02]](#ref-p-02) |
| "BCPIR: More Efficient Keyword PIR via Block Building Codewords" (2026) | 블록 코드 기반 코드워드로 키워드 PIR 통신 복잡도 추가 감소. Springer LNCS 게재 | [[P-03]](#ref-p-03) |
| "GL FHE Scheme for Private AI" (Lee & Gentry, DESILO·Cornami, 2026) | 5세대 FHE 행렬 곱셈 재설계. LLM 암호화 추론 지원. FHE.org 2026 발표. IACR ePrint 2025/1935 | [[P-04]](#ref-p-04) |
| "FHECore: Rethinking GPU Microarchitecture for FHE" (BU·Northeastern·KAIST·Univ. Murcia, 2026) | GPU 마이크로아키텍처를 FHE에 최적화. CKKS 동적 명령 수 2.41× 감소, 부트스트래핑 지연 50% 단축 | [[P-05]](#ref-p-05) |

---

## 전략적 시사점

**기회**

- Intel Heracles(ASIC, 5,547×)·Niobium(8nm ASIC)·Mirror Security(GPU 가속) 3자가 같은 분기에 FHE 하드웨어를 상업화 레인으로 진입시키고 있어, **에지-서버 하이브리드 FHE 키워드 검색** 아키텍처의 현실성이 급격히 높아지고 있다
- HET-PIR·BCPIR·Aikata et al. 논문이 동시에 발표된 것은 키워드 PIR 분야가 "구현 최적화" 단계에 진입했음을 의미. 1~2년 내 라이브러리 통합 및 상용 SDK 등장 가능성이 높다
- NIST 표준화 4월 마감 이후 FHE 파라미터 표준이 확정되면, 상호운용성 기반의 **암호화 검색 SaaS/SDK 시장**이 개화할 수 있다

**위협**

- Intel Heracles의 상용 양산 일정·가격이 미공개 상태. "시연용 칩"과 "상용 제품" 사이의 간극이 클 경우 FHE 하드웨어 시장 진입이 2~3년 지연될 수 있다
- GL 스킴·FHECore 등 5세대 기술이 빠르게 등장하면서, 현재 CKKS 기반 구현(CryptoLab HEaaN 포함)의 **기술 교체 주기**가 예상보다 빨라질 수 있다 — 스택 전환 비용 리스크
- 온디바이스 키워드 검색에서 FHE는 여전히 평문 대비 10³~10⁵배 연산 부담. Aikata et al.의 97% 경량화는 **클라이언트 측 암호화/복호화** 최적화이며, 서버 측 동형 연산 비용은 별개 문제다
- Apple이 SWHE(부분 동형암호)로 PIR 서비스를 이미 운영 중이어서, 스마트폰 제조사 주도 on-device 프라이버시 검색이 표준화 전에 사실상 표준(de facto)으로 굳어질 위험이 있다

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | PR Newswire — DESILO and FHE Inventor Craig Gentry Introduce 5th-Generation "GL" FHE Scheme for Private AI | [링크](https://www.prnewswire.com/news-releases/desilo-and-fhe-inventor-craig-gentry-introduce-5th-generation-gl-fhe-scheme-for-private-ai-302707060.html) | news | 2026-03-07 | [A] |
| <a id="ref-g-02"></a>G-02 | IEEE Spectrum — Intel's Heracles Chip Speeds Up FHE Computing | [링크](https://spectrum.ieee.org/fhe-intel) | news | 2026-03-10 | [B] |
| <a id="ref-g-03"></a>G-03 | Tom's Hardware — Intel's Heracles chip computes fully-encrypted data: 1,074~5,547× faster than Xeon | [링크](https://www.tomshardware.com/tech-industry/cyber-security/intels-heracles-chip-computes-fully-encrypted-data-without-decrypting-it-chip-is-1-074-to-5-547-times-faster-than-a-24-core-intel-xeon-in-fhe-math-operations) | news | 2026-03-10 | [B] |
| <a id="ref-g-04"></a>G-04 | FHE.org — FHE.org 2026 Conference (Taipei, March 8) | [링크](https://fhe.org/conferences/conference-2026/) | news | 2026-03-08 | [A] |
| <a id="ref-g-05"></a>G-05 | NIST CSRC — Multi-Party Threshold Cryptography / NISTIR 8214C Final | [링크](https://csrc.nist.gov/projects/threshold-cryptography) | news | 2026-01-20 | [A] |
| <a id="ref-g-06"></a>G-06 | HomomorphicEncryption.org — 9th HE Standards Meeting (Seoul, LG Sciencepark, Mar 5-6) | [링크](https://homomorphicencryption.org/9th-homomorphicencryption-org-standards-meeting/) | news | 2026-03-05 | [A] |
| <a id="ref-g-07"></a>G-07 | startupnews.fyi — Mirror Security Teams Up With NVIDIA for Encrypted AI | [링크](https://startupnews.fyi/2026/02/18/mirror-security-nvidia-encrypted-ai/) | news | 2026-02-18 | [B] |
| <a id="ref-g-08"></a>G-08 | PR Newswire — SEMIFIVE Partners with Niobium to Develop FHE Accelerator (Samsung 8nm) | [링크](https://www.prnewswire.com/news-releases/semifive-partners-with-niobium-to-develop-fhe-accelerator-driving-us-market-expansion-302692312.html) | news | 2026-02-19 | [A] |
| <a id="ref-g-09"></a>G-09 | Zama — Announcing HPU on FPGA: The First Open-source Hardware Accelerator for FHE | [링크](https://www.zama.org/post/announcing-hpu-on-fpga-the-first-open-source-hardware-accelerator-for-fhe) | news | 2026-02-01 | [A] |
| <a id="ref-g-10"></a>G-10 | Apple Machine Learning Research — Combining Machine Learning and Homomorphic Encryption in the Apple Ecosystem | [링크](https://machinelearning.apple.com/research/homomorphic-encryption) | news | 2024-08-01 | [A] |
| <a id="ref-g-11"></a>G-11 | OpenPR — Homomorphic Encryption Market USD 1.2B (2026) to USD 8.4B (2033) | [링크](https://www.openpr.com/news/4230086/homomorphic-encryption-market-by-type-and-application-rapid) | news | 2026-01-01 | [C] |
| <a id="ref-e-01"></a>E-01 | Craig Gentry (Cornami) · Yongwoo Lee (DESILO) — GL Scheme FHE.org 2026 발표 및 공식 보도자료 인용 | [링크](https://www.prnewswire.com/news-releases/desilo-and-fhe-inventor-craig-gentry-introduce-5th-generation-gl-fhe-scheme-for-private-ai-302707060.html) | IR/발표 | 2026-03-07 | [A] |
| <a id="ref-e-02"></a>E-02 | Mirror Security — Mirror Security and NVIDIA Collaborate to Power Encrypted AI Inference | [링크](https://cxotoday.com/media-coverage/mirror-security-and-nvidia-collaborate-to-power-encrypted-ai-inference-using-nvidia-accelerated-computing/) | IR/발표 | 2026-02-18 | [A] |
| <a id="ref-e-03"></a>E-03 | Niobium CEO Kevin Yoder · SEMIFIVE CEO Brandon Cho · Samsung Electronics VP Taejoong Song — FHE ASIC 파트너십 공식 발언 | [링크](https://www.prnewswire.com/news-releases/semifive-partners-with-niobium-to-develop-fhe-accelerator-driving-us-market-expansion-302692312.html) | IR/발표 | 2026-02-19 | [A] |
| <a id="ref-p-01"></a>P-01 | Aikata, Krieger, Sinha Roy (Graz Univ. of Tech.) — Privacy at your Fingertips: Enabling Rapid Client-Side Operations in FHE | [링크](https://eprint.iacr.org/2026/515) | paper | 2026-03-15 | [A] |
| <a id="ref-p-02"></a>P-02 | HET-PIR — practical Keyword PIR via a Novel homomorphic equality test Algorithm | [링크](https://link.springer.com/article/10.1186/s42400-025-00506-x) | paper | 2026-01-01 | [A] |
| <a id="ref-p-03"></a>P-03 | BCPIR — More Efficient Keyword PIR via Block Building Codewords | [링크](https://link.springer.com/chapter/10.1007/978-3-031-94445-1_9) | paper | 2026-01-01 | [A] |
| <a id="ref-p-04"></a>P-04 | Lee & Gentry (DESILO · Cornami) — GL FHE Scheme for Private AI (IACR ePrint 2025/1935) | [링크](https://eprint.iacr.org/2025/1935) | paper | 2026-03-07 | [A] |
| <a id="ref-p-05"></a>P-05 | BU · Northeastern · KAIST · Univ. Murcia — FHECore: Rethinking GPU Microarchitecture for Fully Homomorphic Encryption | [링크](https://semiengineering.com/a-gpu-microarchitecture-optimized-for-fully-homomorphic-encryption/) | paper | 2026-02-01 | [A] |
| <a id="ref-g-12"></a>G-12 | EU-Startups — Mirror Security secures €2.1M with Intel for FHE-based AI security | [링크](https://www.eu-startups.com/2025/12/ucd-spin-out-mirror-security-secures-e2-1-million-to-advance-fhe-based-ai-security-in-collaboration-with-intel/) | news | 2025-12-01 | [B] |
| <a id="ref-g-13"></a>G-13 | NIST CSRC — MPTS 2026: Workshop on Multi-Party Threshold Schemes (Jan 27, 2026) | [링크](https://csrc.nist.gov/events/2026/mpts2026) | news | 2026-01-27 | [A] |
| <a id="ref-g-14"></a>G-14 | FHEorg Substack Digest #38 — FHE.org 2026 Conference, Upcoming Events, Latest Updates | [링크](https://fheorg.substack.com/p/fheorg-digest-38-fheorg-2026-conference) | news | 2026-03-01 | [B] |
| <a id="ref-g-15"></a>G-15 | GitHub — IntelLabs/encrypted-computing-sdk (Heracles Polynomial ISA open-source SDK) | [링크](https://github.com/IntelLabs/encrypted-computing-sdk) | news | 2026-03-01 | [A] |
