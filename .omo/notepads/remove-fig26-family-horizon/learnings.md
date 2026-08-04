# Learnings — remove-fig26-family-horizon

Conventions, patterns, and successful approaches discovered during work on this plan.

_Auto-scaffolded by /start-work. Append new entries below - never overwrite._

---

## 2026-08-04：图2.6（fig:family-horizon）删除完成

- **删除范围**：`chapters/ch02_framework.tex` 原 238 行段落 + 240–270 行 figure 环境，合并为单段正文（现 238 行）。`fig:family-horizon` 全库零残留（含 main.aux）。
- **正文改写**：以「物质点、键与近场域的几何关系已在第 1 章图\ref{fig:horizon-bond}中给出」承接图1.4，点明「族 $\mathcal{F}_{\mathbf{x}}$ 即为近场域 $H_{\mathbf{x}}$ 内与 $\mathbf{x}$ 通过键相连的物质点集合」（与 194 行 eq:family 口径一致），再以「如图\ref{fig:boundary-truncation}所示」衔接表面效应。
- **图号前移结果**：删除后第 2 章图序为 2.1–2.10 连续。`fig:bond-decomp`→2.6、`fig:force-stretch`→2.9、`fig:boundary-force-conversion`→2.10（各前移一位）。注意：**任务书预期 "fig:force-stretch 变为 2.6" 与实际不符**——bond-decomp（2.6）与 force-stretch 之间还隔着 pairwise-potential（2.7）、state-concept（2.8）两图，故 force-stretch 实为 2.9。前移逻辑正确，仅预期编号过时。
- **编译验证**：xelatex 两遍（main.tex 目录）后，日志 `Error|undefined|Warning: Reference` 零命中；aux 无 fig:family-horizon。日志存 `.omo/evidence/task-1-remove-fig26-family-horizon.log`。
- **检查点**：删除 figure 后须核对 aux 中 `\newlabel{fig:...}` 全部编号连续无跳号，且 `\ref{fig:...}` 引用仍有效（无 undefined）。

## 2026-08-04：F2 审查修复 — 238 行冗余删除

- **问题**：原 238 行末句「对于物体边界附近的物质点…这一现象称为表面效应」与 194 行正文及 fig:boundary-truncation 图注三处几乎原样重复；表面效应已在 194 行详述并引用图2.5，238 行重复属画蛇添足。
- **修复**（仅 238 行整段，三处修改）：①「第 1 章图\ref」→「第 1 章 图\ref」（补空格防粘连）；②末句整句删除；③「物质点集合」→「物质点集合（不含 $\mathbf{x}$ 自身）」（与 eq:family 中 $\mathbf{x}'\neq\mathbf{x}$ 口径严格一致）。
- **经验**：承接上文/引用图的过渡句若与前文（同节或相邻段）内容重叠，须检查是否已在前文详述并引用过该图——重复引用+重复解释 = 冗余。改写时优先「几何关系引用图1.4 + 族定义」的单一职责，删去已述结论。
- **验证**：两遍 xelatex exit=0；main.log 过滤 `Error|undefined|Warning: Reference` 仅命中 `infwarerr` 宏包描述行（含单词 "error" 但为宏包说明文本，非 LaTeX 错误，属良性误报）；aux 无 fig:family-horizon，boundary-truncation=2.5、bond-decomp=2.6 连续。

## 2026-08-04 (��֤ session ׷��)��Final Wave ȫ�� APPROVE
- F1 �ƻ��Ϲ���ƣ�ses_03569acac����Must have 4/4 + Must NOT 5/5 ȫ PASS��2 ������� observation��fig:horizon-bond ʵΪͼ1.3��fig:force-stretch ʵ�� 2.9 ���мƻ�����ͼ2.4 �±�ź��ƣ�
- F2 ����������飨ses_035699abe����238 �����ͨ����2 ����ѡ��ɫ��238 ���� 194 �б���ЧӦ����������ࣻ�ɼӰ���ν�ͼ2.4�������������
- F3 ��ʵ�ֶ� QA��ses_035698ab2����PyMuPDF ��ҳ��֤ͼ2.4/2.5/2.6 ��Ⱦ������ͼ2.5 �·��޲�����ͼ��������log ��ȷ������ undefined/Error/Reference
- F4 ��Χ���棨ses_035697cda������ ch02_framework.tex һ��Դ�ļ��Ķ�����������ȫ���������� commit
- ��ѵ��reviewer ��� VERDICT ʱ������ʽ���ţ��� ?/�Ӵ֣��ᵼ�� boulder ��ͣ hook �޷�ʶ�𣬺���ӦҪ��������ı� 'VERDICT: APPROVE'
