# Issues — ch02_potential-symmetry-fix

Problems and gotchas encountered during work on this plan.

_Auto-scaffolded by /start-work. Append new entries below - never overwrite._

---

## [2026-08-07] Boulder continuation 钩子误触循环（未解决，钩子侧缺陷）

- **现象**：boulder.json `status: "completed"`、计划文件 5/5 复选框 `[x]` 后，boulder continuation 钩子仍反复触发，恒报 `[Status: 0/0 completed, 0 remaining]`，无实际待办。
- **已排除**：计划文件格式问题——编号格式（`1. [ ]`/`F1. [ ]`，文档要求格式）与破折号格式（`- [ ]`）均被解析器报 'no valid task rows'；/stop-continuation 仅停会话级续跑，未阻止项目级钩子。
- **根因定位**：boulder/plan 解析器在 boulder 已 completed 后仍判定"有 active work plan"；完成判定逻辑需在 oh-my-openagent 钩子层修复（如增加 `boulder.json status=completed` 短路判断），超出本会话 .omo/*.md 作用域。
- **处理**：不虚构任务、不误标 `[~]`（无阻塞任务）。每次触发回复相同结论。

