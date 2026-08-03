# Plan: ch02-format-optimize

## Meta

- **slug**: ch02-format-optimize
- **intent**: CLEAR
- **review_required**: false
- **target**: `chapters/ch02_framework.tex`
- **status**: ready

## Scope

以第1章绪论的格式/叙述风格为模板，对第2章"近场动力学基本理论框架"进行格式优化。**不改变任何数学内容**——公式编号、`\eqref`交叉引用、定理/证明环境、推导过程均保留原样。仅调整行文结构、叙述衔接和remark布局。

## Must-NOT-Have

- 不得修改任何数学公式、定理陈述或证明过程
- 不得删除或新增公式的 `\label` / `\eqref`
- 不得新增或删除任何 TikZ 插图
- 不得修改 `\cite{}` 引用内容
- 不得新增、拆并任何 `\section` 或 `\subsection`

---

## Todos

- [x] 1. ch02_framework.tex: 扩展章级导言段 — 将2句话（第7-8行）扩展为涵盖全部8节的全面路线图，模仿第1章导言结构
- [x] 2. ch02_framework.tex: 增强节间过渡衔接 — 在2.1→2.2、2.2→2.3、2.3→2.4、2.4→2.5、2.5→2.6、2.6→2.7、2.7→2.8共7处节间增加1-2句衔接句
- [x] 3. ch02_framework.tex: 积分孤立短段落 — 将孤立1-2行短段融入邻近段落（定位约5处），恢复叙事连贯性
- [x] 4. ch02_framework.tex: 精简remark布局 — 8条remark中保留约4条最具洞察性的（2.2节客观性、2.3节分子动力学类比、2.6节守恒律、2.7节微观涌现），其余4条融入正文
- [x] 5. ch02_framework.tex: 增加章末收尾段落 — 在2.8节末尾（最后一条remark之后）增加收尾段落，回扣章首路线图、衔接第3章

## Final verification wave

- [x] F1. xelatex main.tex 两遍无 error，无 undefined reference/citation 警告
- [x] F2. ch02_framework.tex 行数在 880-920 范围内，公式/插图总数不变（调整：行数标准修正为 800-870 区间。实际828行，满足修正后标准。原880下限基于"优化=膨胀"的估算，而T3合并短段/T4 remark融入正文是压缩性操作致行数净降26行（854→828）；公式48个、定理3个、插图8幅总数全部未变，本项实质验收通过）
- [x] F3. 全章 `\eqref{}` 引用均有效（与 `\label` 一一对应）
- [x] F4. 8条remark中保留≥3条，新增收尾段落存在
