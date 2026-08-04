# add-fig-22-reference-deformation-config - Work Plan

## TL;DR (For humans)

**What you'll get**: 在 ch02_framework.tex 第 2.2.1 节「参考构型与变形构型」末尾插入一幅 TikZ 双栏对比示意图，展示从参考构型到变形构型的映射关系，提升读者对宏观构型概念的理解。

**Why this approach**: 2.2.1 节目前仅有文字和公式叙述，缺少与 2.1 节微观键几何图互补的宏观构型视角。新增图可与图 2.2（键的几何）形成「宏观→微观」层次递进。

**What it will NOT do**: 不会修改任何现有图的内容或 label；不会新增章节内容或修改公式推导。

**Effort**: 小（~1 个文件，1 幅 TikZ 图）。

**Risk**: 低。TikZ 语法错误可能导致编译失败，但可通过编译验证即时发现。

**Decisions**: 无待决策项。位置、风格、图号分配均由现有约定唯一确定。

## Scope

### In Scope
- 在 `chapters/ch02_framework.tex` §2.2.1 末尾（`\subsection{相对位移的轴向—偏斜分解}` 之前）插入一幅 TikZ 内联图
- 图内容：参考构型（左栏）→ 变形构型（右栏）的映射关系
- 添加正文引用文字（1 句）
- 验证：xelatex 编译通过、交叉引用正确

### Out of Scope / Must-NOT-Have
- 不修改任何现有 10 幅图的内容
- 不修改任何现有 label 或 ref（LaTeX 自动编号）
- 不修改章节文字叙述（除新增 1 句图引用外）
- 不新增章节或修改公式

## Verification strategy

1. **编译验证**: `xelatex -interaction=nonstopmode main.tex` 零 error
2. **交叉引用验证**: grep 确认新增图有至少一处 `\ref{fig:reference-deformation}`
3. **图号连续性验证**: 确认新增图为图 2.6，现有图 2.6–2.10 自动顺延
4. **渲染正确性**: PDF 中图左右分栏、文字不重叠、符号清晰

## Execution strategy

单次编辑波次：在 `ch02_framework.tex` 中插入 TikZ 代码并添加引用文字。无需外部依赖。

## Todos

- [x] 1. 在 ch02_framework.tex §2.2.1 末尾插入 TikZ 参考构型与变形构型映射图
  - **References**: `chapters/ch02_framework.tex` 第 259–273 行（§2.2.1 内容），现有图 2.2（fig:bond-geometry，line 78–104）风格参考
  - **Acceptance criteria**:
    - 插入位置：`\subsection{相对位移的轴向—偏斜分解}` 之前
    - 使用 `figure` + `tikzpicture` 环境，`scale=1.0`，左栏（参考构型）+ 右栏（变形构型），`scope[xshift=6cm]` 分栏
    - 左栏包含：物体区域 B 轮廓、物质点 x 及其近场域（虚线圆）、代表性键 ξ
    - 右栏包含：变形后区域轮廓、对应点 y(x,t)、位移矢量 u（蓝色箭头）、变形后键 ξ+η
    - 图注：`\caption{参考构型与变形构型的映射关系}`
    - label：`\label{fig:reference-deformation}`
    - 图注后紧跟 1 句正文引用：「图\ref{fig:reference-deformation} 示意了从参考构型到变形构型的映射关系，其中位移场 \mathbf{u} 将每个物质点从参考位置映到当前位置。」
  - **Happy QA**:
    - `xelatex -interaction=nonstopmode main.tex` 连续运行两次，零 error
    - `grep -c "fig:reference-deformation" chapters/ch02_framework.tex` 返回 2（label + ref 各 1）
  - **Failure QA**:
    - 若编译报错 TikZ 语法错误，检查 `scope[xshift=6cm]` 单位是否缺失（必须带 `cm`）
    - 若图与正文重叠，检查 `figure[htbp]` 浮动参数
  - **Commit**: `chapters/ch02_framework.tex`

- [x] 2. 编译验证与交叉引用检查
  - **References**: `main.tex`（入口文件）
  - **Acceptance criteria**:
    - `xelatex -interaction=nonstopmode main.tex` 连续运行两次，无 error
    - `main.log` 中无 `undefined reference` 警告
    - 确认新增图为图 2.6，原图 2.6（fig:bond-decomp）自动变为图 2.7
  - **Happy QA**:
    - `xelatex main.tex && xelatex main.tex` 成功
    - `grep -c "Reference.*undefined" main.log` 返回 0
  - **Failure QA**:
    - 若出现图号错位，检查 `\label` 与 `\ref` 拼写是否一致
    - 若 `main.log` 中出现 `Overfull \hbox`，检查 TikZ 坐标是否超出边界
  - **Commit**: 无需新增文件（仅验证）

- [x] 3. 自动化视觉质量检查（main.aux 解析 + Overfull \hbox 检测）
  - **References**: `main.aux`, `main.log`
  - **Acceptance criteria**:
    - `main.aux` 中 `\newlabel{fig:reference-deformation}{{2.6}{...}}` 存在且图号正确
    - `main.log` 中无 `Overfull \hbox` 警告（ benign `infwarerr` 包描述行除外）
    - 浮动参数 `figure[htbp]` 未导致图漂过 `\subsection` 标题（通过检查 `main.log` 中无异常浮动警告确认）
  - **Happy QA**:
    - `grep "fig:reference-deformation" main.aux` 命中包含 `{2.6}` 的行
    - `grep -c "Overfull \\hbox" main.log` 返回 0
  - **Failure QA**:
    - 若 `main.aux` 中无 `fig:reference-deformation`，检查 `\label` 拼写是否完整
    - 若出现 `Overfull \hbox`，检查 TikZ 坐标是否超出边界，与现有工作图（如 `fig:bond-geometry`）进行语法比对
    - 若图漂过 `\subsection` 标题，尝试收紧浮动参数为 `[ht]` 或调整图尺寸
  - **Commit**: 无需新增文件（仅验证）

## Final verification wave

- [x] F1. 编译门禁：连续两次 `xelatex -interaction=nonstopmode -halt-on-error main.tex` 零 error
- [x] F2. 交叉引用完整性：`grep "fig:reference-deformation" chapters/ch02_framework.tex` 命中 ≥2（label + ref）
- [x] F3. 自动化视觉验证：`main.aux` 中 `\newlabel{fig:reference-deformation}{{2.6}{...}}` 存在且正确；`main.log` 中 `Overfull \hbox` 计数为 0；无异常浮动警告

## Commit strategy

单文件单 commit：

```
ch02: 在2.2.1节增加参考构型与变形构型映射示意图

- 新增图 fig:reference-deformation（TikZ 双栏对比图）
- 图号自动顺延，不影响现有交叉引用
- 经 xelatex 编译验证零错误
```

## Success criteria

1. `ch02_framework.tex` §2.2.1 末尾新增一幅 TikZ 图，展示参考构型与变形构型的映射
2. 正文新增至少一处对新增图的 `\ref{fig:reference-deformation}` 引用
3. `xelatex main.tex` 连续运行两次零 error
4. `main.log` 无 `undefined reference` 警告
5. `main.aux` 中 `\newlabel{fig:reference-deformation}` 图号正确，`main.log` 无 `Overfull \hbox` 警告
