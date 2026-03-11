# WTIS 도메인 파라미터

Layer 2 핵심 역량(discover, research-deep, validator) 호출 시 전달하는 도메인 설정.

## 기본 도메인 설정

```yaml
domain: telecom_tech_strategy
organization: telecom
```

## 경쟁사
```yaml
competitors:
  domestic: [SKT, KT]
  global: [NTT Docomo, Verizon, AT&T, Deutsche Telekom, SoftBank]
  big_tech: [Samsung, Google, Microsoft, AWS]
```

## 기술 분류 체계
```yaml
taxonomy:
  - AI/ML
  - Network (5G/6G, Open RAN, Network Slicing)
  - Security (Zero Trust, Quantum-safe)
  - Cloud (Edge, MEC)
  - IoT
  - B2B (Enterprise, SMB)
```

## 정책/규제 소스
```yaml
policy_sources:
  - IITP (정보통신기획평가원)
  - NIPA (정보통신산업진흥원)
  - 과기정통부 (과학기술정보통신부)
  - ITU-R (국제전기통신연합)
  - 3GPP
```

## 등록된 MCP 토픽 슬러그
```yaml
topics:
  - ai-network      # AI 기반 네트워크 최적화
  - 6g              # 6G 기술 개발
  - network-slicing # 네트워크 슬라이싱
  - edge-computing  # 엣지 컴퓨팅/MEC
  - quantum-comm    # 양자 통신
  - llm-telecom     # 통신 분야 LLM 응용
  - open-ran        # Open RAN
  - digital-twin    # 디지털 트윈
```

## L2별 분석 초점

L1 도메인 → L2 기술별 분석 파라미터. SKILL-0이 L2를 식별한 후 research-deep에 전달한다.
L1/L2/L3 전체 구조는 `tech-taxonomy.md` 참조.

```yaml
l2_analysis:
  # === Agentic AI ===
  self-evolving-architecture:
    domain: agentic-ai
    name: Self Evolving Architecture
    l2_number: 1
    focus: [Agentic Context Engineering, 자기개선 에이전트, 메타러닝]
    key_players: [Anthropic, OpenAI, DeepMind, Microsoft Research, Elasticsearch, Weaviate, LangChain]

  model-delta-foundry:
    domain: agentic-ai
    name: Model & Delta Foundry
    l2_number: 2
    focus: [자동 프롬프트 최적화, LLM 평가 자동화, 학습-배포 파이프라인, GPU 오케스트레이션]
    key_players: [Stanford NLP, Databricks, Weights&Biases, LangSmith, NVIDIA, Run:ai, Ray, Anyscale, AWS, Google Cloud]

  trusted-multi-agent:
    domain: agentic-ai
    name: Trusted Multi-Agent Orchestration
    l2_number: 3
    focus: [에이전트 오케스트레이션, 에이전트 기반 계획, 협업 프로토콜, 신뢰성]
    key_players: [Microsoft, IBM, AWS, Anthropic, OpenAI, DeepSeek, Alibaba, LangChain, CrewAI, Talkdesk]

  hybrid-ai-infra:
    domain: agentic-ai
    name: Hybrid AI Infra
    l2_number: 4
    focus: [sLM 성능/경량화, 실시간 추론, Edge AI, 5G SA/6G AI-RAN, 단말 제약(메모리/전력)]
    key_players: [Apple, Samsung, Qualcomm, MediaTek, Google, Meta, Hugging Face, SKT, KT, Nokia, Ericsson]

  intent-understanding:
    domain: agentic-ai
    name: 의도 파악 기술
    l2_number: 5
    focus: [Adaptive RAG, Self-Reflective RAG, Query Routing, 멀티턴 대화 이해]
    key_players: [Google, OpenAI, Anthropic, Kore.ai, Databricks, LangChain, Naver, SKT]

  # === Voice AI ===
  speech-perception:
    domain: voice-ai
    name: Speech Perception & Interaction
    l2_number: 6
    focus: [음성 감정 분석, 대화 맥락 인식, 끼어들기/턴테이킹 예측, 실시간 처리]
    key_players: [Google, Amazon, Microsoft, Nuance, Deepgram, AssemblyAI, Naver, Kakao, SKT]

  personal-intelligence:
    domain: voice-ai
    name: Personal Intelligence
    l2_number: 7
    focus: [페르소나 플러그인, 관계 그래프 구축, 컨텍스트 기반 액션 추천]
    key_players: [Naver, Kakao, SKT, Meta, Google, Neo4j, DeepLearning.AI]

  speech-generation:
    domain: voice-ai
    name: Speech Generation
    l2_number: 8
    focus: [Voice Cloning, Voice Synthesis, Zero-shot TTS, 화자 적응]
    key_players: [ElevenLabs, Play.ht, Resemble AI, Google, Microsoft, Amazon, Naver, SKT]

  # === Secure AI ===
  spam-phishing:
    domain: secure-ai
    name: 스팸/피싱탐지
    l2_number: 9
    focus: [AI 기반 실시간 탐지, 보이스피싱 예방, 이미지 스팸 OCR, 통화전 차단]
    key_players: [SKT, KT, Google, Hiya, Vectra AI, Adaptive Security, Resemble AI, 경찰청]

  quantum-he:
    domain: secure-ai
    name: 양자/동형 암호
    l2_number: 10
    focus: [PQC NIST 표준 적용, 동형암호 CKKS 실용화, 통화 녹음 암호화, B2B AICC FHE, HW 가속]
    key_players: [NIST, AWS, Microsoft Research, IBM, Samsung, Fortanix, Ant Group, CryptoLab, SKT, KT]
```

## 분석 프레임워크
```yaml
analysis_frameworks:
  selection: [SMART, TRL_4quadrant, 3B_strategy]
  progress: [Gate_Review_G0_to_G4, risk_matrix]
  discovery: [Porter_5_Forces, 3Layer_needs, priority_matrix]
  validation: [citation_check, numerical_cross_validation, logic_check, bias_check]
```

## 데이터 소스 우선순위
```yaml
data_source_priority:
  1: telco-factbook MCP  # SKT/KT IR 공시 (신뢰도 A)
  2: intel-store MCP     # 통합 인텔리전스 — 논문/특허/뉴스 (신뢰도 A~C)
  3: trend-tracker MCP   # 스냅샷/트렌드 비교 (신뢰도 B~C)
  4: WebSearch           # 최후 fallback (신뢰도 B~D)
```

## 출처 기호 체계
```yaml
source_codes:
  G-xx: "글로벌 웹 검색 (WebSearch)"
  N-xx: "뉴스/동향 (intel-store: news, GDELT, Tavily)"
  E-xx: "기업 발언/보도자료 (실적발표, IR)"
  P-xx: "학술 논문 (intel-store: papers, Semantic Scholar)"
  T-xx: "특허 (intel-store: patents, USPTO, KIPRIS)"
  I-xx: "내부 자료 (사내 보고서, 제안서 원문)"
```

## 외부 API 설정
```yaml
external_apis:
  tavily:
    env_key: TAVILY_API_KEY
    cost: "$0 (무료 1,000건/월) ~ $30/월"
    rate_limit: "0.5s delay"
    reliability: "B"
  gdelt:
    env_key: null  # 키 불필요
    cost: "$0 (완전 무료)"
    rate_limit: "1.0s delay"
    reliability: "C"
  kipris:  # P1
    env_key: KIPRIS_API_KEY
    cost: "$0 (공공데이터포털)"
    rate_limit: "1,000건/월"
  dart:  # P1
    env_key: DART_API_KEY
    cost: "$0 (FSS)"
  sec_edgar:  # P1
    env_key: null  # User-Agent만 필요
    cost: "$0"
```
