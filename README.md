# SHL Intelligent Assessment Recommendation Engine

An enterprise-style AI-powered recommendation platform for SHL assessments.

This system goes beyond basic retrieval by combining:
- deterministic orchestration,
- policy-driven recommendation planning,
- hybrid retrieval,
- consultative intelligence,
- battery coherence validation,
- explanation generation,
- conversational refinement handling.

The project is designed to simulate a production-grade hiring recommendation assistant rather than a simple chatbot.

---

# Features

## Intelligent Recommendation Orchestration
- Context-aware recommendation generation
- Multi-turn hiring refinement support
- Leadership and behavioral assessment inference
- Technical + cognitive + personality battery balancing

## Hybrid Retrieval System
- BM25 lexical retrieval
- Embedding-based semantic retrieval
- Hybrid reranking pipeline

## Policy-Driven Recommendation Planning
- Hiring intent inference
- Domain routing
- Battery planning
- Assessment diversity validation
- Redundancy suppression

## Consultative AI Behavior
- Clarification handling
- Recommendation refinement
- Context-aware follow-up guidance
- Assessment comparison support

## Explainability & Observability
- Recommendation explanations
- Debug trace system
- Transparent orchestration visibility

---

# System Architecture

## High-Level Flow

User Query
↓
Conversation Analysis
↓
Frame Extraction
↓
Hiring Intent Inference
↓
Policy Engine
↓
Domain Routing
↓
Hybrid Retrieval
↓
Battery Planning
↓
Battery Coherence Validation
↓
Explanation Generation
↓
Final Recommendation Response

---

# Core Architectural Components

## 1. Conversation Intelligence Layer
Responsible for:
- extracting hiring signals,
- identifying technical skills,
- detecting leadership requirements,
- inferring hiring scale and evaluation intent.

Files:
- `frame_extractor.py`
- `analyzer.py`
- `state_machine.py`

---

## 2. Recommendation Policy Engine
Builds hiring-aware recommendation policies.

Examples:
- when to prioritize cognitive assessments,
- when to include personality evaluations,
- when to favor scalable screening.

Files:
- `policy_engine.py`
- `policy.py`
- `hiring_intent_inferencer.py`

---

## 3. Domain Routing Layer
Routes recommendations based on role/domain context.

Examples:
- frontend engineering,
- backend engineering,
- leadership hiring,
- data science.

Files:
- `domain_router.py`
- `skill_canonicalizer.py`

---

## 4. Hybrid Retrieval Engine
Combines:
- semantic retrieval,
- lexical retrieval,
- reranking logic.

Files:
- `bm25_engine.py`
- `embedding_engine.py`
- `hybrid_ranker.py`

---

## 5. Battery Planning & Coherence
Ensures:
- assessment diversity,
- balanced batteries,
- suppression of redundant recommendations.

Files:
- `battery_planner.py`
- `battery_coherence_service.py`

---

## 6. Consultative Intelligence Layer
Makes the assistant behave more like a hiring consultant.

Supports:
- clarification,
- refinement,
- follow-up recommendation guidance.

Files:
- `consultation_service.py`
- `orchestrator.py`

---

# Debug Trace System

The API supports optional debug traces.

Example:

```json
{
  "debug": true
}