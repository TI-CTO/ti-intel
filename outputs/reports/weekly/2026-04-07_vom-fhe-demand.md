---
topic: ondevice-fhe
date: 2026-04-07
agent: voice-of-market
videos_analyzed: 3
hn_threads_analyzed: 2
---

## 시장 수요 시그널: 동형암호 (FHE)

### 고객 페인포인트

- **클라우드 배포 시 FHE 자체보다 주변 인프라가 더 복잡** — Intel Labs의 금융기관 대상 PoC(Proof of Concept) 사례에서 발표자 Flavio Bergamaschi는 "FHE now became the smallest part on the deployment — everything that you have to put around is something that we normally don't consider"라고 직접 발언. FHE 쿼리 엔진 외에 HSM 키 관리, TEE(Trusted Execution Environment) 통합, Kafka 메시지 인프라, 클라이언트-서버 보안 채널이 모두 별도 구축 필요. 출처: FHE Deployment Challenges for Secure Cloud Computing (Flavio Bergamaschi, Intel Labs)

- **기존 PKI/HSM과의 통합 불가 문제** — "HSM cannot cope with FHE keys — they're going to say 'you just spent a few million dollars on the current system and you're telling me you need a new one.'" FHE 키가 기존 하드웨어 보안 모듈 규격을 초과하여 기업 고객이 별도 소프트 HSM 구축을 강요받는 상황. 출처: FHE Deployment Challenges for Secure Cloud Computing (Flavio Bergamaschi, Intel Labs)

- **FHE 단독으로 완전한 보안 보장 불가** — "FHE by itself does not provide all these additional guarantees." 쿼리 의도 은닉 외에 코드 무결성 증명, 데이터 무결성, INCPAD 공격 방어는 FHE가 해결하지 못하여 TEE와 함께 사용해야 한다는 한계. 출처: FHE Deployment Challenges for Secure Cloud Computing (Flavio Bergamaschi, Intel Labs)

- **FHE 적용 프로그램 작성의 높은 진입 장벽** — Google HEIR 컴파일러 프로젝트에서 Jeremy Kun은 "Python front end — this was our number one most requested feature"라고 언급. 기존에는 개발자가 FHE 전문 지식 없이 암호화 코드를 작성하는 것이 거의 불가능했음을 시사. 출처: Updates on the HEIR Compiler Project (Jeremy Kun, Google)

- **LLM 등 대규모 모델의 FHE 실행 불가** — HEIR 발표 중 "someone said they were doing LLMs — it takes a long time to run an LLM in FHE." HN 댓글에서도 "FHE computational overhead makes it impossible to run ML workloads except for very small models"라는 실무자 평가 존재. 출처: Updates on the HEIR Compiler Project (Jeremy Kun, Google); HN 쓰레드 #45323027

- **성능 오버헤드: 수천~수만 배** — HN 실무자 커뮤니티에서 "adding two integers takes 7 seconds", "many many many orders of magnitude slower", 메모리 오버헤드 약 20,000배 지적. 9MB 영상 파일이 FHE 암호화 시 188GB로 증가하는 구체 사례 언급. 출처: HN 쓰레드 #34783447 (Google FHE Compiler 프라이머 논의)

### 도입 장벽

- **FHE 파라미터 선택의 전문성 요구** — OpenFHE 발표에서 Yuriy Polyakov(Duality)가 기본 모드에서는 모듈 스위칭·키 스위칭이 자동화되어 있지만, 최적화를 위해서는 "developer or compiler can fine-tune those"라고 설명. HEIR 프로젝트도 "we've implemented four noise models" 및 파라미터 선택 연구 별도 추진이라 언급하여 여전히 자동화 미완성. 출처: OpenFHE (Yuriy Polyakov, Duality); Updates on the HEIR Compiler Project (Jeremy Kun, Google)

- **하드웨어 가속기 생태계 미성숙** — HEIR 발표에서 "the compiler is not ready yet for hardware integration and the hardware folks need to build something — we're meeting them in the middle." FHE 전용 가속기(Cornami, Optalysis, Intel, BelFort 등)와 컴파일러 간 코드젠 표준이 아직 수렴되지 않아 실제 하드웨어 가속 효과를 측정할 벤치마크조차 미확정. 출처: Updates on the HEIR Compiler Project (Jeremy Kun, Google)

- **ML 모델 포맷 호환성 부재** — Google은 PyTorch/TensorFlow 모델을 FHE로 컴파일하는 기능 목표를 가지고 있으나 "we are just blocked on us not implementing all of the random weird reshaping and transposing that just falls out of naturally exporting." ML 모델의 텐서 연산(transpose, reshape 등)이 FHE에 적합하지 않은 형태로 표출되어 엔드-투-엔드 파이프라인 구축 지연. 출처: Updates on the HEIR Compiler Project (Jeremy Kun, Google)

- **풀-테이블 스캔 강제 — 쿼리 효율성 문제** — Intel Labs PoC에서 청중 질의에 대해 발표자가 "when you do the query, does it have to touch every single record? Yes. It's a full table scan."이라 직접 확인. 데이터베이스 규모가 커질수록 FHE 쿼리 비용이 선형 증가하는 구조적 한계. 출처: FHE Deployment Challenges for Secure Cloud Computing (Flavio Bergamaschi, Intel Labs)

- **신뢰 모델의 논리적 모순** — HN 커뮤니티에서 "if the service provider is actually untrustworthy, it's better not to send sensitive data in the first place"라는 근본적 의문 제기. FHE의 실용적 적용 범위가 극히 제한적이라는 회의론이 개발자 커뮤니티에 형성되어 있음. 출처: HN 쓰레드 #34783447

- **BGV/BFV bootstrapping 미완성** — OpenFHE 발표에서 "there is still a gap compared to HEAAN in terms of BGV/BFV bootstrapping — the field is still unstable, many improvements being made." 특히 정수형 연산 스킴에서 bootstrapping 불안정으로 연속 연산 횟수 제한. 출처: OpenFHE (Yuriy Polyakov, Duality)

### 시장 니즈

- **FHE를 위한 Python 친화적 개발 환경** — "Python front end was our number one most requested feature" (Jeremy Kun, Google). FHE 전문가가 아닌 일반 개발자가 접근 가능한 고수준 인터페이스 수요가 커뮤니티 내 가장 높은 우선순위로 확인됨. 출처: Updates on the HEIR Compiler Project (Jeremy Kun, Google)

- **기존 ML 파이프라인과의 원활한 통합** — Google이 2025년 내 목표로 "full support for PyTorch, full support for TensorFlow — make it very easy to take a pre-compiled model, load it into HEIR, and have smart packing"을 공식화. FHE를 별도 시스템이 아닌 기존 ML 워크플로우 안에 통합하는 니즈. 출처: Updates on the HEIR Compiler Project (Jeremy Kun, Google)

- **금융·의료 분야 Private Query 서비스** — Intel Labs PoC는 금융기관 간 공유 데이터베이스에 대해 쿼리 의도를 숨기면서 검색하는 서비스 모델 실증. "client wants to conceal the intent in the query and on the server side the server doesn't even know what you're asking for." 금융 규제 환경에서 데이터 공유 없이 협력하는 구체적 수요. 출처: FHE Deployment Challenges for Secure Cloud Computing (Flavio Bergamaschi, Intel Labs)

- **FHE 전용 하드웨어 가속기** — HEIR 로드맵에서 "starting in 2026, we'd like to start implementing the crypto that's right for each of these hardware accelerators directly in the compiler." Cornami, Optalysis, Intel, BelFort 등 다수 업체가 FHE 가속 하드웨어를 개발 중이며 컴파일러-하드웨어 통합 수요 형성. 출처: Updates on the HEIR Compiler Project (Jeremy Kun, Google)

- **헬스케어 유전체·종양 데이터 분석** — OpenFHE 생태계 분석에서 "healthcare applications — analysis of oncological data, GWAS" 다수 사례 확인. "CKS even outperformed certain MPC solutions" 언급으로 의료 데이터 연합 분석에서 FHE의 실용적 경쟁력이 일부 확인됨. 출처: OpenFHE (Yuriy Polyakov, Duality)

- **Threshold FHE 기반 분산 처리** — OpenFHE가 BGV, BFV, CKKS 스킴에 Threshold FHE를 지원하며 "private, verifiable voting systems using Threshold FHE" 등 다자간 협력 프라이버시 시나리오 수요 제시 (Zama 발표 기준). 출처: Zama at FHE.org 2026 (Zama)

### 분석 소스

| 소스 | 제목 | 유형 | 날짜 |
|------|------|------|------|
| Flavio Bergamaschi (Intel Labs) | FHE Deployment Challenges for Secure Cloud Computing | YouTube / FHE.org 2025 | 2025-03 |
| Jeremy Kun (Google) | Updates on the HEIR Compiler Project | YouTube / FHE.org 2025 | 2025-03 |
| Yuriy Polyakov (Duality) | OpenFHE: Open-Source Fully Homomorphic Encryption Library | YouTube / FHE.org 2025 | 2025-03 |
| HN 커뮤니티 | The Beginner's Textbook for Fully Homomorphic Encryption | Hacker News #45323027 | 2025 |
| HN 커뮤니티 | Google's fully homomorphic encryption compiler – a primer | Hacker News #34783447 | 2023 |
