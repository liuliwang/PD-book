# 拆分图 2.2 计划

## 目标

将图 2.2（`fig:bond-kinematics`）拆分为两个独立的图：图 2.2（键的几何关系）和图 2.3（键的三种伸长状态）。

## 背景

当前图 2.2 包含两个层次的内容：
1. 上半部分：(a) 参考构型、(b) 变形构型的几何关系
2. 底部三小图：s>0（拉伸）、s=0、s<0（压缩）的物理状态

这两个主题属于不同层次，放在同一图中导致信息过载。

## 拆分方案

### 图 2.2（`fig:bond-geometry`）

**内容**：
- (a) 参考构型：显示物质点 x 和 x'，键 ξ
- (b) 变形构型：显示 y 和 y'，键 ξ+η，位移 η

**图注**：键的几何关系：(a) 参考构型；(b) 变形构型

### 图 2.3（`fig:bond-stretch-states`）

**内容**：
- (a) 拉伸（s>0）：|ξ+η|>|ξ|
- (b) 参考长度（s=0）：|ξ+η|=|ξ|
- (c) 压缩（s<0）：|ξ+η|<|ξ|

**图注**：键的三种伸长状态：(a) 拉伸（s>0）；(b) 参考长度（s=0）；（c）压缩（s<0）

## 修改范围

### 文件：`chapters/ch02_framework.tex`

**第78行**（引用文字）：
```latex
% 修改前
键的几何关系与运动学量如图\ref{fig:bond-kinematics}所示：参考构型中两物质点的相对位置由 $\boldsymbol{\xi}$ 确定，变形后的当前构型中该量变为 $\boldsymbol{\xi}+\boldsymbol{\eta}$，伸长率由式\eqref{eq:bond-stretch}给出。

% 修改后
键的几何关系如图\ref{fig:bond-geometry}所示：参考构型中两物质点的相对位置由 $\boldsymbol{\xi}$ 确定，变形后的当前构型中该量变为 $\boldsymbol{\xi}+\boldsymbol{\eta}$。键的伸长率 $s$ 由式\eqref{eq:bond-stretch}定义，其三种典型状态如图\ref{fig:bond-stretch-states}所示。
```

**第80-126行**（图代码）：
- 将原 `fig:bond-kinematics` 拆分为两个独立的 `figure` 环境
- 第一个 `figure` 包含 (a) 和 (b) 部分，标签改为 `fig:bond-geometry`
- 第二个 `figure` 包含三小图，标签为 `fig:bond-stretch-states`

## 引用检查

`fig:bond-kinematics` 仅在 `ch02_framework.tex` 第78行引用，无其他引用需要更新。

## 编译验证

✅ xelatex 两遍编译成功
✅ 无 Error
✅ 无 undefined references
✅ 图编号正确

## 状态

**已完成**

## Todos

- [x] 1. 修改 `ch02_framework.tex` 第78行引用文字
- [x] 2. 拆分第80-126行图为两个独立的 `figure` 环境
- [x] 3. 编译验证（xelatex 两遍）
- [x] 4. 检查图编号和交叉引用是否正确

## 验收标准

- [x] 图 2.2 只包含参考构型和变形构型
- [x] 图 2.3 只包含三种伸长状态
- [x] 正文中对两个图的引用正确
- [x] 编译无错误
- [x] 图编号正确（图 2.2、图 2.3）
