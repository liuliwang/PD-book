## [2026-08-09] task: ch11-intro-11.1-11.2

### Style Decisions
- Followed ch04 pattern: chapter intro previews all sections, section intro previews subsections, subsection intro provides context.
- Used `\leavevmode\usetikzlibrary{arrows.meta}` at file top for TikZ figure in 11.2.3 (basic scope commands only, no special libs needed but declared for consistency).
- Equation labels use `eq:ch11-xxx` pattern; cross-chapter refs use existing labels (`eq:history-variable`, `eq:damage-variable`, `eq:volume-beta`, `eq:surface-alpha`, `eq:critical-stretch-3d`).
- Only 1 remark used in 11.2.2 (budget: max 4 per chapter, 1 in 11.1 + 1 in 11.2 used).
- AI declaration `\emph{AI 辅助生成，需经专业审阅。}` placed at end of 11.1 and 11.2 exactly.

### Tricky LaTeX Pitfalls
- LSP reports "Undefined reference" for cross-file refs (`eq:history-variable`, `eq:damage-variable`, `eq:volume-beta`, `eq:surface-alpha`, `eq:critical-stretch-3d`). These are FALSE POSITIVES -- the labels exist in ch02, ch04, ch06 respectively. Multi-file LaTeX projects always show these in single-file LSP mode.
- Must NOT use `\[ \]` for display math -- all equations use `\begin{equation}` + `\label`.
- Must NOT use `**` (Markdown bold) -- verified zero hits via grep.
- TikZ figure in 11.2.3 uses only basic commands (`scope`, `fill`, `draw`, `node`), no special libraries needed.

### Content Notes for Next Writer
- Sections 11.3--11.6 are left as empty `\section` skeletons -- do NOT remove or reorder.
- Cited NEW bib keys (Du2020, KilicAgwaiMadenci2009, HaBobaru2011) that will be added in a later task -- compilation will warn until then.
- The remark in 11.2.2 cites LeBobaru2018 surface correction data (30-50% boundary damage overestimation) -- verify against original paper if possible.
- Crack speed estimation (11.2.4) references Rayleigh wave speed limit -- if ch03 or ch06 defines `eq:rayleigh-speed`, consider cross-referencing instead of inline definition.

## [2026-08-09] task: ch11-citation-fixes

### FIX 1 -- HaBobaru2010 + HuHaBobaru2012
- **Before**: Claimed HaBobaru2010 studied composite delamination with ply-aligned pre-cracks.
- **After**: HaBobaru2010 = glass plates, dynamic branching, pre-crack via "break all bonds crossing the pre-crack line"; HuHaBobaru2012 = unidirectional fiber-reinforced composite dynamic fracture with ply-aligned pre-cracks.
- **File location**: 11.1.2, second paragraph

### FIX 2 -- KilicAgwaiMadenci2009
- **Before**: Claimed center-cracked laminate under impact, compared FE vs PD implementation complexity.
- **After**: Center-cracked laminate under uniaxial tension; PD predicts damage without special crack growth criteria, agreeing with experiments.
- **File location**: 11.1.2, last paragraph

### FIX 3 -- BobaruHu2012
- **Before**: Claimed m>=4 suppresses oblique-crack mesh sensitivity.
- **After**: Crack-path m-convergence obtained even at m=3; m=4 is typical; larger m costs more without changing results; zigzag smoothed by averaging over many bonds within the horizon.
- **File location**: 11.1.4, second paragraph

### FIX 4 -- LeBobaru2018 (remark in 11.2.2)
- **Before**: Claimed unverifiable 30%-50% boundary damage overestimation figure.
- **After**: Qualitative statement -- surface effect causes stiffness/damage deviation near boundaries, affecting crack identification; dynamic problems accumulate error over time.
- **File location**: 11.2.2, remark environment

## [2026-08-09] task: ch11-11.3-11.4

### Content Summary
- Wrote 11.3 "动态裂纹扩展追踪" (4 subsections: 11.3.1-11.3.4) and 11.4 "I型、II型及混合型断裂" (4 subsections: 11.4.1-11.4.4).
- Final file length: 323 lines (was 200 lines).
- Sections 11.5 and 11.6 skeletons preserved at end of file.

### Labels and Equations Added
- `sec:ch11-dynamic-crack`, `sec:ch11-explicit-time`, `sec:ch11-m-convergence`, `sec:ch11-branching`, `sec:ch11-crack-velocity`
- `sec:ch11-mixed-mode`, `sec:ch11-fracture-modes`, `sec:ch11-mode-i`, `sec:ch11-mode-ii-mixed`, `sec:ch11-mode-limitations`
- `eq:ch11-motion-discrete`, `eq:ch11-velocity-verlet`, `eq:ch11-cfl`, `eq:ch11-rayleigh-equation`, `eq:ch11-energy-criterion`, `eq:ch11-cod`
- All labels referenced at least once in body text.

### Cross-References Used
- ch02: `eq:motion`, `eq:history-variable`, `eq:damage-variable`
- ch04: `eq:volume-beta`, `eq:surface-alpha`
- ch06: `eq:critical-stretch-3d`, `eq:osb-critical-stretch`, `eq:foster-3d`, `eq:osb-3d`, `eq:griffith-irwin`
- ch11 internal: `eq:ch11-damage-band`, `eq:ch11-rayleigh-limit`, `eq:ch11-cfl`

### Citation Keys Used (NEW keys marked)
- 11.3: SillingAskari2005, BobaruHu2012, HaBobaru2010, SillingWeckner2010, HaBobaru2011, BobaruZhang2015, Agwai2011, Ghajari2014
- 11.4: Irwin1957, SillingAskari2005, Griffith1921, KilicAgwaiMadenci2009, Zhang2016Fatigue (NEW), ZhouWang2016, WangZhou2016, KilicMadenci2009, Wang2023 (NEW), Imachi2018 (NEW), Dai2021 (NEW), Imachi2019 (NEW)

### Style Notes
- No remarks used in 11.3 or 11.4 (budget: 1 per section, saved for 11.5/11.6).
- AI declarations placed at end of 11.3 and 11.4.
- Zero Markdown syntax hits (`**`, `# `, backticks) verified via grep.
- No `\[ \]` used; all equations in `\begin{equation}` + `\label`.

### Traps Encountered
- **Syntax error**: `c_{\max}}` had an extra `}` in 11.3.1 -- fixed.
- **Unreferenced labels**: Initial draft had 5 equations with labels but no body references -- fixed by adding `式\eqref{...}` in surrounding text.
- **ch03 has no CFL content**: Had to introduce CFL condition de novo in 11.3.1 rather than cross-referencing.
- **ch06 has no Rayleigh wave speed formula**: Used inline definition in 11.3.4 with cross-reference to `eq:ch11-rayleigh-limit` from 11.2.4.

### Handoff Notes for 11.5/11.6
- 11.4.4 ends with transition sentence: "第 11.5 节将进一步讨论动态应力强度因子的计算方法，其中模式分离是实现精确 SIF 计算的关键。"
- 11.5 (动态应力强度因子的计算) should pick up from 11.4.4's mode-separation theme.
- 11.6 (多裂纹交互作用模拟) should reference 11.1.4's arbitrary-crack discussion and 11.3.3's branching discussion.

## [2026-08-09] task: ch11-11.3-11.4-fixes

### FIX 1 -- line 276: Dipasquale citation
- **Before**: "Dipasquale 等的研究表明..." -- no cite key.
- **After**: Added `\cite{Dipasquale2017}` after verifying the paper title "A discussion on failure criteria for ordinary state-based peridynamics" directly addresses failure-criteria comparison in mixed-mode fracture.
- **File location**: 11.4.1, last paragraph

### FIX 2 -- line 293: uncited 5% claim
- **Before**: "误差可控制在 $5\%$ 以内" -- specific number without citation.
- **After**: Weakened to "吻合良好" because `KilicAgwaiMadenci2009` key does not exist in bibliography.bib; no verifiable source for the 5% figure.
- **File location**: 11.4.2, third paragraph

### FIX 3 -- line 220: longitudinal wave speed mismatch
- **Before**: $c_L$ formula gave $\approx 1830$ m/s but text claimed $1580$ m/s (which is actually the bar wave speed $c_0=\sqrt{E/\rho}$).
- **After**: Changed $1580$ to $1830$ m/s and added "（取 $\nu=0.3$）"; updated subsequent $\Delta t$ from $3.2\times10^{-7}$ s to $2.7\times10^{-7}$ s to match.
- **File location**: 11.3.1, second paragraph

### FIX 4 -- line 196: English word "regime"
- **Before**: "推广到动态断裂 regime。"
- **After**: "推广到动态断裂情形。"
- **File location**: 11.3 section intro

### Verification
- `grep '\*\*'` on ch11_crack_damage.tex: zero hits.
- `grep '\\\[' on ch11_crack_damage.tex: zero hits.
- All 4 fixes localized; no label names changed; 11.5/11.6 skeletons untouched.

## [2026-08-09] task: ch11-11.5-11.6

### Content Summary
- Wrote 11.5 "动态应力强度因子的计算" (4 subsections: 11.5.1-11.5.4) and 11.6 "多裂纹交互作用模拟" (4 subsections: 11.6.1-11.6.4).
- Added chapter closing paragraph after 11.6 AI declaration.
- Final file length: 465 lines (was 323 lines).

### Labels and Equations Added
- `sec:ch11-dynamic-sif`, `sec:ch11-cod-method`, `sec:ch11-nonlocal-j`, `sec:ch11-interaction-integral`, `sec:ch11-dynamic-sif-time`
- `sec:ch11-multi-crack`, `sec:ch11-multi-crack-pre`, `sec:ch11-crack-coalescence`, `sec:ch11-shielding`, `sec:ch11-random-cracks`
- `eq:ch11-displacement-asymptotic`, `eq:ch11-cod-ki`, `eq:ch11-cod-extrapolation`, `eq:ch11-classical-j`, `eq:ch11-pd-j-integral`, `eq:ch11-classical-interaction`, `eq:ch11-williams-field`, `eq:ch11-dynamic-amplification`, `eq:ch11-time-filter`, `eq:ch11-defect-density`, `eq:ch11-weibull`
- All labels referenced at least once in body text.

### Cross-References Used
- ch11 internal: `eq:ch11-cod` (11.4.2), `eq:ch11-cfl` (11.3.1), `eq:ch11-damage-discrete` (11.2.1)
- ch12衔接: 章末收尾段明确衔接第12章"近场动力学与有限元法的混合模型"

### Citation Keys Used (NEW keys marked)
- 11.5: MadenciOterkus2014, KilicAgwaiMadenci2009, HuHaBobaruSilling2012 (NEW), Imachi2018 (NEW), Dai2021 (NEW), Wang2023 (NEW), Imachi2019 (NEW)
- 11.6: ZhouZhuZhu2022 (NEW), WangZhou2016, Wang2023 (NEW), ZhouWang2016, KilicMadenci2009, Bobaru2016, LeBobaru2018, Zhu2021 (NEW)
- Note: `Rice1968` was initially cited for J-integral origin but removed because it is NOT in the approved citation list; replaced with plain text "Rice 于 1968 年首次提出".

### Style Notes
- No remarks used in 11.5 or 11.6 (budget: 1 per section; total chapter remarks = 1, well under the 4-limit).
- AI declarations placed at end of 11.5 and 11.6.
- Zero Markdown syntax hits (`**`, `# `, backticks) verified via grep.
- No `\[ \]` used; all equations in `\begin{equation}` + `\label`.

### Traps Encountered
- **Missing formula content**: `eq:ch11-displacement-asymptotic` was initially just `u\label{...}` with no actual formula body -- fixed by adding full asymptotic displacement field expression.
- **Unreferenced labels**: Initial draft had 3 equations with labels but no body references (`eq:ch11-cod-extrapolation`, `eq:ch11-dynamic-amplification`, `eq:ch11-defect-density`) -- fixed by adding `式\eqref{...}` in surrounding text.
- **Unauthorized citation**: `Rice1968` was cited for J-integral origin but is not in the approved citation list -- removed cite key, kept as plain text attribution.

### Handoff Notes for Future Tasks
- ch11 is now COMPLETE (all 6 sections written: 11.1-11.6).
- Remaining work: add NEW bib keys to `bibliography.bib` (HuHaBobaruSilling2012, Imachi2018, Imachi2019, Dai2021, Wang2023, ZhouZhuZhu2022, Zhu2021); compilation will show "undefined citation" warnings until then.
- Consider adding `eq:j-integral` or similar to ch06 if a dedicated J-integral section is ever added there -- currently ch06 has no J-integral content, so 11.5.2 defines it de novo.
- Chapter closing paragraph references ch12 "近场动力学与有限元法的混合模型" -- verify ch12 title remains accurate before final compilation.

## [2026-08-09] task: ch11-bib-append-14

### Task
Appended 14 BibTeX entries to `bibliography.bib` (ch11 crack/damage citations). File grew from 121 to 135 entries.

### Crossref accessibility
- `https://api.crossref.org/works/<DOI>` reachable and returned JSON for all 14 DOIs.
- Rate limit observed: 4 parallel webfetch calls triggered one 429; batches of 2-3 succeeded.

### 14 keys appended (all verified against Crossref metadata)
HaBobaru2011, BobaruZhang2015, HuHaBobaruSilling2012, KilicMadenci2009, KilicAgwaiMadenci2009, Imachi2018, Imachi2019, Dai2021, Zhang2016Fatigue, NguyenOterkusOterkus2021, Zhu2021, Du2020, ZhouZhuZhu2022, Wang2023

## [2026-08-09] task: ch11-notation-table

### Task
Appended a 5th section to `frontmatter/notation.tex`: `\section*{第 11 章 裂纹与损伤的数值模拟}` in short-tabular format (matching ch02/ch04 style). File grew from 136 to 155 lines.

### 11 symbols registered (descriptions per ch11 actual definitions)
1. `$c_L$` 纵波速（eq:ch11-cfl 算例，$\sqrt{E(1-\nu)/[\rho(1+\nu)(1-2\nu)]}$）
2. `$c_T$` 横波速 $\sqrt{\mu/\rho}$（eq:ch11-rayleigh-equation）
3. `$c_R$` 瑞利波速（eq:ch11-rayleigh-equation；$\nu\approx 0.25$ 时 $c_R\approx 0.92\,c_T$）
4. `$v_c$` 裂纹扩展速度，$v_c<c_R$（eq:ch11-rayleigh-limit）
5. `$C$` CFL 稳定性常数，$\Delta t\le C\Delta x/c_{\max}$（eq:ch11-cfl），常用 $0.3\sim0.7$
6. `$\Lambda_d$` 动态放大因子（eq:ch11-dynamic-amplification）
7. `$J^{\mathrm{PD}}$` 非局部 J 积分（eq:ch11-pd-j-integral），$\delta\to0$ 收敛于经典 J 积分（eq:ch11-classical-j）
8. `$K_I$，$K_{II}$` I 型、II 型应力强度因子
9. `$\rho_d$` 缺陷密度 $N_d/A$（eq:ch11-defect-density）
10. `$\sigma_f$` 断裂强度（Weibull 变量，eq:ch11-weibull）
11. `$\sigma_0$` Weibull 特征强度（eq:ch11-weibull）

### m symbol conflict note
Per task instruction, `$m$` was NOT registered (already in ch06 as weighted volume; also used as grid ratio $m=\delta/\Delta x$ in ch11 11.1.4/11.3.2). Added a `%` LaTeX comment line between `\section*` and `{\small` alerting the author that ch11 11.6.4 reuses `m` as Weibull modulus (shape parameter) — cross-section symbol reuse, author should consider distinguishing.

### Verification
- `\section*{第 11 章` appears exactly once; 11 symbol rows present.
- All 8 eq labels referenced exist in ch11 (verified against source).
- No Markdown syntax, no `\[ \]`.
- Only notation.tex modified; existing 4 sections untouched.

### Format notes
- Author initials from Crossref given names, e.g. Ha Youn Doh → `Ha, Y. D.`; Dai Ming-Jyun → `Dai, M.-J.`; Bordas Stéphane P.A. → `Bordas, S. P. A.`.
- Article-number pages (no range) written without `--`, matching existing `Scabbia2024` style: Dai2021 {102841}, NguyenOterkusOterkus2021 {107373}, Zhu2021 {108572}, Du2020 {107315}, ZhouZhuZhu2022 {221013}, Wang2023 {116016}.
- ZhouZhuZhu2022 kept `number = {10}` (Royal Society Open Science 9(10)).
- Imachi2018/2019, Dai2021, Zhang2016Fatigue, Zhu2021, Du2020, Wang2023 have no Crossref issue number → `number` omitted.
- No duplicates: grep before/after confirmed all 14 keys appear exactly once.

## [2026-08-09] task: ch11-bib-append-3-ch05

### Task
Appended 3 BibTeX entries to `bibliography.bib` to fix missing-key warnings in `ch05_bond_improved.tex` (DianaCasolo2019, WangZhouShou2017, WangZhouWang2018). File grew from 135 to 138 entries.

### Crossref-verified metadata (fields verbatim from Crossref API)
- DianaCasolo2019 = IJSS 160:201-231, 2019, doi 10.1016/j.ijsolstr.2018.10.026
- WangZhouShou2017 = IJMS 128-129:614-643, 2017, doi 10.1016/j.ijmecsci.2017.05.019
- WangZhouWang2018 = IJSS 134:89-115, 2018, doi 10.1016/j.ijsolstr.2017.10.022

### Verification
- 3 keys each appear exactly once in bibliography.bib (grep confirmed).
- Entry count 138 (135 + 3).
- All page ranges use `--` (201--231, 614--643, 89--115); no article-number pages in this batch.
- File is UTF-8 no BOM, CRLF line endings, trailing newline after final `}` (consistent with existing file).
- ch05 compilation warnings for these 3 keys should now disappear.
