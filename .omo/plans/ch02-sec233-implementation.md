# 2.3.3节修改：具体LaTeX实现方案

## 修改位置
文件：`chapters/ch02_framework.tex`
行号：622-640（`\subsection{对力函数的量纲}` 到 `\subsection{小变形线性化与微模量张量}` 之间）

## 原内容（保留核心推导）

```latex
\subsection{对力函数的量纲}

运动方程\eqref{eq:motion}的两端各项必须量纲一致。左端惯性项 $\rho\ddot{\mathbf{u}}$ 的量纲为
\begin{equation}
  [\rho\ddot{\mathbf{u}}]=\frac{\mathrm{kg}}{\mathrm{m}^{3}}\cdot\frac{\mathrm{m}}{\mathrm{s}^{2}}=\frac{\mathrm{N}}{\mathrm{m}^{3}}
  \label{eq:dim-inertia}
\end{equation}
即力密度（单位体积的力）。体力密度 $\mathbf{b}$ 的量纲与之相同，为 $\mathrm{N}/\mathrm{m}^{3}$。右端积分项为对力的体积积分，为使方程两边量纲一致，对力函数 $\mathbf{f}$ 的量纲须为
\begin{equation}
  [\mathbf{f}]=\frac{\mathrm{N}}{\mathrm{m}^{6}}
  \label{eq:dim-force}
\end{equation}
即"力每体积平方"。

这一量纲与经典连续介质力学中应力（$\mathrm{N}/\mathrm{m}^{2}$）有本质区别，反映了近场动力学非局部描述的固有特征：经典理论中，应力描述的是单位面积上的内力；而近场动力学中，对力描述的是单位体积平方上的非局部相互作用力密度。

\begin{remark}
  运动方程 \eqref{eq:motion} 在形式上与分子动力学方程相似，但二者有本质区别：分子动力学处理离散原子间的二体力，力以 $\mathrm{N}$ 为单位；近场动力学处理连续介质中物质点间的非局部相互作用，力以 $\mathrm{N}/\mathrm{m}^{6}$ 为单位，并通过对体积积分得到力密度。这种"连续+非局部"的混合特征使近场动力学既能像分子动力学一样处理不连续性，又能像连续介质力学一样与宏观观测接轨 \cite{Silling2000,SillingLehoucq2010}。
\end{remark}
```

## 修改后完整内容

```latex
\subsection{对力函数的量纲}

在建立了对力函数 $\mathbf{f}$ 的物理图像（2.3.1节）和数学结构（2.3.2节）之后，本节从量纲分析的角度，验证运动方程\eqref{eq:motion}在数学上的自洽性，并揭示对力函数量纲背后的物理内涵。

运动方程\eqref{eq:motion}的两端各项必须量纲一致。左端惯性项 $\rho\ddot{\mathbf{u}}$ 的量纲为
\begin{equation}
  [\rho\ddot{\mathbf{u}}]=\frac{\mathrm{kg}}{\mathrm{m}^{3}}\cdot\frac{\mathrm{m}}{\mathrm{s}^{2}}=\frac{\mathrm{N}}{\mathrm{m}^{3}}
  \label{eq:dim-inertia}
\end{equation}
即力密度（单位体积的力）。体力密度 $\mathbf{b}$ 的量纲与之相同，为 $\mathrm{N}/\mathrm{m}^{3}$。右端积分项为对力的体积积分，为使方程两边量纲一致，对力函数 $\mathbf{f}$ 的量纲须为
\begin{equation}
  [\mathbf{f}]=\frac{\mathrm{N}}{\mathrm{m}^{6}}
  \label{eq:dim-force}
\end{equation}
即"力每体积平方"。

为清晰展示运动方程各项的量纲关系，表~\ref{tab:dim-analysis}给出了完整的量纲分析总览。

\begin{table}[htbp]
  \centering
  \caption{运动方程\eqref{eq:motion}各项的量纲分析}
  \label{tab:dim-analysis}
  \begin{tabular}{llcl}
    \toprule
    项 & 表达式 & 量纲 & 物理意义 \\
    \midrule
    惯性项 & $\rho\ddot{\mathbf{u}}$ & $\mathrm{N}/\mathrm{m}^{3}$ & 单位体积惯性力（力密度）\\
    体力 & $\mathbf{b}$ & $\mathrm{N}/\mathrm{m}^{3}$ & 单位体积外力（力密度）\\
    对力 & $\mathbf{f}$ & $\mathrm{N}/\mathrm{m}^{6}$ & 单位体积对单位体积的力密度\\
    积分后 & $\int\mathbf{f}\,\mathrm{d}V'$ & $\mathrm{N}/\mathrm{m}^{3}$ & 单位体积总非局部力\\
    \bottomrule
  \end{tabular}
\end{table}

式\eqref{eq:dim-force}给出的量纲可直观理解为：对力函数 $\mathbf{f}$ 描述的是\textbf{单位体积微元对单位体积微元的力密度}。由于相互作用涉及两个体积微元（物质点 $\mathbf{x}$ 的体积 $\mathrm{d}V_{\mathbf{x}}$ 与邻居 $\mathbf{x}'$ 的体积 $\mathrm{d}V_{\mathbf{x}'}$），而每个微元的量纲均为体积 $\mathrm{m}^{3}$，因此力的量纲 $\mathrm{N}$ 被两个体积除后得到 $\mathrm{N}/\mathrm{m}^{6}$。这类似于概率论中的"联合密度"：若两个事件各自的测度为 $V$，则联合事件的密度量纲为 $1/V^{2}$。

为建立直观感受，考虑如下量级估计。设某材料密度 $\rho\sim 10^{3}\,\mathrm{kg}/\mathrm{m}^{3}$，在 $10^{6}\,\mathrm{Pa}$（约10个大气压）量级的应力作用下，经典弹性力学中应变约为 $10^{-3}$ 量级。在近场动力学中，若取近场域半径 $\delta\sim 10^{-3}\,\mathrm{m}$（毫米量级），微模量 $c\sim 10^{18}\,\mathrm{N}/\mathrm{m}^{6}$（见第4章标定），则对力函数的量级为 $|\mathbf{f}|\sim c\cdot s\sim 10^{15}\,\mathrm{N}/\mathrm{m}^{6}$。对两个体积均为 $10^{-9}\,\mathrm{m}^{3}$（微米尺度立方体）的物质点，其相互作用力为 $\mathrm{d}F\sim 10^{15}\times 10^{-18}=10^{-3}\,\mathrm{N}$，即毫牛量级——这与经典理论中面积 $10^{-6}\,\mathrm{m}^{2}$ 上受力 $1\,\mathrm{N}$ 的量级一致，验证了量纲分析的自洽性。

这一量纲与经典连续介质力学中应力（$\mathrm{N}/\mathrm{m}^{2}$）有本质区别，反映了近场动力学非局部描述的固有特征。表~\ref{tab:stress-vs-pairwise-force}从多个维度对比了两种理论中"内力描述"的差异。

\begin{table}[htbp]
  \centering
  \caption{经典连续介质力学与近场动力学中"内力描述"的对比}
  \label{tab:stress-vs-pairwise-force}
  \begin{tabular}{p{0.25\textwidth}p{0.30\textwidth}p{0.30\textwidth}}
    \toprule
    特征 & 经典连续介质力学 & 近场动力学 \\
    \midrule
    相互作用对象 & 点与无穷小邻域 & 点与有限距离内所有点 \\
    描述方式 & 应力张量 $\boldsymbol{\sigma}$ & 对力函数 $\mathbf{f}$ \\
    量纲 & $\mathrm{N}/\mathrm{m}^{2}$（力/面积） & $\mathrm{N}/\mathrm{m}^{6}$（力/体积$^2$）\\
    作用载体 & 面积微元 $\mathrm{d}A$ & 体积微元对 $\mathrm{d}V\mathrm{d}V'$ \\
    局部性 & 局部（$\delta\to 0$） & 非局部（有限 $\delta$）\\
    \bottomrule
  \end{tabular}
\end{table}

\begin{remark}
  对力函数的量纲 $\mathrm{N}/\mathrm{m}^{6}$ 揭示了PD在理论谱系中的独特位置：分子动力学（MD）处理离散原子间的二体力，力以 $\mathrm{N}$ 为单位；经典连续介质力学处理局部场，应力以 $\mathrm{N}/\mathrm{m}^{2}$ 为单位；而PD处理的是"连续介质中的非局部对力"，其量纲 $\mathrm{N}/\mathrm{m}^{6}$ 恰好介于两者之间——它比MD多了两个体积除数（体现连续介质假设），又比经典理论多了两个长度除数（体现非局部相互作用）。这种"连续+非局部"的混合特征使PD既能像MD一样处理不连续性，又能像经典力学一样与宏观观测接轨 \cite{Silling2000,SillingLehoucq2010}。
\end{remark}
```

## 修改统计
- **新增内容**：过渡句（2行）、量纲总览表（12行）、物理意义解释（5行）、数值直觉段（7行）、经典理论对比表（12行）
- **修改内容**：Remark优化（从4行扩展到7行）
- **保留内容**：核心量纲推导（8行）
- **总计**：从18行扩展到约60-70行

## 实施建议
1. 用上述代码替换原622-640行内容
2. 确保 `booktabs` 宏包已加载（检查preamble.tex）
3. 编译验证
