# remove-fig26-family-horizon - Work Plan

## TL;DR (For humans)
<!-- Fill this LAST, after the detailed plan below is written, so it summarizes the REAL plan. -->
<!-- Plain English for a non-engineer: NO file paths, NO todo numbers, NO wave/agent/tool names. -->

**What you'll get:** 删除第2章中与第1章图1.4重复的图2.6（fig:family-horizon），改写正文引用为指向第1章图1.4与第2章图2.5，消除重复插图，全书更紧凑。

**Why this approach:** 图2.6与第1章图1.4（fig:horizon-bond）视觉内容相似度超90%，唯一增量是族标签 $\mathcal{F}_{\mathbf{x}}$；族概念已由图2.5（fig:boundary-truncation）支撑，故删除图2.6并将"族"的说明并入引用改写，不损失信息。

**What it will NOT do:** 不修改图2.5（boundary-truncation）；不删除族的定义式（eq:family，192行）；不动第1章内容；不新增任何图。

**Effort:** Quick
**Risk:** Low - 单文件局部删除，引用改写后无悬空 label；编译门禁可验证
**Decisions to sanity-check:** 正文改写后的表述是否自然承接"族"概念（238行段落措辞）

Your next move: 运行 `$start-work` 执行本 plan。执行细节见下。

---

> TL;DR (machine): Quick | Low | 删除 ch02 图2.6（fig:family-horizon）+ 改写 238 行引用 + xelatex 编译验证

## Scope
### Must have
- 删除 `chapters/ch02_framework.tex` 中第 240–270 行的图2.6（`\begin{figure}`…`\end{figure}` 的 `fig:family-horizon` 环境），含 `\label{fig:family-horizon}`（269 行）
- 改写第 238 行正文段落：去掉 `图\ref{fig:family-horizon}综合展示了…` 的表述，改为引用第 1 章图1.4（`fig:horizon-bond`）承接"物质点、键、近场域"的几何关系，并引用图2.5（`fig:boundary-truncation`）说明"族"的完整性受边界截断影响
- 确保删除后全库无 `fig:family-horizon` 残留引用（现仅 238 行 + 269 行两处，均需处理）
- xelatex 两遍编译通过：`xelatex -interaction=nonstopmode -halt-on-error main.tex` 过滤 `Error|undefined` 零命中；图 2.6 之后的图编号自动前移（原图2.7+ 变 2.6+），`main.aux` 中相应 `\newlabel` 同步更新
### Must NOT have (guardrails, anti-slop, scope boundaries)
- 不删除第 1 章 `fig:horizon-bond`（图1.4）
- 不删除第 2 章 `fig:boundary-truncation`（图2.5）及其正文引用（194 行）
- 不删除族定义式 `eq:family`（192 行）及 194 行正文
- 不修改 `main.tex`、`preamble.tex`、其它章节文件
- 不 commit、不 push（人工负责 git 操作）

## Verification strategy
> Zero human intervention - all verification is agent-executed.
- Test decision: none（LaTeX 排版项目无单元测试；以编译门禁为验证手段）
- Evidence: `.omo/evidence/task-1-remove-fig26-family-horizon.log`（xelatex 输出）
- 门禁命令：`xelatex -interaction=nonstopmode -halt-on-error main.tex` 连续两遍，随后 grep log 过滤 `Error|undefined` 应零命中；`main.aux` 中无 `fig:family-horizon` 且图 2.6 变为 `fig:force-stretch`（原图2.7）
- 引用完整性：`grep -rn "fig:family-horizon" chapters/` 应零命中

## Execution strategy
### Parallel execution waves
- Wave 1: Todo 1（单 todo，无并行）

### Dependency matrix
| Todo | Depends on | Blocks | Can parallelize with |
| --- | --- | --- | --- |
| 1 | 无 | 无 | 无（唯一 todo） |

## Todos
> Implementation + Test = ONE todo. Never separate.
<!-- APPEND TASK BATCHES BELOW THIS LINE WITH edit/apply_patch - never rewrite the headers above. -->
- [x] 1. 删除图2.6（fig:family-horizon）并改写正文引用，编译验证通过
  What to do / Must NOT do:
  - 在 `chapters/ch02_framework.tex` 中删除第 240–270 行完整 figure 环境（`\begin{figure}[htbp]`…`\end{figure}`，含 `\label{fig:family-horizon}`），保留 238 行段落与 271 行空行结构
  - 改写第 238 行正文：原文以"图\ref{fig:family-horizon}综合展示了物质点、键、近场域与族四个基本概念…"开头；改为引用第 1 章图1.4（`fig:horizon-bond`）承接物质点/键/近场域几何关系（可用"已在第 1 章图\ref{fig:horizon-bond}中给出"），并点明"族 $\mathcal{F}_{\mathbf{x}}$ 为近场域内与 $\mathbf{x}$ 通过键相连的物质点集合"，衔接引用图2.5（`fig:boundary-truncation`）说明边界物质点族不完整。注意：章节引用全书手写（"第 1 章"），图引用用 `\ref`，禁用 `\autoref`
  - 删除后全库 `grep "fig:family-horizon"` 应零命中（含 chapters/ 与 main.aux 在下一次编译后消失）
  - 不得改动第 1 章 `fig:horizon-bond`、第 2 章 `fig:boundary-truncation`、`eq:family`、`main.tex`、`preamble.tex` 及任何其它章节
  Parallelization: Wave 1 | Blocked by: 无 | Blocks: 无
  References (executor has NO interview context - be exhaustive):
  - `chapters/ch02_framework.tex:238`（待改写正文）
  - `chapters/ch02_framework.tex:240-270`（待删除图环境）
  - `chapters/ch02_framework.tex:194`（族与近场域关系、图2.5引用，改写时保持一致口径）
  - `chapters/ch01_introduction.tex:117-146`（fig:horizon-bond 即图1.4，改写引用对象）
  - 项目规范：`AGENTS.md`（XeLaTeX 编译门禁、章节引用手写、图注无冒号、`xshift` 带单位等）
  Acceptance criteria (agent-executable):
  - `Select-String -Path chapters\ch02_framework.tex -Pattern "family-horizon"` 零命中
  - 编译门禁：`xelatex -interaction=nonstopmode -halt-on-error main.tex` 连续两遍，过滤 `Error|undefined` 零命中；`main.aux` 中无 `fig:family-horizon`
  - `main.aux` 中图编号连续（`fig:force-stretch` 变图 2.6，`fig:boundary-force-conversion` 变图 2.7）
  QA scenarios (name the exact tool + invocation):
  - happy: PowerShell 依次执行两遍 xelatex 后 grep log；再 grep `fig:family-horizon` 确认零命中；Evidence `.omo/evidence/task-1-remove-fig26-family-horizon.log`
  - failure: 若 log 出现 `Reference ... undefined` 或 `fig:family-horizon` 残留，回查 238 行改写是否遗漏引用删除
  Commit: N（人工负责 git）

## Final verification wave
> Runs in parallel after ALL todos. ALL must APPROVE. Surface results and wait for the user's explicit okay before declaring complete.
- [x] F1. Plan compliance audit
- [x] F2. Code quality review
- [x] F3. Real manual QA
- [x] F4. Scope fidelity

## Commit strategy
- 不自动 commit/push。执行完成后由人工审阅 `git status`/`git diff` 后自行提交（项目 AGENTS.md 明确约定）。

## Success criteria
- `chapters/ch02_framework.tex` 中图2.6（fig:family-horizon）已删除，238 行正文已改写且表述通顺
- 全库无 `fig:family-horizon` 残留引用；编译两遍零 `Error|undefined` 警告
- 第1章图1.4、第2章图2.5、族定义式 eq:family 均保持原样
- 图编号自动前移，`main.aux` 交叉引用一致，无悬空 label
