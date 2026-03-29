---
topic: Personal Intelligence
domain: voice-ai
l2_topic: personal-intelligence
date: 2026-03-27
type: wtis-research
agent: research-deep
confidence: medium
status: completed
sources_used: [websearch]
---

# Research: Personal Intelligence

## Executive Summary

> AI 개인 비서·컴패니언 시장은 2025년 기준 약 370억 달러 규모로, 연평균 31% 성장률로 2034년 4,360억 달러에 달할 것으로 전망된다 [[G-01]](#ref-g-01), [[G-02]](#ref-g-02). Personal Intelligence를 구성하는 3개 L3(Persona Plugin, Relationship Graph, Context-Action Recommendation) 모두 2025~2026년에 걸쳐 주요 빅테크의 실제 서비스 적용이 가시화되는 시점이다 — Apple Intelligence 개인 맥락 기능(2026 상반기 출시 예정), Google Gemini Personal Intelligence 무료 개방(2026년 3월), ChatGPT 전체 대화 이력 참조(2025년 4월). 독립 AI 컴패니언 스타트업들(Inflection→Microsoft, Character.ai→Google 라이선싱)은 빅테크에 흡수되는 구조적 통합 추세를 보이며, 통신사는 통화 이력·위치·네트워크 데이터라는 고유 자산을 활용한 차별화 포지션을 모색할 수 있다. 다만 GDPR/개인정보보호 규제는 데이터 기반 개인화 서비스의 핵심 리스크 요인이다.
>
> **신뢰도**: 시장 수치는 복수 출처 교차 검증 완료 [B]. 기업 발표 내용은 공식 발표 기준 [A/B]. SKT/KT 국내 서비스 세부 지표는 단일 소스 [C] 포함.

---

## 연구 질문

통신사 CTO 직속 전략팀 관점에서 Personal Intelligence (Persona Plugin, Relationship Graph, Context-Action Recommendation) 3개 L3의 시장 성숙도, 기술 현황, 경쟁사 동향, 투자 흐름을 파악하고, 통신사의 차별화 기회와 리스크를 정리한다. 최종 Go/No-Go 판정 및 전략 권고는 이 리서치의 범위 밖이다.

---

## 1. 시장 분석

#### 1.1 글로벌 시장 규모

**시장 규모 추정치 (복수 출처 교차 검증)**

| 리서치사 | 2025 기준값 | 2030/2034 전망 | CAGR | 출처 |
|---------|------------|---------------|------|------|
| Grand View Research | $28.19B (2024) | $140.75B (2030) | 30.8% | [[G-01]](#ref-g-01) |
| Precedence Research | $37.12B (2025) | $552.49B (2035) | 31.0% | [[G-02]](#ref-g-02) |
| Fortune Business Insights | $37.73B (2025) | $435.9B (2034) | 31.24% | [[G-03]](#ref-g-03) |
| MarketsandMarkets (AI Assistant) | $3.35B (2025) | $21.11B (2030) | 44.5% | [[G-04]](#ref-g-04) |

*참고: Grand View와 Precedence/Fortune의 기준값 차이는 "AI Companion"과 "AI Assistant" 정의 범위의 차이에서 기인. 컴패니언 시장이 더 넓은 개념을 포함.*

**성장 드라이버**
- On-device AI 하드웨어 확산: Apple M5 뉴럴 엔진, Qualcomm NPU, Google Tensor 칩셋 [[G-19]](#ref-g-19)
- 개인정보 보호 요구 증가: 클라우드 전송 최소화, 온디바이스 처리 수요 [[G-20]](#ref-g-20)
- 감정 인식·장기 기억 기술 성숙: Mem0, Graphiti 등 오픈소스 메모리 레이어 확산 [[G-09]](#ref-g-09)
- 멘탈 헬스·고령화 수요: AI 컴패니언 앱 구독 수익 2025년 상반기 기준 $221M 소비자 지출 [[G-14]](#ref-g-14)

#### 1.2 통신사 시장 기회

통신사는 AI 개인화 서비스에 고유한 데이터 자산을 보유한다:
- 통화·문자 이력, 위치 이동 패턴, 네트워크 품질 데이터
- 고객 계약 기반 실명 인증 및 장기 관계 [[G-11]](#ref-g-11)

Vodafone TOBi(고객 문의 70% 자동 처리), AT&T 네트워크 AI 에이전트, Telefónica Aura 플랫폼 등 글로벌 통신사들이 AI 개인화에 투자 중이며, AI에 투자한 통신사들의 평균 ROI는 일반 디지털 투자 대비 약 4배 수준으로 보고된다 [[G-11]](#ref-g-11).

---

## 2. 기술 성숙도

#### 2.1 Persona Plugin (개인화 페르소나)

**Technology Readiness Level (TRL): 7~8 — 상용 배포 단계**

- **Character.ai**: 캐릭터 생성 시 Long Description, Definition(Advanced), 예시 대화 등을 통한 심층 페르소나 설정. 커뮤니티 생성 캐릭터 라이브러리. MIT Technology Review가 2026년 10대 혁신 기술 중 하나로 선정 [[G-05]](#ref-g-05).
- **Replika**: 단일 AI 컴패니언의 감정 트래킹·적응 특화. "페르소나 캐릭터 다양성" 보다 "관계의 깊이"에 초점. 누적 펀딩 $11M, 연간 매출 약 $3M 수준(소규모) [[G-15]](#ref-g-15).
- **Hume AI**: 감정 인식 특화. EVI(Empathic Voice Interface) — 음성 톤 분석으로 감정 상태 파악, 선호도 최적화. 2024년 3월 시리즈 B $50M 조달 (EQT Ventures 리드) [[E-01]](#ref-e-01).
- 기술 핵심: 사용자 성격 모델(Big Five 트레이트), 대화 스타일 적응, 감정 표현 다양성.

#### 2.2 Relationship Graph (관계 그래프)

**TRL: 6~7 — 초기 상용화 / 연구-상용 경계**

- **Mem0**: AI 에이전트를 위한 장기 메모리 레이어 오픈소스. 대화에서 자동 정보 추출·저장·검색. LOCOMO 벤치마크에서 OpenAI 내장 메모리 대비 26% 정확도 향상, p95 레이턴시 91% 감소, 토큰 사용량 90% 절감 [[G-09]](#ref-g-09). 2025년 10월 시리즈 A $20M + 시드 $3.9M, 총 $24M 조달 (Basis Set Ventures, YC 참여) [[G-09]](#ref-g-09). GitHub 41,000+ 스타.
- **Graphiti (Zep AI)**: 실시간 시간적 지식 그래프 구축. 에피소드(대화)에서 구조화된 관계 자동 추출. 언제 무엇이 사실이었는지를 포함한 시간 축 모델링 [[G-13]](#ref-g-13).
- **ChatGPT**: 2025년 4월 전체 대화 이력 참조 기능 출시. "저장 메모리"와 "대화 이력" 두 가지 방식 병용. Plus/Pro 사용자 우선, 무료 사용자에게 경량 버전 2025년 6월 제공 [[E-03]](#ref-e-03).
- **Gemini**: 과거 대화 기반 장기 기억, 사용자 선호 학습. 2026년 3월 Personal Intelligence(Gmail, Photos, YouTube 이력 연동) 무료 전환 [[G-07]](#ref-g-07). ChatGPT 등 타 AI 앱에서 메모리·컨텍스트 임포트 도구 출시(2026년 3월 26일) [[G-08]](#ref-g-08).
- 기술 핵심: 벡터 임베딩 기반 시맨틱 검색 + 지식 그래프 하이브리드. 개인 지식 그래프(PKG)의 동적 갱신 — 캘린더, 연락처, 이메일, 위치 연동.

#### 2.3 Context-Action Recommendation (맥락 기반 행동 추천)

**TRL: 6~8 — 플랫폼별 격차 큼**

- **Apple Intelligence Personal Context**: 기기 내 이메일·메시지·캘린더 접근 기반 맞춤 응답. "마지막으로 Jen과 통화한 게 언제야?" 등 장기 맥락 질의 지원. 2025년 10월 기준 지연 [[G-06]](#ref-g-06), iOS 26에서 Gemini 파워드 LLM Siri로 2026년 상반기 출시 예정 [[G-17]](#ref-g-17).
- **Google Gemini**: 멀티모달 맥락(화면 인식, 실시간 카메라, 캘린더·이메일 연동). Personal Intelligence 기능 2026년 1월 발표, 3월 무료 개방 [[G-07]](#ref-g-07).
- **Lenovo Qira**: 앱 기반이 아닌 시스템 레벨 Ambient Intelligence. 사용자 호출 없이 백그라운드에서 맥락 파악 → 선제적 제안. 온디바이스 실행으로 오프라인 작동 [[G-21]](#ref-g-21).
- **ContextAgent (학술)**: 웨어러블 센서(비디오, 오디오) 기반 대규모 감각 맥락을 LLM 에이전트에 주입하는 연구. 선제적 행동 추천 최초 시스템으로 논문화 [[P-01]](#ref-p-01).
- 기술 핵심: 온디바이스 추론 + 클라우드 하이브리드, 멀티모달 맥락 융합(화면·음성·위치·캘린더), 선제적(proactive) vs. 반응적(reactive) 트리거 설계.

---

## 3. 경쟁사/플레이어 동향

**주요 플레이어 동향**

| 기업 | 동향 | 출처 |
|------|------|------|
| Apple | Personal Context 기능(이메일·메시지·캘린더 연동 Siri) 2025년 10월 기준 미출시 → Google Gemini 파워드 LLM Siri로 2026 상반기 출시 예정. Apple Silicon 온디바이스 처리 + Private Cloud Compute 이중 구조 | [[G-06]](#ref-g-06), [[G-17]](#ref-g-17) |
| Google | Gemini Personal Intelligence(Gmail·Photos·YouTube 연동) 2026년 3월 무료 전환. 타 AI 앱 메모리 임포트 도구 출시(2026-03-26). 컨텍스트 윈도우 100만 토큰, Google Workspace 크로스앱 기억 | [[G-07]](#ref-g-07), [[G-08]](#ref-g-08) |
| OpenAI | ChatGPT 전체 대화 이력 참조 2025년 4월 출시. 저장 메모리 + 대화 이력 이중 기억 구조. 무료 사용자 경량 버전 2025년 6월 제공 | [[E-03]](#ref-e-03) |
| Samsung | One UI 8.5에서 Bixby + Perplexity AI 통합. Now Brief(사용자 일정 기반 선제적 브리핑), 캘린더 이벤트 제안, 배터리 절약 팁 개인화. MWC 2026에서 Galaxy AI 생태계 확장 발표 | [[E-04]](#ref-e-04), [[G-16]](#ref-g-16) |
| Microsoft | Inflection AI 공동창업자 Mustafa Suleyman 영입, $650M Inflection 모델 라이선스 취득(2024년 3월). Suleyman이 Microsoft AI 부문 CEO로 Copilot 총괄 | [[G-10]](#ref-g-10) |
| Character.ai | Google $2.7B 역취득(Reverse Acquihire) — 공동창업자 Noam Shazeer 구글 복귀, 모델 비독점 라이선스. Character.ai는 독립 운영 유지하나 2025년 8월 매각/신규 펀딩 논의 재개 보도 | [[E-02]](#ref-e-02), [[G-12]](#ref-g-12) |
| SKT | 에이닷 "AI 개인비서"로 전면 개편 — 노트(회의록 자동 생성)·브리핑(일상 종합 분석·선제 제공) 베타 출시. 2026년 조직개편에서 에이닷을 조직명 전면에 배치, 구독 모델 전환·AI 수익화 가속화 방침 | [[E-05]](#ref-e-05), [[E-06]](#ref-e-06) |
| KT | AI 통화비서(소상공인 대상 전화 대응 AI). AI 빅또리 비서(KBO 리그 전용 챗봇 에이전트, 티켓·경기 정보). 개인화 마케팅 플랫폼 B2B 제공 중 | [[G-22]](#ref-g-22) |
| Hume AI | 감정 인식 AI 음성 인터페이스(EVI) 전문. Series B $50M(2024년 3월). 음성 톤 기반 감정 파악, 사용자 만족도 최적화 응답 생성 | [[E-01]](#ref-e-01) |
| Replika | 총 펀딩 $11M, 연간 매출 약 $3M. 단일 AI 컴패니언 심층 감정 관계에 특화. Nomi 등 경쟁사 대비 시장 점유 압박 | [[G-15]](#ref-g-15) |
| Mem0 | AI 에이전트 장기 메모리 레이어 오픈소스. 총 $24M 조달(YC·Peak XV). GitHub 41K 스타, Python 패키지 1,300만+ 다운로드 | [[G-09]](#ref-g-09) |

---

## 4. 제품/서비스 스펙 비교

**L3 기능별 주요 플랫폼 스펙**

| 기업 | 기억/맥락 범위 | 온디바이스 처리 | 출처 |
|------|--------------|---------------|------|
| Apple Intelligence | 기기 내 이메일·메시지·캘린더·사진 (출시 예정) | 온디바이스 우선 + Private Cloud Compute | [[G-06]](#ref-g-06) |
| Google Gemini | Gmail·Photos·YouTube 이력·Docs·Workspace (무료 제공) | 클라우드 우선 + Private AI Compute | [[G-07]](#ref-g-07) |
| ChatGPT | 전체 대화 이력 + 저장 메모리 (Plus/Pro 풀버전, Free 경량) | 클라우드 | [[E-03]](#ref-e-03) |
| Samsung Bixby | 사용자 일정·이용 패턴 (Now Brief) | 온디바이스 + Perplexity 클라우드 | [[E-04]](#ref-e-04) |
| Mem0 (인프라) | LLM 대화 자동 추출 메모리, 모델 무관 | 자체 서버 또는 클라우드 | [[G-09]](#ref-g-09) |
| SKT 에이닷 | 사용자 루틴·일정·콘텐츠 선호 (브리핑 베타) | 공개 정보 없음 | [[E-05]](#ref-e-05) |
| KT AI 비서 | 통화 대응·스포츠 정보 도메인 한정 | 공개 정보 없음 | [[G-22]](#ref-g-22) |

---

## 5. 학술 동향

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory" (Mem0 Team, 2025) | 프로덕션 AI 에이전트용 장기 메모리 시스템 설계. LOCOMO 벤치마크 26% 정확도 향상, 90% 토큰 절감 입증 | [[P-02]](#ref-p-02) |
| "ContextAgent: Context-Aware Proactive LLM Agents with Open-World Sensory Perceptions" (2025) | 웨어러블 센서 기반 실세계 감각 맥락 → LLM 에이전트 선제 행동. 최초 문맥 인식 선제적 에이전트 프레임워크 | [[P-01]](#ref-p-01) |
| "ProPerSim: Developing Proactive and Personalized AI Assistants through User-Assistant Simulation" (2025) | 사용자-어시스턴트 시뮬레이션으로 선제적·개인화 AI 비서 훈련 방법론 | [[P-03]](#ref-p-03) |
| "Situation Graph Prediction: Structured Perspective Inference for User Modeling" (2026) | 사용자 정체성을 고립 선호가 아닌 상황(맥락·감정·목표) 궤적으로 모델링 | [[P-04]](#ref-p-04) |
| "MemX: A Local-First Long-Term Memory System for AI Assistants" (2026) | 로컬 우선 장기 메모리 시스템. 프라이버시 보존 온디바이스 기억 아키텍처 | [[P-05]](#ref-p-05) |

**연구 방향 요약**
- 메모리 효율화: 전체 컨텍스트 대비 선택적 기억 검색으로 레이턴시·비용 절감
- 선제적 에이전트: 사용자 호출 없이 맥락 파악 후 자율 행동 (Proactive vs. Reactive 경계 허물기)
- 개인 지식 그래프: 시간 축 포함 구조화 관계 표현, PKG + 벡터 임베딩 하이브리드
- 감정·상황 모델링: 감정 상태, 의도, 사회적 맥락을 통합한 사용자 모델

---

## 6. 특허 동향

intel-store MCP 미연결 환경으로 특허 DB 직접 조회 불가. 공개 정보 기반 정성 분석.

- **Apple**: 온디바이스 LLM 추론, 프라이버시 보존 개인화 관련 특허 다수 출원 (공개 정보 있음, 구체적 건수 미확인)
- **Google**: 사용자 맥락 그래프, 크로스앱 개인화, 장기 메모리 아키텍처 관련 특허 출원 경향
- **Samsung**: 온디바이스 AI 인터페이스, 사용자 행동 예측 관련 특허 출원
- **Mem0/Zep 등 스타트업**: 특허보다 오픈소스 공개 전략으로 생태계 선점 추구

*정량적 특허 건수·출원인 순위는 USPTO/KIPRIS 직접 조회 필요. 추가 검증 권고.*

---

## 7. 기업 발언 & 보도자료

**공식 발언 및 보도자료**

- **[E-01] Hume AI Series B 발표 (2024년 3월)**: "EVI는 감정 인식 AI의 첫 번째 상용 인터페이스다. 음성 톤으로 사용자 감정 상태를 파악하고 선호도를 최적화한다." — Hume AI 공식 보도자료 [[E-01]](#ref-e-01)

- **[E-02] Character.ai ↔ Google 라이선싱 딜 (2024년 8월)**: Google의 $2.7B 역취득 구조 — 공동창업자 Noam Shazeer 구글 복귀 및 모델 비독점 라이선스. "AI companion 기술의 빅테크 통합 가속화"의 대표 사례로 규제당국(DOJ) 주목 [[E-02]](#ref-e-02)

- **[E-03] OpenAI ChatGPT 메모리 업데이트 발표 (2025년 4월)**: "ChatGPT가 이제 모든 과거 대화를 참조할 수 있다. 사용자가 저장한 메모리와 대화 이력 두 가지 방식으로 더 관련성 높고 맞춤화된 응답을 제공한다." — OpenAI 커뮤니티 공식 발표 [[E-03]](#ref-e-03)

- **[E-04] Samsung Galaxy AI MWC 2026 발표**: "One UI 8.5의 새로운 Bixby는 사용자 일정·이용 패턴에 기반한 Now Brief 개인화 브리핑을 제공하며, Perplexity AI와의 통합으로 복잡한 추론 작업을 처리한다." — Samsung Global Newsroom [[E-04]](#ref-e-04)

- **[E-05] SKT 에이닷 AI 개인비서 개편 발표 (2025년)**: "에이닷이 단순 응답을 넘어 사용자의 루틴을 기억하고 일정을 알아서 챙겨주는 AI 개인비서로 진화한다. 브리핑 서비스는 시간대별 동선에 맞는 기상 정보를 자동 제공한다." — AI타임스 보도 [[E-05]](#ref-e-05)

- **[E-06] SKT 2026 조직개편 방침**: "에이닷을 조직명 전면에 내세우며 구독 모델 전환과 AI 수익화에 속도를 내겠다." — The Bell 보도 (2025년 12월) [[E-06]](#ref-e-06)

---

## 8. 투자/M&A 트렌드

#### 8.1 주요 딜 타임라인 (2024~2026)

| 연도 | 딜 | 금액 | 특이사항 |
|------|-----|------|---------|
| 2024년 3월 | Microsoft ← Inflection AI (acqui-hire) | $650M 라이선스 + 팀 이적 | Mustafa Suleyman, Karen Simonyan 영입. Pi 챗봇은 B2B 피봇 | [[G-10]](#ref-g-10) |
| 2024년 3월 | Hume AI Series B | $50M | EQT Ventures 리드, EVI 출시 동시 발표 | [[E-01]](#ref-e-01) |
| 2024년 8월 | Google ← Character.ai (역취득) | $2.7B 라이선스 | Shazeer 구글 복귀, Character.ai 독립 유지. DOJ 검토 | [[E-02]](#ref-e-02) |
| 2025년 9월 | Meela (시니어 AI 컴패니언) Seed | $3.5M | 고령자 대상 AI 음성 컴패니언 전문 스타트업 | [[G-18]](#ref-g-18) |
| 2025년 10월 | Mem0 Series A | $20M (+시드 $3.9M) | Basis Set Ventures 리드, YC·Peak XV 참여 | [[G-09]](#ref-g-09) |
| 2025년 8월 | Character.ai | 미정 | 매각 또는 신규 펀딩 논의 재개 보도 (단일 소스 [C]) | [[G-12]](#ref-g-12) |

#### 8.2 구조적 트렌드

- **독립 앱 → 플랫폼 통합**: Inflection→Microsoft, Character.ai→Google 구조는 AI 컴패니언 원천 기술이 대형 플랫폼에 흡수되는 패턴을 보여준다. 독립 AI 컴패니언 앱의 생존은 틈새 시장(감성, 고령자, 특정 도메인) 집중 또는 B2B API 전환으로 수렴하는 중.
- **인프라 레이어 투자**: Mem0, Graphiti 등 메모리·지식 그래프 인프라 레이어가 별도 투자 대상으로 부상.
- **AI 컴패니언 앱 수익화**: 2025년 상반기 $221M 소비자 지출, 연간 $120M 수익 궤도 예상. 상위 10% 앱이 89% 수익 집중 [[G-14]](#ref-g-14).
- **글로벌 AI M&A 2025**: 전체 M&A 규모 2025년 기준 $4.9조(+40% YoY) 사상 최대. AI가 VC 자금의 50%+ 차지 [[G-23]](#ref-g-23).

---

## 5. 통신사 적용 가능성

#### 5.1 통신사 고유 자산

통신사는 AI 개인화에 활용할 수 있는 독점적 데이터를 보유한다:
- **통화·문자 이력**: 관계 그래프 구성의 원재료 (누구와, 얼마나 자주, 어떤 맥락)
- **위치·이동 패턴**: 일상 루틴 파악, 맥락 기반 선제 추천의 핵심 신호
- **네트워크 품질 데이터**: 서비스 경험과 연계된 사용자 상태 파악
- **실명 계약 관계**: 장기 고객 데이터 축적 기반

80%의 고객이 개인화된 경험을 위해 데이터를 공유할 의향이 있다고 응답 [[G-11]](#ref-g-11). 단, 이 데이터는 통신사 서비스 이용 목적 동의 하에 수집된 것으로, AI 개인화 목적 재활용을 위한 별도 동의 획득이 필요하다.

#### 5.2 국내 현황

- **SKT 에이닷**: 2026년 조직 전면에 배치하며 AI 수익화 핵심 서비스로 포지셔닝. 구독 모델 전환 추진 중. 브리핑(일상 종합 분석)·노트(회의록 자동 생성) 베타 운영 [[E-06]](#ref-e-06).
- **KT**: AI 통화비서(소상공인 B2B), AI 빅또리 비서(도메인 특화 챗봇). 범용 개인 AI 비서 서비스 부재 — SKT 대비 소비자 개인화 AI에서 후발 위치 [[G-22]](#ref-g-22).

#### 5.3 규제 리스크

- **GDPR**: EU 개인정보보호 규정. 2025년 11월 EU 집행위원회 Digital Omnibus 개정 제안으로 AI 개발 목적 개인정보 처리 "정당한 이익" 조항 신설 논의 중이나, 아직 시행 미정 [[G-24]](#ref-g-24).
- **한국 개인정보보호법**: 목적 외 이용 제한. 통신 데이터를 AI 개인화에 활용 시 별도 동의 필요.
- **ePrivacy**: 유럽 통신사의 위치·통화 데이터 활용 규제. 빅테크 로비로 완화 논의 중이나 불확실 [[G-24]](#ref-g-24).

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- 글로벌 AI 컴패니언 시장 규모 (30~31% CAGR) — 3개 이상 독립 리서치사 교차 검증
- Apple Intelligence Personal Context 기능 지연 및 2026 출시 계획 — CNBC, MacRumors, Apple 관련 다수 보도
- Google Gemini Personal Intelligence 무료 개방 (2026년 3월) — Fortune, Google 공식 발표
- OpenAI ChatGPT 전체 이력 참조 기능 (2025년 4월) — OpenAI 공식 발표
- Microsoft-Inflection 딜 ($650M, 2024년 3월) — 다수 공신력 있는 보도
- Google-Character.ai 딜 ($2.7B, 2024년 8월) — Bloomberg, CNBC 등 복수 확인
- Hume AI Series B ($50M, 2024년 3월) — 공식 보도자료
- Mem0 Series A ($24M, 2025년 10월) — TechCrunch 보도
- SKT 에이닷 2026 전략 방향 — The Bell, AI타임스 보도

**추가 검증 필요 [C/D]:**
- Character.ai 매각 논의 재개 (단일 소스 [D]) — 미확인 보도
- SKT/KT 서비스 기술 세부 스펙 (온디바이스 처리 여부 등) — 공개 정보 없음
- KT의 범용 AI 개인비서 로드맵 — 공개 발표 부재
- Replika 연간 매출 $3M (추정치 [C])

**데이터 공백:**
- 특허 정량 분석 (건수, 출원인 순위) — intel-store MCP 미연결로 미조회
- 한국 AI 개인비서 시장 규모 별도 통계 — 글로벌 수치에 포함, 분리 통계 없음
- NTT, Verizon, AT&T 등 글로벌 통신사 개인화 AI 상세 스펙 — 심층 조회 미실시

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Grand View Research — AI Companion Market Report 2030 | [링크](https://www.grandviewresearch.com/industry-analysis/ai-companion-market-report) | market-report | 2025 | [B] |
| <a id="ref-g-02"></a>G-02 | Precedence Research — AI Companion Market Size to Hit USD 552.49B by 2035 | [링크](https://www.precedenceresearch.com/ai-companion-market) | market-report | 2025 | [B] |
| <a id="ref-g-03"></a>G-03 | Fortune Business Insights — AI Companion Market Growth 2026-2034 | [링크](https://www.fortunebusinessinsights.com/ai-companion-market-113258) | market-report | 2025 | [B] |
| <a id="ref-g-04"></a>G-04 | MarketsandMarkets — AI Assistant Market Size, Share, Trends | [링크](https://www.marketsandmarkets.com/Market-Reports/ai-assistant-market-40111511.html) | market-report | 2025 | [B] |
| <a id="ref-g-05"></a>G-05 | Skywork AI — The Ultimate 2026 Guide to Character AI | [링크](https://skywork.ai/skypage/en/ultimate-guide-character-ai-roleplay-companionship/2032056304473153536) | blog | 2026 | [C] |
| <a id="ref-g-06"></a>G-06 | Fello AI — The State of Apple Intelligence & Siri in October 2025 | [링크](https://felloai.com/the-state-of-apple-intelligence-siri-in-october-2025-apples-ai-vision-vs-reality/) | news | 2025-10 | [B] |
| <a id="ref-g-07"></a>G-07 | Fortune — Google connects Gemini to users' emails and photos | [링크](https://fortune.com/2026/01/14/google-gemini-ai-personal-assistant-gmail-photos-youtube-history-personal-intelligence/) | news | 2026-01-14 | [B] |
| <a id="ref-g-08"></a>G-08 | MacRumors — Google Launches Gemini Import Tool for Switching From ChatGPT, Claude | [링크](https://www.macrumors.com/2026/03/26/gemini-import-tool/) | news | 2026-03-26 | [B] |
| <a id="ref-g-09"></a>G-09 | TechCrunch — Mem0 raises $24M from YC, Peak XV and Basis Set | [링크](https://techcrunch.com/2025/10/28/mem0-raises-24m-from-yc-peak-xv-and-basis-set-to-build-the-memory-layer-for-ai-apps/) | news | 2025-10-28 | [B] |
| <a id="ref-g-10"></a>G-10 | DeepLearning.AI The Batch — Microsoft Pays Inflection AI $650 Million, Hires Most of its Staff | [링크](https://www.deeplearning.ai/the-batch/microsoft-pays-inflection-ai-650-million-hires-most-of-its-staff/) | news | 2024-03 | [B] |
| <a id="ref-g-11"></a>G-11 | Tredence — 7 Agentic AI Trends Transforming Telecom in 2025 | [링크](https://www.tredence.com/blog/agentic-ai-trends-telecom) | blog | 2025 | [B] |
| <a id="ref-g-12"></a>G-12 | Tech Startups — Character.ai in talks to sell or raise new funding | [링크](https://techstartups.com/2025/08/20/character-ai-in-talks-to-sell-or-raise-new-funding-as-chatbot-costs-pile-up/) | news | 2025-08-20 | [C] |
| <a id="ref-g-13"></a>G-13 | GitHub — getzep/graphiti: Build Real-Time Knowledge Graphs for AI Agents | [링크](https://github.com/getzep/graphiti) | blog | 2025 | [B] |
| <a id="ref-g-14"></a>G-14 | TechCrunch — AI companion apps on track to pull in $120M in 2025 | [링크](https://techcrunch.com/2025/08/12/ai-companion-apps-on-track-to-pull-in-120m-in-2025/) | news | 2025-08-12 | [B] |
| <a id="ref-g-15"></a>G-15 | Tracxn — Replika 2026 Company Profile | [링크](https://tracxn.com/d/companies/replika/__rr2kodByhjtv_6oVe5NqDvmeW-R7FJvAXqOeHhy59zs) | database | 2026 | [C] |
| <a id="ref-g-16"></a>G-16 | Samsung Global Newsroom — Samsung Advances Galaxy AI at MWC 2026 | [링크](https://news.samsung.com/global/samsung-advances-galaxy-ai-and-its-connected-ecosystem-at-mwc-2026) | press-release | 2026-02 | [A] |
| <a id="ref-g-17"></a>G-17 | MacRumors — LLM Siri: Complete Guide to Apple's AI Assistant Overhaul Coming in 2026 | [링크](https://www.macrumors.com/guide/llm-siri/) | news | 2026 | [B] |
| <a id="ref-g-18"></a>G-18 | Tracxn — Meela 2026 Company Profile | [링크](https://tracxn.com/d/companies/meela/__DvBlTvWn_PPG4vnM-zceildYs8S94s_bo6RvKD_VlKE) | database | 2026 | [C] |
| <a id="ref-g-19"></a>G-19 | TechGenyz — On-Device AI Smartphones 2025: Powerful Offline Intelligence | [링크](https://techgenyz.com/on-device-ai-smartphones-privacy-performance/) | blog | 2025 | [B] |
| <a id="ref-g-20"></a>G-20 | WebProNews — Apple's Privacy-First AI Strategy: On-Device LLMs by 2026 | [링크](https://www.webpronews.com/apples-privacy-first-ai-strategy-on-device-llms-by-2026/) | blog | 2025 | [B] |
| <a id="ref-g-21"></a>G-21 | Lenovo StoryHub — Introducing Lenovo and Motorola Qira | [링크](https://news.lenovo.com/pressroom/press-releases/lenovo-unveils-lenovo-and-motorola-qira/) | press-release | 2025 | [A] |
| <a id="ref-g-22"></a>G-22 | 스포츠서울 — KT 일냈다! KBO리그 '최초' AI 빅또리 비서 서비스 오픈 | [링크](https://www.sportsseoul.com/news/read/1543887) | news | 2025-09 | [B] |
| <a id="ref-g-23"></a>G-23 | CNBC — The global M&A boom is rolling into 2026 as AI sparks deal frenzy | [링크](https://www.cnbc.com/2026/02/25/global-ma-boom-surges-2026-ai-mega-deals-capital-squeeze-merger-and-acquisition.html) | news | 2026-02-25 | [B] |
| <a id="ref-g-24"></a>G-24 | IAPP — European Commission proposes significant reforms to GDPR, AI Act | [링크](https://iapp.org/news/a/european-commission-proposes-significant-reforms-to-gdpr-ai-act) | news | 2025 | [B] |
| <a id="ref-e-01"></a>E-01 | Hume AI — Series B $50M Fundraise and Empathic Voice Interface Announcement | [링크](https://www.hume.ai/blog/series-b-evi-announcement) | press-release | 2024-03-26 | [A] |
| <a id="ref-e-02"></a>E-02 | Bloomberg — Character.AI Co-Founders Hired by Google in Licensing Deal | [링크](https://www.bloomberg.com/news/articles/2024-08-02/character-ai-co-founders-hired-by-google-in-licensing-deal) | news | 2024-08-02 | [A] |
| <a id="ref-e-03"></a>E-03 | OpenAI Community — ChatGPT can now reference all past conversations (2025-04-10) | [링크](https://community.openai.com/t/chatgpt-can-now-reference-all-past-conversations-april-10-2025/1229453) | IR/발표 | 2025-04-10 | [A] |
| <a id="ref-e-04"></a>E-04 | Samsung Global Newsroom — Samsung Introduces the New Bixby in One UI 8.5 | [링크](https://news.samsung.com/global/samsung-introduces-the-new-bixby-in-one-ui-8-5) | press-release | 2025-11 | [A] |
| <a id="ref-e-05"></a>E-05 | AI타임스 — SKT 에이닷, 'AI 개인비서'로 진화 | [링크](https://www.aitimes.kr/news/articleView.html?idxno=32044) | news | 2025 | [B] |
| <a id="ref-e-06"></a>E-06 | The Bell — [2026 SKT 리빌딩] '에이닷'을 조직 전면에 'AI 수익화 방점' | [링크](https://m.thebell.co.kr/m/newsview.asp?svccode=04&newskey=202512311210233800102717) | news | 2025-12-31 | [B] |
| <a id="ref-p-01"></a>P-01 | ContextAgent: Context-Aware Proactive LLM Agents with Open-World Sensory Perceptions (2025) | [링크](https://arxiv.org/abs/2505.14668) | paper | 2025-05 | [A] |
| <a id="ref-p-02"></a>P-02 | Mem0 Team — Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory (2025) | [링크](https://arxiv.org/abs/2504.19413) | paper | 2025-04 | [A] |
| <a id="ref-p-03"></a>P-03 | ProPerSim: Developing Proactive and Personalized AI Assistants through User-Assistant Simulation (2025) | [링크](https://arxiv.org/html/2509.21730) | paper | 2025-09 | [A] |
| <a id="ref-p-04"></a>P-04 | Situation Graph Prediction: Structured Perspective Inference for User Modeling (2026) | [링크](https://arxiv.org/html/2602.13319) | paper | 2026-02 | [A] |
| <a id="ref-p-05"></a>P-05 | MemX: A Local-First Long-Term Memory System for AI Assistants (2026) | [링크](https://arxiv.org/html/2603.16171) | paper | 2026-03 | [A] |
