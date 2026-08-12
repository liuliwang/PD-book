# ch02_framework.tex 图 2.9 符号标记重叠修复

## 问题分析

图 2.9（`\label{fig:pairwise-potential}`）在 ch02_framework.tex 第 571–596 行，TikZ 代码经改进后（增加 η 标注、线型区分、f/−f 分离、注释框）存在三处符号标记位置重叠：

| # | 重叠对 | 原因 | 坐标分析 |
|---|--------|------|----------|
| 1 | **f 标签 与 ξ+η 标签**（高） | f 标签 `midway` 位于路径中点 (2.05, 0.5)，ξ+η 标签在 (2.35, 0.5)，两者 x 方向仅差 0.3 cm，y 方向 `above` 偏移后几乎重合 | f 中心≈(2.05, 0.75)，ξ+η 中心≈(2.35, 0.80)，占用区域重叠 |
| 2 | **引线与 ξ+η 标签**（中） | 引线终点 (2.35, 0.5) 正好是 ξ+η 标签的 south 锚点 | 箭头头与标签底部边缘重合 |
| 3 | **η 标签 与 y 标签**（中） | η 标签中心≈(-0.15, 0.10)，y 标签占用 x∈[-0.1, 0.3], y∈[0.2, 0.6] | x∈[-0.1, 0.15], y∈[0.2, 0.3] 区域有微小重叠 |

## 修改内容

**文件**：`chapters/ch02_framework.tex`
**目标**：第 583、586、589、595 行（tikzpicture 内）

### 修改 1：ξ+η 标签上移（第 583 行）

```latex
% 旧
\node[red, above] at (2.35,0.5) {$\boldsymbol{\xi}+\boldsymbol{\eta}$};
% 新
\node[red, above] at (2.35,0.65) {$\boldsymbol{\xi}+\boldsymbol{\eta}$};
```

**效果**：标签整体上移 0.15 cm，与 f 标签拉开 y 方向距离；与 −f 标签 y 方向间隙增大。

### 修改 2：η 标签下移（第 586 行）

```latex
% 旧
node[midway, left, purple] {$\boldsymbol{\eta}$}
% 新
node[midway, left, yshift=-0.1cm, purple] {$\boldsymbol{\eta}$}
```

**效果**：η 标签中心从 (-0.15, 0.10) 下移到 (-0.15, 0.00)，与 y 标签（占用 y∈[0.2, 0.6]）彻底分离。

### 修改 3：f 标签左移（第 589 行）

```latex
% 旧
node[midway, above, blue] {$\mathbf{f}$}
% 新
node[pos=0.35, above, blue] {$\mathbf{f}$}
```

**效果**：f 标签从路径中点 (2.05, 0.50) 移到路径 35% 处 (1.525, 0.425)，`above` 偏移后中心≈(1.525, 0.675)，与 ξ+η 标签中心 (2.35, 0.90) 的 x 方向距离从 0.3 cm 增大到约 0.8 cm。

### 修改 4：引线改道（第 595 行）

```latex
% 旧
\draw[->, dashed] (potential.west) -- (2.35, 0.5);
% 新
\draw[->, dashed] (potential.west) -- (3.0, 0.7);
```

**效果**：引线终点从 ξ+η 标签锚点 (2.35, 0.5) 改到变形后键右侧空位 (3.0, 0.7)，完全避开所有标签区域。

## 修改理由

1. **消除 f/ξ+η 重叠**：f 标签左移 + ξ+η 标签上移，两者从 x 方向 0.3 cm/y 方向几乎重合，变为 x 方向约 0.8 cm、y 方向约 0.2 cm 的充分分离
2. **消除引线/标签重合**：引线不再指向任何标签锚点，而是指向键右侧的空白区域
3. **消除 η/y 拥挤**：η 标签下移 0.1 cm，与 y 标签从 y 方向 0.1 cm 间隙增大到 0.2 cm，视觉上不再拥挤

## 验证方法

- xelatex -interaction=nonstopmode -halt-on-error main.tex（三遍）
- bibtex main
- 确认 0 undefined reference/citation
- 可选：用 PDF 查看器检查图 2.9 各标签无重叠
