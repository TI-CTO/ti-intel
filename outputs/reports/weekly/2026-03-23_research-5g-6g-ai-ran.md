---
type: weekly-deep-research
topic: 5g-6g-ai-ran
l3_name: 5G SA/6G (AI-RAN/SRv6)
domain: agentic-ai
week: 2026-W13
date: 2026-03-23
signal: 🟡
---

# Deep 리서치: 5G SA/6G (AI-RAN/SRv6) (2026-W13)

## 이전 대비 변화
- 전주(W12): MWC 2026 대형 발표 집중 — NVIDIA+12사 6G AI-native 연합 결성, Nokia Doksuri 출시, T-Mobile OTA 검증 완료, SoftBank SRv6 MUP 세계 최초 상용, SKT ATHENA 백서 발간
- 금주(W13): MWC 발표의 **실행·구체화 단계** — SKT-에릭슨 AI-RAN MoU 체결(3/19), NVIDIA Aerial 오픈소스화 완료(Apache 2.0), Linux Foundation OCUDU Foundation 출범, Open RAN+AI-RAN 통합 플랫폼 상용화 선언
- 변화 방향: 선언(MWC) → 파트너십 계약·오픈소스 생태계 구축 실행으로 전환. 6G 표준화 경쟁이 개방형 소프트웨어 스택 주도권 다툼으로 가속화

---

## 기술 동향

1. **NVIDIA Aerial 전면 오픈소스화 — AI-native RAN 개발 접근성 혁명적 확대.**
   NVIDIA가 Aerial 소프트웨어 포트폴리오 전체를 Apache 2.0 라이선스로 GitHub에 공개했다. 공개 항목은 (1) Aerial CUDA-Accelerated RAN — 상용급 3GPP·O-RAN 준수 5G/6G gNB 소프트웨어, (2) Aerial Omniverse Digital Twin(AODT) — 무선 네트워크 디지털 트윈 시뮬레이션 도구(2026년 3월 공개), (3) Aerial Framework — Python 코드를 고성능 CUDA 파이프라인으로 변환하는 툴체인의 세 가지다. 이로써 R&D 사이클이 "개월 단위에서 시간 단위"로 단축되며, DGX Spark 같은 소형 슈퍼컴퓨터와 결합 시 랩 수준 연구자도 상용급 AI-RAN 개발이 가능해졌다. [[G-01]](#ref-g-01)[[G-02]](#ref-g-02)

2. **SKT-에릭슨 MoU 체결 — 에릭슨의 ASIC 전략과 SKT 6G 로드맵 공식 결합.**
   3월 19일 SK Telecom과 Ericsson이 2031년 3월까지 5년간 유효한 AI-RAN·5G→6G 기술혁신 MoU에 서명했다. 협력 5개 축은 (1) AI-powered RAN: 자율학습·자원 최적화, (2) 5G 수익화, (3) 오픈·자율 네트워크(멀티벤더 환경), (4) Zero Trust 보안(5G Advanced·6G 대상), (5) 6G 표준화(극한 MIMO 진화·ISAC·에너지 효율·스펙트럼 전략)다. SKT Yu Takki 네트워크기술실장은 "AI 기반 네트워크 진화의 핵심 엔진이 될 것"이라고 발언했다. Ericsson ASIC 전략과 SKT ATHENA 비전이 결합된 이번 MoU는, NVIDIA GPU 의존 없이 독립적 AI-RAN 아키텍처를 추구하는 에릭슨의 표준화 진영 강화로 해석된다. [[G-03]](#ref-g-03)[[G-04]](#ref-g-04)[[E-01]](#ref-e-01)

3. **Linux Foundation OCUDU Ecosystem Foundation 출범 — 오픈소스 AI-RAN 탈벤더록인 움직임.**
   3월 1일 Linux Foundation이 Open CU/DU(OCUDU) Ecosystem Foundation을 MWC 2026에서 공식 설립했다. AMD, AT&T, Cisco, DeepSig, Ericsson, Nokia, NVIDIA, SoftBank, SRS, Verizon 등 창립 멤버 21개사·연구기관 17곳이 참여하며, 미국 FutureG Office·National Spectrum Consortium의 초기 자금 지원을 받았다. OCUDU는 O-RAN 기반 오픈소스 CU·DU 스택에 AI 알고리즘을 통합한 레퍼런스 플랫폼 아키텍처를 제공하며, 독점 인프라에 대한 벤더 종속 해소를 목표로 한다. 경쟁 관계인 Nokia와 Ericsson이 동일 재단에 함께 참여하는 점이 주목된다. [[G-05]](#ref-g-05)[[G-06]](#ref-g-06)

4. **Wind River + AMD: 업계 최초 O-RAN·AI-RAN 통합 플랫폼 상용 출시 선언.**
   3월 2일 Wind River(Aptiv 자회사)와 AMD가 단일 하드웨어에서 vRAN 기능과 AI 추론을 동시 구동하는 통합 플랫폼을 발표했다. AMD EPYC CPU + Wind River Cloud Platform 조합으로, RAN 처리와 실시간 AI(트래픽 예측·이상 감지·에너지 최적화)를 별도 서버 없이 분산 엣지에서 수행한다. 기존 접근법 대비 CAPEX를 최대 절반 수준으로 절감할 수 있다는 주장이다. 이는 GPU 가속(NVIDIA) 없이 범용 CPU 기반으로도 AI-RAN을 구현하는 상용 진입점이 생겼음을 의미한다. [[G-07]](#ref-g-07)[[G-08]](#ref-g-08)

5. **Samsung + AMD: 검증 단계 초월, AI-RAN 상용 배포 공식 전환.**
   Samsung과 AMD가 3월 2일 MWC에서 "검증(verification)에서 상용 배포(commercial deployment)로의 전환"을 공식 선언했다. Samsung AI-powered vRAN에 AMD EPYC 9005 Series CPU 적용, 다중 셀 테스트(삼성 R&D 랩) 완료 및 확장 가능한 상용급 성능 달성이 핵심 성과다. 추가 가속기 없이 완전 가상화 소프트웨어 스택만으로 상용급 AI-RAN 성능을 달성했다는 점이 의미 있다. 캐나다 Videotron에 5G NSA+4G LTE 코어 게이트웨이 배포(AMD EPYC 9005)도 병행 발표됐다. [[G-09]](#ref-g-09)[[G-10]](#ref-g-10)

6. **Rakuten Mobile: 전국망 RIC 구축 완료 — 오픈 RAN AI의 실제 운영 레퍼런스 확보.**
   Rakuten Mobile이 2026년 2월 O-RAN 표준 기반 제3자 rApp 연동 포함 전국망 RIC(RAN Intelligent Controller) 배포를 완료했다. 세계 최초 전국 규모 RIC 제3자 rApp 배포로, 예측적 유지보수·이동성 강화·트래픽 최적화·AI 지원 의사결정 등이 구현됐다. 자체 개발 rApp이 가입자 트래픽 패턴을 분석하고 기지국 이용률을 동적 조정하여 전력 소비를 15~20% 절감한다고 발표했다. Open RAN이 실험실에서 실제 국가 규모 운영으로 전환된 최초 사례로 평가된다. [[G-11]](#ref-g-11)[[G-12]](#ref-g-12)

7. **DeepSig: AI-native Open RAN + 스펙트럼 인식 통합 — 6G 학습형 파형(Learned Waveform) 시연.**
   DeepSig가 MWC 2026에서 NVIDIA·SRS·AI-RAN Alliance와 협력하여 OmniPHY-5G®와 OmniPHY® Axon을 시연했다. 핵심은 3GPP Rel-17 GPU 가속 OCUDU 스택 위에서 Pre-6G 완전 학습형 파형(fully learned waveform)을 구동하는 것으로, NVIDIA DGX Spark 단일 서버에서 상용 5G와 6G 프로토타입이 동시 동작했다. 스펙트럼 인식 측면에서는 PCTEL SeeHawk Scout 플랫폼에 OmniSIG® 통합, 실시간 스펙트럼 모니터링과 간섭 감지 기능을 이식했다. [[G-13]](#ref-g-13)[[G-14]](#ref-g-14)

8. **3GPP Release 20 및 6G 표준화 현황 — 2027년 Full Steam 목표 재확인.**
   3GPP Release 20(5G-Advanced) Stage-2는 2026년 6월까지 80% 완료, 최종 동결은 2026년 9월 목표다. Release 21이 사실상 최초 6G 스펙이 되며, 2026년 6월 Work Item 확정 예정이다. 기술 작업이 2027년 3월부터 "Full Steam"으로 전환되고, ITU IMT-2030 기술 제안서 제출 목표는 2029년 초다. SKT-Ericsson MoU의 5년 유효기간(2031년)이 정확히 초기 6G 상용화 시점을 겨냥하고 있다. [[G-15]](#ref-g-15)[[G-16]](#ref-g-16)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| NVIDIA | Aerial 전체 스택(CUDA-Accelerated RAN, AODT, Framework) Apache 2.0으로 오픈소스 공개. GitHub에 즉시 이용 가능. 프로토타입→상용 개발 사이클 "개월에서 시간으로" 단축 주장 | [[G-01]](#ref-g-01), [[G-02]](#ref-g-02) |
| SK Telecom | 3/19 Ericsson과 AI-RAN·5G→6G 혁신 MoU 체결(유효기간 2031년). 5개 협력 축: AI-powered RAN, 5G 수익화, 오픈·자율 네트워크, Zero Trust 보안, 6G 표준화(ISAC 포함) | [[G-03]](#ref-g-03), [[E-01]](#ref-e-01) |
| Ericsson | SKT MoU로 ASIC 기반 독립 AI-RAN 전략의 통신사 파트너 확보. 동시에 Chunghwa Telecom과도 5G-Advanced·AI 지능망 MoU 체결(MWC). Intel과 AI-native 6G 협력도 병행 | [[G-03]](#ref-g-03), [[G-04]](#ref-g-04) |
| Linux Foundation (OCUDU) | O-RAN·AI-RAN 오픈소스 재단 OCUDU 공식 출범. 창립 멤버: AMD, AT&T, Cisco, DeepSig, Ericsson, Nokia, NVIDIA, SoftBank, SRS, Verizon + 21개 일반회원·17개 연구기관 | [[G-05]](#ref-g-05), [[G-06]](#ref-g-06) |
| Wind River + AMD | 업계 최초 통합 O-RAN + AI-RAN 상용 플랫폼 발표. AMD EPYC + Wind River Cloud Platform으로 vRAN+AI 추론 단일 서버 구현, 별도 GPU 가속기 불필요 | [[G-07]](#ref-g-07), [[G-08]](#ref-g-08) |
| Samsung | AMD와 AI-RAN 공동 검증 → 상용 배포 공식 전환. EPYC 9005 기반 다중 셀 AI vRAN 성능 달성. Videotron(캐나다) 상용 배포 레퍼런스 확보. Vodafone과 신규 칩셋 유럽 검증도 완료 | [[G-09]](#ref-g-09), [[G-10]](#ref-g-10) |
| Rakuten Mobile | 전국망 RIC + 제3자 rApp 세계 최초 배포 완료. 전력 소비 15~20% 절감. O-RAN 실증에서 운영 레퍼런스로 전환 | [[G-11]](#ref-g-11), [[G-12]](#ref-g-12) |
| DeepSig | Pre-6G 학습형 파형 OCUDU 스택에서 시연(MWC). OCUDU Foundation 창립 멤버 합류. PCTEL과 스펙트럼 인식 통합 | [[G-13]](#ref-g-13), [[G-14]](#ref-g-14) |
| SoftBank | AITRAS 16-layer MU-MIMO 야외 실증(처리량 3배 향상). MHI와 엣지 데이터센터 협력 개시. 2026년 상용망 도입 목표 유지 | [[G-17]](#ref-g-17), [[E-02]](#ref-e-02) |

---

## 시장 시그널

- AI-RAN Alliance 회원사가 132개사로 확대됐다. MWC 2026에서 33개 AI 기반 혁신 데모와 4개 산업 청사진을 발표했다. Qualcomm, SK Telecom, Vodafone이 이사회 멤버로 새로 합류했다. [[G-18]](#ref-g-18)
- Juniper Research는 통신사의 AI 기술 투자 규모가 2026년 약 210억 달러에 달할 것으로 추산한다. AI-RAN이 이 투자의 주요 수혜 분야로 지목된다. [C] 단일 추정치로 교차 검증 필요. [[G-19]](#ref-g-19)
- Intel은 AI-RAN Alliance에 아직 참여하지 않고 있다. Ericsson과는 AI-native 6G 협력을 진행 중으로, 표준화 주도권 경쟁에서 칩 공급망 구도가 NVIDIA 중심 vs. CPU/ASIC 진영으로 양분되는 양상이다. [[G-20]](#ref-g-20)
- SRv6 MUP 영역에서 Lanner+Arrcus가 MWC 2026에서 AI-Ready SRv6 MUP 솔루션을 공개했다. SoftBank 상용 레퍼런스를 바탕으로 MEC+네트워크 슬라이싱 결합 상용화가 본격화되고 있다. [[G-21]](#ref-g-21)
- Ericsson은 Chunghwa Telecom과도 5G-Advanced·AI 지능망 MoU를 체결, 아시아 태평양에서의 ASIC 기반 AI-RAN 파트너십을 확장하고 있다. NVIDIA 진영(Nokia)과의 아태 고객 확보 경쟁이 가속되고 있다. [[G-22]](#ref-g-22)
- Nokia는 NVIDIA GTC 2026(3월)에 참가하여 AI-native 6G 비전을 추가 발표할 예정으로, MWC 이후에도 GPU-first 전략 홍보를 지속하고 있다. [[G-23]](#ref-g-23)

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| "Toward E2E Intelligence in 6G Networks: An AI Agent-Based RAN-CN Converged Intelligence Framework" (Han et al., 2026) | LLM + ReAct 패러다임 기반 6G RAN-CN 통합 지능 프레임워크. 별도 태스크별 AI 모델 없이 실시간 크로스 도메인 추론 및 제어 결정. 재훈련 없는 적응성 확보 주장 | [[P-01]](#ref-p-01) |
| "AI-Native PHY-Layer in 6G Orchestrated Spectrum-Aware Networks" (Mutescu et al., 2025) | 6G PHY 계층 스펙트럼 인식 AI 탐지기 2종 제안: (1) OFDM/OTFS 파형 판별기(정확도 99.5%), (2) 수치 구조 탐지기(정확도 83.3~99.9%). IQ 샘플에서 직접 파라미터 추정 | [[P-02]](#ref-p-02) |
| "Towards transparent 6G AI-RAN: A survey on explainable deep reinforcement learning for intelligent network slicing" (ScienceDirect, 2025) | 설명 가능한 심층강화학습(XRL) 기반 AI-RAN 네트워크 슬라이싱 서베이. 투명성·신뢰성 요구사항 분석 및 6G AI-RAN 규제 대응 방향 제시 | [[P-03]](#ref-p-03) |
| "The LLM as a Network Operator: A Vision for Generative AI in the 6G RAN" (arXiv:2509.10478, 2025) | Non-RT RIC에서의 LLM 전략 결정 + Near-RT RIC에서의 반응적 실행 분리 아키텍처. O-RAN 표준과 정렬된 LLM-RAN 운영 프레임워크 제안 | [[P-04]](#ref-p-04) |

---

## 전략적 시사점

**기회**

- NVIDIA Aerial 오픈소스화로 국내 통신사·연구기관의 AI-RAN 프로토타입 진입 비용이 대폭 낮아졌다. SKT가 ATHENA에서 제시한 AI-native RAN 연구를 NVIDIA DGX Spark 급 장비로 즉시 시작할 수 있는 환경이 조성됐다.
- SKT-Ericsson MoU는 6G 표준화 협력 축을 확보했다는 의미와 함께, ISAC(통합 감지·통신) 공동 연구 진입점을 제공한다. 국내 통신사 중 가장 명확한 벤더 전략(Ericsson ASIC 진영)을 보유하게 됐다.
- Linux Foundation OCUDU는 향후 AI-RAN 소프트웨어 스택의 표준 레퍼런스가 될 가능성이 있다. 초기부터 참여하면 개발 방향에 영향력을 행사하고 글로벌 오픈소스 생태계와 연계할 수 있다.
- Rakuten의 전국망 RIC 운영 레퍼런스가 실증됨으로써, Open RAN 기반 AI 운영의 ROI 계산 근거가 실제 데이터로 뒷받침되기 시작했다.

**위협**

- Nokia(GPU-first) vs. Ericsson(ASIC-first) vs. Samsung(CPU-only) 전략 분기가 심화되고 있어, 국내 통신사의 장비 선택이 특정 칩 아키텍처 종속으로 이어질 위험이 있다. 멀티벤더 환경을 전제한 기술 검토가 필요하다.
- NVIDIA Aerial 오픈소스화는 동시에 경쟁자들의 기술 수준을 빠르게 높인다. 글로벌 후발 통신사(동남아·인도 등)가 단기간에 AI-RAN 실증 능력을 확보할 수 있어, 시장 차별화 기회 창출이 더 어려워질 수 있다.
- Intel의 AI-RAN Alliance 비참여는 서버 공급망의 불확실성을 내포한다. vRAN·Open RAN 인프라에서 Intel CPU가 주력인 상황에서, AI 가속 전략에서 Intel이 배제될 경우 기존 인프라 투자와의 정합성 문제가 발생할 수 있다.
- 6G 표준화(3GPP Rel-21)가 2027년 Full Steam 진입 전이기 때문에, 현재 발표되는 "AI-native 6G" 솔루션은 대부분 표준 이전 단계의 독점적 구현이다. 표준 확정 후 재작업 필요성이 생길 수 있다.

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | NVIDIA Blog — Open Sources Aerial Software to Accelerate AI-Native 6G | [링크](https://blogs.nvidia.com/blog/open-source-aerial-ai-native-6g/) | news | 2026-03 | [A] |
| <a id="ref-g-02"></a>G-02 | GitHub — NVIDIA/aerial-cuda-accelerated-ran (Apache 2.0) | [링크](https://github.com/NVIDIA/aerial-cuda-accelerated-ran) | news | 2026-03 | [A] |
| <a id="ref-g-03"></a>G-03 | Ericsson Newsroom — SKT-Ericsson MoU AI-RAN 5G to 6G | [링크](https://www.ericsson.com/ko/news/2/2026/skt-6g-mou) | news | 2026-03-19 | [A] |
| <a id="ref-g-04"></a>G-04 | Computer Weekly — Ericsson SK Telecom MoU AI-RAN 5G to 6G innovation | [링크](https://www.computerweekly.com/news/366640451/Ericsson-SK-Telecom-ink-memorandum-of-understanding-to-strengthen-AI-RAN-5G-to-6G-innovation) | news | 2026-03-19 | [B] |
| <a id="ref-g-05"></a>G-05 | Linux Foundation — OCUDU Ecosystem Foundation Launch | [링크](https://www.linuxfoundation.org/press/linux-foundation-announces-ocudu-ecosystem-foundation-to-accelerate-open-source-ai-ran-innovation) | news | 2026-03-01 | [A] |
| <a id="ref-g-06"></a>G-06 | Open Source For You — Linux Foundation Pushes Open Source AI-RAN | [링크](https://www.opensourceforu.com/2026/03/linux-foundation-pushes-open-source-ai-ran-to-reduce-telecom-vendor-lock-in/) | news | 2026-03 | [B] |
| <a id="ref-g-07"></a>G-07 | BusinessWire — Wind River AMD Unified O-RAN AI-RAN Platform | [링크](https://www.businesswire.com/news/home/20260301788558/en/Wind-River-Announces-Strategic-Collaboration-with-AMD-Delivering-Industrys-First-Unified-O-RAN-and-AI-RAN-Platform) | news | 2026-03-02 | [A] |
| <a id="ref-g-08"></a>G-08 | The Fast Mode — Wind River AMD First Unified Open RAN AI-RAN Platform | [링크](https://www.thefastmode.com/technology-solutions/47474-wind-river-amd-deliver-first-unified-open-ran-and-ai-ran-platform) | news | 2026-03-02 | [B] |
| <a id="ref-g-09"></a>G-09 | Samsung Global Newsroom — Samsung AMD Commercial Deployment AI-RAN | [링크](https://news.samsung.com/global/samsung-and-amd-reinforce-strategic-collaboration-to-advance-ai-powered-network-innovations-for-commercial-deployments) | news | 2026-03-03 | [A] |
| <a id="ref-g-10"></a>G-10 | The Fast Mode — Samsung AMD Beyond Testing to Commercial 5G AI Network | [링크](https://www.thefastmode.com/technology-solutions/47483-samsung-amd-move-beyond-testing-to-commercial-5g-ai-powered-network-deployments) | news | 2026-03 | [B] |
| <a id="ref-g-11"></a>G-11 | Rakuten Symphony Newsroom — Nationwide RIC Third-Party rApp Deployment | [링크](https://symphony.rakuten.com/newsroom/rakuten-mobile-and-rakuten-symphony-advance-open-ran-innovation-with-third-party-rapp-integration-and-nationwide-ric-deployment) | news | 2026-02-26 | [A] |
| <a id="ref-g-12"></a>G-12 | Telecompaper — Rakuten Mobile Nationwide RIC Deployment | [링크](https://www.telecompaper.com/news/rakuten-mobile-completes-nationwide-ric-deployment-with-rapp-integration--1563488) | news | 2026-02 | [B] |
| <a id="ref-g-13"></a>G-13 | DeepSig — AI-Native Open RAN Spectrum Awareness MWC26 | [링크](https://www.deepsig.ai/ai-native-open-ran-and-spectrum-awareness-integration-at-mwc26/) | news | 2026-02-27 | [A] |
| <a id="ref-g-14"></a>G-14 | BusinessWire — DeepSig Joins OCUDU Ecosystem Foundation | [링크](https://www.businesswire.com/news/home/20260302355808/en/DeepSig-Joins-OCUDU-Ecosystem-Foundation-to-Advance-AI-Native-Open-RAN-Innovation) | news | 2026-03-02 | [A] |
| <a id="ref-g-15"></a>G-15 | 3GPP — Release 20 Planning and Progress in TSG SA | [링크](https://www.3gpp.org/news-events/3gpp-news/sa-rel20) | news | 2026 | [A] |
| <a id="ref-g-16"></a>G-16 | 6G-AI.com — 3GPP 6G Timeline Key Milestones 2026-2030 | [링크](https://6g-ai.com/news/3gpp-6g-timeline-milestones-2026-2030) | news | 2026 | [B] |
| <a id="ref-g-17"></a>G-17 | SoftBank — AITRAS 16-Layer MU-MIMO Outdoor Field Trial | [링크](https://www.softbank.jp/en/corp/news/press/sbkk/2025/20251029_02/) | news | 2025-10-29 | [A] |
| <a id="ref-g-18"></a>G-18 | SDxCentral — AI-RAN Alliance 130+ Members MWC | [링크](https://www.sdxcentral.com/news/ai-ran-alliance-pushes-past-130-members-as-ai-native-ran-takes-center-stage-at-mwc/) | news | 2026-03 | [B] |
| <a id="ref-g-19"></a>G-19 | Juniper Research — Direct-to-Device 5G Advanced AI RAN 2026 | [링크](https://www.juniperresearch.com/press/direct-to-device-5g-advanced-ai-ran-to-redefine-global-connectivity-in-2026/) | news | 2026 | [C] |
| <a id="ref-g-20"></a>G-20 | Fierce Network — MWC 2026 Intel Sits Out AI-RAN Alliance | [링크](https://www.fierce-network.com/wireless/mwc-2026-intel-sits-out-ai-ran-alliance-now) | news | 2026-03 | [B] |
| <a id="ref-g-21"></a>G-21 | Lanner Electronics — Lanner Arrcus SRv6 MUP MWC 2026 | [링크](https://www.lannerinc.com/news-and-events/latest-news/lanner-and-arrcus-unveil-ai-ready-srv6-mup-solution-for-next-gen-5g-deployments-at-mwc-2026) | news | 2026-03 | [A] |
| <a id="ref-g-22"></a>G-22 | Ericsson Press Release — Chunghwa Telecom 5G-Advanced AI MoU MWC 2026 | [링크](https://www.ericsson.com/en/press-releases/2026/3/cht-and-ericsson-sign-5g-advanced-and-ai-intelligent-network-mou-at-mwc-2026-to-accelerate-6g-evolution) | news | 2026-03 | [A] |
| <a id="ref-g-23"></a>G-23 | Nokia — Nokia at NVIDIA GTC 2026 | [링크](https://www.nokia.com/events/nvidia-gtc/) | news | 2026-03 | [A] |
| <a id="ref-e-01"></a>E-01 | SK Telecom Newsroom — SKT Ericsson MoU 6G Network Innovation | [링크](https://news.sktelecom.com/en/2854) | IR/발표 | 2026-03-19 | [A] |
| <a id="ref-e-02"></a>E-02 | SoftBank — AITRAS Edge Data Center Collaboration with MHI | [링크](https://www.softbank.jp/en/corp/news/press/sbkk/2026/20260302_02/) | IR/발표 | 2026-03-02 | [A] |
| <a id="ref-p-01"></a>P-01 | Han et al. — Toward E2E Intelligence in 6G Networks: An AI Agent-Based RAN-CN Converged Intelligence Framework | [링크](https://arxiv.org/abs/2602.23623) | paper | 2026-02-27 | [B] |
| <a id="ref-p-02"></a>P-02 | Mutescu et al. — AI-Native PHY-Layer in 6G Orchestrated Spectrum-Aware Networks | [링크](https://pmc.ncbi.nlm.nih.gov/articles/PMC12694481/) | paper | 2025-11-26 | [A] |
| <a id="ref-p-03"></a>P-03 | ScienceDirect — Towards transparent 6G AI-RAN: Explainable DRL for intelligent network slicing | [링크](https://www.sciencedirect.com/science/article/pii/S2949715925000757) | paper | 2025 | [A] |
| <a id="ref-p-04"></a>P-04 | arXiv:2509.10478 — The LLM as a Network Operator: A Vision for Generative AI in the 6G RAN | [링크](https://arxiv.org/abs/2509.10478) | paper | 2025-09 | [B] |
