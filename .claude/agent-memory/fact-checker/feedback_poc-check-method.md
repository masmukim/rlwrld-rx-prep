---
name: poc-check-method
description: PoC/deployment case doc check - generic-price misattribution, "within N months" upper bounds, quoted phrases, search-summary-only items with no reference file
metadata:
  type: feedback
---

PoC·배포 사례 문서(research/poc-playbook.md 류)를 검증할 때 쓴 방법과 잡힌 패턴.

- **업계 일반 가격을 특정 고객 가격으로 붙이는 오류가 잡혔다.** 교촌 기사(daum 2023)의 "조리 로봇 단가 약 2,000만 원, 설치 포함 4,000만 원"은 "A 로봇 제조사 판매 단가"이지 교촌 구매가가 아니었다. **Why:** 기사에서 가격 문장의 주어(제조사, 가맹점, 업계)를 놓치기 쉽다. **How to apply:** 금액을 특정 회사에 붙일 때 원문에서 주어가 그 회사인지 확인한다. "A 제조사", "업계 관계자" 같은 표현이 보이면 오류 후보로 본다.
- **"N개월 내" 표현은 상한이다.** Figure 원문은 "Within 6 months ... began testing", "Within 10 months ... full deployment"라고만 썼다. 두 구간의 차이(약 4개월)는 최대값이므로 "약 4개월"로 단정하지 않고 "최대" 또는 "상한"으로 쓴다.
- **인용 부호 안의 문구는 원문 문자열로 확인한다.** 교촌 "아직 테스트 기간"은 원문 "아직 테스트 기간이기 때문에"로 일치했다. 그러나 Telexistence "100% 성립"은 [10][12] raw 어디에도 없었다. **How to apply:** find.py로 따옴표 안 핵심 단어를 검색하고, 없으면 확인불가로 적는다.
- **검색 요약에서만 온 수치는 reference에 근거 파일이 없는 경우가 많다.** Figure 소송, K-Scale 청산은 reference/에 파일이 없었다(누락). Agility 월 8,500달러는 reference 메모(case--poc-robotreport-digit-cost.md)에만 있었다. 이 항목은 본문에 수치를 두지 말고 확인필요로 둔다.
- **쓸모 있던 방법:** `grep -rn ... reference/`는 파일명·요약 메모 확인에 빠르다. `find.py '키워드' reference/raw/xxx.txt`는 원문 줄 번호를 준다. 원문 날짜는 기사 발행일과 실제 사건일이 다를 수 있다(CJ 용인 "2026-09-03"은 기사일).

**Why:** 2026-10-09 PoC 문서 검증에서 가격 귀속 오류와 상한 표현 문제를 찾았다.
**How to apply:** 사례 수치를 검증할 때 주어, 상한/하한, 따옴표 문구, reference 파일 존재 여부 네 가지를 같이 확인한다. 관련: [[feedback_market-check-method]], [[feedback_competitor-check-method]].
