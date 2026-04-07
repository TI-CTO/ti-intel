---
type: research-deep
topic: spam-phishing-detection
date: 2026-04-06
parent: 2026-04-06_weekly-secure-ai.md
period: 2026-03-30 ~ 2026-04-06
agent: research-deep
confidence: medium-high
status: completed
sources_used: [websearch, webfetch]
---

# Deep Research: 스팸/피싱 감지(통화전) — 2026-W15

## 이전 대비 변화

- **전주 (W13)**: SKT 에이닷 '위험 목소리 탐지' 성문 분석 추가(3/18), FCC SIP 603+ 의무화 마감(3/25), Adaptive Security $81M Series B(NVIDIA·Bain·OpenAI), 온디바이스 AI 탐지 통신3사+삼성 전면 확산
- **금주 (W15)**: INTERPOL-UNODC 글로벌 사기 정상회담(비엔나, 3/16–17) 결과 공개 — $442B 글로벌 손실·"사기의 산업화" 선언; 미국 금융권(ABA·Better Identity Coalition·FSCC) 연방 정책 20개 권고안 발표(4/1); Experian·Security Boulevard가 '에이전트형 AI 사기(Agentic Fraud)'를 2026 최대 신규 위협으로 공식화
- **변화 방향**: ① 규제 프레임이 산업 자율 대응에서 국제 공조·정부 입법으로 격상. ② 공격 주체가 단순 딥페이크 음성 사용에서 완전 자율 AI 에이전트로 진화. ③ 방어 측도 RAG 기반 실시간 통화 정책 검증, Pindrop Pulse 2초 탐지 등 기술 고도화 진행 중

---

## 기술 동향

1. **Agentic AI 사기 — 완전 자율화 공격 벡터 공식화 (3월 말~4월 초)**
   Experian 2026 사기 예측 보고서(1/13)와 Security Boulevard(3월 말)가 '에이전트형 AI 사기'를 독립 위협 범주로 명명했다 [[G-01]](#ref-g-01), [[G-02]](#ref-g-02). 7개 공격 벡터가 연구 개념에서 실제 운용 단계로 전환: 신원 팜(Identity Farm)이 AI 에이전트로 800점대 신용점수를 프로그래매틱하게 생성하고, 기계 간(M2M) 고속 사기 트랜잭션을 실행한다. Sardine AI 분석에 따르면 이 공격들은 현재 은행·핀테크·크립토 파트너 전반에서 실손해를 발생시키고 있다.

2. **RAG 기반 실시간 통화 정책 검증 (arxiv 2025-01)**
   Singh et al.이 제안한 "Advanced Real-Time Fraud Detection Using RAG-Based LLMs"은 통화를 실시간 전사 후 Retrieval-Augmented Generation (RAG)으로 발신자의 개인정보 요청 여부를 정책 문서와 대조 검증한다 [[P-01]](#ref-p-01). 정확도 97.98%, F1 97.44%(100개 합성 통화). 모델 재학습 없이 정책 업데이트 가능하다는 점이 기존 ML 탐지기 대비 핵심 차별점이다.

3. **인간의 AI 음성 구분 능력 — 우연 수준 이하 확인 (arxiv 2026-02 제출)**
   Bhatti et al.의 실험 연구 [[P-02]](#ref-p-02) [철회 상태, 참고용]에서 22명 참가자가 AI 생성·인간 음성 16개 클립을 분류한 결과 평균 정확도 37.5%로 이진 분류 우연 수준(50%) 이하 기록. AI 생성 클립의 75%가 인간으로 오분류. 피싱 방어 마지막 선인 '인간 판단'이 실질적으로 붕괴했음을 시사한다.

4. **Agentic AI 접근법 보이스피싱 탐지 (IEEE 2026)**
   IEEE 2026에 게재된 "Efficient Voice Phishing Detection using the Agentic AI Approach"는 자율 학습·적응형 의사결정 에이전트로 실시간 진화하는 공격에 대응하는 탐지 프레임워크를 제안한다 [[P-03]](#ref-p-03). 공격에서 쓰이는 에이전트형 AI를 방어에도 동일하게 적용하는 대칭 접근이 특징이다.

5. **Pindrop Pulse — 2초 음성에서 99% 딥페이크 탐지**
   Pindrop의 컨택센터 특화 음성 딥페이크 탐지 솔루션 Pindrop Pulse는 2초 발화로 알려진 딥페이크 엔진 99% 탐지, 미탐지 엔진에도 90% 이상 탐지율을 달성하며 오탐율 1% 미만을 유지한다 [[G-03]](#ref-g-03). 370개 이상 TTS(Text-to-Speech) 시스템 데이터 기반, 2,000만+ 오디오 파일 학습.

6. **SKT AI 필터링 — 연간 11억 건 차단, 전년 대비 35% 증가 (2026-01-13 발표)**
   SK Telecom이 발표한 2025년 연간 실적에 따르면 AI 기반 보이스피싱·음성 스팸·사기 문자 메시지 차단 건수가 약 11억 건으로 전년 대비 35% 증가했다 [[G-04]](#ref-g-04). 통화 패턴 분석으로 의심 번호 사전 식별 시스템 포함. 기준 기간이 이번 주 범위 외이지만, 금주 telecom 보도에서 재인용되어 현황 지표로 활용된다.

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| INTERPOL / UNODC | 3/16–17 비엔나 글로벌 사기 정상회담 개최. $442B 손실 공식 발표, 47개국 행동 계획 서명. AI 사기 4.5x 수익성 주요 의제 | [[G-05]](#ref-g-05), [[G-06]](#ref-g-06) |
| ABA / Better Identity Coalition / FSCC | 4/1 공동 정책 문서 발표. 연방·주 차원 20개 권고안: 딥페이크 대응, FIDO 패스키 의무화, 디지털 여권, IRS/USPS 신원 검증 강화. 130명 이상 전문가 18개월 작업 | [[G-07]](#ref-g-07) |
| SKT | 에이닷 '위험 목소리 탐지' + 2025년 11억 건 차단(+35% YoY). 통화 패턴 분석·성문DB 이중 체계 운용 | [[G-04]](#ref-g-04) |
| KT | '후후' 앱 실시간 보이스피싱 탐지: 문맥 탐지+화자 인식+딥보이스 감지 삼중 체계. 2025년 4,680만 건 처리 중 3,000건 차단. 탐지 정확도 Q1 90.3% → Q4 97.2% 향상 | [[G-08]](#ref-g-08) |
| AT&T | 자율 AI 에이전트 배포로 사기 탐지·네트워크 이상 관리. 실시간 네트워크 데이터 분석으로 의심 활동 식별 속도 향상 | [[G-09]](#ref-g-09) |
| Pindrop | Pulse: 2초 탐지, 99% 알려진 딥페이크 엔진 탐지율. 370+ TTS 시스템 대상. Gartner가 2026년까지 30% 기업이 단독 신원 검증 신뢰성 저하 전망 | [[G-03]](#ref-g-03) |
| McAfee | Deepfake Detector: 96% 정확도, 3초 내 탐지, NPU 온디바이스 처리. 단, PC 기반으로 통화 직접 탐지 미지원 [원문 미확인: "2026 업데이트" 세부 변경사항] | [[G-10]](#ref-g-10) |
| Protiviti | 3/27 블로그: "신뢰는 의도적으로 설계되어야" — 통신사에 AI 위험 소유권 명확화, 사기 방지 전략 통합 권고. MWC 2026에서 AI 사기를 통신사 최대 우려사항으로 지목 | [[G-11]](#ref-g-11) |

---

## 시장 시그널

**피해 규모**
- 글로벌 조직화 사기 손실: $442B (Global Anti-Scam Alliance, GASA 추정) [[G-05]](#ref-g-05)
- AI 기반 사기 손실(미국): 2023년 $12.3B → 2027년 $40B 전망 (CAGR 32%, Deloitte Center for Financial Services) [[G-07]](#ref-g-07)
- 딥페이크 비싱 사건당 평균 손실: 약 $600K, 10%+ 사건이 $1M 초과 (Regula Forensics, Group-IB 조사) [[G-12]](#ref-g-12) [추가확인 필요]
- 컨택센터 딥페이크 사기 노출 규모: 평균 $343K/센터 [[G-12]](#ref-g-12) [추가확인 필요]

**공격 지표 악화**
- 딥페이크 사고: 핀테크 부문 2022 대비 2023년 700% 증가 [[G-07]](#ref-g-07)
- Pindrop 분석: 2024년 딥페이크 활동 전년 대비 680% 증가; 소매 컨택센터 통화 127건 중 1건 사기 플래그 [[G-03]](#ref-g-03)
- AI 피싱 이메일 2026: 19초마다 1건, 클릭률 인간 작성 대비 4배 이상 [[G-13]](#ref-g-13)
- 의심활동보고(미국 FinCEN): 2021년 제출 건의 42%가 신원·인증 침해 연관 [[G-07]](#ref-g-07)
- 아직 미확인: AI 사기 4.5x 수익성 수치 원출처 (INTERPOL 보도 자료에는 미확인) [원문 미확인]

**규제·정책 움직임**
- INTERPOL-UNODC 47개국 공동 행동 계획 서명(3/16–17): AI 사기 국제 공조 가속 [[G-05]](#ref-g-05), [[G-06]](#ref-g-06)
- ABA·Better Identity Coalition 연방 정책 권고(4/1): 디지털 여권, FIDO 패스키 의무화, IRS/USPS 신원 검증 서비스 신설 [[G-07]](#ref-g-07)
- Gartner: 2026년까지 30% 기업이 단독 생체 인증 신뢰성 부족 전망 → 다중 요소 인증 압력 [[G-03]](#ref-g-03)

**기술 전환 신호**
- 통신사 방어 방식: 개별 통화 추적 → 네트워크 전체 조직화 활동 감지 패러다임으로 전환 [[G-09]](#ref-g-09)
- 한국 통신3사+경찰청 '긴급차단 시스템': 범죄 번호 10분 내 차단 [[G-08]](#ref-g-08)
- Virginia Tech 연구진: "디지털 쌍둥이(Digital Twin)" 환경으로 SIM 팜 조직화 패턴 학습 [[G-09]](#ref-g-09)

---

## 전략적 시사점

**기회**
- INTERPOL-UNODC 공조 프레임과 ABA 정책 권고가 국내 규제 설계 레퍼런스로 활용 가능 — FIDO 패스키·디지털 여권 정책 연계 검토 시점
- Agentic AI 사기 대응에 에이전트형 방어(IEEE 2026)를 선제 적용하는 통신사가 기술 차별화 포지셔닝 가능
- RAG 기반 실시간 정책 검증(Singh et al.)은 통화 중 컴플라이언스 확인에 재학습 없이 적용 가능 — 통신사 부가서비스 제품화 기회
- 한국 KT Q4 97.2% 탐지 정확도 달성: 기술 성숙도가 상용화 임계점 진입

**위협**
- 인간 판단 37.5% 정확도(Bhatti et al.) 확인 — 인간 2차 검증에 의존하는 탐지 체계의 근본적 한계 노출
- Agentic Fraud: 합성 신원이 800점대 신용점수를 자동 생성·유지 → 기존 신원 검증 체계 전면 무력화 위험
- LLM 피싱 자동화로 공격 비용 95% 절감 [[G-07]](#ref-g-07) — 사기 규모 급격 확대 압력
- Gartner: 단독 생체 인증 신뢰성 저하 시한 2026년 — 인증 인프라 재설계 압박 임박

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Security Boulevard — The Rise of Agentic Fraud: How AI Agents Are Reshaping Security | [링크](https://securityboulevard.com/2026/03/the-rise-of-agentic-fraud-how-ai-agents-are-reshaping-security/) | news | 2026-03 | [B] |
| <a id="ref-g-02"></a>G-02 | Experian — Fraud Forecast: Agentic AI-Driven Financial Fraud 2026 | [링크](https://www.experianplc.com/newsroom/press-releases/2026/experian-s-new-fraud-forecast-warns-agentic-ai--deepfake-job-can) | 보도자료 | 2026-01-13 | [A] |
| <a id="ref-g-03"></a>G-03 | Pindrop — Pindrop Pulse for Audio Deepfake Detection | [링크](https://www.pindrop.com/product/pindrop-pulse/) | 제품 | 2026 | [B] |
| <a id="ref-g-04"></a>G-04 | Telecompaper — SKT reveals rise in AI-driven blocking of spam and voice phishing attempts | [링크](https://www.telecompaper.com/news/skt-reveals-rise-in-ai-driven-blocking-of-spam-and-voice-phishing-attempts--1558993) | news | 2026-01-13 | [B] |
| <a id="ref-g-05"></a>G-05 | INTERPOL — INTERPOL-UNODC global summit ends with call to action against fraud surge | [링크](https://www.interpol.int/en/News-and-Events/News/2026/INTERPOL-UNODC-global-summit-ends-with-call-to-action-against-fraud-surge) | 공식 | 2026-03-17 | [A] |
| <a id="ref-g-06"></a>G-06 | UNODC — UNODC-INTERPOL global summit mobilizes action against fraud surge | [링크](https://www.unodc.org/unodc/en/press/releases/2026/March/unodc-interpol-global-summit-mobilizes-action-against-fraud-surge.html) | 공식 | 2026-03-17 | [A] |
| <a id="ref-g-07"></a>G-07 | Help Net Security — Financial groups lay out a plan to fight AI identity attacks | [링크](https://www.helpnetsecurity.com/2026/04/01/fight-ai-identity-fraud/) | news | 2026-04-01 | [B] |
| <a id="ref-g-08"></a>G-08 | Mobile World Live — KT trials voice phishing detection | [링크](https://www.mobileworldlive.com/asia-pacific/kt-trials-voice-phishing-detection/) | news | 2026 | [B] |
| <a id="ref-g-09"></a>G-09 | PYMNTS — AI Takes On the Spam Call Epidemic | [링크](https://www.pymnts.com/artificial-intelligence-2/2026/ai-takes-on-the-spam-call-epidemic/) | news | 2026 | [B] |
| <a id="ref-g-10"></a>G-10 | McAfee — Deepfake Detector: AI Audio and Video Detection | [링크](https://www.mcafee.com/ai/deepfake-detector/) | 제품 | 2026 | [B] |
| <a id="ref-g-11"></a>G-11 | Protiviti — Telco's Big Test: Engineering Trust in the AI Fraud Era | [링크](https://blog.protiviti.com/2026/03/27/telcos-big-test-engineering-trust-in-the-ai-fraud-era/) | 분석 | 2026-03-27 | [B] |
| <a id="ref-g-12"></a>G-12 | CX Today — Deepfake Voice Fraud is Fueling the Voice Trust Collapse | [링크](https://www.cxtoday.com/security-privacy-compliance/the-voice-trust-collapse-and-deepfake-voice-fraud/) | news | 2026 | [C] |
| <a id="ref-g-13"></a>G-13 | The European — AI Phishing Surge 2026: Attacks Rise 204% | [링크](https://the-european.eu/story-57325/ai-driven-phishing-surges-204-as-firms-face-a-malicious-email-every-19-seconds.html) | news | 2026 | [B] |
| <a id="ref-g-14"></a>G-14 | Sardine AI — AI-driven fraud vectors: 7 agentic attacks now live in 2026 | [링크](https://www.sardine.ai/blog/agentic-attacks) | blog | 2026 | [C] |
| <a id="ref-g-15"></a>G-15 | IBS Intelligence — Agentic AI to drive next wave of fraud in 2026 | [링크](https://ibsintelligence.com/ibsi-news/agentic-ai-to-drive-next-wave-of-fraud-in-2026/) | news | 2026 | [B] |
| <a id="ref-p-01"></a>P-01 | Singh et al. — Advanced Real-Time Fraud Detection Using RAG-Based LLMs (arxiv 2501.15290) | [링크](https://arxiv.org/abs/2501.15290) | paper | 2025-01-25 | [A] |
| <a id="ref-p-02"></a>P-02 | Bhatti et al. — Can You Tell It's AI? Human Perception of Synthetic Voices in Vishing Scenarios (arxiv 2602.20061) [철회] | [링크](https://arxiv.org/abs/2602.20061) | paper | 2026-02-23 | [C] |
| <a id="ref-p-03"></a>P-03 | IEEE 2026 — Efficient Voice Phishing Detection using the Agentic AI Approach | [링크](https://ieeexplore.ieee.org/document/11263515) | paper | 2026 | [A] |
