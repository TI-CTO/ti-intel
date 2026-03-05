---
type: weekly-research
domain: secure-ai
l3_topic: secure-vector-search
date: 2026-03-05
signal: 🟡
agent: research-deep
confidence: medium
status: completed
sources_used: [websearch, webfetch]
---

# Research Report: Secure Vector Search / 암호화 벡터 검색

## Executive Summary (경영진 요약)

> 암호화 벡터 검색(Secure Vector Search)은 TRL 4~5 수준으로, 학계에서 실용화 가능성이 본격적으로 검증되는 단계에 진입했다. Compass(OSDI'25), PANTHER(CCS'25), PP-ANNS(ICDE'25) 등 최정상 학회 채택 논문들이 한꺼번에 등장하며 기술 성숙도가 빠르게 높아지고 있다 [P-01~P-04]. 산업계에서는 IronCore Labs(Cloaked AI), Zama(Concrete ML, 2025 Series B $57M·유니콘), Microsoft Azure Confidential Computing이 실질적인 제품을 출시했으며, Pinecone은 2026년 2월 BYOC(Bring Your Own Cloud) 런칭으로 데이터 주권 요구에 대응하고 있다 [G-03~G-07]. 의료·금융 분야의 규제 강화(HIPAA 암호화 의무화 검토, EU AI Act)가 시장 드라이버로 작용하며, 단기적으로는 TEE 기반 컨피덴셜 컴퓨팅과 거리보존암호화(DCPE)가 현실적 대안으로 부상 중이다. 순수 동형암호(HE) 기반 솔루션은 성능 격차가 여전히 크나, 2025~2026년에 실용화 임계점 돌파 가능성이 있다. 전략적으로, 국내 금융·공공기관의 프라이빗 RAG 도입 시 이 영역이 핵심 보안 요소로 부상할 가능성이 높다.

## 연구 질문

> 최근 1~2주(2026년 3월 기준) 암호화 벡터 검색 분야의 기술·학술·시장·경쟁사 동향을 종합하여, 국내 기업의 전략적 대응 방향을 도출할 수 있는가?

---

## 1. 기술 동향

### 1-1. 기술 성숙도 (TRL)

| 구분 | TRL | 설명 |
|------|-----|------|
| 거리보존암호화(DCPE) 기반 ANN | 5~6 | PP-ANNS(ICDE'25)에서 기존 대비 최대 1,000배 성능 향상 시연 |
| ORAM + 그래프 인덱스(HNSW) | 5 | Compass(OSDI'25)에서 사용자 체감 지연 1초 내 달성, 메모리 3~7배 overhead |
| FHE(완전동형암호) 벡터 검색 | 3~4 | FRAG(arXiv'24), HE 기반 ANN은 실용 속도 미달, 캐시 최적화로 보완 중 |
| TEE(신뢰실행환경) 기반 | 6~7 | Azure Confidential AI, Google Private AI Compute에서 상용 배포 중 |
| 거리보존암호화 + 차분프라이버시 | 5 | ppRAG(arXiv 2601.12331)에서 RAG 파이프라인 통합 프레임워크 제안 |

### 1-2. 핵심 기술 요소

**거리보존암호화 (Distance-Comparison-Preserving Encryption, DCPE)**
- 벡터 간 상대적 거리 순서는 유지하면서 실제 임베딩 값을 암호화
- 클라우드 서버가 유사도 계산은 할 수 있으나 원본 벡터는 볼 수 없음
- PP-ANNS(ICDE'25)는 이를 HNSW 인덱스와 결합하여 기존 대비 최대 3 order of magnitude 속도 향상 [P-02]

**ORAM(Oblivious RAM) + 그래프 탐색**
- 암호화된 인덱스에서 접근 패턴까지 숨기는 기법
- Compass(OSDI'25, UC Berkeley)는 HNSW 특화 ORAM을 설계하여 방향성 필터링(Directional Neighbor Filtering), 예측 프리페치(Speculative Neighbor Prefetch)로 성능을 대폭 개선 [P-01]
- 서버측 메모리는 평문 대비 3.2~6.8배 필요, 클라이언트 메모리는 10MB 이하

**FHE(완전동형암호)**
- 암호화된 상태로 내적(dot product), 코사인 유사도 연산 가능 (CKKS 스킴 활용)
- FRAG: 단일 키 HE 프로토콜 + 곱셈 캐싱으로 연합 환경에서의 ANN 성능 향상 [P-03]
- Zama Concrete ML: FHE 기반 ML 파이프라인, 2025년 TFHE-rs 형식 지원 추가 [G-03]

**단일 서버 Private ANN (PIR/MPC 기반)**
- PANTHER(CCS'25): PIR + 비밀공유 + 가블드서킷 + HE 혼합으로 1,000만 포인트 검색을 18초, 284MB 통신으로 달성, 기존 대비 7.8배 빠르고 20배 통신량 절감 [P-04]

**속성보존암호화 (Property-Preserving Encryption)**
- IronCore Labs Cloaked AI: Scale & Perturb 알고리즘으로 노이즈 추가 후 벡터 재배치, 거리 관계 유지하면서 암호화 [G-04]
- ANN 검색, 클러스터링, 이상탐지를 암호화 상태로 수행 가능

### 1-3. 오픈소스 및 표준화 동향

- **Microsoft SEAL**: CKKS 스킴 기반 HE 라이브러리, 벡터 연산(내적, 거리 계산) 가능 [G-02]
- **FAISS + Encryption**: Meta FAISS는 암호화 지원 미내장, 외부 암호화 레이어와 결합하는 방식
- **W3C/ISO**: 프라이버시 보존 검색 표준화 논의 초기 단계 (공식 표준 없음)

---

## 2. 시장 동향

### 2-1. 시장 드라이버

| 드라이버 | 내용 | 시사점 |
|---------|------|--------|
| 규제 강화 | 미국 HHS, HIPAA Security Rule에 암호화 의무화 추진 검토 (2026 목표) [G-08] | 의료 데이터 벡터 DB 암호화 수요 급증 |
| EU AI Act | 고위험 AI 시스템 데이터 거버넌스 강화 | 금융·의료 RAG 시스템의 암호화 요구 |
| 임베딩 역추론 공격 | Song et al. (2024): 92% 확률로 원본 텍스트 재구성 가능 [G-09] | 기업 RAG 배포 시 벡터 DB 암호화 필수화 |
| 데이터 주권 규제 | 국가별 데이터 역외 이전 제한 강화 | BYOC, On-premise 벡터 DB 암호화 수요 |

### 2-2. 시장 규모 (크로스 검증 미충족, 참고용)

- 벡터 DB 전체 시장은 2025년 약 $2B 추정, CAGR 25~30% 전망 (단일 출처, 추가 검증 필요)
- 암호화 벡터 검색 세부 시장은 아직 독립적 추적 데이터 없음 — 공개 정보 없음

---

## 3. 경쟁사 동향

### 3-1. 주요 플레이어 현황

**IronCore Labs (스타트업, 미국)**
- 제품: Cloaked AI SDK — 벡터 임베딩 암호화 전문
- 2025년 7월: 암호화 학습 데이터로 AI 모델 훈련 기능 확장 발표 [G-04]
- 2025년: Gartner Cool Vendor in Data Security 2025 선정
- Qdrant, 기타 벡터 DB와 연동 가능

**Zama (스타트업, 프랑스)**
- 제품: Concrete ML (FHE 기반 ML 프레임워크), TFHE-rs
- 2025년 6월 Series B $57M 조달, 누적 $150M+, 유니콘 달성 (기업가치 $1B+) [G-03]
- Concrete ML v1.9: TFHE-rs 형식 지원, LoRA LLM fine-tuning, 브라우저/모바일 SDK
- 2025년 7월: Zama Confidential Blockchain Protocol 출시

**Microsoft Azure**
- Azure Confidential Computing: Intel SGX 기반 Enclave, AMD SEV-SNP 지원 [G-05]
- Azure AI Confidential Inferencing: GPU TEE에서 암호화 프롬프트 처리 (Whisper 모델)
- SEAL 라이브러리 오픈소스로 HE 생태계 지원 [G-02]

**Google**
- 2025년 11월: Private AI Compute 발표 — Apple Private Cloud Compute와 유사 [G-06]
- Titanium Intelligence Enclave(TIE): TPU 워크로드 보호
- AMD SEV-SNP: CPU 워크로드 보호
- 추론 후 세션 종료 시 데이터 삭제, 관리자 접근 불가

**Apple**
- Private Cloud Compute: TEE 기반 클라우드 추론, 온디바이스 수준의 프라이버시 [G-06]
- 서버측 데이터 비보유, 독립 검증 가능한 아키텍처

**Pinecone**
- 2026년 2월: BYOC(Bring Your Own Cloud) 런칭 — 고객 VPC 내에서 Pinecone 데이터 플레인 실행, Pinecone의 벡터/메타데이터 접근 차단 [G-07]
- 데이터 주권 요구 기업 대상 Enterprise 계약 필요

**Weaviate / Qdrant**
- Weaviate: 2025년 AWS HIPAA 컴플라이언스 달성, SOC 2 Type II [G-07]
- Qdrant: SOC 2 Type II, HIPAA-readiness 마케팅 (공식 HIPAA 보고서 미발행)

---

## 4. 제품/서비스 스펙 비교

| 기업 | 제품명 | 핵심 암호화 기술 | 성능 지표 | 규제 인증 | 가격 정책 | 발표 시점 | 출처 |
|------|--------|----------------|----------|---------|---------|---------|------|
| IronCore Labs | Cloaked AI | Scale & Perturb (속성보존암호화) | ANN 정확도: 평문과 동등 수준 | Gartner Cool Vendor 2025 | 오픈소스 SDK + 엔터프라이즈 | 2023 출시, 2025년 7월 학습 확장 | [G-04] |
| Zama | Concrete ML | FHE (TFHE/CKKS) | 공개 정보 없음 (FHE 특성상 수십~수백ms) | 공개 정보 없음 | 오픈소스 + 상업 라이선스 | v1.9 (2025년 4월) | [G-03] |
| Microsoft Azure | Confidential Computing | Intel SGX / AMD SEV-SNP (TEE) | 공개 정보 없음 | ISO 27001, SOC 2 Type II | Azure 종량제 | 지속 업데이트 | [G-05] |
| Pinecone | Pinecone BYOC | 고객 VPC 격리 (TEE 미확인) | 공개 정보 없음 | SOC 2 Type II, HIPAA, ISO 27001 | Enterprise 계약 필요 | 2026년 2월 | [G-07] |
| Weaviate | Enterprise Cloud | AES-256 at-rest + TLS (TEE 없음) | 공개 정보 없음 | SOC 2 Type II, HIPAA (AWS) | 종량제 / 엔터프라이즈 | 2025년 | [G-07] |
| Qdrant | Qdrant Cloud | AES-256 + TLS | 공개 정보 없음 | SOC 2 Type II | 종량제 / 엔터프라이즈 | 지속 업데이트 | [G-07] |

---

## 5. 학술 동향

### 5-1. 최근 주요 논문 (2024~2025)

**[P-01] Compass: Encrypted Semantic Search with High Accuracy**
- 저자: Jinhao Zhu 외 (UC Berkeley Sky Computing Lab)
- 게재: OSDI'25 (최정상 시스템 학회)
- 핵심: ORAM + HNSW 화이트박스 공동설계, 방향성 필터링·예측 프리페치 기법
- 성능: 사용자 체감 지연 ~1초, 서버 메모리 3.2~6.8배, 클라이언트 메모리 <10MB
- 의의: 완전히 손상된 서버에서도 데이터·쿼리·검색 결과 보호

**[P-02] Privacy-Preserving Approximate Nearest Neighbor Search on High-Dimensional Data**
- 저자: Yingfan Liu, Yandi Zhang 외
- 게재: ICDE'25 (데이터 엔지니어링 최정상 학회)
- 핵심: Distance Comparison Encryption(DCE) + HNSW 인덱스 + Filter-and-Refine 전략
- 성능: 기존 대비 최대 1,000배 속도 향상, 정확도 손실 없음
- 단일 클라우드 서버 환경, 통신 오버헤드 최소화

**[P-03] FRAG: Toward Federated Vector Database Management for Collaborative and Secure RAG**
- 저자: 공개 정보 — arXiv 2410.13272
- 게재: arXiv (2024년 10월)
- 핵심: 단일 키 HE 프로토콜로 상호 불신 당사자 간 암호화 ANN 검색
- 보안: IND-CPA 수준, 곱셈 캐싱으로 부동소수점 암호화 성능 개선
- 의의: 의료·금융 등 사일로 데이터 협업 RAG 환경 적용 가능

**[P-04] PANTHER: Private Approximate Nearest Neighbor Search in the Single Server Setting**
- 저자: Li, Huang 외
- 게재: ACM CCS'25 (보안 최정상 학회)
- 핵심: PIR + 비밀공유 + 가블드서킷 + HE 혼합 프레임워크
- 성능: 1,000만 포인트 기준 18초, 284MB 통신, 기존 대비 7.8배 속도, 20배 통신량 감소

**[P-05] Efficient Privacy-Preserving RAG with Distance-Preserving Encryption (ppRAG)**
- 저자: Huanyi Ye, Jiale Guo, Ziyao Liu, Kwok-Yan Lam
- 게재: arXiv 2601.12331 (2026년 1월)
- 핵심: CAPRISE(Conditional Approximate Distance-Comparison-Preserving Symmetric Encryption) + 차분프라이버시
- 대상: 비신뢰 클라우드 환경에서의 RAG, 벡터-텍스트 역추론 공격 방어

### 5-2. 연구 방향 요약

1. **단일 서버 설정에서의 실용화**: 두 서버(비공모) 설정에서 단일 서버로 이동 — PANTHER, Compass
2. **RAG 파이프라인 통합**: 암호화 벡터 검색을 RAG end-to-end에 내장 — ppRAG, FRAG
3. **성능 최적화**: 순수 FHE 대신 DCPE + ORAM 혼합으로 오버헤드 절감
4. **접근 패턴 보호**: 쿼리 내용뿐 아니라 어떤 벡터에 접근했는지도 숨기는 ORAM 연구 강화

---

## 6. 특허 동향

> 주의: 이번 조사에서 특허 수집 MCP 도구(intel-store)를 직접 호출하지 못하여 WebSearch 결과 기반 간접 파악. 직접 특허 DB 검색 필요.

### 6-1. 간접 파악 현황

| 기업/기관 | 특허 영역 | 근거 | 출처 |
|---------|---------|------|------|
| Microsoft | HE 라이브러리(SEAL), TEE 기반 AI 추론 | 오픈소스 + Azure 제품 출시 | [G-02, G-05] |
| Apple | Private Cloud Compute 아키텍처 | 2024년 기술 블로그 공개 | [G-06] |
| Google | TPU TEE, Private AI Compute | 2025년 11월 발표 | [G-06] |
| IronCore Labs | 속성보존암호화 기반 벡터 암호화 | 제품 특허 가능성 — 공개 특허 번호 미확인 | [G-04] |
| UC Berkeley | ORAM + HNSW 공동 설계 (Compass) | 학술 논문 기반, 특허 출원 여부 미확인 | [P-01] |

> 데이터 공백: USPTO/Google Patents에서의 직접 검색 미실시 — 추가 검증 필요

---

## 7. 기업 발언 & 보도자료

**IronCore Labs (2025년 7월)**
> "Companies now have the ability to train models using encrypted data that remains private, even to those building or hosting the models." — Cloaked AI 학습 확장 발표 보도자료 [G-04]

**Zama (2025년 Series B 발표)**
> 누적 $150M 이상 조달, FHE 기반 프라이버시 솔루션으로 유니콘 달성. "The privacy revolution of the next decade" — Tracxn/Crunchbase 인용 [G-03]

**Microsoft Azure (2024~2025)**
> "Clients submit encrypted prompts that can only be decrypted within inferencing TEEs, where they are protected from unauthorized access or tampering even by Microsoft." — Azure AI Confidential Inferencing 기술 문서 [G-05]

**Google (2025년 11월)**
> "Private AI Compute brings the privacy of on-device AI to the cloud, giving users faster, more capable AI experiences without compromising data security." — Google 공식 블로그 [G-06]

**Pinecone (2026년 2월)**
> "Enterprise customers can now run Pinecone's data plane inside their own VPC with a zero-access operating model — Pinecone never touches your vectors, metadata, or request payloads." — 벡터 DB 비교 분석 기사 인용 [G-07]

**Gartner (2025년)**
> Gartner, "Cool Vendors in Data Security 2025: Securing Your Data in the Age of GenAI and Quantum Computing"에서 IronCore Labs 선정 [G-04]

---

## 8. 전략적 시사점

### 기회

1. **국내 금융·의료 시장의 프라이빗 RAG 수요**: HIPAA 강화, 금융권 마이데이터, 의료 데이터 3법 등으로 암호화 벡터 검색이 컴플라이언스 필수 요소로 부상 가능
2. **TEE 기반 단기 솔루션**: 순수 FHE 대비 성능 오버헤드가 낮아 상용 배포 가능 — Azure Confidential Computing, Google Private AI Compute 파트너십 활용 여지
3. **DCPE 기반 벡터 암호화 레이어**: IronCore Labs 같은 SDK를 국내 RAG 플랫폼에 통합하는 솔루션 제공 가능
4. **연구 격차**: 국내 학계에서 OSDI·CCS급 암호화 벡터 검색 연구가 희소 — 산학협력 R&D 선점 가능

### 위협

1. **성능 오버헤드의 현실**: FHE 기반은 여전히 수십~수백배 속도 저하. 실시간 RAG에 직접 적용 어려움
2. **글로벌 기술 격차**: Compass(UC Berkeley), PANTHER(CCS'25) 등 학술 최전선은 미국 중심
3. **벤더 락인**: Azure/Google TEE 기반 솔루션 의존 시 클라우드 종속 심화
4. **표준화 부재**: 암호화 벡터 검색 분야의 국제 표준 없음 — 향후 표준 선점 경쟁 예상

### 권고사항

1. **단기(~6개월)**: TEE + DCPE 조합의 프라이빗 RAG PoC 수행. IronCore Labs Cloaked AI 기술 평가
2. **중기(~18개월)**: PANTHER/Compass 오픈소스 구현체 기반 자체 암호화 ANN 레이어 개발 검토
3. **장기(~36개월)**: FHE 가속 하드웨어(삼성, SK하이닉스 PIM) 동향과 연계하여 온디바이스 FHE 벡터 검색 로드맵 수립

---

## 신뢰도 평가

- **높은 확신 [A/B]**:
  - Compass OSDI'25, PANTHER CCS'25, PP-ANNS ICDE'25 논문 존재 및 내용 [P-01~P-04]
  - Zama Series B $57M, 유니콘 달성 (Crunchbase, Tracxn 다중 출처) [G-03]
  - Pinecone BYOC 2026년 2월 출시 [G-07]
  - IronCore Labs Gartner Cool Vendor 2025 선정 [G-04]
  - Google Private AI Compute 2025년 11월 발표 [G-06]

- **추가 검증 필요 [C/D]**:
  - 벡터 DB 시장 규모($2B, CAGR 25~30%) — 단일 비공식 출처
  - 임베딩 역추론 92% 성공률 — Song et al. 2024 원문 직접 확인 필요
  - 국내 의료·금융 시장의 암호화 벡터 검색 수요 — 공개 데이터 없음

- **데이터 공백**:
  - 특허 데이터 (USPTO/Google Patents 직접 검색 미실시)
  - 인텔 스토어 MCP 도구 미활용 (학술 논문 DB 직접 수집 없음)
  - 한국 기업(삼성SDS, LG CNS, SK텔레콤 등)의 대응 현황
  - FHE 하드웨어 가속 현황 (Intel HEXL, Samsung PIM 등)

---

## References

### 글로벌 출처 (G-xx)

| 번호 | 출처명 | 발행일 | 기관 유형 | 제목 | 인용 원문(한글) | 관련성 | 신뢰성 | 최신성 | URL |
|------|--------|-------|---------|------|-------------|--------|--------|--------|-----|
| G-01 | arXiv | 2026-01 | 학술 프리프린트 | Efficient Privacy-Preserving RAG with Distance-Preserving Encryption | ppRAG 프레임워크: CAPRISE 암호화로 비신뢰 클라우드에서 RAG 보호 | 5 | 4 | 5 | https://arxiv.org/abs/2601.12331 |
| G-02 | Microsoft Research | 상시 | 기업 연구소 | Microsoft SEAL — Homomorphic Encryption Library | CKKS 스킴으로 실수/복소수 벡터 연산(거리 계산 등) 지원 | 4 | 5 | 4 | https://github.com/microsoft/SEAL |
| G-03 | Crunchbase / Zama | 2025-06 | 스타트업 / 투자 DB | Zama Series B $57M, Unicorn — FHE Open Source | Concrete ML v1.9: TFHE-rs 지원, LoRA LLM fine-tuning, 유니콘 달성 | 5 | 5 | 5 | https://www.zama.org/ |
| G-04 | IronCore Labs / Wavy.com | 2025-07 | 기업 보도자료 | IronCore Labs Cloaked AI — Encrypted AI Training Data Breakthrough | 암호화 데이터로 AI 모델 훈련, Gartner Cool Vendor 2025 | 5 | 4 | 5 | https://ironcorelabs.com/products/cloaked-ai/ |
| G-05 | Microsoft Learn | 2024~2025 | 공식 기술문서 | Azure Confidential AI — Confidential Inferencing | 암호화 프롬프트, TEE 내에서만 복호화, Microsoft도 접근 불가 | 4 | 5 | 4 | https://learn.microsoft.com/en-us/azure/confidential-computing/confidential-ai |
| G-06 | Google Blog / The Register | 2025-11 | 기업 공식 발표 | Google Private AI Compute — TEE 기반 클라우드 추론 | Titanium Intelligence Enclave, AMD SEV-SNP 활용, 데이터 비보유 | 4 | 5 | 5 | https://blog.google/innovation-and-ai/products/google-private-ai-compute/ |
| G-07 | particula.tech / rahulkolekar.com | 2026-02 | 기술 분석 블로그 | Pinecone BYOC 2026, Weaviate HIPAA, Qdrant SOC 2 비교 | Pinecone BYOC: 고객 VPC 내 실행, 벡터·메타데이터에 Pinecone 접근 불가 | 5 | 3 | 5 | https://rahulkolekar.com/vector-db-pricing-comparison-pinecone-weaviate-2026/ |
| G-08 | HHS / Security Boulevard | 2026-02 | 규제기관 / 보안 미디어 | HIPAA Security Rule 암호화 의무화 추진 | HHS가 HIPAA 보안 규칙에 암호화를 필수 보호 수단으로 추가 검토 | 4 | 4 | 5 | https://securityboulevard.com/2026/02/10-encrypted-email-solutions-for-healthcare-providers-in-2026/ |
| G-09 | Medium / Himansu Saha | 2025-12 | 기술 블로그 | Embedding Inversion + Encrypted Vector DB: Future of Privacy-Aware RAG | 임베딩 역추론 공격으로 92% 확률 원본 재구성 가능 — 암호화 필요성 | 4 | 3 | 5 | https://medium.com/@himansusaha/embedding-inversion-encrypted-vector-db-the-future-of-privacy-aware-rag-e0caf0985ee1 |
| G-10 | Cisco Security | 상시 | 기업 보안 자료 | Securing Vector Databases | 검색가능암호화, Blind Storage, Oblivious RAM의 벡터 DB 적용 | 4 | 4 | 3 | https://sec.cloudapps.cisco.com/security/center/resources/securing-vector-databases |
| G-11 | eprint.iacr.org | 2024-08 | 암호학 프리프린트 | Compass: Encrypted Semantic Search with High Accuracy | ORAM + HNSW 화이트박스 설계, OSDI'25 채택 | 5 | 5 | 4 | https://eprint.iacr.org/2024/1255 |
| G-12 | arXiv | 2025-08 | 학술 프리프린트 | Privacy-Preserving ANN Search on High-Dimensional Data | Distance Comparison Encryption, ICDE'25 채택, 기존 대비 1000배 가속 | 5 | 5 | 5 | https://arxiv.org/pdf/2508.10373 |

### 최신 동향 (N-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색 키워드 | 요약(한글) | URL |
|------|--------|-------|------|-----------|----------|-----|
| N-01 | SitePoint | 2025 | Building a Privacy-Preserving RAG System in the Browser | privacy-preserving RAG 2026 | WebAssembly + 브라우저 내 벡터 DB + 로컬 LLM으로 데이터 외부 전송 없는 RAG | https://www.sitepoint.com/browser-based-rag-private-docs/ |
| N-02 | NSF PAR | 2024 | D-RAG: Privacy-Preserving Framework for Decentralized RAG using Blockchain | privacy RAG decentralized | 블록체인 기반 탈중앙화 RAG로 프라이버시 보호 프레임워크 | https://par.nsf.gov/biblio/10578004-rag-privacy-preserving-framework-decentralized-rag-using-blockchain |
| N-03 | MEXC Blog | 2026 | Zama FHE — $1B Unicorn in Blockchain Privacy | Zama FHE 2026 | Zama, FHE 기반 이더리움/Shibarium 프라이빗 스마트컨트랙트로 블록체인 프라이버시 시장 진출 | https://blog.mexc.com/news/what-is-zama-fhe-the-1b-unicorn-bringing-private-smart-contracts-to-ethereum-and-shibarium-2026/ |
| N-04 | The Hacker News | 2025-11 | Google Launches 'Private AI Compute' — Secure AI Processing | Google confidential AI 2025 | Google Private AI Compute: 온디바이스 수준의 프라이버시를 클라우드로 확장 | https://thehackernews.com/2025/11/google-launches-private-ai-compute.html |
| N-05 | LessWrong | 2025 | Private AI clouds are the future of inference | private AI cloud inference | Apple·Google·Meta 이미 프라이빗 AI 클라우드 운영, OpenAI·Anthropic도 구축 중 | https://www.lesswrong.com/posts/dEGEC9bDwE4mHfdbF/private-ai-clouds-are-the-future-of-inference |

### 기업 발언 (E-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색 키워드 | 요약 원문 |
|------|--------|-------|------|-----------|---------|
| E-01 | IronCore Labs 보도자료 (Wavy.com) | 2025-07 | Cloaked AI Encrypted Training Data Breakthrough | IronCore Labs Cloaked AI 2025 | "Companies now have the ability to train models using encrypted data that remains private, even to those building or hosting the models." |
| E-02 | Microsoft Learn 공식 문서 | 2024-2025 | Azure AI Confidential Inferencing Technical Deep-Dive | Azure confidential AI TEE SGX | "Clients submit encrypted prompts that can only be decrypted within inferencing TEEs, where they are protected from unauthorized access or tampering even by Microsoft." |
| E-03 | Google 공식 블로그 | 2025-11 | Private AI Compute: our next step in building private and helpful AI | Google Private AI Compute 2025 | "Private AI Compute brings the privacy of on-device AI to the cloud, giving users faster, more capable AI experiences without compromising data security." |
| E-04 | Pinecone (벡터 DB 비교 기사 인용) | 2026-02 | Pinecone BYOC Launch | Pinecone BYOC 2026 enterprise | "Enterprise customers can now run Pinecone's data plane inside their own VPC with a zero-access operating model — Pinecone never touches your vectors, metadata, or request payloads." |
| E-05 | Gartner / IronCore Labs | 2025 | Gartner Cool Vendors in Data Security 2025 | IronCore Labs Gartner 2025 | Gartner, "Gartner Cool Vendors in Data Security 2025: Securing Your Data in the Age of GenAI and Quantum Computing"에서 IronCore Labs 선정 |

### 학술 논문 (P-xx)

| 번호 | 저자 | 발행년도 | 제목 | 학술지/컨퍼런스 | 인용수 | 핵심 인용 | DOI/URL |
|------|------|---------|------|----------------|--------|----------|---------|
| P-01 | Jinhao Zhu 외 (UC Berkeley) | 2025 | Compass: Encrypted Semantic Search with High Accuracy | OSDI'25 (USENIX) | 미집계 (신규) | ORAM + HNSW 화이트박스 설계, 체감 지연 ~1초, 서버 메모리 3.2~6.8배 | https://eprint.iacr.org/2024/1255 |
| P-02 | Yingfan Liu, Yandi Zhang 외 | 2025 | Privacy-Preserving Approximate Nearest Neighbor Search on High-Dimensional Data | ICDE'25 (IEEE) | 미집계 (신규) | Distance Comparison Encryption + HNSW, 기존 대비 최대 1,000배 속도 향상 | https://arxiv.org/pdf/2508.10373 |
| P-03 | 공개 정보 미확인 | 2024 | FRAG: Toward Federated Vector Database Management for Collaborative and Secure RAG | arXiv 2410.13272 | 미집계 | 단일 키 HE + 곱셈 캐싱, IND-CPA 보안 보장, 연합 환경 ANN 검색 | https://arxiv.org/abs/2410.13272 |
| P-04 | Li, Huang 외 | 2025 | PANTHER: Private Approximate Nearest Neighbor Search in the Single Server Setting | ACM CCS'25 | 미집계 (신규) | PIR+비밀공유+가블드서킷+HE 혼합, 1천만 포인트 18초, 7.8배 속도↑ | https://dl.acm.org/doi/10.1145/3719027.3765190 |
| P-05 | Huanyi Ye, Jiale Guo, Ziyao Liu, Kwok-Yan Lam | 2026 | Efficient Privacy-Preserving RAG with Distance-Preserving Encryption | arXiv 2601.12331 | 미집계 (신규) | CAPRISE 암호화 + 차분프라이버시, 벡터-텍스트 역추론 공격 방어 | https://arxiv.org/abs/2601.12331 |

### 특허 (T-xx)

| 번호 | 출원인 | 등록/출원일 | 특허번호 | 제목 | 핵심 청구항 | 관할 |
|------|--------|-----------|---------|------|-----------|------|
| - | - | - | - | 공개 정보 없음 (직접 특허 DB 검색 미실시) | - | - |

> T-xx 데이터 공백: intel-store MCP collect_patents 미호출 — 후속 실행 권장

### 내부 자료 (I-xx)

| 번호 | 자료명 | 작성일 | 페이지 | 인용 내용 |
|------|--------|-------|--------|---------|
| I-01 | 2026-03-03_weekly-secure-ai.md | 2026-03-03 | 전체 | secure-ai 도메인 주간 모니터링 — secure-vector-search 🟡 신호 확인, 이번 리서치의 트리거 |
