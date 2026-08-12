# ch02_framework.tex 第 553 行修改：ŵ 意义解释

## TODOs

- [x] 1. 修改 553 行：替换突兀的不变量理论段落为"旋转轨道→新函数 ŵ"自然过渡（chapters/ch02_framework.tex）

## 修改内容

**文件**：`chapters/ch02_framework.tex`
**目标行**：553

### 原文（删除）

```latex
这一推论正是不变量理论（invariant theory）基本结果的直接应用：对三维空间中的两个矢量，旋转群 $\mathrm{SO}(3)$ 的全体不变量由三个基本不变量生成——$|\boldsymbol{\xi}|$、$|\boldsymbol{\eta}|$ 与 $\boldsymbol{\xi}\cdot\boldsymbol{\eta}$，它们恰好构成矢量对 Gram 矩阵的三个独立元素，而任意旋转不变的标量函数都必然可表示为这些基本不变量的函数。因此满足客观性的成对势可一般性地写为 $w=\hat{w}(I_1,I_2,I_3)$。
```

### 修改后

```latex
由于 $w$ 在旋转轨道上的值相同，而每个轨道又被 $(I_1,I_2,I_3)$ 唯一标记，因此 $w$ 的值完全由这三个不变量决定。换言之，$w$ 可以表示为以不变量 $(I_1,I_2,I_3)$ 为自变量的新函数。为与原来的函数 $w(\boldsymbol{\eta},\boldsymbol{\xi})$ 相区分，这个新函数记为 $\hat{w}(I_1,I_2,I_3)$。因此满足客观性的成对势可一般性地写为 $w=\hat{w}(I_1,I_2,I_3)$。
```

## 修改理由

1. **去掉突兀概念**：删除 SO(3)、不变量理论、Gram 矩阵——均未在前后文出现，风格突兀
2. **沿用既有词汇**：基于前文已定义的"旋转轨道"过渡
3. **解释 ŵ 的意义**：明确 ŵ 是以不变量 $(I_1,I_2,I_3)$ 为自变量的新函数，与原来的六分量函数 $w(\boldsymbol{\eta},\boldsymbol{\xi})$ 相区分
4. **衔接流畅**：自然承接前文 6−3=3 自由度与三个不变量的讨论

## Final Verification Wave

- [x] F1. 编译验证：xelatex×3 + bibtex 无 error、无 undefined reference/citation 警告
- [x] F2. 文本通读：修改后的过渡自然衔接（不变量→旋转轨道→新函数 ŵ），无突兀新概念，ŵ 意义明确
