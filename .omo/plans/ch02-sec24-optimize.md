# 第2章2.4节（近场动力学状态）优化修改计划

## 背景

当前2.4节仅3个小节（2.4.1-2.4.3），约69行。作为入门引论篇幅偏短，且2.4.1与2.3.4内容重复。本计划将2.4节优化为4个小节，篇幅扩展至约100行，强化入门定位，突出"键基⊂态型"的认知框架。

## 修改目标

1. **压缩重复**：2.4.1不再重复泊松比推导，直接引用2.3.4结论
2. **精炼定义**：2.4.2补充"态是函数、不是矢量"的直觉
3. **扩展物理含义**：2.4.3补充方程各项的物理解释
4. **新增特例推导**：2.4.4将键基作为态型特例独立成节
5. **统一符号**：首次出现时标注英文术语（state-based/bond-based）及缩写（OSB/NOSB）
6. **衔接前后文**：预告2.5节（Fréchet导数）和第6章（详细展开）

## 修改前后对比

| 小节 | 当前 | 修改后 | 变化 |
|------|------|--------|------|
| 2.4.1 键基局限 | 9行 | 8-10行 | 压缩，去重 |
| 2.4.2 态的定义 | 30行 | 25-28行 | 精炼 |
| 2.4.3 态型运动方程 | 12行 | 18-22行 | 扩展物理含义 |
| **2.4.4 键基作为特例** | **0行** | **22-28行** | **新增** |
| **总计** | **69行** | **~100行** | **+31行** |

## 具体修改内容

### 修改1：2.4.1 节标题和内容重写（压缩）

**当前（ch02_framework.tex, 796-805行）：**

```latex
\subsection{键基理论的局限}

键基对力 $\mathbf{f}(\boldsymbol{\eta},\boldsymbol{\xi})$ 只依赖单条键的相对位移 $\boldsymbol{\eta}$，与该物质点其他键的变形无关。这意味着每条键独立承担自己的恢复力，键与键之间无耦合。对线性各向同性材料，这一限制导致一个固定的泊松比。

考虑均匀各向同性变形...（泊松比推导，约6行）

式\eqref{eq:poisson-limit}是键基理论的标志性局限...（结论，约3行）
```

**修改为：**

```latex
\subsection{从键基到态型：动机与过渡}

键基对力 $\mathbf{f}(\boldsymbol{\eta},\boldsymbol{\xi})$ 只依赖单条键的相对位移 $\boldsymbol{\eta}$，与该物质点其他键的变形无关。这意味着每条键独立承担自己的恢复力，键与键之间无耦合。对线性各向同性材料，这一限制导致泊松比被锁定为 $1/4$（三维）或 $1/3$（二维平面应力），详见式\eqref{eq:poisson-limit}。其物理根源在于：键基对力无法区分"体积变形"与"形状变形"，因为每条键只感知自身的伸长率，不知道邻居键的总体变形状态。实际材料（如金属 $\nu\approx 0.3$、橡胶 $\nu\approx 0.5$）大多不满足这一限制，因此键基理论虽适合作为入门和定性分析，但对定量预测有本质不足。

为突破上述局限，需要将"键到键"的二体力推广为"点到场"的非局部映射：物质点 $\mathbf{x}$ 对邻居 $\mathbf{x}'$ 的力不仅依赖该键自身的变形，还依赖 $\mathbf{x}$ 的整个变形状态。这一推广通过引入\emph{态}（state）的概念实现。
```

### 修改2：2.4.2 补充"态是函数"的直觉（精炼）

**当前（807-845行）：**

```latex
\subsection{态的概念与基本定义}

态型理论的核心思想是：把"键到键"的二体力...推广为...这一推广通过引入\emph{态}（state）的概念实现。

态是一个把键矢量...两个基本态是：

\begin{itemize}
  \item \textbf{变形态}（deformation state）...
  \item \textbf{力态}（force state）...
\end{itemize}

图\ref{fig:state-concept}直观地展示了...

\begin{figure}...

力态依赖整个变形态这一性质...第 6 章将给出常规态型（ordinary state-based）本构的完整理论。
```

**修改为：**

```latex
\subsection{态的概念与基本定义}

态型理论的核心思想是：把"键到键"的二体力 $\mathbf{f}(\boldsymbol{\eta},\boldsymbol{\xi})$ 推广为"点到场"的映射 $\underline{\mathbf{T}}\langle\boldsymbol{\xi}\rangle$。需要特别强调的是，态不是矢量，而是把键矢量 $\boldsymbol{\xi}$ 映射为矢量的函数，记为 $\underline{A}\langle\boldsymbol{\xi}\rangle$，其中下划线表示态、尖括号内为自变量键矢量。两个基本态是：

\begin{itemize}
  \item \textbf{变形态}（deformation state）$\underline{\mathbf{Y}}$：...
  \item \textbf{力态}（force state）$\underline{\mathbf{T}}$：...
\end{itemize}

[保留原图及图注]

力态依赖整个变形态这一性质...第 6 章将给出常规态型（ordinary state-based，简称 OSB）本构的完整理论。
```

### 修改3：2.4.3 扩展物理含义并添加公式编号（扩展）

**当前（847-859行）：**

```latex
\subsection{态型运动方程}

用态表示的运动方程为
\[
  \rho(\mathbf{x})\,\ddot{\mathbf{u}}(\mathbf{x},t)=\int_{\mathcal{H}_{\mathbf{x}}}\Bigl[\underline{\mathbf{T}}\langle\boldsymbol{\xi}\rangle-\underline{\mathbf{T}}'\langle-\boldsymbol{\xi}\rangle\Bigr]\,\mathrm{d}V'+\mathbf{b}(\mathbf{x},t)
\]
其中...该方程的严格形式与各项含义见 6.1 节式\eqref{eq:state-motion}。

键基理论是态型理论的特例...（键基还原推导，移至2.4.4）
```

**修改为：**

```latex
\subsection{态型运动方程}

用态表示的运动方程为
\begin{equation}
  \rho(\mathbf{x})\,\ddot{\mathbf{u}}(\mathbf{x},t)=\int_{\mathcal{H}_{\mathbf{x}}}\Bigl[\underline{\mathbf{T}}\langle\boldsymbol{\xi}\rangle-\underline{\mathbf{T}}'\langle-\boldsymbol{\xi}\rangle\Bigr]\,\mathrm{d}V'+\mathbf{b}(\mathbf{x},t)
  \label{eq:state-motion-ch02}
\end{equation}
其中 $\underline{\mathbf{T}}\langle\boldsymbol{\xi}\rangle$ 为物质点 $\mathbf{x}$ 的力态在键 $\boldsymbol{\xi}$ 处的取值，即 $\mathbf{x}$ 对邻居 $\mathbf{x}'$ 的作用力密度；$\underline{\mathbf{T}}'\langle-\boldsymbol{\xi}\rangle$ 为邻居 $\mathbf{x}'$ 的力态在反向键 $-\boldsymbol{\xi}$ 处的取值，即 $\mathbf{x}'$ 对 $\mathbf{x}$ 的反作用力密度。两者之差的体积积分给出 $\mathbf{x}$ 受到的净非局部力密度，加上体力 $\mathbf{b}(\mathbf{x},t)$ 后等于惯性力。

与键基运动方程\eqref{eq:motion}相比，式\eqref{eq:state-motion-ch02}中的"力态差" $\underline{\mathbf{T}}\langle\boldsymbol{\xi}\rangle-\underline{\mathbf{T}}'\langle-\boldsymbol{\xi}\rangle$ 代替了单力 $\mathbf{f}$，这一形式变化看似微小，意义却深远：它把"成对力"解耦为两个独立的"单端力态"，使本构函数可以独立地依赖每端的变形状态。这一解耦是态型理论突破泊松比限制的数学根源，也是 2.6 节守恒律证明需要重新审视的起点。
```

### 修改4：新增2.4.4节（新增）

在2.4.3后、2.5节前插入：

```latex
\subsection{键基作为态型的特例}

键基理论可以视为态型理论的一个特例。取力态为
\begin{equation}
  \underline{\mathbf{T}}\langle\boldsymbol{\xi}\rangle=\tfrac{1}{2}\,\mathbf{f}(\boldsymbol{\eta},\boldsymbol{\xi})
  \label{eq:bb-state-special}
\end{equation}
其中 $\mathbf{f}$ 为键基对力函数，系数 $1/2$ 的物理意义是"每键被两点共享"：在态型表述中，$\mathbf{x}$ 对键的贡献为 $\underline{\mathbf{T}}\langle\boldsymbol{\xi}\rangle=\mathbf{f}/2$，$\mathbf{x}'$ 对同一键的贡献为 $\underline{\mathbf{T}}'\langle-\boldsymbol{\xi}\rangle=-\mathbf{f}/2$（由反作用条件\eqref{eq:reaction}）。将式\eqref{eq:bb-state-special}代入态型运动方程\eqref{eq:state-motion-ch02}，得
\[
  \underline{\mathbf{T}}\langle\boldsymbol{\xi}\rangle-\underline{\mathbf{T}}'\langle-\boldsymbol{\xi}\rangle
  =\frac{\mathbf{f}}{2}-\left(-\frac{\mathbf{f}}{2}\right)
  =\mathbf{f}(\boldsymbol{\eta},\boldsymbol{\xi})
\]
右端正是键基运动方程\eqref{eq:motion}中的对力项。这说明键基方程是态型方程在力态取式\eqref{eq:bb-state-special}时的自然退化。

上述推导的物理含义是：当力态仅依赖单条键的变形（即 $\underline{\mathbf{T}}$ 退化为键基 $\mathbf{f}$）时，态型理论退化为键基理论。换言之，键基理论是态型理论的子集。态型通过允许力态依赖整个变形状态——而非单条键——实现了对键基的推广。2.5 节将在此基础上建立应变能密度与力态的 Fr\'echet 导数关系；第 6 章则给出常规态型（OSB）与非寻常态型（non-ordinary state-based，简称 NOSB）本构的完整理论。
```

## 文件操作

### 修改文件

- `chapters/ch02_framework.tex`：修改第796-860行（2.4节全部内容）

### 具体编辑指令

使用 `edit` 工具对 `chapters/ch02_framework.tex` 执行以下替换：

1. **替换2.4.1节内容**（第796-805行 → 新的8-10行）
2. **替换2.4.2节内容**（第807-845行 → 新的25-28行）
3. **替换2.4.3节内容**（第847-859行 → 新的18-22行）
4. **在2.4.3后插入2.4.4节**（新增22-28行）

## 编译验证

修改完成后，执行以下命令验证编译：

```powershell
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

**预期结果**：
- 无 error
- `main.log` 中 `undefined` 计数为 0
- 输出 `main.pdf`

## 引用检查

新增/修改的引用关系：
- `eq:state-motion-ch02`：新增，2.4.3节态型运动方程
- `eq:bb-state-special`：新增，2.4.4节键基特例
- `eq:poisson-limit`：已存在，2.4.1引用2.3.4结论
- `eq:reaction`：已存在，反作用条件
- `eq:motion`：已存在，键基运动方程
- `Silling2007`、`SillingLehoucq2010`：已存在于bibliography.bib

## 符号统一

| 术语 | 首次出现位置 | 要求 |
|------|-------------|------|
| 态型 | 2.4节导言 | 标注英文 state-based |
| 键基 | 2.4节导言 | 标注英文 bond-based |
| OSB | 2.4.2末尾 | 标注全称 ordinary state-based |
| NOSB | 2.4.4末尾 | 标注全称 non-ordinary state-based |

## 章节衔接

| 衔接点 | 当前状态 | 修改后 |
|--------|----------|--------|
| 向上（2.3.4） | 2.4.1重复推导 | 2.4.1直接引用结论 |
| 向下（2.5） | 无预告 | 2.4.4末尾预告Fréchet导数 |
| 向前（第6章） | 2.4.2末尾一句话 | 2.4.4末尾强化预告 |

## TODOs

- [x] 1. 重写2.4.1节：标题改为"从键基到态型：动机与过渡"，删除泊松比详细推导，压缩为8-10行（保留引用式\eqref{eq:poisson-limit}与物理根源论述）
- [x] 2. 精炼2.4.2节：补充"态不是矢量、而是函数"的直觉论述，合并重复的背景句，图\ref{fig:state-concept}与图注原样保留，末尾标注"ordinary state-based，简称 OSB"
- [x] 3. 扩展2.4.3节：运动方程由 `\[ \]` 改为编号 `equation` 环境并新增 `\label{eq:state-motion-ch02}`，补充 $\underline{\mathbf{T}}\langle\boldsymbol{\xi}\rangle$ 与 $\underline{\mathbf{T}}'\langle-\boldsymbol{\xi}\rangle$ 的物理含义及与键基方程\eqref{eq:motion}的对比论述，移除键基还原推导段（移至2.4.4）
- [x] 4. 新增2.4.4节"键基作为态型的特例"：含特例公式 `\label{eq:bb-state-special}`、系数1/2的"每键被两点共享"解释、代入态型运动方程的完整还原推导、与2.5节Fréchet导数及第6章OSB/NOSB的衔接预告

## Final Verification Wave

- [x] F1. xelatex 编译门禁：`xelatex -interaction=nonstopmode -halt-on-error main.tex` 无 error，`main.log` 中 undefined reference/citation 计数为 0，结尾出现 `Output written on main.pdf`（按 AGENTS.md 约定，由当前会话直接本地执行，不委托子代理）
- [x] F2. 内容审查：逐行核对修改后 2.4.1–2.4.4 节——泊松比推导已压缩、4 个小节齐备、新增 label 无冲突、state-based/bond-based/OSB/NOSB 首次出现均有英文标注、与 2.3.4/2.5/第6章衔接语句齐备、无遗留 TODO/占位符

## 验收标准

- 2.4.1篇幅压缩至8-10行，不再重复泊松比推导
- 2.4.2补充"态是函数"的直觉，首次出现标注OSB
- 2.4.3补充方程各项物理含义，新增公式编号
- 2.4.4新增，完整推导键基作为态型特例
- xelatex编译通过，无error，无undefined引用
- 所有新增术语首次出现时标注英文及缩写
