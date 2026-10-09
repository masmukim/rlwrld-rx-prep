---
name: harness-check-method
description: Harness/case doc check pitfalls (arXiv version drift, datacenter-vs-harness board, source-number reuse, summary-cut lines, paper arithmetic) and sources that open
metadata:
  type: feedback
---

검증 규칙: arXiv 수치는 reference 초록(v1)만 믿지 말고 source-read로 최신 버전(vN 표기)을 열어 확인한다.

**Why:** B2 검증(2026-10-09)에서 Industrial Dexterity Benchmark 수치가 v1 초록 78%였지만 v3 원문은 76%였다. 또 36%·48회는 자동차 하네스 보드가 아니라 데이터센터 케이블 보드(Board #1) 결과였다. reference의 "구성당 48회"가 WebFetch 요약 기준이었던 것이 단서였다.

**How to apply:**
- reference 메모에 "초록 기준", "WebFetch 요약 기준"이 있으면 원문(raw)으로 버전과 과제(보드)를 먼저 확인한다.
- 논문 수치를 쓸 때 원문의 과제 이름(예: Board #1 vs #2)을 그대로 대조한다. 분야 이름(하네스)이 붙어 있어도 실험 대상이 다를 수 있다.
- source-read find.py는 한 줄을 약 300자에서 잘라 보여 준다. 매칭 어구가 잘린 뒤쪽에 있으면 Read(offset, limit 1~2)로 줄 전체를 확인한다 (Next2OEM, "has been increased" 확인 때 필요했다).
- case/analysis.md 출처 목록에 번호가 중복된 적이 있다 (40이 두 번). 본문 인용 번호를 목록과 한 줄씩 맞춘다.
- 논문 내부 산술도 확인한다. 참고 라인 논문은 "440/5.24 = 95"라고 썼지만 실제로는 약 84다 (95는 효율 85% 식에서 역산된 값).
- 공장 사례의 "해소했다"처럼 개선 효과를 과장하는 표현은 개선 후 최대 사이클과 택트를 나란히 놓고 대조한다 (5.24분 > 5.18분).
- 원문에 없는 "1위권" 같은 시장 지위 서술은 근거 없음으로 본다.

관련: [[feedback_paper-check-method]], [[feedback_market-check-method]]

**열린 확인점:** 住友 "자동화율 15%·50%" 분모는 원문에 없다. 국내 하네스사 라인 수치는 공개 1차 소스가 없다.
