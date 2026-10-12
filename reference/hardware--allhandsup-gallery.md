---
title: All Hands Up! 사이트 홈(갤러리)과 데이터 파일(_registry.json, _kapandji.json)
url: https://allhandsup.org/ko/
publisher: RLWRLD (사이트 푸터 "Published by RLWRLD · 2026")
published: unknown (본문에 발행일 없음. 보도는 2026-06-22~07-07)
fetched: 2026-10-12
tags: [hardware, allhandsup, dexterous-hand, rlwrld]
source_type: 1차
lang: en
---

## 핵심 사실
- JS 렌더링 단일 페이지(SPA). 홈 HTML(4,883줄)이 `hands_urdf/_registry.json`(손 22건)과 `hands_urdf/_kapandji.json`을 불러와 갤러리를 그린다. 영어·한국어·일본어·중국어 UI(`/en/ /ko/ /ja/ /zh/`), 데이터 파일은 언어 공통. sitemap.xml·robots.txt는 없고 SPA 홈으로 대체 응답(2026-10-12 확인).
- 레지스트리 22건 중 4건(XHAND 1 Pro, Xynova Flex 2, Xynova Prima 1, Agibot Omnihand V3)은 `hidden: true`라 갤러리 코드가 걸러 낸다. 화면 노출은 18종(코드 기준 추정, 렌더 화면은 미확인).
- 항목 필드: 제조사, 역구동성(backdrivability), 내·외전(abduction), 촉각(손바닥/손가락), DoF, 길이, 무게, 훅 그립 하중(kg), 손끝 힘(N), 통신 방식·주기, URDF 라이선스. 가격·구동 방식(텐던/직접) 필드는 없다.
- Kapandji 점수(0~11)는 손별 URDF 모델에서 엄지를 11개 기준점에 스윕한 시뮬레이션 값이다. 실물 측정이 아니다.
- 푸터 문구: "Are you a hand manufacturer? We'd love to test your hand and feature it here after testing." 저자: Max Chang Hwan Kim, Mark Seungjae Lee.
- 손 이미지는 AI로 생성되었고 실제 제품과 100% 일치하지 않을 수 있다는 고지문이 있다.
- 항목 노트에 내부 작업 메모가 남아 있다(예: Omnihand V3 "via Max, 2026-09-29", Xynova Prima 1 "2026-09-14 Suzhou meeting note"). 이 파일은 2026-09-29 이후에도 편집되고 있다는 근거다.

## 원문 발췌
> All Hands Up · Published by RLWRLD · 2026 (raw: reference/raw/hardware--allhandsup-home.html)

> Are you a hand manufacturer? We'd love to test your hand and feature it here after testing. (raw: reference/raw/hardware--allhandsup-home.html)

> Measured in simulation by sweeping each hand's thumb against the 11 Kapandji landmarks on its own URDF model. (raw: reference/raw/hardware--allhandsup-home.html)

> HIDDEN until the vendor-supplied URDF licence is confirmed. (raw: reference/raw/hardware--allhandsup-registry.json.txt, robotera_xhand1pro 노트)

## 메모
- 이 요약의 손별 수치는 reference/raw/hardware--allhandsup-registry.json.txt에서 Python으로 파싱했다(research/q9-allhandsup.md 표). 레지스트리는 `cache-control: max-age=0, must-revalidate`이고 ETag만 있으며 Last-Modified가 없어 갱신 시점은 알 수 없다.
- 4건의 hidden 항목은 라이선스 미확정 때문에 숨긴 내부 스테이징 데이터다. 고객 대면 자료에 인용하지 않는다.
- 사용처: Q9, B4 PoC 평가 플랫폼 근거.
