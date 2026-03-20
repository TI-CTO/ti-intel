---
topic: KAIST SoulMate 온디바이스 RAG+LoRA AI 반도체
date: 2026-03-20
agent: research-deep
confidence: medium
status: completed
sources_used: [websearch, webfetch]
---

# Research Report: KAIST '소울메이트' — 온디바이스 RAG+LoRA AI 반도체 심층 분석

## Executive Summary

> KAIST 유회준 교수팀은 2026년 3월 17일, 28nm FD-SOI 공정 기반 온디바이스 LLM 가속기 '소울메이트(SoulMate)'를 공개했다. 핵심 혁신은 RAG와 LoRA를 반도체 내부에 직접 구현한 Mixed-Rank Architecture로, 9.8mW의 초저전력에서 0.2초(216.4ms) 응답을 실현한다. ISSCC 2026 하이라이트 논문으로 선정되어 학술적 검증을 받았으며, 교원 창업기업 온뉴로AI를 통해 2027년 제품화를 목표로 한다. 경쟁 SoC 대비 공정 노드는 열세(28nm vs. 2-3nm)이며, MediaTek Dimensity 9400(2024.10)이 이미 온디바이스 LoRA 학습을 상용 지원하므로 "유일"이라는 주장은 성립하지 않는다. 소울메이트의 실질 차별점은 9.8mW 초저전력에서 RAG+LoRA를 단일 칩으로 동시 완결하는 설계에 있다. LG U+의 익시오가 Gemini API와 EXAONE sLM의 이중 구조로 운영되는 시점에서, 소울메이트 칩은 완전 온디바이스 개인화 AI의 하드웨어 레이어로 기능할 수 있어 통신사 B2B/B2C 전략에서 의미 있는 분기점을 만든다. 다만 지원 가능한 LLM 파라미터 수, 토큰 처리량(tok/s), 메모리 스펙 등 핵심 벤치마크는 공개 논문 전문 미공개로 현시점에서 확인 불가.

## 연구 질문

> KAIST '소울메이트' 칩의 기술적 실체는 무엇인가, 글로벌 경쟁 NPU 대비 어떤 차별점을 갖는가, LG U+ 익시오 아키텍처에 통합 가능한가, 우리 도메인(Voice/Agentic/Secure AI)에 주는 전략적 시사점은 무엇인가.

---

## 1. 기술 상세

### 1-1. 아키텍처 개요

소울메이트는 KAIST 인공지능반도체대학원 유회준 교수팀이 개발한 **온디바이스 LLM 개인화 가속기**다. 공식 논문 제목은 *"SoulMate: A 9.8mW Mobile Intelligence System-on-Chip with Mixed-Rank Architecture for On-Device LLM Personalization"* (ISSCC 2026 Highlight Paper) [G-01].

**핵심 기술 두 축:**

- **RAG 하드웨어 구현**: 사용자 대화 이력을 온칩 메모리에 저장하고, 추론 시 해당 데이터를 검색하여 개인화된 응답을 생성. 외부 벡터 DB 서버 불요.
- **LoRA 온칩 학습**: 사용자 피드백을 수신할 때마다 LoRA 가중치를 실시간 업데이트. 전통적인 파인튜닝 대비 최소 연산 자원만 소요. 모델 전체를 재학습하지 않고 저랭크(low-rank) 행렬만 갱신.

**Mixed-Rank Architecture:**
정보의 중요도에 따라 LoRA 랭크(rank)를 동적으로 조절하는 구조. 중요도 높은 정보에는 높은 랭크를, 중요도 낮은 정보에는 낮은 랭크를 할당해 연산량과 전력을 최적화한다. 이 메커니즘이 9.8mW라는 초저전력을 가능하게 하는 핵심 요소다 [G-02].

### 1-2. 하드웨어 스펙

| 항목 | 값 | 비고 |
|------|-----|------|
| 공정 | 28nm FD-SOI (Fully Depleted Silicon-On-Insulator) | 삼성 파운드리 [G-01] |
| 칩 크기 | 20.25mm² (쌀알 크기) | 배경 정보 기준 |
| 전력 소비 | **9.8mW** | 스마트폰 프로세서의 약 1/500 [G-02] |
| 응답 지연 | **216.4ms (0.2초)** | 학습과 추론 동시 수행 기준 [G-01] |
| 지원 LLM 크기 | **공개 정보 없음** | 풀 논문 미공개 |
| 처리량 (tok/s) | **공개 정보 없음** | 풀 논문 미공개 |
| TOPS | **공개 정보 없음** | 42.5 TOPS/W 언급은 단일 출처 [C] |
| 메모리 | **공개 정보 없음** | 풀 논문 미공개 |

> **참고**: techbytes.app 기사에서 "42.5 TOPS/W 에너지 효율, 16MB RRAM"을 언급하나, 이는 단일 비공식 출처([C])이며 공식 ISSCC 논문과의 일치 여부가 검증되지 않아 [추정]으로만 표기한다.

### 1-3. 이전 연구 이력 — 유회준 교수

유회준 교수는 국내 AI 반도체 분야 최고 권위자 중 한 명이다 [G-05].

- 1995년 현대전자(現 SK하이닉스)에서 세계 최초 256M SDRAM 개발, ISSCC에 한국 최초 논문 발표
- 2008년부터 AI 반도체 연구 시작
- **2014년 세계 최초 DNN 가속기 발표** (ISSCC)
- 2024년 2월: DNN+SNN 하이브리드 아키텍처 기반 GenAI LLM 가속기 발표 — A100 GPU 대비 1/625 전력, 1/41 크기로 GPT-2 구동 (28nm 삼성 공정) [G-06]
- ISSCC 누적 논문 발표 **63편** — 동양인 유일 톱5 최다 발표자 [G-05]
- 현재 KAIST 인공지능반도체대학원 원장, PIM반도체설계 연구센터장

### 1-4. 학술 발표

- **ISSCC 2026 Highlight Paper** 선정 (2026년 2월 16일, 샌프란시스코) [G-01]
- 제1 저자: 홍성연 박사과정 연구원 [G-03]
- 공저자: Jiwon Choi, Jeonggyu So, Nayeong Lee, Wooyoung Jo, Zhamaliddin Kalzhan [G-04]
- IEEE Xplore 수록 예정, 전문 공개 미확인

---

## 2. 경쟁 기술 비교

**주요 온디바이스 AI 플랫폼 스펙 비교**

| 기업/제품 | 공정 | NPU 성능 | 전력 효율 | 온디바이스 학습(LoRA) | 지원 모델 크기 | 출처 |
|-----------|------|----------|----------|----------------------|---------------|------|
| **KAIST SoulMate** | 28nm FD-SOI | 공개 정보 없음 (42.5 TOPS/W [추정]) | 9.8mW 전체 | **가능 (하드웨어 내장)** | 공개 정보 없음 | [[G-01]](#ref-g-01) |
| **MediaTek Dimensity 9400** | TSMC 3nm (N3P) | 공개 정보 없음 | 공개 정보 없음 | **가능 (최초 상용 온디바이스 LoRA)** | ~3B-7B | [팩트 체크] |
| **Qualcomm Snapdragon 8 Elite Gen 5** | TSMC 3nm (N3P) | ~100 TOPS | 공개 정보 없음 | 추론 전용 (학습 불가) | ~3B-7B (추론) | [[G-08]](#ref-g-08) |
| **Apple A18 Pro (Neural Engine)** | TSMC 3nm | 35 TOPS | 공개 정보 없음 | 제한적 (MLX 기반, 서드파티) | ~3B (Apple Foundation) | [[G-09]](#ref-g-09) |
| **Apple M4 (Neural Engine)** | TSMC 3nm | 38 TOPS | 공개 정보 없음 | 가능 (MLX, Swift Foundation Models API) | ~3B (on-device) | [[G-10]](#ref-g-10) |
| **Google Tensor G5** | TSMC 3nm | 공개 정보 없음 (G4 대비 60% 향상) | 공개 정보 없음 | 추론 전용 | Gemini Nano (32K context) | [[G-11]](#ref-g-11) |
| **Samsung Exynos 2600** | 삼성 2nm GAA | **80 TOPS** | 공개 정보 없음 | 추론 전용 | 공개 정보 없음 | [[G-12]](#ref-g-12) |
| **Supertone Supertonic** | 소프트웨어 (ONNX) | 해당 없음 | N/A (추론 전용) | 불가 | **66M (TTS 전용)** | [[G-13]](#ref-g-13) |

**비교 분석:**

- **공정 노드**: 소울메이트 28nm는 경쟁사(2-3nm) 대비 2-3세대 열세. 이는 절대 성능(TOPS)에서 큰 격차를 의미하나, 해당 칩의 설계 목표는 고성능이 아닌 **초저전력 개인화 학습**이므로 직접 비교는 부적절.
- **온디바이스 학습 가능 여부**: ~~소울메이트만이~~ **MediaTek Dimensity 9400**(TSMC 3nm, 2024.10 출시)이 이미 "최초 온디바이스 LoRA 학습" 상용 칩으로 공식 발표됨. Apple M4도 MLX로 LoRA/QLoRA 지원. 따라서 "유일"은 과장이며, 소울메이트의 실질 차별점은 **9.8mW 초저전력에서 RAG+LoRA를 단일 칩으로 동시 완결**하는 설계. [팩트 체크: `2026-03-20_factcheck-kaist-soulmate-claims.md`]
- **전력 소비**: 9.8mW는 극단적 저전력이나, "스마트폰 SoC의 1/500"이라는 비교는 **28nm 단기능 칩 vs 3nm 완전 통합 SoC의 이종 비교**로 오해 유발. 소울메이트가 지원하는 LLM 크기가 미공개이므로 동일 워크로드 기준 비교는 불가. 단, 웨어러블/이어버드 폼팩터에서 LLM 구동이 가능한 전력 수준이라는 점은 의미 있음.
- **Supertonic**: 비교 대상이 다소 다름. 66M 파라미터 TTS 전용 모델로 167× 실시간 처리, 소울메이트가 개인화 LLM 추론에 집중하는 것과 역할 분리가 가능.

---

## 3. 온뉴로AI 창업 현황

**온뉴로AI (OnNeuroAI Inc.) 기본 정보**

- **설립 유형**: KAIST 교원 창업기업 [G-01]
- **대표자/설립자**: 유회준 교수 (KAIST 인공지능반도체대학원 원장) [G-03]
- **법인 등록 여부**: 공개 정보 없음 (정확한 법인 등록일 미확인)
- **투자 유치 현황**: 공개 정보 없음 (발표 시점 기준 공개 투자 정보 없음)
- **팀 구성**: 교수 + 박사과정 학생 스핀오프로 추정 [추정] — 제1 저자 홍성연 박사과정 등 연구팀 포함 가능성

**2027년 제품화 로드맵 구체성 평가:**

언론 보도에서 "2027년경 제품화"가 반복적으로 언급되나 [G-01][G-02][G-03], 다음 사항이 불명확하다:

- 어떤 디바이스 폼팩터(스마트폰, 웨어러블, IoT 모듈)를 타깃으로 하는지
- 파운드리 협력사(삼성 28nm 공정 사용 중이나 양산 계약 여부 불명)
- 투자 라운드 및 자본 조달 방식
- 소프트웨어 스택(SDK, 지원 모델 종류) 공개 일정

> 전반적으로 "기술 검증(TRL 5~6) 완료, 상용화 로드맵은 초기 단계"로 평가된다. 28nm 공정은 TSMC/삼성 모두 성숙 공정으로 양산 접근성이 높은 장점이 있다.

---

## 4. LG U+ 익시오 적용 가능성

### 4-1. 현재 익시오 AI 아키텍처

LG U+ 익시오는 현재 **이중 구조**로 운영 중이다:

- **클라우드 레이어**: Google Gemini 2.5 Flash Live API (대화 맥락 이해, 복잡 질의) [G-14]
- **온디바이스 레이어**: LG AI연구원 EXAONE 3.5 기반 경량 sLM (통화 요약, 키워드 추출 등 단순 기능) — 전력 78% 절감, 모델 크기 82% 축소 [G-15]
- 현재 Snapdragon 8 탑재 Android 기기 우선 지원, iOS 확대 예정 [G-15]

**핵심 구조적 한계**: 개인화 학습(사용자 말투/취향/감정 적응)은 클라우드 Gemini API에 의존. 통화 내용이 서버로 전송되는 프라이버시 리스크 존재 [G-14].

### 4-2. 소울메이트 통합 시나리오

**시나리오 A: 소울메이트 칩 내장 전용 디바이스 (2027+)**

```
[사용자] → [소울메이트 칩 내장 AI 디바이스]
              └─ RAG (온칩 개인화 대화 이력)
              └─ LoRA (실시간 개인 말투 학습)
              └─ 익시오 서비스 레이어 (통신 없이 완전 온디바이스)
```

LG U+가 온뉴로AI와 파트너십을 체결하여 소울메이트 칩 탑재 전용 AI 디바이스(이어버드, 스마트워치, 개인형 AI 디바이스)를 출시하는 시나리오. 9.8mW 전력 특성상 배터리 소형 기기에 최적.

**시나리오 B: 현 스마트폰 구조에 소울메이트 코프로세서 추가 (중장기)**

기존 Snapdragon/Exynos SoC 옆에 소울메이트를 개인화 코프로세서로 탑재. 메인 SoC는 범용 AI 처리, 소울메이트는 개인 학습 전담. 제조사 협력 필요.

**시나리오 C: 소울메이트 IP 라이선스 (단기 현실적)**

온뉴로AI가 SoC 벤더(삼성/퀄컴)에 Mixed-Rank LoRA+RAG 아키텍처 IP를 라이선스. LG U+는 차세대 Exynos/Snapdragon 탑재 익시오 기기에서 수혜.

### 4-3. 적용 시 차별화 포인트

**보안 우위:**
- 현재 Gemini API 전송 구조 → 통화 내용 서버 전달 [G-14]. 소울메이트 완전 온디바이스 전환 시 클라우드 전송 없음.
- GDPR, EU AI Act, 국내 개인정보보호법 대응 측면에서 "데이터 원천 차단" 마케팅 가능.
- 기업 고객(B2B) 대상 임원 통화 보안, 기밀 유지 솔루션으로 포지셔닝 가능.

**개인화 깊이:**
- 현재 익시오의 개인화는 클라우드 기반 세션 단위 → 기기 전원 끄면 컨텍스트 소실.
- 소울메이트 온칩 RAG: 수개월 대화 이력을 디바이스에 영속 저장, 진정한 장기 개인화 실현.

**LG U+ 차별화 전략 맥락:**
- KT/SKT 대비 AI 서비스 차별화 시급 → 프라이버시 보장 + 초개인화 AI 에이전트가 통신사 락인 포인트로 작동 가능.

---

## 5. 우리 도메인 시사점

### 5-1. Voice AI 도메인

**기술 트렌드**

- 소울메이트의 실시간 말투 학습(LoRA) + RAG 이력 기반 응답은 Voice Agent 개인화의 하드웨어 기반을 제공한다.
- Supertone Supertonic(66M, ONNX)과 소울메이트(LLM 개인화)를 결합하면 "완전 온디바이스 개인화 Voice Agent" 스택이 완성된다: Supertonic이 TTS 담당, 소울메이트가 LLM 추론+개인화 담당.

**기회**

- 익시오 AI 비서의 다음 단계: 현재 통화 요약 → 2027년 "내 말투를 아는 AI 비서" 완전 온디바이스 전환
- 감정 인식(소울메이트의 MSPU [C]) + 음성 합성(Supertonic) 결합으로 감성 AI 통화 서비스

**위협**

- Apple이 M 시리즈 Neural Engine + Foundation Models LoRA API(Swift)를 통해 iOS 생태계 내 유사 개인화 기능 제공 시 독자 기술 차별화 희석
- 소울메이트 2027년 제품화까지 격차 — 경쟁사가 먼저 온디바이스 LoRA를 구현할 경우 선점 우위 소실

### 5-2. Agentic AI 도메인

**기술 트렌드**

- RAG를 칩 레벨에서 구현 = Adaptive RAG의 하드웨어 가속. 현재 소프트웨어 레이어 RAG(Gemini API 호출 + 벡터 DB 조회)를 온칩으로 대체하면 레이턴시가 API 왕복 시간(~500ms-2s) → 216ms로 단축.
- 에이전트 루프(Plan → Act → Observe)에서 개인 컨텍스트 조회 단계가 병목 → 소울메이트 온칩 RAG로 해결 가능.

**기회**

- 익시오 AI 에이전트의 툴콜 결정 전 사용자 히스토리 조회를 온디바이스로 전환
- B2B 에이전트 솔루션: 기업 직원의 업무 패턴을 온디바이스 학습 → 데이터가 사내망 밖으로 나가지 않음

**위협**

- 소울메이트가 지원 가능한 LLM 크기 불명 → 복잡한 멀티스텝 Agentic 태스크에는 대형 모델(70B+) 필요, 온디바이스 칩 한계

### 5-3. Secure AI 도메인

**기술 트렌드**

- "Security-Complete AI" 구조 — 모든 개인 데이터를 디바이스 내에서만 처리, 외부 서버 전송 없음 [G-01]
- EU AI Act, GDPR, 국내 개인정보보호법 2.0 시행 환경에서 "온디바이스 = 규제 리스크 최소화" 내러티브 강화

**기회**

- 통신사 AI 서비스의 최대 리스크인 "통화/메시지 데이터 서버 유출" 우려를 원천 차단하는 기술 포지셔닝
- 기업 고객(금융, 법무, 의료) 대상 프리미엄 보안 AI 서비스 라인 구축

**위협**

- 완전 온디바이스화 시 클라우드 AI 업데이트(모델 개선, 프롬프트 패치)가 어려워짐 → 보안 취약점 패치 지연 리스크

### 5-4. 감정교류 AI 시장 기회

**시장 규모 교차 검증:**
- Emotion AI 시장: 2025년 $3.4B → 2034년 $20.77B, CAGR 22.29% (Fortune Business Insights) [G-16]
- AI Companion 시장(더 넓은 범주): 2025년 $33-37B → 2034년 $389-552B, CAGR ~31% (복수 리서치 기관) [G-16]
- 배경 정보의 "$55.5B by 2034" 수치는 단일 출처 기반으로 추정되나 [추정], 방향성(대규모 성장)은 복수 소스 지지

**통신사 포지셔닝:**
- 현재 통신사는 데이터 파이프로만 기능 → 소울메이트 기반 "AI 반려 서비스"의 네트워크+디바이스 번들링으로 OTT 유사 락인 효과
- 고령화 사회(홀로 사는 노인) 대상 감성 AI 서비스는 규제 우호적이고 사회적 명분도 확보 가능

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- 소울메이트 발표 사실, ISSCC 2026 하이라이트 논문 선정 (복수 주요 언론 보도)
- 9.8mW 전력 소비, 216.4ms 응답 지연, 28nm FD-SOI 공정, Mixed-Rank Architecture (ISSCC 공식 발표)
- 유회준 교수 이력 (ISSCC 63편, 2014년 세계 최초 DNN 가속기)
- LG U+ 익시오의 Gemini 2.5 Flash Live + EXAONE sLM 이중 구조 (공식 보도자료)
- Qualcomm S8E Gen 5 (~100 TOPS), Exynos 2600 (80 TOPS, 2nm GAA) 스펙

**팩트 체크 결과 (Devil's Advocate 검증, 2026-03-20):**

| 초기 주장 | 판정 | 핵심 반례 |
|----------|------|----------|
| "유일한 온칩 LoRA 학습" | **과장** | MediaTek Dimensity 9400(2024.10)이 상용 온디바이스 LoRA 최초 |
| "RAG 하드웨어 통합 유일" | **부분적 사실** | RAG는 SW 패턴, 다른 NPU+벡터DB로도 가능. 칩 완결은 차별점 |
| "9.8mW = SoC의 1/500" | **과장** | 28nm 단기능 vs 3nm 통합 SoC 이종 비교 |
| "216ms 실시간 대화" | **미확인** | 모델 크기·토큰 수 조건 미공개 |

> 상세: `outputs/reports/2026-03-20_factcheck-kaist-soulmate-claims.md`

**추가 검증 필요 [C/D]:**
- 소울메이트 TOPS 수치 (42.5 TOPS/W) — techbytes.app 단일 출처, 비공식 딥다이브
- 소울메이트 지원 LLM 파라미터 수 — 풀 논문 미공개, 모든 보도에서 누락
- 온뉴로AI 법인 등록 세부사항, 투자 현황 — 공식 공시 없음
- 감정교류 AI 시장 "$55.5B by 2034" — 배경 정보 수치이나 동일 수치 교차 확인 불가
- **MediaTek Dimensity 9400의 LoRA가 연속 학습인지 초기 1회 파인튜닝인지** — 공개 문서 불명확

**데이터 공백:**
- 소울메이트의 토큰 처리량(tok/s), 메모리 대역폭, 칩 내 SRAM/외부 메모리 연결 방식
- 온뉴로AI 팀 구성, 투자 현황, 파운드리 협력 계약 여부
- 소울메이트가 지원하는 구체적 LLM 모델명 및 파라미터 수
- 경쟁사(Qualcomm Hexagon) 온디바이스 LoRA 학습 로드맵

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Korea Herald — AI soulmate? KAIST builds hyper-personalized AI chip | [링크](https://www.koreaherald.com/article/10696201) | news | 2026-03-17 | [B] |
| <a id="ref-g-02"></a>G-02 | Mirage News — World's 1st SoulMate AI Chip: Personalized Digital Soulmate | [링크](https://www.miragenews.com/worlds-1st-soulmate-ai-chip-personalized-1638207/) | news | 2026-03-17 | [B] |
| <a id="ref-g-03"></a>G-03 | Seoul Economic Daily (EN) — KAIST Develops World's First Hyper-Personalized On-Device AI Chip | [링크](https://en.sedaily.com/technology/2026/03/17/kaist-develops-worlds-first-hyper-personalized-on-device-ai) | news | 2026-03-17 | [B] |
| <a id="ref-g-04"></a>G-04 | TechXplore — SoulMate LLM accelerator evolves according to the specific characteristics of the user | [링크](https://techxplore.com/news/2026-03-soulmate-llm-evolves-specific-characteristics.html) | news | 2026-03-17 | [B] |
| <a id="ref-g-05"></a>G-05 | AI타임스 — 유회준 KAIST 교수, ISSCC 반도체 설계 최고 권위자로 선정 | [링크](https://www.aitimes.com/news/articleView.html?idxno=149726) | news | 2023-03-01 | [B] |
| <a id="ref-g-06"></a>G-06 | IEEE ComSoc Tech Blog — Korea's KAIST develops next-gen ultra-low power GenAI LLM accelerator | [링크](https://techblog.comsoc.org/2024/03/07/koreas-kaist-develops-next-generation-ultra-low-power-genai-llm-accelerator/) | news | 2024-03-07 | [B] |
| <a id="ref-g-07"></a>G-07 | Herald Economy — "사용자 말투·감정까지 학습" KAIST, AI 반도체 '소울메이트' 개발 | [링크](https://biz.heraldcorp.com/article/10695690) | news | 2026-03-17 | [B] |
| <a id="ref-g-08"></a>G-08 | Qualcomm 공식 — Snapdragon 8 Elite Gen 5 Mobile Platform | [링크](https://www.qualcomm.com/smartphones/products/8-series/snapdragon-8-elite-gen-5) | IR/발표 | 2026-02 | [A] |
| <a id="ref-g-09"></a>G-09 | TechCrunch — Apple announces its new A18 and A18 Pro iPhone chips | [링크](https://techcrunch.com/2024/09/09/apple-announces-its-new-a18-iphone-chip/) | news | 2024-09-09 | [B] |
| <a id="ref-g-10"></a>G-10 | Apple 공식 — Apple introduces M4 chip | [링크](https://www.apple.com/newsroom/2024/05/apple-introduces-m4-chip/) | IR/발표 | 2024-05 | [A] |
| <a id="ref-g-11"></a>G-11 | Google Blog — 5 reasons why Google Tensor G5 is a game-changer for Pixel | [링크](https://blog.google/products-and-platforms/devices/pixel/tensor-g5-pixel-10/) | IR/발표 | 2025 | [A] |
| <a id="ref-g-12"></a>G-12 | Samsung Semiconductor 공식 — Exynos 2600 Mobile Processor | [링크](https://semiconductor.samsung.com/processor/mobile-processor/exynos-2600/) | IR/발표 | 2025-12 | [A] |
| <a id="ref-g-13"></a>G-13 | GitHub — supertone-inc/supertonic: Lightning-Fast, On-Device, Multilingual TTS | [링크](https://github.com/supertone-inc/supertonic) | blog | 2025 | [B] |
| <a id="ref-g-14"></a>G-14 | 파이낸셜뉴스 — 구글과 손잡은 LG유플러스, '익시오 AI 비서' 공개 | [링크](https://www.fnnews.com/news/202511130946251383) | news | 2025-11-13 | [B] |
| <a id="ref-g-15"></a>G-15 | 아주경제 — LGU+, 엑사원 온디바이스 sLM 개발… '익시오' 적용 | [링크](https://www.ajunews.com/view/20250925094803994) | news | 2025-09-25 | [B] |
| <a id="ref-g-16"></a>G-16 | Fortune Business Insights — Emotion AI Market Size, Share | [링크](https://www.fortunebusinessinsights.com/emotion-ai-market-112136) | blog | 2025 | [C] |
| <a id="ref-g-17"></a>G-17 | Asia Business Daily (EN) — "Conversing and Connecting Like a Friend": KAIST Develops Personalized AI 'SoulMate' | [링크](https://www.asiae.co.kr/en/article/2026031708222374641) | news | 2026-03-17 | [B] |
| <a id="ref-g-18"></a>G-18 | TechBytes (Deep Dive) — KAIST SoulMate: The First Emotional AI Silicon | [링크](https://techbytes.app/posts/kaist-soulmate-emotional-ai-semiconductor-2026/) | blog | 2026-03 | [C] |
| <a id="ref-g-19"></a>G-19 | LG공식 보도자료 — LGU+, '엑사원 3.5' 경량화 온디바이스 sLM 개발 | [링크](https://www.lg.co.kr/media/release/29403) | IR/발표 | 2025-09-25 | [A] |
| <a id="ref-g-20"></a>G-20 | TrendForce — Samsung Unveils Exynos 2600: Industry-First 2nm GAA AP | [링크](https://www.trendforce.com/news/2025/12/19/news-samsung-officially-unveils-exynos-2600-industry-first-2nm-gaa-ap-with-113-ai-performance-uplift) | news | 2025-12-19 | [B] |
| <a id="ref-g-21"></a>G-21 | Qualcomm 공식 보도자료 — Qualcomm Unveils the Snapdragon 8 Elite Gen 5 for Galaxy | [링크](https://www.qualcomm.com/news/releases/2026/02/qualcomm-unveils-the-snapdragon-8-elite-gen-5-for-galaxy--drivin) | IR/발표 | 2026-02 | [A] |
| <a id="ref-g-22"></a>G-22 | Apple ML Research — Apple Intelligence Foundation Models 2025 | [링크](https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025) | paper | 2025 | [A] |
| <a id="ref-g-23"></a>G-23 | Fortune Business Insights — AI Companion Market Growth 2026-2034 | [링크](https://www.fortunebusinessinsights.com/ai-companion-market-113258) | blog | 2025 | [C] |
| <a id="ref-g-24"></a>G-24 | 전자신문 — 유회준 KAIST 교수, 'ISSCC 반도체' 설계 최고 권위자로 선정...동양인 유일 톱5 '등극' | [링크](https://www.etnews.com/20230301000100) | news | 2023-03-01 | [B] |
