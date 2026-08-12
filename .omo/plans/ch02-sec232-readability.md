# Plan: 第 2 章 2.3.2 节可读性优化

**文件**: `chapters/ch02_framework.tex` 第 495—545 行（2.3.2 节"微弹性材料与成对势"）  
**关联**: 第 2.3.1 节末尾（第 493—494 行）  
**目标**: 消除 8 个可读性障碍，使 2.3.2 节逻辑连贯、推导完整、物理意义清晰。  

---

## Todos

### 任务 1：在 2.3.1 节末尾增加过渡段

- [x] 1. [WHERE] 第 493 行（`\end{figure}` 之后，`\subsection{微弹性材料与成对势}` 之前）增加过渡段，预告 2.3.2 节引入势能的必要性。

**建议文本**（插入第 493 行之后）：

```latex
上述约束条件仅规定了对力函数应满足的运动学限制，但尚未回答一个根本问题：对力从何而来？
在经典弹性力学中，应力由应变能密度对变形的导数给出；类似地，若近场动力学中的相互作用也能由某个势能函数导出，则能量守恒、本构关系的建立将具备更严格的数学基础。
为此，本节引入微弹性材料假设，建立成对势的概念，并讨论其对称性、物理意义与数学结构。
```

**验收标准**：
- 编译无报错
- 过渡段自然衔接 2.3.1 和 2.3.2，明确回答了"为什么要引入势能"

---

### 任务 2：在 2.3.2 节开头补充微弹性材料的动机与定位

- [x] 2. [WHERE] 第 497 行"并非所有对力函数都能从势能导出"之前，增加一段说明微弹性材料在整个理论框架中的位置。

**建议文本**（替换第 497 行开头）：

```latex
\subsection{微弹性材料与成对势}

并非所有对力函数都能从势能导出。
```

改为：

```latex
\subsection{微弹性材料与成对势}

在 2.3.1 节中，对力函数 $\mathbf{f}$ 仅由反作用条件和中心力条件约束，其具体形式尚未确定。
若进一步要求对力可由某个标量势函数导出，则称该材料为\textbf{微弹性材料}（microelastic material）。
这一假设的重要性在于：它不仅使对力的数学形式更具体，而且为后续能量守恒律（2.5 节）的建立、守恒量的严格证明（2.6 节）以及键基本构模型的构造（第 4 章）提供了必要的数学前提。

并非所有对力函数都能从势能导出。
```

**验收标准**：
- 明确说明了微弹性材料的来龙去脉
- 指明了与后续章节（2.5、2.6、第 4 章）的关联
- 不引入新的引用错误

---

### 任务 3：详细解释梯度符号的物理意义

- [x] 3. [WHERE] 第 498—502 行，公式 `\mathbf{f}=\nabla_{\boldsymbol{\eta}} w` 之后增加对梯度符号的解释。

**建议文本**（在第 502 行"导数给出"之后插入）：

```latex
式中 $\nabla_{\boldsymbol{\eta}}$ 表示对标量函数 $w$ 关于矢量自变量 $\boldsymbol{\eta}$ 的梯度，其分量为 $(\nabla_{\boldsymbol{\eta}} w)_i = \partial w / \partial \eta_i$（$i=1,2,3$）。
由于 $w$ 是标量，$\nabla_{\boldsymbol{\eta}} w$ 是矢量，量纲为 $[w]/[\eta]$，与对力函数 $\mathbf{f}$ 的量纲 $[\mathbf{f}]=[\mathrm{N}/\mathrm{m}^6]$ 一致。
```

**验收标准**：
- 梯度的数学定义明确
- 量纲一致性得到验证

---

### 任务 4：补充经典理论与近场动力学的对应表格

- [x] 4. [WHERE] 第 502 行"导数给出"之后（或任务 3 的文本之后），增加一个对照表格。

**建议文本**（插入任务 3 之后）：

```latex
为清晰展示这一对应关系，表~\ref{tab:classical-peridynamics} 对比了经典弹性力学与近场动力学中的核心概念。

\begin{table}[htbp]
  \centering
  \caption{经典弹性力学与近场动力学的对应关系}
  \label{tab:classical-peridynamics}
  \begin{tabular}{p{0.28\textwidth}p{0.28\textwidth}p{0.28\textwidth}}
    \toprule
    & 经典弹性力学 & 近场动力学 \\
    \midrule
    基本描述对象 & 应变张量 $\boldsymbol{\varepsilon}$ & 键的相对位移 $\boldsymbol{\eta}$ \\
    势能 & 应变能密度 $W(\boldsymbol{\varepsilon})$ & 成对势 $w(\boldsymbol{\eta},\boldsymbol{\xi})$ \\
    导出力 & 应力 $\boldsymbol{\sigma}=\partial W/\partial\boldsymbol{\varepsilon}$ & 对力 $\mathbf{f}=\nabla_{\boldsymbol{\eta}} w$ \\
    \bottomrule
  \end{tabular}
\end{table}
```

**验收标准**：
- 表格编译正确，无 Overfull 警告
- 表有编号，正文中有引用 `\ref{tab:classical-peridynamics}`

---

### 任务 5：补充交换对称性保证反作用条件的推导

- [x] 5. [WHERE] 第 514 行"自动满足反作用条件"之后，补充具体推导。

**建议文本**（替换第 514 行的简略表述）：

```latex
交换对称性保证了由式~\eqref{eq:pairwise-force-potential}导出的对力自动满足反作用条件~\eqref{eq:reaction}。
具体而言，对式~\eqref{eq:potential-symmetry}两边关于 $\boldsymbol{\eta}$ 求梯度并令 $\boldsymbol{\eta}\to-\boldsymbol{\eta}$，得
\begin{equation}
  \nabla_{\boldsymbol{\eta}} w(-\boldsymbol{\eta},-\boldsymbol{\xi}) = -\nabla_{\boldsymbol{\eta}} w(\boldsymbol{\eta},\boldsymbol{\xi})
\end{equation}
即 $\mathbf{f}(-\boldsymbol{\eta},-\boldsymbol{\xi})=-\mathbf{f}(\boldsymbol{\eta},\boldsymbol{\xi})$，这正是反作用条件~\eqref{eq:reaction}。
```

**验收标准**：
- 推导完整，无逻辑跳跃
- 引用的公式编号正确

---

### 任务 6：补充"自动满足中心力条件"的论证

- [x] 6. [WHERE] 第 515 行"结合式(13)可知，微弹性材料的对力自动满足中心力条件"之后，补充论证。

**建议文本**（替换现有简略表述）：

```latex
结合式~\eqref{eq:central-force-form}可知，微弹性材料的对力自动满足中心力条件。
事实上，由交换对称性~\eqref{eq:potential-symmetry}可知，$w$ 仅依赖变形后键长 $|\boldsymbol{\xi}+\boldsymbol{\eta}|$ 以及参考键长 $|\boldsymbol{\xi}|$（对客观势函数更一般地依赖二者），因此
\begin{equation}
  w(\boldsymbol{\eta},\boldsymbol{\xi}) = \hat{w}(|\boldsymbol{\xi}+\boldsymbol{\eta}|, |\boldsymbol{\xi}|)
\end{equation}
对其求梯度得
\begin{equation}
  \mathbf{f}(\boldsymbol{\eta},\boldsymbol{\xi}) = \nabla_{\boldsymbol{\eta}} w = \frac{\partial\hat{w}}{\partial|\boldsymbol{\xi}+\boldsymbol{\eta}|}\cdot\frac{\boldsymbol{\xi}+\boldsymbol{\eta}}{|\boldsymbol{\xi}+\boldsymbol{\eta}|}
\end{equation}
显然 $\mathbf{f}$ 与 $\boldsymbol{\xi}+\boldsymbol{\eta}$ 共线，故中心力条件~\eqref{eq:central-force}自动满足。
```

**验收标准**：
- 论证从势函数的一般形式出发，推导 $\mathbf{f}$ 沿键方向
- 推导严谨，无"显然"式省略

---

### 任务 7：增加微弹性材料的具体例子

- [x] 7. [WHERE] 第 538 行（应变能密度定义之前），增加一个简单例子。

**建议文本**（插入第 538 行之前）：

```latex
\begin{example}[线性微弹性材料]
  最简单的微弹性材料对应成对势
  \begin{equation}
    w(\boldsymbol{\eta},\boldsymbol{\xi}) = \frac{1}{2}\,c(|\boldsymbol{\xi}|)\,s^2
  \end{equation}
  其中 $s=(|\boldsymbol{\xi}+\boldsymbol{\eta}|-|\boldsymbol{\xi}|)/|\boldsymbol{\xi}|$ 为键伸长率，$c(|\boldsymbol{\xi}|)$ 为仅依赖参考键长的微模量函数。
  此时对力为
  \begin{equation}
    \mathbf{f}(\boldsymbol{\eta},\boldsymbol{\xi}) = c(|\boldsymbol{\xi}|)\,s\,\frac{\boldsymbol{\xi}+\boldsymbol{\eta}}{|\boldsymbol{\xi}+\boldsymbol{\eta}|}
  \end{equation}
  即沿变形后键方向的线性弹簧力。该形式将在第 4 章键基模型中广泛应用。
\end{example}
```

**验收标准**：
- 例子完整，包含势函数、对力、物理意义
- 使用 `example` 环境（已在 preamble.tex 中定义）

---

### 任务 8：优化应变能密度定义的引入方式

- [x] 8. [WHERE] 第 540—545 行（应变能密度定义段），优化引入逻辑。

**建议文本**（替换第 540—545 行）：

```latex
有了成对势，可以定义物质点 $\mathbf{x}$ 的应变能密度。与经典弹性力学类似，应变能密度是物质点与其族内所有邻居的成对势之和。为避免每条键被重复计算，取半值：
\begin{equation}
  W(\mathbf{x},t)=\frac{1}{2}\int_{\mathcal{F}_{\mathbf{x}}} w\bigl(\boldsymbol{\eta}(\mathbf{x}',\mathbf{x},t),\boldsymbol{\xi}\bigr)\,\mathrm{d}V'
  \label{eq:strain-energy}
\end{equation}
式中系数 $1/2$ 的物理原因是：键 $(\mathbf{x},\mathbf{x}')$ 同时属于物质点 $\mathbf{x}$ 和 $\mathbf{x}'$ 的族，若两点各计 $w$，则总能量中该键被重复计算；各计 $w/2$ 恰好抵消重复。
$W$ 的深入讨论（包括能量平衡、正定性、与第 6 章态型应变能密度的衔接）见 2.5 节。
```

**验收标准**：
- $1/2$ 因子的物理意义解释清楚
- 与经典理论的类比自然
- 逻辑过渡顺畅

---

## Final verification wave

- [x] F1. [编译验证] 执行 `xelatex main.tex` 和 `bibtex main`，确认 2.3.2 节无编译错误、无未定义引用
- [x] F2. [内容验证] 通读修改后的 2.3.2 节，确认 8 个可读性问题均已解决，逻辑连贯，物理意义清晰
- [x] F3. [编号验证] 检查新增公式、表格编号与正文引用的一致性
- [x] F4. [风格验证] 确认新增文本与全书风格一致（术语、标点、数学符号规范）

---

## Dependency Matrix

```
任务 1 (过渡段)  →  任务 2 (动机)  →  任务 3 (梯度解释)
                                              ↓
                                      任务 4 (对照表格)
                                              ↓
                                      任务 5 (反作用推导)
                                              ↓
                                      任务 6 (中心力推导)
                                              ↓
                                      任务 7 (具体例子)
                                              ↓
                                      任务 8 (应变能优化)
```

**说明**：任务间存在逻辑先后关系，建议按编号顺序执行。每个任务均可独立验证。

## Commit suggestion

```
优化第 2 章 2.3.2 节可读性

- 增加 2.3.1 到 2.3.2 的过渡段
- 补充微弹性材料的动机与定位
- 详细解释梯度符号物理意义
- 增加经典理论与近场动力学对照表
- 补充交换对称性保证反作用条件的推导
- 论证微弹性材料自动满足中心力条件
- 增加线性微弹性材料具体例子
- 优化应变能密度定义的引入方式
```
