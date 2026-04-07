---
type: weekly-summary
week: 2026-W14
date: 2026-04-03
domains: agentic-ai, voice-ai, secure-ai
competitors: skt, kt
---

# CTO 주간 기술 인텔리전스 요약 (2026-W14)

> 2026-04-03 | 소스: Agentic AI(W16), Voice AI(W14), Secure AI(W14), 경쟁사 브로드스캔(3/30)

---

## 1. 도메인별 핵심 시그널

### Agentic AI — 🟡 주목

1. **에이전트 프로토콜 3대 스택 확정**: MCP(도구 컨텍스트) · A2A(에이전트 간) · AG-UI(에이전트-사용자)가 AWS·MS·Oracle·Google 동시 채택으로 업계 표준 구도 성립. MCP Dev Summit(4/2-3 NYC) 개막.
2. **에이전트 평가가 프로덕션 게이트로 정착**: AWS AgentCore Evaluations GA(13개 평가기), MS Foundry 평가 GA, LangSmith ABAC/감사로그가 같은 주에 출하 — "배포 전 품질 검증" 업계 합의 형성.
3. **SIP 음성 에이전트 공식화**: OpenAI SDK 0.13.4 RealtimeRunner SIP 지원 + MS Voice Live Preview → 통신사 SIP 트렁크 연동 시나리오 현실화.

### Voice AI — 🔴 긴급

1. **TTS 오픈소스 가격 파괴**: Mistral Voxtral TTS 4B 오픈웨이트 출시(ElevenLabs 대비 68.4% 승률 주장, $0.016/1k chars = 87% 저렴). 3초 제로샷 클로닝으로 진입장벽 사실상 소멸.
2. **빅테크 음성 에이전트 직접 진입**: xAI Grok Voice Agent API($0.05/min, 최저가), ElevenLabs-IBM watsonx 엔터프라이즈 통합 — "빅테크 직접 경쟁 + 플랫폼 통합" 이중 축 재편.
3. **딥페이크 탐지-생성 비대칭 심화**: 오픈소스 클로닝 무료화로 공격 비용 제로 수렴 vs 탐지 모델 실세계 일반화 실패 확인(PMC). 인간 판별 정확도 24.5%.

### Secure AI — 🔴 긴급

1. **Google 2029 PQC 데드라인 선언**: NIST 2030보다 1년, NSA 2033보다 4년 앞당김. Android 17에 ML-DSA 4계층 종합 탑재 — 모바일 OS 최초 PQC 보안 아키텍처.
2. **동형암호 온디바이스 임계점 접근**: "Privacy at your Fingertips" 논문이 클라이언트 FHE 오버헤드 97% 감소 달성. Zama+T-REX $32B 기관 금융 FHE 최초 실도입.
3. **PQC 메시징 대역폭 100× 문제 정량화**: IBM+Signal+Threema가 ML-DSA 직접 치환 시 대역폭 100배 증가 확인 — 실시간 보이스 QoS 저하 위험, SIP/RTP 스택 재설계 필요.

---

## 2. 🔴 긴급 항목 하이라이트

| # | 항목 | 도메인 | 임팩트 | 대응 시한 |
|---|------|--------|--------|-----------|
| 1 | **Voxtral TTS 오픈소스 — 보이스 클로닝 무료화** | Voice AI | 음성 사기 공격 비용 제로 수렴. 기존 ASV 인증 무력화 가시화 | 즉시 |
| 2 | **Google 2029 PQC 데드라인** | Secure AI | 공급망 전체 조기화 압력. 통신사 2030 로드맵 재검토 필요 | Q2 |
| 3 | **KT AI 리더십 동시 공백** | 경쟁사 | CTO+CAIO 동시 이탈(3/27). AI 전략 구조적 리셋 — 1~2개월 공백 예상 | 모니터링 |
| 4 | **Claude Haiku 3 은퇴(4/20)** | Agentic AI | 서브에이전트 모델 마이그레이션 필요. 1M context beta도 4/30 종료 | D-17 |

---

## 3. 경쟁사 동향

### SKT — 🟡 주목
- 정재헌 CEO 체제 출범(3/26). **점유율 40% 탈환 + 1.7조 비과세 배당**(업계 최초)으로 경영 정상화 총력
- AI 전략: 1인 1 AI 에이전트 전환 + SK AX Agent Builder 투트랙. PQC 분야 Thales 5G SIM 협력으로 선두 유지
- 단기 어젠다가 기술→경영 정상화로 전환. 공격적 마케팅(단말 보조금, 요금 할인) 가능성 → 가격 경쟁 리스크

### KT — 🔴 경고
- **CTO 오승필 + CAIO 신동훈 동시 이탈**(3/27) → AI 리더십 구조적 공백
- 박윤영 CEO 3/31 취임, 대규모 조직 개편 예고. MS 협력 AI 2트랙 전략 재구조화 시사
- 재무 양호(영업이익 2.47조, +205%)하나 AI 전략 실행 연속성 불투명
- **4월 첫째 주 AI 리더십 인사 + 조직 개편 발표 주시 필수**

---

## 4. 포트폴리오 현황 변동

| 도메인 | L2 기술 | 이전 | 금주 | 변동 사유 |
|--------|---------|------|------|-----------|
| Voice AI | Voice Synthesis | 🟡 | 🔴 | Voxtral 오픈소스 + xAI 진입 → 가격 파괴·경쟁 축 재편 |
| Voice AI | Voice Cloning | 🟡 | 🟡 | 오픈소스 클로닝 무료화로 위협 심화, 탐지 실효성 의문 지속 |
| Voice AI | Interrupt & Turn-Taking | 🟡 | 🟡 | xAI 신규 진입, 의미 기반 인터럽트 독립 연구 영역 분리 |
| Secure AI | On-Device PQC | 🟡 | 🔴 | Google 2029 데드라인 + Android 17 ML-DSA 전면 탑재 |
| Secure AI | On-Device 동형암호 | 🟡 | 🟡 | FHE 97% 오버헤드 감소, $32B 기관급 실도입 — 실용화 가속 |
| Secure AI | 스팸/피싱 감지 | 🟢 | 🟡 | AI 피싱 204% 급증, QRishing 부상 |
| Agentic AI | Agent Orchestration | 🟡 | 🟡 | 3대 프로토콜 스택 확정, 평가·거버넌스 프로덕션 게이트화 |
| Agentic AI | 기타 10개 L3 | 🟢 | 🟢 | 유의미 변화 없음 (정착 단계 지속) |

---

## 5. 다음 주 주목 이슈

| # | 이슈 | 도메인 | 주시 포인트 |
|---|------|--------|------------|
| 1 | MCP Dev Summit 결과 (4/2-3) | Agentic AI | Auth·Observability·HTTP transport 2026 로드맵 확정 여부 |
| 2 | KT 박윤영 체제 조직 개편 | 경쟁사 | AI 리더십(CTO/CAIO 후임) 인사 결과 — 경쟁 구도 변동 가능 |
| 3 | Claude Haiku 3 은퇴 대비 (D-17) | Agentic AI | 서브에이전트 haiku→haiku-4.5 마이그레이션 검증 |
| 4 | EU AI Act 투명성 CoP 초안 | Voice AI | 5-6월 확정 예정, 다층 워터마킹 의무화 방향 — 4월 중 초안 주시 |
| 5 | FIPS 140-2 종료 카운트다운 (D-175) | Secure AI | 하반기 삼중 데드라인(FIPS·CRA·CNSA 2.0) 대비 로드맵 점검 |

---

## 규제 카운트다운

| 규제 | 시행일 | D-day |
|------|--------|-------|
| Claude Haiku 3 은퇴 | 2026-04-20 | D-17 |
| 1M Context Beta 종료 | 2026-04-30 | D-27 |
| EU AI Act Article 6/50 전면 적용 | 2026-08-02 | D-121 |
| EU CRA 보고 의무 | 2026-09-11 | D-161 |
| FIPS 140-2 인증 종료 | 2026-09-21 | D-171 |
| CNSA 2.0 NSS 조달 의무화 | 2027-01-01 | D-273 |

---

*본 요약은 Agentic AI(2026-04-02), Voice AI(2026-03-30), Secure AI(2026-03-30), 경쟁사 브로드스캔(2026-03-30) 주간 리포트를 종합한 것입니다.*
