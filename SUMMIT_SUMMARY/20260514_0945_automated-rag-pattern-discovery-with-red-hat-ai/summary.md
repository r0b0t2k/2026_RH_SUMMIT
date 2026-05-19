# Stop Guessing, Start Shipping: Automated RAG Pattern Discovery with Red Hat AI

- Date/Time (EDT): 2026-05-14, 9:45 AM - 10:25 AM
- Session Type: Session
- Source Folder: otter_summaries/2026_14/autorag_automl
- Context Note: This summary reflects the talk the attendee actually chose at this time slot, which was the AutoRAG session rather than the originally scheduled MCP talk associated with this source folder.

## Overview
This session focuses on one of the most frustrating realities of enterprise RAG systems: too many configuration choices and too much human trial-and-error. The speaker positions AutoRAG and AutoML in Red Hat OpenShift AI 3.4 as a way to turn RAG design from a manual craft exercise into a guided optimization workflow.

Instead of hand-tuning chunking strategies, embedding models, vector stores, and retrieval settings in an ad hoc way, the platform can explore a search space automatically and rank the resulting patterns using explicit evaluation metrics such as answer correctness and faithfulness. The framing is practical rather than academic: stop vibe-tuning RAG systems and start shipping the patterns that actually score well.

## Key Themes
- RAG design has too many interacting variables for manual tuning to scale well.
- Human-only evaluation becomes a bottleneck long before teams reach a reliable production pattern.
- AutoRAG and AutoML are presented as optimization workflows rather than one-click magic.
- Leaderboards and evaluation metrics make pattern selection more defensible.
- Red Hat OpenShift AI 3.4 is the productization point for these capabilities.

## Chronological Notes
### Why RAG Tuning Becomes Painful
- The talk begins from a common engineering complaint: there are too many choices in modern RAG systems.
- Chunk size, chunking strategy, embedding model, vector database, retrieval settings, and LLM choice all affect quality.
- Without automation, teams end up iterating manually and often choosing patterns based on intuition rather than evidence.

### AutoRAG as Search and Optimization
- AutoRAG is described as an automated optimization run over a structured search space.
- The platform prepares candidate combinations for variables such as chunking, embeddings, vector storage, and model selection.
- This makes RAG tuning look more like an experimental pipeline and less like a series of disconnected prompt tweaks.

### Evaluation as the Ranking Signal
- The talk gives evaluation a central role rather than treating it as an afterthought.
- Metrics such as answer correctness and faithfulness are used to rank the patterns tried during an optimization run.
- The output is a ranked leaderboard, which is a far more useful artifact for a platform team than a single anecdotal demo result.

### AutoML and Product Direction
- AutoML is discussed alongside AutoRAG as part of the broader automation story in OpenShift AI 3.4.
- The talk positions these capabilities as a way to scale expert knowledge rather than requiring every team to become a retrieval specialist.
- An AutoEval roadmap is also referenced, reinforcing that evaluation itself is becoming more automated and productized.

### Practical Outcome
- The strongest operational message is that teams should optimize RAG systems through reproducible experiments and explicit metrics.
- That is a better enterprise posture than shipping whichever pattern happened to feel best during manual testing.

## Technologies and Projects Mentioned
| Name | Type | Notes |
|---|---|---|
| AutoRAG | Optimization workflow | Automates RAG pattern discovery across a configurable search space |
| AutoML | Optimization workflow | Presented alongside AutoRAG as part of OpenShift AI automation |
| Red Hat OpenShift AI 3.4 | Platform release | Product release that introduces these capabilities |
| Vector databases | Retrieval infrastructure | One of the tunable dimensions explored by AutoRAG |
| Answer Correctness / Faithfulness | Evaluation metrics | Used to rank candidate RAG patterns |

## Notable Takeaways
1. Manual RAG tuning does not scale once the search space gets large.
2. Leaderboards and explicit metrics make retrieval-system decisions easier to defend.
3. AutoRAG is valuable because it systematizes experimentation, not because it removes engineering judgment entirely.
4. The talk treats evaluation as part of the product, which is the right direction for enterprise RAG.