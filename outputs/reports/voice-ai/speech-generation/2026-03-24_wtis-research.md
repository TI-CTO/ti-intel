---
topic: Speech Generation (Voice Synthesis + Voice Cloning) — 주간 업데이트
domain: voice-ai
l2_topic: speech-generation
date: 2026-03-24
agent: research-deep
wtis_mode: research-update
confidence: high
status: completed
sources_used: [websearch]
prior_reports:
  - 2026-03-17_wtis-speech-generation.md (Conditional Go, 128/200)
  - 2026-03-20_wtis-full-speech-generation.md (Partner Hybrid, ROI 664%)
research_window: 2026-03-17 ~ 2026-03-24
tags: [claude-code, wtis, research-update]
created: 2026-03-24
---

# Research Report: Speech Generation 주간 업데이트 (2026-03-17~24)

## Executive Summary

> 이번 주(3/17~24)는 Speech Generation 분야의 **기술·규제·보안 3개 축**이 동시에 임계점에 도달한 시기로 평가된다. ElevenLabs는 Eleven v3 GA(3/14), Conversational AI 2.0, 11.ai MCP 통합을 잇달아 출시하며 de facto 표준 지위를 재확인했다. 규제 측면에서 EU AI Act Article 50 시행일(2026-08-02)까지 D-130으로 진입했고, 한국 AI 기본법 Article 31은 1월 시행됐다. 보안 측면에서는 Pindrop-Zoom 실시간 딥페이크 탐지 통합(3/12)과 Pindrop 에이전틱 사기 수사 솔루션(3/17)이 출시되며 **음성 신뢰 붕괴(Voice Trust Collapse)** 대응이 AICC의 핵심 과제로 부상했다. 인프라 투자는 LiveKit $100M/$1B(1월), Deepgram $130M/$1.3B(1월), Synthflow $20M(2025년)으로 Voice AI 에이전트 인프라 전반에 자본이 집중되고 있다. 이전 분석(3/17, 3/20) 대비 **변화 없음** 항목: TAM/SAM/SOM 추정치, WTIS 판정(Conditional Go, 128/200), Partner(Hybrid) 전략 권고.

---

## 연구 질문

> 2026-03-17 이후 1주간(~03-24) Speech Generation(Voice Synthesis + Voice Cloning) 분야에서 이전 WTIS 분석 결론을 수정할 만한 새로운 기술·시장·경쟁·규제 시그널이 있는가?

---

## 1. 기술 현황

### 이전 대비 변화 있음

**ElevenLabs Eleven v3 GA (2026-03-14)**

Eleven v3 모델이 알파를 졸업하고 2026-03-14 일반 공개(General Availability, GA)되었다 [[G-01]](#ref-g-01). 주요 변화는 다음과 같다:

- **70개+ 언어 지원** + Audio Tags(`[whispers]`, `[sighs]`, `[shouts]` 등) 인라인 감정 제어
- **Text-to-Dialogue**: 멀티 스피커 자동 합성, 운율·감정 범위 일치
- 복잡한 텍스트(화학식, 전화번호 등) 오류율 **68% 감소**
- 사용자 선호도 평가에서 알파 대비 **72% 선호** [[G-02]](#ref-g-02)
- Conversational AI용 `eleven_v3_conversational` 모델 추가

**Conversational AI 2.0 출시**

ElevenLabs Conversational AI 2.0이 출시되어 음성 에이전트 플랫폼의 엔터프라이즈 요건을 충족했다 [[E-01]](#ref-e-01):

- 최신 턴테이킹(turn-taking) 모델: 언제 멈추고 말할지 이해
- **빌트인 RAG**: 중앙값 레이턴시 326ms → 155ms (50% 감소) [[G-03]](#ref-g-03)
- 멀티모달, 언어 전환, 배치 콜 지원
- HIPAA 컴플라이언스, EU 데이터 레지던시 지원

**11.ai — MCP 기반 음성 퍼스널 어시스턴트 알파**

ElevenLabs가 Model Context Protocol(MCP) 네이티브 음성 퍼스널 어시스턴트 11.ai를 알파 공개했다 [[E-02]](#ref-e-02). Perplexity, Linear, Slack, Google Calendar 등 MCP 연동 지원, 커스텀 MCP 서버 연결 가능. **음성 인터페이스 + MCP = 도구 사용 에이전트**라는 아키텍처가 실증됐다.

**Google Gemini 2.5 TTS 업데이트**

Gemini 2.5 Flash TTS 및 Gemini 2.5 Pro TTS가 GA로 전환됐다 [[G-04]](#ref-g-04). 30개 스피커, 80개+ 로케일 지원. 스타일 프롬프트 준수율, 멀티스피커 일관성, 맥락 기반 속도 조정 개선.

**Microsoft Azure Dragon HD Omni (2026-01-12 Preview)**

700개+ 사전 구축 음성, 100개+ 스피킹 스타일, 멀티링구얼 지원 Dragon HD Omni가 Microsoft Foundry를 통해 프리뷰 공개됐다 [[G-05]](#ref-g-05). SSML 튜닝 부담 제거, 통합 모델 구조.

**Qwen3-TTS 오픈소스 공개 (2026-01-22)**

Alibaba Cloud가 Qwen3-TTS를 오픈소스로 공개했다 [[G-06]](#ref-g-06):

- 3초 음성 클로닝 (제로샷)
- 10개 언어 지원 (한국어 포함)
- WER 1.835%, 스피커 유사도 0.789 — MiniMax·ElevenLabs 대비 벤치마크 우위 주장
- 0.6B~1.7B 파라미터, HuggingFace 공개
- **시사점**: 상업용 API 없이도 자체 파인튜닝 진입 장벽이 추가로 낮아짐

**Hume AI Octave 2 — 감정 TTS (2025-10 출시, 2026 Q1 확산)**

Octave 2는 감정 컨텍스트 해석 기반 TTS로 한국어 포함 11개 언어를 지원한다 [[G-07]](#ref-g-07):

- 음성 변환(voice conversion) + 음소 직접 편집(phoneme editing) 기능
- 레이턴시 200ms 이하, Octave 1 대비 속도 40% 개선, 가격 50% 절감
- `"두려움에 떨며 속삭이듯"` 등 자연어 감정 디렉션 지원

### 이전 대비 변화 없음

- TRL 8~9 성숙도 판단: 변화 없음
- ElevenLabs의 de facto 표준 지위: v3 GA로 오히려 강화
- 오픈소스(CosyVoice 2) 기반 자체 개발 진입 장벽 낮음 판단: Qwen3-TTS 추가로 유지

---

## 2. 시장 동향

### 이전 대비 변화 없음

- **TAM**: $3.65~4.25B(2025), CAGR 12~14% — 이번 주 신규 시장 조사 미발표
- TTS 시장 $3.65B(2025) → $4.1B(2026) 성장 경로 유지 [[G-08]](#ref-g-08)

### 이전 대비 변화 있음

**인프라 투자 폭증 — Voice AI 에이전트 경제 가시화**

| 기업 | 투자 | 시기 | 의미 |
|------|------|------|------|
| LiveKit | $100M, $1B 유니콘 (Index Ventures 주도) | 2026-01-22 | OpenAI 파트너, 실시간 음성 AI 인프라 [[G-09]](#ref-g-09) |
| Deepgram | $130M, $1.3B 유니콘 (AVP 주도) | 2026-01-13 | 음성 AI 경제 플랫폼화 [[G-10]](#ref-g-10) |
| ElevenLabs | $500M Series D, $11B (Sequoia 주도) | 2026-02 | ARR $330M, 최대 Voice AI 펀딩 [[G-11]](#ref-g-11) |
| Synthflow AI | $20M Series A (Accel 주도) | 2025-06 | 엔터프라이즈 노코드 음성 에이전트 [[G-12]](#ref-g-12) |
| VoiceRun | $5.5M Seed | 2026-01-14 | 음성 에이전트 팩토리 [[G-13]](#ref-g-13) |

2026년 2월은 사상 최대 스타트업 펀딩 월($1,890억 글로벌)로, Voice AI가 자율주행과 함께 대표 성장 섹터로 인식됐다 [[G-14]](#ref-g-14).

---

## 3. 경쟁사 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | Eleven v3 GA (2026-03-14), Conversational AI 2.0, 11.ai MCP 알파. ARR $330M, 기업가치 $11B | [[G-01]](#ref-g-01), [[E-01]](#ref-e-01), [[E-02]](#ref-e-02) |
| Google | Gemini 2.5 Flash/Pro TTS GA, 30 스피커 80개+ 로케일 지원 | [[G-04]](#ref-g-04) |
| Microsoft | Dragon HD Omni 700+ 음성 Preview (Azure Foundry, 2026-01-12) | [[G-05]](#ref-g-05) |
| OpenAI | gpt-4o-mini-tts 스티어러빌리티 개선, WER 35% 감소, 실시간 API 업데이트 | [[G-15]](#ref-g-15) |
| Qwen (Alibaba) | Qwen3-TTS 오픈소스 (2026-01-22), 3초 클로닝, WER 1.835% | [[G-06]](#ref-g-06) |
| Hume AI | Octave 2 출시, 한국어 포함 11언어, 감정 TTS, 200ms 이하 레이턴시 | [[G-07]](#ref-g-07) |
| SKT | MWC 2026에서 A.phone, A.note 등 음성 AI 서비스 포트폴리오 전시 | [[G-16]](#ref-g-16) |
| KT | Agentic Fabric + 음성 기반 에이전틱 AI AICC, "Human-Centered AI" 테마 | [[G-16]](#ref-g-16) |
| Pindrop | Zoom 실시간 딥페이크 탐지 통합(3/12), Fraud Assist 에이전틱 솔루션(3/17) | [[E-03]](#ref-e-03), [[E-04]](#ref-e-04) |
| Deepgram | $130M 시리즈 C 유니콘, OfOne(레스토랑 AI) 인수, 1,300개+ 기업 고객 | [[G-10]](#ref-g-10) |
| LiveKit | $100M 시리즈 C, $1B 유니콘, OpenAI 파트너, 글로벌 엣지 네트워크 | [[G-09]](#ref-g-09) |

---

## 4. 제품/서비스 스펙 비교

**주요 TTS 플랫폼 스펙 비교 (2026-03 기준)**

| 기업 | 레이턴시 / 성능 지표 | 언어 / 음성 수 | 가격(정책) | 출처 |
|------|---------------------|---------------|-----------|------|
| ElevenLabs (v3) | TTFB ~200ms, MOS 4.14 (이전 기준) | 70개+ 언어 | Enterprise $1,320+/월 | [[G-01]](#ref-g-01) |
| Google Gemini 2.5 TTS | N/A | 80개+ 로케일, 30 스피커 | Gemini API 종량제 | [[G-04]](#ref-g-04) |
| Microsoft Dragon HD Omni | N/A | 멀티링구얼 | Azure 종량제 | [[G-05]](#ref-g-05) |
| OpenAI gpt-4o-mini-tts | 저레이턴시 | 다국어 | API 종량제 | [[G-15]](#ref-g-15) |
| Qwen3-TTS (오픈소스) | 듀얼트랙 LM, WER 1.835% | 10개 언어 (한국어 포함) | 무료 오픈소스 | [[G-06]](#ref-g-06) |
| Hume Octave 2 | <200ms | 11개 언어 (한국어 포함) | Octave 1 대비 50% 절감 | [[G-07]](#ref-g-07) |

---

## 5. 학술 동향

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| Qwen3-TTS Technical Report (Alibaba, 2026-01) | 5M시간 학습, WER 1.835%, 3초 클로닝, 10개 언어 | [[P-01]](#ref-p-01) |
| Voice Cloning: Comprehensive Survey (arxiv, 2025-05) | 표준 용어 정립, few-shot/zero-shot/multilingual TTS 분류, 평가 메트릭 | [[P-02]](#ref-p-02) |
| ClonEval: An Open Voice Cloning Benchmark (arxiv, 2025-04) | 음성 클로닝 오픈 벤치마크, 리더보드 공개 | [[P-03]](#ref-p-03) |
| Targeted Speaker Poisoning in Zero-Shot TTS (arxiv, 2026-03) | 제로샷 TTS 음성 클로닝의 스피커 포이즈닝 프라이버시 위험 | [[P-04]](#ref-p-04) |

**연구 방향 변화**

3월에 출현한 Targeted Speaker Poisoning 논문은 **제로샷 TTS를 악용한 신규 공격 벡터**를 다루고 있다 [[P-04]](#ref-p-04). 음성 클로닝 기술의 방어적 측면(딥페이크 탐지, 데이터 포이즈닝 방어)이 주목받고 있으며, 이는 Pindrop의 상용화 방향과 일치한다.

---

## 6. 특허 동향

이전 분석(3/17) 대비 이번 주 특허 출원 현황의 유의미한 신규 변화는 탐지되지 않았다. 음성 합성/클로닝 특허는 빅테크(Google, Microsoft, Apple) 및 한국(삼성, LG, 네이버) 중심의 기존 집중 양상 유지.

---

## 7. 기업 발언 & 보도자료

**ElevenLabs — Conversational AI 2.0 발표 (2026-03)**

> "Conversational AI 2.0 is built to meet stringent enterprise requirements including Full HIPAA Compliance, Enterprise-Grade Security, Third-Party Integrations, and Optional EU Data Residency." [[E-01]](#ref-e-01)

**ElevenLabs — 11.ai MCP 퍼스널 어시스턴트 소개**

> "11ai demonstrates what is possible when you combine voice-first interaction with the Model Context Protocol (MCP) to give an AI assistant the ability to take action." [[E-02]](#ref-e-02)

**Pindrop — Zoom 통합 발표 (2026-03-12)**

> "Pindrop® Pulse, Pindrop® Passport and Pindrop® Protect are now integrated into Zoom Contact Center, extending real-time deepfake detection, voice authentication and fraud risk intelligence into everyday collaboration. AI-driven fraud surged 1,210% in 2025." [[E-03]](#ref-e-03)

**Pindrop — Fraud Assist 에이전틱 솔루션 발표 (2026-03-17)**

> "Generative AI fraud is projected to reach $40 billion in the U.S. by 2027. FNBO achieved a 50% improvement in fraud case disposition accuracy using Fraud Assist, while analyst efficiency increased by up to 70% on average." [[E-04]](#ref-e-04)

**LiveKit — Series C 발표 (2026-01-22)**

> "The company anticipates 2026 will be the year voice AI will be broadly deployed across thousands of use cases around the world. Voice AI applications require new network infrastructure, purpose-built for transporting voice data with as low latency as possible." [[E-05]](#ref-e-05)

**Deepgram — Series C 발표 (2026-01-13)**

> "More than 1,300 organizations build Voice AI functionality powered by Deepgram APIs." — Deepgram CEO [[E-06]](#ref-e-06)

---

## 8. 핵심 시그널 분석 — 6대 이슈

### 시그널 1: "구별 불가능 임계점" 공식 선언

Fortune(2025-12-27)에서 연구자들이 음성 클로닝이 **"구별 불가능 임계점(Indistinguishable Threshold)"을 넘었다**고 선언했다 [[G-17]](#ref-g-17). Microsoft VALL-E 2가 최초 휴먼 패리티 달성을 주장했으며, 2026년 현재 비전문가 청취자의 변별이 사실상 불가능하다. 미국인 4명 중 1명이 AI 딥페이크 음성 통화를 경험했다는 조사 결과도 동반됐다 [[G-18]](#ref-g-18).

**시사점**: 통신사 AICC의 음성 인증 기반이 붕괴. Pindrop-Zoom 통합이 즉각적 대응 사례. 음성 신뢰 인프라가 신규 사업 기회임.

### 시그널 2: EU AI Act Article 50 — D-130

EU AI Act Article 50 투명성 의무 시행일이 **2026-08-02로 D-130**에 진입했다 [[G-19]](#ref-g-19). 핵심 요건:

- 딥페이크 콘텐츠(이미지, 오디오, 영상) 생성/조작 배포자는 **AI 생성 사실을 명시**해야 함
- 최종 행동강령 Code of Practice는 2026-06 확정 예정
- 예술·창작 목적은 면제, 단 존재 사실 공개는 필요

한국 AI 기본법 Article 31(3)도 2026-01-22 시행됐다: **현실과 구별 어려운 AI 생성 음성·영상은 반드시 AI 생성 표시 의무** [[G-20]](#ref-g-20).

**시사점**: 통신사는 EU 서비스 지역에서 음성 합성 콘텐츠에 메타데이터 워터마킹/레이블링 체계 구축이 필수. 한국 내 AICC 음성봇도 Article 31 적용 대상.

### 시그널 3: Pindrop-Zoom 실시간 딥페이크 탐지 통합 (2026-03-12)

Pindrop의 Pulse, Passport, Protect 3개 제품이 Zoom Contact Center에 통합됐다 [[E-03]](#ref-e-03). Pindrop은 같은 날(3/17) Fraud Assist 에이전틱 사기 수사 솔루션도 출시했다 [[E-04]](#ref-e-04). AI 기반 사기가 2025년 1,210% 급증한 상황에서, AICC 보안 시장이 Voice AI 생성 시장의 **필수 동반 섹터**로 부상했다.

**시사점**: Voice AI 도입 시 딥페이크 탐지 스택을 반드시 동시 검토해야 함. Pindrop 같은 음성 보안 업체와의 파트너십이 차별화 요소로 작용 가능.

### 시그널 4: ElevenLabs Eleven v3 GA + 11.ai MCP + Conversational AI 2.0

한 주 안에 ElevenLabs가 3개 제품 마일스톤을 달성했다:

1. **v3 GA** (3/14): 프로덕션급 품질 — 이전 분석의 "de facto 표준" 판단 재확인 [[G-01]](#ref-g-01)
2. **Conversational AI 2.0**: 엔터프라이즈 준비 완료(HIPAA, EU 데이터 레지던시) [[E-01]](#ref-e-01)
3. **11.ai MCP**: Voice AI + MCP 에이전트 아키텍처 시연 [[E-02]](#ref-e-02)

**시사점**: ElevenLabs는 TTS API 공급자에서 **엔터프라이즈 음성 에이전트 플랫폼**으로 포지셔닝이 전환됐다. Partner 전략에서의 협상 레버리지가 더 필요해졌다.

### 시그널 5: LiveKit $100M/$1B + Deepgram $130M/$1.3B — 인프라 투자 폭증

Voice AI 에이전트를 위한 **레이어 1 인프라**에 자본이 집중되고 있다. LiveKit는 OpenAI, xAI, Salesforce 등에 실시간 음성 인프라를 공급하며 유니콘이 됐다 [[E-05]](#ref-e-05). Deepgram은 1,300개+ 기업 고객 기반으로 Series C를 완료했다 [[E-06]](#ref-e-06).

**시사점**: 음성 AI 에이전트 인프라가 성숙기로 진입. 통신사 망 내장형 Voice AI 구축 시 LiveKit/Deepgram 같은 인프라 레이어와의 통합이 현실적 옵션.

### 시그널 6: Hume Octave 2 — 감정 TTS 한국어 포함 11언어

Hume AI의 감정 TTS가 한국어를 포함한 11개 언어로 확장됐다 [[G-07]](#ref-g-07). 감정 컨텍스트 기반 운율·강세 자동 조정, phoneme 직접 편집, 200ms 이하 레이턴시. ElevenLabs와 차별화되는 감정 특화 포지셔닝.

**시사점**: 감정 TTS는 AICC의 상담 품질 향상에 직접 적용 가능. 한국어 지원으로 국내 적용 검토 가능성.

---

## 9. 전략적 시사점

**기술 트렌드**

- ElevenLabs의 플랫폼화(v3 GA + Conversational AI 2.0 + 11.ai MCP)는 단순 TTS API에서 음성 에이전트 플랫폼으로의 진화를 의미. 이전 분석의 Partner(Hybrid) 전략에서 파트너십 범위를 TTS API에서 **음성 에이전트 플랫폼 전체**로 확장해야 함
- 오픈소스(Qwen3-TTS) 강화로 한국어 자체 모델 파인튜닝의 기술적 장벽은 낮아졌으나, SKT/Naver 대비 데이터·인재 격차는 유지

**기회**

- **규제 대응 서비스**: EU Article 50(D-130), 한국 Article 31 — 통신사는 망 레벨에서 AI 음성 레이블링/워터마킹을 제공하는 유일한 포지션을 가짐
- **음성 신뢰 인프라**: Voice Trust Collapse 상황에서 AICC 딥페이크 탐지는 신규 B2B 상품화 가능 (Pindrop 파트너십 또는 자체 솔루션)
- **MCP 기반 음성 에이전트**: 11.ai가 시연한 Voice + MCP 아키텍처는 통신사 API 자산(망, 인증, 위치)을 에이전트 도구로 연결하는 모델 제시

**위협**

- ElevenLabs가 엔터프라이즈 플랫폼으로 진화하며 **통신사 AICC 시장을 직접 공략**할 가능성 증가
- Deepgram·LiveKit이 통신사급 인프라를 일반 기업에 공급 → 통신사 망 통합의 차별화가 빠르게 상쇄될 위험
- AI 생성 사기 1,210% 급증 → AICC 발신 음성에 대한 고객 불신 상승, Voice AI 채택 저항 증가 가능성

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- ElevenLabs v3 GA 일정(3/14), 기능 스펙: 공식 블로그 [A]
- Pindrop-Zoom 통합 발표(3/12), Fraud Assist(3/17): 공식 보도자료 [A]
- EU AI Act Article 50 시행일(2026-08-02): 법령 원문 [A]
- 한국 AI 기본법 시행일(2026-01-22): 법령 원문 [A]
- LiveKit $100M, Deepgram $130M 펀딩: Bloomberg, TechCrunch 등 복수 출처 [A/B]
- Qwen3-TTS WER 1.835% 벤치마크: 공식 기술 리포트 [A]

**추가 검증 필요 [C/D]:**
- "AI 기반 사기 1,210% 급증" 수치: Pindrop 자사 데이터, 독립 검증 필요 [C]
- "미국인 4명 중 1명 딥페이크 음성 경험": 단일 설문 출처 [C]
- "2027년 미국 생성 AI 사기 $400억" 예측: 단일 시장조사 [D]
- SKT/KT의 MWC 2026 이후 구체적 TTS 제품 업데이트: 공식 발표 미확인 [D]

**데이터 공백:**
- 한국 국내 음성 클로닝 사기 통계 (공식 데이터 없음)
- KT의 Agentic Fabric 내 TTS 엔진 구체적 스펙
- ElevenLabs Enterprise 가격 변화 (v3 GA 이후)

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | ElevenLabs — Eleven v3 Generally Available | [링크](https://elevenlabs.io/blog/eleven-v3-is-now-generally-available) | news | 2026-03-14 | [A] |
| <a id="ref-g-02"></a>G-02 | ElevenLabs — Eleven v3 Most Expressive AI TTS Model | [링크](https://elevenlabs.io/blog/eleven-v3) | news | 2026-03 | [A] |
| <a id="ref-g-03"></a>G-03 | ElevenLabs — How we engineered RAG to be 50% faster | [링크](https://elevenlabs.io/blog/engineering-rag) | news | 2026-03 | [A] |
| <a id="ref-g-04"></a>G-04 | Google — Gemini 2.5 TTS model updates | [링크](https://blog.google/technology/developers/gemini-2-5-text-to-speech/) | news | 2026-03 | [A] |
| <a id="ref-g-05"></a>G-05 | Microsoft — Dragon HD Omni Azure Speech Preview | [링크](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-dragon-hd-omni-azure-speech-new-voice-type-now-in-preview-via-micros/4481288) | news | 2026-01-12 | [A] |
| <a id="ref-g-06"></a>G-06 | Alibaba Qwen — Qwen3-TTS Open Source | [링크](https://qwen.ai/blog?id=qwen3tts-0115) | news | 2026-01-22 | [A] |
| <a id="ref-g-07"></a>G-07 | Hume AI — Octave 2 Launch | [링크](https://www.hume.ai/blog/octave-2-launch) | news | 2025-10 | [A] |
| <a id="ref-g-08"></a>G-08 | MarketsandMarkets — Text-to-Speech Market Size | [링크](https://www.marketsandmarkets.com/Market-Reports/text-to-speech-market-2434298.html) | report | 2026-03 | [B] |
| <a id="ref-g-09"></a>G-09 | TechCrunch — LiveKit $1B valuation | [링크](https://techcrunch.com/2026/01/22/voice-ai-engine-and-openai-partner-livekit-hits-1b-valuation/) | news | 2026-01-22 | [A] |
| <a id="ref-g-10"></a>G-10 | TechCrunch — Deepgram $130M 1.3B valuation | [링크](https://techcrunch.com/2026/01/13/deepgram-raises-130m-at-1-3b-valuation-and-buys-a-yc-ai-startup/) | news | 2026-01-13 | [A] |
| <a id="ref-g-11"></a>G-11 | AssemblyAI — Voice AI in 2026 | [링크](https://www.assemblyai.com/blog/voice-ai-in-2026-series-1) | report | 2026-03 | [B] |
| <a id="ref-g-12"></a>G-12 | BusinessWire — Synthflow AI $20M Series A | [링크](https://www.businesswire.com/news/home/20250624442670/en/Synthflow-AI-Raises-$20M-to-Transform-the-$168B-Global-Conversational-AI-Market-With-Enterprise-AI-Voice-Agents) | news | 2025-06-24 | [A] |
| <a id="ref-g-13"></a>G-13 | TechCrunch — VoiceRun $5.5M | [링크](https://techcrunch.com/2026/01/14/voicerun-nabs-5-5m-to-build-voice-agent-factory/) | news | 2026-01-14 | [A] |
| <a id="ref-g-14"></a>G-14 | AssemblyAI — Voice AI Investment Landscape 2026 | [링크](https://www.assemblyai.com/blog/voice-ai-in-2026-series-1) | report | 2026-03 | [B] |
| <a id="ref-g-15"></a>G-15 | OpenAI — gpt-4o-mini-tts updates | [링크](https://developers.openai.com/blog/updates-audio-models/) | news | 2026-03 | [A] |
| <a id="ref-g-16"></a>G-16 | Korea Tech Today — AI-Telco Moment MWC 2026 | [링크](https://koreatechtoday.com/koreas-ai-telco-moment-strategic-signaling-at-mwc-2026/) | news | 2026-03 | [B] |
| <a id="ref-g-17"></a>G-17 | Fortune — Voice cloning crossed indistinguishable threshold | [링크](https://fortune.com/2025/12/27/2026-deepfakes-outlook-forecast/) | news | 2025-12-27 | [B] |
| <a id="ref-g-18"></a>G-18 | State of the Call 2026 — AI Deepfake Voice Calls Hit 1 in 4 Americans | [링크](https://www.galvnews.com/state-of-the-call-2026-ai-deepfake-voice-calls-hit-1-in-4-americans-as/article_7d33386c-0819-5d0e-a328-7c0ab4f3f27b.html) | news | 2026-03 | [B] |
| <a id="ref-g-19"></a>G-19 | EU AI Act — Article 50 Transparency Obligations | [링크](https://artificialintelligenceact.eu/article/50/) | 법령 | 2024 | [A] |
| <a id="ref-g-20"></a>G-20 | South Korea AI Basic Act — Article 31 Enforcement | [링크](https://www.cooley.com/news/insight/2026/2026-01-27-south-koreas-ai-basic-act-overview-and-key-takeaways) | 법령 | 2026-01-27 | [A] |
| <a id="ref-e-01"></a>E-01 | ElevenLabs — Conversational AI 2.0 발표 | [링크](https://elevenlabs.io/blog/conversational-ai-2-0) | 보도자료 | 2026-03 | [A] |
| <a id="ref-e-02"></a>E-02 | ElevenLabs — Introducing 11.ai | [링크](https://elevenlabs.io/blog/introducing-11ai) | 보도자료 | 2026-03 | [A] |
| <a id="ref-e-03"></a>E-03 | Pindrop — Zoom Integration 딥페이크 탐지 | [링크](https://www.globenewswire.com/news-release/2026/03/12/3254709/0/en/Pindrop-Zoom-Integration-Embeds-Real-Time-Deepfake-Detection-and-Identity-Verification-in-Zoom-Contact-Center.html) | 보도자료 | 2026-03-12 | [A] |
| <a id="ref-e-04"></a>E-04 | Pindrop — Fraud Assist 에이전틱 솔루션 | [링크](https://www.globenewswire.com/news-release/2026/03/17/3257231/0/en/Pindrop-Unveils-First-Agentic-Fraud-Investigation-Solution-to-Combat-Surging-AI-Driven-Fraud.html) | 보도자료 | 2026-03-17 | [A] |
| <a id="ref-e-05"></a>E-05 | LiveKit — Series C Funding Announcement | [링크](https://blog.livekit.io/livekit-series-c/) | 보도자료 | 2026-01-22 | [A] |
| <a id="ref-e-06"></a>E-06 | Deepgram — Series C Press Release | [링크](https://deepgram.com/learn/press-release-deepgram-raises-series-c) | 보도자료 | 2026-01-13 | [A] |
| <a id="ref-p-01"></a>P-01 | Alibaba Qwen et al. — Qwen3-TTS Technical Report | [링크](https://arxiv.org/html/2601.15621) | paper | 2026-01 | [A] |
| <a id="ref-p-02"></a>P-02 | Comprehensive Survey on Voice Cloning | [링크](https://arxiv.org/abs/2505.00579) | paper | 2025-05 | [A] |
| <a id="ref-p-03"></a>P-03 | ClonEval: An Open Voice Cloning Benchmark | [링크](https://arxiv.org/abs/2504.20581) | paper | 2025-04 | [A] |
| <a id="ref-p-04"></a>P-04 | Targeted Speaker Poisoning in Zero-Shot TTS (2026-03) | [링크](https://arxiv.org/abs/2603.07551) | paper | 2026-03 | [A] |
