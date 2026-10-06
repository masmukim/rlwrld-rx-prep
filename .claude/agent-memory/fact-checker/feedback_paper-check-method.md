---
name: paper-check-method
description: How to verify arXiv-abstract numbers (relative vs percentage points) and pitfalls of WebFetch summaries on papers
metadata:
  type: feedback
---

arxiv.org/abs/<id> opens fine and gives abstract text cheaply; use it for the 5 mandatory original checks on papers.

**Why:** WebFetch summarizes with a small model. For "N% improvement" it will assert relative or %p without basis. In A6 the same ForceVLA 23.2% got "percentage points" from the abs page and "relative" from the PDF fetch. Large PDFs (>10MB, e.g. EgoScale) fail with maxContentLength.

**How to apply:** Never accept a summarizer's relative/%p verdict; keep as 확인필요 unless the table values (baseline and method averages) are read. Also grep reference/ for the primary source (e.g. competitors--nvidia-*) before claiming "1차 소스 미확인" in a research doc. Check arXiv version dates (v2/v3 revisions can change numbers).

See [[market-check-method]] for market docs.
