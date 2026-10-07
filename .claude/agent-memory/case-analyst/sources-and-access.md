---
name: sources-and-access
description: case-analyst가 공정 근거를 찾을 때 통한 소스·검색어, 막힌 사이트, 권한·도구 문제 (B1 2026-10-06, B2 2026-10-07 기준)
metadata:
  type: reference
---

**도구·권한 (B2 2026-10-07 갱신)**
- B2 세션에서는 Bash가 허용돼 find.py(`.venv/bin/python .claude/skills/source-read/find.py '패턴' 파일들`)가 잘 돌았다. B1에서 Bash가 거부됐던 것과 달라졌다.
- Grep 도구가 세션에 없을 수 있다. 그럴 때는 Bash `grep -n -E '패턴' 파일`로 대신한다(한 번에 거부 없이 통함).
- **case/*.md를 Write하면 하네스가 "서브에이전트는 보고서 파일을 쓰지 말라"며 거부했다(B2).** 우회(Bash heredoc 등)하지 말고, 문서 전문을 최종 응답에 담고 메인에게 저장을 요청한다. 작성 전에 이 거부를 예상하고 처음부터 반환 텍스트로 쓰면 Write 한 번을 아낀다.
- 시작할 때 `ls reference/raw/`와 git status의 untracked reference를 먼저 본다. B2에서는 앞선 중단 시도가 reference 24건과 원문을 이미 저장해 두어 웹을 거의 열지 않고 끝냈다.

**막힌 사이트와 우회**
- MDPI(mdpi.com) 논문 페이지는 WebFetch 403. 같은 논문의 초록은 저자 소속 기관 저장소(예: research.chalmers.se/en/publication/<id>)에서 열린다.
- ScienceDirect는 403. Journal of Manufacturing Systems 논문은 Tampere 저장소(researchportal.tuni.fi)에서 초록이 열렸다.
- 日刊自動車新聞(netdenjd.com)은 앞부분만 무료.

**잘 통한 검색어·소스**
- "wire harness assembly collaborative robots literature review manual labor percentage" → Navas-Reascos 2022(수작업 90%).
- arXiv API `all:"wire harness" AND all:robot`, sortBy=submittedDate → 하네스·DLO·커넥터 논문 목록.
- 하네스 라인 인원·택트의 공개 수치: EasyChair 프리프린트 10031(모로코 엔진 하네스 라인, 32개 작업장, 택트 5.18분, SMH 2.16시간)이 거의 유일하다.
- 국내 하네스 현장: 서울경제 경림테크 경산공장 기사(2025-07, 다음 뉴스 게재). 업계 자동화율: 住友グループ広報委員会 페이지(약 15%, 모델 라인 약 50%).
- 하네스 자동화 경쟁 해법 최신: Automotive Manufacturing Solutions 2026-09 Cellios/TE 기사(배선·단자 삽입이 가장 어렵다, 시제품은 사람보다 느림).
- 한국어 "경신 와이어링 하네스 국내 공장" 검색은 해외 JV 기사만 나오고 국내 사업장 역할은 안 나왔다.

**쓸모없던 것**
- "FPC connector insertion manual assembly" 영어 검색은 커넥터 제조사 가이드만 나옴.

관련: [[b1-scoring-practice]], [[citation-precision]]
