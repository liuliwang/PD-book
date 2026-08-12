# ch02-sec233-dimension-transition - Work Plan

## TL;DR (For humans)
在 ch02_framework.tex 第 2.3.3 节开头插入一段过渡文字，解释"为什么要回到运动方程反推对力函数量纲"，消除原句"运动方程(2.6)两端各项的量纲必须一致"的突兀感。修改后读者能明确理解：对力函数量纲无法从定义式单独确定，必须依赖运动方程的自洽性。

**范围**：仅修改 `chapters/ch02_framework.tex`，不涉及其他文件。
**风险**：无——不改公式、不改编号、不改引用。
**努力**：1 个 todo，约 5 分钟。

## Scope
- **IN**：`chapters/ch02_framework.tex` 第 644–645 行之间插入过渡段（约 3 行 LaTeX 源码）
- **OUT**：其他所有文件、公式编号、图表引用均不受影响

## Verification strategy
- 编译验证：`xelatex main.tex` 无 error/warning（含参考文献完整流程）
- 逻辑验证：阅读 2.3.3 节，确认过渡段使"运动方程量纲必须一致"不再突兀

## Execution strategy
单文件单处插入，直接编辑即可。

## Todos
- [x] 1. 在 ch02_framework.tex 第 644–645 行之间插入过渡段并编译验证
  - **References**: `chapters/ch02_framework.tex` 第 641–690 行（2.3.3 节完整内容）
  - **Acceptance criteria**:
    - 第 644 行后新增过渡段落，包含两个核心信息：(a) 为什么无法从对力函数定义式直接确定量纲；(b) 为什么回到运动方程反推
    - 插入位置精确：第 644 行（"在此基础上…"段）之后、第 645 行（"运动方程…"）之前
    - 新插入文字与前后文风格一致，无重复、无遗漏
    - 不改变任何公式编号或引用
  - **Happy QA**: `xelatex main.tex` 编译通过，无 error、无新增 warning；阅读 2.3.3 节，逻辑连贯自然
  - **Failure QA**: 若编译失败，检查是否误删了换行符或导致了 unmatched brace
  - **Commit**: 仅 stage `chapters/ch02_framework.tex`，提交信息说明为"改善 2.3.3 节量纲分析过渡"

## Final verification wave
- [x] F1. 编译通过：`xelatex main.tex` 无 error（含参考文献完整流程）
- [x] F2. 逻辑连贯：阅读 2.3.3 节，确认"运动方程量纲必须一致"不再突兀

## Commit strategy
单文件单 commit：`chapters/ch02_framework.tex`

## Success criteria
- `xelatex main.tex` 编译无 error
- 2.3.3 节阅读体验改善，逻辑过渡自然
