# optimize-fig-22-reference-deformation - Work Plan

## TL;DR (For humans)

**What you'll get**: 优化图 2.6（fig:reference-deformation）的 TikZ 代码，解决 5 个视觉表达问题，提升读者对参考构型→变形构型映射关系的理解。

**Why this approach**: 当前图 2.6 存在关键遗漏（右栏缺少 y(x',t) 点）和表达不足（位移矢量 u 位置不明确、左右栏映射关系弱），需要系统性修复。

**What it will NOT do**: 不会修改其他图、章节文字、公式或标签。

**Effort**: 小（~1 个文件，TikZ 代码修改）。

**Risk**: 低。TikZ 语法错误可通过编译验证即时发现。

**Decisions**: 用户确认执行全部 5 个优化方向。

## Scope

### In Scope
- 在 `chapters/ch02_framework.tex` fig:reference-deformation（lines 275-305）进行 TikZ 代码修改
- 方向 1：右栏补全 y(x',t) 对应点（关键遗漏）
- 方向 2：位移矢量 u 的起点位置优化
- 方向 3：强化左右两栏映射对应关系
- 方向 4：图注与正文配合优化
- 方向 5：视觉细节微调（颜色、线型、对齐等）
- 编译验证与交叉引用检查

### Out of Scope / Must-NOT-Have
- 不修改任何其他图的内容或 label
- 不修改章节文字叙述（除 caption 外）
- 不修改公式或章节结构
- 不改变现有图号分配

## Verification strategy

1. **编译验证**: `xelatex -interaction=nonstopmode main.tex` 零 error
2. **视觉检查**: 右栏包含 y(x',t) 点，位移矢量 u 位置明确，左右栏映射关系清晰
3. **交叉引用验证**: 确认 label/ref 未被破坏

## Execution strategy

单次编辑波次：在 `ch02_framework.tex` 中修改 fig:reference-deformation 的 TikZ 代码。无需外部依赖。

## Todos

- [x] 1. 补全右栏 y(x',t) 对应点及变形键表示（关键遗漏）
  - **References**: `chapters/ch02_framework.tex` lines 290-299（fig:reference-deformation 右栏）
  - **Acceptance criteria**:
    - 右栏包含 y(x',t) 点（红色圆点，带标签）
    - 变形键 ξ+η 完整连接 y(x,t) 和 y(x',t)
    - 键的箭头方向从 y(x,t) 指向 y(x',t)
  - **Happy QA**:
    - 编译零 error
    - PDF 渲染显示两个红点及连接键
  - **Failure QA**:
    - 若右栏显示异常，检查 TikZ 坐标是否与左栏 x' 对应
  - **Commit**: `chapters/ch02_framework.tex`

- [x] 2. 优化位移矢量 u 的起点位置
  - **References**: `chapters/ch02_framework.tex` lines 291-293
  - **Acceptance criteria**:
    - 蓝色 u 箭头明确表示从参考位置 x 到当前位置 y(x,t) 的位移
    - 箭头起点与左栏 x 点在水平或垂直方向上形成对应关系
  - **Happy QA**:
    - PDF 渲染中 u 箭头的物理含义清晰可辨
  - **Failure QA**:
    - 若 u 箭头含义模糊，调整起点位置或添加辅助虚线

- [x] 3. 强化左右两栏映射对应关系
  - **References**: `chapters/ch02_framework.tex` lines 277-300（完整图代码）
  - **Acceptance criteria**:
    - 添加从左栏到右栏的隐式或显式映射线索（如对齐、颜色对应、辅助线等）
    - 或保持两栏相对位置一致，让读者自然对应
  - **Happy QA**:
    - 左右两栏的对应关系直观可辨
  - **Failure QA**:
    - 若对应关系仍不清晰，考虑添加虚线箭头或同色标记

- [x] 4. 图注与正文配合优化
  - **References**: `chapters/ch02_framework.tex` line 301-305
  - **Acceptance criteria**:
    - Caption 保持简洁（无冒号），必要时微调文字
    - 正文引用句适当补充对键变形的描述
  - **Happy QA**:
    - Caption 符合项目规范（无冒号）
    - 正文与图的描述不重复、互补
  - **Failure QA**:
    - 若 caption 过长，精简并移入正文

- [x] 5. 视觉细节微调
  - **References**: `chapters/ch02_framework.tex` lines 277-300
  - **Acceptance criteria**:
    - 颜色、线型、对齐等细节与全书风格一致
    - 近场域圆线型与 fig:horizon-definition 一致
    - 子图标注 (a)(b) 位置正确
  - **Happy QA**:
    - 与现有图（如 fig:bond-geometry）风格一致
  - **Failure QA**:
    - 若颜色对比度不足，调整 fill opacity 或线条粗细

## Final verification wave

- [x] F1. 编译门禁：连续两次 `xelatex -interaction=nonstopmode -halt-on-error main.tex` 零 error
- [x] F2. 交叉引用完整性：`grep "fig:reference-deformation" chapters/ch02_framework.tex` 命中 ≥2（label + ref）
- [x] F3. 视觉验证：PDF 中右栏显示 y(x',t) 点，u 箭头含义清晰，左右栏映射关系明确

## Commit strategy

单文件单 commit：

```
ch02: 优化图2.6参考构型与变形构型映射示意图

- 补全右栏 y(x',t) 对应点及变形键
- 优化位移矢量 u 位置表达
- 强化左右两栏映射对应关系
- 微调视觉细节（颜色、线型、对齐）
- 编译验证零错误
```

## Success criteria

1. 图 2.6 右栏完整显示 y(x,t) 和 y(x',t) 两个点及变形键 ξ+η
2. 位移矢量 u 的起点和含义明确
3. 左右两栏的映射对应关系直观可辨
4. Caption 和正文引用协调一致
5. `xelatex main.tex` 连续运行两次零 error
