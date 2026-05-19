# Mitigating AI's New Risk Frontier: Security and Safety

- Date/Time (EDT): 2026-05-11, 2:40 PM - 3:00 PM
- Session Type: Community Day Session
- Source Folder: otter_summaries/2026_11/mitigating_AI_new_risk_frontier

## Overview
This session separates two frequently conflated domains: AI security and AI safety. Speakers position AI security in the traditional confidentiality-integrity-availability framework, while treating AI safety as behavior alignment, harmful output reduction, and trustworthiness management. The central recommendation is to integrate both domains into existing enterprise security governance rather than launching separate, isolated AI-specific teams.

The talk emphasizes that safety issues often differ from software vulnerabilities because they may be probabilistic and not deterministically "fixed" with a single patch. As a result, continuous evaluation, guardrails, and platform-level controls are framed as essential to reducing risk in production.

## Key Themes
- AI security and AI safety are related but operationally distinct.
- Security controls should remain embedded in existing enterprise security structures.
- Safety requires continuous measurement and runtime controls, not one-time remediation.
- Platform architecture is critical: controls span far beyond the model layer.
- Supply-chain visibility for models (AI BOMs/agent BOMs) is becoming necessary.

## Chronological Notes
### Security vs Safety Definitions
- Security: protecting confidentiality, integrity, availability and preventing exploit paths.
- Safety: reducing harmful, biased, or non-compliant model behavior and maintaining trust.

### Why It Matters in Production
- Session references recent incidents (prompt injection, data exposure, model supply-chain compromise).
- Agentic systems are described as increasing blast radius when controls are weak.

### Safety Lifecycle and Guardrails
- The speakers stress continuous evaluation across training, tuning, and runtime drift.
- Guardrails are presented as runtime control points for both input and output safety.

### Model Supply-Chain and Governance
- Discussion includes model provenance, adaptation lineage, and enterprise traceability.
- AI BOM / agent BOM concepts are positioned as emerging governance artifacts.

### Enterprise Control Surface
- Architecture-level controls include identity, authorization, network isolation, workload boundaries, and policy management.
- Recommendation: unify AI risk with existing governance/compliance/security programs.

## Technologies and Frameworks Mentioned
| Name | Type | Notes |
|---|---|---|
| TrustyAI | AI safety/control tooling | Referenced for evaluation and guardrail workflows |
| OWASP Top 10 for LLMs/Agents | Risk framework | Cited as practical threat-model guidance |
| MITRE ATLAS | Threat framework | Mentioned for AI threat mapping |
| NIST AI RMF (referenced contextually) | Risk management framework | Discussed in governance/risk mapping context |
| AI BOM / Agent BOM | Governance artifact | Proposed for model/component provenance and traceability |

## Notable Takeaways
1. AI risk programs need both classic security engineering and safety engineering disciplines.
2. Safety management is iterative and measurement-driven rather than purely patch-driven.
3. Model and agent supply-chain provenance is emerging as a core enterprise requirement.
4. Platform-level controls are as important as model-level safeguards.
