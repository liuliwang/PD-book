# Issues â€” ch02-format-optimize

Problems and gotchas encountered during work on this plan.

_Auto-scaffolded by /start-work. Append new entries below - never overwrite._

---

## [2026-08-03] Blocker: F2 line-count criterion mismatch
- ch02_framework.tex final line count: 828 (criterion requires 880-920)
- Root cause: T3 (merge 5 short paragraphs, -10) and T4 (dissolve 5 remarks into prose, -20) are compression operations; T1(+2)/T2(+0)/T5(+2) net = 828
- Formula (48 equation) + theorem (3) + TikZ (8) counts UNCHANGED - that half of F2 passes
- Plan criterion was estimated as 854+increments during planning; actual optimization compressed, not expanded
- Options presented to user: (a) adjust F2 range to ~810-870 [recommended], (b) pad content to hit 880 [not recommended]
- Status: F2 marked [~] blocked, awaiting user decision; all other tasks (T1-T5, F1, F3, F4) complete
- Worktree note: index has stale staged entries (early subagent git add with version-A intro); deliverable is worktree state, per AGENTS.md no auto-commit

## [2026-08-03] F2 ¾öÒé£ºĞĞÊı±ê×¼µ÷Õû
- ¾ö²ß£º²ÉÄÉ·½°¸(a)£¬ĞĞÊı±ê×¼ 880-920 ¡ú 800-870£¨Êµ¼Ê828ĞĞ£©
- ÒÀ¾İ£ºT3/T4 ÎªÑ¹ËõĞÔ²Ù×÷£¨ºÏ²¢¶Ì¶Î -10¡¢remarkÈÚÈëÕıÎÄ -20£©£¬ĞĞÊı¾»½µ26ĞĞÊÇ¸ñÊ½ÓÅ»¯µÄºÏÀí½á¹û£»¹«Ê½48+¶¨Àí3+²åÍ¼8×ÜÊıÈ«²¿Î´±ä
- ¼Æ»®ÎÄ¼ş F2 ÒÑ±ê¼Ç [x] ²¢×¢Ã÷µ÷ÕûÀíÓÉ
