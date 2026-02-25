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
  2: research-hub MCP    # 학술 논문 (신뢰도 A)
  3: patent-intel MCP    # USPTO 특허 (신뢰도 A)
  4: trend-tracker MCP   # 뉴스/트렌드 (신뢰도 B~C)
  5: WebSearch           # 최신 뉴스/보고서 (신뢰도 B~D)
```
