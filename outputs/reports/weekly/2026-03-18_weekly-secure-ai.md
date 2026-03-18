---
type: weekly-monitor
domain: secure-ai
week: 2026-W12
date: 2026-03-18
l3_count: 5
deep_count: 3
---

# 주간 기술 동향: Secure AI (2026-W12)

## Executive Summary

| 세부기술 | 신호 | 핵심 내용 | 분석 |
|----------|------|----------|------|
| 스팸/피싱 감지(통화전) | 🔴 긴급 | P1 Vishing-as-a-Service($399/월) 실체 노출, Microsoft Teams Pre-Call 사칭 방지, Meta 전 플랫폼 AI 사기 탐지 출시. KT 2.0 상용화 | Deep |
| On-Device 동형암호 | 🔴 긴급 | DESILO×Gentry GL 스킴(5세대 FHE) 발표, Intel Heracles ASIC 5,547배 성능, 클라이언트-사이드 97% 경량화. FHE 하드웨어 레이스 본격화 | Deep |
| OnDevice 양자암호(PQC) | 🟡 주목 | Akamai TLS 전면 PQC 완료, Samsung Exynos 2600 HW-PQC 양산, QCi+Ciena 1.6Tb/s PQC+QKD 시연. FIPS 140-2 종료 6개월 카운트다운 | Deep |
| OCR 이미지 스팸 | 🟢 평온 | Gmail RETVec/TF 이미지 스팸 차단 강화 외 구조적 변화 없음 | Quick |
| Secure Vector Search | 🟢 평온 | Hermes FHE-native 벡터DB 논문(1,600× 처리량), AHE 대안 연구. 상용 돌파 없음 | Quick |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음
>
> **분석** : Deep = 심층 리서치 수행 | Quick = 1줄 요약만

---

## 🟢 Quick 요약 (변화 미미)

### OCR 이미지 스팸 차단
- Gmail TensorFlow 기반 이미지 스팸 탐지가 일 1억건 추가 차단 달성. RETVec(Resilient & Efficient Text Vectorizer)로 조작 텍스트 탐지 효율 개선. Gemini Nano 온디바이스 보호 확대. 구조적 기술 돌파 없음.

### Secure Vector Search
- Hermes(FHE-native 벡터DB) 논문이 1,600× 처리량 달성으로 주목받으나 아직 연구 단계. AHE(Additively Homomorphic Encryption)가 FHE 대비 실용적 대안으로 연구 진행 중. Apple Private NN Search 외 상용 돌파 없음.

---

## 🔴 Deep 심층 분석

### 스팸/피싱 감지(통화전) — 🔴 긴급

#### 이전 대비 변화
- 전주: LG U+ Anti-DeepVoice GLOMO 수상, KT 97.2% 정확도, Virgin Media O2 10억건 탐지
- 금주: Scam-as-a-Service 인프라 실체 공개(P1 플랫폼), VoIP·메시징 플랫폼의 독자 Pre-Call 보안 구축(Microsoft·Meta), KT 2.0 3중 탐지 상용화
- 변화 방향: 사기 도구의 서비스화(SaaS) → 탐지 전선이 통신사 망 레이어에서 플랫폼 레이어로 확산

#### 기술 동향

1. **P1 Vishing-as-a-Service 플랫폼 노출 — ElevenLabs TTS 남용 자동화 사기 인프라.**
   Mirage Security가 P1(p1bot.io) 비난독화 JS를 분석, 월 $399로 전화번호 스푸핑+AI 음성+WebRTC 발신+DTMF 캡처를 제공하는 완전 자동화 사기 플랫폼의 전모를 공개했다. 영어 15·프랑스어 4·스페인어 4개 음성 카탈로그 탑재. ElevenLabs는 즉시 악용 계정 차단. [[G-01]](#ref-g-01)

2. **Microsoft Teams Brand Impersonation Protection — VoIP Pre-Call 보안 첫 주요 사례.**
   3월 중순 Targeted Release, 4월 말 GA. 미지 외부 VoIP 통화 수신 전 사칭 패턴 자동 경고. 관리자 설정 불필요. 통신사 망이 아닌 플랫폼 레이어에서 독자 구현한 첫 주요 사례. [[G-02]](#ref-g-02), [[G-03]](#ref-g-03)

3. **Meta 전 플랫폼 AI 사기 탐지 도구 3월 동시 출시.**
   WhatsApp(QR 코드 피싱 방어)·Facebook(의심 친구 요청 경고)·Messenger(AI 사기 리뷰) 동시 배포. 동남아 스캠센터 계정 15만+ 비활성화, 법집행 공조 21명 검거. [[G-04]](#ref-g-04), [[G-05]](#ref-g-05)

4. **KT AI 보이스피싱 탐지 2.0 상용화 — 화자인식+딥보이스 3중 체계.**
   국과수 '그놈목소리' 성문 DB 기반 화자인식 + 딥보이스 탐지를 문맥 탐지(v1.0)에 추가. 개인정보보호위원회 규제 승인. 2025년 1,300억원 피해 예방, 경찰 공조 피해 25% 감소. [[G-06]](#ref-g-06), [[G-07]](#ref-g-07)

5. **C2PA Content Credentials 확산 — 음성 인증 기반 발전 가능성.**
   OpenAI DALL-E/SORA에 자동 적용, BBC·Reuters 등 6,000+ 조직 채택. 통신사 Pre-Call 음성 출처 인증(AI vs 사람)에 적용 가능하나 통신사 직접 채택 사례는 미확인. [[G-08]](#ref-g-08)

6. **AI 교육이 음성 사기 대응 핵심 — 기술 탐지만으로 불충분.**
   딥페이크 음성이 '구별 불가 임계점'을 넘어 순수 기술 탐지 한계 가속화. 탐지 도구 + 사용자 인식 교육의 이중 접근 필요. [[G-09]](#ref-g-09)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| SKT | ScamVanguard 11억건 차단(+35% YoY), 통화패턴 AI 모델로 미신고 번호 선제 탐지 | [[G-10]](#ref-g-10) |
| KT | AI 보이스피싱 2.0 상용화: 국과수 성문 DB+딥보이스+문맥 3중 체계. 97.2% 정확도. 피해 예방 1,300억원 | [[G-06]](#ref-g-06), [[G-07]](#ref-g-07) |
| Microsoft | Teams Brand Impersonation Protection 3월 배포 시작, 4월 GA | [[G-02]](#ref-g-02) |
| Meta | WhatsApp·Facebook·Messenger 전 플랫폼 AI 사기 탐지 동시 출시. 스캠센터 15만+ 계정 비활성화 | [[G-04]](#ref-g-04) |
| Hiya | State of Call 2026: 미국인 25% 딥페이크 수신, 소비자 38% 이통사 교체 의향 | [[G-11]](#ref-g-11) |
| Mirage Security | P1 vishing-as-a-service 노출(ElevenLabs TTS, $399/월) | [[G-01]](#ref-g-01) |

#### 시장 시그널
- Hiya: 미국인 주당 9.9건 원치 않는 통화(+16% CAGR since 2023), 소비자 "스캐머가 통신사보다 2:1 앞선다" 응답 [[G-11]](#ref-g-11)
- FTC 2024년 미국 사기 피해 $12.5B, 딥페이크 기반 사기 2027년 $40B 전망 [[G-12]](#ref-g-12)
- CrowdStrike: 2024년 H2 vishing 사건 H1 대비 442% 급증 [[G-13]](#ref-g-13)
- Scam-as-a-Service 가격화: P1 플랫폼 월 $399 — AI 음성 사기 진입장벽 실질적 붕괴 [[G-01]](#ref-g-01)

#### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| AI Powered Deepfake Voice and Scam Call Detector (Saxena et al., ICSIAIML 2025) | CNN+RNN 통합 딥페이크 음성·스캠 통화 탐지 시스템 | [[P-01]](#ref-p-01) |
| AudioFakeNet (Boucherit et al., MDPI 2025) | CNN+LSTM+Multi-Head Attention 하이브리드, MFCC 기반 EER SOTA | [[P-02]](#ref-p-02) |
| VoiceRadar (NDSS 2025) | 마이크로 주파수 기반 레이더 방식 실시간 딥보이스 탐지 | [[P-03]](#ref-p-03) |

#### 전략적 시사점

**기회**
- P1 플랫폼 노출로 ElevenLabs 음성 ID 등 TTS 패턴 역이용한 음성 지문 탐지 고도화 가능
- 통신사는 망 레이어 고유 우위(STIR/SHAKEN, 메타데이터)로 Microsoft·Meta 플랫폼 탐지와 차별화 가능
- KT 국과수 성문 DB 규제 승인은 유사 기술 도입의 규제 선례

**위협**
- Scam-as-a-Service 진입장벽 붕괴($399/월) — 사기 도구 확산이 탐지 대응 속도를 초과
- Microsoft·Meta 자체 탐지 레이어가 통신사 앱 기반 부가 서비스 가치를 희석

---

### On-Device 동형암호 키워드 검색 — 🔴 긴급

#### 이전 대비 변화
- 전주: LG U+×CryptoLab CKKS+ 4.5세대 AICC 상용화, Niobium FHE ASIC 양산 준비, NIST Th-FHE 진입
- 금주: 5세대 GL FHE 공식 발표, Intel Heracles ASIC 5,547배 성능 실물 시연, 클라이언트-사이드 97% 경량화 논문, FHE 하드웨어 레이스 3자 동시 진입
- 변화 방향: FHE가 이론→하드웨어 레이스 구도로 전환. 키워드 PIR 연구가 구현 단계로 진입

#### 기술 동향

1. **DESILO×Gentry GL 스킴 — 5세대 FHE 공식 발표 (FHE.org 2026 타이베이).**
   FHE 발명자 Craig Gentry와 DESILO가 행렬 곱셈을 FHE 상태에서 재설계한 GL 스킴을 3월 8일 발표. Private AI — 프롬프트·입력·출력이 암호화된 상태로 LLM 추론 — 실증 시연. [[G-14]](#ref-g-14)

2. **Intel Heracles FHE ASIC — ISSCC 2026 실물 시연, 5,547배 성능.**
   3nm FinFET, 197mm², 176W, 48GB HBM3. BGV·BFV·CKKS 3대 스킴 지원. 24코어 Xeon 대비 1,074~5,547배. 오픈소스 Polynomial ISA SDK 공개. [[G-15]](#ref-g-15), [[G-16]](#ref-g-16)

3. **클라이언트-사이드 FHE 97% 경량화 — EuroS&P 2026 논문.**
   Graz Univ. Aikata et al. — 부트스트래핑으로 클라이언트 FHE 암호화/복호화 재설계. 연산량·통신 오버헤드 97% 감소, FPGA/ASIC 76배 가속. 마이크로컨트롤러 구현 포함. 온디바이스 PIR 클라이언트에 직접 응용 가능. [[P-04]](#ref-p-04)

4. **FHE.org 2026 — 타이베이, 10편 구두·23편 포스터.**
   GL 스킴 외 Zama HPU(FPGA TFHE 가속기), Apple PIR 개선 발표. 산학 FHE 연간 기준점으로 자리잡음. [[G-17]](#ref-g-17)

5. **NIST Threshold Call 4월 20일 마감 — FHE 표준화 진입.**
   Zama(TFHE/ZHEnith/Nexus), CryptoLab(Threshold CKKS) 제출 선언. 표준화 불확실성 해소 시작. [[G-18]](#ref-g-18)

6. **Mirror Security×NVIDIA — GPU 가속 FHE AI 추론 플랫폼 출시.**
   CUDA/cuBLAS/TensorRT-LLM 활용, 데이터 전 과정 복호화 없는 Secure AI Inference 구현. Intel과 €2.1M 공동연구 병행. [[G-19]](#ref-g-19)

7. **키워드 PIR 연구 가속 — HET-PIR·BCPIR 논문 2편 연속 발표.**
   HET-PIR: FHE 동치 테스트 최적화로 단일 서버 키워드 PIR 실용화. BCPIR: 블록 코드 기반 통신 복잡도 추가 감소. 온디바이스 암호화 검색이 구현 단계로 이행. [[P-05]](#ref-p-05), [[P-06]](#ref-p-06)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| DESILO (한국) | Craig Gentry와 GL 스킴(5세대 FHE) FHE.org 2026 발표. Private AI 데모 | [[G-14]](#ref-g-14) |
| Intel | Heracles ASIC ISSCC 2026 실물 시연. 3nm, 5,547×. 오픈소스 SDK | [[G-15]](#ref-g-15) |
| Niobium+SEMIFIVE+Samsung | FHE ASIC 설계 진행 중(100억원, Samsung 8nm). 추가 발표 없음 | [[G-20]](#ref-g-20) |
| Mirror Security | NVIDIA 협력 GPU 가속 FHE 추론 플랫폼 출시. Intel €2.1M 공동연구 | [[G-19]](#ref-g-19) |
| Zama | TFHE·ZHEnith·Nexus NIST 제출 패키지, 오픈소스 HPU 출시 | [[G-18]](#ref-g-18) |
| CryptoLab (한국) | CKKS+ 상용화 지속, 9차 HE 표준화 회의(서울) 주도 | [[G-21]](#ref-g-21) |

#### 시장 시그널
- Intel·Niobium·Mirror Security 3자가 같은 분기에 FHE 하드웨어 상업화 레인 진입 — 하드웨어 레이스 구도 형성
- Private AI("암호화 데이터에서 직접 LLM 서비스") 방향으로 시장 내러티브 이동
- CryptoLab·DESILO·Samsung Foundry·LGU+가 FHE 핵심 공급망에 동시 참여하며 한국 비중 확대
- NIST 4월 마감 이후 FHE 파라미터 표준 확정 시 상호운용성 기반 암호화 검색 SaaS/SDK 시장 개화 가능

#### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| Privacy at your Fingertips (Aikata et al., Graz, EuroS&P 2026) | FHE 클라이언트 97% 경량화, FPGA 76× 가속, 마이크로컨트롤러 구현 | [[P-04]](#ref-p-04) |
| HET-PIR (Cybersecurity/Springer, 2026) | FHE 동치 테스트 최적화, 단일 서버 키워드 PIR 실용화 | [[P-05]](#ref-p-05) |
| BCPIR (Springer LNCS, 2026) | 블록 코드 기반 키워드 PIR 통신 복잡도 감소 | [[P-06]](#ref-p-06) |
| GL FHE Scheme (Lee & Gentry, IACR ePrint 2025/1935) | 5세대 FHE, 암호화 행렬 곱셈 재설계, LLM 추론 지원 | [[P-07]](#ref-p-07) |
| FHECore (BU·KAIST et al., 2026) | GPU 마이크로아키텍처 FHE 최적화, CKKS 명령 수 2.41× 감소 | [[P-08]](#ref-p-08) |

#### 전략적 시사점

**기회**
- FHE 하드웨어 레이스(Intel·Niobium·Mirror)로 에지-서버 하이브리드 FHE 키워드 검색 아키텍처 현실성 급상승
- HET-PIR·BCPIR 동시 발표 — 키워드 PIR이 "구현 최적화" 단계 진입. 1~2년 내 상용 SDK 등장 가능
- 한국 생태계(DESILO·CryptoLab·Samsung Foundry·LGU+)가 글로벌 FHE 공급망 핵심 축

**위협**
- GL 스킴 등 5세대 기술이 빠르게 등장하며 현재 CKKS 기반 구현의 기술 교체 주기 단축 위험
- Apple이 SWHE 기반 PIR을 이미 운영 중 — 스마트폰 제조사 주도 de facto 표준화 위험

---

### OnDevice 양자암호 (PQC) — 🟡 주목

#### 이전 대비 변화
- 전주: Google PLANTS/MTC 14,700B→736B, Cloudflare PQC SASE 60%+, Microsoft PQC APIs GA, Samsung S3SSE2A HW PQC SE
- 금주: Akamai TLS 전면 PQC 완료, Samsung Exynos 2600 HW-PQC 양산, QCi+Ciena 1.6Tb/s PQC+QKD OFC 시연, FIPS 140-2 6개월 카운트다운
- 변화 방향: CDN/SoC/광통신 레이어에서 PQC 실배포 가속. 규제 마감 압박 본격화

#### 기술 동향

1. **Akamai TLS 전면 PQC 완료 — CDN 전 경로 양자내성화.**
   Client-to-Edge, Edge-to-Origin, Mid-tier 3단계 X25519MLKEM768 기본 활성화 완료(Q1 2026). [[G-22]](#ref-g-22)

2. **Samsung Exynos 2600 — 세계 최초 HW-PQC 스마트폰 SoC.**
   ML-DSA ROM-rooted protection, Galaxy S26 탑재. Knox Matrix E2E PQC 강화. 단, S26 Ultra는 Snapdragon으로 HW-PQC 미지원. [[G-23]](#ref-g-23), [[G-24]](#ref-g-24)

3. **QCi+Ciena OFC 2026 — 1.6 Tb/s PQC+QKD 통합 광통신 시연.**
   WaveLogic 6 Extreme + NIST 인증 PQC + QKD 결합(2026-03-12). ETSI 표준 API QKD 연동. 통신 인프라 PQC 실용화 확인. [[G-25]](#ref-g-25)

4. **FIPS 140-2 종료 6개월 카운트다운 — 2026-09-21.**
   NIST CMVP가 잔존 모듈을 Historical로 이전. 이후 신규 조달 FIPS 140-3만 허용. PQC 전환의 규제적 출발점. [[G-26]](#ref-g-26)

5. **HQC 초안 표준 2026년 발행 예정 — ML-KEM 백업 알고리즘.**
   코드 기반 KEM으로 격자 기반 ML-KEM 대비 알고리즘 다양성 확보. Crypto-agile 설계 필요성 강조. [[G-27]](#ref-g-27)

6. **3GPP PQC 도입 연구 착수 — VoLTE/VoNR 음성 보안 표준화 진행.**
   SIP 시그널링·SRTP·DTLS 양자내성화 필요하나 3GPP 사양 채택 전까지 라이브 배포 불가. 2027년 이후 현실적. [[G-28]](#ref-g-28)

7. **한국 PQC 전환 파일럿 확대 — 5개 부문, 45억원.**
   2035년 전면 전환 마스터플랜. 한국 자체 알고리즘(AIMer, SMAUG-T, HAETAE) 포함. [[G-29]](#ref-g-29)

8. **LG유플러스 ixi-Guardian 2.0 — PQC+동형암호+SASE 통합.**
   MWC 2026 공개. 광전송 PQC 적용, NIST+KpqC 전 알고리즘 지원 인터페이스. U+ PQC-VPN 운영 중. [[G-30]](#ref-g-30)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Samsung | Exynos 2600 세계 최초 HW-PQC SoC 양산, Galaxy S26. S3SSE2A CC EAL6+ | [[G-23]](#ref-g-23) |
| Akamai | Q1 2026 TLS 전 경로 X25519MLKEM768 기본 배포 완료 | [[G-22]](#ref-g-22) |
| Ciena+QCi | OFC 2026: 1.6 Tb/s PQC+QKD 통합 시연 | [[G-25]](#ref-g-25) |
| SKT | QKD+PQC 하이브리드 상용화, 양자기술 협의체 참여 | [[G-31]](#ref-g-31) |
| LG유플러스 | ixi-Guardian 2.0 (PQC+동형암호+SASE). U+ PQC-VPN 운영 | [[G-30]](#ref-g-30) |
| KT | PQC+QKD 하이브리드 전략 공식화, 양자기술 협의체 참여 | [[G-32]](#ref-g-32) |
| NIST | FIPS 140-2 종료 2026-09-21. HQC 초안 2026년 발행 예정 | [[G-26]](#ref-g-26), [[G-27]](#ref-g-27) |

#### 시장 시그널
- PQC 시장 2025년 $4.2억 → 2030년 $28~78억(CAGR 37~46%, 기관별 편차) [[G-33]](#ref-g-33)
- GlobeNewswire: "PQC 마이그레이션은 1조 달러 규모 과제"로 프레이밍 [[G-34]](#ref-g-34)
- VoLTE/VoNR PQC는 3GPP 표준화 지연으로 2027년 이후 현실적. 현 시점은 at-rest 암호화에 집중 [[G-28]](#ref-g-28)
- HNDL 위협이 통화 녹음 파일 보안의 핵심 드라이버로 부상 [[G-29]](#ref-g-29)
- 한국: PQC 파일럿 3→5개 부문, 45억원 투입. 2035년 전면 전환 [[G-29]](#ref-g-29)

#### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| Securing Cryptography in Age of QC and AI (arXiv:2603.06969, 2026-03) | 양자+AI 이중 위협 하 PQC 구현 전략 종합 리뷰 | [[P-09]](#ref-p-09) |
| PQC authentication for Industrial IoT (Nature Sci. Rep., 2026-03) | ML-KEM+ML-DSA TLS 1.3 통합, IoT 인증 실측값 | [[P-10]](#ref-p-10) |
| PQC in the 5G Core (arXiv:2512.20243, 2025-12) | 하이브리드 X25519+Kyber768 적용, 레이턴시 +10~20ms, 가용성 영향 없음 | [[P-11]](#ref-p-11) |

#### 전략적 시사점

**기회**
- Samsung Exynos 2600 HW-PQC로 On-Device PQC 통화 녹음 암호화의 하드웨어 기반 실용화
- 한국 PQC 파일럿 확대(5개 부문, 45억원)는 공공 레퍼런스 확보 창구
- HNDL 위협 대비 "레거시 녹음 파일 재암호화" 기능이 차별화 요소

**위협**
- 3GPP PQC 표준화 지연 → VoLTE/VoNR 실시간 PQC는 2027년 이후. At-rest 집중 필요
- HQC 표준 확정 시 ML-KEM 단독 구현 조직의 재마이그레이션 비용 발생 — Crypto-agile 필수
- FIPS 140-3 완전 CMVP PQC 모듈 희소 → 규제 산업 조달 마찰

---

## 경쟁사 동향 (SKT / KT)

> 이번 주 Secure AI 도메인과 관련된 SKT·KT의 주요 움직임.

### SKT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| AI 스팸 필터링 성과 | ScamVanguard 2025년 11억건 차단(+35% YoY). 통화패턴 AI로 미신고 번호 선제 탐지. 음성 피싱 250억건(+119%) 차단 | spam-phishing-detection | [[G-10]](#ref-g-10) |
| QKD+PQC 하이브리드 | 세계 최초 QKD-PQC 하이브리드 양자암호 상용화. IDQ Clavis XG + 자체 PQC SW. FIPS 203/204 준수 | pqc-voice-encryption | [[G-31]](#ref-g-31) |
| 양자기술 협의체 | 2026년 1월 출범, 삼성·LG전자·KT와 공동 참여. 2028년 국가 인프라 양자암호통신망 목표 | pqc-voice-encryption | [[G-35]](#ref-g-35) |

### KT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| AI 보이스피싱 탐지 2.0 | 국과수 성문 DB + 딥보이스 + 문맥 3중 탐지 상용화. 97.2% 정확도. 2025년 1,300억원 피해 예방 | spam-phishing-detection | [[G-06]](#ref-g-06) |
| 양자암호 전략 | PQC+QKD 하이브리드 전략 공식화. 초당 30만개 암호키 생성 장비 개발 | pqc-voice-encryption | [[G-32]](#ref-g-32) |
| 6G 퀀텀세이프 | 6G 지능형 네트워크 청사진에 양자암호+AI 침해탐지+동형암호 내재화 계획 | pqc-voice-encryption, he-keyword-search | [[G-36]](#ref-g-36) |

### 시사점
- SKT·KT 모두 AI 스팸 탐지 + 양자암호에서 적극적 투자 진행. SKT는 양(건수) 중심, KT는 질(3중 체계, 성문 DB) 중심으로 차별화
- 양자암호는 두 사업자 모두 PQC+QKD 하이브리드로 수렴. 2028년 국가 인프라 양자통신망이 경쟁의 다음 전장

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **탐지 vs 암호화의 동시 진화**: 스팸/피싱 탐지(공격 차단)와 PQC/FHE(데이터 보호)가 동시에 급진전하며, "보안"의 양 축이 모두 임계점에 도달. 통신사는 두 축을 통합한 종합 보안 포지셔닝이 가능

2. **FHE 하드웨어 레이스 ↔ PQC 규제 마감**: Intel·Niobium FHE ASIC과 FIPS 140-2 종료가 같은 시기에 진행. 양자내성 + 프라이버시 보존이 동시 요구되는 규제 환경이 형성 중

3. **플랫폼 vs 통신사 보안 경쟁**: Microsoft Teams·Meta가 독자 Pre-Call/인메시지 보안을 구축하며 통신사의 보안 부가서비스 가치 희석 위험. 망 레이어 고유 우위(STIR/SHAKEN, 메타데이터, QoS)로 차별화 필요

### 후속 조치 제안

- 🔴 스팸/피싱 감지 — Scam-as-a-Service 대응 전략 검토. P1 플랫폼 TTS 패턴 역분석 기반 탐지 고도화 검토
- 🔴 동형암호 — Intel Heracles/Niobium ASIC 로드맵 추적. GL 스킴의 CKKS 대체 가능성 평가 필요
- 🟡 PQC — FIPS 140-2 종료(9/21) 대비 내부 인증 모듈 점검. At-rest 통화 녹음 PQC 암호화 PoC 검토

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Help Net Security — AI-powered vishing platform P1 노출 | [링크](https://www.helpnetsecurity.com/2026/03/11/researchers-uncover-ai-powered-vishing-platform/) | news | 2026-03-11 | [B] |
| <a id="ref-g-02"></a>G-02 | BleepingComputer — Microsoft Teams Brand Impersonation Protection | [링크](https://www.bleepingcomputer.com/news/microsoft/microsoft-teams-to-add-brand-impersonation-warnings-to-calls/) | news | 2026-03 | [B] |
| <a id="ref-g-03"></a>G-03 | SC Media — Teams call security enhancement | [링크](https://www.scworld.com/brief/microsoft-teams-enhances-call-security-with-brand-impersonation-protection) | news | 2026-03 | [B] |
| <a id="ref-g-04"></a>G-04 | Meta Newsroom — Fighting Scammers with AI | [링크](https://about.fb.com/news/2026/03/fighting-scammers-protecting-people-with-new-technology-and-partnerships/) | 보도자료 | 2026-03 | [A] |
| <a id="ref-g-05"></a>G-05 | Malwarebytes — Meta anti-scam tools | [링크](https://www.malwarebytes.com/blog/news/2026/03/meta-rolls-out-anti-scam-tools-across-whatsapp-facebook-and-messenger) | news | 2026-03 | [B] |
| <a id="ref-g-06"></a>G-06 | BusinessPost — KT AI 보이스피싱 탐지 2.0 출시 | [링크](https://www.businesspost.co.kr/BP?command=article_view&num=405398) | news | 2026-03 | [B] |
| <a id="ref-g-07"></a>G-07 | Digital Today — KT 딥보이스 탐지 3중 체계 | [링크](https://www.digitaltoday.co.kr/news/articleView.html?idxno=580815) | news | 2026-03 | [B] |
| <a id="ref-g-08"></a>G-08 | Content Authenticity Initiative — State of Content Authenticity 2026 | [링크](https://contentauthenticity.org/blog/the-state-of-content-authenticity-in-2026) | blog | 2026 | [B] |
| <a id="ref-g-09"></a>G-09 | TechXplore — AI education for voice scams | [링크](https://techxplore.com/news/2026-03-ai-crucial-tackling-voice-scams.html) | news | 2026-03 | [B] |
| <a id="ref-g-10"></a>G-10 | Telecompaper — SKT AI-driven spam blocking | [링크](https://www.telecompaper.com/news/skt-reveals-rise-in-ai-driven-blocking-of-spam-and-voice-phishing-attempts--1558993) | news | 2026-01 | [B] |
| <a id="ref-g-11"></a>G-11 | Hiya / NatLawReview — State of the Call 2026 | [링크](https://natlawreview.com/press-releases/state-call-2026-ai-deepfake-voice-calls-hit-1-4-americans-consumers-say) | 리포트 | 2026-03-02 | [B] |
| <a id="ref-g-12"></a>G-12 | DeepStrike — Vishing Statistics & $40B projection | [링크](https://deepstrike.io/blog/vishing-statistics-2025) | blog | 2025 | [C] |
| <a id="ref-g-13"></a>G-13 | Offenso Academy — Vishing 442% surge (CrowdStrike) | [링크](https://tvm.offensoacademy.com/vishing-attacks-2026-voice-scams-beating/) | blog | 2026 | [C] |
| <a id="ref-g-14"></a>G-14 | PR Newswire — DESILO×Gentry GL FHE 5세대 | [링크](https://www.prnewswire.com/news-releases/desilo-and-fhe-inventor-craig-gentry-introduce-5th-generation-gl-fhe-scheme-for-private-ai-302707060.html) | 보도자료 | 2026-03-07 | [A] |
| <a id="ref-g-15"></a>G-15 | IEEE Spectrum — Intel Heracles FHE ASIC | [링크](https://spectrum.ieee.org/fhe-intel) | news | 2026-03-10 | [B] |
| <a id="ref-g-16"></a>G-16 | Tom's Hardware — Heracles 5,547× faster | [링크](https://www.tomshardware.com/tech-industry/cyber-security/intels-heracles-chip-computes-fully-encrypted-data-without-decrypting-it-chip-is-1-074-to-5-547-times-faster-than-a-24-core-intel-xeon-in-fhe-math-operations) | news | 2026-03-10 | [B] |
| <a id="ref-g-17"></a>G-17 | FHE.org — Conference 2026 Taipei | [링크](https://fhe.org/conferences/conference-2026/) | 공식 | 2026-03-08 | [A] |
| <a id="ref-g-18"></a>G-18 | NIST CSRC — Threshold Cryptography / NISTIR 8214C | [링크](https://csrc.nist.gov/projects/threshold-cryptography) | 공식 | 2026-01-20 | [A] |
| <a id="ref-g-19"></a>G-19 | startupnews.fyi — Mirror Security×NVIDIA FHE inference | [링크](https://startupnews.fyi/2026/02/18/mirror-security-nvidia-encrypted-ai/) | news | 2026-02-18 | [B] |
| <a id="ref-g-20"></a>G-20 | PR Newswire — SEMIFIVE×Niobium FHE ASIC (Samsung 8nm) | [링크](https://www.prnewswire.com/news-releases/semifive-partners-with-niobium-to-develop-fhe-accelerator-driving-us-market-expansion-302692312.html) | 보도자료 | 2026-02-19 | [A] |
| <a id="ref-g-21"></a>G-21 | HomomorphicEncryption.org — 9th Standards Meeting (Seoul) | [링크](https://homomorphicencryption.org/9th-homomorphicencryption-org-standards-meeting/) | 공식 | 2026-03-05 | [A] |
| <a id="ref-g-22"></a>G-22 | Akamai — PQC Client to Edge | [링크](https://techdocs.akamai.com/property-mgr/docs/pqc-client-to-edge) | 공식 | 2026-01 | [A] |
| <a id="ref-g-23"></a>G-23 | Samsung Semiconductor — Exynos 2600 PQC | [링크](https://semiconductor.samsung.com/news-events/tech-blog/where-trust-begins-exynos-anchors-post-quantum-security-at-the-root-of-mobile-socs/) | 공식 | 2026 | [A] |
| <a id="ref-g-24"></a>G-24 | Technosports — Exynos 2600 quantum-proof | [링크](https://technosports.co.in/exynos-2600-quantum-proof-encryption/) | news | 2026-02 | [B] |
| <a id="ref-g-25"></a>G-25 | Quantum Insider — QCi+Ciena OFC 2026 | [링크](https://thequantuminsider.com/2026/03/12/qci-ciena-quantum-secure-communications-demo/) | news | 2026-03-12 | [B] |
| <a id="ref-g-26"></a>G-26 | SafeLogic — FIPS 140-2 September 21, 2026 | [링크](https://www.safelogic.com/blog/what-happens-on-september-21-2026) | blog | 2026 | [B] |
| <a id="ref-g-27"></a>G-27 | NIST — HQC Fifth Algorithm | [링크](https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption) | 공식 | 2025-03-11 | [A] |
| <a id="ref-g-28"></a>G-28 | postquantum.com — Telecom PQC Challenges | [링크](https://postquantum.com/post-quantum/telecom-pqc-challenges/) | news | 2026 | [B] |
| <a id="ref-g-29"></a>G-29 | Pentasecurity — 2026 양자보안 솔루션 리포트 | [링크](https://www.pentasecurity.co.kr/in-the-news/2026-quantum-security-solution-report/) | news | 2026-02 | [B] |
| <a id="ref-g-30"></a>G-30 | EBN — LG유플러스 ixi-Guardian 2.0 (MWC 2026) | [링크](https://www.ebn.co.kr/news/articleView.html?idxno=1701212) | news | 2026-03 | [B] |
| <a id="ref-g-31"></a>G-31 | SKT Newsroom — QKD+PQC 하이브리드 | [링크](https://news.sktelecom.com/207758) | 보도자료 | 2024-10-15 | [A] |
| <a id="ref-g-32"></a>G-32 | Thelec.kr — KT PQC+QKD 하이브리드 전략 | [링크](https://www.thelec.kr/news/articleView.html?idxno=28391) | news | 2026 | [B] |
| <a id="ref-g-33"></a>G-33 | MarketsandMarkets — PQC Market $0.42B→$2.84B | [링크](https://www.marketsandmarkets.com/PressReleases/post-quantum-cryptography.asp) | report | 2025 | [C] |
| <a id="ref-g-34"></a>G-34 | GlobeNewswire — PQC Migration Trillion-Dollar Imperative | [링크](https://www.globenewswire.com/news-release/2026/02/19/3241234/0/en/Post-Quantum-Cryptography-Migration-Is-Now-a-Trillion-Dollar-Imperative.html) | news | 2026-02-19 | [B] |
| <a id="ref-g-35"></a>G-35 | 전자신문 — 양자기술 협의체 출범 | [링크](https://www.etnews.com/20260129000199) | news | 2026-01-29 | [B] |
| <a id="ref-g-36"></a>G-36 | InsightKorea — SKT·KT·LGU+ 양자 보안 | [링크](https://www.insightkorea.co.kr/news/articleView.html?idxno=242127) | news | 2026 | [B] |
| <a id="ref-p-01"></a>P-01 | Saxena et al. — AI Powered Deepfake Voice and Scam Call Detector (ICSIAIML 2025) | [링크](https://www.atlantis-press.com/proceedings/icsiaiml-25/126021219) | paper | 2026-01 | [A] |
| <a id="ref-p-02"></a>P-02 | Boucherit et al. — AudioFakeNet (MDPI Algorithms, 2025) | [링크](https://www.mdpi.com/1999-4893/18/11/716) | paper | 2025-11 | [A] |
| <a id="ref-p-03"></a>P-03 | NDSS 2025 — VoiceRadar | [링크](https://www.ndss-symposium.org/wp-content/uploads/2025-3389-paper.pdf) | paper | 2025 | [A] |
| <a id="ref-p-04"></a>P-04 | Aikata et al. — Privacy at your Fingertips (Graz, EuroS&P 2026) | [링크](https://eprint.iacr.org/2026/515) | paper | 2026-03-15 | [A] |
| <a id="ref-p-05"></a>P-05 | HET-PIR — Keyword PIR via homomorphic equality test (Springer) | [링크](https://link.springer.com/article/10.1186/s42400-025-00506-x) | paper | 2026 | [A] |
| <a id="ref-p-06"></a>P-06 | BCPIR — Keyword PIR via Block Building Codewords (Springer LNCS) | [링크](https://link.springer.com/chapter/10.1007/978-3-031-94445-1_9) | paper | 2026 | [A] |
| <a id="ref-p-07"></a>P-07 | Lee & Gentry — GL FHE Scheme (IACR ePrint 2025/1935) | [링크](https://eprint.iacr.org/2025/1935) | paper | 2026-03-07 | [A] |
| <a id="ref-p-08"></a>P-08 | BU·KAIST et al. — FHECore GPU Microarchitecture (2026) | [링크](https://semiengineering.com/a-gpu-microarchitecture-optimized-for-fully-homomorphic-encryption/) | paper | 2026-02 | [A] |
| <a id="ref-p-09"></a>P-09 | arXiv:2603.06969 — Securing Cryptography in Age of QC and AI | [링크](https://arxiv.org/html/2603.06969v1) | paper | 2026-03 | [A] |
| <a id="ref-p-10"></a>P-10 | Nature Sci. Rep. — PQC authentication for Industrial IoT | [링크](https://www.nature.com/articles/s41598-025-28413-8) | paper | 2026-03 | [A] |
| <a id="ref-p-11"></a>P-11 | arXiv:2512.20243 — PQC in the 5G Core | [링크](https://arxiv.org/html/2512.20243v1) | paper | 2025-12 | [A] |
