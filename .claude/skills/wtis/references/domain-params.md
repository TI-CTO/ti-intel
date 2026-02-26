# WTIS 도메인 파라미터 — LG U+ 기술전략

Layer 2 핵심 역량(discover, research-deep, validator) 호출 시 전달하는 도메인 설정.

## 기본 도메인 설정

```yaml
domain: telecom_tech_strategy
organization: LG U+
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
  2: research-hub MCP    # 학술 논문 — Semantic Scholar (신뢰도 A)
  3: patent-intel MCP    # 특허 — USPTO, KIPRIS(P1) (신뢰도 A)
  4: trend-tracker MCP   # 뉴스/트렌드 — Tavily, GDELT (신뢰도 B~C)
  5: WebSearch           # 최후 fallback (신뢰도 B~D)
```

## 출처 기호 체계
```yaml
source_codes:
  G-xx: "글로벌 웹 검색 (WebSearch, Tavily)"
  N-xx: "뉴스/동향 (trend-tracker MCP, GDELT)"
  E-xx: "기업 발언/보도자료 (실적발표, IR)"
  P-xx: "학술 논문 (research-hub MCP, Semantic Scholar)"
  T-xx: "특허 (patent-intel MCP, USPTO, KIPRIS)"
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
