---
type: weekly-research
topic: context-action-recommendation
week: 2026-W15
date: 2026-04-06
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
---

# Deep 리서치: 컨텍스트 기반 액션 추천 (W15)

## 이전 대비 변화

- **전주 (W14)**: Lenovo Qira 프로액티브 AI 슈퍼에이전트(CES 2026) 발표. "프롬프트 이전에 행동"하는 패러다임 전환 논의 부상. Apple Siri+Gemini 통합(iOS 26.4) 지연 우려.
- **금주 (W15)**: Apple Siri 개선이 iOS 26.5에서도 부재 → iOS 27(WWDC 2026) 이전 출시 불가 확정. Salesforce Slackbot이 **데스크톱 컨텍스트 인식** 기능 추가(30개 AI 기능 발표, 3/31). Samsung Galaxy S26 "Now Nudge" 크로스앱 추천 공개(MWC 2026). Anthropic "Conway" 상시 구동 에이전트 플랫폼 테스트 시작(4/3).
- **변화 방향**: 컨텍스트 인식 범위가 **단일 앱 → 크로스앱 → 데스크톱 전체**로 확장되는 궤적이 뚜렷해짐. 소비자 디바이스(Samsung, Apple)와 엔터프라이즈 플랫폼(Slackbot, Glean, Microsoft 365 Copilot) 양쪽에서 동시 경쟁이 가속 중. 학술계에서는 Agentic Recommender System (AgenticRS) 프레임워크가 정립 단계에 진입(arXiv 2603.26100, 3/27).

---

## 기술 동향

1. **Apple Siri 개선, iOS 26.5 베타에도 부재 → iOS 27 이전 출시 불가 확정 (3/30)**
   MacRumors(Mark Gurman/Bloomberg 인용)가 3월 30일 보도한 바에 따르면, iOS 26.5 초기 베타에 새로운 Apple Intelligence Siri 기능이 포함되지 않았다. 당초 iOS 26.4(3월 출시 목표) → iOS 26.5(5월) 순으로 연기되었으나, 26.5 베타에도 기능이 없어 사실상 iOS 27(2026년 9월, WWDC 이후 출시) 이전 탑재는 불가능한 상황이다. WWDC 2024에서 최초 공개 이후 **약 2년 지연**이다 [[G-01]](#ref-g-01). 지연 원인은 정확도 문제(쿼리 미처리, 응답 지연)로, Apple 내부 엔지니어들이 iOS 26.4 테스트 중 발견했다고 알려졌다 [[G-02]](#ref-g-02).

2. **Apple-Google Gemini 딜: $1B/년, Private Cloud Compute 기반 (1/12 발표)**
   Apple은 1월 12일 Google과 Gemini 모델 기반 멀티연도 협력을 발표했다. Gemini가 차세대 Apple Foundation Model의 기반이 되며, 연간 약 $1억 달러(약 1억 달러; 원문 "$1 billion/year") 규모다 [[G-03]](#ref-g-03). Gemini 모델은 Apple Private Cloud Compute 서버에서 실행되어 사용자 데이터가 Google 인프라에 전달되지 않는 구조다. 새 Siri의 핵심 기능으로는 복수 명령 동시 처리, 온스크린 인식(Onscreen Awareness), 크로스앱 통합, World Knowledge Answers가 계획되어 있으나 출시 시점이 불투명하다 [[G-04]](#ref-g-04).

3. **Salesforce Slackbot 30개 AI 기능 업데이트: 데스크톱 컨텍스트 인식 도입 (3/31)**
   Salesforce가 3월 31일 Slackbot에 30개 이상의 AI 기능을 추가 발표했다. 핵심은 **Slack 인터페이스 밖 데스크톱 전체로 컨텍스트 확장**이다. Slackbot이 사용자의 딜(CRM), 대화, 캘린더, 습관 데이터를 기반으로 데스크톱 전반에서 액션 가능한 제안(Actionable Suggestions)을 제공한다. 또한 MCP(Model Context Protocol) 클라이언트로 동작하여 외부 에이전트·서비스와 연동 가능하다. 재사용 가능한 AI 스킬(Reusable AI Skills) 기능으로 사용자가 커스텀 태스크를 정의하고 재활용할 수 있다 [[G-05]](#ref-g-05). Salesforce CTO Parker Harris는 "Slack이 업무가 실행되는 미래 인터페이스"라고 밝혔다 [[E-01]](#ref-e-01).

4. **Samsung Galaxy S26 "Now Nudge": 크로스앱 컨텍스트 추천 (MWC 2026)**
   삼성이 MWC 2026에서 Galaxy S26의 Now Nudge 기능을 공개했다. 앱 간 컨텍스트를 분석해 팝업 형태로 타이밍이 맞는 제안을 제공하는 방식이다. 예를 들어 메신저에서 저녁 약속 질문을 받으면, Galaxy AI가 캘린더를 확인해 충돌을 감지하고 맞춤형 Nudge 팝업을 띄운다 [[G-06]](#ref-g-06). Now Brief는 일정·컨텍스트 기반 일일 브리핑을 제공한다. Bixby 외 Gemini·Perplexity를 단일 진입점에서 활용 가능하여 멀티에이전트 구조로 진화 중이다 [[E-02]](#ref-e-02).

5. **Anthropic "Conway" 상시 구동 에이전트 플랫폼 테스트 (4/3)**
   Dataconomy가 4월 3일 보도한 바에 따르면, Anthropic이 Claude를 상시(always-on) 자율 환경으로 운영하는 "Conway" 플랫폼을 내부 테스트 중이다. Slack 채널·Jira 보드·코드 저장소에서 Claude가 반응형 도구가 아닌 **프로액티브 분석자**로 동작하는 구조다 [[G-07]](#ref-g-07). 공개 출시 일정은 미확인 상태다 [원문 미확인].

6. **Microsoft 365 Copilot March 2026 업데이트: Work IQ 컨텍스트 레이어**
   3월 업데이트에서 Work IQ 레이어가 장기 메모리로 동작하며 사용자 역할·조직 구조·프로젝트 이력을 M365 전반에 걸쳐 지속 인식하는 기능이 추가되었다. Excel에서 이메일·미팅·채팅·파일 컨텍스트를 자동 가져와 다단계 편집을 지원하며, Agent Recommendations가 Copilot 대화 중 관련 에이전트를 자동 제안한다 [[G-08]](#ref-g-08).

7. **Agentic Recommender System(AgenticRS) 아키텍처 프레임워크 확립 (arXiv, 3/27)**
   Alibaba International 연구팀(Hu et al.)이 3월 27일 "Rethinking Recommendation Paradigms: From Pipelines to Agentic Recommender Systems"를 발표했다. 추천 모듈을 에이전트로 승격하는 조건(기능적 폐루프·독립 평가 가능성·진화 가능 결정 공간)을 정의하고, Decision/Evolution/Infrastructure 3계층 구조를 제안했다. RL 기반 로컬 최적화와 LLM 기반 구조적 혁신을 결합한 진화 메커니즘이 핵심이다 [[P-01]](#ref-p-01).

8. **AMEM4Rec: 크로스유저 메모리 기반 에이전트 추천 시스템 (arXiv, 2/9)**
   Nguyen et al.이 2월 9일 발표한 AMEM4Rec은 글로벌 메모리 풀에 사용자 행동 패턴을 저장하고 크로스유저 유사성을 통해 메모리를 진화시키는 Agentic LLM (Large Language Model) 기반 추천 시스템이다. Amazon·MIND 데이터셋에서 최신 LLM 기반 추천 모델 대비 성능이 향상되었다고 보고했다 [[P-02]](#ref-p-02).

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| Apple | Siri 개선 iOS 26.5 베타에도 부재 확인(3/30). Gemini 연동($1B/년)은 확정이나 실제 탑재 시점은 iOS 27(9월) 이전 불가. 2년 지연 공식화. | [[G-01]](#ref-g-01), [[G-03]](#ref-g-03) |
| Salesforce | 3/31 Slackbot 30개 AI 기능 발표. 데스크톱 컨텍스트 인식·MCP 클라이언트·재사용 AI 스킬·CRM 자동 업데이트 추가. GA: 2026 1/13(Business+/Enterprise+). | [[G-05]](#ref-g-05), [[E-01]](#ref-e-01) |
| Samsung | Galaxy S26 Now Nudge(크로스앱 컨텍스트 팝업), Now Brief(일일 브리핑) 발표. MWC 2026에서 Agentic AI 비전 제시. Gemini·Perplexity 멀티에이전트 단일 진입점 지원. | [[G-06]](#ref-g-06), [[E-02]](#ref-e-02) |
| Microsoft | M365 Copilot 3월 업데이트: Work IQ 장기 메모리, Agent Recommendations, 회의 컨텍스트 요약 기능 추가. Excel에 이메일·캘린더 컨텍스트 자동 연결. | [[G-08]](#ref-g-08), [[E-03]](#ref-e-03) |
| Google | CC 에이전트(Gmail·Calendar·Drive 통합 일일 브리핑) 12/16 조기 접속 개시. 소비자용 실험 단계. | [[G-09]](#ref-g-09) |
| Glean | 2/17 Glean Assistant 발표. 프로액티브 에이전트 템플릿(일정 정리·태스크 실행) GA. 실시간 음성·슬라이드 생성·엔터프라이즈 액션 포함. | [[G-10]](#ref-g-10) |
| Anthropic | Conway 플랫폼 테스트(4/3): Claude의 Slack·Jira·코드 저장소 상시 구동 프로액티브 에이전트 구조. 출시 일정 미정. | [[G-07]](#ref-g-07) |
| Arahi AI (Rahi) | 프로액티브 인박스·캘린더·태스크 관리 에이전트. 1,500+ 앱 연동, 과거 상호작용 메모리 기반 패턴 학습. 개인·경영진 대상. | [[G-11]](#ref-g-11) |
| Moveworks | ServiceNow와 통합(EmployeeWorks): 대화형 AI + 자율 워크플로우. 프로액티브 Ambient AI 에이전트·전문 도메인 어시스턴트(영업·채용 등) 2026 상반기 예정. | [[G-12]](#ref-g-12) |

---

## 시장 시그널

**시장 규모**

- AI 기반 추천 시스템 시장: 2025년 USD 22억 달러(2,205.1M), 2026년 USD 23.7억 달러(2,372.6M) 전망, CAGR 7.6%(2026~2035) [[G-13]](#ref-g-13) [원문 미확인]
- 컨텍스트 인식 컴퓨팅(Context-Aware Computing) 시장: 2025년 USD 838억 달러(83.76B), 2034년 USD 2,898억 달러(289.83B) 전망, CAGR 13.9% [[G-14]](#ref-g-14)
- 두 수치는 단일 소스 기반이며 교차 검증이 필요하다 [추가확인 필요]

**기술 트렌드**

- **컨텍스트 범위 확장**: 단일 앱 내 → 크로스앱 → 데스크톱 전체로 인식 범위가 단계적으로 확대되는 패턴이 Slackbot(데스크톱), Now Nudge(크로스앱), Copilot Work IQ(M365 전반)에서 동시에 관찰됨
- **메모리 아키텍처**: 단기 세션 메모리에서 장기·크로스유저 메모리(AMEM4Rec, Work IQ, Arahi AI)로 진화 중
- **MCP 표준화 효과**: Slackbot이 MCP 클라이언트로 채택하면서 컨텍스트 기반 에이전트의 인터롭(Interoperability) 표준으로 MCP가 자리잡는 흐름
- **온디바이스 vs 클라우드**: Apple Private Cloud Compute 방식과 Samsung 온디바이스 처리의 차별화 전략이 대비됨

**경쟁 구도 시그널**

- Apple의 반복 지연이 경쟁사에 시장 선점 기회를 제공 중. Samsung Now Nudge와 Google CC가 소비자 시장에서 선행하는 형국
- 엔터프라이즈에서는 Slackbot(Salesforce), Glean, Microsoft Copilot, Moveworks가 프로액티브 워크플로우 자동화를 두고 각축
- 학술 프레임워크(AgenticRS)와 산업 구현 간 격차가 좁혀지며 기술 상업화 속도 가속

---

## 전략적 시사점

**기회**

- **크로스앱 컨텍스트 수집 레이어**: Now Nudge·Slackbot Desktop 방식처럼 앱 전환 없이 컨텍스트를 통합 수집하는 미들웨어 기술이 핵심 역량으로 부상. 통신사 고객 서비스·B2B 워크플로우 도입 검토 가능
- **Apple 공백기 활용**: iOS 27 이전 약 5~6개월간(2026년 4~8월) Apple 생태계에서 경쟁사 대비 차별화 기능 구현 여지 존재
- **MCP 기반 통합**: MCP 클라이언트 아키텍처 채택으로 이종 에이전트·서비스와 컨텍스트 연동 비용을 낮출 수 있음

**위협**

- **Big Tech 번들링**: Microsoft(Work IQ), Salesforce(Slackbot), Google(CC+Gemini)이 기존 생산성 플랫폼에 컨텍스트 추천을 내재화하는 방향으로 수렴. 독립 솔루션의 포지셔닝이 어려워질 수 있음
- **프라이버시 규제 리스크**: 데스크톱 전체 컨텍스트 수집(Slackbot Desktop, Anthropic Conway)은 GDPR·국내 개인정보보호법과의 충돌 가능성이 있으며, 기업 도입 시 법무 검토 필요
- **Siri 지연에 따른 생태계 분열**: Apple 생태계 사용자에 대한 컨텍스트 기반 추천 기능 도달이 늦어지면서 Android 중심 사용자층과 기능 격차 발생

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | MacRumors — New Siri Features Absent From iOS 26.5 Beta, Likely Pushed to iOS 27 | [링크](https://www.macrumors.com/2026/03/30/ios-26-5-no-new-siri-features/) | news | 2026-03-30 | [B] |
| <a id="ref-g-02"></a>G-02 | Bloomberg / MacRumors — Siri iOS 26.4 Internal Testing Snags | [링크](https://www.macrumors.com/2026/02/11/siri-features-delayed-ios-26-4/) | news | 2026-02-11 | [B] |
| <a id="ref-g-03"></a>G-03 | CNBC — Apple picks Google's Gemini to run AI-powered Siri | [링크](https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html) | news | 2026-01-12 | [A] |
| <a id="ref-g-04"></a>G-04 | 9to5Mac — New Siri is coming this year: Here's the expected release date | [링크](https://9to5mac.com/2026/01/05/new-siri-is-coming-this-year-heres-the-expected-release-date/) | news | 2026-01-05 | [B] |
| <a id="ref-g-05"></a>G-05 | SiliconANGLE — Salesforce transforms Slackbot into the ultimate work assistant with 30 new AI features | [링크](https://siliconangle.com/2026/03/31/salesforce-transforms-slackbot-ultimate-work-assistant-30-new-ai-features/) | news | 2026-03-31 | [B] |
| <a id="ref-g-06"></a>G-06 | Samsung Newsroom — Samsung Advances Galaxy AI and Its Connected Ecosystem at MWC 2026 | [링크](https://news.samsung.com/global/samsung-advances-galaxy-ai-and-its-connected-ecosystem-at-mwc-2026) | news | 2026-03 | [A] |
| <a id="ref-g-07"></a>G-07 | Dataconomy — Anthropic Tests Conway As A Persistent Agent Platform For Claude | [링크](https://dataconomy.com/2026/04/03/anthropic-tests-conway-platform-for-continuous-claude/) | news | 2026-04-03 | [B] |
| <a id="ref-g-08"></a>G-08 | Microsoft Tech Community — What's New in Microsoft 365 Copilot, March 2026 | [링크](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--march-2026/4506322) | news | 2026-03 | [A] |
| <a id="ref-g-09"></a>G-09 | Google Blog — Help boost your daily productivity with CC, a new experimental AI agent | [링크](https://blog.google/technology/google-labs/cc-ai-agent/) | news | 2025-12-16 | [A] |
| <a id="ref-g-10"></a>G-10 | Business Wire — Glean's Latest AI Assistant Moves Every Employee from Insight to Execution | [링크](https://www.businesswire.com/news/home/20260217973304/en/Gleans-Latest-AI-Assistant-Moves-Every-Employee-from-Insight-to-Execution) | news | 2026-02-17 | [A] |
| <a id="ref-g-11"></a>G-11 | Arahi AI — Best Personal AI Assistant in 2026 | [링크](https://arahi.ai/blog/which-personal-ai-assistant-should-you-choose-practical-guide-2026) | blog | 2026 | [C] |
| <a id="ref-g-12"></a>G-12 | ServiceNow Newsroom — ServiceNow launches Autonomous Workforce, adds Moveworks | [링크](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-launches-Autonomous-Workforce-that-thinks-and-acts-adds-Moveworks-to-the-ServiceNow-AI-Platform/default.aspx) | news | 2026 | [A] |
| <a id="ref-g-13"></a>G-13 | Global Growth Insights — AI-Based Recommendation System Market 2026-2035 | [링크](https://www.globalgrowthinsights.com/market-reports/ai-based-recommendation-system-market-102057) | report | 2026 | [C] |
| <a id="ref-g-14"></a>G-14 | Fortune Business Insights — Context-Aware Computing Market | [링크](https://www.fortunebusinessinsights.com/industry-reports/context-aware-computing-market-101605) | report | 2026 | [B] |
| <a id="ref-g-15"></a>G-15 | Alpha-Sense — Proactive AI in 2026: Moving Beyond the Prompt | [링크](https://www.alpha-sense.com/resources/research-articles/proactive-ai/) | blog | 2026 | [B] |
| <a id="ref-g-16"></a>G-16 | AndroidHeadlines — What is Samsung Now Nudge? Galaxy S26 AI Feature Explained | [링크](https://www.androidheadlines.com/2026/02/samsung-galaxy-s26-now-nudge-ai-feature-explained.html) | news | 2026-02 | [B] |
| <a id="ref-g-17"></a>G-17 | TechCrunch — Salesforce announces an AI-heavy makeover for Slack, with 30 new features | [링크](https://techcrunch.com/2026/03/31/salesforce-announces-an-ai-heavy-makeover-for-slack-with-30-new-features/) | news | 2026-03-31 | [B] |
| <a id="ref-g-18"></a>G-18 | IDC Blog — MWC 2026: The year devices moved from smart to intelligent | [링크](https://www.idc.com/resource-center/blog/intelligent-devices-mwc-2026/) | report | 2026-03 | [B] |
| <a id="ref-p-01"></a>P-01 | Hu et al. — Rethinking Recommendation Paradigms: From Pipelines to Agentic Recommender Systems (arXiv:2603.26100) | [링크](https://arxiv.org/abs/2603.26100) | paper | 2026-03-27 | [A] |
| <a id="ref-p-02"></a>P-02 | Nguyen et al. — AMEM4Rec: Leveraging Cross-User Similarity for Memory Evolution in Agentic LLM Recommenders (arXiv:2602.08837) | [링크](https://arxiv.org/abs/2602.08837) | paper | 2026-02-09 | [A] |
| <a id="ref-p-03"></a>P-03 | Huang et al. — Towards Agentic Recommender Systems in the Era of Multimodal Large Language Models (arXiv:2503.16734) | [링크](https://arxiv.org/abs/2503.16734) | paper | 2025-03-20 | [A] |
| <a id="ref-e-01"></a>E-01 | Salesforce — Parker Harris CTO 발언: "We see it as the future interface for work" (Slackbot 30 AI features 발표) | [링크](https://siliconangle.com/2026/03/31/salesforce-transforms-slackbot-ultimate-work-assistant-30-new-ai-features/) | IR/발표 | 2026-03-31 | [A] |
| <a id="ref-e-02"></a>E-02 | Samsung Newsroom — Galaxy S26 Unpacked 2026: Now Nudge 공식 발표 | [링크](https://news.samsung.com/global/galaxy-unpacked-2026-a-first-look-at-the-galaxy-s26-series-samsungs-most-intuitive-ai-phone-yet) | IR/발표 | 2026-02 | [A] |
| <a id="ref-e-03"></a>E-03 | Microsoft Tech Community — Copilot March 2026 업데이트: Work IQ, Agent Recommendations 공식 발표 | [링크](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--march-2026/4506322) | IR/발표 | 2026-03 | [A] |
