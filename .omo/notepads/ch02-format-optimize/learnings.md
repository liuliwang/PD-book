# Learnings — ch02-format-optimize

Conventions, patterns, and successful approaches discovered during work on this plan.

_Auto-scaffolded by /start-work. Append new entries below - never overwrite._

---

## [2026-08-03] T1: Inserted chapter-level introductory paragraph in ch02_framework.tex between the tikz library line (line 4) and the first section (line 8). The new paragraph spans lines 6–6 (single long paragraph) and previews all 8 sections (2.1–2.8节) in reading order, states the chapter's purpose mirroring Ch1's structure, and references Ch1 and Ch3. Final line count: 856 (was 854). xelatex main.tex compiled successfully with no ch02-related errors.

## [2026-08-03] T2: Added transition sentences at three section boundaries (2.5→2.6, 2.6→2.7, 2.7→2.8) in ch02_framework.tex. Boundaries 1-4 (2.1→2.2, 2.2→2.3, 2.3→2.4, 2.4→2.5) were evaluated and found to already have adequate backward-referencing opening sentences; no changes made. For boundaries 5-7, new 1-2 sentence transitions were woven into the existing opening paragraphs: 2.6 now connects 2.5's energy discussion to compatibility conditions, 2.7 connects 2.6's conservation proofs to damage/failure, and 2.8 connects 2.7's damage model to boundary conditions. All transitions use hand-written section references ("2.5 节" etc.) per project convention. xelatex main.tex compiled successfully with no errors. Final line count: 856.

## [2026-08-03] T4: Dissolved 5 remark blocks into surrounding prose in ch02_framework.tex, leaving exactly 4 remarks (matching Chapter 1's style). Kept: (1) L298 — 键伸长客观性几何本质 (2.2节); (2) L392 — 分子动力学类比 (2.3节); (3) L640 — 守恒律证明共同结构"换元—相消" (2.6节); (4) L744 — "从微观涌现宏观" (2.7节). Dissolved: (1) L195-197 — 四概念层级关系 → merged into motion equation paragraph; (2) L467-469 — 力态差解耦 → merged into state-based equation paragraph; (3) L517-519 — 能量分析两条主线 → merged into stability paragraph; (4) L609-611 — 角动量以变形后位置定义 → merged into angular momentum theorem interpretation; (5) L844-846 — 非局部边界本质特征 → merged into boundary correction methods paragraph. All \eqref{}, \ref{}, and \cite{} references preserved. xelatex main.tex compiled successfully with no errors. Final line count: 826 (was 846).

## [2026-08-03] T5: Added chapter-closing paragraph at EOF (after 2.8 section's final content) in ch02_framework.tex. The paragraph echoes the T1 intro roadmap (2.1→2.8节), reaffirms the chapter's purpose (自洽、完备、与经典力学相容的理论框架), and previews Chapter 3 (手写"第 3 章"衔接). No math, cite, label, or section commands added. xelatex main.tex compiled successfully with no errors. Final line count: 828 (was 826).

## [2026-08-03] T6: Updated AGENTS.md to codify ch02 format optimization conventions. Edit 1: Appended ch02 format optimization fact to ##项目性质 (line 5) — includes chapter-level intro roadmap, section transitions, dissolved short paragraphs, remark reduction from 9 to 4, and chapter-closing paragraph; file size 828 lines. Edit 2: Added new ###章节写作模式 sub-section under ###写作质量 with 5 bullets: 章级导言段, 节间衔接, 段落连贯, remark克制, 章末收尾. Verified: AGENTS.md now 102 lines, valid Markdown, no existing content deleted.
