# 第5章撰写工作笔记

## 任务
撰写 chapters/ch05_bond_improved.tex（键型模型的改进与扩展），结合专著现有内容，目录可调整优化。

## 已确认决策
- 用户选择选项 A：补充真实 bib 条目（共轭键、微梁模型）
- 已新增 3 条 bib 条目：WangZhouShou2017（共轭键原始文献）、WangZhouWang2018（共轭键3D）、DianaCasolo2019（微极键型广义化）；Gerstle2007 已在库中（微梁概念源头）
- ZhouWang2016/WangZhou2016 为扩展 NOSB 文献，与共轭键无关，不冲突

## 第5章结构（待撰写确认）
- 5.1 考虑长程力空间衰减的修正（5.1.1 影响函数与衰减核类型 / 5.1.2 近场范围、收敛性与尺度效应 / 5.1.3 衰减核与临界伸长率对断裂预测的影响）
- 5.2 微梁模型（Gerstle2007 微极键型：键=微悬臂 Euler-Bernoulli 梁，双刚度 c'、d'；DianaCasolo2019 广义化）
- 5.3 共轭键模型（WangZhouShou2017 基于修正 Stillinger-Weber 势；WangZhouWang2018 3D；动机 TrageserSeleson2020 泊松比限制）
- 5.4 键转动键型近场动力学（ZhuNi2017）
- 5.5 对偶双影响域模型（Ren2017dualhorizon）
- 5.6 面向各向异性材料的键型模型（5.6.1 单向纤维 HuHaBobaru2012 / 5.6.2 正交各向异性 Ghajari2014 / 5.6.3 键型各向异性限制 OterkusMadenci2012）
- 章末总结（衔接 ch06）

## 关键衔接
- ch06 6.1.1："第 5 章介绍的微梁模型、共轭键模型等改进方案，正是试图在键的层次引入额外的弯曲、扭转自由度来部分缓解这一困难，但这些方案本质上仍在成对相互作用的框架内修补"
- ch06 6.4："各向异性材料的键型模型对比可参见 \cite{HuHaBobaru2012,Ghajari2014}"
- ch04 为键型基础（基本假设/微势/PMB/率定/表面效应/固有局限）
- ch01 1.5.1/1.5.2 点名 ZhuNi2017、Ren2017dualhorizon

## 写作规范（AGENTS.md 强制）
- 编号公式（禁 \[...\]）、\eqref{}/\ref{} 引用、label/ref 一一对应
- 图注标题式≤300字；三线表 booktabs
- 新符号登记 notation.tex
- 禁 Markdown 语法、禁 **；remark 全章≤4条
- 每节 % --- 本节说明：... --- 注释块
- 节级导言自含；章级导言 ~10行
- 引用仅用 bib 中真实 cite key
- AI 输出声明推导需人工复核

## 编译
xelatex main.tex -> bibtex main -> xelatex x2（本会话本地执行，不委托子代理）

## 2026-08-08 第5章撰写完成
- ch05_bond_improved.tex: 398行，6节+章末总结，23公式+48label+4remark
- notation.tex: 新增第5章小节，20条符号（L96，第6/7章之间）
- bibliography.bib: 新增 WangZhouShou2017/WangZhouWang2018/DianaCasolo2019（用户选选项A）
- 最终编译: xelatex x3 + bibtex 全部 exit 0，无 error/undefined/Overfull；第5章位于 PDF 第53页起
- 经验: ①子代理必须复用原session（新session会循环卡死）②"no file changes"是git误报 ③L398孤立}、L305下标未闭合是子代理常见错误，编译前必须人工核查花括号平衡 ④PowerShell regex对中文/UTF8有转义误报，用Grep工具替代
- 待作者人工复核: 所有推导已标注"该推导需作者人工复核"；C1-C9标定系数待定（DianaCasolo2019对照）

## [2026-08] AGENTS.md 维护完成
- 用户要求更新项目 AGENTS.md（就地改进非重写）
- 主会话纠错2处：ch05 完成度（398行已完整）、bib 条数 121→124、新增"编译执行细节"（清理辅助文件/重定向/长超时/检查点）
- 子代理（ses_0207c647effe6iep4k4YbND1kc）补充2项：符号冲突预警（θ膨胀/φ损伤/α(x)morphing/R旋转 已占用；第5章避让先例 ϑ/φ_b/β_b）、子代理委托注意3条（no-file-changes误报须git diff核实/花括号平衡人工核查/多轮撰写复用session）
- 注意：子代理声称 appC-E 为1行与实测2行不符，但其最终写入"1–2行占位空文件"为安全表述
- 文件 165→168 行
