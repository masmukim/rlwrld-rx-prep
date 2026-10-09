---
name: cases-check-method
description: Checking overseas customer-case docs (research/rx-cases.md type) against reference/raw without web access. Plan-vs-achieved, unsaved cited URLs, search-summary numbers
metadata:
  type: feedback
---

Check order that worked (2026-10-09, rx-cases.md, no web access allowed):
1. Map each citation number to its raw file by grepping `^URL:` across `reference/raw/rxcase--*.txt` and `competitors--*.txt`. Match the exact URL first, then read the lines. Some cited URLs have no raw or reference file at all.
2. Grep the raw with find.py for the number plus its unit (for example `84|37 seconds`, `98%`, `300店舗`). Read only the matching lines.
3. Cross-check the summary files (research/skild-pi-deep-dive.md, research/poc-playbook.md) for the same number. Their notes on what was unverified are usually right.

Recurring pitfalls:
- **Plan read as achieved.** The FamilyMart 2022 release says "今後300店舗へ拡大" (will expand to 300 stores), a plan. Docs write "300개 매장" as a result. Compare the verb tense in the Japanese original.
- **Search-summary numbers that stay in the table.** A number flagged "미확인" in one file (for example Ultra 96.4%) often still appears in the table. Recommend deleting it, not just flagging it.
- **Conditions dropped.** Weave "개입 50% 감소" holds only when the model is trained on Weave-specific data (raw humanoidsdaily line 29). Summaries drop that condition.
- **Company claims tagged as press.** Skild's ARR and 60-customer numbers are company claims (securitiesio raw line 12 says "company blog post"). Tag them "회사 주장", not "기사".
- **Cited URLs with no saved file.** Several cited articles (theaiinsider 2026/06/26 and 2026/09/22, startupfortune, roboticsandautomationnews 2026/09/18, the Dexterity Hagerstown post, and the PI blog) have no reference/ or raw/ file. Report them as 누락 (unsaved source).
- **Specific facts with no trace.** Details like "필리핀 원격 조작자", "Tracy 시험 현장", and "Sanctuary 21-DoF" appear in no saved file. Mark them 확인불가.
- **Team proposals stated as company facts.** "14주 PoC" comes from case/b4-proposal.md, not from RLWRLD's public pages (KDDI PoC was 3개월).

**Why:** A customer deliverable with an unsourced or plan-as-achieved number is the main risk. Web access was excluded in this run, so the raw/ files and reference/ notes were the only evidence.
**How to apply:** Run the three-step check above before any web fetch. Whenever a number is "기사" or "검색 요약", look for the original-language PR in raw/ first.

Related: [[feedback_market-check-method]], [[feedback_competitor-check-method]]
