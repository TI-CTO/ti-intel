---
validator_status: partial
target_file: /Users/ctoti/Project/ClaudeCode/outputs/reports/voice-ai/2026-03-17_speech-generation/2026-03-17_wtis-skill1.md
verified_at: 2026-03-17
---

# Validation Report: Speech Generation (WTIS SKILL-1)

## 요약
- 상태: PARTIAL
- 주요 이슈: References 테이블 미등재 코드 11건 (고아 인용), 미인용 수치 2건, 논리 경미 이슈 1건

---

## 1. 인용 검증

| 항목 | 결과 | 비고 |
|------|------|------|
| References 테이블 존재 | ✅ | 20개 출처 등재 |
| 모든 [N] 인용 매칭 | ❌ | 미매칭 11건 — 아래 목록 참조 |
| 미인용 주장 발견 | ✅ | 2건 발견 — 아래 목록 참조 |

### References 테이블 미등재 코드 (본문 인용 → 테이블 없음)

| 코드 | 인용 위치 | 인용 내용 |
|------|----------|----------|
| G-03-C | 경쟁사 비교표, Gap Analysis | ElevenLabs de facto Voice Cloning 표준 |
| G-11-C | TRL 매핑, Gap Analysis (규제 대응), 경쟁사 표 | Google Chirp 3 Voice Cloning, Google 오디오 무보존 |
| G-13-C | 경쟁사 표 (Google), TRL 매핑 | Google Hume AI팀 흡수 |
| G-14-C | TRL 매핑 (Emotional TTS Watch) | Index TTS 2 |
| G-14-S | 사업포텐셜 리스크 (마진 압박) | Inworld '20배 저렴' 주장 |
| G-15-C | 경쟁사 비교표 (Microsoft Azure) | Personal Voice v2.1, 140+ 언어 |
| G-32 | TRL 매핑 (On-device), 경쟁사 표 (Supertone) | Supertonic ONNX 47ms |
| G-34 | 경쟁사 표 (Naver), 기술경쟁력 리스크 | Naver MOS 4.22 (자사 벤치마크) |
| G-35 | SMART Test Relevant 항목 | 에이닷 MAU 810만 |
| G-37 | 기술경쟁력 배점 근거 (표준/인증) | C2PA 음성 출처 표준 확산 |
| E-05 | 경쟁사 비교표 (KT) | KT MWC 2026 공개 근거 |

**총 11개 코드가 본문에서 인용되었으나 References 테이블에 미등재.**

> 참고: References 섹션 서두에 "핵심 출처만 요약"이라는 면책 문구가 있으나(`선행 리서치 .../research.md의 References 섹션에 전수 수록`), WTIS 검증 기준상 본 파일 내 References 테이블이 인용 코드를 완전히 커버하지 않으면 고아 인용으로 판정한다.

### 미인용 주장 (출처 없는 팩트)

| 위치 | 미인용 주장 |
|------|------------|
| 경쟁사 비교표, 고객가치 강점 | Deutsche Telekom "50개 언어 실시간 번역" — E-03 인용이 있으나, 해당 수치(50개 언어)가 E-03에서 확인됨. 단, 본문 일부 위치에서 [E-03] 없이 서술 (라인 112 테이블 vs 라인 64는 적절히 인용). **경미** |
| 상용 API 가격 비교표 | "$5~19/1M chars" 종량제 가격 — [G-13-S]가 근처에 있으나 해당 테이블 행(라인 91)에 인라인 인용 없음 |

---

## 2. 수치 검증

| 수치 | 인용 코드 | 소스 수 | 독립 검증 결과 | 판정 |
|------|----------|---------|--------------|------|
| TAM $3.65~4.25B (2025) | G-26, G-27, G-28 | 3 | WebSearch 확인: 복수 기관 수렴 ($3.65B BusinessResearchInsights, $3.87B Mordor, $4.25B ExpertMktResearch). 범위 일치 ✅ | PASS |
| CAGR 12~14% (보수적) | G-26, G-27 | 2 | WebSearch 확인: 12.3~12.89% 수렴 구간. 보수적 추정으로 적절. "14%"는 상한 추정치이나 Mordor 12.89%를 약간 상회 — 경미 ✅ | PASS |
| Voice AI Agent CAGR 34.8% | G-29 | 1 | WebSearch 확인: market.us 출처 수치 정확히 일치 ✅. 단, C등급 단일 출처 | [B] 단일 출처 |
| ElevenLabs $11B 밸류에이션 | E-02 | 1 | WebSearch 확인: 2026-02-04 Series D $500M at $11B (CNBC, TechCrunch 다수 보도). 수치 정확 ✅ | PASS |
| ElevenLabs 800+ B2B 파트너 | G-06-S | 1 | WebSearch 확인: ElevenLabs 공식 발표 "Fortune 500 41%" + "$330M ARR"는 확인. "800+ B2B 파트너" 수치는 직접 확인 불가. E-02 원문 기준 | [B] 미확인 |
| Cartesia TTFB 40ms | G-12-S | 1 | WebSearch 확인: Sonic Turbo 40ms 수치 다수 출처 일치 (Cartesia 공식 docs, eesel.ai, smallest.ai 벤치마크). 단, G-12-S는 Inworld 블로그 [C] 출처 — 40ms 수치 자체는 Cartesia 자체 공식 데이터에서도 확인 가능 ✅ | PASS (수치 정확, 소스 등급 낮음) |
| Inworld <250ms P90 | G-13-S | 1 | WebSearch 확인: Inworld TTS-1.5 Max가 <250ms P90 수치 일치 ✅. 단, G-13-S 코드가 Artificial Analysis 리더보드로 등재 — Inworld P90 수치는 Inworld 자체 블로그에서 유래. **코드-내용 불일치 가능성** | [B] 코드 맥락 불일치 의심 |
| Deutsche Telekom 50개 언어 | E-03 | 1 | WebSearch 확인: Deutsche Telekom 공식 보도자료 — "향후 12개월 내 최대 50개 언어 지원 계획". 현재 서비스 아닌 로드맵 수치. 본문에서 "50개 언어 실시간 번역"으로 표현 — 현재 구현이 아닌 계획임을 명시 필요 | [B] 표현 과장 가능성 |
| SKT "5년 뒤 10조 시장" | E-01 | 1 | 경쟁사 발언 인용. 단일 언론 출처. 역산 근거로 사용된 SAM $500M~1B 산출 로직 미공개 | [B] SAM 역산 근거 불투명 |
| Naver HyperCLOVA X Omni MOS 4.22 | G-34 | 1 | G-34 References 미등재. "자사 벤치마크"로 명기 — 자체 공표 수치로 독립 검증 불가 | [D] 자사 벤치마크 |
| Qwen3-TTS WER 1.835% | G-31 | 1 | G-31은 Softcery 블로그 [C] 단일 출처 | [C] 단일 소스 |
| ElevenLabs WER 2.83% | G-31 | 1 | 동일 Softcery [C] 블로그 단일 출처 | [C] 단일 소스 |
| 상용 API 가격 $5~19/1M chars | 미인용 | 0 | 인라인 인용 없음 | 미인용 |

---

## 보강 필요 항목 (reinforcement_needed)

```yaml
reinforcement_needed:
  - claim: "ElevenLabs 800+ B2B 파트너"
    current_sources: 1
    suggested_keywords: ["ElevenLabs enterprise customers 2026", "ElevenLabs B2B partnerships Fortune500"]

  - claim: "Deutsche Telekom Magenta AI 50개 언어 실시간 번역"
    current_sources: 1
    note: "현재 구현이 아닌 12개월 로드맵 수치. 표현 수정 필요"
    suggested_keywords: ["Deutsche Telekom Magenta AI Call Assistant languages roadmap", "Telekom ElevenLabs 50 languages plan"]

  - claim: "Voice AI Agent CAGR 34.8%"
    current_sources: 1
    suggested_keywords: ["voice AI agents market CAGR 2024 2034 Grand View", "voice AI market growth forecast independent"]

  - claim: "Cartesia TTFB 40ms (G-12-S = Inworld 블로그로 등재)"
    current_sources: 1
    note: "G-12-S 출처가 Inworld 블로그(경쟁사 자료)로 등재됨. Cartesia 공식 또는 중립 벤치마크로 보강 권장"
    suggested_keywords: ["Cartesia Sonic Turbo latency benchmark 2026", "Cartesia TTFB independent test"]

  - claim: "SAM ~$500M~1B (SKT 10조 시장 역산)"
    current_sources: 0
    note: "역산 로직 및 방법론 미공개. [D] 태그 부여는 적절하나 역산 산출 근거 명시 필요"
    suggested_keywords: ["AICC 시장 규모 한국 2025", "통신사 AICC 솔루션 시장 규모"]

  - claim: "상용 API 가격 $5~19/1M chars"
    current_sources: 0
    suggested_keywords: ["ElevenLabs pricing per million characters 2026", "TTS API pricing comparison 2026"]
```

---

## 3. 논리 검증

### 3-1. 채점 근거 일관성

| 항목 | 점수 | 논리 평가 |
|------|------|----------|
| 고객가치 합계 | 8+7+5+6 = **26** ✅ | 산술 정확 |
| 시장매력도 합계 | 8+8+7+8 = **31** ✅ | 산술 정확 |
| 기술경쟁력 합계 | 9+5+4+7 = **25** ✅ | 산술 정확 |
| 경쟁우위 합계 | 4+6+5+7 = **22** ✅ | 산술 정확 |
| 실행가능성 합계 | 5+7+7+5 = **24** ✅ | 산술 정확 |
| **총점** | 26+31+25+22+24 = **128** ✅ | 산술 정확 |

### 3-2. 논리적 도약 여부

| 위치 | 내용 | 평가 |
|------|------|------|
| 3B 의사결정 로직 | "차별화 중요도(5) < 8 → BUILD 단독 부적합"이라는 임계값 기준이 명시되지 않음 — 8이라는 임계값의 출처 불명 | 경미 이슈. 프레임워크 내부 기준이므로 외부 검증 불가하나, 근거 없는 수치 제시 |
| Inworld <250ms P90이 Real-time Voice Agent TRL 근거로 사용 | G-13-S(Artificial Analysis)로 인용됐으나 실제 내용은 Inworld 자체 발표 수치 | 코드-내용 불일치 (경미) |
| 경쟁사 대응력 점수 5/10에 [D] 인용 | "SKT/KT도 동일 파트너십 가능. 기술 자체 차별화 어려움 [D]" — [D]는 데이터 부족 태그인데 점수 산정 근거로 사용됨. [D]를 낮은 점수의 근거로 쓰는 것은 논리적으로 타당(불확실성이 점수를 낮춤). **문제 없음** | PASS |
| Deutsche Telekom 모델의 마진 구조 미공개 | [D] 태그 부여 후 "Borrow 모델 ROI 구조 실증"이라고 동시에 주장 — 수익 세부 구조는 미공개이나 사업 모델 자체의 실증은 별개 개념. 논리적 충돌 아님 | PASS |

### 3-3. 결론 vs 증거 수준

- Borrow + Build 전략 권고는 3B 매트릭스, TRL 분석, 경쟁 Gap Analysis의 복수 근거에서 도출 — 논리 도약 없음.
- "통신사 고유 역량(망 통합)"을 핵심 차별화로 제시 — Deutsche Telekom 사례가 실증 근거로 적절.
- 리스크 3건 모두 근거 있으며 완화 방안이 대칭적으로 제시됨.

**논리 검증: 주요 이슈 없음 (경미 2건)**

---

## 4. 편향 검증

| 항목 | 평가 | 비고 |
|------|------|------|
| 긍정/부정 균형 | ✅ PASS | 고객가치·사업포텐셜·기술경쟁력 각 섹션에서 강점과 리스크를 대칭적으로 제시 |
| 경쟁사 분석 균형 | ✅ PASS | ElevenLabs/Google 우위 명시, SKT/KT 선점 인정, 자사 약점(다국어·Voice Cloning 열위) 명시 |
| SKT/KT 편향 | ✅ PASS | SKT/KT 선점 사실을 리스크로 명시. 자사 대비 격차 솔직히 기술 |
| Cherry-picking | 경미 이슈 | Deutsche Telekom 마진 구조 미공개임에도 "ROI 구조 실증" 표현. 파트너십 비용 구조 불투명성 충분히 강조되지 않음 — 단, 리스크 섹션에서 "파트너 종속 리스크"로 언급됨. 경미 |
| 자사 내부 역량 공백 처리 | ✅ PASS | [D] 태그와 "데이터 부족" 명시로 정직하게 처리 |
| WTP 미검증 | ✅ PASS | B2C 고객 WTP를 [D]로 명시. 적절한 불확실성 표현 |

**편향 검증: PASS (경미 1건)**

---

## 5. 단일 소스 이슈

| 수치/주장 | 코드 | 등급 | 판정 |
|-----------|------|------|------|
| Voice Cloning 시장 $7.75B (2029) | N-01 | [B] | 단일 출처 — 문서 내 명시됨 ✅ |
| Voice AI Agent CAGR 34.8% | G-29 | [C] | 단일 출처 — 문서 내 명시됨 ✅ |
| Qwen3-TTS WER 1.835%, ElevenLabs WER 2.83% | G-31 | [C] | 단일 블로그 출처 |
| Naver MOS 4.22 | G-34 | 자사 벤치마크 [D] | 단일·자체 출처 |
| ElevenLabs 800+ B2B 파트너 | G-06-S | [B] | 단일 TechCrunch 기사 |
| Cartesia TTFB 40ms (G-12-S) | G-12-S | [C] | Inworld 경쟁사 블로그 인용 — 독립 검증으로 수치 자체는 일치하나 소스 등급 낮음 |
| 상용 API 가격 $5~19/1M chars | 미인용 | — | 인라인 인용 없음 |

---

## 이슈 목록

| # | 심각도 | 카테고리 | 설명 | 처리 권고 |
|---|--------|---------|------|----------|
| 1 | **심각** | 인용 | G-03-C, G-11-C, G-13-C, G-14-C, G-14-S, G-15-C, G-32, G-34, G-35, G-37, E-05 — 11개 코드가 본문에서 인용되었으나 References 테이블에 미등재 | References 테이블에 11개 출처 추가 또는 선행 research.md를 명시적으로 포인터로 인정하는 구조 변경 필요 |
| 2 | **심각** | 수치 | Deutsche Telekom "50개 언어 실시간 번역" — 현재 구현이 아닌 12개월 로드맵 계획 수치. 본문 표현이 현재 완료형으로 오해될 소지 | "향후 12개월 내 최대 50개 언어 지원 예정"으로 수정 |
| 3 | **경미** | 인용 | G-12-S (Inworld 블로그)가 Cartesia TTFB 40ms 근거로 사용됨 — 경쟁사 블로그가 유일 출처. 수치 자체는 독립 검증에서 확인되나 소스 등급이 낮음 | Cartesia 공식 docs 또는 중립 벤치마크 소스로 교체 권고 |
| 4 | **경미** | 수치 | G-13-S (Artificial Analysis 리더보드) 코드로 Inworld <250ms P90 수치를 인용 — 해당 수치는 Inworld 자체 발표 수치이므로 코드-내용 불일치 | Inworld 공식 출처 별도 코드 부여 필요 |
| 5 | **경미** | 인용 | 상용 API 가격 "$5~19/1M chars" (라인 91 테이블) — 인라인 인용 없음 | [G-13-S] 또는 별도 출처 추가 |
| 6 | **경미** | 논리 | 3B 의사결정 로직의 임계값 "8" 기준 출처 불명 | 프레임워크 기준 명시 또는 괄호 주석 추가 |
| 7 | **경미** | 편향 | Deutsche Telekom 마진 구조 미공개인 상황에서 "ROI 구조 실증"은 과장 표현 가능성 | "사업 모델 가능성 실증" 수준으로 표현 완화 권고 |

---

## 결론

본 리포트는 시장 데이터(TAM 4개 출처 교차)와 기술 데이터(독립 벤치마크), 규제 데이터(공식 법률 텍스트)에서 높은 신뢰도를 보이며, 채점 산술 오류 없이 128/200 Conditional Go 판정이 논리적으로 일관성 있게 도출된다. 그러나 References 테이블에 미등재된 인용 코드가 11건으로 다수 발견되며, 이 중 일부(G-11-C의 규제 대응 강점, G-34의 Naver MOS 비교 등)는 핵심 논거의 근거에 해당한다. Deutsche Telekom 50개 언어 수치가 현재 구현이 아닌 12개월 로드맵임을 표현이 모호하게 처리한 점도 수정이 필요하다. 인용 구조 보완 후 재검토 권장.

---

*Validated by: Validator Agent (claude-sonnet-4-6) | 2026-03-17*
