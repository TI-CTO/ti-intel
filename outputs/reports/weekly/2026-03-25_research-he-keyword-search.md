---
type: weekly-research
topic: he-keyword-search
date: 2026-03-25
period: 2026-03-18 ~ 2026-03-25
agent: research-deep
confidence: high
status: completed
sources_used: [websearch]
prior_report: 2026-03-18_research-he-keyword-search.md
---

# Deep 리서치: On-Device 동형암호 — 키워드 검색 (2026-W13)

> 기간: 2026-03-18 ~ 2026-03-25

## 기술 동향

1. **Intel Heracles 커버리지 지속 확산 — Privacy Guides, Tom's Hardware 등 일반 기술 미디어로 확장 (3/19).**
   3월 19일 Privacy Guides가 "Intel's Fully Homomorphic Encryption Chip Could Revolutionize Privacy"를 게재하며 Heracles가 보안·프라이버시 커뮤니티 주류 미디어에 노출됐다. 5년 전 DARPA Data Protection in Virtual Environments (DRIVE) 프로그램에서 시작된 칩이 E2EE 서버 측 연산 가능성을 열 수 있다는 시각으로 분석됐다. 8,192-way SIMD 엔진, 3nm FinFET(Intel 3 공정), 197mm², 176W TDP, 48GB HBM3(819 GB/s)의 기술 사양이 일반 독자용으로 정리·전파됐다. Tom's Hardware 기사(1,074~5,547× Xeon 대비 가속)도 동일 주간에 재인용됐다. [[G-01]](#ref-g-01), [[G-02]](#ref-g-02)

2. **UTS — 세계 최초 FHE 기반 딥강화학습(DRL) 프레임워크, Nature Machine Intelligence 게재 (3/18).**
   호주 기술대학교 (University of Technology Sydney, UTS) Associate Professor Hoang Dinh 팀이 완전 동형암호(FHE) 상태에서 딥강화학습을 가능하게 하는 프레임워크를 Nature Machine Intelligence에 발표했다(3월 18일). 핵심 기술 혁신은 역제곱근(inverse square root) 고차 다항식 근사 없이 동작하는 HE 호환 Adam 옵티마이저 설계다. 암호화 DRL 모델이 비암호화 기준 대비 **10% 이내** 성능 격차를 유지한다. 공동연구자: Meta AI Research Dr. Kristin Lauter, 한양대 Associate Professor Miran Kim. 이 결과는 암호화 데이터에서 AI 에이전트가 학습·추론할 수 있음을 처음 실증한 것으로, 온디바이스 프라이버시 보존 AI의 핵심 기반 기술에 해당한다. [[G-03]](#ref-g-03), [[G-04]](#ref-g-04), [[P-01]](#ref-p-01)

3. **FHECore — GPU FHE 전용 마이크로아키텍처, BU/Northeastern/KAIST/Murcia 공동 발표 (arXiv 2602.22229).**
   2월 발표 후 3월 이후 커버리지 확산. Boston University, Northeastern University, KAIST, University of Murcia의 공동 연구진이 GPU Streaming Multiprocessor에 FHE 전용 연산 유닛(FHECore)을 통합하는 마이크로아키텍처를 제안했다. Semiengineering이 3월 중순 상세 기술 분석 기사를 게재했다. 수치 이론 변환(Number Theoretic Transform, NTT)과 기저 변환(Base Conversion)을 단일 wide-precision 모듈 연산 하드웨어로 통합 처리한다. CKKS 기본 연산에서 명령어 수 기하평균 2.41× 감소, 엔드투엔드 성능 최대 2.12× 향상, 부트스트래핑 지연 50% 감소, 면적 오버헤드 2.4%. [[G-05]](#ref-g-05), [[P-02]](#ref-p-02)

4. **CUDA GPU FHE 벤치마크 — Jetson Nano 부적합, 소비자급 GPU 가능성 확인 (MDPI 게재).**
   MDPI Big Data and Cognitive Computing 저널이 3월 중 "Feasibility Study of CUDA-Accelerated Homomorphic Encryption and Benchmarking on Consumer-Grade and Embedded GPUs"를 게재했다. GTX 1650 Ti(노트북), RTX 4060(서버), Jetson Nano 2GB(엣지)를 비교 벤치마크한 결과: Jetson Nano는 Maxwell GPU 아키텍처의 64비트 정수 비호환성과 메모리 부족으로 FHE 연산에 부적합한 것으로 판정됐다. 소비자급 GPU에서는 FHE 연산 실행 가능성이 확인됐으며, CPU 전용 대비 유의미한 가속이 관측됐다. 온디바이스 HE 키워드 검색의 엣지 적용 가능성 범위를 제한하는 중요한 실증 데이터다. [[G-06]](#ref-g-06), [[P-03]](#ref-p-03)

5. **IACR — Vinod Vaikuntanathan MIT 교수, FHE 공헌으로 IACR Fellows 선정 (3/23).**
   국제암호학연구협회(International Association for Cryptologic Research, IACR)가 3월 23일 2026년 IACR Fellows를 발표했다. MIT의 Vinod Vaikuntanathan 교수가 FHE, 보안 다자간 계산(Secure Multi-Party Computation), 양자 암호학, 정보 이론 암호학에 대한 근본적 기여로 선정됐다. Vaikuntanathan은 학습 오류(Learning With Errors, LWE) 기반 FHE 이론의 핵심 설계자 중 한 명으로, 이번 선정은 FHE 학술 커뮤니티의 위상 강화를 상징한다. [[G-07]](#ref-g-07)

6. **PIR(프라이빗 정보 검색) — EUROCRYPT 2026 논문, FHE 기반 준선형 서버 시간 달성.**
   Alexandra Henzinger와 Seyoon Ragavan이 EUROCRYPT 2026에 채택된 "Two-Server PIR in Sublinear Time and Quasilinear Space"에서 압축 선형 동형암호를 활용해 통신 복잡도를 n^0.31 × poly(lambda) 수준으로 낮추는 데 성공했다. 임의의 상수 서버 수를 가진 정보 이론적 PIR 중 **최초로** 준선형 서버 저장 공간과 다항식 준선형 서버 시간을 동시 달성한다. HE 기반 키워드 PIR의 이론적 효율성 상한을 끌어올리는 기초 연구다. [[G-08]](#ref-g-08)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| Intel (미국) | Heracles FHE ASIC 보도 지속 확산. Privacy Guides(3/19), Tom's Hardware 등 일반 기술 미디어 커버리지 추가. 양산 일정 미발표 상태. DARPA DRIVE 프로그램 기원 서사 강조 | [[G-01]](#ref-g-01), [[G-02]](#ref-g-02) |
| LG유플러스 + CryptoLab (한국) | MWC 2026(바르셀로나, 3/4)에서 ixi-O AI 에이전트 및 AICC(AI Contact Center)에 동형암호 탑재 협력 발표. 해킹·데이터 유출 시에도 개인정보 암호화 상태 유지. CryptoLab은 CKKS 4세대 원천 특허 보유 | [[G-09]](#ref-g-09), [[E-01]](#ref-e-01), [[E-02]](#ref-e-02) |
| CryptoLab + UClone (한국·미국) | 2025년 4월 발표된 파트너십이 이번 주 재조명. Encrypted Vector Search(ES2) for Retrieval-Augmented Generation(RAG)을 UClone AI 에이전트 플랫폼에 통합. 소비자 대상 FHE 구동 AI 에이전트 최초 상용 사례로 업계 인용 지속 | [[G-10]](#ref-g-10) |
| Niobium + SEMIFIVE + Samsung Foundry (미국·한국) | 2월 19일 발표된 FHE ASIC 계약(100억 원, Samsung 8nm 8LPU) 이후 이번 주 추가 발표 없음. 설계 진행 단계. 세계 최초 상용 FHE 가속기 목표 | [[G-11]](#ref-g-11) |
| Axelera AI + Kudelski Labs (네덜란드·스위스) | Europa Edge AI 칩에 Kudelski Secure Enclave (KSE3) 통합 발표. PQC(후양자암호, ML-KEM·ML-DSA) 탑재, SESIP/PSA Level 3 목표. HE 직접 탑재는 아니나 FHE ASIC 설계 시 참조 사례. Cyber Resilience Act (CRA) 중요 제품 분류 대응 | [[G-12]](#ref-g-12), [[E-03]](#ref-e-03) |
| Zama (프랑스) | FHE.org 2026(3/8, 타이베이)에서 8편 기여(3편 구두 발표 + 5편 포스터). TFHE 부트스트래핑 가속, FHE 랜덤화, 암호화 행렬 검증 가능 연산 발표. NIST 제출 패키지 준비 중 | [[G-13]](#ref-g-13), [[E-04]](#ref-e-04) |
| UTS (호주) | FHE 기반 DRL 프레임워크를 Nature Machine Intelligence에 게재(3/18). Meta AI Research·한양대와 공동 연구. 암호화 상태 AI 학습의 첫 실증. 성능 격차 10% 이내 | [[G-03]](#ref-g-03), [[P-01]](#ref-p-01) |

---

## 시장 시그널

**파트너십 & 제휴**

- LG유플러스 + CryptoLab: MWC 2026에서 ixi-O AI 에이전트 및 AICC에 동형암호 적용 협력 공식 발표. CKKS 기반 암호화 AI 서비스의 국내 통신사 최초 상용화 경로 [[G-09]](#ref-g-09), [[E-01]](#ref-e-01)
- Axelera AI + Kudelski Labs: Europa 엣지 AI 칩에 양자 저항 암호 보안 IP 통합. FHE 직접 채택은 아니나 엣지 보안 반도체 설계에서 HE 계층 통합 트렌드의 선행 사례 [[G-12]](#ref-g-12)
- Niobium + SEMIFIVE + Samsung Foundry: 세계 최초 상용 FHE ASIC 양산 계약(2/19 발표). Samsung 8nm 공정, 설계 진행 중 [[G-11]](#ref-g-11)

**시장 전망**

- HE 시장 규모 추정: 2026년 기준 USD 0.31B~1.2B(복수 리서치사, 방법론 차이로 범위 큼) [[G-14]](#ref-g-14), [[G-15]](#ref-g-15)
- 2033~2035년 전망: USD 1.3B~8.4B, CAGR 20~30% [[G-14]](#ref-g-14), [[G-15]](#ref-g-15) [단일 소스 외 교차 미검증, 수치 활용 시 주의 필요]
- FHE 스타트업 8개사 누적 투자 합계 USD 278.9M(평균 USD 34.9M/사). Zama $57M Series B(유니콘, 기업가치 $1B+) [[G-16]](#ref-g-16)
- Fortune 1000 기업 중 38% 이상이 HE 기반 암호화 데이터 협업 파일럿 개시 [출처: 시장 리서치사 보고, [C] 등급] [[G-14]](#ref-g-14)

**연구 동향**

- "Empowering AI with Homomorphic Encryption for Secure DRL" (Nguyen et al., 2025/2026) — FHE 상태 DRL 세계 최초 실증. 성능 격차 10% 이내. [[P-01]](#ref-p-01)
- "FHECore: Rethinking GPU Microarchitecture for FHE" (BU/Northeastern/KAIST/Murcia, 2026) — GPU SM에 FHE 전용 유닛 통합. CKKS 2.41× 명령어 감소, 부트스트래핑 50% 감소. [[P-02]](#ref-p-02)
- "Feasibility Study of CUDA-Accelerated HE on Consumer-Grade and Embedded GPUs" (MDPI, 2026) — Jetson Nano 부적합 판정. 소비자급 GPU 가능성 확인. [[P-03]](#ref-p-03)
- "Two-Server PIR in Sublinear Time and Quasilinear Space" (Henzinger & Ragavan, EUROCRYPT 2026) — 압축 선형 동형암호 활용, 통신 복잡도 n^0.31 달성. [[G-08]](#ref-g-08)

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Privacy Guides — Intel's Fully Homomorphic Encryption Chip Could Revolutionize Privacy | [링크](https://www.privacyguides.org/news/2026/03/19/intels-fully-homomorphic-encryption-chip-could-revolutionize-privacy/) | news | 2026-03-19 | [B] |
| <a id="ref-g-02"></a>G-02 | Tom's Hardware — Intel's Heracles chip computes fully-encrypted data without decrypting it | [링크](https://www.tomshardware.com/tech-industry/cyber-security/intels-heracles-chip-computes-fully-encrypted-data-without-decrypting-it-chip-is-1-074-to-5-547-times-faster-than-a-24-core-intel-xeon-in-fhe-math-operations) | news | 2026-03-18 | [B] |
| <a id="ref-g-03"></a>G-03 | UTS News — UTS researchers achieve breakthrough in privacy-preserving AI | [링크](https://www.uts.edu.au/news/2026/03/uts-researchers-achieve-breakthrough-in-privacy-preserving-ai) | news | 2026-03-18 | [A] |
| <a id="ref-g-04"></a>G-04 | Xinhua — Researchers in Australia unveil privacy-preserving AI that learns on encrypted data | [링크](https://english.news.cn/20260318/48ad5edb8fd6425a85eeb03f3ad93df4/c.html) | news | 2026-03-18 | [B] |
| <a id="ref-g-05"></a>G-05 | Semiengineering — A GPU Microarchitecture Optimized for Fully Homomorphic Encryption | [링크](https://semiengineering.com/a-gpu-microarchitecture-optimized-for-fully-homomorphic-encryption/) | news | 2026-03-18 | [B] |
| <a id="ref-g-06"></a>G-06 | MDPI Big Data Cogn. Comput. — Feasibility Study of CUDA-Accelerated HE and Benchmarking on Consumer-Grade and Embedded GPUs | [링크](https://www.mdpi.com/2504-2289/10/3/79) | paper | 2026-03 | [A] |
| <a id="ref-g-07"></a>G-07 | IACR — News item: 23 March 2026 (Vinod Vaikuntanathan Fellow) | [링크](https://iacr.org/news/item/28062) | news | 2026-03-23 | [A] |
| <a id="ref-g-08"></a>G-08 | GitHub — finite-diffs-pir: Two-Server PIR (EUROCRYPT 2026) | [링크](https://github.com/ahenzinger/finite-diffs-pir) | paper | 2026-03 | [A] |
| <a id="ref-g-09"></a>G-09 | Asia Business Daily — LG Uplus and Cryptolab Aim to Block Hacking Risks with Homomorphic Encryption (MWC26) | [링크](https://www.asiae.co.kr/en/article/2026031008212144575) | news | 2026-03-10 | [B] |
| <a id="ref-g-10"></a>G-10 | PRNewswire — CryptoLab and UClone Partner to Bring First FHE-Powered AI Agents to Consumers | [링크](https://www.prnewswire.com/news-releases/cryptolab-and-uclone-partner-to-bring-first-fully-homomorphic-encryption-powered-ai-agents-to-consumers-302439395.html) | news | 2025-04-28 | [A] |
| <a id="ref-g-11"></a>G-11 | PRNewswire — SEMIFIVE Partners with Niobium to Develop FHE Accelerator | [링크](https://www.prnewswire.com/news-releases/semifive-partners-with-niobium-to-develop-fhe-accelerator-driving-us-market-expansion-302692312.html) | news | 2026-02-19 | [A] |
| <a id="ref-g-12"></a>G-12 | Electronics Weekly — Axelera AI, Kudelski Labs collaborate for secure Edge AI | [링크](https://www.electronicsweekly.com/news/products/software-products/embedded-axelera-ai-kudelski-labs-collaborate-for-secure-edge-ai-processing-2026-03/) | news | 2026-03 | [B] |
| <a id="ref-g-13"></a>G-13 | Zama — Zama at FHE.org 2026: Eight Contributions from Taipei | [링크](https://www.zama.org/post/zama-at-fhe-org-2026-eight-contributions-from-taipei) | news | 2026-03-08 | [A] |
| <a id="ref-g-14"></a>G-14 | OpenPR — Homomorphic Encryption Market: Rapid Growth Projected from USD 1.2B (2026) to USD 8.4B (2033) | [링크](https://www.openpr.com/news/4230086/homomorphic-encryption-market-by-type-and-application-rapid) | news | 2026 | [C] |
| <a id="ref-g-15"></a>G-15 | Business Research Insights — Homomorphic Encryption Market Size, 2026 Share | [링크](https://www.businessresearchinsights.com/market-reports/homomorphic-encryption-market-117172) | report | 2026 | [C] |
| <a id="ref-g-16"></a>G-16 | The Quantum Insider — Niobium Raises $23M+ to Advance Next-Gen FHE Hardware | [링크](https://thequantuminsider.com/2025/12/03/niobium-23m-fhe-funding/) | news | 2025-12-03 | [B] |
| <a id="ref-p-01"></a>P-01 | Nguyen et al. — Empowering Artificial Intelligence with Homomorphic Encryption for Secure Deep Reinforcement Learning | [링크](https://www.nature.com/articles/s42256-025-01135-2) | paper | 2026-03-18 | [A] |
| <a id="ref-p-02"></a>P-02 | Jiang et al. — FHECore: Rethinking GPU Microarchitecture for Fully Homomorphic Encryption (arXiv:2602.22229) | [링크](https://arxiv.org/abs/2602.22229) | paper | 2026-02 | [A] |
| <a id="ref-p-03"></a>P-03 | MDPI — Feasibility Study of CUDA-Accelerated Homomorphic Encryption and Benchmarking on Consumer-Grade and Embedded GPUs | [링크](https://www.mdpi.com/2504-2289/10/3/79) | paper | 2026-03 | [A] |
| <a id="ref-e-01"></a>E-01 | LG유플러스 보도자료 — Korea IT Times: LG Uplus Unveils AI, Homomorphic Encryption and Quantum-Resistant Security Technologies at MWC26 | [링크](https://www.koreaittimes.com/news/articleView.html?idxno=151253) | IR/발표 | 2026-03-10 | [A] |
| <a id="ref-e-02"></a>E-02 | Korea IT Times — LG Uplus Unveils Proactive AI ixi-O pro at MWC 2026 | [링크](https://www.koreaittimes.com/news/articleView.html?idxno=151339) | IR/발표 | 2026-03-10 | [A] |
| <a id="ref-e-03"></a>E-03 | EQS News — Axelera AI Adds Kudelski Labs Security IP to Europa Chip | [링크](https://www.eqs-news.com/news/corporate/axelera-ai-adds-kudelski-labs-security-ip-to-europa-chip-to-enable-secure-high-performance-edge-ai/f12fc9c7-71d6-4462-b542-b18f0637e468_en) | IR/발표 | 2026-03 | [A] |
| <a id="ref-e-04"></a>E-04 | Zama Blog — Zama at FHE.org 2026: Eight Contributions from Taipei | [링크](https://www.zama.org/post/zama-at-fhe-org-2026-eight-contributions-from-taipei) | IR/발표 | 2026-03-08 | [A] |
