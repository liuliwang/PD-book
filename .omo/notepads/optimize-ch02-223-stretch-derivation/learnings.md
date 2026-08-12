# Learnings — optimize-ch02-223-stretch-derivation

Conventions, patterns, and successful approaches discovered during work on this plan.

_Auto-scaffolded by /start-work. Append new entries below - never overwrite._

---

## 2026-08-06: 2.2.3 节可读性优化（修改点 A + B）

### 修改点 A（第 367 行附近）
- **问题**：原文 `$O(|\boldsymbol{\eta}|^{2})$` 表述歧义，读者困惑为何 $O(|\boldsymbol{\eta}|^{2})$ 本身就是高阶的。
- **解决**：重写为显式说明根号内各项除以 $|\boldsymbol{\xi}|^{2}$ 后的贡献量级——线性项 $2\,\boldsymbol{\xi}\cdot\boldsymbol{\eta}_{\parallel}/|\boldsymbol{\xi}|^{2}$ 为 $O(|\boldsymbol{\eta}|/|\boldsymbol{\xi}|)$（一阶），而 $|\boldsymbol{\eta}_{\parallel}|^{2}/|\boldsymbol{\xi}|^{2}$ 与 $|\boldsymbol{\eta}_{\perp}|^{2}/|\boldsymbol{\xi}|^{2}$ 为 $O(|\boldsymbol{\eta}|^{2}/|\boldsymbol{\xi}|^{2})$（二阶），从而消除歧义。
- **关键**：通过"除以 $|\boldsymbol{\xi}|^{2}$ 后"的视角转换，让读者直接看到各项对伸长率 $s$ 的量级贡献，而非抽象的 $O(|\boldsymbol{\eta}|^{2})$。

### 修改点 B（第 386 行后）
- **问题**：式 (2.14) 得出"偏斜分量为高阶小量"后，缺少物理直观解释。
- **解决**：在"这一结果有一个重要推论"之前，于同一段落中插入解释句："其物理含义是：键的伸长主要由轴向分量引起，而偏斜分量仅使键发生偏转、对键长的改变是二阶效应，这类似于经典小应变理论中刚体转动不产生应变。"
- **约束**：未新增 `\begin{remark}` 环境（全章 remark 仍为 4 条），解释句融入现有段落，避免孤立短段。

### 验证结果
- `\begin{remark}` 数量：4 条（未变）
- 公式、label、eqref、cite 均未改动
- 修改仅涉及叙述性文字，未引入列表环境
