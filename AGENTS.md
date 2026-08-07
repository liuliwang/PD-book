# AGENTS.md — 近场动力学专著 LaTeX 项目

<!--
文件性质：AI 指令集（Agent Instruction Set）
作用域：仅指导 AI 行为，非项目文档，非变更日志
维护者：全体协作者，修改需人工 review
禁止内容：历史变更记录、动态状态信息、行号引用、个人工作笔记
-->

## 项目概览

专著《近场动力学理论与数值方法》的 LaTeX 书籍项目（ctexbook，A4，11pt）。
章节完成度参差：ch01、ch02、ch03、ch06、ch07 为完整章节（数百行），是写作新章节时的范例；ch04、ch05、ch08–ch19 目前仅为十余行占位骨架；附录 appA–appE 为占位空文件（动手前先 Read 确认行数）。

## 编译

必须用 XeLaTeX（ctexbook + 中文）。TeX 发行版：MiKTeX 26.5。以下命令顺序即 `.vscode/settings.json` 中 latex-workshop 的 recipe「完整编译 (含参考文献)」；autoBuild/autoClean 均为 never，不会自动编译清理。

```powershell
xelatex main.tex
bibtex main
xelatex main.tex
xelatex main.tex
```

## 文件组织

`main.tex` 是唯一入口，仅含 `\input` 语句——**编辑章节文件，不要改 main.tex 的结构**。

| 位置                      | 内容                                 |
| ------------------------- | ------------------------------------ |
| `preamble.tex`          | 宏包、页面设置、章节样式、定理环境   |
| `frontmatter/`          | 封面、前言、符号表                   |
| `chapters/ch01–ch19`   | 19 章正文，格式`chNN_英文主题.tex` |
| `appendices/appA–appE` | 5 个附录，格式`appX_英文主题.tex`  |
| `bibliography.bib`      | BibTeX 文献库                        |
| `figures/`              | CC-BY 论文插图、TikZ 自绘图          |

## 排版规则

- **文档类**：`ctexbook`，UTF8，A4，11pt（`main.tex` 定义）
- **章节编号**：`第X章`（ctexset，阿拉伯数字）
- **章节标题**：章标题居中 `\Huge\bfseries`、节 `\Large\bfseries`、小节 `\large\bfseries`（`preamble.tex` 已配置，勿改）
- **定理环境**（按章编号）：`theorem`→定理、`definition`→定义、`lemma`→引理、`remark`→注记、`example`→例
- **页面边距**：上下右 2.5cm，左 3cm（`geometry` 已配置）
- **页眉页脚**：居中章名（`\leftmark`），居中页码（`fancyhdr`）
- **图注**：`caption` 包，`font=small`，`labelsep=quad`（编号与文字间空格，无冒号）
- **代码环境**：`listings` 包（`frame=single`、`breaklines`、左行号）
- **链接颜色**：`hyperref` 已配置 colorlinks，PDF 中交叉引用/文献链接为蓝色（预期行为，勿当错误）

### 插图

- **TikZ**：直接内联在章节 `.tex` 中，`xshift`/`yshift` 必须带单位（如 `xshift=6cm`）；preamble 未加载 TikZ 库，用到的 `\usetikzlibrary{...}` 在章节文件头自行声明（如 ch02 的 `arrows.meta, positioning, calc`），漏声明会导致编译失败
- **CC-BY 图**：下载到 `figures/`（`\graphicspath` 已指向），用 `\includegraphics` 插入
  - 来源标注：`\cite{XXX}`，无冒号，无"CC BY 4.0"字样
  - 宽度通常 `width=0.9\textwidth`
- **图注**：标题式，不超过 300 字；正文解释而非图注解释
- **一图一主题**：多主题拆分为独立 `figure`
- **图文对应**：定义→见图→解释；多子图 (a)(b) 描述嵌入对应概念定义处

### 表格

- **三线表**：用 `booktabs`（`\toprule`/`\midrule`/`\bottomrule`），禁止竖线
- **短表**：`tabular`，列宽 `p{0.22\textwidth}p{0.65\textwidth}`
- **长表**：`longtable`，列宽 `p{4.8cm}>{\raggedright\arraybackslash}p{10.2cm}`（防 Overfull）
- **表注**：表下方小字标注数据来源，表须有编号且正文有 `\ref` 引用

### 编号与引用

- **公式**：所有单独成行公式必须编号（`\begin{equation}` + `\label{}`），禁止用 `\[ \]`；正文用 `\eqref{}` 引用
- **图/表**：须有编号，正文必有 `\ref`/ `\eqref` 引用
- **章节引用**：手写（如"第 3 章""2.6 节"），勿用 `\autoref`
- **坐标轴**：标注物理量与单位（如 `$s$（伸长率）`）

## 写作规范

### 质量

- **逻辑通顺**：章节内连贯，章间前后呼应
- **来源可溯源**：`\cite{}` 标注，优先原始文献，禁止转引二手文献
- **公式与图表规范**：编号公式、坐标轴单位、数据来源
- **不伪造不捏造**：遵守 CY/T 118—2015 学术规范

### AI 写作约束

以下约束直接面向 AI 生成正文内容时的行为：

- **数学推导**：每步标注依据（定义/定理/变换），不得跳过关键步骤；生成新公式后须明确提示"该推导需作者人工复核"
- **术语一致**：引入新术语须首次定义并检查与 `frontmatter/notation.tex` 冲突；统一使用约定术语
- **文献引用**：引用须给出准确 `bibliography.bib` 中的 cite key，禁止编造文献；禁止模糊引用
- **逻辑链**：因果链须完整，每个结论前须有足够前提支撑；禁止"显而易见""容易证明"等省略
- **数值算例**：给出完整参数（材料常数、horizon δ、网格尺寸、时间步长等），数据来源须可溯源
- **责任边界**：输出数学/物理内容时须声明"AI 辅助生成，需经专业审阅"；不得替代作者做物理假设或理论判断

#### AI 自查清单

生成每节后，AI 须通检：

- [ ] 推导链完整，每步有标注依据
- [ ] 新术语已定义，与符号表无冲突
- [ ] 引用文献准确，无编造 cite key
- [ ] 因果链无跳跃，无"显而易见"式省略
- [ ] 数值算例参数完整，数据来源可溯源

### 章节模式

1. **章级导言段**：~10 行，预告各节 + 本章目的 + 前后章衔接
2. **节级导言段**：预告本节各子节要点，自含上下文，禁止"作进一步讨论"等笼统表述
3. **段落连贯**：禁止孤立 1-2 行短段；图前引用并入邻近段落
4. **remark 克制**：全章不超过 4 条，仅用于关键洞察
5. **章末收尾**：回扣路线图、重申章旨、衔接下一章
6. **节段与章段分离**：`\section` 首段不重复 `\chapter` 首段结构
7. **节段自含**：以该节主题为主线自含入口，不写"第 X 章…本章…"式回顾

### 术语与符号

- **符号表**：新符号在 `frontmatter/notation.tex` 登记，首次出现时定义
- **表格列宽**：短表 `p{0.22\textwidth}p{0.65\textwidth}`，长表用 `p{4.8cm}>{\raggedright\arraybackslash}p{10.2cm}` 的 longtable
- **标点与数字**：GB/T 15834、GB/T 15835
- **量与单位**：GB 3100、GB/T 3101；量符号斜体，单位符号正体，矢量粗体或箭头

## 编译前核查（强制）

完成推导修改后、编译前，必须通检：

1. **逻辑自洽**：推导与上下文无跳跃、无矛盾
2. **推导正确**：代数、积分、求导完整复核；引用公式 `\eqref{}` 确实包含所需结论
3. **编号与引用**：公式/图/表按章递增、无跳号；`\label` 与 `\ref`/ `\eqref` 一一对应
4. **无遗留错误**：无未定义变量、无前后矛盾、无未完成句子

## 文献与可复现性

- **参考文献**：统一由 `bibliography.bib` 管理（121 条）；当前 `main.tex` 用 `\bibliographystyle{plain}`（非 GB/T 7714），若切换 GB/T 7714 须更换 bibstyle 并引入 `gbt7714` 宏包
- **编译质量门禁**：xelatex + bibtex 无 error；无 undefined reference/citation 警告
- **编译验证执行方式**：涉及 xelatex 编译验证的 QA 任务（如最终编译检查、F-wave 验证），**由当前会话直接本地执行**，不委托子代理。原因：章节文件（`chNN_*.tex`）不能单独编译，必须由 `main.tex` 入口编译；子代理可能编译错误文件、PowerShell 环境差异导致阻塞、或未按格式输出 `VERDICT` 导致 boulder 暂停。

## Git 约定

- 提交时只 stage 源文件（`.tex`/`.bib` 等）
- 不要自动 commit/push
- 编译产物（`*.aux`/`*.log`/`*.pdf`/`*.bbl` 等）与 `.omo/` 已被 `.gitignore` 忽略，勿手动 stage

## 对话约定

- **公式展示**：Unicode 纯文本（如 `s=(|ξ+η|-|ξ|)/|ξ|`）
- **LaTeX 源码**：仅用于核对/修改 `.tex` 内容、检查编号
- **两套写法分离**：对话用 Unicode，写入 `.tex` 用规范 LaTeX

---

**本文件性质声明**

- 这是 **AI 指令集**，不是项目文档
- 禁止包含：历史记录、变更日志、动态信息、个人笔记、行号引用
- 项目介绍/变更历史等文档性内容请另立文件（当前仓库尚无 README.md、CHANGELOG.md）；工作记录写入 `.omo/notepads/` 对应目录
- 修改本文件须经团队 review
