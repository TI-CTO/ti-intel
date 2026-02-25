---
topic: Self Evolving Agent 기술정보 수집
date: 2026-02-24
wtis_skill: SKILL-4 (Research Collector)
status: completed
mode: standard+
---

# WTIS SKILL-4 기술정보 수집: Self Evolving Agent

## 수집 요약
- 주제: Self Evolving Agent (AICC)
- 수집일: 2026-02-24
- 검색 쿼리 수: 18건
- 수집 레퍼런스 수: 28건
- 신뢰도 분포: [A] 9건 / [B] 12건 / [C] 5건 / [D] 2건

---

## 1. 기술 현황

### 1-1. Self-Evolving Agent의 기술적 정의와 메커니즘

"Self-evolving agent"는 배포 후에도 환경과의 상호작용 데이터를 기반으로 스스로 개선하는 AI 시스템을 의미한다. 2025년 상반기에 두 편의 대형 서베이 논문이 이 개념을 체계화했다 [1][2].

**핵심 메커니즘 4가지 (arXiv 2508.07407 분류 기준):**
1. **System Inputs**: 상호작용 데이터, 피드백, 환경 신호
2. **Agent System**: LLM 기반 추론 + 메모리 + 도구 사용
3. **Environment**: 실제 배포 환경에서의 폐쇄 루프(closed-loop)
4. **Optimisers**: RLHF, continual fine-tuning, RAG 자동 업데이트

**실제 구현 사례:**
- **EvoAgent** (arXiv 2502.05907, Feb 2025): Continual World Model을 보유한 자가 진화 에이전트. Minecraft/Atari 실험에서 평균 성공률 105% 향상, 비효율 행동 6배 이상 감소. 세 모듈(메모리 기반 플래너, WM 가이드 행동 컨트롤러, 경험 기반 리플렉터)로 구성 [3].
- **AgentEvolver** (arXiv 2511.10395, Nov 2025): 자기질문(self-questioning), 자기탐색(self-navigating), 자기귀인(self-attributing) 세 메커니즘으로 LLM의 자율 진화 구현 [4].
- **ALAS** (arXiv 2508.15805): Autonomous Learning Agent for Self-Updating Language Models — 언어 모델의 자율 업데이트를 위한 에이전트 [5].

### 1-2. Continual Learning의 핵심 기술적 과제

LLM의 continual learning에서 최대 난제는 **catastrophic forgetting** — 새로운 도메인 학습 시 기존 지식이 손상되는 현상이다 [6].

**2024-2025년 주요 해결 방안:**
- **Self-Synthesized Rehearsal (SSR)**: LLM이 합성 인스턴스를 생성해 과거 지식을 리허설. ACL 2024 채택 논문 [6].
- **Self-Distillation Fine-Tuning (SDFT)**: 데모 기반 in-context learning으로 과거 능력 보존하면서 신규 스킬 습득. 단, 표준 SFT 대비 컴퓨팅 2.5배 소요 [7].
- **Model Growth**: 소규모 모델을 활용한 점진적 성장 전략 [7].
- **LoRA/QLoRA**: Parameter-Efficient Fine-Tuning으로 기존 가중치 손상 최소화 (업계 표준으로 자리잡음).

### 1-3. AICC 도메인에서의 Self-Evolving 구현 현황

**산업계 적용 형태 (2025년 기준):**
- **RAG 자동 업데이트**: 지식베이스를 콜 로그 기반으로 자동 갱신 — 가장 현실적이고 배포 사례 많음
- **Override/Escalation 피드백 루프**: 상담사 수동 수정, 에스컬레이션 케이스를 AI 훈련 신호로 재활용 [8]
- **LLM-as-Judge (Autorater)**: 에이전틱 파이프라인 내 실시간 품질 평가 + 자동 수정 루프 [9]
- **RLHF 프로덕션 적용**: 고객 만족도, 해결률, 에스컬레이션률을 보상 신호로 활용 [10]

**기술 성숙도(TRL) 평가:**
- RAG 자동 업데이트: TRL 8-9 (상용 배포 단계)
- LLM-as-Judge 자동 수정: TRL 7-8 (초기 상용화)
- 완전 자율 continual fine-tuning: TRL 5-6 (파일럿/실험 단계)
- Closed-loop RLHF from contact logs: TRL 4-5 (연구-파일럿 경계)

---

## 2. 경쟁사 동향

### SKT

**브랜드/솔루션**: SKT AI CCaaS (구독형), SKAX AICC (구축형/엔터프라이즈), Agentic AICC

**주요 현황:**
- SKT는 자체 **텔코 LLM** 개발 — 36개 이상의 고객센터 상담 전문가 데이터로 훈련, 반복적 강화학습(iterative reinforcement learning)으로 통신 도메인 특화 [11]
- **MWC 2026** (3월 2-5일)에서 **Agentic AICC** 전시 예정 — "상담뿐 아니라 실제 업무처리까지 자동화"하는 차세대 컨택센터로 소개 [12]
- **A.X K1**: 519B 파라미터 하이퍼스케일 AI 모델, 2026년 1월 정부 주권AI 파운데이션 모델 프로젝트 2단계 진입 [13]
- 글로벌 텔코 AI 얼라이언스(GTAA) 참여, LLM 합작법인 설립

**자가학습/진화 기능 공개 현황**: 공식 자료에서 "iterative reinforcement learning" 언급 있으나, 운영 배포된 시스템의 자율 업데이트 메커니즘은 비공개 [11].

---

### KT

**브랜드/솔루션**: KT A'Cen(에이센), A'Cen Cloud, kt cloud AI 에이전트

**주요 현황:**
- KT는 국내 AICC 시장 **점유율 69%** (2023년 기준) 선두 — 2017년부터 AICC 사업 참여 [14]
- 연간 AICC 수주액 **2,500억원 이상** (전년 대비 3배 규모, 특정 연도 기준) [15]
- **'상담 Assist'**: 상담사 실시간 지원 AI. 상담 시간 15초 → 5초 단축, 요약·분류 60-120초 → 10초 미만 달성 [16]
- **AI 에이전트 '마이K'**: 2025년 9월 본격 출시 발표, A2A(Agent-to-Agent) 협업, MCP 지원 [16]
- kt cloud 기술 블로그에서 AI 에이전트 아키텍처, A2A 통합 패턴을 공개 연재 (2025년 3월~7월) [16]

**자가학습/진화 기능**: 공식 발표 자료에 명시적 언급 없음. 상담 데이터 기반 지속 개선은 운영 체계 수준에서 시행 추정 [데이터 갭].

---

### 네이버클라우드 / 카카오엔터프라이즈

**네이버클라우드:**
- **CLOVA AiCall** (HyperCLOVA X 기반) — 롯데카드 AICC 도입 2년 후 운영 리소스 **40% 절감** 달성 [17]
- HyperCLOVA X SEED: 오픈소스 공개 1개월 내 30만 회 이상 다운로드 [18]
- 2025년 6월 추론 모델 공개 계획 발표 [18]
- 금융·공공 레퍼런스 확보 중 (롯데카드가 대표 사례)

**카카오엔터프라이즈:**
- **CenterFlow** (센터플로우): 카카오 i 커넥트센터에서 브랜드 개편. 카카오클라우드 기반 SaaS형 AICC [19]
- Kanana Model Family: 중소형 LLM '카나나 에센스', 모바일용 sLM '카나나 나노' 서비스 적용 중 [20]
- 카카오뱅크·카카오채널 연동 강점, 스타트업·SMB 중심 포지셔닝

**자가학습/진화 기능**: 양사 모두 공식 자료에 자율 학습 메커니즘 구체적 언급 없음.

---

### 글로벌 (Google, Amazon, Genesys, NICE, Salesforce)

**Google CCAI:**
- CCAI (Contact Center AI) + Vertex AI Conversation 통합
- UJET과의 OEM 계약으로 CCaaS 플랫폼으로 확장 중
- 평가(Evaluation)를 에이전틱 파이프라인의 구성 요소로 통합 — LLM-as-Judge 기반 실시간 자동 수정 루프 [9]

**Amazon Connect:**
- **2025년 11월 AWS re:Invent**: 29개의 에이전틱 AI 기능 발표 [21]
- **Agentic Self-Service**: Amazon Nova Sonic 기반, 감정·억양 적응형 음성 인터랙션
- MCP(Model Context Protocol) 지원으로 외부 시스템과 AI 에이전트 실시간 연동
- 실제 효과: Centrica 1만 명 상담사 배포 후 **AHT 38% 감소** (140초 → 87초) [21]

**Genesys:**
- **2025년 6월**: Genesys Cloud AI Studio 발표 — No-code AI 에이전트 구축 플랫폼
- **2026년 2월 10일**: 업계 최초 **LAM(Large Action Model) 기반 Agentic Virtual Agent** 발표 [22]
  - Scaled Cognition APT-1 LAM 탑재 — "이해·설명"하는 LLM과 달리 "결정·실행"에 특화
  - M&T Bank, Banco Pichincha 등 금융기관 포함 초기 파트너 참여
  - 전면 출시: 2026 FY Q1 (2026년 2월~4월) 예정

**NICE:**
- **2025년 7월**: Cognigy 인수 발표 (인수가 약 9억 5,500만 달러 — NICE 40년 역사상 최대 인수) [23]
- **2025년 9월 8일**: 인수 완료
- Cognigy.AI: 100개 이상 언어, 전 채널 지원 — Mercedes-Benz, Nestlé, Lufthansa Group 레퍼런스
- 통합 목표: CXone Mpower + Cognigy 에이전틱 AI = 프론트/백오피스 통합 CX AI 플랫폼
- Cognigy의 2026년 ARR 성장률 80% 예상 [23]

**Salesforce Agentforce:**
- Agentforce for Service: 자율적으로 행동하고 **self-learning**으로 성능 향상 공식화 [24]
- Atlas Reasoning Engine: 2025년 2월 런칭, 에이전트의 추론 능력 강화
- 목표: 2025년 말까지 10억 개 에이전트 구축 지원

---

### 국내 스타트업 (Maum.ai 등)

**Maum.ai (마음에이아이):**
- Physical AI + SUDA·MAAL·WoRV 기반 기업 생산성 자동화 솔루션
- AICC 전문 스타트업, 금융권 레퍼런스 다수 보유
- 망분리 규제 완화로 **금융권 AICC 수요 확대** 직접 수혜 예상 [25]

**제네시스 클라우드 (국내):**
- 2025년 7월 혁신금융서비스로 지정 → 금융 SaaS 컨택센터 구축 자격 획득
- S금융투자 300석(IaaS), A생명 1,100석(SaaS) 구축 완료 [25]

---

## 3. 시장 데이터

| 지표 | 수치 | 출처 | 신뢰도 |
|------|------|------|--------|
| 글로벌 콜센터 AI 시장 규모 (2025) | USD 2.41B ~ 4.20B | Fortune Business Insights / Mordor Intelligence | [B] |
| 글로벌 콜센터 AI 시장 CAGR (2025-2030) | 21.6% ~ 22.7% | Fortune / Mordor | [B] |
| 글로벌 콜센터 AI 시장 규모 (2030 전망) | USD 10.07B ~ 11.80B | Fortune / Mordor | [B] |
| 한국 콜센터 AI 시장 규모 (2030 전망) | USD 275.8M | Grand View Research | [B] |
| 한국 콜센터 AI 시장 CAGR (2025-2030) | 28.8% | Grand View Research | [B] |
| 국내 AICC 시장 규모 (2020) | USD 42.14M (약 578억원) | Goover Report | [C] |
| 국내 AICC 시장 규모 (2025 전망) | USD 350.88M (약 4,815억원) | Goover Report | [C] |
| 국내 AICC 시장 CAGR (2020-2025) | 23.7% | Goover Report | [C] |
| 한국 콘택트센터 소프트웨어 시장 (2024) | USD 779.48M | IMARC Group | [B] |
| 한국 콘택트센터 소프트웨어 시장 (2033 전망) | USD 2,891.56M | IMARC Group | [B] |
| KT AICC 국내 시장점유율 | 약 69% | Goover Report | [C] |
| KT AICC 연간 수주액 | 2,500억원 이상 (특정 연도) | 핀포인트뉴스 | [B] |
| LG유플러스 AICC 매출 목표 (2028) | 3,000억원 | Goover Report | [C] |
| LGU+ AI콜봇 1개 → 상담사 대체 수 | 36명 | Goover Report | [C] |
| Centrica AHT 감소 (Amazon Connect 적용) | 140초 → 87초 (38% 감소) | CX Today / AWS | [B] |
| 네이버클라우드 롯데카드 AICC 운영리소스 절감 | 40% | AI타임스 | [B] |
| NICE의 Cognigy 인수가 | USD 955M | NICE 공식 보도자료 | [A] |
| Cognigy 2026 ARR 성장률 전망 | 80% | NICE 공식 보도자료 | [A] |
| 글로벌 AICC 시장 (2025 전망, 카카오 인용) | USD 36.1B (약 46.9조원) | 카카오엔터프라이즈 보도자료 | [C] |

---

## 4. 특허/논문 동향

### 주요 서베이 논문 (2025)

| # | 제목 | arXiv ID | 발행일 | 핵심 내용 |
|---|------|----------|--------|----------|
| P1 | A Comprehensive Survey of Self-Evolving AI Agents | 2508.07407 | 2025.08 | Self-evolving agent 통합 프레임워크. 4요소(입력·시스템·환경·최적화기) 분류. 금융 등 도메인별 진화 전략 검토 |
| P2 | A Survey of Self-Evolving Agents: What, When, How, Where | 2507.21046 | 2025.07 | "무엇을, 언제, 어떻게, 어디서 진화할 것인가" 3차원으로 체계화. 초지능(ASI) 경로 논의 |
| P3 | EvoAgent: Self-evolving Agent with Continual World Model | 2502.05907 | 2025.02 | Continual World Model 기반 자율 에이전트. 게임(Minecraft/Atari) 실험에서 105% 성공률 향상 |
| P4 | AgentEvolver: Towards Efficient Self-Evolving Agent System | 2511.10395 | 2025.11 | 자기질문·자기탐색·자기귀인 3메커니즘으로 효율적 자가 진화 |
| P5 | Self-Evolving LLMs via Continual Instruction Tuning | 2509.18133 | 2025.09 | 동적 태스크 자율 적응, 크로스태스크 지식 통합, 외부 개입 최소화 정의 |
| P6 | ALAS: Autonomous Learning Agent for Self-Updating LMs | 2508.15805 | 2025.08 | LM 자율 업데이트를 위한 학습 에이전트 |
| P7 | Continual Learning of LLMs (ACM CSUR Survey) | CSUR 2025 | 2025 | LLM continual learning 종합 서베이. Catastrophic forgetting 완화 전략 체계화 |
| P8 | Mitigating Catastrophic Forgetting (Self-Synthesized Rehearsal) | ACL 2024 | 2024 | LLM 스스로 합성 인스턴스 생성하여 과거 지식 리허설 |

### 특허 동향
- 국내 "자가 진화 에이전트" 특허 검색 결과: 공개 검색에서 통신사·AICC 특화 특허 직접 확인 불가 [데이터 갭]
- 글로벌 특허 데이터베이스 별도 검색 필요

---

## 5. 규제/정책 동향

### 5-1. 금융권 망분리 규제 완화

- **배경**: 금융위원회·금융감독원이 2024년 「금융분야 망분리 개선 로드맵」 발표. 기존 완전 망분리 → 조건부 SaaS/클라우드 허용으로 전환 [26]
- **허용 범위**: 연구개발망·생산계망에 SaaS·클라우드 이용 허용. 일정 요건 충족 시 실제 업무 적용 가능
- **보안 조건**: 개인정보 반드시 가명 처리, 규제 샌드박스 승인 필수
- **2025년 말 목표**: 1단계 규제 특례(생성형 AI, 임직원 업무망 SaaS) 효용성 평가 후 정규 제도화
- **직접 효과**: 제네시스 클라우드가 2025년 7월 혁신금융서비스로 지정 → 금융 SaaS 컨택센터 구축 자격 획득 [25]

### 5-2. 금융보안원 AI 가이드라인

- **금융분야 AI 보안 가이드라인** 2025년 개정 예정 — 생성형 AI·신규 AI 기술 반영 [27]
- **7대 원칙**: ①거버넌스 ②합법성 ③보조수단성 ④신뢰성 ⑤금융안정성 ⑥신의성실 ⑦보안성
- **AI 보안성 검증체계**: 2025년 금융회사 AI 서비스 제3자 검증 수행 계획
- **FDS 연합학습·합성데이터** 등 AI 프라이버시 강화기술(PET) 연구 병행 [27]

### 5-3. AI 기본법 (인공지능 발전과 신뢰 기반 조성 등에 관한 기본법)

- **시행일**: 2026년 1월 22일 (제정: 2025년 1월) [28]
- **AICC 관련 규제 분류**:
  - **고영향 AI**: AI 기반 신용평가·대출 심사 → 설명 가능성 확보, 편향성 테스트 강제
  - **규제 대상 가능성 낮음**: 챗봇 상담, 단순 정보 제공 (단순 보조 수단 성격)
- **계도 기간**: 시행 초기 1년 이상 과태료 미부과 (혼란 최소화 목적) [28]
- **실질 시사점**: 금융권 AICC가 "AI 최종 판단" 역할 수행 시 고영향 AI로 분류될 수 있음 → 설명 가능성(XAI) 요건 충족 필요

### 5-4. 은행권 AI 도입 현황 (2024-2025)

- **NH농협은행**: 2024년 11월 생성형 AI 도입 프로젝트 47억원 규모 발주 → LG CNS 수주 [29]
- **우리은행**: AI 상담 통합 플랫폼 구축 우선협상 완료, 고객센터 'AI 전담 운영팀' 신설 계획 [29]
- **전반적 현황**: 2024년은 대고객 서비스보다 내부 업무 자동화, 파일럿 성격 sLLM 적용이 주류 [29]
- 2026년 1월 은행권 망분리 규제 추가 완화 예고 → 2026년부터 클라우드 기반 AICC 본격 도입 가속 예상 [30]

---

## 6. 핵심 발견 & 시사점

> 아래는 수집된 사실로부터 도출한 관찰이며, 전략 제언(Buy/Build/Borrow)은 포함하지 않는다.

- **"Self-Evolving Agent"는 2025년에 학계에서 본격 정의되기 시작한 개념**: 2025년 7-8월에 첫 종합 서베이 논문이 발표됐으며, 실제 AICC 도메인 적용은 주로 RAG 자동 업데이트, LLM-as-Judge 피드백 루프 수준에 머물고 있다. 완전 자율 continual fine-tuning은 연구-파일럿 경계(TRL 4-5)에 위치한다.

- **국내 통신 3사 모두 Agentic AICC로 전환 중이나, 자가 진화 기능은 비공개**: SKT는 MWC 2026에서 "Agentic AICC" 전시, LG유플러스는 2025년 12월 OpenAI 기반 "에이전틱 콜봇" 출시, KT는 "마이K" 에이전트 출시. 그러나 3사 모두 자율 학습/진화의 구체적 메커니즘은 공개하지 않고 있다.

- **글로벌 빅플레이어의 Self-Improving 구현이 구체화**: Genesys는 2026년 2월 LAM 기반 에이전틱 버추얼 에이전트 발표, Amazon Connect는 2025년 11월 re:Invent에서 29개 에이전틱 기능 발표(Centrica AHT 38% 감소 실증), NICE는 Cognigy 약 9.5억 달러 인수로 에이전틱 AI 포트폴리오 강화. 글로벌 솔루션의 기술 성숙도가 국내보다 앞서 있다.

- **금융권 규제 완화가 AICC 시장의 결정적 변수**: 망분리 개선 로드맵(2024)으로 금융권 SaaS AICC 도입 장벽이 낮아졌고, AI 기본법(2026.1 시행)은 AICC가 "최종 판단"을 내리는 경우에만 고영향 AI로 규제한다. 즉, 단순 정보 제공·보조 역할의 AICC는 규제 부담이 크지 않으나, 자율 의사결정 기능을 확대하면 XAI 요건 충족이 필수다.

- **국내 AICC 시장 성장률이 글로벌 평균 상회**: 국내 CAGR 23.7-28.8% vs. 글로벌 21.6-22.7%. KT가 시장 점유율 약 69%로 선두이나, LG유플러스가 2028년 3,000억 목표를 공표하며 추격 중.

---

## 7. 데이터 갭 & 한계

| 항목 | 현황 | 보완 방법 |
|------|------|---------|
| 국내 통신사 AICC 자가학습 메커니즘 | SKT·KT·LGU+ 모두 비공개 | 기술 컨퍼런스(KSC, IITP) 논문, 내부 IR 자료 확인 |
| 국내 AICC 시장 규모 공신력 있는 수치 | Goover 등 AI 생성 리포트 의존 → [C] 등급 | IDC, Gartner 코리아 리포트 별도 구매 검토 |
| 5대 시중은행 구체적 AICC RFP 현황 | 개별 발주 건만 파편적으로 확인 | 금융권 조달 시스템(나라장터) 직접 검색 |
| 국내 AICC 자가진화 특허 현황 | 공개 검색 불가 | 키프리스(KIPRIS) 직접 검색 필요 |
| LG유플러스 ixi-GEN의 AICC 적용 현황 | 정보 없음 | 사내 확인 필요 |
| Maum.ai 금융권 레퍼런스 상세 | 공개 정보 미흡 | 직접 문의 또는 업계 네트워크 |
| Self-evolving AICC의 실제 비즈니스 ROI | Centrica 사례(AHT -38%) 외 한국 사례 없음 | 국내 벤더 케이스 스터디 확보 |

---

## References

| # | 출처명 | URL | 발행일 | 접근일 | 신뢰도 |
|---|--------|-----|--------|--------|--------|
| 1 | arXiv: A Comprehensive Survey of Self-Evolving AI Agents (2508.07407) | https://arxiv.org/abs/2508.07407 | 2025.08.31 | 2026-02-24 | [A] |
| 2 | arXiv: A Survey of Self-Evolving Agents (2507.21046) | https://arxiv.org/abs/2507.21046 | 2025.07 | 2026-02-24 | [A] |
| 3 | arXiv: EvoAgent (2502.05907) | https://arxiv.org/abs/2502.05907 | 2025.02.09 | 2026-02-24 | [A] |
| 4 | arXiv: AgentEvolver (2511.10395) | https://arxiv.org/abs/2511.10395 | 2025.11 | 2026-02-24 | [A] |
| 5 | arXiv: ALAS (2508.15805) | https://arxiv.org/html/2508.15805v1 | 2025.08 | 2026-02-24 | [A] |
| 6 | ACL 2024: Mitigating Catastrophic Forgetting (SSR) | https://aclanthology.org/2024.acl-long.77/ | 2024 | 2026-02-24 | [A] |
| 7 | InfoWorld: Self-distillation fix for catastrophic forgetting | https://www.infoworld.com/article/4131242/researchers-propose-a-self-distillation-fix-for-catastrophic-forgetting-in-llms.html | 2024-2025 | 2026-02-24 | [B] |
| 8 | Mosaicx: AI-Driven Contact Center Automation Trends 2025 | https://www.mosaicx.com/blog/contact-center-ai-trends | 2025 | 2026-02-24 | [B] |
| 9 | Google Cloud Blog: Lessons from 2025 on agents and trust | https://cloud.google.com/transform/ai-grew-up-and-got-a-job-lessons-from-2025-on-agents-and-trust | 2025 | 2026-02-24 | [B] |
| 10 | CleverX: Enterprise RLHF Implementation Checklist 2025 | https://cleverx.com/blog/enterprise-rlhf-implementation-checklist-complete-deployment-framework-for-production-systems | 2025 | 2026-02-24 | [C] |
| 11 | SKT 뉴스룸: AI-Powered Customer Service Utilizing Proprietary Telco LLM | https://news.sktelecom.com/en/1647 | 2024-2025 | 2026-02-24 | [A] |
| 12 | The Fast Mode: SK Telecom Unveils Full-Stack AI at MWC 2026 | https://www.thefastmode.com/technology-solutions/47220-sk-telecom-unveils-full-stack-ai-at-mwc-barcelona-2026-featuring-hyperscale-ai-model | 2026.02 | 2026-02-24 | [B] |
| 13 | SKT 뉴스룸 (영문): Full-Stack AI at MWC 2026 | https://news.sktelecom.com/en/2742 | 2026.02 | 2026-02-24 | [A] |
| 14 | Goover 리포트: 2025년 AICC 시장 경쟁 구도와 통신사 전략 | https://seo.goover.ai/report/202503/go-public-report-ko-53c96b24-a1a8-42a9-be6a-bdb5acb9ee2c-0-0.html | 2025.03 | 2026-02-24 | [C] |
| 15 | 핀포인트뉴스: 통신3사가 콕 찍은 AICC | https://www.pinpointnews.co.kr/news/articleView.html?idxno=213245 | 2023-2024 | 2026-02-24 | [B] |
| 16 | kt cloud 기술 블로그: AI 에이전트 시리즈 | https://tech.ktcloud.com/entry/2025-03-ktcloud-ai-agent | 2025.03-07 | 2026-02-24 | [B] |
| 17 | AI타임스: 네이버클라우드 롯데카드 AICC 40% 절감 | https://www.aitimes.com/news/articleView.html?idxno=170834 | 2025 | 2026-02-24 | [B] |
| 18 | AI타임스: 하이퍼클로바X 추론 모델 공개 계획 | https://www.aitimes.com/news/articleView.html?idxno=170749 | 2025 | 2026-02-24 | [B] |
| 19 | 카카오엔터프라이즈 공식: 센터플로우 브랜드 변경 | https://kakaoenterprise.com/press/centerflow-new-brand/ | 2024-2025 | 2026-02-24 | [A] |
| 20 | 카카오: Kanana Model Family 소개 | https://www.kakaocorp.com/page/detail/11334 | 2025 | 2026-02-24 | [A] |
| 21 | AWS 공식: Amazon Connect at re:Invent 2025 | https://aws.amazon.com/blogs/contact-center/amazon-connect-at-reinvent-2025-creating-the-future-of-customer-experience-with-ai/ | 2025.11 | 2026-02-24 | [A] |
| 22 | Genesys 공식 보도자료: LAM 기반 Agentic Virtual Agent | https://www.genesys.com/company/newsroom/announcements/genesys-unveils-industrys-first-agentic-virtual-agent-powered-by-lams-for-enterprise-cx | 2026.02.10 | 2026-02-24 | [A] |
| 23 | NICE 공식 보도자료: Closes Acquisition of Cognigy | https://www.nice.com/press-releases/nice-closes-acquisition-of-cognigy | 2025.09.08 | 2026-02-24 | [A] |
| 24 | Salesforce 공식: What Is Autonomous Customer Service | https://www.salesforce.com/service/what-is-autonomous-customer-service/ | 2025 | 2026-02-24 | [A] |
| 25 | 디지털데일리: 망분리 규제 완화 속 금융권 AICC 시대 개막 | https://www.ddaily.co.kr/page/view/2025091014390239063 | 2025.09.10 | 2026-02-24 | [B] |
| 26 | 금융위원회 공식: 금융분야 망분리 개선 로드맵 | https://www.fsc.go.kr/no010101/82885 | 2024 | 2026-02-24 | [A] |
| 27 | 금융보안원 공식: AI 보안 가이드라인 개정 계획 | https://www.fsec.or.kr/bbs/detail?menuNo=69&bbsNo=11607 | 2025 | 2026-02-24 | [A] |
| 28 | 피카부랩스: AI 기본법 완전 정리 (2026.1 시행) | https://peekaboolabs.ai/blog/ai-basic-law-guide | 2025-2026 | 2026-02-24 | [B] |
| 29 | 삼성SDS 인사이트: 2025년 국내 은행 AI 활용 전망 | https://www.samsungsds.com/kr/insights/ai-in-banking-in-2025.html | 2025 | 2026-02-24 | [B] |
| 30 | 전자신문: 은행권 망분리 규제 완화 AI·SaaS 도입 가속 | https://www.etnews.com/20260128000169 | 2026.01.28 | 2026-02-24 | [B] |
