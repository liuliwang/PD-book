---
slug: remove-fig26-family-horizon
status: awaiting-approval
intent: clear
review_required: false
pending-action: user 已批准（"执行"）→ plan 已写入 .omo/plans/remove-fig26-family-horizon.md
approach: 删除 ch02 图2.6（fig:family-horizon，240-270行）+ 改写 238 行正文引用指向第1章 fig:horizon-bond 与图2.5 + xelatex 编译验证
---

# Draft: remove-fig26-family-horizon

## Components (topology ledger)
- 单组件：ch02_framework.tex 中删除 fig:family-horizon 图环境并改写引用 | outcome: 删除后编译零 Error|undefined、无悬空 label | status: active | evidence: .omo/evidence/task-1-remove-fig26-family-horizon.log

## Open assumptions (announced defaults)
- 正文改写措辞由执行者按项目文风自定（Quick 级微编辑，不改动其它内容）| adopted default: 引用第1章图1.4承接几何关系+引用图2.5说明族 | rationale: 图2.6唯一增量是族标签，可并入文字 | reversible?: 是

## Findings (cited - path:lines)
- ch02_framework.tex:238 正文以 `图\ref{fig:family-horizon}综合展示了…` 开头，是唯一正文引用
- ch02_framework.tex:240-270 为 fig:family-horizon 完整 figure 环境（TikZ：中心点+近场域圆+键+变形后位置+族标签）
- ch02_framework.tex:192,194 族定义式 eq:family 与正文独立存在，不受删除影响
- ch02_framework.tex:196-236 fig:boundary-truncation（图2.5）已展示内部vs边界族差异
- ch01_introduction.tex:117-146 fig:horizon-bond（图1.4）与图2.6 视觉相似度>90%（中心点/近场域圆/键/变形后位置/ξ与ξ+η标注全同，仅差族标签）
- main.aux:208 确认 fig:family-horizon 编译编号为 2.6
- grep 确认 fig:family-horizon 全库仅 2 处（238行引用 + 269行 label）

## Decisions (with rationale)
- 删除图2.6 而非修改：与第1章图1.4 重复度>90%，符合项目"一图一主题"规范；族标签信息并入正文文字
- 保留图2.5：内容独立（表面效应/边界截断），第1章无对应
- 正文改写引用第1章图1.4（跨章引用图用 \ref，章节名手写"第 1 章"），符合项目约定

## Scope IN
- 删除 ch02 图2.6 + 改写 238 行引用 + 编译验证

## Scope OUT (Must NOT have)
- 不动第1章 fig:horizon-bond、第2章 fig:boundary-truncation、eq:family、main.tex、preamble.tex、其它章节；不 commit/push

## Open questions
- 无

## Approval gate
status: awaiting-approval
- 用户已确认图2.6 并批准执行（"执行"）→ plan 已写入 .omo/plans/，下一步：运行 $start-work 执行
