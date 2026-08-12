# learnings.md — ch02-sec232-readability

## [2026-08-07] Section 2.3.2 rewrite — engineering decisions

### File anchors (D:\PD-book\chapters\ch02_framework.tex, verified 2026-08-07)
- L493: `\end{figure}` (fig:central-force) — Task 1 inserts transition paragraph AFTER this, BEFORE `\subsection{微弹性材料与成对势}` (L495)
- L497: opening "并非所有对力函数都能从势能导出。" — Task 2 inserts motivation BEFORE this sentence
- L498-501: eq:pairwise-force-potential; L502: definition paragraph (microelastic material) — Tasks 3+4 insert after L502's paragraph (gradient explanation, then table)
- L504-513: objectivity (eq:potential-objectivity L507), exchange symmetry (eq:potential-symmetry L512)
- L514: ONE paragraph covering BOTH "反作用条件自动满足" AND "中心力条件自动满足" — Tasks 5+6 = combined rewrite of this single paragraph
- L516-538: fig:pairwise-potential figure
- L540-545: strain energy density paragraph + eq:strain-energy — Task 8 replaces; MUST preserve \label{eq:strain-energy} (referenced in 2.5)
- Task 7 example inserts between `\end{figure}` (L538) and L540 (strain energy paragraph)

### Mathematical corrections (CRITICAL — plan suggested text was flawed)
1. Task 6: Exchange symmetry alone does NOT imply w depends only on |ξ+η| and |ξ|. Objectivity implies w = w(|ξ|, |η|, ξ·η); exchange symmetry is AUTOMATIC for such invariant potentials. Central force requires restricting to bond-length-only potentials w(η,ξ)=ŵ(|ξ+η|,|ξ|), then f = (∂ŵ/∂|ξ+η|)(ξ+η)/|ξ+η| is manifestly central. The book's claim "微弹性材料的对力自动满足中心力条件" is an overstatement — correct text says it holds for bond-length-dependent potentials (the class bond-based PD uses).
2. Task 7: w = ½c(|ξ|)s² would give f = c·s·(ξ+η)/(|ξ||ξ+η|) — NOT the stated form. Correct potential is w = ½c(|ξ|)s²|ξ| so that ∇_η w = c·s·(ξ+η)/|ξ+η| (standard Silling-Askari PMB form; c units N/m⁶).

### Environment facts
- amsthm IS loaded in preamble.tex (L9) → `\begin{example}[optional title]` works
- booktabs (L13), longtable (L15) loaded; theorem envs L51-55: theorem/definition/lemma/remark/example, numbered [chapter]
- Compile verification (xelatex) done LOCALLY by orchestrator session, NEVER delegated (AGENTS.md rule)
- All referenced labels exist: eq:reaction(139), eq:central-force(144), eq:central-force-form(444), eq:pairwise-force-potential(500), eq:potential-objectivity(507), eq:potential-symmetry(512), eq:strain-energy(543), eq:bond-stretch(75)
- New labels to add (no conflicts with existing 54 labels): eq:reaction-from-symmetry, eq:potential-bond-length, eq:central-force-derivation, eq:linear-potential, eq:linear-force

### AGENTS.md conventions for this task
- Standalone display equations MUST use \begin{equation} + \label{} (never \[ \])
- Tables: booktabs 三线表 (\toprule/\midrule/\bottomrule), no vertical lines; table must be \ref'd in text
- No \[ \], no fabricating citations, every derivation step states its basis
- AI-generated math must be flagged "AI 辅助生成，需经专业审阅" to the user (not in book text)

---

## [2026-08-07] Edit execution completed

All 8 edits applied to `chapters/ch02_framework.tex` in single pass.

### Diff summary

1. **Task 1 (transition)**: Inserted ~4-sentence transition paragraph after `fig:central-force` `\end{figure}` and before `\subsection{微弹性材料与成对势}`.
2. **Task 2 (motivation)**: Replaced opening sentence `并非所有对力函数都能从势能导出。` with 2-paragraph motivation (microelastic material definition + importance) followed by original sentence.
3. **Task 3 (gradient explanation)**: Appended gradient symbol definition + dimensional analysis after `...对力由成对势对相对位移的导数给出。`
4. **Task 4 (comparison table)**: Inserted `tab:classical-peridynamics` (booktabs 3-column table) after Task 3 text.
5. **Task 5 (exchange symmetry → reaction)**: Replaced first sentence of L514 paragraph with explicit derivation (eq:reaction-from-symmetry); kept figure description; deleted final claim about central force (moved to Task 6).
6. **Task 6 (central force argument)**: Added new paragraph after figure description with corrected argument: objectivity → invariants {|ξ|,|η|,ξ·η} → bond-length restriction w=ŵ(|ξ+η|,|ξ|) → chain rule → central force (eq:potential-bond-length, eq:central-force-derivation).
7. **Task 7 (linear example)**: Inserted `example` environment between `fig:pairwise-potential` `\end{figure}` and strain energy paragraph. Used corrected potential w=½c(|ξ|)s²|ξ| (not plan's flawed ½c s²). Label `eq:linear-force` changed to `eq:linear-microelastic-force` to avoid collision with existing label at L638.
8. **Task 8 (strain energy density)**: Replaced paragraph with improved introduction + preserved `\label{eq:strain-energy}`.

### Labels added
- `eq:reaction-from-symmetry`
- `eq:potential-bond-length`
- `eq:central-force-derivation`
- `eq:linear-potential`
- `eq:linear-microelastic-force` (plan suggested `eq:linear-force` but collided with existing label at L638)
- `tab:classical-peridynamics`

### Labels preserved
- `eq:strain-energy` (referenced in section 2.5)

### Anchor mismatches resolved
- None; all anchors matched exactly using text search.
