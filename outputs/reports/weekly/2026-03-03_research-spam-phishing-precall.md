---
topic: 스팸/피싱 사전 탐지 (Pre-call Spam/Phishing Detection)
date: 2026-03-03
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
mcp_unavailable: [research-hub, patent-intel, trend-tracker]
---

# Research Report: 스팸·피싱 사전 탐지 기술 동향 (Pre-call Spam/Phishing Detection)

## Executive Summary (경영진 요약)

> 2026년 2월을 기점으로 한국 이통3사(SKT·KT·LGU+)와 삼성전자가 온디바이스 AI 기반 보이스피싱 탐지 서비스를 공동 출시하며 기술 경쟁이 본격화됐다. LGU+는 세계 최초 상용 안티딥보이스(탐지 정확도 98%)로 출시 1개월 만에 5,500건 탐지·2,900억원 피해 예방을 주장했고, KT는 97.2% 정확도(2025 Q4), SKT는 연간 11억 건 차단(YoY +35%)을 발표했다. 글로벌 측면에서는 Galaxy S26에 Google Gemini Nano 기반 Scam Detection이 탑재(2026-02-25)됐으며, Hiya의 "State of the Call 2026" 보고서는 미국인 4명 중 1명이 AI 딥페이크 음성 통화를 수신했다고 집계했다. 한국 보이스피싱 피해액은 2025년 1~10월 누적 1조 566억 원으로 사상 첫 1조 원 돌파가 확인됐다. 학술계에서는 실시간 초단기 입력(0.5~2초) 딥페이크 탐지·멀티모달 탐지·텔레콤 사기 데이터셋 구축이 2025~2026년 집중 연구 영역으로 부상했다. 전반적 신뢰도: 높음 (국내 공식 발표 및 복수 언론 교차 확인 완료).

---

## 연구 질문

> 2026년 초 기준, 스팸·보이스피싱 통화 사전/실시간 탐지 기술의 최신 현황은 무엇인가? 국내외 주요 플레이어(통신사, 단말 제조사, 글로벌 앱)의 기술 스펙, 성과 수치, 정부 규제 동향, 학술·특허 연구 흐름을 종합하라.

---

## 1. 기술 현황

### 1.1 기술 성숙도 (TRL)
- **전반적 TRL: 8~9** — 주요 국내 서비스는 이미 상용 배포 완료 단계
- 핵심 기반 기술: 온디바이스 AI 추론, 딥페이크 오디오 탐지, 화자 인식(Speaker Verification), 자연어 처리(NLP) 기반 스크립트 분석
- **신규 도전 영역**: 초단기 입력(0.5~2.0초) 에서의 딥페이크 탐지, 실시간 스트리밍 상황에서 엣지 추론 → TRL 5~6

### 1.2 주요 기술 요소

| 기술 요소 | 설명 | 국내 적용 사례 |
|-----------|------|---------------|
| On-Device AI 추론 | 외부 서버 비전송, 단말 내 처리 | Samsung·SKT·KT·LGU+ 전 서비스 |
| 딥페이크(Anti-DeepVoice) 탐지 | 합성·변조 음성 판별 | LGU+ 익시오 (98% 정확도, 5초 내 탐지) |
| 대화 패턴 분석 (NLP/LLM) | 보이스피싱 스크립트 키워드·문맥 분석 | SKT 에이닷 전화, KT 후후, Samsung 갤럭시 전화 |
| 화자 인식 (Speaker ID) | 신고된 범죄자 성문과 비교 | LGU+ 익시오 '범죄자 목소리 탐지', KT 후후 2.0 |
| 딥보이스 탐지 (KT) | 딥페이크 음성 여부 별도 판별 | KT '후후 AI 보이스피싱 탐지 서비스 2.0' |
| Gemini Nano 추론 | Google의 온디바이스 LLM 기반 통화 패턴 탐지 | Galaxy S26 (미국, 영어 전용) |
| RAG 기반 실시간 탐지 | 외부 지식베이스 검색 + LLM 추론 결합 | 학술 단계 (arXiv 2501.15290, F1 97.44%) |

### 1.3 탐지 방식 비교
- **사전 탐지 (Pre-call)**: 번호 DB 비교, 스팸 신고 이력 매칭 → KT 후후, Truecaller 방식
- **실시간 탐지 (In-call)**: 통화 오디오 실시간 분석 → 국내 이통3사·삼성 공동 출시 서비스의 핵심 차별점
- **빠른 초기 탐지 (First-greeting)**: 통화 시작 0.5~2초 내 딥페이크 판별 → ICASSP 2026 Short-MGAA 논문 대상 [P-01]

---

## 2. 시장 동향

### 2.1 한국 보이스피싱 피해 규모 [N-01][N-02]

| 지표 | 수치 | 기준 |
|------|------|------|
| 2025년 1~10월 누적 피해액 | **1조 566억 원** | 1만 9,972건 (경찰청) |
| 전년 동기 대비 증가율 | **+73.8%** | 2024년 1~10월 대비 |
| 2025년 1분기 피해액 | 3,116억 원 | 건수 5,878건 |
| 1분기 피해액 YoY 증가 | **+2.2배** | 2024년 1분기 대비 |
| 건당 평균 피해액 | **5,290만 원** | 전년 2,498만 원 대비 약 2배 |
| 기관사칭형 비중 | 약 77% | 전체 피해액 기준 |

### 2.2 글로벌 딥페이크 음성 위협 규모 [G-01]
- 미국인 1/4이 지난 12개월 내 AI 딥페이크 음성 통화 수신 경험 (Hiya, 12,000명 이상 설문)
- 추가 24%는 진짜와 딥페이크 구분 불가 → 사실상 미국 인구 절반이 노출·취약
- 미 소비자: 통신사 vs. 스캐머 싸움에서 스캐머 우세 **2:1** 비율로 응답
- 55세 이상 시니어 1건당 평균 피해 **$1,298** (젊은 층 대비 3배)
- 38%: 보이스피싱 무방비 시 이동통신사 교체 의향
- 글로벌 통신 사기 손실 2025년 피크 추정 **$45B** (Subex 예측) [G-02]

### 2.3 기술 위협 수준 상승 [G-03]
- 보이스 클로닝이 '식별 불가 임계점(indistinguishable threshold)'을 넘어섰다는 연구자 경고 (Fortune, 2025-12-27)
- Queen Mary University of London 연구: AI 생성 음성이 인간 녹음과 동등 수준의 사실성 달성, 평균 청취자 구분 불가
- McAfee 연구: 단 3초 오디오로 85% 정확도 보이스 클론 생성 가능
- 일부 대형 소매업체: AI 생성 스캠 콜 **하루 1,000건 이상** 수신 보고

---

## 3. 경쟁사 동향

### 3.1 국내 통신사

**SKT (에이닷 전화)**
- 2025년 연간 통신사기 시도 **11억 건 차단** (음성 스팸·피싱 2.5억 건 포함) [E-01]
- 음성 스팸·피싱 차단: YoY **+119%** / 문자 스팸: +22%
- 탐지 방식: 의심 키워드, 대화 패턴 종합 분석 → '의심'/'위험' 2단계 알림
- 경찰청 긴급차단 제도(10분 내 번호 이용정지) 공동 참여

**KT (후후)**
- 2025년 연간 **약 1,300억 원** 피해 예방 추산 [E-02]
- 탐지 정확도: 2025 Q1 90.3% → Q4 **97.2%** (지속 고도화)
- 2025년 상반기: 1,460만 건 통화 분석, 91.6% 정확도, 710억 원 피해 예방
- 'AI 보이스피싱 탐지 서비스 2.0': 화자 인식 + 딥보이스 탐지 통합 (2025-07 출시) [E-03]
- 은행연합회 MOU → 탐지 데이터 금융기관 제공, 계좌 이상 모니터링 연계
- 4,680만 건 이상 통화 트래픽 중 3,000여 건 보이스피싱 예방 (2025년 기준)
- 안드로이드 전용, 통신사 무관 이용 가능

**LGU+ (익시오 ixi-O)**
- 세계 최초 온디바이스 **'안티딥보이스'** 상용화 (2025-06 말 출시) [E-04]
- 출시 1개월 만에 위변조 음성 **5,500건 탐지**, 약 **2,900억 원** 피해 예방 추산
- 합성 음성 탐지 정확도 **98%**, 통화 시작 후 **5초** 내 위변조 판별
- 추가 기능: '범죄자 목소리 탐지' — 신고된 피싱범 성문과 실시간 대조
- 개인정보보호위원회·국립과학수사연구원 협업
- KB국민은행 연동: 보이스피싱 패턴 탐지 → 이상 거래 추적 → 계좌 지급정지
- MWC 2026: 홍범식 CEO 기조연설 — "익시오로 통신 미래 열겠다" [E-05]
- '익시오 프로' 공개, AI 시대 핵심 인터페이스는 '음성' 강조

### 3.2 글로벌 단말 제조사

**Samsung (갤럭시 전화 앱)**
- One UI 8 기반, 경찰청·국립과학수사연구원 제공 보이스피싱 데이터 약 3만 개로 딥러닝 학습 [E-06]
- 알림 2단계: '의심(노란색, 보이스피싱 의심)' / '경고(빨간색, 보이스피싱 감지)'
- 한국 전용 서비스 (Galaxy 전 모델, 타 통신사 무관)
- Galaxy S26 (2026): Google Scam Detection (Gemini Nano) 추가 탑재 [G-04]

**Google (Galaxy S26 Scam Detection)**
- 발표일: 2026-02-25 (Samsung Unpacked 행사)
- Gemini Nano 완전 온디바이스 처리, 오디오·통화 내용 외부 전송 없음
- 미국 영어 전용, 연락처 저장된 번호 제외
- Pixel 독점 기능이었던 Scam Detection을 Samsung S26으로 최초 확장

### 3.3 글로벌 앱/플랫폼

**Hiya**
- "State of the Call 2026" 보고서 발행 (2026-03-02) [G-01]
- 6개국 12,000명 이상 소비자 설문 기반
- 550+ million 월간 사용자 플랫폼
- 핵심 주장: "통신 인프라에 AI를 직접 내장해 통화 전 인증(pre-ring authentication)해야"

**Truecaller**
- 전 세계 450M 사용자, 일 6,300만 건 스팸 탐지 [G-05]
- AI Call Scanner: 통화 중 음성 실시간 분석, AI 생성 목소리 구분
- Family Protection: 최대 5명 가족 공유 스팸 차단 설정 (2026 Q1 인도 출시)
- 166M 스팸 신고/일 (커뮤니티 기반)

---

## 4. 제품/서비스 스펙 비교

| 기업 | 서비스명 | 핵심 기술 | 탐지 정확도 | 처리 방식 | 추가 기능 | 출시 시점 | 출처 |
|------|---------|----------|------------|----------|----------|---------|------|
| SKT | 에이닷 전화 | 키워드·패턴 분석 온디바이스 | 공개 정보 없음 | On-Device | 2단계 경보 | 2025 | [E-01] |
| KT | 후후 (AI 보이스피싱 탐지 2.0) | 문맥탐지 + 화자인식 + 딥보이스 탐지 | **97.2%** (2025 Q4) | On-Device | 은행연합회 데이터 연계 | 2025-07 | [E-02][E-03] |
| LGU+ | 익시오 (ixi-O) | 안티딥보이스 + 범죄자 목소리 탐지 | **98%** (합성음성) | On-Device | 5초 내 탐지, KB국민은행 연동 | 2025-06 말 | [E-04] |
| Samsung | 갤럭시 전화 앱 (One UI 8) | 딥러닝 (경찰청·국과수 데이터) | 공개 정보 없음 | On-Device | 2단계 시각+청각 경보 | 2025 | [E-06] |
| Samsung | Galaxy S26 + Google Scam Detection | Gemini Nano LLM | 공개 정보 없음 | On-Device | 오디오+햅틱 실시간 경보 | 2026-02-25 | [G-04] |
| Truecaller | AI Call Scanner | AI 음성 분석 모델 | 공개 정보 없음 | 서버 처리 | 450M 사용자 크라우드소스 DB | 2024 | [G-05] |
| Hiya | Hiya Protect | 네트워크 레벨 AI 탐지 | 공개 정보 없음 | 통신 인프라 내장 | 550M 사용자, 통신사 파트너십 | 서비스 중 | [G-01] |

---

## 5. 학술 동향

### 5.1 최근 주요 논문 (2025~2026)

**[P-01] Short-MGAA — 초단기 입력 딥페이크 탐지 (ICASSP 2026)**
- 제목: "Audio Deepfake Detection at the First Greeting: 'Hi!'"
- 저자: Haohan Shi, Xiyu Shi, Safak Dogan, Tianjin Huang, Yunxiao Zhang
- 제출: 2026-01-27, ICASSP 2026 채택
- 핵심: 0.5~2.0초 초단기 오디오에서 딥페이크 탐지 가능한 경량 모델 Short-MGAA
- 성과: 9개 SOTA 베이스라인 초과, 엣지 디바이스 배포에 적합한 저연산 설계
- 의의: 실통화 시나리오(첫인사 직후)에서 즉각 탐지 가능성 제시

**[P-02] TeleAntiFraud-28k — 텔레콤 사기 멀티모달 데이터셋 (2025)**
- 제목: "TeleAntiFraud-28k: An Audio-Text Slow-Thinking Dataset for Telecom Fraud Detection"
- 저자: Zhiming Ma, Peidong Wang et al. (10명)
- arXiv: 2503.24115 (2025-03-31 제출, 2025-08-18 최종 업데이트)
- 핵심: 28,511개 음성-텍스트 쌍, 3가지 태스크 (시나리오 분류·사기 탐지·사기 유형 분류)
- 데이터 구성: 실제 통화 녹취 ASR 변환 + LLM 기반 의미 증강 + 멀티 에이전트 적대적 합성
- 오픈소스 데이터셋 최초 공개 예정

**[P-03] 멀티모달 보이스피싱 탐지 시스템 (MDPI Applied Sciences, 2025-10)**
- 제목: "A Multimodal Voice Phishing Detection System Integrating Text and Audio Analysis"
- 학술지: MDPI Applied Sciences, 2025-10-18
- 구성: KoBERT 기반 텍스트 분류기 + MFCC+CNN-BiLSTM 오디오 분류기
- 최적 성과: 가중 퓨전(텍스트 8 : 오디오 2) → **F1-score 0.994**
- 데이터: 실제 통화 기록 + 보이스피싱 데이터셋 + 합성 음성 코퍼스

**[P-04] VoiceRadar — 마이크로 주파수 딥페이크 탐지 (NDSS 2025)**
- 제목: "VoiceRadar: Voice Deepfake Detection using Micro-Frequency and Compositional Analysis"
- 컨퍼런스: NDSS 2025, Distinguished Paper Award 수상
- 소속: TU Darmstadt, KOBIL
- 성능: Voice Conversion 탐지 F1-score **0.99**, EER **0.45** (TTS), TPR **99.88%** (VC)
- 방식: 레이더 물리 모델에서 착안한 마이크로 주파수 진동 + 구성적 분석
- 상용화: KOBIL·TU Darmstadt 공동으로 AI VoiceRadar 제품 출시

**[P-05] AUDETER 데이터셋 (2025-09)**
- 제목: "AUDETER: A Large-scale Dataset for Deepfake Audio Detection in Open Worlds"
- arXiv: 2509.04345
- 규모: 4,500시간 이상 합성 오디오, TTS 모델 11종 생성
- 성과: AUDETER 학습 XLS-R 기반 탐지기 → In-the-Wild 벤치마크 **EER 1.87%** 달성
- 기여: 도메인 시프트 문제 해결을 위한 커리큘럼 러닝 기반 접근법 제안

**[P-06] RAG 기반 실시간 사기 탐지 (2025-01)**
- 제목: "Advanced Real-Time Fraud Detection Using RAG-Based LLMs"
- arXiv: 2501.15290
- 성과: 정확도 **97.98%**, F1-score **97.44%**
- 방식: 외부 지식베이스 + LLM 추론 실시간 결합

**[P-07] ScamAgents — AI 에이전트 스캠 콜 자동화 (2025-08)**
- 제목: "ScamAgents: How AI Agents Can Simulate Human-Level Scam Calls"
- arXiv: 2508.06457, CAMLIS 2025 채택
- 내용: LLM 기반 자율 멀티턴 에이전트가 사기 스크립트 + TTS로 완전 자동화 피싱 파이프라인 구현
- 시사: 공격 자동화 기술 연구로서 방어 시스템 고도화 필요성 입증

**[P-08] VoiceWukong 벤치마크 (USENIX Security 2025)**
- 제목: "VoiceWukong: Benchmarking Deepfake Voice Detection"
- 규모: 34개 방법론 × 6,800 영어 딥페이크 음성 / 19개 방법론 × 3,800 중국어 딥페이크 음성
- 기여: 다국어 딥페이크 음성 탐지 표준 벤치마크 확립

### 5.2 연구 방향 요약

1. **초단기 실시간 탐지**: 통화 개시 0.5~2초 내 딥페이크 판별 (경량 모델, 엣지 배포)
2. **멀티모달 융합**: 텍스트(NLP/LLM) + 오디오(음향 특징) 결합 → 단일 모달 대비 F1 향상
3. **오픈월드 강건성**: 학습-배포 도메인 시프트 극복, In-the-Wild 성능 보장
4. **공격 시뮬레이션**: ScamAgents 방식 — 방어 시스템 평가용 적대적 사례 자동 생성
5. **한국어 특화**: KoBERT 기반 한국어 보이스피싱 탐지, 실제 한국 통화 데이터셋 활용

---

## 6. 특허 동향

### 6.1 주요 등록·출원 특허

**[T-01] US11423926B2 — Real-time voice phishing detection (Google)**
- 출원인: Google LLC
- 등록일: 2022-08-23
- PCT: WO2021126444A1
- 핵심 청구항: (1) 딥스캐터링 스펙트럼(DSS) + 시프트델타 켑스트라(SDC) 특징 기반 음성 변조 탐지 (2) 내용 탐지기 — 보이스피싱 관련 발화 내용 모니터링 (3) 스푸핑 탐지 — 화자 생체인식 프로파일 비교
- 관할: 미국 USPTO

**[T-02] US12380896B1 — Audio speech signal analysis for fraud detection (Morgan Stanley)**
- 출원인: Morgan Stanley Services Group Inc
- 출원일: 2025-04-30 (등록)
- 핵심 청구항: 콘택트센터 실시간 통화 오디오 사기 탐지; 포그라운드/백그라운드 오디오 분리; 앙상블 모델 (화자 오디오 모델 + 화자 의도 모델 + 합성 음성 탐지 모델 + 운율 모델) 복합 적용
- 관할: 미국 USPTO

**[T-03] 딥브레인AI — 딥러닝 기반 딥보이스 탐지 기술 특허 (한국)**
- 출원인: 딥브레인AI (DeepBrain AI Inc)
- 출원 발표: 2024-02-05
- 핵심 청구항: MFCC 한계 극복 — 고주파 영역 음성 특징 추출 강화; 정보 추출 모델 + 위변조 판별 모델 통합 딥러닝; SaaS형 딥페이크 탐지 솔루션 적용
- 관할: 한국 (KIPO 출원)
- 비고: 특허 번호는 공개 정보 없음

### 6.2 특허 트렌드 관찰
- 딥페이크 음성 대응 특허가 2024~2025년 급증 추세 (단일 소스, 정량 데이터 없음) [D]
- 미국 측 주요 출원인: Google (방어 기술), Morgan Stanley (금융 콘택트센터 특화)
- 한국 측: 딥브레인AI 등 AI 전문기업, 통신사 특허 출원은 공개 정보 없음
- 기술 분화: 음성 변조 탐지 ↔ 통화 내용 분석 ↔ 화자 인증 — 세 축이 독립 특허 영역으로 형성

---

## 7. 기업 발언 & 보도자료

### E-01 SKT — 연간 11억 건 차단 발표
> "SK텔레콤은 2025년 한 해 동안 음성 스팸·보이스피싱 통화, 문자 등 각종 통신 사기 시도 약 11억 건을 선제적으로 차단했으며, 이는 전년 대비 35% 증가한 수치"
- 출처: SKT 뉴스룸 / 서울경제 보도 (2026-01-13)
- 신뢰도: [A] 기업 공식 발표

### E-02 KT — 1,300억원 피해예방 발표
> "KT가 지난 1월 상용화한 실시간 AI 보이스피싱 탐지 서비스를 통해 2025년 약 1,300억 원 규모의 보이스피싱 피해를 예방한 것으로 나타났습니다"
- 출처: 전자신문 (2025-12-23)
- 신뢰도: [B] 주요 IT 전문지, 기업 주장

### E-03 KT — AI 보이스피싱 탐지 2.0 출시 발표
> "국내 최초로 화자 인식과 AI 변조 음성인 '딥보이스' 탐지 기능을 통합한 실시간 'AI 보이스피싱 탐지서비스 2.0'을 상용화"
- 출처: KT 공식 보도자료 (corp.kt.com) / 디지털투데이 (2025-07-29)
- 신뢰도: [A] 기업 공식 보도자료

### E-04 LGU+ — 안티딥보이스 5,500건 탐지 발표
> "LG유플러스가 세계 최초로 상용화한 온디바이스 AI 기반 '안티딥보이스(Anti-DeepVoice)' 기술이 한 달 만에 5,500여 건의 피싱 시도를 탐지했다. 일평균 183건에 달하는 수치로, 1건당 평균 피해 금액 5,300만 원 기준 약 2,900억 원 피해 예방 효과"
- 출처: LG그룹 공식 보도자료 (lg.co.kr) / 복수 언론 확인
- 신뢰도: [A] 기업 공식 보도자료

### E-05 LGU+ 홍범식 CEO — MWC 2026 기조연설
> "익시오(ixi-O)를 통해 통신의 미래를 열겠다. AI 시대에도 가장 본질적인 인터페이스는 '음성'이다"
- 출처: 겟뉴스 / EBN (2026-03-02, 바르셀로나)
- 신뢰도: [B] 복수 언론 현장 보도

### E-06 Samsung — 경찰청·국과수 데이터 기반 학습 발표
> "삼성전자는 경찰청과 국립과학수사연구원에서 2024년부터 제공된 보이스피싱 데이터 약 3만 개를 기반으로 딥러닝 학습을 거쳐, 기기 내(On-Device) AI 기술로 보이스피싱 여부를 탐지하는 솔루션을 개발"
- 출처: 삼성전자 뉴스룸 (news.samsung.com/kr)
- 신뢰도: [A] 기업 공식 발표

### E-07 과기정통부 — 삼성·이통3사 보이스피싱 탐지 이용 권고 (2026-02-12)
> "과학기술정보통신부는 2026년 2월 12일 보이스피싱 피해 방지를 위해 삼성전자, 이동통신 3사(SKT·KT·LGU+)가 제공하는 인공지능 기반 보이스피싱 탐지·알림 서비스를 이용해 주기를 바란다"
- 출처: 대한민국 정책브리핑 (korea.kr) — 공식 정부 채널
- 신뢰도: [A] 정부 공식 발표

### E-08 Google — Galaxy S26 Scam Detection 프라이버시 선언
> "Call audio is processed ephemerally — no conversation audio or transcription is recorded, stored on the device, or sent to Google or third parties. Because the analysis is on-device via Gemini Nano, alerts can appear quickly without sending call audio to external servers."
- 출처: Google 공식 블로그 (blog.google, 2026-02-25)
- 신뢰도: [A] 기업 공식 발표

---

## 8. 한국 규제 및 정책 동향

### 8.1 경찰청 긴급차단 제도 [N-03]
- **시행일**: 2024-11-24
- **내용**: 보이스피싱 범죄 이용 전화번호를 **10분 내** 이용정지 (기존 2일 이상 → 10분)
- **참여**: 경찰청, SKT·KT·LGU+, 삼성전자
- **신고 채널**: 삼성 '간편제보' 기능 (2024-12 적용) + www.counterscam112.go.kr

### 8.2 AI 민생 10대 프로젝트 [N-04]
- 과기정통부 주도, 보이스피싱 차단 포함
- 2026~2027년 'AI 기반 보이스피싱 통신서비스 공동 대응 플랫폼' 구축 사업
- 경찰청·KISA 등 유관기관 + 이통3사·삼성전자 참여
- 예산: 4개 과제 각 100억 원(2년) / 기타 과제 30억 원(2년)
- 보이스피싱 R&D 민·관 협의체 출범 (과기정통부, IITP, 개인정보보호위, 경찰청, 국과수, 통신3사, ETRI, KAIST 참여)

### 8.3 금융위원회 ASAP 플랫폼 [N-05]
- 발표: 2025-10-29
- 'AI 보이스피싱 정보공유·분석 플랫폼(ASAP)' 출범
- 130개 금융회사 참여, 9개 유형 90개 항목 정보 실시간 공유

### 8.4 대량문자 전송자격인증제 [N-06]
- 시행: 2024-06-01 (자율규제)
- 2026년: 법적 의무화 법안 상임위 통과 (법제화 임박)
- 불법 스팸 방지 역량 갖춘 사업자만 시장 진입 허용

### 8.5 KISA 조직 개편 [N-07]
- 2026-02-09: 'AI보안산업본부' + '디지털위협예방본부' 신설
- 'AI 기반 보이스피싱 차세대 보안 제품 상용화 지원(Type2)' 사업 공고 (2026-02-13)

---

## 전략적 시사점

**핵심 관찰 사항 (사실 기반)**

1. **국내 서비스 차별화 축**: KT는 정확도(97.2%)와 피해 예방 규모(1,300억 원), LGU+는 세계 최초 딥보이스 탐지 + 빠른 응답(5초), SKT는 커버리지(11억 건 차단)로 각각 경쟁 포인트를 다르게 설정하고 있음
2. **생태계 연계**: LGU+-KB국민은행, KT-은행연합회 등 금융권 연동이 단순 탐지를 넘어 계좌 차단까지 확장되는 추세
3. **글로벌 vs. 한국 갭**: Google/Samsung Galaxy S26은 미국·영어 전용; 한국 서비스는 한국어 특화·온디바이스 처리로 글로벌 솔루션 대비 앞선 출시 타이밍
4. **정부-산업 협력 구조화**: 경찰청 긴급차단 + 과기정통부 공동플랫폼 + KISA 조직 개편 + ASAP으로 다층적 공공 인프라 구축 중
5. **위협 기술 진화 속도**: 보이스 클로닝 '식별 불가 임계점' 도달, 스캠 콜 AI 자동화(ScamAgents) 논문 발표 — 방어 기술 대응 속도가 관건

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- SKT 11억 건 차단 수치 (기업 공식 발표 + 복수 언론 확인)
- KT 97.2% 정확도, 1,300억 원 예방 (기업 공식 + 전문지 보도)
- LGU+ 안티딥보이스 5,500건·2,900억 원 (기업 공식 보도자료)
- 과기정통부 공동 출시 발표 2026-02-12 (정부 공식 채널)
- Google Gemini Nano Galaxy S26 탑재 (Google 공식 블로그)
- 보이스피싱 1조 566억 원 (경찰청 통계 기반 복수 언론 보도)
- 학술 논문 P-01~P-08 (arXiv, NDSS, MDPI 등 검증된 채널)

**추가 검증 필요 [C/D]:**
- LGU+ "세계 최초" 안티딥보이스 주장 (경쟁사 반박 없으나 독립 검증 없음) [C]
- Truecaller AI Call Scanner 탐지 정확도 (공개된 독립 벤치마크 없음) [C]
- Morgan Stanley 특허 US12380896B1 등록 여부 (검색 결과 미확인) [C]
- 글로벌 통신 사기 손실 $45B 예측 (단일 분석사 추정) [C]
- 딥브레인AI 특허 출원 번호 미공개 (2024-02 발표, 등록 여부 미확인) [C]

**데이터 공백:**
- LGU+ 익시오 전체 가입자 수 (목표 3년 내 600만 언급, 현재 수치 없음)
- KT 후후 탐지 서비스 이용자 수
- MCP 소스(research-hub, patent-intel, trend-tracker) 미접속 — 학술 논문 인용수, 특허 등록 번호 일부 미확인

---

## References

### 글로벌 출처 (G-xx)

| 번호 | 출처명 | 발행일 | 기관유형 | 제목 | 인용원문(한글) | 관련성 | 신뢰성 | 최신성 | URL |
|------|--------|-------|----------|------|-------------|--------|--------|--------|-----|
| G-01 | Hiya / Web and IT News | 2026-03-02 | 기업 리서치 리포트 | State of the Call 2026: AI Deepfake Voice Calls Hit 1 in 4 Americans | 미국인 4명 중 1명 딥페이크 음성 통화 수신, 스캐머가 통신사보다 우세 2:1 | 5 | 4 | 5 | https://www.webanditnews.com/2026/03/02/state-of-the-call-2026-ai-deepfake-voice-calls-hit-1-in-4-americans-as-consumers-say-scammers-are-beating-mobile-network-operators-2-to-1/ |
| G-02 | Subex / telecoms.com | 2025 | 산업분석 | Top Telecom Fraud Trends in 2025 | 글로벌 통신 사기 손실 2025년 $45B 피크 후 2028년 $36B으로 감소 전망 | 3 | 3 | 4 | https://www.subex.com/blog/top-telecom-fraud-trends-in-2025-evolving-threats-solutions/ |
| G-03 | Fortune / QMUL | 2025-12-27 | 주요 언론 + 대학 연구 | Voice cloning has crossed the 'indistinguishable threshold' | 보이스 클로닝 '식별 불가 임계점' 도달, 3초 오디오로 85% 정확도 클론 생성 가능 | 5 | 4 | 5 | https://fortune.com/2025/12/27/2026-deepfakes-outlook-forecast/ |
| G-04 | Google Blog / Android Authority | 2026-02-25 | 기업 공식 블로그 | Scam Detection comes to Samsung Galaxy S26 (Gemini Nano) | Galaxy S26에 Gemini Nano 온디바이스 Scam Detection 탑재, 완전 로컬 처리 | 5 | 5 | 5 | https://9to5google.com/2026/02/25/google-messages-scam-detection-gemini/ |
| G-05 | Truecaller / TechCrunch | 2024~2026 | 기업 발표 + IT 전문지 | Truecaller AI Call Scanner & Family Protection | 일 6,300만 건 스팸 탐지, 450M 사용자, AI 음성 실시간 분석 | 4 | 4 | 4 | https://techcrunch.com/2024/03/18/truecaller-automatically-reject-all-spam-calls-android-update/ |
| G-06 | Android Authority / SammyFans | 2026-02-25 | IT 전문지 | Google's Scam Detection is now on the Galaxy S26 | Pixel 전용 기능이었던 Scam Detection의 삼성 S26 최초 확장 | 5 | 4 | 5 | https://www.androidauthority.com/google-scam-detection-samsung-galaxy-s26-3643942/ |
| G-07 | Android Police | 2025 | IT 전문지 | Samsung Galaxy phones get on-device AI voice phishing detection in Korea | 삼성 갤럭시 한국 전용 온디바이스 보이스피싱 탐지, 경찰청·국과수 데이터 학습 | 5 | 4 | 5 | https://www.androidpolice.com/samsung-ai-voice-phishing-scam-detection/ |
| G-08 | Hiya Blog | 2025 | 기업 블로그 | 1 in 4 calls reviewed by Hiya contain AI-generated audio | Hiya 검토 통화의 1/4이 AI 생성 오디오 포함 | 4 | 4 | 5 | https://blog.hiya.com/1-in-4-calls-reviewed-by-hiya-contain-ai-generated-audio |
| G-09 | KOBIL / Morningstar | 2025 | 기업 보도자료 | KOBIL and TU Darmstadt Launch AI VoiceRadar Against Fraud | KOBIL-TU Darmstadt AI VoiceRadar 상용화, NDSS 2025 우수논문상 기반 | 4 | 4 | 4 | https://www.morningstar.com/news/accesswire/1015567msn/kobil-and-tu-darmstadt-launch-ai-voiceradar-against-fraud |

### 최신 동향 (N-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약(한글) | URL |
|------|--------|-------|------|-----------|----------|-----|
| N-01 | 뉴시스 / 한국경제 | 2025-11-24 | 보이스피싱 연간 피해액 1조 돌파 | 보이스피싱 피해액 2025 경찰청 | 2025년 1~10월 누적 피해액 1조566억원, 건당 평균 5290만원 | https://www.newsis.com/view/NISX20251124_0003414755 |
| N-02 | 세계일보 | 2025-04-27 | 2025년 1분기 보이스피싱 피해액 3,116억원 | 보이스피싱 피해액 2025 | 1분기 피해액 2.2배 급증, 건수 5,878건 | https://www.segye.com/newsView/20250427507459 |
| N-03 | 대한민국 정책브리핑 | 2024-11-24 | 보이스피싱 전화번호 10분 내 차단 긴급차단 제도 시행 | 경찰청 긴급차단제도 | 범죄 이용 전화번호 기존 2일→10분 내 이용정지, 경찰청·이통3사·삼성 협력 | https://www.korea.kr/news/policyNewsView.do?newsId=148955189 |
| N-04 | 서울경제 / 파이낸셜뉴스 | 2025-11 | AI 민생 10대 프로젝트: 보이스피싱 차단 포함 | AI 민생 10대 프로젝트 과기정통부 | 보이스피싱 AI 탐지 고도화 포함, 2026년 본격 지원 예산 배정 | https://www.sedaily.com/NewsView/2H0KUUTYHU |
| N-05 | 뉴시스 | 2025-10-29 | 보이스피싱 AI 정보공유 플랫폼 ASAP 출범 | KISA 보이스피싱 공동대응 | 금융위 주도, 130개 금융회사 참여, 9유형 90항목 실시간 공유 | https://www.newsis.com/view/NISX20251029_0003381419 |
| N-06 | 전자신문 | 2025-01-06 | 대량문자 전송자격인증제 법제화 임박 | 대량문자 전송자격인증제 스팸 규제 | 자율규제→법적 의무화 법안 상임위 통과 | https://www.etnews.com/20250106000276 |
| N-07 | 데일리시큐 | 2026-02-09 | KISA 조직개편: AI보안산업본부·디지털위협예방본부 신설 | KISA 조직개편 AI 보안 | AI 기반 사회 실현 국정과제 추진을 위한 조직 재편 | https://www.dailysecu.com/news/articleView.html?idxno=204896 |
| N-08 | 대한민국 정책브리핑 | 2026-02-12 | 인공지능으로 통화 중 보이스피싱 잡는다 | 보이스피싱 AI 탐지 삼성 이통3사 | 과기정통부 삼성·SKT·KT·LGU+ 공동 서비스 이용 권고 | https://www.korea.kr/news/policyNewsView.do?newsId=148959497 |
| N-09 | 아주경제 | 2026-03-01 | MWC 2026 LGU+ 홍범식 기조연설 | MWC 2026 LGU+ 익시오 홍범식 | 국내 통신사 CEO 유일 기조연설, 보이스 기반 AI 익시오 글로벌 제안 | https://www.ajunews.com/view/20260301194502115 |

### 기업 발언 (E-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약원문 |
|------|--------|-------|------|-----------|---------|
| E-01 | SKT 뉴스룸 / 서울경제 | 2026-01-13 | SKT, 2025년 통신사기 시도 11억건 차단 | SKT 에이닷 스팸차단 2025 | "2025년 11억 건 통신사기 시도 차단, 전년 대비 35% 증가. 음성 스팸·피싱 2.5억 건 (+119% YoY)" |
| E-02 | 전자신문 | 2025-12-23 | KT, AI 보이스피싱 탐지로 약 1,300억원 피해 예방 | KT AI 보이스피싱 탐지 1300억원 | "2025년 약 1,300억 원 피해 예방 추산, 탐지 정확도 Q1 90.3%→Q4 97.2%" |
| E-03 | KT 공식보도자료 / 디지털투데이 | 2025-07-29 | KT, AI 보이스피싱 탐지 서비스 2.0 출시 | KT 후후 보이스피싱 2.0 | "화자인식+딥보이스 탐지 통합. 목표: 연간 2,000억 원 이상 피해예방, 95% 이상 정확도" |
| E-04 | LG그룹 공식보도자료 | 2025 | 안티딥보이스, 한 달 만에 5,500건 탐지 | LGU+ 안티딥보이스 5500건 | "일평균 183건, 2,900억 원 피해예방 추산. 98% 탐지 정확도, 5초 내 위변조 판별" |
| E-05 | 겟뉴스 / EBN | 2026-03-02 | MWC26 홍범식 CEO 기조연설 | MWC 2026 LGU+ 홍범식 기조연설 | "익시오를 통해 통신 미래 열겠다. AI 시대 가장 본질적 인터페이스는 음성" |
| E-06 | 삼성전자 뉴스룸 | 2025 | 삼성 갤럭시, AI로 보이스피싱·스팸 차단 | 삼성전자 보이스피싱 탐지 | "경찰청·국과수 보이스피싱 데이터 3만 개 기반 딥러닝 학습, 의심/경고 2단계 알림" |
| E-07 | 대한민국 정책브리핑 | 2026-02-12 | 인공지능으로 통화 중 보이스피싱 잡는다 | 과기정통부 AI 보이스피싱 탐지 권고 | "모든 통화 내용 분석은 온디바이스 AI 기반. 2026~2027년 AI 기반 공동 대응 플랫폼 구축 계획" |
| E-08 | Google 공식 블로그 | 2026-02-25 | A more intelligent Android on Samsung Galaxy S26 | Google Scam Detection Galaxy S26 | "Scam Detection analysis happens entirely on device. No audio stored, no data sent to Google." |

### 학술 논문 (P-xx)

| 번호 | 저자 | 발행년도 | 제목 | 학술지/컨퍼런스 | 핵심 성과 | DOI/URL |
|------|------|---------|------|----------------|---------|---------|
| P-01 | Haohan Shi et al. | 2026 | Audio Deepfake Detection at the First Greeting: "Hi!" | ICASSP 2026 | Short-MGAA: 9개 SOTA 초과, 0.5~2.0초 입력, 엣지 배포 적합 | https://arxiv.org/abs/2601.19573 |
| P-02 | Zhiming Ma, Peidong Wang et al. | 2025 | TeleAntiFraud-28k: An Audio-Text Slow-Thinking Dataset for Telecom Fraud Detection | arXiv 2503.24115 | 28,511개 음성-텍스트 쌍, 최초 텔레콤 사기 오픈소스 멀티모달 데이터셋 | https://arxiv.org/abs/2503.24115 |
| P-03 | (MDPI Applied Sciences) | 2025-10 | A Multimodal Voice Phishing Detection System Integrating Text and Audio Analysis | MDPI Applied Sciences 15(20) | KoBERT+CNN-BiLSTM 가중 퓨전 F1-score 0.994 | https://www.mdpi.com/2076-3417/15/20/11170 |
| P-04 | (TU Darmstadt, KOBIL) | 2025 | VoiceRadar: Voice Deepfake Detection using Micro-Frequency and Compositional Analysis | NDSS 2025 (Distinguished Paper Award) | VC 탐지 F1 0.99, EER 0.45 (TTS), TPR 99.88% (VC) | https://www.ndss-symposium.org/ndss-paper/voiceradar-voice-deepfake-detection-using-micro-frequency-and-compositional-analysis/ |
| P-05 | (arXiv 2509.04345) | 2025-09 | AUDETER: A Large-scale Dataset for Deepfake Audio Detection in Open Worlds | arXiv 2509.04345 | 4,500시간+ 합성 오디오, XLS-R 학습 후 In-the-Wild EER 1.87% | https://arxiv.org/abs/2509.04345 |
| P-06 | (arXiv 2501.15290) | 2025-01 | Advanced Real-Time Fraud Detection Using RAG-Based LLMs | arXiv 2501.15290 | RAG+LLM 정확도 97.98%, F1 97.44% | https://arxiv.org/html/2501.15290v1 |
| P-07 | (arXiv 2508.06457) | 2025-08 | ScamAgents: How AI Agents Can Simulate Human-Level Scam Calls | CAMLIS 2025 | LLM+TTS 완전 자동화 피싱 파이프라인, 방어 시스템 평가 필요성 입증 | https://arxiv.org/html/2508.06457 |
| P-08 | (USENIX Security 2025) | 2025 | VoiceWukong: Benchmarking Deepfake Voice Detection | USENIX Security 2025 | 34개 방법론, 영어 6,800건/중국어 3,800건 딥페이크 표준 벤치마크 | https://www.usenix.org/system/files/usenixsecurity25-yan-ziwei.pdf |
| P-09 | (ESDD2/arXiv 2508.04529) | 2025-08 | ESDD 2026: Environmental Sound Deepfake Detection Challenge | ICME 2026 챌린지 | 환경음 포함 구성 요소 레벨 스푸핑 탐지 챌린지 | https://arxiv.org/abs/2508.04529 |

### 특허 (T-xx)

| 번호 | 출원인 | 등록/출원일 | 특허번호 | 제목 | 핵심 청구항 | 관할 |
|------|--------|-----------|---------|------|-----------|------|
| T-01 | Google LLC | 2022-08-23 (등록) | US11423926B2 | Real-time voice phishing detection | DSS+SDC 특징 기반 음성 변조 탐지, 통화 내용 모니터링, 화자 바이오메트릭 비교 | USPTO (미국) |
| T-02 | Morgan Stanley Services Group | 2025-04-30 (등록) | US12380896B1 | Audio speech signal analysis for fraud detection | 콘택트센터 실시간 오디오 사기 탐지; 앙상블 모델 (화자+의도+합성음성+운율) | USPTO (미국) |
| T-03 | 딥브레인AI | 2024-02-05 (출원 발표) | 미공개 (KIPO 출원) | 딥러닝 기반 딥보이스 탐지 기술 | 고주파 영역 강화 정보 추출 + 위변조 판별 딥러닝 모델, MFCC 한계 극복 | KIPO (한국) |

### 내부 자료 (I-xx)

해당 없음 (내부 자료 미사용)

---

*본 리포트는 MCP 소스 (research-hub, patent-intel, trend-tracker) 미접속 상태에서 WebSearch와 WebFetch만으로 작성되었습니다. 학술 논문 인용수 및 일부 특허 번호는 공개 데이터 미확인 상태이므로 추가 검증이 권장됩니다.*
