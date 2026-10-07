---
name: poc-research-notes
description: PoC/배포 사례(A10) 조사에서 잘 열린 소스, 막힌 사이트, 반복된 실수
metadata:
  type: reference
---

- 잘 열린 raw: agilityrobotics.com/content/(GXO 보도자료, investors.gxo.com은 타임아웃), family.co.jp news_releases(일본어 1차), tx-inc.com/?p=ID, therobotreport.com, hyundaimotorgroup.com/en/story, blogs.nvidia.com, thebridge.jp, byline.network, economist.co.kr, newdaily, v.daum.net, aol.com(Reuters 재게재).
- 막힘: axios, techspot, supermarketperimeter, automation.com은 403. pi.website/blog/partner는 429. monoist.itmedia.co.jp는 Shift-JIS가 깨져 읽을 수 없음(대신 thebridge.jp 사용). mujinspire URL은 검색 결과 URL이 404.
- 검색 요약(WebSearch)은 가격·소송·감원 같은 주장을 섞어 준다(예: Agility 월 8,500달러, usagepricing/ai2.work 계열). 원문을 열지 못하면 본문에 쓰지 말고 `확인필요` 목록으로 보낸다.
- 실수 방지: 1차 보도자료도 KPI를 "목표"로만 적는 경우가 있다(Figure-BMW). 기존 문서의 "달성"이 원문에 있는지 find.py로 다시 확인한다.
- 한국 사례는 "2023 청사진 vs 2026 실적"을 같은 회사 기사 2건으로 비교하면 확산 격차를 증명할 수 있다(교촌). 검색어 "교촌 튀김 로봇 두산로보틱스 도입 매장 수 2026".
- find.py 출력이 길면 Read로 offset/limit를 줘서 해당 줄만 읽는다. logi-today 같은 사이트는 raw가 1,000줄 넘는 메뉴 잡음이라 find.py만 쓴다.
