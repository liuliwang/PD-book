# optimize-ch0231-central-force - Work Plan

## TL;DR (For humans)
优化 `chapters/ch02_framework.tex` 第 436-447 行（2.3.1 节）关于中心力条件式 (2.23) 的文字说明。当前文字从叉积条件直接跳到力的标量分解形式，缺少中间推导链条，导致研究生水平读者难以理解。计划在现有文字中插入一段补充推导：从叉积为零说明两向量平行，进而引入比例系数 λ，最后归一化得到标准形式。不涉及公式变更，仅增加中间步骤的文字说明。

## Scope
- **修改范围**：`chapters/ch02_framework.tex` 第 436-447 行（2.3.1 节"对力函数的物理意义"中，从中心力条件方程到 `式\eqref{eq:central-force-form}` 之间的文字段落）
- **修改类型**：纯文字改写，不涉及公式编号变更、不新增公式、不改引用
- **In scope**：
  - 在 `(\boldsymbol{\xi}+\boldsymbol{\eta})\times\mathbf{f}(\boldsymbol{\eta},\boldsymbol{\xi})=\mathbf{0}`（第 438 行，无 label）之后、`从几何角度看`（第 442 行）之前，插入一段补充推导文字
  - 推导链：叉积为零 → 两向量共线 → 存在标量 λ 使 f = λ(ξ+η) → 令 λ = g/|ξ+η| 得到标准形式
  - 插入文字量：不超过 4-5 行正文（约 100-150 字）
  - 保留图 2.5（`fig:central-force`）的引用和文字
  - 保持与 2.6 节角动量守恒定理的衔接
- **Must-NOT-Have**：
  - 新增 `\begin{equation}` 环境（避免编号错位）
  - 修改现有 `equation`、`figure` 等环境
  - 新增章节或子节
  - 改动第 436 行之前和第 448 行之后的内容（即不改动 `\begin{figure}[htbp]` 及之后内容）
  - 引入未在 `frontmatter/notation.tex` 登记的新符号（允许用自然语言描述"比例系数"而不引入 λ）

## Verification strategy
- **Agent-executed QA**：
  - **结构验证**：grep `ch02_framework.tex` 中关键词（"共线"、"平行"、"比例系数"），确认出现位置在 `(\boldsymbol{\xi}+\boldsymbol{\eta})\times\mathbf{f}` 之后、`从几何角度看` 之前
  - **编号验证**：修改前后分别运行 `grep -c 'label{' ch02_framework.tex`，确认 `\label` 数量不变；确认未新增 `\begin{equation}` 环境
  - **引用完整性验证**：grep 确认以下引用未被破坏：
    - `eq:central-force-form`（第 445 行，2.3.1 节引用）
    - `eq:central-force`（第 ~142 行，2.1 节引用）
    - `fig:central-force`（第 449 行，2.3.1 节引用）
  - **编译验证**：按 AGENTS.md 规定的 PowerShell 命令序列执行：
    ```powershell
    xelatex main.tex
    bibtex main
    xelatex main.tex
    xelatex main.tex
    ```
    确认输出中无 error、无 undefined reference/citation 警告
- **Happy path**：xelatex 编译通过，PDF 中 2.3.1 节出现补充推导段落
- **Failure path**：编译报错 → 检查是否有未闭合环境或非法字符；公式号错位 → 检查是否误增了 `\label`

## Execution strategy
单步修改：定位 `chapters/ch02_framework.tex`，在中心力条件方程（第 438 行，无 label）之后的段落与 `从几何角度看`（第 442 行）之间，插入一段补充推导文字。插入位置的精确锚点：`该条件要求对力方向与变形后键的方向 \boldsymbol{\xi}+\boldsymbol{\eta} 共线`（第 440 行）之后、`从几何角度看`（第 442 行）之前。

插入文字的参考内容（不超过 4-5 行）：
```
从向量代数可知，两个非零向量的叉积为零当且仅当它们平行（共线）。因此中心力条件 \eqref{eq:central-force} 意味着对力矢量 \mathbf{f} 与变形后的键矢量 \boldsymbol{\xi}+\boldsymbol{\eta} 平行，即存在某个标量函数使得 \mathbf{f} 可写成该方向上的力。将这一方向用单位矢量 \frac{\boldsymbol{\xi}+\boldsymbol{\eta}}{|\boldsymbol{\xi}+\boldsymbol{\eta}|} 表示，则对力可分解为该方向与力大小的乘积。
```

## Todos
- [x] 1. 阅读目标文件确认当前内容和插入位置：读取 `chapters/ch02_framework.tex` 第 430-450 行，确认 `该条件要求对力方向与变形后键的方向 \boldsymbol{\xi}+\boldsymbol{\eta} 共线`（第 440 行）和 `从几何角度看`（第 442 行）的位置
- [x] 2. 在 `chapters/ch02_framework.tex` 第 441 行（即第 440 行之后）插入补充推导段落：从叉积为零 → 两向量共线 → 存在标量使得 f 可写为该方向上的力 → 归一化得到式 \eqref{eq:central-force-form} 的标准形式；插入文字不超过 4-5 行
- [x] 3. 运行结构验证：grep 确认插入文字包含"共线""平行""标量"等关键词，且位于 `(\boldsymbol{\xi}+\boldsymbol{\eta})\times\mathbf{f}` 和 `从几何角度看` 之间
- [x] 4. 运行编号验证：`grep -c 'label{' ch02_framework.tex` 修改前后对比，确认未新增 `\label`；`grep -c 'begin{equation}' ch02_framework.tex` 确认未新增 `\begin{equation}`
- [x] 5. 编译验证：按以下 PowerShell 命令顺序执行并确认无 error/无 undefined reference/citation：
  ```powershell
  xelatex main.tex
  bibtex main
  xelatex main.tex
  xelatex main.tex
  ```
- [x] 6. 引用完整性检查：grep 确认 `eq:central-force-form`、`eq:central-force`、`fig:central-force` 仍被正确引用，未因行号变化而断裂

## Final verification wave
- [x] F1. 结构审计：grep 确认新增推导文字包含"共线""平行""标量"，且位于 `(\boldsymbol{\xi}+\boldsymbol{\eta})\times\mathbf{f}` 之后、`从几何角度看` 之前
- [x] F2. 编号审计：确认 `\label` 总数不变、`\begin{equation}` 环境数不变、未新增公式编号
- [x] F3. 编译质量：xelatex 编译无 error，无 undefined reference/citation 警告
- [x] F4. 引用完整性：确认 `eq:central-force-form`（第 445 行）、`eq:central-force`（第 ~142 行）、`fig:central-force`（第 449 行）的引用未被破坏
- [x] F5. 范围合规：确认未改动 `(\boldsymbol{\xi}+\boldsymbol{\eta})\times\mathbf{f}` 之前和 `\end{figure}`（图 2.5）之后的任何行

## Commit strategy
- Stage 仅 `chapters/ch02_framework.tex`
- 提交消息：`docs(ch02): 补充 2.3.1 节中心力条件推导链条`
- 不提交编译产物
- AI 写作约束：新增文字为 AI 辅助生成，须提交前经作者人工复核；须通过 AI 自查清单（推导链完整、术语一致、无编造引用、因果链无跳跃）；避免引入未登记符号

## Success criteria
- xelatex 编译通过，无 error
- 2.3.1 节出现从叉积为零到式 (2.23) 的完整推导说明
- 未新增公式编号
- 未破坏前后文引用和衔接
