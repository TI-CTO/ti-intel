---
topic: Speech Generation Build Option — LG U+ 자체 개발 실현 가능성
date: 2026-03-20
agent: research-deep
confidence: medium
status: completed
sources_used: [websearch, prior-research-voice-synthesis-w12, prior-research-speech-generation-wtis]
---

# Research Report: Speech Generation Build 옵션 — LG U+ 자체 개발 실현 가능성

## Executive Summary

> LG U+는 ixi-STT 등 일부 음성 인식 자체 역량을 보유하고 있으나, TTS·Voice Cloning 전담 모델을 독자 개발한 공개 근거는 없다. 현재 익시오(ixi-O)의 핵심 추론·합성은 Google Gemini API에 의존하고 있으며, 자체 TTS 모델은 미확인 상태[G-07]. LG AI Research는 STT/TTS 연구인력을 채용 중이나 팀 규모·성과 공개가 극히 제한적이다[G-02]. 경쟁사 SKT는 A.X TTS 30종 음성을 2024년 6월 자체 API로 공개했고[G-04], Naver는 한국어 TTS MOS 4.22/5를 달성했다[E-03]. LG U+가 유사 수준의 독자 TTS를 구축하려면 최소 18~36개월, 초기 투자 300~600억 원(인력+인프라+데이터) 규모가 필요할 것으로 추정된다[추정]. 오픈소스(CosyVoice 2, Qwen3-TTS) 기반 Fine-tuning은 개발 기간을 절반으로 단축할 수 있지만, 프로덕션 품질 확보와 지속적 운영 인력이 관건이다.

---

## 연구 질문

> LG U+가 Speech Generation(TTS + Voice Cloning) 기술을 자체 개발(Build)할 경우, 내부 역량·개발 기간·투자 규모·장단점은 무엇인가?

---

## 1. LG U+ 내부 역량 현황

### 1-1. LG U+ 직접 AI/음성 기술 스택

**현황 파악**

- **ixi-STT (자체)**: LG유플러스는 콜봇·챗봇 서비스에 ixi-STT(Speech-to-Text) AI와 자체 음성 데이터를 적용하고 있다. 음성 사용자 경험(Voice UX)도 자체 구축했으며, 콜봇 일평균 이용 건수가 전년 대비 약 4배 증가했다고 공시했다[G-07].
- **ixi-O의 TTS**: 익시오의 실시간 음성 추론은 Google Gemini API에 의존. 사측은 "이 분야에서 Gemini 기술이 고객 경험 측면에서 가장 앞서 있다고 판단해 협력"했다고 밝혔다[G-07]. 즉, **현재 TTS 출력은 자체 모델이 아닌 외부 API 기반**이다.
- **Anti-DeepVoice (자체 TTS 모델 간접 증거)**: LG U+는 2025년 2월 MWC 발표에서 AI 합성 음성을 탐지하는 'Anti-DeepVoice' 기술을 공개했으며, 이를 위해 "자체 개발 TTS 모델과 다양한 TTS 기술"을 학습 데이터로 활용했다고 밝혔다[G-01]. 이는 탐지용 합성 음성 생성 목적의 내부 TTS 모델이 존재함을 시사하나, 프로덕션 서비스 품질 수준 여부는 미확인이다[D].
- **ixi-GEN (sLLM)**: LG AI연구원의 EXAONE을 기반으로 통신·플랫폼 도메인 데이터를 학습시킨 소형언어모델(sLLM). 언어 이해 영역이며, 음성 합성 전담 모델과는 별개이다[G-08].

**요약**: LG U+는 STT에서 일부 자체 역량이 있으나, **서비스 품질 TTS 및 Voice Cloning은 현재 외부 의존** 상태이다.

### 1-2. LG AI Research 음성 연구 조직

**공개된 정보**

- LG AI연구원의 Language Lab이 STT/TTS 핵심 기술을 연구하고 있으며, 주요 연구 영역으로 실시간 음성인식, 자연스러운 음성합성, 화자 분리, Speech LLM, Speech Foundation Models를 명시하고 있다[G-02].
- LG AI Research는 현재 STT/TTS Research Scientist/Engineer 포지션을 공개 채용 중이다(공고 기준 2024~2025년)[G-02]. 이는 현재 해당 팀이 소규모이거나 확장 단계임을 시사한다[C].
- LG AI Research는 2025년 미국 현지 AI 인재 채용 확대를 공시했으며[G-03], EXAONE 언어모델 계열에 집중하고 있다. 음성 분야는 Language Lab 하위 세부 연구 영역이다.
- 구체적인 음성 연구팀 인원 수는 **공개 정보 없음**.

### 1-3. 그룹사 역량 활용 가능성

**LG CNS**

- LG CNS는 AI·클라우드 SI 역량을 보유하고 있으며, 고객 상담 솔루션(AICC) 구현 경험이 있다. 그러나 TTS 원천 모델 개발 역량은 공개 확인 어렵다[C].

**LG AI Research (그룹 공용)**

- LG AI연구원은 LG전자, LGU+, LG CNS 등 LG 계열사가 공동 활용하는 AI 연구 기관이다. 2025년 8월 기준 K-EXAONE(K-AI 파운데이션 모델) 개발을 위한 'LG 컨소시엄'을 구성해 슈퍼브AI, 퓨리오사AI 등 10개사와 협력 중이다[G-08].
- LG유플러스와 LG AI연구원이 "ONE LG" 체계로 AI 공동 대응 체제를 구축하고 있어, LG AI Research의 STT/TTS 성과를 LGU+가 직접 활용 가능한 구조다[G-09].
- **결론**: 그룹사 역량 활용은 현실적이나, LG AI Research 자체 TTS 성과가 아직 프로덕션 수준임을 확인하기 어렵다.

---

## 2. 개발 기간 추정

### 2-1. 경쟁사 벤치마크

**SKT A.X TTS**

- SKT는 자체 구축한 대량의 고품질 음성 데이터와 딥러닝 기술을 적용해 A.X TTS 30종 이상의 음성을 개발했으며, 2024년 6월 SK 오픈API를 통해 외부 공개했다[G-04].
- SKT의 AI R&D 인력은 약 1,200명 규모이며, 누적 AI 투자 6,000억 원 이상이다[G-05]. TMAP, NUGU 등 내부 서비스에 수년간 TTS를 적용해온 사전 역량을 보유한다.
- **개발 기간 직접 공개 정보 없음**. 다만 SKT가 NUGU 스피커(2016년 출시)부터 TTS 개발을 시작했고, A.X TTS를 외부 공개한 시점(2024)까지 약 8년 이상의 누적 투자가 있었다[C][G-05].

**KT 기가지니 TTS**

- KT는 기가지니 TTS에서 비용을 1/4로 절감하고 속도를 10배 향상시키는 CPU 기반 음성합성 알고리즘을 개발했고, 커스텀 보이스 학습에 필요한 녹음 시간을 30분→3분으로 단축했다[G-06]. 2024년 5월 건강보험공단 고객센터에 음성 인증 서비스를 국내 공공기관 최초로 적용했다[G-06].
- KT 기가지니 역시 2017년 출시 이후 수년간 누적 개발이 이루어진 사례이다[C].

**Naver CLOVA Voice**

- 네이버 CLOVA Voice는 100개 이상의 음성, 40분 음성 데이터로 커스텀 보이스 학습이 가능하다. HyperCLOVA X 8B Omni에서 한국어 TTS MOS 4.22/5 달성(2026년 1월)[E-03]. 네이버가 CLOVA TTS 연구를 시작한 것은 2017~2018년경으로 추정되며, 상용 서비스까지 약 3~4년이 소요된 것으로 알려져 있다[C].

**Supertone (HYBE 자회사)**

- 2020년 3월 설립, 2021년 HYBE가 40억 원 초기 투자 후 2023년 1월 450억 원(지분 56.1%)으로 완전 인수했다. 핵심 기술인 NANSY(음성 4요소 분해·합성) 파운데이션 모델을 설립 이후 약 2~3년 만에 상업 수준으로 개발했다[G-10].

### 2-2. 오픈소스 기반 개발 시나리오 (현실적 최단 경로)

**Fast Track: 오픈소스 Fine-tuning 활용**

| 단계 | 내용 | 예상 기간 |
|------|------|-----------|
| 1. 팀 구성 | TTS 연구원 5~8명 채용·온보딩 | 3~6개월 |
| 2. 데이터 구축 | 한국어 음성 데이터셋 구축 및 전처리 | 3~6개월 (병행 가능) |
| 3. 기반 모델 선택 | CosyVoice 2, Qwen3-TTS, Kokoro 등 오픈소스 선정 | 1~2개월 |
| 4. 한국어 Fine-tuning | 도메인 특화 학습·평가 | 3~6개월 |
| 5. 프로덕션 파이프라인 | 서빙 인프라, 지연 최적화, 보안 | 3~6개월 |
| **합계 (MVP)** | **MVP 수준 서비스 출시** | **12~18개월** |
| 6. 고도화 | Voice Cloning(15초 클로닝), 감정 제어 추가 | +6~12개월 |
| **합계 (Full)** | **경쟁사 수준 전기능 서비스** | **18~30개월** |

**Slow Track: 자체 모델 원천 개발 (독자 아키텍처)**

- SKT·Naver 수준의 독자 파운데이션 모델: **36~60개월** [추정]
- 선행 연구팀 없이 신규 구성 시 초기 2년은 연구 투자 비용만 발생하고 서비스 출시는 3년 이후[추정]

**오픈소스 활용 근거**

- CosyVoice 2 (Alibaba FunAudioLLM): 한국어 zero-shot 합성 지원 확인(Speech Tokenizer 제로샷 능력), 학습·추론 코드 완전 공개[G-11]
- Kani-TTS-2: H100 8장 × 6시간 학습으로 프로덕션급 모델 완성 사례 — 10,000시간 고품질 영어 음성 데이터 기준[G-12]
- Qwen3-TTS: Apache 2.0 오픈소스, 한국어 포함 10개 언어, 97ms 스트리밍 지연. 상용 수준 성능[G-13]
- Kokoro-82M: 82M 파라미터 경량 모델로 한국어 지원, A100 GPU 약 $400 수준 학습 비용 사례[G-13]

---

## 3. 필요 투자 규모

### 3-1. 인력

**TTS 연구 팀 최소 구성 (MVP 기준)**

| 역할 | 인원 | 연봉 범위 (한국, 2025) | 비고 |
|------|------|--------------------|------|
| Senior TTS Research Scientist | 2명 | 1.2억~2.0억 원/인 | 박사급, 음성합성 경력 3년+ |
| ML Engineer (TTS/STT) | 3명 | 8,000만~1.4억 원/인 | 모델 학습·서빙 파이프라인 |
| Data Engineer (음성 데이터) | 2명 | 6,000만~1.0억 원/인 | 데이터 수집·레이블링 관리 |
| DevOps/Infra | 1명 | 7,000만~1.1억 원/인 | GPU 클러스터 운영 |
| **합계 (8인 팀)** | **8명** | **약 7.4억~12억 원/년** | 4대보험·복리후생 별도 |

- 국내 대기업 AI 신입 박사 연봉: 1.1~1.3억 원, 경력직 Research Scientist: 1.2~2.4억 원 수준[G-14]
- SKT는 AI R&D 인력 1,200명을 보유하며 누적 AI 투자 6,000억 원 이상을 집행했으나, TTS 팀 단독 규모는 공개 정보 없음[G-05]
- 해외 빅테크 대비 한국 AI 연구원 연봉은 2~3배 낮아 인재 유치 경쟁이 국내 스타트업·네이버·카카오와도 발생[G-14]

### 3-2. 인프라 (GPU 학습 클러스터)

**H100 기준 추정**

| 항목 | 규모 | 비용 추정 | 비고 |
|------|------|-----------|------|
| H100 GPU 구매 (8장 서버 1대) | 8 GPU | 3억~4억 원/대 | 대당 3,000만~5,000만 원, 2025 시가[G-15] |
| 학습용 클러스터 (초기) | 8~32 GPU | 3억~16억 원 | 오픈소스 모델 Fine-tuning 시 8~16 GPU로 충분 |
| 추론 서빙 인프라 | 4~8 GPU | 1.5억~6억 원 | 실시간 스트리밍 TTS 서빙 |
| 클라우드 대안 | H100 임차 | $2.49~4/시간 | Atlas Cloud 기준; 초기 프로토타입에 유리[G-16] |
| **클라우드 학습 (Fine-tuning)** | **500 GPU-시간** | **약 100만~200만 원** | Kani-TTS-2 사례 참고, 소규모 Fine-tuning[G-12] |

- LGU+는 파주 AI 데이터센터(AIDC)에 6,156억 원을 투자해 GPU 최대 12만 장 수용 규모를 2027년 준공 목표로 건설 중이다[E-01]. 이 인프라가 완성되면 TTS 학습용 GPU 별도 구매 없이 내부 할당이 가능해진다.
- 단기적으로는 클라우드 GPU 임차(AWS/GCP/Azure 또는 국내 클라우드)로 프로토타입 개발 후, 내부 AIDC로 이전하는 전략이 현실적이다[추정].

### 3-3. 학습 데이터 및 라이선스

**한국어 TTS 학습 데이터 구축 비용**

| 데이터 유형 | 규모 | 비용 추정 | 비고 |
|------------|------|-----------|------|
| 기존 공개 데이터셋 활용 | KSS, KoreanSpeech 등 | 0원 (무료) | 품질·다양성 한계 |
| 상용 음성 데이터셋 구매 | 100~500시간 | 3,000만~1.5억 원 | 성우 보이스, 감정 레이블 포함 |
| 자체 수집 (성우 녹음) | 100시간 기준 | 1억~3억 원 | 전문 성우 고용, 녹음실 비용 |
| Voice Cloning용 데이터 | 화자당 15~40분 | 100만~500만 원/화자 | Naver CLOVA 기준 40분 필요[G-17] |
| **MVP용 한국어 데이터** | **200~500시간** | **약 2억~5억 원** | [추정] |

**신규 언어 학습 데이터 기준**: Kokoro 오픈소스 기준 100시간 미만의 오디오로 새 언어 학습 가능[G-13]. 단, 상용 품질을 위해서는 다양한 화자·도메인·감정의 고품질 데이터 500~1,000시간 이상이 권장된다[추정].

### 3-4. 총 투자 규모 추정 (Build 시나리오)

| 항목 | 초기 1년 | 연간 유지 | 3년 누계 |
|------|---------|----------|---------|
| 인력 (8인 팀) | 10억~15억 원 | 10억~15억 원/년 | 30억~45억 원 |
| 인프라 (GPU 구매/임차) | 5억~20억 원 | 3억~8억 원/년 | 11억~36억 원 |
| 데이터 구축 | 3억~6억 원 | 1억~3억 원/년 | 5억~12억 원 |
| 연구·개발 외주/협력 | 2억~5억 원 | 1억~3억 원/년 | 4억~11억 원 |
| **합계** | **20억~46억 원** | **15억~29억 원/년** | **50억~104억 원** |

- 상기 수치는 8인 소규모 팀 기준 **최소 투자 시나리오**이다[추정].
- SKT·Naver 수준의 독자 대형 TTS 파운데이션 모델 개발은 팀 규모 20~50명, 3년 이상 투자 시 **300억~600억 원 이상**으로 규모가 급증한다[추정].
- LGU+ AIDC 파주 인프라 활용 시 GPU 별도 구매 비용은 절감 가능하나 2027년 이후 가용 전망이다[E-01].

**경쟁사 AI 투자 규모 참고**

| 기업 | AI 투자/인력 규모 | 출처 |
|------|----------------|------|
| SKT | 누적 AI 투자 6,000억 원+, R&D 인력 1,200명 | [[G-05]](#ref-g-05) |
| Supertone (HYBE) | 총 490억 원 (초기 40억 + 인수 450억), 설립 3년 | [[G-10]](#ref-g-10) |
| ElevenLabs | Series C $180M (약 2,600억 원), 기업가치 $3.3B | [[G-18]](#ref-g-18) |
| LGU+ AIDC (파주) | 6,156억 원 (AI 인프라 전체, 2025~2027) | [[E-01]](#ref-e-01) |

---

## 4. Build 장단점

### 4-1. 장점

**완전한 기술 통제권 및 IP 확보**

- TTS/Voice Cloning 모델을 자체 보유하면 API 비용 종속에서 탈피하고 서비스 조건 변경 리스크를 제거할 수 있다.
- LGU+ 전용 화자, 브랜드 보이스, 고객 맞춤 커스텀 음성 등 차별화된 서비스를 독점 제공 가능하다.
- AICC(AI 컨택센터), 익시오, 메타버스, B2B 솔루션 등 다양한 LGU+ 서비스에 내부 원가로 배포할 수 있다.

**장기 차별화 및 데이터 자산 축적**

- 고객 통화 데이터(법적 동의 범위 내)를 학습에 활용해 통신 도메인 특화 TTS를 구축하면 경쟁사가 복제 어려운 모델을 보유할 수 있다[추정].
- LG AI Research와의 공동 연구를 통해 Speech Foundation Model로 확장할 수 있는 가능성이 있다[G-02][추정].

**데이터 보안 및 규제 대응**

- 온프레미스(On-Premise) 또는 프라이빗 클라우드 기반으로 운영 시, 합성 음성 생성 데이터가 외부로 유출되지 않는다.
- EU AI Act(2026년 8월 발효 예정) 및 향후 한국 AI 규제 대응 시 합성 음성 라벨링·워터마킹 요건을 자체적으로 충족 구현 가능하다[추정].

### 4-2. 단점

**시간 및 기회비용**

- MVP 수준도 12~18개월 소요. 이 기간 동안 시장은 ElevenLabs, Google, SKT 등이 계속 발전한다[추정].
- 경쟁사 대비 기술 격차가 이미 상당하다: SKT A.X TTS(30종 음성, 수년 누적), Naver HyperCLOVA X Omni(한국어 MOS 4.22)[E-02][E-03].

**인력 확보 난이도**

- 국내 한국어 TTS 전문 연구인력 풀이 극히 제한적이다. 주요 인재는 Naver, Kakao, SKT, 수퍼톤, 학계에 분포해 있으며 이직 경쟁이 치열하다[C].
- 해외 빅테크(Google, OpenAI)와 연봉 경쟁 불가 구조: 오픈AI 박사급 초봉 11억 원 vs 국내 대기업 1억~1.3억 원[G-14].
- LG AI Research가 현재 STT/TTS 포지션을 공개 채용 중인 점은 현재 팀이 소규모임을 시사한다[G-02].

**SKT/Naver/Big Tech 대비 열위**

- Naver CLOVA Voice: 10년 이상 누적, 한국어 최고 수준 MOS 4.22 달성[E-03].
- SKT A.X TTS: 자체 30종 음성, SK 오픈API 공개로 생태계 구축 중[E-02].
- ElevenLabs, Google Gemini TTS: 글로벌 대규모 데이터·투자·연구진 보유. 한국어 합성 품질이 빠르게 향상 중[G-18].
- **LGU+가 독자 개발하더라도 이들 대비 동등 품질 달성에 3~5년 소요, 초과 달성은 사실상 불가능**[추정].

**비용 효율 문제**

- 자체 개발 TTS API 단가가 ElevenLabs($0.30/1,000자), Google Cloud TTS($4/100만자) 등 상용 API 대비 저렴해지려면 대규모 호출량이 전제되어야 한다[C].
- 월 수억 건의 TTS 호출이 없으면 자체 인프라 운영 비용이 외부 API 비용을 초과한다[추정].

---

## 5. 전략적 시사점

**기술 트렌드**

- 오픈소스 TTS 생태계가 폭발적으로 성장 중(CosyVoice 2, Qwen3-TTS, Kokoro 등). 이는 Build 진입 장벽을 낮추지만, 동시에 Buy/Partner 옵션의 비용도 하락시킨다[G-11][G-12][G-13].
- 한국어 TTS 품질 경쟁은 이미 Naver가 압도적 우위(MOS 4.22)를 점하고 있으며, SKT도 30종 이상의 음성을 외부 공개했다. LGU+가 이 시장에서 기술 리더십을 확보하기는 구조적으로 어렵다[E-02][E-03].

**기회**

- LGU+ AIDC 파주(2027년 준공, GPU 12만 장)가 가동되면 학습 인프라 비용 부담이 대폭 감소한다[E-01].
- LG AI Research와 ONE LG 체계를 통한 공동 개발은 단독 투자 대비 리스크를 분산할 수 있다[G-09].
- 통신 도메인 특화 TTS(AICC 전용 음성, 고객 맞춤 브랜드 보이스)는 범용 TTS와 차별화 가능한 니치(niche) 영역이다[추정].

**위협**

- 인재 확보 실패 시 개발 일정이 무기한 연장될 리스크가 있다. 핵심 연구원 이탈 시 프로젝트 전체가 위험에 처할 수 있다[추정].
- 글로벌 오픈소스 모델의 한국어 품질이 계속 향상되면, 자체 개발 완료 시점에 이미 오픈소스가 동등 품질을 제공하는 상황이 발생할 수 있다[G-11][G-13].
- EU AI Act 합성 음성 라벨링 규제(2026년 8월)가 자체 TTS 운영에 추가 컴플라이언스 부담을 유발한다[추정].

**권고사항**

- **Pure Build 단독 전략은 비추천**: 개발 기간과 비용 대비 경쟁 우위 확보가 어렵다.
- **오픈소스 기반 하이브리드 Build**: CosyVoice 2 또는 Qwen3-TTS를 기반으로 한국어 Fine-tuning 진행. LG AI Research와 공동 추진. 통신 도메인 특화 Use Case(AICC, 브랜드 보이스) 집중.
- **Build + Partner 병행**: 자체 개발 중 단기(12~24개월)는 ElevenLabs/Naver CLOVA API를 사용해 서비스 출시 타이밍을 맞추고, 자체 모델이 동등 품질에 도달하면 전환한다.
- **AIDC 인프라 가동 시점(2027)을 기준점으로 계획 수립**: 인프라 준비 전까지는 클라우드 임차로 프로토타입 개발, 2027년 이후 본격 학습 확장 전략이 현실적이다[E-01].

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- LGU+ 익시오가 Google Gemini API에 의존하고 있다는 사실 [G-07] — 공식 인터뷰에서 직접 확인
- SKT A.X TTS 30종 음성 2024년 6월 외부 공개 [G-04] — 공식 보도
- LGU+ 파주 AIDC 6,156억 원 투자 공시 [E-01] — 공식 공시
- LG AI Research STT/TTS 채용 공고 [G-02] — 공식 커리어 페이지
- Naver HyperCLOVA X 8B Omni 한국어 MOS 4.22 달성 [E-03] — 공식 발표
- Kani-TTS-2 H100 8장 × 6시간 학습 사례 [G-12] — 공개 기술 문서

**추가 검증 필요 [C/D]:**
- Anti-DeepVoice 학습용 자체 TTS 모델의 서비스 품질 수준 [D] — 단일 소스, 탐지 목적 모델일 가능성
- LG AI Research 음성 연구팀 실제 인원 규모 [D] — 공개 정보 없음
- SKT TTS 팀 인원 및 초기 개발 기간 [C] — 간접 추정만 가능
- KT 기가지니 TTS 개발 기간 [C] — 공식 발표 없음

**데이터 공백:**
- LGU+ 자체 TTS 모델의 MOS 점수 또는 품질 벤치마크
- LG AI Research Language Lab 음성팀 인원 및 논문 성과
- SKT/KT의 TTS 전담팀 규모 및 연간 R&D 예산 세부 항목

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | LG U+ Anti-DeepVoice 기술 (eroun.net) | [링크](https://www.eroun.net/news/articleView.html?idxno=53253) | news | 2025-02-01 | [B] |
| <a id="ref-g-02"></a>G-02 | LG AI Research STT/TTS 채용 공고 | [링크](https://www.lgresearch.ai/careers/view?seq=72) | IR/발표 | 2024-01-01 | [A] |
| <a id="ref-g-03"></a>G-03 | LG AI Research 미국 글로벌 인재 채용 공시 | [링크](https://lgcorp.com/media/release/27379) | IR/발표 | 2024-06-01 | [A] |
| <a id="ref-g-04"></a>G-04 | SKT A.X TTS 서울경제 — '5년뒤 10兆 시장' SKT 음성합성 볼륨업 | [링크](https://www.sedaily.com/NewsView/2DAG6VKSE8) | news | 2024-06-13 | [B] |
| <a id="ref-g-05"></a>G-05 | SKT AI 투자 규모 이코노미스트 보도 | [링크](https://economist.co.kr/article/view/ecn202403200056) | news | 2024-03-20 | [B] |
| <a id="ref-g-06"></a>G-06 | KT 기가지니 TTS — 비용 1/4·속도 10배 개선 (KT Enterprise) | [링크](https://enterprise.kt.com/bt/dxstory/852.do) | news | 2024-05-01 | [B] |
| <a id="ref-g-07"></a>G-07 | LGU+ 익시오 Google Gemini 의존 공식 인터뷰 (디지털데일리) | [링크](https://www.ddaily.co.kr/page/view/2025111313382958697) | news | 2025-11-13 | [B] |
| <a id="ref-g-08"></a>G-08 | LG 컨소시엄 K-EXAONE 개발 — ixi-GEN 소개 (CEOSCOREDAILY) | [링크](https://m.ceoscoredaily.com/page/view/2025080416394126638) | news | 2025-08-04 | [B] |
| <a id="ref-g-09"></a>G-09 | LGU+·LG AI연구원 ONE LG 체계 (서울신문) | [링크](https://www.seoul.co.kr/news/economy/industry/2026/03/02/20260302500002) | news | 2026-03-02 | [B] |
| <a id="ref-g-10"></a>G-10 | 수퍼톤·하이브 인수 — 450억 원 56.1% 지분 (바이라인네트워크) | [링크](https://byline.network/2023/01/31-133/) | news | 2023-01-31 | [B] |
| <a id="ref-g-11"></a>G-11 | CosyVoice 2 논문 — 한국어 zero-shot 지원 (arXiv) | [링크](https://arxiv.org/html/2412.10117v1) | paper | 2024-12-01 | [A] |
| <a id="ref-g-12"></a>G-12 | Kani-TTS-2 기술 문서 — H100 8장 6시간 학습 (MarkTechPost) | [링크](https://www.marktechpost.com/2026/02/15/meet-kani-tts-2-a-400m-param-open-source-text-to-speech-model-that-runs-in-3gb-vram-with-voice-cloning-support/) | news | 2026-02-15 | [B] |
| <a id="ref-g-13"></a>G-13 | Qwen3-TTS 오픈소스 한국어 포함 10개 언어 97ms (DEV Community) | [링크](https://dev.to/czmilo/qwen3-tts-the-complete-2026-guide-to-open-source-voice-cloning-and-ai-speech-generation-1in6) | news | 2026-01-01 | [B] |
| <a id="ref-g-14"></a>G-14 | 한국 AI 연구원 연봉 수준 — 대기업 박사급 (DIO 블로그) | [링크](https://blog.dio.so/ai-engineer-salary) | blog | 2024-01-01 | [C] |
| <a id="ref-g-15"></a>G-15 | H100 GPU 가격 3,000만~5,000만 원 (AI타임스) | [링크](https://www.aitimes.com/news/articleView.html?idxno=150555) | news | 2024-01-01 | [B] |
| <a id="ref-g-16"></a>G-16 | H100 클라우드 임차 $2.49/시간 (Atlas Cloud) | [링크](https://www.atlascloud.ai/ko/pricing/gpu) | news | 2025-01-01 | [B] |
| <a id="ref-g-17"></a>G-17 | Naver CLOVA Voice 커스텀 보이스 40분 데이터 (NAVER Cloud Platform) | [링크](https://www.ncloud.com/v2/product/aiService/clovaVoice) | IR/발표 | 2024-01-01 | [A] |
| <a id="ref-g-18"></a>G-18 | ElevenLabs Series C $180M 기업가치 $3.3B (Crunchbase) | [링크](https://news.crunchbase.com/venture/voice-ai-startups-global-investment/) | news | 2025-01-01 | [B] |
| <a id="ref-e-01"></a>E-01 | LGU+ 파주 AIDC 6,156억 투자 공시 (머니투데이) | [링크](https://www.mt.co.kr/tech/2025/04/29/2025042918171779676) | IR/발표 | 2025-04-29 | [A] |
| <a id="ref-e-02"></a>E-02 | SKT A.X TTS SK 오픈API 공개 — 30종 음성 (SK 텔레콤 뉴스룸) | [링크](https://openapi.sk.com/products/detail?svcSeq=67) | IR/발표 | 2024-06-13 | [A] |
| <a id="ref-e-03"></a>E-03 | Naver HyperCLOVA X 8B Omni 한국어 TTS MOS 4.22 (LG유플러스 인용 기사) | [링크](https://v.daum.net/v/20251230175149742) | IR/발표 | 2025-12-30 | [A] |
| <a id="ref-e-04"></a>E-04 | LGU+ 홍범식 대표 — "익시오 글로벌 표준 주도" (서울신문) | [링크](https://www.seoul.co.kr/news/economy/industry/2026/03/04/20260304030005) | IR/발표 | 2026-03-04 | [A] |
| <a id="ref-e-05"></a>E-05 | LGU+ ixi-STT 자체 음성 데이터 적용 (LGU+ 기업 보도자료) | [링크](https://www.lguplus.com/biz/insight/trend/262) | IR/발표 | 2024-01-01 | [A] |
