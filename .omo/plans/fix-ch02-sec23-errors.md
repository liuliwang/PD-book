# Plan: fix-ch02-sec23-errors

## Slug

fix-ch02-sec23-errors

## Intent

CLEAR — user explicitly requested a correction plan for 2.3节.

## Review Required

false

## Status

awaiting-approval → approved → committed

## Problem Statement

第2章2.3节（受力描述与运动方程）经审查发现2处实质性错误及3处可优化项，需修正以确保理论自洽、符号统一、物理图像清晰。

## Todos

- [x] 1. Fix dimension error: rho-uddot unit from N/m^4 to N/m^3 in ch02_framework.tex line 488
  - **Where:** `chapters/ch02_framework.tex`, line 488
  - **How:** Replace `=\mathrm{N}/\mathrm{m}^{4}` with `=\mathrm{N}/\mathrm{m}^{3}`
  - **Why:** kg/m^3 * m/s^2 = N/m^3, not N/m^4
  - **QA:** Compile with xelatex; grep `N/m^{4}` should return zero matches in ch02_framework.tex

- [x] 2. Fix physical description contradiction in ch02_framework.tex line 488
  - **Where:** Same line, phrase "f dV' 为力"
  - **How:** Rewrite to "integral f dV' 为力密度" or "f dV' 为力密度"
  - **Why:** integral f dV' must match left side rho-uddot (force density N/m^3), not force (N)
  - **QA:** Re-read paragraph to confirm consistency with equation dimensions

- [x] 3. Unify integration domain symbol from H_x to F_x in Eq. (2.19)
  - **Where:** `chapters/ch02_framework.tex`, line 477
  - **How:** Replace `\mathcal{H}_{\mathbf{x}}` with `\mathcal{F}_{\mathbf{x}}` in Eq. (2.19)
  - **Why:** Motion equation (2.4) uses F_x; consistency reduces reader confusion
  - **QA:** Verify no other H_x in 2.3.2 remains inconsistent

- [x] 4. Standardize potential derivative notation in Eq. (2.17)
  - **Where:** `chapters/ch02_framework.tex`, line 440
  - **How:** Replace `\frac{\partial w}{\partial\boldsymbol{\eta}}` with `\nabla_{\boldsymbol{\eta}} w` and add inline definition
  - **Why:** partial w/partial eta is non-standard; gradient notation is unambiguous
  - **QA:** Verify LaTeX compiles and notation is consistent with Chapter 6

- [x] 5. Enhance physical interpretation of central-force condition in 2.3.1
  - **Where:** `chapters/ch02_framework.tex`, around line 427
  - **How:** Add 2-3 sentences explaining: action-reaction allows perpendicular force components (creating torque), only central-force eliminates them; reference fig 2.2
  - **Why:** Reader may wonder why central-force is "stronger" than action-reaction
  - **QA:** Review paragraph for clarity; confirm no new undefined symbols introduced

## Final verification wave

- [x] F1. Compile ch02_framework.tex with xelatex (nonstopmode) and confirm zero errors
- [x] F2. Grep scan: `N/m^{4}` and `N/m^4` must have zero matches in ch02_framework.tex
- [x] F3. Cross-reference check: Eq. (2.19) domain symbol matches Eq. (2.4)
- [x] F4. Manual read-through of 2.3节 to confirm logical flow and consistency

## Scope

Must-NOT-Have: Changes to any other chapter or section; new figures; new equations.
