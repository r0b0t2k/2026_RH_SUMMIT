# Agent Skills with Quarkus and the LangChain4j Skills Module

- Date/Time (EDT): 2026-05-13, 1:30 PM - 1:50 PM
- Session Type: Session
- Source Folder: otter_summaries/2026_13/agent_skills_with_quarkus_and_langchain4j_module

## Overview
This talk uses the newly emerging skills pattern to address a very practical LLM problem: context overload. Instead of trying to fix unreliable outputs by endlessly expanding prompts, the speaker argues for packaging reusable, domain-specific instructions as skills that can be discovered, activated, and executed only when relevant.

Quarkus and LangChain4j are then presented as a Java-native implementation path for that idea. The result is a development pattern where teams can manage reusable AI workflows in version control, expose them through a predictable specification, and combine them with tool guardrails so that portability does not come at the cost of security.

## Key Themes
- Bigger prompts are often a poor answer to weak AI results because they can worsen context compression.
- Skills provide a reusable, shareable unit of AI workflow and instruction design.
- The skills specification is intentionally small and portable.
- Progressive disclosure helps agents keep the main context window lean until a skill is needed.
- Tool access needs guardrails because portable skills can become a data-exfiltration risk.

## Chronological Notes
### Problem: Context Overflow
- The talk opens by naming a common failure pattern: when results are weak, users keep adding more detail until the prompt itself becomes part of the problem.
- The speaker argues that context overflow causes detail loss, unreliable results, and sloppy outputs.

### What Skills Are
- Skills are introduced as reusable directories centered on a `SKILL.md` file with YAML frontmatter and concise markdown instructions.
- Their benefits are framed in practical team terms: reusability, consistency, specialization, portability, and collaboration through version control.
- Supporting files such as checklists, templates, or reference documents can be bundled alongside the main skill prompt.

### Progressive Disclosure
- A key concept in the talk is progressive disclosure.
- At startup, the agent loads only the skill names and descriptions into the model context.
- When a task matches, the full skill and any related files are then loaded, which preserves context budget until the skill is actually needed.

### Quarkus and LangChain4j Implementation
- The Java implementation path is direct: add the `quarkus-langchain4j-skills` dependency, configure the skills directory, and wire the assistant to a system-message provider.
- The talk positions Quarkus as a practical enterprise runtime for skills because it pairs AI orchestration with familiar Java tooling.

### Security and Usage Notes
- The later slides are intentionally cautious.
- Skills are described as powerful but potentially risky because their real-world effect depends on the tools they can call.
- The recommendation is to expose only the minimum necessary tools and to apply strict input and output validation through tool guardrails.

## Technologies and Projects Mentioned
| Name | Type | Notes |
|---|---|---|
| Agent Skills specification | Open format | Defines portable skill directories with metadata and instructions |
| Quarkus | Java framework | Used as the enterprise runtime for skill-enabled assistants |
| LangChain4j | Java AI framework | Provides the underlying assistant and tooling integration |
| quarkus-langchain4j-skills | Quarkus extension | Adds skills support to LangChain4j on Quarkus |
| Tool Guardrails | Control pattern | Used to validate and constrain tool use |

## Notable Takeaways
1. Skills are a better scaling unit than ever-expanding prompts when teams want reuse and consistency.
2. Progressive disclosure is the practical mechanism that keeps skills from bloating the main context window.
3. The Quarkus and LangChain4j implementation makes the skills pattern approachable for Java teams.
4. Portable skills are only safe when their tool access is tightly constrained.