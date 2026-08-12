# 修复 Problems 面板 Error/Warning

## 目标
消除 LaTeX 项目中导致 Problems 面板报错的所有问题，使 xelatex + bibtex 完整编译零 error。

## Todos

- [x] 1. `bibliography.bib`: 删除第 1748–1758 行格式错误块（嵌套条目 WangZhouShou2017/DianaCasolo2019）- expect BibTeX parse error 消除
- [x] 2. `bibliography.bib`: 将原第 1750 行的论文（"A full orthotropic micropolar peridynamic formulation..."）以新键名 `DianaCasolo2019ortho` 添加到第 1590 行之后（紧接现有 DianaCasolo2019 之后）- expect 该文献可正常引用
- [x] 3. `bibliography.bib`: 删除第 1738–1746 行（DianaCasolo2019 重复条目）- expect repeated entry warning 消除
- [x] 4. `bibliography.bib`: 删除第 1760–1768 行（WangZhouShou2017 重复条目）- expect repeated entry warning 消除
- [x] 5. `bibliography.bib`: 删除第 1770–1778 行（WangZhouWang2018 重复条目）- expect repeated entry warning 消除
- [x] 6. 清理残留编译产物：删除项目根目录和 `chapters/` 下所有 `*.aux`、`*.bbl`、`*.blg`、`*.log`、`*.out`、`*.toc` 文件 - expect 干净编译环境
- [x] 7. 执行完整四步编译 `xelatex → bibtex → xelatex → xelatex`，检查 `.log` 文件中的 error/warning - expect 零 BibTeX error，无 repeated entry warning，无 undefined reference（或仅限骨架章节的预期缺失）
- [x] 8. 若编译发现 undefined citation/reference，定位并修复（补录 bib 条目或修正 ref 键名）- expect 所有 `\cite` 和 `\ref` 均有对应定义

## 验收标准
- `xelatex main.tex` + `bibtex main` 无 error
- `.log` 中无 `repeated entry` 警告
- `.log` 中无 `Expecting a curly bracket` 错误
- 生成的 PDF 可正常打开，参考文献正确显示

## 约束
- 不修改 `main.tex` 结构
- 不修改 `preamble.tex`
- 不修改章节文件内容（除非发现 undefined reference 需修正键名）
- 新增的 `DianaCasolo2019ortho` 条目内容与原第 1750 行完全一致，仅改键名
