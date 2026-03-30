---
type: weekly-deep-research
topic: interrupt-turn-taking
date: 2026-03-30
parent: 2026-03-30_weekly-voice-ai.md
agent: research-deep
confidence: high
status: completed
sources_used: [websearch]
---

# Deep 리서치: Interrupt & Turn-Taking (2026-W14)

> **조사 범위**: 2026-03-23 ~ 2026-03-30 / 기술·시장·경쟁 동향 종합
> **MCP 상태**: intel-store MCP 미호출 (VSCode 확장 환경 제약) — WebSearch 전량 대체. 수집 품질 [B] 이상.
> **추적 키워드**: xAI Grok, ElevenLabs, IBM, SoundHound, LiveKit, Deepgram, AssemblyAI, Retell AI, turn-taking, barge-in, full-duplex, interrupt detection

---

## 이전 대비 변화

- **전주 (W13, 2026-03-24)**: ElevenLabs Conversational AI (CA) 2.0 출시 — 독자 턴테이킹 신경망 + 인터럽트 감지 정확도 95% 주장. 음성 에이전트 인프라 투자 폭증 (LiveKit $100M, ElevenLabs $500M, Synthflow $20M, Newo.ai $25M, Hamming.ai $3.8M). τ-Voice 벤치마크(arXiv 2603.13686) 발표. Deepgram Flux EOT ~260ms.
- **금주 (W14, 2026-03-30)**: xAI Grok Voice Agent API 신규 진입 — OpenAI Realtime API 호환, LiveKit 플러그인 탑재, TTFA(Time to First Audio) <1s, Big Bench Audio 1위, $0.05/분 최저가 포지셔닝. ElevenLabs-IBM watsonx Orchestrate 통합(3/25) — 70개 언어 AI 전화 에이전트 엔터프라이즈 확장. SoundHound AI Aragon Research Globe Agent Platforms 2026 리더 선정(3/26). AssemblyAI Universal-3 Pro Streaming 출시 — VAD 이후 ~150ms P50 레이턴시. 의미 기반 인터럽트 감지 전용 논문(arXiv 2603.24144, ICME 2026) 공개.
- **변화 방향**: LLM 빅테크(xAI)의 음성 에이전트 직접 진입으로 인프라 경쟁 축이 재편되고 있음. 플랫폼 파트너십(ElevenLabs-IBM)이 엔터프라이즈 채널 확장의 주요 전략으로 부상. 학술계에서 인터럽트 감지 전용 벤치마크·지표·모델 연구가 독립 연구 영역으로 분리되는 시그널.

---

## 기술 동향

1. **xAI Grok Voice Agent API — OpenAI Realtime API 호환 신규 진입, <1s TTFA·Big Bench Audio 1위.**
   xAI가 Grok Voice Agent API를 공개했다. OpenAI Realtime API 스펙과 완전 호환되며 xAI 공식 LiveKit 플러그인을 통해 턴 감지 설정을 커스터마이징할 수 있다. 텍사스 모바일 앱과 Tesla 차량 내 Grok Voice에 사용하던 동일 스택을 API로 개방했으며, 평균 TTFA(Time to First Audio) <1s로 "경쟁사 대비 5배 빠름"을 자사 기준으로 주장한다 [추가확인 필요]. Big Bench Audio 음성 추론 벤치마크 1위를 기록했다. 가격은 $0.05/분(연결 시간 기준)으로 경쟁 대비 최저가 포지셔닝이다. 향후 독립 TTS·STT 엔드포인트와 강화된 오디오 모델을 추가 출시 예고했다 [[G-01]](#ref-g-01), [[G-02]](#ref-g-02), [[G-03]](#ref-g-03), [[E-01]](#ref-e-01).

2. **ElevenLabs CA 2.0 엔터프라이즈 확장 — IBM watsonx Orchestrate 통합으로 70개 언어 AI 전화 에이전트.**
   3월 25일 ElevenLabs와 IBM이 TTS(Text-to-Speech) 및 STT(Speech-to-Text)를 IBM watsonx Orchestrate에 통합하는 파트너십을 발표했다. 10,000+ 보이스 라이브러리·70개 언어·멀티 지역 억양을 기업 AI 전화 에이전트에 즉시 적용할 수 있다. PCI 준수, HIPAA 데이터 핸들링 지원, 데이터 레지던시 옵션을 포함한 엔터프라이즈 보안을 제공한다. 금융·의료·유틸리티·보험사를 주요 타깃으로 명시했다. CA 2.0의 턴테이킹 신경망(Eager/Normal/Patient 3단계, Turn Timeout 1~30초)이 이 파트너십의 기술 기반으로 작동한다 [[G-04]](#ref-g-04), [[G-05]](#ref-g-05), [[E-02]](#ref-e-02), [[E-03]](#ref-e-03).

3. **AssemblyAI Universal-3 Pro Streaming — 음향+의미 통합 엔드포인팅, ~150ms P50 레이턴시 달성.**
   AssemblyAI가 3월 24일 음성 에이전트용 최고 정확도 실시간 전사 모델 Universal-3 Pro Streaming을 출시했다. VAD 엔드포인트 감지 이후 P50 ~150ms 레이턴시, 영어 도메인 WER(Word Error Rate) 8.14%를 달성했다. 신경망 턴 감지 모델이 침묵뿐 아니라 발화 의미·흐름을 분석하여 end_of_turn_confidence_threshold 초과 시 즉시 턴을 종료하고, 미달 시 VAD 기반 max_turn_silence 폴백을 사용하는 이중 방어 구조를 채택했다. 멀티링구얼 Universal-Streaming 출시로 글로벌 지원도 확장됐다 [[G-06]](#ref-g-06), [[G-07]](#ref-g-07).

4. **Semantic-Aware Interruption Detection (arXiv 2603.24144, ICME 2026) — 인터럽트 감지 전용 벤치마크·지표·LLM 모델 동시 제안.**
   Alibaba Qwen 팀이 3월 25일 제출한 논문은 인터럽트 감지를 독립 연구 문제로 분리하여 세 가지 기여를 동시에 제안했다. (1) SID-Bench: 실제 인간 대화에서 구축된 최초의 의미 기반 인터럽트 감지 벤치마크. (2) APT 지표(Average Penalty Time): 오탐(false alarm)과 지연 반응(late response)에 시간적 비용을 부여하는 새 평가 메트릭. (3) LLM 기반 감지 모델: 미세한 의미적 단서 포착을 위한 새로운 학습 패러다임 적용. 기존 VAD 기반 "오탐 과다"와 End-to-End 모델의 "반응 지연" 사이의 구조적 딜레마를 해결 목표로 제시했다 [[P-01]](#ref-p-01).

5. **LiveKit 턴 감지 — VAD·STT 엔드포인팅·모델 기반 3계층 전략, 추론 ~25ms.**
   LiveKit은 음성 에이전트 턴 감지를 위한 세 가지 계층적 접근법(VAD 전용, STT 엔드포인팅, 모델 기반 감지)을 공식 문서화했다. 고유 개발 오픈 웨이트 턴 감지 모델은 Qwen2.5 7B 교사 → 0.5B 학생 모델 지식 증류로 RAM ~400MB, 추론 ~25ms를 실현한다. 실시간 부분 전사를 읽어 의미적 완전성(semantic completeness)으로 턴 종료를 예측하는 방식이며, VAD 트리거 전 조기 턴 종료가 가능해 레이턴시를 추가 단축한다. xAI Grok API 통합이 이 LiveKit 에이전트 프레임워크 위에서 작동한다 [[G-08]](#ref-g-08), [[G-09]](#ref-g-09).

6. **Deepgram Flux — 의미적 턴 감지 + EOT 레이턴시 ~260ms, 오탐 ~30% 감소.**
   Deepgram의 대화형 음성 인식(CSR) 모델인 Flux는 ASR과 턴 감지를 단일 모델에 통합한다. 전통적 침묵 기반 VAD와 달리 "because..." 같은 불완전 발화와 "Thanks." 같은 완결 발화를 의미적으로 구분한다. EOT(End-of-Turn) 감지 레이턴시 중앙값 ~300ms(P95 1.5s), 파이프라인 방식 대비 레이턴시 200~600ms 절감, 오탐 ~30% 감소를 달성했다. eot_threshold·eager_eot_threshold 파라미터로 레이턴시-정확도 트레이드오프를 조정할 수 있다 [[G-10]](#ref-g-10), [[G-11]](#ref-g-11).

7. **Retell AI Interruption Sensitivity Slider — 인터럽트 민감도 API·대시보드 양방향 제어 공개.**
   Retell AI가 Interruption Sensitivity Slider를 API 및 대시보드 모두에서 접근 가능하도록 업데이트했다. interruption_sensitivity 파라미터는 0~1 범위로 설정하며, 0은 인터럽트 완전 차단, 1은 즉각 반응이다. 독자 턴테이킹 모델은 의미 기반 판단으로 사용자의 실제 인터럽트와 배경 소음을 구분하며, "Wait, hold on" 발화 시 <700ms 내 음성 중단을 달성한다. 전체 플랫폼 레이턴시 ~600ms, ARR $40M+ 수준이다 [[G-12]](#ref-g-12), [[G-13]](#ref-g-13).

---

## 플레이어 동향

**주요 플레이어 동향 (2026-W14)**

| 기업 | 동향 | 출처 |
|------|------|------|
| xAI | Grok Voice Agent API 출시. OpenAI Realtime API 호환, LiveKit 플러그인 탑재, TTFA <1s, Big Bench Audio 1위, $0.05/분. Tesla·모바일 동일 스택 | [[G-01]](#ref-g-01), [[E-01]](#ref-e-01) |
| ElevenLabs | IBM watsonx Orchestrate와 TTS/STT 통합(3/25). 70개 언어·10,000+ 보이스, PCI·HIPAA 지원. CA 2.0 엔터프라이즈 확장 | [[G-04]](#ref-g-04), [[E-02]](#ref-e-02) |
| SoundHound AI | Aragon Research Globe Agent Platforms 2026 리더 선정(3/26). 2025년 음성 AI 인터랙션 처리 건수 약 3천만 건(통신·유통). Multi-agent 오케스트레이션 플랫폼 강점 | [[G-14]](#ref-g-14), [[E-04]](#ref-e-04) |
| IBM | watsonx Orchestrate에 ElevenLabs 음성 통합. 기업용 AI 전화 에이전트 강화. 콜센터 비용 40% 절감 사례 인용 | [[G-05]](#ref-g-05), [[E-03]](#ref-e-03) |
| AssemblyAI | Universal-3 Pro Streaming 출시(3/24). ~150ms P50, WER 8.14%. 의미+음향 통합 이중 방어 엔드포인팅 | [[G-06]](#ref-g-06), [[G-07]](#ref-g-07) |
| LiveKit | xAI Grok Voice Agent API 공식 파트너. 턴 감지 3계층 전략 공식화. ~25ms 추론, 14개 언어 모델(한국어 포함) | [[G-02]](#ref-g-02), [[G-08]](#ref-g-08) |
| Deepgram | Flux CSR 모델 EOT ~260ms~300ms. 파이프라인 대비 레이턴시 200~600ms 절감, 오탐 ~30% 감소 | [[G-10]](#ref-g-10), [[G-11]](#ref-g-11) |
| Retell AI | Interruption Sensitivity Slider API·대시보드 공개. ~600ms 전체 레이턴시, ARR $40M+. 인터럽트 0~1 단계 세분화 | [[G-12]](#ref-g-12), [[G-13]](#ref-g-13) |
| Cisco Webex | AI Agent 자체 턴 감지 모델 내장. PSTN 경로 ~1.3s 레이턴시. VAD→ASR→LLM→TTS 모듈러 파이프라인 | [[G-15]](#ref-g-15) |
| SKT | MWC 2026 "AI Native" 전략 발표, AI 컨택 센터(AICC) 강화 계획 공개. A.auto 차량 내 음성 에이전트 출시 | [[G-16]](#ref-g-16) |
| KT | Agentic Fabric(AI 운영체제) + AI 컨택 센터 방향. GiGA Genie 800만 사용자 운영, AICC 하루 10만+ 콜 자동 처리 | [[G-17]](#ref-g-17) |

---

## 시장 시그널

**투자 & M&A**

- 음성 AI 시장 규모 2026년 $22.5B 추정(전년 대비 34.8% CAGR), 2034년 $47.5B 전망 [[G-18]](#ref-g-18).
- 콜센터 AI 시장 2026년 $9.9B 전망(CAGR 22.6%) [[G-18]](#ref-g-18).
- 전주 누계 확인된 투자: ElevenLabs $500M(Series D, $11B 밸류), LiveKit $100M($1B 밸류), Deepgram $130M(Series C), PolyAI $86M(Series D, $750M 밸류), VoiceRun $5.5M(시드).
- xAI Grok Voice Agent API 출시 — 빅테크 직접 진입으로 인프라 시장 경쟁 격화 신호.

**파트너십 & 제휴**

- **ElevenLabs × IBM**: watsonx Orchestrate 통합(3/25). 엔터프라이즈 AI 전화 에이전트 공동 출시 [[G-04]](#ref-g-04), [[E-02]](#ref-e-02).
- **xAI × LiveKit**: Grok Voice Agent API 공식 파트너십. LiveKit 에이전트 프레임워크에 Grok 직접 통합 [[G-02]](#ref-g-02), [[G-03]](#ref-g-03).
- **Twilio ConversationRelay**: <0.5s 중앙값 레이턴시(P95 <0.725s) 달성, PSTN 전화 경로 실증 [[G-19]](#ref-g-19).

**시장 전망**

- Gartner: 대화형 AI가 2026년 콜센터 에이전트 인건비 $80B 절감 예상 [[G-18]](#ref-g-18).
- 기업의 80%가 2026년까지 AI 음성 기술을 고객 서비스에 통합 계획 [추가확인 필요] [[G-20]](#ref-g-20).
- 콜당 비용 AI($0.40) vs 인간($7~12) — 90~95% 절감 효과 [[G-20]](#ref-g-20).
- 음성 AI 도입 기업의 3년 ROI 331~391%(Forrester Consulting 인용) [추가확인 필요] [[G-20]](#ref-g-20).

**도입 사례**

- IBM: AI 음성 에이전트 도입 후 콜센터 비용 40% 절감 사례 공개 [[E-03]](#ref-e-03).
- KT GiGA Genie: 하루 10만+ 콜 무인 자동 처리 (한국) [[G-17]](#ref-g-17).
- SoundHound AI: 2025년 통신·유통 분야 약 3천만 건 AI 인터랙션 처리 [[E-04]](#ref-e-04).
- AHT(Average Handle Time) 감소: 특정 물류 기업 6분 → 3.8분(37% 절감). 운영 비용 30~50% 절감, CSAT 25~40% 증가 사례 다수 [[G-20]](#ref-g-20).

**연구 동향**

- **arXiv 2603.24144** (ICME 2026): Alibaba Qwen 팀 — 의미 인식 인터럽트 감지 벤치마크(SID-Bench) + APT 지표 + LLM 기반 감지 모델 동시 제안(3/25 제출) [[P-01]](#ref-p-01).
- **arXiv 2603.13686** (τ-Voice): 전주 확인, Full-Duplex 음성 에이전트 실세계 평가 표준(Sierra Research) [[P-02]](#ref-p-02).
- **arXiv 2503.04721** (Full-Duplex-Bench): 전주 확인, NTU/UC Berkeley/MIT 컨소시엄 — 일시 정지·백채널링·턴테이킹·인터럽트 4차원 평가 [[P-03]](#ref-p-03).
- NVIDIA PersonaPlex-7B (ICASSP 2026): Full-Duplex S2S(Speech-to-Speech) 오픈소스 모델, Smooth Turn-Taking 레이턴시 실측 0.170~0.265s, MIT 라이선스 상업 이용 가능 [[G-21]](#ref-g-21).

---

## 전략적 시사점

**기술 트렌드**

- VAD 단독 → 의미+음향 하이브리드 엔드포인팅으로 산업 표준이 이동 중. VAD 전용 방식은 300~500ms 레이턴시 페널티를 수반하며 경쟁력 상실.
- LLM 기반 의미 인식 인터럽트 감지가 학술·상용 양쪽에서 동시 부상 (Alibaba Qwen SID-Bench, ElevenLabs CA 2.0, AssemblyAI Universal-3, LiveKit 턴 감지 모델).
- Full-Duplex S2S 아키텍처(NVIDIA PersonaPlex-7B류)가 기존 Cascaded 파이프라인 대비 레이턴시·자연성 측면에서 우위를 입증. 오픈소스화로 진입 장벽 하락 추세.

**기회**

- xAI Grok API($0.05/분, OpenAI Realtime API 호환)와 LiveKit 오픈소스 프레임워크 조합을 활용한 저비용 통신사 자체 음성 에이전트 인프라 구축 가능성.
- ElevenLabs-IBM 파트너십 채널 — watsonx Orchestrate 기반 엔터프라이즈 AI 전화 에이전트 도입 시 70개 언어·고품질 TTS를 즉시 탑재 가능.
- SoundHound AI의 Aragon 리더 선정 — 통신사 AICC(AI Contact Center) 외부 플랫폼 도입 검토 시 우선 평가 후보.
- Deepgram Flux·AssemblyAI Universal-3: 기존 AICC에서 레이턴시 200~600ms 추가 절감 가능. 운영 중인 STT 레이어 교체만으로 대화 자연성 즉각 향상 가능.

**위협**

- LLM 빅테크(xAI) 직접 진입: $0.05/분 가격 파괴로 음성 인프라 스타트업(LiveKit 포함) 수익 모델 압박 예상. 자체 구축 대비 vendor lock-in 위험도 존재.
- 평가 표준 다양화(τ-Voice, Full-Duplex-Bench, SID-Bench, Big Bench Audio)로 벤치마크 선택에 따라 "1위" 주장이 상충. 벤치마크 리터러시 없이 플랫폼 선택 시 기술 미스매치 위험.
- 통신사 AICC 자체 개발 역량 부재 시 ElevenLabs·SoundHound·Retell AI 등 외부 플랫폼 의존도 심화 → 전략 협상력 약화.

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | xAI — Grok Voice Agent API 공식 발표 | [링크](https://x.ai/news/grok-voice-agent-api) | news | 2026-03 | [B] |
| <a id="ref-g-02"></a>G-02 | LiveKit Blog — xAI & LiveKit 파트너십 | [링크](https://blog.livekit.io/xai-livekit-partnership-grok-voice-agent-api/) | news | 2026-03 | [B] |
| <a id="ref-g-03"></a>G-03 | LiveKit Docs — xAI Grok Voice Agent API 플러그인 | [링크](https://docs.livekit.io/agents/models/realtime/plugins/xai/) | news | 2026-03 | [B] |
| <a id="ref-g-04"></a>G-04 | ElevenLabs Blog — IBM watsonx Orchestrate 파트너십 | [링크](https://elevenlabs.io/blog/elevenlabs-partners-with-ibm-to-bring-premium-voice-to-watsonx-orchestrate) | news | 2026-03-25 | [B] |
| <a id="ref-g-05"></a>G-05 | PR Newswire — ElevenLabs × IBM 공식 보도자료 | [링크](https://www.prnewswire.com/news-releases/enterprise-ai-finds-its-voice-elevenlabs-and-ibm-bring-premium-voice-capabilities-to-agentic-ai-302723870.html) | news | 2026-03-25 | [A] |
| <a id="ref-g-06"></a>G-06 | AssemblyAI — 신제품·모델 업데이트 발표 | [링크](https://www.assemblyai.com/blog/introducing-new-products-and-model-updates) | news | 2026-03 | [B] |
| <a id="ref-g-07"></a>G-07 | AssemblyAI Blog — 턴 감지·엔드포인팅 기술 설명 | [링크](https://www.assemblyai.com/blog/turn-detection-endpointing-voice-agent) | news | 2026-03-24 | [B] |
| <a id="ref-g-08"></a>G-08 | LiveKit Blog — 턴 감지: VAD·엔드포인팅·모델 기반 비교 | [링크](https://livekit.com/blog/turn-detection-voice-agents-vad-endpointing-model-based-detection) | news | 2026-03 | [B] |
| <a id="ref-g-09"></a>G-09 | LiveKit Blog — 트랜스포머 기반 EOT 감지 개선 | [링크](https://blog.livekit.io/using-a-transformer-to-improve-end-of-turn-detection) | news | 2026-03 | [B] |
| <a id="ref-g-10"></a>G-10 | Deepgram — Flux CSR 모델 소개 | [링크](https://deepgram.com/learn/introducing-flux-conversational-speech-recognition) | news | 2026-03 | [B] |
| <a id="ref-g-11"></a>G-11 | Deepgram Docs — Flux Eager EOT 최적화 | [링크](https://developers.deepgram.com/docs/flux/voice-agent-eager-eot) | news | 2026-03 | [B] |
| <a id="ref-g-12"></a>G-12 | Retell AI — 턴테이킹 모델 기술 설명 | [링크](https://www.retellai.com/blog/how-retell-ais-turn-taking-model-ensures-seamless-calls) | news | 2026-03 | [B] |
| <a id="ref-g-13"></a>G-13 | Retell AI Changelog | [링크](https://www.retellai.com/changelog) | news | 2026-03 | [B] |
| <a id="ref-g-14"></a>G-14 | SoundHound AI — Aragon Research Globe 리더 선정 보도자료(Yahoo Finance) | [링크](https://finance.yahoo.com/sectors/technology/articles/soundhound-ai-named-leader-aragon-130300526.html) | news | 2026-03-26 | [B] |
| <a id="ref-g-15"></a>G-15 | Webex Engineering Blog — Cisco AI Agent 레이턴시 최적화 | [링크](https://blog.webex.com/engineering/building-voice-ai-that-can-keep-up-with-real-conversations/) | news | 2026-03 | [B] |
| <a id="ref-g-16"></a>G-16 | TelecomLead — MWC 2026 SKT AI Native 전략 | [링크](https://telecomlead.com/telecom-services/mwc-2026-sk-telecom-unveils-ai-native-strategy-to-transform-telecom-build-1gw-ai-data-center-hub-and-advance-sovereign-ai-124858) | news | 2026-03 | [B] |
| <a id="ref-g-17"></a>G-17 | KoreaTechToday — 한국 AI-통신 MWC 2026 전략 시그널 | [링크](https://koreatechtoday.com/koreas-ai-telco-moment-strategic-signaling-at-mwc-2026/) | news | 2026-03 | [B] |
| <a id="ref-g-18"></a>G-18 | Ringly.io — 2026 음성 AI 통계: 시장 규모·성장·트렌드 | [링크](https://www.ringly.io/blog/voice-ai-statistics-2026) | news | 2026-03 | [C] |
| <a id="ref-g-19"></a>G-19 | Twilio Blog — ConversationRelay 핵심 레이턴시 가이드 | [링크](https://www.twilio.com/en-us/blog/developers/best-practices/guide-core-latency-ai-voice-agents) | news | 2026-03 | [B] |
| <a id="ref-g-20"></a>G-20 | Famulor Blog — 엔터프라이즈 음성 AI 2026: CX·ROI | [링크](https://www.famulor.io/blog/enterprise-voice-ai-in-2026-driving-cx-and-roi) | news | 2026-03 | [C] |
| <a id="ref-g-21"></a>G-21 | MarkTechPost — NVIDIA PersonaPlex-7B-v1 출시 리뷰 | [링크](https://www.marktechpost.com/2026/01/17/nvidia-releases-personaplex-7b-v1-a-real-time-speech-to-speech-model-designed-for-natural-and-full-duplex-conversations/) | news | 2026-01-17 | [B] |
| <a id="ref-p-01"></a>P-01 | Qwen Team (Alibaba) et al. — Semantic-Aware Interruption Detection in Spoken Dialogue Systems: Benchmark, Metric, and Model | [링크](https://arxiv.org/abs/2603.24144) | paper | 2026-03-25 | [A] |
| <a id="ref-p-02"></a>P-02 | Ray et al. — τ-Voice: Benchmarking Full-Duplex Voice Agents on Real-World Domains | [링크](https://arxiv.org/abs/2603.13686) | paper | 2026-03-14 | [A] |
| <a id="ref-p-03"></a>P-03 | Lin et al. — Full-Duplex-Bench: A Benchmark to Evaluate Full-Duplex Spoken Dialogue Models on Turn-taking Capabilities | [링크](https://arxiv.org/abs/2503.04721) | paper | 2026-03 | [A] |
| <a id="ref-e-01"></a>E-01 | xAI (공식 X 계정) — "Grok Voice Agent API는 OpenAI Realtime API 스펙과 호환되며 공식 xAI LiveKit 플러그인을 통해서도 이용 가능. 수주 내 TTS·STT 독립 엔드포인트 및 강화 오디오 모델 출시 예정" | [링크](https://x.com/xai/status/2001385977932320832) | IR/발표 | 2026-03 | [A] |
| <a id="ref-e-02"></a>E-02 | IBM Newsroom — "Enterprise AI Finds its Voice: ElevenLabs and IBM Bring Premium Voice Capabilities to Agentic AI" | [링크](https://newsroom.ibm.com/2026-03-25-enterprise-ai-finds-its-voice-elevenlabs-and-ibm-bring-premium-voice-capabilities-to-agentic-ai) | IR/발표 | 2026-03-25 | [A] |
| <a id="ref-e-03"></a>E-03 | IBM (보도자료 인용) — "IBM cites a 40% reduction in call-center costs after rolling out AI voice agents" | [링크](https://www.famulor.io/blog/enterprise-voice-ai-in-2026-driving-cx-and-roi) | IR/발표 | 2026-03 | [B] |
| <a id="ref-e-04"></a>E-04 | SoundHound AI (공식 보도자료) — "In 2025 alone, the company processed nearly 30 million AI-driven customer interactions for telecom and retail" | [링크](https://www.soundhound.com/newsroom/press-releases/soundhound-ai-named-leader-in-the-aragon-research-globe-for-agent-platforms-2026/) | IR/발표 | 2026-03-26 | [A] |
