# Evaluation-Driven Development: AI Applications That Don't Lie

**Session**: LT3001 (DevZone)  
**Date/Time**: May 12, 2026, 11:15 AM – 11:35 AM EDT  
**Presenter**: William Caban, Sr Principal Product Manager, Red Hat AI  
**Format**: Live-coding demonstration with visual slides (37 images)

---

## Executive Summary

This session introduces **Evaluation-Driven Development (EDD)**, a methodology addressing the critical gap between traditional test-driven development (TDD) and the reality of AI/LLM systems. Traditional QA assumes deterministic outputs and binary pass/fail testing—assumptions that fundamentally break with language models. EDD replaces this with continuous measurement against quality thresholds throughout development and production. The session demonstrates this with live examples using EvalHub, an open-source unified evaluation platform that catches hallucinations, retrieval gaps, and consistency issues before users discover them.

---

## Problem Statement: Why Traditional Testing Fails with AI

### The Core Challenge
- **60-80% of AI projects never reach production** due to undetected quality failures
- **AI projects fail silently**—tests pass while real-world performance breaks down
- Classic scenario: Internal testing passes, pilot runs smoothly, CI is green—then three weeks into production, users discover wrong eligibility dates or hallucinated information

### Three Broken Assumptions of Traditional QA

| Assumption | Traditional QA Reality | AI Reality |
|---|---|---|
| **Output Determinism** | Same input → same output always | Same input → different output every call (non-determinism) |
| **Test Validation** | Binary pass/fail (it works or doesn't) | Spectrum quality: answers range 0–1; "pass" is a threshold of "good enough" |
| **Test Data** | Static fixtures with hand-written mock data | Dynamic knowledge: models don't know what they don't know; ground truth must be generated at scale |

---

## The Evaluation-Driven Development Methodology

### The EDD Cycle: Define → Measure → Iterate
1. **Define** thresholds for quality metrics (e.g., accuracy ≥ 0.80, consistency ≥ 0.50, hallucination rate ≤ 0.10)
2. **Measure** every change against baseline scores before production deployment
3. **Iterate** optimizations based on scoring results; catch regressions before users do

### Key Principle
> "Every change gets evaluated before it reaches production. Catches regressions before users do."

---

## EvalHub: The Unified Evaluation Toolkit

EvalHub is a framework-agnostic, production-scale evaluation orchestration platform with these core capabilities:

| Capability | Details |
|---|---|
| **Framework Agnostic** | Unified orchestration of LM Evaluation Harness, LightEval, Garak, CLEAR, GuideLLM, and custom evaluators (bring-your-own-framework/BYOF) |
| **Simultaneous Assessment** | Runs capability benchmarks AND security/safety probes in the same evaluation run |
| **Bottleneck Identification** | Pinpoints exactly where the pipeline breaks: model, context, retrieval, or prompts |
| **Full Context Tracking** | Captures hardware, software, and configuration for every run via MLflow integration |
| **EDD-Native Design** | Built specifically for the Define → Measure → Iterate workflow |
| **Production Scalability** | Runs on local laptop or OpenShift/Kubernetes at enterprise scale |

### EvalHub Architecture
- **EvalHub SDK**: Client library for application integration
- **EvalHub Server**: Job scheduler, scorer runner, result store
- **MLflow**: Centralized results and history repository
- **Kubernetes/vLLM/RHOAI**: Production model endpoints and compute
- **Your AI Application**: RAG pipeline, chatbot, summarizer, etc.

---

## Three Core Evaluation Scorers

### 1. Domain F1 (Factual Accuracy)
- **Measures**: Do answers match ground-truth facts word-for-word?
- **Scoring**: 0–1 (1.0 = perfect match, 0.0 = no overlap)
- **Threshold**: ≥ 0.80
- **Catches**: Wrong dates, missing information
- **Use Case**: Start here; add domain-specific scorers as you discover issues

### 2. Consistency (Jaccard Similarity)
- **Measures**: Do consecutive answers agree? (same question, 5 runs)
- **Scoring**: 0–1 (1.0 = identical every run, 0.0 = no words in common)
- **Threshold**: ≥ 0.50
- **Catches**: Non-deterministic behavior in LLM outputs

### 3. Confabulation Detection
- **Measures**: Does the answer invent facts not in the source?
- **Scoring**: Fraction of answers with NO hallucinated facts (0–1 scale)
- **Threshold**: ≥ 0.90
- **Catches**: Hallucinated dates, numbers, and fabricated information

---

## Live Demo: The Four Acts

### Act 1: The TDD Illusion
A RAG pipeline for HR benefits eligibility passes all traditional tests (returns a string, not empty, not copy of input). CI is green. Yet for the same question asked 5 times:
- Call 1: Correct answer
- Call 2: Hallucination (wrong enrollment window)
- Call 3: Hallucination (wrong closing date)

**Result**: Traditional tests never asked if answers were *right*.

### Act 2: The Reveal (EDD Evaluation)
Running the three scorers on the same pipeline:
- **Consistency Jaccard**: ~0.31 (threshold ≥ 0.50) → **CONCERN** (answers vary too much)
- **Domain F1**: ~0.42 (threshold ≥ 0.80) → **FAIL** (wrong dates, missing facts)
- **Confabulation pass rate**: ~0.60 (threshold ≥ 0.90) → **FAIL** (2 of 5 answers contain hallucinated dates)

**Overall**: FAILING—pipeline should NOT be deployed.

### Act 3: EDD Collection at Development Scale
Using EvalHub to run a collection (3 benchmarks defined once):
```
✓ Provider registered: hr-rag-byop
✓ Collection created: hr-rag-eval-v1 (3 benchmarks)
✓ Job submitted: id=702e5172...
BLOCKED – hr-consistency 0.32 < 0.50
          hr-domain-f1 0.62 < 0.80
          hr-confabulation 0.60 < 0.90
```

**Result**: Deploy BLOCKED at all three thresholds.

### Act 4: Production Scale on OpenShift
Same collection, same thresholds, 1,000 samples instead of manual test set:
```
hr-consistency    0.32 FAIL ✗  (1,000 samples)
hr-domain-f1      0.62 FAIL ✗  (1,000 samples)
hr-confabulation  0.71 FAIL ✗  (1,000 samples)
BLOCKED at production gate.
```

**Result**: Scale changes. The verdict doesn't. Same evaluation framework applies from laptop to Kubernetes.

---

## Key Takeaways

### 1. The AI Gap is Structural
Traditional QA is necessary but not sufficient for AI. The gap cannot be fixed with more test cases—it requires a different testing paradigm entirely.

### 2. EDD Provides Measurable Quality
Evaluation-Driven Development gives teams a methodology for measuring what actually matters in AI systems:
- Faithfulness (answers match ground truth)
- Relevance (answers address the question)
- Groundedness (no hallucinated facts)

### 3. Collections = Portable Quality Gates
- Define benchmark suite once
- Every CI/CD run references it by ID
- Thresholds and gate policies travel with the collection, not guessed per deployment
- **BYOP + Collections pattern**: Bring your scorer, register once, EvalHub runs it everywhere

### 4. Production Scale Doesn't Break the Model
The same evaluation framework scales from development laptops to OpenShift at 1,000+ samples without changing thresholds or losing consistency.

---

## Getting Started

### Prerequisites
- Python 3.12+
- `uv` (fast Python package manager)
- `podman` (container runtime)

### Resources
- **Demo Repository**: `https://github.com/williamcaban/edd-demo`
- **Setup Guide**: `https://red.ht/edd-evalhub`
- **Quick Start**:
  ```bash
  git clone https://github.com/williamcaban/edd-demo
  cd edd-demo
  uv sync
  podman play kube pod.yaml
  ```

---

## Technical Stack

| Component | Purpose | Integration |
|---|---|---|
| **EvalHub SDK** | Client library for pipeline integration | Integrated into RAG/LLM application code |
| **EvalHub Server** | Centralized evaluation orchestration | Runs as container or Kubernetes pod |
| **Scorer Frameworks** | Diverse evaluation backends (LightEval, Garak, CLEAR, GuideLLM) | Framework-agnostic BYOF pattern |
| **MLflow** | Experiment tracking & results history | Stores evaluation runs with full metadata |
| **OpenShift/Kubernetes** | Production compute | Scales evaluation jobs horizontally |
| **vLLM/RHOAI** | Model endpoints | Serves LLM inference during evals |

---

## Design Philosophy

> "EvalHub, because 'Looks good to me' isn't a benchmark."

The presentation challenges the false confidence that traditional QA and green CI builds provide. EDD shifts from asking "Did our tests pass?" to "Does our AI work correctly *in reality*?" at every stage from local development through production.

---

## Visual Assets
37 slides extracted from presenter deck, including:
- Problem scenario illustrations
- Comparison tables (traditional vs. AI testing)
- EDD cycle diagram
- EvalHub architecture diagrams
- Live demonstration code outputs
- Scorer metrics visualizations
- Key takeaway summary slides

See `img_manifest.csv` for detailed slide-by-slide breakdown.

---

**Next Steps**: Consider adopting EDD methodology in your RAG pipeline or LLM application. Start with the demo repo and the three core scorers (Domain F1, Consistency, Confabulation) to catch quality issues before production deployment.
