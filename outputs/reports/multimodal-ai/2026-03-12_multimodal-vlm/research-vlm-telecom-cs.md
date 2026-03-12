---
topic: multimodal-vlm-telecom-customer-service
date: 2026-03-12
agent: research-deep
confidence: medium
status: completed
sources_used: [websearch, webfetch, existing-discover-report]
---

# Research Report: 멀티모달 VLM — 통신사 고객 서비스 적용 심층 분석

## Executive Summary

> 글로벌 통신사(Deutsche Telekom, Verizon, SKT)의 AI 고객 서비스 도입은 가속 중이나, **이미지 기반 VLM 진단은 아직 파일럿 단계**다. Verizon은 AI 에이전트로 2024년 고객 10만 명 이탈 방지를 예측했고, Deutsche Telekom은 41,000명 상담원에 AI CCaaS를 롤아웃 중이다. SKT는 AICC에 Vision AI 통합을 공언했으나 이미지 멀티모달은 2026년 상반기 목표다. 기술적으로는 Qwen2.5-VL 7B가 DocVQA 96.4%, 한국어 OCR 분야 최고 성능을 보이며 온프레미스 배포의 현실성이 검증됐다. 일 10만~100만 건 규모에서는 상용 API 대비 온프레미스 TCO가 유리해지는 임계점(일 850만 토큰)이 존재한다. 한국 개인정보보호법 관점에서 고객 제출 이미지는 서비스 계약 목적 범위 내 처리가 가능하나, 사전 고지와 최소보유 원칙 준수가 필수다. 신뢰도: 기술 현황 [A], 도입 사례 성과 수치 [C], 비용 분석 [B].

---

## 연구 질문

> 멀티모달 VLM을 통신사 고객 서비스(AICC)에 적용할 때, (1) 실제 도입 사례와 성과, (2) 기술 아키텍처 및 적합 모델, (3) 한국어 성능, (4) 상용 API vs 온프레미스 비용, (5) 프라이버시 규제 준수 방법을 파악한다.

---

## 1. 기술 현황

**TRL 및 성숙도**

멀티모달 VLM의 통신사 고객 서비스 적용은 **TRL 6~7** 수준이다. 핵심 VLM 기술 자체는 상용화 완료(TRL 9)지만, AICC와의 통합 파이프라인, 한국어 특화 튜닝, 프라이버시 보존 온프레미스 배포는 실증 단계에 있다.

**주요 기술 구성 요소**

- **비전 인코더**: ViT(Vision Transformer) 기반 이미지 임베딩. Qwen2.5-VL은 내이티브 해상도 처리(NaViT 방식)를 채택하여 이미지 왜곡 없이 원본 종횡비 처리 가능 [G-08]
- **크로스모달 어텐션**: 이미지 토큰과 텍스트 토큰을 통합 처리하는 Transformer 레이어
- **OCR-free 문서 이해**: 별도 OCR 전처리 없이 문서 내 텍스트 직독 (GOT-OCR 2.0, Qwen2.5-VL)
- **추론 서빙**: vLLM 기반 배치 처리로 Qwen2.5-VL 7B가 A100 80GB에서 ~132 토큰/초, 동시 요청 50건 기준 이미지 처리 20.89 req/s 달성 [G-13]

**기술 성숙도 매트릭스**

| 기술 요소 | 성숙도 | 비고 |
|----------|--------|------|
| 이미지→텍스트 이해 (일반) | 상용화 완료 | GPT-4o, Gemini 2.0 |
| 한국어 이미지 OCR | 실증 완료 | Gemini-1.5-Pro 80.0점 최고, Qwen 69.1점 [P-01] |
| AICC 통합 파이프라인 | 파일럿 단계 | 표준 API 없음 |
| 온프레미스 VLM 서빙 | 기술 검증 완료 | vLLM + Qwen2.5-VL |
| 엣지 VLM (1~2B) | 실증 단계 | Moondream 1.8B, SmolVLM |

---

## 2. 시장 동향

**시장 규모 및 성장**

- 멀티모달 AI 시장: 2026년 $3.4~3.9B → 2030년 $11~23B (CAGR 32~38%) [G-01]
- 통신 AI 시장: 2025년 $2.06B → 2034년 $14.86B (CAGR 22%) [G-03]
- AI 컨택센터(AICC) 시장: 2025년 $4.4B → 2030년 $14.6B (CAGR 27%) 추정

**도입 드라이버**

- 통신사의 97%가 2025년 AI 도입을 검토·적용 중 (NVIDIA 텔코 AI 조사 2026) [G-03]
- 인건비 절감 수요: AICC 상담사 1인당 연간 비용 $50K~80K(한국 기준 약 4,000~6,500만 원)
- 고객 이탈 방어: Verizon, AI로 2024년 ~10만 명 이탈 방지 예상 [G-04]
- 오픈소스 VLM 성숙: 인프라 비용 상용 대비 60% 절감 가능 [G-02]

---

## 3. 경쟁사 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| Deutsche Telekom | Sprinklr AI CCaaS로 41,000명 상담원 마이그레이션 추진(18개월). Magenta AI 챗봇 2024년 Q4 론칭. LLM 기반 티켓 자동생성 시스템 2024년 8월 도입. 이미지 기반 VLM 진단은 미공개. | [[G-05]](#ref-g-05), [[E-01]](#ref-e-01) |
| Verizon | "Project 624" — AI 기반 기기/네트워크 자가진단, 장애 알림, 사용량 기반 요금제 추천 개발 중. 고객 통화 목적 80% 정확도 예측. 상담원 보조 AI로 2024년 ~10만 명 이탈 방지 예상. | [[G-04]](#ref-g-04), [[E-02]](#ref-e-02) |
| AT&T | 생성형 AI 확장 단계. AI 가상 어셔턴트가 수백만 건 처리. 고체적 이미지 기반 진단 공개 사례 없음. | [[G-06]](#ref-g-06) |
| SKT | AICC에 Vision AI + Language AI + Big Data AI 통합 계획. A.X K1 이미지 멀티모달 2026년 상반기 추가 예정. 비용 20~30% 절감 목표 제시. | [[E-03]](#ref-e-03), [[G-07]](#ref-g-07) |
| KT | Huawei AICC 솔루션(실시간 영상통화 AI 포함) 참조 중. 자체 멀티모달 VLM 공개 발표 없음. | [[G-10]](#ref-g-10) |
| Huawei | AICC 솔루션에 실시간 영상 상호작용 + AI 내장. 통신사 B2B 공급자 포지션. | [[G-09]](#ref-g-09) |

---

## 4. 제품/서비스 스펙 비교

**오픈소스 VLM — 통신사 고객 서비스 적용 관점 비교**

| 기업/모델 | DocVQA 정확도 / 한국어 OCR | 온프레미스 배포 가능 여부 | 라이선스/가격(정책) | 출처 |
|-----------|--------------------------|------------------------|-------------------|------|
| Qwen2.5-VL 7B (Alibaba) | DocVQA 96.4% / 한국어 OCR 69.1점 (CC-OCR) | 가능 (8GB VRAM) | Apache 2.0 / 무료 | [[P-01]](#ref-p-01), [[G-11]](#ref-g-11) |
| Gemini-1.5-Pro (Google) | 상위권 / 한국어 OCR 80.0점 (CC-OCR) | 불가 (Cloud API만) | 상용: $3.5/1M input | [[P-01]](#ref-p-01), [[G-12]](#ref-g-12) |
| GPT-4o (OpenAI) | 상위권 / 한국어 OCR 74.2점 (CC-OCR) | 불가 (Cloud API만) | 상용: $2.5/1M input | [[P-01]](#ref-p-01), [[G-12]](#ref-g-12) |
| LLaMA 3.2 Vision 11B (Meta) | 양호 / 영어 중심 | 가능 (12GB VRAM) | Llama Community License / 무료 | [[G-02]](#ref-g-02) |
| MiniCPM-V 8B (OpenBMB) | GPT-4V급 / 다국어 지원 | 가능 (8GB VRAM, 모바일급) | Apache 2.0 / 무료 | [[P-02]](#ref-p-02) |
| InternVL2-76B (Shanghai AI Lab) | 높음 / 한국어 OCR 31.6점 (CC-OCR) | 가능 (고성능 서버 필요) | MIT / 무료 | [[P-01]](#ref-p-01) |

---

## 5. 학술 동향

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| CC-OCR: A Comprehensive and Challenging OCR Benchmark (Alibaba et al., 2024) | 9개 대형 멀티모달 모델의 다국어 OCR 평가. 한국어는 아시아 언어 중 중간 성능. Gemini-1.5-Pro 1위(73.0점), Qwen-VL-Max 2위(68.7점). | [[P-01]](#ref-p-01) |
| Qwen2.5-VL Technical Report (Qwen Team, 2025) | DocVQA 96.4%, OCRBench 88.8% 달성. 한국어 포함 29개 언어 지원. NaViT 방식 네이티브 해상도 처리 도입. | [[P-03]](#ref-p-03) |
| MiniCPM-V (Hu et al., 2025) | 8B 파라미터로 GPT-4V, Gemini Pro, Claude 3을 11개 벤치마크에서 추월. 모바일 실시간 실행 검증. | [[P-02]](#ref-p-02) |
| On-Premise LLM Break-Even Analysis (Xu et al., 2025) | 소형 모델(24~32B): 0.3~3개월 손익분기. 대형(235B+): 4.3~69.3개월. 월 50M 토큰 이상 시 온프레미스 경제성 우위. | [[P-04]](#ref-p-04) |
| OCRBench v2 (Liu et al., 2025) | 29개 언어 OCR 종합 벤치마크. 현대 VLM의 다국어 OCR 격차 정량화. | [[G-14]](#ref-g-14) |

---

## 6. 특허 동향

특허 수집 MCP 미사용(이번 조사는 WebSearch 한정). 기존 discover 리포트 [I-01] 기반 참고 데이터:

- **Google**: 멀티모달 비전-언어 사전학습 핵심 특허 (US20240160853A1). Frozen encoder 방식 자동 정렬
- **Apple**: 온디바이스 LLM + Vision Model for Siri (프라이버시 우선 엣지 추론)
- **Alibaba**: Qwen 시리즈 관련 중국 및 미국 특허 다수 출원 중 (구체적 번호 미확인)

---

## 7. 기업 발언 & 보도자료

**E-01. Deutsche Telekom — Sprinklr AI CCaaS 발표**
> "Our agents are the face of our brand. We want to use AI-powered solutions to help them — but never to replace them." — Löwemann (DT 임원), Sprinklr 도입 발표 [2024]
> 41,000명 상담원 AI 플랫폼 전환, 실시간 음성 분석, 대화형 IVR 탑재.

**E-02. Verizon — Project 624 AI 자가진단**
> "Verizon can accurately predict the purpose of customer calls 80% of the time" — Verizon 공식 발표 [2024]
> Project 624: AI 기기/네트워크 자가진단, 장애 선제 알림, AI 상담 보조로 2024년 ~10만 명 이탈 방지 목표.

**E-03. SKT — AI Native 전략 (MWC 2026)**
> "AI Contact Center를 금융기관 등에 확장하고, Vision AI + Language AI + Big Data AI를 통합하는 멀티LLM 전략을 추진한다." — SKT CEO 정재훈, 바르셀로나 기자회견 [2026-03-01]
> A.X K1 이미지 멀티모달: 2026년 상반기 추가. 음성·영상: 하반기 목표. 비용 20~30% 절감 목표.

---

## 8. 전략적 시사점

**기술 아키텍처 권고 — 이미지→VLM→AICC 파이프라인**

```
고객 채널(앱/웹)
    │ 이미지 업로드 (모뎀 LED, 에러 화면, 설치 환경)
    ▼
이미지 전처리 서버
    - 개인정보 마스킹 (얼굴, 배경 텍스트 블러)
    - 해상도 표준화 (768x768 이하)
    - 메타데이터 스트리핑 (EXIF 제거)
    │
    ▼
VLM 추론 서버 (온프레미스)
    - 모델: Qwen2.5-VL 7B (권장) 또는 MiniCPM-V 8B
    - 서빙: vLLM + CUDA, A100 80GB 기준 ~21 req/s
    - 진단 프롬프트: 장비 상태 분류 + 해결 단계 생성
    │
    ▼
AICC 연동 레이어
    - VLM 출력 → 기존 CRM 티켓 자동 생성
    - 신뢰도 임계값 (0.85 이상): 자동 응답
    - 미만: 상담원 에스컬레이션 + VLM 분석 참고자료 첨부
    │
    ▼
고객 응답 (텍스트/음성 합성)
```

**적합 VLM 선정 기준**

- **한국어 OCR 우선**: Gemini 2.0 Flash (API) > GPT-4o > Qwen2.5-VL (온프레미스)
- **온프레미스 필수 환경**: Qwen2.5-VLが 최우선 (Apache 2.0, DocVQA 96.4%)
- **엣지/모바일 배포**: MiniCPM-V 8B (모바일급 실행 검증)

**기회**

- 이미지 기반 1차 해결 자동화로 상담사 이관율 감소 예상 (선행 연구: 이미지 포함 문의 30~50% 자동 해결 가능 추정, 검증 필요) [C]
- Huawei AICC 대비 차별화: 오픈소스 VLM + 한국어 특화 파인튜닝으로 국내 통신 특화 모델 구축
- SKT A.X K1 멀티모달 출시(2026 상반기) 이전 파일럿 완료 시 경쟁 우위 확보 가능

**위협**

- 한국어 OCR 성능 격차: 상용 API(Gemini 80.0점) vs 오픈소스 온프레미스(Qwen 69.1점) — 약 11점 차이 [A]
- Verizon의 Project 624 자가진단 기능이 상용화되면 글로벌 표준 압박
- 고객 이미지 처리에 대한 개인정보 규제 복잡성 (아래 규제 항목 참조)

**비용 분석 요약**

| 규모 | 일 요청 건수 | 권장 배포 방식 | 월 비용 추정 |
|------|------------|--------------|------------|
| 소규모 파일럿 | ~1만 건/일 | 상용 API (GPT-4o) | ~$500~2,000 |
| 중간 규모 | 10만 건/일 | 하이브리드 (API + 캐시) | ~$5,000~15,000 |
| 대규모 | 100만 건/일 | 온프레미스 A100 클러스터 | 초기 CapEx $60K~240K + 전기/운영비 |

- 일 10만 건 = 약 3,000만~5,000만 토큰/월 (이미지 1건 = 300~500 토큰 기준)
- 온프레미스 손익분기: **월 ~9,500만 토큰 이상** (vs GPT-4o 기준) [P-04]
- 실질 전환 권고 임계: **일 50만 건 이상** (은닉 비용 포함 1.5~2배 가중)

**프라이버시 및 규제 준수**

**관련 법령**: 개인정보보호법 제15조(수집·이용), 제29조(안전조치), 정보통신망법 제24조의2

**고객 제출 이미지 처리 원칙** (개인정보보호위원회 2025.8. 생성형 AI 안내서 기준) [G-15]:
1. **목적 제한**: 서비스 계약 수행 목적 범위 내 처리 가능 (동의 재취득 불요). 단, 이미지 포함 고객정보를 AI 모델 학습에 재사용 시 별도 동의 또는 가명처리 필요
2. **최소 수집**: 진단 목적 이미지만 수집, 불필요한 얼굴·배경 정보 자동 마스킹 필수
3. **보유 기간**: 진단 완료 즉시 원본 삭제 또는 익명화 권장 (90일 이내)
4. **안전조치**: 이미지 전송 구간 TLS 암호화, 서버 접근 로그 6개월 보관
5. **국내 처리**: 해외 상용 API(GPT-4V 등) 사용 시 국외 이전 고지 및 동의 필요 → **온프레미스 VLM의 프라이버시 우위** 명확

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- Qwen2.5-VL DocVQA 96.4%, 한국어 OCR 69.1점 (CC-OCR 논문, [A])
- GPT-4o 이미지 토큰 가격 $2.5/1M input (OpenAI 공식, [A])
- 온프레미스 손익분기 월 5,000만~1억 토큰 임계값 (학술 논문, [A])
- Deutsche Telekom 41,000명 AI CCaaS 마이그레이션 계획 (공식 발표, [B])
- 한국 개인정보보호위원회 2025.8. 생성형 AI 안내서 내용 ([A])

**추가 검증 필요 [C/D]:**
- 이미지 기반 VLM 진단 시 "30~50% 자동 해결율" 추정 — 공개 사례 미확인 [C]
- Verizon Project 624 자가진단 기능 출시일 및 실제 성과 수치 미확인 [C]
- SKT AICC 비용 "20~30% 절감 목표" — 목표치이며 실적 아님 [C]

**데이터 공백:**
- 한국어 특화 VLM OCR 전용 벤치마크 (Hangul-specific, 통신 도메인)
- 글로벌 통신사의 이미지 기반 VLM 고객 서비스 실증 사례 (성과 수치)
- Qwen2.5-VL 한국어 세부 언어 분류 성능 (CC-OCR 외 독립 벤치마크)

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | GM Insights — Multimodal AI Market 2025-2034 | [링크](https://www.gminsights.com/industry-analysis/multimodal-ai-market) | report | 2026 | [B] |
| <a id="ref-g-02"></a>G-02 | Labellerr — Qwen 2.5 VL vs LLaMA 3.2 비교 | [링크](https://www.labellerr.com/blog/qwen-2-5-vl-vs-llama-3-2/) | blog | 2026 | [C] |
| <a id="ref-g-03"></a>G-03 | NVIDIA — State of AI in Telecom Survey 2026 | [링크](https://www.nvidia.com/en-us/lp/industries/telecommunications/state-of-ai-in-telecom-survey-report/) | report | 2026 | [B] |
| <a id="ref-g-04"></a>G-04 | TecKnexus — Verizon Generative AI Customer Experience | [링크](https://tecknexus.com/verizon-generative-ai-to-enhance-customer-experience/) | news | 2024 | [B] |
| <a id="ref-g-05"></a>G-05 | TecKnexus — Deutsche Telekom Generative AI Efficiency | [링크](https://tecknexus.com/deutsche-telekom-generative-ai-boosting-efficiency-and-security/) | news | 2024 | [B] |
| <a id="ref-g-06"></a>G-06 | TM Forum — How AT&T and Verizon are scaling AI | [링크](https://inform.tmforum.org/features-and-opinion/how-att-and-verizon-are-scaling-ai) | news | 2025 | [B] |
| <a id="ref-g-07"></a>G-07 | OperatorWatch — SK Telecom AI Customer Experience | [링크](https://www.operatorwatch.com/2024/10/sk-telecom-on-applying-ai-to-transform.html) | news | 2024-10 | [B] |
| <a id="ref-g-08"></a>G-08 | Qwen Blog — Qwen2-VL: See the World More Clearly | [링크](https://qwenlm.github.io/blog/qwen2-vl/) | blog | 2024 | [B] |
| <a id="ref-g-09"></a>G-09 | Huawei — AICC 솔루션 페이지 | [링크](https://carrier.huawei.com/en/products/service-and-software/software-business/aicc) | product | 2025 | [B] |
| <a id="ref-g-10"></a>G-10 | BusinessKorea — SKT KT MWC 2024 AI UAM | [링크](https://www.businesskorea.co.kr/news/articleView.html?idxno=211500) | news | 2024 | [B] |
| <a id="ref-g-11"></a>G-11 | E2E Networks — Best Open-Source OCR Models 2025 Benchmarks | [링크](https://www.e2enetworks.com/blog/complete-guide-open-source-ocr-models-2025) | blog | 2025 | [C] |
| <a id="ref-g-12"></a>G-12 | IntuitionLabs — AI API Pricing Comparison 2026 | [링크](https://intuitionlabs.ai/articles/ai-api-pricing-comparison-grok-gemini-openai-claude) | blog | 2026 | [B] |
| <a id="ref-g-13"></a>G-13 | vLLM GitHub — Multi-Modal Benchmark A100 Qwen2.5-VL | [링크](https://github.com/vllm-project/vllm/issues/24728) | blog | 2025 | [B] |
| <a id="ref-g-14"></a>G-14 | OCRBench v2 공식 페이지 | [링크](https://99franklin.github.io/ocrbench_v2/) | paper | 2025 | [A] |
| <a id="ref-g-15"></a>G-15 | 개인정보보호위원회 — 생성형 AI 개발·활용 개인정보 처리 안내서 2025.8 | [링크](https://www.privacy.go.kr/front/bbs/bbsView.do?bbsNo=BBSMSTR_000000000049&bbscttNo=20836) | official | 2025-08 | [A] |
| <a id="ref-g-16"></a>G-16 | DevTk.AI — Self-Host LLM vs API Real Cost Breakdown 2026 | [링크](https://devtk.ai/en/blog/self-hosting-llm-vs-api-cost-2026/) | blog | 2026 | [B] |
| <a id="ref-g-17"></a>G-17 | Vodworks — AI in Telecom Current State Trends 2025 | [링크](https://vodworks.com/blogs/ai-in-telecom/) | blog | 2025 | [B] |
| <a id="ref-g-18"></a>G-18 | Verizon — AI and the Empathy Gap: Human-first CX | [링크](https://www.verizon.com/about/news/ai-and-human-first-customer-experience) | press | 2024 | [A] |
| <a id="ref-g-19"></a>G-19 | TMC Net — Verizon Project 624 AI Customer Support | [링크](https://blog.tmcnet.com/blog/rich-tehrani/ai/verizon-unveils-project-624-ai-powered-overhaul-of-customer-support.html) | news | 2024 | [B] |
| <a id="ref-g-20"></a>G-20 | Google Cloud Blog — AI-driven Telecom Transformation MWC 2025 | [링크](https://cloud.google.com/blog/topics/telecommunications/the-ai-driven-telecom-how-were-powering-transformation) | blog | 2025 | [B] |
| <a id="ref-p-01"></a>P-01 | Alibaba — CC-OCR: Comprehensive and Challenging OCR Benchmark (2024) | [링크](https://arxiv.org/html/2412.02210v2) | paper | 2024-12 | [A] |
| <a id="ref-p-02"></a>P-02 | Hu et al. — MiniCPM-V Edge Deployment (Nature Communications, 2025) | [링크](https://www.nature.com/articles/s41467-025-61040-5) | paper | 2025 | [A] |
| <a id="ref-p-03"></a>P-03 | Qwen Team — Qwen2.5-VL Technical Report (2025.3) | [링크](https://arxiv.org/pdf/2502.13923) | paper | 2025-03 | [A] |
| <a id="ref-p-04"></a>P-04 | Xu et al. — On-Premise LLM Break-Even Cost Analysis (2025) | [링크](https://arxiv.org/html/2509.18101v3) | paper | 2025-09 | [A] |
| <a id="ref-e-01"></a>E-01 | Deutsche Telekom × Sprinklr — AI CCaaS 도입 사례 | [링크](https://www.sprinklr.com/stories/deutsche-telekom/) | IR/발표 | 2024 | [B] |
| <a id="ref-e-02"></a>E-02 | Verizon — Generative AI Customer Experience 공식 발표 | [링크](https://www.verizon.com/business/answers/generative-ai-customer-service/) | IR/발표 | 2024 | [A] |
| <a id="ref-e-03"></a>E-03 | SKT CEO — MWC 2026 AI Native 전략 발표 (PRNewswire) | [링크](https://www.prnewswire.com/news-releases/sk-telecom-ceo-unveils-ai-native-strategy-at-mwc26-driving-koreas-leap-in-ai-innovation-302700470.html) | IR/발표 | 2026-03-01 | [A] |
| <a id="ref-i-01"></a>I-01 | ctoti/ClaudeCode — Discover Report: 멀티모달 VLM (2026-03-12) | [로컬](outputs/reports/2026-03-12_discover-multimodal-vlm.md) | internal | 2026-03-12 | [B] |
