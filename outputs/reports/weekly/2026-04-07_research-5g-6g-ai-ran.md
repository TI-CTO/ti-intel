---
type: weekly-research
topic: 5g-6g-ai-ran
date: 2026-04-07
parent: 2026-04-07_weekly-agentic-ai.md
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
---

# 심층 리서치: 5G SA/6G (AI-RAN/SRv6) — 2026-W16

## 핵심 요약

NTT DOCOMO와 SK Telecom(SKT)이 2026-03-31 공동 백서를 발간하며 virtualized RAN(vRAN) 진화와 AI-RAN(AI-Centric RAN) 전환을 위한 3대 기술 요건(HW/SW 분리, 리소스 풀링, xPU 기반 AI 컴퓨팅)을 통신사 관점에서 공식 정의했다. Samsung은 Intel Xeon 6 SoC 기반 vRAN으로 유럽 첫 상용 콜(Vodafone)을 달성하며 AI-native 상용화 궤도 진입을 가속화했다. 3GPP Release 21 일정은 2026년 6월까지 확정 예정으로, 6G 표준화의 공식 출발선이 가시화되고 있다.

---

## 기술 동향

1. **DOCOMO-SKT 공동 백서 발간 — 통신사 관점의 AI-RAN 3대 기술 요건 공식화.**
   NTT DOCOMO와 SKT는 2026-03-31 "Requirements for Advancing vRAN and AI-RAN in Mobile Networks" 백서를 공동 발간했다. 백서는 양사의 실제 네트워크 구축·운영 경험을 바탕으로 통신사 관점(mobile operator's perspective)에서 vRAN 및 AI-RAN 발전에 필수적인 3가지 기술 요건을 정의한다: (1) **HW/SW 분리** — RAN 소프트웨어를 특정 하드웨어 및 가상화 플랫폼에서 분리하여 소프트웨어 독립 배포 가능, (2) **리소스 풀링** — 서비스 품질을 유지하면서 용량 개선 및 전력 소비 절감, (3) **AI 컴퓨팅 능력** — xPU(CPU·GPU 등 정보처리 유닛의 총칭) 기반 아키텍처와 리소스 오케스트레이션을 통해 기지국이 이동통신 서비스 품질을 저해하지 않으면서 AI 컴퓨팅을 제공. 이는 vRAN을 이동통신 플랫폼에서 이동통신과 AI 서비스를 함께 제공하는 통합 AI 플랫폼으로 진화시키는 것을 목표로 한다. SKT Yu Takki 네트워크기술실장은 "통신사 관점에서 vRAN 혜택을 극대화하는 데 필수적인 핵심 기능을 제시한다"고 발언했다. 양사는 2022년 11월 5G Evolution·6G 기술 연구 협력협약을 체결한 배경에서 나온 성과다. [[G-01]](#ref-g-01) [[E-01]](#ref-e-01)

2. **Samsung vRAN + Intel Xeon 6 SoC — 유럽 최초 AI-native vRAN 상용 콜 달성.**
   Samsung Electronics와 Vodafone이 Intel Xeon 6 SoC(System-on-Chip) 기반 Samsung vRAN 솔루션으로 유럽 최초 콜을 완료했다. 동 칩은 2G·4G·5G 네트워크를 단일 고성능 서버에서 동시 지원하는 집중적 워크로드, AI 애플리케이션을 처리하는 vRAN 최적화 SoC다. Dell Technologies(서버), Wind River Studio 클라우드 플랫폼과 협력하여 구현되었으며, 2026년 중 상용 배포 예정이다. 이 구성은 Vodafone이 관리 시스템과 하드웨어 수를 줄이면서 기존 RAN 기저대역 솔루션과 동등 또는 우수한 성능을 달성, 비용·에너지 소비를 절감하고 AI 도입 유연성을 확보하는 것을 목표로 한다. 별도로 Samsung은 2026년 1월 Intel Xeon 6700P-B(최대 72코어) 프로세서를 사용하여 미국 Tier 1 통신사 상용 네트워크에서 업계 최초 vRAN 상용 콜을 달성한 바 있다. [[G-02]](#ref-g-02) [[E-02]](#ref-e-02)

3. **NVIDIA-Nokia 6G AI 플랫폼 협력 — L1 RAN 전체를 CUDA 플랫폼으로 설계.**
   Nokia는 MWC 2026(2026-03-01)에서 NVIDIA와의 전략적 AI-RAN 파트너십 진전을 발표했다. Nokia anyRAN 소프트웨어를 NVIDIA GPU 가속 AI-RAN 플랫폼 위에서 실증하는 기능 테스트를 T-Mobile, Indosat Ooredoo Hutchison(IOH), SoftBank와 각각 성공적으로 완료했다. 핵심 아키텍처 전환으로 Nokia는 IT 자원을 가장 많이 소비하는 Layer 1(L1) RAN 전체를 NVIDIA CUDA 플랫폼과 GPU에서 구동하도록 설계할 예정이다. 또한 Nokia와 NVIDIA는 Red Hat과 협력하여 Red Hat OpenShift 및 Red Hat AI Enterprise 기반 클라우드 네이티브 통합 플랫폼에서 AI-RAN 기술을 스케일 아웃하는 작업도 진행 중이다. IOH는 MWC에서 Southeast Asia 최초 AI RAN 기반 L3 5G 콜을 시연했으며, SoftBank는 AITRAS Orchestrator로 여유 AI-RAN 컴퓨팅 자원을 식별하여 제3자 AI 태스크를 구동하는 수익화 모델을 제시했다. [[G-03]](#ref-g-03) [[E-03]](#ref-e-03)

4. **NVIDIA-12사 6G AI-native 연합 — MWC 2026 최대 규모 업계 공약.**
   NVIDIA는 2026-02-28 MWC에서 Booz Allen, BT Group, Cisco, Deutsche Telekom, Ericsson, MITRE, Nokia, SK Telecom, SoftBank, T-Mobile 등 11개 기관과 함께 "AI-native, 개방형, 보안·신뢰 가능한 플랫폼" 위에 6G 네트워크를 구축하겠다는 공약을 발표했다. Jensen Huang NVIDIA CEO는 "AI가 컴퓨팅을 재정의하고 있으며 통신이 다음 차례"라고 발언했다. T-Mobile은 Nokia AirScale massive MIMO 무선(3.7GHz)으로 5G 서비스와 동시에 비디오 스트리밍·생성형 AI·AI 캡셔닝 애플리케이션을 공중(over-the-air) 실증했다. AI-RAN Alliance는 현재 130개 이상 참여사를 보유하고 있으며, NVIDIA는 2025년 10월 AI-WIN(AI-Native Wireless Networks) 프로젝트도 발족시켰다. [[G-04]](#ref-g-04) [[E-04]](#ref-e-04)

5. **Ericsson-Intel 협력 — ASIC 전략에 COTS 컴퓨팅 통합, AI-native 6G 생태계 확장.**
   Ericsson과 Intel은 MWC 2026에서 AI-native 6G 상용화 경로 가속을 위해 모바일 연결, 클라우드 기술, AI 기반 RAN·패킷 코어 컴퓨팅 역량을 결합한다고 발표했다. Ericsson의 Erik Ekudden CTO는 "우리는 이미 인텔리전트 패브릭을 향한 여정 위에 있고 지금 일어나고 있다"고 말했다. Ericsson은 Qualcomm, MediaTek·Apple(디바이스 에코시스템), Linux Foundation OCUDU(오픈소스 CU/DU)와도 파트너십을 맺어 경쟁사 Nokia와 차별화된 멀티 파트너 전략을 구사하고 있다. Nokia가 NVIDIA GPU 플랫폼에 L1 RAN을 올리는 것과 달리 Ericsson은 자체 Silicon(ASIC)을 주축으로 NVIDIA·Intel·Qualcomm에 모두 연결되는 이종(heterogeneous) 구조를 추구한다. [[G-05]](#ref-g-05) [[E-05]](#ref-e-05)

6. **Ericsson-T-Mobile 포터블 AI-RAN 실증 — 하드웨어 독립 RAN 소프트웨어 이식성 확인.**
   Ericsson Cloud RAN 소프트웨어를 NVIDIA AI 인프라(NVIDIA Aerial CUDA 기술) 위에서 구동하는 공중 실증이 워싱턴주 Bellevue의 AI-RAN Innovation Center에서 완료됐다. Ericsson의 Mårten Lerner는 "Cloud RAN 소프트웨어는 설계 자체가 포터블(portable by design)이며, 동일 RAN 소프트웨어 스택이 Ericsson Silicon, NVIDIA 인프라, 기타 COTS 솔루션 등 여러 하드웨어 플랫폼에서 동일하게 실행된다"고 강조했다. T-Mobile의 Ankur Kapoor는 "이번 실증은 연결성 제공업체에서 인텔리전트 플랫폼으로의 진화를 보여준다"고 발언했다. [[E-06]](#ref-e-06) [[G-06]](#ref-g-06)

7. **3GPP Release 21 일정 — 2026년 6월 최종 결정, 6G 표준화 공식 시작점.**
   3GPP는 Release 21(사실상 최초 6G 스펙) 작업 기간을 2026년 6월까지 확정할 예정이다. 현재 RAN 수준 요구사항 연구 단계(Release 20)가 2024년 9월 시작되어 2026년 6월 완료 목표로 진행 중이며, 기술 작업 그룹에서의 실질 작업은 2025년 3분기에 착수했다. Release 21은 21개월 기간이 예상되며, 3GPP 사양(ASN.1/OpenAPI 동결)은 2029년 3월로 전망된다. Ericsson은 6G 스펙이 2028년 말까지 완성되어 2030년 첫 상용 6G 시스템 출시를 가능하게 할 것이라고 전망한다. [[G-07]](#ref-g-07)

8. **O-RAN Alliance·AI-RAN Alliance 통합 추진 — AI-native RAN의 표준·생태계 양축 성숙.**
   AI-RAN Alliance는 MWC 2026 기준 132개 회원사를 보유하며, Qualcomm·SKT·Vodafone을 신규 이사회 멤버로 영입했다. MWC에서 33개 AI 혁신 데모를 선보이며 AI-RAN Reference Architecture 프레임워크, AI/ML 기법 보고서, 플랫폼·인프라 오케스트레이션 문서, AI-on-RAN 수익화 백서 등 4개 기초 간행물을 발표했다. O-RAN Alliance 통계에 따르면 Omdia의 2026 Open RAN 오퍼레이터 조사에서 13%가 "O-RAN을 전략적으로 적극 배포 중", 27%가 "O-RAN 원칙이 RAN 진화를 가이드 중"으로 합산 40%가 의미 있는 채택 상태다. 단, Intel은 AI-RAN Alliance에 불참하며 "기존 표준 기구와 Xeon CPU가 이미 RAN AI를 지원한다"는 입장을 고수하고 있다. [[G-08]](#ref-g-08) [[G-09]](#ref-g-09)

9. **Qualcomm Agentic RAN 관리 서비스 출시 — 자율 6G 네트워크 경로 개척.**
   Qualcomm은 MWC 2026(2026-03-01)에서 상용 RAN 플랫폼을 위한 Agentic RAN Management Service를 Dragonwing RAN Automation Suite 내에 출시했다. 이 서비스는 단순 자동화를 넘어 RAN AI 에이전트들이 협력하여 네트워크 상태를 공동 모니터링, 이슈를 분석, 액션 플랜을 생성·테스트, 자율적으로 변경을 실행하는 6G급 자율 네트워크를 목표로 한다. 6G 칩 관련으로는 3개 축인 연결성·광역 센싱·고성능 컴퓨팅을 AI-native 설계 원칙으로 통합하는 방향을 제시했으며, Arm 기반 Oryon CPU를 포함한 통합 6G급 텔코 서버 개발도 논의 중이다. [[G-10]](#ref-g-10) [[E-07]](#ref-e-07)

10. **SRv6(Segment Routing over IPv6) 글로벌 확산 — 5G·6G 백홀 네트워크 기반 프로토콜로 부상.**
    SRv6는 트래픽 분리(L3VPN), 도메인 간 엔드투엔드 트래픽 엔지니어링, 네트워크 슬라이싱, SLA 집행, 50ms 미만 경로 복원 등의 기능을 제공하며 5G 이상 백홀 네트워크의 기본 프로토콜로 자리잡고 있다. SoftBank, Iliad, China Mobile이 모바일 네트워크에 SRv6를 운영 중이며, SoftBank는 Arrcus와 함께 SRv6 MUP(Mobile User Plane) 솔루션을 세계 최초로 상용 도입했다. Jio는 SRv6 프로그래머빌리티를 AI 워크로드와 5G/6G 서비스 최적화에 활용하는 미래지향 IP 네트워크 아키텍처를 구축 중이며, 1억 가구와 6억 모바일·기업 고객을 연결하는 4배 트래픽 증가를 목표로 한다. [[G-11]](#ref-g-11) [[G-12]](#ref-g-12)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| NTT DOCOMO | SKT와 공동으로 "Requirements for Advancing vRAN and AI-RAN" 백서 발간(2026-03-31). 91만 명 이상 가입자 보유 통신사 관점의 AI-RAN 3대 요건 정의 | [[G-01]](#ref-g-01), [[E-01]](#ref-e-01) |
| SK Telecom | DOCOMO와 AI-RAN 백서 공동 발간. MWC에서 AI-native 전사 전략 선언. Ericsson과 5년 MoU 체결(2026-03-18, 만료 2031-03). NVIDIA 6G 연합 참여. AI-RAN Alliance 이사회 멤버 합류 | [[G-01]](#ref-g-01), [[E-01]](#ref-e-01), [[E-08]](#ref-e-08) |
| Samsung | Intel Xeon 6700P-B 기반 vRAN으로 미국 Tier 1 통신사 업계 최초 상용 콜(2026-01). Vodafone과 Intel Xeon 6 SoC로 유럽 최초 vRAN 콜 완료(2026 상용 배포 예정). NVIDIA와 AI-native 소프트웨어 정의 네트워크 협력 | [[G-02]](#ref-g-02), [[E-02]](#ref-e-02) |
| Nokia | anyRAN으로 T-Mobile·IOH·SoftBank와 GPU 가속 AI-RAN 기능 테스트 완료. L1 RAN 전체를 NVIDIA CUDA 플랫폼에서 구동하는 설계 방향 확정. Doksuri 무선 신제품 출시. Red Hat과 OpenShift 기반 클라우드 네이티브 AI-RAN 통합 | [[G-03]](#ref-g-03), [[E-03]](#ref-e-03) |
| Ericsson | T-Mobile과 Cloud RAN 포터블 AI-RAN 실증 완료. Intel·Qualcomm·MediaTek·Apple·OCUDU와 파트너십으로 멀티 생태계 전략 추진. ASIC 기반 독립 아키텍처 유지하면서 NVIDIA와도 협력. SKT와 5년 MoU 체결 | [[E-05]](#ref-e-05), [[E-06]](#ref-e-06), [[G-05]](#ref-g-05) |
| NVIDIA | 2026-02-28 12사와 6G AI-native 연합 결성. AI-RAN Alliance 130개+ 회원사. Aerial 소프트웨어 Apache 2.0 오픈소스화. T-Mobile과 물리적 AI 애플리케이션 AI-RAN 엣지 통합 실증 | [[G-04]](#ref-g-04), [[E-04]](#ref-e-04) |
| Qualcomm | AI-RAN Alliance 신규 이사회 멤버. Dragonwing RAN Automation Suite 내 Agentic RAN Management Service 출시. X105 5G 모뎀(세계 최초 Release 19 지원) 샘플링 시작. AI-native 6G 3축 비전(연결·감지·고성능 컴퓨팅) 제시 | [[G-10]](#ref-g-10), [[E-07]](#ref-e-07) |
| Intel | AI-RAN Alliance 불참 입장 유지("기존 표준 기구와 Xeon이 이미 충분"). Samsung·Vodafone vRAN용 Xeon 6 SoC 공급. Ericsson과 AI-native 6G 협력 발표 | [[G-09]](#ref-g-09) |
| Vodafone | Samsung + Intel Xeon 6 SoC로 유럽 최초 vRAN 콜 완료. AI-RAN Alliance 신규 이사회 멤버. 2027년까지 영국 2,500 사이트 Open RAN 목표. 유럽 기지국 30%를 2030년까지 Open RAN 전환 목표 | [[G-02]](#ref-g-02), [[G-08]](#ref-g-08) |

---

## 시장 시그널

**투자 & M&A**

- AI-RAN 글로벌 시장 규모 2025년 29.6억 달러 → 2026년 38.1억 달러로 성장 전망, 2035년 371.9억 달러(연평균 성장률(CAGR) 28.79%) [[G-13]](#ref-g-13) [추가확인 필요]
- Open RAN 시장 2025년 65.3억 달러 → 2026년 85.7억 달러, 2033년 450.9억 달러(CAGR 26.8%) [[G-14]](#ref-g-14) [추가확인 필요]
- AT&T가 Ericsson과 체결한 Open RAN 5년 계약(최대 140억 달러)은 단일 오퍼레이터 역대 최대 Open RAN 계약이며, 2026년 말까지 무선 트래픽의 70%를 오픈 지원 플랫폼으로 전환 목표 [[G-14]](#ref-g-14)

**파트너십 & 제휴**

- NVIDIA와 Marvell이 NVLink Fusion 플랫폼을 활용한 AI-RAN 인프라 확장 파트너십 체결 [[G-09]](#ref-g-09)
- SKT-Ericsson 5년 MoU(2026-03-18): AI-powered RAN, 5G 수익화, 오픈·자율 네트워크, Zero Trust 보안, 6G 표준화 5개 영역 [[E-08]](#ref-e-08)
- QCT(Quanta Cloud Technology)가 Nokia anyRAN·NVIDIA ARC-Pro 지원 AI-RAN 서버 QuantaEdge EGN77C-2U 발표 [[G-15]](#ref-g-15)

**시장 전망**

- Omdia 2026 Open RAN 오퍼레이터 조사: "전략적 적극 배포 중" 13% + "원칙이 미래 진화 가이드" 27% = 의미 있는 채택 40% [[G-08]](#ref-g-08)
- 북미가 AI-RAN 시장 37% 점유(2025), 2035년까지 139.5억 달러 규모 성장 예상 [[G-13]](#ref-g-13)
- 아시아·태평양이 AI-RAN 최고속 성장 지역(CAGR 25.5%, 2026-2035) [[G-13]](#ref-g-13)
- Qualcomm: 6G 프리커머셜 작업 2028년(로스앤젤레스 올림픽 시점), 상용화 2029년 목표 [[G-10]](#ref-g-10)

**도입 사례**

- Deutsche Telekom: 독일 내 3,000개 이상 사이트에 Open RAN 배포 완료(Huawei → Nokia+Fujitsu 교체) [[G-14]](#ref-g-14)
- Bharti Airtel: Mavenir과 협력하여 인도 농촌 지역 2,500개 Open RAN 사이트 배포(10,000개로 확장 옵션 포함) [[G-14]](#ref-g-14)
- SoftBank: Arrcus와 SRv6 MUP(Mobile User Plane) 세계 최초 상용 도입 [[G-12]](#ref-g-12)
- Zain Kuwait: SRv6 1단계 배포 완료 발표(MENOG24) [[G-12]](#ref-g-12)

**연구 동향**

- IEEE INFOCOM 2026 산하 "6G AI-RAN 2026" 워크숍 개최: AI-native 분산 인텔리전스, 학습 기반 아키텍처, AI 강화 신호처리, 스펙트럼 할당이 핵심 주제 [[G-16]](#ref-g-16)
- Frontiers에 "AI-native 6G 종합 리뷰" 게재(2025): 시맨틱 통신, Reconfigurable Intelligent Surface(RIS), 엣지 인텔리전스 통합 아키텍처 제안 [[P-01]](#ref-p-01)
- 통합 감지·통신(ISAC) 기술의 6G 주요 기능 확정 예상되나 초기 6G 롤아웃에는 미포함 전망. 주류 ISAC 배포는 2030년 이후 예측 [[G-17]](#ref-g-17)
- Nature Communications에 광대역 실시간 스펙트럼 감지 관련 6G 무선 네트워크 논문 게재(2026) [[P-02]](#ref-p-02)

**커뮤니티 시그널**

- AI-RAN Alliance MWC 2026에서 33개 데모 발표, 130+ 회원사. 업계 전반의 집결 속에서도 Intel 불참은 주요 이슈 [[G-09]](#ref-g-09)
- lightreading.com 분석: "Ericsson과 Nokia는 AI-RAN에서 어느 때보다 큰 차이를 벌리고 있다" — Ericsson의 이기종 전략 vs Nokia의 CUDA 중심 전략 [[G-05]](#ref-g-05)

---

## 전략적 시사점

**기회**

- SKT가 DOCOMO와 공동 백서를 통해 vRAN→AI-RAN 전환의 기술 요건을 표준화 의제로 선점. Ericsson MoU(5년)와 결합하면 국내 6G 상용화 공급망에서 주도적 위치 확보 가능
- AI-RAN을 "이동통신 + AI 컴퓨팅 통합 플랫폼"으로 포지셔닝하면 기지국 인프라가 엣지 AI 서비스 플랫폼으로 확장되어 통신사의 새로운 수익원 창출 시나리오 유효
- SRv6 기반 백홀 구축은 네트워크 슬라이싱·5G SA 서비스 차별화 기반으로, Jio·SoftBank 등 선행 사례가 벤치마킹 가능한 레퍼런스를 제공
- Open RAN 40% 채택률(Omdia 2026)과 AT&T 140억 달러 계약 사례는 국내 통신사의 Open RAN 전환 비즈니스 케이스 수립에 활용 가능

**위협**

- NVIDIA GPU 중심 AI-RAN 생태계가 빠르게 고착화될 경우 삼성·Qualcomm 등 ASIC/CPU 진영의 벤더 다양성이 제한되고 비용 경쟁력 약화 우려
- Intel의 AI-RAN Alliance 불참은 단기적으로 생태계 분열 리스크 — Xeon 기반 vRAN(Samsung/Vodafone 검증)과 GPU 기반 AI-RAN(NVIDIA 진영) 간 표준 충돌 가능성
- 3GPP Release 21 일정이 2026년 6월에 확정되더라도 ASN.1 동결은 2029년 3월로, 실제 6G 표준화까지 3년 이상 공백기. 그 기간 동안 특정 벤더 솔루션의 사실상(de facto) 표준화 위험
- Ericsson-Nokia의 AI-RAN 전략적 분기(Ericsson ASIC 이기종 vs Nokia CUDA 집중)는 통신사의 벤더 선택에 불확실성 증가 요인

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | NTT DOCOMO — DOCOMO and SK Telecom Publish White Paper on Requirements for Advancing vRAN and AI-RAN | [링크](https://www.docomo.ne.jp/english/info/media_center/pr/2026/0331_00.html) | press-release | 2026-03-31 | [A] |
| <a id="ref-g-02"></a>G-02 | Samsung Global Newsroom — Samsung and Vodafone Drive the Future of AI-Native Networks Across Europe | [링크](https://news.samsung.com/global/samsung-and-vodafone-drive-the-future-of-ai-native-networks-across-europe-with-successful-validation-of-a-new-chipset) | press-release | 2026-03 | [A] |
| <a id="ref-g-03"></a>G-03 | Nokia Newsroom — Nokia accelerates AI-RAN momentum with new partnerships driving path to AI-Native 6G #MWC26 | [링크](https://www.nokia.com/newsroom/nokia-accelerates-ai-ran-momentum-with-new-partnerships-driving-path-to-ai-native-6g-mwc26/) | press-release | 2026-03-01 | [A] |
| <a id="ref-g-04"></a>G-04 | NVIDIA Newsroom — NVIDIA and Global Telecom Leaders Commit to Build 6G on Open and Secure AI-Native Platforms | [링크](https://nvidianews.nvidia.com/news/nvidia-and-global-telecom-leaders-commit-to-build-6g-on-open-and-secure-ai-native-platforms) | press-release | 2026-02-28 | [A] |
| <a id="ref-g-05"></a>G-05 | Light Reading — Ericsson and Nokia are diverging like never before on AI-RAN | [링크](https://www.lightreading.com/5g/ericsson-and-nokia-are-diverging-like-never-before-on-ai-ran) | news | 2026-03 | [B] |
| <a id="ref-g-06"></a>G-06 | T-Mobile Newsroom — T-Mobile and Ericsson Advance Portable AI RAN Software On NVIDIA AI Infrastructure | [링크](https://www.t-mobile.com/news/network/t-mobile-and-ericsson-advance-portable-ai-ran-software-on-nvidia-ai-infrastructure) | press-release | 2026-03 | [A] |
| <a id="ref-g-07"></a>G-07 | Ericsson — 6G standardization timeline and technology principles | [링크](https://www.ericsson.com/en/blog/2024/3/6g-standardization-timeline-and-technology-principles) | blog | 2024-03 | [B] |
| <a id="ref-g-08"></a>G-08 | AI-RAN Alliance — MWC 2026 Momentum Press Release | [링크](https://ai-ran.org/press-releases/mwc-2026-momentum) | press-release | 2026-02-26 | [A] |
| <a id="ref-g-09"></a>G-09 | Fierce Network — MWC 2026: Intel sits out AI-RAN Alliance, for now | [링크](https://www.fierce-network.com/wireless/mwc-2026-intel-sits-out-ai-ran-alliance-now) | news | 2026-03 | [B] |
| <a id="ref-g-10"></a>G-10 | Qualcomm Newsroom — Qualcomm Launches Agentic RAN Management Service and AI Enhancements | [링크](https://www.qualcomm.com/news/releases/2026/03/qualcomm-launches-agentic-ran-management-service-and-ai-enhancem) | press-release | 2026-03-01 | [A] |
| <a id="ref-g-11"></a>G-11 | Light Reading — SKT and NTT Docomo define the path to vRAN and AI-RAN | [링크](https://www.lightreading.com/virtualization/skt-and-ntt-docomo-define-the-path-to-vran-and-ai-ran) | news | 2026-04-02 | [B] |
| <a id="ref-g-12"></a>G-12 | APNIC Blog — SRv6: Deployed use-cases | [링크](https://blog.apnic.net/2020/05/08/srv6-deployed-use-cases/) | blog | 2020-05 | [B] |
| <a id="ref-g-13"></a>G-13 | Precedence Research — AI-RAN Market Size to Hit USD 37.19 Billion by 2035 | [링크](https://www.precedenceresearch.com/ai-ran-market) | market-report | 2026 | [C] |
| <a id="ref-g-14"></a>G-14 | 5G World Pro — The Real 5G Open RAN Numbers in 2026 | [링크](https://5gworldpro.com/blog/2026/03/10/the-real-5g-open-ran-numbers-in-2026) | blog | 2026-03-10 | [C] |
| <a id="ref-g-15"></a>G-15 | National Law Review — QCT Unveils QuantaEdge EGN77C-2U, New AI-RAN Server Supporting Nokia anyRAN and NVIDIA ARC-Pro | [링크](https://natlawreview.com/press-releases/qct-unveils-quantaedge-egn77c-2u-new-ai-ran-server-supporting-nokia-anyran) | press-release | 2026-03 | [A] |
| <a id="ref-g-16"></a>G-16 | IEEE INFOCOM 2026 — First Workshop on AI Native Distributed Intelligence for 6G Networks (6G AI-RAN 2026) | [링크](https://infocom2026.ieee-infocom.org/first-workshop-ai-native-distributed-intelligence-6g-networks-6g-ai-ran-2026-call-papers) | conference | 2026 | [A] |
| <a id="ref-g-17"></a>G-17 | Fierce Network — 6G and integrated sensing: What comes next for ISAC | [링크](https://www.fierce-network.com/wireless/isacs-web-6g-and-sensing) | news | 2026 | [B] |
| <a id="ref-e-01"></a>E-01 | SK Telecom — Yu Takki 발언 (DOCOMO-SKT 백서 공동 발간) | [링크](https://en.acnnewswire.com/press-release/english/106047/docomo-and-sk-telecom-publish-white-paper-on-requirements-for-advancing-vran-and-ai-ran-in-mobile-networks) | press-release | 2026-03-31 | [A] |
| <a id="ref-e-02"></a>E-02 | Samsung Business Global Networks — Samsung and Vodafone Drive the Future of AI-Native Networks | [링크](https://www.samsung.com/global/business/networks/insights/press-release/0303-samsung-and-vodafone-drive-the-future-of-ai-native-networks-across-europe-with-successful-validation-of-a-new-chipset/) | press-release | 2026-03-03 | [A] |
| <a id="ref-e-03"></a>E-03 | Nokia Newsroom — NVIDIA and Nokia to Pioneer the AI Platform for 6G | [링크](https://www.nokia.com/newsroom/nvidia-and-nokia-to-pioneer-the-ai-platform-for-6g--powering-americas-return-to-telecommunications-leadership/) | press-release | 2026-02-28 | [A] |
| <a id="ref-e-04"></a>E-04 | NVIDIA Investor Relations — NVIDIA and Global Telecom Leaders Commit to Build 6G | [링크](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Global-Telecom-Leaders-Commit-to-Build-6G-on-Open-and-Secure-AI-Native-Platforms/default.aspx) | IR | 2026-02-28 | [A] |
| <a id="ref-e-05"></a>E-05 | Ericsson — Ericsson leads the 6G journey toward an intelligent fabric at MWC 2026 | [링크](https://www.ericsson.com/en/press-releases/2026/3/ericsson-leads-the-6g-journey-toward-an-intelligent-fabric-at-mwc-2026) | press-release | 2026-03 | [A] |
| <a id="ref-e-06"></a>E-06 | Ericsson Newsroom — Ericsson and T-Mobile test portable AI RAN on NVIDIA platform | [링크](https://www.ericsson.com/en/news/2026/3/ericsson-t-mobile-boost-portable-ai-ran-on-nvidia-platform) | press-release | 2026-03 | [A] |
| <a id="ref-e-07"></a>E-07 | Qualcomm — Qualcomm accelerates 6G with AI-native device-to-data-center network transformation | [링크](https://www.qualcomm.com/news/onq/2026/03/qualcomm-6g-device-to-data-center-transformation) | blog | 2026-03 | [A] |
| <a id="ref-e-08"></a>E-08 | Ericsson Korea — SKT-Ericsson AI-RAN 및 6G 기술혁신 MoU 체결 | [링크](https://www.ericsson.com/ko/news/2/2026/skt-6g-mou) | press-release | 2026-03-18 | [A] |
| <a id="ref-p-01"></a>P-01 | Frontiers — A comprehensive review of AI-native 6G: integrating semantic communications, RIS, and edge intelligence | [링크](https://www.frontiersin.org/journals/communications-and-networks/articles/10.3389/frcmn.2025.1655410/full) | paper | 2025 | [A] |
| <a id="ref-p-02"></a>P-02 | Nature Communications — Integrated photonic ultrawideband real-time spectrum sensing for 6G wireless networks | [링크](https://www.nature.com/articles/s41467-026-70389-0) | paper | 2026 | [A] |
