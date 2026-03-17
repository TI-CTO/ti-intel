---
type: deep-research
topic: 5g-6g-ai-ran
date: 2026-03-16
parent: 2026-03-16_weekly-voice-ai.md
---

# 5G SA/6G (AI-RAN/SRv6) — 심층 리서치 (W12)

> 수집 기간: 2026-03-09 ~ 2026-03-16 | MWC 2026(3/2~5) 후속 분석 포함
> 신뢰도: **medium-high** — 주요 사실은 기업 공식 발표 및 복수 소스 교차 검증. 시장 규모 수치는 단일 리서치 기관 추정치 포함.

---

## 기술 동향

1. **NVIDIA 주도 6G AI-native 플랫폼 연합 결성** — MWC 2026 개막 전날(3/1), NVIDIA와 BT Group, Cisco, Deutsche Telekom, Ericsson, Nokia, SK Telecom, SoftBank, T-Mobile 등 12개 기업이 6G 네트워크를 "개방형·AI-native·보안·신뢰 기반" 플랫폼 위에 구축하겠다는 공동 선언을 발표했다. AI-RAN Alliance 참가사는 이미 130개사 이상으로, MWC 2026 기간 33개 데모 중 26개가 NVIDIA AI Aerial 소프트웨어 정의 아키텍처를 채택했다. [[E-01]](#ref-e-01)[[G-01]](#ref-g-01)

2. **Nokia vs. Ericsson: AI-RAN 구현 전략 분기** — 양대 서방 통신장비사가 AI를 RAN에 통합하는 방식에서 근본적으로 갈라섰다. Nokia는 NVIDIA로부터 10억 달러 투자를 유치하고 차세대 5G/6G RAN 소프트웨어를 NVIDIA Grace Hopper 플랫폼 위에서 구동하는 GPU-first 전략을 채택했다. 반면 Ericsson은 Many-Core Architecture에 신경망 가속기(프로그래머블 매트릭스 코어)를 내장한 자사 Silicon ASIC으로 AI를 RAN에 직접 통합하며, NVIDIA GPU 없이 서브밀리초 빔포밍·채널 추정을 실현한다. Ericsson의 핵심 논거는 비용·전력·공급망 독립성이다. [[G-02]](#ref-g-02)[[G-03]](#ref-g-03)[[E-02]](#ref-e-02)

3. **Nokia Doksuri 라디오 출시 및 상용 AI-RAN 로드맵 확정** — Nokia는 MWC 2026에서 ReefShark SoC 기반 Doksuri Remote Radio Head를 발표했다. 전력효율 30% 향상, 무게 25% 감소, 설치 시간 70% 단축이 특징이다. Nokia CTO Pallavi Mahajan은 "2026년 첫 상용 필드 트라이얼, 2027년 첫 상용 릴리즈"라는 일정을 공식화했다. [[E-03]](#ref-e-03)[[G-04]](#ref-g-04)

4. **T-Mobile: Nokia+NVIDIA AI-RAN OTA 검증 완료** — T-Mobile Seattle AI-RAN Innovation Centre에서 Nokia AirScale Massive MIMO(3.7 GHz, n77 대역) + NVIDIA Grace Hopper GH200 단일 서버 위에서 RAN 처리와 AI 추론(비디오 스트리밍·생성AI 쿼리·AI 자막)을 동시 구동하는 OTA 검증을 완료했다. 상용 디바이스 대상 실증이라는 점에서 업계 첫 사례로 평가된다. [[E-04]](#ref-e-04)[[G-05]](#ref-g-05)

5. **Ericsson: Cloud RAN의 NVIDIA 플랫폼 이식성 확인** — Ericsson은 T-Mobile과 함께 Ericsson Cloud RAN 소프트웨어를 NVIDIA AI Infrastructure(CUDA Aerial) 위에서 구동하는 데 성공했다. Ericsson의 전략은 자사 Silicon을 기본으로 하되, 연산 플랫폼에 관계없이 동일 소프트웨어가 동작하는 하드웨어 무관(portable) RAN 스택을 지향한다. [[E-05]](#ref-e-05)[[G-06]](#ref-g-06)

6. **IOH(Indosat): 동남아 첫 AI-powered 5G 콜 시연** — Indosat Ooredoo Hutchison이 Nokia·NVIDIA와 함께 MWC 2026에서 동남아시아 최초의 AI 기반 5G 콜을 시연했다. 라이브 5G 네트워크에서 로봇견 원격 제어를 포함한 실시간 크로스보더 연결을 구현했으며, 인도네시아 4개 도시에 AI-RAN 클러스터 배포 계획을 밝혔다. 수라바야에 Nokia·NVIDIA와 공동 AI-RAN 연구센터도 설립했다. [[G-07]](#ref-g-07)[[N-01]](#ref-n-01)

7. **T-Mobile + Deutsche Telekom: 공동 6G Innovation Hub 출범** — 2026년 2월 28일 T-Mobile(미국 Bellevue)과 Deutsche Telekom(독일 베를린 T-Labs)이 공동 6G Innovation Hub를 공식 출범했다. AI-native 자율 네트워크, 광역 감지·측위, 연결성+고성능 컴퓨팅 융합을 3대 축으로 6G를 설계하겠다는 선언이다. [[E-06]](#ref-e-06)[[G-08]](#ref-g-08)

8. **SK Telecom: 'AI Native 기업' 선언 및 ATHENA 6G 백서 발간** — SKT CEO 정재헌은 MWC 2026 현지에서 "AI Native 기업으로의 전환" 전략을 공식 발표하고, 국내 하이퍼스케일 AI 데이터센터 1 GW 이상 구축 계획을 공개했다. 3번째 6G 백서 'ATHENA'(AI·Trust·Hyper-connectivity·Experience·opeN·Agility)를 통해 AI-native RAN 로드맵을 제시했다. [[E-07]](#ref-e-07)[[G-09]](#ref-g-09)

9. **SRv6 MUP: SoftBank 세계 최초 5G 상용 서비스 제공(2025년 12월)** — SoftBank가 2025년 12월 SRv6 MUP 기반 5G 상용 서비스(FWA)를 세계 최초로 개시했다. Broadcom Jericho2 라우팅 칩셋, Arrcus ArcOS, VMware Telco Cloud Platform 조합으로 구성했으며, MEC·네트워크 슬라이싱을 단일 IPv6 전달 평면에서 구현한다. 4G 네트워크로 확대 적용 중이다. [[G-10]](#ref-g-10)[[N-02]](#ref-n-02)

10. **3GPP AI/ML 표준화 진행 현황** — Rel-18 AI/ML normative 작업은 2023년 Q4 완료, Rel-19 에너지절감·부하분산·이동성 최적화 규범화 작업 진행 중. Rel-20에서 양방향(Two-sided) AI 모델(디바이스+네트워크 동시 AI)이 공식 Work Item으로 채택됐으며 2027년 H2 완료 예정이다. 6G 규격은 2029년 목표. [[G-11]](#ref-g-11)[[G-12]](#ref-g-12)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| NVIDIA | MWC 2026에서 12개 통신사와 6G AI-native 플랫폼 공동 선언. AI-RAN Alliance 130개사 확대. MWC 26개 데모에 AI Aerial 플랫폼 채택 | [[E-01]](#ref-e-01), [[G-01]](#ref-g-01) |
| Nokia | Doksuri 라디오 출시(전력 -30%, 무게 -25%), 2026 필드 트라이얼·2027 상용 릴리즈 확정. NVIDIA GPU-first 전략, $1B 투자 유치 | [[E-03]](#ref-e-03), [[G-04]](#ref-g-04) |
| Ericsson | 자사 ASIC Silicon(신경망 가속기 내장)으로 NVIDIA 독립 AI-RAN 구현. 동시에 Cloud RAN의 NVIDIA 플랫폼 이식성 시연(T-Mobile 협업). "6G 지능형 패브릭" 비전 공개 | [[E-02]](#ref-e-02), [[E-05]](#ref-e-05), [[G-06]](#ref-g-06) |
| T-Mobile (US) | Nokia+NVIDIA OTA AI-RAN 검증 완료(GH200 단일 서버), Deutsche Telekom과 6G Innovation Hub 출범 | [[E-04]](#ref-e-04), [[E-06]](#ref-e-06) |
| Deutsche Telekom | T-Mobile과 6G R&D Hub 공동 출범. MWC 2026서 AI 기반 Smart Call Assistant 세계 최초 공개 | [[E-06]](#ref-e-06), [[G-08]](#ref-g-08) |
| SK Telecom | AI Native 기업 선언. ATHENA 6G 백서 발간. AI-RAN Alliance 이사회 멤버. AI 데이터센터 1 GW+ 투자 계획 | [[E-07]](#ref-e-07), [[G-09]](#ref-g-09) |
| SoftBank | SRv6 MUP 5G 상용 서비스 세계 최초 제공(2025-12). 4G망 확대 적용 중 | [[G-10]](#ref-g-10) |
| Indosat (IOH) | 동남아 최초 AI-powered 5G 콜 시연. 4개 도시 AI-RAN 클러스터 배포 계획. Nokia·NVIDIA와 수라바야 AI-RAN 연구센터 설립 | [[G-07]](#ref-g-07), [[N-01]](#ref-n-01) |

---

## 시장 시그널

- 글로벌 AI-RAN 시장 규모는 2026년 약 38억 달러(USD 3.81B)로 추산되며, 2035년 372억 달러(CAGR 28.79%)까지 성장할 것으로 전망된다 [[G-13]](#ref-g-13). Open RAN 시장은 2026년 약 42~54억 달러 수준이다 [[G-14]](#ref-g-14). (단일 리서치사 추정치이므로 [C] 등급 참고)
- 5G SA 상용망은 GSA 기준 73개국 181개 사업자가 투자 중이며, 최소 47개국 85개 사업자가 라이브 서비스를 운영하고 있다 [[G-15]](#ref-g-15). 5G SA 다운로드 속도 중앙값은 269.51 Mbit/s로 NSA 대비 52% 우위를 기록했다.
- Intel은 AI-RAN Alliance 참여에 소극적인 입장을 유지하고 있어, 칩 공급망 다각화 측면에서 장기 변수로 작용할 수 있다 [[G-16]](#ref-g-16).
- MWC 2026 업계 내부 분위기: "5G에서 AI-powered 6G로 중심축이 이동"했다는 평가가 지배적이며, AI-native 네트워크가 더 이상 6G만의 약속이 아니라 현재 진행형임이 실증됐다 [[G-17]](#ref-g-17).
- 하드웨어 생태계 확장: Quanta(COTS AI-RAN), Supermicro(ARC-Pro), MSI(AI-vRAN), Lanner(AstraEdge) 등 화이트박스 서버 기업이 AI-RAN용 상용 제품을 속속 출시 중이다 [[G-01]](#ref-g-01).
- T-Mobile의 AI-RAN 전략은 NVIDIA 단독이 아닌 멀티벤더 접근임이 확인됐다. Nokia, Ericsson 양쪽과 동시에 AI-RAN 파일럿을 진행하고 있다 [[G-18]](#ref-g-18).

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| AI-RAN: Transforming RAN with AI-driven Computing Infrastructure (Kundu et al., 2025) | AI-for-RAN·AI-on-RAN·AI-and-RAN 3가지 구현 유형 분류 체계 제시. NVIDIA GH200에서 RAN+AI 동시 처리 개념증명 | [[P-01]](#ref-p-01) |
| Toward E2E Intelligence in 6G Networks (Han et al., 2026) | LLM+ReAct 패러다임으로 RAN-CN 통합 지능화 프레임워크 제안. 미지의 네트워크 시나리오에 대한 적응성 향상 | [[P-02]](#ref-p-02) |
| Agentic AI for Intent-driven Optimization in Cell-free O-RAN (Shokouhi & Wong, 2026) | 다중 LLM 에이전트(감독·자원관리·모니터링)로 O-RAN 의도 번역 및 최적화 구현. 활성 O-RU 41.93% 감소, 파라미터 효율화 92% 메모리 절감 | [[P-03]](#ref-p-03) |
| Embracing AI in 5G-Advanced Toward 6G (IEEE, 2023) | 3GPP-O-RAN 공동 관점에서 5G-Advanced→6G AI 통합 경로 제시 | [[P-04]](#ref-p-04) |
| AI-RAN: untying the knot for 6G (The Mobile Network, 2026) | AI-RAN이 6G 표준화에서 RAN 진화의 결절점임을 분석 | [[P-05]](#ref-p-05) |

---

## 전략적 시사점

**기술 트렌드**
- AI-RAN은 이제 6G 선행 연구 단계가 아니라, 2026년 필드 트라이얼·2027년 상용화를 향한 실행 단계에 진입했다. Nokia의 타임라인 공식화가 그 분수령이다.
- Nokia(GPU-first)와 Ericsson(ASIC-first) 간 구현 전략 분기는 통신사 입장에서 향후 5~7년간 공급망 선택의 핵심 변수가 된다. 두 전략 모두 소프트웨어 이식성을 명분으로 내세우고 있어, 실제 TCO 비교가 의사결정의 핵심이 될 것이다.
- RAN+AI 컴퓨팅 수렴(AI-on-RAN) 트렌드는 기지국 인프라를 에지 AI 컴퓨팅 플랫폼으로 재정의하고 있으며, NVIDIA가 칩 생태계 장악을 통해 통신 밸류체인에 직접 진입하는 경로가 열리고 있다.

**기회**
- SRv6 MUP 기반 5G SA 전송망 표준화 흐름이 가속화되고 있어, 국내 통신사(SKT 포함) 전송망 현대화 사업에서 SRv6-MUP 채택이 구체화될 수 있다.
- AI-RAN Alliance 130개사 생태계는 Open RAN 레퍼런스 아키텍처와 결합해, 신규 진입자(중소 통신장비사·소프트웨어 벤더)가 GPU 플랫폼 위에서 RAN 소프트웨어를 공급할 수 있는 구조를 만들고 있다.
- SKT의 ATHENA 6G 백서는 AI-native RAN 구현의 표준 비전을 제시하고 있어, 국내 6G 연구 아젠다 및 정책 레퍼런스로 활용 가능하다.

**위협**
- Intel의 AI-RAN Alliance 불참 지속 시, NVIDIA 칩 중심 생태계 집중이 심화되어 공급망 리스크와 가격 협상력 약화를 초래할 수 있다.
- Nokia의 NVIDIA 의존 심화는 장기적으로 Nokia 자체 실리콘 경쟁력 약화와 함께 NVIDIA의 통신장비 생태계 내 지렛대를 확대한다.
- 5G SA 글로벌 배포율은 증가 중이나, Opensignal에 따르면 수익화(Monetisation)는 여전히 지연되고 있어 ROI 실현까지 상당한 기간이 필요할 수 있다 [[G-15]](#ref-g-15).

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-e-01"></a>E-01 | NVIDIA — NVIDIA and Global Telecom Leaders Commit to Build 6G on Open and Secure AI-Native Platforms | [링크](https://nvidianews.nvidia.com/news/nvidia-and-global-telecom-leaders-commit-to-build-6g-on-open-and-secure-ai-native-platforms) | 보도자료 | 2026-03-01 | [A] |
| <a id="ref-e-02"></a>E-02 | Ericsson — Ericsson Charts Its Own Path to AI-RAN, No Nvidia Required | [링크](https://5gstore.com/blog/2026/03/02/ericsson-ai-ran/) | 뉴스 | 2026-03-02 | [B] |
| <a id="ref-e-03"></a>E-03 | Nokia — Nokia expands network portfolio for premium performance in the AI-RAN era #MWC26 | [링크](https://www.nokia.com/newsroom/nokia-expands-network-portfolio-for-premium-performance-in-the-ai-ran-era-mwc26/) | 보도자료 | 2026-03-01 | [A] |
| <a id="ref-e-04"></a>E-04 | Nokia — Nokia accelerates AI-RAN momentum with new partnerships driving path to AI-Native 6G #MWC26 | [링크](https://www.nokia.com/newsroom/nokia-accelerates-ai-ran-momentum-with-new-partnerships-driving-path-to-ai-native-6g-mwc26/) | 보도자료 | 2026-03-01 | [A] |
| <a id="ref-e-05"></a>E-05 | Ericsson — Ericsson, T-Mobile test portable AI RAN on NVIDIA platform | [링크](https://www.ericsson.com/en/news/2026/3/ericsson-t-mobile-boost-portable-ai-ran-on-nvidia-platform) | 보도자료 | 2026-03-02 | [A] |
| <a id="ref-e-06"></a>E-06 | T-Mobile / Deutsche Telekom — T-Mobile and Deutsche Telekom Launch Joint 6G Innovation Hub | [링크](https://www.t-mobile.com/news/network/t-mobile-and-deutsche-telekom-6g-innovation-hub) | 보도자료 | 2026-02-28 | [A] |
| <a id="ref-e-07"></a>E-07 | SK Telecom — SK Telecom Publishes Third 6G White Paper 'ATHENA' | [링크](https://news.sktelecom.com/en/2751) | 보도자료 | 2026-02-23 | [A] |
| <a id="ref-e-08"></a>E-08 | T-Mobile — T-Mobile and Ericsson Advance Portable AI RAN Software On NVIDIA AI Infrastructure | [링크](https://www.t-mobile.com/news/network/t-mobile-and-ericsson-advance-portable-ai-ran-software-on-nvidia-ai-infrastructure) | 보도자료 | 2026-03-02 | [A] |
| <a id="ref-g-01"></a>G-01 | NVIDIA Blog — Software-Defined AI-RAN Is the Next Wireless Generation | [링크](https://blogs.nvidia.com/blog/software-defined-ai-ran/) | news | 2026-03-01 | [B] |
| <a id="ref-g-02"></a>G-02 | Light Reading — Ericsson does AI-RAN minus Nvidia in push for 5G silicon freedom | [링크](https://www.lightreading.com/5g/ericsson-does-ai-ran-minus-nvidia-in-push-for-5g-silicon-freedom) | news | 2026-02-20 | [B] |
| <a id="ref-g-03"></a>G-03 | IEEE ComSoc Blog — Ericsson goes with custom silicon (rather than Nvidia GPUs) for AI RAN | [링크](https://techblog.comsoc.org/2026/02/20/ericsson-goes-with-custom-silicon-rather-than-nvidia-gpus-for-ai-ran/) | news | 2026-02-20 | [B] |
| <a id="ref-g-04"></a>G-04 | Fierce Network — MWC 2026: Nokia promises commercial AI-RAN in 2027 | [링크](https://www.fierce-network.com/wireless/nokia-promises-commercial-ai-ran-2027) | news | 2026-03-02 | [B] |
| <a id="ref-g-05"></a>G-05 | SDxCentral — Nokia doubles down on AI-RAN with new Doksuri radios & Nvidia partnership momentum | [링크](https://www.sdxcentral.com/news/nokia-doubles-down-on-ai-ran-with-new-doksuri-radios-nvidia-partnership-momentum/) | news | 2026-03-02 | [B] |
| <a id="ref-g-06"></a>G-06 | TechAfrica — Ericsson Demonstrates Cloud RAN Software on NVIDIA AI Infrastructure with T-Mobile | [링크](https://techafricanews.com/2026/03/02/ericsson-demonstrates-cloud-ran-software-on-nvidia-ai-infrastructure-with-t-mobile/) | news | 2026-03-02 | [C] |
| <a id="ref-g-07"></a>G-07 | The Fast Mode — Indosat, Nokia, NVIDIA Demonstrate Southeast Asia's First AI 5G Call | [링크](https://www.thefastmode.com/technology-solutions/47414-indosat-nokia-nvidia-demonstrate-southeast-asia-s-first-ai-5g-call) | news | 2026-03-02 | [B] |
| <a id="ref-g-08"></a>G-08 | TelecomTV — MWC26: DT, T-Mobile US unite for 6G R&D | [링크](https://www.telecomtv.com/content/6g/mwc26-dt-t-mobile-us-unite-for-6g-r-d-54958/) | news | 2026-03-02 | [B] |
| <a id="ref-g-09"></a>G-09 | Korea IT Times — SK telecom Declares Shift to 'AI Native' Company at MWC 2026 | [링크](https://www.koreaittimes.com/news/articleView.html?idxno=151344) | news | 2026-03-01 | [B] |
| <a id="ref-g-10"></a>G-10 | The Fast Mode — SoftBank Delivers World-First SRv6 MUP Services on 5G Commercial Network | [링크](https://www.thefastmode.com/technology-solutions/46488-softbank-delivers-world-first-srv6-mup-services-on-5g-commercial-network) | news | 2025-12 | [B] |
| <a id="ref-g-11"></a>G-11 | 3GPP — AI/ML for NG-RAN & 5G-Advanced towards 6G | [링크](https://www.3gpp.org/technologies/ai-ml-ngran) | 표준 | 2026-03 | [A] |
| <a id="ref-g-12"></a>G-12 | NVIDIA Technical Blog — Boosting AI-Driven Innovation in 6G with the AI-RAN Alliance, 3GPP, and O-RAN | [링크](https://developer.nvidia.com/blog/boosting-ai-driven-innovation-in-6g-with-the-ai-ran-alliance-3gpp-and-o-ran/) | blog | 2026-02 | [B] |
| <a id="ref-g-13"></a>G-13 | Precedence Research — AI-RAN Market Size to Hit USD 37.19 Billion by 2035 | [링크](https://www.precedenceresearch.com/ai-ran-market) | report | 2026 | [C] |
| <a id="ref-g-14"></a>G-14 | Precedence Research — Open RAN Market Size to Hit USD 46.33 Billion by 2035 | [링크](https://www.precedenceresearch.com/open-ran-market) | report | 2026 | [C] |
| <a id="ref-g-15"></a>G-15 | Opensignal — 5G Standalone State of Play: Architecture Deployed, Monetisation Pending | [링크](https://insights.opensignal.com/2026/02/5g-standalone-state-of-play-architecture-deployed-monetisation-pending/dt) | report | 2026-02 | [B] |
| <a id="ref-g-16"></a>G-16 | Fierce Network — MWC 2026: Intel sits out AI-RAN Alliance, for now | [링크](https://www.fierce-network.com/wireless/mwc-2026-intel-sits-out-ai-ran-alliance-now) | news | 2026-03-02 | [B] |
| <a id="ref-g-17"></a>G-17 | TechSpot — At MWC 2026, the telecom industry pivoted from 5G to AI-powered 6G | [링크](https://www.techspot.com/news/111597-mwc-2026-telecom-industry-pivoted-5g-ai-powered.html) | news | 2026-03-02 | [B] |
| <a id="ref-g-18"></a>G-18 | Light Reading — T-Mobile's AI RAN plan is more than Nvidia | [링크](https://www.lightreading.com/ai-machine-learning/t-mobile-s-ai-ran-plan-is-more-than-nvidia) | news | 2026-03 | [B] |
| <a id="ref-g-19"></a>G-19 | TelecomLead — Global 5G Investment and Deployment Trends 2025-2026 (GSA) | [링크](https://telecomlead.com/5g/global-5g-investment-and-deployment-trends-2025-2026-insights-from-gsa-123755) | report | 2026-02 | [B] |
| <a id="ref-g-20"></a>G-20 | EE Times — Nokia Bets the Network on Nvidia in AI and 6G Pivot | [링크](https://www.eetimes.com/nokia-bets-the-network-on-nvidia-in-ai-and-6g-pivot/) | news | 2026-03 | [B] |
| <a id="ref-g-21"></a>G-21 | HyperFRAME Research — MWC26: Nokia and NVIDIA Advance Blueprint for a Distributed AI Factory | [링크](https://hyperframeresearch.com/2026/03/05/mwc26-nokia-and-nvidia-advance-blueprint-for-a-distributed-ai-factory/) | blog | 2026-03-05 | [C] |
| <a id="ref-g-22"></a>G-22 | Booz Allen — AI-RAN and the Race to 6G | [링크](https://www.boozallen.com/insights/velocity/ai-ran-and-the-race-to-6g.html) | blog | 2026 | [C] |
| <a id="ref-n-01"></a>N-01 | Telecom Review Asia — Indosat, Nokia, NVIDIA Complete Southeast Asia's First AI-Powered 5G Call at MWC26 | [링크](https://www.telecomreviewasia.com/news/technology-news/28548-indosat-nokia-nvidia-complete-southeast-asias-first-ai-powered-5g-call-at-mwc26/) | news | 2026-03-02 | [B] |
| <a id="ref-n-02"></a>N-02 | SDxCentral — Broadcom's VMware, Arrcus power SoftBank SRv6 MUP success | [링크](https://www.sdxcentral.com/news/broadcoms-vmware-arrcus-power-softbank-srv6-mup-success/) | news | 2025 | [B] |
| <a id="ref-p-01"></a>P-01 | Kundu et al. — AI-RAN: Transforming RAN with AI-driven Computing Infrastructure | [링크](https://arxiv.org/abs/2501.09007) | paper | 2025-01 | [A] |
| <a id="ref-p-02"></a>P-02 | Han et al. — Toward E2E Intelligence in 6G Networks: An AI Agent-Based RAN-CN Converged Intelligence Framework | [링크](https://arxiv.org/abs/2602.23623) | paper | 2026-02 | [A] |
| <a id="ref-p-03"></a>P-03 | Shokouhi & Wong — Agentic AI for Intent-driven Optimization in Cell-free O-RAN | [링크](https://arxiv.org/abs/2602.22539) | paper | 2026-02 | [A] |
| <a id="ref-p-04"></a>P-04 | IEEE Xplore — Embracing AI in 5G-Advanced Toward 6G: A Joint 3GPP and O-RAN Perspective | [링크](https://ieeexplore.ieee.org/document/10353004/) | paper | 2023 | [A] |
| <a id="ref-p-05"></a>P-05 | The Mobile Network — AI-RAN: untying the knot for 6G | [링크](https://the-mobile-network.com/2026/02/ai-ran-untying-the-knot-for-6g/) | blog | 2026-02 | [C] |
