# fix-bond-stretch-definition - Work Plan

## TL;DR (For humans)
<!-- Fill this LAST, after the detailed plan below is written, so it summarizes the REAL plan. -->
<!-- Plain English for a non-engineer: NO file paths, NO todo numbers, NO wave/agent/tool names. -->

**What you'll get:** 第 2 章 2.1.2 节中键伸长率 $s$ 的定义从行内文本升级为带编号的公式，可被全书精确交叉引用；术语从"键的伸长"统一为"键的伸长率"，与符号表和其他章节一致。

**Why this approach:** $s$ 是全书最高频运动学量，但定义无编号——同页的反作用条件和中心力条件均有编号，$s$ 不应例外。同时修复定义外的两处连带问题（行内冗余重复、图注术语不一致）。

**What it will NOT do:** 不修改符号表、2.7 节、其他章节、数学定义内容、或任何 TikZ 插图布局。

**Effort:** Quick（单文件，2 处 edit）
**Risk:** Low — 仅文本替换和公式编号化，不涉及内容变更
**Decisions to sanity-check:** `eq:bond-stretch` 标签名不与现有 48 个标签冲突（已验证）；"伸长 → 伸长率"的范围仅限 2.1.2 节（2.2 节标题"键伸长的客观性"待后续独立处理）。

Your next move: approve, then run via `/start-work fix-bond-stretch-definition`. Full execution detail follows below.

---

> TL;DR (machine): Quick, Low, 单文件 2 处 LaTeX 文本/公式编辑 + 1 次 xelatex 编译验证

## Scope
### Must have
- `ch02_framework.tex` 第 73 行：行内 `$s=...$` 变为 `\begin{equation}...\label{eq:bond-stretch}`，术语"伸长"→"伸长率"
- `ch02_framework.tex` 第 73 行（同一段）：删除行尾 `键的伸长根据 $s=...$ 计算`，改为 `伸长率由式\eqref{eq:bond-stretch}给出`
- `ch02_framework.tex` 第 119 行：图注中"键伸长定义为 $s=...$"→"键伸长率 $s$ 由式\eqref{eq:bond-stretch}定义"
- xelatex ×2 编译通过，无 error，无 `eq:bond-stretch` 未定义警告

### Must NOT have (guardrails, anti-slop, scope boundaries)
- 不修改 `notation.tex`（已正确使用"伸长率"）
- 不修改 2.7 节（已正确使用"伸长率"）
- 不修改 2.2 节标题"键伸长的客观性"（不在本次范围）
- 不修改 `main.tex`、`preamble.tex`、`bibliography.bib`
- 不增减任何数学定义的内容
- 不新增或修改 TikZ 图

## Verification strategy
> Zero human intervention - all verification is agent-executed.
- Test decision: tests-after（编译 + grep 验证）
- Evidence: `.omo/evidence/fix-bond-stretch-definition/`

## Execution strategy
### Parallel execution waves
单波（Wave 1）：2 个编辑任务可并行，然后编译验证。总共 3 个任务。

### Dependency matrix
| Todo | Depends on | Blocks | Can parallelize with |
| --- | --- | --- | --- |
| 1 | — | 3 | 2 |
| 2 | — | 3 | 1 |
| 3 | 1, 2 | — | — |

## Todos
> Implementation + Test = ONE todo. Never separate.
<!-- APPEND TASK BATCHES BELOW THIS LINE WITH edit/apply_patch - never rewrite the headers above. -->

- [x] 1. 将第 73 行行内公式升级为编号公式 + 替换行尾冗余重复
  What to do / Must NOT do:
    - 将第 73 行从：
      ```
      于是键的当前长度为 $|\boldsymbol{\xi}+\boldsymbol{\eta}|$，参考长度为 $|\boldsymbol{\xi}|$。键的伸长（stretch）定义为 $s=(|\boldsymbol{\xi}+\boldsymbol{\eta}|-|\boldsymbol{\xi}|)/|\boldsymbol{\xi}|$，其推导已在第 1 章 1.4 节给出，此处不再重复。键的几何关系与运动学量如图\ref{fig:bond-kinematics}所示：参考构型中两物质点的相对位置由 $\boldsymbol{\xi}$ 确定，变形后的当前构型中该量变为 $\boldsymbol{\xi}+\boldsymbol{\eta}$，键的伸长根据 $s=(|\boldsymbol{\xi}+\boldsymbol{\eta}|-|\boldsymbol{\xi}|)/|\boldsymbol{\xi}|$ 计算。
      ```
      替换为：
      ```
      于是键的当前长度为 $|\boldsymbol{\xi}+\boldsymbol{\eta}|$，参考长度为 $|\boldsymbol{\xi}|$。键的伸长率（bond stretch）定义为
      \begin{equation}
        s = \frac{|\boldsymbol{\xi} + \boldsymbol{\eta}| - |\boldsymbol{\xi}|}{|\boldsymbol{\xi}|}
        \label{eq:bond-stretch}
      \end{equation}
      其推导已在第 1 章 1.4 节给出，此处不再重复。键的几何关系与运动学量如图\ref{fig:bond-kinematics}所示：参考构型中两物质点的相对位置由 $\boldsymbol{\xi}$ 确定，变形后的当前构型中该量变为 $\boldsymbol{\xi}+\boldsymbol{\eta}$，伸长率由式\eqref{eq:bond-stretch}给出。
      ```
      不可仅删除公式片段而保留"根据计算"，否则产生语法破损。
      不可修改数学定义本身（公式等价，仅从行内数学模式转到显示模式）。
      不可改动 `\ref{fig:bond-kinematics}` 引用。
    - 文件不可在第 73 行以外产生任何变更
  Parallelization: Wave 1 | Blocked by: — | Blocks: 3
  References (executor has NO interview context - be exhaustive):
    - `chapters/ch02_framework.tex:73` — 当前内容（上为精确原文）
    - `frontmatter/notation.tex:21` — 符号表已用"伸长率"
    - `chapters/ch02_framework.tex:644+` — 2.7 节已用"伸长率"
    - `chapters/ch02_framework.tex:124-132` — 同页 `eq:reaction` / `eq:central-force` 格式参考
  Acceptance criteria (agent-executable):
    - `grep -c '\\label{eq:bond-stretch}' chapters/ch02_framework.tex` → 输出 `1`
    - `grep -c '键的伸长（stretch）' chapters/ch02_framework.tex` → 输出 `0`
    - `grep -c '键的伸长根据.*\\$s=' chapters/ch02_framework.tex` → 输出 `0`（冗余重复已删除）
    - `grep -c '伸长率由式' chapters/ch02_framework.tex` → 输出 `1`
    - `grep 'eq:bond-stretch' chapters/ch02_framework.tex` → 应在 `\label` 行和 `\eqref` 行各出现一次
  QA scenarios (name the exact tool + invocation):
    - Happy: xelatex ×2 编译通过后，grep 验证上述所有条件均满足
    - Failure: 如果 `grep -c '键的伸长（stretch）'` 仍 > 0 → 替换不完整，需检查是否匹配正确完整字符串
    Evidence: `.omo/evidence/fix-bond-stretch-definition/task-1-qa.txt`
  Commit: Y | `fix(ch02): 键伸长率 s 升级为编号公式 eq:bond-stretch，术语统一为伸长率`

- [x] 2. 修正第 119 行图注术语 + 交叉引用
  What to do / Must NOT do:
    - 将第 119 行从：
      ```
        \caption{键的运动学：参考构型与变形构型中的键几何关系，键伸长定义为 $s=(|\boldsymbol{\xi}+\boldsymbol{\eta}|-|\boldsymbol{\xi}|)/|\boldsymbol{\xi}|$}
      ```
      替换为：
      ```
        \caption{键的运动学：参考构型与变形构型中的键几何关系，键伸长率 $s$ 由式\eqref{eq:bond-stretch}定义}
      ```
      不可改动"键的运动学"前缀（此处"键"为对象，非术语"键伸长"的一部分）。
      不可改动 `\label{fig:bond-kinematics}`。
  Parallelization: Wave 1 | Blocked by: — | Blocks: 3
  References:
    - `chapters/ch02_framework.tex:119` — 当前图注原文
    - `chapters/ch02_framework.tex:73` — 任务 1 中新建的 `\label{eq:bond-stretch}`（图注中 `\eqref{eq:bond-stretch}` 将解析到此编号）
  Acceptance criteria (agent-executable):
    - `grep -c '键伸长率 \$s\$ 由式' chapters/ch02_framework.tex` → 输出 `1`
    - `grep -c '键伸长定义为' chapters/ch02_framework.tex` → 输出 `0`
    - `grep -c '\\\\eqref{eq:bond-stretch}' chapters/ch02_framework.tex` → 输出 `1`（图注中）
  QA scenarios:
    - Happy: xelatex ×2 后，grep `main.aux` 确认 `\newlabel{eq:bond-stretch}` 存在且带 `{2.1}` 之类编号；PDF 中图 2.2 图注显示"键伸长率 s 由式(2.1)定义"（编号依实际编译结果）
    - Failure: 若 `\eqref{eq:bond-stretch}` 未定义 → 任务 1 的 `\label` 未成功写入，需要回溯
    Evidence: `.omo/evidence/fix-bond-stretch-definition/task-2-qa.txt`
  Commit: Y（与任务 1 合并提交）| `fix(ch02): 图注中键伸长率术语与交叉引用同步更新`

- [x] 3. 编译验证 + 交叉引用完整性检查
  What to do / Must NOT do:
    - 在 `D:\PD-book` 目录执行：
      ```powershell
      xelatex main.tex
      xelatex main.tex
      ```
      两遍编译确保交叉引用稳定。
    - 不可使用 pdflatex（中文 + ctexbook 会失败）
    - 检查编译输出：无 `LaTeX Error`，无 `undefined reference` 警告提及 `eq:bond-stretch`
    - 交叉引用验证：
      - `grep 'newlabel{eq:bond-stretch}' main.aux` → 应有输出（如 `\newlabel{eq:bond-stretch}{{2.1}{...}}`）
      - `grep '键伸长率' main.aux` → 在 `\newlabel{fig:bond-kinematics}` 条目中应出现新术语
      - `grep '键伸长定义为' main.aux` → 应无输出（旧术语已清除；注意排除旧 `.aux` 缓存——本任务编译两遍后会更新 `.aux`）
  Parallelization: Wave 1 | Blocked by: 1, 2 | Blocks: —
  References:
    - `project:AGENTS.md` — 编译命令规范
    - `main.aux` — xelatex 编译生成的交叉引用缓存文件
  Acceptance criteria (agent-executable):
    - xelatex 两次编译 exit code 均为 0
    - `grep -c 'undefined' main.log` 不包含 `eq:bond-stretch` 相关行
    - `grep 'newlabel{eq:bond-stretch}' main.aux` 有非空输出
  QA scenarios:
    - Happy: 两遍 xelatex 均无 error，PDF 生成成功，`main.aux` 含 `\newlabel{eq:bond-stretch}`
    - Failure（交叉引用断裂）: 若第一遍 xelatex 后有 `LaTeX Warning: Reference eq:bond-stretch undefined` → 第二遍应消除（正常 LaTeX 行为）；若第二遍仍存在 → `\label` 或 `\eqref` 拼写错误，需回溯任务 1/2
    Evidence: `.omo/evidence/fix-bond-stretch-definition/task-3-qa.txt`
  Commit: Y（与任务 1/2 合并为单个提交）| —（已在任务 1 中指定提交信息）

## Final verification wave
> Runs in parallel after ALL todos. ALL must APPROVE. Surface results and wait for the user's explicit okay before declaring complete.
- [x] F1. Plan compliance audit: 确认仅 `ch02_framework.tex` 被修改，无其他文件变更；`git diff --stat` 仅一行
- [x] F2. Code quality review: 确认 LaTeX 语法无错误，`\begin{equation}...\end{equation}` 正确闭合，`\label`/`\eqref` 标签一致
- [x] F3. Real manual QA: 打开 `main.pdf`，翻到 2.1.2 节确认：(a) 键伸长率公式为编号显示公式，(b) 图 2.2 图注显示"键伸长率 s 由式(2.X)定义"（X 为实际编号），(c) 正文中无残留"键的伸长（stretch）"
- [x] F4. Scope fidelity: `grep -c '键的伸长（stretch）' chapters/ch02_framework.tex` → 0；`grep -c '键的伸长根据' chapters/ch02_framework.tex` → 0；`grep -c '\\\\label{eq:bond-stretch}' chapters/ch02_framework.tex` → 1

## Commit strategy
- 单提交，类型 `fix(ch02)`：`fix(ch02): 键伸长率 s 升级为编号公式 eq:bond-stretch，术语统一为伸长率`
- 提交包含 `chapters/ch02_framework.tex` 的变更 + `.omo/evidence/` 下的 QA 证据文件（可选）

## Success criteria
1. `chapters/ch02_framework.tex` 中 `\label{eq:bond-stretch}` 存在且仅一处
2. 全文中"键的伸长（stretch）"替换为"键的伸长率（bond stretch）"（仅限 2.1.2 节范围）
3. 图注中旧公式被 `\eqref{eq:bond-stretch}` 替代
4. xelatex ×2 编译无错误，`eq:bond-stretch` 引用解析成功
5. 无语法破损（中文文本在公式删改后仍通顺）
