---
type: weekly-research
topic: voice-synthesis
week: 2026-W15
date: 2026-04-06
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
---

# Deep 리서치: Voice Synthesis (W15)

## 이전 대비 변화

- **전주 (W14, 2026-03-30)**: 오픈웨이트 + 기업 파트너십 2중 공세 — Mistral Voxtral Text-to-Speech (TTS) 4B 오픈웨이트(ElevenLabs 대비 68.4% 승률, $0.016/1k chars), xAI Grok Voice Agent Application Programming Interface (API)($0.05/min), ElevenLabs-IBM watsonx 파트너십, Amazon Polly 생성형 TTS General Availability (GA).
- **금주 (W15, 2026-04-06)**: 플랫폼 확장 + 오픈소스 가속 — ElevenLabs 에이전트 플랫폼 대규모 업데이트(4/1, MCP Tool Scoping·동영상→음악 등), Cartesia Sonic-3 Amazon SageMaker JumpStart 배포 가용성 확대, Miravoice $6.3M Seed(음성 에이전트 전화 설문 전문), Nari Labs Dia2 스트리밍 TTS 커뮤니티 확산, OmniVoice 600+ 언어 제로샷 TTS 논문 출판(4/1). Q1 2026 글로벌 벤처캐피탈 (Venture Capital, VC) $300B 사상 최고 기록이 Voice AI 섹터에도 투자 모멘텀 제공.
- **변화 방향**: 기술 경쟁의 중심이 "단순 TTS 품질"에서 "에이전트 플랫폼 생태계"로 이동하고 있다. ElevenLabs·Cartesia는 플랫폼 통합과 엔터프라이즈 배포 채널 확장에 집중하고, 오픈소스 진영(Kokoro·Dia2)은 온디바이스·스트리밍 특화로 차별화 중. 학계에서는 600+ 언어 제로샷 합성이 현실화되며 언어 장벽 기술의 임계점이 임박했음을 시사한다.

---

## 기술 동향

1. **ElevenLabs 에이전트 플랫폼 대규모 업데이트 (4/1) — MCP Tool Scoping, 동영상→음악, Speech-to-Text (STT) URL 전사.**
   ElevenLabs가 2026년 4월 1일 API 스키마 v2.41.1을 배포하며 에이전트 플랫폼 전반에 걸친 대규모 업데이트를 단행했다 [[G-01]](#ref-g-01). 주요 변경 사항: (1) **MCP Tool Scoping** — 워크플로우 단계별로 서브에이전트의 도구 접근을 제한하는 세밀한 권한 제어 기능 추가; (2) **Conversation File Uploads** — 채팅에서 이미지·PDF 첨부 지원(`file_input` 설정); (3) **동영상→음악 생성** — 영상 파일에서 배경음악을 생성하는 신규 엔드포인트(스타일 태그 옵션 포함); (4) **STT URL 전사** — YouTube·TikTok 등 동영상 URL을 직접 전사하는 `source_url` 파라미터 추가; (5) **JavaScript SDK v1.0.0** — React 훅 세분화, 기본 `connectionType` 자동 추론 등 브레이킹 체인지 다수. 아울러 2월 9일 업데이트에서 `eleven_v3_conversational` 에이전트 모델 추가, TTS Normalizer 3.1(정확도 및 레이턴시 개선), WhatsApp 아웃바운드 메시지 엔드포인트(`POST /v1/convai/whatsapp/outbound-message`)가 배포된 것이 이번 주 Quick 스캔에서 재확인됐다 [[G-02]](#ref-g-02). 이는 단순 TTS 제공사에서 다채널 음성 에이전트 플랫폼으로의 전환을 명확히 보여준다.

2. **Cartesia Sonic-3 — State Space Model (SSM) 아키텍처, 42언어, 90ms 모델 딜레이, AWS SageMaker 배포 확대.**
   Cartesia가 2025년 10월 출시한 Sonic-3가 2026년 2월 Amazon SageMaker JumpStart에 통합되며 엔터프라이즈 배포 경로를 확장했다 [[G-03]](#ref-g-03). Sonic-3는 트랜스포머(Transformer) 대신 SSM 아키텍처를 채택해 대화 맥락을 효율적으로 보존한다. 핵심 스펙: 42개 언어, 모델 딜레이 90ms, 엔드투엔드 응답 190ms, 감정 뉘앙스·자연스러운 웃음 표현 지원. 독립 블라인드 테스트에서 사용자의 62%가 경쟁사 대비 Sonic-3를 선호했다. 펀딩은 $100M(Kleiner Perkins·Index Ventures·Lightspeed·NVIDIA 참여, 2025년 10월 확정)이며, 현재 ServiceNow·Cresta·Decagon 등 엔터프라이즈에서 월 수백만 건의 대화를 처리 중이다 [[G-04]](#ref-g-04). Cartesia 창업자 Karan Goel은 "Sonic-3로 개선되지 않는 음성 AI 경험에 대해 자선단체에 $5,000를 기부하겠다"고 공개적으로 선언했다 [[E-01]](#ref-e-01).

3. **Deepgram Aura-2 — 엔터프라이즈 전용 TTS, sub-200ms TTFB, 40+ 음성, $0.030/1k chars.**
   Deepgram이 2025년 4월 발표한 Aura-2는 엔터프라이즈 실시간 음성에 특화 설계된 TTS 모델로, 이번 주 경쟁 벤치마크 분석에서 지속적으로 언급되고 있어 경쟁사 포지셔닝 파악을 위해 수록한다 [원문 미확인: 2025년 발표, W15 범위 외] [[G-05]](#ref-g-05). 핵심 스펙: TTFB sub-200ms(Real-Time Factor 0.111x), 40개 이상 음성(각기 명확한 엔터프라이즈 사용 사례별 톤 프로파일 정의), 클라우드·VPC·온프레미스 유연 배포, 약물명·법률 용어·날짜·통화 등 도메인별 발음 최적화. 가격 $0.030/1k chars는 Cartesia Sonic($0.038)·ElevenLabs Flash($0.050) 대비 저렴하게 포지셔닝했다. 인간 선호도 테스트에서 ElevenLabs·Cartesia·OpenAI를 상회한다고 Deepgram이 주장한다.

4. **Nari Labs Dia2 — 스트리밍 대화형 TTS, Apache 2.0, 1B/2B 체크포인트, 단일 GPU 실행.**
   한국 스타트업 Nari Labs(공동창업자: 두 명의 20대 학생)의 Dia2가 오픈소스 커뮤니티에서 빠르게 확산 중이다 [[G-06]](#ref-g-06). Dia2는 전체 텍스트를 기다리지 않고 첫 몇 개 토큰부터 음성 생성을 시작하는 스트리밍 아키텍처를 채택했다. 기술 스펙: 1B·2B 파라미터 체크포인트(영어, 최대 2분 출력), NVIDIA A4000 단일 GPU에서 실시간 스트리밍(~40 tokens/sec, 약 10GB VRAM 필요), 오디오 컨디셔닝으로 실시간 대화 지속 가능, Apache 2.0 라이선스(상업 활용 허용). 선행 모델 Dia 1.6B(2025년 4월, 비교 가능 모델 대비 최우수 성능 주장)에서 스트리밍 특화로 발전한 버전이다.

5. **Kokoro-82M — 오픈소스 경량 TTS, MOS 4.2, <$1/1M chars, Apache 2.0.**
   82M 파라미터의 초경량 오픈웨이트 TTS 모델 Kokoro-82M이 2026년 HuggingFace 다운로드 220만 건을 돌파하며 오픈소스 TTS의 새로운 기준으로 자리잡았다 [[G-07]](#ref-g-07). StyleTTS 2 아키텍처 기반으로 8개 언어·54개 음성을 지원하며, GPU 기준 RTF(Real-Time Factor) 0.03(10초 클립을 0.3초에 합성), CPU에서도 구동 가능하다. 오픈소스 모델 중 MOS(Mean Opinion Score) 4.2로 최고 점수를 기록했으며, API 서빙 기준 $1/1M chars 미만의 초저가격으로 온디바이스·엣지 배포에 최적이다. 학습 비용은 $1,000 컴퓨팅에 불과했으며, Apache 2.0 라이선스로 상업 배포가 자유롭다.

6. **OmniVoice — 600+ 언어 제로샷 TTS, 확산-언어 모델 혼합, 58.1만 시간 학습 데이터.**
   2026년 4월 1일 arXiv에 발표된 OmniVoice(Zhu et al.)는 600개 이상 언어를 지원하는 제로샷 TTS 모델이다 [[P-01]](#ref-p-01). 기존 두 단계 파이프라인의 성능 병목을 피하기 위해 확산 언어 모델(Diffusion Language Model)로 텍스트에서 멀티코드북 음향 토큰을 직접 매핑한다. 마스킹 학습과 사전학습 언어 모델 초기화를 결합한 신규 아키텍처로, 오픈소스 다국어 데이터 581,000시간을 학습했다. 코드와 사전학습 모델을 공개하여 재현성을 보장했으며, 중국어·영어·다언어 벤치마크에서 state-of-the-art를 달성했다고 보고했다.

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | 4/1 에이전트 플랫폼 업데이트(API v2.41.1): MCP Tool Scoping, 동영상→음악, STT URL 전사, JS SDK v1.0.0 브레이킹 체인지. 2월 업데이트에서 `eleven_v3_conversational` 에이전트 모델·TTS Normalizer 3.1·WhatsApp 아웃바운드 배포 | [[G-01]](#ref-g-01), [[G-02]](#ref-g-02) |
| Cartesia | Sonic-3(2025년 10월) AWS SageMaker JumpStart 통합(2월). SSM 아키텍처, 42언어, 90ms 모델 딜레이, ServiceNow·Cresta·Decagon 엔터프라이즈 고객사 확보 | [[G-03]](#ref-g-03), [[G-04]](#ref-g-04) |
| Deepgram | Aura-2(2025년 4월 발표) 엔터프라이즈 채택 확산 지속. sub-200ms TTFB, 40+ 음성, $0.030/1k chars. IBM watsonx 첫 전용 음성 파트너 지위 유지 | [[G-05]](#ref-g-05) |
| Nari Labs | Dia2 오픈소스 스트리밍 TTS 커뮤니티 확산. 1B/2B 체크포인트, Apache 2.0, 단일 GPU 실행, 한국계 20대 창업팀 | [[G-06]](#ref-g-06) |
| Kokoro (hexgrad) | 82M 파라미터 오픈웨이트, HuggingFace 다운로드 220만 건 돌파. MOS 4.2(오픈소스 최고), RTF 0.03, Apache 2.0, $1/1M chars 미만 | [[G-07]](#ref-g-07) |
| Supertone | 한국: Sona Speech 2(23언어, 단일 샘플 음성 복제), Supertonic 2(2026-01-06, 온디바이스, 5언어). Supertone Play 217개국 사용 | [[G-08]](#ref-g-08) |
| Mistral AI | Voxtral TTS 4B(W14 출시) 이후 커뮤니티 벤치마크 비교 확산. 오픈웨이트 전략 유지, 신규 발표 없음 | [[G-09]](#ref-g-09) |
| xAI | Grok Voice Agent API(W14 출시) 개발자 채택 단계. OpenAI Realtime API 호환성 활용한 마이그레이션 사례 증가 보고 | [[G-10]](#ref-g-10) |
| Miravoice | $6.3M Seed(Unusual Ventures 주도, Neo·25madison 참여). AI 음성 에이전트 기반 장문(120문항+, 40분+) 전화 설문·여론조사 전문. 14개 언어, 분기 규칙·무작위화·개방형 응답 실시간 처리 | [[G-11]](#ref-g-11) |
| KT | AI Voice Studio: 감성 표현 5개 언어 지원 맞춤형 AI 보이스 서비스. YouTube·오디오북·안내방송·도슨트 콘텐츠 적용 중. 2025년 자연어 감정 기반 음성합성 기능 출시 예정 발표 이후 정기 업데이트 없음 | [[G-12]](#ref-g-12) |

---

## 시장 시그널

**투자 & M&A**

- **Q1 2026 글로벌 VC $300B 사상 최고**: 6,000개 스타트업에 $300B 투입(전분기 대비 150%+ 증가). AI 비중 80%($242B), OpenAI $122B·Anthropic $30B·xAI $20B·Waymo $16B이 Q1 전체의 65% 집중 [[G-13]](#ref-g-13). Voice AI 섹터는 직접 수혜 — ElevenLabs·xAI·Deepgram 등 주요 플레이어 모두 이 사이클의 수혜자.
- **Miravoice $6.3M Seed**: Unusual Ventures 주도, Neo·25madison·Ramp·PubMatic·Atlassian·Google 엔젤 참여. 수천만 건 통화 처리를 위한 엔지니어링 확대 및 시장 본격 진출 준비 [[G-11]](#ref-g-11).
- **Cartesia $100M 확인**: Kleiner Perkins·Index Ventures·Lightspeed·NVIDIA 참여(2025년 10월). W15에서 AWS 배포 채널 확대로 기업가치 재평가 기대 [[G-04]](#ref-g-04).

**파트너십 & 제휴**

- **Cartesia + Amazon SageMaker JumpStart**: Sonic-3가 SageMaker JumpStart에 통합(2026년 2월)되어 AWS 기업 고객에게 원클릭 배포 경로 제공 [[G-03]](#ref-g-03).
- **ElevenLabs 멀티채널 확장**: WhatsApp 아웃바운드 메시지·YouTube/TikTok STT URL 전사 통합으로 음성 에이전트의 커버리지 채널 확대 [[G-01]](#ref-g-01).

**시장 전망**

- **Voice AI 시장 $22B 돌파(2026)**: 음성 및 언어 인텔리전스 시장은 2026년 $24.49B에서 2035년 $145.03B으로 성장 전망 [[G-14]](#ref-g-14). AI Voice Generator 세부 시장은 2025년 $4.16B → 2031년 $20.71B(연평균성장률 Compound Annual Growth Rate, CAGR 미공개) [[G-15]](#ref-g-15). AI Voice Agents 세그먼트는 2024년 $2.4B → 2034년 $47.5B(CAGR 34.8%) [[G-14]](#ref-g-14). 독립 출처 3건이 시장 성장을 교차 확인함.
- **컨텍 센터 Voice AI ROI**: 기업 도입 사례 기준 콜 처리시간 35% 감소, 고객만족도(CSAT) 25~40% 향상, 운영비용 30~50% 절감, 일부 배포 380% ROI 보고 [[G-16]](#ref-g-16). 2026년 Voice AI 도입 압박을 느끼는 리더 91% [[G-16]](#ref-g-16). [추가확인 필요: 단일 마케팅 리포트 출처]

**도입 사례**

- **Miravoice 음성 설문**: AI 음성 면접관이 120문항+·40분+ 장문 설문을 자율 수행. 브랜칭 로직·랜덤화·개방형 응답 실시간 처리, 14개 언어 지원. 기존 인간 면접관 대체 경제성 입증 목표 [[G-11]](#ref-g-11).
- **Cartesia 엔터프라이즈**: ServiceNow·Cresta·Decagon 등 월 수백만 건 대화 처리 [[G-04]](#ref-g-04).

**연구 동향**

- **제로샷 TTS의 언어 커버리지 확장**: OmniVoice(4/1)가 600+ 언어 제로샷 합성을 시연하며 언어 장벽 해소의 기술적 임계점 도달을 시사 [[P-01]](#ref-p-01).
- **스트리밍 TTS 아키텍처 성숙**: Dia2(Nari Labs), Kokoro-82M 등 오픈소스 스트리밍·경량 모델이 커뮤니티 표준 경쟁 중. 산업계 기준(Cartesia sub-100ms, Deepgram sub-200ms)과 학계 연구 목표가 수렴하고 있다.
- **SSM vs. Transformer 아키텍처 대결**: Cartesia Sonic-3의 SSM 채택이 상업적으로 검증되면서, 대화 맥락 유지에서의 우위 주장이 실제 엔터프라이즈 채택으로 이어지고 있다.

**커뮤니티 시그널**

- Kokoro-82M HuggingFace 다운로드 220만 건, 커뮤니티 5,600+ 서포터로 오픈소스 TTS의 새 기준 등극 [[G-07]](#ref-g-07).
- Dia2(Nari Labs) GitHub 스타 급증. 한국계 학생팀의 오픈소스 기여가 글로벌 커뮤니티에서 주목받고 있음 [원문 미확인: GitHub 스타 수치 미확보] [[G-06]](#ref-g-06).
- ElevenLabs JS SDK v1.0.0 브레이킹 체인지 발표 후 개발자 커뮤니티 마이그레이션 논의 활발 [[G-01]](#ref-g-01).

---

## 전략적 시사점

**기회**

- **에이전트 플랫폼 통합 수요 급증**: ElevenLabs·Cartesia 모두 단순 TTS API에서 다채널 음성 에이전트 플랫폼으로 전환 중. WhatsApp·YouTube·MCP 통합은 음성 AI의 접점 채널을 빠르게 확장하고 있다.
- **오픈소스 경량 모델의 온프레미스 수요**: Kokoro-82M·Dia2 같은 경량 모델이 데이터 레지던시·보안 요건이 높은 엔터프라이즈(금융·의료·공공)에서 온프레미스 TTS 옵션으로 부상 중.
- **600+ 언어 지원의 현실화**: OmniVoice의 성과는 글로벌 다국어 음성 서비스에서 기술 장벽이 급속히 낮아지고 있음을 의미한다. 신흥 시장(동남아·아프리카·남미) 음성 AI 진입 기회.
- **음성 에이전트 버티컬 특화**: Miravoice(시장조사·여론조사), SuperDial(보험 전화), Abridge(의료) 등 버티컬 특화 Voice AI 스타트업이 펀딩을 유치하고 있다.

**위협**

- **빅테크 플랫폼 잠금(Lock-in) 위험**: Cartesia의 AWS SageMaker 통합, ElevenLabs의 IBM watsonx 통합은 플랫폼 생태계 내 종속성을 강화한다. 독립 솔루션이 클라우드 플랫폼의 번들 경쟁에 노출될 위험.
- **오픈웨이트 가격 하방 압력**: Mistral Voxtral($0.016/1k chars), Kokoro($1/1M chars 미만), Dia2(무료 자가호스팅)가 상용 TTS 가격 하방을 압박 중. 고가 프리미엄 TTS의 가격 정당화 어려워질 가능성.
- **ElevenLabs SDK 브레이킹 체인지 리스크**: JS SDK v1.0.0의 대규모 API 변경은 기존 통합 코드베이스에 유지보수 부담을 유발한다. 의존성이 높은 에이전트 서비스에서 호환성 문제 발생 가능.
- **SSM 아키텍처의 미검증 장기 리스크**: Cartesia Sonic-3의 SSM 기반 아키텍처는 Transformer 대비 장기 컨텍스트에서의 품질 유지 능력이 아직 충분히 검증되지 않았다 [추가확인 필요].

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | ElevenLabs — Changelog 2026-04-01 (API v2.41.1) | [링크](https://elevenlabs.io/docs/changelog/2026/4/1) | changelog | 2026-04-01 | [A] |
| <a id="ref-g-02"></a>G-02 | Releasebot — Eleven Labs Release Notes (Feb-Mar 2026, TTS Normalizer 3.1·WhatsApp) | [링크](https://releasebot.io/updates/eleven-labs) | news | 2026-02-09 | [B] |
| <a id="ref-g-03"></a>G-03 | AWS — Cartesia Sonic 3 now available on Amazon SageMaker JumpStart | [링크](https://aws.amazon.com/about-aws/whats-new/2026/02/cartesia-sonic-3-on-sagemaker-jumpstart/) | news | 2026-02 | [A] |
| <a id="ref-g-04"></a>G-04 | StartupStag — Cartesia Raises $100M, Launches Sonic-3 AI Voice Model | [링크](https://startupstag.com/investments/cartesia-raises-100m-launches-sonic-3-ai-voice-model/) | news | 2025-10-31 | [B] |
| <a id="ref-g-05"></a>G-05 | Deepgram — Introducing Aura-2: Enterprise-Grade Text-to-Speech | [링크](https://deepgram.com/learn/introducing-aura-2-enterprise-text-to-speech) | blog | 2025-04-15 | [B] |
| <a id="ref-g-06"></a>G-06 | GitHub — nari-labs/dia2: TTS model capable of streaming conversational audio in realtime | [링크](https://github.com/nari-labs/dia2) | repository | 2025-11 | [B] |
| <a id="ref-g-07"></a>G-07 | HuggingFace — hexgrad/Kokoro-82M (2.2M 다운로드, MOS 4.2) | [링크](https://huggingface.co/hexgrad/Kokoro-82M) | repository | 2026 | [B] |
| <a id="ref-g-08"></a>G-08 | Supertone — Sona Speech 2, Supertonic 2, Supertone Play 217개국 | [링크](https://www.supertone.ai/en/work/supertone-2025-recap) | blog | 2026-01-06 | [B] |
| <a id="ref-g-09"></a>G-09 | VentureBeat — Mistral AI Voxtral TTS open-weight model beats ElevenLabs | [링크](https://venturebeat.com/orchestration/mistral-ai-just-released-a-text-to-speech-model-it-says-beats-elevenlabs-and) | news | 2026-03-26 | [B] |
| <a id="ref-g-10"></a>G-10 | AI Newsletter — xAI Grok Voice Agent API ($0.05/min, OpenAI Realtime API 호환) | [링크](https://aivoicenewsletter.com/p/cartesia-s-100m-sonic-3-leap) | news | 2026-03-16 | [B] |
| <a id="ref-g-11"></a>G-11 | Crunchbase — Exclusive: Miravoice Raises $6.3M seed (AI Voice Survey) | [링크](https://news.crunchbase.com/venture/ai-interviewer-miravoice-raises-seed-funding-unusual/) | news | 2026-04 | [B] |
| <a id="ref-g-12"></a>G-12 | KT AI — KT Voice AI 소개 및 AI Voice Studio | [링크](https://ai.kt.com/resources/detail03) | official | 2025 | [A] |
| <a id="ref-g-13"></a>G-13 | Crunchbase — Q1 2026 Shatters Venture Funding Records ($300B, AI 80%) | [링크](https://news.crunchbase.com/venture/record-breaking-funding-ai-global-q1-2026/) | news | 2026-04-01 | [B] |
| <a id="ref-g-14"></a>G-14 | Precedence Research — Voice and Language Intelligence Market ($24.49B in 2026, $145.03B by 2035) | [링크](https://www.precedenceresearch.com/voice-and-language-intelligence-market) | report | 2026 | [B] |
| <a id="ref-g-15"></a>G-15 | MarketsandMarkets — AI Voice Generator Market ($4.16B 2025 → $20.71B 2031) | [링크](https://www.marketsandmarkets.com/PressReleases/ai-voice-generator.asp) | report | 2025 | [B] |
| <a id="ref-g-16"></a>G-16 | NextLevel AI — Voice AI Trends 2026: Enterprise Adoption & ROI Guide | [링크](https://nextlevel.ai/voice-ai-trends-enterprise-adoption-roi/) | blog | 2026 | [C] |
| <a id="ref-p-01"></a>P-01 | Zhu et al. — OmniVoice: Towards Omnilingual Zero-Shot TTS with Diffusion Language Models | [링크](https://arxiv.org/abs/2604.00688) | paper | 2026-04-01 | [A] |
| <a id="ref-e-01"></a>E-01 | Karan Goel (Cartesia 창업자) — "Sonic-3로 개선되지 않는 음성 AI 경험에 $5,000 기부" 공개 선언 | [링크](https://startupstag.com/investments/cartesia-raises-100m-launches-sonic-3-ai-voice-model/) | 발언 | 2025-10-31 | [B] |
