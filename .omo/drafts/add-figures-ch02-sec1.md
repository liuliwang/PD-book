---
slug: add-figures-ch02-sec1
status: drafting
intent: clear
review_required: false
pending-action: write .omo/plans/add-figures-ch02-sec1.md
approach: 在 ch02_framework.tex 第2.1节中新增3-4幅TikZ自绘教学插图，按子节分布在键、族等关键概念处，正文添加\ref引用，并在编译验证后确认无误。
---

# Draft: add-figures-ch02-sec1

## Components (topology ledger)
<!-- Lock the SHAPE before depth. One row per top-level component that can succeed or fail independently. -->
<!-- id | outcome (one line) | status: active|deferred | evidence path -->

| id | outcome | status | evidence |
|----|---------|--------|----------|
| C1 | 图A：键的运动学详图（2.1.2节，ξ与ξ+η的参考→变形构型对比） | active | ch02_framework.tex:16-24 |
| C2 | 图B：边界截断与族不完整（2.1.4节，内部vs边界物质点的H_x和F_x对比） | active | ch02_framework.tex:49-57 |
| C3 | 图C：键伸长三态对比（2.1.2节，s>0/s=0/s<0三态，可并入A） | active | ch02_framework.tex:24 |
| C4 | 图D（可选）：四概念层级关系图（2.1节末尾注记附近） | deferred | ch02_framework.tex:101-103 |
| C5 | 编译验证：xelatex ×2 + bibtex，确认无error/undefined ref | active | main.tex |
| C6 | 交叉引用验证：正文中对所有新图的\ref调用均正确解析 | active | ch02_framework.tex |

## Open assumptions (announced defaults)
<!-- assumption | adopted default | rationale | reversible? -->

| assumption | adopted default | rationale | reversible? |
|-----------|----------------|-----------|-------------|
| 插图类型 | 全部TikZ自绘 | 2.1节为基础概念定义章节，适合干净的教学示意图；现有figures/目录无可直接借用的合适图源 | yes |
| 图C放置 | 优先与图A合并为单图（多panel） | 减少插图总数，保持2.1节简洁；若视觉拥挤则独立为单独figure | yes |
| 图片来源标注 | 无需cite | 全部为原创TikZ教学图，非论文摘图 | n/a |
| 图注格式 | 遵循preamble.tex配置：labelsep=quad，无冒号 | 全局一致 | no |
| 编译环境 | XeLaTeX (MiKTeX 26.5)，已配置 | 项目AGENTS.md规定 | no |

## Findings (cited - path:lines)

- 2.1节仅1幅图：`fig:family-horizon` (ch02_framework.tex:60-90)，TikZ自绘，综合展示四概念
- 第1章插图风格：TikZ自绘5幅 + CC-BY论文图4幅 (ch01_introduction.tex)
- bibliography.bib已有所需引用：Silling2000, Bobaru2009, LeBobaru2018, Mitchell2015
- preamble.tex已配置TikZ、graphicx、caption(labelsep=quad)等所需宏包
- main.tex结构不动——编辑只针对ch02_framework.tex
- 图注全局格式：labelsep=quad（编号与文字间无冒号，空格分隔）
- 符号表已登记2.1节全部符号 (notation.tex:4-23)

## Decisions (with rationale)

1. **图A设计为上下双panel对比图**：上=参考构型（实线ξ），下=变形构型（ξ+η虚线），η独立标注。理由：这是全书运动学几何基础，需要清晰的一对一对比。
2. **图B设计为左右双panel对比图**：左=内部物质点（完整H_x，完整F_x），右=边界物质点（截断H_x，残缺F_x，截断处虚线标示）。理由：直观解释表面效应因果链。
3. **图C优先与图A合并**：在A的变形构型panel中用颜色区分s>0/s=0/s<0三种键。独立成图仅作为备选。
4. **图D作为可选（deferred）**：若前三幅图后2.1节插图密度合适则加入，否则省略。层级关系在注记中已有文字说明。
5. **编译流程**：xelatex ×2 → 检查log无undefined reference/citation warning → 产物main.pdf验证。

## Scope IN

- `ch02_framework.tex`：在2.1.2节（键）和2.1.4节（族）中分别插入TikZ插图
- 为每幅新图添加`\label{}`和对应的正文`\ref{}`引用
- 为每幅新图添加`\caption{}`（符合labelsep=quad格式）
- 编译验证：xelatex ×2，确保无编译错误、无undefined reference
- 图注中若涉及引用（如图B边界效应引LeBobaru2018/Mitchell2015），添加`\cite{}`

## Scope OUT (Must NOT have)

- 不修改 `main.tex`（文件结构不动）
- 不修改 `preamble.tex`（宏包和配置不动）
- 不修改 `frontmatter/notation.tex`（2.1节符号已完整登记）
- 不新增 `bibliography.bib` 条目（所有引用已存在）
- 不新增 `figures/` 目录下的外部图片（全部TikZ inline）
- 不修改其他章节文件
- 不改变现有图2.1 (`fig:family-horizon`) 的内容和位置

## Open questions

无。所有设计决策基于代码库探索和教学效能分析完成，无需要用户决定的遗留分歧。

## Approval gate
status: approved → generating plan
approved_at: 2026-08-03
