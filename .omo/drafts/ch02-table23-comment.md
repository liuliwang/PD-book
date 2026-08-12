---
slug: ch02-table23-comment
status: drafting
intent: clear
review_required: false
pending-action: write .omo/plans/ch02-table23-comment.md
approach: 在 chapters/ch02_framework.tex 表 2.3（tab:dim-analysis）与后文"量纲推导给出了…"段之间插入一段表内容说明文字（约 2-3 行 LaTeX 源码），单文件单处插入
---

# Draft: ch02-table23-comment

## Components (topology ledger)
<!-- Lock the SHAPE before depth. One row per top-level component that can succeed or fail independently. -->
<!-- id | outcome (one line) | status: active|deferred | evidence path -->
<!-- comp-1 | 插入表 2.3 说明段并编译验证 | active | chapters/ch02_framework.tex -->

## Open assumptions (announced defaults)
<!-- Record any default you adopt instead of asking, so the user can veto it at the gate. -->
<!-- assumption | adopted default | rationale | reversible? -->
<!-- 说明段不涉及与经典应力 N/m^2 的深入对比 | 该对比已由后文 673 行段承担，避免重复 | 段落职责分离 | 可逆 -->

## Findings (cited - path:lines)
- chapters/ch02_framework.tex:657 —— 表前引导句"为清晰展示运动方程各项的量纲关系，表~\ref{tab:dim-analysis}汇总了惯性项、体力、对力及其积分后的量纲对比。"
- chapters/ch02_framework.tex:661-671 —— 表 2.3（tab:dim-analysis）：四行（惯性项 N/m^3、体力 N/m^3、对力 N/m^6、积分后 N/m^3）
- chapters/ch02_framework.tex:673 —— 表后直接是"量纲推导给出了 $\mathrm{N}/\mathrm{m}^{6}$ 的代数来源，但其物理含义仍需进一步阐释。…"（与经典应力 $\boldsymbol{\sigma}$ 的 $\mathrm{N}/\mathrm{m}^{2}$ 对比）
- 表后无任何对表内内容的文字转述：N/m^3 vs N/m^6 的两组量纲对比、"积分降维"机制均未在正文点明 → 表与正文断层

## Decisions (with rationale)
- 插入位置：`\end{table}`（671 行）之后、673 行"量纲推导给出了…"段之前，独立成段（前后空行）
- 定稿文本（逐字插入，不得改动措辞）：
  ```
  表~\ref{tab:dim-analysis} 显示，惯性项与体力均为 $\mathrm{N}/\mathrm{m}^{3}$ 的力密度，而对力函数 $\mathbf{f}$ 的量纲为 $\mathrm{N}/\mathrm{m}^{6}$，高出一个体积维度；经积分 $\int\mathbf{f}\,\mathrm{d}V'$ 后又回到 $\mathrm{N}/\mathrm{m}^{3}$，与左端惯性项一致。这一升一降正是运动方程结构自洽的体现。
  ```
- 理由：转述表内两组量纲对比 + 点明积分降维机制；不提前剧透 673 段的"经典应力对比"内容（职责分离，避免重复）
- 不改变任何公式编号、\label、\eqref、\cite

## Scope IN
- `chapters/ch02_framework.tex`：表 2.3 后插入说明段（约 2-3 行源码 + 前后空行）

## Scope OUT (Must NOT have)
- 其他所有文件；表 2.3 内容本身；673 行及以后所有段落；公式编号/引用；compile 验证由编排者本地执行

## Open questions
- 无（方案已定稿）

## Approval gate
status: awaiting-approval
<!-- When exploration is exhausted and unknowns are answered, set status: awaiting-approval. -->
<!-- That durable record is the loop guard: on a later turn read it and resume at the gate instead of re-running exploration. -->
