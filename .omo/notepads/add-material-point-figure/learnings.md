# Learnings — add-material-point-figure

Conventions, patterns, and successful approaches discovered during work on this plan.

_Auto-scaffolded by /start-work. Append new entries below - never overwrite._

---
## [2026-08-03] 修复: xshift 单位陷阱
- TikZ scope 的 xshift/yxshift 裸数字默认单位是 **pt** 不是 cm！xshift=6 只平移 6pt(0.21cm)，导致 fig:material-point-comparison 的 (a)(b) 两栏几乎完全叠合（用户反馈重叠）。
- 修复: 第 39 行 xshift=6 -> xshift=6cm。两圆中心距验证 = 170pt ≈ 6.0cm，间隙 93.6pt ≈ 3.3cm，分离正常。
- **同类潜在 bug**: fig:boundary-truncation（第 132 行 xshift=5.5）同样叠合，需用户决策是否修复为 5.5cm。
- 验证方法备忘: 模型不能看图，用 pymupdf get_drawings 找圆 rect（直径近似: 0.7cm->39.7pt, 2.0cm->113.4pt）+ get_text words 定位标注 x 范围，几何判断重叠，比目视可靠。中文输出需设置 PYTHONIOENCODING=utf-8 或避免 print 中文（gbk 编码报错）。
