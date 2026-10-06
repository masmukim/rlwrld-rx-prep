---
name: competitor-check-method
description: Method notes for checking research/competitors.md style docs (funding, vendor blogs, Korean news)
metadata:
  type: feedback
---

Vendor blogs (HF GR00T, figure.ai, deepmind.google blog, Yahoo/BusinessWire) open fine via WebFetch. nate.com summaries are garbled (swap company names); etnews opens fine and answers budget-scope questions well.

**Why:** reference notes written from summarizer output hide cherry-picking. A3 check found DeepMind "36%" (screw bulb) quoted while same blog lists unscrew bulb 92%; etnews 497억 is whole LG consortium, not KT alone.

**How to apply:** for success-rate numbers, ask the fetch for ALL listed rates on the same task family; for budget figures ask which project each number belongs to. For funding "conflicts", sum known rounds (PI 70M+400M+600M=1.07B; +1.05B Series C=2.12B) before calling it a conflict.
