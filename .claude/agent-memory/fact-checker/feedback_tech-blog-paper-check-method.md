---
name: tech-blog-paper-check-method
description: Checking a company tech blog against its arXiv report (RLDX-1 case) - integer test on percentages, appendix location, find.py output cap, precision differences
metadata:
  type: feedback
---

RLDX-1 tech blog vs tech report check (2026-10-09). Method notes:

- **Integer test for percentages.** When a success rate is given as a % with n trials, check that k/n gives it. RLDX-1 Egg Pick-and-Place 61.1% is not an integer count over the stated 24 trials (14/24=58.3, 15/24=62.5). It fits 44/72 only, while the appendix says 3 positions x 8 trials. Found a source-internal contradiction this way. Run it on every table row where n is stated.
- **Trial counts and demo counts live in the appendix.** In the raw tech report, the per-task protocol is in the appendix G sections (G.3 ALLEX, G.4 FR3), near the end of the file (about line 3380 onward). The main text only gives the summary. Search for "trials", "demonstrations" and "Training Demonstrations" there.
- **find.py caps output at about 20 lines per file** and prints "N more". Use narrow patterns (a few task names or one term at a time), or Read with offset around the line numbers it returns.
- **Precision differs between sources.** The blog's latency table gives 2 decimals (43.70, 41.59, 71.22). The paper gives 1 decimal (43.7, 41.6, 71.2). Cite the blog for the 2-decimal values.
- **Wilson CI.** Compute inline with `.venv/bin/python -c` (z=1.96). 8/24 gives 18.0 to 53.3. 5/24 gives 9.2 to 40.5.
- **Raw copies already exist.** The reference/raw text files saved by the researcher are verbatim fetch output, so grepping them avoids summarizer error. Re-fetching is only needed if the raw file is missing or looks truncated.
- **Blog vs paper wording.** The blog's prose ("below 30%, nearly 90%") can contradict its own table. Check the table first and treat the prose as a summary.

**Why:** A11 check. The Egg 61.1 and "frozen weights" errors were missed by the reference summary and were only found in raw text.
**How to apply:** For any paper or blog with percentages, run the integer test and the appendix search before marking a table row as matching.

See also [[feedback_paper-check-method]].
