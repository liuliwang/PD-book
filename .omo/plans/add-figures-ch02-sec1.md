# add-figures-ch02-sec1 - Work Plan

## TL;DR (For humans)
为专著第2.1节（基本概念）增加 **3 幅 TikZ 教学插图**，提高读者对键的运动学、族不完整（表面效应）、四概念层级关系的理解。全部 inline TikZ 自绘，不引入新宏包、不改动其他文件、不新增外部图片。按文件自顶向下顺序串行插入：键运动学对比图 → 边界截断对比图 → 概念层级图 → 正文引用更新 → xelatex 编译验证。编译门禁：无 error、无 undefined reference/citation。单 commit 交付。

## Scope
### Must have
- 在 `ch02_framework.tex` 第2.1节中新增 **3 幅 TikZ 教学插图**（图A：键运动学对比，图B：边界截断，图D：概念层级），均在对应子节中融入正文
- 每幅图有 `\label{}`、正文 `\ref{}` 引用、符合 `labelsep=quad` 格式的 `\caption{}`
- 编译验证：xelatex ×2 → 无编译 error、无 undefined reference/citation 警告
- 图A中集成图C（键伸长三态展示），以多 panel 形式呈现

### Must NOT have (guardrails, anti-slop, scope boundaries)
- 不修改 `main.tex`、`preamble.tex`、`frontmatter/notation.tex`、`bibliography.bib`
- 不新增 `figures/` 目录下的外部图片（全部 TikZ inline）
- 不改变现有图 `fig:family-horizon` 的位置和内容
- 不修改其他章节文件
- 不引入新 LaTeX 宏包，**且不使用 `subcaption`/`subfigure`/`subfloat` 包**（多 panel 用单个 `tikzpicture` 内 `scope` 或 `minipage` + 手动 `\textbf{(a)}` 标注实现）
- 不绘制 3D/透视 TikZ 图（限 2D 示意）
- 不新增 `bibliography.bib` 条目（仅使用已有引用）
- 不在 `figures/` 目录新增任何文件
- 编译临时文件（.aux/.log/.toc 等）不提交
- 每幅新图的 TikZ 代码 ≤ 60 行（防止单图过度膨胀）
- 不修改 `fig:family-horizon` 的 label 或编号

## Verification strategy
> Zero human intervention - all verification is agent-executed.
- Test decision: tests-after — 添加插图后运行编译验证
- Evidence: `.omo/evidence/add-figures-ch02-sec1/` (xelatex log 提取、grep 检查)

## Execution strategy
### TikZ style convention（全书统一，所有新图必须遵循）
- **黑色实线**：参考构型元素（物质点、参考键、物体边界）
- **红色实线/箭头**：变形构型元素（变形后的键、位移量）
- **蓝色虚线/箭头**：纯标注量（η 矢量、s 标注等辅助信息）
- **灰色虚线**：非物理几何边界（近场域 H_{\mathbf{x}}）
- **线宽**：结构线 `thick`，辅助线 `thin` 或 `dashed`
- **点**：`\filldraw (x,y) circle (2pt)` — 遵循现有 fig:family-horizon 风格
- 遵循现有 `fig:family-horizon`（第 60–90 行）的色彩约定

### Parallel execution waves
- **Wave 1**（串行，共享同一文件）：Todo 1（图A）、Todo 2（图B）、Todo 3（图D）、Todo 4（引用更新）
  - 四个 todo 严格串行：都编辑 `ch02_framework.tex`，按文件自顶向下顺序插入以避免行号漂移
  - 插入顺序：2.1.2 图A → 2.1.4 图B → 2.1 末尾图D → 正文引用更新（扫尾，更新前后文 `\ref` 调用）
- **Wave 2**：Todo 5（编译验证）

### Dependency matrix
| Todo | Depends on | Blocks | Can parallelize with |
| --- | --- | --- | --- |
| 1. 图A | — | 2,3,4（文件内顺序） | — |
| 2. 图B | 1 | 3,4 | — |
| 3. 图D | 1,2 | 4 | — |
| 4. 引用更新 | 1,2,3 | 5 | — |
| 5. 编译验证 | 4 | — | — |

## Todos
> Implementation + Test = ONE todo. Never separate.
<!-- APPEND TASK BATCHES BELOW THIS LINE WITH edit/apply_patch - never rewrite the headers above. -->

- [x] 1. 在 2.1.2 节插入图A：键的运动学详图（参考↔变形构型对比，集成伸长三态）
  What to do / Must NOT do:
    - **前置步骤**：在 `ch02_framework.tex` 文件顶部（第 1 行 `\chapter` 之后、第 2 行 `\section` 之前）添加一行 `\usetikzlibrary{arrows.meta, positioning, calc}` — 遵循 ch01_introduction.tex（第 4 行）和 ch06_ordinary_state.tex（第 4 行）的惯例。不加载则图A和图B的箭头/布局语法编译失败。
    - 在 ch02_framework.tex 中，于"对力函数"段落之前（约第 24–25 行之间，即 s 定义之后、\mathbf{f} 描述之前）插入完整的 `\begin{figure}[htbp]...\end{figure}` 块
    - 图A为 TikZ 多 panel 图，上下排列，使用 `\begin{tikzpicture}` 绘制：
      - **上 panel（参考构型）**：两个黑色圆点 \mathbf{x} 和 \mathbf{x}'，连线标注 \boldsymbol{\xi}，长度 |\boldsymbol{\xi}|
      - **下 panel（变形构型）**：以灰色虚线标出参考位置；黑色圆点为变形后 \mathbf{y} 和 \mathbf{y}'，红色连线标注 \boldsymbol{\xi}+\boldsymbol{\eta}，蓝色箭头标注 \boldsymbol{\eta} = \mathbf{u}(\mathbf{x}',t)-\mathbf{u}(\mathbf{x},t)
      - **下 panel 中集成三个子键示例**（用小图或色彩区分）：s>0（拉伸，红色）、s=0（参考，灰色）、s<0（压缩，蓝色），每个标注 s 值和键长
      - 使用 `\node` 标注 panel 标题"（a）参考构型""（b）变形构型"
    - `\caption{键的运动学：参考构型与变形构型中的键几何关系，键伸长定义为 s=(|\boldsymbol{\xi}+\boldsymbol{\eta}|-|\boldsymbol{\xi}|)/|\boldsymbol{\xi}|}`
    - `\label{fig:bond-kinematics}`
    - 图注中不使用冒号（全局 `labelsep=quad` 已处理）
    - 不引入新宏包；若需要箭头样式，在 `\begin{tikzpicture}` 后加 `\usetikzlibrary{arrows.meta}`
    - 不修改该图前后的现有文字
  Parallelization: Wave 1 | Blocked by: — | Blocks: 2（文件内顺序依赖）
  References (executor has NO interview context - be exhaustive):
    - ch02_framework.tex:16-24（键的定义、ξ、η、s 的文字描述——图要放在这些定义之后）
    - ch02_framework.tex:60-90（现有 fig:family-horizon 的 TikZ 风格参考——使用 `\filldraw`, `\draw[dashed, thick]`, `circle (2pt)`, `\node` 标注）
    - ch01_introduction.tex:111-139（第1章 fig:horizon-bond 的键示意图风格参考）
    - preamble.tex:13（graphicx），preamble.tex:18（tikz），preamble.tex:11,36（caption 格式 labelsep=quad）
    - notation.tex:4-22（第2章符号表——确认所有符号已登记）
  Acceptance criteria (agent-executable):
    1. `grep -c "fig:bond-kinematics" chapters/ch02_framework.tex` 返回 ≥1
    2. 图块 `\begin{figure}` 至 `\end{figure}` 包含 `\caption{...}` 和 `\label{fig:bond-kinematics}`
    3. caption 文本中无冒号分隔符（`labelsep=quad` 全局生效）
    4. TikZ 代码包含 `\boldsymbol{\xi}`, `\boldsymbol{\eta}`, `\boldsymbol{\xi}+\boldsymbol{\eta}` 的标注
    5. 编译后无 TikZ 语法错误
  QA scenarios (name the exact tool + invocation):
    - Happy: 执行 `xelatex main.tex` → 编译无 error，产物 main.pdf 中可见新插图且编号正确
    - Failure: 故意在 `\boldsymbol{\xi}` 中拼错 → 编译报 `Undefined control sequence`
    Evidence: `.omo/evidence/add-figures-ch02-sec1/task-1-bond-kinematics.log`
  Commit: Y | feat(ch02): add bond kinematics figure (reference vs deformed config) with stretch states

- [x] 2. 在 2.1.4 节插入图B：边界截断与族不完整示意图
  What to do / Must NOT do:
    - 在 ch02_framework.tex 中，于族定义（式\eqref{eq:family}）之后、"表面效应"提及之前（约第 56–57 行之间）插入 `\begin{figure}[htbp]...\end{figure}` 块
    - 图B为 TikZ 左右双 panel 对比图：
      - **左 panel（内部物质点）**：物体 \mathcal{B} 的矩形区域内部，物质点 \mathbf{x} 居中，虚线圆 H_{\mathbf{x}} 完整，圆内散点表示 \mathcal{F}_{\mathbf{x}} 成员，标注"H_{\mathbf{x}}（完整）""\mathcal{F}_{\mathbf{x}}（完整）"
      - **右 panel（边界物质点）**：\mathbf{x} 靠近 \mathcal{B} 左边界，H_{\mathbf{x}} 被边界截断为不完整圆弧，\mathcal{F}_{\mathbf{x}} 散点显著减少，截断处以红色虚线标示，标注"H_{\mathbf{x}}（截断）""\mathcal{F}_{\mathbf{x}}（不完整）"
    - 边界用 `\draw[thick]` 或矩形表示
    - `\caption{内部物质点与边界物质点的近场域和族对比：边界附近的物质点其近场域被物体边界截断，族不完整，导致表面效应（surface effect，详见第10章）\cite{LeBobaru2018,Mitchell2015}}`
    - `\label{fig:boundary-truncation}`
    - 不引入新宏包
    - 不修改该图前后的现有文字和公式
  Parallelization: Wave 1 | Blocked by: 1（文件内顺序） | Blocks: 3,4
  References (executor has NO interview context - be exhaustive):
    - ch02_framework.tex:49-57（族定义、H_{\mathbf{x}} vs \mathcal{F}_{\mathbf{x}} 区别、表面效应提及）
    - ch02_framework.tex:60-90（现有 TikZ 风格参考：`\draw[dashed, thick]` 画圆、`\filldraw` 画点）
    - bibliography.bib 中 LeBobaru2018（行 389）和 Mitchell2015（行 399）均已存在
    - preamble.tex:11,36（caption 格式）
    - 现有 \cite{LeBobaru2018,Mitchell2015} 用法已在 ch02_framework.tex:56 中
  Acceptance criteria (agent-executable):
    1. `grep -c "fig:boundary-truncation" chapters/ch02_framework.tex` 返回 ≥1
    2. 图块包含 `\label{fig:boundary-truncation}` 和 `\caption{...}`
    3. caption 中包含 `\cite{LeBobaru2018,Mitchell2015}`
    4. TikZ 代码包含左右双 panel 结构（两个 `\begin{scope}[xshift=...]` 或等效布局）
    5. 编译后无 undefined citation 警告
  QA scenarios (name the exact tool + invocation):
    - Happy: `xelatex main.tex` → `bibtex main` → `xelatex main.tex` → `xelatex main.tex` → 无 "Citation … undefined" 警告
    - Failure: 移除 `\cite{LeBobaru2018}` → bibtex 后报 undefined citation
    Evidence: `.omo/evidence/add-figures-ch02-sec1/task-2-boundary-trunc.log`
  Commit: Y | feat(ch02): add boundary truncation / incomplete family figure for surface effect

- [~] 3. 在 2.1 节末尾插入图D：四概念层级关系图（可选——若前两幅图后密度合适则插入）CANCELLED：2.1 节已有 3 幅图（fig:family-horizon + fig:bond-kinematics + fig:boundary-truncation），密度已合理，按计划判据跳过
  What to do / Must NOT do:
    - 在 ch02_framework.tex 中，于 2.1 节注记（`\begin{remark}...\end{remark}`，第 101 行）之后、`\section{变形描述}`（第 105 行）之前插入 `\begin{figure}[htbp]...\end{figure}` 块
    - 图D为 TikZ 结构化框图，使用 `\node[draw, ...]` 绘制：
      ```
      物质点 \mathbf{x}（描述的主体）
        ↓
      键 (\mathbf{x},\mathbf{x}')（相互作用的基本单元）
        ↓
      近场域 H_{\mathbf{x}}（相互作用发生的几何范围）
        ↓
      族 \mathcal{F}_{\mathbf{x}}（参与相互作用的物质点集合）
      ```
    - 使用 `\usetikzlibrary{positioning}` 来排列节点，箭头用 `-Stealth`（此库需在 `{tikzpicture}` 环境内 `\usetikzlibrary{arrows.meta, positioning}` 加载)
    - 每个框用不同浅色填充（如 `fill=blue!10`, `fill=green!10` 等）
    - 四个框中分别附简要英文术语（material point, bond, horizon, family）
    - `\caption{物质点、键、近场域与族四个基本概念的层级关系}`
    - `\label{fig:concept-hierarchy}`
    - **判断标准**：若 Todo 1 和 2 完成后，2.1 节已有 3 幅图（含现有 fig:family-horizon），密度已合理则**跳过此 Todo**，在 plan 中标记为 `cancelled`
    - 不修改注记的现有文字
  Parallelization: Wave 1 | Blocked by: 1,2 | Blocks: 4
  References (executor has NO interview context - be exhaustive):
    - ch02_framework.tex:101-103（注记中已有层级关系的文字描述——图是可视化补充）
    - ch01_introduction.tex:350-368（第1章 fig:book-structure 的框图风格参考——使用了 `box/.style`, `fill=...!10`）
    - preamble.tex:18（tikz 宏包已加载）
  Acceptance criteria (agent-executable):
    1. 若执行：`grep -c "fig:concept-hierarchy" chapters/ch02_framework.tex` 返回 ≥1
    2. 图块包含 4 个 `\node[draw, ...]` 元素，对应四个概念
    3. 图块包含箭头连接（`\draw[-Stealth]` 或等效）
    4. 若跳过：在此 todo 状态标记为 `cancelled` 并在最终 commit message 中注明
  QA scenarios (name the exact tool + invocation):
    - Happy: `xelatex main.tex` → 编译无 error，产物 main.pdf 中可见层级框图
    - Failure: 忘记 `\usetikzlibrary{positioning}` → 编译报 "I do not know the key '/tikz/below'"
    Evidence: `.omo/evidence/add-figures-ch02-sec1/task-3-concept-hierarchy.log`
  Commit: Y | feat(ch02): add four-concept hierarchy diagram (or cancelled if density sufficient)

- [x] 4. 更新正文中的交叉引用：为每幅新图添加 `\ref{}` 调用
  What to do / Must NOT do:
    - 在 ch02_framework.tex 中，为每幅新增插图在正文中添加图号引用句：
    - **图A（fig:bond-kinematics）**：在 2.1.2 节中，约在 s 定义之后、对力函数之前（第 24–25 行区域），图 `\begin{figure}` 块之前插入引导句。例如："键的几何关系与运动学量如图\ref{fig:bond-kinematics}所示：参考构型中两物质点的相对位置由\boldsymbol{\xi}确定，变形后的当前构型中该量变为\boldsymbol{\xi}+\boldsymbol{\eta}，键的伸长根据s=(|\boldsymbol{\xi}+\boldsymbol{\eta}|-|\boldsymbol{\xi}|)/|\boldsymbol{\xi}|计算。"
    - **图B（fig:boundary-truncation）**：在 2.1.4 节中，约在族定义之后（第 56 行 `\cite{...}` 之后），图块之前插入引导句。例如："图\ref{fig:boundary-truncation}对比了内部物质点与边界附近物质点在近场域与族上的差异：边界附近的物质点其近场域被物体边界截断，族不完整，导致有效刚度与内部物质点存在差异。"
    - **图D（fig:concept-hierarchy）**（若执行）：在注记之前或之后，图块之前插入引导句。例如："四个概念之间的层级递进关系可参见图\ref{fig:concept-hierarchy}。"
    - **关键约束**：每次 `\ref{}` 调用必须在其对应 `\label{}` 之前（LaTeX 交叉引用规则——`\ref` 可以在 `\label` 之前，但需编译两遍才能解析。最优实践：引导句在图块之前，图块中的 `\label` 在 `\caption` 之内或之后，编译器第二次运行即可解析）
    - 不修改任何已有 `\ref{fig:family-horizon}` 调用（第 58 行）
    - 不修改任何已有 `\eqref{}` 调用
    - 引用句用中文，专业术语用英文（遵循全书风格）
    - 章节引用用手写（如"第2章"），图引用用 `\ref{}`
  Parallelization: Wave 1 | Blocked by: 1,2,3 | Blocks: 5
  References (executor has NO interview context - be exhaustive):
    - ch02_framework.tex:58（现有 `\ref{fig:family-horizon}` 用法模板："图\ref{fig:family-horizon}综合展示了..."）
    - ch01_introduction.tex:27,61,109,143 等（第1章多处 `\ref{}` 引导句式模板）
    - 全书规范（AGENTS.md）: "图、表、公式用 `\ref`/`\eqref`；章节引用全书用手写"
  Acceptance criteria (agent-executable):
    1. `grep -c "\\\\ref{fig:bond-kinematics}" chapters/ch02_framework.tex` 返回 ≥1（注：命令行中需转义反斜杠，实际在文件中为 `\ref{fig:bond-kinematics}`）
    2. `grep -c "\\\\ref{fig:boundary-truncation}" chapters/ch02_framework.tex` 返回 ≥1
    3. 若图D已插入：`grep -c "\\\\ref{fig:concept-hierarchy}" chapters/ch02_framework.tex` 返回 ≥1
    4. 每个 `\ref{}` 调用出现在对应 `\label{}` 之前（读文件验证顺序）
  QA scenarios (name the exact tool + invocation):
    - Happy: `xelatex main.tex` ×2 → 所有 `\ref{fig:...}` 解析为正确编号（如 2.2, 2.3, 2.4），无 "Reference … undefined" 警告
    - Failure: 缺少引用句 → `grep` 计数为 0
    Evidence: `.omo/evidence/add-figures-ch02-sec1/task-4-crossrefs.log`
  Commit: Y | docs(ch02): add cross-reference text for new figures in section 2.1

- [x] 5. 编译验证：XeLaTeX 完整编译无错误
  What to do / Must NOT do:
    - 在 Todo 1–4 全部完成后，执行完整编译：
      ```
      xelatex main.tex
      xelatex main.tex
      ```
    - 第二次 xelatex 生成正确的交叉引用编号
    - **不需要运行 bibtex**（若未新增 bib 引用则不需要；但图B引用了 LeBobaru2018 和 Mitchell2015，这些引用已在 bibliography.bib 中且在第1章等已有使用，bib 条目不变则不需要重新 bibtex）
    - 检查编译输出：
      1. 无 `!` 开头的 LaTeX Error
      2. 无 `Warning: Reference ... undefined`（交叉引用未解析——运行第二遍 xelatex 后应消失）
      3. 无 `Warning: Citation ... undefined`（文献引用未找到）
    - 记录产物 `main.pdf` 的页数作为基线
    - **不提交编译临时文件**（.aux, .log, .toc, .out, .synctex.gz 等）
    - 编译产物 main.pdf 不提交（已在 .gitignore 或项目约定中）
  Parallelization: Wave 2 | Blocked by: 4 | Blocks: —
  References (executor has NO interview context - be exhaustive):
    - 项目 AGENTS.md: "编译：必须用 XeLaTeX（ctexbook + 中文内容，pdflatex 会失败）。TeX 发行版：MiKTeX 26.5"
    - main.tex: 入口文件，仅含 `\input` 语句
    - ch02_framework.tex: 目标编辑文件
  Acceptance criteria (agent-executable):
    1. xelatex 第一遍：退出码 0，无 Fatal Error
    2. xelatex 第二遍：退出码 0
    3. `grep -c "undefined" main.log` → 0（或仅非关键 undefined）
    4. `grep "Warning" main.log` → 无 "Reference" 或 "Citation" 相关的 Warning
    5. main.pdf 存在且文件大小 > 0
  QA scenarios (name the exact tool + invocation):
    - Happy: 两次 `xelatex main.tex` 均返回 0，log 中无 undefined ref/citation → 通过
    - Failure: 故意制造未定义引用 → 预期编译通过但 log 中有 "undefined" warning → 检测到并失败
    Evidence: `.omo/evidence/add-figures-ch02-sec1/task-5-compile.log`, `main.log`（编译日志备份）
   Commit: Y (amend previous) | 或单独 commit: verify(ch02): confirm xelatex compilation after adding figures

- [x] 6. 修复图 A（fig:bond-kinematics）排版缺陷：消除符号重叠遮挡 + 子图名称移至图下方
  What to do / Must NOT do:
    - 仅修改 `ch02_framework.tex` 中 `fig:bond-kinematics` 对应的 `\begin{tikzpicture}...\end{tikzpicture}` 范围内的 TikZ 坐标和 node 位置
    - **问题 1 — 子图名称位置**：当前 （a）和（b）用 `\node[left] at (-1.5,...)` 放在左侧（行 39、52），改为 `\node at (x_center, y_below)` 居中于各子图下方
    - **问题 2 — 符号重叠遮挡**：变形构型子图与三态示意区间距不足。η 公式在 y=-4.1，三态标签从 y=-4.8 起，渲染时重叠。需加大两段间距。
    - **具体坐标修正**（整个 tikzpicture 替换为下方版本）：
      - 上部面板保持坐标不变，(a) 标签移至 `\node at (1.1,-0.6) {（a）参考构型};`
      - 下部面板整体下移约 0.8 单位：参考虚线 (0,-4.0)→(2.4,-3.4)，变形点 (0.3,-4.2)→(3.0,-3.0)，红键 (0.3,-4.2)→(3.0,-3.0)，灰虚线 ξ (0.3,-4.2)→(2.7,-3.6)，蓝箭头 η (2.7,-3.6)→(3.0,-3.0)
      - 所有面板内标签同步偏移：ξ+η 标签 at (1.65,-3.6)、ξ 标签 at (1.5,-3.9)、η 标签 at (2.85,-3.3)
      - η 公式移至 `\node[blue] at (1.65,-4.8)`，(b) 标签移至 `\node at (1.65,-5.4) {（b）变形构型};`
      - 三态示意整体下移至 y=-6.2：所有 gray dashed 线段、red/blue 线段 y=-6.2，above/below 标签 y=-6.2/-6.48
      - **所有 `[above]`/`[below]` 改为 `[above=4pt]`/`[below=4pt]` 增加标签与线条间距**（上部面板两处 + 下部面板 ξ 和 η 标签）；三态标签用 `[above=2pt]`/`[below=2pt]`（此处标签更密）
      - 不改变 caption、label、颜色约定、线条粗细、节点大小；不新增/删除任何几何元素
    - 不修改其他文件，不引入新宏包
  Parallelization: Wave 1 | Blocked by: — | Blocks: F5
  References (executor has NO interview context - be exhaustive):
    - `ch02_framework.tex` 行 32–72：图 A 当前 TikZ 代码（含坐标和标签位置）
    - 完整替换 TikZ 代码见下方
  Acceptance criteria (agent-executable):
    1. xelatex ×2 编译通过（exit 0），无 new error/warning
    2. main.pdf 中图 2.1 渲染：(a) 和 (b) 标签在各子图正下方居中，非左侧
    3. η 公式与三态标签之间无文字重叠
    4. ξ 和 |ξ| 标签与键线之间有清晰间距（≥4pt）
  QA scenarios (name the exact tool + invocation):
    - Happy: xelatex ×2 → PDF 打开第 16 页，目视确认（a）（b）在子图下方、无重叠
    - Failure: 未修改坐标 → （a）（b）仍在左侧 → grep 确认 node 位置已变
    Evidence: `.omo/evidence/add-figures-ch02-sec1/task-6-fix-overlap.md`
  Commit: Y | fix(ch02): fix symbol overlap and relocate subfigure labels in fig:bond-kinematics

## Final verification wave
> Runs in parallel after ALL todos. ALL must APPROVE. Surface results and wait for the user's explicit okay before declaring complete.
- [x] F1. Plan compliance audit: 对比最终 ch02_framework.tex 与 Scope（Must have 和 Must NOT have 全部满足？是否有溢出修改？）。用 `git diff` 确认仅 ch02_framework.tex 被修改。
- [x] F2. 插图质量审查: 所有新增插图（1）TikZ 绘制，非截图/外部图片；（2）图注 labelsep=quad 格式；（3）中文标注为主、专业术语英文；（4）线条/字体清晰可读。
- [x] F3. 编译产物验证: main.pdf 中按页查找新插图，确认编号顺序正确（2.1→2.2→2.3...），图中文字无乱码、无越界。
- [x] F4. Scope fidelity: 确认 main.tex、preamble.tex、frontmatter/notation.tex、bibliography.bib 未被修改；无新增 figures/ 文件；现有 fig:family-horizon 未变。
- [x] F5. 修复后质量审查：xelatex ×2 编译通过，main.pdf 中图 2.1 的 (a)(b) 标签在子图正下方居中，η 公式与三态标签无重叠，ξ/|ξ| 标签与键线间距 ≥4pt。用 multimodal-looker 目视确认。

## Commit strategy
- 单个 commit（全部 Todo 1–5 完成后）：
  ```
  feat(ch02): add 3 TikZ teaching figures to section 2.1 (bond kinematics, boundary truncation, concept hierarchy)

  - Fig 2.2: bond kinematics (reference vs deformed config with stretch states)
  - Fig 2.3: boundary truncation and incomplete family for surface effect
  - Fig 2.4: four-concept hierarchy diagram
  - All figures inline TikZ, no external images or new dependencies
  - Cross-references added in text body
  - Verified: xelatex ×2 clean, no undefined refs
  ```
- 若图D被跳过（cancelled），commit message 中移除对应行

## Success criteria
1. `ch02_framework.tex` 第2.1节含 3–4 幅插图的完整 figure 块（含 TikZ 代码、caption、label）
2. 正文中每幅新图有 `\ref{}` 引用
3. `xelatex main.tex` ×2 无编译错误、无 undefined reference/citation 警告
4. 所有 Scope OUT 项未被触碰
5. main.pdf 中新插图渲染正确、编号连续
