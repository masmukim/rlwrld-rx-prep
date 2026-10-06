---
name: competitors-research-notes
description: 경쟁사 비교(A3)에서 잘 열린 1차 소스, 막힌 사이트, 병렬 에이전트 파일 충돌 주의
metadata:
  type: reference
---

- 잘 열린 1차 소스: deepmind.google/blog, figure.ai/news/(helix-02, series-c), skild.ai/blogs, huggingface.co/blog/nvidia/gr00t-n1-7, investor.nvidia.com 보도자료, blogs.nvidia.com, tx-inc.com 블로그, arxiv.org/abs.
- 막힘: businesswire.com 403 -> 같은 보도자료를 finance.yahoo.com/news/ 재게재본으로 열면 된다.
- WebSearch 요약은 투자 총액과 일자가 소스마다 다르다(PI 누적 10억 vs 21억 달러, Figure 누적 19억 달러). 1차 보도자료로 확인되는 값(Figure 시리즈C, Skild 14억 라운드)만 본문 수치로 쓰고 나머지는 `추정`.
- WebFetch 요약 모델은 한국어 기사에서 회사명을 잘못 적는 경우가 있다(nate RFM 기사에서 "셀렉트스타가 RLDX-1 개발"). 기업명이 이상하면 reference 메모에 "요약 오류 의심"을 남기고 본문에 쓰지 않는다.
- 병렬로 다른 에이전트(A4 hardware)가 reference/를 같이 쓴다. reference/papers--*, hardware--*는 내가 Write하기 전에 Glob으로 다시 확인할 것. 이번에 papers--gemini-robotics.md를 덮어쓴 일이 있었다(같은 소스라 내용은 동일 계열).
- 한국 정책 소스: etnews(전자신문) 기사가 과기정통부 피지컬 AI 과제 예산(정부 340억 + 민간 157억 = 497억 원)을 가장 정확히 담음. 검색어 "LG전자 컨소시엄 피지컬AI 국책과제".
- 일본 소스는 검색 요약에서 SoftBank 컨소시엄, NEDO 사업 등이 보였으나 원문을 열지 않아 본문에 쓰지 못했다. 다음 갱신 때 NEDO 공모 페이지(nedo.go.jp/koubo/CD2_100431.html)와 METI AIロボティクス戦略 자료를 우선 열 것.
