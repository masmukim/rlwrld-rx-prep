---
name: analysis-check-method
description: case/analysis.md 후반부(가정표, 예비 회수 계산) 검증 방법. 식의 누락 변수, 원문 확인 도구 한계
metadata:
  type: feedback
---

가정표의 값은 reference 원문 문장과 1:1로 대조하고, 계산식은 `.venv/bin/python -c`로 다시 돌린다. 산술이 맞아도 식에 빠진 비용 항목이 결론을 바꾼다.

**Why:** 2026-10-09 B2 검증에서 7.5 회수 계산(5.7년)의 산술은 전부 맞았지만, 같은 문서 가정표의 "손 교체 주기 1회/년"이 식에 없었다. 손 2개 교체비를 넣으면 회수가 약 77년, 손 1개면 약 10.6년이 된다.

**How to apply:**
- 계산 표를 보면 식의 변수 목록을 같은 문서의 가정표 행(특히 소모품, 유지보수, 교체 주기)과 대조한다.
- 감가상각 기간(행 280, 5년)과 회수 기간을 비교한다. 결론 문장이 표와 맞는지 본다.
- 가정표의 "출처" 열이 1차 페이지를 가리키는데 가격이 검색 요약에만 있으면 인용 오귀속이다 (Hand-E 가격이 [33] Robotiq 페이지에 없음). reference에 그 리셀러 요약이 저장돼 있는지 확인한다.
- 같은 수치가 `추정` 없이 소스 번호에 붙은 곳을 찾는다 (회로당 8초 = 본 팀 계산인데 [2]에 붙음).
- Q정정 표시 행은 건너뛴다.

**도구 함정:**
- Grep 도구가 없다. `.venv/bin/python .claude/skills/source-read/find.py '패턴' 파일...`을 쓴다.
- find.py는 긴 줄을 잘라서 보여 준다. 문장을 확인하려면 Read로 그 줄 번호를 offset/limit 지정해 전체를 읽는다 (dual-arm 논문 초록의 55%·73%가 이렇게 확인됐다).
- `reference/raw/`에 이미 저장된 원문은 다시 받지 않고 find.py로 검색해도 원문 확인으로 본다. 보고서에는 "기존 raw 저장본 대조"라고 적는다.
- 원문 raw 파일명은 reference 파일 본문의 `raw:` 표기와 다를 수 있다 (예: Cellios는 `case--ams-automated-harness-assembly.txt`). `ls reference/raw/`로 먼저 확인한다.

관련: [[feedback_market-check-method]], [[feedback_hardware-check-method]]
