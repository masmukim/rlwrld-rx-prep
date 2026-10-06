---
name: sources-and-access
description: case-analyst가 공정 근거를 찾을 때 통한 소스·검색어와 막힌 사이트, 권한 문제(B1 2026-10-06 기준)
metadata:
  type: reference
---

**막힌 것과 우회**
- 2026-10-06 B1 세션에서 Bash 실행 권한이 거부되어 source-read(fetch.py)를 못 썼다. mkdir 없이 단일 명령으로 다시 해도 거부. 대신 WebFetch로 초록·원문 인용을 받고, 산출물 "확인하지 못한 항목"에 "WebFetch 요약 인용이라 fact-check 원문 대조 필요"라고 적었다.
- MDPI(mdpi.com) 논문 페이지는 WebFetch 403. 같은 논문의 초록은 저자 소속 기관 저장소(예: research.chalmers.se/en/publication/<id>)에서 열린다.
- ScienceDirect는 403(A5 기록과 동일).

**잘 통한 검색어·소스**
- "wire harness assembly collaborative robots literature review manual labor percentage" → Navas-Reascos 2022(수작업 90%) 바로 나옴.
- arXiv API `all:"wire harness" AND all:robot`, sortBy=submittedDate → 하네스·DLO·커넥터 논문 10건 목록. 목록 1회 호출로 연구 동향 근거 확보.
- 한국어 "와이어링 하네스 수작업 ... 경신 유라코퍼레이션" → 디일렉 2022 기사(3사 중국 생산, 점유율).
- 물류 피킹 경쟁 근거: aboutamazon.com Vulcan 발표(약 75% 품목 유형, 흡착·패들 + 힘센서).

**쓸모없던 것**
- "FPC connector insertion manual assembly" 영어 검색은 커넥터 제조사 가이드만 나옴. 전자 조립 인력·자동화율 근거는 다른 검색어 필요.

관련: [[b1-scoring-practice]]
