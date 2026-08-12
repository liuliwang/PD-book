# 计划：§2.2.3 公式(2.13)拆分推导步骤

## 背景
第2章§2.2.3节"小变形近似"中，公式(2.12)→(2.13)存在推导跳跃，需要补充"提取 $|\boldsymbol{\xi}|^2$"的中间步骤。

## 目标
将原公式(2.13)拆分为两个公式：
1. 新公式(2.13)：展示忽略高阶小量后、提取 $|\boldsymbol{\xi}|^2$ 的过渡形式
2. 新公式(2.14)：展示泰勒展开后的结果（原公式2.13的后两个等号）

## 影响
- **公式编号**：原(2.14)→(2.15)，原(2.15)→(2.16)
- **引用安全**：全文引用通过 `\eqref{eq:stretch-linear}` 和 `\eqref{eq:stretch-uniform}` label，无硬编码编号，编译自动更新
- **风险**：零 —— 仅文字描述和公式排版修改，不改变任何数学内容

## 修改位置
`chapters/ch02_framework.tex`，第 367–377 行

## 修改内容（替换）

### 原文（第367行）
```latex
由于 $|\boldsymbol{\eta}|\ll|\boldsymbol{\xi}|$，式中 $|\boldsymbol{\eta}_{\parallel}|^{2}$ 与 $|\boldsymbol{\eta}_{\perp}|^{2}$ 均为 $O(|\boldsymbol{\eta}|^{2})$ 的高阶小量，可暂忽略；将根号内保留到一阶项，并对 $\sqrt{1+\varepsilon}\approx 1+\varepsilon/2$（$\varepsilon\ll 1$）作泰勒展开，得
```

### 改为
```latex
由于 $|\\boldsymbol{\\eta}|\\ll|\\boldsymbol{\\xi}|$，式中 $|\\boldsymbol{\\eta}_{\\parallel}|^{2}$ 与 $|\\boldsymbol{\\eta}_{\\perp}|^{2}$ 均为 $O(|\\boldsymbol{\\eta}|^{2})$ 的高阶小量，可暂忽略。将根号内保留到一阶项，并提取 $|\\boldsymbol{\\xi}|^{2}$，得
```

### 原文（第368–372行）
```latex
\begin{equation}
  s\approx\frac{|\boldsymbol{\xi}|\sqrt{1+\dfrac{2\,\boldsymbol{\xi}\cdot\boldsymbol{\eta}_{\parallel}}{|\boldsymbol{\xi}|^{2}}}-\,|\boldsymbol{\xi}|}{|\boldsymbol{\xi}|}
  \approx\frac{|\boldsymbol{\xi}|\left(1+\dfrac{\boldsymbol{\xi}\cdot\boldsymbol{\eta}_{\parallel}}{|\boldsymbol{\xi}|^{2}}\right)-|\boldsymbol{\xi}|}{|\boldsymbol{\xi}|}
  =\frac{\boldsymbol{\xi}\cdot\boldsymbol{\eta}_{\parallel}}{|\boldsymbol{\xi}|^{2}}
\end{equation}
```

### 改为
```latex
\begin{equation}
  s\approx\frac{\sqrt{|\boldsymbol{\xi}|^{2}+2\,\boldsymbol{\xi}\cdot\boldsymbol{\eta}_{\parallel}}-\,|\boldsymbol{\xi}|}{|\boldsymbol{\xi}|}
  =\frac{|\boldsymbol{\xi}|\sqrt{1+\dfrac{2\,\boldsymbol{\xi}\cdot\boldsymbol{\eta}_{\parallel}}{|\boldsymbol{\xi}|^{2}}}-\,|\boldsymbol{\xi}|}{|\boldsymbol{\xi}|}
\end{equation}
再对 $\sqrt{1+\varepsilon}\approx 1+\varepsilon/2$（$\varepsilon\ll 1$）作泰勒展开，得
\begin{equation}
  s\approx\frac{|\boldsymbol{\xi}|\left(1+\dfrac{\boldsymbol{\xi}\cdot\boldsymbol{\eta}_{\parallel}}{|\boldsymbol{\xi}|^{2}}\right)-|\boldsymbol{\xi}|}{|\boldsymbol{\xi}|}
  =\frac{\boldsymbol{\xi}\cdot\boldsymbol{\eta}_{\parallel}}{|\boldsymbol{\xi}|^{2}}
\end{equation}
```

## 验证步骤
- [x] 1. 编辑 `chapters/ch02_framework.tex` 第367–377行
- [x] 2. 执行 `xelatex -interaction=nonstopmode -halt-on-error main.tex` 两遍
- [x] 3. 检查编译输出：零 Error、零 undefined reference、公式编号正确
- [x] 4. 确认 `\eqref{eq:stretch-linear}` 引用正常
