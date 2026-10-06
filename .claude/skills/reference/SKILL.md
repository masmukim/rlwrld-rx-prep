---
name: reference
description: reference/ 폴더의 조사 자료를 찾아 읽고, 새로 조사한 소스를 저장한다. 웹 리서치를 하기 전(이미 조사한 자료가 있는지 확인), 중요한 소스를 읽은 직후(저장), 사실 검증이나 가정값의 근거를 찾을 때 사용한다.
argument-hint: "[find <키워드> | save <URL 또는 주제> | list]"
---

# 레퍼런스 저장소 (reference/)

조사한 소스를 한 건당 파일 하나로 저장해 두고, 다음 작업에서 다시 조사하지 않고 꺼내 쓴다.
research/*.md가 정리된 **결론**이라면, reference/는 그 결론의 **근거 원자료**다.

## 파일 형식
파일명: `reference/<태그>--<짧은-영문-슬러그>.md` (예: `reference/company--rldx1-launch.md`)

```
---
title: RLWRLD, RLDX-1 공개
url: https://...
publisher: 발행처
published: YYYY-MM-DD      # 모르면 unknown
fetched: YYYY-MM-DD        # 조사일
tags: [company, rldx-1]
source_type: 1차 | 기사 | 논문 | 공식문서 | 보고서
lang: ko | en | ja
---

## 핵심 사실
- 수치와 사실을 한 줄씩. 각 줄은 원문에 실제로 있는 내용만 쓴다.

## 원문 발췌
> 수치나 주장의 근거가 되는 문장만 짧게 인용한다 (저작권 때문에 전문 복사 금지).

## 메모
- 다른 소스와 다른 점, 해석, 어떤 작업에 쓰였는지 (예: A1, B3 가정값)
```

**태그** (첫 태그가 파일명 접두어): `company`, `tech`, `competitors`, `hardware`, `market`, `papers`, `case`, `claude-code`

논문은 paper-search 스킬의 논문 전용 필드(authors, citations)를 추가로 쓴다.

## 찾기 (find / list)
웹 검색 **전에** 항상 먼저 찾는다.
1. 목록 보기: Grep으로 `^(title|tags|fetched):` 패턴을 `reference/` 전체에서 검색한다.
2. 주제로 찾기: 파일명 접두어(`reference/competitors--*`)나 Grep 키워드 검색을 쓴다.
3. 찾은 파일을 Read로 읽고 `fetched` 날짜를 확인한다.
   - 30일 이내이고 필요한 내용이 있으면 그대로 쓰고, 웹 검색을 생략한다.
   - 오래됐거나 빠진 내용이 있으면 웹에서 보완하고 저장한다.
4. research/나 case/ 문서에 인용할 때는 원래 URL과 함께 reference 파일 경로를 적는다.

## 저장하기 (save)
WebFetch로 읽은 소스 중 결과물에 **인용하는 것**은 저장한다. 검색만 하고 쓰지 않은 소스는 저장하지 않는다.
1. 같은 URL의 파일이 이미 있는지 Grep으로 확인한다. 있으면 새로 만들지 않고 그 파일을 갱신한다. `fetched` 날짜를 바꾸고, 바뀐 사실에는 `(YYYY-MM-DD 갱신)`을 붙인다.
2. 없으면 위 형식으로 새 파일을 만든다.
3. 파일 하나에는 소스 하나만 담는다. 여러 소스를 종합한 내용은 research/에 쓴다.

## 작업별 사용
| 사용자 | 언제 |
|--------|------|
| researcher | 조사 전에 찾기, 인용한 소스는 저장 |
| case-analyst | 후보 공정, 사이클 타임, 인력 수치의 근거를 찾고, 새로 조사한 소스는 저장 |
| roi-modeler | 가정값(단가, 인건비)의 출처를 reference에서 찾아 엑셀 출처 열에 적는다 |
| fact-checker | 주장을 reference의 원문 발췌와 먼저 대조하고, 부족할 때만 URL을 다시 연다 |
| 메인 에이전트 | 장표, 면접 준비, Claude Code 설정을 바꿀 때 (`claude-code` 태그) |
