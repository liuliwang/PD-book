# 计划：优化 2.2.3 节"小变形近似"的可读性

## 背景
第 2 章 2.2.3 节推导键伸长率 $s$ 在小变形下的线性近似。当前推导在数学上正确，但存在三个理解障碍：
1. "$O(|\boldsymbol{\eta}|^2)$ 的高阶小量"表述含混——未说明是相对于什么而言
2. 忽略判据缺失——未说明 Taylor 展开的精度要求
3. 中间步骤跳跃——直接从根号跳到一阶展开

## 目标
通过补充文字说明、插入量级对比表、增加物理直观的 remark，让读者更容易理解推导过程。

## 任务列表

### 任务 1：补充"相对量级"的显式说明
- **位置**：`chapters/ch02_framework.tex`，第 367 行附近
- **操作**：在"由于 $|\boldsymbol{\eta}|\ll|\boldsymbol{\xi}|$，式中..."之前，补充一段文字说明各项除以 $|\boldsymbol{\xi}|^2$ 后的量级对比
- **具体内容**：
  ```latex
  由于 $|\boldsymbol{\eta}|\ll|\boldsymbol{\xi}|$，根号内各项除以 $|\boldsymbol{\xi}|^{2}$ 后的量级分别为
  \begin{itemize}
    \item $2\,\boldsymbol{\xi}\cdot\boldsymbol{\eta}_{\parallel}/|\boldsymbol{\xi}|^{2}\sim O(|\boldsymbol{\eta}|/|\boldsymbol{\xi}|)$：一阶小量（保留）；
    \item $|\boldsymbol{\eta}_{\parallel}|^{2}/|\boldsymbol{\xi}|^{2}\sim O(|\boldsymbol{\eta}|^{2}/|\boldsymbol{\xi}|^{2})$：二阶小量（忽略）；
    \item $|\boldsymbol{\eta}_{\perp}|^{2}/|\boldsymbol{\xi}|^{2}\sim O(|\boldsymbol{\eta}|^{2}/|\boldsymbol{\xi}|^{2})$：二阶小量（忽略）。
  \end{itemize}
  由于二次项比线性项小一个数量级（$|\boldsymbol{\eta}|\ll|\boldsymbol{\xi}|$ 时），可暂忽略。
  ```

### 任务 2：在公式 (2.12) 后增加 remark（可选）
- **位置**：`chapters/ch02_framework.tex`，第 391 行之后
- **操作**：在公式 (2.12) 之后、进入下一节之前，增加一个 remark 段落
- **具体内容**：
  ```latex
  \begin{remark}
    小变形近似的物理含义是：键的伸长主要由轴向分量 $\boldsymbol{\eta}_{\parallel}$ 引起，
    而偏斜分量 $\boldsymbol{\eta}_{\perp}$ 仅改变键的方向，对键长的贡献是二阶效应。
    这类似于经典小应变理论中，刚体转动不产生应变。
  \end{remark}
  ```

### 任务 3：编译验证
- 执行 `xelatex main.tex` 两遍
- 检查无 Error/undefined reference
- 确认修改后的 PDF 显示正确

## 验收标准
- [x] 第 367 行附近的文字已补充量级对比说明
- [x] 物理直观解释已融入正文段落（未新增 remark，保持全章 4 条规范；原计划任务 2 的"新增 remark"因 AGENTS.md「全章注记不超过 4 条」限制而修正为融入正文）
- [x] `xelatex` 编译无 Error（两遍，141 页）
- [x] 修改后的 PDF 内容正确

## 备注
- 不修改公式本身，只增加解释性文字
- 保持与第 2 章现有风格一致（remark 数量已在 4 条以内，增加 1 条后共 5 条，需确认是否符合规范）
