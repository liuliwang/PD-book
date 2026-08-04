# Learnings — optimize-fig-22-reference-deformation

Conventions, patterns, and successful approaches discovered during work on this plan.

_Auto-scaffolded by /start-work. Append new entries below - never overwrite._

---
# Learnings — optimize-fig-22-reference-deformation

Conventions, patterns, and successful approaches discovered during work on this plan.

_Auto-scaffolded by /start-work. Append new entries below - never overwrite._

---
## Task 1: 5-direction optimization of fig:reference-deformation (2026-08-04)

### Changes made (ch02_framework.tex, figure block line 275-303 + citation sentence line 305)
- **Dir 2 (u arrow origin)**: right-panel ghost reference position moved (2.8,1.9) -> (2.6,1.6) — now coincides EXACTLY with left-panel x coordinate; blue u arrow starts at (2.6,1.6) -> y(x,t) (3.6,2.8), making "x -> y(x,t) connected by u" visually explicit.
- **Dir 3 (panel correspondence)**: achieved via same-coordinate trick above (left x <-> right ghost circle at same local (2.6,1.6)); NO cross-panel arrows/lines added (layout separation preserved).
- **Dir 5 (label crowding)**: u label changed `above left` @(3.2,2.35) -> `above` @(3.1,2.2) (centered over arrow midpoint); xi+eta label changed `above` -> `left` @(3.3,3.2) — original `above` + y(x',t) `right` combo had only ~0.1cm vertical gap (3.42 vs 3.55); `left` gives full vertical separation (3.2-3.4 vs 3.6-3.78). Verified no text/arrow/outline overlap by coordinate math.
- **Dir 1 (verified already-present)**: y(x,t) @(3.6,2.8) & y(x',t) @(3.0,3.6) both red filldraw 2.5pt with labels; deformed bond red -{Stealth} (3.6,2.8)->(3.0,3.6) labeled xi+eta — no change needed.
- **Dir 4 (caption+text)**: caption kept as-is (title-style, no colon). Citation sentence line 305 extended: appended "，参考键 $\boldsymbol{\xi}$ 相应变为变形后的 $\boldsymbol{\xi}+\boldsymbol{\eta}$。" — wording differs from both eq:deformed-bond (formula) and §2.1.2 text (which uses "相对位移矢量 eta 使键矢量变为"), no verbatim repetition.
- **Unchanged (compliant already)**: horizon dashed circle `[dashed, thick]` + delta dash-dot gray line match fig:horizon-definition; xshift=6cm (unit kept); (a)(b) full-width parens, centered below panels; scale=1.0.

### Verification (all passed)
- xelatex -halt-on-error x2: exit 0 both passes, 139 pages.
- main.log filter (Error|undefined|Warning: Reference, excluding infwarerr line): 0 hits; Overfull hbox: 0; Underfull vbox: 1 (known-benign notation.tex).
- grep fig:reference-deformation in ch02_framework.tex = 2 (label line 302 + ref line 305).
- main.aux `\newlabel{fig:reference-deformation}` = {2.6}{20} — figure number 2.6 and page 20 unchanged (no float displacement).

### Reusable tips
- For two-panel correspondence without cross-panel lines: give right-panel ghost/reference markers the SAME local coordinates as left-panel counterparts — zero layout risk, immediate visual match.
- When a vector label and a point label compete for the same corner region, switch vector label to `left`/`right` of the line midpoint instead of `above`/`below` to free vertical space.
- Label anchor `above` at arrow midpoint: pick midpoint = (start+end)/2 of the arrow.
