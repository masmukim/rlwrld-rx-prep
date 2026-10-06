---
name: rlwrld-research-notes
description: RLWRLD 조사에서 잘 통한 소스/검색어, 막힌 사이트, 소스 충돌 패턴
metadata:
  type: reference
---

- WebSearch 한 번에 요약+URL이 나오므로, 여러 언어 검색(한/영/일)을 병렬로 던진 뒤 핵심만 WebFetch.
- 1차 소스: PR Newswire(시드1 보도자료), arXiv 2605.03269, github.com/RLWRLD/RLDX-1, rlwrld.ai/en/rldx-1, AWS physical-ai 블로그.
- 일본어 소스가 풍부: KDDI MUGENLABO, Impress AI Watch, THE BRIDGE, 日経. 검색어 "RLWRLD KDDI ローソン".
- 막힘: platum.kr, thebridge 일부는 403. koreatimes.com은 DNS 실패. 대체로 벤처스퀘어/besuccess 사용.
- 주의: 2차 기사(R&D World, 데모데이, nate 요약)는 수치 오류가 있음(시드1 $21M 오기, "NVIDIA-backed", 파트너 BMW/Honda 단독 등장). 1차와 대조 필수.
- 기술 주제(A2): arxiv.org/abs/<id> 초록 페이지는 가볍고 안정적(저자, 날짜, 핵심 주장 확보). 논문 수치는 초록에 없는 경우가 많아 "수치 미확인"으로 적는다. OpenAlex filter 쿼리 1회로 대표 논문+인용 수 확보(인용 수는 arXiv/학회판 분리 집계라 낮게 나옴). arxiv.org/html/<id>는 서베이의 도전과제 인용에 유용.
- WebSearch 결과에 alphaxiv.org, 2차 요약이 섞임. 논문은 arXiv abs로 직접 확인. 일본어 "模倣学習 VLA", 한국어 "로봇 파운데이션 모델 텔레오퍼레이션" 검색이 xTECH, 디일렉으로 연결됨.
- 기사(디일렉 등)의 수치(하루 50~200 시연, 1만 시간 등)는 기사 인용이라 1차 확인 전 `추정`급. 서베이 비교표는 WebFetch 요약이 만든 것일 수 있어 원문과 차이 가능.
- WebFetch 요약 모델이 날짜를 기사 게시일과 이벤트일로 섞어 보고하는 경우가 있음. 공개일은 GitHub/arXiv로 교차 확인.
