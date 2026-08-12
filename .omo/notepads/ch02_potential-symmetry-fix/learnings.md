# Learnings — ch02_potential-symmetry-fix

Conventions, patterns, and successful approaches discovered during work on this plan.

_Auto-scaffolded by /start-work. Append new entries below - never overwrite._

---
## [2026-08-07] �ƻ���ʽ����������
- /start-work �� boulder �������޷�ʶ�����б���ʽ�� checkbox��'1. [ ]' / 'F1. [ ]'������ʹ�����侯��Ҫ������+��+�ո��Ա� 'no valid task rows'������ Progress ��ʾ 0/0��
- ���ۣ�Progress ���������󱨣�������ֵ�Լƻ��ļ�ʵ�� checkbox ״̬Ϊ׼��grep '^[12F][12]?\. \[.\]' ��֤����
- �����޸�1+�޸�2 ���ɵ��Ӵ�����category=writing��һ��ί����ɣ�������λ��ͬһ�ļ��������򣬱����ļ���ͻ����֤ͨ����xelatex��3+bibtex �� error���� undefined��main.pdf 157ҳ��
- ch02_framework.tex 2.3.2 �����Ѻ������Ƶ������͹��ԡ���ת������(I1,I2,I3)��w=w^(I1,I2,I3)�������Գ��Բ����ԡ�|��+��|=sqrt(I1^2+2I3+I2^2)����ʽ�����м䲽���f��(��+��)�������������Զ������ͼ2.9��

## [2026-08-07 22:30] �޸� 3���������������ͶΣ����
- �û�����㣺Ϊʲô������������ ?_��w �� (��+��)��Ϊʲôǡ��������ת��������
- �޸� 3 �ڵ� 549 �� \] ����� 3 �н��ͶΣ�551 �У������� 6 ����?3 ��ת���ɶ�=3 ���������������ȼ۲������� |��+��|,|��?��|,�Ρ���
- ��֤������ Read ͨ����551 ����ƻ� newString ����һ�£�\[/\] �ɶԣ���git diff +20/?7 �� 3 �о���������
- ���룺xelatex��3 + bibtex ȫ�� exit 0���� error���� undefined reference/citation
- �ƻ��ļ� 5/5 ��ѡ�� [x]��boulder.json status=completed��ended_at=2026-08-07T22:30:00Z��
- ί�У�ses_0236b248cffeq0o397LiqCspx4��writing ���kimi-k2.6������ edit �ɹ�����������
- ��ѵ���û�����ѧֱ����Ϊ������ĳ���죩����������Ӧд�����Ķ��ǽ��Ի����ͣ�prometheus ֻ�ܱ༭ .omo/*.md�������޸�һ�ɾ� /start-work �ƻ�ִ��

## [2026-08-07 23:00] 格式实验结论：计划解析器缺陷确证
- 实验：将计划文件 5 个复选框从编号格式（`1. [x]` / `F1. [x]`）改为破折号格式（`- [x]`），plan-format-warning 依旧报 'no valid task rows'；随后恢复编号格式，警告依旧触发。
- 结论：两种格式均被解析器拒绝 → 缺陷在 boulder/plan 解析器侧，与计划文件格式无关。计划文件已恢复为解析器文档要求的编号格式（`1. ` / `F1. `），并保持 5/5 `[x]` 完成态。
- boulder continuation 误触循环无法通过调整计划文件格式修复；需在 oh-my-openagent 钩子层修复完成判定逻辑。
