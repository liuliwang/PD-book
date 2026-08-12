# ch02-sec233-dimension-transition — Draft

## Status
- intent: clear
- review_required: false
- classification: trivial (single-file text edit, ~5 lines added)
- status: awaiting-approval

## Scope
在 ch02_framework.tex 第 2.3.3 节（对力函数的量纲与物理意义）开头，添加一段过渡文字，改善"运动方程(2.6)两端各项的量纲必须一致"这一论断的逻辑连贯性。

## Problem
当前第 643–645 行：
```latex
2.3.1 节和 2.3.2 节分别建立了对力函数 $\mathbf{f}$ 的物理图像与数学结构。
在此基础上，本节通过量纲分析确定 $\mathbf{f}$ 的量纲——这是理解其物理意义的关键一步，也是第 4 章微模量标定的前提。

运动方程\eqref{eq:motion}两端各项的量纲必须一致，否则方程失去物理意义。
```

问题：从"本节目标"直接跳到"运动方程量纲必须一致"，缺少动机交代。读者会困惑：为什么回到运动方程？为什么不用对力函数定义式直接确定量纲？

## Proposed Fix
在第 644 行（"在此基础上…"段）之后、第 645 行（"运动方程…"）之前，插入一段过渡：

```latex
对力函数 $\mathbf{f}$ 的量纲无法从其定义式
$\mathrm{d}\mathbf{F}=\mathbf{f}\,\mathrm{d}V'\mathrm{d}V$
单独确定，因为该式中 $\mathrm{d}V'\mathrm{d}V$ 只是积分微元的标记，不携带独立量纲信息。
自然的做法是回到运动方程 \eqref{eq:motion}，利用方程两端量纲必须自洽这一条件来反推 $\mathbf{f}$ 的量纲。
```

## Acceptance
- 插入后第 645 行变为新插入文字，原第 645 行顺延
- 新插入文字与前后文衔接自然，无重复、无遗漏
- 不改变后续任何公式编号或引用
