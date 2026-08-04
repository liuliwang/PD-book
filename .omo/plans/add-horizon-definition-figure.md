# 为 2.1.3 节添加近场域示意图

## 任务目标
在 ch02_framework.tex 的 2.1.3 节（近场域）中，添加一幅独立的近场域定义示意图，使"定义→见图→解释"的节奏更连贯。

## 当前问题
- 2.1.3 节首次定义近场域 $H_{\mathbf{x}}$ 时无图支撑
- 现有图 fig:boundary-truncation 侧重表面效应，fig:family-horizon 是四概念综合图，均不专注于"近场域定义"本身
- 违反"图文位置即时对应"原则

## 计划

- [x] 1. 在 2.1.3 节公式 (eq:horizon) 之后插入一幅极简 TikZ 示意图
  - **位置**：ch02_framework.tex 第 154 行（`eq:horizon` 定义之后、`近场范围 \delta 具有三个层面的含义`之前）
  - **内容**：以物质点 \mathbf{x} 为中心，虚线圆表示 H_{\mathbf{x}}，标注半径 \delta，内部点缀若干物质点
  - **风格**：与现有 fig:family-horizon、fig:boundary-truncation 一致（scale=1.1，2.5pt 中心点，2pt 邻居点，dashed thick 虚线圆）
  - **图注**：近场域 $H_{\mathbf{x}}$ 的定义：以物质点 $\mathbf{x}$ 为中心、$\delta$ 为半径的球（二维为圆），内部物质点与 $\mathbf{x}$ 通过键直接相互作用
  - **标签**：`fig:horizon-definition`
  - **引用**：在正文中添加引用，如"如图\ref{fig:horizon-definition}所示"

- [x] 2. 验证编译通过
  - 执行 `xelatex -interaction=nonstopmode -halt-on-error main.tex` 两遍
  - 确认无 Error / undefined reference / Warning: Reference
  - 检查图号与正文引用一致

- [x] 3. 更新符号表（如需要）
  - 确认新图未引入新符号（均为已有符号：$\mathbf{x}$、$H_{\mathbf{x}}$、$\delta$）

## 验收标准
- [x] ch02_framework.tex 2.1.3 节新增一幅 TikZ 图，图注简洁、标签正确
- [x] 正文有对图的引用（`见图\ref{fig:horizon-definition}`或类似表述）
- [x] xelatex 编译零错误，零 undefined reference 警告
- [x] 图与现有风格一致（虚线圆、点的大小、颜色方案）
