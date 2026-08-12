## [2026-08-07] 第4章写作大纲与理论要点

### 章使命（ch03 末尾原文）
"第 4 章将在此理论基础上具体化键型 PMB 模型的微弹性势、参数率定与表面效应修正"

### 优化后目录
- 章导言段（~10行）：回顾第2章一般框架+第3章经典对应 -> 具体化键型模型族；预告各节；衔接第5/6章
- 4.1 键型理论的基本假设：4.1.1 三假设（成对性、中心力 eq:central-force、微弹性 eq:pairwise-force-potential）；4.1.2 键型对力一般形式（客观性+交换对称性约化，f 仅依赖单根键）；4.1.3 键型模型族分类（线性微弹性、PMB、非线性微势）
- 4.2 微势与键力密度函数：4.2.1 微势构造与物理要求（w(0)=0、w'(0)=0、凸性）；4.2.2 键力密度 f=c(|ξ|)s(ξ+η)/|ξ+η|、线性化 f=c(|ξ|)sξ?；4.2.3 微模量张量 C(ξ)=c(|ξ|)ξ?ξ/|ξ|2（衔接3.3 eq:iso-micro-modulus）；4.2.4 应变能密度键型形式
- 4.3 经典微弹脆性模型（PMB）：4.3.1 完整定义（w=?cs2|ξ|、f=cs(ξ+η)/|ξ+η|、断键μ引用第2章2.7）；4.3.2 力-伸长率关系与卸载路径（线性+突降+永久断裂，图）；4.3.3 G_c 与 s_c 重述（标注推导见2.7.3，勿重复）；4.3.4 适用范围与典型参数（SillingAskari2005、Bobaru2016）
- 4.4 材料参数的率定（核心）：4.4.1 率定原理（应变能密度等价）；4.4.2 一维 c=2E/(Aδ2)；4.4.3 二维平面应力 c=9E/(πtδ3)、平面应变 c=48E/(5πtδ3)；4.4.4 三维 c=12E/(πδ?)、K=2E/3、μ=2E/5；4.4.5 微模量-经典模量对应表
- 4.5 表面效应及其修正：4.5.1 回顾与数值影响（勿重复2.8 k_eff）；4.5.2 微模量修正法；4.5.3 体积修正法（可展开）；4.5.4 虚拟材料层+短程力；4.5.5 四方法对比表
- 4.6 键型模型的固有局限：4.6.1 泊松比锁定（根源=单参数微模量）；4.6.2 可压缩性限制；4.6.3 对力仅依赖单键变形（->第5章微梁/共轭键/键转动预告）；4.6.4 各向异性困难（->第5章各向异性键型预告）
- 章末收尾段（回扣+衔接第5/6章）

### 率定公式（已独立推导验证）
一维：c=2E/(Aδ2)（单轴应变）；二维平面应力：c=9E/(πtδ3)（等双轴 σ_zz=0，横向收缩比1/3）；二维平面应变：c=48E/(5πtδ3)（等双轴 ε_zz=0，材料ν=1/4）；三维：c=12E/(πδ?)（均匀膨胀，ν=1/4）
推导模板（三维）：均匀膨胀 s=ε；W_PD=?∫?cε2r·4πr2dr=πcε2δ?/4；经典 W=9Kε2/2，K=2E/3 -> W=3Eε2；πcδ?/4=3E -> c=12E/(πδ?)。二维 W_PD=πctε2δ3/6。

### 2倍因子陷阱（关键）
σ_PD 满足 σ_PD=2·?W_PD/?ε。用 λ_PD=μ_PD=4πR/15 反推 E 得 E_PD=2E 矛盾。率定纯用能量法；物理模量 μ=2E/5、K=2E/3（ν=1/4）；衔接第3章只提"与 eq:pd-lame 对应"，不展开数值反推。

### 必须避免重复
2.7.3 s_c-G_c 推导；2.8 k_eff 公式+三类修正概述；3.3 λ=μ=4πR/15 推导+4π/15积分+ν根源；2.4.1 泊松比锁定；第2章基本概念（键、近场域、运动方程、量纲）

### 文献 keys（已验证存在）
Silling2000, SillingAskari2005, Silling2007, SillingLehoucq2008, SillingLehoucq2010, Silling2017, MadenciOterkus2014, Bobaru2016, Bobaru2009, LeBobaru2018, Mitchell2015, TrageserSeleson2020, KilicMadenci2010, SillingZimmermannAbeyaratne2003, HaBobaru2010, BobaruHu2012, DuZhou2011, Dipasquale2014, Bessa2014

### 项目规范
编译 xelatex×2+bibtex（本会话验证）；公式 equation+label 禁 \[ \]；图/表编号+正文引用；booktabs 三线表；TikZ 库章节头声明+坐标带单位；章节引用手写禁 \autoref；章导言~10行、节级导言自含、禁孤立短段、remark≤4、章末收尾；每节末尾 "\emph{AI 辅助生成，需经专业审阅。}"；禁 Markdown 语法、写完 grep \*\* 零命中；\cite 仅真实 keys；新术语首现定义；推导每步标注依据；参照 ch02/ch03 行文风格


## [2026-08-07] Part 1 completed: Chapter intro + 4.1-4.3 (340 lines)

### Completed content:
- **Chapter intro**: ~10 lines, references ch02 framework and ch03 classical correspondence, previews all 6 sections, links to ch05 (improved models) and ch06 (state-based theory)
- **4.1 Key-based theory assumptions**: 4.1.1 Three assumptions (pairwise nature, central force eq:central-force, microelastic eq:pairwise-force-potential); 4.1.2 General form of bond force via objectivity eq:potential-objectivity and symmetry eq:potential-symmetry, deriving w=w(s,|xi|) and f=(1/|xi|)(dw/ds)(xi+eta)/|xi+eta|; 4.1.3 Model family classification (linear microelastic, PMB, nonlinear micropotential) with literature sources
- **4.2 Micropotential and bond force density**: 4.2.1 Physical requirements (w(0)=0, w'(0)=0, convexity, dimensional analysis); 4.2.2 Explicit force density forms (general, linear full, linear small); 4.2.3 Micro-modulus and micro-modulus tensor (C(|xi|) relation to ch03 eq:iso-micro-modulus, attenuation forms previewing ch05); 4.2.4 Bond-type strain energy density (W = 1/2 int w dV', linear and PMB forms)
- **4.3 PMB model**: 4.3.1 Complete definition (w=1/2 c s^2 |xi|, f=c s (xi+eta)/|xi+eta|, bond failure via mu eq:history-variable); 4.3.2 Force-stretch relationship with TikZ figure fig:pmb-force-stretch (linear loading, abrupt failure, irreversible failure, unload/reload paths, distinguished from ch02 fig:force-stretch); 4.3.3 Fracture energy and critical stretch (restating eq:sc-gc-pmb-3d and eq:sc-gc-pmb-2d from ch02 2.7.3 with PMMA example parameters); 4.3.4 Applicability (brittle materials, delta selection m>=3, c calibration formulas, connections to later chapters)
- **Transition paragraph**: bridges Part 1 (theory) to Part 2 (sections 4.4-4.6, engineering application)

### Key new labels created:

eq:central-force-recall, eq:central-force-scalar, eq:pairwise-force-potential-recall, eq:force-from-w, eq:pairwise-potential-simplified, eq:pairwise-potential-alt, eq:key-force-dir, eq:linear-bond-force, eq:linear-micro-potential, eq:w-zero-condition, eq:w-derivative-zero, eq:w-convexity, eq:f-general-form, eq:f-linear-full, eq:f-linear-small, eq:C-tensor-bond, eq:C-comparison, eq:ch4-strain-energy, eq:ch4-strain-energy-linear, eq:ch4-strain-energy-pmb, eq:pmb-potential, eq:pmb-force, eq:pmb-damaged-force, eq:sc-gc-pmb-3d-recall, eq:sc-gc-pmb-2d-recall

### Verification passed:
- Zero '**' hits (no markdown syntax)
- Zero standalone '[' or ']' equations
- All \cite keys verified in bibliography.bib (Silling2000, SillingAskari2005, Silling2007, SillingZimmermannAbeyaratne2003, HaBobaru2010, Bobaru2016, KilicMadenci2010, Bobaru2009, TrageserSeleson2020)
- All \eqref references to ch02/ch03 labels verified existing (eq:motion, eq:central-force, eq:pairwise-force-potential, eq:potential-objectivity, eq:potential-symmetry, eq:bond-stretch, eq:stretch-linear, eq:stretch-uniform, eq:linear-force, eq:dim-force, eq:reaction, eq:strain-energy, eq:history-variable, eq:iso-micro-modulus, eq:pd-lame, eq:sc-gc-pmb-3d, eq:sc-gc-pmb-2d)
- All \ref references verified (fig:pmb-force-stretch defined, fig:force-stretch from ch02 verified)
- 2 remarks total (one in 4.1.1, one in 4.3.1) - within 4-remark limit
- AI declaration at end of each section (4.1, 4.2, 4.3)
- Sections 4.4, 4.5, 4.6 headers preserved as placeholders

## [2026-08-07] 阶段1完成验证
- 4.1-4.3 已写入（338行），7+1处修正全部通过审查与编译（0 error, 0 undefined）
- 修正要点：line98 无残余力；line135 J/m^6；line203 W=3Eε^2（K=2E/3）；line234 2.7.1节；line313 c=1.4e20, s_c=3.9e-3；line325 NOSB本构对应表述；TikZ f_max=3.8
- 阶段2目标：4.4 率定（能量法：一维2E/(Aδ^2)、二维平面应力9E/(πtδ^3)ν=1/3、平面应变48E/(5πtδ^3)ν=1/4、三维12E/(πδ^4)K=2E/3 μ=2E/5）+4.5 表面效应修正（回顾2.8勿重复、微模量/体积/虚拟层/短程力修正、对比表）


## [2026-08-07] Stage 2 completed: Sections 4.4 and 4.5 (500 lines total)

### 4.4 Material parameter calibration (energy method)
- **4.4.1 Rate-ding principle**: Energy equivalence W_PD = W_CCM under uniform deformation; explicitly avoids Ch3 stress tensor method (factor-2 ambiguity from sigma_PD definition)
- **4.4.2 1D**: c = 2E/(A*delta^2), derived from integral of |xi| on [-delta,delta] = delta^2
- **4.4.3 2D plane stress**: c = 9E/(pi t delta^3), equi-biaxial with nu=1/3, verified with SillingAskari2005, MadenciOterkus2014
- **4.4.3 2D plane strain**: c = 48E/(5 pi t delta^3), equi-biaxial with nu=1/4, full 3D Hooke derivation with epsilon_zz=0 constraint; verified sigma_xx = 2(lambda+mu)epsilon = 8E/5 epsilon; noted common pitfall (using plane stress formula yields incorrect 8E/(pi t delta^3))
- **4.4.4 3D**: c = 12E/(pi delta^4), isotropic expansion with nu=1/4, consistent with 4.2.4 line 203 and 4.3.3 PMMA example (c~1.4e20); derived auxiliary moduli: mu=2E/5, K=2E/3, lambda=mu=2E/5
- **4.4.5 Parameter summary table** (tab:rate-summary): booktabs table with 4 rows (1D/2D-PS/2D-PE/3D), columns: dimension, deformation mode, integral value, c formula, nu_eff

### 4.5 Surface effect and corrections
- **4.5.1 Quantitative review**: references ch02 eq:effective-stiffness and eq:surface-stiffness; k_eff^(bdy) ~ 0.5 k_eff^(inf) for 3D flat surface; scale dependency L/delta; cites LeBobaru2018, BobaruHu2012, MadenciOterkus2014
- **4.5.2 Micro-modulus correction**: c -> c/alpha(x), alpha = V_H/V_H^inf; simple to implement but alpha hard to compute for complex geometry; cites LeBobaru2018
- **4.5.3 Volume correction**: corrects integration measure beta(x,x') instead of c; naturally compatible with mesh-based discretization; cites Bobaru2016
- **4.5.4 Fictitious material layer + short-range force correction**: virtual layer extends delta beyond boundary; Mitchell2015 short-range force on boundary pairs; comparison table (tab:surface-methods)

### Verification:
- Zero '**' hits, zero standalone '[' or ']' equations
- 5 AI declarations (4.1 through 4.5), 2 remarks total (within 4-remark limit)
- 19 new labels following eq:rate-*, eq:surface-*, tab:rate-*, tab:surface-* conventions
- All cite keys verified (SillingAskari2005, MadenciOterkus2014, Bobaru2016, LeBobaru2018, BobaruHu2012, Mitchell2015)
- All cross-references verified (eq:effective-stiffness, eq:surface-stiffness from ch02; eq:C-tensor-bond, eq:ch4-strain-energy-pmb, eq:stretch-uniform, eq:pd-lame, eq:poisson-limit from existing chapters)
- Plane strain calibration verified: sigma_xx=2(lambda+mu)epsilon=8E/5 epsilon, W=8E/5 epsilon^2, W_PD=pi c t delta^3/6 -> c=48E/(5 pi t delta^3)


## [2026-08-07] Stage 3 (final) completed: Section 4.6 + closing paragraph (601 lines total)

### Pre-corrections (2 items)
1. **Line 329**: '第10章工程算例' -> '第10章边界条件处理' (correct chapter topic)
2. **Line 483**: Removed inaccurate 'weighted average of bond lengths' claim; replaced with 'integral domain halves, effective stiffness approximately halves'

### 4.6 Intrinsic limitations of bond-based models (3 subsections)
- **4.6.1 Poisson ratio lock**: Restates nu=1/4 (3D) and nu=1/3 (2D PS) from eq:poisson-limit; root cause: single parameter R=int c r^4 dr vs. two needed; Cauchy relation C_1122=C_1212 (cite TrageserSeleson2020); consequences for real materials (metals nu~0.3, rubber nu~0.5); impact on s_c calibration
- **4.6.2 Single-bond dependency**: Core limitation: f(eta,xi) only depends on one bond; no transverse coupling; three consequences: (a) no bending stiffness - adjacent bond rotations produce zero resistance; (b) volume-shear inseparability at single-bond level; (c) limited constitutive expressiveness - plastic flow, viscoelasticity, rate-dependence require state framework; unified root cause: 'bond-independence' assumption
- **4.6.3 Anisotropy and computational challenges**: Isotropic c(|xi|) cannot express directionality; anisotropic c(xi-hat) possible but Poisson lock remains; computational: mesh sensitivity (m=delta/dx, mesh bias cite BobaruHu2012), surface effect residual; cost-accuracy spectrum: PMB->improved bond->ordinary state->non-ordinary state

### Chapter closing paragraph
Recaps chapter roadmap (4.1 assumptions -> 4.2 micropotential -> 4.3 PMB -> 4.4 calibration -> 4.5 surface -> 4.6 limitations); central theme: 'bond-independence' gives simplicity and efficiency at cost of nu-lock, no bending, limited expressiveness; previews ch05 (micro-modulus decay, micro-beam, conjugate bond, bond rotation, dual-influence) and ch06 (state-based, T = 1/2 f as special case)

### Verification:
- Zero '**' hits, zero standalone '[' or ']' equations
- 6 AI declarations (4.1 through 4.6), 2 remarks total (within 4-remark limit)
- 1 new label: eq:limit-poisson (restating nu constraint within 4.6)
- All cite keys verified: TrageserSeleson2020, BobaruHu2012 in bibliography.bib
- All cross-references verified: eq:poisson-limit (ch02), eq:pd-lame (ch03), eq:sc-gc-pmb-3d-recall, eq:sc-gc-pmb-2d-recall (ch04 4.3.3), eq:limit-poisson (ch04 4.6)
- Chapter 5 section titles (from ch05 skeleton) accurately previewed: micro-modulus decay, micro-beam, conjugate bond, bond rotation, dual-influence domain, anisotropic
- Chapter 6 opening text (ch06_ordinary_state.tex sec:state-limits) consulted for consistency - 4.6 text aligns with ch06 framing of bond-based limitations

## [2026-08-07] 第4章完成
- ch04_bond_based.tex 601 行：4.1 基本假设/4.2 微势与键力密度/4.3 PMB/4.4 率定（1D 2E/(Aδ^2)、2D-PS 9E/(πtδ^3)、2D-PE 48E/(5πtδ^3)、3D 12E/(πδ^4)）/4.5 表面效应（微模量/体积/虚拟层/短程力）/4.6 局限 + 章末收尾
- notation.tex 新增第4章符号小节（7 符号：c、c(|ξ|)、g、α、β、k_eff、f_max）
- 最终编译：0 error、0 undefined、0 multiply defined；main.pdf 1.93MB
- remark 全章 2 条、AI 声明 6 条、图 1 幅（TikZ PMB 力-伸长率）、表 2 张（rate-summary、surface-methods）
