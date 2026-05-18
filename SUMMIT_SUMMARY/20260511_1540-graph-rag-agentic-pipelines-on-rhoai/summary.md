# GraphRAG and Agentic Pipelines on RHOAI

- Date/Time (EDT): 2026-05-11, 3:40 PM - 4:00 PM
- Session Type: Community Day Session
- Source Folder: otter_summaries/2026_11/graphRAG_agentic_pipelines_on_RHOAI

## Overview
This session argues that traditional flat-vector RAG is often insufficient for enterprise reasoning tasks that depend on relationships across systems, ownership, policy, and operational dependencies. The speaker proposes GraphRAG as a better retrieval strategy for complex enterprise data, especially when paired with multi-agent orchestration.

A core distinction is introduced between static knowledge graphs and richer context graphs. In this framing, GraphRAG is the retrieval method, while the context graph is the governed substrate that enables traceable, policy-aware decision support for agentic workflows.

## Key Themes
- Enterprise data fragmentation breaks simple top-k chunk retrieval assumptions.
- Graph structures preserve relationship context required for multi-hop reasoning.
- Agentic workflows gain reliability when backed by structured context retrieval.
- Context engineering becomes a control plane for agent behavior.
- RHOAI/OpenShift-native deployment supports scalable, governable operations.

## Chronological Notes
### Problem Statement
- Enterprise knowledge is distributed across databases, tickets, docs, APIs, and operational systems.
- Flat chunk retrieval loses dependency and ownership relationships needed for impact analysis.

### GraphRAG Foundations
- Entities become nodes; typed relations become edges; properties carry timestamps/metadata/confidence.
- Retrieval shifts from nearest-neighbor chunks to graph traversal plus semantic matching.

### Pipeline Design
- Stages presented: extract entities/relations, build graph store, traverse relevant subgraphs, assemble context, generate with LLM.
- Hybrid retrieval can combine graph traversal with vector-based relevance.

### Agentic Orchestration Layer
- Multi-agent roles (planner/retriever/reasoner/executor) are described over graph context.
- The demo highlights human-in-the-loop controls before potentially disruptive actions.

### Context Graph Framing
- Speaker differentiates static knowledge graphs from context graphs with stronger governance semantics.
- Emphasis is placed on "context engineering" as a practical discipline for enterprise agent control.

## Technologies and Projects Mentioned
| Name | Type | Notes |
|---|---|---|
| GraphRAG | Retrieval strategy | Relationship-aware retrieval over graph structures |
| Neo4j | Graph database | Mentioned as graph persistence/query option |
| PostgreSQL + Apache AGE | Graph-on-relational option | Alternative graph storage/query approach |
| OpenShift AI (RHOAI) | Deployment platform | Runtime context for scalable, policy-governed serving |
| vLLM / Llama Stack / OPA | Serving + governance components | Mentioned in architecture as inference and policy layers |

## Notable Takeaways
1. Multi-hop dependency questions are a weak fit for flat vector-only retrieval.
2. Context-rich graph retrieval improves enterprise reasoning quality and operational relevance.
3. Agentic systems require explicit governance substrate, not only model capability.
4. Human-in-the-loop checkpoints remain important for high-impact operational actions.
