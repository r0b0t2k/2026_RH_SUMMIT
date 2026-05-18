# Code, Environment, Data: The Holy Trinity of Reproducible Models

- Date/Time (EDT): 2026-05-11, 2:20 PM - 2:40 PM
- Session Type: Community Day Session
- Source Folder: otter_summaries/2026_11/lakefs

## Overview
This talk focuses on a reproducibility gap in enterprise ML systems: code and environment are often well tracked, but dataset state and lineage are not. The presenter argues that many compliance and debugging failures occur because teams cannot reconstruct the exact data state used to produce a model.

LakeFS is presented as a metadata layer that brings Git-like semantics to object-store data, enabling branch, commit, diff, merge, and tag patterns for datasets without deep-copying full objects. The practical objective is to make data state as auditable and reproducible as code state.

## Key Themes
- Reproducibility requires version control across code, environment, and data.
- Object stores optimize for scale/durability, not reproducible lineage by default.
- Git-like workflows for data reduce copy sprawl and improve auditability.
- Immutable dataset references improve post-hoc model investigations.
- Compliance in regulated industries depends on exact training-data reconstruction.

## Chronological Notes
### Problem Framing
- Speaker contrasts mature code/env versioning with weaker data-state tracking.
- Common failure mode: teams can reproduce pipeline code but not exact data used.

### LakeFS Approach
- LakeFS is introduced as a metadata layer over object storage.
- Zero-copy branching is highlighted for safe experimentation and lower storage overhead.

### Demonstration Pattern
- Baseline workflow logs experiment metadata but lacks immutable data snapshot linkage.
- Second workflow adds commits/tags for each data transformation stage.
- Result: experiment tracking can link to specific, navigable dataset state.

### Enterprise Implications
- Reduced data duplication across teams and experiments.
- Improved incident response/compliance posture through lineage visibility.
- Positioned as complementary to broader cloud and data-platform ecosystems.

## Technologies and Projects Mentioned
| Name | Type | Notes |
|---|---|---|
| LakeFS | Data versioning layer | Git-like operations for object-store datasets |
| MLflow | Experiment tracking | Used to show environment/code tracking vs data gap |
| MinIO | S3-compatible object store | Demo storage backend |
| DVC | Data versioning project | Mentioned in competitive/adjacent context |

## Notable Takeaways
1. Reproducibility failures are often data-lineage failures, not only code issues.
2. Tagging dataset state before training creates a durable audit anchor.
3. Zero-copy branching enables safer experimentation with lower storage cost.
4. Regulated environments benefit from explicit, immutable data provenance links.
