# ch02-233-dimension-optimization - Work Plan

## TL;DR (For humans)

**What you'll get:** 2.3.3节"对力函数的量纲"重组为"对力函数的量纲与物理意义"，优化逻辑流与过渡衔接，将溢出"量纲"主题的多维度对比表移至2.3.1节末尾，提升可读性与标题匹配度。

**Why this approach:** 当前2.3.3节标题狭窄（仅"量纲"），但内容涵盖了物理意义阐释、数值估计、理论定位等，存在"标题包不住内容"问题。方案B通过扩展标题+重组内容+优化过渡，使标题与内容精准匹配，同时保持逻辑连贯。

**What it will NOT do：** 不修改2.3.1/2.3.2/2.3.4节的主体内容；不新增公式或定理；不引入新文献引用。

**Effort：** 1个文件（ch02_framework.tex），约80行修改，1轮编译验证。

**Risk：** 低。仅为文本重组，无公式推导改动，编译风险极低。

---

## Scope

### IN scope (this plan)
- [ ] 1. 修改2.3.3节标题为"对力函数的量纲与物理意义"
- [ ] 2. 优化2.3.3节内部过渡句（4处过渡衔接）
- [ ] 3. 将多维度对比表（`tab:stress-vs-pairwise-force`）从2.3.3节移至2.3.1节末尾
- [ ] 4. 将Remark理论总结段融入2.3.3节正文末尾
- [ ] 5. 在2.3.3节末尾增加小节总结句
- [ ] 6. 编译验证（xelatex无error，无undefined引用）

### OUT of scope (will NOT touch)
- 2.3.1/2.3.2/2.3.4节的主体内容（除新增对比表位置外）
- 公式推导、定理证明
- 文献引用
- 图表绘制（TikZ代码）
- `main.tex`、`preamble.tex` 等全局文件

---

## Verification strategy

**编译验证：** `xelatex -interaction=nonstopmode -halt-on-error main.tex`
- 预期：无error，无undefined reference/citation
- 检查：`main.log` 中 `undefined` 计数为0

**结构验证：**
- 2.3.3节新标题与内容匹配
- 多维度对比表在2.3.1节末尾正常显示
- 所有`\ref`/`\eqref`引用正确（无broken reference）
- 表格编号连续，无跳号

**可读性验证：**
- 逻辑流顺畅：量纲推导→量纲表→物理意义→数值估计→理论总结
- 过渡句自然，无"硬切换"

---

## Execution strategy

按依赖顺序执行，前一步完成后才能开始下一步。

### 依赖关系
```
1. 移动对比表至2.3.1节末尾（前置，避免2.3.3节内容引用断裂）
   ↓
2. 修改2.3.3节标题
   ↓
3. 优化2.3.3节过渡句
   ↓
4. 融入Remark至正文
   ↓
5. 增加小节总结句
   ↓
6. 编译验证
```

---

## Todos

- [x] 1. **移动多维度对比表至2.3.1节末尾**
  - **Where:** `chapters/ch02_framework.tex`，第668-683行（`tab:stress-vs-pairwise-force`）
  - **What:** 将表格从2.3.3节剪切，粘贴到2.3.1节末尾（第496行附近，"键基模型均取这一形式"之后）
  - **How:** 使用`edit`工具，先删除原位置，再在2.3.1节末尾插入
  - **Acceptance:** 表格在2.3.1节末尾正常显示，2.3.3节中不再出现该表格
  - **QA (happy):** 编译后PDF中表格出现在2.3.1节末尾，内容完整
  - **QA (failure):** 若表格编号断裂，检查是否有遗留`\label`或`\ref`
  - **Commit:** 单独commit，message: "ch02: move stress-vs-pairwise-force table from 2.3.3 to end of 2.3.1"

- [x] 2. **修改2.3.3节标题**
  - **Where:** `chapters/ch02_framework.tex`，第622行
  - **What:** `\subsection{对力函数的量纲}` → `\subsection{对力函数的量纲与物理意义}`
  - **Acceptance:** 标题文本正确，编译后PDF显示新标题
  - **QA (happy):** `grep "对力函数的量纲与物理意义" ch02_framework.tex` 返回1行
  - **QA (failure):** 若标题格式错误（如缺少`\subsection`），编译报错
  - **Commit:** 单独commit，message: "ch02: rename 2.3.3 section title to include physical meaning"

- [x] 3. **优化2.3.3节过渡句（共4处）**
  - **Where:** 见下表
  - **What:** 替换4处过渡句，使逻辑流更顺畅
  - **Acceptance:** 每处过渡句自然衔接前后内容，无"硬切换"

  | 位置 | 原文 | 修改为 |
  |------|------|--------|
  | 量纲推导→量纲表 | "表~\\ref{tab:dim-analysis}汇总了运动方程各项的量纲。" | "为清晰展示运动方程各项的量纲关系，表~\\ref{tab:dim-analysis}汇总了惯性项、体力、对力及其积分后的量纲对比。" |
  | 量纲表→物理意义 | "从表~\\ref{tab:dim-analysis}可以看出，运动方程两端均为..." | "量纲推导给出了N/m⁶的代数来源，但其物理含义仍需进一步阐释。" |
  | 物理意义→数值估计 | "表格给出了量纲的代数关系，但抽象的N/m⁶仍需具体数值来建立直觉。" | "上述分析给出了对力函数量纲的代数来源，但N/m⁶这一抽象量纲在物理上究竟对应多大的力？下面通过具体参数进行量级估计。" |
  | 数值估计→理论总结 | （当前直接跳到对比表，已删除） | 增加："数值估计表明，虽然N/m⁶看似抽象，但在典型工程尺度下对应着合理的力学量级。它同时也说明，对力函数的量纲并非任意设定，而是运动方程自洽性的必然结果。" |

  - **QA (happy):** 编译后PDF中过渡自然，逻辑连贯
  - **QA (failure):** 若过渡句引入编译错误（如特殊字符），检查LaTeX语法
  - **Commit:** 单独commit，message: "ch02: optimize transition sentences in 2.3.3 for logical flow"

- [x] 4. **融入Remark至正文末尾**
  - **Where:** `chapters/ch02_framework.tex`，第685-687行
  - **What:** 删除`\begin{remark}`和`\end{remark}`环境标记，将内容转为普通正文段落
  - **Acceptance:** 内容保留，但不再是remark环境，编译后显示为普通段落
  - **QA (happy):** PDF中内容显示为正文段落，格式正确
  - **QA (failure):** 若remark环境嵌套导致编译错误，检查环境标记
  - **Commit:** 单独commit，message: "ch02: integrate remark content into main text of 2.3.3"

- [x] 5. **增加小节总结句**
  - **Where:** `chapters/ch02_framework.tex`，第689行之后（"本节部分内容经AI辅助生成..."之前）
  - **What:** 插入总结句："本节从量纲分析出发，确立了对力函数$\\mathbf{f}$的量纲为$\\mathrm{N}/\\mathrm{m}^{6}$，阐明了其物理意义，并通过数值估计验证了量纲的自洽性。这一定量特征为第4章微模量的标定提供了必要的理论前提。"
  - **Acceptance:** 总结句准确概括本节内容，与2.3.4节衔接自然
  - **QA (happy):** 编译后PDF中总结句显示正确
  - **QA (failure):** 若`\mathbf{f}`等公式编译错误，检查LaTeX语法
  - **Commit:** 单独commit，message: "ch02: add concluding summary to 2.3.3"

- [x] 6. **编译验证**
  - **Command:** `xelatex -interaction=nonstopmode -halt-on-error main.tex`
  - **Acceptance:** 
    - `main.log` 中无`!` error
    - `main.log` 中`undefined`计数为0
    - 输出PDF中2.3.3节显示正确
  - **QA (happy):** 编译通过，PDF内容正确
  - **QA (failure):** 若编译失败，根据错误信息回溯修正
  - **Commit:** 最终验证通过，message: "ch02: verify compilation of ch02 after 2.3.3 reorganization"

---

## Final verification wave

- [x] F1. **结构检查：** 确认2.3.3节标题为"对力函数的量纲与物理意义"，内容与标题匹配
- [x] F2. **引用检查：** 确认所有`\ref`/`\eqref`无broken reference
- [x] F3. **表格检查：** 确认`tab:stress-vs-pairwise-force`在2.3.1节末尾正常显示
- [x] F4. **逻辑流检查：** 从量纲推导→量纲表→物理意义→数值估计→理论总结→小节总结，逻辑连贯无跳跃

---

## Commit strategy

每完成一个待办事项即commit一次，保持commit粒度清晰：
1. `ch02: move stress-vs-pairwise-force table from 2.3.3 to end of 2.3.1`
2. `ch02: rename 2.3.3 section title to include physical meaning`
3. `ch02: optimize transition sentences in 2.3.3 for logical flow`
4. `ch02: integrate remark content into main text of 2.3.3`
5. `ch02: add concluding summary to 2.3.3`
6. `ch02: verify compilation of ch02 after 2.3.3 reorganization`

---

## Success criteria

1. **标题匹配：** 2.3.3节标题准确概括内容（"量纲与物理意义"）
2. **内容完整：** 量纲推导、量纲表、物理意义、数值估计、理论总结全部保留
3. **逻辑连贯：** 4处过渡句自然流畅，无"硬切换"
4. **引用正确：** 所有`\ref`/`\eqref`无broken reference
5. **编译通过：** `xelatex`无error，无undefined
6. **表格位置正确：** `tab:stress-vs-pairwise-force`在2.3.1节末尾
