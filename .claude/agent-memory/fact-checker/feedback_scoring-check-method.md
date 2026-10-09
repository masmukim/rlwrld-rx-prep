---
name: scoring-check-method
description: Checking weighted candidate scores (C1~C7) and zsh/grep pitfalls in local-only fact checks
metadata:
  type: feedback
---

점수표 검증은 (1) 가중합을 직접 재계산하고 (2) 점수 기준 정의와 개별 점수가 맞는지 본다. 가중합은 여러 번 맞았지만, 기준 정의와 점수가 어긋난 곳이 더 자주 나온다.

**Why:** 2026-10-09 candidates.md Q4.3 검증에서 17개 후보 가중합은 모두 맞았다. 반면 5점 기준("RLWRLD 투자자이거나 그룹사")에 맞는 투자자 후보(LG, SK, ANA, 三井化学·島津)가 4점으로 남아 있었고, C5(정부 과제)도 기준과 대조하면 맞지 않는 칸이 있었다.

**How to apply:**
- 가중합은 스크립트 없이 손으로 계산해도 되지만, 항목마다 한 줄씩 적어 확인한다.
- 각 점수 칸을 기준 문장과 하나씩 대조한다. 1~4점에 정의가 없으면 "정의 부재"로 따로 표시한다.
- 가중합이 맞다는 것만으로 "문제 없음"이라고 하지 않는다.

**Pitfalls (로컬 검증 시):**
- zsh에서 `echo "=== 라벨"`은 `==` 때문에 eval 오류가 나고 뒤의 명령이 멈춘다. 구분선에 `===`를 쓰지 않는다.
- `grep -rn --include=*.md`는 zsh에서 "no matches found"가 난다. 디렉터리 인자만 쓰고 `cut`으로 자른다.
- find.py는 `reference/raw/`에 저장된 원문이 있으면 웹을 열지 않고도 원문 대조가 된다. 사용자가 웹 조사를 금지하면 이 방법을 쓴다.
- 원문 줄이 잘려 나올 수 있다 (예: ARR 수치가 같은 줄 뒤쪽). 원문 확인 "완료"는 본문 전체가 보일 때만 쓴다.

관련: [[feedback_competitor-check-method]], [[feedback_market-check-method]]
