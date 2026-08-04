# adjust-fig24-hx-label - Work Plan

## TL;DR (For humans)

**What you'll get:** 第 2 章图 2.4（内部物质点与边界物质点的近场域对比）中，(a) 面板的 $H_{\mathbf{x}}$（完整）标签略微上移约 0.15 cm，使其与虚线圆弧的留白与 (b) 面板一致，消除标签几乎贴住圆弧的拥挤感。

**Why this approach:** 方案A：仅移动 (a) 标签 y 坐标（2.95 → 3.1）。保持 (b) 面板不变，因为 (b) 的截断弧最高点较低（约 y≈2.70），标签 (0.7,2.95) 已有足够留白；(a) 的完整圆弧最高点较高（y=2.9），原坐标 2.95 几乎贴弧，故单独上移 (a)。单行修改，风险最低，不触碰任何其他元素。

**What it will NOT do:** 不改动 (b) 面板标签；不改动子图标题（已在下方 y=-0.7）；不改动空心圆、虚线弧、图注、label 或其他任何行；不新增/删除物质点；不触碰其他章节文件。

**Effort:** Quick
**Risk:** Low - 单行坐标修改，仅影响一张图内一个标签的排版位置
**Decisions to sanity-check:** 新 y 坐标取 3.1（而非 3.05 或 3.15）：3.1 距弧顶 2.9 约 0.2 cm，与 (b) 面板 0.25 cm 留白视觉接近；3.1 仍低于矩形顶边 3.2 且不会与 $\mathcal{B}$ 标签（(4,3.2) above right）冲突。

Your next move: 执行工作流已完成用户授权（/start-work 触发，No-plan bootstrap 视其为批准），直接开始执行。

---

> TL;DR (machine): Quick / Low - 单行修改 ch02_framework.tex:205，坐标 (2,2.95)→(2,3.1)，xelatex 两遍编译零错误。

## Scope
### Must have
- 修改 `chapters/ch02_framework.tex` 第 205 行：`\node[above] at (2,2.95) {$H_{\mathbf{x}}$（完整）};` → `\node[above] at (2,3.1) {$H_{\mathbf{x}}$（完整）};`
- xelatex 两遍编译通过（exit 0），日志过滤 `^!|undefined|Warning: Reference|Warning: Citation` 零命中
- 唯一改动文件：`chapters/ch02_framework.tex`

### Must NOT have (guardrails, anti-slop, scope boundaries)
- 不得修改 (b) 面板第 228 行 `(0.7,2.95)` 标签
- 不得修改子图标题（第 215/235 行）、空心圆（224-226）、虚线弧、图注（238）、label（239）
- 不得改动 main.tex、preamble.tex、其他章节文件
- 不得引入任何新宏包/依赖
- 不得自动 git commit/push（人工负责提交）

## Verification strategy
> Zero human intervention - all verification is agent-executed.
- Test decision: none（LaTeX 排版修改，无单元测试框架；以编译门禁 + 几何校验替代）
- Evidence: `.omo/evidence/adjust-fig24-hx-label/task-1-verify.txt`

## Execution strategy
### Parallel execution waves
- Wave 1: 单任务 todo 1（无并行对象，任务本身即最小单元）

### Dependency matrix
| Todo | Depends on | Blocks | Can parallelize with |
| --- | --- | --- | --- |
| 1 | 无 | F1-F4 | 无 |

## Todos
> Implementation + Test = ONE todo. Never separate.
<!-- APPEND TASK BATCHES BELOW THIS LINE WITH edit/apply_patch - never rewrite the headers above. -->
- [x] 1. 修改 ch02_framework.tex:205 的 $H_{\mathbf{x}}$（完整）标签坐标 (2,2.95)→(2,3.1) 并编译验证
  What to do / Must NOT do: 用 Edit 工具将第 205 行 `\node[above] at (2,2.95) {$H_{\mathbf{x}}$（完整）};` 精确替换为 `\node[above] at (2,3.1) {$H_{\mathbf{x}}$（完整）};`（唯一一处改动，oldString 含完整行文本确保唯一匹配）。不得改动文件内任何其他行，尤其不得触碰 (b) 面板第 228 行 `\node[above] at (0.7,2.95) {$H_{\mathbf{x}}$（截断）};`。修改后在项目根目录 `D:\PD-book` 运行 `xelatex -interaction=nonstopmode -halt-on-error main.tex` 两遍，两次 exit code 均须为 0。随后用 PowerShell 过滤 `Select-String -Path main.log -Pattern '^!|undefined|Warning: Reference|Warning: Citation'` 须零命中（已知良性：1 处 `Underfull \vbox` 与 infwarerr 宏包自述行不属于上述 pattern，允许存在）。最后用 `Select-String -Path main.aux -Pattern 'newlabel\{fig:boundary-truncation\}'` 确认图 2.4 的 label 仍存在。
  Parallelization: Wave 1 | Blocked by: 无 | Blocks: F1-F4
  References (executor has NO interview context - be exhaustive): `D:\PD-book\chapters\ch02_framework.tex:205`（当前行内容 `\node[above] at (2,2.95) {$H_{\mathbf{x}}$（完整）};`）；(b) 面板对照行 228（`(0.7,2.95)`，不得改）；圆弧几何：圆心 (2,1.6) 半径 1.3 → 弧顶 y=2.9，新标签 y=3.1 留白 0.2cm；矩形顶边 y=3.2 无冲突。项目编译规范见 `D:\PD-book\AGENTS.md`（XeLaTeX 必须、编译门禁过滤规则、已知良性警告）。
  Acceptance criteria (agent-executable): `Select-String -Path chapters\ch02_framework.tex -Pattern 'at \(2,3.1\)'` 命中 1 处；两遍 xelatex exit code 均 0；日志过滤零命中；`main.aux` 中 `\newlabel{fig:boundary-truncation}` 存在。
  QA scenarios (name the exact tool + invocation): happy - bash 运行两遍 `xelatex -interaction=nonstopmode -halt-on-error main.tex` 检查 `$LASTEXITCODE` 为 0；failure - 用 Edit 工具读取改动前后行内容确认无多余变更、无错位；Evidence `.omo/evidence/adjust-fig24-hx-label/task-1-verify.txt`（记录 exit codes、过滤结果、aux 核对行）。
  Commit: N（人工负责 git 提交）
- [x] 2. 修改 ch02_framework.tex:228 的 $H_{\mathbf{x}}$（截断）标签坐标 (0.7,2.95)→(0.7,3.1) 并编译验证（用户补充需求：b 子图标签与 a 对称上调）
  What to do / Must NOT do: 用 Edit 工具将第 228 行 `\node[above] at (0.7,2.95) {$H_{\mathbf{x}}$（截断）};` 精确替换为 `\node[above] at (0.7,3.1) {$H_{\mathbf{x}}$（截断）};`。不得改动文件内任何其他行，尤其不得触碰 (a) 面板第 205 行（已改为 (2,3.1)）。修改后运行 xelatex 两遍（exit 0），过滤 `^!|undefined|Warning: Reference|Warning: Citation` 零命中，核对 aux label 存在。
  Parallelization: Wave 1 | Blocked by: 无 | Blocks: F1-F4
  References (executor has NO interview context - be exhaustive): `D:\PD-book\chapters\ch02_framework.tex:228`（当前行 `\node[above] at (0.7,2.95) {$H_{\mathbf{x}}$（截断）};`）；(a) 面板第 205 行现为 `(2,3.1)`；对称性目标：两标签 y 坐标均为 3.1；(b) 截断弧顶约 y≈2.69（57.4°处），新标签 y=3.1 留白约 0.41cm；矩形顶 y=3.2，标签锚点在矩形内。
  Acceptance criteria (agent-executable): `Select-String -Path chapters\ch02_framework.tex -Pattern 'at \(0.7,3.1\)'` 命中 1 处且第 205 行仍为 `(2,3.1)`；两遍 xelatex exit code 均 0；日志过滤零命中；aux label 存在。
  QA scenarios (name the exact tool + invocation): happy - 两遍 `xelatex -interaction=nonstopmode -halt-on-error main.tex` 检查 `$LASTEXITCODE`；failure - read 核对第 205/228 行内容无错位；Evidence `.omo/evidence/adjust-fig24-hx-label/task-2-verify.txt`。
  Commit: N（人工负责 git 提交）

## Final verification wave
> Runs in parallel after ALL todos. ALL must APPROVE. Surface results and wait for the user's explicit okay before declaring complete.
- [x] F1. Plan compliance audit
- [x] F2. Code quality review
- [x] F3. Real manual QA
- [x] F4. Scope fidelity

## Commit strategy
- 不自动提交。源文件改动（chapters/ch02_framework.tex）由人工在合适时机 commit；编译产物（main.pdf/.aux/.log 等）勿提交（AGENTS.md 约定）。

## Success criteria
- `chapters/ch02_framework.tex:205` 显示 `\node[above] at (2,3.1) {$H_{\mathbf{x}}$（完整）};`
- 两遍 xelatex 编译 exit 0，main.log 过滤 `^!|undefined|Warning: Reference|Warning: Citation` 零命中
- 图 2.4 (a) 标签与圆弧留白约 0.2 cm，与 (b) 面板视觉一致
- 除第 205 行外无任何其他文件变更
