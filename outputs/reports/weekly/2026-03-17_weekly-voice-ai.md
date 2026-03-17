---
type: weekly-monitor
domain: voice-ai
week: 2026-W12
date: 2026-03-17
l3_count: 8
deep_count: 4
tags: [claude-code, weekly]
created: 2026-03-17
updated: 2026-03-17
---

# 주간 기술 동향: Voice AI (2026-W12)

## Executive Summary

| 세부기술 | 신호 | 핵심 내용 | 분석 |
|----------|------|----------|------|
| Voice Synthesis | 🔴 | Google Gemini 2.5 TTS 멀티스피커+실시간 번역(70언어), OpenAI gpt-4o-mini-tts WER 35%↓, Anthropic Claude Code ElevenLabs TTS 채택 | Deep |
| Voice Cloning | 🔴 | ElevenLabs SXSW "1M Voices"($1B), Iconic Marketplace(28명 유명인 라이선스), YouTube 딥페이크 탐지 확대 | Deep |
| Emotional Analysis | 🟡 | Foundation Model zero-shot SER 학술 공식화(Nature npj AI), MME-Emotion ICLR 2026 — 최고 모델도 39.3%, Hume AI EVI 3 출시 | Deep |
| Interrupt & Turn-Taking | 🟡 | Full-Duplex-Bench 수치 공개(Gemini 1.3s vs Moshi 0.27s), OpenAI gpt-realtime 정식 출시, LiveKit 한국어 지원 | Deep |
| Context Recognition | 🟢 | 멀티턴 대화 성숙 지속, LLM 기반 DST 표준화 진행, 구조적 변화 없음 | Quick |
| Persona Plugin | 🟢 | PersonaPlex 페르소나 프롬프트 커스터마이징 확인, 점진적 발전 | Quick |
| Relationship Graph | 🟢 | GraphRAG 주류화 지속, Knowledge Graph Conference 2026 개최 | Quick |
| Context Action Recommendation | 🟢 | 프로액티브 AI 트렌드 확산, 27% 기업 GenAI 음성 도입, 특별한 돌파 없음 | Quick |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음
>
> **분석** : Deep = 심층 리서치 수행 | Quick = 1줄 요약만

---

## 🟢 Quick 요약 (변화 미미)

### Context Recognition
- LLM 기반 멀티턴 대화 시스템이 산업 표준으로 정착 중. Gartner 예측: 2026년 Conversational AI가 컨택센터 에이전트 인건비 $80B 절감. Google Gemini 3.1 Pro가 최대 컨텍스트 윈도우로 장문 대화 이력 처리를 리드하나, W11 대비 구조적 돌파구 없음.

### Persona Plugin
- NVIDIA PersonaPlex-7B이 텍스트 프롬프트만으로 다양한 페르소나·역할을 커스터마이징하는 방식을 검증함. 컨텍스트 기반 정보 검색·응답이 가능. AI 페르소나의 동적 메모리·적응이 2026년 핵심 트렌드로 유지되나, W11 대비 추가 돌파구 없음.

### Relationship Graph
- GraphRAG가 2026년 AI 워크플로우의 핵심 인프라로 자리매김. Gartner: Knowledge Graph를 GenAI의 "Critical Enabler"로 분류. Knowledge Graph Conference 2026(Cornell Tech, NYC) 개최. Neo4j·PuppyGraph 등 AI-native 그래프 DB 생태계 확장 중이나, 이번 주 기술적 돌파구 없음.

### Context Action Recommendation
- 프로액티브 AI(사용자 의도 선제 파악·행동 추천)가 확산 중. 27% 기업이 GenAI 기반 음성 커뮤니케이션 도입, 2026년 75% 예상. Lenovo Qira(CES 2026), Google Project Astra의 프로액티브 추천 연구 지속. W11 대비 추가 변화 없음.

---

## 🔴 Voice Synthesis — 긴급

> 상세 리서치: [2026-03-17_research-voice-synthesis.md](2026-03-17_research-voice-synthesis.md)

### 이전 대비 변화
- **전주**: 오픈소스 TTS 빅뱅 — Qwen3-TTS(97ms), Kani-TTS-2(3GB VRAM), Orpheus(감정태그), Kokoro(82M)
- **금주**: Big Tech 반격 — Google Gemini 2.5 TTS 멀티스피커+실시간 번역, OpenAI WER 35%↓, Anthropic ElevenLabs OEM 채택
- **변화 방향**: 기술 경쟁 축이 "모델 성능" → "플랫폼 통합+생태계 포섭"으로 이동

### 기술 동향

1. **Google Gemini 2.5 TTS 대폭 업그레이드 — 멀티스피커, 실시간 번역, 24언어.**
   Enhanced Expressivity(풍부한 톤), Precision Pacing(맥락 인식 속도 조절), Multi-Speaker(캐릭터 음성 일관성)를 추가. Native Audio를 통해 실시간 Speech-to-Speech 번역(70언어, 2,000언어쌍)이 Google Translate 앱에 적용. 헤드폰 사용 시 화자의 억양·속도·피치를 보존하며 번역. [[G-01]](#ref-g-01) [[G-02]](#ref-g-02)

2. **OpenAI gpt-4o-mini-tts — WER 35% 감소, Custom Voices 개선.**
   Common Voice·FLEURS 벤치마크 기준 약 35% 낮은 WER. Custom Voices에서 방언 정확도·자연스러움 향상. 중국어·힌디어·일본어 등 비영어권 특히 강화. 가격 동결로 성능/가격비 개선. [[G-03]](#ref-g-03)

3. **Anthropic Claude Code 음성모드 — ElevenLabs TTS OEM 채택.**
   자체 TTS 모델 개발 대신 ElevenLabs를 서브컨트랙터로 채택. 5개 음성 선택, 초기 5% 사용자 대상 점진적 확대 중. "TTS-as-Infrastructure" 모델이 LLM 기업에 확산되는 구조적 시그널. [[G-04]](#ref-g-04) [[G-05]](#ref-g-05)

4. **ElevenLabs '1M Voices' 이니셔티브 (SXSW 2026-03-11).**
   영구 음성 손실 환자 100만 명에게 음성 복원 무료 제공($1B in-kind 가치). '11 Voices' 다큐시리즈 SXSW 초연. 7,000명 지원, 800+ NPO 파트너. 기술 기업이 접근성·사회적 임팩트를 브랜드 전략으로 전환하는 대형 사례. [[G-06]](#ref-g-06)

5. **Cartesia Sonic 3 — AWS SageMaker JumpStart 통합.**
   SSM 기반, TTFB 40ms(Turbo)로 업계 최저 지연. 42언어 지원. 엔터프라이즈 클라우드 마켓플레이스 진입 전략. [[G-07]](#ref-g-07)

6. **Inworld TTS-1.5-Max — 품질 벤치마크 1위(ELO 1,160).**
   Artificial Analysis Speech Arena에서 ElevenLabs·OpenAI TTS를 상회. HuggingFace TTS Arena에서는 Vocu V3.0(ELO 1,600)이 1위. 벤치마크별 결과 불일치 — 기업이 유리한 벤치마크를 선별 인용하는 현상 가속. [[G-08]](#ref-g-08)

### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Google | Gemini 2.5 Flash/Pro TTS 멀티스피커+실시간 번역(70언어). 24언어 지원. Native Audio로 Google Translate 앱 내장 | [[G-01]](#ref-g-01) [[G-02]](#ref-g-02) |
| OpenAI | gpt-4o-mini-tts WER 35%↓, Custom Voices 방언·자연스러움 향상. 가격 동결 | [[G-03]](#ref-g-03) |
| Anthropic | Claude Code 음성모드(2026-03-03). ElevenLabs TTS OEM 채택. 5개 음성, 추가 비용 없음 | [[G-04]](#ref-g-04) [[G-05]](#ref-g-05) |
| ElevenLabs | SXSW '1M Voices'($1B in-kind). Iconic Marketplace(28명). ElevenCreative 멀티모달 플랫폼. Anthropic TTS 공식 파트너 | [[G-06]](#ref-g-06) [[G-09]](#ref-g-09) |
| Cartesia | Sonic 3 AWS SageMaker 통합. TTFB 40ms. 42언어. SSM 아키텍처 | [[G-07]](#ref-g-07) |
| Inworld AI | TTS-1.5-Max ELO 1,160 벤치마크 1위. 실시간 음성 에이전트 특화 | [[G-08]](#ref-g-08) |

### 시장 시그널
- AI 음성 생성기 시장: 2025년 $4.16B → 2031년 $20.71B 전망, CAGR 30.7%
- "TTS-as-Infrastructure" 모델 확산: Anthropic이 자체 개발 대신 ElevenLabs OEM 채택 → LLM 기업의 TTS 아웃소싱 구조적 트렌드
- 규제 타임라인: EU AI Act Article 50(합성음 라벨링) 2026-08-02, 미국 뉴욕주 합성 퍼포머 공시 의무 2026-06 시행
- 실시간 TTS 지연: Cartesia 40ms, ElevenLabs 75ms, Inworld <250ms — 음성 에이전트 요건(800ms) 내 상위권 전부 충족

### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| Causal Prosody Mediation for TTS (Mohanty, 2026-03-12) | FastSpeech2에 인과 구조 모델 추가. 감정 조건화로 운율 조작 가능 | [[P-01]](#ref-p-01) |
| DS-TTS: Zero-Shot Speaker Style Adaptation (2026) | 단일 오디오 샘플로 화자 음성 합성. Dual-Style Encoding + Dynamic Generator | [[P-02]](#ref-p-02) |
| CosyVoice 2 (FunAudioLLM, 2024-12) | 스트리밍 150ms, 발음 오류 30~50% 감소, MOS 5.53 | [[P-03]](#ref-p-03) |

### 전략적 시사점

**기회**
- Anthropic ElevenLabs OEM은 "LLM 기업에 TTS를 B2B 납품"하는 수익 모델 검증. 한국 LLM 기업(Naver 등)에도 유사 파트너십 기회
- Google Speech-to-Speech 번역(70언어)이 한국어 통·번역 제품과 직접 경쟁 — 위협이자 API 활용 기회

**위협**
- Big Tech TTS가 자사 플랫폼에 번들 통합 → 독립 TTS API 기업 가격 경쟁력 위협
- EU AI Act Article 50(2026-08) 합성음 라벨링 의무 시행 → 컴플라이언스 미비 시 B2B 리스크
- 오픈소스 경량 TTS(Kyutai Pocket 100M, Kokoro 82M)의 품질 추격 → 온프레미스 선호 고객 API 이탈 가속

---

## 🔴 Voice Cloning — 긴급

> 상세 리서치: [2026-03-17_research-voice-cloning.md](2026-03-17_research-voice-cloning.md)

### 이전 대비 변화
- **전주**: ElevenLabs $500M Series D($11B), Qwen3-TTS·Chatterbox 오픈소스 공세, Play.ht 종료
- **금주**: ElevenLabs SXSW 3방향 전략(접근성+B2B 라이선싱+플랫폼 통합), YouTube 딥페이크 탐지 정치인 확대, Hume AI→Google DeepMind 이동
- **변화 방향**: ElevenLabs가 기술 → 사회 인프라·브랜딩·엔터테인먼트로 지배력 확장. 규제 압박이 탐지·투명성 투자를 가속

### 기술 동향

1. **ElevenLabs "1 Million Voices" — $1B 현물 투자, 음성 복원 무상 제공.**
   ALS·뇌졸중 환자 100만 명 대상. 소량 과거 녹음으로 화자 음성 재건 → TTS 인터페이스 탑재. 배우 Eric Dane(ALS) 유산 기리며 시작. [[G-06]](#ref-g-06) [[G-10]](#ref-g-10)

2. **ElevenLabs Iconic Voice Marketplace — 28개 유명인 음성 라이선스.**
   Michael Caine, Matthew McConaughey 등 포함. CMG Worldwide 에스테이트 네트워크 활용. 동의(consent-only) 원칙, 70언어. 광고·나레이션·게임·더빙 활용. [[G-09]](#ref-g-09) [[G-11]](#ref-g-11)

3. **ElevenCreative 멀티모달 플랫폼 공식 런칭 (2026-03-10).**
   음성·음악·영상·이미지 통합 제작 환경. 70언어 팟캐스트 더빙, 보이스 클로닝, Conversational AI 멀티모달 기능 포함. [[G-12]](#ref-g-12)

4. **OpenAI Voice Engine — 2년째 일반 배포 지연.**
   2024-03 발표 후 안전성 검토가 병목. 선정 파트너사에만 제한 제공. ElevenLabs가 이 공백을 활용해 생태계 확장 중. [[G-13]](#ref-g-13)

5. **Google Chirp 3 Instant Custom Voice — EU·미국 리전 확대, 30개+ 로케일.**
   Google Meet AI 음성 번역에 보이스 클로닝 기반 "immersive voice" 라이브 데모. 오디오 미보존(zero retention) 정책으로 프라이버시 리스크 완화. [[G-14]](#ref-g-14)

6. **YouTube 딥페이크 탐지 도구 확대 (2026-03-10).**
   정치인·정부 관료·언론인 대상 확대. 음성 딥페이크 탐지도 로드맵에 포함. 플랫폼 레벨 음성 진위 검증 인프라 구축 시작. [[G-15]](#ref-g-15)

### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | SXSW: 1M Voices($1B) + Iconic Marketplace(28명) + ElevenCreative. Claude Code TTS 공급. 7,000명 지원, 800+ 파트너 | [[G-06]](#ref-g-06) [[G-09]](#ref-g-09) [[G-12]](#ref-g-12) |
| OpenAI | Voice Engine 2년째 지연. gpt-4o-mini-tts 제한적 Custom Voices. 안전성 검토 병목 | [[G-13]](#ref-g-13) |
| Google | Chirp 3 EU·미국 확대(30+ 로케일). Meet 보이스 클로닝 번역 데모. Hume AI 팀 DeepMind 합류 | [[G-14]](#ref-g-14) [[G-16]](#ref-g-16) |
| YouTube | 딥페이크 탐지 정치인·언론인 확대(2026-03-10). 음성 탐지 로드맵 포함 | [[G-15]](#ref-g-15) |
| Microsoft | Azure Personal Voice DragonV2.1, VibeVoice-1.5B HuggingFace 공개. 100언어 | [[G-17]](#ref-g-17) |

### 시장 시그널
- 글로벌 보이스 클로닝 시장: 2026년 $1.1~4.1B, 2030년 $9.6~10.8B(CAGR 23~26%)
- 아시아태평양 CAGR 28.1%로 글로벌 평균 초과 — 한국·일본·인도 주요 성장 거점
- ElevenLabs의 Iconic Marketplace: 유명인 음성 라이선싱이 새로운 B2B 수익 모델로 제도화
- EU AI Act 2026-08 전면 시행: 합성 음성 투명성 표기 의무 → 중소 사업자 진입장벽 상승

### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| Targeted Speaker Poisoning (arXiv 2603.07551, 2026-03-08) | 제로샷 TTS 특정 화자 학습 삭제(machine unlearning) 프레임워크. 15명까지 효과적 | [[P-04]](#ref-p-04) |
| Fed-PISA: Federated Voice Cloning (2025-09) | 연합학습 기반 보이스 클로닝. ID-LoRA 로컬 보존, style-LoRA만 서버 전송 | [[P-05]](#ref-p-05) |
| Voice Cloning: Comprehensive Survey (2025-05) | Few/zero-shot·다국어·화자 적응 종합 서베이. Representation disentanglement 핵심 | [[P-06]](#ref-p-06) |

### 전략적 시사점

**기회**
- Iconic Marketplace 모델을 한국 연예인·방송인에 적용 가능. 한류 다국어 AI 더빙 수요와 연결
- ElevenLabs "1M Voices" 공익 프레임: 국내 언어 장애 환자 대상 음성 복원 사업 가능성

**위협**
- OpenAI Voice Engine 배포 지연은 안전성 요건 높다는 신호 — 동의 없는 보이스 클로닝 규제 표적 가능
- YouTube 딥페이크 탐지 확대 + EU AI Act → 무단 클로닝 콘텐츠 배포 창구 차단 가속

---

## 🟡 Emotional Analysis — 주목

> 상세 리서치: [2026-03-17_research-emotional-analysis.md](2026-03-17_research-emotional-analysis.md)

### 이전 대비 변화
- **전주**: Google DeepMind Hume AI acqui-hire, 마고 CES 2026 감정인식 데모, 음성 바이오마커 임상 가속
- **금주**: Foundation Model zero-shot SER 학술 공식화, MME-Emotion(ICLR 2026) 첫 벤치마크, Hume AI EVI 3 출시
- **변화 방향**: "특화 모델 vs. Foundation Model" 경쟁 구도 핵심화. 정확도 경쟁 → 벤치마크 표준화 단계 진입

### 기술 동향

1. **Foundation Model zero-shot SER — Nature npj AI에서 학술 공식화.**
   "Affective computing has changed: the foundation model disruption" (Liang et al.). SenseVoice-Small(Alibaba)이 파인튜닝 없이 기존 SER SOTA 초과 달성. 데이터 수집·어노테이션 비용 패러다임 붕괴. [[G-18]](#ref-g-18)

2. **MME-Emotion — ICLR 2026, LLM 감정 지능 첫 종합 벤치마크.**
   6,500 비디오, 27 시나리오, 8 태스크. 최고 성능 Gemini-2.5-Pro가 39.3%에 불과 — 현존 LLM의 감정 지능에 구조적 한계 수치화. [[G-19]](#ref-g-19)

3. **Hume AI EVI 3 출시 — Google acqui-hire 후 독립 신모델.**
   신임 CEO Andrew Ettinger 체제. 200K+ 목소리 커스터마이제이션, 30초 클로닝, 300ms 이하 레이턴시. Claude 4·Gemini 2.5·Kimi K2 통합 지원. [[G-20]](#ref-g-20)

4. **SKT 멘탈비전 사내 정식 출시 (2025-09).**
   음성 4문장 + 얼굴 스캔 → 불안감·우울감 분석 → 맞춤 프로그램 추천. 보컬비전 식약처 의료기기 허가 취득. 2026년 외부 서비스 확장 준비 중. [[E-01]](#ref-e-01)

### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Google DeepMind | Hume AI CEO + 7명 합류(2026-01). Gemini 음성 감정 통합 진행 중 | [[G-16]](#ref-g-16) |
| Hume AI | EVI 3 출시. 신임 CEO 체제. Claude 4·Gemini 2.5 통합. GPT-4o 대비 감정 표현 우위 주장 | [[G-20]](#ref-g-20) |
| Alibaba (FunAudioLLM) | SenseVoice-Small zero-shot SER SOTA. MME-Emotion 벤치마크 개발(ICLR 2026) | [[G-18]](#ref-g-18) [[G-19]](#ref-g-19) |
| OpenAI | GPT-4o 안면 감정인식 86%(NimStim). Advanced Voice Mode 감정 적응형 응답 | [[G-21]](#ref-g-21) |
| SKT | 멘탈비전 사내 출시(2025-09). 보컬비전 식약처 허가. 음성+얼굴 멀티모달 | [[E-01]](#ref-e-01) |

### 시장 시그널
- 감정 AI 시장: $5.7B(2023) → $38.5B(2035), CAGR 20.9% (Roots Analysis)
- 음성 감정 세그먼트 CAGR 22%+로 감정 AI 내 최고 성장
- Foundation Model 패러다임 전환: 특화 어노테이션 불필요 → 진입장벽 하락, 동시에 Foundation Model 보유 기업 경쟁 우위 강화
- ACII 2026: 9월 7~10일, 멕시코 Puebla. 논문 마감 2026-03-27

### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| Affective computing has changed (Liang et al., npj AI 2025) | Foundation Model이 zero-shot으로 SER SOTA 달성. 어노테이션 패러다임 붕괴 | [[P-07]](#ref-p-07) |
| MME-Emotion (FunAudioLLM, ICLR 2026) | 6,500 비디오·8 태스크. Gemini-2.5-Pro 최고 39.3%. LLM 감정 지능 한계 수치화 | [[P-08]](#ref-p-08) |
| SER in Mental Health (JMIR, 2025-09) | 3,648편 → 14편. 우울증 53%. 임상 보완 가능성 확인, 독립 진단 대체는 미달 | [[P-09]](#ref-p-09) |
| LLM facial emotion (npj Digital Medicine, 2025) | GPT-4o 86%, Gemini 84%, Claude 74% (NimStim). 인간 수준 이상 | [[P-10]](#ref-p-10) |

### 전략적 시사점

**기회**
- Foundation Model zero-shot SER: 어노테이션 비용 급감 → 벤치마크 설계자가 시장 표준 주도
- SKT 보컬비전 식약처 허가 선례: 국내 음성 바이오마커 의료기기 인허가 경로 가시화
- 멀티모달(음성+얼굴) 조합이 성능 한계 보완의 확실한 경로

**위협**
- MME-Emotion 결과(39.3%)는 감정 AI 미성숙 → 제품화 시 과대 선전 리스크
- Gemini·GPT-4o가 감정 인식을 내재화하면 독립 감정 AI API 차별화 근거 희박
- EU AI Act 감정 인식 규제: 공공 공간 실시간 제한 → B2B·동의 기반으로 도메인 수렴

---

## 🟡 Interrupt & Turn-Taking — 주목

> 상세 리서치: [2026-03-17_research-interrupt-turn-taking.md](2026-03-17_research-interrupt-turn-taking.md)

### 이전 대비 변화
- **전주**: Full-duplex 주류화, NVIDIA PersonaPlex 170ms, LiveKit EOU 오탐 85%↓, Deepgram Flux
- **금주**: Full-Duplex-Bench 수치 공개, OpenAI gpt-realtime 정식(베타 졸업), LiveKit 한국어 지원, Magic Data 한국어 데이터셋
- **변화 방향**: 한국어 지원 공백이 부분 해소. 평가 인프라 수치화로 경쟁 가시화. OpenAI full-duplex 전환 공식화

### 기술 동향

1. **Full-Duplex-Bench — 턴테이킹 정량 평가 표준 확립.**
   4축 평가: Pause Handling, Backchanneling, Turn-Taking, Interruption. Gemini Live Turn-Taking Latency 1.301s vs Moshi 0.265s — 상용 클라우드의 반응 속도 한계 수치화. [[P-11]](#ref-p-11)

2. **OpenAI gpt-realtime — 베타 졸업, Semantic VAD 정식 지원.**
   `semantic_vad` 모드 공식 지원: "음..." 같은 일시 정지를 턴 종료로 오인 방지. instruction-following +18.6%p, tool-calling +12.9%p. [[G-22]](#ref-g-22)

3. **OpenAI 차세대 Full-Duplex 아키텍처 Q1 2026 목표.**
   오디오 팀 통합, "동시 발화" 처리 신규 아키텍처 개발 중. 공식 발표 미확인(2026-03-17 기준). [[G-23]](#ref-g-23)

4. **LiveKit turn-detector v0.4.1-intl — 한국어 포함 14개 언어, 오탐 39%↓ 추가.**
   v0.3.0-intl 대비 오탐 39.23% 추가 감소. RAM ~400MB, 추론 ~25ms. 한국어 공식 포함. [[G-24]](#ref-g-24)

5. **NVIDIA PersonaPlex-7B — FullDuplexBench SOTA.**
   실측: Turn-Taking 0.170s, Interruption 0.240s. ICASSP 2026 채택. 단일 Transformer로 파이프라인 지연 제거. [[G-25]](#ref-g-25)

6. **Magic Data 다국어 full-duplex 데이터셋 — 한국어 포함.**
   한국어 경어체·감정 종결어미·빠른 턴테이킹 반영. 독립 채널 분리(오버랩 포함). 상업 라이선스. [[G-26]](#ref-g-26)

### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| OpenAI | gpt-realtime 정식 출시. Semantic VAD 공식. Q1 2026 동시 발화 아키텍처 개발 중 | [[G-22]](#ref-g-22) [[G-23]](#ref-g-23) |
| Google | Gemini Live API Proactive Audio + barge-in 개선. 서버사이드 VAD 인터럽트 즉시 처리 | [[G-27]](#ref-g-27) |
| Meta | SyncLLM: Llama-3-8B 기반 full-duplex, 160~240ms 청크. EMNLP 2024 | [[P-12]](#ref-p-12) |
| NVIDIA | PersonaPlex-7B: Turn-Taking 0.170s. FullDuplexBench SOTA. ICASSP 2026 | [[G-25]](#ref-g-25) |
| LiveKit | v0.4.1-intl: 한국어 포함 14개 언어. 오탐 39%↓ 추가. ~25ms 추론 | [[G-24]](#ref-g-24) |
| Deepgram | Flux: 동적 EOT 감지 ~260ms. Telnyx 등 통신사 배포 확대 | [[G-28]](#ref-g-28) |
| Huawei | MWC 2026: AICC 차세대 Voice Virtual Agent. 자기해결률 20%↑ 주장 | [[E-02]](#ref-e-02) |

### 시장 시그널
- Full-Duplex-Bench: 정량 비교 기준점 확립. 오픈소스 Moshi가 상용 Gemini Live를 반응 속도에서 5배 앞서는 결과
- OpenAI Realtime API 베타 졸업: 인터럽트·턴 감지를 기업 도입 가능 수준으로 공식화
- 한국어 full-duplex 인프라 구축 시작: LiveKit 한국어 모델 + Magic Data 한국어 데이터셋 동시 등장
- Edge full-duplex: sub-100ms AEC+VAD가 표준 요구 사항으로 정착

### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| Full-Duplex-Bench (Gao et al., 2025) | 4축 정량 평가. Gemini Live 1.301s vs Moshi 0.265s. 상용 vs 오픈소스 격차 수치화 | [[P-11]](#ref-p-11) |
| SyncLLM (Tu et al., Meta/UW, 2024) | Llama-3-8B wall-clock 동기화 full-duplex. 212k시간 합성 데이터 | [[P-12]](#ref-p-12) |
| PersonaPlex (NVIDIA, ICASSP 2026) | 단일 Transformer ASR+LLM+TTS 통합. 0.170s Turn-Taking | [[P-13]](#ref-p-13) |
| ICASSP 2026 HumDial Challenge | Full-Duplex Interaction 공식 경쟁 트랙 신설 | [[P-14]](#ref-p-14) |

### 전략적 시사점

**기회**
- LiveKit 한국어 모델(25ms, 400MB) + Magic Data 데이터셋: 한국어 시맨틱 턴 감지 즉시 구현 가능
- Full-Duplex-Bench 수치로 Gemini Live 1.3s 대비 경쟁력 있는 제품 스펙 수립 가능
- OpenAI Realtime API 정식 출시: 빠른 프로토타이핑 경로 확보

**위협**
- 오픈소스(Moshi 0.27s)가 상용(Gemini 1.3s) 반응 속도 5배 앞서 — 클라우드 API 의존 전략 한계
- OpenAI Q1 신규 아키텍처 완성 시 현재 반이중 시스템과의 격차 급확대 우려
- NVIDIA PersonaPlex·Meta SyncLLM의 단일 Transformer 성숙 시 기존 STT+LLM+TTS 파이프라인 재설계 압박
- Huawei AICC 통신사 채널 배포: SKT·KT 플랫폼 전략에 직접 경쟁 변수

---

## 경쟁사 동향 (SKT / KT)

> 이번 주 Voice AI 도메인과 관련된 SKT·KT의 주요 움직임.

### SKT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| MWC 2026 익시오(ixi-O) 확장 전략 | 홍 CEO: "음성이 다시 사람을 연결하는 본질적 수단" — 통화 맥락 이해·보이스피싱 탐지·실시간 검색을 스마트안경·자율주행차·휴머노이드에 연결 | context-recognition, spam-phishing-detection | [[E-03]](#ref-e-03) |
| 멘탈비전 사내 출시 (2025-09) | 음성 4문장 + 얼굴 → 불안·우울 분석. 보컬비전 식약처 의료기기 허가. 2026 외부 확장 준비 | emotional-analysis | [[E-01]](#ref-e-01) |

### KT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| 6G = AI 인프라 전략 | MWC 2026에서 6G를 단순 속도 경쟁이 아닌 'AI 인프라'로 재정의 선언 | (L3 밖) | [[E-03]](#ref-e-03) |
| KT AI 보이스 스튜디오 종료 | 2025-03-31부로 서비스 종료 | voice-synthesis | [[E-04]](#ref-e-04) |

### 시사점
- SKT는 익시오를 통해 Voice AI를 멀티디바이스 AI 플랫폼으로 확장하는 전략. 통화 맥락 이해(Context Recognition)와 보이스피싱 탐지가 핵심 기능.
- SKT 멘탈비전의 식약처 의료기기 허가는 국내 음성 감정인식 임상 적용의 선례. 2026년 외부 서비스 확장 시 B2C 시장 형성 가능성.
- KT는 AI 보이스 스튜디오 종료로 TTS 자체 서비스에서 후퇴. 6G AI 인프라 전략에 집중하는 방향.

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **ElevenLabs의 수직 통합 전략이 Voice AI 전체를 관통한다.** Voice Synthesis(Anthropic OEM)·Voice Cloning(1M Voices + Iconic Marketplace)·Emotional Analysis(Hume AI EVI 3 통합)·Turn-Taking(Claude Code 음성모드) 전 영역에서 ElevenLabs가 핵심 인프라로 자리잡고 있다. 단일 기업의 생태계 영향력이 W11 대비 현저히 확대됐다.

2. **한국어 Voice AI 인프라가 W12에 처음으로 가시화됐다.** LiveKit 한국어 턴 감지 모델 + Magic Data 한국어 full-duplex 데이터셋의 동시 등장. 그러나 TTS·감정 인식·보이스 클로닝에서의 한국어 특화 모델은 여전히 부재 — Naver HyperCLOVA X가 유일한 고품질 한국어 TTS.

3. **"플랫폼 통합 > 단일 모델 성능"이 W12의 메타 트렌드.** Google(Gemini TTS+번역+Meet), OpenAI(Realtime API 정식+Semantic VAD), Anthropic(Claude Code+ElevenLabs), ElevenLabs(ElevenCreative 멀티모달) — 모든 주요 플레이어가 개별 기술이 아닌 플랫폼 번들 전략으로 전환 중.

4. **규제 타임라인이 구체화되고 있다.** EU AI Act Article 50(2026-08), 미국 뉴욕주 합성 퍼포머 공시(2026-06), YouTube 딥페이크 탐지 확대. 감정 인식·보이스 클로닝·TTS 전 영역에 걸쳐 컴플라이언스 요구 사항 증가.

### 후속 조치 제안

- 🔴 Voice Synthesis 플랫폼 전환: Google Gemini TTS 멀티스피커+번역이 한국어 통번역 제품과 직접 경쟁 → 자사 Voice AI 전략 재검토 권고
- 🔴 Voice Cloning 규제 대응: EU AI Act 2026-08 시행 대비 합성 음성 투명성 표기 컴플라이언스 스택 점검
- 🟡 한국어 Full-Duplex 파일럿: LiveKit 한국어 모델 + Magic Data 데이터셋 활용 PoC 검토
- 🟡 SKT 멘탈비전 외부 확장 모니터링: 음성 감정인식 B2C 시장 형성 시 경쟁 구도 변화

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Google Blog — Gemini 2.5 Native Audio upgrade + TTS model updates | [링크](https://blog.google/products/gemini/gemini-audio-model-updates/) | blog | 2025-12-12 | [A] |
| <a id="ref-g-02"></a>G-02 | Google Blog — Gemini 2.5 Text-to-Speech model updates | [링크](https://blog.google/technology/developers/gemini-2-5-text-to-speech/) | blog | 2025-12-12 | [A] |
| <a id="ref-g-03"></a>G-03 | OpenAI Developer Blog — Updates for developers building with voice | [링크](https://developers.openai.com/blog/updates-audio-models/) | blog | 2025-12-22 | [A] |
| <a id="ref-g-04"></a>G-04 | TechCrunch — Claude Code rolls out a voice mode capability | [링크](https://techcrunch.com/2026/03/03/claude-code-rolls-out-a-voice-mode-capability/) | news | 2026-03-03 | [B] |
| <a id="ref-g-05"></a>G-05 | The Decoder — Anthropic's Claude uses ElevenLabs technology for speech | [링크](https://the-decoder.com/anthropics-claude-uses-elevenlabs-technology-for-speech-features-rather-than-an-in-house-model/) | news | 2026-03-03 | [B] |
| <a id="ref-g-06"></a>G-06 | PR Newswire — ElevenLabs '11 Voices' docuseries at SXSW, 1M Voices | [링크](https://www.prnewswire.com/news-releases/elevenlabs-debuts-11-voices-docuseries-at-sxsw-as-part-of-global-campaign-to-reach-1-million-people-with-voice-loss-302711275.html) | press | 2026-03-11 | [A] |
| <a id="ref-g-07"></a>G-07 | AWS — Cartesia Sonic-3 on Amazon SageMaker JumpStart | [링크](https://aws.amazon.com/about-aws/whats-new/2026/02/cartesia-sonic-3-on-sagemaker-jumpstart/) | news | 2026-02 | [A] |
| <a id="ref-g-08"></a>G-08 | Artificial Analysis — Text to Speech Leaderboard | [링크](https://artificialanalysis.ai/text-to-speech/leaderboard) | tool | 2026-03 | [B] |
| <a id="ref-g-09"></a>G-09 | AdWeek — ElevenLabs AI Voice Licensing Marketplace, McConaughey | [링크](https://www.adweek.com/media/elevenlabs-ai-voice-marketplace-matthew-mcconaughey/) | news | 2026-03 | [B] |
| <a id="ref-g-10"></a>G-10 | ElevenLabs Blog — Honoring Eric Dane's Legacy, 1 Million Voices | [링크](https://elevenlabs.io/blog/honoring-eric-danes-legacy-at-sxsw-advancing-1-million-voices) | blog | 2026-03-11 | [A] |
| <a id="ref-g-11"></a>G-11 | ElevenLabs Blog — Partnership with Sir Michael Caine, Iconic Marketplace | [링크](https://elevenlabs.io/blog/announcing-partnership-with-sir-michael-caine-to-newly-launched-iconic-marketplace) | blog | 2026-03 | [A] |
| <a id="ref-g-12"></a>G-12 | Blockchain.news — ElevenLabs ElevenCreative Multimodal AI | [링크](https://blockchain.news/ainews/elevenlabs-launches-elevencreative-account-multimodal-ai-for-voice-cloning-70-language-dubbing-and-music-generation-latest-2026-update) | news | 2026-03-10 | [B] |
| <a id="ref-g-13"></a>G-13 | TechCrunch — OpenAI still hasn't released voice cloning tool | [링크](https://techcrunch.com/2025/03/06/a-year-later-openai-still-hasnt-released-its-voice-cloning-tool/) | news | 2025-03-06 | [B] |
| <a id="ref-g-14"></a>G-14 | Google Cloud Docs — Chirp 3 Instant Custom Voice Release Notes | [링크](https://docs.cloud.google.com/text-to-speech/docs/chirp3-instant-custom-voice) | doc | 2026-03 | [A] |
| <a id="ref-g-15"></a>G-15 | TechCrunch — YouTube expands AI deepfake detection to politicians | [링크](https://techcrunch.com/2026/03/10/youtube-expands-ai-deepfake-detection-to-politicians-government-officials-and-journalists/) | news | 2026-03-10 | [B] |
| <a id="ref-g-16"></a>G-16 | TechCrunch — Google snags team behind Hume AI | [링크](https://techcrunch.com/2026/01/22/google-reportedly-snags-up-team-behind-ai-voice-startup-hume-ai/) | news | 2026-01-22 | [B] |
| <a id="ref-g-17"></a>G-17 | Microsoft Tech Community — Personal Voice v2.1 Azure AI Speech | [링크](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/personal-voice-upgraded-to-v2-1-in-azure-ai-speech-more-expressive-than-ever-bef/4435233) | blog | 2026 | [A] |
| <a id="ref-g-18"></a>G-18 | Nature npj AI — Affective computing has changed: foundation model disruption | [링크](https://www.nature.com/articles/s44387-025-00061-3) | paper | 2025 | [A] |
| <a id="ref-g-19"></a>G-19 | OpenReview — MME-Emotion: Holistic Evaluation Benchmark (ICLR 2026) | [링크](https://openreview.net/forum?id=oSX9aenbea) | paper | 2026 | [A] |
| <a id="ref-g-20"></a>G-20 | Hume AI Blog — Introducing EVI 3 | [링크](https://www.hume.ai/blog/introducing-evi-3) | blog | 2025 | [B] |
| <a id="ref-g-21"></a>G-21 | npj Digital Medicine — LLMs identifying human facial emotions | [링크](https://www.nature.com/articles/s41746-025-01985-5) | paper | 2025 | [A] |
| <a id="ref-g-22"></a>G-22 | OpenAI — gpt-realtime and Realtime API updates | [링크](https://community.openai.com/t/introducing-gpt-realtime-and-realtime-api-updates-for-production-voice-agents/1355039) | blog | 2025-12-22 | [A] |
| <a id="ref-g-23"></a>G-23 | Implicator — OpenAI merges audio teams, new voice architecture by March 2026 | [링크](https://www.implicator.ai/openai-merges-audio-teams-targets-new-voice-architecture-by-march-2026/) | news | 2026-01 | [B] |
| <a id="ref-g-24"></a>G-24 | LiveKit — Improved End-of-Turn Model Cuts Interruptions 39% | [링크](https://blog.livekit.io/improved-end-of-turn-model-cuts-voice-ai-interruptions-39/) | blog | 2025-12 | [B] |
| <a id="ref-g-25"></a>G-25 | NVIDIA — PersonaPlex: Natural Conversational AI | [링크](https://research.nvidia.com/labs/adlr/personaplex/) | news | 2026-01-15 | [A] |
| <a id="ref-g-26"></a>G-26 | MagicHub — Multilingual Full-Duplex Conversational Speech Datasets | [링크](https://magichub.com/large-scale-multilingual-full-duplex-conversational-speech-datasets-accelerating-voice-ai-industrialization-with-magic-data/) | news | 2026 | [B] |
| <a id="ref-g-27"></a>G-27 | Google Cloud Blog — Gemini Live API Native Audio in Vertex AI | [링크](https://cloud.google.com/blog/topics/developers-practitioners/how-to-use-gemini-live-api-native-audio-in-vertex-ai) | blog | 2026 | [A] |
| <a id="ref-g-28"></a>G-28 | Telnyx — Deepgram Flux Voice AI Release | [링크](https://telnyx.com/release-notes/deepgram-flux-voice-ai-release) | news | 2026 | [B] |
| <a id="ref-e-01"></a>E-01 | SKT 뉴스룸 — 멘탈비전 AI 음성 분석 마음건강 | [링크](https://news.sktelecom.com/214844) | IR/발표 | 2025-09-04 | [A] |
| <a id="ref-e-02"></a>E-02 | Huawei — Next-Gen Voice Virtual Agents for AICC (MWC 2026) | [링크](https://www.huawei.com/en/news/2026/3/mwc-voice-interaction-aicc) | IR/발표 | 2026-03-02 | [A] |
| <a id="ref-e-03"></a>E-03 | WithNews — 통신사 AI 인프라 전쟁 MWC 2026 | [링크](https://car.withnews.kr/economy/telecom-companies-ai-infrastructure-war-mwc-2026) | news | 2026-03 | [B] |
| <a id="ref-e-04"></a>E-04 | KT AI 보이스 스튜디오 — 서비스 종료 안내 | [링크](https://aivoicestudio.ai/) | web | 2025-03-31 | [B] |
| <a id="ref-p-01"></a>P-01 | Mohanty — Causal Prosody Mediation for TTS (arXiv 2603.11683) | [링크](https://arxiv.org/abs/2603.11683) | paper | 2026-03-12 | [A] |
| <a id="ref-p-02"></a>P-02 | DS-TTS — Zero-Shot Speaker Style Adaptation | [링크](https://arxiv.org/html/2506.01020v1) | paper | 2026 | [A] |
| <a id="ref-p-03"></a>P-03 | FunAudioLLM — CosyVoice 2 Scalable Streaming TTS (arXiv 2412.10117) | [링크](https://arxiv.org/abs/2412.10117) | paper | 2024-12 | [A] |
| <a id="ref-p-04"></a>P-04 | Targeted Speaker Poisoning in Zero-Shot TTS (arXiv 2603.07551) | [링크](https://arxiv.org/abs/2603.07551) | paper | 2026-03-08 | [A] |
| <a id="ref-p-05"></a>P-05 | Fed-PISA — Federated Voice Cloning (arXiv 2509.16010) | [링크](https://arxiv.org/html/2509.16010v1) | paper | 2025-09 | [A] |
| <a id="ref-p-06"></a>P-06 | Voice Cloning: Comprehensive Survey (arXiv 2505.00579) | [링크](https://arxiv.org/abs/2505.00579) | paper | 2025-05 | [A] |
| <a id="ref-p-07"></a>P-07 | Liang et al. — Affective Computing Foundation Model Disruption (arXiv 2409.08907) | [링크](https://arxiv.org/abs/2409.08907) | paper | 2025 | [A] |
| <a id="ref-p-08"></a>P-08 | FunAudioLLM — MME-Emotion (arXiv 2508.09210, ICLR 2026) | [링크](https://arxiv.org/abs/2508.09210) | paper | 2026 | [A] |
| <a id="ref-p-09"></a>P-09 | JMIR — SER in Mental Health: Systematic Review | [링크](https://mental.jmir.org/2025/1/e74260) | paper | 2025-09 | [A] |
| <a id="ref-p-10"></a>P-10 | npj Digital Medicine — LLMs identifying facial emotions | [링크](https://www.nature.com/articles/s41746-025-01985-5) | paper | 2025 | [A] |
| <a id="ref-p-11"></a>P-11 | Gao et al. — Full-Duplex-Bench (arXiv 2503.04721) | [링크](https://arxiv.org/abs/2503.04721) | paper | 2025-03-06 | [A] |
| <a id="ref-p-12"></a>P-12 | Tu et al. — SyncLLM: Full-Duplex Dialogue Agents (arXiv 2409.15594) | [링크](https://arxiv.org/abs/2409.15594) | paper | 2024-09 | [A] |
| <a id="ref-p-13"></a>P-13 | NVIDIA — PersonaPlex: Full Duplex Conversational AI (ICASSP 2026) | [링크](https://research.nvidia.com/labs/adlr/files/personaplex/personaplex_preprint.pdf) | paper | 2026-01 | [A] |
| <a id="ref-p-14"></a>P-14 | ICASSP 2026 HumDial Challenge (arXiv 2601.05564) | [링크](https://arxiv.org/abs/2601.05564) | paper | 2026-02-04 | [A] |
