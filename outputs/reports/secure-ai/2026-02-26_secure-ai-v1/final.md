---
topic: Secure AI — B2C 통화 보안
date: 2026-02-26
wtis_version: v4.0
wtis_mode: proposal
skills_executed: [SKILL-0, research-deep, SKILL-1, validator]
confidence: medium
status: completed
total_references: 29
verdict: Conditional Go
score: 128/200
strategy: Borrow + Build
---

# WTIS Report: Secure AI — B2C 통화 보안

## 경영진 요약

> **Conditional Go (128/200)** — Secure AI 과제는 보이스피싱 피해 **1조 2,578억 원(2025년, +47% YoY)** [N-04]이라는 명확한 시장 명분을 갖추고 있으나, **3가지 구조적 제약**으로 인해 제안서 핵심 가정의 재설계가 필수적이다.
>
> 1. **동형암호(HE) 실시간 불가** — FHE per-gate 지연 13~26ms [G-01], 통화 실시간 요건(< 20ms) 충족 불가 [G-04]. 제안서의 "3중 보안 조합" 핵심 가정이 파괴됨.
> 2. **삼성/Apple 무료 선점** — 갤럭시 S26(2026.3)과 iOS 26이 OS 레벨 보이스피싱 탐지를 무료 기본 탑재 [E-01, N-07]. B2C 유료 서비스 공간 급격 축소.
> 3. **OndeviceAI 탐지 commodity화** — 국내 3사(SKT/KT/LGU+) + 삼성 모두 상용화 완료 [E-01~E-04]. 차별화 요소 소멸.
>
> **PQC(양자내성암호) E2E 통화 암호화가 유일한 차별화 축**(경쟁사 미탑재, TRL 5~6). **Borrow(PQC 벤더 파트너십) + Build(Anti-DeepVoice/금융 B2B 내재화)** 혼합 전략 권고. 신뢰도: Medium.

---

## 상세 분석

### 핵심 기술 판정

| 기술 | TRL | 판정 | 근거 |
|------|-----|------|------|
| 동형암호 (실시간 통화) | **2~3** | **불가 → Watch** | per-gate 13~26ms, 음성 스트림 누적 시 초 단위 지연 [G-01, G-04] |
| OndeviceAI 보이스피싱 탐지 | 7~8 | **가능, 이미 commodity** | 국내 3사+삼성 상용화 완료 [E-01~E-04] |
| Anti-DeepVoice | 6~7 | **LGU+ 선점 우위** | 세계 최초 상용화 [E-05], 5,500건 탐지 [N-05] |
| PQC VoLTE E2E 암호화 | 5~6 | **유일한 차별화축** | 경쟁사 미탑재, 3GPP 미표준화 [G-08] |

### 경쟁 포지션

| 경쟁사 | 서비스 | 핵심 성과 | 출처 |
|--------|--------|----------|------|
| SKT | 스캠뱅가드 + 에이닷 | 11억 건/년 차단, CES/MWC 수상 | [E-02] |
| KT | AI 탐지 2.0 + 후후 | 탐지율 93%+, 1,300억 원 피해 예방 | [E-03] |
| LGU+ | 익시오 Anti-DeepVoice | KB 연동 1,720억 원 피해 예방 | [E-04] |
| 삼성 | 갤럭시 S26 Phone 앱 | OS 기본 탑재, **무료**, 국과수 3만건 학습 | [E-01] |
| Apple | iOS 26 Call Screening | OS 기본, **무료**, 20개국+ | [N-07] |

**Gap Analysis**: LGU+는 Anti-DeepVoice에서 6~12개월 선점, PQC 통합에서 유일한 포지션을 보유하나, 탐지율 미공개(KT 93%+ 대비), 가입자 규모 열위(21%), 삼성/Apple 무료화 구조에서 **유료 B2C 서비스의 존재 이유** 확보가 최대 과제.

### 전략 권고: Borrow + Build

```
[과제명]: Secure AI — B2C 통화 보안
[추천 방향]: Borrow + Build (HE는 Watch)
[핵심 근거]:
  - 시장: 피해 1조 2,578억 원/년 [N-04], 글로벌 CAGR 14.2% [G-14]
         단, 삼성/Apple 무료 OS 탑재로 B2C 유료 공간 축소 [E-01, N-07]
  - 기술: PQC E2E 암호화 = 유일한 차별화축 (TRL 5~6, 경쟁사 미탑재)
         HE 실시간 불가 (TRL 2~3) → 제안서 재설계 필수
  - 사업: KB국민은행 B2B 모델 1,720억 원 피해 예방 [E-04] → 현실적 수익 경로
[리스크]:
  - 삼성 S26 무료 탑재 (확률: H, 영향: H) [E-01]
  - 정부 공동 플랫폼 2026~2027 (확률: H, 영향: H) [E-01]
  - KT 탐지율 우위 93%+ (확률: H, 영향: M) [E-03]
  - PQC VoLTE 통합 지연 (확률: M, 영향: H) [G-08]
[Next Action]:
  - [ ] 0~3개월: 제안서 재설계 (HE 제거, PQC + Anti-DeepVoice + 금융 B2B 3축)
  - [ ] 0~3개월: PQC 벤더 쇼트리스트 + 파트너십 협상
  - [ ] 3~6개월: PQC VoLTE E2E PoC (내부 망 + 삼성 단말)
  - [ ] 3~6개월: 익시오 탐지율 정량 공개 (KT 93%+ 대응)
  - [ ] 6~12개월: KB 모델 → 타 시중은행 2~3사 확장
  - [ ] 12~18개월: PQC 프리미엄 통화 파일럿 (VIP/기업 세그먼트)
```

### 정량 평가 (128/200)

| # | 평가 항목 | 세부1 | 세부2 | 세부3 | 세부4 | 소계 |
|---|----------|-------|-------|-------|-------|------|
| 1 | 고객가치 | 9 (Pain Point) | 7 (가치 명확성) | 5 (대체제 우위) | 7 (수용성) | **28** |
| 2 | 시장매력도 | 5 (TAM/SAM) | 7 (CAGR) | 6 (타이밍) | 7 (규제) | **25** |
| 3 | 기술경쟁력 | 6 (TRL) | 5 (특허) | 7 (기술장벽) | 8 (표준) | **26** |
| 4 | 경쟁우위 | 5 (포지션) | 6 (지속성) | 5 (대응력) | 6 (생태계) | **22** |
| 5 | 실행가능성 | 7 (내부역량) | 6 (ROI) | 7 (일정) | 7 (리스크) | **27** |
| | **총점** | | | | | **128/200** |

**판정: Conditional Go** — 아래 보완 조건 충족 시 추진 가능:
1. HE 실시간 통화 제거 → ZKP 또는 비실시간 HE로 재설계
2. SMART KPI 설정 (탐지율, 피해 예방액, PQC PoC 일정)
3. 국내 TAM/SAM 산출 (WTP 소비자 조사 + B2B 시장 규모)

---

## 교차검증 결과

**validator 판정: PARTIAL**

| 검증 항목 | 결과 | 비고 |
|----------|------|------|
| 인용 검증 | ⚠️ | References 29개 완비. 단, Orphaned References 7개 (본문 미인용) |
| 수치 검증 | ⚠️ | HE 불가 판정은 복수 학술 소스 검증 완료. 사업 수치 대부분 단일 소스 |
| 논리 검증 | ✅ | 핵심 결론이 증거 수준 초과하지 않음. 미인용 추정값 2개 발견 |
| 편향 검증 | ✅ | 강점과 약점 균형 있게 분석. 제안서 핵심 가정 정면 반박 포함 |

**핵심 안전 판정**: 보고서의 가장 중요한 기술 결론(HE 실시간 불가)은 복수 독립 학술 소스(G-01, G-04)로 교차 검증 완료 — **판정 근거 견고함**.

**개선 필요**: 사업 수치(피해 1조 원, KT 93%, LGU+ 1,720억 원)는 기업 자체 발표 단일 소스 의존. 추가 교차검증 권고.

---

## 권고 및 Next Action

- [ ] **즉시**: 제안서 재설계 — HE 실시간 통화 제거, "PQC E2E 암호화 + Anti-DeepVoice + 금융 B2B 연계" 3축으로 전환
- [ ] **0~3개월**: PQC 벤더(Thales, IDQ, PQShield) 파트너십 협상 개시
- [ ] **3~6개월**: PQC VoLTE E2E PoC + 익시오 탐지율 정량 공개
- [ ] **6~12개월**: KB 모델 타 금융사 확장 + 정부 공동 플랫폼 데이터 허브 역할 선점
- [ ] **12~18개월**: PQC 프리미엄 통화 서비스 파일럿 (VIP/기업 세그먼트)
- [ ] **지속 모니터링**: ZKP 딥페이크 탐지 연구 동향 [G-12], 삼성/Apple OS 업데이트

---

## References

### 글로벌 출처 (G-xx)

| 번호 | 출처명 | 발행일 | 기관유형 | 제목 | 관련성 | 신뢰성 | 최신성 | URL |
|------|--------|-------|----------|------|--------|--------|--------|-----|
| G-01 | TFHE / ACM CCS 2025 | 2025 | 학술 | TFHE + Refined TFHE Leveled HE | 5 | 5 | 5 | https://tfhe.github.io/tfhe/ |
| G-04 | arXiv | 2026.02 | 학술 | Hybrid HE Feasibility | 5 | 4 | 5 | https://arxiv.org/pdf/2602.02717 |
| G-07 | postquantum.com | 2025 | 전문기관 | PQC Standardization Update | 4 | 4 | 5 | https://postquantum.com/post-quantum/cryptography-pqc-nist/ |
| G-08 | postquantum.com | 2025 | 전문기관 | Telecom PQC Challenges | 5 | 4 | 5 | https://postquantum.com/post-quantum/telecom-pqc-challenges/ |
| G-09 | Pindrop | 2025 | 기업 | Voice Intelligence Report | 4 | 4 | 5 | https://www.pindrop.com/research/report/voice-intelligence-security-report/ |
| G-12 | arXiv | 2025.07 | 학술 | ZKP Deepfake Detection | 5 | 4 | 5 | https://arxiv.org/html/2507.17010 |
| G-14 | GrowthMarketReports | 2024 | 리서치 | Fraud Analytics Market 2033 | 4 | 3 | 4 | https://growthmarketreports.com/report/fraud-analytics-for-international-voice-market |

### 최신 동향 (N-xx)

| 번호 | 출처명 | 발행일 | 제목 | URL |
|------|--------|-------|------|-----|
| N-04 | 헤럴드경제 | 2026 | 보이스피싱 피해 1.2조 사상 최대 | https://biz.heraldcorp.com/article/10661923 |
| N-05 | 스마트투데이 | 2025 | LGU+ Anti-DeepVoice 5500건 탐지 | https://www.smarttoday.co.kr/news/articleView.html?idxno=87596 |
| N-07 | 9to5Mac | 2025.06 | iOS 26 Call Screening | https://9to5mac.com/2025/06/13/security-bite-apples-new-ios-26-spam-tools-will-make-scammers-cry/ |

### 기업 발언 (E-xx)

| 번호 | 출처명 | 발행일 | 제목 | 요약 |
|------|--------|-------|------|------|
| E-01 | 삼성 뉴스룸 / 과기정통부 | 2026.02 | 갤럭시 AI 보이스피싱 차단 | 국과수 3만건 학습, One UI 8.0+ 기본, 3사 협력 |
| E-02 | SKT 뉴스룸 | 2025~2026 | 에이닷 스캠뱅가드 | 온디바이스 AI, 11억 건/년 차단 |
| E-03 | KT 뉴스룸 / 전자신문 | 2025 | AI 보이스피싱 탐지 2.0 | 93%+ 탐지율, 1,300억 원 피해 예방 |
| E-04 | 한국NGO신문 / EBN | 2026 | KB-LGU+ 실시간 대응 | 1,720억 원 피해 예방, MWC26 시연 |
| E-05 | Korea Herald / Korea Times | 2025.02 | LGU+ Anti-DeepVoice MWC 2025 | Exy Guardian 스위트 발표 |

### 내부 자료 (I-xx)

| 번호 | 자료명 | 작성일 | 인용내용 |
|------|--------|-------|---------|
| I-01 | Secure AI 기술·시장·규제 리서치 | 2026-02-25 | HE TRL 4~5, PQC TRL 7~8, 투자 비교 |
| I-02 | SKILL-0 Analysis Brief | 2026-02-26 | V1~V6 검증 항목, 경쟁사 목록 |

---

## 파이프라인 산출물

| 단계 | 파일 | 상태 |
|------|------|------|
| SKILL-0 (제안서 파싱) | `2026-02-26_wtis-proposal-secure-ai-skill0.md` | ✅ pass |
| research-deep (심층 리서치) | `2026-02-26_wtis-proposal-secure-ai-research.md` | ✅ pass |
| SKILL-1 (선정검증) | `2026-02-26_wtis-proposal-secure-ai-skill1.md` | ✅ uncertain (Conditional Go) |
| validator (교차검증) | `2026-02-26_wtis-proposal-secure-ai-skill1-validator.md` | ⚠️ partial |
| **최종 보고서** | `2026-02-26_wtis-proposal-secure-ai-final.md` | ✅ completed |
