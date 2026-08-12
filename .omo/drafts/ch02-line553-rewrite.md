# Draft: ch02-line553-rewrite

## Intent

CLEAR — user explicitly asked to modify line 553 of `chapters/ch02_framework.tex`.

## Problem Statement

Current line 553 abruptly introduces new concepts (SO(3), invariant theory, Gram matrix) that do not appear elsewhere in the chapter, creating a jarring transition. Additionally, the meaning of the new function symbol `\hat{w}` is never explained.

## Proposed Change

**File**: `chapters/ch02_framework.tex`  
**Line**: 553

**Old text**:
```
这一推论正是不变量理论（invariant theory）基本结果的直接应用：对三维空间中的两个矢量，旋转群 $\mathrm{SO}(3)$ 的全体不变量由三个基本不变量生成——$|\boldsymbol{\xi}|$、$|\boldsymbol{\eta}|$ 与 $\boldsymbol{\xi}\cdot\boldsymbol{\eta}$，它们恰好构成矢量对 Gram 矩阵的三个独立元素，而任意旋转不变的标量函数都必然可表示为这些基本不变量的函数。因此满足客观性的成对势可一般性地写为 $w=\hat{w}(I_1,I_2,I_3)$。
```

**New text**:
```
由于 $w$ 在旋转轨道上的值相同，而每个轨道又被 $(I_1,I_2,I_3)$ 唯一标记，因此 $w$ 的值完全由这三个不变量决定。换言之，$w$ 可以表示为以不变量 $(I_1,I_2,I_3)$ 为自变量的新函数。为与原来的函数 $w(\boldsymbol{\eta},\boldsymbol{\xi})$ 相区分，这个新函数记为 $\hat{w}(I_1,I_2,I_3)$。因此满足客观性的成对势可一般性地写为 $w=\hat{w}(I_1,I_2,I_3)$。
```

## Rationale

1. **Removes abrupt concepts**: Drops SO(3), invariant theory, and Gram matrix — none of which appear in the surrounding paragraphs.
2. **Uses established vocabulary**: Builds on "rotation orbit" already defined in the preceding paragraphs.
3. **Explains `\hat{w}`**: Explicitly states that `\hat{w}` is a new function whose arguments are the invariants $(I_1,I_2,I_3)$, and clarifies the distinction from the original six-argument function $w(\boldsymbol{\eta},\boldsymbol{\xi})$.
4. **Maintains flow**: The sentence naturally follows the discussion of $6-3=3$ degrees of freedom and the three invariant quantities.

## Verification

After edit, run:
```powershell
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

Expected: no errors, no undefined references.

## Status

awaiting-approval