# Learnings — add-horizon-definition-figure

Conventions, patterns, and successful approaches discovered during work on this plan.

_Auto-scaffolded by /start-work. Append new entries below - never overwrite._

---
## [2026-08-04] 任务完成：图2.4 fig:horizon-definition 插入 2.1.3 节
- 位置：eq:horizon 后（第155行引用+第157-183行图块），label 第182行，图号自动分配 2.4
- 规格：虚线圆 circle(2.2)、中心点2.5pt node[below left]{x}、半径标注 dash dot gray thin 圆心至(2.2,0) midway below δ、圆内4点+thick键、圆外3灰点不连线
- 图注标题式无冒号：近场域 H_x 的定义示意
- 关键教训：图描述不得与正文定义逐字重复（曾违反被修复，改为纯图形语言）
- 视觉验证法：PDF 矢量几何（pymupdf get_drawings）比 look_at 可靠，look_at 对细灰线/灰点有 3 轮误读
- 编译验证：xelatex 两遍 exit 0，main.pdf 141页（当时含family-horizon）
- 后续：boulder 已切换到 remove-fig26-family-horizon 计划，删除图2.6 由另一 session 执行完成
