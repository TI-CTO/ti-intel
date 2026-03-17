---
type: wtis-research
topic: hybrid-ai-infra
domain: agentic-ai
date: 2026-03-16
agent: research-deep
confidence: medium-high
status: completed
sources_used: [websearch, prev-research-w12]
prior_reports:
  - outputs/reports/weekly/2026-03-16_research-5g-6g-ai-ran.md
  - outputs/reports/weekly/2026-03-16_research-ondevice-slm.md
---

# Hybrid AI Infra — WTIS 심층 리서치

> **분석 범위**: On-Device sLM / 실시간 화자분할(2인) / Edge AI / 5G SA·6G AI-RAN — 4개 L3 통합 분석
> **분석 기준일**: 2026-03-16 | **선행 리서치 반영**: W12 Deep Research 2건 (5G AI-RAN, On-Device sLM)
> **보고서 목적**: WTIS 선정검증(SKILL-1) 입력 데이터 수집. 판정(Go/No-Go) 미포함.

---

## Executive Summary

Hybrid AI Infra 4개 L3 기술은 모두 고성장 시장을 향하고 있으나 성숙도와 수익화 시점이 다르다. On-Device sLM(TRL 7~8)과 클라우드 Speaker Diarization(TRL 7~8)은 상용 적용 가능 단계이며, Edge AI/MEC(TRL 6~8)와 5G SA AI-RAN(TRL 5~6)은 2026~2027년 필드 트라이얼·상용화 진입 단계다. 시장 규모는 Edge AI $25~47B(2026), On-Device AI $10~33B(2026), AI-RAN $3.8B(2026) 수준이며 모두 20~37% CAGR로 성장 중(단, 리서치사별 편차 커서 [C] 등급). SKT는 삼성과 AI-RAN MOU(2025-11), A.X K1(5천억 파라미터 MoE, 2025-12) 발표로 풀스택 AI 인프라를 선점하고 있으며, KT는 삼성과 상용망 AI-RAN 검증(2025-12), NVIDIA와 글로벌 허브 구축 MOU, Agentic AICC(MWC 2026) 공개로 B2B AI 수익화 경로를 확보 중이다. 통신사 수익 모델은 내부 OPEX 절감(AI로 20~30%)에서 GPU-as-a-Service·에지 AI API·에이전틱 AICC로 외부 수익화로 전환하는 구조적 변화가 2026년부터 가시화되고 있다. NVIDIA 2026 텔코 서베이에서 통신사 90%가 AI 긍정적 ROI를 보고했고, 89%가 AI 지출 확대 계획이다.

---

## 연구 질문

WTIS 선정검증에 필요한 7가지 추가 데이터:
1. Edge AI / On-Device AI / AI-RAN TAM/SAM/SOM 수치(연도별, 출처별 교차)
2. SKT·KT의 구체적 서비스·투자 현황
3. 실시간 화자분할(2인) 기술 현황 — W12 미수록 L3
4. 특허 현황 — 주요 출원인 동향
5. 표준화 진행 상태(3GPP Rel-18/19/20, O-RAN WG2)
6. 통신사 관점 수익 모델 및 CAPEX/OPEX 영향
7. 각 L3별 TRL 수준 근거

---

## 1. 시장 분석

### TAM/SAM/SOM

**Edge AI 시장 규모**

| 연도 | 규모 (USD) | 출처 | 신뢰도 |
|------|-----------|------|--------|
| 2025 | $11.8B ~ $25.7B | BCC Research / Precedence Research | [C] |
| 2026 | $29.0B ~ $47.6B | Business Research Company / Precedence Research | [C] |
| 2030 | $57B ~ $103B | BCC Research / Business Research Company | [C] |
| 2033~34 | $118B ~ $143B | Grand View Research / Precedence Research | [C] |
| CAGR | 21% ~ 37% (출처별 상이) | 복수 리서치사 | [C] |

**On-Device AI 시장 규모**

| 연도 | 규모 (USD) | 출처 | 신뢰도 |
|------|-----------|------|--------|
| 2024 | $5.1B ~ $15.2B | Verified Market Reports / Reports and Data | [C] |
| 2025 | $10.6B ~ $10.8B | Data Insights Market / Grand View Research | [C] |
| 2026 | ~$33.2B (상단 추정) | Coherent Market Insights | [C] |
| 2033 | $30.9B ~ $156.6B (편차 큼) | 복수 리서치사 | [C] |
| CAGR | 15% ~ 28% | 복수 리서치사 | [C] |

**AI-RAN 시장 규모**

| 연도 | 규모 (USD) | 출처 | 신뢰도 |
|------|-----------|------|--------|
| 2026 | $3.81B | Precedence Research | [C] |
| 2035 | $37.19B | Precedence Research | [C] |
| CAGR | 28.79% (2026~2035) | Precedence Research | [C] |

**AI in Telecom 광의 시장**

| 연도 | 규모 (USD) | 출처 | 신뢰도 |
|------|-----------|------|--------|
| 2025 | $2.66B ~ $4.45B | Precedence / SkyQuest | [C] |
| 2026 | $6.73B | Fortune Business Insights | [C] |
| 2025 B2B AI 수익 | $4B → 65% CAGR → 2030 성장 | GSMA Intelligence (단일 소스) | [D] |

> 주의: 시장 규모 수치는 리서치 기관별 정의 범위와 방법론이 상이하여 직접 비교 불가. 모든 수치는 [C] 이하 등급이며 방향성 참고용으로 활용. 시장 규모 주장에 대한 2건 이상 독립 교차검증은 아래와 같이 수행됨:
> - Edge AI: Precedence($143B by 2034) vs. Grand View Research($119B by 2033) — 방향성 일치, 구체적 수치는 편차 존재. [[G-01]](#ref-g-01), [[G-02]](#ref-g-02)
> - AI-RAN: Precedence($37.2B by 2035) — 단일 소스. 비교 가능 수치 없음. [[G-03]](#ref-g-03)

### 성장률 및 전망

- Edge AI가 클라우드 AI(전체 20% CAGR) 대비 높은 성장세의 핵심 동인: 레이턴시(온디바이스 <20ms vs. 클라우드 200~500ms), 프라이버시 규제(EU AI Act), 데이터 주권 이슈 [[G-04]](#ref-g-04)
- 2026년 AI 추론 시장 핵심 화두: "클라우드 규모화"에서 "에지 추론"으로 이동하는 구조적 전환 [[G-05]](#ref-g-05)
- NVIDIA 2026 텔코 AI 서베이: 통신사 90%가 AI ROI 긍정적, 89%가 2026년 AI 지출 확대 계획. 자율 네트워크(AI-RAN 포함) ROI 1위(50%) [[E-01]](#ref-e-01)
- 온프레미스·엣지 배포가 27.25% CAGR로 클라우드 LLM(전체 20.08% CAGR) 성장률 상회 [[G-06]](#ref-g-06)

---

## 2. 기술 현황 (L3별)

### L3 기술 성숙도 매트릭스

| L3 기술 | TRL | 단계 | 핵심 제약 |
|---------|-----|------|-----------|
| On-Device sLM | 7~8 | 상용 배포 초기 | 프레임워크 파편화(6종+), 통신사 도메인 특화 미성숙 |
| 실시간 화자분할(2인) | 5~6 (온디바이스) / 7~8 (클라우드) | 클라우드 상용, 온디바이스 초기 | 온디바이스 메모리/배터리, 소음 환경 DER |
| Edge AI / MEC | 6~8 | 필드 트라이얼 ~ 상용 초기 | 통신사 MEC 킬러앱 미성숙, 수익화 지연 |
| 5G SA / AI-RAN | 5~6 | OTA 검증 ~ 필드 트라이얼 | GPU 전력·비용, 표준화 2027+ |

### On-Device sLM

> W12 심층 리서치(2026-03-16_research-ondevice-slm.md) 상세 참조.

**TRL 7~8 근거**:
- Apple Intelligence, Samsung Galaxy AI 등 상용 단말 탑재 완료 (TRL 9 수준 일반 sLM)
- 통신사 특화(네트워크 최적화·고객 응대) 도메인 적용은 TRL 5~6 수준
- ExecuTorch 1.0 GA(Meta), Cactus v1, llama.cpp 등 배포 프레임워크 안정화

**통신사 전용 sLM 사례**: NetoAI TSLAM-1.5B — 텔레콤 특화 오픈소스 1.5B sLM, 네트워크 자동화·운영 지원 목적으로 출시 [[G-07]](#ref-g-07)

**성능 기준점**:
- iPhone 17 / Galaxy S25 Ultra: 70+ tok/sec (Qwen3-600M INT8, Cactus v1)
- Qualcomm Snapdragon 8 Elite FastVLM: TTFT 0.12초, decode 100+ tok/sec
- Pixel 8 Pro GGUF Q4_K_M(3B): 11.2 tok/sec, 1.7GB, 콜드스타트 4.2초

### 실시간 화자분할(2인)

**기술 현황**

2인 전화 통화 화자분할은 End-to-End Neural Diarization(EEND) 기반으로 2023~2025년 급격히 발전했다. 통신사 콜센터, 회의 녹음, AI 보이스 에이전트 통합이 주요 적용 분야다.

**주요 기술 동향**:
- **NVIDIA Streaming Sortformer**: 실시간 화자분할 API. 미팅·통화·음성 앱에서 즉각적 화자 레이블링. 스트리밍 방식으로 낮은 지연 달성 [[G-08]](#ref-g-08)
- **pyannote 3.1 / community-1 (오픈소스)**: DER ~10%, GPU 기준 실시간 팩터 2.5%(NVIDIA V100 기준). 2025년 community-1 업데이트로 화자 수 산정·배정 정확도 크게 향상 [[G-09]](#ref-g-09)
- **AssemblyAI**: 2025년 새 화자 임베딩 모델로 소음 환경 30% 정확도 향상 [[G-09]](#ref-g-09)
- **pyannoteAI + Argmax**: 온디바이스 전환 프로젝트 진행 중 — pyannoteAI 모델을 로컬(iOS) 실행 가능하도록 포팅 [[G-10]](#ref-g-10)
- **SpeakerKit**: pyannote v3 기반 추론 효율화 시스템, pyannote v3 대비 9.6배 빠른 처리 속도
- **2인 통화 특화 저지연 모델**: 0.32초 지연으로 경쟁력 있는 DER 달성. 전화 통화 특화 스트리밍 아키텍처 [[G-11]](#ref-g-11)

**TRL 평가**:
- 서버/클라우드 실시간 화자분할: TRL 7~8 (AssemblyAI·Deepgram·NVIDIA 상용 API)
- 온디바이스(스마트폰) 실시간 2인 화자분할: TRL 5~6 (기술 검증, 상용급 배포 초기)
- 핵심 제약: 소음 환경 DER 저하, 온디바이스 화자 임베딩 모델 메모리(~200~500MB), 배터리

**학술 최신 동향**:
- SpeakerLM (arXiv 2508.06372, 2025-08): SenseVoice-large + Qwen2.5-7B 기반 E2E 멀티모달 LLM 화자분할·인식 통합. AliMeeting·AISHELL4·AISHELL5 벤치마크 SOTA [[P-01]](#ref-p-01)
- Streaming Sortformer (Interspeech 2025): 화자 캐시 기반 온라인 화자분할, 실시간 처리 개선 [[P-02]](#ref-p-02)
- SDBench (Interspeech 2025): 13개 다양 데이터셋 통합 벤치마크 스위트, 13개 데이터셋 기준 온디바이스/서버 시스템 성능 비교 체계화 [[P-03]](#ref-p-03)

### Edge AI

> W12 심층 리서치에서 일부 언급. 추가 현황:

**TRL 7~8 (일반 추론) / TRL 5~6 (통신사 네트워크 엣지 전용)**

- 일반 엣지 AI (산업용 카메라·로보틱스·디지털 트윈): Qualcomm QCS8550, NVIDIA Jetson Orin 등 상용 하드웨어 위에서 TRL 8~9
- 통신사 MEC 기반 AI 서비스: TRL 6~7 — KT 국내 유일 5G SA 상용망 보유, AI-RAN 기술 상용망 적용 검증(2025-08)
- 텔레콤 엣지 AI 주요 사용 사례: 실시간 네트워크 최적화(AI-for-RAN), 엔터프라이즈 엣지 AI(AIoT·스마트 팩토리), 에이전틱 AICC

### 5G SA/6G AI-RAN

> W12 심층 리서치(2026-03-16_research-5g-6g-ai-ran.md) 상세 참조.

**TRL 5~6 (AI-on-RAN 기준)**:
- AI-for-RAN (네트워크 최적화): TRL 6~7 — Nokia 2026 필드 트라이얼, KT·삼성 상용망 검증 완료
- AI-on-RAN (RAN+AI 컴퓨팅 통합): TRL 5~6 — T-Mobile/Nokia/NVIDIA OTA 검증, 상용 출시 2027 예정
- AI-and-RAN (AI 독립 처리 레이어): TRL 4~5 — 개념 증명 단계
- 6G AI-native RAN: TRL 2~3 — 2029년 표준화 목표

---

## 3. 경쟁사 현황

### SKT

**주요 사업 현황**

| 기업 | 동향 | 출처 |
|------|------|------|
| SKT | A.X K1 출시(2025-12-30): 5,190억 파라미터 MoE, 활성 파라미터 ~330억. 한국어 특화 설계. 42dot(온디바이스 AI), Rebellions(NPU), Krafton(멀티모달), KAIST·서울대로 구성한 '정예팀'으로 풀스택 소버린 AI 구축. | [[E-02]](#ref-e-02) |
| SKT | 에이닷(A.) AI 에이전트: 가입자 1,000만+. 에이닷 비즈(B2B, SK그룹사 25개·8만 명, 2025-09). 에이닷 오토(차량 온디바이스 AI, 르노코리아 Filante 탑재). AI 관련 투자 누적 6,000억 원+, AI R&D 인력 1,200명+. | [[E-03]](#ref-e-03) |
| SKT | AI-RAN: 삼성전자와 MOU(2025-11-26) — AI 기반 채널 추정·분산 MIMO·스케줄러 공동 개발. AI-RAN Alliance 이사회 멤버. NVIDIA와 6G AI-native 플랫폼 공동 선언(MWC 2026-03-01). | [[E-04]](#ref-e-04), [[E-05]](#ref-e-05) |
| SKT | ATHENA 6G 백서(2026-02-23): AI-native RAN 로드맵 공개. AI 데이터센터 국내 1 GW+ 투자 계획. MWC 2026 "AI Native 기업" 선언. | [[E-06]](#ref-e-06) |

### KT

**주요 사업 현황**

| 기업 | 동향 | 출처 |
|------|------|------|
| KT | AI-RAN 상용망 검증(2025-12): 삼성전자와 경기 성남 약 1.8만 명 대상 상용 5G망 AI-RAN 적용 검증 완료. 사용자별 맞춤 네트워크 설정 자동화, 접속 장애 예방 효과 확인. 이전 시뮬레이션 검증(2025-06) 후 실 상용망 최초 적용. | [[E-07]](#ref-e-07) |
| KT | 5G SA 상용망: 국내 통신사 중 유일하게 5G SA 전국 상용망 구축 완료. AI-RAN Alliance 가입(2025-01). | [[G-12]](#ref-g-12) |
| KT | NVIDIA·삼성·SKT·LGU+·ETRI·연세대와 AI-RAN 글로벌 허브 구축 MOU. 한국을 AI-RAN 글로벌 허브로 육성, 국제 표준화·테스트베드 공동 구축 추진. | [[E-08]](#ref-e-08) |
| KT | Agentic AICC (MWC 2026 공개): 다중 AI 에이전트가 고객 상담~해결 전 과정 자동화. KT Agent Connector(플러그인 AI 에이전트 추가). 현재 약 300개사 AICC 고객(금융사 30개사+). 플랫폼 구축 기간 1/3 단축. | [[E-09]](#ref-e-09) |
| KT | Microsoft와 5년 AI·클라우드·IT 2.4조 원 공동 투자. Phi 3.5 기반 공공·금융 특화 sLM 공동 개발 계획. | [[G-13]](#ref-g-13) |

### 글로벌 통신사 (NTT, Verizon, AT&T, DT)

| 기업 | 동향 | 출처 |
|------|------|------|
| Deutsche Telekom | T-Mobile과 6G Innovation Hub 공동 출범(2026-02-28). AI 기반 Smart Call Assistant 세계 최초 공개(MWC 2026). | [[G-14]](#ref-g-14) |
| T-Mobile (US) | Nokia+NVIDIA AI-RAN OTA 검증(GH200 단일 서버), Ericsson Portable AI RAN 동시 파일럿. 멀티벤더 AI-RAN 전략. | 선행 보고서 참조 |
| SoftBank | SRv6 MUP 5G 상용 서비스 세계 최초(2025-12). 4G망 확대 적용 중. | 선행 보고서 참조 |

### 장비사 (Nokia, Ericsson, Samsung)

| 기업 | 동향 | 출처 |
|------|------|------|
| Nokia | NVIDIA로부터 $1B 투자 유치. Doksuri RRH 출시(전력 -30%, 무게 -25%). 2026 필드 트라이얼·2027 상용 AI-RAN 릴리즈 확정. GPU-first 전략. | 선행 보고서 참조 |
| Ericsson | 자사 ASIC Silicon(신경망 가속기 내장)으로 NVIDIA 독립 AI-RAN 구현. Cloud RAN NVIDIA 플랫폼 이식성 동시 시연. | 선행 보고서 참조 |
| Samsung | SKT와 AI-RAN MOU(AI 채널 추정·분산 MIMO·스케줄러 공동 개발). KT와 상용망 AI-RAN 검증 완료. AI-RAN Alliance 공동 Work Item 제안(AI 기반 채널 추정). | [[E-04]](#ref-e-04), [[E-07]](#ref-e-07) |

### 칩셋 (Qualcomm, MediaTek, Apple, Samsung)

| 기업 | 동향 | 출처 |
|------|------|------|
| Qualcomm | Snapdragon X2 Plus(80 TOPS NPU, CES 2026). Snapdragon Wear Elite(웨어러블 첫 Hexagon NPU, MWC 2026). FastVLM decode 100+ tok/sec. 2024 USPTO 특허 취득 3,749건(3위). | [[G-15]](#ref-g-15) |
| Samsung | Exynos 2600(2nm 세계 최초, AI 성능 +113%). 2025년 미국 특허 7,054건(+11% YoY). AI 특허 출판 건수 500대 기업 중 1위(9,982건). | [[G-16]](#ref-g-16) |
| Apple | Core ML + MLX로 Llama-3.1-8B M1 Max 33 tok/sec. Apple Intelligence 온디바이스 집중. 2025년 미국 특허 2,722건(-12% YoY, 순위 하락). | [[G-16]](#ref-g-16) |

---

## 4. 특허 현황

**2024~2025 USPTO AI 특허 주요 동향**

| 기업/분야 | 동향 | 출처 |
|-----------|------|------|
| Samsung (전체) | AI 특허 출판 건수 500대 기업 1위(9,982건, 2023-01~2024-10). 2025년 미국 특허 7,054건(+11% YoY). 반도체·NPU·온디바이스 AI 집중. | [[G-16]](#ref-g-16) |
| Qualcomm | 2024 USPTO 취득 3,749건(3위). 5G 특허 44,657건 부문 상위 출원인. NPU 아키텍처·엣지 추론 가속 특허 강화. | [[G-15]](#ref-g-15) |
| Apple | 2025년 미국 특허 2,722건(-12% YoY, 순위 하락). LLM 관련 출원 비율 낮음, 온디바이스 AI 일반 특허 집중. | [[G-16]](#ref-g-16) |
| Nokia/Ericsson | AI 기반 빔포밍·채널 추정·자율 RAN 최적화 영역 출원 활발. 구체적 건수는 DB 직접 조회 필요. | [C] |

**Edge AI 특허 트렌드 (2025)**
- 추론 최적화(양자화·프루닝·지식 증류), NPU 아키텍처, 온디바이스 멀티모달 처리 영역 집중 출원 [[G-17]](#ref-g-17)
- 삼성-SKT AI-RAN MOU의 핵심 기술인 'AI 기반 채널 추정'이 AI-RAN Alliance 공식 Work Item으로 채택됨 → 향후 표준 특허(SEP) 포지셔닝 가능 [[E-04]](#ref-e-04)

> 데이터 공백: Nokia·Ericsson·Qualcomm의 Edge AI 추론 특허 구체적 건수·청구항은 USPTO/KIPRIS 직접 DB 조회 필요. 국내(KIPRIS) SKT·KT 출원 현황 미수집.

---

## 5. 표준화 동향

### 3GPP AI/ML RAN 표준화 로드맵

| 릴리즈 | 주요 내용 | 상태 | 완료 시점 |
|--------|----------|------|----------|
| Rel-18 | AI/ML 데이터 수집 강화, 신호 지원 규범화. CSI 피드백·빔 관리·포지셔닝 AI/ML 적용 스터디 완료 | **완료** | 2023 Q4 |
| Rel-19 | 에너지 절감·부하 분산·이동성 최적화 AI/ML 규범화. 추가 유스케이스 확장 | 진행 중 (2024 Q2 시작) | 2025~2026 |
| Rel-20 | Two-sided AI 모델(디바이스+네트워크 동시 AI) Work Item 채택 | 예정 | 2027 H2 |
| 6G | AI-native RAN 규격. 첫 라디오 스터디 2026-06 완료 목표 | 초기 | 2029 |

[[G-18]](#ref-g-18), [[G-19]](#ref-g-19)

### O-RAN Alliance AI/ML 표준화

- **WG2 (Non-RT RIC, A1 인터페이스)**: AI/ML 모델 배포·등록·발견·훈련 API 규격 지속 업데이트. Bootstrap API, RAN OAM CM/FM API, AI/ML 모델 배포·검색·훈련 API 신규 추가 [[G-20]](#ref-g-20)
- **2025년 3월 이후 기술 문서 60건 신규/갱신**, 전체 134건 현행 버전(총 830건 아카이브) [[G-20]](#ref-g-20)
- **3GPP-O-RAN 6G 공동 조정**: 2025-03 ETSI 공동 워크숍. O-RAN 개방형 지능 RAN 솔루션과 3GPP 6G 생태계 간 일관성 확보 추진 [[G-19]](#ref-g-19)
- **표준화 시사점**: AI-RAN이 3GPP Rel-19/20 및 O-RAN 표준에 채택되기 전까지 상용 배포는 벤더 독자 구현에 의존. SKT의 ATHENA 백서 및 AI-RAN Alliance 기여가 표준화 선점에 직결됨 [[G-12]](#ref-g-12)

---

## 6. 통신사 관점 사업 모델

### 수익 모델 레이어 구조

**레이어 1: 내부 OPEX 절감 (현재 ~ 2026)**
- AI 기반 네트워크 자동화: MTTR 30~50% 감소, OPEX 20~25% 절감, 콜센터 문의 40% 감소 [[G-21]](#ref-g-21)
- AI-RAN 에너지 효율화: 기지국 AI 전력 관리로 운영 비용 절감 (KT-삼성 상용망 검증 완료)
- NVIDIA 서베이: 텔코 90%가 AI 긍정적 ROI, 자율 네트워크(AI-RAN 포함) ROI 1위(50%) [[E-01]](#ref-e-01)

**레이어 2: 외부 B2B AI 서비스 수익화 (2025~2027)**
- **Agentic AICC**: KT 에이전틱 AICC(MWC 2026). SKT 에이닷 비즈(B2B, 그룹사 25개사). 통신사가 AICC 플랫폼을 B2B SaaS로 제공. KT 약 300개 기업 고객 [[E-09]](#ref-e-09)
- **GPU-as-a-Service**: 텔코 엣지 데이터센터 GPU 컴퓨팅 자원을 기업·정부에 임대. 데이터 주권·저지연 강점. 단, 배치 처리 대비 비용 최대 50배 높아 경제성 확보 과제 [[G-22]](#ref-g-22)
- **네트워크 슬라이싱 + Edge AI API**: 5G SA 기반 슬라이싱으로 AI 워크로드 전용 레인 제공 → API 수익화. KT 5G SA 전국망이 경쟁 우위

**레이어 3: AI-native 인프라 서비스 (2027~)**
- **AI-RAN 컴퓨팅 통합**: 기지국을 AI 추론 플랫폼으로 활용. RAN+AI on-RAN에서 AI 워크로드(자막·번역·영상 AI) 동시 처리
- **Edge AI 플랫폼**: 통신사 MEC 위에서 sLM 추론·온디바이스 AI 오케스트레이션 서비스 제공
- **데이터 파이프라인 수익화**: 네트워크 트래픽·위치 패턴 데이터를 AI 학습에 활용하는 데이터 비즈니스

### CAPEX/OPEX 영향 분석

| 항목 | 영향 | 출처 |
|------|------|------|
| 글로벌 통신사 CAPEX 강도 | 2024년 15.9%(2022~23년 17~18%에서 하락). 2025년 추가 감소 예상. AI로 효율 향상 추진. | [B] |
| AI-RAN 도입 CAPEX | GPU 인프라(Grace Hopper GH200 등) 추가 투자 필요. 하드웨어 비용 vs. OPEX 절감 5~7년 상각 시 TCO 우위 가능. | [C] |
| 엔터프라이즈 에지 AI CAPEX | 중소형 제조 시설 기준 $200K~$500K 초기 투자. 3~5년 상각 시 클라우드 대비 TCO 우위 가능 [[G-23]](#ref-g-23) | [C] |
| AI OPEX 절감 효과 | MTTR 30~50%, OPEX 20~25%, 콜센터 40% 감소 [[G-21]](#ref-g-21) | [B] |
| B2B AI 수익 성장 | 2025년 $4B → 65% CAGR → 2030년 잠재 (GSMA Intelligence, 단일 소스 [D]) [[G-06]](#ref-g-06) | [D] |

---

## 7. 기업 발언 & 보도자료

**E-01 NVIDIA — State of AI in Telecom 2026 Survey (2026-02)**
> "89%의 텔코가 2026년 AI 지출을 확대할 계획이며, 90%가 AI가 수익과 비용에 긍정적 영향을 미쳤다고 응답했다. 자율 네트워크가 ROI 1위(50%) 사용 사례다. 77%가 AI-native 무선 네트워크 아키텍처의 배포가 기존 6G 사이클보다 훨씬 빨라질 것으로 예상한다."
[[E-01]](#ref-e-01)

**E-02 SKT 뉴스룸 — A.X K1 공개 발표 (2025-12-28)**
> "SKT 정예팀은 AI 반도체, AI 데이터센터, AI 모델, AI 서비스에 이르는 전체 밸류체인을 독자 기술로 구축한 '풀스택 소버린 AI'를 완성했다. A.X K1은 총 5,190억 개의 매개변수로 구성되며, 추론 시 약 330억 개의 매개변수가 활성화되는 MoE 구조다."
[[E-02]](#ref-e-02)

**E-04 Samsung 뉴스룸 — SKT-삼성 AI-RAN MOU (2025-11-26)**
> "Samsung Research는 AI 기반 채널 추정, 스케줄러, 분산 MIMO 기술을 개발하고, SKT는 전국 상용망 기반 데이터 제공 및 테스트 인프라를 담당한다. 양사는 AI-RAN Alliance에서 공동으로 AI 기반 채널 추정 기술을 Work Item으로 제안해 공식 채택됐다."
[[E-04]](#ref-e-04)

**E-07 Samsung 뉴스룸 — KT-삼성 AI-RAN 상용망 검증 (2025-12)**
> "AI-RAN 최적화 기술은 사용자의 이동 경로와 사용 패턴에 따른 문제를 AI가 학습해 반복 발생 트렌드를 파악, 잠재적 문제를 사전에 예방한다. 성남 약 1.8만 명 대상 필드 테스트에서 가장 큰 영향을 받은 사용자들의 접속 실패율이 크게 감소했다."
[[E-07]](#ref-e-07)

**E-09 Asia Business Daily — KT Agentic AICC (MWC 2026, 2026-02-27)**
> "에이전틱 AICC는 기존 챗봇·보이스봇 중심에서 벗어나 상담 기록을 바탕으로 실제 업무를 처리하는 자율 솔루션이다. KT Agent Connector가 핵심으로, 다양한 AI 에이전트를 기존 AICC 플랫폼에 플러그인 방식으로 추가할 수 있다."
[[E-09]](#ref-e-09)

---

## 8. 전략적 시사점

**기술 트렌드**

- 클라우드-엣지-단말 3계층 AI 추론 아키텍처가 2026년을 기점으로 통합 인프라로 수렴 중이다. 통신사는 이 구조에서 '엣지 레이어 오퍼레이터' 역할이 부상하고 있다.
- AI-RAN은 6G의 선행 연구 단계를 넘어 2027년 상용화를 향한 실행 단계에 진입했다 (Nokia CTO 타임라인 공식화).
- On-Device sLM 오픈소스 생태계 성숙으로 통신사 앱/서비스에 즉시 내장 가능한 환경이 도래했다.
- Speaker Diarization은 클라우드 기준 TRL 7~8의 성숙 기술로, 통신사 핵심 사업(콜센터·음성 서비스)에 즉시 적용 가능하다.

**기회**

- **AI-RAN으로 인프라 수익 이중화**: RAN 하드웨어를 AI 컴퓨팅 플랫폼으로 재정의하면 기지국 TCO 절감과 에지 AI PaaS 매출을 동시에 달성할 수 있다. Nokia/NVIDIA 생태계 참여가 최단 경로.
- **온디바이스 sLM + 통신 API 결합 서비스**: 디바이스 내 sLM + 통신사 인증/컨텍스트 API의 결합으로 클라우드 LLM 대비 프라이버시·레이턴시 우위를 가진 특화 서비스 가능. KT Agentic AICC·SKT 에이닷 비즈가 선행 사례.
- **Speaker Diarization 즉시 적용 기회**: AI AICC(상담 자동화), 회의 분석, 음성 컴플라이언스 — 국내 금융·의료 규제 환경에서 온프레미스 Speaker Diarization 패키지 수요 고성장 전망.
- **국내 정책 후광 효과**: 과기정통부 2026 AI·ICT R&D 1조 2,040억 원, 온디바이스 AI·차세대 NPU 우선 지원 확정. 국내 통신사-장비사 컨소시엄 정부 과제 수주 기회.

**위협**

- **NVIDIA 생태계 집중화**: Intel의 AI-RAN Alliance 불참 지속 시 NVIDIA 의존 심화 → 가격 협상력 약화, 공급망 리스크 누적.
- **SKT 선점 효과**: SKT가 AI Pyramid Strategy·AI-RAN Alliance 이사회·ATHENA 6G 백서로 국내 표준 레퍼런스 선점 중. 후발 진입 시 생태계 접근 비용 상승.
- **5G SA 수익화 지연**: Opensignal 보고서 "Architecture Deployed, Monetisation Pending" — AI-RAN 투자 ROI 회수까지 수년 필요.
- **플랫폼 OS 잠금**: Android Intelligent OS(2026-02), Apple Intelligence의 OS 레벨 에이전트 통합 강화 → 통신사 독립 온디바이스 AI 앱이 OS 벤더 모델과 직접 경쟁 구도 심화.
- **GPU-as-a-Service 경제성**: 저지연 컴퓨팅 비용-per-token이 배치 처리 대비 최대 50배 높아 수익 모델 성립이 어려움 [[G-22]](#ref-g-22).

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- SKT A.X K1 출시(5,190억 파라미터 MoE) — 공식 뉴스룸 발표 [A]
- KT-삼성 AI-RAN 상용망 검증(성남, 1.8만 명) — Samsung 공식 뉴스룸 [A]
- SKT-삼성 AI-RAN MOU(2025-11-26) — 양사 공식 뉴스룸 [A]
- KT 국내 유일 5G SA 전국 상용망 구축 — 복수 보도 [B]
- NVIDIA 2026 텔코 AI 서베이(90% 긍정적 ROI, 89% AI 지출 확대) — NVIDIA 공식 [A]
- 3GPP Rel-18 완료, Rel-19 진행 중, Rel-20 Two-sided AI 채택 — 3GPP 공식 [A]
- O-RAN WG2 AI/ML API 규격 60건 신규 출판(2025) — O-RAN Alliance 공식 [A]
- KT Agentic AICC(MWC 2026, ~300개사 고객) — 복수 보도 [B]
- pyannote 3.1 DER ~10%, 실시간 팩터 2.5% — 공식 기술 문서 [A]

**추가 검증 필요 [C/D]:**
- 시장 규모 수치 전체 (Edge AI $25~143B 편차, 기관별 정의 불일치) [C]
- 통신사 B2B AI 수익 65% CAGR (GSMA Intelligence, 단일 소스) [D]
- GPU-as-a-Service "50배 비용" 주장 (단일 분석) [C]
- 엔터프라이즈 에지 AI CAPEX $200K~$500K (단일 분석) [C]

**데이터 공백:**
- KT의 Edge AI / sLM 서비스 독자 투자 규모 (공개 수치 없음)
- SKT·KT의 실제 MEC 트래픽·수익 데이터
- 화자분할 온디바이스 배포 시 DER 성능 실측 데이터 (벤치마크 부재)
- Nokia·Ericsson·Qualcomm의 Edge AI 추론 특허 구체적 건수·청구항 (DB 조회 필요)
- 국내(KIPRIS) 통신사 AI 특허 출원 현황 미수집

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-e-01"></a>E-01 | NVIDIA — Survey Reveals AI Advances in Telecom: 90% Positive ROI (State of AI in Telecom 2026) | [링크](https://blogs.nvidia.com/blog/ai-in-telco-survey-2026/) | 보도자료 | 2026-02 | [A] |
| <a id="ref-e-02"></a>E-02 | SKT 뉴스룸 — SKT, 5천억 파라미터로 5천만 국민 '모두의 AI' 실현 나섰다 (A.X K1) | [링크](https://news.sktelecom.com/217811) | 보도자료 | 2025-12-28 | [A] |
| <a id="ref-e-03"></a>E-03 | SKT 뉴스룸 — SKT, SK그룹 전반에 '에이닷 비즈' 확대 도입 | [링크](https://news.sktelecom.com/215522) | 보도자료 | 2025-09 | [A] |
| <a id="ref-e-04"></a>E-04 | Samsung Global Newsroom — Samsung and SK Telecom Join Forces To Lead 6G Era With AI-RAN Technology | [링크](https://news.samsung.com/global/samsung-and-sk-telecom-join-forces-to-lead-6g-era-with-ai-ran-technology) | 보도자료 | 2025-11-26 | [A] |
| <a id="ref-e-05"></a>E-05 | NVIDIA Newsroom — NVIDIA and Global Telecom Leaders Commit to Build 6G on Open AI-Native Platforms | [링크](https://nvidianews.nvidia.com/news/nvidia-and-global-telecom-leaders-commit-to-build-6g-on-open-and-secure-ai-native-platforms) | 보도자료 | 2026-03-01 | [A] |
| <a id="ref-e-06"></a>E-06 | SKT 뉴스룸 (영문) — SK Telecom Publishes Third 6G White Paper 'ATHENA' | [링크](https://news.sktelecom.com/en/2751) | 보도자료 | 2026-02-23 | [A] |
| <a id="ref-e-07"></a>E-07 | Samsung Global Newsroom — Samsung Electronics and KT Corporation Successfully Validate AI-RAN on Commercial Networks | [링크](https://news.samsung.com/global/samsung-electronics-and-kt-corporation-successfully-validate-ai-ran-on-commercial-networks-accelerating-6g-development) | 보도자료 | 2025-12 | [A] |
| <a id="ref-e-08"></a>E-08 | 한국NGO신문 — KT, NVIDIA와 AI-RAN 글로벌 허브 구축 협력 | [링크](https://www.ngonews.kr/news/articleView.html?idxno=217442) | news | 2025-11 | [B] |
| <a id="ref-e-09"></a>E-09 | The Asia Business Daily — "From Consultation to Resolution with AI": KT Unveils Agentic AICC at MWC | [링크](https://www.asiae.co.kr/en/article/2026022709140663398) | 보도자료 | 2026-02-27 | [A] |
| <a id="ref-e-10"></a>E-10 | Nokia Newsroom — Nokia expands network portfolio for premium performance in the AI-RAN era #MWC26 | [링크](https://www.nokia.com/newsroom/nokia-expands-network-portfolio-for-premium-performance-in-the-ai-ran-era-mwc26/) | 보도자료 | 2026-03-01 | [A] |
| <a id="ref-g-01"></a>G-01 | Grand View Research — Edge AI Market Size, Share & Trends (USD 118.69B by 2033) | [링크](https://www.grandviewresearch.com/industry-analysis/edge-ai-market-report) | report | 2026 | [C] |
| <a id="ref-g-02"></a>G-02 | Precedence Research — Edge AI Market Size to Attain USD 143.06 Billion by 2034 | [링크](https://www.precedenceresearch.com/edge-ai-market) | report | 2026 | [C] |
| <a id="ref-g-03"></a>G-03 | Precedence Research — AI-RAN Market Size to Hit USD 37.19 Billion by 2035 | [링크](https://www.precedenceresearch.com/ai-ran-market) | report | 2026 | [C] |
| <a id="ref-g-04"></a>G-04 | TechCrates — Edge AI vs Cloud AI 2026: Which Wins for Business Efficiency? | [링크](https://www.techcrates.com/edge-ai-vs-cloud-ai-2026-which-wins-for-business-efficiency/) | blog | 2026 | [C] |
| <a id="ref-g-05"></a>G-05 | RD World Online — 2026 AI story: Inference at the edge, not just scale in the cloud | [링크](https://www.rdworldonline.com/2026-ai-story-inference-at-the-edge-not-just-scale-in-the-cloud/) | news | 2026 | [B] |
| <a id="ref-g-06"></a>G-06 | TelecomLead — Telecom Operators Accelerate AI Monetisation with New Revenue Models (GSMA Intelligence) | [링크](https://telecomlead.com/telecom-services/telecom-operators-accelerate-ai-monetisation-with-new-revenue-models-says-gsma-intelligence-124916) | report | 2026 | [C] |
| <a id="ref-g-07"></a>G-07 | isStories — NetoAI TSLAM-1.5B: Telecom Specific Small Language Model for Mobile and Edge | [링크](https://www.isstories.com/2025/03/04/netoai-launched-tslam-1-5b-telecom-specific-small-language-model-for-mobile-and-edge/) | news | 2025-03-04 | [B] |
| <a id="ref-g-08"></a>G-08 | NVIDIA Technical Blog — Identify Speakers with Streaming Sortformer in Real-Time | [링크](https://developer.nvidia.com/blog/identify-speakers-in-meetings-calls-and-voice-apps-in-real-time-with-nvidia-streaming-sortformer/) | blog | 2025 | [B] |
| <a id="ref-g-09"></a>G-09 | AssemblyAI — Top 8 Speaker Diarization Libraries and APIs in 2026 | [링크](https://www.assemblyai.com/blog/top-speaker-diarization-libraries-and-apis) | blog | 2026 | [B] |
| <a id="ref-g-10"></a>G-10 | Argmax — pyannoteAI on Argmax SDK (On-Device Diarization) | [링크](https://www.argmaxinc.com/blog/pyannote-argmax) | blog | 2025 | [B] |
| <a id="ref-g-11"></a>G-11 | inference.plus — Near-Real-Time Speaker Diarization on CoreML (0.32s latency) | [링크](https://inference.plus/p/low-latency-speaker-diarization-on) | blog | 2025 | [C] |
| <a id="ref-g-12"></a>G-12 | 경제미디어일보 — 통신망이 곧 컴퓨터다…엔비디아 손잡은 SKT, 효율 택한 KT·LGU+와 '다른 길' | [링크](https://www.economidaily.com/view/20260227172207712) | news | 2026-02-27 | [B] |
| <a id="ref-g-13"></a>G-13 | CEOSCOREDAILY — [2025 전망] AI 컴퍼니 전환 완료…SKT·KT·LGU+, '돈 버는 AI' 출격 | [링크](https://ceoscoredaily.com/page/view/2024112913043906447) | news | 2024-11-29 | [B] |
| <a id="ref-g-14"></a>G-14 | TelecomTV — MWC26: DT, T-Mobile US unite for 6G R&D | [링크](https://www.telecomtv.com/content/6g/mwc26-dt-t-mobile-us-unite-for-6g-r-d-54958/) | news | 2026-03-02 | [B] |
| <a id="ref-g-15"></a>G-15 | Qualcomm — Snapdragon Wear Elite Press Release (MWC 2026) | [링크](https://www.qualcomm.com/news/releases/2026/03/qualcomm-powers-the-rise-of-personal-ai-with-new-snapdragon-wear) | 보도자료 | 2026-03 | [A] |
| <a id="ref-g-16"></a>G-16 | IAM Media — Samsung, TSMC, Qualcomm are 2024's top US patentees | [링크](https://www.iam-media.com/article/samsung-tsmc-qualcomm-are-2024s-top-us-patentees) | news | 2025 | [B] |
| <a id="ref-g-17"></a>G-17 | Patsnap — Edge Computing Patent Trends 2025: Prior Art Search Guide | [링크](https://www.patsnap.com/resources/blog/articles/edge-computing-patent-trends-2025-prior-art-search/) | blog | 2025 | [C] |
| <a id="ref-g-18"></a>G-18 | 3GPP — AI/ML for NG-RAN & 5G-Advanced towards 6G (Rel-18/19/20 로드맵) | [링크](https://www.3gpp.org/technologies/ai-ml-ngran) | 표준 | 2026-03 | [A] |
| <a id="ref-g-19"></a>G-19 | 3GPP — 3GPP & O-RAN ALLIANCE Joint Workshop on 6G Coordination (ETSI, 2025-03) | [링크](https://www.3gpp.org/news-events/3gpp-news/oran-3gpp-ws) | 표준 | 2025-03 | [A] |
| <a id="ref-g-20"></a>G-20 | O-RAN Alliance — 60 New or Updated O-RAN Technical Documents Released since March 2025 | [링크](https://www.o-ran.org/blog/60-new-or-updated-o-ran-technical-documents-released-since-march-2025) | 표준 | 2025 | [A] |
| <a id="ref-g-21"></a>G-21 | nybsys — Generative AI in Telecom: Cutting OPEX, Boosting ARPU, and Powering Zero-Touch 5G | [링크](https://nybsys.com/generative-ai-in-telecom/) | blog | 2025 | [C] |
| <a id="ref-g-22"></a>G-22 | RCR Wireless — Telecom GPU-as-a-Service: Beyond the hype (Analyst Angle) | [링크](https://www.rcrwireless.com/20251030/analyst-angle/telecom-gpu-as-a-service) | news | 2025-10-30 | [B] |
| <a id="ref-g-23"></a>G-23 | TechCrates — Edge AI vs Cloud AI 2026: Enterprise CAPEX $200K~$500K | [링크](https://www.techcrates.com/edge-ai-vs-cloud-ai-2026-which-wins-for-business-efficiency/) | blog | 2026 | [C] |
| <a id="ref-g-24"></a>G-24 | Coherent Market Insights — On-Device AI Market (USD 33.21B in 2026, USD 156.59B by 2033) | [링크](https://www.coherentmarketinsights.com/industry-reports/on-device-ai-market) | report | 2026 | [C] |
| <a id="ref-g-25"></a>G-25 | Grand View Research — On-Device AI Market Size & Share, 2033 (USD 10.8B in 2025 → 75.5B by 2033) | [링크](https://www.grandviewresearch.com/industry-analysis/on-device-ai-market-report) | report | 2026 | [C] |
| <a id="ref-g-26"></a>G-26 | RCR Wireless — Samsung and SK Telecom ink AI-RAN deal (2025-11) | [링크](https://www.rcrwireless.com/20251126/5g/sk-telecom-ai-ran) | news | 2025-11-26 | [B] |
| <a id="ref-g-27"></a>G-27 | Korea Tech Today — Samsung and KT Validate 6G AI-RAN on Live Commercial Network | [링크](https://koreatechtoday.com/samsung-and-kt-validate-6g-ai-ran-on-live-commercial-network/) | news | 2025-12 | [B] |
| <a id="ref-g-28"></a>G-28 | BCC Research — Edge AI Market 2025~2030 ($11.8B → $56.8B, 36.9% CAGR) | [링크](https://www.bccresearch.com/market-research/information-technology/edge-ai-market.html) | report | 2025 | [C] |
| <a id="ref-g-29"></a>G-29 | Fortune Business Insights — AI in Telecommunication Market ($6.73B in 2026) | [링크](https://www.fortunebusinessinsights.com/ai-in-telecommunication-market-109439) | report | 2026 | [C] |
| <a id="ref-g-30"></a>G-30 | Sammyfans — US patents show Samsung innovation outworking Apple (2025) | [링크](https://www.sammyfans.com/2026/01/15/samsung-apple-us-patents-2025/) | news | 2026-01-15 | [B] |
| <a id="ref-p-01"></a>P-01 | Liu et al. — SpeakerLM: End-to-End Versatile Speaker Diarization and Recognition with Multimodal LLMs (arXiv 2508.06372) | [링크](https://arxiv.org/abs/2508.06372) | paper | 2025-08 | [A] |
| <a id="ref-p-02"></a>P-02 | Medennikov et al. — Streaming Sortformer: Speaker Cache-Based Online Speaker Diarization (Interspeech 2025) | [링크](https://www.isca-archive.org/interspeech_2025/medennikov25_interspeech.pdf) | paper | 2025 | [A] |
| <a id="ref-p-03"></a>P-03 | Durmus et al. — SDBench: A Comprehensive Benchmark Suite for Speaker Diarization (Interspeech 2025) | [링크](https://www.isca-archive.org/interspeech_2025/durmus25_interspeech.pdf) | paper | 2025 | [A] |

---

*선정검증(SKILL-1) 입력용 데이터 수집 보고서. 판정(Go/No-Go) 미포함.*
*선행 보고서: [5G/6G AI-RAN W12](../../weekly/2026-03-16_research-5g-6g-ai-ran.md) | [On-Device sLM W12](../../weekly/2026-03-16_research-ondevice-slm.md)*
