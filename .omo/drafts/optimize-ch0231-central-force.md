# Draft: optimize-ch0231-central-force

## Intent
- **intent**: CLEAR
- **review_required**: false

## Request
优化 `chapters/ch02_framework.tex` 中 2.3.1 节（"对力函数的物理意义"）关于中心力条件的文字说明，让读者更容易理解为什么中心力条件可以写成式 (2.23) 的形式。

## Current State
- 当前文字从叉积为零直接跳到 `f = (ξ+η)/|ξ+η| · g(|ξ+η|, ξ)`，缺少中间推导链条
- 读者（特别是研究生水平的读者）可能难以理解叉积为零与力可以表示为方向向量乘以标量函数之间的等价关系

## Approach
在现有段落基础上增加中间推导步骤：
1. 先解释叉积为零的几何意义（两向量平行/共线）
2. 展示从叉积为零到 f = λ(ξ+η) 的推导
3. 解释为什么 λ 可以写成 g(|ξ+η|, ξ)/|ξ+η| 的形式
4. 解释 g 的物理意义和依赖关系

## Components
1. `chapters/ch02_framework.tex` 第 436-447 行（中心力条件段落）的内容改写

## Status
- awaiting-approval
- approach: 文字改写，不涉及公式变更
