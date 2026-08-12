# ch02-sec233-polish-v2 - Work Plan

## TL;DR (For humans)

**What you'll get:** 2.3.3 节「第二段后面」内容的阅读性优化——更清晰的过渡、更贴切的类比、更易读的数值段、更深度的 remark，避免与对比表的信息重叠。

**Why this approach:** 当前表格→物理意义→数值直觉→对比表→remark 的衔接存在认知跳跃和重复，通过增加过渡句、替换类比、拆短句、重构 remark，使段落层次递进更自然。

**What it will NOT do:** 不改动量纲推导公式（eq:dim-inertia、eq:dim-force 保持不变）；不改动对比表结构；不新增章节。

**Effort:** Short
**Risk:** Low - 纯文本改写，无新增 LaTeX 环境或宏包依赖
**Decisions to sanity-check:** remark 中 local limit 伏笔引用第7章（而非原建议的第2.4节），是否符合全书结构

Your next move: approve and run `/start-work ch02-sec233-polish-v2`.

---

> TL;DR (machine): Short effort, low risk, polish post-derivation content in ch02_framework.tex lines 638-681; 7 text-level optimizations, no new environments/packages.

---

> TL;DR (machine): <1 line - effort, risk, deliverables>

## Scope
### Must have
1. 表引导句前新增过渡句（约2行），引入「两个体积除数」概念
2. 物理意义解释替换为「表格解读+力学类比」，替换概率论类比
3. 数值直觉段拆短句 + `\textbf` 标出关键数字
4. remark 重写：避免重复对比表内容，提升到理论谱系 + 第7章 local limit 伏笔
5. 表格与数值直觉之间加「承上启下」过渡句

### Must NOT have (guardrails, anti-slop, scope boundaries)
- 不改动量纲推导公式（eq:dim-inertia、eq:dim-force）
- 不改动对比表结构（lines 662-677 保持原样）
- 不新增章节或子节
- 不引入新宏包或新环境
- 不改动 2.3.3 节以外的内容

## Verification strategy
> Zero human intervention - all verification is agent-executed.
- Test decision: none (LaTeX text-level polish, compile-only verification)
- Evidence: `.omo/evidence/ch02-sec233-polish-v2/` — xelatex compilation log and PDF diff

## Execution strategy
### Parallel execution waves
- Wave 1: Todos 1-3（文本改写，互相无依赖，可并行）
- Wave 2: Todo 4（remmark 重写，依赖 Wave 1 完成后的文件状态）
- Wave 3: Todos 5-6（过渡句和合规检查，依赖 Wave 2）
- Wave 4: Final verification (F1-F4)

### Dependency matrix
| Todo | Depends on | Blocks | Can parallelize with |
| --- | --- | --- | --- |
| 1 | — | 3 | 2 |
| 2 | — | 3 | 1 |
| 3 | — | 4 | 1,2 |
| 4 | 1,2,3 | 5,6 | — |
| 5 | 4 | 6 | — |
| 6 | 5 | F-wave | — |

## Todos
> Implementation + Test = ONE todo. Never separate.

- [x] 1. 表引导句前新增过渡句
  What to do / Must NOT do: 在 line 638 表格引导句「为清晰展示运动方程各项的量纲关系」之前，新增一句过渡：「运动方程两端均为 N/m³，意味着对力函数 f 必须自带「两个体积除数」。为清晰展示这一关系...」。保持 line 638 引导句主体不变，仅在其前插入新句。Must NOT 删除或改动原有引导句。
  Parallelization: Wave 1 | Blocked by: — | Blocks: 4
  References: chapters/ch02_framework.tex:636-638
  Acceptance criteria: 过渡句存在且包含「两个体积除数」关键词；xelatex 编译无 error
  QA scenarios: Read file lines 636-640, verify new sentence exists before table guide
  Commit: Y | polish(ch02): add transition sentence before dim-analysis table

- [x] 2. 物理意义解释替换为表格解读+力学类比
  What to do / Must NOT do: 将 line 656「式\eqref{eq:dim-force}给出的量纲可直观理解为...联合事件的密度量纲为 $1/V^{2}$。」整段替换为：「从表\ref{tab:dim-analysis}可以看出，对力函数 f 的量纲 N/m⁶ 与经典应力 σ 的 N/m² 存在本质差异：经典理论中，内力通过面积微元 dA 传递，因此量纲含 m² 除数；而在近场动力学中，相互作用发生在两个体积微元之间，量纲须含 m⁶ 除数。f 可理解为「单位体积微元对单位体积微元的力密度」——正如 σ 描述「单位面积上的力」，f 描述的是「单位体积对上的力」。」Must NOT 保留概率论类比。
  Parallelization: Wave 1 | Blocked by: — | Blocks: 4
  References: chapters/ch02_framework.tex:656
  Acceptance criteria: 新段落包含「面积微元」「体积微元」类比；不含「联合密度」或「概率论」关键词；xelatex 编译无 error
  QA scenarios: Grep file for "联合密度" → 0 matches; Grep for "面积微元" → ≥1 match
  Commit: Y | polish(ch02): replace probability analogy with mechanics analogy

- [x] 3. 数值直觉段拆短句+粗体标关键数字
  What to do / Must NOT do: 将 line 658 的超长数值段拆分为 2-3 个短句，并用 `\textbf{}` 标出关键量级数字（|f|~c·s~10¹⁵、毫牛量级）。具体拆分：「为建立直观感受，考虑如下量级估计。设材料密度 ρ~10³ kg/m³，在 10⁶ Pa 应力下经典应变约为 10⁻³。取近场域半径 δ~10⁻³ m，微模量 c~10¹⁸ N/m（见第4章标定），则对力函数量级为 \textbf{|f|~c·s~10¹⁵ N/m}。对两个体积均为 10⁻⁹ m³（微米尺度立方体）的物质点，其相互作用力为 \textbf{dF~10⁻³ N}，即\textbf{毫牛量级}——这与经典理论中 10⁻⁶ m² 面积上受力 1 N 的量级一致，验证了量纲分析的自洽性。」Must NOT 改动数值或量纲。
  Parallelization: Wave 1 | Blocked by: — | Blocks: 4
  References: chapters/ch02_framework.tex:658
  Acceptance criteria: 段落拆分为 ≤3 句；包含 ≥3 个 `\textbf{}` 标记；数值和量纲与原文完全一致
  QA scenarios: Read line 658 area, count sentences (≤3); count `\textbf` (≥3)
  Commit: Y | polish(ch02): split numerical intuition into short sentences with bold highlights

- [x] 4. remark 重写：避免重复对比表，提升到理论谱系 + 第7章 local limit 伏笔
  What to do / Must NOT do: 将 lines 679-681 的 remark 替换为：「对力函数的量纲 N/m⁶ 并非偶然，而是 PD 理论架构的数学签名。分子动力学（MD）处理离散原子，力以 N 为单位；经典连续介质力学处理局部场，应力以 N/m² 为单位；而 PD 处理的是「连续介质中的非局部对力」，其量纲 N/m⁶ 恰好反映了它兼具两者的特征——比 MD 多了连续介质假设带来的两个体积除数，比经典多了非局部相互作用带来的两个长度除数。当近场域半径 δ→0 时，对力函数的体积积分将退化为面积分，此时 N/m⁶ 的量纲行为将趋近于 N/m²（详见第 7 章的微极限分析），这进一步说明 N/m⁶ 是 PD 在非局部框架下对经典理论的自然推广。」Must NOT 重复对比表中已出现的「相互作用对象」「描述方式」「作用载体」等信息；local limit 引用指向第7章（ch07 第944行已有相关内容）。
  Parallelization: Wave 2 | Blocked by: 1,2,3 | Blocks: 5,6
  References: chapters/ch02_framework.tex:679-681; ch07_nonordinary_state.tex:944
  Acceptance criteria: remark 不含「相互作用对象」「描述方式」「作用载体」关键词；含「第7章」或「第 7 章」；xelatex 编译无 error
  QA scenarios: Grep for "相互作用对象" in remark area → 0; Grep for "第.章" → match found
  Commit: Y | polish(ch02): rewrite remark to avoid table repetition and add ch7 foreshadowing

- [x] 5. 表格与数值直觉之间加「承上启下」过渡句
  What to do / Must NOT do: 在 line 656（新的物理意义解释段）和 line 658（数值直觉段）之间插入一句：「表格给出了量纲的「代数定义」，但抽象的符号仍需具体的数值锚点来填充直觉。」Must NOT 改动前后段落内容。
  Parallelization: Wave 3 | Blocked by: 4 | Blocks: 6
  References: chapters/ch02_framework.tex:656-658
  Acceptance criteria: 过渡句存在；xelatex 编译无 error
  QA scenarios: Read lines 656-660, verify transition sentence exists between interpretation and numerical sections
  Commit: Y | polish(ch02): add bridge sentence between table/interpretation and numerical intuition

- [x] 6. 合规检查：AI 辅助生成声明
  What to do / Must NOT do: 检查全文修改区域是否有 AI 辅助生成的数学/物理内容。如有，在文件适当位置（如章末或本节末尾）添加声明：「本节部分内容经 AI 辅助生成，需经专业审阅。」本项目 AGENTS.md 要求「AI 生成数学/物理内容须声明」。如已有声明则跳过。Must NOT 在正文中插入突兀的注释。
  Parallelization: Wave 3 | Blocked by: 5 | Blocks: F-wave
  References: AGENTS.md "AI 写作约束" section; ch02_framework.tex
  Acceptance criteria: 检查全文是否已有 AI 声明；如有新增内容则为 AI 辅助，需有声明；如无新增 AI 内容则跳过
  QA scenarios: Grep ch02_framework.tex for "AI 辅助生成" or "AI-generated" → check count
  Commit: N (no code change if skipped)

## Final verification wave
> Runs in parallel after ALL todos. ALL must APPROVE. Surface results and wait for the user's explicit okay before declaring complete.
- [x] F1. Plan compliance audit: Verify all 7 optimizations implemented; no scope creep (unchanged lines: 626-636, 662-677)
- [x] F2. Code quality review: Check for overfull hboxes, orphaned lines, bad line breaks in new text
- [x] F3. Real manual QA: xelatex compile with `-interaction=nonstopmode -halt-on-error`; check main.log for undefined=0, errors=0
- [x] F4. Scope fidelity: Verify only lines 638-681 modified; no changes outside this range

## Commit strategy
- Single commit with all polish changes: `polish(ch02): optimize 2.3.3 post-derivation readability`
- Stage only `chapters/ch02_framework.tex`

## Success criteria
- [x] 7 项优化全部实现
- [x] 编译通过（xelatex 无 error）
- [x] 内容无重复，逻辑连贯
- [x] remark 与对比表无信息重叠
- [x] local limit 伏笔引用指向第7章
