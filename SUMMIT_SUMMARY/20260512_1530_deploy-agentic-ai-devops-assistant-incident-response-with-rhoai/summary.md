# Deploy an Agentic AI DevOps Assistant: Augmenting Incident Response with Red Hat OpenShift AI

- Date/Time (EDT): 2026-05-12, 3:30 PM - 5:00 PM
- Session Type: Lab
- Source Folder: otter_summaries/2026_12/Deploy_agentic_AiDevOps_assistant_augmenting_incident_response_with_RHOAI

## Overview
This lab is a hands-on walkthrough of an agentic incident-response assistant built for real operations teams rather than a generic chatbot demo. The scenario centers on failed automation jobs, ticket creation, chat notifications, model-backed triage, and audit-ready incident handling. The user's note that they completed the lab in person matches the source material: the emphasis is on interactive workflows and operational tradeoffs, not just a presentation deck.

The key design idea is that the assistant augments SRE workflows by gathering context, classifying failures, invoking targeted subagents, and producing structured incident output while preserving human control where it matters. The supporting showroom documentation expands that story into a full Meridian Financial scenario with compliance pressure, Ansible Automation Platform, Rocket.Chat, ticketing, model selection, and human-in/on/out-of-the-loop patterns.

## Key Themes
- Agentic operations need strong context engineering, not just a capable model.
- Failed automation jobs are a practical trigger point for AI-assisted incident workflows.
- Human oversight remains part of the operating model for higher-risk actions.
- Audit trails and compliance evidence are core requirements, not secondary features.
- OpenShift AI model choice and operational integration matter as much as the agent logic itself.

## Chronological Notes
### Setting the Stage
- The presenters begin by grounding the session in real ops scale, with discussion around the number of VMs and daily changes teams manage.
- They explicitly acknowledge skepticism toward vendor-pitched AI agents and frame the lab as an open, inspectable alternative.

### Lab Architecture
- The failure signal originates in Ansible Automation Platform, where a job failure triggers the agent workflow.
- A primary ops agent retrieves artifacts such as logs, templates, and job details, then dynamically creates specialized SRE subagents.
- The workflow updates a ticketing system called Kira and sends notifications through Rocket.Chat to simulate a ChatOps loop.

### Context Engineering and Skills
- One of the strongest practical points in the lab is that good results depend on providing the agent tight, relevant context.
- Skills are used to encode both general operational knowledge and organization-specific tribal knowledge.
- That makes the assistant more useful than a generic prompt against a generic model.

### Human Oversight and Compliance
- The lab documentation emphasizes human-in, human-on, and human-out-of-the-loop patterns depending on the risk of the action.
- Audit-ready incident reports are treated as a deliverable in their own right, especially for regulated environments.
- The target outcome is faster and more consistent response without pretending that all judgment should be fully automated.

### Business Outcome Framing
- The supporting material frames the operational goal as reducing MTTR for common failure patterns, scaling ticket handling volume, and capturing reusable knowledge.
- The final message is augmentation: the agent handles mechanical triage and investigation so humans can focus on higher-value decisions.

## Technologies and Projects Mentioned
| Name | Type | Notes |
|---|---|---|
| Ansible Automation Platform | Automation platform | Source of failure events and remediation workflows |
| OpenShift AI MaaS | Model access layer | Used to swap models and balance cost, capability, and compliance |
| Kira | Ticketing interface | Used in the lab to capture structured incidents |
| Rocket.Chat | ChatOps interface | Used for notifications and operational feedback loops |
| LangChain Deep Agents | Agent framework | Referenced in the showroom lab design |
| Gitea | Source control | Hosts playbooks and artifacts used during investigation |

## Notable Takeaways
1. The most credible AIOps assistant starts from existing operational systems and failure signals.
2. Context engineering and skills are what turn an LLM into something useful for SRE work.
3. Compliance-ready audit output is a first-class requirement for enterprise incident-response agents.
4. The lab's strongest claim is not autonomy for its own sake, but faster, more disciplined incident handling with humans still in control.