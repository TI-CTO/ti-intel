# 기술전략 분류체계 (Tech Taxonomy)

3개 도메인(L1) × 10개 기술영역(L2) × 25개 세부기술(L3).
`/weekly-monitor` 스킬과 WTIS 파이프라인에서 참조한다.

---

## Agentic AI (월요일)

### 1. Self Evolving Architecture
| L3 | slug | 검색 키워드 |
|----|------|------------|
| a. Agentic Context Engineering | `agentic-context-engineering` | context window management, self-improving agents, meta-learning agents |

### 2. Model & Delta Foundry
| L3 | slug | 검색 키워드 |
|----|------|------------|
| a. FeedbackOps: 자율형 Meta-prompt Engineering PoC | `feedbackops-prompt` | automated prompt optimization, DSPy, prompt tuning, meta-prompt |
| b. EvaluationOps: KMS 성능평가 자동화 PoC | `evalops-kms` | LLM evaluation automation, RAGAS, LLM-as-judge, KMS benchmark |
| c. 데이터-학습-배포 통합 자동화 파이프라인 | `mlops-pipeline` | MLOps pipeline, LLMOps, fine-tuning CI/CD |
| d. 하이브리드 GPU Orchestration | `gpu-orchestration` | GPU cluster orchestration, Ray, Skypilot, hybrid GPU |

### 3. Trusted Multi-Agent Orchestration
| L3 | slug | 검색 키워드 |
|----|------|------------|
| a. Intelligent Agent Orchestration | `agent-orchestration` | multi-agent orchestration, LangGraph, CrewAI, AutoGen |
| b. Agent Oriented Orchestration | `agent-oriented-orchestration` | agent-oriented planning, task decomposition, ReAct, tree-of-thought |

### 4. Hybrid AI Infra
| L3 | slug | 검색 키워드 |
|----|------|------------|
| a. On-Device sLM | `ondevice-slm` | on-device small language model, edge LLM, TinyLLM |
| b. 실시간 화자분할(2인) 기술 확보 | `speaker-diarization` | real-time speaker diarization, two-speaker separation |
| c. Edge AI | `edge-ai` | edge AI inference, on-device AI, edge computing AI |
| d. 5G SA/6G(AI-RAN/SRv6) | `5g-6g-ai-ran` | 5G standalone, 6G, AI-RAN, SRv6, network AI |

### 5. 의도 파악 기술
| L3 | slug | 검색 키워드 |
|----|------|------------|
| a. Adaptive RAG | `adaptive-rag` | adaptive RAG, self-reflective RAG, CRAG, query routing |

---

## Voice AI (화요일)

### 6. Speech Perception & Interaction
| L3 | slug | 검색 키워드 |
|----|------|------------|
| a. Emotional Analysis | `emotional-analysis` | speech emotion recognition, voice sentiment analysis, affective computing |
| b. Context Recognition | `context-recognition` | conversational context understanding, dialogue state tracking |
| c. Interrupt & Turn-Taking | `interrupt-turn-taking` | turn-taking prediction, barge-in detection, conversational flow |

### 7. Personal Intelligence
| L3 | slug | 검색 키워드 |
|----|------|------------|
| a. 페르소나 플러그인 기술 고도화 | `persona-plugin` | persona-based AI, user profile adaptation |
| b. 관계 그래프 구축 기술 확보 | `relationship-graph` | knowledge graph construction, social graph AI |
| c. 컨텍스트 기반 액션 추천 기술 확보 | `context-action-recommendation` | context-aware recommendation, proactive AI assistant |

### 8. Speech Generation
| L3 | slug | 검색 키워드 |
|----|------|------------|
| a. Voice Cloning | `voice-cloning` | voice cloning, speaker adaptation, zero-shot TTS |
| b. Voice Synthesis | `voice-synthesis` | text-to-speech, neural TTS, speech synthesis |

---

## Secure AI (수요일)

### 9. 스팸/피싱탐지
| L3 | slug | 검색 키워드 |
|----|------|------------|
| a. 스팸/피싱 감지(통화전) | `spam-phishing-detection` | pre-call spam detection, AI scam detection, voice phishing |
| b. OCR 활용 이미지 스팸 차단 | `ocr-image-spam` | image spam detection OCR, visual spam filtering |

### 10. 양자/동형 암호
| L3 | slug | 검색 키워드 |
|----|------|------------|
| a. On-Device 양자암호: 통화 녹음 파일 암호화 | `pqc-voice-encryption` | post-quantum cryptography PQC, voice encryption, CRYSTALS-Kyber |
| b. On-Device 동형암호: 키워드 검색 | `he-keyword-search` | homomorphic encryption CKKS, encrypted keyword search |
| c. Secure Vector Search: B2B AICC 동형암호 적용 | `secure-vector-search` | encrypted vector search, privacy-preserving AICC, FHE vector |

---

## Slug 전체 목록 (quick reference)

```
# Agentic AI (10)
agentic-context-engineering
feedbackops-prompt
evalops-kms
mlops-pipeline
gpu-orchestration
agent-orchestration
agent-oriented-orchestration
ondevice-slm
speaker-diarization
edge-ai
5g-6g-ai-ran
adaptive-rag

# Voice AI (8)
emotional-analysis
context-recognition
interrupt-turn-taking
persona-plugin
relationship-graph
context-action-recommendation
voice-cloning
voice-synthesis

# Secure AI (5)
spam-phishing-detection
ocr-image-spam
pqc-voice-encryption
he-keyword-search
secure-vector-search
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
