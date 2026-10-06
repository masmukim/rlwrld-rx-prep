---
name: market-check-method
description: Fact-check workflow notes for market/statistics docs (A5): what the reference files hide and which checks caught errors
metadata:
  type: feedback
---

Statistics docs: reference summaries often drop rank/order and basis (scope) info that the original page has.

**Why:** In A5 (research/market.md, 2026-10-06) the MOEL reference listed industries without rank, but the original korea.kr page states 순위 순서, so "2위" claims were fine. Conversely, the JARA 2026 forecast (1.22조 엔, +16.7%) was on a 会員+非会員 base (2025 = 1.0456조 엔) while the doc compared it with the 会員-only 9,258억 엔 base.

**How to apply:**
- Always sanity-check growth rates: base x (1+g) should equal the forecast. Mismatch means mixed bases.
- For annual stats (IFR World Robotics), check whether a newer edition exists. IFR WR 2026 came out 2026-09-24, before the A5 doc date.
- Useful: ifr.org press pages, tdb.co.jp, korea.kr, automation-news.jp, robot-digest.com open fine via WebFetch. WebSearch with Japanese query resolved the JARA basis quickly.
- Check persona drift: deliverables must read as RX-team output, not "면접" prep (CLAUDE.md role rule).
