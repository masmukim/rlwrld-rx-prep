---
name: data-pipeline-research-notes
description: Skild/PI 데이터 파이프라인 비교(T2) 조사에서 잘 열린 소스, 막힌 곳, 내가 했던 실수
metadata:
  type: reference
---

- 잘 열린 1차: skild.ai/blogs/* (building-the-general-purpose-robotic-brain, s1, physical-self-play, skild-crosses-100m-arr), www.pi.website/blog/pistar06 (www 붙이면 열림), arxiv.org/html/<id>, NVIDIA customer story (nvidia.com/en-eu/case-studies/skild-ai/). fetch.py로 모두 OK.
- Skild 데이터 철학의 1차 근거는 2025-07-29 글(시뮬+인터넷 영상 선언, "<1% 실로봇" 비판)과 S1 블로그 "The Data Engine" 절. 출처별 비율은 어디에도 없음.
- PI 논문은 본문에 시간 수치가 숨어 있다. π0 "about 10,000 hours"를 첫 Grep 패턴에서 놓치고 "시간 수치 없음"이라고 썼다가 동시 작업(T1)이 저장한 raw에서 발견해 고침. 교훈: 논문에서 "없음"을 쓰기 전에 `hours` 패턴으로 결론부·소개부까지 Grep하고, 같은 논문의 다른 raw 파일(papers--t1-*)이 있는지 ls로 확인.
- 부정 확인("시뮬레이션 데이터 서술 없음")은 `grep -c simulat`로 하고 "찾지 못함"으로만 쓴다.
- π*0.6 부록 "600"은 본문(autonomous)과 부록(demonstrations)이 달라 확정 불가. 논문 내부 불일치는 둘 다 적는다.
- Grep 도구는 이 환경에서 없을 수 있다. Bash grep과 find.py 사용.
