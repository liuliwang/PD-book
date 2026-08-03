---
slug: fix-bond-stretch-definition
status: plan-complete
intent: clear
review_required: false
pending-action: write .omo/plans/fix-bond-stretch-definition.md
approach: 在 ch02_framework.tex 2.1.2 节中：将键伸长率 s 的行内公式升级为带编号的 \begin{equation}...\label{eq:bond-stretch}，统一术语"伸长"→"伸长率"，删除行内冗余重复定义，同步修正图注。
---

# Draft: fix-bond-stretch-definition

## Components (topology ledger)
| id | outcome | status | evidence path |
| -- | ------- | ------ | ------------- |
| bond-stretch-eq | s 获得编号公式 eq:bond-stretch | active | ch02_framework.tex:28 |
| terminology | "伸长"→"伸长率" 与 notation.tex 和 2.7 节统一 | active | notation.tex:21, ch02_framework.tex:644+ |
| inline-cleanup | 删除行内重复定义，图注同步 | active | ch02_framework.tex:28,74 |

## Open assumptions (announced defaults)
Record any default you adopt instead of asking, so the user can veto it at the gate.
| assumption | adopted default | rationale | reversible? |
| ---------- | --------------- | --------- | ------------ |
| 无 | — | — | — |

## Findings (cited - path:lines)
- `ch02_framework.tex:28` — 行内定义 `键的伸长（stretch）定义为 $s=(|\boldsymbol{\xi}+\boldsymbol{\eta}|-|\boldsymbol{\xi}|)/|\boldsymbol{\xi}|$`，无编号无标签
- `ch02_framework.tex:74` — 图注中重复定义 `键伸长定义为 $s=...$`
- `notation.tex:21` — 符号表官方术语：`$s$ & 伸长率（stretch）`
- `notation.tex:27` — `$s_c$ & 临界伸长率`
- `ch02_framework.tex:644+` — 2.7 节全程使用"伸长率"
- `ch02_framework.tex:79-87` — 反作用条件 `eq:reaction`、中心力条件 `eq:central-force` 均有编号（同级公式都应编号）
- `ch02_framework.tex:310` — 2.2 节线性化时「代入伸长定义」无法用 `\eqref` 引用，是引用断裂实例
- 中文 PD 文献（力学进展 2022、上海交大乔丕忠团队）统一使用"伸长率"对应 "stretch"

## Decisions (with rationale)
1. **新增编号公式** `eq:bond-stretch`：s 是全书最高频运动学量之一，地位等同于同页的 reaction/central-force 条件，不应只有行内定义
2. **术语统一为"伸长率"**：与符号表 (`notation.tex:21`)、2.7 节、以及中文 PD 文献一致；"伸长"暗示绝对伸长量（m），而 s 无量纲
3. **公式附英文术语**：`键的伸长率（bond stretch）` 保持中英对照惯例
4. **删除行内重复**：原段落中 s 的公式出现了两次（定义行 + 图引用行），编号化后只保留一处定义

## Scope IN
- `ch02_framework.tex` 第 28 行：行内公式 → `\begin{equation}...\label{eq:bond-stretch}`
- `ch02_framework.tex` 第 28 行附近：删除图引用中的重复公式
- `ch02_framework.tex` 第 74 行：图注中"键伸长"→"键伸长率"

## Scope OUT (Must NOT have)
- 不修改 `notation.tex`（已正确使用"伸长率"）
- 不修改 2.7 节（已正确使用"伸长率"）
- 不修改 `main.tex` 或 `preamble.tex`
- 不增减任何数学定义的内容，仅做编号化和术语统一
- 不添加新的 TikZ 图或修改现有图的布局

## Open questions
无。

## Approval gate
status: awaiting-approval

**探索已穷尽。所有发现基于文件原文与中文 PD 文献惯例。无剩余分叉决策。**

> **计划摘要**：在 `chapters/ch02_framework.tex` 第 28 行将键伸长率 $s$ 从行内公式升级为带编号的 `\begin{equation}...\label{eq:bond-stretch}`，同时将术语"键的伸长"统一为"键的伸长率"（与符号表及 2.7 节一致），并删除图引用文字中的冗余重复定义。共三处文本修改，全部在 2.1.2 节内。

请确认是否按此方案生成正式计划文件。
