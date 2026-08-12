# ch02_framework.tex 修改计划

## TODOs

1. [x] 修改 1：客观性 → 旋转不变量（ch02_framework.tex 第546-548行区域：删除独立图引句，改写中心力条件引导段，引入 I₁, I₂, I₃ 不变量、w=ŵ(I₁,I₂,I₃) 一般形式与 |ξ+η|=√(I₁²+2I₃+I₂²) 桥梁）
2. [x] 修改 2：链式法则推导 + 图2.9位置（ch02_framework.tex 第553-558行区域：补 ∇_η|ξ+η| 中间步骤，图引用移到中心力条件自动满足之后）
3. [x] 修改 3：补充"独立不变量"解释段落（ch02_framework.tex 第549行 `\]` 与第550行"因此满足客观性…"之间插入一段，解释"为什么恰好有三个独立旋转不变量"及等价不变量组）

## 修改 1：客观性 → 旋转不变量（第548行前后）

**目标位置**：`ch02_framework.tex` 第546-548行

### 原文（删除）

```latex
如图\ref{fig:pairwise-potential}所示：成对势 $w$ 在键两端对称，导出的对力 $\mathbf{f}$ 沿变形后键方向作用（蓝色箭头）。

关于中心力条件，需对成对势的形式作进一步限定。由客观性\eqref{eq:potential-objectivity}可知，$w$ 只能依赖矢量对 $(\boldsymbol{\eta},\boldsymbol{\xi})$ 的旋转不变量，即 $|\boldsymbol{\xi}|$、$|\boldsymbol{\eta}|$ 与 $\boldsymbol{\xi}\cdot\boldsymbol{\eta}$；交换对称性\eqref{eq:potential-symmetry}对这些不变量不施加新的约束。要使导出的对力满足中心力条件，$w$ 须进一步只依赖变形后键长与参考键长：
```

### 修改后

```latex
关于中心力条件，需对成对势的形式作进一步限定。由客观性\eqref{eq:potential-objectivity}可知，$w$ 对任意旋转 $\mathbf{R}$ 满足 $w(\mathbf{R}\boldsymbol{\eta},\mathbf{R}\boldsymbol{\xi})=w(\boldsymbol{\eta},\boldsymbol{\xi})$，这意味着 $w$ 只能依赖矢量对 $(\boldsymbol{\eta},\boldsymbol{\xi})$ 的旋转不变量。在三维空间中，这样的独立不变量共有三个，可取为
\[
  I_1=|\boldsymbol{\xi}|,\quad I_2=|\boldsymbol{\eta}|,\quad I_3=\boldsymbol{\xi}\cdot\boldsymbol{\eta}
\]
因此满足客观性的成对势可一般性地写为 $w=\hat{w}(I_1,I_2,I_3)$。交换对称性\eqref{eq:potential-symmetry}要求 $w$ 在 $(\boldsymbol{\eta},\boldsymbol{\xi})\to(-\boldsymbol{\eta},-\boldsymbol{\xi})$ 下保持不变；由于三个不变量 $I_1, I_2, I_3$ 均在该变换下不变（$|\boldsymbol{\xi}|$ 和 $|\boldsymbol{\eta}|$ 为模长，$\boldsymbol{\xi}\cdot\boldsymbol{\eta}$ 中两矢量同时反号时点积不变），故交换对称性不施加额外的约束。

要使导出的对力满足中心力条件，需让 $\nabla_{\boldsymbol{\eta}}w$ 的方向与 $\boldsymbol{\xi}+\boldsymbol{\eta}$ 一致。注意到 $|\boldsymbol{\xi}+\boldsymbol{\eta}|$ 可由上述三个不变量表示为 $|\boldsymbol{\xi}+\boldsymbol{\eta}|=\sqrt{I_1^2+2I_3+I_2^2}$，因此若 $w$ 仅以 $|\boldsymbol{\xi}+\boldsymbol{\eta}|$ 和 $|\boldsymbol{\xi}|$ 为自变量，即
```

---

## 修改 2：链式法则推导 + 图2.9位置（第553-558行）

**目标位置**：`ch02_framework.tex` 第553-558行

### 原文（删除）

```latex
此时由链式法则
\begin{equation}
  \mathbf{f}(\boldsymbol{\eta},\boldsymbol{\xi}) = \nabla_{\boldsymbol{\eta}} w = \frac{\partial \hat{w}}{\partial |\boldsymbol{\xi}+\boldsymbol{\eta}|}\,\frac{\boldsymbol{\xi}+\boldsymbol{\eta}}{|\boldsymbol{\xi}+\boldsymbol{\eta}|}
  \label{eq:central-force-derivation}
\end{equation}
$\mathbf{f}$ 与 $\boldsymbol{\xi}+\boldsymbol{\eta}$ 共线，故中心力条件\eqref{eq:central-force}自动满足。键基模型（第 4 章）所采用的成对势均属此类。
```

### 修改后

```latex
则由链式法则，利用
\[
  \nabla_{\boldsymbol{\eta}}|\boldsymbol{\xi}+\boldsymbol{\eta}| = \frac{\boldsymbol{\xi}+\boldsymbol{\eta}}{|\boldsymbol{\xi}+\boldsymbol{\eta}|}
\]
得
\begin{equation}
  \mathbf{f}(\boldsymbol{\eta},\boldsymbol{\xi}) = \nabla_{\boldsymbol{\eta}} w = \frac{\partial \hat{w}}{\partial |\boldsymbol{\xi}+\boldsymbol{\eta}|}\,\frac{\boldsymbol{\xi}+\boldsymbol{\eta}}{|\boldsymbol{\xi}+\boldsymbol{\eta}|}
  \label{eq:central-force-derivation}
\end{equation}
此时 $\mathbf{f}$ 与 $\boldsymbol{\xi}+\boldsymbol{\eta}$ 共线，故中心力条件\eqref{eq:central-force}自动满足。如图\ref{fig:pairwise-potential}所示，成对势 $w$ 的上述形式保证了对力 $\mathbf{f}$ 沿变形后键方向作用（蓝色箭头），同时满足反作用条件和中心力条件。键基模型（第 4 章）所采用的成对势均属此类。
```

---

## 修改 3：补充"独立不变量"解释段落（第549行后）

**目标位置**：`ch02_framework.tex` 第549行 `\]` 之后，第550行"因此满足客观性的成对势可一般性地写为 $w=\hat{w}(I_1,I_2,I_3)$"之前

### 修改原因

用户反馈"三个不变量的引入，也不好理解"。原文从客观性直接给出 I₁, I₂, I₃，未解释：
1. 为什么一对向量 (**η**, **ξ**) 的独立旋转不变量恰好是三个（6 个分量 − SO(3) 的 3 个旋转自由度 = 3 个独立不变量）
2. I₁, I₂, I₃ 的选取并非唯一，存在等价不变量组（如 |**ξ**+**η**|, |**ξ**−**η**|, **ξ**·**η**）

### 修改后

**oldString：**

```latex
\]
因此满足客观性的成对势可一般性地写为 $w=\hat{w}(I_1,I_2,I_3)$。交换对称性
```

**newString：**

```latex
\]

这三个量之所以是``独立''的，是因为一对向量 $(\boldsymbol{\eta},\boldsymbol{\xi})$ 共有六个分量，而三维空间中的旋转（保内积变换）消去了三个自由度，因此独立旋转不变量恰好为三个。读者也可选择其他等价的不变量组，例如以 $|\boldsymbol{\xi}+\boldsymbol{\eta}|$、$|\boldsymbol{\xi}-\boldsymbol{\eta}|$ 和 $\boldsymbol{\xi}\cdot\boldsymbol{\eta}$ 为基，它们与 $I_1,I_2,I_3$ 之间可以相互表示；但无论选取哪组不变量，满足客观性的最一般成对势都是等价的。

因此满足客观性的成对势可一般性地写为 $w=\hat{w}(I_1,I_2,I_3)$。交换对称性
```

### 编译验证

修改后需执行：
```powershell
xelatex main.tex
bibtex main
xelatex main.tex
xelatex main.tex
```

---

## 修改说明

### 修改原因

原文存在4处逻辑跳跃，导致"成对势须满足两个基本对称性"到"中心力条件自动满足"之间的推导链条断裂：

1. **客观性 → "只能依赖旋转不变量"**：原文直接给出结论，未说明三维空间中两个矢量的独立旋转不变量恰好是 |ξ|, |η|, ξ·η
2. **交换对称性 → "不施加新的约束"**：原文未验证三个不变量在 (η, ξ)→(-η, -ξ) 变换下的行为
3. **"三个不变量" → "只依赖 |ξ+η| 和 |ξ|"**：原文直接跳跃，未说明 |ξ+η| 如何用三个不变量表示
4. **链式法则一步到位**：原文缺少 ∇_η|ξ+η| = (ξ+η)/|ξ+η| 这一关键中间步骤

### 修改后逻辑链

```
客观性 → 旋转不变量（I₁,I₂,I₃）→ 一般形式 w=ŵ(I₁,I₂,I₃)
   ↓
交换对称性 → 对 I₁,I₂,I₃ 无额外约束（说明原因）
   ↓
中心力条件 → 需 ∇w ∥ (ξ+η) → 引入 |ξ+η|=√(I₁²+2I₃+I₂²)
   ↓
链式法则 → ∇_η|ξ+η|=(ξ+η)/|ξ+η| → f ∥ (ξ+η) → 自动满足中心力条件
   ↓
图2.9 → 总结：力沿键方向，满足所有条件
```

### 编译验证

修改后需执行：
```powershell
xelatex main.tex
bibtex main
xelatex main.tex
xelatex main.tex
```

## Final Verification Wave

F1. [x] 编译验证：xelatex×3 + bibtex 无 error、无 undefined reference/citation 警告
F2. [x] 文本通读：修改后的 2.3.2 节逻辑链完整（客观性→不变量→交换对称性→中心力条件→图2.9），无跳跃、无未定义符号
