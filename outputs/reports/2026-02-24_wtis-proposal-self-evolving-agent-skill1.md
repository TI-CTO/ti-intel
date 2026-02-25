---
topic: Self Evolving Agent 선정검증
date: 2026-02-24
wtis_skill: SKILL-1 (Selection Validator)
status: uncertain
confidence: medium
recommendation: hybrid
---

# WTIS 선정검증: Self Evolving Agent

## 경영진 요약

> **추천 방향: Build + Borrow 하이브리드** (신뢰도: Medium). Self Evolving Agent는 AICC 차세대 경쟁의 핵심 차별화 포인트로서 전략적 타당성이 높다. 그러나 과제 제안서에 KPI 수치, 예산, 타임라인이 모두 미명시되어 있어 SMART 기준을 충족하지 못하며, 핵심 기술인 완전 자율 continual fine-tuning은 TRL 4-5(연구-파일럿 경계)에 불과하다 [1][2]. 국내 AICC 시장은 KT가 69% 점유율로 선두이고 [14], 글로벌에서는 Genesys(LAM 기반 에이전틱 에이전트, 2026.2) [22], NICE(Cognigy $9.55억 인수) [23], Amazon Connect(AHT 38% 감소 실증) [21]가 구체적 성과를 내고 있다. LG U+는 2028년 AICC 매출 3,000억원 목표를 공표했으나 [14], 자가 진화 기능의 기술적 실체가 불분명한 상태로 과제를 진행할 경우 R&D 리스크가 크다. 따라서 즉시 상용화 가능한 RAG 자동 업데이트 + LLM-as-Judge(TRL 7-9)는 Build로 내재화하고, 완전 자율 continual learning(TRL 4-5)은 학계/스타트업과 Borrow(공동연구/기술제휴)로 접근하는 단계적 전략을 권고한다.

---

## 1. 목표 검증

### SMART 테스트

| 기준 | 평가 | 근거 |
|------|------|------|
| **Specific** | **Fail** | KPI가 "고객센터 운영 효율성 향상 + AICC 상품 경쟁력 강화 → B2B 구축형 AICC 수주 경쟁력 상승"으로 명시 — 구체적 수치(수주 건수, 매출액, 자동화율, AHT 감소폭) 없음 |
| **Measurable** | **Fail** | 정량 지표 부재. 경쟁사 사례: Amazon Connect는 AHT 38% 감소(140초→87초) [21], 네이버클라우드는 운영 리소스 40% 절감 [17]으로 구체적 측정 가능 |
| **Achievable** | **Uncertain** | 핵심 기술(완전 자율 continual fine-tuning)이 TRL 4-5 수준 [SKILL-4 1-3절]. RAG 자동 업데이트(TRL 8-9)만으로는 "Self Evolving"이라는 차별화 주장 약화. 단, 글로벌 학계에서 2025년 7-8월에 첫 종합 서베이가 발표될 정도로 emerging 분야 [1][2] |
| **Relevant** | **Pass** | LG U+ 2028년 AICC 매출 3,000억원 목표 [14], AI B2B 전략과 직접 정렬. 5대 시중은행 타겟은 금융권 망분리 규제 완화(2024 로드맵) [26]와 시기 적합 |
| **Time-bound** | **Fail** | 예산·타임라인 미명시. 경쟁사 비교: Genesys는 LAM 에이전틱 에이전트를 2026 FY Q1(2-4월) 전면 출시 확정 [22], SKT는 MWC 2026(3월)에서 Agentic AICC 전시 [12] |

**SMART 종합: 5항목 중 1 Pass / 1 Uncertain / 3 Fail → 재설계 필요**

### 시장 규모 (TAM/SAM/SOM)

| 구분 | 추정치 | 근거 |
|------|--------|------|
| **TAM** (글로벌 콜센터 AI 시장, 2030) | USD 10.07B ~ 11.80B | Fortune Business Insights / Mordor Intelligence [SKILL-4 3절]. CAGR 21.6-22.7% |
| **SAM** (국내 AICC 시장, 2025) | 약 4,815억원 (USD 350.88M) | Goover Report [14]. 단, [C] 등급 데이터로 공신력 제한적. 별도 추정: 한국 콘택트센터 SW 시장 USD 779.48M(2024) [IMARC] 중 AI 비중 약 45% 적용 시 약 3,500억원 |
| **SOM** (LG U+ 획득 가능 시장) | 약 1,500~3,000억원 (2028 목표) | LG U+ 공표 목표 3,000억원 [14]. KT 69% 점유율 감안 시, 현실적 SOM은 시장의 15-20% = 약 1,500억원 수준. 현재 점유율 데이터 부재 [데이터 갭] |

**시장 규모 평가**: 국내 AICC 시장은 CAGR 23.7-28.8%로 글로벌 평균(21.6-22.7%)을 상회하며 [SKILL-4 3절], 금융권 망분리 규제 완화가 2026년부터 본격 가속 요인으로 작용할 전망 [26][30]. 다만 KT 69% 점유율이라는 압도적 선두 구도에서 LG U+의 점유율 확대는 차별화 없이는 어렵다.

---

## 2. 기술 성숙도 맵

### 핵심 기술 요소별 TRL 평가

| 기술 요소 | TRL | 배포 사례 | 출처 |
|-----------|-----|----------|------|
| RAG 자동 업데이트 (지식베이스 자동 갱신) | 8-9 | 다수 상용 배포. 가장 현실적 자가 개선 메커니즘 | [SKILL-4 1-3절] |
| LLM-as-Judge (Autorater) 자동 수정 루프 | 7-8 | Google CCAI 에이전틱 파이프라인 통합 [9], 초기 상용화 단계 | [9] |
| Override/Escalation 피드백 루프 | 7-8 | 상담사 수정 데이터 재활용, 업계 표준 운영 패턴 | [8] |
| Continual Fine-tuning (LoRA/QLoRA) | 5-6 | 파일럿/실험 단계. Catastrophic forgetting 미해결 — SSR [6], SDFT [7] 등 연구 진행 중 | [6][7] |
| Closed-loop RLHF from Contact Logs | 4-5 | 연구-파일럿 경계. 프로덕션 적용 사례 극소 | [10] |
| Autonomous Workflow Update (완전 자율) | 3-4 | 학술 실험 수준. EvoAgent(게임 환경) [3], AgentEvolver(범용) [4] 등 연구 | [1][2][3][4] |

### 4사분면 배치

```
               파괴적 영향
                  ^
                  |
    [베팅]        |        [탐색]
    RAG 자동 업데이트    |   Closed-loop RLHF
    LLM-as-Judge  |   Autonomous Workflow
                  |   Update
    --------------|--------------->
    높은 TRL      |        낮은 TRL
                  |
    [유지]        |        [Watch]
    Override/     |   Continual Fine-tuning
    Escalation    |   (LoRA/QLoRA + 
    피드백 루프    |    Forgetting 완화)
                  |
```

**[베팅] (즉시 투자)**
- RAG 자동 업데이트 (TRL 8-9): 상용화 검증 완료, 즉시 구현 가능. 콜 로그 기반 지식베이스 자동 갱신으로 "진화" 스토리의 기반
- LLM-as-Judge (TRL 7-8): Google CCAI가 에이전틱 파이프라인에 통합 [9]. 실시간 품질 평가 + 자동 수정으로 운영 효율 극대화

**[Watch] (모니터링 + 소규모 실험)**
- Continual Fine-tuning (TRL 5-6): Catastrophic forgetting이 핵심 리스크. SSR [6], SDFT [7] 등 완화 기법이 연구 중이나 컴퓨팅 비용 2.5배 증가 [7]. 12-18개월 내 TRL 7 도달 가능성 관찰 필요

**[탐색] (장기 R&D / 학계 협력)**
- Closed-loop RLHF from Contact Logs (TRL 4-5): 고객 만족도, 해결률을 보상 신호로 활용하는 개념은 매력적이나, 프로덕션 적용 사례가 극소 [10]
- Autonomous Workflow Update (TRL 3-4): EvoAgent [3], AgentEvolver [4] 등 학술 실험 수준. AICC 도메인 적용은 미확인

**[유지] (현행 운영)**
- Override/Escalation 피드백 루프 (TRL 7-8): 이미 업계 표준 운영 패턴. 차별화 요소로는 부족하나 기본 인프라로 필수

---

## 3. 경쟁사 현황

### 비교표

| 경쟁사 | 유사 기능/솔루션 | 자가 진화 단계 | 타임라인 | 특허 | 투자 규모 | 출처 |
|--------|-----------------|---------------|---------|------|----------|------|
| **SKT** | Agentic AICC, 텔코 LLM (36개 전문가 데이터 학습), iterative RL | Agentic 전환 중, 자가 진화 메커니즘 비공개 | MWC 2026(3월) 전시 | 비공개 | A.X K1 (519B 파라미터) 개발, GTAA 합작법인 | [11][12][13] |
| **KT** | A'Cen(에이센), 상담 Assist (15초→5초 단축), AI 에이전트 '마이K' | AICC 점유율 69% 선두, A2A/MCP 지원. 자가 진화 구체적 미공개 | 마이K 2025.9 출시 | 비공개 | 연 2,500억원+ AICC 수주, 2017년부터 참여 | [14][15][16] |
| **네이버클라우드** | CLOVA AiCall (HyperCLOVA X), 롯데카드 40% 절감 | 자율 학습 미공개 | 2025.6 추론 모델 공개 | 비공개 | HyperCLOVA X SEED 오픈소스 | [17][18] |
| **카카오** | CenterFlow (구 카카오 i 커넥트센터), 카나나 모델 패밀리 | 자율 학습 미공개 | SaaS형 AICC 운영 중 | 비공개 | 카나나 에센스/나노 sLM | [19][20] |
| **Google** | CCAI + Vertex AI Conversation, UJET OEM | LLM-as-Judge 기반 실시간 자동 수정 루프 통합 | 상용 운영 중 | 다수 (미상세) | CCAI 플랫폼 투자 (미공개) | [9] |
| **Amazon** | Connect + Amazon Q, Nova Sonic, MCP 지원 | 29개 에이전틱 기능, Agentic Self-Service | 2025.11 re:Invent 발표 | 다수 | Centrica 1만명 배포 (AHT -38%) | [21] |
| **Genesys** | Cloud CX, AI Studio, LAM 기반 Agentic Virtual Agent | **업계 최초 LAM 기반 에이전틱 가상 에이전트** — "결정·실행" 특화 | 2026 FY Q1 (2-4월) 전면 출시 | Scaled Cognition APT-1 LAM 탑재 | M&T Bank, Banco Pichincha 파트너 | [22] |
| **NICE** | CXone Mpower + Cognigy 에이전틱 AI | Cognigy 인수로 에이전틱 AI 포트폴리오 완성 | 2025.9 인수 완료 | Cognigy 100+ 언어 | **USD 955M** (40년 역사 최대 인수) | [23] |

### Gap Analysis

**LG U+ 포지션 평가:**

1. **KT 대비 격차 (심각)**: KT는 국내 AICC 시장 69% 점유율 [14], 2017년부터 8년간 축적된 금융권 레퍼런스 보유. LG U+는 2028년 3,000억원 목표를 세웠으나 현재 점유율 데이터조차 미확인. 격차: 약 3-5년.

2. **SKT 대비 격차 (보통)**: SKT는 자체 텔코 LLM + iterative RL로 기술 내재화 진행 [11], MWC 2026에서 Agentic AICC 발표 [12]. LG U+도 ixi-GEN sLLM 보유하나 AICC 적용 현황 불명 [데이터 갭]. 격차: 약 1-2년.

3. **글로벌 대비 격차 (심각)**: Genesys LAM 에이전틱 에이전트 [22], NICE $9.55억 Cognigy 인수 [23], Amazon Connect 29개 에이전틱 기능 [21] 등 이미 상용화/대형 M&A 진행. 기술 성숙도에서 2-3년 격차.

4. **차별화 기회**: "Self Evolving"을 금융권 규제 적합형(XAI 설명 가능성 + 컴플라이언스 자동 검증)으로 특화하면 글로벌 솔루션과 차별화 가능. 국내 금융권은 망분리·보안 요건으로 글로벌 CCaaS 직접 도입이 어려움 [25][26].

---

## 4. 3B 전략 분석

### 판단 매트릭스

| 판단 요인 | 평가 | 근거 |
|-----------|------|------|
| **차별화 중요도** | 9/10 | KT 69% 점유율 선두 시장에서 "Self Evolving"은 유일한 차별화 스토리. Agentic AICC는 SKT·KT도 추진 중이므로 에이전틱만으로는 차별화 불가 |
| **내부 역량 보유** | 5/10 | ixi-GEN sLLM 보유하나 AICC 자가 진화 기술(continual learning, RLHF)은 미확인 [데이터 갭]. 에이전틱 콜봇(2025.12 출시)은 보유 |
| **시장 여유** | 12-18개월 | Genesys LAM(2026 Q1) [22], SKT MWC 2026(3월) [12] — 글로벌·국내 모두 2026년 상반기가 분수령. 18개월 기준 미충족 |
| **시장 진입 긴급도** | 7/10 | 금융권 망분리 완화(2026~) [30]로 5대 시중은행 AICC 발주 본격화 예상. 2027년이 핵심 수주 시즌 |
| **기술 격차** | 기술별 상이 | RAG/LLM-as-Judge: 0-1년 (Build 가능). Continual fine-tuning: 2년+ (Borrow 필요). 완전 자율: 3년+ (Watch) |

### 영역별 3B 판단

| 기술 영역 | 판단 | 이유 |
|-----------|------|------|
| RAG 자동 업데이트 + LLM-as-Judge | **Build** | TRL 7-9, 차별화 중요도 높음, 내부 역량으로 12개월 내 구현 가능. ixi-GEN sLLM + 콜봇 기존 인프라 활용 |
| Override/Escalation 피드백 루프 | **Build** | TRL 7-8, 업계 표준이므로 내부 구현 필수. 기존 AICC 운영 데이터 활용 |
| Continual Fine-tuning (LoRA 기반) | **Borrow** | TRL 5-6, catastrophic forgetting 미해결. 학계(KAIST, SNU AI 연구실) 또는 스타트업(Maum.ai)과 공동연구. SDFT 등 최신 기법 공동 실험 |
| Closed-loop RLHF from Contact Logs | **Borrow** | TRL 4-5, 프로덕션 적용 사례 극소 [10]. 산학 협력으로 파일럿 진행, 데이터(콜 로그)는 LG U+ 고유 자산으로 활용 |
| Autonomous Workflow Update | **Watch** | TRL 3-4, 학술 실험 수준. 2-3년 후 재평가. EvoAgent [3], AgentEvolver [4] 등 논문 모니터링 |
| 금융권 규제 컴플라이언스 (XAI) | **Build** | 차별화 9/10, 글로벌 솔루션이 국내 규제 특화하기 어려움. AI 기본법 [28] + 금융보안원 가이드라인 [27] 준수 모듈을 자체 개발하면 KT·SKT 대비 차별화 |

### 최종 3B 결론: **Build + Borrow 하이브리드**

- Build 비중: 60% — 즉시 상용화 가능한 RAG/LLM-as-Judge + 금융 컴플라이언스 내재화
- Borrow 비중: 30% — Continual learning/RLHF는 산학 협력 또는 기술 제휴
- Watch 비중: 10% — 완전 자율 진화는 모니터링
- Buy 미권고 이유: 국내 "Self Evolving AICC" 전문 솔루션 벤더가 부재. 글로벌 솔루션(Genesys, NICE)은 직접 인수 규모($9.5억+ [23]) 대비 LG U+ 투자 가용 범위 초과 가능성

---

## 5. 최종 제언

**[과제명]**: Self Evolving Agent

**[추천 방향]**: Build + Borrow 하이브리드 (단계적 접근)

**[핵심 근거]**:
- **시장 근거**: 국내 AICC 시장 CAGR 23.7-28.8% [SKILL-4 3절], 2025년 약 4,815억원 규모. 금융권 망분리 규제 완화(2026~)로 5대 시중은행 AICC 발주 본격화 예상 [26][30]. LG U+ 2028 목표 3,000억원 달성에 "Self Evolving"이 핵심 차별화 포인트
- **기술 근거**: RAG 자동 업데이트(TRL 8-9)와 LLM-as-Judge(TRL 7-8)는 즉시 Build 가능. Continual fine-tuning(TRL 5-6)과 RLHF(TRL 4-5)는 2025년에야 학계 서베이가 등장한 초기 분야로 [1][2], 산학 협력이 적합. 글로벌 특허 검색 결과 확인 불가 [데이터 갭]
- **사업 근거**: KT 69% 점유율 시장에서 에이전틱 AICC만으로는 차별화 부족. "자가 진화 + 금융 컴플라이언스 특화"라는 이중 차별화로 포지셔닝해야 5대 시중은행 수주 가능

**[리스크]**:

| 리스크 | 확률 | 영향 | 대응 |
|--------|------|------|------|
| KPI 미구체화로 R&D 방향 표류 | H | H | 과제 착수 전 SMART KPI 재설계 필수 (예: "금융권 AICC 수주 2건, AHT 30% 감소, 자동화율 60%") |
| Continual fine-tuning catastrophic forgetting 미해결 | M | H | RAG+LLM-as-Judge 우선 구현으로 리스크 분리. Continual learning은 별도 R&D 트랙 |
| KT 선점으로 금융권 시장 잠식 | H | H | 금융 컴플라이언스 특화(XAI + AI 기본법 준수 모듈)로 차별화. 중소 금융사(저축은행, 증권사) 우선 레퍼런스 확보 |
| 글로벌 솔루션(Genesys, NICE) 국내 금융권 직접 진출 | M | M | 망분리 규제 + 한국어 특화 + 로컬 지원이 진입 장벽. 제네시스 클라우드 혁신금융서비스 지정 [25]은 경계 요소 |
| "Self Evolving" 차별화 주장의 기술적 실체 부족 | H | H | 단계적 구현: Phase 1은 RAG+Judge로 "Learning Agent", Phase 2에서 Continual learning 추가하여 "Evolving Agent"로 브랜딩 |

**[Next Action]**:

| 단계 | 기간 | 액션 | 담당 |
|------|------|------|------|
| 0 | 즉시 (1주) | **KPI 재설계**: SMART 기준 충족하는 수치 목표 수립 (예: AHT 감소율, 자동화율, 수주 건수, 매출액) | 과제 PM + 전략팀 |
| 1 | 0-3개월 | **Build Phase 1**: RAG 자동 업데이트 파이프라인 구축 (콜 로그→지식베이스 자동 갱신). LLM-as-Judge 품질 평가 루프 PoC | AI Lab + AICC 사업부 |
| 2 | 0-3개월 | **Borrow 파트너 탐색**: Continual learning 공동연구 파트너 쇼트리스트 (KAIST, SNU, Maum.ai, 학회 논문 저자 컨택) | CTO실 + 산학협력팀 |
| 3 | 3-6개월 | **Build Phase 2**: LLM-as-Judge + Override 피드백 루프 통합. 금융 컴플라이언스 모듈 설계 (AI 기본법 [28] + 금융보안원 [27] 요건 매핑) | AI Lab + 법무팀 |
| 4 | 3-6개월 | **파일럿 확보**: 중소 금융사(저축은행, 증권사) 1-2사 PoC 계약. "Learning Agent" 브랜딩 | 영업 + AICC 사업부 |
| 5 | 6-12개월 | **Borrow Phase 1**: Continual fine-tuning(LoRA + SSR/SDFT) 파일럿. LG U+ 콜 로그 데이터로 catastrophic forgetting 실험 | AI Lab + 공동연구 파트너 |
| 6 | 12-18개월 | **5대 시중은행 RFP 대응**: Phase 1+2 기반 "Self Evolving Agent" 풀 패키지 제안. 금융 컴플라이언스 특화 포지셔닝 | AICC 사업부 + 전략팀 |
| 7 | 18-24개월 | **RLHF 파일럿**: 실제 운영 데이터 기반 closed-loop RLHF 실험. 성과 측정 후 Phase 3("Evolving Agent") 브랜딩 결정 | AI Lab |

---

## 신뢰도: Medium

**Medium 판단 근거:**

- **높은 확신 (High Confidence)**:
  - 국내 AICC 시장 성장률이 높고(CAGR 23.7-28.8%), 금융권 규제 완화가 시장 가속 요인인 점 [26][30]
  - RAG 자동 업데이트(TRL 8-9)와 LLM-as-Judge(TRL 7-8)는 즉시 구현 가능한 검증된 기술 [SKILL-4 1-3절]
  - KT 69% 점유율 선두, 경쟁 심화 사실 [14]
  - 글로벌 빅플레이어(Genesys, NICE, Amazon)가 구체적 제품/투자를 집행 중인 사실 [21][22][23]

- **추가 검증 필요 (Needs Verification)**:
  - LG U+ ixi-GEN sLLM의 AICC 적용 현황 — 사내 확인 필수 [데이터 갭]
  - 국내 AICC 시장 규모 수치(Goover Report [C] 등급) — IDC/Gartner 리포트로 교차 검증 필요
  - 5대 시중은행 AICC RFP 구체적 일정 — 금융권 조달 시스템 직접 확인 필요
  - 국내 통신사 AICC 자가학습 메커니즘 — 3사 모두 비공개 상태
  - 국내 AICC 자가진화 특허 현황 — KIPRIS 검색 필요
  - 과제의 예산·타임라인·KPI 수치 — 제안서 보완 필수

---

## References (SKILL-4에서 인용한 출처)

| # | 출처 | URL | 신뢰도 |
|---|------|-----|--------|
| 1 | arXiv: A Comprehensive Survey of Self-Evolving AI Agents (2508.07407) | https://arxiv.org/abs/2508.07407 | [A] |
| 2 | arXiv: A Survey of Self-Evolving Agents (2507.21046) | https://arxiv.org/abs/2507.21046 | [A] |
| 3 | arXiv: EvoAgent (2502.05907) | https://arxiv.org/abs/2502.05907 | [A] |
| 4 | arXiv: AgentEvolver (2511.10395) | https://arxiv.org/abs/2511.10395 | [A] |
| 5 | arXiv: ALAS (2508.15805) | https://arxiv.org/html/2508.15805v1 | [A] |
| 6 | ACL 2024: Mitigating Catastrophic Forgetting (SSR) | https://aclanthology.org/2024.acl-long.77/ | [A] |
| 7 | InfoWorld: Self-distillation fix for catastrophic forgetting | https://www.infoworld.com/article/4131242 | [B] |
| 8 | Mosaicx: AI-Driven Contact Center Automation Trends 2025 | https://www.mosaicx.com/blog/contact-center-ai-trends | [B] |
| 9 | Google Cloud Blog: Lessons from 2025 on agents and trust | https://cloud.google.com/transform/ai-grew-up-and-got-a-job-lessons-from-2025-on-agents-and-trust | [B] |
| 10 | CleverX: Enterprise RLHF Implementation Checklist 2025 | https://cleverx.com/blog/enterprise-rlhf-implementation-checklist | [C] |
| 11 | SKT 뉴스룸: AI-Powered Customer Service Utilizing Proprietary Telco LLM | https://news.sktelecom.com/en/1647 | [A] |
| 12 | The Fast Mode: SK Telecom Unveils Full-Stack AI at MWC 2026 | https://www.thefastmode.com/technology-solutions/47220 | [B] |
| 13 | SKT 뉴스룸: Full-Stack AI at MWC 2026 | https://news.sktelecom.com/en/2742 | [A] |
| 14 | Goover 리포트: 2025년 AICC 시장 경쟁 구도와 통신사 전략 | https://seo.goover.ai/report/202503/go-public-report-ko-53c96b24 | [C] |
| 15 | 핀포인트뉴스: 통신3사가 콕 찍은 AICC | https://www.pinpointnews.co.kr/news/articleView.html?idxno=213245 | [B] |
| 16 | kt cloud 기술 블로그: AI 에이전트 시리즈 | https://tech.ktcloud.com/entry/2025-03-ktcloud-ai-agent | [B] |
| 17 | AI타임스: 네이버클라우드 롯데카드 AICC 40% 절감 | https://www.aitimes.com/news/articleView.html?idxno=170834 | [B] |
| 18 | AI타임스: 하이퍼클로바X 추론 모델 공개 계획 | https://www.aitimes.com/news/articleView.html?idxno=170749 | [B] |
| 19 | 카카오엔터프라이즈: 센터플로우 브랜드 변경 | https://kakaoenterprise.com/press/centerflow-new-brand/ | [A] |
| 20 | 카카오: Kanana Model Family 소개 | https://www.kakaocorp.com/page/detail/11334 | [A] |
| 21 | AWS: Amazon Connect at re:Invent 2025 | https://aws.amazon.com/blogs/contact-center/amazon-connect-at-reinvent-2025 | [A] |
| 22 | Genesys: LAM 기반 Agentic Virtual Agent | https://www.genesys.com/company/newsroom/announcements/genesys-unveils-industrys-first-agentic-virtual-agent-powered-by-lams | [A] |
| 23 | NICE: Closes Acquisition of Cognigy | https://www.nice.com/press-releases/nice-closes-acquisition-of-cognigy | [A] |
| 24 | Salesforce: What Is Autonomous Customer Service | https://www.salesforce.com/service/what-is-autonomous-customer-service/ | [A] |
| 25 | 디지털데일리: 망분리 규제 완화 속 금융권 AICC 시대 개막 | https://www.ddaily.co.kr/page/view/2025091014390239063 | [B] |
| 26 | 금융위원회: 금융분야 망분리 개선 로드맵 | https://www.fsc.go.kr/no010101/82885 | [A] |
| 27 | 금융보안원: AI 보안 가이드라인 개정 계획 | https://www.fsec.or.kr/bbs/detail?menuNo=69&bbsNo=11607 | [A] |
| 28 | 피카부랩스: AI 기본법 완전 정리 (2026.1 시행) | https://peekaboolabs.ai/blog/ai-basic-law-guide | [B] |
| 29 | 삼성SDS: 2025년 국내 은행 AI 활용 전망 | https://www.samsungsds.com/kr/insights/ai-in-banking-in-2025.html | [B] |
| 30 | 전자신문: 은행권 망분리 규제 완화 AI·SaaS 도입 가속 | https://www.etnews.com/20260128000169 | [B] |
