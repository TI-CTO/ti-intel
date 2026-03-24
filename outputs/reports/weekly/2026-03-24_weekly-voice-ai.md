---
type: weekly-monitor
domain: voice-ai
week: 2026-W13
date: 2026-03-24
l3_count: 8
deep_count: 4
tags: [claude-code, weekly]
created: 2026-03-24
updated: 2026-03-24
---

# 주간 기술 동향: Voice AI (2026-W13)

## Executive Summary

| 세부기술 | 신호 | 핵심 내용 | 분석 |
|----------|------|----------|------|
| Voice Cloning | 🔴 | "구별 불가능 임계점" 공식 선언(Fortune), Pindrop-Zoom 실시간 딥페이크 탐지 통합, EU AI Act Article 50 D-130 | Deep |
| Voice Synthesis | 🟡 | Hume Octave 2 감정 TTS 출시(11언어·200ms), ElevenLabs 11.ai MCP 음성비서 알파, Eleven v3 GA | Deep |
| Emotional Analysis | 🟡 | Hume Octave 2 다국어 감정 TTS, ElevenLabs Japan 고객 괴롭힘 대응 솔루션, VoxEmo 벤치마크 | Deep |
| Interrupt & Turn-Taking | 🟡 | 음성에이전트 인프라 투자 $648M+(LiveKit $1B 유니콘), ElevenLabs Conversational AI 2.0, τ-Voice 벤치마크 | Deep |
| Context Recognition | 🟢 | Conversational AI 채택 가속(Gartner: critical velocity), 구조적 돌파 없음 | Quick |
| Persona Plugin | 🟢 | Life-long Personalization 연구 지속, 특이사항 없음 | Quick |
| Relationship Graph | 🟢 | LLM-TEXT2KG 워크숍, GraphRAG 산업 표준화 지속 | Quick |
| Context Action Recommendation | 🟢 | Apple Siri+Gemini 통합 지연(iOS 26.5 베타 3/30), 프로액티브 AI 트렌드 지속 | Quick |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음
>
> **분석** : Deep = 심층 리서치 수행 | Quick = 1줄 요약만

---

## 🟢 Quick 요약 (변화 미미)

### Context Recognition
- Conversational AI 채택이 Gartner 기준 "critical velocity"에 도달. LLM 기반 멀티턴 대화 시스템이 산업 표준으로 정착 중이나 W12 대비 구조적 돌파 없음.

### Persona Plugin
- Life-long Personalization of LLMs(Large Language Models) 연구가 지속되며 동적 사용자 프로필 적응 프레임워크가 학술적으로 정비 중. 상용 제품 수준의 돌파구 없음.

### Relationship Graph
- LLM-TEXT2KG 2026 워크숍(5회차)이 Knowledge Graph 자동 생성 연구 커뮤니티를 확장 중. Nature Scientific Reports에 LLM 기반 KG(Knowledge Graph) 구축 논문 게재. GraphRAG가 Gartner 선정 GenAI "Critical Enabler"로 유지.

### Context Action Recommendation
- Apple Siri + Google Gemini 통합이 iOS 26.5 베타(3/30 예상)로 지연. Arahi Rahi 프로액티브 AI 비서 출시, Anthropic Claude 메모리 기능 전체 사용자 확대. 프로액티브 AI 트렌드는 지속되나 구조적 변화 없음.

---

## 🔴 Voice Cloning — 긴급

> 상세 리서치: [2026-03-24_research-voice-cloning.md](2026-03-24_research-voice-cloning.md)

### 이전 대비 변화
- **전주**: ElevenLabs SXSW "1M Voices"($1B), Iconic Marketplace(28명 유명인 라이선스), YouTube 딥페이크 탐지 확대
- **금주**: "구별 불가능 임계점" 공식 선언, Pindrop-Zoom 실시간 탐지 통합, UN·INTERPOL 음성 클로닝 조직 사기 경고, EU AI Act 8월 시행 D-130
- **변화 방향**: 생성·탐지 비대칭성 전면화 → 규제·탐지 인프라 동시 가속

### 기술 동향

1. **"구별 불가능 임계점" 공식 선언 — 인간 탐지 정확도 54%(우연 수준).**
   Fortune/Siwei Lyu(SUNY Buffalo)가 음성 클로닝의 "indistinguishable threshold" 돌파를 선언. 수초 샘플로 억양·리듬·감정·숨소리까지 완전 복제 가능. 온라인 딥페이크 볼륨 900%+ 성장(2023년 50만→2025년 800만 건). [[G-01]](#ref-g-01)

2. **ElevenLabs Eleven v3 GA — 70개 언어, Audio Tags, Multi-speaker Dialogue API.**
   Flagship 모델이 GA 전환. `[excited]` `[whispers]` 등 오디오 태그로 감정 제어, 오류율 15.3%→4.9%(68% 감소). Studio 3.0으로 엔드투엔드 콘텐츠 제작 환경 완성. [[G-02]](#ref-g-02)

3. **Pindrop-Zoom 실시간 딥페이크 탐지 통합 (3/12) — 2초 내 탐지, 정확도 99% 주장.**
   15억 건 인터랙션으로 훈련된 모델. 금융·의료·통신·정부 타깃. 300개+ 특허 보유. Gartner: 2026년까지 기업 30%가 단일 음성 인증을 불신. [[G-03]](#ref-g-03)

4. **UN·INTERPOL 음성 클로닝 조직 사기 경고 — AI 주도 사기 1,210% 급증.**
   비엔나·방콕 이중 서밋에서 음성 클로닝이 사이버범죄 서비스(CaaS)로 표준화됐다고 경고. 미국 2024년 대상 피해 $10B. [[G-04]](#ref-g-04)

5. **EU AI Act Article 50 전면 시행 D-130 — 합성 음성 레이블링 의무, 위반 시 매출 7%.**
   2026년 8월 2일 전면 시행. AI 생성 음성에 레이블링·워터마킹·메타데이터 의무 부과. 콘텐츠 투명성 코드 오브 프랙티스 5~6월 확정 예정. [[G-05]](#ref-g-05)

6. **딥페이크 탐지 일반화 실패 — 통신 채널 통과 시 성능 급락.**
   PMC 리뷰 논문이 기존 탐지 모델의 실세계 일반화 실패를 진단. 개선 가이드라인 적용 시 57% 정확도 향상 가능. [[P-01]](#ref-p-01)

### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | Eleven v3 GA(70언어, Audio Tags). $500M Series D/$11B. Iconic Voice Marketplace 확대 | [[G-02]](#ref-g-02) |
| OpenAI | gpt-realtime 프로덕션 출시(지시 추종 +48%, 함수 호출 +34%). Voice Engine 커스텀 클로닝은 제한 배포 지속 | [[G-06]](#ref-g-06) |
| Google | Gemini 2.5 TTS GA(30스피커, 80로케일). AI Studio 음성 클로닝 UI 노출(비활성) | [[G-07]](#ref-g-07) |
| LiveKit | Series C $100M/$1B 유니콘. OpenAI·Tesla 핵심 인프라 공급 | [[G-08]](#ref-g-08) |
| Pindrop | Zoom Contact Center 실시간 딥페이크 탐지 통합. 300개+ 특허 | [[G-03]](#ref-g-03) |
| Meta | PlayAI 인수(2025-07) 내재화 완료. 팀 35명 Meta Superintelligence Lab 편입 | [[G-09]](#ref-g-09) |

### 시장 시그널
- LiveKit $100M/$1B, ElevenLabs $500M/$11B, Synthflow $20M — 생성 플랫폼과 탐지 인프라에 자본 동시 유입 [[G-08]](#ref-g-08), [[G-10]](#ref-g-10)
- Meta PlayAI 인수로 독립 음성 클로닝 플랫폼 소멸 → 빅테크 흡수 가속 [[G-09]](#ref-g-09)
- 한국: SKT·Naver 음성 클로닝 전용 기술 공시 부재. 글로벌 API 생태계 잠금 진행 중 [[G-11]](#ref-g-11)

### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| Audio Deepfake Detection: What Has Been Achieved (PMC, 2026) | 탐지 시스템의 실세계 일반화 실패 진단, 통신 채널 가이드라인으로 57% 개선 | [[P-01]](#ref-p-01) |
| Targeted Speaker Poisoning Framework (Trachu et al., 2026) | 제로샷 TTS에서 특정 화자 생성 차단, 15명까지 효과적 | [[P-02]](#ref-p-02) |

### 전략적 시사점

**기회**
- 통신사 컨택센터에 Pindrop 수준 실시간 딥페이크 탐지 번들링 → EU AI Act 선점
- ElevenLabs Iconic Marketplace 모델 참고, 한국어 음성 라이선스 마켓플레이스 구축 가능

**위협**
- 음성 기반 본인 확인(ARS, 콜센터) 신뢰 붕괴. 단일 음성 인증 의존 시 2026년 내 대체 필요
- EU AI Act 8월 시행 → 합성 음성 서비스 수출 시 즉각 컴플라이언스 대응 필수

---

## 🟡 Voice Synthesis — 주목

> 상세 리서치: [2026-03-24_research-voice-synthesis.md](2026-03-24_research-voice-synthesis.md)

### 이전 대비 변화
- **전주**: Big Tech 반격 — Gemini 2.5 TTS(70언어 번역), OpenAI gpt-4o-mini-tts WER 35%↓, Anthropic+ElevenLabs OEM
- **금주**: 플랫폼 전환 완성 — Hume Octave 2 감정 TTS, ElevenLabs 11.ai MCP 음성비서, Eleven v3 GA, MS Dragon HD Omni
- **변화 방향**: "모델 성능 경쟁" → "플랫폼·에이전트 통합 경쟁"으로 완전 전환

### 기술 동향

1. **Hume Octave 2 — 감정 인지 TTS 2세대, 11언어·200ms·50% 가격 인하.**
   스크립트 맥락에서 감정을 자율 추론하는 레이어 탑재. Voice Conversion·Phoneme Editing 신규 기능. 한국어 포함 11개 언어. [[G-12]](#ref-g-12)

2. **ElevenLabs 11.ai 알파 — MCP 통합 음성 우선 AI 어시스턴트.**
   Salesforce·Gmail·Slack 등 외부 서비스를 음성 명령으로 제어. 멀티턴 맥락 유지. TTS가 에이전트 제어 레이어로 확장. [[G-13]](#ref-g-13)

3. **Eleven v3 GA (3/14) — Audio Tags, Text to Dialogue API, 오류율 68% 감소.**
   `[excited]` `[whispers]` 태그로 감정·음향 효과 제어. JSON 배열 입력으로 자연스러운 멀티스피커 대화 자동 생성. [[G-14]](#ref-g-14)

4. **Gemini 2.5 TTS Native Audio 업그레이드 — 멀티턴 맥락·Function Calling 개선.**
   Flash+Pro TTS의 표현력·멀티스피커 일관성 개선. Gemini Live·Search Live 통합 시작. [[G-15]](#ref-g-15)

5. **Microsoft Dragon HD Omni — 단일 통합 모델로 700+ 음성·150+ 언어.**
   SSML 튜닝 부담 대폭 절감. 엔터프라이즈 음성 서비스 구축 비용 감소 전환점. [[G-16]](#ref-g-16)

6. **Kitten TTS v0.8 — 오픈소스 15M~80M 파라미터, CPU 실행 에지 TTS.**
   상용 API 없이 온디바이스 음성 합성 가능. 초경량 에지 TTS 경쟁 심화(Kyutai Pocket TTS 100M 이어). [[G-17]](#ref-g-17)

### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Hume AI | Octave 2 출시. 11언어, 200ms, 50% 가격 인하. Voice Conversion 예고 | [[G-12]](#ref-g-12) |
| ElevenLabs | 11.ai MCP 비서 알파 + Eleven v3 GA. 일본 법인 설립, 81PRODUCE 파트너십. $500M/$11B | [[G-13]](#ref-g-13), [[G-14]](#ref-g-14), [[G-18]](#ref-g-18) |
| Google | Gemini 2.5 TTS Native Audio 업그레이드. Gemini Live 통합. Speech-to-Speech 번역 70언어 | [[G-15]](#ref-g-15) |
| Microsoft | Dragon HD Omni 프리뷰. 700+ 음성 단일 모델. Azure Speech 마이그레이션 경로 공개 | [[G-16]](#ref-g-16) |
| Inworld | TTS-1.5-Max ELO 1,160 1위. $10/1M chars. TTFB P90 250ms 이하 | [[G-19]](#ref-g-19) |
| Cartesia | Sonic 3 AWS SageMaker 통합. Turbo TTFB 40ms. 42언어 | [[G-20]](#ref-g-20) |

### 시장 시그널
- ElevenLabs $500M Series D/$11B, 누적 $781M, ARR $330M. Audio General Intelligence 연구 투자 [[G-18]](#ref-g-18)
- Voice AI 섹터 2026년 1~3월 신규 에퀴티가 2024년 연간 수준($371M)에 도달 [[G-21]](#ref-g-21)
- 글로벌 AI 음성 에이전트 시장: 2024년 $2.4B → 2034년 $47.5B(CAGR ~35%) [[G-21]](#ref-g-21)

### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| Towards Controllable Speech Synthesis in the Era of LLMs (2024) | 피치·감정·스타일 등 제어 파라미터별 최신 방법론 체계화 | [[P-03]](#ref-p-03) |
| Low-Latency Voice Agents for Telecommunications (2025) | 통신 음성 에이전트용 스트리밍 ASR + 양자화 LLM + 실시간 TTS 통합 파이프라인 | [[P-04]](#ref-p-04) |

### 전략적 시사점

**기회**
- Hume Octave 2의 한국어 포함 감정 TTS → 통신사 AICC(AI Contact Center) 즉각 OEM 채택 가능
- Google 실시간 Speech-to-Speech 번역(70언어) → 국제 로밍/통화 서비스 통합 킬러 피처
- 초경량 에지 TTS(Kitten 15M) → 온디바이스 음성 서비스 API 비용 없이 구현 가능

**위협**
- ElevenLabs $11B + 글로벌 대형 라운드 집중 → 국내 음성 AI 플레이어에 가격·기능 구조적 압박
- 빅테크 내재화(Meta PlayAI, Anthropic+ElevenLabs OEM) → 독립 TTS 공급사 생존 공간 축소

---

## 🟡 Emotional Analysis — 주목

> 상세 리서치: [2026-03-24_research-emotional-analysis.md](2026-03-24_research-emotional-analysis.md)

### 이전 대비 변화
- **전주**: Foundation Model zero-shot SER(Speech Emotion Recognition) 학술 공식화, MME-Emotion 최고 39.3%, Hume EVI 3 출시
- **금주**: Hume Octave 2 다국어 감정 TTS 출시, ElevenLabs Japan 고객 괴롭힘 대응 솔루션, VoxEmo 벤치마크 등장, EU AI Act 직장 내 감정 인식 금지 발효
- **변화 방향**: "학술 벤치마크 정비 → 상용 제품 출시 가속" + 규제 리스크 현재화

### 기술 동향

1. **Hume Octave 2 — 다국어 감정 TTS, 한국어 포함 11언어·200ms.**
   스크립트 감정 맥락 자율 이해. "겁에 질린 속삭임" "빈정거리는 톤" 등 다국어 동일 구현. Octave 1 대비 50% 가격 인하. [[G-12]](#ref-g-12)

2. **ElevenLabs Japan — 고객 괴롭힘(카스하라) 대응 감정 AI 보이스 솔루션.**
   AI 보이스가 1차 응대 "방파제" 역할. 언어폭력으로부터 상담원 보호. 통신사 고객센터 전환 참고 모델. [[G-22]](#ref-g-22)

3. **VoxEmo — 15개 언어·35개 코퍼스 Speech LLM SER 벤치마크 (arxiv 2603.08936).**
   USC·셰필드대 공동. zero-shot 모델이 하드 레이블 정확도는 낮지만 인간 주관 분포와 일치성이 더 높다는 핵심 발견. [[P-05]](#ref-p-05)

4. **EU AI Act 직장 내 감정 인식 금지 — 2025년 2월 발효.**
   Article 5가 직장·교육기관 감정 인식 AI 사용을 명시 금지. 위반 시 최대 €3,500만 또는 연간 매출 7%. B2B 수출 시 컴플라이언스 설계 선결 과제. [[G-23]](#ref-g-23)

5. **Microsoft DragonHD — 감정 단서 자동 감지·실시간 톤 조정.**
   별도 감정 태그 없이 텍스트 내용만으로 감정 톤 추론. 클라우드 3사 모두 감정 AI 내재화 완료 단계. [[G-16]](#ref-g-16)

### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Hume AI | Octave 2(11언어, 200ms, 50% 가격 인하). EVI 3(200K+ 커스터마이제이션, 300ms 응답) | [[G-12]](#ref-g-12) |
| ElevenLabs | Japan LLC customer harassment 솔루션. 상담원 보호 "방파제" AI 보이스 | [[G-22]](#ref-g-22) |
| Microsoft | DragonHD 감정 자동 감지. Video Indexer 4가지 감정 상태 탐지 | [[G-16]](#ref-g-16) |
| SKT | 멘탈비전 사내 운영 중. 보컬비전(VocAl VISION) 식약처 의료기기 허가 취득 | [[E-01]](#ref-e-01) |
| KT | AI 보이스 스튜디오 감정 표현 TTS. AICC A.sen Cloud 보이스봇 감정 응대 | [[E-02]](#ref-e-02) |
| Uniphore | Gartner Magic Quadrant 리더. $610M 누적 투자, ARR $100M+ | [[G-24]](#ref-g-24) |

### 시장 시그널
- 감정 AI 시장: 2026년 $41.5B → 2034년 $207.7B(CAGR 22.29%). 음성 세그먼트 CAGR 37.1%로 최고 성장 [[G-25]](#ref-g-25)
- WHO "책임 있는 정신건강 AI" 로드맵 발표(2026-03-20) — 감정 AI 헬스케어 응용 임상 기준 요구 [[G-26]](#ref-g-26)

### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| VoxEmo (Zhang et al., 2026) | 15개 언어·35개 코퍼스 SER 벤치마크. zero-shot 모델의 인간 주관 분포 일치성 발견 | [[P-05]](#ref-p-05) |
| Pioneering Multimodal Emotion Recognition (2025) | Open-Vocabulary MER(Multimodal Emotion Recognition) 최초 체계적 연구. 오디오·비디오·텍스트 삼중 융합 최적 | [[P-06]](#ref-p-06) |

### 전략적 시사점

**기회**
- ElevenLabs Japan customer harassment 모델 → 국내 고객센터 상담원 보호 + 운영 효율 이중 가치
- SKT 보컬비전 식약처 허가 → 헬스케어 SaaS 진입 경로 실증

**위협**
- EU AI Act 직장 내 감정 인식 금지 → 글로벌 B2B 수출 시 컴플라이언스 리스크
- LLM 감정 지능 구조적 한계(최고 모델 39.3%) → 오인식 사고 위험

---

## 🟡 Interrupt & Turn-Taking — 주목

> 상세 리서치: [2026-03-24_research-interrupt-turn-taking.md](2026-03-24_research-interrupt-turn-taking.md)

### 이전 대비 변화
- **전주**: Full-Duplex-Bench 수치 공개, OpenAI gpt-realtime GA, LiveKit 한국어 지원
- **금주**: 음성에이전트 인프라 투자 $648M+ 폭증, ElevenLabs Conversational AI 2.0 독자 턴테이킹 모델, τ-Voice 벤치마크 등장
- **변화 방향**: 평가·인프라 표준화가 시장 구조 재편 촉진. 인프라 vs 애플리케이션 투자 양극화

### 기술 동향

1. **ElevenLabs Conversational AI 2.0 — 독자 신경망 턴테이킹 + 95% 인터럽트 감지.**
   VAD를 넘어 필러 워드·운율·발화 리듬 종합 분석. Turn Eagerness 3단계(Eager/Normal/Patient). HIPAA 준수·EU 데이터 레지던시. [[G-27]](#ref-g-27)

2. **τ-Voice — Full-Duplex 음성 에이전트 벤치마크 신규 표준 (arXiv 2603.13686).**
   실세계 복잡도 기반 과제형 평가. 인터럽트·백채널링·노이즈·억양 다양성 포함. Full-Duplex-Bench에 이어 복수 표준으로 확장. [[P-07]](#ref-p-07)

3. **Deepgram Flux — 세계 최초 대화 전용 음성 인식(CSR), End-of-Turn ~260ms.**
   VAD·엔드포인팅·맥락 인식 턴 감지를 단일 모델에 통합. GPU당 100+ 스트림 병렬 처리. [[G-28]](#ref-g-28)

4. **LiveKit 턴 감지 — 한국어 포함 14개 언어, 의미적 완전성 기반 예측.**
   Qwen2.5 7B→0.5B 지식 증류. RAM ~400MB, 추론 ~25ms. TPR 85%. [[G-29]](#ref-g-29)

5. **AssemblyAI Universal-3 Pro — ~150ms P50 레이턴시, 음향+의미 통합 엔드포인팅.**
   멀티링구얼 Universal-Streaming 출시. WER 8.14%. [[G-30]](#ref-g-30)

### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | Conversational AI 2.0. $500M/$11B. Deutsche Telekom·Revolut 확보. $330M ARR | [[G-27]](#ref-g-27) |
| LiveKit | $100M/$1B 유니콘. ChatGPT·xAI·Meta·Spotify 인프라 공급. 한국어 턴 감지 | [[G-08]](#ref-g-08), [[G-29]](#ref-g-29) |
| Deepgram | Flux CSR GA. Voice Agent API(STT·TTS·오케스트레이션 단일 API) | [[G-28]](#ref-g-28) |
| Retell AI | 턴테이킹 모델 업데이트 150ms 절감. $40M ARR. 멀티채널 전환 | [[G-31]](#ref-g-31) |
| NVIDIA | PersonaPlex-7B(ICASSP 2026). Smooth Turn-Taking 0.170s SOTA | [[P-08]](#ref-p-08) |
| SKT | A.auto 차량 내 AI 에이전트 출시(르노코리아 필란테). MWC26 AI Native 전략 | [[E-03]](#ref-e-03) |

### 시장 시그널
- 1~2주 내 음성 에이전트 인프라 투자 $648M+: LiveKit $100M, ElevenLabs $500M, Synthflow $20M, Newo.ai $25M, Hamming.ai $3.8M [[G-08]](#ref-g-08), [[G-32]](#ref-g-32), [[G-33]](#ref-g-33)
- Hamming.ai $3.8M 시드 — 음성 에이전트 테스트 자동화 QA 세부 시장 형성 신호 [[G-34]](#ref-g-34)
- 대화형 AI 시장: 2025년 $14.3B → 2030년 $41.4B(CAGR 23.7%) [[G-21]](#ref-g-21)

### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| τ-Voice (Ray et al., 2026) | Full-duplex 음성 에이전트 실세계 벤치마크. τ²-bench 음성 확장 | [[P-07]](#ref-p-07) |
| Noise-Robust Turn-Taking (Inoue et al., IROS 2025) | 쇼핑몰 현장 실험에서 Transformer VAP 모델 응답 레이턴시 단축 실증 | [[P-09]](#ref-p-09) |
| PersonaPlex (NVIDIA, ICASSP 2026) | Moshi 기반 full-duplex, Smooth Turn-Taking 0.170s SOTA | [[P-08]](#ref-p-08) |

### 전략적 시사점

**기회**
- LiveKit 한국어 공식 지원 → 한국어 턴테이킹 파트너십 또는 독자 모델 개발 시간 확보
- τ-Voice·Full-Duplex-Bench 표준화 → 객관적 기술 격차 측정 및 WTIS 분석 정밀화
- 차량 내 음성 에이전트(SKT A.auto) → 통신사 고유 데이터 활용 턴테이킹 개인화

**위협**
- ElevenLabs $330M ARR + Deutsche Telekom 파트너십 → 글로벌 통신사 직접 공략, 생태계 잠금(lock-in)
- 노코드 플랫폼(Synthflow, Newo.ai)이 SMB 시장 잠식 → 통신사 ARS/컨택센터 사업 중기 위협
- 영미권 인프라 레이어 집중 → 한국어 훈련 데이터 다양성·오류율 편차 과제

---

## 경쟁사 동향 (SKT / KT)

> 이번 주 Voice AI 도메인 관련 SKT·KT 주요 움직임.

### SKT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| "1인 1 AI 에이전트" 전략 (3/16) | 전 직원 대상 업무 특화 AI 에이전트 목표. 에이닷 비즈/폴라리스/플레이그라운드 플랫폼 공개 | (L3 밖) | [[E-04]](#ref-e-04) |
| A.auto 차량 내 AI 에이전트 | 르노코리아 필란테 탑재. A.X 4.0 LLM 기반 음성 제어(T-map·FLO·전화·뉴스) | interrupt-turn-taking | [[E-03]](#ref-e-03) |
| 멘탈비전·보컬비전 | 음성+얼굴 불안·우울 분석 사내 서비스. 보컬비전 식약처 의료기기 허가 | emotional-analysis | [[E-01]](#ref-e-01) |
| MWC 2026 AI Native 전략 | 풀스택 AI 전시. 1GW AIDC 구축, 1T 파라미터 멀티모달 모델 업그레이드 | (L3 밖) | [[E-05]](#ref-e-05) |

### KT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| AI 보이스피싱 탐지서비스 2.0 | 화자인식 + 딥보이스 탐지 통합 상용화. 2025년 ~1,300억원 피해 예방 | voice-cloning | [[E-06]](#ref-e-06) |
| AICC A.sen Cloud | 보이스봇 감정 응대 내재화. AI 보이스 스튜디오 인간 수준 감정 표현 TTS | emotional-analysis | [[E-02]](#ref-e-02) |

### 시사점
- SKT는 "1인 1에이전트" + 차량 AI(A.auto)로 음성 에이전트 생태계를 확장 중이나, 글로벌 플레이어(ElevenLabs $11B, LiveKit $1B) 대비 음성 클로닝·턴테이킹 독자 기술 공시가 부재. API 의존 vs 독자 기술 전략 결정이 임박.
- KT는 보이스피싱 탐지에서 국내 선두(~1,300억원 피해 예방)이나, Pindrop의 Zoom 통합 같은 글로벌 플랫폼 연동 사례와 비교 시 확장성 과제.

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **ElevenLabs 풀스택 전환의 파급력.** 이번 주 ElevenLabs는 4개 Deep 토픽 모두에서 핵심 플레이어로 등장했다. Eleven v3(Voice Cloning/Synthesis), 11.ai MCP(Voice Synthesis), Conversational AI 2.0(Turn-Taking), Japan 솔루션(Emotional Analysis). $11B 밸류에이션의 플랫폼 기업이 통신사 직접 공략(Deutsche Telekom 파트너십)을 시작한 것은 구조적 경고 신호다.

2. **생성-탐지 비대칭성의 산업화.** Voice Cloning의 "구별 불가능 임계점" 선언과 동시에 Emotional Analysis의 감정 표현 TTS 고도화가 진행되고 있다. 생성 기술이 "사기 인프라"와 "고객 서비스 혁신" 양면으로 동시 확산 중이며, 통신사는 양면 모두에 대응 전략이 필요하다.

3. **벤치마크 표준화 파도.** τ-Voice(Turn-Taking), VoxEmo(Emotion), Full-Duplex-Bench(Turn-Taking), MME-Emotion(Multimodal) — 주요 L3마다 평가 표준이 수립되면서 기술 격차의 "객관적 측정"이 가능해졌다. 내부 기술 수준 벤치마킹에 즉시 활용 가능.

4. **규제 시계 가속.** EU AI Act Article 50(합성 음성 레이블링, 8/2), Article 5(직장 내 감정 인식 금지, 이미 발효), WHO 정신건강 AI 로드맵 — 3개 규제 트랙이 Voice AI 전 영역에 걸쳐 동시 진행 중. 컴플라이언스 설계가 제품 기획 초기 단계부터 필수화됐다.

### 후속 조치 제안

- 🔴 Voice Cloning 긴급 → `/wtis standard speech-generation` 검증 권고 (음성 클로닝·합성 포괄 Go/No-Go)
- 🟡 Interrupt & Turn-Taking → τ-Voice/Full-Duplex-Bench 기반 내부 기술 수준 벤치마킹 검토
- 📊 프레젠테이션 필요 시 → `/slides` 변환
- 📅 다른 도메인 → `/weekly-monitor secure-ai` (수요일)

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Fortune — Voice cloning crossed 'indistinguishable threshold' | [링크](https://fortune.com/2025/12/27/2026-deepfakes-outlook-forecast/) | news | 2025-12 | [B] |
| <a id="ref-g-02"></a>G-02 | ElevenLabs — Eleven v3 Most Expressive AI TTS Model | [링크](https://elevenlabs.io/blog/eleven-v3) | blog | 2026-02 | [A] |
| <a id="ref-g-03"></a>G-03 | Globe Newswire — Pindrop-Zoom Real-Time Deepfake Detection Integration | [링크](https://www.globenewswire.com/news-release/2026/03/12/3254709/0/en/Pindrop-Zoom-Integration-Embeds-Real-Time-Deepfake-Detection-and-Identity-Verification-in-Zoom-Contact-Center.html) | news | 2026-03-12 | [A] |
| <a id="ref-g-04"></a>G-04 | UN News — Deepfakes, voice cloning and weaponised AI: Global wake-up call | [링크](https://news.un.org/en/story/2026/03/1167144) | news | 2026-03 | [A] |
| <a id="ref-g-05"></a>G-05 | EU Digital Strategy — Code of practice on marking AI-generated content | [링크](https://digital-strategy.ec.europa.eu/en/news/commission-launches-work-code-practice-marking-and-labelling-ai-generated-content) | news | 2026 | [A] |
| <a id="ref-g-06"></a>G-06 | OpenAI — Introducing gpt-realtime for production voice agents | [링크](https://openai.com/index/introducing-gpt-realtime/) | blog | 2026 | [A] |
| <a id="ref-g-07"></a>G-07 | Google Blog — Gemini 2.5 Text-to-Speech model updates | [링크](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-2-5-text-to-speech/) | blog | 2025-12 | [A] |
| <a id="ref-g-08"></a>G-08 | SiliconANGLE — LiveKit raises $100M at $1B valuation | [링크](https://siliconangle.com/2026/01/22/livekit-raises-100m-1b-valuation-scale-real-time-ai-media-platform/) | news | 2026-01-22 | [B] |
| <a id="ref-g-09"></a>G-09 | TechCrunch — Meta acquires voice startup Play AI | [링크](https://techcrunch.com/2025/07/13/meta-acquires-voice-startup-play-ai/) | news | 2025-07 | [B] |
| <a id="ref-g-10"></a>G-10 | TFN — Synthflow AI raises $20M Series A | [링크](https://techfundingnews.com/enterprise-voice-ai-synthflow-raises-20m-series-a/) | news | 2026-03 | [B] |
| <a id="ref-g-11"></a>G-11 | Korea Herald — LG, SKT advance in sovereign AI project | [링크](https://www.koreaherald.com/article/10656367) | news | 2026-01 | [B] |
| <a id="ref-g-12"></a>G-12 | Hume AI — Octave 2: Next-Generation Multilingual Voice AI | [링크](https://www.hume.ai/blog/octave-2-launch) | blog | 2025-10 | [A] |
| <a id="ref-g-13"></a>G-13 | ElevenLabs — Introducing 11.ai | [링크](https://elevenlabs.io/blog/introducing-11ai) | blog | 2026-03 | [A] |
| <a id="ref-g-14"></a>G-14 | ElevenLabs — Eleven v3 is Now Generally Available | [링크](https://elevenlabs.io/blog/eleven-v3-is-now-generally-available) | blog | 2026-03-14 | [A] |
| <a id="ref-g-15"></a>G-15 | Google Blog — Gemini 2.5 Native Audio upgrade + TTS updates | [링크](https://blog.google/products/gemini/gemini-audio-model-updates/) | blog | 2026-03 | [A] |
| <a id="ref-g-16"></a>G-16 | Microsoft — Introducing Dragon HD Omni: Azure Speech New Voice Type | [링크](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-dragon-hd-omni-azure-speech-new-voice-type-now-in-preview-via-micros/4481288) | blog | 2026-01 | [A] |
| <a id="ref-g-17"></a>G-17 | Sesame Disk — Kitten TTS v0.8: Open-Source Voice Synthesis for Edge | [링크](https://sesamedisk.com/kitten-tts-open-source-voice-synthesis/) | news | 2026-03-19 | [C] |
| <a id="ref-g-18"></a>G-18 | TechCrunch — ElevenLabs raises $500M from Sequoia at $11B valuation | [링크](https://techcrunch.com/2026/02/04/elevenlabs-raises-500m-from-sequioia-at-a-11-billion-valuation/) | news | 2026-02-04 | [B] |
| <a id="ref-g-19"></a>G-19 | Inworld — Best TTS APIs for Real-Time Voice Agents (2026 Benchmarks) | [링크](https://inworld.ai/resources/best-voice-ai-tts-apis-for-real-time-voice-agents-2026-benchmarks) | blog | 2026 | [B] |
| <a id="ref-g-20"></a>G-20 | AWS — Cartesia Sonic 3 on Amazon SageMaker JumpStart | [링크](https://aws.amazon.com/about-aws/whats-new/2026/02/cartesia-sonic-3-on-sagemaker-jumpstart/) | blog | 2026-02 | [A] |
| <a id="ref-g-21"></a>G-21 | AssemblyAI — Voice AI in 2026: Inside the companies and investments | [링크](https://www.assemblyai.com/blog/voice-ai-in-2026-series-1) | blog | 2026 | [B] |
| <a id="ref-g-22"></a>G-22 | IT Business Today — ElevenLabs Promotes AI Voice Agent for Customer Service | [링크](https://itbusinesstoday.com/martech/customer-experience/elevenlabs-promotes-ai-voice-agent-for-customer-service/) | news | 2026-03 | [B] |
| <a id="ref-g-23"></a>G-23 | Wolters Kluwer — Prohibition of AI Emotion Recognition in Workplace under AI Act | [링크](https://legalblogs.wolterskluwer.com/global-workplace-law-and-policy/the-prohibition-of-ai-emotion-recognition-technologies-in-the-workplace-under-the-ai-act/) | news | 2025-02 | [A] |
| <a id="ref-g-24"></a>G-24 | Uniphore — Emotion AI Platform | [링크](https://www.uniphore.com/emotion-ai/) | blog | 2026 | [B] |
| <a id="ref-g-25"></a>G-25 | Fortune Business Insights — Emotion AI Market Forecast 2034 | [링크](https://www.fortunebusinessinsights.com/emotion-ai-market-112136) | news | 2026 | [C] |
| <a id="ref-g-26"></a>G-26 | WHO — Towards Responsible AI for Mental Health | [링크](https://www.who.int/news/item/20-03-2026-towards-responsible-ai-for-mental-health-and-well-being--experts-chart-a-way-forward) | news | 2026-03-20 | [A] |
| <a id="ref-g-27"></a>G-27 | VentureBeat — ElevenLabs Conversational AI 2.0 turn-taking | [링크](https://venturebeat.com/ai/elevenlabs-debuts-conversational-ai-2-0-voice-assistants-that-understand-when-to-pause-speak-and-take-turns-talking) | news | 2025-05 | [B] |
| <a id="ref-g-28"></a>G-28 | Deepgram — Introducing Flux: Conversational Speech Recognition | [링크](https://deepgram.com/learn/introducing-flux-conversational-speech-recognition) | blog | 2025-10 | [B] |
| <a id="ref-g-29"></a>G-29 | LiveKit — Turn Detection: VAD, Endpointing, and Model-Based Detection | [링크](https://livekit.com/blog/turn-detection-voice-agents-vad-endpointing-model-based-detection) | blog | 2025-12 | [B] |
| <a id="ref-g-30"></a>G-30 | AssemblyAI — How intelligent turn detection solves the biggest challenge | [링크](https://www.assemblyai.com/blog/turn-detection-endpointing-voice-agent) | blog | 2026 | [B] |
| <a id="ref-g-31"></a>G-31 | GlobeNewswire — Retell AI $40M ARR, Updated Platform | [링크](https://www.globenewswire.com/news-release/2026/01/29/3228780/0/en/Upgraded-Retell-AI-Voice-Platform-Enables-Corporate-Call-Centers-to-Deploy-Infinite-AI-Sales-and-Support-Agents-Across-Voice-Chat-Email-and-SMS-Company-Revenue-Now-Exceeds-40M-ARR.html) | IR/발표 | 2026-01 | [A] |
| <a id="ref-g-32"></a>G-32 | SiliconANGLE — Newo.ai $25M Series A | [링크](https://siliconangle.com/2026/02/10/newo-lands-25m-bring-production-ready-ai-receptionists-small-businesses/) | news | 2026-02 | [B] |
| <a id="ref-g-33"></a>G-33 | BusinessWire — Synthflow AI $20M Series A | [링크](https://www.businesswire.com/news/home/20250624442670/en/Synthflow-AI-Raises-$20M-to-Transform-the-$168B-Global-Conversational-AI-Market-With-Enterprise-AI-Voice-Agents) | IR/발표 | 2025-06 | [A] |
| <a id="ref-g-34"></a>G-34 | TFN — Hamming.ai $3.8M seed voice agent reliability | [링크](https://techfundingnews.com/hamming-ai-voice-agent-reliability-funding/) | news | 2026-03-05 | [B] |
| <a id="ref-e-01"></a>E-01 | SKT 뉴스룸 — 멘탈비전 AI 기술로 마음건강 | [링크](https://news.sktelecom.com/214844) | IR/발표 | 2025-09 | [A] |
| <a id="ref-e-02"></a>E-02 | KT 보도자료 — AI 보이스봇·챗봇 서비스 | [링크](https://corp.kt.com/html/promote/news/report_detail.html?rows=10&page=1&datNo=18036) | IR/발표 | 2026 | [A] |
| <a id="ref-e-03"></a>E-03 | SKT PRNewswire — CEO Unveils AI Native Strategy at MWC26 | [링크](https://www.prnewswire.com/news-releases/sk-telecom-ceo-unveils-ai-native-strategy-at-mwc26-driving-koreas-leap-in-ai-innovation-302700470.html) | IR/발표 | 2026-03-01 | [A] |
| <a id="ref-e-04"></a>E-04 | SKT 뉴스룸 — '1인 1AI 에이전트 시대로 전환' | [링크](https://news.sktelecom.com/222847) | IR/발표 | 2026-03-16 | [A] |
| <a id="ref-e-05"></a>E-05 | SKT 뉴스룸 — 풀스택 AI로 MWC26 무대 | [링크](https://news.sktelecom.com/221927) | IR/발표 | 2026-03 | [A] |
| <a id="ref-e-06"></a>E-06 | 디지털투데이 — KT 'AI 보이스피싱 탐지 서비스 2.0' 출시 | [링크](https://www.digitaltoday.co.kr/news/articleView.html?idxno=580815) | news | 2026 | [B] |
| <a id="ref-p-01"></a>P-01 | PMC — Audio Deepfake Detection: What Has Been Achieved | [링크](https://pmc.ncbi.nlm.nih.gov/articles/PMC11991371/) | paper | 2026 | [A] |
| <a id="ref-p-02"></a>P-02 | Trachu et al. — Targeted Speaker Poisoning Framework (arXiv 2603.07551) | [링크](https://arxiv.org/abs/2603.07551) | paper | 2026-03 | [A] |
| <a id="ref-p-03"></a>P-03 | 익명 외 — Towards Controllable Speech Synthesis in the Era of LLMs | [링크](https://arxiv.org/html/2412.06602v1/) | paper | 2024-12 | [A] |
| <a id="ref-p-04"></a>P-04 | 익명 외 — Low-Latency Voice Agents for Telecommunications | [링크](https://arxiv.org/html/2508.04721v1) | paper | 2025 | [A] |
| <a id="ref-p-05"></a>P-05 | Zhang et al. — VoxEmo: Benchmarking SER with Speech LLMs (arXiv 2603.08936) | [링크](https://arxiv.org/abs/2603.08936) | paper | 2026-03-09 | [A] |
| <a id="ref-p-06"></a>P-06 | 익명 외 — Pioneering Multimodal Emotion Recognition: Closed Sets to Open Vocabularies | [링크](https://arxiv.org/html/2512.20938v1) | paper | 2025-12 | [A] |
| <a id="ref-p-07"></a>P-07 | Ray et al. — τ-Voice: Benchmarking Full-Duplex Voice Agents (arXiv 2603.13686) | [링크](https://arxiv.org/abs/2603.13686) | paper | 2026-03-14 | [A] |
| <a id="ref-p-08"></a>P-08 | NVIDIA — PersonaPlex: Voice and Role Control for Full Duplex (ICASSP 2026) | [링크](https://arxiv.org/abs/2602.06053) | paper | 2026-02 | [A] |
| <a id="ref-p-09"></a>P-09 | Inoue et al. — Noise-Robust Turn-Taking for Dialogue Robots (IROS 2025) | [링크](https://arxiv.org/abs/2503.06241) | paper | 2025-03 | [A] |
