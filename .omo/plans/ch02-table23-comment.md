# ch02-table23-comment - Work Plan

## TL;DR (For humans)
在《近场动力学理论与数值方法》第 2 章 2.3.3 节中，量纲分析表 2.3 之后缺少对表内内容的文字说明，读者看完表格无法立刻把握"N/m³ 与 N/m⁶ 两组量纲、积分后降维回到 N/m³"这一核心对比。本计划在表格与后文之间插入一段约三行的说明文字，点明表中两组量纲及"积分降维"机制，使表格真正成为正文的延伸。

**What you'll get:** 表 2.3 后新增一段说明文字，消除表格与正文之间的断层。

**Why this approach:** 单文件单处插入，不触碰公式编号与引用；说明段聚焦表内对比，"与经典应力的深入对比"留给后文，避免重复。

**What it will NOT do:** 不修改表 2.3 内容、不修改其他章节/文件、不改变任何公式编号或引用。

**Effort:** Quick
**Risk:** Low - 纯文本插入，无公式改动
**Decisions to sanity-check:** 说明段文本是否准确转述了表内量纲关系（N/m³ vs N/m⁶、积分后回 N/m³）

Your next move: 启动执行（$start-work）。

---

> TL;DR (machine): Quick effort, Low risk, 单文件插入说明段 + 编译验证

## Scope
### Must have
- `chapters/ch02_framework.tex`：表 2.3（`\end{table}` 之后、673 行"量纲推导给出了…"段之前）插入定稿说明段，独立成段（前后空行）
- 说明段包含两个核心信息：(a) 惯性项/体力为 N/m³ 力密度 vs 对力为 N/m⁶；(b) 积分后回到 N/m³，与左端一致，体现方程结构自洽
### Must NOT have (guardrails, anti-slop, scope boundaries)
- 不修改 main.tex、preamble.tex 或任何其他文件
- 不修改表 2.3 本身（行、列、caption、label 均不动）
- 不修改 673 行及以后任何段落
- 不改变任何公式编号、\label、\eqref、\cite
- 不运行 xelatex 编译（编译验证由编排者本地执行，AGENTS.md 规定）
- 不自动 commit/push

## Verification strategy
> Zero human intervention - all verification is agent-executed.
- Test decision: none（LaTeX 文本插入，无单元测试框架）+ 编译门禁
- Evidence: .omo/evidence/ 下记录编译输出与阅读结论；编译命令 `xelatex -interaction=nonstopmode -halt-on-error main.tex`（快速失败）+ 完整流程 `xelatex; bibtex; xelatex; xelatex`，检查 main.log undefined=0、`Output written on main.pdf`

## Execution strategy
### Parallel execution waves
- Wave 1: 唯一实现任务（单文件单处插入）

### Dependency matrix
| Todo | Depends on | Blocks | Can parallelize with |
| --- | --- | --- | --- |
| 1 | 无 | F1, F2 | 无 |

## Todos
> Implementation + Test = ONE todo. Never separate.
<!-- APPEND TASK BATCHES BELOW THIS LINE WITH edit/apply_patch - never rewrite the headers above. -->
- [x] 1. 在 ch02_framework.tex 表 2.3 后插入说明段并编译验证
  What to do / Must NOT do: 在 `\end{table}`（671 行）之后、673 行"量纲推导给出了…"段之前插入以下定稿段落（逐字插入，不得改动措辞）：
  ```
  表~\ref{tab:dim-analysis} 显示，惯性项与体力均为 $\mathrm{N}/\mathrm{m}^{3}$ 的力密度，而对力函数 $\mathbf{f}$ 的量纲为 $\mathrm{N}/\mathrm{m}^{6}$，高出一个体积维度；经积分 $\int\mathbf{f}\,\mathrm{d}V'$ 后又回到 $\mathrm{N}/\mathrm{m}^{3}$，与左端惯性项一致。这一升一降正是运动方程结构自洽的体现。
  ```
  段落前后保留空行、独立成段。不得修改任何其他内容。
  Parallelization: Wave 1 | Blocked by: 无 | Blocks: F1, F2
  References (executor has NO interview context - be exhaustive): chapters/ch02_framework.tex:657（表前引导句）、:661-671（表 2.3）、:673（表后段落起点）
  Acceptance criteria (agent-executable): 插入段位于 `\end{table}` 与"量纲推导给出了"之间，文本逐字匹配定稿，公式编号/引用未变
  QA scenarios (name the exact tool + invocation): happy - 编排者本地执行 `xelatex -interaction=nonstopmode -halt-on-error main.tex` 无 error；failure - 若编译失败检查 unmatched brace/换行符丢失。Evidence .omo/evidence/ch02-table23-comment-compile.log
  Commit: N（AGENTS.md 禁止自动 commit，且工作区含用户未提交的其他改动）

## Final verification wave
> Runs in parallel after ALL todos. ALL must APPROVE. Surface results and wait for the user's explicit okay before declaring complete.
- [x] F1. 编译通过：`xelatex main.tex` 无 error（含参考文献完整流程），main.log undefined=0
- [x] F2. 逻辑连贯：阅读 2.3.3 节，确认说明段承接表 2.3 并与前后文衔接自然、无重复

## Commit strategy
单文件单 commit：`chapters/ch02_framework.tex`（仅当用户确认后手动执行）

## Success criteria
- `xelatex main.tex` 编译无 error、main.log undefined=0
- 表 2.3 后说明段存在且与前后文衔接自然，表格不再孤立
