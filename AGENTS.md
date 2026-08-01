# AGENTS.md — 近场动力学专著 LaTeX 项目

## 项目性质

专著《近场动力学理论与数值方法》的 LaTeX 书籍项目。当前状态：**第1章绪论已完成**（约9000字，10幅插图，71篇文献），其余章节仍为骨架。

## 编译

**必须用 XeLaTeX**（ctexbook + 中文内容，pdflatex 会失败）。TeX 发行版：MiKTeX 26.5。

```powershell
# 快速编译（目录/交叉引用需两遍）
xelatex main.tex
xelatex main.tex

# 完整编译（含参考文献，推荐）
xelatex main.tex
bibtex main
xelatex main.tex
xelatex main.tex
```

产物 `main.pdf`（当前 78 页）。编译临时文件（.aux/.log/.toc 等）勿提交。

## 文件组织

`main.tex` 是唯一入口，仅含 `\input` 语句——**编辑章节文件，不要改 main.tex 的结构**。

| 位置 | 内容 |
|------|------|
| `preamble.tex` | 宏包、页面设置、章节样式、定理环境、代码环境、caption 格式 |
| `frontmatter/` | titlepage（封面）、preface（前言）、notation（符号表） |
| `chapters/ch01–ch19` | 19 章正文，文件名格式 `chNN_英文主题.tex` |
| `appendices/appA–appE` | 5 个附录，文件名格式 `appX_英文主题.tex` |
| `bibliography.bib` | BibTeX 文献库（71 条，持续增长中） |
| `figures/` | 插图目录（CC-BY 论文插图、TikZ 自绘图） |

## 项目特定约定

- **文档类**：`ctexbook`，A4，11pt
- **章节编号**：`第X章` 格式（ctexset 配置，阿拉伯数字）
- **定理环境**（均按章编号）：`theorem`→定理、`definition`→定义、`lemma`→引理、`remark`→注记、`example`→例
- **代码环境**：`listings` 包，`\begin{lstlisting}` / `\end{lstlisting}`
- **页面边距**：上下右 2.5cm，左 3cm
- **页眉**：居中显示当前章名（`\leftmark`）；页脚：居中页码
- **图注格式**：`caption` 宏包配置，`labelsep=quad`（编号与文字间无冒号，用空格分隔）
- **目录深度**：`tocdepth=1`（仅显示章+节，不显示三级标题）。由于 `titlesec` 宏包会覆盖标准 LaTeX 的 `tocdepth` 行为，preamble.tex 中已通过 `\addcontentsline` 补丁在写入 `.toc` 时过滤 subsection 条目。如需调整目录深度，请勿仅修改 `\setcounter{tocdepth}{}`，需同步检查补丁逻辑。
- **占位待替换**：`frontmatter/titlepage.tex` 中"作者姓名"

## 插图规范

- **TikZ 自绘图**：直接内联在章节 `.tex` 中，矢量输出
- **CC-BY 论文插图**：下载到 `figures/` 目录，用 `\includegraphics` 插入
  - 来源标注格式：`（图片来源\cite{XXX}）`（无冒号，无"CC BY 4.0"字样）
  - 图片宽度：通常 `width=0.9\textwidth`，根据内容调整
- **图注中不得使用冒号**：已通过 `\captionsetup[figure]{labelsep=quad}` 全局去除

## 书籍编写规范

### 写作质量

- **逻辑通顺**：章节内部论述连贯，章节之间前后呼应，避免逻辑跳跃或自相矛盾。
- **适当详细**：核心推导和关键概念须充分展开，避免过度简略；次要内容可适度精简，保持全书篇幅均衡。
- **来源可靠可溯源**：所有事实性陈述、数据、结论须标注来源（`\cite{}`），优先引用原始文献；禁止转引二手文献。
- **不伪造不捏造**：严格遵守 CY/T 118—2015 第 4.5 条学术不端红线，不抄袭、不剽窃、不篡改成果、不伪造或篡改数据、不捏造事实。
- **公式与图表规范**：公式须按章编号（`\begin{equation}`），正文用 `\eqref{}` 引用；图表须有编号且正文必有引用，坐标轴须标注物理量与单位。

### 格式与符号

- **标点符号**：符合 GB/T 15834《标点符号用法》
- **数字用法**：符合 GB/T 15835《出版物上数字用法》
- **科技术语**：符合 CY/T 119《学术出版规范 科学技术名词》；全书术语统一，英文缩写首次出现须给全称（如"近场动力学（peridynamics，PD）"）
- **量与单位**：符合 GB 3100—1993《国际单位制及其应用》、GB/T 3101—1993《有关量、单位和符号的一般原则》；量符号斜体，单位符号正体，矢量用粗体或箭头标注
- **符号表维护**：新符号须在 `frontmatter/notation.tex` 登记，并在正文中首次出现时定义

### 编号与引用

- **公式编号**：全书公式统一按章编号，禁止硬编码编号
- **交叉引用**：正文引用图、表、公式、章节时须使用 `\ref` / `\eqref` / `\autoref`，禁止手写编号
- **表格规范**：与插图规范并列——表须有编号+正文引用、表注规范、数据来源标注

### 文献与可复现性

- **参考文献格式**：符合 GB/T 7714—2025《信息与文献 参考文献著录规则》；每条文献须可查 DOI/卷期页，统一由 `bibliography.bib` 管理
- **数值算例可复现**：给出完整参数（材料常数、horizon δ、网格尺寸、时间步长等），附录代码可用
- **编译质量门禁**：xelatex 两遍 + bibtex 无 error；无 undefined reference/citation 警告

## Git

- 分支 `main`，尚无提交
- `.gitignore` 忽略 `/.omo`（OpenCode 运行时目录）
