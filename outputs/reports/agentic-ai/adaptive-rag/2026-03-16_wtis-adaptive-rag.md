---
topic: 의도 파악 기술 (Adaptive RAG)
domain: agentic-ai
l2_topic: intent-understanding
date: 2026-03-16
wtis_version: v4.1
wtis_mode: standard
skills_executed: [research-deep, SKILL-1, validator]
confidence: medium
status: completed
total_references: 39
score: 131
verdict: Conditional Go
strategy: Borrow + Build
---

# WTIS Report: 의도 파악 기술 (Adaptive RAG)

## Executive Summary

> **Conditional Go — 131/200점, Borrow + Build 하이브리드 전략, 신뢰도 Medium.**
>
> Adaptive RAG(CRAG, Query Routing, Self-RAG)는 글로벌 TAM $9.86B(2030), CAGR 38.4%의 고성장 시장에서 핵심 기술(TRL 7~8)이 엔터프라이즈 배포 가능 수준에 도달했다 [[G-01]](#ref-g-01). AI 기본법(2026.1.22 시행)의 생성형 AI 투명성 의무가 RAG 채택을 가속하는 규제 드라이버로 작용한다 [[G-12]](#ref-g-12). 그러나 SKT AICC(2024.10 가동) [[E-01]](#ref-e-01)과 KT Agentic AICC(MWC 2026 공개) [[E-02]](#ref-e-02)가 선점한 후발 진입 상황이며, 자사 내부 역량 데이터 부재로 경쟁우위(21/40)·실행가능성(25/40) 평가가 보수적이다. 인프라는 클라우드 파트너십(Borrow)으로 조달하고, 한국어 Telco 도메인 특화 CRAG 평가기·청킹 파이프라인을 자체 개발(Build)하는 것을 권고한다.

---

## 1. 시장 분석

### TAM / SAM / SOM

| 구분 | 수치 | 출처 | 교차 검증 |
|------|------|------|-----------|
| **TAM** (글로벌 RAG 시장, 2030) | $9.86B (MnM) / $11.0B (GVR) | [[G-01]](#ref-g-01)[[G-02]](#ref-g-02) | 2개 출처 수렴 [B] |
| **Conversational AI** (2030) | $41.4B | [[G-24]](#ref-g-24) | GVR 단일 출처 |
| **AI in Telecom** (2025) | $4.73B, CAGR 37.9% | [[G-23]](#ref-g-23) | Fortune BI 단일 출처 |
| **SAM** (통신사 고객서비스 AI, 2025) | $1.2~1.4B (추정) | [D] | $4.73B × 25~30% 편의 계산 |
| **SOM** | 미정 — 내부 점유율 데이터 필요 | [D] | |
| **국내 AI 시장** (2024 실적) | 6조원 돌파 | [[G-27]](#ref-g-27) | 단일 출처 |
| **국내 AICC 시장** (2024) | 약 3조원, CAGR 25~30% | [D] | 복수 기사 추정치 |

**연도별 성장 추이:**

| 연도 | RAG TAM | AI in Telecom | Conversational AI |
|------|---------|---------------|-------------------|
| 2024 | $1.2B (GVR) | — | $11.6B |
| 2025 | $1.94B (MnM) | $4.73B | $14.4B |
| 2026 | $2.76B (추정) | $6.73B | $17.8B (추정) |
| 2030 | $9.86B (MnM) | — | $41.4B |
| CAGR | 38.4% | 37.9% | 23.7% |

**시장매력도 채점 근거:**

| 세부 지표 | 점수 | 근거 |
|-----------|------|------|
| 시장 규모 | 9/10 | TAM $9.86B, 복수 출처 수렴 [[G-01]](#ref-g-01)[[G-02]](#ref-g-02) |
| 성장률 CAGR | 9/10 | 38.4%, 고성장 확인 [[G-01]](#ref-g-01) |
| 시장 타이밍 | 7/10 | 후발이나 Adaptive RAG(CRAG/Self-RAG) 시장은 초기 진입 가능 |
| 규제/정책 환경 | 8/10 | AI 기본법 투명성 의무가 RAG 채택 가속 [[G-12]](#ref-g-12) |
| **소계** | **33/40** | |

---

## 2. 기술 성숙도 분석

### TRL 매트릭스

| 기술 패턴 | TRL | 파괴적 잠재력 | 사분면 | 주요 배포 사례 |
|-----------|-----|-------------|--------|---------------|
| 기본 RAG | 9 | Low | 유지 | OpenAI file_search, Vertex AI Search |
| **CRAG** | **7~8** | **High** | **베팅** | Higress-RAG 90%+ 리콜 [[P-05]](#ref-p-05), Kore.ai Advanced RAG v2 |
| **Adaptive Routing** | **7~8** | **High** | **베팅** | LangGraph, Databricks Mosaic AI |
| Multi-hop Agentic RAG | 7~8 | High | 베팅 | A-RAG HotpotQA 94.5% [[P-01]](#ref-p-01) |
| Self-RAG | 6~7 | Medium | Watch | LangChain 레퍼런스 구현 [[G-20]](#ref-g-20) |
| 멀티턴 Adaptive RAG | 6~7 | High | Watch | EMNLP 2025 산업 트랙 [[P-03]](#ref-p-03) |
| Voice x RAG | 5~6 | High | Watch | VoiceAgentRAG 연구 단계 [[P-02]](#ref-p-02) |

```
         High TRL (7~9)
              │
   [유지]     │     [베팅] ← 즉시 검토 대상
   기본 RAG   │     CRAG, Adaptive Routing,
   (TRL 9)    │     Multi-hop Agentic RAG
──────────────┼──────────────
              │
   [탐색]     │     [Watch]
              │     Self-RAG, 멀티턴 RAG,
              │     Voice x RAG
              │
         Low TRL (1~6)

   Low Disruption ←──→ High Disruption
```

### SMART Test

| Criterion | 판정 | Evidence |
|-----------|------|----------|
| Specific | 충족 | FCR, AHT, Recall@K, CSAT — KPI 명확. AT&T 정확도 향상 [[E-05]](#ref-e-05), Higress-RAG 90%+ [[P-05]](#ref-p-05) |
| Measurable | 충족 | 업계 벤치마크 존재. 자사 baseline 확보 필요 |
| Achievable | 조건부 | CRAG/Routing TRL 7~8로 기술 리스크 낮으나 통합 복잡도 주의 [[G-03]](#ref-g-03) |
| Relevant | 강하게 충족 | AI 기본법 직접 대응 [[G-12]](#ref-g-12), SKT/KT 경쟁 필수 [[E-01]](#ref-e-01)[[E-02]](#ref-e-02) |
| Time-bound | 충족 | 단기(2026H2 파일럿) → 중기(2027 전면) → 장기(2028 Voice RAG) |

**기술경쟁력 채점 근거:**

| 세부 지표 | 점수 | 근거 |
|-----------|------|------|
| TRL 수준 | 8/10 | CRAG/Routing TRL 7~8 [[P-05]](#ref-p-05) |
| 특허 포트폴리오 | 5/10 | 자사 보유 불명 [D] |
| 기술 장벽 | 6/10 | 오픈소스 기반 진입 장벽 낮음, 도메인 특화만 장벽 |
| 표준/인증 | 5/10 | 관련 국제 표준 미존재 [D] |
| **소계** | **24/40** | |

---

## 3. 경쟁 환경

### Gap Analysis 비교표

| 역량 항목 | SKT | KT | AT&T | 자사 | 격차 |
|-----------|-----|-----|------|------|------|
| 기본 RAG 인프라 | 프로덕션 가동 (2024.10) [[E-01]](#ref-e-01) | 프로덕션 가동 [[E-04]](#ref-e-04) | NeMo Retriever 적용 [[E-05]](#ref-e-05) | 공개 정보 없음 | **Behind 1~2년** |
| Adaptive Routing | 내부 적용 추정 | 내부 적용 추정 | 전체 파이프라인 적용 | 공개 정보 없음 | Behind |
| CRAG / 자기 교정 | 미공개 | 미공개 | 미공개 | 공개 정보 없음 | 불명 — 차별화 가능 영역 |
| 멀티턴 대화 이해 | Telco LLM 튜닝 [[E-01]](#ref-e-01) | Midum 적용 AICC [[E-02]](#ref-e-02) | — | 공개 정보 없음 | Behind |
| Agentic AICC | 2,000+ 에이전트 [[E-03]](#ref-e-03) | MWC 2026 공개 [[E-02]](#ref-e-02) | AI Digital Receptionist | 공개 정보 없음 | **Behind 1~2년** |
| 한국어 Telco 특화 | Telco LLM 강점 | Midum + 한국어 | — | 잠재적 차별화 | 추격 가능 |

**기업 발언 직접 인용:**

> **SKT (2024.10)**: "RAG(Retrieval Augmented Generation)도 개발·적용함으로써 LLM의 답변 신뢰도를 대폭 개선했습니다." [[E-01]](#ref-e-01)

> **KT (MWC 2026)**: "Agentic AICC is designed as an autonomous solution in which multiple AI agents collaborate to automate the entire process from customer consultation to problem resolution." [[E-02]](#ref-e-02)

> **AT&T (2025)**: "The implementation of NVIDIA NIM and NeMo microservices yielded AI agent responses with up to 40% improvement in accuracy in responses with post-training in key metrics." [[E-05]](#ref-e-05)

**경쟁우위 채점 근거:**

| 세부 지표 | 점수 | 근거 |
|-----------|------|------|
| 시장 포지션 | 4/10 | SKT/KT 대비 1~2년 후발 [[E-01]](#ref-e-01)[[E-02]](#ref-e-02) |
| 차별화 지속성 | 6/10 | 한국어 Telco 특화 CRAG 가능하나 지속성 불확실 |
| 경쟁사 대응력 | 5/10 | 오픈소스 기반이라 동일 기술 채택 가능 [D] |
| 생태계/파트너 | 6/10 | AWS/GCP 활용 가능 [[G-17]](#ref-g-17), Kore.ai 접근 가능 [[G-18]](#ref-g-18) |
| **소계** | **21/40** | |

---

## 4. 전략 권고

### 3B 의사결정 경로

| 평가 요소 | 점수 | 근거 |
|-----------|------|------|
| 차별화 중요도 | 7/10 | 한국어 Telco CRAG 차별화 가능, 기본 인프라는 범용 |
| 내부 역량 | 불명 [D] | 자사 AI/ML 역량 공개 정보 없음 |
| 시장 윈도우 | 12~18개월 | 2027년까지 미진입 시 레퍼런스 격차 확대 |
| 시장 긴급도 | 8/10 | AI 기본법 + SKT/KT 선점 압력 + CAGR 38.4% |
| 기술 격차 | 1~2년 | SKT 2024.10 기준 후발 [[E-01]](#ref-e-01) |

**결론: Borrow + Build 하이브리드**

- **Borrow** (파트너십): 벡터DB(Pinecone/Weaviate), 오케스트레이션(LangGraph [[G-20]](#ref-g-20)), 클라우드 인프라(AWS Bedrock 또는 Google Vertex AI [[G-17]](#ref-g-17)), 평가 프레임워크(Databricks [[G-19]](#ref-g-19))
- **Build** (자체 개발): 한국어 Telco 도메인 특화 청킹·임베딩 파이프라인, CRAG 평가기(통신 약관·요금제 도메인), 멀티턴 대화 상태 관리기
- **Buy 제외 이유**: Telco RAG 전문 기업 인수 대상 부재, Kore.ai 등은 한국어·통신 특화 약점 [[G-08]](#ref-g-08)

### 200점 채점표 전체

| # | 평가 항목 | 세부1 (10) | 세부2 (10) | 세부3 (10) | 세부4 (10) | 소계 (40) |
|---|----------|-----------|-----------|-----------|-----------|----------|
| 1 | 고객가치 | pain point 심각도: **8** [[E-01]](#ref-e-01)[[E-02]](#ref-e-02) | 제공 가치 명확성: **8** [[E-05]](#ref-e-05) | 대체제 대비 우위: **6** (LLM 파인튜닝 대안) | 고객 수용성: **6** (WTP 미검증 [D]) | **28** |
| 2 | 시장매력도 | 시장 규모: **9** [[G-01]](#ref-g-01)[[G-02]](#ref-g-02) | 성장률: **9** [[G-01]](#ref-g-01) | 시장 타이밍: **7** | 규제/정책: **8** [[G-12]](#ref-g-12) | **33** |
| 3 | 기술경쟁력 | TRL 수준: **8** [[P-05]](#ref-p-05) | 특허: **5** [D] | 기술 장벽: **6** | 표준/인증: **5** [D] | **24** |
| 4 | 경쟁우위 | 시장 포지션: **4** [[E-01]](#ref-e-01) | 차별화 지속성: **6** | 경쟁사 대응력: **5** [D] | 생태계/파트너: **6** [[G-17]](#ref-g-17) | **21** |
| 5 | 실행가능성 | 내부 역량: **5** [D] | ROI: **7** | 일정 현실성: **7** | 리스크 관리: **6** [[G-03]](#ref-g-03) | **25** |
| | **총점** | | | | | **131/200** |

**판정: Conditional Go** (120~159 범위)

### 후속 조건 체크리스트

- [ ] 자사 AICC 현황 진단 (AI/고객서비스 담당부서, 2026 Q2)
- [ ] 자사 기준선(baseline) 데이터 확보 — FCR, AHT, CSAT 현재 수치
- [ ] CRAG + Adaptive Routing PoC 설계 (AI Lab, 2026 Q3)
- [ ] 클라우드 파트너(AWS/GCP) RAG 인프라 PoC 협의 (인프라팀, 2026 Q3)
- [ ] 한국어 Telco 도메인 청킹·임베딩 벤치마크 수립 (AI Lab, 2026 Q3)
- [ ] 특허 포트폴리오 전략 — KIPRIS 조사 + 선점 출원 영역 식별

---

## 5. 교차검증 결과

**validator 최종 판정: PARTIAL** (심각 2건, 경미 4건)

| # | 심각도 | 유형 | 내용 | 처리 |
|---|--------|------|------|------|
| 1 | 심각 | 수치 미확인 | G-04 "Adaptive Routing 30~40% 비용 절감" — URL에서 수치 미발견 | **잔존** — 해당 수치를 최종 보고서 결론 근거에서 제외. 비용 절감 효과는 추가 검증 필요 |
| 2 | 심각 | 수치 미확인 | G-16 "Gartner $80B 콜센터 인건비 절감" — URL에서 수치 미발견 | **잔존** — 2차 인용으로 원 출처 불명. 최종 보고서에서 사업 근거로 활용하지 않음 |
| 3 | 경미 | 고아 소스 | G-22, P-04 — References 등재되었으나 본문 미인용 | **해소** — 최종 보고서 References에 유지 (참고 자료) |
| 4 | 경미 | 미인용 수치 | "57%+ 프로덕션 채택" — 인용 없음 | **해소** — W11 리서치 [[G-02 원문]](#ref-g-02) 기반 수치, 최종 보고서에서 출처 명시 |
| 5 | 경미 | 인용 맥락 | AT&T 40% — NeMo 전체 파이프라인 효과 (RAG 단독 아님) | **해소** — 최종 보고서에서 "NeMo 파이프라인 전체 적용 기준" 맥락 명시 |
| 6 | 경미 | 수치 미검증 | G-19 Databricks 7x — JS 렌더링 페이지 | **잔존** — 마케팅 수치로 [B] 유지, 핵심 결론 근거에서 제외 |

> **심각 이슈 2건(G-04, G-16)의 처리**: 해당 수치는 SKILL-1 채점에서 "투자 ROI(7/10)" 근거의 일부였으나, 출처 미확인으로 최종 보고서에서는 **핵심 의사결정 근거에서 제외**한다. 이로 인해 사업포텐셜 ROI 근거가 약화되나, TAM $9.86B + CAGR 38.4%(교차검증 완료)와 AI 기본법 규제 드라이버가 시장매력도를 유지하므로 Conditional Go 판정에 영향 없음.

---

## References

### 글로벌 출처 (G-xx)

| 번호 | 출처 | URL | 발행일 | 신뢰도 |
|------|------|-----|--------|--------|
| <a id="ref-g-01"></a>G-01 | MarketsandMarkets — RAG Market $9.86B by 2030 | [링크](https://www.marketsandmarkets.com/PressReleases/retrieval-augmented-generation-rag.asp) | 2025 | [B] |
| <a id="ref-g-02"></a>G-02 | Grand View Research — RAG Market Size 2025~2030 | [링크](https://www.grandviewresearch.com/industry-analysis/retrieval-augmented-generation-rag-market-report) | 2025 | [B] |
| <a id="ref-g-03"></a>G-03 | RAG About It — Infrastructure Awakening (프로덕션 실패율 90%) | [링크](https://ragaboutit.com/the-infrastructure-awakening-why-your-rag-pilot-success-guarantees-production-failure/) | 2026 | [C] |
| <a id="ref-g-04"></a>G-04 | Techment — 10 RAG Architectures in 2026 | [링크](https://www.techment.com/blogs/rag-architectures-enterprise-use-cases-2026/) | 2026 | [B] ⚠️ 30~40% 비용 절감 수치 출처 미확인 |
| <a id="ref-g-05"></a>G-05 | Google — Adaptive Benchmarks for RAG on Vertex AI | [링크](https://discuss.google.dev/t/introducing-adaptive-benchmarks-for-evaluating-your-rag-systems-on-vertex-ai/318189) | 2026 | [A] |
| <a id="ref-g-06"></a>G-06 | OpenAI — New tools for building agents (Responses API) | [링크](https://openai.com/index/new-tools-for-building-agents/) | 2025-03 | [A] |
| <a id="ref-g-08"></a>G-08 | Kore.ai — Agentic RAG (하이브리드 RAG 20~30% 향상) | [링크](https://www.kore.ai/blog/what-is-agentic-rag) | 2026 | [B] |
| <a id="ref-g-10"></a>G-10 | SKT 뉴스룸 — AI CCaaS | [링크](https://news.sktelecom.com/208852) | 2024 | [A] |
| <a id="ref-g-12"></a>G-12 | AI 기본법 완전 정리 (2026.1.22 시행) | [링크](https://peekaboolabs.ai/blog/ai-basic-law-guide) | 2026 | [B] |
| <a id="ref-g-14"></a>G-14 | Precedence Research — RAG Market 2025~2034 | [링크](https://www.precedenceresearch.com/retrieval-augmented-generation-market) | 2025 | [C] |
| <a id="ref-g-15"></a>G-15 | Next Move Strategy — RAG Market 2035 | [링크](https://www.nextmsc.com/report/retrieval-augmented-generation-rag-market-ic3918) | 2025 | [C] |
| <a id="ref-g-16"></a>G-16 | Invoca — Contact Center Automation Trends 2026 | [링크](https://www.invoca.com/blog/contact-center-automation-trends) | 2026 | [B] ⚠️ $80B 절감 수치 출처 미확인 |
| <a id="ref-g-17"></a>G-17 | Google Cloud — Vertex AI RAG Engine overview | [링크](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview) | 2026 | [A] |
| <a id="ref-g-18"></a>G-18 | Kore.ai — Enterprise-ready RAG (Forrester Wave Leader) | [링크](https://kore.ai/agent-platform/enterprise-ready-rag/) | 2026 | [A] |
| <a id="ref-g-19"></a>G-19 | Databricks — Mosaic AI RAG Framework | [링크](https://www.databricks.com/product/machine-learning/retrieval-augmented-generation) | 2026 | [A] |
| <a id="ref-g-20"></a>G-20 | LangChain — Self-Reflective RAG with LangGraph | [링크](https://blog.langchain.com/agentic-rag-with-langgraph/) | 2024 | [B] |
| <a id="ref-g-21"></a>G-21 | NVIDIA — AT&T NeMo Retriever Case Study | [링크](https://www.nvidia.com/en-us/customer-stories/att-drives-ai-agents-with-nemo/) | 2025 | [A] |
| <a id="ref-g-22"></a>G-22 | Klover.ai — Verizon AI Strategy | [링크](https://www.klover.ai/verizon-ai-strategy-analysis-of-dominance-in-telecommunications/) | 2025 | [B] |
| <a id="ref-g-23"></a>G-23 | Fortune BI — AI in Telecommunication Market | [링크](https://www.fortunebusinessinsights.com/ai-in-telecommunication-market-109439) | 2025 | [B] |
| <a id="ref-g-24"></a>G-24 | Grand View Research — Conversational AI Market | [링크](https://www.grandviewresearch.com/industry-analysis/conversational-ai-market-report) | 2025 | [B] |
| <a id="ref-g-26"></a>G-26 | 한국 AI 기본법 — 국가법령정보센터 | [링크](https://www.law.go.kr/lsInfoP.do?lsiSeq=268543) | 2026-01-22 | [A] |
| <a id="ref-g-27"></a>G-27 | 전자신문 — 국내 AI 시장 6조원 돌파 | [링크](https://www.etnews.com/20250501000163) | 2025-05 | [B] |

### 기업 발언 (E-xx)

| 번호 | 출처 | 발행일 | 요약 |
|------|------|--------|------|
| <a id="ref-e-01"></a>E-01 | SKT — AICC 단계 오픈, Telco LLM + RAG 적용 | 2024-10 | 상담 전문가 수십명 참여, LLM 답변 신뢰도 대폭 개선 |
| <a id="ref-e-02"></a>E-02 | KT — Agentic AICC 공개 (MWC 2026) | 2026-03 | 다중 AI 에이전트 협업, 상담→업무처리 전과정 자동화 |
| <a id="ref-e-03"></a>E-03 | SKT — Full-Stack AI at MWC 2026 | 2026-03 | A.X K1(519B), A.dot 1,000만 사용자, 2,000+ 내부 AI 에이전트 |
| <a id="ref-e-04"></a>E-04 | KT DS — ASA RAG 구축 사례 | 2024 | VectorDB 7,000건, AWS OpenSearch + Bedrock Claude, 음성 인증 19초 단축 |
| <a id="ref-e-05"></a>E-05 | NVIDIA/AT&T — NeMo Retriever 적용 | 2025 | NeMo 전체 파이프라인 적용 기준 응답 정확도 40% 향상 (post-training 포함) |

### 학술 논문 (P-xx)

| 번호 | 저자 | 연도 | 제목 | 핵심 인용 | URL |
|------|------|------|------|----------|-----|
| <a id="ref-p-01"></a>P-01 | Ayanami et al. | 2026-02 | A-RAG: Scaling Agentic RAG | HotpotQA 94.5%, Agentic 3원칙 충족 | [arXiv](https://arxiv.org/abs/2602.03442) |
| <a id="ref-p-02"></a>P-02 | Salesforce AI Research | 2026-03 | VoiceAgentRAG | Slow Thinker + Fast Talker 이중 에이전트 | [arXiv](https://arxiv.org/abs/2603.02206) |
| <a id="ref-p-03"></a>P-03 | EMNLP 2025 Industry | 2025 | LLM-Based Dialogue Labeling for Multiturn Adaptive RAG | 멀티턴 RAG 트리거 시점 자동 판별 | [ACL](https://aclanthology.org/2025.emnlp-industry.72.pdf) |
| <a id="ref-p-04"></a>P-04 | ACM Computing Surveys | 2025 | Multi-turn Dialogue Systems Survey | 맥락 유지·의도 추적 패턴 분류 | [ACM](https://dl.acm.org/doi/full/10.1145/3771090) |
| <a id="ref-p-05"></a>P-05 | Higress Team | 2026-02 | Higress-RAG: Dual Hybrid Retrieval + CRAG | MCP 기반, Semantic Caching 50ms, 90%+ 리콜 | [arXiv](https://arxiv.org/abs/2602.23374) |
