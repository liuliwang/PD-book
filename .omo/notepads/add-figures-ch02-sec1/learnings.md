# Learnings — add-figures-ch02-sec1

Conventions, patterns, and successful approaches discovered during work on this plan.

_Auto-scaffolded by /start-work. Append new entries below - never overwrite._

---

## 2026-08-03 �� Implementation complete

- Added `\leavevmode\usetikzlibrary{arrows.meta, positioning, calc}` at ch02_framework.tex line 4 (after \chapter, blank lines around, ch01 convention).
- Figure A fig:bond-kinematics (two panels top/bottom, 41 TikZ lines): lead-in sentence line 28, figure block lines 29-76, label line 75. Bottom panel uses rigorous triangle construction: gray dashed translated �� (y �� y+��), blue Stealth arrow �� (y+�� �� y'), red bond ��+�� closing the triangle. Three sub-bond stretch examples (s>0 red / s=0 gray / s<0 blue) at y=-4.8 with |��+��|?|��| length labels.
- Figure B fig:boundary-truncation (two panels via \begin{scope}[xshift=5.5], 33 TikZ lines): lead-in line 110, figure block lines 111-152, label line 151. Truncated horizon drawn as arc only: (0.7,1.6) ++(-57.4:1.3) arc[start angle=-57.4, end angle=57.4, radius=1.3] (visible cap 114.8��; cut since cos�� �� -0.538 �� �ȡ�[-57.4��,57.4��]). Truncation marked with red dashed line along body boundary x=0.
- Figure D (concept hierarchy) NOT added �� section 2.1 now has 3 figures.
- Compilation: xelatex twice, exit 0 both passes, 88 pages; log has no ! errors, no undefined Reference/Citation warnings. Pre-existing warnings unchanged (caption Unused \captionsetup[table], notation.tex overfull 85.85pt).
- Gotcha: first xelatex pass shows "Reference undefined" for the two new labels �� expected; second pass resolves (no bibtex run needed).

## [2026-08-03] add-figures-ch02-sec1 COMPLETE
- Added 2 TikZ figures to ch02_framework.tex section 2.1 (fig:bond-kinematics=2.1, fig:boundary-truncation=2.2)
- Figure D (concept hierarchy) CANCELLED - density sufficient (3 figures total)
- Added \leavevmode\usetikzlibrary{arrows.meta, positioning, calc} at file top (line 4)
- xelatex x2 exit 0, 88 pages, zero undefined refs/citations
- Only ch02_framework.tex modified (+195 lines); notation.tex/AGENTS.md changes are pre-existing
- multimodal-looker APPROVED both figures visually
- Color convention used: black=reference, red=deformed, blue=annotations, gray dashed=geometric boundaries

## 2026-08-03 fix fig:bond-kinematics labels/spacing
- Relocated subfigure labels (a)/(b) from left edge to centered below each panel: `\node at (1.1,-0.6) {（a）参考构型};`, `\node at (1.65,-5.4) {（b）变形构型};`
- Spacing fix: label offsets `[above=N pt]`/`[below=N pt]` (4pt upper panel, 3pt lower panel, 2pt three-state); bottom panel shifted ~0.8 down (y≈-3.2→-4.0), three-state section to y=-6.2, η formula to y=-4.8
- Only the tikzpicture block of fig:bond-kinematics modified (lines 32-73); caption/label/surrounding text untouched
- xelatex x2 exit 0, 88 pages, no new warnings (notation.tex overfull 85.85pt + caption Unused \captionsetup[table] both pre-existing)
