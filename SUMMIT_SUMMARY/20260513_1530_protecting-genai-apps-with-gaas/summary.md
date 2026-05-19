# Protecting GenAI Apps with GAAS

- Date/Time (EDT): 2026-05-13, 3:30 PM - 5:00 PM
- Session Type: Lab
- Source Folder: otter_summaries/2026_13/protecting_genai_apps_with_GAAS

## Overview
This lab turns AI safety into something concrete and visible. Instead of discussing guardrails abstractly, participants work through a themed chatbot example and see how a loosely constrained assistant behaves before and after TrustyAI guardrails are added. The user's note captures the hands-on purpose well: the lab focused on constraining a peach-themed customer-service bot so it would stay on topic and behave within explicit boundaries.

The extracted introduction and the supporting `lemonade-stand-assistant` repository show the architecture behind that experience. The system treats both the user and the LLM as untrusted, validates inputs and outputs, and uses multiple detector models plus simple regex rules to enforce business, safety, and brand constraints around the assistant.

## Key Themes
- Guardrails are easier to understand when users can compare behavior before and after enforcement.
- A zero-trust mindset applies to both user input and model output.
- Real safety controls combine model-based detectors with simpler deterministic rules.
- Guardrails are not only about abuse prevention; they also control cost, topic drift, and brand risk.
- The lab makes TrustyAI guardrails feel operational rather than theoretical.

## Chronological Notes
### Why Guardrails Matter
- The introduction opens with examples of public chatbot failures and explains that these incidents are still common.
- The speakers connect those failures to off-topic cost, malicious misuse, and reputational damage.
- That framing makes guardrails an operational requirement rather than a niche compliance feature.

### Zero-Trust Design
- The lab explicitly adopts a zero-trust policy.
- User input is validated before reaching the model, and model output is validated before it reaches the user.
- The speakers emphasize that an LLM is not inherently trustworthy just because it is helpful.

### Guardrail Components
- The walkthrough includes an orchestrator plus multiple detectors: hate and abusive content detection, prompt-injection detection, language validation, and simpler text rules.
- The supporting repository adds more detail: the reference implementation uses a main LLM, Granite Guardian HAP for safety screening, a DeBERTa-based prompt injection detector, a language detector, and regex-based filters.
- The result is a layered control stack rather than a single classifier.

### The Lab Scenario
- Participants are tasked with locking the assistant to its intended domain and protecting what the presenters jokingly call the triple B: the brand, the budget, and the bot.
- The exercise is effective because users can observe the behavioral difference once guardrails are turned on.
- That makes the abstract idea of safe prompting much more concrete.

### Productization Angle
- The repo behind the lab shows how this pattern can be deployed on OpenShift AI with detector services, dashboards, and configurable model back ends.
- That expands the lesson from a summit lab into a reusable architecture for enterprise GenAI apps.

## Technologies and Projects Mentioned
| Name | Type | Notes |
|---|---|---|
| TrustyAI | Guardrails and safety project | Provides the broader guardrails context for the lab |
| lemonade-stand-assistant | Reference application | Demonstrates guardrails around a customer-service chatbot |
| Granite Guardian HAP | Safety detector | Screens for hate, abuse, and profanity |
| DeBERTa prompt injection detector | Security detector | Flags prompt injection attempts |
| Lingua | Language detector | Enforces language constraints |
| Llama 3.2 3B Instruct | Main LLM | Default model in the reference implementation |

## Notable Takeaways
1. Guardrails are about business control as much as they are about content safety.
2. Treating both users and LLMs as untrusted is a strong mental model for production GenAI apps.
3. Layered controls work better than relying on one safety model to do everything.
4. The lab's strongest value is experiential: participants can see guardrails change behavior rather than only hear about policy.

## Representative Visuals
Representative visuals retained from transcript-style PDFs or source photos:

- ![Representative visual 1](img/PXL_20260513_134633186.jpg)
- ![Representative visual 2](img/PXL_20260513_134703038.jpg)
- ![Representative visual 3](img/PXL_20260513_134745263.jpg)
- ![Representative visual 4](img/PXL_20260513_134745375.jpg)