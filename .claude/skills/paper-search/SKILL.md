---
name: paper-search
description: 로봇 조작, VLA, 로봇 손, 촉각 센서, 산업 자동화 관련 학술 논문을 arXiv, OpenAlex, Semantic Scholar에서 찾고 요약해 reference/에 저장한다. 기술 리서치, 경쟁사 기술 비교, 공정의 기술적 난이도 근거가 필요할 때 사용한다.
argument-hint: "[영어 키워드]"
---

# 논문 리서치

논문 검색어는 **영어로** 쓴다. 한국어 결과가 필요하면 마지막에 한국어 키워드로 한 번 더 찾는다.

## 1. 검색 소스 (WebFetch로 호출, 모두 2026-10-06에 동작 확인)

| 목적 | 소스 | URL 형식 |
|------|------|----------|
| 최신 논문 | arXiv API | `https://export.arxiv.org/api/query?search_query=all:%22<구문>%22+AND+all:<단어>&max_results=10&sortBy=submittedDate` |
| 영향력 높은 논문 (인용 수) | OpenAlex | `https://api.openalex.org/works?filter=title_and_abstract.search:%22<구문>%22,publication_year:%3E2022&per-page=10&sort=cited_by_count:desc&select=title,publication_year,cited_by_count,doi,ids` |
| 보조 (인용 관계, 요약) | Semantic Scholar | `https://api.semanticscholar.org/graph/v1/paper/search?query=<키워드>&limit=10&fields=title,year,citationCount,venue,externalIds,url` |

- OpenAlex는 `search=` 대신 반드시 `filter=title_and_abstract.search:`를 쓴다. `search=`에 인용 수 정렬을 걸면 관련 없는 논문이 나온다.
- Semantic Scholar는 키 없이 쓰면 자주 429(요청 과다)를 돌려준다. 실패하면 건너뛰고 arXiv와 OpenAlex만 쓴다.
- 일반 웹 검색(WebSearch)에 `site:arxiv.org`나 회사 연구 블로그를 붙여 보완한다.

## 2. 핵심 키워드 (조합해서 쓴다)
- 모델: vision-language-action (VLA), robot foundation model, generalist robot policy, cross-embodiment
- 손 조작: dexterous manipulation, multi-fingered hand, in-hand manipulation, high-DoF hand
- 데이터: teleoperation, imitation learning, human demonstration, data scaling, sim-to-real
- 센서: tactile sensing, visuo-tactile, force control
- 산업 적용: industrial assembly, cable insertion, deformable object manipulation, bin picking, kitting, packaging, logistics automation

## 3. 고르는 기준
한 주제당 3~7편을 고른다.
- 인용 수가 많은 기반 논문 1~2편 + 최근 1년 이내 논문 2~3편 + 산업 적용 사례 1~2편
- 경쟁사(Physical Intelligence, Google DeepMind, NVIDIA 등)와 RLWRLD 관련 논문은 우선 포함한다.

## 4. 읽고 요약하기
- 초록은 `https://arxiv.org/abs/<id>`에서 읽는다. 본문까지 필요하면 `https://arxiv.org/pdf/<id>`를 연다.
- 초록이나 본문에 실제로 있는 내용만 쓴다. 성능 수치는 실험 조건과 함께 적는다.

## 5. 저장 (reference 스킬 형식 + 논문 전용 필드)
파일명: `reference/papers--<짧은-영문-슬러그>.md`
```
---
title: 논문 원제목
url: https://arxiv.org/abs/<id>
publisher: 학회/저널 또는 arXiv
published: YYYY-MM-DD
fetched: YYYY-MM-DD
tags: [papers, <주제 태그>]
source_type: 논문
lang: en
authors: 제1저자 외 (소속)
citations: <수> (OpenAlex, YYYY-MM-DD 기준)
---

## 핵심 사실
- 문제: 무엇을 풀려고 했나
- 방법: 핵심 아이디어 1~2줄
- 결과: 주요 수치와 실험 조건
- 한계: 저자가 밝힌 한계

## 원문 발췌
> 초록에서 핵심 문장 1~2개

## 메모 (RX 관점)
- 산업 현장 적용 가능성, RLWRLD와의 관계, 고객에게 설명할 때 쓸 수 있는 포인트
```
