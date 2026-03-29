---
type: weekly-summary
week: 2026-W14
date: 2026-03-27
domains: [agentic-ai, voice-ai, secure-ai]
---

# CTO 주간 기술 동향 요약 (2026-W14)

> 작성일: 2026-03-27 | 소스: Agentic AI (W14), Voice AI (W13), Secure AI (W14) 주간 리포트

---

## 1. 도메인별 핵심 시그널

### Agentic AI

1. **에이전트 프레임워크 4강 동시 업데이트** — OpenAI SDK 0.13 tool search, Claude Code Channels, Google ADK 네이티브 A2A, MS Foundry Agent Service GA. MCP+A2A 듀얼 스택이 사실상 표준으로 수렴.
2. **GPU 오케스트레이션 "학습→추론" 구조적 전환** — NVIDIA Dynamo 1.0 GA(오픈소스 추론 OS), Vera Rubin 플랫폼 공개. Jensen Huang 2027년 $1T 수주 전망. 추론이 AI 컴퓨트의 2/3 차지.
3. **에지 AI 대규모 상용 배포 시작** — AT&T-Cisco-NVIDIA AI Grid 라이브, Akamai 4,400 에지 로케이션 배포. OpenAI GPT-5.4 mini/nano 출시로 sLM-First 아키텍처(비용 60-70% 절감) 본격화.

### Voice AI

1. **🔴 보이스 클로닝 "구별 불가능 임계점" 공식 돌파** — 인간 탐지율 54%(동전 던지기 수준). 미국인 25% 딥페이크 통화 경험(Hiya). UN·INTERPOL 글로벌 사기 경고. 글로벌 사기 손실 $442B.
2. **음성 에이전트 인프라 투자 $648M+ 폭증** — ElevenLabs $500M/$11B, LiveKit $100M/$1B 유니콘. Conversational AI 2.0(95% 인터럽트 감지 턴테이킹 신경망) 출시.
3. **오픈소스 TTS 혁신 + 빅테크 GA 릴리스** — Hume TADA(환각 제로, RTF 0.09), Kitten TTS(25MB 엣지). Google Gemini 2.5 TTS GA, MS Dragon HD Omni 700+ 음성 프리뷰.

### Secure AI

1. **PQC 실용화 3개 레이어 동시 이정표** — ZeroTier Quantum E2E PQC 네트워킹(RSAC 2026), Kudelski KSE3 PQC 반도체 IP, Thales 5G SIM OTA PQC 세계 최초 시연. ML-KEM/ML-DSA 중심으로 수렴.
2. **FHE 기반 AI 학습 세계 최초 실증** — UTS, Nature Machine Intelligence 게재(3/18). 암호화 데이터에서 딥강화학습, 비암호화 대비 성능 격차 10% 이내.
3. **삼중 규제 데드라인 동시 압박** — FIPS 140-2 종료(D-180, 9/21), EU CRA 보고 의무(D-170, 9/11), CNSA 2.0 신규 조달(D-281, 1/1/2027). FCC SIP 603+ 시행 완료(3/25).

---

## 2. 🔴 긴급 항목

| 항목 | 영향 | 대응 필요 |
|------|------|----------|
| **보이스 클로닝 구별 불가능 임계점** | 인간 탐지율 54%, 인프라 레벨 방어 필수. AI 음성 사기 1,210% 증가(YoY) | Pindrop-Zoom 모델 참조 AICC 딥페이크 탐지 도입 검토. 보이스피싱 탐지 서비스 강화 |
| **EU AI Act Article 50 D-131** | 합성 음성 라벨링 의무화(2026-08-02) | 자사 TTS/음성 서비스 컴플라이언스 점검 |
| **FIPS 140-2 종료 + EU CRA + CNSA 2.0** | 3건 하반기 집중. PQC 인증 모듈 542일 소요로 Acquisition Gap 발생 | 내부 암호화 자산 인벤토리 + Crypto-agility 역량 평가 착수 |
| **ElevenLabs 서울 포함 글로벌 확장** | $11B 밸류에이션, 14개 도시 진출. 국내 음성 AI 시장 직접 진입 가능성 | 경쟁 포지셔닝 재점검 |

---

## 3. 포트폴리오 현황 변동

| 도메인 | L2 기술 | 신호 변동 | 비고 |
|--------|---------|----------|------|
| Agentic AI | Intelligent Agent Orchestration | 🟢→🟡 | 4강 동시 업데이트, KT 에이전트 빌더 대응 필요 |
| Agentic AI | 하이브리드 GPU Orchestration | 🟢→🟡 | Dynamo 1.0 GA, 추론 전환 구조적 |
| Agentic AI | On-Device sLM | 🟢→🟡 | GPT-5.4 mini/nano, 상용 소형 모델 등장 |
| Agentic AI | Edge AI | 🟢→🟡 | AT&T-Cisco-NVIDIA 상용 배포, PoC→프로덕션 전환 |
| Voice AI | Voice Cloning | 🟡→🔴 | 구별 불가능 임계점 돌파, 보안 위협 현실화 |
| Voice AI | Voice Synthesis | 🟢→🟡 | Hume TADA, Gemini 2.5 TTS GA, 플랫폼 경쟁 분화 |
| Voice AI | Interrupt & Turn-Taking | 🟢→🟡 | $648M+ 투자, Conv AI 2.0 턴테이킹 신경망 |
| Voice AI | Emotional Analysis | 🟢→🟡 | Octave 2 한국어 지원, EU 감정인식 금지 발효 |
| Secure AI | On-Device PQC | 유지 🟡 | RSAC 2026 ZeroTier Quantum, KSE3, SIM OTA |
| Secure AI | On-Device FHE | 유지 🟡 | UTS FHE DRL 첫 실증, Intel Heracles 미디어 확산 |

> 🟢 평온 유지: 5G/6G AI-RAN, Speaker Diarization, ACE, Adaptive RAG, Spam/Phishing, OCR Spam, Secure Vector Search, Context Recognition, Persona Plugin, Relationship Graph, Context Action Recommendation

---

## 4. 경쟁사 동향 요약

### SKT
- **에릭슨 MoU(3/19)**: AI-RAN·5G 수익화·6G 표준화 5개 축, 2031년까지
- **AI 메가 데이터센터**: 전국 1GW+ 규모, 아시아 최대 AI 허브 목표
- **A.auto 차량용 AI 에이전트**: 르노코리아 필랑트 탑재, Voice AI "모바일 밖" 확장

### KT
- **에이전트 빌더**: MWC26 노코드 에이전트 제작 플랫폼 공개 → B2B 시장 선점
- **AI 보이스피싱 탐지 2.0**: 93%+ 정확도, 1,300억원 피해 예방 (Pindrop 99% 대비 갭)
- **6G Quantum-Safe 전략**: QKD+AI 침해탐지+동형암호 전 구간 적용 계획

### LGU+ (주목)
- **ixi-Guardian 2.0**: NIST+KpqC PQC 광전송 장비, GSMA GLOMO 수상
- **CryptoLab 협력**: ixi-O AICC에 CKKS 동형암호 탑재 — 국내 통신사 FHE 상용화 최근접

---

## 5. 다음 주 주목 이슈

| 이슈 | 예상 시점 | 영향도 |
|------|----------|--------|
| Apple Siri+Gemini 통합 iOS 26.5 베타 | ~3/30 | Voice AI 에코시스템 변화 |
| RSAC 2026 후속 — AI 에이전트 보안 프레임워크 구체화 | W15 | Agentic AI + Secure AI 교차 |
| EU AI Act Article 50 D-124 | 카운트다운 진행 | 합성 음성 라벨링 대비 |
| FIPS 140-2 종료 D-173 | 카운트다운 진행 | PQC 마이그레이션 압박 |
| ElevenLabs 11.ai MCP 음성비서 알파 → 베타 전환 | 추적 | 음성 에이전트 플랫폼 경쟁 |
| KT 에이전트 빌더 후속 동향 | 추적 | B2B 에이전트 시장 경쟁 |

---

*본 요약은 2026-03-24(Agentic AI, Voice AI) 및 2026-03-25(Secure AI) 주간 모니터링 리포트를 기반으로 작성되었습니다.*
