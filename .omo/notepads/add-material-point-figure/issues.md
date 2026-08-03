# Issues — add-material-point-figure

Problems and gotchas encountered during work on this plan.

_Auto-scaffolded by /start-work. Append new entries below - never overwrite._

---

## 2026-08-03 图 2.1 (a)(b) 两栏重叠 — 已修复

**现象**：用户反馈图 2.1（fig:material-point-comparison）左右两栏（a）经典局部模型与（b）近场动力学非局部模型重叠在一起。

**根因**（pymupdf 像素级定位）：TikZ 的 `xshift` 是 `<dimension>` 参数，**裸数字默认单位为 pt 而非 cm**。`\begin{scope}[xshift=6]` 实际只平移 6pt≈0.21cm，右 panel 与左 panel 几乎完全叠合（两 panel 中心间距仅 6pt）。修复前 PDF 中右 panel 的 H_x 圆（r=2.0cm）直接覆盖左 panel 圆（r=0.7cm），f/ξ/δ/x' 标注全部落在左 panel 元素上。

**修复**：`xshift=6` → `xshift=6cm`（ch02_framework.tex 第 39 行，唯一改动）。

**验证**（170dpi 像素列投影 + 矢量元素坐标）：
- 修复前：图内容 x∈[504,856]px（宽 5.3cm），**无任何 >15px 空隙** → 两栏叠合
- 修复后：图内容 x∈[323,1045]px（宽 10.8cm），两栏之间 **110px≈1.64cm 纯空白带**
- 矢量验证：左圆 x∈[160,200]pt、右圆 x∈[294,407]pt，间隙 93.6pt≈3.3cm；所有标注（无穷小邻域、σ/∇u、H_x、f、ξ、δ、x'、（a）（b））均在自己的栏内、无侵入
- xelatex 两遍零 error，无 undefined reference

**遗留风险（未在本任务范围修复）**：fig:boundary-truncation（第 132 行 `\begin{scope}[xshift=5.5]`）存在**相同 bug**——5.5pt 位移导致 (a) 内部物质点与 (b) 边界物质点两个矩形完全叠合（第 30 页文字坐标证实两 panel 标注重叠）。建议另行修复为 `xshift=5.5cm`。

**教训**：TikZ 中所有尺寸参数（xshift/yshift/radius 等）裸数字默认 pt。写分栏图必须显式写 cm；验证图不能依赖单次目视，应提取 PDF 元素坐标或做像素投影定量检查。

## 2026-08-03 fig:boundary-truncation 同类 xshift 单位陷阱 — 已修复（用户批准）

**现象**：图 2.3（fig:boundary-truncation，2.1.4 节族）(a) 内部物质点与 (b) 边界物质点两个 panel 叠合。

**根因**：与图 2.1 相同——`\begin{scope}[xshift=5.5]` 裸数字默认 pt，仅平移 5.5pt≈0.19cm，两矩形（各宽 4cm）98.7% 面积重合。

**修复**：ch02_framework.tex 第 177 行 `xshift=5.5` → `xshift=5.5cm`（唯一改动，panel 内部坐标/标注/caption/label 全不变）。

**验证**（pymupdf 矢量坐标，第 30 页，scale=1.1，1 单位=31.3pt）：
- 修复前：两物质点中心相距 34.5pt，H_x（完整）[256,313] 与 H_x（截断）[222,279] 完全叠合，(a)(b) 子图标注互相压盖
- 修复后：(a) 矩形 x∈[135,260]，(b) 矩形 x∈[307,432]，**矩形间隙 46.4pt≈1.63cm**（与图 2.1 间隙 1.64cm 一致）；H_x（完整）[169,226] vs H_x（截断）[300,357] 分离；子图标注（a）[154,235] vs（b）[325,407] 分离；两 B 标注、族内点均各居其栏；图总宽 11cm < textwidth
- xelatex 两遍零 error，无 undefined reference；图 2.3 编号未变

**结论**：5.5cm 与原设计意图同量级（与图 2.1 的 6cm 一致），保持 5.5cm 未微调。


