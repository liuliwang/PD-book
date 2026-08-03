# add-material-point-figure - Work Plan

## TL;DR (For humans)

在 2.1.1 "物质点"小节末尾（两个自然段之后、2.1.2 之前）插入一幅左右对比的 TikZ 图，直观展示经典连续介质力学（局部）与近场动力学（非局部）在物质点相互作用方式上的本质区别。改动仅涉及 `chapters/ch02_framework.tex` 一处文件，约 35-50 行 TikZ 代码，不修改任何公式或段落内容。

## Scope

- **IN**: `chapters/ch02_framework.tex` 的 2.1.1 小节（第 12–16 行区域），插入一幅 TikZ 图 + `\label` + `\caption` + 正文引用句
- **OUT**: 不修改任何已有公式、段落、定理环境、引用；不碰其他文件
- **Must-NOT-Have**: 不与 fig:family-horizon（四概念整合图）内容重复；不用外部图片，全部 TikZ 矢量

## Verification strategy

- 编译验证：`xelatex main.tex` 两遍无 error，无新增 `undefined reference` 警告
- 视觉验证：生成的 PDF 中图位置正确（htbp 浮动，不独占整页），图中文字符号无重叠
- 交叉引用：正文中 `\ref{fig:material-point-comparison}` 解析为正确图号

## Execution strategy

单阶段，1 个实现 todo。无依赖。

## Todos

- [x] 1. 在 2.1.1 第二段后插入经典 CM vs PD 物质点对比 TikZ 图 — 图包含左右两个 panel：(a) 局部模型，物质点仅与无限小邻域内的点通过应力/变形梯度间接作用；(b) 非局部模型，物质点通过有限距离 δ 内的键直接与远处物质点相互作用。图注点明"经典局部连续介质力学与近场动力学在物质点相互作用方式上的对比"。在图前正文引用句中用 `\ref{}` 引用该图。

  **References**:
  - 目标文件: `chapters/ch02_framework.tex`，2.1.1 小节（当前行 12–16）
  - 插入位置: 行 16 之后、`\subsection{键}`（行 18）之前
  - 已有图风格参考: fig:bond-kinematics（行 30–76）、fig:family-horizon（行 154–184）
  - 引用格式: `图\ref{fig:material-point-comparison}`，label 为 `fig:material-point-comparison`
  - 使用 TikZ 内联绘图，`scale=1.0` 左右，图中文字用正文字体

  **Acceptance criteria**:
  - `grep 'fig:material-point-comparison' chapters/ch02_framework.tex` 恰好命中两处（`\label` + `\ref`）
  - 图注不含冒号（`caption` 宏包已全局配置 `labelsep=quad`）
  - TikZ 中使用 `\filldraw`、`\draw`、节点标注，风格与现有 8 幅图一致

  **QA — happy path**:
  - 命令: `xelatex main.tex && xelatex main.tex`
  - 预期: 编译无 error；无 `undefined` 相关警告；`main.pdf` 生成成功
  - 证据: 终端输出中无 `Error` 和 `Warning: Reference` 字样

  **QA — failure path**:
  - 若 `\label` 未定义或拼写错误：编译警告 `Reference ... undefined`，grep 对比 `\label` 和 `\ref` 字符串
  - 若图过大溢出：检查 `Overfull \hbox` 警告中是否有该图相关行号

  **Commit**: `feat(ch02): 在 2.1.1 物质点小节添加经典 CM 与 PD 非局部对比图`

## Final verification wave

- [x] F1. 计划合规审计：确认仅修改 `ch02_framework.tex`；确认 `\label` 和 `\ref` 成对出现；确认图注风格与项目规范一致
- [x] F2. 代码质量审查：TikZ 代码无硬编码坐标导致符号重叠；缩放因子不破坏页面布局
- [x] F3. 实际编译 QA：执行 `xelatex main.tex` 两遍，验证 PDF 无新增异常
- [x] F4. 范围保真度：确认未修改任何公式、未引入新包或外部图片

## Commit strategy

单次提交：`feat(ch02): 在 2.1.1 物质点小节添加经典 CM 与 PD 非局部对比图`

## Success criteria

1. 编译零 error，零新增 warning
2. 图在 PDF 中正确渲染，符号清晰无重叠
3. 交叉引用正确解析
4. 图的内容不重复 fig:family-horizon，聚焦于"局部 vs 非局部"的对比主题
