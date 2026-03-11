-- Register 25 L3 topics for the new taxonomy (2026-03-11)
-- Replaces old L1-level topics (secure-ai, agentic-ai, etc.) with L3 granularity.
-- Idempotent: ON CONFLICT DO NOTHING.

-- ============================================================
-- Agentic AI domain (12 L3)
-- ============================================================

-- L2: Self Evolving Architecture
INSERT INTO topics (slug, display_name, description)
VALUES ('agentic-context-engineering', 'Agentic Context Engineering', 'Context window management, self-improving agents, meta-learning agents')
ON CONFLICT (slug) DO NOTHING;

-- L2: Model & Delta Foundry
INSERT INTO topics (slug, display_name, description)
VALUES ('feedbackops-prompt', 'FeedbackOps: Meta-prompt Engineering', 'Automated prompt optimization, DSPy, prompt tuning, meta-prompt')
ON CONFLICT (slug) DO NOTHING;

INSERT INTO topics (slug, display_name, description)
VALUES ('evalops-kms', 'EvaluationOps: KMS Benchmark', 'LLM evaluation automation, RAGAS, LLM-as-judge, KMS benchmark')
ON CONFLICT (slug) DO NOTHING;

INSERT INTO topics (slug, display_name, description)
VALUES ('mlops-pipeline', 'MLOps Pipeline', 'Data-training-deploy integrated automation pipeline, LLMOps, fine-tuning CI/CD')
ON CONFLICT (slug) DO NOTHING;

INSERT INTO topics (slug, display_name, description)
VALUES ('gpu-orchestration', 'Hybrid GPU Orchestration', 'GPU cluster orchestration, Ray, Skypilot, hybrid GPU')
ON CONFLICT (slug) DO NOTHING;

-- L2: Trusted Multi-Agent Orchestration
INSERT INTO topics (slug, display_name, description)
VALUES ('agent-orchestration', 'Intelligent Agent Orchestration', 'Multi-agent orchestration, LangGraph, CrewAI, AutoGen')
ON CONFLICT (slug) DO NOTHING;

INSERT INTO topics (slug, display_name, description)
VALUES ('agent-oriented-orchestration', 'Agent Oriented Orchestration', 'Agent-oriented planning, task decomposition, ReAct, tree-of-thought')
ON CONFLICT (slug) DO NOTHING;

-- L2: Hybrid AI Infra
INSERT INTO topics (slug, display_name, description)
VALUES ('ondevice-slm', 'On-Device sLM', 'On-device small language model, edge LLM, TinyLLM')
ON CONFLICT (slug) DO NOTHING;

INSERT INTO topics (slug, display_name, description)
VALUES ('speaker-diarization', 'Speaker Diarization', 'Real-time speaker diarization, two-speaker separation')
ON CONFLICT (slug) DO NOTHING;

INSERT INTO topics (slug, display_name, description)
VALUES ('edge-ai', 'Edge AI', 'Edge AI inference, on-device AI, edge computing AI')
ON CONFLICT (slug) DO NOTHING;

INSERT INTO topics (slug, display_name, description)
VALUES ('5g-6g-ai-ran', '5G SA/6G (AI-RAN/SRv6)', '5G standalone, 6G, AI-RAN, SRv6, network AI')
ON CONFLICT (slug) DO NOTHING;

-- L2: 의도 파악 기술
INSERT INTO topics (slug, display_name, description)
VALUES ('adaptive-rag', 'Adaptive RAG', 'Adaptive RAG, self-reflective RAG, CRAG, query routing')
ON CONFLICT (slug) DO NOTHING;

-- ============================================================
-- Voice AI domain (8 L3)
-- ============================================================

-- L2: Speech Perception & Interaction
INSERT INTO topics (slug, display_name, description)
VALUES ('emotional-analysis', 'Emotional Analysis', 'Speech emotion recognition, voice sentiment analysis, affective computing')
ON CONFLICT (slug) DO NOTHING;

INSERT INTO topics (slug, display_name, description)
VALUES ('context-recognition', 'Context Recognition', 'Conversational context understanding, dialogue state tracking')
ON CONFLICT (slug) DO NOTHING;

INSERT INTO topics (slug, display_name, description)
VALUES ('interrupt-turn-taking', 'Interrupt & Turn-Taking', 'Turn-taking prediction, barge-in detection, conversational flow')
ON CONFLICT (slug) DO NOTHING;

-- L2: Personal Intelligence
INSERT INTO topics (slug, display_name, description)
VALUES ('persona-plugin', 'Persona Plugin', 'Persona-based AI, user profile adaptation')
ON CONFLICT (slug) DO NOTHING;

INSERT INTO topics (slug, display_name, description)
VALUES ('relationship-graph', 'Relationship Graph', 'Knowledge graph construction, social graph AI')
ON CONFLICT (slug) DO NOTHING;

INSERT INTO topics (slug, display_name, description)
VALUES ('context-action-recommendation', 'Context Action Recommendation', 'Context-aware recommendation, proactive AI assistant')
ON CONFLICT (slug) DO NOTHING;

-- L2: Speech Generation
INSERT INTO topics (slug, display_name, description)
VALUES ('voice-cloning', 'Voice Cloning', 'Voice cloning, speaker adaptation, zero-shot TTS')
ON CONFLICT (slug) DO NOTHING;

INSERT INTO topics (slug, display_name, description)
VALUES ('voice-synthesis', 'Voice Synthesis', 'Text-to-speech, neural TTS, speech synthesis')
ON CONFLICT (slug) DO NOTHING;

-- ============================================================
-- Secure AI domain (5 L3)
-- ============================================================

-- L2: 스팸/피싱탐지
INSERT INTO topics (slug, display_name, description)
VALUES ('spam-phishing-detection', 'Spam/Phishing Detection', 'Pre-call spam detection, AI scam detection, voice phishing')
ON CONFLICT (slug) DO NOTHING;

INSERT INTO topics (slug, display_name, description)
VALUES ('ocr-image-spam', 'OCR Image Spam Detection', 'Image spam detection OCR, visual spam filtering')
ON CONFLICT (slug) DO NOTHING;

-- L2: 양자/동형 암호
INSERT INTO topics (slug, display_name, description)
VALUES ('pqc-voice-encryption', 'PQC Voice Encryption', 'Post-quantum cryptography PQC, voice encryption, CRYSTALS-Kyber')
ON CONFLICT (slug) DO NOTHING;

INSERT INTO topics (slug, display_name, description)
VALUES ('he-keyword-search', 'HE Keyword Search', 'Homomorphic encryption CKKS, encrypted keyword search')
ON CONFLICT (slug) DO NOTHING;

INSERT INTO topics (slug, display_name, description)
VALUES ('secure-vector-search', 'Secure Vector Search', 'Encrypted vector search, privacy-preserving AICC, FHE vector')
ON CONFLICT (slug) DO NOTHING;
