---
type: weekly-monitor
domain: secure-ai
week: 2026-W10
date: 2026-03-03
l3_count: 7
---

# 주간 기술 동향: Secure AI (W10)

## Executive Summary

| L3 | 변화 | 핵심 내용 |
|----|------|----------|
| 🔴 OnDevice sLM | urgent | Samsung Galaxy S26 (2nm, NPU +113%) 출시 + Qualcomm Wear Elite MWC 발표 |
| 🟡 실시간 화자분할 | notable | pyannote Community-1 SOTA 달성, NVIDIA Streaming Sortformer 실시간화 |
| 🔴 스팸피싱감지 | urgent | 삼성+통신3사 정부주도 AI 보이스피싱 공동 탐지 발표, KT 정확도 97.2% |
| 🟡 OCR 이미지 스팸 | notable | Google+Airtel RCS AI 스팸 필터 인도 배포, VBSF 시각 기반 탐지 제안 |
| 🔴 OnDevice 양자암호 | urgent | PQC "연구→의무" 전환 선언, CNSA 2027 데드라인, EU 로드맵 발표 |
| 🟡 OnDevice 동형암호 | notable | Niobium+SemiFive 세계 첫 FHE ASIC 착수 (Samsung 8nm), 시장 CAGR 20.2% |
| 🟡 Secure Vector Search | notable | CyborgDB 상용 암호화 벡터DB, ppRAG 거리보존 암호화 논문 |

---

## OnDevice AI

### a. OnDevice sLM

**기술 동향**

- **Samsung Galaxy S26** (2026-02-26 출시): 2nm GAA 엑시노스 2600 탑재, NPU 성능 전작 대비 +113%. 3B~7B SLM을 LoRA 어댑터로 기능별 hot-swap 실행. 클라우드 없이 온디바이스 개인화 AI 처리 시대 개막 — [Samsung Newsroom](https://news.samsung.com/global/samsung-unveils-galaxy-s26-series-the-most-intuitive-galaxy-ai-phone-yet)
- **Qualcomm Snapdragon Wear Elite** (MWC 2026, 2026-03-02): 웨어러블 최초 NPU 내장 칩, 2B 파라미터 온디바이스 처리. 차기 Galaxy Watch 탑재 확정 — [Business Standard](https://www.business-standard.com/technology/tech-news/qualcomm-unveils-snapdragon-wear-elite-chip-for-on-device-ai-on-wearables-126030200737_1.html)
- **Meta ExecuTorch 1.0 GA 이후**: Instagram, WhatsApp, Messenger, Facebook 4대 앱에 온디바이스 SLM 전면 배포, 수십억 사용자 서비스 중 — [Edge AI and Vision Alliance](https://www.edge-ai-vision.com/2026/01/on-device-llms-in-2026-what-changed-what-matters-whats-next/)
- 서브-1B 모델 생태계 성숙: Gemma 3 (270M), Phi-4 mini (3.8B), SmolLM2 (135M~1.7B), Qwen2.5 (0.5B~1.5B)

**플레이어 동향**

| 회사 | 동향 | 출처 |
|------|------|------|
| Samsung | Galaxy S26: 2nm NPU +113%, 3-7B SLM on-device, Gauss AI 스위트 | [Samsung Newsroom](https://news.samsung.com/global/samsung-unveils-galaxy-s26-series-the-most-intuitive-galaxy-ai-phone-yet) |
| Qualcomm | Snapdragon Wear Elite: 웨어러블 최초 NPU, 2B 파라미터 지원 | [Business Standard](https://www.business-standard.com/technology/tech-news/qualcomm-unveils-snapdragon-wear-elite-chip-for-on-device-ai-on-wearables-126030200737_1.html) |
| Meta | ExecuTorch 1.0 → 4대 앱 전면 배포 (수십억 사용자) | [Edge AI Vision](https://www.edge-ai-vision.com/2026/01/on-device-llms-in-2026-what-changed-what-matters-whats-next/) |
| Google | Gemma 3 (270M) 모바일 최적화 | [Samsung MWC 2026](https://telecomlead.com/telecom-equipment/samsung-showcases-galaxy-ai-intelligent-networks-and-next-gen-devices-at-mwc-2026-124895) |
| Microsoft | Phi-4 mini (3.8B) 엣지 배포 최적화 | [Edge AI Vision](https://www.edge-ai-vision.com/2026/01/on-device-llms-in-2026-what-changed-what-matters-whats-next/) |

**변화 수준**: 🔴 긴급 — Galaxy S26 출시로 온디바이스 SLM이 플래그십 기본 탑재. 웨어러블까지 확산 시작.

---

### b. 실시간 화자분할(2인)

**기술 동향**

- **pyannote Community-1** (pyannote.audio 4.0): 기존 3.1 대비 모든 지표에서 SOTA 달성. AMI(IHM) 기준 1시간 오디오를 31초에 처리. Speaker confusion 대폭 감소 — [pyannoteAI](https://www.pyannote.ai/blog/community-1)
- **NVIDIA Streaming Sortformer**: NeMo 기반 실시간 화자 식별 모델. 콜센터, 미팅, 보이스 앱용 생산급 스트리밍 추론 — [NVIDIA](https://developer.nvidia.com/blog/identify-speakers-in-meetings-calls-and-voice-apps-in-real-time-with-nvidia-streaming-sortformer/)
- **AssemblyAI 신규 모델**: 노이즈/원거리 환경 DER 29.1% → 20.4% (30% 개선) — [AssemblyAI](https://www.assemblyai.com/blog/speaker-diarization-update)
- **Mistral Voxtral Transcribe 2**: 오픈소스, 실시간 화자 분리 포함, 온디바이스 실행 가능 — [VentureBeat](https://venturebeat.com/technology/mistral-drops-voxtral-transcribe-2-an-open-source-speech-model-that-runs-on)
- 기술 방향: 파이프라인 → end-to-end 통합 모델 전환. 겹치는 발화 + 짧은 발화 처리 대폭 개선.

**플레이어 동향**

| 회사 | 동향 | 출처 |
|------|------|------|
| pyannoteAI | Community-1: SOTA 달성, 오픈소스, 31초/1시간 처리 | [pyannoteAI](https://www.pyannote.ai/blog/community-1) |
| NVIDIA | Streaming Sortformer: 실시간 콜센터용 GPU 워크로드 | [NVIDIA](https://developer.nvidia.com/blog/identify-speakers-in-meetings-calls-and-voice-apps-in-real-time-with-nvidia-streaming-sortformer/) |
| AssemblyAI | 노이즈 환경 DER 30% 개선, 엔터프라이즈 적용 40%+ | [AssemblyAI](https://www.assemblyai.com/blog/speaker-diarization-update) |
| Mistral AI | Voxtral Transcribe 2: 오픈소스 + 온디바이스 옵션 | [VentureBeat](https://venturebeat.com/technology/mistral-drops-voxtral-transcribe-2-an-open-source-speech-model-that-runs-on) |

**변화 수준**: 🟡 주목 — E2E 모델 성숙 + 오픈소스 SOTA로 통신 기기 내장 가능성 확대.

---

## 스팸/피싱/탐지

### a. 스팸피싱감지(통화전)

**기술 동향**

- **삼성전자 + SKT/KT/LG U+ 4사 공동 발표** (2026-02-12): 과학기술정보통신부 주도, 통화 중 AI 실시간 보이스피싱 탐지 서비스 공동 출시 — [StarNews Korea](https://www.starnewskorea.com/en/business-life/2026/02/12/2026021214210282736)
- **KT 'Who Who' 앱**: 2025년 4,680만 통화 중 3,000건 피싱 차단. 탐지 정확도 1년 만에 90.3% → 97.2% (+7%p). 문맥탐지 + 화자인식 + 딥보이스 탐지 3중 구조 — [The Fast Mode](https://www.thefastmode.com/technology-solutions/39153-kt-unveils-real-time-ai-voice-phishing-protection)
- **미국 딥페이크 피싱 급증**: 4명 중 1명이 딥페이크 음성 통화 수신. 스캠 피해 2040억달러 전망. 38%가 피해 시 통신사 변경 고려 — [MarTech Series](https://martechseries.com/predictive-ai/ai-platforms-machine-learning/state-of-the-call-2026-ai-deepfake-voice-calls-hit-1-in-4-americans-as-consumers-say-scammers-are-beating-mobile-network-operators-2-to-1/)
- **FBI 경고**: AI 음성 클로닝 피싱이 2027년까지 400억달러 손실 예상 — [BlackFog](https://www.blackfog.com/fbi-warning-ai-voice-phishing-how-to-stop-threat/)

**플레이어 동향**

| 회사 | 동향 | 출처 |
|------|------|------|
| Samsung | One UI 8.0+: 미등록 번호 "의심"/"경고" 2단계 알림 내장 | [StarNews](https://www.starnewskorea.com/en/business-life/2026/02/12/2026021214210282736) |
| SKT | 'Aida Phone' 앱: 통화 중 키워드·패턴 실시간 분석 + 팝업·진동 경보 | [Financial News](https://en.fnnews.com/news/202512011003132108) |
| KT | 'Who Who': 문맥+화자+딥보이스 3중 탐지, 정확도 97.2% | [The Fast Mode](https://www.thefastmode.com/technology-solutions/39153-kt-unveils-real-time-ai-voice-phishing-protection) |
| LG U+ | 'ixi-O': 대화 패턴 + Anti-Deep Voice + 범죄자 음성 매칭 | [StarNews](https://www.starnewskorea.com/en/business-life/2026/02/12/2026021214210282736) |

**변화 수준**: 🔴 긴급 — 한국 통신 4사 정부주도 공동 서비스 출시. 보이스피싱이 가입자 이탈 핵심 지표로 부상.

---

### b. OCR 이미지 스팸 차단

**기술 동향**

- **Google + Airtel 협력** (2026-03): RCS 채팅에 AI 스팸 필터 + 신원 확인 통합. 인도 배포. Airtel 네트워크 인텔리전스 + Google AI 결합 — [TechCrunch](https://techcrunch.com/2026/03/01/google-looks-to-tackle-longstanding-rcs-spam-in-india-but-not-alone/)
- **VBSF 논문** (arXiv 2512.23788): 화면 렌더링 방식으로 난독화 텍스트 이미지 스팸 탐지. OCR 우회 시도에 대응하는 시각적 렌더링 기반 아키텍처 — [arXiv](https://www.arxiv.org/pdf/2512.23788)
- RCS 고해상도 이미지/비디오 지원으로 이미지 스팸 공격 표면 확대. E2E 암호화 RCS는 필터 우회 구조적 취약점 존재

**플레이어 동향**

| 회사 | 동향 | 출처 |
|------|------|------|
| Google + Airtel | RCS AI 스팸 필터 인도 배포. 개인 발신자 스팸 시 쓰로틀링 | [Airtel PR](https://www.airtel.in/press-release/03-2026/airtel-and-google-collaborate-to-advance-spam-protection-in-india-with-secure-rcs-messaging/) |
| WhatsApp (Meta) | AI 이미지 인식 + 발신자 행동 분석 스팸 판정 | [MediaNama](https://www.medianama.com/2026/03/223-airtel-spam-detection-googles-rcs-messaging-india/) |
| Hiya | RCS 스캠 신흥 위협 보고서: 마이크로 스캠 유형 문서화 | [Hiya Blog](https://blog.hiya.com/emerging-text-based-threats-micro-scams-and-the-dawn-of-rcs-scams) |

**변화 수준**: 🟡 주목 — RCS 채널 확산에 따른 이미지 스팸 위협 증가. 통신사-플랫폼 협력 모델 등장.

---

## 양자동형암호

### a. OnDevice 양자암호

**기술 동향**

- **"양자 보안의 해 2026" 선언** (YQS2026): FBI/CISA/NIST 공동 지지. PQC가 실험에서 의무로 전환 — [GlobeNewswire](https://www.globenewswire.com/news-release/2026/02/23/3242432/28124/en/Post-Quantum-Cryptography-Industry-Research-Report-2026-PQC-Transitions-from-Research-Concept-to-Core-Cybersecurity-Pillar-Amid-Rising-Quantum-Computing-Breakthroughs.html)
- **Google PQC 정책 촉구** (2026-02-06): R&D에서 정부 정책 요구로 전환. Chrome에 X25519Kyber768 하이브리드 TLS 활성화 (Chrome 124). Cloud KMS PQC 키 타입 지원 — [The Meridiem](https://www.themeridiem.com/security/2026/2/6/google-shifts-post-quantum-encryption-from-r-d-to-government-policy-mandate)
- **NIST HQC 선정**: ML-KEM 백업용 5번째 PQC 표준. 2026년 초 초안 예정 — [Encryption Consulting](https://www.encryptionconsulting.com/decoding-nist-pqc-standards/)
- **CNSA 2.0**: 미국 국가안보 신규 시스템 2027년 1월까지 양자 안전 의무화 — [GrayGroup](https://www.graygroupintl.com/blog/post-quantum-cryptography-enterprise-guide/)
- **EU PQC 로드맵**: 조정된 구현 로드맵 발표 — [European Commission](https://digital-strategy.ec.europa.eu/en/library/coordinated-implementation-roadmap-transition-post-quantum-cryptography)
- **Apple Safari/iOS PQC 미지원**: 웹 전체 PQC 전환의 최대 병목으로 지목

**플레이어 동향**

| 회사/기관 | 동향 | 출처 |
|----------|------|------|
| NIST | ML-KEM/ML-DSA/SLH-DSA 3표준 확정 + HQC 5번째 표준 선정 | [NIST](https://www.encryptionconsulting.com/decoding-nist-pqc-standards/) |
| Google | Chrome X25519Kyber768 하이브리드 TLS, Cloud KMS PQC 지원 | [The Meridiem](https://www.themeridiem.com/security/2026/2/6/google-shifts-post-quantum-encryption-from-r-d-to-government-policy-mandate) |
| AWS/Azure | PQC 활성화 서비스 2026년 전면 배포 목표 | [GrayGroup](https://www.graygroupintl.com/blog/post-quantum-cryptography-enterprise-guide/) |
| Apple | Safari/iOS PQC cipher 미지원 — 최대 병목 | [GlobeNewswire](https://www.globenewswire.com/news-release/2026/02/23/3242432/28124/en/) |
| EU | 조정된 PQC 구현 로드맵 발표 | [EC](https://digital-strategy.ec.europa.eu/en/library/coordinated-implementation-roadmap-transition-post-quantum-cryptography) |

**변화 수준**: 🔴 긴급 — 규제 데드라인(CNSA 2027/01) 임박. 하이브리드 방식 배포 가속. 통신 인프라 교체 일정 수립 필요.

---

### b. OnDevice 동형암호

**기술 동향**

- **Niobium + SemiFive FHE ASIC** (2026-02-19): 세계 최초 상용 FHE 가속기 칩 개발 착수. Samsung Foundry 8nm (8LPU) 공정. 설계 수주 약 100억원 — [PR Newswire](https://www.prnewswire.com/news-releases/semifive-partners-with-niobium-to-develop-fhe-accelerator-driving-us-market-expansion-302692312.html)
- **Niobium 2,300만달러+ 후속 투자** (2025-12): 2세대 FHE 하드웨어 플랫폼 개발 — [The Quantum Insider](https://thequantuminsider.com/2025/12/03/niobium-23m-fhe-funding/)
- **FHE 시장 전망**: 2026년 2.51억달러 → 2035년 13.19억달러 (CAGR 20.2%), FHE가 48% 점유 — [360 Research](https://www.360researchreports.com/market-reports/homomorphic-encryption-market-206111)
- FHE.org 2026 컨퍼런스 개최 예정

**플레이어 동향**

| 회사 | 동향 | 출처 |
|------|------|------|
| Niobium (미국) | 세계 첫 상용 FHE ASIC. Samsung 8nm. 암호화 상태 AI 연산 목표 | [PR Newswire](https://www.prnewswire.com/news-releases/semifive-partners-with-niobium-to-develop-fhe-accelerator-driving-us-market-expansion-302692312.html) |
| SemiFive (한국) | 100억원 규모 FHE 가속기 설계 수주. 설계+패키징+테스트 통합 | [ITBrief](https://itbrief.asia/story/niobium-taps-samsung-for-encrypted-ai-chip-production) |
| Zama (프랑스) | Concrete-ML: 암호화 신경망 추론 벤치마크 | [FHE.org](https://fhe.org/conferences/conference-2026/) |
| Fhenix (이스라엘) | Ethereum 기반 FHE 기밀 DeFi 플랫폼 | [The Quantum Insider](https://thequantuminsider.com/2025/12/03/niobium-23m-fhe-funding/) |

**변화 수준**: 🟡 주목 — FHE ASIC 세계 최초 착수로 "상용화 직전" → "상용화 진입" 전환 시그널. 다만 ITU-T 150ms 기준 실시간 통신 적용은 여전히 도전적.

---

### c. Secure Vector Search

**기술 동향**

- **ppRAG 논문** (arXiv 2601.12331): 거리보존 암호화(CAPRISE)를 이용한 효율적 프라이버시 보존 RAG. 쿼리 임베딩 암호화 후 원격 유사도 검색 — [arXiv](https://arxiv.org/abs/2601.12331)
- **CyborgDB**: FIPS 준수 E2E 암호화 벡터 DB. 임베딩·메타데이터·콘텐츠 모두 암호화. 컨피덴셜 엔클레이브 내 쿼리. 지연 sub-10ms — [CyborgDB](https://www.cyborgdb.co/new)
- **IronCore Labs**: 속성 보존 암호화로 kNN/k-means 유지하면서 벡터 임베딩 보호. Qdrant 등 주요 벡터DB 통합 — [IronCore Labs](https://ironcorelabs.com/ai-encryption/)
- **임베딩 역변환 공격 위협 문서화**: RAG 임베딩에서 이름·주소·전화번호 복원 가능 (IACR ePrint 2026/105) — [IACR](https://eprint.iacr.org/2026/105.pdf)
- Apple ML Research: 동형암호 + ML을 Apple 생태계에 적용. Private Cloud Compute 연계 — [Apple](https://machinelearning.apple.com/research/homomorphic-encryption)

**플레이어 동향**

| 회사 | 동향 | 출처 |
|------|------|------|
| CyborgDB | E2E 암호화 벡터DB, FIPS 준수, sub-10ms | [CyborgDB](https://www.cyborgdb.co/new) |
| IronCore Labs | 속성 보존 암호화, Qdrant 통합 | [IronCore](https://ironcorelabs.com/ai-encryption/) |
| Apple | HE + ML Private Cloud Compute 연계 | [Apple ML](https://machinelearning.apple.com/research/homomorphic-encryption) |
| 학계 | ppRAG (거리보존), 임베딩 역변환 공격 문서화 | [arXiv](https://arxiv.org/abs/2601.12331) |

**변화 수준**: 🟡 주목 — RAG 임베딩 보안 위협이 학계에서 공식화. 상용 솔루션(CyborgDB, IronCore) 등장으로 AICC 파이프라인 암호화 현실화.

---

## References

| # | 출처명 | URL | 유형 | 날짜 |
|---|--------|-----|------|------|
| [1] | Samsung Galaxy S26 발표 | https://news.samsung.com/global/samsung-unveils-galaxy-s26-series-the-most-intuitive-galaxy-ai-phone-yet | news | 2026-02-26 |
| [2] | Qualcomm Snapdragon Wear Elite | https://www.business-standard.com/technology/tech-news/qualcomm-unveils-snapdragon-wear-elite-chip-for-on-device-ai-on-wearables-126030200737_1.html | news | 2026-03-02 |
| [3] | On-Device LLMs in 2026 | https://www.edge-ai-vision.com/2026/01/on-device-llms-in-2026-what-changed-what-matters-whats-next/ | analysis | 2026-01-28 |
| [4] | Samsung MWC 2026 | https://telecomlead.com/telecom-equipment/samsung-showcases-galaxy-ai-intelligent-networks-and-next-gen-devices-at-mwc-2026-124895 | news | 2026-03 |
| [5] | pyannote Community-1 | https://www.pyannote.ai/blog/community-1 | tech | 2026 |
| [6] | NVIDIA Streaming Sortformer | https://developer.nvidia.com/blog/identify-speakers-in-meetings-calls-and-voice-apps-in-real-time-with-nvidia-streaming-sortformer/ | tech | 2026 |
| [7] | AssemblyAI Speaker Diarization | https://www.assemblyai.com/blog/speaker-diarization-update | tech | 2026 |
| [8] | Mistral Voxtral Transcribe 2 | https://venturebeat.com/technology/mistral-drops-voxtral-transcribe-2-an-open-source-speech-model-that-runs-on | news | 2026 |
| [9] | 삼성+통신3사 보이스피싱 공동 대응 | https://www.starnewskorea.com/en/business-life/2026/02/12/2026021214210282736 | news | 2026-02-12 |
| [10] | KT Who Who 앱 정확도 97.2% | https://www.thefastmode.com/technology-solutions/39153-kt-unveils-real-time-ai-voice-phishing-protection | news | 2026 |
| [11] | State of the Call 2026 딥페이크 | https://martechseries.com/predictive-ai/ai-platforms-machine-learning/state-of-the-call-2026-ai-deepfake-voice-calls-hit-1-in-4-americans-as-consumers-say-scammers-are-beating-mobile-network-operators-2-to-1/ | report | 2026 |
| [12] | FBI AI 음성 피싱 경고 | https://www.blackfog.com/fbi-warning-ai-voice-phishing-how-to-stop-threat/ | news | 2026 |
| [13] | Google+Airtel RCS 스팸 필터 | https://techcrunch.com/2026/03/01/google-looks-to-tackle-longstanding-rcs-spam-in-india-but-not-alone/ | news | 2026-03-01 |
| [14] | VBSF 이미지 스팸 탐지 논문 | https://www.arxiv.org/pdf/2512.23788 | paper | 2025-12 |
| [15] | PQC Industry Report 2026 | https://www.globenewswire.com/news-release/2026/02/23/3242432/28124/en/ | report | 2026-02-23 |
| [16] | Google PQC 정책 촉구 | https://www.themeridiem.com/security/2026/2/6/google-shifts-post-quantum-encryption-from-r-d-to-government-policy-mandate | news | 2026-02-06 |
| [17] | NIST HQC 5번째 표준 | https://www.encryptionconsulting.com/decoding-nist-pqc-standards/ | analysis | 2026 |
| [18] | CNSA 2.0 데드라인 | https://www.graygroupintl.com/blog/post-quantum-cryptography-enterprise-guide/ | analysis | 2026 |
| [19] | EU PQC 로드맵 | https://digital-strategy.ec.europa.eu/en/library/coordinated-implementation-roadmap-transition-post-quantum-cryptography | policy | 2026 |
| [20] | Niobium+SemiFive FHE ASIC | https://www.prnewswire.com/news-releases/semifive-partners-with-niobium-to-develop-fhe-accelerator-driving-us-market-expansion-302692312.html | news | 2026-02-19 |
| [21] | Niobium Samsung 파운드리 | https://itbrief.asia/story/niobium-taps-samsung-for-encrypted-ai-chip-production | news | 2026-02 |
| [22] | Niobium 2300만달러 투자 | https://thequantuminsider.com/2025/12/03/niobium-23m-fhe-funding/ | news | 2025-12 |
| [23] | FHE 시장 전망 2026-2035 | https://www.360researchreports.com/market-reports/homomorphic-encryption-market-206111 | report | 2026 |
| [24] | ppRAG 거리보존 암호화 | https://arxiv.org/abs/2601.12331 | paper | 2026-01 |
| [25] | CyborgDB 암호화 벡터DB | https://www.cyborgdb.co/new | product | 2026 |
| [26] | IronCore Labs 임베딩 암호화 | https://ironcorelabs.com/ai-encryption/ | product | 2026 |
| [27] | Apple HE + ML Research | https://machinelearning.apple.com/research/homomorphic-encryption | research | 2026 |
| [28] | 프라이버시 보존 LLM 추론 | https://eprint.iacr.org/2026/105.pdf | paper | 2026 |
