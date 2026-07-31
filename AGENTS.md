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
- **占位待替换**：`frontmatter/titlepage.tex` 中"作者姓名"

## 插图规范

- **TikZ 自绘图**：直接内联在章节 `.tex` 中，矢量输出
- **CC-BY 论文插图**：下载到 `figures/` 目录，用 `\includegraphics` 插入
  - 来源标注格式：`（图片来源\cite{XXX}）`（无冒号，无"CC BY 4.0"字样）
  - 图片宽度：通常 `width=0.9\textwidth`，根据内容调整
- **图注中不得使用冒号**：已通过 `\captionsetup[figure]{labelsep=quad}` 全局去除

## Git

- 分支 `main`，尚无提交
- `.gitignore` 忽略 `/.omo`（OpenCode 运行时目录）
