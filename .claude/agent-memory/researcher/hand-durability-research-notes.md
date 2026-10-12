---
name: hand-durability-research-notes
description: 다관절 손 수명·유지보수(Q7) 조사에서 통한 소스, 막힌 곳, 검색어, 실수
metadata:
  type: reference
---

- 잘 열린 소스: 第一财经 yicai.com 기사(일부만 저장, 영문 재게재 itiger.com/news/1123099345가 더 김), 36kr.com 영문판(eu.36kr.com), Honda global.honda 다지 핸드 페이지(일본어, 45만 회), unitree.com/Dex2-5, dexterous-hand.readthedocs.io(Shadow 정비 문서), arXiv html/pdf(2511.07797, 2608.24242, 2608.28578, 2504.04259v2), blog.robotiq.com 지식베이스, shadowrobot.com/how-much-does-a-robot-hand-cost/.
- 막힘: robotomated.com 410, grabarobot.com 본문은 fetch.py가 308(WebFetch는 열림), roboticscenter.ai 수리 페이지에 가격 없음(검색 요약의 "$800부터"는 거짓 단서), XELA newequipment 기사에는 "커버 교체" 문장이 없었음(검색 요약과 불일치, 인용 금지).
- 잘 통한 검색어: "dexterous hand durability lifetime cycles tendon failure field MTBF", "humanoid dexterous hands break after 50 uses", "Shadow Dexterous Hand tendon replacement maintenance". 한국어·일본어 검색은 현장 수치가 거의 안 나옴(일본어는 Honda만).
- 패턴: 공개 수명 수치는 모두 제조사 자체 시험 또는 고객 진술이고 사이클 정의가 서로 다르다. 단일 논문 안에서도 정의가 어긋난다(ORCA 10,000회=20시간 대 2,250회=2.5시간). 검색 요약이 만든 수치(가격, 커버 교체)는 원문에서 안 나올 수 있으니 fetch.py + find.py로 대조한다.
- 중간 조정: 코디네이터가 중간에 "추가 검색 중단, 바로 작성"을 지시하면 그때까지의 reference 저장분을 정리하고 한 번의 Write로 쓴다.
