---
title: DexBench 공식 사이트 (Defining the Benchmark for Industrial Dexterity)
url: https://dexbench.org/en/
publisher: RLWRLD (사이트 푸터 "Published by RLWRLD · 2026")
published: 2026-06-23 (sitemap lastmod, 사이트 본문에 발행일 없음)
fetched: 2026-10-09
tags: [benchmark, dexbench, rlwrld]
source_type: 1차
lang: en
---

## 핵심 사실
- JS 렌더링 단일 페이지. 홈 HTML이 `/data/contents_<en|kr|jp>.json`을 불러와 그린다. 단순 수집은 87자만 남는다.
- 버전 "Documentation v1.0". 영어·한국어·일본어 모두 18과제, 55평가 케이스.
- 구성: Home, OSC Axes(6축), Dexterity Regimes(E1~E5), 과제 18개(Task 0~17), Object Reference(48개 물체, 45개 구매 항목, 맞춤 키트 5종).
- 5영역: E1 Grasp Diversity, E2 Spatial Precision, E3 Temporal Precision, E4 Contact Precision, E5 Context Awareness. 영역별 과제 수(태그 기준, 계산) E1 13, E2 10, E3 4, E4 13, E5 14.
- 설계 원칙 4개: State Transition, State-Based Judgment, Real Objects, Breakdown Curves.
- 케이스 기술: 객체, 초기 상태, 목표 상태, 실패 조건. 시행 수, 합격 기준, 점수 산식, 리더보드, 제출 절차, 라이선스, 코드·논문 링크는 없음.
- 플랫폼 파트너: RLWRLD, NVIDIA. 산업 파트너 9곳: Hotel Lotte, Himart, SK Telecom, Hyosung, HL Mando, CJ Logistics, Fuji Electric(링크 도메인 fuji.co.jp), ANA, Mitsui Chemicals.
- 문의: inquiry@dexbench.org (일본어판 partnership.jp@rlwrld.ai). 외부 링크로 ALL HANDS UP(allhandsup.org).
- sitemap.xml은 /en/, /ko/, /ja/ 3개(lastmod 2026-06-23). /leaderboard, /about, /docs, /paper, /results, /data/leaderboard.json, /data/results.json은 404.

## 원문 발췌
> DexBench · Published by RLWRLD · 2026 (raw: reference/raw/benchmark--dexbench-contents-en.json)

> Not success rate, but where performance collapses. (raw: reference/raw/benchmark--dexbench-contents-en.json)

> Dexterity is not a property of the hand. It is a property of the solution (raw: reference/raw/benchmark--dexbench-contents-en.json)

## 메모
- 원문: reference/raw/benchmark--dexbench-home.html, benchmark--dexbench-contents-en.json, -kr.json, -jp.json.
- 55케이스는 8월 RLWRLD 발표의 80 use cases와 다르다. research/q5-dexbench.md 참조.
- 사이트 서술은 RLWRLD 자체 서술이다. 중립 증거로 쓰지 않는다.
