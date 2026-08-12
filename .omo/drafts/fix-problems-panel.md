# Draft: Fix Problems Panel Errors/Warnings

## Intent: CLEAR
## Review Required: false (trivial diagnostic task)

## Issues Found

### Issue 1: Malformed BibTeX entry (CRITICAL — causes BibTeX parse error)
- **File**: `bibliography.bib` lines 1748–1758
- **Problem**: `@article{WangZhouShou2017,` at line 1748 is incomplete — only has `author` field, then line 1750 starts `@article{DianaCasolo2019,` INSIDE it. This creates a nested/malformed entry that BibTeX cannot parse.
- **Evidence**: Lines 1748-1758:
  ```
  @article{WangZhouShou2017,
    author  = {Wang, Y. T. and Zhou, X. P. and Shou, Y. D.},
  @article{DianaCasolo2019,
    author  = {Diana, V. and Casolo, S.},
    title   = {A full orthotropic micropolar peridynamic formulation...}
    ...
  }
  ```
- **Fix**: Delete lines 1748-1758 entirely (the malformed block). The correct `WangZhouShou2017` exists at line 1572 and again at 1760. The `DianaCasolo2019` at line 1750 is a DIFFERENT paper (orthotropic) that needs a new key.

### Issue 2: Duplicate BibTeX entries (WARNING — BibTeX "repeated entry" warning)
- **File**: `bibliography.bib`
- **Problem**: Three keys appear multiple times:
  - `DianaCasolo2019`: lines 1562, 1738, 1750 (3× — 1750 is malformed, see Issue 1)
  - `WangZhouShou2017`: lines 1572, 1748, 1760 (3× — 1748 is malformed, see Issue 1)
  - `WangZhouWang2018`: lines 1582, 1770 (2×, identical)
- **Fix**: After removing the malformed block (Issue 1), delete the remaining duplicates:
  - Delete line 1738-1746 (`DianaCasolo2019` duplicate of line 1562)
  - Delete line 1760-1768 (`WangZhouShou2017` duplicate of line 1572)
  - Delete line 1770-1778 (`WangZhouWang2018` duplicate of line 1582)
- **Special**: The paper at line 1750 ("A full orthotropic micropolar peridynamic formulation") is a DIFFERENT paper from line 1562 ("A bond-based micropolar peridynamic model with shear deformability"). After removing the malformed block, this paper needs to be re-added with a unique key like `DianaCasolo2019ortho`.

### Issue 3: Stale build artifacts (WARNING — can cause cascade errors)
- **File**: `chapters/ch01_introduction.log` (empty, 0 lines)
- **Problem**: `autoClean=never` in LaTeX Workshop means stale `.aux`/`.bbl`/`.log` files accumulate. While `.gitignore` excludes them from git, they remain on disk and can cause "File ended while scanning" or phantom undefined-reference warnings.
- **Fix**: Delete all stale build artifacts: `*.aux`, `*.bbl`, `*.blg`, `*.log`, `*.out`, `*.toc` in the project root and `chapters/` subdirectory. Then do a clean full compile.

### Issue 4: Potential undefined cross-references (NEEDS VERIFICATION)
- **Problem**: 1700+ cross-references across 12 chapter files. Skeleton chapters (ch12-ch19) and appendices (appA-appE) have only headings — if any `\ref`/`\eqref` points to a label in these empty files, it will be undefined.
- **Verification**: Requires full compilation to detect. After fixing Issues 1-3, a clean compile will reveal any remaining undefined references.

### Issue 5: Hyperref warnings from ch03 section title (LOW — harmless)
- **File**: `chapters/ch03_ccm_pd.tex` line 291
- **Problem**: Section title contains `\texorpdfstring{$\sigma^{\mathrm{PD}}$}{sigma PD}` — this is ALREADY the correct fix. The AGENTS.md mentions 4 "Token not allowed in PDF string" warnings, but the current code already uses `\texorpdfstring`. These warnings are cosmetic and do not affect the PDF output.
- **Fix**: No action needed.

## Status: awaiting-approval
