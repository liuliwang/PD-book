# ch09 空间离散与时间积分 — 调研记录

## 任务
撰写 chapters/ch09_discretization.tex 完整正文（当前 12 行占位），目录可优化，须覆盖占位骨架 6 节主题。

## 全书衔接（撰写必须遵守）
- ch01 行348：第三部分数值方法与断裂模拟（9-11 章）"涵盖空间离散与时间积分（第 9 章）、边界条件（第 10 章）、裂纹与损伤数值模拟（第 11 章）"。行380：工程人员先读 1 章 + 9-11 章。
- ch07 行343：预告"第 9 章将介绍两类准静态求解策略——自适应动力松弛法 KilicMadenci2010 与隐式求解"。（注：此句误写"第 5 章建立的显式时间积分"，实际显式积分归属第 9 章，第 9 章要承接此语境，不纠正 ch07 措辞，只保证自身内容完备。）
- ch07 行345："如同第 5 章的键型离散"（疑误指 ch09 空间离散）。
- ch07 行1030：dual-horizon 属"离散化/多尺度技术"，"其详述见第 9 章（离散化）与第 12 章"——第 9 章须含变 horizon 离散化数值实现，但 ch05 5.5 已详述 dual-horizon 理论，第 9 章只做数值实现层面衔接，勿重复理论。
- ch06 行208：权重函数影响"表面修正（第 9、10 章）"；行328：二维 OSB 公式"在第 9 章数值实现中将反复使用"；行614：回映算法"是第 9 章数值实现的基础 cite Mitchell2011,Mousavi2021"。
- ch04 行514-527：体积修正 β(x,x')（eq:volume-beta）在离散实现中等价于判断邻居是否在近场域内，Peridigm/LAMMPS 默认采用；表面效应详细理论留待第 10 章。
- ch02 eq:motion 运动方程 ρ ü = L + b；非局部边界条件 b_eff（h=δ）。
- ch03 渐近相容性、收敛性（δ→0 且 Δx→0 双重极限）。
- ch07 7.3/7.4 已详述 NOSB 线性（CG、预条件、K_glob）与非线性（Newton、K_t、有限差分切线、载荷步、收敛判据）隐式求解——第 9 章隐式节只做策略总览与衔接，禁止重复推导。ch07 7.5 零能模式（Silling2017）——第 9 章显式积分稳定性可与零能模式衔接。
- ch08（占位）超弹性/黏弹性/蠕变/晶体弹塑性/JH-2/有限变形本构；ch10（占位）边界条件/非局部边界层/接触；ch11（占位）裂纹表征/损伤场/动态裂纹追踪；ch17（占位）数据结构/邻居搜索/MPI-GPU 并行——细节留给各章，第 9 章只预告。

## 目录设计（最终版，覆盖原 6 节骨架）
1. \section{无网格离散格式}
   - 9.1.1 均匀离散与物质点
   - 9.1.2 非均匀离散与自适应细化（含 Voronoi 图自适应离散）
   - 9.1.3 变 horizon 与对偶影响域的实现（衔接 ch05 5.5，数值实现层面）
2. \section{体积修正与积分方案}
   - 9.2.1 键积分离散误差与体积修正
   - 9.2.2 表面修正的数值实现（衔接 ch04 α、ch10 预告）
   - 9.2.3 求积方案与误差估计
3. \section{时域积分的显式方法}
   - 9.3.1 中心差分法
   - 9.3.2 速度 Verlet 与蛙跳格式（Parks2008 LAMMPS）
   - 9.3.3 显式方法的稳定性条件
   - 9.3.4 数值耗散与时间步选取
4. \section{自适应动力松弛法}
   - 9.4.1 动力松弛的基本思想（KilicMadenci2010）
   - 9.4.2 自适应参数更新（Gresho 算法）
   - 9.4.3 收敛判据与应用
5. \section{隐式求解策略}
   - 9.5.1 线性与非线性问题的隐式求解（总览，衔接 ch07 7.3/7.4）
   - 9.5.2 隐式求解的稳定性与零能模式（衔接 ch07 7.5）
6. \section{拟静力分析方法}
   - 9.6.1 准静态求解策略的比较与选择（ADR vs 隐式 vs 显式+阻尼）
   - 9.6.2 准静态断裂模拟流程（衔接 ch11）

## 可用 cite key（已在 bibliography.bib 确认存在，撰写前须再 grep 核实 title）
- 离散：SillingAskari2005（meshfree method，Comput Struct 83:1526）、Macek2007（PD via FEM）、Parks2008（Implementing PD within MD code/LAMMPS）、Ganzenmuller2015（PD-SPH similarity）、Bessa2014（reproducing kernel PD）、Seleson2009（PD upscaling of MD）、Bobaru2009（Convergence, adaptive refinement, scaling in 1D PD）、Silling2011coarsening、Dipasquale2014（Crack propagation with adaptive grid refinement in 2D PD）、BobaruDuangpanya2010（transient heat conduction）、Ren2017dualhorizon、ZhuNi2017
- 体积/表面修正：SelesonParks2011（influence function role）、SelesonLittlewood2016（Convergence studies in meshfree PD）、LeBobaru2018（Surface corrections）、MadenciOterkus2014（book）、HuHaBobaru2012（surface correction composites）
- 显式积分：SillingAskari2005、Parks2008、Warren2009（NOSB method，IJSS 46:1186）、BelytschkoLiuMoran2000（book, CFL）、Silling2017（stability correspondence）、BobaruHu2012（horizon selection/crack branching）、HaBobaru2010、Foster2010（viscoplasticity）、Silling2000
- ADR：KilicMadenci2010（TAFM 53:194）、MadenciOterkus2014、Ganzenmuller2015
- 隐式（仅总览引用）：Breitenfeld2014、BreitenfeldThesis2014、Littlewood2010、Littlewood2015、Ni2019（Static solution crack propagation）、Li2019（Implicit stabilized NOSB）、Hashim2020、Mitchell2015、QueirugaMoridis2017、Ouchi2015、Foster2011
- 综述/背景：Diehl2019（benchmark experiments）、OterkusOterkus2026（comprehensive review）、ZhangHeng2022（中文综述 力学进展 52:852）、GuZhang2019（中文综述 力学进展 49:201910）、MadenciOterkus2016

## 写作规范要点（AGENTS.md 强制）
- .tex 禁 Markdown 语法；grep '\*\*' 零命中；每节末 \emph{AI 辅助生成，需经专业审阅。}
- 公式全部 \begin{equation}+\label；正文 \eqref 引用；禁止 \[ \]
- 图/表须编号+正文 \ref 引用；表格 booktabs 三线表禁竖线；短表 p{0.22\textwidth}p{0.65\textwidth}
- 章节引用手写（"第 9 章""2.6 节"），禁 \autoref
- 章级导言 ~10 行预告各节+前后章衔接；节级导言段预告子节+文献；禁孤立 1-2 行短段；remark 全章 ≤4 条；章末收尾回扣路线图衔接下一章
- 符号首次出现定义；新符号登记 frontmatter/notation.tex（新增"第 9 章"小节）
- 推导每步标注依据；禁止"显而易见/容易证明"；新公式提示"该推导需作者人工复核"；数值算例给完整参数且数据可溯源
- 引用必须 bibliography.bib 真实 cite key，禁止编造

## 符号表现状（notation.tex 已有，避免冲突）
第 2 章：B ρ x u y ξ η f b δ H_x F_x dV_x' s η_∥ η_⊥ R w W C(ξ) s_c μ(ξ,t) φ g_0 G_c t b_eff n̂
第 4 章：c c(|ξ|) g(s,|ξ|) α(x) β(x,x') k_eff f_max
第 6 章态型：Y T t e^i e^d ψ_0 f λ H g ψ I_1 K_IC M X θ k μ m Λ a d b_F b_T b_FT Q_ij K P σ F J E S R U D C ε^(m) c<ξ> H（注：m 已用于加权体积！网格比不得用 m，可用 M 或 n=δ/Δx）
第 7 章：N(x_j) Q(x_j) U_glob F_ext K_glob R(U) F_int K_t A z<ξ> Π e(k) W^s β γ x_s F~ F^bond F^(1) F^(2) Ξ A^aij V^aijk ξ^ai a^aij v^aijk T_1^ai L(x,t) ε_tol
第 9 章需新登记：Δt（时间步长）、时间层记号 t^n、显式格式系数、ADR 的 c^n(阻尼)、k^n、λ^n、收敛判据等。注意 a 已被 ch06 复合材料参数占用，加速度用 \ddot{\mathbf{u}}（第 2 章 eq:motion 即用此记号）。

## 稳定性条件关键事实（撰写依据）
- 一维显式中心差分：SillingAskari2005 给出稳定时间步与波速关系 Δt ≤ Δx/v（v 为最大波速）；三维 PMB 稳定条件按文献推导并标注依据。
- BobaruHu2012：网格比选取影响精度（推荐 δ/Δx ≥ 3）；网格比符号避免与加权体积 m 冲突。
- Warren2009：NOSB 显式积分的稳定条件与波速关系。
- Silling2017：显式积分下零能模式稳定性（衔接 ch07 7.5）。
- HaBobaru2010/BobaruHu2012：时间步与裂纹分支、δ 的关系。
- Ganzenmuller2015：PD 与 SPH 的相似性，网格比对波速影响的数值观测。

## 2026-08-08 撰写记录：9.1--9.3 节正文定稿

### 文件规模
- 总行数：420 行（符合 400--550 目标）

### 目录结构（定稿）
与 learnings.md 设计一致，实际撰写了 9.1--9.3 共 3 节 10 个子节：
- 9.1 无网格离散格式：均匀离散与物质点、非均匀离散与自适应细化、变 horizon 与对偶影响域的实现
- 9.2 体积修正与积分方案：键积分离散误差与体积修正、表面修正的数值实现、求积方案与误差估计
- 9.3 时域积分的显式方法：中心差分法、速度 Verlet 与蛙跳格式、显式方法的稳定性条件、数值耗散与时间步选取

### 符号决策
- 网格比符号：n = δ/Δx（避免与加权体积 m 冲突，notation.tex 第 6 章已占用 m）
- 时间步：Δt，时间层 t^n
- 加速度沿用 ch02 记号 \ddot{\mathbf{u}}（a 已被 ch06 复合材料参数占用）
- β 延续 ch04 eq:volume-beta 的含义（体积修正因子，二值），本章扩展为连续 [0,1] 的 β_{ij}
- C_s：安全系数（无符号冲突）
- η：阻尼系数（无符号冲突）
- n_c：单元链表平均物质点数（局部变量）

### 本章 label 清单（全部以 eq:disc-、eq:vol-、eq:exp-、sec:disc-、tab: 前缀）
sec:disc-meshfree (9.1), sec:disc-uniform (9.1.1), eq:disc-motion-pmb, eq:disc-motion-state, eq:disc-mesh-ratio,
sec:disc-nonuniform (9.1.2), sec:disc-variable-horizon (9.1.3), eq:disc-dual-force,
sec:disc-volume (9.2), sec:disc-quadrature-error (9.2.1), eq:vol-partial-beta,
sec:disc-surface-correction (9.2.2), eq:vol-alpha-numerical,
sec:disc-quadrature-schemes (9.2.3), eq:vol-l2-error,
sec:disc-explicit (9.3), eq:exp-semi-discrete,
sec:disc-central-difference (9.3.1), eq:exp-cd-velocity, eq:exp-cd-acceleration, eq:exp-cd-update, eq:exp-cd-startup,
sec:disc-verlet-leapfrog (9.3.2), eq:exp-verlet-step1, eq:exp-verlet-step2, eq:exp-leapfrog-velocity, eq:exp-leapfrog-displacement, eq:exp-leapfrog-startup, tab:exp-schemes,
sec:disc-stability (9.3.3), eq:exp-cfl-1d, eq:exp-c-3d, eq:exp-stability-3d, eq:exp-wave-speed, eq:exp-safe-dt, tab:stability-dimensional,
sec:disc-dissipation (9.3.4), eq:exp-damped-motion, eq:exp-cd-damped, eq:exp-num-wave

### 引用的其他章 label
- ch02: eq:motion, eq:reaction, fig:boundary-truncation
- ch04: eq:volume-beta, eq:surface-alpha, eq:surface-correction-c, eq:keff-pmb
- ch07: eq:zero-energy-stability-condition, eq:zero-energy-nullspace
- （ch05 sec:dual-horizon 以手写"第 5 章 5.5 节"引用，未用 label）

### 引用的 cite key（共 24 个，均在 bibliography.bib 核实）
Silling2000, SillingAskari2005, Parks2008, Ganzenmuller2015, Seleson2009, Bobaru2009, BobaruHu2012, HaBobaru2010, Silling2011coarsening, Dipasquale2014, BobaruDuangpanya2010, Bessa2014, Ren2017dualhorizon, MadenciOterkus2014, LeBobaru2018, SelesonLittlewood2016, HuHaBobaru2012, LeBobaru2018Obj, BelytschkoLiuMoran2000, Warren2009, Silling2017, KilicMadenci2010, Foster2010, Diehl2019

### 采用的稳定性公式
- 一维 CFL：Δt ≤ Δx/v_c（由弹簧-质量模型推导，ω_max ≈ 2v_c/Δx，中心差分稳定条件 ω_max·Δt ≤ 2）
- 三维 PMB：Δt ≈ C_s·Δx_min/c_max，c_max = sqrt((K+4G/3)/ρ) = sqrt(E(1-ν)/(ρ(1+ν)(1-2ν)))
- 安全系数 C_s：弹性波 0.8~1.0，含损伤 0.5~0.8，接触/碰撞 0.2~0.5
- BobaruHu2012 关于 n=2 需额外降低 C_s 10%~20% 的数值观测
- NOSB 需配合稳定化技术（衔接 ch07 eq:zero-energy-stability-condition）

### 数值算例
- 9.1.2：二维 PMB 非均匀离散演示参数（E=30GPa, ν=1/3, ρ=2400, δ=2mm, Δx1=δ/5, Δx2=δ/3）
- 9.3.4：三维 PMB 铝杆波传播演示参数（E=72GPa, ν=1/4, ρ=2700, Δx=1mm, δ=3.15mm, n=3.15, Δt=1.42×10^{-7}s, C_s=0.8）

### 格式检查结果
- grep '\*\*'：零命中 ✓
- grep '\\\['：仅 \\[4pt] 行间距（align 环境），无不编号公式 ✓
- grep '\\autoref'：零命中 ✓
- 所有公式用 \begin{equation}+\label ✓
- 手写章节引用（"第 X 章""X.X 节"）✓
- remark 全章 2 条（9.1.1、9.3.1），≤4 条约束 ✓
- 每节末尾 \emph{AI 辅助生成...} ✓
- 推导提示"需作者人工复核"：9.3.3 节一维稳定性推导处 ✓
- 量纲检查：9.3.3 节表 tab:stability-dimensional ✓

### 已知问题与后续任务注意
- 符号表 notation.tex 需新增第 9 章符号（Δt, t^n, n=δ/Δx, C_s, η, c_max 等），由后续任务统一更新
- 未引用 cite key：GuZhang2019, ZhangHeng2022, OterkusOterkus2026, MadenciOterkus2016（保留给后续 9.4-9.6 使用）
- 未使用的 label：部分方程 label 定义后在紧邻正文中直接解释而未显式 \eqref（如 eq:disc-mesh-ratio、eq:exp-leapfrog-velocity），在学术专著中属常见写法

## 2026-08-08 修复记录：主协调者发现的 5 处问题

### 问题 1（严重）微模量公式错误 — 行 310
- 修复前：c = 18E/(πδ⁴) 
- 修复后：c = 12E/(πδ⁴)
- 依据：ch04 eq:rate-3d 定稿值为 12E/(πδ⁴)（ν=1/4；SillingAskari2005 原文 18k/(πδ⁴) 中 k 为体积模量，ν=1/4 时 k=2E/3 → 12E/(πδ⁴)）
- 同步修改：行 313 括注由"三维情形下…"改为"三维 PMB 微模量，与第 4 章式 \eqref{eq:rate-3d} 一致 \cite{SillingAskari2005}；…"
- grep 确认：无其他 "18" 引用残留

### 问题 2 阻尼差分公式推导描述不一致 — 行 379
- 修复前：文字称"向后差分近似 (u_i^n - u_i^{n-1})/Δt"
- 修复后：文字改为"中心差分近似 (u_i^{n+1} - u_i^{n-1})/(2Δt)"，并补充"与 u^{n+1} 耦合但可显式解出"
- 验证：所得阻尼中心差分公式 (1+ηΔt/2ρ)u^{n+1}=[2u^n-(1-ηΔt/2ρ)u^{n-1}+(Δt²/ρ)(F^n+b^n)] 确实由中心差分速度近似推导

### 问题 3 9.1.2 演示算例 Δt 数量级错误 — 行 70
- 修复前：Δt≈5×10^{-9} s
- 修复后：Δt≈5×10^{-8} s
- 依据：按 9.3.3 公式 C_s·Δx_min/c_max，平面应力 c_max≈3751 m/s，Δx_1=4e-4 m → Δt_cr≈1.07e-7 s，C_s=0.5 → ≈5.3e-8 s
- 总模拟时长 2×10^{-5} s 不变（约 400 步）

### 问题 4 BobaruHu2012 玻璃算例 Δt 内部矛盾 — 行 396
- 修复前：Δt≈2×10^{-9} s（与 C_s=0.5, Δx=2e-4, c_max≈5e3 矛盾）
- 修复后：Δt≈2×10^{-8} s
- 验证：0.5×2e-4/5e3 = 2×10^{-8} s，与公式自洽

### 问题 5 ω_max≈2v_c/Δx 表述跳跃 — 行 299
- 修复前："可得 ω_max≈2v_c/Δx"
- 修复后：改为"近似可得 ω_max 的量级为 2v_c/Δx（该估计假定…，属保守的工程近似；严格值依赖具体离散与影响函数，见下文人工复核注记）"
- 说明：单键弹簧分析给出 ω≈2.76v_c/(n²Δx)，n=3 时 ≈0.307v_c/Δx，2v_c/Δx 是保守上限估计

## 2026-08-08 撰写记录：9.4--9.6 节正文定稿

### 文件规模
- 总行数：697 行（从 420 行扩展，符合 650--700 目标）

### 目录结构（定稿）
- 9.4 自适应动力松弛法：9.4.1 动力松弛的基本思想、9.4.2 自适应参数更新（Gresho 算法）、9.4.3 收敛判据与应用
- 9.5 隐式求解策略：9.5.1 线性与非线性问题的隐式求解（总览，衔接 ch07 7.3/7.4）、9.5.2 隐式求解的稳定性与零能模式（衔接 ch07 7.5）
- 9.6 拟静力分析方法：9.6.1 准静态求解策略的比较与选择（含选择准则表 tab:qs-comparison）、9.6.2 准静态断裂模拟流程（衔接到 ch11）
- 章末收尾段：回扣本章路线图，衔接第 10 章（边界条件）与第 11 章（裂纹与损伤）

### 新增 label 清单（前缀无冲突，全部 grep 核实）
9.4 节：sec:adr, sec:adr-basics, sec:adr-gresho, sec:adr-convergence
  eq:adr-damped-motion, eq:adr-cd-damped, eq:adr-rayleigh, eq:adr-potential-measure, eq:adr-mass-measure, eq:adr-gresho-c, eq:adr-gresho-dt, tab:adr-gresho, eq:adr-kinetic, eq:adr-convergence-kinetic, eq:adr-residual, eq:adr-convergence-force
9.5 节：sec:imp-strategies, sec:imp-overview, sec:imp-stability, eq:imp-reduced-system
9.6 节：sec:qs-analysis, sec:qs-comparison, sec:qs-fracture, tab:qs-comparison
（注：sec:implicit-* 前缀已在 ch07 被占用，故 ch09 隐式节改用 sec:imp-* 前缀）

### 引用的 ch07 label（仅 \eqref 引用，不重复推导）
- eq:implicit-equilibrium, eq:global-system, eq:bc-partition, eq:bc-eliminated, eq:jacobi-precond（7.3 线性隐式）
- eq:nl-residual, eq:nr-iteration, eq:tangent-stiffness, eq:tangent-nosb, eq:load-stepping-equation, eq:convergence-residual, eq:smooth-softening, eq:softening-tangent（7.4 非线性隐式）
- eq:zero-energy-stability-condition, eq:zero-energy-nullspace, eq:stabilization-energy, eq:stabilization-force（7.5-7.6 零能模式与稳定化）
- eq:discrete-shape-tensor, eq:discrete-grad-u, eq:discrete-strain, eq:strain-matrix-form, eq:family-stiffness-block（7.3 离散化）

### 引用的 cite key（共 18 个，均在 bibliography.bib 有真实条目）
KilicMadenci2010（主文献，ADR 奠基性工作）、MadenciOterkus2014、MadenciOterkus2016、
Ni2019（静态裂纹扩展隐式求解）、Li2019（稳定化 NOSB 隐式）、
Breitenfeld2014、BreitenfeldThesis2014、Littlewood2015、Mitchell2015、
Hashim2020（解析 Jacobian+平滑软化隐式）、Ouchi2015（隐式流固耦合）、
HaBobaru2010、Diehl2019、ZhangHeng2022、Silling2017、Chen2018
（未使用：Underwood1983、Gresho1980 不在 bibliography.bib，已替换为 KilicMadenci2010）

### 格式检查结果
- grep '\*\*'：零命中 ✓
- grep '\\\[' 独立行：零命中（无不用 \begin{equation} 的公式）✓
- grep '\\autoref'：零命中 ✓
- remark 全章 3 条（9.1.1, 9.3.1, 9.4.1），≤4 条约束 ✓
- 所有公式用 \begin{equation}+\label ✓
- 手写章节引用（"第 7 章 7.3 节""9.3.3 节"等）✓
- 每节末尾 \emph{AI 辅助生成...}：9.4.1, 9.4.2, 9.4.3, 9.5.1, 9.5.2, 9.6.1, 9.6.2 ✓
- 章末收尾段含衔接第 10、11 章预告 ✓
- 推导提示"需作者人工复核"：9.4.2 节瑞利商近似推导处 ✓

### 符号登记
- notation.tex 新增"第 9 章 空间离散与时间积分"小节，登记 27 个新符号
- 关键符号：\Delta t, n=\delta/\Delta x, C_s, \eta, c_{\max}, C_{\text{ADR}}, E_{\text{kin}}, \varepsilon_{\text{ADR}}, \omega^{n}, P^{n}, Q^{n}, \mathbf{K}^{n}, \lambda, N_{\text{step}}
- 与已有符号无冲突（m 仍为加权体积、a 仍为复合材料参数）

### 已知问题
- ch07 7.3 节预告语"第 9 章将介绍两类准静态求解策略"中误写"第 5 章建立的显式时间积分"，未在本次修正（属 ch07 内容）
- ch07 sec:implicit-* 前缀占用导致 ch09 隐式节不得不用 sec:imp-* 替代，若将来 ch07 label 重构可统一为 sec:chNN-* 前缀

### 删除原 9.1--9.3 小节
原 9.3.4 末尾的"本章 9.1--9.3 节小结"段在本次更新中移入章末收尾段（与 9.4--9.6 节内容合并为全章总结），原处不留残段。

## 2026-08-08 修复记录：9.5.1 节无 label 公式清理
- 位置：9.5.1 节"非线性问题"段落（原行 584-587）
- 问题：独立成行 equation（K_t(U^l)·ΔU^{l+1}=R(U^l)）无 \label，且是对 ch07 eq:nr-iteration 的重复定义，违反 AGENTS.md"公式须 \begin{equation}+\label"强制规定
- 修复：删除整个 equation 环境，改写为纯文字引用"在第 $l$ 次迭代，求解线性化系统（即式 \eqref{eq:nr-iteration}）"，括号原文保留并直接跟随文字，原其后"其中切线刚度矩阵…"衔接不变
- 验证：grep 确认 begin=31 end=31 配对，正则逐块检查全部 31 个 equation 均含 \label；\eqref{eq:tangent-stiffness}、eq:tangent-nosb、eq:convergence-residual、eq:load-stepping-equation 等引用保持不动
- 全文件其余内容未改；文件 697 行 → 692 行（删除 5 行：equation 4 行 + 1 空行）

## 2026-08-09 最终验证结论
- ch09_discretization.tex 定稿 692 行：6 节 17 子节、64 label、3 表（tab:exp-schemes/tab:adr-gresho/tab:qs-comparison）、3 条 remark（≤4 ✓）
- notation.tex 新增第 9 章小节（27 符号，longtable 格式合规）
- 全链编译通过：xelatex(210页)→bibtex→xelatex(228页)→xelatex(228页)，无 error，无 ch09 undefined reference
- 未引用 label 为项目惯例（ch04 29 个/ch07 26 个同样存在），非违规
- 遗留问题（非本次范围）：ch05 引用 3 个 bib 缺失 key：DianaCasolo2019（行91/144/275）、WangZhouShou2017（行164/200/206）、WangZhouWang2018（行164/200/206）；hyperref PDF string 警告 4 处来自 ch03 行 291（既有）。建议后续补 bib 条目或改引。
- 修复记录：ch09 无 label 公式已删（9.5.1 Newton 迭代式改为引用 ch07 eq:nr-iteration）；c=12E/(πδ⁴) 与 ch04 eq:rate-3d 一致；阻尼差分描述改中心差分；两处算例 Δt 数量级已修正
