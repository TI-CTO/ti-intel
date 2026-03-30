---
validator_status: partial
target_file: /Users/ctoti/Project/ClaudeCode/outputs/reports/weekly/2026-03-30_weekly-voice-ai.md
verified_at: 2026-03-30
---

# Validation Report — 2026-W14 Voice AI Weekly

## 요약
- 상태: **PARTIAL** (Critical 3건, Minor 6건 발견)
- References 테이블: 36개 소스 (G-01~G-30, P-01~P-05, E-01~E-05)
- Critical 이슈: TTFA 수치 오기입(90ms→실제 70ms), 시작 시장 규모 불일치(Voice AI $2.4B→실제 $3.14B), E-01 날짜 오기입(3/14→실제 1/14)
- Minor 이슈: G-21 URL 귀속 오류, G-22 주요 수치 미지지, G-26 핵심 수치 미지지, E-03/G-03 접근 불가, G-29 "1인 1 AI 에이전트" 표현 미지지, P-04 저자 "Alibaba Qwen 팀" 미확인

---

## 1. 인용 검증

| 항목 | 결과 | 비고 |
|------|------|------|
| References 테이블 존재 | ✅ | G-01~G-30, P-01~P-05, E-01~E-05 (36개) |
| 모든 [N] 인용 매칭 | ⚠️ | G-30은 테이블 등재됐으나 본문 미인용 (고아 소스 1건) |
| 미인용 주장 발견 | ✅ | 주요 주장 전반 인용 확인됨 |

**고아 소스 (테이블 등재, 본문 미인용):**
- **G-30** (VentureBeat — Mistral Voxtral TTS beats ElevenLabs): 본문 어디에도 `[[G-30]]` 인용 없음

---

## 2. 수치 검증

| 수치 | 소스 수 | 판정 | 비고 |
|------|---------|------|------|
| Voxtral TTFA 90ms | 1 (G-01) | ❌ Critical | 실제 G-01 페이지: "70ms for a typical input voice sample of 10 seconds". 리포트 표기 90ms는 오기입 |
| Voxtral ElevenLabs 68.4% 승률 | 2 (G-01, P-01) | ✅ | G-01 미기재, P-01(arXiv)에서 "68.4% win rate over ElevenLabs Flash v2.5" 확인 |
| Voxtral $0.016/1k chars | 1 (G-01) | ✅ | G-01 직접 확인 |
| Voxtral 9개 언어 | 1 (G-01) | ✅ | G-01 직접 확인 |
| Voxtral 3초 제로샷 클로닝 | 1 (G-01) | ✅ | G-01 직접 확인 |
| xAI $0.05/min | 1 (G-04) | ⚠️ | G-04 페이지에 가격 정보 없음 (G-03 403 오류). 대안 소스 탐색 필요 |
| ElevenLabs v3 오류율 15.3%→4.9% | 1 (G-08) | ⚠️ | G-08 CSS만 반환. 내용 미검증 |
| Voice AI 에이전트 시장 2024년 $2.4B | 1 (G-13) | ❌ Critical | G-13 실제 수치: $3.14B (전체 시장). 리포트의 $2.4B 불일치 |
| Voice AI 에이전트 시장 2034년 $47.5B | 1 (G-13) | ✅ | G-13 확인됨 |
| TTS 시장 2026년 $4.36B→2031년 $7.92B (CAGR 12.66%) | 1 (G-12) | ✅ | G-12(Mordor Intelligence) 직접 확인 |
| 보이스 클로닝 시장 2032년 $162억 (CAGR 27.3%) | 1 (G-20) | ✅ | G-20(Allied Market Research) 직접 확인 |
| Deepgram $130M Series C / $1.3B 밸류 | 1 (G-11) | ✅ | G-11 직접 확인 |
| ElevenLabs Series D $500M / $11B | 1 (G-11 인용) | ⚠️ | G-11은 Deepgram 발표. ElevenLabs 펀딩 별도 출처 없음. 단일 소스 귀속 오류 의심 |
| IBM 콜센터 비용 40% 절감 | 1 (E-04) | ⚠️ | G-05(IBM 뉴스룸) 및 E-04(동일 URL) 모두에서 해당 수치 미확인 |
| Deepgram Flux EOT ~260ms | 1 (G-24) | ❌ | G-24 페이지에 260ms 수치 없음. 실제: p90 latency 1s, p95 1.5s (200~600ms 개선치) |
| Deepgram Flux 오탐 ~30% 감소 | 1 (G-24) | ✅ | G-24 직접 확인 |
| SoundHound 3천만 건 AI 인터랙션(2025) | 1 (G-23/E-05) | ❌ | G-23/E-05(공식 보도자료)에 "3천만 건" 없음. "billions of AI interactions each year" 표현만 존재 |
| PMC 실세계 정확도 57% 향상 | 1 (P-02) | ❌ | P-02 페이지에 57% 수치 없음. 관련 내용(일반화 실패)은 있으나 구체 수치 미확인 |
| McAfee 90%→96% 정확도 | 1 (G-16) | ⚠️ | G-16 타임아웃. 검증 불가 |
| Pindrop FNBO 조사 시간 35~40%↓ 정확도 50%↑ | 1 (E-02) | ✅ | E-02 직접 확인 |
| Pindrop $400억 AI 사기 피해 2027 | 1 (E-02) | ✅ | E-02 직접 확인 |
| LiveKit ~25ms 추론, ~400MB RAM, 14개 언어 | 1 (G-22) | ❌ | G-22 페이지에 해당 수치 없음. VAD/STT/모델 기반 4계층(리포트는 3계층으로 서술) |
| AssemblyAI ~150ms P50, WER 8.14% | 1 (G-21) | ❌ | G-21 URL 귀속 오류 (아래 참조) |
| KT GiGA Genie 10만+ 콜/일 | 1 (G-27) | ⚠️ | G-27(KoreaTechToday) 403 오류. 검증 불가 |
| AI 콜당 $0.40 vs 인간 $7~12 (90~95% 절감) | 1 (G-26) | ❌ | G-26 페이지에 해당 수치 없음. "up to 90% reduction"만 있음 |
| 기업 80% AI 음성 2026년 통합 | 1 (G-26) | ❌ | G-26 페이지에 없음. "82% of companies expect AI to increase voice call traffic"는 존재하나 내용 다름 |
| Retell AI ARR $40M+ | 1 (G-25) | ❌ | G-25 페이지에 없음. Retell AI ARR 출처 불명 |

---

## 보강 필요 항목 (reinforcement_needed)

```yaml
reinforcement_needed:
  - claim: "ElevenLabs Series D $500M, $11B 밸류에이션"
    current_sources: 0 (G-11은 Deepgram Series C 기사)
    suggested_keywords: ["ElevenLabs Series D funding $500M", "ElevenLabs valuation $11B 2026"]

  - claim: "xAI Grok Voice Agent API $0.05/min"
    current_sources: 1 (G-04 가격 정보 없음, G-03 접근 불가)
    suggested_keywords: ["xAI Grok Voice Agent API pricing 0.05 per minute", "xAI audio API pricing"]

  - claim: "Deepgram Flux EOT ~260ms"
    current_sources: 0 (G-24에 260ms 없음)
    suggested_keywords: ["Deepgram Flux end of turn latency milliseconds", "Deepgram Flux CSR latency"]

  - claim: "AssemblyAI Universal-3 Pro Streaming ~150ms P50, WER 8.14%"
    current_sources: 0 (G-21 URL 귀속 오류)
    suggested_keywords: ["AssemblyAI Universal-3 Pro Streaming 150ms endpointing", "AssemblyAI Universal-3 WER 8.14"]

  - claim: "LiveKit 턴 감지 3계층, ~25ms 추론, ~400MB RAM, 14개 언어"
    current_sources: 0 (G-22에 해당 수치 없음)
    suggested_keywords: ["LiveKit turn detection 25ms inference model", "LiveKit Qwen2.5 knowledge distillation"]

  - claim: "SoundHound 2025년 통신·유통 3천만 건 AI 인터랙션"
    current_sources: 0 (G-23/E-05 보도자료에 없음)
    suggested_keywords: ["SoundHound 30 million AI interactions telecom 2025"]

  - claim: "PMC 개선 가이드라인 적용 시 실세계 정확도 57% 향상"
    current_sources: 0 (P-02에 수치 없음)
    suggested_keywords: ["audio deepfake detection real-world accuracy improvement 57%"]

  - claim: "콜당 비용 AI $0.40 vs 인간 $7~12"
    current_sources: 0 (G-26에 해당 수치 없음)
    suggested_keywords: ["AI call center cost per call $0.40 versus human agent cost"]

  - claim: "기업 80%가 2026년까지 AI 음성 기술 고객 서비스 통합 계획"
    current_sources: 0 (G-26 수치 다름)
    suggested_keywords: ["80% enterprises voice AI customer service 2026 integration"]

  - claim: "Retell AI ARR $40M+"
    current_sources: 0 (G-25에 없음)
    suggested_keywords: ["Retell AI ARR $40 million annual recurring revenue"]
```

---

## 5. URL-Content 검증

| # | URL 상태 | 본문 주장 | 판정 | 비고 |
|---|---------|---------|------|------|
| G-01 | 200 OK | Voxtral TTFA 90ms | ❌ 불일치 | 실제: 70ms ("70ms for a typical input voice sample of 10 seconds"). 리포트 90ms는 오기입 |
| G-01 | 200 OK | ElevenLabs 68.4% 승률 | ⚠️ 부분 일치 | G-01 페이지 미기재. P-01(arXiv)에서 확인됨 |
| G-02 | 200 OK (CSS only) | Voxtral 기술 내용 | ⚠️ 접근 제한 | TechCrunch 기사 본문 미로드. 메타데이터만 확인 |
| G-03 | 403 접근 불가 | xAI Grok Voice Agent API 공식 발표 | 🔗 접근 불가 | |
| G-04 | 200 OK | xAI $0.05/min, LiveKit 플러그인 | ⚠️ 부분 일치 | LiveKit 통합 ✅, 가격 정보 없음 ❌. 대안: xAI 가격 페이지 확인 필요 |
| G-05 | 200 OK | ElevenLabs-IBM 파트너십 (10,000+ 음성, 70언어, PCI/HIPAA) | ✅ 일치 | 모든 주요 항목 확인 |
| G-06 | 200 OK | Deepgram IBM watsonx 첫 전용 음성 파트너 | ✅ 일치 | "IBM's first voice partner" 확인 |
| G-07 | 200 OK | Amazon Polly Gen TTS 10개 음성 GA + Bidirectional Streaming | ✅ 일치 | 모든 항목 확인 |
| G-08 | 200 OK (CSS only) | ElevenLabs v3 GA, 오류율 15.3%→4.9% | ⚠️ 접근 제한 | Tailwind CSS만 반환. 내용 검증 불가 |
| G-09 | 200 OK (CSS only) | Gemini 2.5 Flash/Pro TTS 가격 $20/$10/1M tokens | ⚠️ 부분 일치 | Flash/Pro 이중화 ✅, 가격 정보 미확인 |
| G-10 | 200 OK | gpt-4o-mini-tts WER 35%, Custom Voices 확대 | ✅ 일치 | 모든 항목 확인 |
| G-11 | 200 OK | ElevenLabs $500M Series D $11B 밸류 | ❌ 불일치 | G-11은 Deepgram 기사. ElevenLabs 언급 없음. 별도 출처 필요 |
| G-12 | 200 OK | TTS 시장 $4.36B→$7.92B (CAGR 12.66%) | ✅ 일치 | Mordor Intelligence 직접 확인 |
| G-13 | 200 OK | Voice AI 2024년 $2.4B → 2034년 $47.5B (CAGR 34.8%) | ⚠️ 부분 일치 | 2034년 $47.5B ✅, CAGR 34.8% ✅, **2024년 시작값 $3.14B (리포트 $2.4B 불일치)** |
| G-14 | 200 OK | 딥페이크 공격 비용 $10,000 미만, Arup $2,500만 | ⚠️ 부분 일치 | $2,500만 사건 ✅, 공격 비용 "$10,000 미만" 수치 없음(G-14에는 "$2 미만" 언급). Arup 귀속 없음 |
| G-15 | 403 접근 불가 | $2,500만 딥페이크 사건 | 🔗 접근 불가 | |
| G-16 | timeout | McAfee 90%→96% 정확도 | 🔗 접근 불가 | 타임아웃 |
| G-17 | 200 OK | EU AI Act Article 50 2026-08-02 발효, 매출 7% 과징금 | ⚠️ 부분 일치 | 시행일 ✅, 5-6월 확정 ✅, **다층 워터마킹 의무화 ❌, 매출 7%/EUR 1,500만 과징금 ❌** (페이지에 과징금 미기재) |
| G-18 | timeout | Hiya 미국인 25% 딥페이크 통화, 사기범 2:1 | 🔗 접근 불가 | 타임아웃 |
| G-19 | 200 OK | Resemble AI DETECT-2B 94~98% 정확도, PerTh 워터마킹 | ⚠️ 부분 일치 | DETECT-2B ✅, **정확도 수치 미확인**, PerTh 미확인 |
| G-20 | 200 OK | 보이스 클로닝 시장 2032년 $162억 (CAGR 27.3%) | ✅ 일치 | 모든 항목 확인 |
| G-21 | 200 OK | AssemblyAI Universal-3 Pro Streaming ~150ms P50, WER 8.14% | ❌ 불일치 | 페이지는 2025-10-22 기사로 Universal-2/Slam 발표. Universal-3 Pro Streaming은 링크로만 존재. 실제 Universal-3 Pro Streaming 기사 URL이 아님. 대안: assemblyai.com/blog/introducing-universal-3-pro-streaming (404 오류 확인됨) |
| G-22 | 200 OK | LiveKit 턴 감지 3계층, ~25ms 추론, ~400MB RAM, 14개 언어 | ❌ 불일치 | 페이지에 해당 수치 전혀 없음. 실제: 4가지 전략 개념 설명만 있음. Qwen2.5 언급 없음 |
| G-23 | 200 OK | SoundHound Aragon 리더 선정(3/26) | ✅ 일치 | 날짜 포함 확인 |
| G-24 | 200 OK | Deepgram Flux EOT ~260ms | ❌ 불일치 | 260ms 수치 없음. 실제: p90 latency 1s, p95 1.5s. "200~600ms 개선치"를 절대값으로 오해한 것으로 추정 |
| G-25 | 200 OK | Retell AI ARR $40M+, ~600ms 레이턴시, Slider 0~1 | ❌ 불일치 | 세 항목 모두 페이지에 없음. ARR 출처 불명 |
| G-26 | 200 OK | AI $0.40/call vs 인간 $7~12, 기업 80% 통합 계획 | ❌ 불일치 | 두 수치 모두 페이지에 없음 (82% 수치는 다른 의미) |
| G-27 | 403 접근 불가 | KT GiGA Genie 10만+ 콜/일, Agentic Fabric | 🔗 접근 불가 | |
| G-28 | 200 OK | NVIDIA PersonaPlex-7B ICASSP 2026, 턴테이킹 0.170~0.265s | ⚠️ 부분 일치 | 모델명 ✅, 상세 수치는 CSS/코드만 반환으로 미확인 |
| G-29 | 403 접근 불가 | SKT "1인 1 AI 에이전트" MWC 2026 | 🔗 접근 불가 | G-29 403 오류. G-27(KoreaTechToday)에서 우회 시도했으나 "1인 1 AI 에이전트" 표현 미확인 |
| G-30 | 429 (Rate limit) | (본문 미인용 — 고아 소스) | — | G-30 본문 인용 없음 |
| P-01 | 200 OK | Voxtral 하이브리드 아키텍처, ElevenLabs 68.4% 승률 | ✅ 일치 | arXiv 논문 직접 확인. "auto-regressive semantic tokens + flow-matching acoustic tokens" ✅ |
| P-02 | 200 OK | PMC 실세계 정확도 57% 향상, 전화 채널 성능 급락 | ⚠️ 부분 일치 | 일반화 실패 문제 제기 ✅, **57% 향상 수치 없음 ❌**, 전화 채널 성능 급락 직접 언급 없음 |
| P-03 | 303 리다이렉트 | Hybrid CNN+LSTM+GRU 딥페이크 탐지 | 🔗 접근 불가 | Springer 페이지 리다이렉트. 내용 검증 불가 |
| P-04 | 200 OK | SID-Bench, ICME 2026, APT 지표 | ⚠️ 부분 일치 | SID-Bench ✅, ICME 2026 ✅, APT ✅, **저자 "Alibaba Qwen 팀" 미확인** (저자: Kangxiang Xia, Bingshen Mu, Xian Shi, Jin Xu, Lei Xie) |
| P-05 | 200 OK | τ-Voice Full-Duplex Benchmark, 2026-03-14 제출 | ✅ 일치 | 모든 항목 확인. 저자: Soham Ray et al. |
| E-01 | 200 OK | SKT 에이닷 오토 르노코리아 탑재, 날짜 3/14 | ❌ 불일치 | 내용 ✅, **날짜 오기입: 실제 보도자료는 2026-01-14 발표 (1월). 리포트에 3/14로 기재** |
| E-02 | 200 OK | Pindrop Fraud Assist, FNBO 수치, $400억 | ✅ 일치 | 모든 항목 확인 |
| E-03 | 402 접근 불가 | xAI Grok Voice Agent API OpenAI Realtime 호환 | 🔗 접근 불가 | x.com 402 오류 |
| E-04 | 200 OK (G-05와 동일) | IBM 콜센터 비용 40% 절감 | ❌ 불일치 | G-05/E-04 동일 URL. 해당 수치 없음 |
| E-05 | 200 OK | SoundHound 3천만 건 AI 인터랙션 | ❌ 불일치 | 공식 보도자료에 "3천만 건" 없음. "billions of AI interactions each year" 표현만 있음 |

---

## 3. 논리 검증

- **Deepgram Flux EOT ~260ms 해석 오류**: G-24에서 "200~600ms 개선치(comparative)"를 Flux의 절대 EOT 레이턴시로 해석한 것으로 보임. 실제 p90은 1초로 전혀 다른 스케일.
- **E-01 날짜 오기입**: SKT 에이닷 오토 발표를 "3/14"로 기재했으나 실제는 1/14. "이전 대비 변화" 섹션에서 "전주: Pindrop-Zoom 탐지 통합. UN·INTERPOL 경고" 다음에 이번 주 변화로 서술했는데, 1월 발표를 3월 이번 주 소식으로 분류한 논리적 오류.
- **Voice AI 시장 시작점 불일치**: 동일 출처(G-13)를 두 곳에서 다른 맥락으로 인용. "2024년 $2.4B" (Voice Synthesis 섹션 111행)과 "2026년 $22.5B" (Interrupt 섹션 273행)이 서로 다른 기준을 사용했으나 일관성 없음. G-13 실제 수치는 2024년 $3.14B.
- **IBM 콜센터 40% 절감**: E-04가 G-05와 동일 URL임에도 독립 출처처럼 인용. E-04 귀속 주장(IBM 도입 후 40% 절감)이 해당 URL에 없음 — 출처 귀속 오류.
- **전반적 논리 일관성**: 오픈웨이트 TTS의 양면성(기회/위협), 엔터프라이즈 플랫폼 통합 가속, 턴테이킹 분기점 등 핵심 분석 프레임은 논리적으로 일관됨.

---

## 4. 편향 검증

- **긍정/부정 균형**: Voice Synthesis의 기회(비용 절감)와 위협(딥페이크, 라이선스 제약)을 균형 있게 다루고 있음. PASS
- **경쟁사 분석**: SKT와 KT 동향을 별도 섹션에서 명시했으나 "자체 턴테이킹 기술 역량은 미확인"으로 공정하게 서술. PASS
- **기술 리스크**: 탐지-생성 군비 경쟁, S2S 아키텍처 추론 저하 트레이드오프, 벤치마크 리터러시 부재 등 균형적 위협 분석. PASS
- **시장 조사 출처**: G-13(VoiceAIWrapper, [C] 등급)에 "추가확인 필요" 태그 부여 — 적절한 신뢰도 관리. PASS

---

## 6. Critical 이슈 요약

### Critical-1: Voxtral TTFA 90ms → 실제 70ms
- **위치**: 63행, 87행 플레이어 동향 테이블
- **근거**: G-01 원문 "70ms for a typical input voice sample of 10 seconds"
- **수정 제안**: "TTFA 90ms" → "TTFA 70ms (10초 입력 기준)"

### Critical-2: Voice AI 시장 시작점 $2.4B → 실제 $3.14B
- **위치**: 111행 "Voice AI 에이전트 시장: 2024년 $2.4B → 2034년 $47.5B(CAGR 34.8%)"
- **근거**: G-13(VoiceAIWrapper) 실제 수치 "2024년 $3.14B"
- **수정 제안**: "$2.4B" → "$3.14B"

### Critical-3: E-01 날짜 3/14 → 실제 1/14 (1월 발표)
- **위치**: 95행, 107행, 333행 경쟁사 섹션
- **근거**: SKT 뉴스룸 보도자료 날짜 2026-01-14
- **수정 제안**: 날짜 "3/14" → "1/14"로 수정. 리포트 내 "금주 신규 진입"으로 분류된 것도 재검토 필요 (1월 발표를 W14 신규로 분류하는 것은 오류)

---

## 결론

본 리포트는 전반적으로 잘 구조화된 주간 모니터 형식을 따르고 있으며, 인용 커버리지도 높다. 그러나 검증 과정에서 Critical 3건, Minor 6건의 이슈가 확인되었다. 특히 Voxtral TTFA 수치 오기입(90ms→70ms), Voice AI 시장 시작점 불일치($2.4B→$3.14B), SKT 에이닷 오토 날짜 오기입(3/14→1/14)은 팩트 오류에 해당한다. AssemblyAI Universal-3 Pro Streaming의 URL 귀속 오류(G-21이 다른 기사를 가리킴)와 LiveKit/Famulor/Retell AI의 구체 수치들이 원본 URL에서 확인되지 않는 점도 수정이 필요하다. 고아 소스 G-30은 삭제하거나 본문에 인용을 추가해야 한다.
