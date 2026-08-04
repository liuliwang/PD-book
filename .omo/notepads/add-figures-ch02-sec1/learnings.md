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

## [2026-08-04] fig:boundary-truncation（现图2.5）优化：caption精简+正文去冗余+空心圆
- 背景：该图在 2.1.3 节插入 fig:horizon-definition（图2.4）后编号变为 2.5（aux 确认 {2.5}{19}，实际渲染页 35；aux 页码与渲染页可偏移，定位图须全文搜 caption 文本而非信 aux）
- 改动 A：caption 精简为标题式「内部物质点与边界物质点的近场域和族对比」，删表面效应解释+cite（正文 194 行已有，无 undefined citation）
- 改动 B：194 行末句原与段内前句重复「近场域被截断/族不完整/有效刚度差异」，改写为解释空心圆「图中物体边界以外的空心圆表示因近场域被截断而无法与 x 相互作用的潜在物质点」——去冗余+交代新图形元素，一举两得
- 改动 C：panel(b) 红色边界线 x=0 外侧加 3 个空心圆 (-0.3,1.6)/(-0.4,2.2)/(-0.5,1.2)，circle(2pt) 无填充，均<horizon 半径 1.3（距中心 1.0/1.25/1.27）且 x<0；最左 x=-0.5 绝对坐标 5.0cm 与 panel(a) 右缘 4cm 无重叠
- 验证法：pymupdf get_drawings 用 d['rect']（item[1] 是 Point 无 rect）过滤 3-6.5pt 小圆，3 hollow+15 filled 全部就位；空心圆 x_pdf 303-309 在 panel(a) 右缘 274 与 panel(b) 左缘 321 之间间隙
- 编译：xelatex 两遍 exit 0，139 页，log 过滤 ^!|undefined|Warning: Reference|Warning: Citation 零命中

## [2026-08-04] fig:boundary-truncation 子图标题移至面板下方
- 用户要求「子图标题放置在图片下方」（AGENTS.md 规范本就要求子图图名在图下方居中）
- 改动：panel(a)/panel(b) 的 `\node[above] at (2,3.6) {（a）内部物质点};` / `\node[above] at (2,3.6) {（b）边界物质点};` → `\node[below] at (2,-0.7) {…};`（x=2 保持面板相对中心，scope xshift 自动平移；y=-0.7 位于 F_x 标签 y=-0.25 下方约 0.2cm）
- 验证：pymupdf search_for 确认两标题 y=212.4-223.3 与 F_x y=199.1-210.0 间隙 2.4pt 无重叠；标题中心 x≈208.6/380.1 vs 面板中心 211.9/383.5（偏差<0.1cm 正常）；xelatex 两遍 exit 0 139 页
