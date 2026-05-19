# Experimenting with vLLM on Kubernetes Using MicroShift, Podman Desktop, and KServe

- Date/Time (EDT): 2026-05-12, 10:30 AM - 10:50 AM
- Session Type: Session
- Source Folder: otter_summaries/2026_12/experiment_vLLM_kube_microshift_podman

## Overview
This talk shows how to build a realistic local inference stack for LLM experimentation without jumping straight to a GPU-heavy cluster. The presenter positions MicroShift, Podman Desktop, KServe, and vLLM as a practical bridge between laptop prototyping and production-grade Red Hat OpenShift AI deployments.

The emphasis is not on claiming that a laptop CPU suddenly becomes a production inference platform. Instead, the point is to create a compatible stack where developers can validate APIs, deployment patterns, model serving behavior, and integration logic locally before scaling up to larger infrastructure.

## Key Themes
- Local AI experimentation should mirror production APIs and control planes as closely as possible.
- vLLM matters because its memory management and batching strategies improve inference efficiency under concurrent load.
- KServe provides a stable serving abstraction so teams can swap models without rewriting their applications.
- MicroShift and Podman Desktop create a lightweight OpenShift-like environment for early testing.
- Red Hat OpenShift AI is the intended production landing zone once the pattern works locally.

## Chronological Notes
### Problem Framing
- The presenter starts from a familiar pain point: running LLMs locally often overwhelms laptop resources and makes it hard to test AI applications before production.
- Typical issues include RAM pressure, long model load times, and weak concurrency on small machines.

### Why vLLM
- vLLM is presented as the core inference engine because of PagedAttention, which improves KV-cache utilization and reduces wasted memory.
- Continuous batching is highlighted as the mechanism that helps process requests as they arrive rather than serializing them inefficiently.
- The broader message is that inference optimization matters as much as model quality when teams want usable latency and throughput.

### Why KServe and the Local Stack
- KServe is positioned as the serving layer that standardizes inference APIs and deployment patterns.
- MicroShift provides the lightweight Kubernetes/OpenShift substrate, while Podman Desktop makes that environment approachable on a developer machine.
- The talk frames this combination as a safe way to test integrations, manifests, and inference services before moving to a full cluster.

### Demo and Benchmark Discussion
- The demo walks through installing the KServe stack, configuring an `InferenceService`, wiring the components together, and running live inference.
- The benchmark discussion is nuanced: smaller CPU-oriented tools can sometimes do better on a laptop, but vLLM shows its value as workloads become more parallel and production-like.
- The presenter also points ahead to tensor parallelism, distributed serving, and speculative decoding features that matter more in larger environments.

### Enterprise Context
- The closing argument is that a local stack is useful when it preserves the same operational ideas teams will use later in OpenShift AI.
- Teams can validate the serving pattern locally, then scale up to GPU-backed, distributed inference with fewer surprises.

## Technologies and Projects Mentioned
| Name | Type | Notes |
|---|---|---|
| vLLM | Inference engine | Uses PagedAttention and continuous batching for efficient serving |
| KServe | Serving platform | Standardizes model serving with `InferenceService` resources |
| MicroShift | Lightweight Kubernetes/OpenShift | Provides a laptop-friendly local cluster footprint |
| Podman Desktop | Local container tooling | Used to stand up and manage the local environment |
| Red Hat OpenShift AI | Enterprise AI platform | Framed as the production target for the pattern |
| Ollama | Local inference tool | Used as a comparison point in benchmark discussion |

## Notable Takeaways
1. The real value of the stack is compatibility with production patterns, not raw laptop speed.
2. vLLM's memory and batching optimizations become more meaningful as concurrency rises.
3. KServe reduces friction when swapping models or moving from local to cluster deployments.
4. Local validation on a production-shaped platform lowers the risk of later OpenShift AI rollouts.