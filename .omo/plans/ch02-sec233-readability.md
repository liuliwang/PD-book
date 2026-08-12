# ch02-sec233-readability - Work Plan

## TL;DR (For humans)
<!-- Fill this LAST, after the detailed plan below is written, so it summarizes the REAL plan. -->
<!-- Plain English for a non-engineer: NO file paths, NO todo numbers, NO wave/agent/tool names. -->

**What you'll get:** 第 2 章第 3.3 节（对力函数的量纲）的 7 处结构优化，使推导逻辑更连贯、段落层次更清晰、内容无冗余。

**Why this approach:** 当前小节存在导入突兀、解释位置不当、推导跳跃、段落过长、内容重复 5 类可读性问题；通过调整文字位置和拆分长段落即可解决，无需改动公式或表格数据。

**What it will NOT do:** 不会修改其他章节，不会改动公式数学内容，不会增减表格数据。

**Effort:** Short
**Risk:** Low - 纯文本调整，不涉及编译配置或外部依赖
**Decisions to sanity-check:** Remark 精简后是否保留了“数学签名”这一核心洞察；量级估计拆分为三段后是否损失了物理直觉的连贯性。

Your next move: 批准计划后，执行者按 Wave 1 → Wave 2 顺序完成 7 个 todo，最后通过编译验证和逻辑审查。

---

> TL;DR (machine): Short effort, Low risk - 7 readability improvements to ch02 section 2.3.3 (dimensional analysis of pairwise force), no formula changes, compilation verification included.

---

> TL;DR (machine): <1 line - effort, risk, deliverables>

## Scope
### Must have
- 改写段首导入，明确本节目标
- 调整左端惯性项解释位置（推导→公式→解释）
- 增加右端积分推导引导语（引入邻域体积 V_δ）
- 优化量纲分析表前后过渡（总结移至表后）
- 拆分量级估计段落（参数-计算-验证三段式）
- 消除第662行与Remark的重复内容
- 精简Remark，聚焦“数学签名”核心观点
- 编译验证（xelatex + bibtex 无 error）
- 逻辑连贯性检查（无未定义引用、无未完成句子）

### Must NOT have (guardrails, anti-slop, scope boundaries)
- 不修改其他章节（ch01, ch03-ch19, appendices）
- 不修改公式数学内容（仅调整文字描述和段落结构）
- 不增减表格数据或图表
- 不改动符号表（frontmatter/notation.tex）或文献引用（bibliography.bib）
- 不引入未定义的符号或术语
- 不改动对比表（tab:stress-vs-pairwise-force）的结构和数据

## Verification strategy
> Zero human intervention - all verification is agent-executed.
- Test decision: tests-after（编译验证 + 逻辑检查）
- Evidence: .omo/evidence/ch02-sec233-readability/
- 验证工具：
  1. 编译验证：`xelatex -interaction=nonstopmode -halt-on-error main.tex`（检查无 error）
  2. 引用检查：`grep "undefined" main.log` 计数为 0
  3. 逻辑检查：读取修改后的 2.3.3 节全文，确认无未完成句子、无未定义引用
  4. 结构检查：确认段落拆分后各段主题明确、衔接自然

## Execution strategy
### Parallel execution waves
> Target 5-8 todos per wave. Fewer than 3 (except the final) means you under-split.

### Dependency matrix
| Todo | Depends on | Blocks | Can parallelize with |
| --- | --- | --- | --- |
| 1. 改写段首导入 | none | none | 2, 3, 4 |
| 2. 调整左端惯性项解释位置 | none | none | 1, 3, 4 |
| 3. 增加右端推导引导语 | none | none | 1, 2, 4 |
| 4. 优化量纲分析表前后过渡 | none | Wave 2 | 1, 2, 3 |
| 5. 拆分量级估计段落 | Wave 1 | none | 6 |
| 6. 消除第662行与Remark重复 | Wave 1 | none | 5, 7 |
| 7. 精简Remark内容 | Wave 1, Todo 6 | none | 5, 6 |

## Todos
> Implementation + Test = ONE todo. Never separate.
<!-- APPEND TASK BATCHES BELOW THIS LINE WITH edit/apply_patch - never rewrite the headers above. -->

### Wave 1: 结构优化（独立修改）

- [x] 1. 改写段首导入（第624-625行）
  What to do / Must NOT do: 将“在建立了对力函数 f 的物理图像（2.3.1节）和数学结构（2.3.2节）之后，本节从量纲分析的角度，验证运动方程(2.6)在数学上的自洽性，并揭示对力函数量纲背后的物理内涵”改写为更具体的导入，明确本节目标：“本节通过量纲分析确定对力函数 f 的量纲，这是理解其物理意义的关键一步”。Must NOT: 删除对2.3.1和2.3.2节的引用。
  Parallelization: Wave 1 | Blocked by: none | Blocks: none
  References: ch02_framework.tex:622-625; 对比 ch01/ch06 同类章节导入风格
  Acceptance criteria: 段首句明确本节“做什么”（确定量纲）和“为什么重要”（理解物理意义），避免“验证自洽性”等抽象表述。
  QA scenarios: happy=编译通过且段首句通顺；failure=导入仍含糊或丢失对前两节的引用。
  Commit: Y | docs(ch02): 改写2.3.3节段首导入，明确本节目标

- [x] 2. 调整左端惯性项解释位置（第626-631行）
  What to do / Must NOT do: 将“即力密度（单位体积的力）”从公式前移至公式后。修改后结构：公式(2.x)给出量纲→“这意味着运动方程左端描述的是单位体积的惯性力（力密度）”→再引入体力密度 b。Must NOT: 改动公式本身。
  Parallelization: Wave 1 | Blocked by: none | Blocks: none
  References: ch02_framework.tex:626-631
  Acceptance criteria: 公式(2.x)后直接跟解释句，逻辑顺序为“推导→公式→解释→对比”。
  QA scenarios: happy=解释句在公式后；failure=解释句仍在公式前或逻辑断裂。
  Commit: Y | docs(ch02): 调整左端惯性项量纲解释的位置

- [x] 3. 增加右端推导引导语（第631-636行）
  What to do / Must NOT do: 在“右端积分项为对力的体积积分”后增加过渡：“设邻域体积为 V_δ，则积分项量纲为 [f]·V_δ。为使方程两端量纲匹配，对力函数 f 的量纲须为...”。Must NOT: 引入未定义的符号（如用 V_δ 但不在本节定义）。
  Parallelization: Wave 1 | Blocked by: none | Blocks: none
  References: ch02_framework.tex:631-636
  Acceptance criteria: 右端推导中出现“设邻域体积为 V_δ”或等效表述，明确积分如何影响量纲。
  QA scenarios: happy=推导步骤可见 V_δ 的引入；failure=仍直接跳至结论。
  Commit: Y | docs(ch02): 增加右端积分项量纲推导的引导语

- [x] 4. 优化量纲分析表前后过渡（第638-639行、第655-657行）
  What to do / Must NOT do: （1）表前：将第638行“运动方程两端均为 N/m³，意味着对力函数 f 必须自带两个体积除数”移至表后作为总结；（2）表前替换为简单导入“表2.1汇总了运动方程各项的量纲”；（3）表后接原第638行内容作为解释。Must NOT: 删除或修改表格数据。
  Parallelization: Wave 1 | Blocked by: none | Blocks: Wave 2（影响后续段落衔接）
  References: ch02_framework.tex:638-639, 655-657
  Acceptance criteria: 表格前有简短导入，表格后有“为什么 N/m⁶”的解释（两个体积除数）。
  QA scenarios: happy=表格前后过渡自然；failure=总结句仍在表前或表后缺少解释。
  Commit: Y | docs(ch02): 调整量纲分析表的前后过渡语

### Wave 2: 段落重组与精炼

- [x] 5. 拆分量级估计段落（第658-661行）
  What to do / Must NOT do: 将单一长段拆分为三段：（1）参数设定段：引入+材料参数（ρ, δ, c）；（2）计算过程段：对力量级 |f| ~ c·s ~ 10¹⁵ N/m，具体算例 dF ~ 10⁻³ N；（3）验证结论段：与经典理论量级对比，验证自洽性。Must NOT: 修改数值或物理结论。
  Parallelization: Wave 2 | Blocked by: Wave 1 | Blocks: none
  References: ch02_framework.tex:658-661
  Acceptance criteria: 原文内容完整保留但分为三个独立段落，每段有明确主题句。
  QA scenarios: happy=三段结构清晰；failure=仍为一个长段或拆分后丢失内容。
  Commit: Y | docs(ch02): 拆分量级估计段落为三段式

- [x] 6. 消除第662行与Remark重复（第662行、第681-683行）
  What to do / Must NOT do: （1）保留第662行作为表格后的过渡句，内容精简为“这一量纲与经典连续介质力学中应力（N/m²）有本质区别，反映了近场动力学非局部描述的固有特征”；（2）Remark 中删除与第662行重复的经典应力对比内容，仅保留表格未涵盖的“数学签名”观点。Must NOT: 删除对比表或第662行整句。
  Parallelization: Wave 2 | Blocked by: Wave 1 | Blocks: none
  References: ch02_framework.tex:662, 681-683
  Acceptance criteria: 第662行与Remark内容无重复，各承担不同功能（过渡 vs 深入洞察）。
  QA scenarios: happy=无重复；failure=Remark仍重复第662行内容。
  Commit: Y | docs(ch02): 消除第662行与Remark的重复内容

- [x] 7. 精简Remark内容（第681-683行）
  What to do / Must NOT do: 将Remark精简为2-3句，保留核心“数学签名”观点（N/m⁶ 是PD理论架构的数学签名，兼具MD和经典力学特征），删除或简化关于“δ→0极限”的细节（留给第7章引用）。Must NOT: 完全删除Remark。
  Parallelization: Wave 2 | Blocked by: Wave 1, Todo 6 | Blocks: none
  References: ch02_framework.tex:681-683; ch07 微极限分析章节（仅引用）
  Acceptance criteria: Remark 长度 ≤ 3 句，核心观点为“数学签名”，极限分析指向第7章。
  QA scenarios: happy=Remark简洁且聚焦；failure=仍超过4句或保留冗余的极限分析推导。
  Commit: Y | docs(ch02): 精简Remark，聚焦“数学签名”核心观点

## Final verification wave
> Runs in parallel after ALL todos. ALL must APPROVE. Surface results and wait for the user's explicit okay before declaring complete.
- [x] F1. 编译合规审计：`xelatex -interaction=nonstopmode -halt-on-error main.tex` 无 error，`main.log` 中 `undefined` 计数为 0
- [x] F2. 逻辑质量审查：读取修改后的 2.3.3 节全文，确认推导链完整、术语一致、无未定义引用
- [x] F3. 结构质量审查：确认 7 处修改均完成，段落拆分后各段主题明确，表格前后过渡自然
- [x] F4. 范围保真度：确认未修改其他章节、未改动公式数学内容、未增减表格数据

## Commit strategy
- 每完成一个 todo 提交一次（共 7 次 commit），commit message 格式：`docs(ch02): <描述>`
- 最终验证通过后，如有必要，可合并为一个 commit：`docs(ch02): 提升2.3.3节“对力函数的量纲”可读性`
- 编译产物（*.aux/*.log/*.pdf/*.bbl 等）不提交（已由 .gitignore 忽略）

## Success criteria
1. **编译通过**：`xelatex main.tex` + `bibtex main` + `xelatex main.tex` 无 error，无 undefined reference/citation 警告
2. **逻辑连贯**：段首导入明确→左端推导→右端推导→表格→物理意义→量级估计→对比表→Remark，每步衔接自然
3. **无冗余**：第662行与Remark内容不重复，各承担不同功能
4. **段落长度适中**：量级估计拆分为三段，每段有明确主题句
5. **Remark 精简**：长度 ≤ 3 句，聚焦“数学签名”核心观点
6. **范围受控**：仅修改 ch02_framework.tex 第 622–686 行，其他章节和文件未动
