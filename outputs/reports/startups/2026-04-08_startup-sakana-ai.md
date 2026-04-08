---
company: Sakana AI
date: 2026-04-08
skill: startup-analyst
confidence: high
sources_count: 26
---

# Sakana AI 심층 분석

## 0. 한 줄 요약

> 자연 진화에서 영감을 받은 AI 모델 합성·자동 연구 기술로, 일본 최대 AI 유니콘($2.6B)으로 성장한 도쿄 기반 연구 기업.

## 1. 기업 개요

**기본 정보:**

| 항목 | 내용 | 출처 |
|------|------|------|
| 설립일 | 2023년 7월 | [[G-02]](#ref-g-02) |
| 소재지 | 일본, 도쿄 | [[E-03]](#ref-e-03) |
| 대표자 | David Ha (CEO) | [[E-03]](#ref-e-03) |
| 직원 수 | 138명 (2026-02) | [[G-06]](#ref-g-06) |
| 상태 | active | [[E-05]](#ref-e-05) |
| 웹사이트 | https://sakana.ai | |

**핵심 인력:**

| 이름 | 직함 | 주요 경력 | 출처 |
|------|------|----------|------|
| David Ha | CEO / 공동창업자 | 토론토대 학사, 도쿄대 PhD. Google Brain Japan 연구디렉터 → Stability AI Head of Research | [[G-01]](#ref-g-01), [[G-02]](#ref-g-02) |
| Llion Jones | CTO / 공동창업자 | U of Birmingham CS. YouTube → Google Research. **"Attention Is All You Need" (Transformer 논문) 공동 저자** | [[G-03]](#ref-g-03), [[G-04]](#ref-g-04) |
| Ren Ito | COO / 공동창업자 | 도쿄대 법학, NYU Law LLM, Stanford. 일본 외무성 → World Bank 11년 → Mercari 전무 (IPO 주도) → Stability AI COO | [[E-01]](#ref-e-01) |

**인력 동향:**

| 시점 | 인원 | 출처 |
|------|------|------|
| 2024년 | ~20명 | [[G-05]](#ref-g-05) |
| 2025-05 | ~28명 | [[G-06]](#ref-g-06) |
| 2026-02 | 138명 | [[G-06]](#ref-g-06) |

- 1년 간 약 5배 인원 증가. 급성장 단계.

## 2. 기술력 및 IP

### "Nature-Inspired AI" 철학

사명 Sakana(魚)는 물고기 떼의 집합 지능에서 착안. CEO David Ha: "모두가 세계 데이터를 모아 거대 모델을 만들고 엄청난 에너지를 소비한다. 개미부터 인간까지 종들이 협력해 문제를 해결하는 방식이 대안" [[E-02]](#ref-e-02). 핵심 테제: **진화(evolution)와 집합 지능을 AI 개발에 적용** — 거대 단일 모델이 아닌, 소규모 특화 모델들의 조합과 진화로 성능 달성.

### 핵심 기술 (5대 연구)

**1. Evolutionary Model Merging (진화적 모델 병합)**

진화 알고리즘으로 기존 오픈소스 모델을 자동 조합. 파라미터 공간(가중치 혼합) + 데이터 플로우 공간(레이어 순서 최적화) 두 차원에서 동시 탐색. 그래디언트 학습 없이 수백 세대 진화 후 최적 모델 발견 [[G-08]](#ref-g-08).

- EvoLLM-JP: 7B 파라미터로 기존 70B 모델 성능 초과 (일본어 수학)
- 논문: *Nature Machine Intelligence* Vol. 7 (2025-01-27 출판) [[G-09]](#ref-g-09)

**2. AI Scientist (자동 연구 시스템)**

토픽 → 아이디어 생성 → 문헌 검토 → 실험 코드 → 데이터 분석 → 논문 초안까지 전 연구 프로세스 자동화 [[G-10]](#ref-g-10).

- AI Scientist-v2: ICLR 2025 ICBINB 워크샵 블라인드 리뷰 통과 (평균 6.33/10) [[G-10]](#ref-g-10)
- 단, 워크샵 수락률 60–70% (메인 트랙 20–30% 대비 낮은 기준); 수락 시 사전 합의로 철회 [[G-11]](#ref-g-11) [추가확인 필요]
- AI Scientist 시스템 자체를 설명한 **인간 저자 논문**이 *Nature* 게재 (2026-03-26) [[G-12]](#ref-g-12)

**3. Transformer² (Self-Adaptive LLMs)**

2단계 적응: 태스크 분석 → Singular Value Decomposition (SVD)으로 가중치 분해 후 강화학습(RL)으로 태스크별 신호 강화/억제. GSM8K, 코딩, 추론에서 Low-Rank Adaptation (LoRA) 초과 성능. 크로스 모델 전이 가능 (Llama → Mistral 적용 시 성능 개선) [[G-13]](#ref-g-13).

**4. Darwin Gödel Machine (DGM)**

자기 코드를 수정하며 스스로 개선하는 에이전트. SWE-bench 20%→50%, Polyglot 14.2%→30.7% 성능 향상 자동 달성 [[G-14]](#ref-g-14).

**5. TinySwallow-1.5B**

Temporally Adaptive Interpolated Distillation (TAID) 기법으로 32B→1.5B 압축 일본어 Small Language Model (SLM). iPhone 14에서 실행 가능. ICLR 2025 Spotlight 논문 [[G-16]](#ref-g-16).

**IP 현황:**

| 구분 | 내용 | 출처 |
|------|------|------|
| 주요 학술 출판 | Nature (2026), Nature Machine Intelligence (2025), ICLR 2025 Spotlight | [[G-09]](#ref-g-09), [[G-12]](#ref-g-12), [[G-16]](#ref-g-16) |
| 특허 | 공개 정보 없음 | |
| 오픈소스 | EvoLLM-JP, EvoVLM-JP, TinySwallow 등 Hugging Face 공개 | [[G-08]](#ref-g-08) |

**기술 스택** (채용 공고 및 공개 정보 기반):

- Python, JAX, PyTorch, 진화 알고리즘 프레임워크, Hugging Face Transformers

## 3. 제품/서비스 및 비즈니스 모델

**주요 서비스:**

Sakana AI는 현재 **연구 중심 기업**으로, 일반 소비자 대상 상용 제품이나 공개 API는 없다.

| 제품 | 유형 | 특징 |
|------|------|------|
| TinySwallow-1.5B | 일본어 SLM (오픈소스) | 모바일 구동, ICLR 2025 Spotlight |
| EvoLLM-JP / EvoVLM-JP | 일본어 LLM/VLM (오픈소스) | 7B로 70B 성능, 진화적 합성 |
| AI Scientist v2 | 자동 연구 도구 | 논문 생성 자동화 |
| Darwin Gödel Machine | 자기 개선 에이전트 | 코딩 벤치마크 자기 수정 |

**수익 모델:**

1. **엔터프라이즈 B2B 파트너십**: 일본 대형 금융·산업 기업과 공동 모델 개발. MUFG와 3년+ 다년 파트너십 체결 (2025-05) — 문서 작성 자동화에서 시작, 엔터프라이즈 시스템 통합 확대 계획 [[E-06]](#ref-e-06)
2. **오픈소스 생태계**: 연구 성과 공개로 신뢰 구축 및 채용 효과
3. **방위·인텔리전스**: IQT 투자를 통한 미국 정보기관 연계 시장 진입 [[G-20]](#ref-g-20)

**성장 지표 (Traction):**

| 지표 | 수치 | 기간 | 출처 |
|------|------|------|------|
| 매출/GMV | 공개 정보 없음 | — | — |
| MAU | 공개 정보 없음 (B2B 모델) | — | — |
| 논문 피인용 | Transformer 원 논문 120K+, 자체 논문 Nature급 2편 | 2024–2026 | [[G-04]](#ref-g-04), [[G-09]](#ref-g-09) |

## 4. 투자 이력

| 라운드 | 금액 | 통화 | 리드 투자사 | 일자 | 출처 |
|--------|------|------|-----------|------|------|
| Seed | $30M | USD | Lux Capital | 2024-01-16 | [[E-03]](#ref-e-03) |
| Series A | ~$200M | USD | NEA, Khosla Ventures, Lux Capital | 2024-09-04 | [[E-04]](#ref-e-04) |
| Series B | $135M | USD | MUFG, Khosla, Factorial 등 | 2025-11-17 | [[E-05]](#ref-e-05) |

**누적 투자금:** ~$347M (¥520B, 공식 발표 기준) [[E-05]](#ref-e-05)

**Post-money 밸류에이션:** $2.635B (¥400B, Series B 기준) — 원문 확인 [[E-05]](#ref-e-05)

**주요 투자사:**

- **미국 VC**: Lux Capital, Khosla Ventures, NEA, 500 Global, NVIDIA
- **일본 전략 투자**: NTT Group, KDDI CVC, Sony Group, MUFG, SMBC, 미즈호, NEC, SBI, 후지쓰, 노무라, ANA, 도쿄 마린
- **특이 투자자**: In-Q-Tel (IQT) — 미국 정보기관 연계 VC (Series B 참여) [[E-05]](#ref-e-05)

## 5. 시장 및 경쟁 우위

**경쟁사 분석:**

| 기업 | 핵심 강점 | 핵심 약점 | 비고 |
|------|----------|----------|------|
| Mistral AI (프랑스) | 소규모 효율 모델, 오픈소스, 유럽 시장 | 스크래치 학습 중심; 진화 알고리즘 미사용 | 밸류에이션 ~$6B |
| Cohere (캐나다) | B2B API 제품화 완료 | 모델 합성 아닌 파인튜닝 접근 | 상용화 선행 |
| AI21 Labs (이스라엘) | Jamba MoE 아키텍처 혁신 | 진화적 방법 미사용 | 아키텍처 혁신 초점 |
| Preferred Networks (일본) | 일본 산업 로보틱스 AI | 학술 출판·글로벌 VC 접근 약함 | 일본 내 비교 대상 |

**차별화 포인트 (Moat):**

1. **Transformer 공동 발명자 (Llion Jones)**: AI 분야 최고 수준의 학술 신뢰도
2. **진화적 모델 합성**: GPU 대량 투자 없이도 고성능 모델 생산 — 컴퓨트 효율성에서 구조적 우위
3. **일본어·일본 문화 특화**: 주권 AI (Sovereign AI) 수요에 직접 대응
4. **자동 연구 (AI Scientist)**: R&D 자동화 선도 — Nature 게재로 학술적 검증
5. **IQT 투자**: 미국 방위·인텔리전스 시장 진입 경로 확보

## 6. 파트너십 및 최근 동향

**전략적 제휴 (최근 3년):**

| 파트너 | 관계 | 시점 | 출처 |
|--------|------|------|------|
| NTT Group | Seed 투자 + 연구 파트너 | 2024-01 | [[E-03]](#ref-e-03) |
| KDDI | Seed/Series A 투자, 통신 AI 공동 개발 | 2024 | [[E-03]](#ref-e-03), [[E-04]](#ref-e-04) |
| Sony Group | Seed 투자 | 2024-01 | [[E-03]](#ref-e-03) |
| NVIDIA | Series A 투자, TinySwallow 홍보 | 2024-09 | [[E-04]](#ref-e-04), [[G-16]](#ref-g-16) |
| MUFG | Series A/B 투자 + 3년+ 다년 엔터프라이즈 파트너십 | 2025-05 | [[E-06]](#ref-e-06) |
| In-Q-Tel (IQT) | Series B 투자 (미국 정보기관 연계) | 2025-11 | [[E-05]](#ref-e-05) |

**최근 1년 주요 이슈 (2025-04 ~ 2026-04):**

| 날짜 | 이벤트 | 출처 |
|------|--------|------|
| 2025-05 | MUFG 다년 파트너십 발표 | [[E-06]](#ref-e-06) |
| 2025-05 | Darwin Gödel Machine, Continuous Thought Machines 발표 | [[G-14]](#ref-g-14), [[G-15]](#ref-g-15) |
| 2025-09 | Japan Times 인터뷰 — Sovereign AI 전략 방향 공개 | [[E-02]](#ref-e-02) |
| 2025-11-17 | Series B $135M 발표, $2.635B 유니콘 달성 | [[E-05]](#ref-e-05) |
| 2026-03-26 | AI Scientist 논문 *Nature* 정식 게재 | [[G-12]](#ref-g-12) |

**글로벌 확장 계획:**

- 금융 → 제조·정부·방위·인텔리전스 섹터로 엔터프라이즈 확장 [[E-05]](#ref-e-05)
- 주권 AI 솔루션 수출 — 일본 모델을 타국 적용 가능성 탐색 [[G-22]](#ref-g-22)
- IQT 투자로 미국 방위·인텔리전스 시장 접근 경로 확보 [[G-20]](#ref-g-20)

## 7. 종합 평가

**5차원 스코어:**

| 차원 | 점수 (1-10) | 근거 |
|------|------------|------|
| 기술 경쟁력 (tech_strength) | 9 | Transformer 공동 발명자 보유, Nature/Nature MI 출판, 진화적 합성·AI Scientist·DGM 등 독보적 연구 포트폴리오 |
| 시장성 (market_potential) | 7 | 일본 주권 AI 수요 + 방위/인텔리전스 시장 진입. 단, 상용 제품 부재로 TAM 실현까지 시간 필요 |
| 팀 역량 (team_quality) | 9 | CEO(Google Brain/Stability AI), CTO(Transformer 공저자), COO(Mercari IPO/외교관) — 기술+사업+글로벌 역량 균형 |
| 사업 적합도 (business_fit) | 6 | 진화적 모델 합성·SLM 기술은 Model & Delta Foundry 영역과 직접 관련. 단, 일본 시장 중심이라 국내 적용에 로컬라이제이션 필요 |
| 견인력 (traction) | 5 | $347M 누적 투자, MUFG 파트너십 확보. 그러나 매출·고객 수 미공개, 상용 제품 부재 |
| **종합 (overall)** | **72** | |

**투자 매력도:**

- **강점**: 세계적 연구 역량 + 일본 대기업 전략 투자 네트워크 + 유니콘 밸류에이션. 진화적 모델 합성은 GPU 부족 환경에서 구조적 우위를 제공하며, AI Scientist는 R&D 생산성 혁신 잠재력 보유.
- **Exit 가능성**: 일본 대기업(NTT, KDDI, Sony)의 전략적 인수 또는 IPO 경로 모두 열려 있음. IQT 참여로 미국 방위 시장 진출 시 밸류에이션 상향 가능.

**리스크 요인:**

1. **상용화 지연**: 연구 성과는 탁월하나 매출을 만드는 제품이 아직 없음. 번레이트 대비 수익 모델 불명확
2. **경쟁 심화**: OpenAI, Anthropic, Google 등 빅테크가 모델 효율화(소형 모델, 합성 데이터)에 본격 진입
3. **일본 시장 한정**: 일본어 특화 전략이 강점이자 성장 천장. 글로벌 확장 실행력 미검증
4. **핵심 인력 의존**: CEO/CTO 2인에 대한 기술적 의존도가 높음
5. **밸류에이션 정당화**: $2.6B 밸류에이션 대비 매출 미공개 — 후속 라운드나 다운라운드 리스크

## 8. DB 등록용 정규화 데이터

> 아래 데이터는 사용자 승인 후 startup-db MCP 도구로 저장한다.

### upsert_company
```json
{
  "name": "Sakana AI",
  "slug": "sakana-ai",
  "description": "자연 진화에서 영감을 받은 AI 모델 합성·자동 연구 기술 개발. Transformer 공동 발명자 Llion Jones가 CTO로 참여. 진화적 모델 병합, AI Scientist, Transformer² 등 독보적 연구 포트폴리오 보유.",
  "website": "https://sakana.ai",
  "status": "active",
  "main_category": "Model / Engine",
  "sub_category": "LLM",
  "tags": ["llm", "evolutionary-ai", "model-merging", "slm", "japan", "sovereign-ai"],
  "country": "일본",
  "city": "도쿄",
  "technology": "Evolutionary Model Merging, AI Scientist, Transformer², TAID distillation, Darwin Gödel Machine",
  "main_product": "EvoLLM-JP (진화적 모델 합성 일본어 LLM), TinySwallow-1.5B (모바일 일본어 SLM), AI Scientist v2 (자동 연구 시스템)",
  "discovery_source": "Cbinsights AI Top 100",
  "employee_range": "101-200",
  "growth_stage": "growth",
  "total_raised": 347000000,
  "last_funding_date": "2025-11-17",
  "last_funding_type": "series_b",
  "one_liner": "자연 진화 기반 AI 모델 합성·자동 연구로 일본 최대 AI 유니콘 ($2.6B)",
  "metadata": {
    "tech_competitiveness": 5,
    "business_alignment": "유",
    "bigtech_collaboration": "NTT Group, KDDI CVC, Sony Group, NVIDIA, MUFG, In-Q-Tel (IQT)",
    "valuation_usd": 2635000000,
    "valuation_date": "2025-11-17"
  }
}
```

### add_funding_round (기존 데이터 업데이트 — Series A 금액 수정)
```json
[
  {
    "company_slug": "sakana-ai",
    "round_type": "seed",
    "raised_amount": 30000000,
    "currency": "USD",
    "announced_date": "2024-01-16",
    "metadata": {"lead_investor": "Lux Capital", "investors": "Khosla Ventures, NTT Group, KDDI CVC, Sony Group, 500 Global, Miyako Capital, Basis Set Ventures, JAFCO, July Fund, Geodesic Capital, Learn Capital"}
  },
  {
    "company_slug": "sakana-ai",
    "round_type": "series_a",
    "raised_amount": 200000000,
    "currency": "USD",
    "announced_date": "2024-09-04",
    "metadata": {"lead_investor": "NEA, Khosla Ventures, Lux Capital", "investors": "Translink Capital, 500 Global, NVIDIA, Global Brain, JAFCO, Miyako Capital, MUFG, SMBC, Mizuho, NEC, SBI, Dai-ichi Life, ITOCHU, KDDI, Fujitsu, Nomura, ANA, Tokio Marine", "valuation_note": "$1.5B post-money [추가확인 필요]"}
  },
  {
    "company_slug": "sakana-ai",
    "round_type": "series_b",
    "raised_amount": 135000000,
    "currency": "USD",
    "announced_date": "2025-11-17",
    "metadata": {"lead_investor": "multiple (MUFG, Khosla, Factorial)", "investors": "Macquarie Capital, Fundomo, Mouro Capital, NEA, Geodesic Capital, Lux Capital, Ora Global, MPower Partners, Shikoku Electric Power, In-Q-Tel (IQT)", "post_money_valuation": "$2.635B"}
  }
]
```

### upsert_person (인물별)
```json
[
  {"name": "David Ha", "title": "CEO / Co-founder", "role": "ceo", "metadata": {"education": "U of Toronto BSc, U of Tokyo PhD", "prior": "Goldman Sachs Japan → Google Brain Japan → Stability AI Head of Research"}},
  {"name": "Llion Jones", "title": "CTO / Co-founder", "role": "cto", "metadata": {"education": "U of Birmingham CS BSc/MSc", "prior": "YouTube → Google Research. Transformer ('Attention Is All You Need') 공동 저자"}},
  {"name": "Ren Ito", "title": "COO / Co-founder", "role": "coo", "metadata": {"education": "U of Tokyo Law, NYU Law LLM, Stanford", "prior": "일본 외무성 → World Bank 11년 → Mercari 전무 (IPO) → Stability AI COO"}}
]
```

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-e-01"></a>E-01 | NYU School of Law — Ren Ito LLM '04 profile | [링크](https://www.law.nyu.edu/news/ren-ito-tech-sakana-ai) | profile | 2024 | [A] |
| <a id="ref-e-02"></a>E-02 | TechXplore — Sakana AI nature-inspired tech 인터뷰 (David Ha 발언) | [링크](https://techxplore.com/news/2025-09-japan-sakana-ai-touts-nature.html) | news | 2025-09-10 | [B] |
| <a id="ref-e-03"></a>E-03 | Sakana AI — Seed round 공식 발표 | [링크](https://sakana.ai/seed-round/) | IR | 2024-01-16 | [A] |
| <a id="ref-e-04"></a>E-04 | Sakana AI — Series A 공식 발표 | [링크](https://sakana.ai/series-a/) | IR | 2024-09-04 | [A] |
| <a id="ref-e-05"></a>E-05 | Sakana AI — Series B 공식 발표 | [링크](https://sakana.ai/series-b/) | IR | 2025-11-17 | [A] |
| <a id="ref-e-06"></a>E-06 | Yahoo Finance / MUFG — 다년 AI 파트너십 발표 | [링크](https://finance.yahoo.com/news/mufg-enters-multiyear-ai-partnership-115633622.html) | IR | 2025-05-20 | [A] |
| <a id="ref-g-01"></a>G-01 | Google Scholar — David Ha 프로필 | [링크](https://scholar.google.com/citations?user=N7X-kbUAAAAJ&hl=en) | profile | 2024 | [B] |
| <a id="ref-g-02"></a>G-02 | Silicon.co.uk — Google Researcher Leaves To Co-Found Sakana AI | [링크](https://www.silicon.co.uk/e-innovation/artificial-intelligence/google-ai-sakana-525959) | news | 2023 | [B] |
| <a id="ref-g-03"></a>G-03 | FourWeekMBA — Llion Jones background & career | [링크](https://fourweekmba.com/llion-jones/) | blog | 2024 | [C] |
| <a id="ref-g-04"></a>G-04 | arXiv — "Attention Is All You Need" (Vaswani et al., 2017) | [링크](https://arxiv.org/abs/1706.03762) | paper | 2017-06-12 | [A] |
| <a id="ref-g-05"></a>G-05 | Wikipedia — Sakana AI | [링크](https://en.wikipedia.org/wiki/Sakana_AI) | reference | 2026-04 | [B] |
| <a id="ref-g-06"></a>G-06 | Tracxn — Sakana AI Company Profile | [링크](https://tracxn.com/d/companies/sakana/__Rxr2r3OKVsnvG1iZDZfSuo_0DuLgIoPwG_c5RX-eMWw) | database | 2026-02-28 | [B] |
| <a id="ref-g-07"></a>G-07 | PitchBook — Sakana AI Profile | [링크](https://pitchbook.com/profiles/company/537652-45) | database | 2026 | [B] |
| <a id="ref-g-08"></a>G-08 | Sakana AI Blog — Evolutionary Model Merge | [링크](https://sakana.ai/evolutionary-model-merge/) | official | 2024-03-21 | [A] |
| <a id="ref-g-09"></a>G-09 | Nature Machine Intelligence — Evolutionary optimization of model merging recipes | [링크](https://www.nature.com/articles/s42256-024-00975-8) | paper | 2025-01-27 | [A] |
| <a id="ref-g-10"></a>G-10 | Sakana AI — AI Scientist First Peer-Reviewed Publication | [링크](https://sakana.ai/ai-scientist-first-publication/) | official | 2025-03-12 | [A] |
| <a id="ref-g-11"></a>G-11 | TechCrunch — AI-generated paper peer review nuance | [링크](https://techcrunch.com/2025/03/12/sakana-claims-its-ai-paper-passed-peer-review-but-its-a-bit-more-nuanced-than-that/) | news | 2025-03-12 | [B] |
| <a id="ref-g-12"></a>G-12 | Sakana AI — AI Scientist Published in Nature | [링크](https://sakana.ai/ai-scientist-nature/) | official | 2026-03-26 | [A] |
| <a id="ref-g-13"></a>G-13 | Sakana AI — Transformer² Self-Adaptive LLMs | [링크](https://sakana.ai/transformer-squared/) | official | 2025-01 | [A] |
| <a id="ref-g-14"></a>G-14 | Sakana AI — Darwin Gödel Machine | [링크](https://sakana.ai/dgm/) | official | 2025-05 | [A] |
| <a id="ref-g-15"></a>G-15 | Sakana AI — Continuous Thought Machines | [링크](https://pub.sakana.ai/ctm/) | official | 2025-05 | [A] |
| <a id="ref-g-16"></a>G-16 | Sakana AI — TAID TinySwallow-1.5B | [링크](https://sakana.ai/taid/) | official | 2025-01-30 | [A] |
| <a id="ref-g-17"></a>G-17 | Sakana AI — Automating the Search for Artificial Life | [링크](https://sakana.ai/asal/) | official | 2024 | [A] |
| <a id="ref-g-18"></a>G-18 | TechCrunch — Sakana AI Series B $135M | [링크](https://techcrunch.com/2025/11/17/sakana-ai-raises-135m-series-b-at-a-2-65b-valuation-to-continue-building-ai-models-for-japan/) | news | 2025-11-17 | [B] |
| <a id="ref-g-19"></a>G-19 | SiliconANGLE — Sakana AI $135M on $2.635B valuation | [링크](https://siliconangle.com/2025/11/17/sakana-ai-lands-135m-2-635b-valuation-accelerate-frontier-research-applied-ai-japan/) | news | 2025-11-17 | [B] |
| <a id="ref-g-20"></a>G-20 | WebProNews — Japan's Bid for Sovereign AI (IQT 분석) | [링크](https://www.webpronews.com/sakana-ais-135m-haul-japans-bid-for-sovereign-ai-dominance-in-finance-and-defense/) | news | 2025-11 | [C] |
| <a id="ref-g-22"></a>G-22 | Axis Intelligence — Sakana AI Japan Unicorn Story | [링크](https://axis-intelligence.com/sakana-ai-japan-unicorn-story-valuation/) | news | 2025-11 | [C] |
