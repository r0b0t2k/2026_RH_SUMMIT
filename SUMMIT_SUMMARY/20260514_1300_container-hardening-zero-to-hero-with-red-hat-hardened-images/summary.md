# Container Hardening: From Zero to Hero with Red Hat Hardened Images

- Date/Time (EDT): 2026-05-14, 1:00 PM - 2:30 PM
- Session Type: Lab
- Source Folder: otter_summaries/2026_14/container_hardening_from_zero_to_hero_with_redhat_hardend_images

## Overview
This closing lab makes a direct argument for treating container base images as a major part of the software-security problem rather than as a passive dependency. The speakers position Red Hat Hardened Images as a way to reduce vulnerability-management toil by starting from minimal, hardened, verifiable images that are continuously rebuilt and quickly remediated when upstream fixes land.

The talk is especially strong because it does not pretend CVEs can be wished away. Instead, it frames hardened images as a practical response to rising vulnerability volume, compliance pressure, and the engineering time lost to maintenance. The lab then turns that into hands-on work through the hardened image catalog, SBOM inspection, and remediation-oriented workflows.

## Key Themes
- CVE volume and compliance pressure are turning image maintenance into a serious productivity drag.
- Minimal, container-native images reduce attack surface and lower noise.
- Provenance, SBOMs, and reproducible builds matter as much as raw package count.
- Fast upstream-aligned remediation is a core feature, not a side benefit.
- Hardened images should fit existing CI/CD and cloud-native practices rather than forcing a different developer experience.

## Chronological Notes
### The Security Squeeze
- The session opens with the macro problem: vulnerability counts are rising quickly and traditional triage processes struggle to keep pace.
- The resulting pressure shows up as compliance burden and as an innovation tax on engineering teams.

### What Red Hat Hardened Images Are
- Red Hat Hardened Images are described as a foundational set of language, runtime, database, web, and utility images.
- They are built on a minimal hardened Linux userspace optimized for containers.
- The presentation emphasizes that they are available without a separate image price tag when customers already run RHEL or OpenShift.

### Guiding Principles
- The guiding principles are explicit: minimalism, hardened-by-default builds, familiar developer experience, upstream proximity, and verifiability.
- Distroless design, non-root defaults, SBOM delivery, and SLSA 3 provenance are all part of that package.
- The overarching goal is to reduce toil without making developers fight the platform.

### Project Hummingbird and Remediation Flow
- Project Hummingbird is presented as the packaging and build foundation behind the images.
- The slides claim significant reductions in package count and image size, with a near-zero CVE target and typical critical-fix turnaround inside 24 hours.
- The remediation workflow is shown end to end, from vulnerability discovery through analysis, package rebuild, image rebuild, publication, and customer consumption.

### Lab Experience
- The lab itself focuses on practical exploration: finding images in the catalog, checking pull commands, comparing CVE counts and variants, and inspecting SBOM and verification data.
- Later lab content points toward usage practices, update patterns, build automation, and secured pipelines.

## Technologies and Projects Mentioned
| Name | Type | Notes |
|---|---|---|
| Red Hat Hardened Images | Container image program | Minimal, hardened, verifiable image catalog |
| Project Hummingbird | Build and packaging foundation | Powers the hardened image pipeline |
| SLSA 3 | Supply-chain provenance standard | Used to describe trusted build provenance |
| SBOM | Software inventory artifact | Delivered for transparency and verification |
| OpenSCAP / CIS / STIG | Compliance and scanning references | Part of the hardening and benchmark story |
| images.redhat.com | Image catalog | Used in the lab exercises |

## Notable Takeaways
1. Image selection is an application-security decision, not a trivial packaging choice.
2. Minimal images help most when they are paired with fast remediation and strong provenance.
3. SBOMs and verification data are becoming table stakes for enterprise container trust.
4. The lab presents hardened images as a way to buy back engineering time, not just a way to shrink image size.

## Representative Visuals
Representative visuals retained from transcript-style PDFs or source photos:

- ![Representative visual 1](img/container_hardening_transcript_p001_img01.jpeg)
- ![Representative visual 2](img/container_hardening_transcript_p001_img02.jpeg)