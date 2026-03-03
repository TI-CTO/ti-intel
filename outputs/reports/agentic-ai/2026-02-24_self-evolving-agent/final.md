---
topic: Self Evolving Agent (AICC)
date: 2026-02-24
wtis_mode: proposal
skills_executed: [SKILL-0, SKILL-4, SKILL-1, SKILL-5]
confidence: medium
status: completed
total_references: 28
cross_validation: PARTIAL (1 error, 5 unverifiable)
recommendation: Build + Borrow Hybrid
---

# WTIS Proposal Report: Self Evolving Agent

## 경영진 요약

> **추천: Build + Borrow 하이브리드** (신뢰도: Medium)
>
> "Self Evolving Agent"는 LG U+의 AICC 사업에서 KT(국내 선두) 및 글로벌 플레이어(Genesys, NICE, Amazon) 대비 차별화할 수 있는 전략적 과제이나, **과제 제안서의 KPI가 정량화되지 않아 SMART 기준 3/5 미충족**으로 착수 전 재설계가 필수적이다.
>
> 핵심 기술인 "자가 진화"는 RAG 자동 업데이트(TRL 8-9, 즉시 구현 가능)부터 완전 자율 학습(TRL 3-4, 학술 실험 수준)까지 스펙트럼이 넓다. **즉시 상용화 가능한 RAG + LLM-as-Judge는 Build로 내재화하고, 미성숙 기술(Continual Fine-tuning, RLHF)은 산학 협력 Borrow로 접근하는 단계적 전략**을 권고한다.
>
> 금융권 망분리 규제 완화(2024 로드맵)와 AI 기본법(2026.1 시행)이 맞물려, **"자가 진화 + 금융 컴플라이언스 특화"라는 이중 차별화**가 5대 시중은행 수주의 핵심 포지셔닝이다.

---

## 1. 과제 개요

| 항목 | 내용 |
|------|------|
| 과제명 | Self Evolving Agent |
| 기술 도메인 | AICC (AI Contact Center) — AI/Data + B2B/Enterprise |
| 타겟 고객 | 콜봇, 상담 어드바이저, 고객센터, 5대 시중은행 B2B |
| 목표 KPI | 고객센터 운영 효율성 향상 → B2B 구축형 AICC 수주 경쟁력 상승 |
| 예산/타임라인 | **미명시** (재설계 필요) |

### 핵심 Pain Point (유추)
1. 기존 AICC의 고정 시나리오 한계 → 수동 업데이트 비용
2. LLM 기반 응답 생성은 이미 시장 표준 → "진화" 능력이 차기 차별화 포인트
3. 금융권의 높은 정확도·컴플라이언스·설명 가능성 요구

---

## 2. 기술 분석

### "Self Evolving"의 기술 성숙도 스펙트럼

| 기술 요소 | TRL | 상용화 상태 | 전략 |
|-----------|-----|------------|------|
| RAG 자동 업데이트 | 8-9 | 다수 상용 배포 | **Build** (즉시) |
| LLM-as-Judge 자동 수정 | 7-8 | Google CCAI 통합 | **Build** (0-6개월) |
| Override/Escalation 피드백 | 7-8 | 업계 표준 | **Build** (기존) |
| Continual Fine-tuning (LoRA) | 5-6 | 실험 단계, forgetting 미해결 | **Borrow** (산학 협력) |
| Closed-loop RLHF | 4-5 | 프로덕션 사례 극소 | **Borrow** (파일럿) |
| 완전 자율 Workflow Update | 3-4 | 학술 실험 수준 | **Watch** |

**학술 동향**: "Self-Evolving Agent" 개념의 첫 종합 서베이가 2025년 7-8월에야 arXiv에 등장 [1][2]. EvoAgent [3], AgentEvolver [4] 등 구현 연구도 게임/범용 환경 중심으로 AICC 특화 적용은 미확인.

### 4사분면 배치

```
              High Disruption
                   │
    [베팅]          │          [탐색]
    RAG 자동 업데이트 │    Closed-loop RLHF
    LLM-as-Judge    │    완전 자율 진화
                    │
────────────────────┼────────────────────
    High TRL        │         Low TRL
                    │
    [유지]          │          [Watch]
    Override/       │    Continual Fine-tuning
    Escalation      │    (LoRA + forgetting 완화)
                    │
              Low Disruption
```

---

## 3. 경쟁사 현황

### 국내

| 경쟁사 | 현황 | 자가 진화 기능 | 출처 |
|--------|------|---------------|------|
| **KT** | 국내 AICC 선두 (2017~), A'Cen 서비스, 마이K 에이전트 | 자율 학습 메커니즘 비공개 | [14][15][16] |
| **SKT** | 텔코 LLM (519B), MWC 2026 Agentic AICC 전시 | iterative RL 언급, 상세 비공개 | [11][12][13] |
| **네이버클라우드** | CLOVA AiCall, 롯데카드 40% 절감 실적 | 자율 학습 미공개 | [17][18] |
| **카카오** | CenterFlow AICC, 카나나 모델 | 자율 학습 미공개 | [19][20] |

### 글로벌

| 경쟁사 | 주요 성과 | 출처 |
|--------|----------|------|
| **Genesys** | 업계 최초 LAM 기반 Agentic Virtual Agent (2026.2.10 발표) | [22] |
| **NICE** | Cognigy 인수로 에이전틱 AI 포트폴리오 완성 | [23] |
| **Amazon** | Connect 에이전틱 기능 확대, re:Invent 2025 발표 | [21] |
| **Google** | CCAI에 LLM-as-Judge 기반 실시간 자동 수정 루프 통합 | [9] |

### LG U+ 포지션
- **KT 대비**: 약 3-5년 격차 (레퍼런스·점유율)
- **SKT 대비**: 약 1-2년 격차 (기술 내재화)
- **글로벌 대비**: 약 2-3년 격차 (상용화·투자 규모)
- **차별화 기회**: 금융 컴플라이언스 특화 (망분리 규제 + 한국어 + 로컬 지원)

---

## 4. 시장 데이터

| 지표 | 수치 | 출처 | 신뢰도 |
|------|------|------|--------|
| 글로벌 콜센터 AI TAM (2030) | USD 10.07B ~ 11.80B | Fortune BI / Mordor Intelligence | [B] |
| 국내 AICC 시장 (2030) | USD 350M / ~4,546억원 | 얼라이드마켓리서치 via 핀포인트뉴스 [15] | [B] |
| 국내 AICC 시장 (2025 추정) | ~1,650억원 (CAGR 23.7% 역산) | 교차검증 결과 [SKILL-5] | [B] |
| 국내 AICC CAGR | 23.7% | 얼라이드마켓리서치 [15] | [B] |
| LG U+ AICC 매출 목표 (2028) | 3,000억원 | Goover [14] | [C] |

> **교차검증 주의**: SKILL-1의 원래 SAM 수치(4,815억원)는 2030년 목표값과 혼동된 것으로 SKILL-5에서 지적됨. 위 표는 수정된 수치를 반영.

### 시장 촉매
- **금융위 망분리 개선 로드맵** (2024.8 발표) → 금융권 SaaS AICC 장벽 완화 [26]
- **AI 기본법** (2026.1 시행) → 단순 보조 AICC는 규제 대상 외, 자율 판단 확대 시 XAI 요건 충족 필수 [28]
- **은행권 AI·SaaS 도입 가속** (2026.1 보도) → 5대 시중은행 AICC 발주 본격화 예상 [30]

---

## 5. 3B 전략 권고

### Build + Borrow 하이브리드 (Build 60% / Borrow 30% / Watch 10%)

| 영역 | 전략 | 기간 | 근거 |
|------|------|------|------|
| RAG 자동 업데이트 + LLM-as-Judge | **Build** | 0-6개월 | TRL 7-9, 즉시 구현 가능 |
| 금융 컴플라이언스 모듈 (XAI) | **Build** | 3-6개월 | 글로벌 솔루션이 국내 규제 특화 어려움 |
| Continual Fine-tuning | **Borrow** | 6-18개월 | TRL 5-6, 산학 협력 (forgetting 해결 필요) |
| RLHF from Contact Logs | **Borrow** | 12-24개월 | TRL 4-5, 파일럿 수준 |
| 완전 자율 진화 | **Watch** | 24개월+ | TRL 3-4, 학술 수준 |

### Buy를 권고하지 않는 이유
- 국내 "Self Evolving AICC" 전문 벤더 부재
- 글로벌 솔루션 인수 규모가 과대 (NICE-Cognigy 수준)
- 단, 해외 소규모 스타트업 기술 라이선스는 추가 탐색 권장 [SKILL-5 P3 권고]

---

## 6. 교차검증 결과

| 항목 | 결과 |
|------|------|
| **최종 판정** | **PARTIAL** |
| 검증 클레임 | 12건 |
| 확인됨 | 4건 + 부분 확인 2건 |
| 오류 | 1건 (SAM 수치 과대 계상 → 본 보고서에서 수정 반영) |
| 미검증 | 5건 (NICE 인수 금액, Amazon Connect 수치, KT 점유율, CAGR 상한) |

### 주요 검증 결과
- **확인**: Genesys LAM 발표, 망분리 로드맵, AI 기본법, 네이버클라우드 실적, SKT MWC, arXiv 논문
- **오류 수정**: SAM 4,815억원 → ~1,650억원 (2025년 역산값)으로 수정
- **미검증 주의**: KT 69% 점유율, NICE $955M 인수 금액은 독립 확인 불가

---

## 7. 리스크

| 리스크 | 확률 | 영향 | 대응 |
|--------|------|------|------|
| KPI 미구체화로 R&D 방향 표류 | **H** | **H** | 착수 전 SMART KPI 재설계 필수 |
| Continual fine-tuning forgetting 미해결 | M | H | RAG+Judge 우선, learning은 별도 R&D 트랙 |
| KT 금융권 시장 선점 | **H** | **H** | 금융 컴플라이언스 특화로 차별화 + 중소 금융사 우선 |
| 글로벌 솔루션 국내 직접 진출 | M | M | 망분리·한국어·로컬 지원이 진입 장벽 |
| "Self Evolving" 기술적 실체 부족 | **H** | **H** | 단계적 브랜딩: Phase 1 "Learning Agent" → Phase 2 "Evolving Agent" |

---

## 8. 권고 및 Next Action

| 단계 | 기간 | 액션 | 담당 |
|------|------|------|------|
| **0** | 즉시 (1주) | SMART KPI 재설계: AHT 감소율, 자동화율, 수주 건수 등 정량 목표 확정 | 과제 PM + 전략팀 |
| **1** | 0-3개월 | Build Phase 1: RAG 자동 업데이트 + LLM-as-Judge PoC | AI Lab + AICC 사업부 |
| **2** | 0-3개월 | Borrow 파트너 쇼트리스트: Continual learning 공동연구 파트너 탐색 | CTO실 + 산학협력팀 |
| **3** | 3-6개월 | 금융 컴플라이언스 모듈 설계 (AI 기본법 + 금융보안원 가이드라인 매핑) | AI Lab + 법무팀 |
| **4** | 3-6개월 | 중소 금융사 1-2사 PoC → "Learning Agent" 레퍼런스 확보 | 영업 + AICC 사업부 |
| **5** | 6-12개월 | Continual fine-tuning 파일럿 (LoRA + forgetting 완화 실험) | AI Lab + 공동연구 |
| **6** | 12-18개월 | 5대 시중은행 RFP 대응: "Self Evolving Agent" 풀 패키지 | AICC 사업부 + 전략팀 |

---

## References

| # | 출처 | URL | 발행일 | 신뢰도 |
|---|------|-----|--------|--------|
| [1] | arXiv: Comprehensive Survey of Self-Evolving AI Agents | https://arxiv.org/abs/2508.07407 | 2025-08 | [A] |
| [2] | arXiv: A Survey of Self-Evolving Agents | https://arxiv.org/abs/2507.21046 | 2025-07 | [A] |
| [3] | arXiv: EvoAgent | https://arxiv.org/abs/2502.05907 | 2025-02 | [A] |
| [4] | arXiv: AgentEvolver | https://arxiv.org/abs/2511.10395 | 2025-11 | [A] |
| [6] | ACL 2024: Mitigating Catastrophic Forgetting (SSR) | https://aclanthology.org/2024.acl-long.77/ | 2024 | [A] |
| [9] | Google Cloud: Lessons from 2025 on agents and trust | https://cloud.google.com/transform/ai-grew-up-and-got-a-job | 2025 | [B] |
| [11] | SKT 뉴스룸: Telco LLM Customer Service | https://news.sktelecom.com/en/1647 | 2025 | [A] |
| [12] | The Fast Mode: SK Telecom at MWC 2026 | https://www.thefastmode.com/technology-solutions/47220 | 2026-02 | [B] |
| [13] | SKT 뉴스룸: Full-Stack AI at MWC 2026 | https://news.sktelecom.com/en/2742 | 2026-02 | [A] |
| [14] | Goover: 2025년 AICC 시장 경쟁 구도 | https://seo.goover.ai/report/202503/go-public-report-ko-53c96b24 | 2025-03 | [C] |
| [15] | 핀포인트뉴스: 통신3사가 콕 찍은 AICC | https://www.pinpointnews.co.kr/news/articleView.html?idxno=213245 | 2025 | [B] |
| [16] | kt cloud 기술 블로그: AI 에이전트 시리즈 | https://tech.ktcloud.com/entry/2025-03-ktcloud-ai-agent | 2025-03 | [B] |
| [17] | AI타임스: 네이버클라우드 롯데카드 40% 절감 | https://www.aitimes.com/news/articleView.html?idxno=170834 | 2025 | [B] |
| [19] | 카카오엔터프라이즈: CenterFlow | https://kakaoenterprise.com/press/centerflow-new-brand/ | 2025 | [A] |
| [20] | 카카오: Kanana Model Family | https://www.kakaocorp.com/page/detail/11334 | 2025 | [A] |
| [21] | AWS: Amazon Connect at re:Invent 2025 | https://aws.amazon.com/blogs/contact-center/amazon-connect-at-reinvent-2025 | 2025-11 | [A] |
| [22] | Genesys: LAM Agentic Virtual Agent | https://www.genesys.com/company/newsroom/announcements/genesys-unveils-industrys-first-agentic-virtual-agent-powered-by-lams | 2026-02-10 | [A] |
| [23] | NICE: Cognigy Acquisition | https://www.nice.com/press-releases/nice-closes-acquisition-of-cognigy | 2025-09 | [A] |
| [26] | 금융위: 망분리 개선 로드맵 | https://www.fsc.go.kr/no010101/82885 | 2024-08-13 | [A] |
| [27] | 금융보안원: AI 보안 가이드라인 | https://www.fsec.or.kr/bbs/detail?menuNo=69&bbsNo=11607 | 2025 | [A] |
| [28] | 피카부랩스: AI 기본법 2026 시행 | https://peekaboolabs.ai/blog/ai-basic-law-guide | 2025 | [B] |
| [30] | 전자신문: 은행권 망분리 규제 완화 | https://www.etnews.com/20260128000169 | 2026-01-28 | [B] |

---

*WTIS v3.0 Proposal Report | 2026-02-24 | AI-generated analysis — 최종 의사결정은 담당자 검토 필요*
*교차검증: PARTIAL (SAM 수치 수정 반영, 5건 미검증 주의)*
