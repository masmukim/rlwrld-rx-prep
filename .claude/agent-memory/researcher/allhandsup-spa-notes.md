---
name: allhandsup-spa-notes
description: RLWRLD 계열 SPA 사이트(allhandsup.org, dexbench.org) 수집법과 함정
metadata:
  type: reference
---

- RLWRLD 사이트(dexbench.org, allhandsup.org)는 SPA라 fetch.py 결과가 비거나 1,470자뿐이다. curl로 홈 HTML을 scratchpad에 받아 `grep -n "fetch(\|_URL"`로 데이터 파일 경로를 찾으면 된다. allhandsup.org는 `hands_urdf/_registry.json`(손 목록+사양), `_kapandji.json`, `blog/part1·part2(.ko/.ja)`(확장자 .html은 308 리다이렉트, 확장자 없이 받는다).
- JSON은 `.venv/bin/python -I 스크립트경로`로 파싱(스크립트는 scratchpad). sitemap.xml/robots.txt는 SPA 홈 HTML로 대체 응답하므로 "200이면 존재"로 믿지 말 것.
- 레지스트리의 `hidden: true` 항목은 갤러리 코드가 거르는 내부 스테이징 데이터(라이선스 미확정). 노출 수는 JSON 전체가 아니라 필터 후로 센다. 내부 메모(Notion, 회의 날짜)가 섞여 있으니 인용 금지.
- 보도 날짜가 매체마다 다르다(한국 06-22, 일본 PR TIMES 07-01, 영문 07-07). URL 날짜로 최초 공개일을 잡는다.
- 사용자 설명("RLWRLD가 지원하는 하드웨어")이 사이트 서술보다 강할 수 있다. 근거 문장이 없으면 "아카이브/평가"로 낮추고 이유를 적는다.
- WebSearch 요약은 취지 수준은 맞았으나 손 목록은 없다고 답했다. 손 목록은 데이터 파일에서만 얻었다.
