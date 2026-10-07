---
name: paper-deep-read-notes
description: 회사 블로그와 arXiv 논문을 대조해 읽는 법(arxiv html 저장, find.py 패턴, 부록 위치, 렌더링 깨짐 주의)
metadata:
  type: reference
---

- 회사 블로그(요약판)는 시행 수, 시연 수, 점수 방식이 없다. arXiv HTML(`https://arxiv.org/html/<id>`)을 source-read로 저장하면 부록(G.x Experimental Details)에 모두 있다 (RLDX-1 A11: 4,100줄, find.py 4~5회로 충분).
- 잘 통한 find.py 패턴: `trials|per task|episodes`, `Evaluation Protocol`, `Training Demonstrations`, `limitation|Conclusion`. 결과가 "... N more"로 잘리면 offset으로 Read.
- arXiv HTML 텍스트는 숫자가 중복 렌더링된다(195195 hours = 195시간, 7272K = 72K, 55:55 = 5:5). 문맥으로 읽고 `추정`으로 표시한다.
- 블로그 서술문과 같은 블로그의 표가 어긋나는 경우가 있다(RLDX-1: "기준선 30% 미만" vs 표 평균 39.1, 44.8). 표와 논문 결론을 기준으로 삼고 서술문은 별도 표기한다.
- 평균 열에 성공률과 진행 점수(progress score)가 섞일 수 있다. 평가 프로토콜 절에서 지표 정의를 확인한다.
- 회사 모듈 근거 논문(MoSS, HAMLET)은 RLWRLD 소속 저자가 병기되어 독립 검증이 아니다. 저자 소속은 HTML 첫 60줄에 있다.
- 작은 시행 수(24회)의 성공률 비교는 Wilson 구간을 손계산해 겹침 여부를 본다.
