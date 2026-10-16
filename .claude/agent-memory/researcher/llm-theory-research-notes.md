---
name: llm-theory-research-notes
description: LLM/트랜스포머 이론 논문(arXiv pdf, transformer-circuits) 일괄 수집과 근거표 작성 때 통한 방법과 함정
metadata:
  type: reference
---

- arXiv `https://arxiv.org/pdf/<id>` 를 fetch.py로 한 턴에 20여 건 병렬 저장해도 모두 OK였다(1,000~4,000줄 텍스트). 초록부터 5줄 안팎이라 `Read offset=1 limit=30`으로 초록을 바로 확인하는 편이 find.py보다 정확하다.
- transformer-circuits.pub HTML도 fetch.py로 저장됨(줄이 길어 find.py가 한 줄을 통째로 보여 줌).
- find.py는 15줄에서 잘린다. 패턴을 좁히거나 Read로 해당 줄 근처만 연다. PDF 텍스트는 단어 붙음/기호 누락이 잦다(Chinchilla "5.5x"가 "55"로 깨짐) → 깨진 수치는 인용하지 않는다.
- 같은 reference 파일(예: papers--pi0.md)을 다른 작업이 동시에 고칠 수 있다. Edit 전에 Read하고, 내 raw 파일명은 `papers--t1-*`처럼 작업 접두어를 붙여 충돌을 피한다.
- 이론 논문은 "표현력(할 수 있나)"과 "학습 가능성(학습으로 찾나)", 손실 법칙과 능력 주장을 섞기 쉽다. 근거표에서 조건/단서 열을 따로 둔다.
- 요약 문장이 본문 태그보다 강해지지 않았는지 쓰기 직전에 대조(A1 교훈).
