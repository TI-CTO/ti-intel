---
topic: spam-phishing-detection
date: 2026-03-05
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
domain: secure-ai
l3_topic: 스팸피싱감지(통화전)
---

# Research Report: 스팸/피싱 감지 (통화전) 기술 동향

> 수집 기간: 2026-03-05 / 참조 기간: 2025-01 ~ 2026-03

## Executive Summary (경영진 요약)

스팸·보이스피싱 감지 기술은 2025~2026년 사이 **기기내(On-Device) AI** 와 **네트워크 레벨 사전 차단** 이라는 두 축으로 급속히 고도화되었다. Google이 Gemini Nano 온디바이스 AI를 Galaxy S26에 탑재(2026-02-25)하고, SKT·KT·LG U+ 3사가 각각 에이닷 전화·후후·익시오 앱을 통해 통화 중 실시간 탐지 서비스를 상용화했다. 국제적으로는 Deutsche Telekom·e&·Singtel·SKT·SoftBank 5개 통신사가 합작법인 Syntelligence(런던, $37.5M 투자)를 통해 네트워크 데이터 기반 사전 차단 시스템을 개발 중이다. 학술 분야에서는 KoBERT+CNN-BiLSTM 멀티모달 융합(F1=0.994), RAG 기반 LLM(정확도 97.98%) 등 고성능 모델이 2025년 발표되었다. 규제 측면에서는 미국 FCC의 STIR/SHAKEN 3rd-party 서명 규제(2025-09) 강화와 한국 과기정통부의 AI 공동대응 플랫폼(2026~2027 구축 예정)이 제도적 기반을 다지고 있다.

**신뢰도: 높음** — 주요 사실관계는 기업 공식 발표 및 학술 논문(A/B급) 출처로 교차확인됨.

---

## 연구 질문

> 2025-01 이후 스팸·피싱 감지(통화전/통화중) 기술의 기술 성숙도, 경쟁사 움직임, 시장 구조, 학술·특허 동향은 어떠한가?

---

## 1. 기술 현황

### 1.1 기술 성숙도 (TRL)

| 기술 계층 | TRL | 비고 |
|-----------|-----|------|
| 네트워크 레벨 사전 차단 (메타데이터 분석) | 8–9 | T-Mobile, KT 등 상용화 |
| 온디바이스 AI (통화중 실시간 텍스트 분석) | 7–8 | SKT 에이닷, Google Gemini Nano |
| 딥보이스 탐지 (음성 위변조 감지) | 6–7 | KT 3중 체계 포함, 상용화 시작 |
| 멀티모달 (텍스트+음성 융합) | 5–6 | 연구 단계, 2025 논문 발표 |
| RAG 기반 LLM 실시간 탐지 | 4–5 | 연구 단계 (~98% 정확도) |

### 1.2 핵심 기술 요소

**통화전(Pre-Call) 사전 차단 방식:**
- **메타데이터 기반**: 전화번호 패턴, 호 발신 빈도, 통화 시간 예측, 발신 범위 스캔 특성 등 행동 시그니처 분석. T-Mobile은 6분마다 모델 업데이트 [G-06]
- **STIR/SHAKEN 발신번호 인증**: 미국 FCC 강제화. 2025-09부터 3자 서명자 규제 강화 [G-14]
- **군집 데이터 활용**: 최근 1시간 내 수천 명에게 발신된 번호 플래그. Syntelligence는 5개 통신사 수십억 건 호 패턴으로 훈련 [G-07]

**통화중(In-Call) 실시간 탐지 방식:**
- **온디바이스 LLM**: Gemini Nano (Google/Samsung), 에이닷 전화 자체 모델 (SKT). 서버 미전송, 개인정보 보호 [G-02][E-01]
- **키워드+대화 패턴 분석**: 보이스피싱 유형별 스크립트 패턴 학습. '의심(suspected) / 위험(dangerous)' 2단계 알림 [E-01]
- **3중 체계 (KT)**: AI 문맥 탐지 + 화자인식(범죄자 음성DB) + 딥보이스 탐지 [E-02]

---

## 2. 시장 동향

### 2.1 시장 규모

- **글로벌 모바일 피싱 방어 시장**: 2024년 $2.67B → 2034년 $15.99B (CAGR 19.6%) [G-08]
- **전화 스팸 피해 규모**: 2024년 전 세계 $41.8B 손실, 미국 성인 92%가 스팸 전화 수신 [G-07]
- **한국 보이스피싱 피해**: KT 2025년 탐지 기준 건당 평균 피해액 약 4,100만원, SKT 기준 2025년 1인당 평균 5,384만원 [E-02][E-04]

### 2.2 주요 드라이버

1. **AI 생성 보이스피싱 위협 고도화**: 음성 클론 기술의 범용화로 딥보이스 기반 사기 급증 [G-01][G-09]
2. **스마트폰 OS 수준 통합**: Google Android / Samsung One UI가 탐지 기능을 OS 레이어로 흡수 [G-02]
3. **통신사 규제 강화**: FCC STIR/SHAKEN 확대, 한국 과기정통부 AI 공동대응 플랫폼 법제화 추진 [G-14][N-04]
4. **소비자 인식 상승**: 피해 뉴스가 지속적으로 노출되며 탐지 솔루션 수요 증가

---

## 3. 경쟁사 동향

### 3.1 글로벌 플레이어

**Google (Alphabet)**
- Gemini Nano 기반 Scam Detection을 2026-02-25 Galaxy S26에 확장 [G-02][G-03]
- 이전 Pixel 전용에서 Android 생태계 전반으로 확대 전략
- 현재 미국·영어 한정, 추후 다국어·다기기 확장 예정
- MWC 2026에서 Android AI 업데이트 발표 중 포함 [G-03]

**Samsung**
- Galaxy S26에 Google Scam Detection 네이티브 통합 (Phone by Google 앱 불필요) [G-03]
- 삼성전자 한국 내 이통3사와 통화 중 AI 보이스피싱 탐지 협력 [N-03]

**T-Mobile (미국)**
- Scam Shield: 네트워크 레이어에서 6분 간격 AI 모델 업데이트
- 타 미국 이통사 대비 스캠 탐지 30% 우위 (GlobalData) [G-06]
- 기본 무료 제공 + 프리미엄 유료 옵션

**Syntelligence (합작법인)**
- 설립: 2025년 말 영국 런던, $37.5M 펀딩 [G-07]
- 창립사: Deutsche Telekom·e&·Singtel·SK Telecom·SoftBank
- CEO: Prateek Choudhary (前 Meta AI·Amazon Prime Video)
- 의장: SKT 정석근
- 핵심 제품: Security Shield (네트워크 레벨 사전 차단), Welcome Manager (AI 고객응대)
- 경쟁 우위: 5개 통신사 수십억 건 호 패턴 학습 데이터

### 3.2 국내 플레이어

**SK Telecom**
- 에이닷 전화에 AI 보이스피싱 탐지 기능 추가 (2025-12-01 출시) [E-01]
- 온디바이스 AI: 통화 데이터 서버 미전송, Android/iOS 지원
- 탐지 수준: '의심' / '위험' 2단계 팝업·알림음·진동
- Syntelligence 창립 멤버 겸 의장사

**KT**
- 실시간 AI 보이스피싱 탐지 서비스 (2025-01 상용화, 후후 앱 기반) [E-02][E-03]
- 2025년 성과: 44백만 건 통화 분석, 약 3만 건 경보, 1,300억원 피해 예방
- 탐지 정확도: Q1 90.3% → Q4 93%+ 지속 개선
- 국내 최초 3중 예방 체계 (AI 문맥 + 화자인식 + 딥보이스)
- 2025-07 KT AI 보이스피싱 탐지 서비스 2.0 출시 [E-03]
- 국무조정실 '적극행정 우수사례' 국민투표 최우수 선정 (2025-11)

**LG유플러스**
- 익시오(ixi-O) 앱 통화 중 보이스피싱 탐지·알림 [E-04][E-05]
- 안티딥보이스 + 범죄자 목소리 탐지 기능 포함
- 독자적 접근: 국내 통신사 유일 악성 앱 제어 서버 추적 시스템
- 2025년 약 800개 악성 서버 추적, 3만 3,000명 위기 고객 특정 → 경찰 정보 제공
- 예방 피해액 추산: 1조 8,000억원 규모 [E-04]
- '고객피해방지 분석시스템': AI 기반 대내외 데이터 통합 분석
- 스팸 위험도 수치화 기능 ('익시오' 업데이트) [E-05]

**KT 후후 (B2C)**
- 착신 번호 정보 제공 + 통화 중 실시간 AI 탐지 결합
- 안드로이드 기반 앱 서비스

---

## 4. 제품/서비스 스펙 비교

| 기업 | 탐지 방식 | 탐지 정확도 | 처리 방식 | 주요 기능 | 출시/업데이트 | 출처 |
|------|----------|------------|---------|---------|-------------|------|
| Google (Pixel/Galaxy S26) | 온디바이스 Gemini Nano | 공개 정보 없음 | On-Device | 통화중 패턴 분석, 음성+텍스트 알림 | 2026-02-25 (S26 확장) | [G-02][G-03] |
| T-Mobile Scam Shield | 네트워크 레벨 메타데이터 | 공개 정보 없음 | Network | 6분 간격 모델 업데이트, Scam Likely 표시 | 운영 중 (2025 업데이트) | [G-06] |
| Syntelligence Security Shield | 네트워크 레벨 (5사 데이터) | 공개 정보 없음 | Network | 수십억 호 패턴 학습, 통화 전 차단 | 개발 중 (2025년 말 설립) | [G-07] |
| SKT 에이닷 전화 | 온디바이스 AI (의심키워드+패턴) | 공개 정보 없음 | On-Device | 2단계 알림, Android/iOS, 에이닷 앱 | 2025-12-01 | [E-01] |
| KT 후후 (AI 보이스피싱 탐지) | 온디바이스 AI + 3중 체계 | Q4 2025: 93%+ | On-Device | AI문맥+화자인식+딥보이스 | 2025-01 상용화, 2025-07 v2.0 | [E-02][E-03] |
| LG유플러스 익시오 (ixi-O) | 온디바이스 AI + 악성서버 추적 | 공개 정보 없음 | On-Device + Network | 안티딥보이스, 범죄자 목소리 탐지, 악성 앱 서버 추적 | 2025년 운영 중 | [E-04][E-05] |

---

## 5. 학술 동향

### 5.1 주요 논문 (2025)

**[P-01] 멀티모달 보이스피싱 탐지 시스템 (MDPI Applied Sciences, 2025-10-18)**
- 텍스트 모듈: KoBERT 기반 트랜스포머 + Self-Attention
- 오디오 모듈: MFCC 피처 + CNN-BiLSTM (딥보이스 감지)
- 가중 융합(8:2 텍스트:오디오) → F1-score **0.994**
- 실세계 통화 전사, 피싱 데이터셋, 합성 음성 코퍼스 대상 실험
- 출처: [G-10]

**[P-02] RAG 기반 LLM 실시간 사기 탐지 (arXiv, 2025-01)**
- 저자: Gurjot Singh, Prabhjot Singh, Maninder Singh
- BERT, 비훈련 LLM, RAG 모델 비교
- RAG 접근법: 정책 재훈련 없이 업데이트 가능 (배포 유연성 강점)
- 정확도 **97.98%**, F1-score **97.44%** (100콜 테스트)
- 2가지 방어: 개인정보 요청 차단 + 신원 사칭 탐지
- 출처: [P-02 arXiv 2501.15290]

**[P-03] SpaLLM-Guard: SMS 스팸 감지 LLM 비교 (arXiv, 2025-01)**
- GPT-4, DeepSeek, LLAMA-2, Mixtral 평가
- Fine-tuning 전략이 최효과적: Mixtral **98.61% 정확도**
- Zero-shot, Few-shot, CoT prompting 방식별 성능 비교
- 출처: [G-11]

**[P-04] LLM의 스팸 탐지 취약성 연구 (arXiv, 2025-04)**
- GPT2, BERT 기반 탐지 시스템의 적대적 공격 취약성 분석
- 공격자가 LLM을 활용하여 피싱 분류기를 우회하는 'Talking Like a Phisher' 공격 벡터 제시
- 출처: [G-11]

**[P-05] Vishing 최초 종합 서베이 및 로드맵 (ScienceDirect, 2025)**
- 미국 연간 30만 명 이상 피해
- 심리적 설득 전략, 음성 기반 탐지, AI 생성 vishing 감지/생성 로드맵 제시
- 출처: [G-12]

### 5.2 연구 방향 요약

- **멀티모달 융합**: 텍스트(전사)+오디오(음성특성) 결합이 단일 모달 대비 성능 우위 확인
- **딥보이스 위협 대응**: 합성 음성 감지 모듈이 탐지 시스템 필수 구성요소로 자리잡음
- **LLM 적용 확대**: Fine-tuning 및 RAG 방식으로 98% 수준의 정확도 달성
- **온디바이스 추론**: 개인정보 보호 요구로 에지 배포 연구 증가
- **적대적 공격 연구**: LLM이 탐지기를 우회하는 공격 벡터도 동시에 연구됨 (군비경쟁 구도)

---

## 6. 특허 동향

### 6.1 주요 출원 현황

**Apple**
- 스팸 통화 사전 차단 특허: 발신 번호 + 네트워크 장비 식별자 + 서버 신원을 온라인 DB와 교차 확인하여 통화 연결 전 사용자 알림. 최초 출원 2017, 지속 보강 중 [G-13]
- 발신번호 스푸핑 방지 관련 특허 보유

**Google**
- Gemini Nano 기반 온디바이스 AI 시스템 관련 특허 다수 출원 (구체 번호 공개 정보 없음)

**국내 통신사**
- KT: 실시간 통화 분석 + 화자인식 기반 보이스피싱 탐지 기술 특허 출원 (구체 번호 공개 정보 없음)

> 주: SerpAPI Google Patents 수집 미실행 상태. 위 내용은 뉴스/보도 기반 [B/C급]. 특허 세부 청구항은 추가 검색 필요.

---

## 7. 기업 발언 & 보도자료

### E-01 SKT — 에이닷 전화 AI 보이스피싱 탐지 기능 출시 (2025-12-01)

> "AI 보이스피싱 탐지는 온디바이스 AI 기술을 기반으로 통화 내용 분석부터 경고 알림까지의 전 과정을 단말 내에서 처리한다. 통화 데이터가 서버를 거치지 않고 별도의 데이터 저장·삭제 과정이 없기 때문에, 정보 유출 우려 없는 안전한 탐지가 가능하다."
— SKT 뉴스룸 공식 보도자료 [A급]

### E-02 KT — AI 보이스피싱 탐지 2025년 성과 발표 (2025-12-23)

> "지난 1월 상용화한 실시간 AI 보이스피싱 탐지 서비스를 통해 올 한해 약 1,300억원 규모의 보이스피싱 피해를 예방한 것으로 나타났다. 탐지 정확도는 Q1 90.3%에서 Q4 93% 이상으로 지속 개선됐다."
— KT 공식 보도자료, 전자신문 [A급]

### E-03 KT — AI 보이스피싱 탐지 서비스 2.0 출시 (2025-07-29)

> "목소리까지 잡는다. 신고된 보이스피싱 범죄자의 음성 특징을 활용한 화자인식 기술, 딥보이스(Deep Voice) 탐지 기능을 결합한 국내 최초 '3중 보이스피싱 예방 체계'를 구축해 운영 중이다."
— 경향신문 [B급]

### E-04 LG유플러스 — 악성 앱 서버 추적으로 3만명 보호 (2026-02~03 보도)

> "국내 통신사 중 유일하게 보이스피싱·스미싱 범죄 조직이 운영하는 악성 앱 제어 서버를 추적하고 있다. 약 800개 악성 서버를 추적·분석했으며 고객 3만3,000여명을 특정해 경찰에 정보를 제공했다. 피해 예방 성과는 금액 기준 약 1조8,000억원 규모."
— LG유플러스 뉴스룸 및 다수 언론 [A/B급]

### E-05 Syntelligence — 5개 통신사 합작법인 설립 및 CEO 선임 발표

> "Security Shield는 실제 네트워크 데이터를 기반으로 수십억 건의 통화 패턴을 학습한 세계에서 가장 강력한 스캠 탐지 시스템이다. 창립 5개 통신사의 시장에 먼저 출시할 계획이다."
— Syntelligence 공식 발표 / TelecomTV [B급]

### E-06 Google — MWC 2026 Android AI 업데이트 발표 (2026-03-02)

> "Scam Detection on the Galaxy S26 series uses Google's Gemini Nano on-device AI model to monitor calls for speech patterns linked to scams. Users don't need the Google Phone app — it's now integrated into Samsung's native phone application."
— Android Authority / Google 공식 블로그 [A/B급]

### E-07 과기정통부 — AI 보이스피싱 서비스 이용 안내 (2026-02-12)

> "삼성전자와 SK텔레콤·KT·LG유플러스 등 이동통신 3사가 AI를 활용해 통화 중 보이스피싱을 실시간으로 탐지하고 이용자에게 즉시 알리는 서비스를 제공하고 있다. 'AI 기반 보이스피싱 통신서비스 공동 대응 플랫폼' 구축 사업(2026~2027년)을 추진 중이다."
— 전자신문 [B급]

---

## 8. 전략적 시사점

### 8.1 기술 트렌드 요약

1. **탐지 레이어 이원화**: 통화 전(네트워크/메타데이터)과 통화 중(온디바이스 AI)이 상호 보완적으로 발전. 단일 레이어만으로는 고도화된 AI 생성 보이스피싱에 대응 한계
2. **온디바이스 AI 패러다임 확립**: 개인정보 보호 요구가 서버 전송 방식에서 온디바이스 처리로 업계 표준 전환 가속
3. **딥보이스 탐지가 핵심 변수**: 음성 클론 기술 범용화로 화자인식+딥보이스 감지 모듈이 필수화
4. **멀티모달 연구 성숙**: 텍스트+오디오 융합 모델(F1=0.994)이 상용화 문턱에 근접
5. **군비경쟁 구도**: 공격자(LLM 기반 피싱 스크립트 자동화)와 방어자(LLM 기반 탐지) 간 경쟁이 심화

### 8.2 시장 구조 관찰

- **플랫폼 통합 경쟁**: Google이 Android OS 레벨에서 탐지 기능을 흡수하는 전략은 독립 앱 기반 서비스 사업자에게 위협
- **통신사 컨소시엄**: Syntelligence는 네트워크 데이터 독점성을 경쟁 무기로 내세우며 기기 레이어와 차별화
- **한국 통신사 3사**: 각사 독자 앱 서비스로 사용자 락인 강화 동시에 정부 공동플랫폼 참여 의무 예상
- **규제 환경 강화**: 미국 FCC의 STIR/SHAKEN 확대와 한국 과기정통부 플랫폼 사업이 시장 의무 참여 수요 형성

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- SKT 에이닷 전화 AI 보이스피싱 탐지 출시 (2025-12-01) — 공식 보도자료
- KT 후후 2025년 성과 수치 (1,300억원, 탐지 정확도 93%+) — 공식 보도자료+전자신문
- LG유플러스 악성 앱 서버 추적 3만 3,000명 보호 — 뉴스룸 발표
- Google Scam Detection Galaxy S26 확장 (2026-02-25) — Google 공식 블로그
- Syntelligence 설립 멤버, $37.5M 투자, CEO 인선 — TelecomTV·공식 발표
- P-01 멀티모달 F1=0.994, P-02 RAG 97.98% — 동료심사 학술지/arXiv

**추가 검증 필요 [C/D]:**
- T-Mobile의 'GlobalData 30% 우위' 주장 — 출처 단일, 독립 검증 필요
- Syntelligence Security Shield 출시 일정 및 실제 성능 — "곧 발표 예정" 수준
- 특허 청구항 세부 내용 — 특허 DB 직접 검색 미수행
- LG U+ 예방 피해액 1조 8,000억원 — 추산 방식에 의존성 (1인당 피해액 가정)

**데이터 공백:**
- Apple iOS 사전 통화 차단 최신 제품 사양 (2025-2026 업데이트 내용)
- Syntelligence Security Shield 실제 출시 후 성능 데이터
- 국내 3사 서비스 가입자 수 및 탐지 건수 (SKT·LG U+ 미공개)
- FCC STIR/SHAKEN 2025-12 FNPRM 최종 채택 여부

---

## References

### 글로벌 출처 (G-xx)

| 번호 | 출처명 | 발행일 | 기관유형 | 제목 | 인용원문(한글) | 관련성 | 신뢰성 | 최신성 | URL |
|------|--------|-------|----------|------|-------------|--------|--------|--------|-----|
| G-01 | Kymatio Blog | 2026 | 보안 전문 미디어 | Phishing Trends 2026: AI-Phishing, QRishing & Voice Deepfakes | 음성 클론 AI로 딥보이스 피싱이 2026년 핵심 위협으로 부상 | 5 | 4 | 5 | [링크](https://kymatio.com/blog/phishing-trends-ai-phishing-qrishing-and-voice-attacks) |
| G-02 | Android Authority | 2026-02-25 | 기술 미디어 | Google's Scam Detection is now on the Galaxy S26 | Google Gemini Nano가 Samsung Galaxy S26에서 미국 영어 한정 가동 | 5 | 5 | 5 | [링크](https://www.androidauthority.com/google-scam-detection-samsung-galaxy-s26-3643942/) |
| G-03 | Jetstream Blog | 2026-02 | 기술 미디어 | Phone by Google Scam Detection Expands to Samsung Devices | Google Scam Detection이 Samsung 네이티브 전화 앱에 통합 | 5 | 4 | 5 | [링크](https://jetstream.blog/en/phone-by-google-scam-detection-expands-samsung/) |
| G-04 | Android Central | 2026-03 | 기술 미디어 | Galaxy S26 steps up its Android defenses with Scam Detection | Galaxy S26의 AI 기반 통화 보안 기능 상세 분석 | 5 | 4 | 5 | [링크](https://www.androidcentral.com/phones/samsung-galaxy/galaxy-s26-steps-up-its-android-defenses-with-scam-detection-and-this-is-exactly-what-i-needed) |
| G-05 | Google Security Blog | 2025-03 | 기업 공식 블로그 | New AI-Powered Scam Detection Features to Help Protect You on Android | Google의 Android AI 스캠 탐지 기능 공식 발표 | 5 | 5 | 4 | [링크](https://security.googleblog.com/2025/03/new-ai-powered-scam-detection-features.html) |
| G-06 | T-Mobile | 운영 중 | 이통사 공식 | T-Mobile Scam Shield App | 6분 간격 AI 업데이트, 네트워크 레벨 Scam Likely 표시 | 5 | 5 | 4 | [링크](https://www.t-mobile.com/benefits/scam-shield) |
| G-07 | Trending Topics EU | 2025 | 기술 미디어 | Syntelligence: 5 Telecom Giants Launch AI Joint Venture to Combat Spam Calls | 5개 통신사 합작, $37.5M, Security Shield 개발 중 | 5 | 4 | 5 | [링크](https://www.trendingtopics.eu/syntelligence-5-telecom-giants-launch-ai-joint-venture-to-combat-spam-calls/) |
| G-08 | Market.us | 2024-2034 | 시장조사기관 | Mobile Phishing Protection Market Size, CAGR of 19.6% | 모바일 피싱 방어 시장 2024년 $2.67B → 2034년 $15.99B | 4 | 3 | 4 | [링크](https://market.us/report/mobile-phishing-protection-market/) |
| G-09 | Group-IB Blog | 2025 | 보안기업 | The Anatomy of a Deepfake Voice Phishing Attack | AI 생성 음성 기반 차세대 스캠 공격 분석 | 5 | 4 | 5 | [링크](https://www.group-ib.com/blog/voice-deepfake-scams/) |
| G-10 | MDPI Applied Sciences | 2025-10-18 | 학술지 | A Multimodal Voice Phishing Detection System Integrating Text and Audio Analysis | KoBERT+CNN-BiLSTM 융합 모델, F1=0.994 달성 | 5 | 5 | 5 | [링크](https://www.mdpi.com/2076-3417/15/20/11170) |
| G-11 | arXiv | 2025-01 | 프리프린트 | SpaLLM-Guard / LLM Spam Detection Vulnerability | Mixtral Fine-tuning 98.61%, LLM 취약성 동시 연구 | 4 | 4 | 5 | [링크](https://arxiv.org/html/2501.04985v1) |
| G-12 | ScienceDirect | 2025 | 학술지 | Vishing: Detecting social engineering in spoken communication | 미국 연간 30만 vishing 피해, 최초 종합 서베이 | 5 | 5 | 5 | [링크](https://www.sciencedirect.com/science/article/pii/S0885230825000270) |
| G-13 | Gearbrain / Pocketnow | 2017+ | 기술 미디어 | Apple Patents spam call detection before answer | 발신번호+네트워크 장비+서버 신원 교차확인 특허 | 3 | 4 | 2 | [링크](https://www.gearbrain.com/iphone-spam-call-blocking-2611717625.html) |
| G-14 | Sangoma Blog / FCC | 2025-09 | 규제기관/기업 | Understanding FCC's New STIR/SHAKEN Rules 2025 | 3자 서명자 규제 강화, 2025-09 발효 | 5 | 5 | 5 | [링크](https://sangoma.com/blog/the-new-fcc-stir-shaken-rules-and-why-they-matter-for-your-business-in-2025/) |
| G-15 | TelecomTV | 2025 | 통신 전문 미디어 | Five major telcos pump $37.5m into AI venture | Syntelligence $37.5M 투자 확인 | 5 | 4 | 5 | [링크](https://www.telecomtv.com/content/ai/five-major-telcos-pump-37-5m-into-ai-venture-54939/) |

### 최신 동향 (N-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약(한글) | URL |
|------|--------|-------|------|-----------|----------|-----|
| N-01 | 아시아에이 | 2025-12 | SKT 에이닷 전화, AI로 통화 중에도 보이스피싱 잡아낸다 | SKT 에이닷 전화 보이스피싱 탐지 | 에이닷 전화 AI 보이스피싱 탐지 기능 탑재 소개 | [링크](https://www.asiaa.co.kr/news/articleView.html?idxno=232111) |
| N-02 | 전자신문 | 2025-12-23 | KT, AI 보이스피싱 탐지로 2025년 약 1300억원 이용자 피해 예방 | KT 보이스피싱 AI 탐지 | 44백만 건 통화 분석, 탐지 정확도 93%+ | [링크](https://www.etnews.com/20251223000189) |
| N-03 | 정책브리핑 | 2026 | 인공지능으로 통화 중에 '보이스피싱' 잡는다 | 과기정통부 보이스피싱 AI | 삼성+이통3사 협력, 과기정통부 2026~2027 공동플랫폼 계획 | [링크](https://www.korea.kr/news/policyNewsView.do?newsId=148959497) |
| N-04 | 전자신문 | 2026-02-12 | 과기정통부 "보이스피싱 피해 방지, AI 탐지·알림 서비스 이용하세요" | 과기정통부 AI 보이스피싱 공동대응 플랫폼 2026 | 공동대응 플랫폼 2026~2027 구축 공식 발표 | [링크](https://www.etnews.com/20260212000065) |
| N-05 | The Mobile Network | 2026-02 | Syntelligence AI is the Global Telco AI Alliance now | Syntelligence GTAA spam call | Syntelligence가 Global Telco AI Alliance로 리브랜딩 | [링크](https://the-mobile-network.com/2026/02/syntelligence-ai-is-the-global-telco-ai-alliance-now/) |
| N-06 | 이지이코노미 | 2026 | AI로 범죄 서버 쫓은 LG유플러스, 보이스피싱 위기 고객 3만명 구했다 | LG유플러스 보이스피싱 AI 스팸차단 2025 | 악성 앱 서버 800개 추적, 1.8조 피해 예방 추산 | [링크](https://www.ezyeconomy.com/news/articleView.html?idxno=231337) |

### 기업 발언 (E-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약원문 |
|------|--------|-------|------|-----------|---------|
| E-01 | SKT 뉴스룸 | 2025-12-01 | SKT 에이닷 전화, AI로 통화 중에도 보이스피싱 잡아낸다 | SKT 에이닷 전화 보이스피싱 탐지 출시 | "통화 데이터가 서버를 거치지 않고... 정보 유출 우려 없는 안전한 탐지가 가능하다" |
| E-02 | KT 공식 / 전자신문 | 2025-12-23 | KT, AI 보이스피싱 탐지로 2025년 약 1300억원 피해 예방 | KT 보이스피싱 1300억 2025 | 탐지 정확도 90.3%→93%+, 44백만 건 분석, 1,300억원 피해 예방 |
| E-03 | 경향신문 | 2025-07-29 | KT, AI로 보이스피싱 범죄자 목소리 잡아낸다 | KT AI 보이스피싱 탐지 서비스 2.0 | 국내 최초 3중 보이스피싱 예방 체계 (AI 문맥+화자인식+딥보이스) |
| E-04 | LG유플러스 뉴스룸 / 언론 | 2026-02~03 | LG유플러스, 악성 앱 서버 추적해 보이스피싱 위기 고객 3만명 보호 | LG유플러스 보이스피싱 AI 2025 | 국내 통신사 유일 악성 앱 제어 서버 추적, 예방 1.8조 추산 |
| E-05 | LG유플러스 뉴스룸 | 2025 | 스팸 위험도를 숫자로! 더 똑똑해진 ixi-O | LG유플러스 익시오 스팸 | 스팸 위험도 수치화, 안티딥보이스, 범죄자 목소리 탐지 기능 |
| E-06 | Google 공식 블로그 / Android Authority | 2026-02-25 | Google's Scam Detection is now on Galaxy S26 | Google Scam Detection Gemini Nano S26 2026 | "Google Gemini Nano on-device AI model... monitors calls for speech patterns linked to scams" |
| E-07 | 전자신문 / 정책브리핑 | 2026-02 | 과기정통부 "AI 탐지·알림 서비스 이용하세요" | 과기정통부 AI 보이스피싱 공동대응 플랫폼 2026 | 삼성+이통3사 서비스 안내, 2026~2027 공동 플랫폼 구축 계획 발표 |

### 학술 논문 (P-xx)

| 번호 | 저자 | 발행년도 | 제목 | 학술지/컨퍼런스 | 인용수 | 핵심 인용 | DOI/URL |
|------|------|---------|------|----------------|--------|----------|---------|
| P-01 | (저자명 공개 정보 없음) | 2025-10-18 | A Multimodal Voice Phishing Detection System Integrating Text and Audio Analysis | MDPI Applied Sciences | - | KoBERT+CNN-BiLSTM 융합 F1=0.994, 텍스트:오디오 8:2 가중 융합 최적 | [링크](https://www.mdpi.com/2076-3417/15/20/11170) |
| P-02 | Gurjot Singh, Prabhjot Singh, Maninder Singh | 2025-01 | Advanced Real-Time Fraud Detection Using RAG-Based LLMs | arXiv (2501.15290) | - | RAG 기반 실시간 통화 사기 탐지, 정확도 97.98%, F1 97.44% | [링크](https://arxiv.org/html/2501.15290v1) |
| P-03 | (다수 저자) | 2025-01 | SpaLLM-Guard: Pairing SMS Spam Detection Using Open-source and Commercial LLMs | arXiv (2501.04985) | - | Mixtral fine-tuning 98.61%, GPT-4/DeepSeek/LLAMA-2 비교 | [링크](https://arxiv.org/html/2501.04985v1) |
| P-04 | (다수 저자) | 2025-04 | An Investigation of Large Language Models and Their Vulnerabilities in Spam Detection | arXiv (2504.09776) | - | GPT2/BERT 기반 탐지기 적대적 공격 취약성 분석 | [링크](https://arxiv.org/abs/2504.09776) |
| P-05 | (다수 저자) | 2025 | Vishing: Detecting social engineering in spoken communication — A first survey & urgent roadmap | ScienceDirect (Computer Speech and Language) | - | 미국 30만+/년 vishing 피해, 탐지 로드맵 최초 제시 | [링크](https://www.sciencedirect.com/science/article/pii/S0885230825000270) |
| P-06 | (다수 저자) | 2025 | The silence of the phishers: Early-stage voice phishing detection with runtime permission requests | ScienceDirect (Computers & Security) | - | 통화 연결 전 런타임 권한 요청 패턴으로 조기 탐지 | [링크](https://www.sciencedirect.com/science/article/abs/pii/S0167404825000537) |

### 특허 (T-xx)

| 번호 | 출원인 | 등록/출원일 | 특허번호 | 제목 | 핵심 청구항 | 관할 |
|------|--------|-----------|---------|------|-----------|------|
| T-01 | Apple Inc. | 2017 출원 (이후 보강) | 공개 정보 없음 | Detection of Spoofed Call Information | 발신번호+네트워크 장비 식별자+서버 신원 교차 확인 → 통화 전 사용자 알림 | USPTO |

> 주: 특허 DB (Google Patents / USPTO) 직접 수집 미실행. 위 내용은 언론 보도 기반 [C급]. 추가 특허 검색 권장.

### 내부 자료 (I-xx)

해당 없음 (이번 리서치에서 내부 문서 참조 없음)
