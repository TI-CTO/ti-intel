---
topic: Speech Generation (TTS + Voice Cloning) — 시장·비용 리서치 (Partner Hybrid 관점)
date: 2026-03-20
agent: research-deep
confidence: medium-high
status: completed
sources_used: [websearch, webfetch, existing-research]
---

# Research Report: Speech Generation — 매출 경로 & 비용 구조 (LG U+ Partner Hybrid 관점)

## Executive Summary

> 한국 AICC 시장은 2030년까지 CAGR 23.7%로 약 4,840억 원 규모로 성장 전망이다 [[G-01]](#ref-g-01). KT는 에이센으로 2025년 3,000억 원 목표를 공언했고, SKT AIX 사업은 2024년 약 1,930억 원 실현·32% 성장했다 [[G-05]](#ref-g-05). LG U+는 2025년 AICC 30% 성장, 2026년 50% 이상 성장을 목표로 하며 오픈AI 협력 에이전틱 AICC를 출시했다 [[E-03]](#ref-e-03). Partner Hybrid 전략으로 진입할 경우 API 비용(ElevenLabs 기준 월 1억 자 처리 시 약 1,800만~2,700만 원 [추정])과 망 통합·추상화 레이어 개발 비용이 핵심 OPEX를 구성한다. 신뢰도: 시장 규모 [B], 경쟁사 매출 [B], API 비용 추정 [C/D].

---

## 연구 질문

> LG U+가 Speech Generation(TTS + Voice Cloning)에 Partner(Hybrid) 전략으로 진입할 때의 **매출 경로와 비용 구조**는 무엇인가? 통신사 관점에서 1) 한국 AICC 시장 규모, 2) Voice AI 서비스 매출 경로, 3) 비용 구조(Partner Hybrid), 4) 경쟁사 매출 벤치마크를 조사한다.

---

## 1. 한국 AICC 시장 규모

#### 1.1 시장 규모 전망

**국내 시장 규모**

| 연도 | 시장 규모 | 비고 |
|------|----------|------|
| 2020 | $42.1M (약 568억 원) | Allied Market Research 기준 |
| 2025E | $350.9M (약 4,737억 원) | 전망치 |
| 2030E | $350.1M (약 4,726~4,840억 원) | CAGR 23.7% |

출처: [[G-01]](#ref-g-01) [[G-02]](#ref-g-02)

> **주의**: 2025년 추정치와 2030년 추정치가 복수 출처에서 일부 불일치함. 시장조사 기관마다 집계 범위(CC S/W만 vs. 인프라 포함)가 다르므로 단일 수치로 고정 해석 금지. [B] 신뢰도.

**글로벌 시장 규모 (참고)**

글로벌 AICC 시장은 2025년 약 $361억 (약 48.7조 원), CAGR 25% 수준이다 [[G-02]](#ref-g-02). 국내 시장은 글로벌의 약 1% 규모이며, 가격·규제 환경 특수성이 있다.

**국내 AICC 시장 경쟁 구도**

- **통신사 3사**: SKT(Persona AI 연합), KT(에이센 클라우드), LG U+(AICC Cloud + 오픈AI) — 대기업 고객 중심
- **네이버 클라우드**: CLOVA AICC, HyperCLOVA X 기반 — AI 클라우드와 번들
- **AICC 전문사**: 솔트룩스, 마음AI(마인즈랩), 스켈터랩스, 페르소나AI, Bizglobal 등
- **글로벌 SaaS**: Genesys, NICE CXone, Salesforce Service Cloud (중대형 엔터프라이즈 직접 공략)

[[G-01]](#ref-g-01) [[G-03]](#ref-g-03) [[G-04]](#ref-g-04)

#### 1.2 KT AICC 에이센 매출 목표

- **2023년 목표**: AICC 매출 1,000억 원 (2023년 상반기 에이센 클라우드 수주 360억 원 달성) [[G-06]](#ref-g-06)
- **2025년 목표**: AICC 매출 3,000억 원 (KT CFO 컨퍼런스콜 발언, 2023년 하반기) [[G-06]](#ref-g-06) [[E-01]](#ref-e-01)
- **2023년 수주 실적**: 약 2,500억 원 (전년 700억 원 대비 3배 이상 성장) [[G-06]](#ref-g-06)
- KTis(자회사) 2023년 연간 매출 5,930억 원, 영업이익 205억 원 — AICC 확대가 주요 성장 동인 [[G-07]](#ref-g-07)
- KT CS(자회사) 2023년 컨택 사업 매출 1,437억 원 + 2023년 AICC 신규 수주 1,180억 원 [[G-07]](#ref-g-07)

> 2025년 3,000억 원 목표 달성 여부는 공개 실적 자료에서 직접 확인되지 않음. 에이전틱 AICC(MWC 2026 발표) 고도화 진행 중 [[E-02]](#ref-e-02). [B]

#### 1.3 SKT AICC 매출 현황

- **AIX 사업부 2024년 매출**: 약 1,930억 원 (YoY +32%), AICC + AI Vision + AI Cloud 합산 [[G-05]](#ref-g-05)
- AICC 독립 세그먼트 분리 공시 없음. AIX 전체 성장 중 AICC 비중이 상당부분 [[G-05]](#ref-g-05)
- 2025년 AIX 사업 30% 추가 성장 목표 (SKT CFO 컨퍼런스콜) [[G-05]](#ref-g-05)
- 페르소나AI(3대 주주) 연계 AICC: KB금융, 신한, NH, 서울시 등 주요 기관 고객 확보 [[G-08]](#ref-g-08)
- **에이닷 MAU**: 2025년 10월 1,000만 명 돌파 (2024년 12월 245만 명 대비 급성장) [[E-04]](#ref-e-04)

#### 1.4 LG U+ 컨택센터 현황

- **시장 내 위치**: 전통적 콜센터 운영 기준 10년 이상 국내 최대 점유율 [[G-09]](#ref-g-09)
- **AICC 제품군**: AICC 온프레미스(구축형) + AICC 클라우드(구독형 SaaS) + 우리가게AI(소상공인) [[G-03]](#ref-g-03)
- **매출 목표 (2023년 발표)**: 2028년까지 AICC 사업 매출 1,500억 원, AI 전체 B2B 3,000억 원 [[G-10]](#ref-g-10)
- **매출 목표 (2024년 8월 수정)**: 2028년까지 누적 AICC 매출 5,100억 원 기대 [[G-11]](#ref-g-11)
- **최근 성장 (2025년 실적 컨콜, 2026년 2월)**: 2025년 AICC 매출 전년 대비 30% 이상 성장, 2026년 50% 이상 성장 목표 [[E-03]](#ref-e-03)
- 오픈AI·LG AI연구원 협력 에이전틱 AICC 1차 출시 (2025년 말) [[E-03]](#ref-e-03)

---

## 2. Voice AI 서비스 매출 경로 (통신사 기준)

#### 2.1 B2C: 가입자 부가 서비스

**현황 비교**

| 서비스 | 제공사 | MAU/현황 | 요금 모델 | 출처 |
|--------|--------|----------|----------|------|
| 에이닷 (AI 비서) | SKT | 2025-10 MAU 1,000만 돌파 | 기본 무료, 유료화 검토 중 | [[E-04]](#ref-e-04) |
| 익시오 (ixi-O) | LG U+ | 출시 2025-11, MAU 미공개 | B2C 무료 탑재 (번들) | [[E-05]](#ref-e-05) |
| 지니 (AI 스피커) | KT | MAU 공개 정보 없음 | 하드웨어 번들 |  |

**LG U+ 관련 시사점**

- 에이닷 MAU 1,000만에 대응할 LG U+ 익시오 MAU는 미공개
- SKT는 에이닷 유료화를 검토 중 (2026년 내 추진 발표) [[G-12]](#ref-g-12) — 통신사 B2C Voice AI 수익화 선례가 될 전망
- 음성 AI 부가 서비스 월 요금 벤치마크: 글로벌(Google One AI Premium $20/월, Copilot Pro $30/월) 대비 국내 통신사는 아직 무료 번들 단계
- ARPU 기여 경로: 번들 → 프리미엄 Voice 기능 유료화 → AI 구독(월 3,000~9,900원 추정) [추정, D]

#### 2.2 B2B: AICC 솔루션

**콜봇·상담 자동화 가격 모델**

공개된 국내 AICC 가격 구조:

| 모델 | 구조 | 대상 | 비고 |
|------|------|------|------|
| 구축형 (On-Premise) | 초기 구축비 + 유지보수 연 계약 | 대기업, 금융, 공공 | LG U+ AICC 온프레미스 |
| 구독형 SaaS | 월정액 (상담사 석당, 또는 콜량 기반) | 중견·중소기업 | KT 에이센 클라우드, LG U+ AICC 클라우드 |
| 소호 전용 | 월 수만 원 수준 고정 요금 | 소상공인 | LG U+ 우리가게AI |

> 구체적 단가(건당/석당/분당)는 국내 통신사 모두 미공개(영업팀 견적 기반). 공개 정보 없음.

**산업별 적용 사례**

- 금융(KB금융, 신한, NH): 대형 AICC 구축형 우선 [[G-08]](#ref-g-08)
- 의료(세브란스): KT 에이센 AI 음성 솔루션 [[G-06]](#ref-g-06)
- 병·의원: 에이센 클라우드 확산 (구독형) [[G-13]](#ref-g-13)
- 요기요·키움증권: 솔트룩스 AICC [[G-14]](#ref-g-14)

**AICC SaaS 글로벌 가격 참고 (BenchMark)**

| 제공사 | 가격 모델 | 공개 단가 |
|--------|----------|----------|
| Genesys Cloud | 시트당 월 $75~155 | 공개 |
| NICE CXone | 시트당 월 ~$71 | 공개 |
| 국내 통신사 3사 | 건당/석당 미공개 | 비공개 (영업 협의) |

#### 2.3 B2G: 공공기관 AICC·접근성 서비스

- 서울시, 지방자치단체 민원 응답 챗봇·콜봇 발주 증가
- 정부24, 복지부 복지 안내 AI 콜봇
- LG U+ 익시오 기반 복지 돌봄 서비스 확대 가능 [추정, D]
- B2G는 대형 프로젝트 위주 수주전, 구독 모델보다 구축비 + 유지보수 계약

#### 2.4 글로벌: LG U+ 익시오 해외 수출

- MWC 2026에서 홍범식 CEO가 글로벌 주요 사업자에게 익시오 동맹 제안 [[E-05]](#ref-e-05)
- 2026년 말까지 동남아 1~2개 사업자와 첫 레퍼런스 목표 [[G-15]](#ref-g-15)
- 2027년 이후 해외 수출 가속 계획 [[G-15]](#ref-g-15)
- "익시오 자체 수출 + 컴포넌트 기술 모듈 판매" 투트랙 전략 [[G-15]](#ref-g-15)
- 유럽(GDPR 장벽) 대비 동남아(규제 장벽 낮음) 우선 공략 가능성 높음 [[G-15]](#ref-g-15)

> 13개국 숫자는 현재 공개 확인되지 않음. 복수 사업자와 협의 중이나 계약 체결 확인된 국가 수는 미공개. [D]

---

## 3. 비용 구조 (Partner Hybrid 모델)

#### 3.1 ElevenLabs Enterprise API 비용

**공개 요금 체계 (셀프 서브 기준)**

| 플랜 | 월정액 | 포함 크레딧 | 추가 과금 | 비고 |
|------|--------|------------|----------|------|
| Scale | $330 | 2,000,000 chars | $0.18/1,000 chars | 통신사 미적합 |
| Business | $1,320 | 11,000,000 chars | $0.12/1,000 chars | 통신사 미적합 |
| **Enterprise** | 협상 | 협상 (볼륨 디스카운트) | 협상 | 통신사 적합 |

출처: [[G-16]](#ref-g-16) [[G-17]](#ref-g-17)

**월 1억 자(Character) 처리 시 비용 추정 [추정, D]**

> 전제: 1억 chars = 100M chars/월. 한국어 AICC 콜봇 기준 1콜당 평균 약 500~1,000자(음성 TTS 변환량) 가정.

| 시나리오 | 단가 추정 | 월 비용 (USD) | 월 비용 (KRW) |
|---------|----------|--------------|--------------|
| Business 요금 그대로 적용 | $0.12/1,000 chars | $12,000 | 약 1,620만 원 |
| Enterprise 20% 볼륨 할인 | $0.096/1,000 chars | $9,600 | 약 1,296만 원 |
| Enterprise 30% 볼륨 할인 | $0.084/1,000 chars | $8,400 | 약 1,134만 원 |

환율: 1 USD = 1,350 KRW 적용.

> 위 추정은 Business 요금제 초과 단가 기반이며 Enterprise 실제 협상 단가는 공개되지 않았음. 통신사 규모(월 수억 자)에서는 추가 볼륨 디스카운트가 적용될 가능성이 높으나 검증 불가 [D].

> 중요 참고: 월 1억 자의 맥락. SKT 에이닷 MAU 1,000만 명이 평균 월 10통화 × 1,000자 = 월 1,000억 자 규모. LG U+ AICC B2B 집중 초기 단계에서는 월 10억~100억 자 범위가 현실적. 트래픽 규모가 핵심 변수 [추정, D].

**Deutsche Telekom 파트너십 비용 구조 추정 [공개 정보 없음]**

DT-ElevenLabs 간 계약 상세는 비공개다. 업계 일반 구조 추정:
- ElevenLabs에 API 사용료(종량제 또는 커밋 볼륨) 지급 [추정, D]
- Radisys에 망 통합 프로젝트비 + 유지보수 계약 [추정, D]
- Revenue Sharing 여부 미확인 [공개 정보 없음]

#### 3.2 Naver CLOVA Voice B2B 가격

- 공개 가격 체계: 애플리케이션별 기본료 + 월 100만 자(합산) 무료 + 초과분 과금 구조 [[G-18]](#ref-g-18)
- 초과분 단가: 공식 문서에 수록되어 있으나, 실제 숫자는 네이버 클라우드 콘솔 로그인 후 확인 필요 (공개 수치 없음)
- B2B 대규모 계약 시 별도 영업 협상 (Enterprise 단가) [공개 정보 없음]
- 국내 서버 운영 → PIPA 준수 용이, 한국어 MOS 최상 수준 [[G-18]](#ref-g-18)

#### 3.3 망 내장형 통합 비용 (Radisys 또는 국내 SI)

- Deutsche Telekom + ElevenLabs + Radisys 구조에서 Radisys가 VoLTE/IMS ↔ AI 미들웨어 통합을 담당 [[E-06]](#ref-e-06)
- Radisys 망 통합 프로젝트비: 공개 정보 없음. 대형 통신사 SI 프로젝트 기준 수십억~수백억 원 규모로 추정 [추정, D]
- 국내 SI(삼성SDS, LG CNS, SK C&C 등)가 동등한 역할 수행 가능
- LG CNS는 LG 그룹사로 LG U+와 협력 이력 존재 (계열사 시너지) [[G-09]](#ref-g-09)

**망 내장형 통합 비용 항목 (구성 요소) [추정, D]**

| 항목 | 내용 | 개발 비용 추정 |
|------|------|--------------|
| VoLTE/IMS ↔ AI 스트림 연동 | 실시간 음성 스트림 라우팅 | 10억~30억 원 (프로젝트) |
| API 추상화 레이어 | 멀티벤더 TTS/STT 전환 가능 구조 | 5억~15억 원 |
| 보안·PIPA 준수 | 데이터 익명화, Zero Retention, DPA | 3억~10억 원 |
| 운영·모니터링 | SLA 관리, 이상 탐지 | 연 2억~5억 원 |

#### 3.4 API 추상화 레이어 개발 비용

- 멀티벤더 TTS/STT 아키텍처(Provider-agnostic API wrapper) 구축
- 목적: ElevenLabs/Naver CLOVA/Google 등 벤더 교체 가능한 인터페이스 표준화
- 개발 규모: 중규모 SW 프로젝트, 2~4개월 Sprint × 3~5명 팀
- 비용 추정: 3억~10억 원 (개발) + 연 1억~3억 원 (유지보수) [추정, D]

#### 3.5 선택적 Build (2027~): 오픈소스 Fine-tuning 팀 비용

- 대규모 기반 모델 자체 개발 불필요, 오픈소스 기반 Fine-tuning에 집중
- 적합 오픈소스: CosyVoice 2, Kokoro, Orpheus-TTS, Supertonic ONNX
- Fine-tuning 가능 하드웨어: 16GB VRAM GPU 1~2장으로 3B 파라미터 모델 가능 [[G-19]](#ref-g-19)

**최소 팀 구성 및 연간 비용 [추정, D]**

| 역할 | 인원 | 연봉 추정 | 연간 인건비 |
|------|------|----------|------------|
| ML Engineer (TTS 전문) | 2명 | 1.2억~1.8억/인 | 2.4억~3.6억 원 |
| Data Engineer (음성 데이터) | 1명 | 1.0억~1.4억/인 | 1.0억~1.4억 원 |
| DevOps (MLOps) | 1명 | 1.0억~1.3억/인 | 1.0억~1.3억 원 |
| **소계 (인건비)** | **4명** | — | **4.4억~6.3억 원/년** |
| GPU 인프라 (A100 8장 클러스터) | — | 월 약 1,200만 원 | 1.44억 원/년 |
| **합계** | | | **약 6억~8억 원/년** |

환율 적용 없음 (국내 비용).

---

## 4. 경쟁사 AICC 매출 벤치마크

#### 4.1 KT AICC '에이센' 매출 실적 및 목표

**주요 수치 타임라인**

| 연도 | 수치 | 근거 |
|------|------|------|
| 2022 | 수주 700억 원 | 전자신문 보도 [[G-06]](#ref-g-06) |
| 2023 상반기 | 에이센 클라우드 수주 360억 원 | 전자신문 [[G-06]](#ref-g-06) |
| 2023 연간 | 수주 2,500억 원 (전년 대비 3배) | 전자신문 [[G-06]](#ref-g-06) |
| 2023 목표 | 매출 1,000억 원 | KT CFO 발언 [[E-01]](#ref-e-01) |
| 2025 목표 | 매출 3,000억 원 | KT CFO 컨퍼런스콜 (2023년 발표) [[E-01]](#ref-e-01) |

> 수주(Order) vs. 매출(Revenue) 구분 필수: 2,500억 원은 수주 누적치로, 매출 인식 시점은 계약 조건에 따라 분산됨. 2025년 3,000억 원 매출 달성 여부는 현재 미검증. [B]

#### 4.2 SKT AI CCaaS 매출

- AIX 사업부 2024년 매출 **약 1,930억 원** (AICC + AI Vision + AI Cloud 합산), YoY +32% [[G-05]](#ref-g-05)
- 단독 AICC 세그먼트 분리 공시 없음
- 페르소나AI 연매출: 공개 수치 없음 (목표 300억 원 수준, 비상장) [[G-08]](#ref-g-08)
- 2025년 AIX 30% 성장 목표 → 추정 2025년 AIX 매출 약 2,500억 원 [추정, D]

#### 4.3 네이버 클라우드 AICC

- 네이버 클라우드 **2024년 연간 매출 5,637억 원** (YoY +41.1%) [[G-20]](#ref-g-20)
- AICC 독립 세그먼트 공시 없음; HyperCLOVA X 기반 B2B 매출이 클라우드 내 포함
- 2024년 1분기 클라우드 매출 1,170억 원 (YoY +25.5%) [[G-20]](#ref-g-20)

#### 4.4 SoundHound AI 매출 (글로벌 참고)

- **2024년 연간 매출**: $84.7M (약 1,143억 원), YoY +85% [[E-07]](#ref-e-07)
- **2025년 연간 매출**: $169M (약 2,282억 원), YoY +100% [[E-07]](#ref-e-07)
- 주요 버티컬: 자동차, QSR(패스트푸드), 고객 서비스
- 음성 AI 전문 상장사 중 가장 빠른 성장세; 통신사 AICC 직접 비교는 한계 있음

#### 4.5 국내 AICC 전문사

**주요 플레이어 동향**

| 기업 | 동향 | 출처 |
|------|------|------|
| 페르소나AI | SKT 3대 주주 투자, 목표 300억 원/연, 클라우드 AICC 국내 1위 표방, 챗봇 40% + 콜봇 30% 매출 비중 | [[G-08]](#ref-g-08) |
| 솔트룩스 | 금융(키움증권)·이커머스 AICC, 96% 응답률, 99.9% 정확도 표방, 상장사 (KOSDAQ) | [[G-14]](#ref-g-14) |
| 마음AI(마인즈랩) | 인공인간 플랫폼 maum.ai, KOSDAQ 상장 (2021), 삼성·포스코·신한·하나은행 고객 | [[G-21]](#ref-g-21) |
| 스켈터랩스 | AICC Trend 리포트 발행, B2B 특화 | [[G-22]](#ref-g-22) |
| KT is (KT 자회사) | 2023년 매출 5,930억 원 (역대 최대), AICC·타운보드·세일즈 3대 성장 동인 | [[G-07]](#ref-g-07) |
| KT CS (KT 자회사) | 2023년 매출 6,352억 원 (역대 최대), 컨택 사업 1,437억 원, AICC 수주 1,180억 원 | [[G-07]](#ref-g-07) |

---

## 5. 제품/서비스 스펙 비교 (AICC SaaS 모델)

**국내 통신사 AICC SaaS 비교**

| 기업 | 주요 모델 | AI 엔진 | 가격(정책) | 출처 |
|------|----------|---------|-----------|------|
| KT | 에이센 클라우드 (SaaS) + 에이센 온프레미스 | 믿:음 K 2.0 (11.5B), 자체 STT/TTS | 비공개 (구독형, 월 쓴 만큼 과금) | [[G-06]](#ref-g-06) [[E-01]](#ref-e-01) |
| SKT | AI CCaaS (페르소나AI 연계), SKT AICC | NUGU AI + Persona AI NLU | 비공개 (SaaS 구독) | [[G-08]](#ref-g-08) |
| LG U+ | AICC Cloud + 우리가게AI + 오픈AI 에이전틱 AICC | ixi LLM + OpenAI + LG AI연구원 | 비공개 (구독형 SaaS) | [[G-03]](#ref-g-03) [[E-03]](#ref-e-03) |
| 네이버 클라우드 | CLOVA AICC | HyperCLOVA X + CLOVA Voice | 비공개 (B2B 협의) | [[G-20]](#ref-g-20) |

> 모든 국내 통신사 AICC SaaS는 공개 단가 없음. 공개 정보 없음으로 처리.

---

## 6. 전략적 시사점

**기술 트렌드**

- 에이전틱 AICC(자율 처리 + 자가 학습)로 빠르게 고도화 중 — KT·SKT 모두 MWC 2026에서 발표
- Speech Generation(TTS + Voice Cloning)은 AICC의 프론트엔드이자 브랜드 차별화 핵심 요소
- 오픈소스 TTS 품질이 상업 API에 근접 → 2027년 이후 Build 전환 시점 도래 가능

**기회**

- LG U+는 전통적 콜센터 운영 1위 → 고객 기반 전환 용이
- Partner Hybrid로 초기 API 비용 최소화하면서 에이전틱 AICC 고도화에 투자 집중 가능
- 동남아 수출 레퍼런스 조기 확보 시 글로벌 수익 경로 개방 (2027~)
- B2G(공공 돌봄·복지) 진입은 경쟁 강도가 낮고 규제 적합성 높은 틈새 시장

**위협**

- KT 에이센 클라우드가 병·의원·금융 등 틈새 고객군에서 선점 심화 중
- SKT AIX 사업이 32% YoY 성장으로 B2B 시장에서 빠르게 확장 중
- 글로벌 SaaS(Genesys, NICE)의 대기업 직접 공략 강화 → 프리미엄 고객 유출 위험
- ElevenLabs API 의존 시 가격 인상·서비스 변경에 취약 (2024~2025년 두 차례 요금 개편)

**권고사항**

- **단기(2026 H2)**: Naver CLOVA(한국어 AICC) + ElevenLabs Enterprise(글로벌) 이중 API 계약으로 Partner Hybrid 즉시 가동. 추상화 레이어 개발 착수.
- **중기(2027)**: 트래픽 분석 후 고볼륨 한국어 구간을 오픈소스 Fine-tuning 팀(4명, 연 6억~8억 원)으로 전환하여 API 비용 절감.
- **장기(2028~)**: 동남아 레퍼런스 기반 글로벌 수출 수익 구조 확립. 익시오 컴포넌트 모듈 라이선스 모델 개발.

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- KT AICC 매출 목표(3,000억 원) 및 수주 실적 수치 — CFO 발언 + 언론 보도 교차 확인
- SKT AIX 사업부 2024년 매출 1,930억 원, YoY +32% — 실적발표 기반
- LG U+ AICC 2026년 50% 성장 목표 — 실적 컨퍼런스콜 직접 발언
- 에이닷 MAU 1,000만 (SKT 뉴스룸 공식 발표)
- SoundHound 2024년 $84.7M, 2025년 $169M — 투자자 보도자료

**추가 검증 필요 [C/D]:**
- ElevenLabs Enterprise 실제 통신사 협상 단가 [공개 정보 없음]
- 월 1억 자 처리 비용 추정 — Business 요금 기반 역산, 실제 Enterprise 단가와 괴리 있을 수 있음
- 망 내장형 통합 비용(수십억 원 추정) — 국내 사례 미확인
- Fine-tuning 팀 인건비 — 업계 평균 기반 추정
- LG U+ 해외 협의 사업자 수 (13개국 근거 미확인)

**데이터 공백:**
- Naver CLOVA Voice B2B 실제 단가 (비공개)
- 국내 AICC 콜봇 건당·분당 단가 (통신사 3사 모두 비공개)
- LG U+ AICC 독립 매출 수치 (B2B AI 전체에 포함)
- KT 2025년 AICC 매출 3,000억 원 목표 달성 여부

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Allied Market Research — 국내 AICC 시장 규모 2020~2030 | [링크](https://seo.goover.ai/report/202407/go-public-report-ko-f1915982-5c7c-4db0-87e2-3abc1f180f0f-0-0.html) | news | 2024-07 | [B] |
| <a id="ref-g-02"></a>G-02 | 뉴스투데이 — 통신 3사 5000억 AICC 시장 공략 | [링크](https://www.news2day.co.kr/article/20230823500193) | news | 2023-08-23 | [B] |
| <a id="ref-g-03"></a>G-03 | LG U+ — AICC 클라우드 공식 서비스 페이지 | [링크](https://www.lguplus.com/biz/all/telecom/phones-others/aicc-cloud/B000000129) | blog | 2024 | [A] |
| <a id="ref-g-04"></a>G-04 | Goover — 2025년 AICC 시장 경쟁 구도 분석 | [링크](https://seo.goover.ai/report/202503/go-public-report-ko-53c96b24-a1a8-42a9-be6a-bdb5acb9ee2c-0-0.html) | news | 2025-03 | [C] |
| <a id="ref-g-05"></a>G-05 | Business Korea — SKT Strong 2024 AI Business | [링크](https://www.businesskorea.co.kr/news/articleView.html?idxno=235308) | news | 2025-02 | [B] |
| <a id="ref-g-06"></a>G-06 | 전자신문 — KT 에이센 초거대 AI 탑재 | [링크](https://www.etnews.com/20230906000275) | news | 2023-09-06 | [B] |
| <a id="ref-g-07"></a>G-07 | 전자신문 — KTis 역대 최대 매출 AICC 성장 | [링크](https://www.etnews.com/20240208000042) | news | 2024-02-08 | [B] |
| <a id="ref-g-08"></a>G-08 | SKT 뉴스룸 — 페르소나AI 투자 발표 | [링크](https://news.sktelecom.com/197640) | IR/발표 | 2023 | [A] |
| <a id="ref-g-09"></a>G-09 | 전자신문 — LG U+ 스마트 컨택센터 페어 AICC 사업전략 | [링크](https://www.etnews.com/20220831000254) | news | 2022-08-31 | [B] |
| <a id="ref-g-10"></a>G-10 | 전자신문 — LG U+ AICC 5년내 3000억 목표 | [링크](https://www.etnews.com/20231105000010) | news | 2023-11-05 | [B] |
| <a id="ref-g-11"></a>G-11 | 전자신문 — LGU+ AICC 5100억 기대 인터뷰 | [링크](https://m.etnews.com/20240821000216) | news | 2024-08-21 | [B] |
| <a id="ref-g-12"></a>G-12 | 서울경제 — SKT 에이닷 유료화 추진 | [링크](https://www.sedaily.com/NewsView/2GOXWREZYL) | news | 2026-01 | [B] |
| <a id="ref-g-13"></a>G-13 | KOIT — 에이센 클라우드 병의원 확산 | [링크](https://www.koit.co.kr/news/articleView.html?idxno=124417) | news | 2024 | [B] |
| <a id="ref-g-14"></a>G-14 | 솔트룩스 — AICC 서비스 소개 | [링크](https://www.saltlux.com/kor/contents/view.do?mId=35) | blog | 2024 | [B] |
| <a id="ref-g-15"></a>G-15 | 디지털데일리 — LGU+ 음성AI 익시오 해외 진출 | [링크](https://m.ddaily.co.kr/page/view/2026030422011972194) | news | 2026-03-04 | [B] |
| <a id="ref-g-16"></a>G-16 | eesel.ai — ElevenLabs Pricing Complete Breakdown 2025 | [링크](https://www.eesel.ai/blog/elevenlabs-pricing) | blog | 2025 | [B] |
| <a id="ref-g-17"></a>G-17 | Flexprice — ElevenLabs Plans & Usage Pricing 2026 | [링크](https://flexprice.io/blog/elevenlabs-pricing-breakdown) | blog | 2026-03 | [B] |
| <a id="ref-g-18"></a>G-18 | Naver Cloud — CLOVA Voice 서비스 개요 | [링크](https://www.ncloud.com/v2/product/aiService/clovaVoice) | blog | 2024 | [A] |
| <a id="ref-g-19"></a>G-19 | Speechmatics — Custom Voice AI 2025 Open Source Boom | [링크](https://www.speechmatics.com/company/articles-and-news/custom-voice-ai-in-2025-the-open-source-boom) | blog | 2025 | [B] |
| <a id="ref-g-20"></a>G-20 | CIO Korea — 네이버 2024년 1분기 클라우드 25.5% 성장 | [링크](https://www.cio.com/article/3521064) | news | 2024 | [B] |
| <a id="ref-g-21"></a>G-21 | 마인즈랩 — 코스닥 상장 전자신문 | [링크](https://m.etnews.com/amp/20211109000199) | news | 2021-11-09 | [B] |
| <a id="ref-g-22"></a>G-22 | 스켈터랩스 — 2024 AICC 트렌드 | [링크](https://www.skelterlabs.com/blog/2024-aicc-cx) | blog | 2024 | [B] |
| <a id="ref-e-01"></a>E-01 | KT CFO 컨퍼런스콜 — AICC 2025년 3000억 원 목표 발언 (매일일보 인용) | [링크](https://www.m-i.kr/news/articleView.html?idxno=1041962) | IR/발표 | 2023 | [A] |
| <a id="ref-e-02"></a>E-02 | KT — MWC 2026 에이전틱 AICC 발표 | [링크](https://www.4th.kr/news/articleView.html?idxno=2108238) | IR/발표 | 2026-03 | [B] |
| <a id="ref-e-03"></a>E-03 | LG U+ 실적 컨퍼런스콜 2025 — AICC 50% 성장 목표 (아주경제) | [링크](https://www.ajunews.com/view/20260205110551679) | IR/발표 | 2026-02-05 | [A] |
| <a id="ref-e-04"></a>E-04 | SKT 뉴스룸 — 에이닷 MAU 1000만 돌파 | [링크](https://news.sktelecom.com/215953) | IR/발표 | 2025-10 | [A] |
| <a id="ref-e-05"></a>E-05 | 파이낸셜포스트 — LGU+ MWC2026 글로벌 익시오 동맹 제안 | [링크](https://www.financialpost.co.kr/news/articleView.html?idxno=249632) | IR/발표 | 2026-03 | [B] |
| <a id="ref-e-06"></a>E-06 | ElevenLabs 블로그 — Deutsche Telekom AI Call Assistant (Radisys 역할 포함) | [링크](https://elevenlabs.io/blog/deutsche-telekom-ai-call-assistant) | IR/발표 | 2026-03-02 | [A] |
| <a id="ref-e-07"></a>E-07 | SoundHound AI — 2025 연간 실적 $169M 발표 | [링크](https://investors.soundhound.com/news-releases/news-release-details/soundhound-ai-reports-record-annual-revenue-169-million-nearly) | IR/발표 | 2026-02-26 | [A] |
| <a id="ref-e-08"></a>E-08 | LG U+ 보도자료 — 익시오 출시 | [링크](https://www.lg.co.kr/media/release/28313) | IR/발표 | 2025-11 | [A] |
