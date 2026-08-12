# ch02_framework.tex 图 2.9（成对势示意图）改进

## TODOs

- [x] 1. 改进图 2.9 TikZ 代码：增加 η 标注、变形前后线型区分、分离 f/−f 箭头、势函数标注框线化（chapters/ch02_framework.tex 第 571–590 行）

## 修改内容

**文件**：`chapters/ch02_framework.tex`
**目标**：第 571–590 行 `figure` 环境（`\label{fig:pairwise-potential}`，图 2.9）

### 现状问题

| # | 问题 | 具体表现 |
|---|------|----------|
| 1 | **η 未出现** | 正文第 523 行定义 η 为"键的相对位移"，图中仅标注 ξ 与 ξ+η，η 本身缺失 |
| 2 | **变形前后区分弱** | 仅靠颜色（黑/红）区分参考/变形构型，对灰度打印不友好 |
| 3 | **f 与 −f 重叠** | 两个力矢量画在同一直线上完全重合，视觉上易误判 |
| 4 | **势函数标注简陋** | "成对势"仅用简单虚线箭头指向键，无框线，视觉层级不清晰 |

### 修改后代码（替换整个 tikzpicture 环境）

```latex
  \begin{tikzpicture}[scale=1.0]
    % 参考构型（变形前）
    \filldraw (0,0) circle (3pt) node[below] {$\mathbf{x}$};
    \filldraw (4,0) circle (3pt) node[below] {$\mathbf{x}'$};
    \draw[thick, dashed, gray] (0,0) -- (4,0);
    \node[above, gray] at (2,0) {$\boldsymbol{\xi}$};
    % 变形后位置
    \filldraw[red] (0.3,0.2) circle (2.5pt) node[above left, red] {$\mathbf{y}$};
    \filldraw[red] (4.4,0.8) circle (2.5pt) node[above right, red] {$\mathbf{y}'$};
    \draw[ultra thick, red] (0.3,0.2) -- (4.4,0.8);
    \node[red, above] at (2.35,0.5) {$\boldsymbol{\xi}+\boldsymbol{\eta}$};
    % 变形矢量 η（新增）
    \draw[-{Stealth}, densely dotted, purple] (0,0) -- (0.3,0.2)
      node[midway, left, purple] {$\boldsymbol{\eta}$};
    % 对力（分离显示，避免重叠）
    \draw[-{Stealth}, ultra thick, blue] (0.3,0.25) -- ++(3.5,0.5)
      node[midway, above, blue] {$\mathbf{f}$};
    \draw[-{Stealth}, ultra thick, blue] (4.4,0.75) -- ++(-3.5,-0.5)
      node[midway, below, blue] {$-\mathbf{f}$};
    % 势函数注释框
    \node[draw, rectangle, rounded corners, fill=white, align=center]
      (potential) at (6.5, 0.4) {成对势\\ $w(\boldsymbol{\eta},\boldsymbol{\xi})$};
    \draw[->, dashed] (potential.west) -- (2.35, 0.5);
  \end{tikzpicture}
```

### 保留不变

- `\centering`、`\caption`（第 591 行）、`\label{fig:pairwise-potential}`（第 592 行）
- 图注文字：`微弹性材料中，成对势 $w$ 在键两端对称，导出的对力 $\mathbf{f}$ 沿变形后键方向并满足反作用条件`（如语义仍准确则不改，仅当图注与新增 η 标注冲突时才微调）

## 修改理由

1. **η 是核心变量**：正文第 553–559 行以 η 为核心讨论不变量与成对势形式，图中 η 缺失导致"键的相对位移"概念缺乏直观载体
2. **灰度打印友好**：线型区分（虚线=参考构型、实线=当前构型）使信息不依赖颜色
3. **反作用条件视觉清晰**：f 与 −f 微移分离，体现"作用在两点上的作用–反作用对"
4. **注释框规范化**：与 AGENTS.md 插图规范一致，视觉层级分明

## Final Verification Wave

- [x] F1. 编译验证：xelatex×3 + bibtex 无 error、无 undefined reference/citation 警告
- [x] F2. 图注一致性：图注文字与新增 η 标注不冲突，全书线型约定（参考构型虚线、当前构型实线）自洽
