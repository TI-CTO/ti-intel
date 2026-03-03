# LG U+ 기술전략 분류체계 (Tech Taxonomy)

3개 도메인(L1) × 9개 기술영역(L2) × 18개 세부기술(L3).
`/weekly-monitor` 스킬과 WTIS 파이프라인에서 참조한다.

---

## Agentic AI (월요일)

### 1. 의도파악기술
| L3 | slug | 검색 키워드 |
|----|------|------------|
| a. Adaptive RAG | `adaptive-rag` | adaptive RAG, self-reflective RAG, CRAG, query routing |

### 2. Multi-Agent
| L3 | slug | 검색 키워드 |
|----|------|------------|
| a. Intelligent Agent Orchestration | `agent-orchestration` | multi-agent orchestration, LangGraph, CrewAI, AutoGen |
| b. Agent Oriented Planning | `agent-planning` | LLM planning, task decomposition, ReAct, tree-of-thought |

### 3. Self Evolving Agent
| L3 | slug | 검색 키워드 |
|----|------|------------|
| a. Agentic Context Engineering | `agentic-context-engineering` | context window management, self-improving agents, meta-learning agents |

### 4. 관계추론기술
| L3 | slug | 검색 키워드 |
|----|------|------------|
| a. 페르소나 플러그인 기술 | `persona-plugin` | persona-based AI, user profile adaptation |
| b. 관계 그래프 구축 기술 | `relationship-graph` | knowledge graph construction, social graph AI |
| c. 컨텍스트 기반 액션 추천 기술 | `context-action-recommendation` | context-aware recommendation, proactive AI assistant |

---

## Secure AI (수요일)

### 5. OnDevice AI
| L3 | slug | 검색 키워드 |
|----|------|------------|
| a. OnDevice sLM | `ondevice-slm` | on-device small language model, edge LLM, TinyLLM |
| b. 실시간 화자분할(2인) | `speaker-diarization` | real-time speaker diarization, two-speaker separation |

### 6. 스팸/피싱/탐지
| L3 | slug | 검색 키워드 |
|----|------|------------|
| a. 스팸피싱감지(통화전) | `spam-phishing-detection` | pre-call spam detection, AI scam detection, voice phishing |
| b. OCR 이미지 스팸 차단 | `ocr-image-spam` | image spam detection OCR, visual spam filtering |

### 7. 양자동형암호
| L3 | slug | 검색 키워드 |
|----|------|------------|
| a. OnDevice 양자암호 | `ondevice-pqc` | post-quantum cryptography PQC, CRYSTALS-Kyber |
| b. OnDevice 동형암호 | `ondevice-he` | homomorphic encryption CKKS, encrypted keyword search |
| c. Secure Vector Search | `secure-vector-search` | encrypted vector search, privacy-preserving AICC |

---

## AXOps (금요일)

### 8. FeedBackOps/EvalOps
| L3 | slug | 검색 키워드 |
|----|------|------------|
| a. FeedBackOps Meta Prompt Eng. | `feedbackops-prompt` | automated prompt optimization, DSPy, prompt tuning |
| b. EvalOps KMS 성능평가 | `evalops-kms` | LLM evaluation automation, RAGAS, LLM-as-judge |

### 9. ML/LLMOps
| L3 | slug | 검색 키워드 |
|----|------|------------|
| a. 학습 배포 통합 파이프라인 | `mlops-pipeline` | MLOps pipeline, LLMOps, fine-tuning CI/CD |
| b. 하이브리드 GPU Orchestration | `gpu-orchestration` | GPU cluster orchestration, Ray, Skypilot |

---

## Slug 전체 목록 (quick reference)

```
# Agentic AI (7)
adaptive-rag
agent-orchestration
agent-planning
agentic-context-engineering
persona-plugin
relationship-graph
context-action-recommendation

# Secure AI (7)
ondevice-slm
speaker-diarization
spam-phishing-detection
ocr-image-spam
ondevice-pqc
ondevice-he
secure-vector-search

# AXOps (4)
feedbackops-prompt
evalops-kms
mlops-pipeline
gpu-orchestration
```

## 쿼리 확장 규칙

키워드를 OR로 연결하여 검색:
```
"{회사용어}" OR "{업계키워드1}" OR "{업계키워드2}"
```

예시:
```
"Adaptive RAG" OR "self-reflective RAG" OR "CRAG" OR "query routing"
```
