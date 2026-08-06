# Learnings — add-fig-22-reference-deformation-config

Conventions, patterns, and successful approaches discovered during work on this plan.

_Auto-scaffolded by /start-work. Append new entries below - never overwrite._

---
## Task 1: insert fig:reference-deformation (2026-08-04)
- Inserted figure[htbp] fig:reference-deformation at end of §2.2.1 (after line-273 paragraph, before §2.2.2), plus one citation sentence: 图\ref{fig:reference-deformation} 示意了从参考构型到变形构型的映射关系，其中位移场 $\mathbf{u}$ 将每个物质点从参考位置映到当前位置。
- Style: two panels via scope[xshift=6cm] (explicit cm unit), scale=1.0, smooth-cycle light-fill region outlines (blue!8 / orange!8), dashed horizon r=1.5 with dash-dot gray δ annotation, -{Stealth} arrows, red deformed bond + ξ+η label, blue u arrow, ghost reference position as gray dashed circle (fig:bond-geometry precedent). Notation reuses §2.2.1: \mathcal{B}, \mathbf{x}, \mathbf{x}', \boldsymbol{\xi}, \mathbf{y}(\mathbf{x},t), \mathbf{y}(\mathbf{x}',t), \mathbf{u}, \boldsymbol{\xi}+\boldsymbol{\eta}, \delta. Caption title-style (no colon). Auto-numbered 2.6.
- Verification: xelatex x2 exit=0 both passes; log filter (Error|undefined|Warning: Reference minus infwarerr line) = zero hits; main.aux newlabel fig:reference-deformation = {2.6}{20}; grep -c fig:reference-deformation in ch02 = 2 (1 label + 1 ref). No commit performed.
