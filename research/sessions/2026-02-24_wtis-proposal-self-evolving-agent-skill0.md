---
topic: Self Evolving Agent 과제 제안서 분석
date: 2026-02-24
wtis_skill: SKILL-0 (Analysis Brief)
status: completed
domain: AICC / AI Contact Center
---

# Analysis Brief: Self Evolving Agent

## 경영진 요약

> "Self Evolving Agent"는 LG U+의 AICC 솔루션(콜봇, 상담 어드바이저)에 자가 학습·자율 개선 능력을 부여하여, 고정 시나리오 한계를 극복하고 5대 시중은행을 포함한 B2B 고객을 대상으로 구축형 AICC 수주 경쟁력을 높이는 것이 핵심 목표다. 국내 통신 3사(SKT·KT·LG U+)가 모두 LLM 기반 AICC를 경쟁적으로 출시하고 있으며, 네이버클라우드·카카오엔터프라이즈·Maum.ai 등 플레이어도 금융권 AICC를 공략 중이다. "스스로 진화"라는 차별화 주장의 기술적 실체(continual learning, RLHF from contact logs, autonomous workflow update 등)와 금융권 규제 적합성 검증이 이후 리서치의 핵심 과제다.

---

## 1. 과제 개요

| 항목 | 내용 |
|------|------|
| 과제명 | Self Evolving Agent |
| 기술 도메인 | AICC (AI Contact Center) |
| 주요 타겟 고객 | 콜봇, 상담 어드바이저, 고객센터, 5대 시중은행 B2B 고객 |
| 목표 KPI | 고객센터 운영 효율성 향상 + AICC 상품 경쟁력 강화 → B2B 구축형 AICC 수주 경쟁력 상승 |
| 예산/타임라인 | 미명시 (Unspecified) |
| LG U+ 기술 분류 | AI/Data (AI Agents) + B2B/Enterprise (AI DX) |

### 과제 해석
- **Self Evolving Agent**: 스스로 학습하고 개선하는 AI 상담 에이전트. 단순 규칙/시나리오 기반을 탈피하여 실제 상담 로그·고객 피드백을 통해 자율적으로 응답 품질과 워크플로우를 개선하는 시스템.
- **AICC (AI Contact Center)**: 고객센터 업무(인바운드/아웃바운드 콜, 채팅, 음성봇)를 AI로 처리하거나 상담사를 보조하는 플랫폼.
- **B2B 구축형**: 클라우드 공용 서비스(CCaaS)가 아닌 기업 전용 온프레미스 또는 프라이빗 클라우드 방식으로 납품·구축.

### 유추된 Pain Point
1. **고정 시나리오 한계**: 기존 AICC는 미리 정의된 대화 트리에 의존 → 신규 상품/정책 변경 시 수동 업데이트 필요
2. **지속적 유지보수 비용**: 콜 로그 기반 시나리오 개선에 전문 인력·시간 소요
3. **경쟁사 대비 차별화 부족**: LLM 기반 응답 생성은 이미 시장 표준 → "진화" 능력이 차기 차별화 포인트
4. **금융권 요구사항**: 5대 시중은행은 높은 정확도·컴플라이언스·설명 가능성 요구 → 단순 생성형 AI로는 충족 어려움

---

## 2. 핵심 키워드

### 기술 키워드 (영어)
- Self-evolving AI agent, self-learning AI, autonomous improvement
- Continual learning, online learning, lifelong learning AI
- RLHF (Reinforcement Learning from Human Feedback), RLAIF
- Autonomous agent, agentic AI, LLM agent
- AICC (AI Contact Center), CCaaS (Contact Center as a Service)
- Conversational AI, dialogue system, task-oriented dialogue
- Agent Assist, Real-time Agent Coaching, Next Best Action
- Retrieval-Augmented Generation (RAG), knowledge base update
- Automated QA (Quality Assurance) for contact centers
- LLM fine-tuning, continual fine-tuning, parameter-efficient fine-tuning (LoRA, QLoRA)

### 기술 키워드 (한국어)
- 자가 학습 AI 상담봇, 자율 개선 AI 에이전트
- 콜봇, 상담봇, 음성봇, 챗봇
- 상담 어드바이저, 실시간 상담 코칭, 에이전트 어시스트
- AICC 구축형, 온프레미스 AI 컨택센터
- LLM 기반 고객센터, 생성형 AI 상담
- 금융권 AICC, 은행 AI 고객센터

### 시장/비즈니스 키워드
- B2B 구축형 AICC 수주, 금융권 RFP
- 고객센터 운영 효율성, 콜 처리율 (Call Containment Rate)
- 상담사 생산성, 평균 처리 시간 (AHT), 고객 만족도 (CSAT)
- AI 전환율, 자동화율 (Automation Rate)

---

## 3. 경쟁 분석 대상

### 국내 직접 경쟁사

| 경쟁사 | 솔루션/브랜드 | 특이사항 |
|--------|-------------|---------|
| SKT | 누구 비즈니스, AI Contact Center, A. (에이닷) | 자사 고객센터 자체 운용 경험, T-AX 등 금융 AI 협력 |
| KT | AI One Center, 기가지니 비즈, AI 통화비서 | KT DS 통해 B2B 구축형 강점, 금융권 다수 레퍼런스 |

### 국내 간접 경쟁사

| 경쟁사 | 솔루션/브랜드 | 특이사항 |
|--------|-------------|---------|
| 네이버클라우드 | CLOVA AiCall, CLOVA Studio | HyperCLOVA X 기반, 금융·공공 레퍼런스 확보 중 |
| 카카오엔터프라이즈 | 카카오 i 커넥트센터 | 카카오채널 연동 강점, 카카오뱅크 레퍼런스 |
| Maum.ai (마음AI) | 마음AI 컨택센터 솔루션 | AICC 전문 스타트업, 다수 금융사 레퍼런스 |
| Saltlux | 인텔리뷰, AICC 솔루션 | NLP/AI 전문, 공공·금융 AICC 구축 경험 |
| Sigor.ai | AICC 플랫폼 | 통신사 AICC 운용 경험 기반 스타트업 |

### 글로벌 경쟁사

| 경쟁사 | 솔루션/브랜드 | 특이사항 |
|--------|-------------|---------|
| Google | CCAI (Contact Center AI), Vertex AI Conversation | 실시간 에이전트 어시스트, AutoML 통합 |
| Amazon | Amazon Connect + Amazon Q | AWS 기반 구축형/클라우드 모두 지원 |
| Genesys | Genesys Cloud CX, AI Experience | 글로벌 CCaaS 1위, AI 자동화 강점 |
| NICE | CXone, Enlighten AI | 대형 엔터프라이즈 중심, AI 품질관리 특화 |
| Salesforce | Einstein for Service, Agentforce | CRM 연동 AI 에이전트, 자율 에이전트 기능 강조 |
| Five9 | Five9 Intelligent CX Platform | LLM 기반 자율 에이전트 최근 출시 |

---

## 4. 검색 전략

### 4-1. 기술 트렌드 쿼리

**영어 (3개)**
1. `"self-evolving" OR "self-improving" AI agent contact center 2025`
2. `continual learning LLM customer service chatbot autonomous improvement`
3. `RLHF contact center agent conversational AI fine-tuning production`

**한국어 (3개)**
1. `자가 학습 AI 상담봇 AICC 자율 개선 2025`
2. `LLM 기반 콜센터 AI 지속 학습 업데이트 방법론`
3. `에이전트 어시스트 실시간 코칭 생성형 AI 금융 고객센터`

### 4-2. 경쟁사 동향 쿼리

**영어 (3개)**
1. `SKT KT "AI contact center" "self-learning" OR "adaptive AI" Korea 2025`
2. `Google CCAI Amazon Connect "autonomous agent" "self-improving" 2025`
3. `Genesys NICE "agentic AI" contact center autonomous workflow update`

**한국어 (3개)**
1. `SKT KT AI 컨택센터 자가 학습 진화 에이전트 2025`
2. `네이버클라우드 카카오 AICC 자율 개선 LLM 업데이트 기술`
3. `마음AI Saltlux AICC 자가 학습 에이전트 금융권 수주`

### 4-3. 시장/투자 쿼리

**영어 (3개)**
1. `AI contact center market size 2025 2026 Korea B2B enterprise`
2. `AICC investment funding "self-evolving" OR "adaptive" conversational AI startup 2024 2025`
3. `Korean bank AI contact center RFP procurement "Big 5" banks`

**한국어 (3개)**
1. `국내 AICC 시장 규모 2025 B2B 구축형 성장률`
2. `5대 시중은행 AI 고객센터 구축 발주 현황 2024 2025`
3. `AICC 스타트업 투자 유치 자가 학습 에이전트 2025`

### 4-4. 특허/논문 쿼리

**영어 (3개)**
1. `"self-evolving agent" OR "autonomous improving agent" dialogue system patent 2023 2024`
2. `arxiv continual learning dialogue systems LLM fine-tuning customer service`
3. `"lifelong learning" conversational AI contact center quality improvement`

**한국어 (3개)**
1. `자가 진화 에이전트 특허 AI 상담 시스템 한국특허 2023 2024`
2. `지속 학습 대화 시스템 LLM 파인튜닝 논문 고객센터`
3. `자율 업데이트 챗봇 워크플로우 특허 국내 통신사`

---

## 5. 분석 깊이 권장

**권장 등급: Standard+** (Standard와 Deep 사이)

**근거:**
- B2B 수주 경쟁이 이미 심화된 분야 (SKT·KT·네이버·카카오 모두 공략 중)
- "5대 시중은행"이라는 구체적 고액 타겟 명시 → 금융권 규제·컴플라이언스 리서치 필수
- "Self Evolving"이라는 핵심 차별화 주장의 기술적 실체 검증 필요
- 단, KPI가 구체적 수치 없이 "경쟁력 강화"로만 명시 → SMART 검증 우선 필요

**심층 검증 우선 영역:**
1. "Self Evolving"의 기술적 정의 — 어떤 메커니즘(continual learning? RLHF? RAG 자동 업데이트?)인지 불명확
2. 금융권(5대 시중은행) 규제 적합성 — 금융보안원 가이드라인, AI 설명 가능성 요구
3. 경쟁사 유사 기능 보유 현황 — "진화" 기능이 실질적 차별화인지 확인 필요

---

## 6. 추가 조사 필요 항목

| 항목 | 현재 상태 | 중요도 |
|------|---------|--------|
| 구체적 KPI 수치 (매출, 수주 건수, 자동화율 목표) | 미명시 | 높음 |
| 예산 및 타임라인 | 미명시 | 높음 |
| "Self Evolving"의 기술 구현 방식 | 미명시 | 매우 높음 |
| LG U+ 현재 AICC 솔루션 기술 수준 | 부분 파악 필요 | 높음 |
| 5대 시중은행 AICC 도입 현황 및 RFP 일정 | 미명시 | 높음 |
| 금융권 AI 규제(금융보안원, FSS 가이드라인) 요건 | 별도 조사 필요 | 높음 |
| ixi-GEN sLLM의 AICC 적용 가능성 | 별도 조사 필요 | 중간 |

---

## 메타데이터

| 항목 | 내용 |
|------|------|
| 작성일 | 2026-02-24 |
| 작성자 | Senior Technology Strategist, LG U+ |
| 근거 원문 | 과제 제안서 (Self Evolving Agent, AICC 도메인) |
| 다음 단계 | SKILL-1 (선정검증) 또는 SKILL-2 (시장/기술 리서치) 실행 |
| 연관 파일 | 없음 (신규 과제) |
