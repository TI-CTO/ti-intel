---
topic: OCR-free 문서 AI 및 통신사 B2B 플랫폼
date: 2026-03-12
agent: research-deep
confidence: medium
status: completed
sources_used: [websearch]
---

# Research Report: OCR-free 문서 AI 및 통신사 B2B 플랫폼

## Executive Summary

> OCR-free VLM 기반 문서 AI 시장은 2025~2026년 급격히 성숙하여, PaddleOCR-VL(OmniDocBench 94.5%), Mistral OCR 3($2/1,000페이지), Qwen2.5-VL 등이 전통 파이프라인을 빠르게 대체하고 있다. 글로벌 IDP 시장은 2025년 약 $3.2B에서 2034년 $43.9B(CAGR 33.7%)로 성장 전망이며, ABBYY·UiPath·Kofax가 엔터프라이즈 시장을 장악하고 있으나 한국어·한글 특화 틈새는 상대적으로 취약하다. 국내에서는 업스테이지(Document Parse, 한국어 특화, $45M 투자 유치)가 유력 대안이며, KT 에이전틱 패브릭과 SKT 에이닷 비즈가 각각 B2B AI 플랫폼 전략을 가속화하고 있어 통신사의 문서 AI 수직화 기회가 존재한다. 단, 한국어 VLM 벤치마크 데이터와 통신사 문서 AI 구체 수치가 공개 정보로 부족해 신뢰도는 Medium으로 평가한다.

## 연구 질문

- OCR-free VLM 모델들의 정확도·속도·한국어 지원 현황은 어떠한가?
- 글로벌 IDP 시장 규모와 주요 플레이어의 포지셔닝은?
- 금융·보험·의료 분야에서의 문서 AI 도입 ROI 실증 수치는?
- 한국어 특화 문서 AI 국내 플레이어 현황은?
- 통신사(SKT/KT)가 문서 AI를 B2B SaaS로 연계할 수 있는 기회 구조는?

---

## 1. 기술 현황

### 1-1. OCR-free VLM 패러다임 전환

전통 OCR 파이프라인(검출 → 인식 → 구조화)은 2024~2025년을 기점으로 **End-to-End VLM(Vision-Language Model)** 방식으로 급속히 대체되고 있다. VLM 방식은 이미지를 직접 입력받아 텍스트·레이아웃·표·수식을 동시에 이해하고 Markdown/JSON/HTML 등 구조화 포맷으로 출력한다.

**기술 성숙도 (TRL):** TRL 7~8 (파일럿·상용화 단계). Mistral OCR, Upstage Document Parse는 이미 프로덕션 API로 제공 중이다.

**주요 기술 요소:**
- 동적 해상도 인코딩 (NaViT-style): 고해상도 문서 처리 효율화
- 언어 모델 통합: 레이아웃 이해 + 텍스트 생성 동시 처리
- 멀티페이지 처리: 최대 1,000페이지/요청(Mistral OCR 기준)
- 구조화 출력: Markdown, LaTeX, HTML 표 재구성

### 1-2. OCR-free VLM 주요 모델 현황

**모델별 특성 요약:**

| 모델 | 개발사 | 파라미터 | 벤치마크 점수 | 한국어 지원 | 라이선스 |
|------|--------|---------|-------------|-----------|---------|
| PaddleOCR-VL 1.5 | Baidu | 0.9B | OmniDocBench 94.5 (SOTA) | 지원 (109개 언어) | 오픈소스 |
| Mistral OCR 3 | Mistral AI | 비공개 | JSON 추출 72.2% | 제한적 | 상용 API |
| Qwen2.5-VL 72B | Alibaba | 72B | JSON 추출 최상위 | 중국어 중심, 다국어 | 오픈소스 |
| GOT-OCR 2.0 | UCAS | 580M | OmniDocBench 상위권 | 영어·중국어 중심 | 오픈소스 |
| DocOwl 2 (mPLUG) | Alibaba | 비공개 | 멀티페이지 특화 | 영어·중국어 | 오픈소스 |
| Florence-2 | Microsoft | 0.2B~0.8B | CC-OCR 49.70 (특화모델) | 다국어 (한국어 약함) | 오픈소스 |
| Nougat | Meta | 250M | 학술 PDF 특화 | 영어 중심 | 오픈소스 |

**한국어 지원 평가:**

CC-OCR 벤치마크에 따르면, 아시아 언어(한국어·일본어·베트남어·아랍어) 정확도는 라틴계 언어 대비 전반적으로 낮다. 범용 모델 중 Gemini 1.5 Pro가 다국어 트랙 1위(78.97점)이며, 오픈소스 특화 모델(Florence 등)은 한국어 성능이 상대적으로 취약하다 [[G-01]](#ref-g-01). PaddleOCR-VL은 109개 언어를 지원하며 한국어 포함을 명시하고 있으나, 한국어 전용 정확도 수치는 공개 정보 없음 [[G-09]](#ref-g-09).

---

## 2. 시장 동향

### 2-1. 글로벌 IDP 시장 규모

시장조사 기관별 추정치에 편차가 있으나, 고성장 트렌드는 일치한다.

**시장 규모 추정 (복수 출처 교차 검증):**

| 기관 | 2025년 시장규모 | 2030~2034년 전망 | CAGR |
|------|---------------|----------------|------|
| Precedence Research | $3.22B | $43.92B (2034) | 33.7% |
| Grand View Research | $2.30B (2024) | $12.35B (2030) | 33.1% |
| Fortune Business Insights | $10.57B (2025) | $91.02B (2034) | 26.2% |
| Mordor Intelligence | $3.17B (2026) | $7.18B (2031) | 17.8% |

> **주의**: 기관별 시장 정의 범위 차이로 추정치가 큰 편차를 보임. 보수적으로는 $3B 규모, 향후 10년 내 $40B+ 잠재 시장으로 이해하는 것이 적절하다 [C].

**주요 성장 드라이버:**
- 비정형 데이터(전체 기업 데이터의 90%+)의 AI 처리 수요 급증
- Cloud SaaS 전환 가속 (온프레미스 → 구독 모델)
- 보험·금융권 규제 강화로 인한 자동화 필수화
- LLM 연계 RAG 파이프라인 구축 수요

**지역 분포:** 북미 47.6% 점유 (2025), 아시아 시장 급성장 중 [[G-03]](#ref-g-03).

---

## 3. 경쟁사 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| ABBYY (Vantage) | 35년 OCR 경험 기반, 150+ 사전학습 스킬 마켓플레이스, 200개 언어 지원, 90%+ Day-1 정확도 주장. 페이지 수 기반 구독 라이선스 | [[G-11]](#ref-g-11) |
| UiPath (Document Understanding) | RPA 생태계 통합 강점. 소비 모델(consumption model) 가격 구조로 변동 비용 복잡. IDP 독립 제품보다 RPA 연계 번들로 주로 판매 | [[G-11]](#ref-g-11) |
| Kofax (Tungsten Automation) | 2024년 1월 사명 변경. 40년 이력·25,000+ 고객. TotalAgility 8.1: 문서 지능 + 프로세스 오케스트레이션 + 로우코드 통합. 영구 라이선스 모델 유지 | [[G-11]](#ref-g-11) |
| Mistral AI (OCR 3) | 2025년 12월 출시. $2/1,000페이지 (배치: $1). 50MB/1,000페이지 지원. HTML 표 재구성 추가. 스타트업 중 가장 공격적인 가격 전략 | [[G-07]](#ref-g-07) |
| Upstage (Document Parse) | 한국 스타트업. 한글·한자·저품질 스캔 지원. 삼성·국내 보험사 납품. 95%+ 정확도 주장. $45M Series B Bridge (KDB·Amazon·AMD 참여, 2025년 8월) | [[G-12]](#ref-g-12) |
| Baidu (PaddleOCR-VL) | 0.9B 초경량 오픈소스. OmniDocBench 94.5 SOTA. 109개 언어 지원. 엣지·온프레미스 배포 가능 | [[G-09]](#ref-g-09) |

---

## 4. 제품/서비스 스펙 비교

**OCR-free 문서 AI 주요 솔루션 스펙**

| 기업/모델 | 정확도(벤치마크) | 한국어 지원 | 가격(정책) | 출처 |
|---------|--------------|-----------|----------|------|
| PaddleOCR-VL 1.5 (Baidu) | OmniDocBench 94.5 (SOTA) | 지원 (109개 언어) | 무료 (오픈소스) | [[G-09]](#ref-g-09) |
| Mistral OCR 3 | JSON 추출 72.2%, 형식 문서 74% 개선 | 제한적 (라틴 중심) | $2/1,000 페이지 (배치 $1) | [[G-07]](#ref-g-07) |
| Qwen2.5-VL 72B (Alibaba) | JSON 추출 최상위권 | 중국어·다국어 | 무료 (오픈소스) / 클라우드 별도 | [[G-01]](#ref-g-01) |
| GOT-OCR 2.0 (UCAS) | 580M 파라미터 SOTA 수준 | 영어·중국어 | 무료 (오픈소스) | [[G-02]](#ref-g-02) |
| Upstage Document Parse | 95%+ (자사 주장) | 한글·한자 특화 | 공개 정보 없음 (API 사용량 기반 추정) | [[G-12]](#ref-g-12) |
| ABBYY Vantage | 90%+ Day-1 (표준 문서) | 200개 언어 | 페이지 수 기반 구독 (세부 공개 없음) | [[G-11]](#ref-g-11) |
| NAVER CLOVA OCR | 공개 벤치마크 없음 | 한국어·일본어 특화 | API 종량제 (네이버 클라우드) | [[G-04]](#ref-g-04) |

---

## 5. 학술 동향

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| "General OCR Theory: Towards OCR-2.0 via a Unified End-to-end Model" (Wei et al., 2024) | 580M 파라미터 단일 모델로 텍스트·표·수식·악보·분자식 통합 처리. OCR 2.0 패러다임 제시 | [[P-01]](#ref-p-01) |
| "mPLUG-DocOwl2: High-resolution Compressing for OCR-free Multi-page Document Understanding" (Alibaba, 2024) | 멀티페이지 고해상도 문서 압축 처리 기법. 효율적 토큰 압축으로 긴 문서 이해 가능 | [[P-02]](#ref-p-02) |
| "CC-OCR: A Comprehensive and Challenging OCR Benchmark for Evaluating Large Multimodal Models in Literacy" (2024) | 다국어 포함 종합 OCR 벤치마크. 아시아 언어에서 기존 모델 성능 한계 실증 | [[P-03]](#ref-p-03) |
| "PaddleOCR-VL-1.5: Towards a Multi-Task 0.9B VLM for Robust In-the-Wild Document Parsing" (Baidu, 2026) | 0.9B 초경량 VLM으로 OmniDocBench v1.5 94.5 달성. 실세계 다양한 문서 환경 강건성 | [[P-04]](#ref-p-04) |
| "OmniDocBench" (opendatalab, CVPR 2025) | 1,355 PDF 페이지, 9종 문서·4종 레이아웃·3종 언어 포함 종합 파싱 벤치마크. 사실상 표준 평가 기준 | [[P-05]](#ref-p-05) |

**연구 방향 요약:**
- 경량화(0.9B 수준)로 엣지 배포 가능한 VLM 개발 가속화
- 멀티페이지·멀티모달(표+수식+이미지 혼재) 문서 처리
- 아시아 언어 특화 벤치마크 및 모델 개선 연구 부족 — 기회 영역

---

## 6. 특허 동향

특허 전용 수집 도구(intel-store) 미활용으로 상세 특허 분석은 제한적이다. WebSearch 기반 정황 정보:

- ABBYY, Kofax(Tungsten)는 문서 인식·워크플로우 자동화 관련 다수 특허 보유
- 네이버·카카오는 한국어 문서 인식 관련 국내 특허 출원 중 (세부 수치 공개 정보 없음)
- Baidu PaddleOCR 관련 특허는 중국 CNIPA에 집중
- **데이터 공백**: 한국어 특화 문서 VLM 관련 USPTO/KIPRIS 특허 출원 현황 추가 조사 필요

---

## 7. 기업 발언 & 보도자료

**주요 기업 공식 발언 및 발표 요약**

**KT — 에이전틱 패브릭 (MWC 2026, 2026-03-02)**

KT는 MWC 2026에서 기업용 AI 운영체제 "에이전틱 패브릭(Agentic Fabric)"을 공개했다. 5개 레이어(Experience / Intelligence / Context / Execution / Governance)로 구성된 아키텍처로, 통신·재무·자산·HR 등 내부 핵심 업무에 실제 적용하며 성능을 검증했다고 발표했다. 믿:음 K 2.0(11.5B) 및 Mini(2.3B) 모델은 AICC, 상품 검색 챗봇, **문서 인식**, 법률·금융 특화 서비스에 적용 중이다 [[E-01]](#ref-e-01).

**SKT — 에이닷 비즈 & 소버린 AI**

SKT는 2025년 2월 기업용 AI 에이전트 "에이닷 비즈" CBT를 시작했으며, 9월 SK그룹 25개사로 확대했다. 에이닷 비즈는 정보 검색·일정 관리·**회의록 작성** 등 업무 효율화 기능 제공. 에이닷엑스(A.X) 3.1(34B/7B)을 허깅페이스에 오픈소스 공개하여 소버린 AI 생태계 조성 중이다. 유영상 CEO: "AI 데이터센터 토털 솔루션 시장 공략 등 AI B2B·B2C 사업 고도화해 수익 낼 것" [[E-02]](#ref-e-02).

**Upstage — $45M 투자 유치 (2025-08-20)**

"우리는 Fortune 500 기업 및 삼성을 포함한 고객사에 문서 인텔리전스 솔루션을 공급하고 있으며, 국내 보험사에 광범위하게 도입되었다. 이번 투자를 통해 미국·일본 시장 확장을 가속화한다." — Upstage 보도자료(PR Newswire, 2025-08) [[E-03]](#ref-e-03).

**MWC 2026 통신 3사 공통 메시지**

SKT·KT·LGU+는 MWC 2026에서 AI 데이터센터, AI 모델, **산업용 AI 서비스**를 핵심 키워드로 제시. SKT·KT는 B2B, LGU+는 B2C에 집중하는 3색 전략이 명확히 분화됐다 [[E-04]](#ref-e-04).

---

## 8. 구축 사례 및 ROI

### 8-1. 금융 서비스

- AI 기반 대출 처리: **정확도 90% 향상**, 처리 시간 70% 단축. 대출 승인 시간 80% 감소(30~60초 vs 기존 며칠) [[G-05]](#ref-g-05)
- 금융 AI 도입 기업 중 57%가 ROI 기대 초과 달성 [[G-05]](#ref-g-05)

### 8-2. 의료·헬스케어

- 병원 RCM(Revenue Cycle Management): 46% 병원이 AI 도입 완료
- Cleveland Clinic: 100+ 문서를 1.5분 처리, 임상 문서 독해 2초 이내 [[G-05]](#ref-g-05)
- Iodine AwarePre-Bill: **청구 검토 시간 63% 단축**, 2024년 1,000개+ 의료 시스템에서 $23.94억 총 환급 달성 [[G-05]](#ref-g-05)

### 8-3. 보험

- Allstate: AI 기반 고객 클레임 처리 시스템 도입, 하루 **5만 건** 메시지 처리 [[G-05]](#ref-g-05)
- Thoughtful AI(보험 청구): 거절율 **75% 감소**, 처리 정확도 95%+ [[G-05]](#ref-g-05)
- 전체 보험사의 54%가 이미 가격 산정에 AI 활용 [[G-05]](#ref-g-05)

### 8-4. 전반적 ROI

- 엔터프라이즈 AI 투자 $1당 평균 $3.70 ROI 달성 (2025 기준)
- 생산성 향상: 26~55% 범위 [[G-05]](#ref-g-05)

---

## 9. 전략적 시사점 (통신사 B2B 관점)

**기술 트렌드**
- OCR-free VLM은 이제 실용화 단계. PaddleOCR-VL(오픈소스, 0.9B)과 Mistral OCR($2/1K 페이지)의 등장으로 **구축 비용 장벽이 크게 낮아졌다**.
- 한국어 VLM 정확도는 아직 라틴 언어 대비 열위. 한국어 특화 파인튜닝이 곧 차별화 요소다.

**기회**
- KT 믿:음 K 모델이 이미 "문서 인식" 적용 사례를 보유 중. 이를 **독립 B2B SaaS 상품**으로 패키징하는 것이 가장 빠른 GTM 경로다.
- 통신사는 기업 고객(SME~대기업) 네트워크와 클라우드 인프라를 보유. IDP 솔루션을 **AI DC 번들**로 제공하면 진입 장벽 우회 가능.
- 보험·금융·공공기관의 한국어 문서 처리 수요는 국내 플레이어(업스테이지, CLOVA)가 집중하는 시장 — 통신사가 **데이터 주권(온프레미스·프라이빗 클라우드)** 옵션으로 차별화 가능.
- SKT 에이닷 비즈의 회의록 작성 기능을 **계약서·청구서·민원서류 이해** 기능으로 확장하면 문서 AI B2B 라인업 완성 가능.

**위협**
- 업스테이지가 삼성·보험사 채널을 이미 확보하고 $45M으로 미국·일본 확장 중 — 국내 중소 금융권 락인이 빠르게 진행 중.
- ABBYY·UiPath는 글로벌 SI 파트너망을 통해 대기업 ERP 연계 거래를 독점. 통신사가 진입하기 어려운 세그먼트.
- 오픈소스 모델(PaddleOCR-VL, GOT-OCR) 급성장으로 기술 자체의 차별화가 어려워지는 상품화(commoditization) 압력.

**권고사항**
- **단기 (6개월)**: KT 믿:음 K 문서 인식 기능을 B2B API로 외부 개방. 파일럿 고객 3~5개 확보(보험 또는 공공 기관 우선).
- **중기 (12~18개월)**: 한국어 문서 파인튜닝 데이터셋 구축 + 업스테이지 또는 국내 스타트업과 파트너십/인수 검토. AI DC 번들(스토리지+문서 AI API) 상품 설계.
- **장기 (24개월+)**: 통신사 특화 수직(B2B 계약서, 주파수 허가, 고객 청구서 자동화) 파인튜닝 모델로 포트폴리오 구축.

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- IDP 시장 고성장 트렌드 (복수 시장조사 기관 일치)
- PaddleOCR-VL OmniDocBench SOTA 수치 (공식 논문 및 Hugging Face 검증)
- Upstage $45M 투자 및 삼성·보험사 납품 (공식 보도자료)
- KT 에이전틱 패브릭 5레이어 아키텍처 (MWC 2026 공식 발표)
- 금융·의료 ROI 수치 (Cleveland Clinic, Iodine AwarePre-Bill 개별 사례)

**추가 검증 필요 [C/D]:**
- IDP 시장 규모 절대값 ($3.2B vs $10.6B 기관별 편차 큼) [C]
- Fortune Business Insights의 $10.57B 추정치는 타 기관 대비 과대 추정 가능성 [D]
- Mistral OCR 3 "74% 개선" 주장 — 독립 검증 벤치마크 없음 [C]

**데이터 공백:**
- 한국어 전용 VLM 정확도 공개 벤치마크 부재
- NAVER CLOVA OCR 2025년 정확도·시장 점유율 수치
- KT/SKT 문서 AI 관련 실제 매출 또는 고객 수 공개 정보 없음
- 국내 IDP 시장 규모 (한국 단독) 추정치 부재

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | CodeSOTA — Best OCR Models 2026: Benchmarks & Comparison | [링크](https://www.codesota.com/ocr) | benchmark | 2026 | [B] |
| <a id="ref-g-02"></a>G-02 | MarkTechPost — GOT General OCR Theory Unveiled | [링크](https://www.marktechpost.com/2024/09/16/got-general-ocr-theory-unveiled-a-revolutionary-ocr-2-0-model-that-streamlines-text-recognition-across-multiple-formats-with-unmatched-efficiency-and-precision/) | news | 2024-09-16 | [B] |
| <a id="ref-g-03"></a>G-03 | Research Nester — Intelligent Document Processing Market Revenue to exceed $122B by 2035 | [링크](https://finance.yahoo.com/news/intelligent-document-processing-market-revenue-093000688.html) | market-report | 2025 | [C] |
| <a id="ref-g-04"></a>G-04 | NAVER Cloud Platform — CLOVA OCR 공식 페이지 | [링크](https://www.ncloud.com/v2/product/aiService/ocr) | official | 2025 | [A] |
| <a id="ref-g-05"></a>G-05 | Strativera — AI Healthcare Business Transformation 2025: 3.2X ROI and 30% Efficiency Gains | [링크](https://strativera.com/ai-healthcare-business-transformation-frameworks-2025/) | report | 2025 | [C] |
| <a id="ref-g-06"></a>G-06 | Precedence Research — IDP Market Size to Hit USD 43.92B by 2034 | [링크](https://www.precedenceresearch.com/intelligent-document-processing-market) | market-report | 2025 | [C] |
| <a id="ref-g-07"></a>G-07 | Mistral AI — Mistral OCR 공식 뉴스 | [링크](https://mistral.ai/news/mistral-ocr) | official | 2025-03 | [A] |
| <a id="ref-g-08"></a>G-08 | byteiota — Mistral OCR 3: $2/1000 Pages Cuts Document AI Costs 97% | [링크](https://byteiota.com/mistral-ocr-3-2-1000-pages-cuts-document-ai-costs-97/) | news | 2025-12 | [B] |
| <a id="ref-g-09"></a>G-09 | PaddleOCR Documentation — PaddleOCR-VL Introduction | [링크](https://www.paddleocr.ai/latest/en/version3.x/algorithm/PaddleOCR-VL/PaddleOCR-VL.html) | official | 2025-10 | [A] |
| <a id="ref-g-10"></a>G-10 | Docsumo — 50 Key Statistics and Trends in IDP for 2025 | [링크](https://www.docsumo.com/blogs/intelligent-document-processing/intelligent-document-processing-market-report-2025) | report | 2025 | [B] |
| <a id="ref-g-11"></a>G-11 | NILG.AI — Top 8 Intelligent Document Processing Solutions for 2025 | [링크](https://nilg.ai/202505/intelligent-document-processing-solutions/) | review | 2025-05 | [B] |
| <a id="ref-g-12"></a>G-12 | SiliconANGLE — Upstage bags $45M to expand AI-native document intelligence suite to the US | [링크](https://siliconangle.com/2025/08/20/upstage-bags-45m-expand-ai-native-document-intelligence-suite-us/) | news | 2025-08-20 | [B] |
| <a id="ref-g-13"></a>G-13 | Grand View Research — IDP Market Report 2030 | [링크](https://www.grandviewresearch.com/industry-analysis/intelligent-document-processing-market-report) | market-report | 2025 | [B] |
| <a id="ref-g-14"></a>G-14 | 아주경제 — AI 회사로 변신, 통신 3사 3色 전략 | [링크](https://www.ajunews.com/view/20260309151001903) | news | 2026-03-09 | [B] |
| <a id="ref-g-15"></a>G-15 | SKT 뉴스룸 — SKT B2B 생성형 AI 플랫폼 엔터프라이즈 AI 마켓 | [링크](https://news.sktelecom.com/202034) | official | 2025 | [A] |
| <a id="ref-g-16"></a>G-16 | devocean.sk.com — 2023년 최신판 OCR 8가지 API 비교평가 | [링크](https://devocean.sk.com/blog/techBoardDetail.do?ID=165524&boardType=techBlog) | blog | 2023 | [C] |
| <a id="ref-p-01"></a>P-01 | Wei et al. — General OCR Theory: Towards OCR-2.0 via a Unified End-to-end Model | [링크](https://arxiv.org/html/2409.01704v1) | paper | 2024-09 | [A] |
| <a id="ref-p-02"></a>P-02 | Alibaba — mPLUG-DocOwl2: High-resolution Compressing for OCR-free Multi-page Document Understanding | [링크](https://arxiv.org/html/2409.03420v1) | paper | 2024-09 | [A] |
| <a id="ref-p-03"></a>P-03 | CC-OCR: A Comprehensive and Challenging OCR Benchmark for Evaluating Large Multimodal Models in Literacy | [링크](https://arxiv.org/html/2412.02210v2) | paper | 2024-12 | [A] |
| <a id="ref-p-04"></a>P-04 | Baidu — PaddleOCR-VL-1.5: Towards a Multi-Task 0.9B VLM for Robust In-the-Wild Document Parsing | [링크](https://arxiv.org/html/2601.21957v1) | paper | 2026-01 | [A] |
| <a id="ref-p-05"></a>P-05 | opendatalab — OmniDocBench (CVPR 2025) | [링크](https://github.com/opendatalab/OmniDocBench) | paper | 2025 | [A] |
| <a id="ref-e-01"></a>E-01 | KT — MWC 2026 에이전틱 패브릭 공개, 믿:음 K 2.0 문서 인식 적용 | [링크](https://www.youthdaily.co.kr/news/article.html?no=214413) | IR/발표 | 2026-03-02 | [A] |
| <a id="ref-e-02"></a>E-02 | SKT 뉴스룸 — 유영상 CEO AI B2B·B2C 사업 고도화 발언 | [링크](https://news.sktelecom.com/210184) | IR/발표 | 2025 | [A] |
| <a id="ref-e-03"></a>E-03 | Upstage PR Newswire — $45M Series B Bridge 완료 발표 | [링크](https://www.prnewswire.com/news-releases/upstage-completes-45m-series-b-bridge-to-accelerate-enterprise-grade-genai-and-global-expansion-302534044.html) | IR/발표 | 2025-08-20 | [A] |
| <a id="ref-e-04"></a>E-04 | EBN뉴스 — MWC 2026 이통3사 AI 인프라社 변신 전략 | [링크](https://www.ebn.co.kr/news/articleView.html?idxno=1701757) | news | 2026-03 | [B] |
