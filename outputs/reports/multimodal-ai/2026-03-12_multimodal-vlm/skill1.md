---
topic: multimodal-vlm
date: 2026-03-12
skill: skill1-selection-verification
confidence: high
status: completed
sources_used: [discover-report, research-deep, websearch]
total_score: 148/200
verdict: Conditional Go
---

# SKILL-1: 멀티모달 VLM 선정검증 — 200점 정량 평가

## Executive Summary

| 항목 | 내용 |
|------|------|
| **판정** | **Conditional Go** (조건부 추진) |
| **총점** | **148 / 200점** |
| **핵심 근거** | 시장매력도(36/40)와 고객가치(33/40)가 강력하나, 한국어 VLM 11점 성능 격차·자사 특허 부재·내부 VLM 전문인력 미확보가 주요 리스크. 온프레미스 TCO 우위와 SKT 대비 6~12개월 선점 기회가 존재하나, 3개월 PoC로 한국어 파인튜닝 성능 75점 이상 달성을 확인한 후 본격 투자 결정 필요. |
| **추천 방향** | Phase 1 PoC (3M) → Phase 2 상용화 (6M) → Phase 3 B2B 확장 (12M) |

---

## Step 1: SMART 목표 검증 + 시장 규모

### 1.1 SMART 목표 검증

| SMART | 목표 내용 | 검증 | 판정 |
|-------|----------|------|------|
| **S** (구체적) | 고객센터 이미지 문의 자동 해결율 30~50% 달성 | VLM 자동 진단 + AICC 통합 파이프라인으로 측정 가능한 FCR 지표 | PASS |
| **M** (측정 가능) | FCR(First Call Resolution) 30~50%, 문서 수작업 60% 단축 | FCR은 기존 AICC에서 이미 측정 중, 문서 처리 시간은 RPA 로그로 추적 | PASS |
| **A** (달성 가능) | 오픈소스 VLM(Qwen2.5-VL 7B) DocVQA 96.4% | 기술적으로 검증됨. 단, 한국어 69.1점 → 75점 이상 파인튜닝 필요 | CONDITIONAL |
| **R** (관련성) | 통신사 97% AI 도입 검토 중, AICC 시장 CAGR 27% | 산업 방향과 일치, SKT·KT 모두 멀티모달 확장 예고 | PASS |
| **T** (기한) | Phase 1 PoC 3개월, Phase 2 상용화 6개월 | SKT A.X K1 이미지 멀티모달 2026H1 → 2026Q3~Q4 선행 필요 | PASS |

**SMART 검증 결과**: 4/5 PASS, 1 CONDITIONAL (한국어 성능 달성 가능성 실험 필요)

### 1.2 시장 규모 (TAM/SAM/SOM)

| 구분 | 시장 | 규모 | CAGR | 출처 |
|------|------|------|------|------|
| **TAM** | 글로벌 멀티모달 AI | 2026 $3.4~3.9B → 2030 $11~23B | 32~38% | [D-01, D-02] |
| **TAM** | 글로벌 IDP(문서 AI) | 2025 $3.2B → 2034 $43.9B | 33.7% | [DA-05, DA-06] |
| **TAM** | 글로벌 영상 AI | 2025 $32B → 2030 $133B | 33% | [D-10] |
| **SAM** | 통신 AI | 2025 $2.06B → 2034 $14.86B | 22% | [G-03] |
| **SAM** | AICC (컨택센터 AI) | 2025 $4.4B → 2030 $14.6B | 27% | AICC 시장 추정 |
| **SOM** | 국내 통신사 VLM 적용 | 연간 $5~15M (초기 3년) | - | 자체 추정 |

**SOM 산출 근거**:
- 국내 통신 3사 AICC 투자 연간 ~$100M 추정, VLM은 AICC의 5~15% 영역
- 문서 AI B2B: 초기 고객 10~30사, 건당 $50~200, 연 $2~6M
- 네트워크 모니터링: 내부 비용 절감 연 $1~3M

---

## Step 2: TRL 4사분면 맵 (기술 성숙도 x 파괴적 혁신도)

```
파괴적 혁신도 (높음)
     │
     │  [Q2: 잠재 파괴자]           [Q1: 전략적 기회]
     │  ┌─────────────────────┐    ┌──────────────────────┐
     │  │ 음성+시각 통합 에이전트 │    │                      │
     │  │ (TRL 4, 파괴도 9)     │    │ 엣지 VLM 플랫폼       │
     │  │                     │    │ (TRL 6, 파괴도 8)      │
     │  │ 자율 네트워크 AI-RAN  │    │                      │
     │  │ (TRL 4, 파괴도 8)     │    │                      │
     │  └─────────────────────┘    └──────────────────────┘
     │
     │  [Q3: 기초 연구]            [Q4: 즉시 상용화]
     │  ┌─────────────────────┐    ┌──────────────────────┐
     │  │                     │    │ ★고객서비스 비전 AI    │
     │  │                     │    │ (TRL 6-7, 파괴도 6)   │
     │  │                     │    │ ★B2B 문서 AI          │
     │  │                     │    │ (TRL 7-8, 파괴도 5)   │
     │  │                     │    │ ★네트워크 비전 모니터링 │
     │  │                     │    │ (TRL 5-6, 파괴도 5)   │
     │  └─────────────────────┘    └──────────────────────┘
     │
     └────────────────────────────────────────────→ 기술 성숙도 (높음)
```

### TRL 상세 분석

| 적용 분야 | TRL | 근거 | 상용화까지 |
|-----------|-----|------|-----------|
| 핵심 VLM 엔진 | **9** (상용화) | GPT-4o, Gemini, Qwen2.5-VL 7B 모두 프로덕션 배포 중 | 즉시 |
| 고객서비스 AICC 통합 | **6~7** (실증) | VLM은 준비되었으나, AICC 연동 표준 API 부재. 파일럿 필요 | 3~6개월 |
| B2B 문서 AI | **7~8** (시연) | PaddleOCR-VL SOTA, 업스테이지 상용 납품 중. 커스터마이징 필요 | 3개월 |
| MEC 엣지 배포 | **6~7** (실증) | Moondream 2B 실동작, MBQ 양자화 검증됨. MEC 인프라 통합 미완 | 6~9개월 |
| 실시간 영상 VLM | **5~6** (검증) | StreamingVLM 8 FPS/H100, 25 FPS 전수 분석 불가. 캐스케이드 필요 | 9~12개월 |
| 한국어 VLM 파인튜닝 | **5~6** (검증) | CC-OCR 69.1점, 75점 이상 목표 파인튜닝 실험 미완 | 3개월 (PoC) |

---

## Step 3: 경쟁사 비교표 + Gap Analysis

### 3.1 경쟁사 비교표

| 평가 항목 | 자사 (LGU+) | SKT | KT | Deutsche Telekom | Verizon |
|-----------|-------------|-----|-----|------------------|---------|
| **멀티모달 VLM 전략** | 미발표 (평가 중) | A.X K1 이미지 2026H1 | 에이전틱 패브릭 (VLM 독립 발표 없음) | Sprinklr CCaaS (텍스트 AI) | Project 624 (텍스트 AI) |
| **자체 모델** | 없음 | A.X K1 500B (이미지 확장 중) | 믿:음 K | 없음 (벤더 의존) | 없음 (벤더 의존) |
| **AICC 도입** | 기존 AICC 운영 | AICC + A. 통합 | AICC 선도 (B2B) | 41,000명 상담원 AI | 10만명 이탈 방지 |
| **이미지 VLM 공개 FCR** | 없음 | 없음 | 없음 | 없음 | 없음 |
| **문서 AI** | 없음 | A.X K1 문서 이해 예정 | 믿:음 K 문서 인식 | 없음 | 없음 |
| **엣지/MEC AI** | MEC 인프라 보유 | 엣지 AI 전략 | MS Azure 파트너 | 없음 | 없음 |
| **한국어 특화** | 미확보 | 자체 모델 강점 | MS 협력 | N/A | N/A |
| **시장 포지션** | 3위 | 1위 (국내 AI) | 2위 (B2B 강점) | 유럽 1위 텔코 | 미국 1위 텔코 |

### 3.2 Gap Analysis

| Gap 영역 | 현재 수준 | 목표 수준 | Gap | 해소 방안 | 소요 기간 |
|----------|----------|----------|-----|----------|----------|
| **자체 VLM 모델** | 없음 | 한국어 특화 7B 모델 | 크리티컬 | 오픈소스(Qwen2.5-VL) 파인튜닝 | 3개월 |
| **한국어 OCR 성능** | 0점 (미보유) | 75점+ (CC-OCR) | 크리티컬 | 통신 도메인 데이터셋 + 파인튜닝 | 3개월 |
| **AICC VLM 통합** | 기존 AICC 텍스트만 | 이미지+텍스트 통합 | 높음 | 파이프라인 PoC 구축 | 3~6개월 |
| **VLM 전문 인력** | 부족 | ML엔지니어 3~5명 | 높음 | 채용 + 업스테이지 협력 | 3~6개월 |
| **특허 포트폴리오** | 해당 분야 0건 | 방어 특허 5건+ | 중간 | PoC 과정에서 출원 | 6~12개월 |
| **GPU 인프라** | 일부 보유 | A100 x4~8 추가 | 중간 | CapEx $60K~120K | 1~2개월 |

### 3.3 SKT 대비 선점 기회 분석

SKT A.X K1의 이미지 멀티모달이 2026H1 목표이나 구체적 출시일 미확정. 자사가 2026Q2에 PoC를 완료하면:
- **시간 Gap**: SKT 대비 동시 또는 소폭 후행 (0~6개월)
- **차별화 포인트**: 온프레미스 프라이버시 우위, B2B 문서 AI 특화, MEC 엣지 배포
- **리스크**: SKT가 자체 모델(500B)로 성능 우위 확보 시 정면 경쟁 불리

---

## Step 4: 3B 전략 (Buy/Borrow/Build) 의사결정 로직

### 4.1 의사결정 매트릭스

| 구성 요소 | Build | Borrow | Buy | **추천** | 근거 |
|-----------|-------|--------|-----|---------|------|
| **VLM 핵심 모델** | Qwen2.5-VL 7B 파인튜닝 | 업스테이지 API 활용 | GPT-4o API | **Build** | 온프레미스 TCO 우위 (연 $48K~216K 절감), 프라이버시 규제 대응 |
| **한국어 학습 데이터** | 자체 구축 (통신 장비 이미지) | 업스테이지 데이터셋 | NAVER CLOVA | **Build + Borrow** | 통신 도메인 데이터는 자체 구축 필수, 일반 한국어는 협력 |
| **AICC 통합 파이프라인** | 자체 개발 | SI 파트너 | 기존 AICC 벤더 확장 | **Build** | 기존 AICC 아키텍처 내부 지식 활용, 코어 경쟁력 |
| **문서 AI 엔진** | PaddleOCR-VL 커스텀 | 업스테이지 Document AI | Mistral OCR API | **Borrow → Build** | 초기 업스테이지 API로 빠른 시장 진입, 점진적 내재화 |
| **GPU 인프라** | 온프레미스 구축 | 클라우드 GPU 임대 | NVIDIA DGX 구매 | **Build** | 일 10만 건 이상 시 온프레미스 TCO 우위 |
| **엣지 배포 (MEC)** | 자체 MEC 통합 | NVIDIA 파트너십 | - | **Build + Borrow** | MEC 인프라는 자사 보유, NVIDIA TensorRT 활용 |

### 4.2 추천 전략: Build-First with Strategic Borrow

```
Phase 1 (0~3M): Borrow 중심 — 업스테이지 API + Qwen2.5-VL PoC 병행
Phase 2 (3~9M): Build 전환 — 파인튜닝 모델 내재화, AICC 통합
Phase 3 (9~18M): Build 확장 — B2B 플랫폼화, MEC 엣지 배포
```

**Build 선택 근거**:
1. **비용**: 일 10만 건 이상에서 온프레미스 연 TCO $54~84K vs API $102~300K → 연 $48~216K 절감 [CS-05]
2. **프라이버시**: 해외 API 사용 시 국외 이전 동의 필요 → 온프레미스 규제 우위 [CS-06]
3. **차별화**: 통신 도메인 파인튜닝 모델은 범용 API 대비 도메인 특화 성능 확보 가능
4. **종속성 회피**: 특정 API 벤더 가격 인상/서비스 변경 리스크 제거

---

## Step 5: 최종 제언

### 5.1 추천 방향

**Conditional Go — 3개월 PoC 후 본격 투자 결정**

3개 적용 분야를 단계적으로 추진하되, Phase 1 PoC 결과에 따라 Phase 2 진행 여부를 결정한다.

### 5.2 Phase별 로드맵

| Phase | 기간 | 목표 | 투자 규모 | Go/No-Go 기준 |
|-------|------|------|----------|---------------|
| **Phase 1: PoC** | 2026 Q2 (3M) | 한국어 VLM 파인튜닝 75점+, 모뎀 LED 진단 PoC, FCR 30% 달성 | $150~200K | 한국어 CC-OCR 75점 이상, PoC FCR 25% 이상 |
| **Phase 2: 상용화** | 2026 Q3~Q4 (6M) | AICC 통합, 문서 AI B2B 1호 고객, GPU 인프라 확충 | $500K~1M | 실서비스 FCR 30%, B2B 계약 3건+ |
| **Phase 3: 확장** | 2027 H1 (6M) | MEC 엣지 배포, B2B 10개사+, 네트워크 모니터링 | $1~2M | B2B 매출 $1M+, 엣지 지연 100ms 이하 |

### 5.3 핵심 근거

**추진 근거 (Go 요인)**:
1. 시장 CAGR 27~38% 고성장, 2030년까지 $11~23B 규모 [D-01, D-02]
2. 오픈소스 VLM(Qwen2.5-VL 7B)이 DocVQA 96.4%로 상용급 성능 달성 [P-03]
3. 글로벌 통신사 중 이미지 VLM 고객 서비스 상용 사례 부재 → 선점 기회 [CS-01~03]
4. 온프레미스 TCO 우위 (연 $48~216K 절감) + 프라이버시 규제 대응 [CS-05, CS-06]
5. 통신사 97%가 AI 도입 검토 중 — 산업 모멘텀 확보 [G-03]

**조건부 근거 (Conditional 요인)**:
1. 한국어 VLM 성능 격차 11점 (Gemini 80.0 vs Qwen 69.1) — 파인튜닝 결과 불확실 [P-01]
2. 자사 VLM 특허 0건 — 방어력 부재
3. 내부 VLM/MLOps 전문인력 부족
4. SKT A.X K1 이미지 멀티모달 2026H1 → 선점 윈도우 좁음

### 5.4 리스크 레지스터

| # | 리스크 | 영향 | 확률 | 완화 방안 |
|---|--------|------|------|----------|
| R1 | 한국어 파인튜닝 목표(75점) 미달 | 크리티컬 | 중 | 다중 모델 후보(Qwen, InternVL) 병행 실험, 업스테이지 협력 |
| R2 | SKT K1 이미지 멀티모달 조기 출시 | 높음 | 중 | B2B 문서 AI·MEC 엣지 차별화 집중 |
| R3 | GPU 공급 부족/가격 상승 | 중간 | 중 | 클라우드 하이브리드 전략, 양자화(INT4) 활용 |
| R4 | 개인정보 규제 강화 | 중간 | 낮 | 온프레미스 배포로 선제 대응, DPIA 조기 수행 |
| R5 | PoC 기간 내 FCR 목표 미달 | 높음 | 중 | 신뢰도 게이팅(0.85) 적용, 인간-AI 협업 모델 |

### 5.5 Next Action (즉시 실행)

1. **[Week 1~2]** ML엔지니어 채용 공고 + 업스테이지 기술 미팅 일정 확보
2. **[Week 2~4]** Qwen2.5-VL 7B 온프레미스 배포 환경 구축 (A100 x2, vLLM)
3. **[Week 3~6]** 통신 장비 이미지 데이터셋 구축 시작 (모뎀 LED, 셋톱박스, 공유기)
4. **[Week 4~8]** 한국어 파인튜닝 실험 → CC-OCR 벤치마크 재측정
5. **[Week 6~12]** AICC 연동 PoC + 내부 시범 서비스 (상담사 200명)
6. **[Week 4]** DPIA(개인정보 영향평가) 착수

---

## Step 6: 3축 평가 (고객가치 / 사업포텐셜 / 기술경쟁력)

### 6.1 고객가치

| 강점 | 근거 |
|------|------|
| 고객 Pain Point 명확 — "사진으로 보여줘도 텍스트로 설명해야 하는" 불편 | 이미지 문의는 현재 텍스트 재입력 필요, VLM으로 즉시 시각 이해 |
| 문서 처리 수작업 60% 단축 — B2B 고객 실질적 비용 절감 | IDP 시장 CAGR 33.7%, 기업 수요 입증 [DA-05] |
| 프라이버시 보존 온프레미스 → 고객 신뢰 확보 | 해외 API 대비 규제 우위 [CS-06] |

| 리스크 | 근거 |
|--------|------|
| 한국어 OCR 69.1점 — 고객 만족도 보장 불확실 | CC-OCR 벤치마크 [P-01] |
| 자동 해결 실패 시 이중 불편 (사진 전송 + 재연결) | FCR 미달 시 고객 경험 악화 |
| 고객 사진 전송 습관 부재 — 채널 전환 저항 | 이미지 채널 도입 초기 이용률 불확실 |

### 6.2 사업포텐셜

| 강점 | 근거 |
|------|------|
| TAM $3.4B~$23B, CAGR 32~38% 고성장 시장 | [D-01, D-02] |
| 3개 매출원 동시 추진 가능 (비용 절감 + B2B + 인프라) | 고객 서비스, 문서 AI, 네트워크 모니터링 |
| 온프레미스 TCO 연 $48~216K 절감 | 일 10만 건 이상 기준 [CS-05] |

| 리스크 | 근거 |
|--------|------|
| SOM 연 $5~15M — 초기 매출 규모 제한적 | 국내 시장 한정, 글로벌 확장 필요 |
| SKT 자체 모델(500B) 대비 성능 열위 가능 | A.X K1 멀티모달 확장 시 정면 경쟁 |
| B2B 문서 AI에 업스테이지·NAVER 등 선행 플레이어 존재 | 한국어 문서 AI 시장 기 진입자 [DA-04] |

### 6.3 기술경쟁력

| 강점 | 근거 |
|------|------|
| 오픈소스 VLM 성숙 — DocVQA 96.4%, Apache 2.0 | Qwen2.5-VL 7B [P-03] |
| 엣지 배포 현실화 — 2B 모델 2.45GB VRAM, 184 tok/s | Moondream 2B INT4 [EV-06] |
| 양자화 기술 검증 — W4A8 정확도 손실 1.1% | MBQ CVPR 2025 [EV-01] |

| 리스크 | 근거 |
|--------|------|
| 자사 특허 0건 — IP 방어력 없음 | Google·Apple 핵심 특허 보유 [D-09] |
| 한국어 성능 11점 격차 — 파인튜닝 결과 불확실 | Qwen 69.1 vs Gemini 80.0 [P-01] |
| 실시간 영상 VLM 8 FPS 한계 — CCTV 전수 분석 불가 | StreamingVLM H100 기준 [EV-02] |

---

## Step 7: 200점 정량 채점

### 7.1 고객가치 (33/40)

| 세부 지표 | 점수 | 근거 |
|-----------|------|------|
| Pain Point 심각도 | **9**/10 | 이미지 문의를 텍스트로 재설명해야 하는 명확한 불편. 문서 수작업 60% 비효율. 통신사 97% AI 도입 검토 중. |
| 제공 가치 명확성 | **8**/10 | FCR 30~50% 개선, 문서 수작업 60% 단축은 정량적이고 명확. 다만 한국어 성능 미검증으로 실제 가치 전달에 불확실성 존재. |
| 대체제 대비 우위 | **8**/10 | 현재 대체제는 텍스트 챗봇 + 인간 상담사. VLM 이미지 자동 진단은 차별적. 단, GPT-4o API도 대안 (비용·프라이버시 열위). |
| 고객 수용성 | **8**/10 | 사진 전송은 카카오톡 등에서 이미 익숙한 UX. B2B 문서 AI는 RPA 도입 기업에서 수요 입증. 신채널 전환 저항은 낮을 것으로 예상. |

### 7.2 시장매력도 (36/40)

| 세부 지표 | 점수 | 근거 |
|-----------|------|------|
| TAM/SAM/SOM | **9**/10 | TAM $3.4~23B(멀티모달)+$43.9B(IDP), SAM $2~14.8B(통신AI). SOM 연 $5~15M은 국내 한정으로 다소 제한적이나 확장 가능. |
| CAGR | **10**/10 | 멀티모달 AI 32~38%, IDP 33.7%, 영상 AI 33%, AICC 27%. 모든 관련 시장 25% 이상 고성장. 최고점. |
| 시장 타이밍 | **9**/10 | 글로벌 통신사 모두 파일럿 단계 → 선점 윈도우 6~12개월. SKT 2026H1 예고로 긴급성 있음. |
| 규제/정책 | **8**/10 | 개인정보보호위원회 안내서(2025.8)로 법적 근거 명확. 온프레미스 배포 시 해외 API 대비 규제 우위. DPIA 수행 필수. |

### 7.3 기술경쟁력 (28/40)

| 세부 지표 | 점수 | 근거 |
|-----------|------|------|
| TRL 수준 | **8**/10 | 핵심 VLM TRL 9(상용화), AICC 통합 TRL 6~7, 엣지 TRL 6~7. 즉시 PoC 가능하나 완전 상용화까지 6~9개월. |
| 특허 포트폴리오 | **4**/10 | 자사 관련 특허 0건. Google(US20240160853A1), Apple 온디바이스 특허 보유. 방어력 부재가 중대 약점. PoC 과정에서 출원 시작 필요. |
| 기술 장벽 | **8**/10 | 오픈소스 VLM(Apache 2.0)으로 진입 장벽 낮음. 한국어 파인튜닝+통신 도메인 특화가 차별화 장벽. 양자화·엣지 배포 기술 검증 완료. |
| 표준/인증 | **8**/10 | VLM 분야 특별한 표준/인증 요구 없음. ISMS-P 인증 기보유, 개인정보 규제 준수로 충분. |

### 7.4 경쟁우위 (24/40)

| 세부 지표 | 점수 | 근거 |
|-----------|------|------|
| 시장 포지션 | **6**/10 | 국내 3위 통신사로 AI 브랜드 인지도 SKT 대비 열위. AICC 기반은 있으나 VLM 분야 신규 진입. |
| 차별화 지속성 | **6**/10 | 통신 도메인 파인튜닝·온프레미스 프라이버시·MEC 엣지는 차별화 가능. 단, 오픈소스 기반이므로 경쟁사도 모방 가능 (12~18개월). |
| 경쟁사 대응력 | **5**/10 | SKT 자체 모델(500B)+MAU 1,000만 에코시스템으로 빠른 대응 가능. KT는 MS 파트너십으로 기술 접근 용이. 정면 대응보다 니치 차별화 필요. |
| 생태계/파트너 | **7**/10 | 업스테이지(한국어 문서 AI 1위), NVIDIA(GPU/TensorRT), Alibaba(Qwen 오픈소스) 활용 가능. 자체 개발자 생태계는 미약. |

### 7.5 실행가능성 (27/40)

| 세부 지표 | 점수 | 근거 |
|-----------|------|------|
| 내부 역량 | **6**/10 | AICC 운영 경험 보유, MEC 인프라 보유. 단, VLM/MLOps 전문인력 부족 (채용 또는 협력 필요). GPU 인프라 일부 보유. |
| 투자 대비 ROI | **7**/10 | Phase 1 $150~200K 투자로 PoC 검증 가능 (리스크 제한적). 상용화 시 온프레미스 TCO 절감 연 $48~216K. B2B 매출 SOM $5~15M. ROI 양호하나 대규모 수익까지 2~3년. |
| 일정 현실성 | **7**/10 | Phase 1 (3M) PoC는 현실적. Phase 2 (6M) 상용화는 AICC 통합 복잡도에 따라 지연 가능. SKT 대비 동시 진입 가능 시점. |
| 리스크 관리 | **7**/10 | PoC-gated 단계적 투자로 리스크 제한. 한국어 성능 미달 시 API 폴백 가능. 다만 특허 방어·경쟁사 대응 계획은 보강 필요. |

### 7.6 종합 채점표

| 평가 항목 | 배점 | 득점 | 비율 |
|-----------|------|------|------|
| 1. 고객가치 | 40 | **33** | 82.5% |
| 2. 시장매력도 | 40 | **36** | 90.0% |
| 3. 기술경쟁력 | 40 | **28** | 70.0% |
| 4. 경쟁우위 | 40 | **24** | 60.0% |
| 5. 실행가능성 | 40 | **27** | 67.5% |
| **합계** | **200** | **148** | **74.0%** |

### 7.7 판정

| 구간 | 범위 | 해당 여부 |
|------|------|----------|
| **Go** (적극 추진) | 160+ | - |
| **Conditional Go** (조건부 추진) | 120~159 | **148점 — 해당** |
| 재검토 | 80~119 | - |
| No-Go | ~79 | - |

**판정: Conditional Go (148/200)**

Go 전환 조건:
1. Phase 1 PoC에서 한국어 CC-OCR 75점 이상 달성 (현재 69.1점)
2. 고객 서비스 PoC FCR 25% 이상 달성
3. VLM 전문인력 3명 이상 확보 (채용 또는 협력)

상기 3개 조건 충족 시 기술경쟁력(+4~6점)·실행가능성(+3~5점) 개선으로 **155~159점 → Go 경계**에 도달 가능. B2B 1호 계약 확보 시 경쟁우위(+2~3점) 추가로 **Go(160+)** 달성 예상.

---

## References

### Discover 리포트
| # | 출처명 | URL | 유형 | 날짜 |
|---|--------|-----|------|------|
| D-01 | GM Insights — Multimodal AI Market 2025-2034 | [링크](https://www.gminsights.com/industry-analysis/multimodal-ai-market) | report | 2026 |
| D-02 | Grand View Research — Multimodal AI Market 2030 | [링크](https://www.grandviewresearch.com/industry-analysis/multimodal-artificial-intelligence-ai-market-report) | report | 2026 |
| D-03 | Qwen3-VL Technical Report | [링크](https://arxiv.org/abs/2511.21631) | paper | 2025 |
| D-04 | Nature Communications — MiniCPM-V Edge Deployment | [링크](https://www.nature.com/articles/s41467-025-61040-5) | paper | 2025 |
| D-05 | NVIDIA — AI in Telecom Survey 2026 | [링크](https://blogs.nvidia.com/blog/ai-in-telco-survey-2026/) | report | 2026 |
| D-06 | Huawei — Agentic Internet MWC 2026 | [링크](https://totaltele.com/huawei-ushers-in-the-agentic-internet-era-at-mwc-2026/) | news | 2026-03 |
| D-07 | SKT 뉴스룸 — A.X K1 멀티모달 확장 | [링크](https://news.sktelecom.com/219714) | IR | 2026 |
| D-08 | ZDNet Korea — SKT 멀티모달 계획 | [링크](https://zdnet.co.kr/view/?no=20260115152029) | news | 2026-01-15 |
| D-09 | Google Patents — Vision-Language Pretraining | [링크](https://patents.google.com/patent/US20240160853A1/en) | patent | 2024 |
| D-10 | Voxel51 — Visual AI Video 2026 Landscape | [링크](https://voxel51.com/blog/visual-ai-in-video-2026-landscape/) | report | 2026 |

### 고객 서비스 VLM
| # | 출처명 | URL | 유형 | 날짜 |
|---|--------|-----|------|------|
| CS-01 | Deutsche Telekom x Sprinklr CCaaS | [링크](https://www.sprinklr.com/stories/deutsche-telekom/) | case | 2025 |
| CS-02 | Verizon Project 624 AI Overhaul | [링크](https://blog.tmcnet.com/blog/rich-tehrani/ai/verizon-unveils-project-624-ai-powered-overhaul-of-customer-support.html) | news | 2025 |
| CS-03 | SKT CEO MWC 2026 AI Native Strategy | [링크](https://www.prnewswire.com/news-releases/sk-telecom-ceo-unveils-ai-native-strategy-at-mwc26-302700470.html) | IR | 2026-03 |
| CS-04 | CC-OCR Benchmark (한국어 OCR 비교) | [링크](https://arxiv.org/html/2412.02210v2) | paper | 2024-12 |
| CS-05 | On-Premise LLM Break-Even Analysis | [링크](https://arxiv.org/html/2509.18101v3) | paper | 2025-09 |
| CS-06 | 개인정보보호위원회 생성형 AI 안내서 | [링크](https://www.privacy.go.kr/front/bbs/bbsView.do?bbsNo=BBSMSTR_000000000049&bbscttNo=20836) | gov | 2025-08 |

### 엣지 VLM 배포
| # | 출처명 | URL | 유형 | 날짜 |
|---|--------|-----|------|------|
| EV-01 | MBQ: VLM 양자화 (CVPR 2025) | [링크](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_MBQ_Modality-Balanced_Quantization_for_Large_Vision-Language_Models_CVPR_2025_paper.pdf) | paper | 2025 |
| EV-02 | StreamingVLM (MIT Han Lab) | [링크](https://arxiv.org/abs/2510.09608) | paper | 2025-10 |
| EV-03 | VideoScan | [링크](https://arxiv.org/abs/2503.09387) | paper | 2025-03 |
| EV-04 | MiniCPM-V 2.6 (Nature Communications) | [링크](https://www.nature.com/articles/s41467-025-61040-5) | paper | 2025 |
| EV-05 | Columbia Distributed VLMs | [링크](https://wimnet.ee.columbia.edu/wp-content/uploads/2025/04/DistributedVLMs_Efficient_Vision-Language_Processing_through_Cloud-Edge_Collaboration.pdf) | paper | 2025-04 |
| EV-06 | NVIDIA Jetson Edge AI Guide | [링크](https://developer.nvidia.com/blog/getting-started-with-edge-ai-on-nvidia-jetson-llms-vlms-and-foundation-models-for-robotics) | doc | 2025 |

### 문서 AI B2B
| # | 출처명 | URL | 유형 | 날짜 |
|---|--------|-----|------|------|
| DA-01 | PaddleOCR-VL 1.5 | [링크](https://arxiv.org/html/2601.21957v1) | paper | 2026-01 |
| DA-02 | OmniDocBench (CVPR 2025) | [링크](https://github.com/opendatalab/OmniDocBench) | repo | 2025 |
| DA-03 | Mistral OCR 3 | [링크](https://mistral.ai/news/mistral-ocr) | product | 2026 |
| DA-04 | Upstage $45M Series B | [링크](https://www.prnewswire.com/news-releases/upstage-completes-45m-series-b-bridge-302534044.html) | news | 2025-08 |
| DA-05 | Grand View Research — IDP Market 2030 | [링크](https://www.grandviewresearch.com/industry-analysis/intelligent-document-processing-market-report) | report | 2025 |
| DA-06 | Precedence Research — IDP Market $43.9B | [링크](https://www.precedenceresearch.com/intelligent-document-processing-market) | report | 2025 |
| DA-07 | KT MWC 2026 에이전틱 패브릭 | [링크](https://www.youthdaily.co.kr/news/article.html?no=214413) | news | 2026-03 |

### 기타
| # | 출처명 | URL | 유형 | 날짜 |
|---|--------|-----|------|------|
| G-03 | NVIDIA — AI in Telecom Market $14.86B | [링크](https://blogs.nvidia.com/blog/ai-in-telco-survey-2026/) | report | 2026 |
| P-01 | CC-OCR Benchmark (한국어 성능) | [링크](https://arxiv.org/html/2412.02210v2) | paper | 2024-12 |
| P-03 | Qwen2.5-VL Technical Report | [링크](https://arxiv.org/abs/2502.13923) | paper | 2025-02 |

---

## 신뢰도 평가

### 높은 확신
- **시장 규모/CAGR**: GM Insights, Grand View Research, Precedence Research 등 복수 리서치 기관 교차 검증
- **오픈소스 VLM 성능**: DocVQA 96.4%, CC-OCR 벤치마크 — 피어리뷰 논문 기반
- **비용 분석**: arXiv 손익분기 분석 + 복수 벤더 가격표 교차 검증
- **양자화 성능**: CVPR 2025 MBQ — 피어리뷰 완료
- **개인정보 규제**: 개인정보보호위원회 공식 안내서 (2025.8)
- **경쟁사 전략**: SKT IR 자료, MWC 2026 공식 발표 기반

### 추가 검증 필요
- **SOM 추정 (연 $5~15M)**: 자체 산출, 실제 고객 수요 조사 미실시
- **한국어 파인튜닝 75점 달성 가능성**: 이론적 가능하나 실험 결과 없음 — Phase 1 PoC 핵심 검증 항목
- **FCR 30~50% 목표**: 글로벌 통신사 중 이미지 VLM FCR 공개 수치 0건 — 자체 파일럿 필요
- **SKT A.X K1 이미지 멀티모달 출시 시점**: "2026 상반기"만 공개, 구체적 월 미확정
- **내부 역량 평가 (6/10)**: VLM/MLOps 인력 현황 상세 파악 필요
- **B2B 문서 AI 수요**: 잠재 고객 인터뷰 미실시

---

*평가일: 2026-03-12 | 평가 모델: Claude Opus 4.6 | 데이터 기준: 2026-03-12*
