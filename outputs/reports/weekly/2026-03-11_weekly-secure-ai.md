---
type: weekly-monitor
domain: secure-ai
week: 2026-W11
date: 2026-03-11
l3_count: 7
deep_count: 4
---

# 주간 기술 동향: Secure AI (2026-W11)

## Executive Summary

| 세부기술 | 신호 | 핵심 내용 | 분석 |
|----------|------|----------|------|
| OnDevice 양자암호 | 🔴 긴급 | Google PLANTS/MTC PQC 인증서 경량화, Cloudflare 완전 PQC SASE, NIST/NSA 이중 규제 마감 | Deep |
| OnDevice sLM | 🟡 주목 | Gemma 3n 생태계 통합 완료, Qwen3.5 0.8B 온디바이스 비디오 최초, Qualcomm 13B 실증 | Deep |
| 스팸피싱감지(통화전) | 🟡 주목 | LG U+ Anti-DeepVoice GLOMO 수상, KT 97.2%, Virgin Media O2 10억건 탐지 | Deep |
| OnDevice 동형암호 | 🟡 주목 | LG U+×CryptoLab CKKS+ 4.5세대 AICC 상용화, Niobium FHE ASIC 양산, NIST Th-FHE 진입 | Deep |
| 실시간 화자분할 | 🟢 평온 | Pyannote 3.1 선두 유지, AssemblyAI 30% 개선 | Quick |
| OCR 이미지 스팸 | 🟢 평온 | 특이사항 없음 | Quick |
| Secure Vector Search | 🟢 평온 | Apple Private NN Search 외 구조적 변화 없음 | Quick |

---

## 🟢 Quick 요약 (변화 미미)

### 실시간 화자분할(2인)
- Pyannote 3.1이 DER 11~19%로 선두 유지. AssemblyAI가 자체 화자 임베딩 모델로 노이즈/원거리 환경 정확도 30% 개선. 실시간 2인 분리 특화 돌파구는 없음.

### OCR 이미지 스팸 차단
- 최근 1주간 유의미한 기술/시장 변화 없음. 기존 OCR+ML 기반 탐지 유지.

### Secure Vector Search
- Apple Private NN Search(암호화 벡터 kNN 검색) 유지. IronCore Labs가 프라이버시 보존 AI 임베딩 암호화 솔루션을 제공 중이나 구조적 돌파 없음.

---

## 🔴 Deep 심층 분석

### OnDevice 양자암호 (PQC) — 🔴 긴급

#### 기술 동향

1. **Google PLANTS/MTC — PQC TLS 인증서 아키텍처 혁신.**
   Google이 PQC 인증서 크기 문제를 해결하는 Merkle Tree Certificates(MTC) 아키텍처와 IETF PLANTS 워킹그룹을 발표했다. 기존 X.509에 PQC 서명(ML-DSA-44)을 삽입하면 TLS 핸드셰이크 데이터가 **14,700바이트**로 팽창하지만, MTC는 736바이트 경량 포함 증명으로 해결한다 [[G-01]](#ref-g-01), [[G-02]](#ref-g-02). 롤아웃 3단계: Phase 1(Google-Cloudflare 타당성 검토 진행 중) → Phase 2(Q1 2027 CT Log 부트스트래핑) → Phase 3(Q3 2027 Chrome CQRS 온보딩).

2. **Cloudflare 세계 최초 완전 PQC SASE.**
   IPsec IKEv2에 하이브리드 ML-KEM을 적용해 SASE 전 계층을 PQC화했다. 인간 생성 TLS 트래픽의 **60% 이상**이 하이브리드 ML-KEM 사용 중이다 [[G-03]](#ref-g-03).

3. **Microsoft PQC APIs GA.**
   Windows 11(24H2, 25H2), Windows Server 2025, .NET 10에서 ML-KEM·ML-DSA API가 정식 출시됐다 [[G-04]](#ref-g-04).

4. **규제 이중 마감.**
   NIST CMVP가 2026-09-21에 FIPS 140-2를 Historical로 이동하고, NSA CNSA 2.0은 2027-01부터 신규 시스템에 양자내성 알고리즘을 의무화한다 [[G-05]](#ref-g-05), [[G-06]](#ref-g-06).

5. **Google 내부 ML-KEM 전환 완료.**
   모든 내부 트래픽 키 교환을 X25519+ML-KEM-768(X-Wing KEM) 하이브리드로 전환 완료. 대규모 PQC 배포의 기술적 실현 가능성을 실증했다 [[G-07]](#ref-g-07).

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Google | PLANTS/MTC 아키텍처 발표(14,700B→736B). 전사 내부 트래픽 ML-KEM 전환 완료 | [[G-01]](#ref-g-01), [[G-02]](#ref-g-02), [[G-07]](#ref-g-07) |
| Cloudflare | 세계 최초 완전 PQC SASE. IPsec IKEv2 하이브리드 ML-KEM 추가, 트래픽 60%+ 적용 | [[G-03]](#ref-g-03) |
| Microsoft | ML-KEM·ML-DSA API GA (Windows 11/Server 2025/.NET 10). ADCS PQC 2026 초 목표 | [[G-04]](#ref-g-04) |
| Samsung | S3SSE2A: 업계 최초 HW PQC SE, CC EAL6+, 소프트웨어 대비 17배 속도. CES 2026 사이버보안 혁신상 | [[G-08]](#ref-g-08) |
| Thales | 세계 최초 5G SIM/eSIM OTA PQC 원격 업그레이드 실증(2026-03-02). 기기 교체 불필요 | [[G-09]](#ref-g-09) |
| Apple | iMessage PQ3 기배포(ML-KEM+Kyber 하이브리드, 50메시지/7일 키 로테이션) | [[G-10]](#ref-g-10) |
| SKT | QKD+PQC 하이브리드 세계 최초 출시, Q-HSM 양산, Thales와 5G SA SUPI PQC 실증 | [[G-11]](#ref-g-11) |
| NIST | FIPS 140-2 Historical 이전(2026-09-21). HQC 5번째 PQC 표준 초안 2026년 예정 | [[G-05]](#ref-g-05), [[G-12]](#ref-g-12) |

#### 시장 시그널
- PQC 시장 2026년 약 $5.1억, 2030년 $28~46억 전망(CAGR 39~46%) [[G-13]](#ref-g-13)
- 하이브리드(고전+PQC) 방식이 사실상 표준 경로로 고착화. 순수 PQC 배포는 극히 드묾 [[G-14]](#ref-g-14)
- 기업 사이버보험에서 PQC 전환 계획 부재 시 보험료 인상/양자 면책 조항 삽입 움직임 [[G-14]](#ref-g-14)
- NSA CNSA 2.0(2027-01) + NIST FIPS 140-2 종료(2026-09) 이중 마감이 기업 조달 전환 압박 [[G-05]](#ref-g-05), [[G-06]](#ref-g-06)
- Thales 5G SIM OTA PQC 업그레이드: 수십억 대 기배포 기기의 양자내성 전환 경로 개방 [[G-09]](#ref-g-09)

#### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| Lattice-Based Cryptographic Accelerators (MDPI, 2026-01) | FPGA/ASIC NTT 가속기 종합 리뷰. 다중 스킴 지원 설계가 면적 효율 81.85% | [[P-01]](#ref-p-01) |
| Performance Analysis of PQC Algorithms (arXiv:2503.12952) | ARM Cortex-A53 ML-KEM 150 ops/s vs Intel i7 85,000 ops/s. 모바일 저레이턴시 실증 | [[P-02]](#ref-p-02) |
| PQC in the 5G Core (arXiv:2512.20243) | 하이브리드 X25519+Kyber768: +2.3KB, 레이턴시 10~20ms 추가. 5G 가용성 영향 미미 | [[P-03]](#ref-p-03) |
| Formal Analysis of iMessage PQ3 (USENIX Security '25) | PQ3 양자내성·순방향 비밀성 형식 검증 완료 | [[P-04]](#ref-p-04) |

#### 전략적 시사점

**기회**
- Google PLANTS/MTC는 PQC 인증서 성능 장벽을 제거. 국내 PKI/CA 사업자는 2026년 내 MTC 호환 인프라 준비 착수 필요
- Thales OTA 5G SIM PQC 업그레이드는 SKT/KT에게 수천만 단말의 양자내성 전환을 기기 교체 없이 추진할 수 있는 경로 제공
- Samsung S3SSE2A(17배 속도)가 온디바이스 HW-PQC 레퍼런스를 확립. Exynos SoC 통합으로 2~3년 내 완전 HW-PQC 플래그십 전망

**위협**
- 하이브리드 모드 처리량 약 절반 감소. 리소스 제한 IoT 기기(ARM Cortex-A53 150 ops/s)에서 최적화 검증 필수
- FIPS 140-3 PQC 인증 모듈 부재가 금융/의료/공공 조달을 지연시킬 수 있음
- Google MTC/CQRS는 기존 X.509 PKI를 우회하는 새 신뢰 체계 — 기존 인증서 비즈니스 모델 파괴 리스크

---

### OnDevice sLM — 🟡 주목

#### 기술 동향

1. **Gemma 3n 오픈소스 생태계 통합 완료.**
   HuggingFace, MLX, llama.cpp, Ollama 등 주요 라이브러리에 전체 통합됐다. MatFormer(탄성 추론) + PLE(레이어별 임베딩 분리) 아키텍처로 E4B(8B 파라미터)를 3GB 메모리로 실행한다 [[G-15]](#ref-g-15), [[G-16]](#ref-g-16). MediaTek Dimensity 9500 NPU에서 E2B 기준 **prefill 1,600 tok/sec** 실측 [[G-17]](#ref-g-17).

2. **Qwen3.5 Small Apache 2.0 공개(2026-03-02).**
   0.8B 모델이 **최초로 온디바이스 비디오 처리**(60초, 8FPS)를 지원하며 "서브 1B = 텍스트 전용" 한계를 돌파했다. Gated DeltaNet + Full Attention 하이브리드로 262K 컨텍스트. 9B 모델이 GPQA Diamond에서 GPT-OSS-120B를 13.5배 작은 크기로 상회 [[G-18]](#ref-g-18), [[G-19]](#ref-g-19).

3. **Persistent Q4 KV Cache 논문(arXiv 2603.04428).**
   에지 멀티에이전트 추론에서 KV 캐시를 4-bit 양자화하여 디스크 영속 저장. Apple M4 Pro에서 Gemma 3 12B 기준 TTFT **22~136배 단축** [[P-05]](#ref-p-05).

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Google | Gemma 3n E2B/E4B 오픈소스 생태계 통합 완료. Gemma 3 1B 모바일 GPU 2,585 tok/sec | [[G-15]](#ref-g-15) |
| Alibaba | Qwen3.5 0.8B~9B Apache 2.0. 0.8B 최초 온디바이스 비디오, 9B가 GPT-OSS-120B 초과 | [[G-18]](#ref-g-18), [[G-19]](#ref-g-19) |
| Qualcomm | MWC 2026: Snapdragon 8 Elite Gen 5 NPU ~100 TOPS, 13B 완전 온디바이스 실증 | [[G-20]](#ref-g-20) |
| MediaTek | Dimensity 9500 NPU ~50 TOPS, Gemma 3n E2B 1,600 tok/sec. Google LiteRT 통합 | [[G-17]](#ref-g-17) |
| Apple | Foundation Models ~3B 온디바이스(iOS 26). 2-bit QAT, KV 캐시 공유 최적화 | [[G-21]](#ref-g-21) |
| Samsung | Galaxy S26 + Gauss2 Compact. Gemini/Perplexity/Bixby+Gauss2 3원 구도 | [[G-22]](#ref-g-22) |
| Meta | ExecuTorch 1.0 GA, 수십억 사용자 앱에서 작동. React Native ExecuTorch 공개 | [[G-23]](#ref-g-23) |
| SKT | MWC 2026 Edge AI를 3대 인프라 축(AIDC, GPUaaS, Edge AI)으로 선언 | [[G-24]](#ref-g-24) |

#### 시장 시그널
- 멀티모달 온디바이스 sLM이 Apache 2.0/오픈소스로 진입 장벽 제거 — 파인튜닝 상업화 현실화 [[G-15]](#ref-g-15), [[G-18]](#ref-g-18)
- 0.8B 멀티모달 임계값 돌파 — 웨어러블/IoT/스마트홈 AI 파이프라인 설계 가능성 개방 [[G-18]](#ref-g-18)
- Qualcomm Snapdragon Wear Elite: 웨어러블 최초 전용 NPU(2B, 10 tok/sec). 스마트워치급 온디바이스 LLM 시작점 [[G-20]](#ref-g-20)
- SLM 시장 온프레미스/엣지 배포 51.85% 점유, CAGR 27.25%(2031년까지). Gartner: 2027년 SLM 사용량이 LLM 3배 전망 [[G-25]](#ref-g-25)
- 하이브리드 Attention(Gated DeltaNet, Mamba-2) 아키텍처가 복수 플레이어에서 동시 채택, 표준화 추세 [[G-19]](#ref-g-19)

#### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| Persistent Q4 KV Cache (arXiv 2603.04428) | 에지 멀티에이전트 TTFT 22~136배 단축. M4 Pro에서 FP16 대비 4배 메모리 절감 | [[P-05]](#ref-p-05) |
| On-Device LM Inference Feasibility (arXiv 2503.09114) | Raspberry Pi 5/Jetson Orin Nano 실측. 양자화가 병목 완화하나 완전 제거 못함 | [[P-06]](#ref-p-06) |
| Oaken: Hybrid KV Cache Quantization (ISCA 2026) | 온·오프라인 혼합 KV 캐시 양자화, A100 대비 1.58배 처리량. 정확도 손실 0.54% | [[P-07]](#ref-p-07) |

#### 전략적 시사점

**기회**
- Gemma 3n + Qwen3.5 오픈소스 멀티모달 sLM으로 엔터프라이즈 내부망 파인튜닝 즉시 가능
- Persistent KV Cache 기법이 에지 멀티에이전트 추론의 실용 임계를 돌파 — 복잡한 에이전틱 태스크 설계 가능

**위협**
- Alibaba가 서브 1B 시장에서도 주도권 확보 시작. 중국 오픈소스 생태계의 글로벌 표준 선점 리스크
- 칩-프레임워크-모델 수직 통합(Qualcomm/MediaTek + Google LiteRT) 강화로 비벤더 독립 솔루션 입지 축소

---

### 스팸피싱감지(통화전) — 🟡 주목

#### 기술 동향

1. **LG U+ Anti-DeepVoice 세계 최초 온디바이스 상용화.**
   MWC 2026에서 ixi-O AI 에이전트에 통화 시작 수 초 내 딥보이스 실시간 감지 기능을 공개. 클라우드 전송 없이 단말 내 처리. GSMA GLOMO 2026 CTO Choice 수상 [[G-26]](#ref-g-26), [[G-27]](#ref-g-27).

2. **KT Who Who 정확도 97.2% 도달(Q4 2025).**
   AI 문맥 탐지 + 화자인식 + 딥보이스 탐지 3중 체계. 연간 2,000억원 피해 예방 목표 [[G-28]](#ref-g-28).

3. **Samsung + 이통 3사 협력.**
   One UI 8.0 Galaxy에 경찰청 3만+ 녹취 학습 온디바이스 AI 내장. '의심/위험' 2단계 경보, 한국 전용 [[G-29]](#ref-g-29).

4. **Hiya AI Call Assistant + Virgin Media O2 10억건.**
   통화 중 라이브/딥페이크 스캠 실시간 차단 출시. Virgin Media O2와 Call Defence 서비스로 10억건 탐지 달성(월 7,000만건) [[G-30]](#ref-g-30), [[G-31]](#ref-g-31).

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| LG Uplus | Anti-DeepVoice 세계 최초 온디바이스, GLOMO CTO Choice 수상 | [[G-26]](#ref-g-26), [[G-27]](#ref-g-27) |
| KT | Who Who 97.2% 정확도, AI 3중 체계, 연간 2,000억원 피해 예방 목표 | [[G-28]](#ref-g-28) |
| SKT | 2025년 11억건 차단, Aida Phone 실시간 AI '의심/위험' 2단계 알림 | [[G-32]](#ref-g-32) |
| Samsung | One UI 8.0 경찰청 데이터 학습 온디바이스 AI. 이통3사 협력 체계 | [[G-29]](#ref-g-29) |
| Hiya | AI Call Assistant(딥페이크 실시간 차단) 출시. Virgin Media O2와 10억건 달성 | [[G-30]](#ref-g-30), [[G-31]](#ref-g-31) |
| FCC | AI 생성 음성 로보콜 불법화. Robocall Mitigation DB 강화(2026-02-05 발효) | [[G-33]](#ref-g-33) |

#### 시장 시그널
- Hiya 'State of the Call 2026': 미국인 25%가 딥페이크 음성 통화 수신. 38%가 보호 불충분 시 이통사 교체 의향 [[G-34]](#ref-g-34)
- 딥페이크 지원 사기 손실 2027년 $40B(약 55조원) 전망. 55세+ 시니어 피해 평균 $1,298/건 [[G-35]](#ref-g-35)
- AI 생성 피싱 이메일 클릭률 기존 대비 4배. 분석 이메일 82.6%가 AI 포함 [[G-36]](#ref-g-36)
- 음성 클로닝이 '구별 불가 임계점' 돌파 — 수 초 오디오로 억양/리듬/감정/호흡 재현 가능 [[G-37]](#ref-g-37)

#### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| AudioFakeNet (MDPI Algorithms, 2025) | CNN+LSTM+Multi-Head Attention 하이브리드, MFCC 기반 EER SOTA | [[P-08]](#ref-p-08) |
| Audio Deepfake Detection Survey (PMC, 2025) | ASVspoof 2019~2025 기반 최신 탐지 연구 종합 서베이 | [[P-09]](#ref-p-09) |
| VoiceRadar (NDSS 2025) | 실환경 딥보이스 탐지 레이더 프레임워크, 실시간성 강조 | [[P-10]](#ref-p-10) |

#### 전략적 시사점

**기회**
- LG U+ GLOMO 수상으로 온디바이스 Anti-DeepVoice가 글로벌 표준 기술로 인정. 해외 진출 레퍼런스
- KT 97.2% 정확도는 마케팅 차별화 활용 가능. Virgin Media O2 모델은 네트워크 레이어 협력 확대 참조

**위협**
- 소비자 38% 이통사 교체 의향 — 탐지 품질 격차가 가입자 이탈로 직결
- McAfee/Hiya 등 독립 보안 플랫폼이 동등 기능 제공 — 앱 기반 고객 락인 전략 희석
- 크로스-데이터셋 일반화 한계 — 새 생성 모델 출현 시 탐지율 급락 위험

---

### OnDevice 동형암호 — 🟡 주목

#### 기술 동향

1. **LG U+ × CryptoLab CKKS+ 상용화 발표.**
   MWC 2026에서 AICC·AI 에이전트 Xio에 CKKS+ 4.5세대 동형암호 적용 PoC를 공식 발표. 행렬 연산 암호화 실행, "실시간 지연 없는 수준"으로 온디바이스 경량화 달성 주장 [[E-01]](#ref-e-01), [[G-38]](#ref-g-38).

2. **NIST Threshold FHE 표준화 진입.**
   CryptoLab Damien Stehlé가 MPTS 2026에서 CKKS 기반 임계 FHE 발표. 신뢰 딜러 없이 분산 키 생성, AES128 임계 암호화 0.1초 미만 [[G-39]](#ref-g-39).

3. **Discrete-CKKS 논문(ePrint 2026/450).**
   이진 벡터 기반 mod-2 정수 연산을 다항식으로 처리, 기존 대비 **3배 낮은 지연**. 도메인 스위칭으로 실수/정수 연산 겸용 [[P-11]](#ref-p-11).

4. **EUROCRYPT 2026 부트스트래핑.**
   Fourier Extension 기반 함수형 부트스트래핑으로 정밀도 **10~27비트 향상**, 지연 1.1~2배 단축 [[P-12]](#ref-p-12).

5. **Niobium FHE ASIC.**
   Samsung Foundry 8nm(8LPU) 공정 양산 계약 약 100억원 확인 [[G-40]](#ref-g-40).

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| CryptoLab | CKKS+ 4.5세대. NIST MPTS 2026 Th-FHE 발표. LG U+/UClone/Macrogen 다중 파트너십 | [[E-01]](#ref-e-01), [[G-39]](#ref-g-39) |
| LG Uplus | MWC 2026 동형암호 AICC·Xio PoC 공식화. 통신사 AICC 동형암호 세계 첫 사례 | [[E-01]](#ref-e-01), [[G-38]](#ref-g-38) |
| Niobium + SEMIFIVE | 세계 최초 상용 FHE ASIC, Samsung 8nm 양산. 약 100억원 규모 | [[G-40]](#ref-g-40) |
| OpenFHE | v1.5.0 개발 버전(2026-02-26). BFV/BGV/CKKS/TFHE 전 스킴 지원 | [[G-41]](#ref-g-41) |

#### 시장 시그널
- LG U+가 통신사 AICC 동형암호 적용 세계 첫 사례로 포지셔닝 [[E-01]](#ref-e-01)
- Niobium FHE ASIC 상용화 시 서버/에지 FHE 처리 속도 수십 배 향상 전망 [[G-40]](#ref-g-40)
- CryptoLab이 글로벌 벤처·통신사·스타트업 생태계를 동시 공략하며 한국계 FHE 스택의 글로벌 공급망 형성
- NIST Threshold Call에 FHE 포함 확정 — FHE 표준화 2~3년 내 가시권 진입

#### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| Discrete-CKKS (ePrint 2026/450) | 정수 연산 지연 3배 단축. 도메인 스위칭 지원 | [[P-11]](#ref-p-11) |
| Fourier Extension Bootstrapping (ePrint 2026/367) | 부트스트래핑 정밀도 10~27비트 향상. EUROCRYPT 2026 채택 | [[P-12]](#ref-p-12) |
| P2P-CKKS (Springer) | 동적 power-of-two 패딩, 비표준 벡터 100% 성공률 | [[P-13]](#ref-p-13) |
| Threshold FHE from CKKS (NIST MPTS 2026) | 분산 키 생성, AES128 임계 암호화 0.1초 미만 | [[P-14]](#ref-p-14) |

#### 전략적 시사점

**기회**
- CKKS+ 온디바이스 경량화 실증 시 통신사 AICC 프라이버시 보장 서비스 조기 상용화. LG U+가 6~12개월 선점
- FHE ASIC 상용화로 에지-서버 하이브리드 FHE 모델이 현실적 대안으로 부상

**위협**
- LG U+×CryptoLab은 PoC 단계이며 독립 검증 미완료. "실시간 지연 없음"은 단일 소스 주장 [C]
- FHE 연산 비용이 평문 대비 10³~10⁶배 — 실제 스마트폰 적용까지 추가 HW 혁신 필요

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **양자암호 + 동형암호 시너지**: PQC 전환과 FHE 상용화가 동시 진행 중이며, CryptoLab이 양쪽 모두에서 핵심 역할(CKKS+ HE + PQC 상용화 파트너십). 통신사가 "양자내성 + 데이터 프라이버시" 이중 보안을 원스톱으로 제공할 수 있는 구도가 형성되고 있다.

2. **온디바이스 AI + 온디바이스 보안의 합류**: OnDevice sLM의 급속한 발전(Gemma 3n 2GB, Qwen3.5 0.8B 비디오)과 온디바이스 보안(Anti-DeepVoice, HW PQC SE, CKKS+ 경량화)이 동일한 "단말 내 처리" 방향으로 수렴하고 있다. 에지 AI와 에지 보안의 통합 아키텍처가 차세대 경쟁력이 될 전망이다.

3. **한국 통신사의 글로벌 리더십 부상**: LG U+(Anti-DeepVoice GLOMO, 동형암호 AICC), SKT(QKD+PQC 하이브리드, Edge AI 인프라), KT(97.2% 탐지 정확도)가 MWC 2026에서 각각 차별적 포지셔닝을 확보했다. 보안 AI 분야에서 한국 통신사가 글로벌 레퍼런스를 창출하고 있다.

### 후속 조치 제안

- 🔴 **OnDevice 양자암호**: `/wtis standard` Go/No-Go 검증 권장. NIST/NSA 이중 마감(2026-09, 2027-01) 대응 긴급성 높음
- 🟡 Obsidian 동기화: `/obsidian-bridge` 실행으로 리포트 반영

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | The Hacker News — Google Develops Merkle Tree Certificates | [링크](https://thehackernews.com/2026/03/google-develops-merkle-tree.html) | news | 2026-03 | [B] |
| <a id="ref-g-02"></a>G-02 | Google Security Blog — Quantum-safe HTTPS | [링크](https://security.googleblog.com/2026/02/cultivating-robust-and-efficient.html) | blog | 2026-02 | [A] |
| <a id="ref-g-03"></a>G-03 | InfoQ — Cloudflare Post-Quantum IPsec | [링크](https://www.infoq.com/news/2026/03/cloudflare-post-quantum-ipsec/) | news | 2026-03 | [B] |
| <a id="ref-g-04"></a>G-04 | Microsoft — PQC APIs GA | [링크](https://techcommunity.microsoft.com/blog/microsoft-security-blog/post-quantum-cryptography-apis-now-generally-available-on-microsoft-platforms/4469093) | official | 2026 | [A] |
| <a id="ref-g-05"></a>G-05 | postquantum.com — US PQC Regulatory Framework 2026 | [링크](https://postquantum.com/quantum-policies/us-pqc-regulatory-framework-2026/) | news | 2026 | [B] |
| <a id="ref-g-06"></a>G-06 | NSA — CNSA 2.0 Algorithms | [링크](https://media.defense.gov/2025/May/30/2003728741/-1/-1/0/CSA_CNSA_2.0_ALGORITHMS.PDF) | official | 2025 | [A] |
| <a id="ref-g-07"></a>G-07 | Kiteworks — Google Quantum Threats 2026 | [링크](https://www.kiteworks.com/cybersecurity-risk-management/google-quantum-computing-encryption-threat-post-quantum-cryptography/) | news | 2026-02 | [B] |
| <a id="ref-g-08"></a>G-08 | Samsung Semiconductor — S3SSE2A HW PQC | [링크](https://semiconductor.samsung.com/news-events/tech-blog/ces-innovations-awards-2026-honoree-interview-s3sse2a/) | official | 2026-01 | [A] |
| <a id="ref-g-09"></a>G-09 | The Quantum Insider — Thales 5G SIM PQC OTA | [링크](https://thequantuminsider.com/2026/03/02/thales-remote-post-quantum-5g-sim-upgrade/) | news | 2026-03-02 | [B] |
| <a id="ref-g-10"></a>G-10 | Apple Security — iMessage PQ3 | [링크](https://security.apple.com/blog/imessage-pq3/) | official | 2024-02 | [A] |
| <a id="ref-g-11"></a>G-11 | SKT Newsroom — Quantum-safe future | [링크](https://news.sktelecom.com/en/853) | official | 2024 | [A] |
| <a id="ref-g-12"></a>G-12 | Utimaco — NIST HQC 5th algorithm | [링크](https://utimaco.com/news/blog-posts/pqc-news-nist-announces-hqc-fifth-algorithm-be-standardized) | news | 2025 | [B] |
| <a id="ref-g-13"></a>G-13 | GlobeNewswire — PQC Industry Report 2026 | [링크](https://www.globenewswire.com/news-release/2026/02/23/3242432/28124/en/Post-Quantum-Cryptography-Industry-Research-Report-2026-PQC-Transitions-from-Research-Concept-to-Core-Cybersecurity-Pillar-Amid-Rising-Quantum-Computing-Breakthroughs.html) | news | 2026-02-23 | [C] |
| <a id="ref-g-14"></a>G-14 | Graygroup — PQC Enterprise Guide 2026 | [링크](https://www.graygroupintl.com/blog/post-quantum-cryptography-enterprise-guide/) | blog | 2026 | [C] |
| <a id="ref-g-15"></a>G-15 | HuggingFace Blog — Gemma 3n fully available | [링크](https://huggingface.co/blog/gemma3n) | news | 2026-02-27 | [A] |
| <a id="ref-g-16"></a>G-16 | Google Developers — Gemma 3n developer guide | [링크](https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/) | news | 2025-05 | [A] |
| <a id="ref-g-17"></a>G-17 | Google Developers — MediaTek NPU and LiteRT | [링크](https://developers.googleblog.com/mediatek-npu-and-litert-powering-the-next-generation-of-on-device-ai/) | news | 2025-12 | [A] |
| <a id="ref-g-18"></a>G-18 | MarkTechPost — Qwen 3.5 Small Models | [링크](https://www.marktechpost.com/2026/03/02/alibaba-just-released-qwen-3-5-small-models-a-family-of-0-8b-to-9b-parameters-built-for-on-device-applications/) | news | 2026-03-02 | [B] |
| <a id="ref-g-19"></a>G-19 | StableLearn — Qwen3.5: 9B Beats 120B | [링크](https://stable-learn.com/en/qwen35-native-multimodal-agent-model/) | news | 2026-03 | [B] |
| <a id="ref-g-20"></a>G-20 | DEV Community — MWC 2026 Developer AI Roundup | [링크](https://dev.to/giolaq/mwc-2026-what-every-developer-building-ai-features-should-know-1a45) | news | 2026-03 | [B] |
| <a id="ref-g-21"></a>G-21 | Apple ML Research — Foundation Language Models 2025 | [링크](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates) | official | 2025 | [A] |
| <a id="ref-g-22"></a>G-22 | Samsung Newsroom — Galaxy AI at MWC 2026 | [링크](https://news.samsung.com/global/samsung-advances-galaxy-ai-and-its-connected-ecosystem-at-mwc-2026) | official | 2026-03 | [A] |
| <a id="ref-g-23"></a>G-23 | Arm Newsroom — ExecuTorch 1.0 GA | [링크](https://newsroom.arm.com/news/executorch-1-0-ga-release-edge-ai) | news | 2025-10 | [A] |
| <a id="ref-g-24"></a>G-24 | Korea Tech Today — Korea's AI-Telco Moment at MWC 2026 | [링크](https://koreatechtoday.com/koreas-ai-telco-moment-strategic-signaling-at-mwc-2026/) | news | 2026-03 | [B] |
| <a id="ref-g-25"></a>G-25 | Calmops — SLMs Complete Guide 2026 | [링크](https://calmops.com/ai/small-language-models-slm-complete-guide-2026/) | news | 2026 | [C] |
| <a id="ref-g-26"></a>G-26 | Korea IT Times — LG Uplus Anti-DeepVoice at MWC26 | [링크](https://www.koreaittimes.com/news/articleView.html?idxno=151439) | news | 2026-03-03 | [B] |
| <a id="ref-g-27"></a>G-27 | Digital Today — LG Uplus GLOMO CTO Choice | [링크](https://www.digitaltoday.co.kr/en/view/18425/mwc26-lg-uplus-wins-three-glomo-awards-including-cto-choice) | news | 2026-03 | [B] |
| <a id="ref-g-28"></a>G-28 | The Fast Mode — KT AI Voice Phishing Detection | [링크](https://www.thefastmode.com/technology-solutions/39153-kt-unveils-real-time-ai-voice-phishing-protection) | news | 2026-03 | [B] |
| <a id="ref-g-29"></a>G-29 | Android Police — Samsung Galaxy AI voice phishing detection | [링크](https://www.androidpolice.com/samsung-ai-voice-phishing-scam-detection/) | news | 2026-02 | [B] |
| <a id="ref-g-30"></a>G-30 | Hiya — AI Call Assistant launch | [링크](https://www.hiya.com/en-ca/newsroom/press-releases/hiya-launches-first-ai-call-assistant-that-stops-live-and-deepfake-scams-in-real-time) | IR | 2025 | [A] |
| <a id="ref-g-31"></a>G-31 | Virgin Media O2 — 1 billion scam calls detected | [링크](https://news.virginmediao2.co.uk/ai-helps-virgin-media-o2-detect-and-flag-1-billion-suspected-scam-and-spam-calls-to-customers/) | IR | 2026-03-10 | [A] |
| <a id="ref-g-32"></a>G-32 | Telecompaper — SKT AI-driven spam blocking | [링크](https://www.telecompaper.com/news/skt-reveals-rise-in-ai-driven-blocking-of-spam-and-voice-phishing-attempts--1558993) | news | 2026-03 | [B] |
| <a id="ref-g-33"></a>G-33 | FCC — AI-Generated Voices in Robocalls Illegal | [링크](https://www.fcc.gov/document/fcc-makes-ai-generated-voices-robocalls-illegal) | official | 2024-02 | [A] |
| <a id="ref-g-34"></a>G-34 | Hiya — State of the Call 2026 | [링크](https://natlawreview.com/press-releases/state-call-2026-ai-deepfake-voice-calls-hit-1-4-americans-consumers-say) | report | 2026-03-02 | [B] |
| <a id="ref-g-35"></a>G-35 | CX Today — Voice Trust Collapse 2026 | [링크](https://www.cxtoday.com/security-privacy-compliance/the-voice-trust-collapse-and-deepfake-voice-fraud/) | news | 2026-03 | [B] |
| <a id="ref-g-36"></a>G-36 | StrongestLayer — AI-Generated Phishing Enterprise Threat | [링크](https://www.strongestlayer.com/blog/ai-generated-phishing-enterprise-threat) | blog | 2026-03 | [C] |
| <a id="ref-g-37"></a>G-37 | Fortune — 2026 Deepfakes Outlook | [링크](https://fortune.com/2025/12/27/2026-deepfakes-outlook-forecast/) | news | 2025-12 | [B] |
| <a id="ref-g-38"></a>G-38 | Korea IT Times — LG Uplus HE+Quantum at MWC26 | [링크](https://www.koreaittimes.com/news/articleView.html?idxno=151253) | news | 2026-03-04 | [B] |
| <a id="ref-g-39"></a>G-39 | NIST CSRC — Threshold FHE from CKKS (MPTS 2026) | [링크](https://csrc.nist.gov/presentations/2026/mpts2026-2b4) | official | 2026-01 | [A] |
| <a id="ref-g-40"></a>G-40 | PR Newswire — SEMIFIVE + Niobium FHE Accelerator | [링크](https://www.prnewswire.com/news-releases/semifive-partners-with-niobium-to-develop-fhe-accelerator-driving-us-market-expansion-302692312.html) | news | 2026-02-19 | [A] |
| <a id="ref-g-41"></a>G-41 | GitHub — OpenFHE v1.5.0 | [링크](https://github.com/openfheorg/openfhe-development) | official | 2026-02-26 | [A] |
| <a id="ref-e-01"></a>E-01 | Asia Business Daily — LG Uplus × CryptoLab MWC 2026 | [링크](https://www.asiae.co.kr/en/article/2026031008212144575) | IR | 2026-03-04 | [A] |
| <a id="ref-p-01"></a>P-01 | Bathen et al. — Lattice-Based Crypto Accelerators (MDPI) | [링크](https://www.mdpi.com/2079-9292/15/2/475) | paper | 2026-01 | [A] |
| <a id="ref-p-02"></a>P-02 | arXiv:2503.12952 — PQC Performance Analysis & Deployment | [링크](https://arxiv.org/html/2503.12952v1) | paper | 2026-03 | [A] |
| <a id="ref-p-03"></a>P-03 | arXiv:2512.20243 — PQC in the 5G Core | [링크](https://arxiv.org/html/2512.20243v1) | paper | 2025-12 | [A] |
| <a id="ref-p-04"></a>P-04 | Linker — iMessage PQ3 Formal Analysis (USENIX) | [링크](https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-595-linker.pdf) | paper | 2025 | [A] |
| <a id="ref-p-05"></a>P-05 | arXiv:2603.04428 — Persistent Q4 KV Cache Multi-Agent Edge | [링크](https://arxiv.org/abs/2603.04428) | paper | 2026-03 | [B] |
| <a id="ref-p-06"></a>P-06 | arXiv:2503.09114 — On-Device LM Inference Feasibility | [링크](https://arxiv.org/abs/2503.09114) | paper | 2026-03 | [B] |
| <a id="ref-p-07"></a>P-07 | Oaken — Hybrid KV Cache Quantization (ISCA 2026) | [링크](https://dl.acm.org/doi/10.1145/3695053.3731019) | paper | 2026 | [A] |
| <a id="ref-p-08"></a>P-08 | Boucherit et al. — AudioFakeNet (MDPI Algorithms) | [링크](https://www.mdpi.com/1999-4893/18/11/716) | paper | 2025-11 | [A] |
| <a id="ref-p-09"></a>P-09 | PMC — Audio Deepfake Detection Survey | [링크](https://pmc.ncbi.nlm.nih.gov/articles/PMC11991371/) | paper | 2025-03 | [A] |
| <a id="ref-p-10"></a>P-10 | VoiceRadar — Voice Deepfake Detection (NDSS 2025) | [링크](https://www.ndss-symposium.org/wp-content/uploads/2025-3389-paper.pdf) | paper | 2025 | [A] |
| <a id="ref-p-11"></a>P-11 | Rovida — Discrete-CKKS (ePrint 2026/450) | [링크](https://eprint.iacr.org/2026/450) | paper | 2026-03 | [A] |
| <a id="ref-p-12"></a>P-12 | Bian et al. — Fourier Extension Bootstrapping (ePrint 2026/367) | [링크](https://eprint.iacr.org/2026/367) | paper | 2026-03 | [A] |
| <a id="ref-p-13"></a>P-13 | P2P-CKKS (Springer JESIT) | [링크](https://link.springer.com/article/10.1186/s43067-025-00276-z) | paper | 2025-12 | [A] |
| <a id="ref-p-14"></a>P-14 | Stehlé — Threshold FHE from CKKS (NIST MPTS 2026) | [링크](https://csrc.nist.gov/csrc/media/presentations/2026/mpts2026-2b4/images-media/mpts2026-2b4-slides-thfhe-ckks-stehle.pdf) | paper | 2026-01 | [A] |
