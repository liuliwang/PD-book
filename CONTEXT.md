# Peridynamics Monograph — Domain Glossary

Terminology for the LaTeX book project on Peridynamics theory and numerical methods (ctexbook, A4, 11pt). This glossary captures canonical terms and their definitions as established across the 19-chapter monograph. It does not contain implementation details or writing conventions — those live in AGENTS.md.

## Language

**键** (bond): 近场动力学中连接物质点 x 与 x'=x+ξ 的基本相互作用单元。
_Avoid_: bond-based, 键型（←see 键基/键型）

**态** (state): 定义在近场域内所有键矢量上的函数，将族内键信息打包为整体的数学工具。
_Avoid_: 物理状态, state-based

**变形态** (deformation state) Y[x,t]⟨ξ⟩=ξ+η: 记录每根键变形后几何的态；值域为变形后键矢量 ξ+η = y(x+ξ,t) − y(x,t)，与键基记号 ξ+η = y(x',t) − y(x,t)（x'=x+ξ）等价。
_Avoid_: 变形状态

**力态** (force state) T[x,t]⟨ξ⟩: 记录每根键上的力密度的态。
_Avoid_: 力密度

**净力密度** T⟨ξ⟩−T′⟨−ξ⟩: 物质点 x 沿单根键获得的合力密度，即 x 的力态在键 ξ 上的取值与对端 x′ 力态在反向键 −ξ 上的取值之差；对其作体积积分，得到 x 所受的非局部合力密度。
_Avoid_: 力态差, 净非局部力密度, 单端力态

**伸长态** (extension state) e⟨ξ⟩=|Y⟨ξ⟩|−|ξ|: 标量值态，度量键的伸长量。
_Avoid_: 伸长量

**族** F_x / **近场域** H_x: 物质点 x 的近场作用范围内的键集合。二者仅差零测点 x 自身，积分等价、同义使用；各处择一并在首次并用处注明等价性（现状：ch02 键基运动方程用 F_x 以突出族的概念，ch02 态型运动方程及第 6 章起用 H_x）。
_Avoid_: 近场范围, neighborhood

**键基** / **键型** (bond-based): 二体力假设下的近场动力学框架，力态依赖单键变形。同义，各章保留现状用词。
_Avoid_: bond-based PD

**态基** / **态型** (state-based): 力态可依赖整族变形态的推广框架。同义，各章保留现状用词。
_Avoid_: state-based PD

**OSB** (ordinary state-based): 力态沿变形后键方向的态型特例。
_Avoid_: 常规态型（←see OSB）

**NOSB** (non-ordinary state-based): 力态可偏离键方向的一般态型。
_Avoid_: 非常规态型（←see NOSB）

**对力函数** f(η,ξ): 键基理论中单根键上的力密度，量纲 N/m⁶。
_Avoid_: pair force, 力密度

**微模量** c / C(ξ): 表征材料刚度的本构参数。键基中为标量 c（量纲 N/m⁶），态型中为标量 c 或张量 C(ξ)。
_Avoid_: 微弹性常数

**伸长率** s: s=(|ξ+η|−|ξ|)/|ξ|，键的相对伸长量。
_Avoid_: stretch
