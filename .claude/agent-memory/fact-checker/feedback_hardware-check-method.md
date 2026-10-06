---
name: hardware-check-method
description: A4 hardware.md fact-check notes: which pages open, which reference summaries drift from original
metadata:
  type: feedback
---

Hardware docs: product pages (sharpa.com, inspire-robots.store, robotiq.com Hand-E, humanoid.guide, calcalistech, sbbit.jp, wetalktesla) all opened fine via WebFetch; values matched reference.

**Why:** In A4 (2026-10-06) numbers were accurate, but errors were in attribution: a spec (Tesla 25 actuators, finger 4 + wrist 2 DoF) was cited to a source that does not contain it (the Tech Times article is the source of 25 actuators). Reseller price ranges quoted from one WebSearch missed other resellers (Inspire RH56DFX also $9,250 and $10,500).

**How to apply:**
- Check each citation number [n] actually contains the spec next to it, not just that the number exists somewhere in reference/.
- Check whether a newer article (competitors--*) in reference/ contradicts the hardware doc's "unconfirmed" claim.
- Re-run one WebSearch on price conflicts; reseller ranges drift.
- Per CLAUDE.md role rule, flag "면접에서" sections as persona drift.
