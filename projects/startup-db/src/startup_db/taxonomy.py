"""Tech taxonomy: L1/L2/L3 hierarchy and sub_category→L1 mapping.

3 L1 domains × 10 L2 areas × 25 L3 technologies.
L3 slugs are stored in su_company_topics; L1/L2 are derived here.
"""

from __future__ import annotations

# L1 → L2 → list[L3 slugs]
TAXONOMY: dict[str, dict[str, list[str]]] = {
    "agentic-ai": {
        "self-evolving-architecture": [
            "agentic-context-engineering",
        ],
        "model-delta-foundry": [
            "feedbackops-prompt",
            "evalops-kms",
            "mlops-pipeline",
            "gpu-orchestration",
        ],
        "trusted-multi-agent-orchestration": [
            "agent-orchestration",
            "agent-oriented-orchestration",
        ],
        "hybrid-ai-infra": [
            "ondevice-slm",
            "speaker-diarization",
            "edge-ai",
            "5g-6g-ai-ran",
        ],
        "intent-recognition": [
            "adaptive-rag",
        ],
    },
    "voice-ai": {
        "speech-perception-interaction": [
            "emotional-analysis",
            "context-recognition",
            "interrupt-turn-taking",
        ],
        "personal-intelligence": [
            "persona-plugin",
            "relationship-graph",
            "context-action-recommendation",
        ],
        "speech-generation": [
            "voice-cloning",
            "voice-synthesis",
        ],
    },
    "secure-ai": {
        "spam-phishing-detection": [
            "spam-phishing-detection",
            "ocr-image-spam",
        ],
        "quantum-homomorphic-encryption": [
            "pqc-voice-encryption",
            "he-keyword-search",
            "secure-vector-search",
        ],
    },
}

# sub_category → L1 slug mapping (for backfill and Obsidian export)
L1_BY_SUBCATEGORY: dict[str, str] = {
    # Agentic AI
    "Work Agent": "agentic-ai",
    "Media Agent": "agentic-ai",
    "Agent": "agentic-ai",
    "Coding Agent": "agentic-ai",
    "Mobile Agent": "agentic-ai",
    "Home Agent": "agentic-ai",
    "LAM": "agentic-ai",
    "RAG": "agentic-ai",
    "AI 검색": "agentic-ai",
    "LLM": "agentic-ai",
    "sLLM": "agentic-ai",
    "sLM": "agentic-ai",
    "AI Ops": "agentic-ai",
    "ML Ops": "agentic-ai",
    "MLOps": "agentic-ai",
    "개인화": "agentic-ai",
    # Voice AI
    "Speech": "voice-ai",
    "AICC": "voice-ai",
    "mVoIP": "voice-ai",
    # Secure AI
    "안심 / 보안": "secure-ai",
}

# L1 display labels
L1_LABELS: dict[str, str] = {
    "agentic-ai": "Agentic AI",
    "voice-ai": "Voice AI",
    "secure-ai": "Secure AI",
}

# L1 colors for UI badges
L1_COLORS: dict[str, str] = {
    "agentic-ai": "#6366F1",  # indigo
    "voice-ai": "#0EA5E9",  # sky
    "secure-ai": "#F59E0B",  # amber
}

# ── Pre-built reverse indexes ──────────────────────────────────

_l3_to_l2: dict[str, str] = {}
_l3_to_l1: dict[str, str] = {}
_l2_to_l1: dict[str, str] = {}

for _l1, _l2_map in TAXONOMY.items():
    for _l2, _l3_list in _l2_map.items():
        _l2_to_l1[_l2] = _l1
        for _l3 in _l3_list:
            _l3_to_l2[_l3] = _l2
            _l3_to_l1[_l3] = _l1


def get_l1_for_l3(slug: str) -> str | None:
    """Return the L1 domain for a given L3 slug."""
    return _l3_to_l1.get(slug)


def get_l2_for_l3(slug: str) -> str | None:
    """Return the L2 area for a given L3 slug."""
    return _l3_to_l2.get(slug)


def get_l3_slugs_for_l1(l1: str) -> list[str]:
    """Return all L3 slugs belonging to an L1 domain."""
    result: list[str] = []
    for l2_map in TAXONOMY.get(l1, {}).values():
        result.extend(l2_map)
    return result


def get_l3_slugs_for_l2(l2: str) -> list[str]:
    """Return all L3 slugs belonging to an L2 area."""
    l1 = _l2_to_l1.get(l2)
    if not l1:
        return []
    return list(TAXONOMY[l1].get(l2, []))


def get_all_l3_slugs() -> list[str]:
    """Return all 25 L3 slugs."""
    return list(_l3_to_l1.keys())


def get_l2_slugs_for_l1(l1: str) -> list[str]:
    """Return all L2 slugs belonging to an L1 domain."""
    return list(TAXONOMY.get(l1, {}).keys())


def is_valid_l3(slug: str) -> bool:
    """Check if a slug is a valid L3 technology."""
    return slug in _l3_to_l1
