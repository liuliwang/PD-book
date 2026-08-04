---
slug: optimize-fig-22-reference-deformation
status: awaiting-approval
intent: clear
review_required: false
pending-action: write .omo/plans/optimize-fig-22-reference-deformation.md
approach: Modify TikZ code in ch02_framework.tex fig:reference-deformation to address 5 optimization directions identified in visual review.
---

# Draft: optimize-fig-22-reference-deformation

## Components (topology ledger)
<!-- Lock the SHAPE before depth. One row per top-level component that can succeed or fail independently. -->
<!-- id | outcome (one line) | status: active|deferred | evidence path -->

## Open assumptions (announced defaults)
<!-- Record any default you adopt instead of asking, so the user can veto it at the gate. -->
<!-- assumption | adopted default | rationale | reversible? -->

## Findings (cited - path:lines)

## Decisions (with rationale)

- **Optimization scope**: User confirmed ALL 5 directions (m0086).
  - Direction 1 (critical): Add missing y(x',t) point in right panel
  - Direction 2: Clarify displacement vector u origin
  - Direction 3: Strengthen mapping correspondence between panels
  - Direction 4: Improve caption-text coordination
  - Direction 5: Fine-tune visual details (colors, line styles)
- **File target**: `chapters/ch02_framework.tex` lines 275-305 (fig:reference-deformation)
- **Compile verification**: xelatex twice, zero errors

## Scope IN

- Modify TikZ code in fig:reference-deformation
- Add missing geometric elements (y(x',t) point, mapping arrows)
- Refine displacement vector positioning
- Update caption text if needed
- Compile verification and cross-reference check

## Scope OUT (Must NOT have)

- Do NOT modify any other figures
- Do NOT modify chapter text beyond caption
- Do NOT modify equations or section structure
- Do NOT change figure numbering or labels

## Open questions

- None remaining. User confirmed all 5 directions.

## Approval gate
status: awaiting-approval
<!-- When exploration is exhausted and unknowns are answered, set status: awaiting-approval. -->
<!-- That durable record is the loop guard: on a later turn read it and resume at the gate instead of re-running exploration. -->
