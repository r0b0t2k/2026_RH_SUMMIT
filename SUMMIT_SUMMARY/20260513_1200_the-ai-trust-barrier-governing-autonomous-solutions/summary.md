# The AI Trust Barrier: Why and How Enterprises Must Govern Autonomous Solutions for Adoption

- Date/Time (EDT): 2026-05-13, 12:00 PM
- Session Type: Session
- Source Folder: otter_summaries/2026_13/AI_Trust_barrier_how_enterprises_must_govern_autonomous_solutions
- Disclaimer: This summary is an estimation based on the slide deck and note file because the attendee did not physically attend this session and no transcript was available.

## Overview
This talk frames enterprise AI adoption as a trust and governance problem rather than a model-access problem. The presenters argue that agentic AI increases autonomy faster than governance programs can keep up, creating a gap between what organizations want to deploy and what security, risk, and compliance teams are willing to approve.

The central design principle is clean and memorable: separate AI intelligence from AI execution. In the session's architecture, Cisco AI Defense secures the intelligence layer across model discovery, supply-chain risk, validation, and runtime protection, while Red Hat Ansible Automation Platform governs execution through approved playbooks, RBAC, approval gates, credential management, and auditable automation.

## Key Themes
- Agentic AI expands risk across prompts, models, agents, data, tools, and supply chain components.
- Governance fails when intelligence and execution are treated as one undifferentiated system.
- AI defense and automation governance should operate as complementary layers.
- The automation library becomes the approved menu of actions that AI is allowed to take.
- MCP integration needs policy boundaries so agents can reach only authorized automation assets.

## Chronological Notes
### The Trust Gap
- The talk opens by contrasting fast AI capability growth with slower governance maturity.
- It cites a familiar mismatch: many organizations plan to deploy agentic AI, but far fewer feel ready to do so securely.
- The security consequences listed are concrete: financial damage, litigation, reputational harm, noncompliance, IP leakage, and supply-chain compromise.

### Separate Intelligence from Execution
- The presentation's core governance principle is to isolate the reasoning layer from the action layer.
- AI can recommend or decide what should happen, but automation must still control how actions are executed.
- That separation is presented as the basis for building trust in autonomous workflows.

### Cisco AI Defense Layer
- Cisco AI Defense is described across the AI lifecycle: discovery, supply-chain risk management, model and application validation, and runtime protection.
- The intent is to inventory assets, scan repositories and MCP servers, red-team models, and block harmful behavior in production.
- The framework is mapped to established security standards such as OWASP, MITRE ATLAS, and NIST.

### Ansible as the Trusted Execution Layer
- Red Hat Ansible Automation Platform is presented as the governed execution layer for IT operations.
- Existing controls such as RBAC, approval gates, auditing, content signing, and credential management become the boundary that constrains AI-driven action.
- The talk makes a strong point that an automation library is not just a convenience; it is the security boundary and audit trail.

### Converged AI Operations
- The later slides connect the two sides through MCP plugins, AIOps automation, and workflow tooling that can orchestrate AI-driven, task-driven, and event-driven automation together.
- The goal is not blind autonomy but confident, governed deployment where every action is deterministic, repeatable, and reviewable.

## Technologies and Projects Mentioned
| Name | Type | Notes |
|---|---|---|
| Cisco AI Defense | AI security platform | Covers discovery, validation, supply-chain scanning, and runtime protection |
| Red Hat Ansible Automation Platform | Automation platform | Governs execution with RBAC, approvals, and auditability |
| MCP | Integration protocol | Used to connect AI systems to approved automation capabilities |
| OWASP / MITRE ATLAS / NIST | Security frameworks | Referenced as mappings for the AI security framework |

## Notable Takeaways
1. The session's strongest idea is that trust comes from separating recommendation from execution.
2. AI governance gets much easier when autonomous actions are constrained to approved automation assets.
3. Existing automation controls such as RBAC and approval gates become more valuable in the age of agents, not less.
4. Enterprises do not need to choose between AI and governance if they layer them deliberately.