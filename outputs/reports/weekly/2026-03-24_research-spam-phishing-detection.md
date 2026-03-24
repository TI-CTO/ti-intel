---
type: research-deep
topic: spam-phishing-detection
date: 2026-03-24
parent: 2026-03-24_weekly-secure-ai.md
---

# Deep 리서치: 스팸/피싱 감지(통화전) — 2026-W13

## 이전 대비 변화

- **전주**: P1 Vishing-as-a-Service($399/월) 실체 노출, Microsoft Teams Brand Impersonation Protection 배포, Meta 전 플랫폼 AI 사기 탐지 출시, KT 2.0 상용화
- **금주**: SKT 에이닷 '위험 목소리 탐지' 성문 분석 추가(3/18), FCC SIP 603+ 의무화 마감(3/25), Adaptive Security $81M Series B(NVIDIA·Bain), 온디바이스 AI 탐지 통신3사+삼성 전면 확산
- **변화 방향**: 탐지 기술이 텍스트→성문(voice-print) 레이어로 확장. 규제(FCC 603+)가 analytics-based blocking을 제도화. AI 딥페이크 방어 시장에 대형 VC 자금 유입 가속

## 기술 동향

1. **SKT 에이닷 '위험 목소리 탐지' — 온디바이스 성문 분석 추가 (3/18).**
   기존 텍스트 기반 통화 분석에 국과수(NFS) 보이스피싱 범죄자 성문 데이터와의 유사도 비교를 추가. 온디바이스 AI로 통화 데이터를 외부 전송 없이 단말 내 처리. 탐지 정확도 96%. ICT 규제 샌드박스 실증특례 승인으로 성문 민감정보 활용 근거 확보. [[G-01]](#ref-g-01), [[G-02]](#ref-g-02)

2. **FCC SIP 603+ 의무화 마감 — 2026년 3월 25일.**
   미국 FCC Eighth Report and Order에 따라 모든 통신사의 analytics-based call blocking이 SIP 603+("Network Blocked") 코드를 반드시 사용해야 함. 기존 603/607/608 코드는 폐지. STIR/SHAKEN과 결합된 분석 기반 차단 투명성 제도화. 미국 STIR/SHAKEN 서명 트래픽 85% 달성했으나, 비Tier-1 사업자의 서명률은 21%로 격차 존재. [[G-03]](#ref-g-03), [[G-04]](#ref-g-04)

3. **Adaptive Security $81M Series B — NVIDIA·OpenAI·a16z 투자.**
   Bain Capital Ventures 주도, NVentures(NVIDIA), OpenAI Startup Fund, a16z, Citi Ventures, Capital One Ventures 참여. 누적 $146.5M. 500+ 엔터프라이즈 고객(PayPal, Bose, NHL, Xerox). AI 기반 딥페이크 음성·영상·문자 시뮬레이션으로 직원 교육. 딥페이크 사고 17x 증가(2023→2024). [[G-05]](#ref-g-05), [[G-06]](#ref-g-06)

4. **삼성전자·통신3사 온디바이스 보이스피싱 탐지 전면 확산.**
   삼성 Galaxy 본 전화앱 + SKT 에이닷 + KT 후후 + LGU+ 익시오(ixi-O)에서 온디바이스 AI 실시간 통화 분석 제공. 통화 데이터 외부 전송 없이 기기 내 처리. 과기정통부 'AI 기반 보이스피싱 공동 대응 플랫폼' 2026년 구축 착수. [[G-07]](#ref-g-07), [[G-08]](#ref-g-08)

5. **딥페이크 음성 위협 지표 악화 — 미국인 25% 수신 경험.**
   Hiya State of Call 2026: 미국인 1/4이 AI 생성 딥페이크 음성 통화 수신. 주당 9.9건 원치 않는 통화(+16% CAGR). 소비자 38%가 이통사 교체 의향. 딥페이크 비싱 2025 Q1에 1,600% 급증. 음성 복제에 3초 오디오면 충분. [[G-09]](#ref-g-09)

## 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| SKT | 에이닷 '위험 목소리 탐지' 3/18 출시. 국과수 성문DB+텍스트 분석 이중 체계. 정확도 96%. 규제 샌드박스 승인 | [[G-01]](#ref-g-01) |
| Samsung | Galaxy 본 전화앱에 온디바이스 AI 보이스피싱 탐지 내장. 통신3사와 협력 | [[G-07]](#ref-g-07) |
| Adaptive Security | $81M Series B (NVIDIA·Bain·OpenAI). 500+ 기업 고객. 딥페이크 시뮬레이션 플랫폼 | [[G-05]](#ref-g-05) |
| FCC (미국) | SIP 603+ 의무화 3/25 시행. Analytics-based blocking 투명성 제도화 | [[G-03]](#ref-g-03) |
| 과기정통부 (한국) | AI 보이스피싱 공동 대응 플랫폼 2026년 구축 착수 | [[G-08]](#ref-g-08) |

## 시장 시그널

**투자 & M&A**
- Adaptive Security $81M Series B (Bain·NVIDIA·OpenAI·a16z). 누적 $146.5M. AI 딥페이크 방어 시장 최대 규모 투자 중 하나 [[G-05]](#ref-g-05)

**시장 전망**
- 딥페이크 기반 사기 2027년 $40B 피해 전망 (FTC 2024년 미국 사기 피해 $12.5B) [[G-09]](#ref-g-09)
- 딥페이크 비싱 2025 Q1에 전분기 대비 1,600% 급증 (미국) [[G-09]](#ref-g-09)

**도입 사례**
- SKT 에이닷: 온디바이스 성문 분석 상용 서비스 — 통신사 최초 성문DB 기반 실시간 탐지 [[G-01]](#ref-g-01)
- FCC SIP 603+: 미국 전 통신사 analytics-based blocking 투명성 의무화 (3/25) [[G-03]](#ref-g-03)

## 시장 수요 (voice-of-market)

이번 주 해당 기술 관련 컨퍼런스 영상에서 수요 시그널을 확인하지 못함.

## 전략적 시사점

**기회**
- SKT 성문DB 기반 탐지가 ICT 규제 샌드박스 승인 선례 — 유사 기술 도입 시 규제 경로가 열린 상태
- FCC SIP 603+ 의무화는 analytics-based blocking의 글로벌 참조 모델 — 한국 통신 규제에도 유사 제도화 가능성
- 온디바이스 AI 탐지의 통신3사+삼성 전면 확산으로 "통화 보안"이 기본 기능으로 자리잡기 시작

**위협**
- Adaptive Security 등 SaaS 플랫폼이 기업 단위 딥페이크 방어를 직접 제공 — 통신사 부가서비스와 경쟁
- 딥페이크 음성 복제 진입장벽 극히 낮음(3초 오디오) — 공격 도구 진화 속도가 탐지 기술을 초과할 위험 지속

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | 전자신문 — SKT 에이닷 '위험 목소리 탐지' 적용 | [링크](https://www.etnews.com/20260318000294) | news | 2026-03-18 | [B] |
| <a id="ref-g-02"></a>G-02 | 뉴시스 — "검찰입니다" 그놈 말투 알아채는 AI | [링크](https://www.newsis.com/view/NISX20260318_0003553437) | news | 2026-03-18 | [B] |
| <a id="ref-g-03"></a>G-03 | ACA International — FCC Call Blocking Redress: Final Compliance Deadline March 25 | [링크](https://www.acainternational.org/news/fcc-call-blocking-redress-final-compliance-deadline-is-march-25/) | news | 2026-03 | [B] |
| <a id="ref-g-04"></a>G-04 | TNS — 2026 Robocall Report: Going Further Than STIR/SHAKEN | [링크](https://tnsi.com/resource/com/tns-2026-robocall-report-going-further-than-stir-shaken-blog/) | report | 2026 | [B] |
| <a id="ref-g-05"></a>G-05 | PR Newswire — Adaptive Security $81M Series B | [링크](https://www.prnewswire.com/news-releases/adaptive-security-raises-81-million-series-b-to-stop-ai-powered-cyber-threats-302643174.html) | 보도자료 | 2026-01 | [A] |
| <a id="ref-g-06"></a>G-06 | BankInfoSecurity — Adaptive Security AI Deepfake Defense | [링크](https://www.bankinfosecurity.com/adaptive-security-gets-81m-series-b-for-ai-deepfake-defense-a-30332) | news | 2026-01 | [B] |
| <a id="ref-g-07"></a>G-07 | HelloT — 통신3사·삼성전자 온디바이스 탐지 서비스 활성화 | [링크](https://www.hellot.net/news/article.html?no=110341) | news | 2026-02 | [B] |
| <a id="ref-g-08"></a>G-08 | 정책브리핑 — AI로 통화 중 보이스피싱 잡는다 | [링크](https://www.korea.kr/news/policyNewsView.do?newsId=148959497) | 공식 | 2026-03 | [A] |
| <a id="ref-g-09"></a>G-09 | Hiya / NatLawReview — State of the Call 2026 | [링크](https://natlawreview.com/press-releases/state-call-2026-ai-deepfake-voice-calls-hit-1-4-americans-consumers-say) | report | 2026-03-02 | [B] |
