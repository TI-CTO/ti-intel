"""Register 25 L3 technology topics in Supabase.

Inserts into `topics` table, then registers each as a `watch_topic` (weekly).
Uses the trend-tracker Supabase client for DB access.

Usage:
    cd projects/trend-tracker && ~/.local/bin/uv run python ../../scripts/register_l3_topics.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Add trend-tracker src to path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "projects" / "trend-tracker" / "src"))

from trend_tracker.db.client import get_client  # noqa: E402

L3_TOPICS: list[dict] = [
    # ── Agentic AI ──
    {
        "slug": "adaptive-rag",
        "display_name": "Adaptive RAG",
        "description": "Self-reflective RAG, CRAG, query routing for intent understanding",
        "keywords": ["adaptive RAG", "self-reflective RAG", "CRAG", "query routing"],
    },
    {
        "slug": "agent-orchestration",
        "display_name": "Intelligent Agent Orchestration",
        "description": "Multi-agent orchestration frameworks (LangGraph, CrewAI, AutoGen)",
        "keywords": ["multi-agent orchestration", "LangGraph", "CrewAI", "AutoGen"],
    },
    {
        "slug": "agent-planning",
        "display_name": "Agent Oriented Planning",
        "description": "LLM planning, task decomposition, ReAct, tree-of-thought",
        "keywords": ["LLM planning", "task decomposition", "ReAct", "tree-of-thought"],
    },
    {
        "slug": "agentic-context-engineering",
        "display_name": "Agentic Context Engineering",
        "description": "Context window management, self-improving agents, meta-learning",
        "keywords": ["context window management", "self-improving agents", "meta-learning agents"],
    },
    {
        "slug": "persona-plugin",
        "display_name": "페르소나 플러그인 기술",
        "description": "Persona-based AI, user profile adaptation",
        "keywords": ["persona-based AI", "user profile adaptation"],
    },
    {
        "slug": "relationship-graph",
        "display_name": "관계 그래프 구축 기술",
        "description": "Knowledge graph construction, social graph AI",
        "keywords": ["knowledge graph construction", "social graph AI"],
    },
    {
        "slug": "context-action-recommendation",
        "display_name": "컨텍스트 기반 액션 추천",
        "description": "Context-aware recommendation, proactive AI assistant",
        "keywords": ["context-aware recommendation", "proactive AI assistant"],
    },
    # ── Secure AI ──
    {
        "slug": "ondevice-slm",
        "display_name": "OnDevice sLM",
        "description": "On-device small language model, edge LLM, TinyLLM",
        "keywords": ["on-device small language model", "edge LLM", "TinyLLM"],
    },
    {
        "slug": "speaker-diarization",
        "display_name": "실시간 화자분할(2인)",
        "description": "Real-time speaker diarization, two-speaker separation",
        "keywords": ["real-time speaker diarization", "two-speaker separation"],
    },
    {
        "slug": "spam-phishing-detection",
        "display_name": "스팸피싱감지(통화전)",
        "description": "Pre-call spam detection, AI scam detection, voice phishing",
        "keywords": ["pre-call spam detection", "AI scam detection", "voice phishing"],
    },
    {
        "slug": "ocr-image-spam",
        "display_name": "OCR 이미지 스팸 차단",
        "description": "Image spam detection OCR, visual spam filtering",
        "keywords": ["image spam detection OCR", "visual spam filtering"],
    },
    {
        "slug": "ondevice-pqc",
        "display_name": "OnDevice 양자암호",
        "description": "Post-quantum cryptography PQC, CRYSTALS-Kyber",
        "keywords": ["post-quantum cryptography PQC", "CRYSTALS-Kyber"],
    },
    {
        "slug": "ondevice-he",
        "display_name": "OnDevice 동형암호",
        "description": "Homomorphic encryption CKKS, encrypted keyword search",
        "keywords": ["homomorphic encryption CKKS", "encrypted keyword search"],
    },
    {
        "slug": "secure-vector-search",
        "display_name": "Secure Vector Search",
        "description": "Encrypted vector search, privacy-preserving AICC",
        "keywords": ["encrypted vector search", "privacy-preserving AICC"],
    },
    # ── Agentic AI: Model & Delta Foundry ──
    {
        "slug": "feedbackops-prompt",
        "display_name": "FeedBackOps Meta Prompt Engineering",
        "description": "Automated prompt optimization, DSPy, prompt tuning",
        "keywords": ["automated prompt optimization", "DSPy", "prompt tuning"],
    },
    {
        "slug": "evalops-kms",
        "display_name": "EvalOps KMS 성능평가",
        "description": "LLM evaluation automation, RAGAS, LLM-as-judge",
        "keywords": ["LLM evaluation automation", "RAGAS", "LLM-as-judge"],
    },
    {
        "slug": "mlops-pipeline",
        "display_name": "학습 배포 통합 파이프라인",
        "description": "MLOps pipeline, LLMOps, fine-tuning CI/CD",
        "keywords": ["MLOps pipeline", "LLMOps", "fine-tuning CI/CD"],
    },
    {
        "slug": "gpu-orchestration",
        "display_name": "하이브리드 GPU Orchestration",
        "description": "GPU cluster orchestration, Ray, Skypilot",
        "keywords": ["GPU cluster orchestration", "Ray", "Skypilot"],
    },
]


def main() -> None:
    client = get_client()

    print(f"Registering {len(L3_TOPICS)} L3 topics...\n")

    success = 0
    errors = 0

    for entry in L3_TOPICS:
        slug = entry["slug"]
        keywords = entry.pop("keywords")

        # 1. Insert into topics table (skip if already exists)
        topic_row = {
            "slug": entry["slug"],
            "display_name": entry["display_name"],
            "description": entry["description"],
        }
        try:
            result = client.table("topics").upsert(
                topic_row, on_conflict="slug"
            ).execute()
            topic_id = result.data[0]["id"]
            print(f"  [topics] {slug} → id={topic_id}")
        except Exception as e:
            print(f"  [topics] {slug} FAILED: {e}")
            errors += 1
            continue

        # 2. Register as watch_topic (weekly)
        watch_row = {
            "topic_id": topic_id,
            "keywords": json.dumps(keywords, ensure_ascii=False),
            "frequency": "weekly",
            "is_active": True,
        }
        try:
            client.table("watch_topics").upsert(
                watch_row, on_conflict="topic_id"
            ).execute()
            print(f"  [watch]  {slug} → weekly, keywords={len(keywords)}")
            success += 1
        except Exception as e:
            print(f"  [watch]  {slug} FAILED: {e}")
            errors += 1

    print(f"\nDone: {success} registered, {errors} errors")


if __name__ == "__main__":
    main()
