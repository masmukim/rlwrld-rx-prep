---
name: skild-sumitomo-research-notes
description: 일본 기업 보도자료와 Skild 블로그를 1차로 확인하는 방법, WebSearch 요약이 틀린 사례, 막힌 소스 (Q2 작업, 2026-10-09)
metadata:
  type: reference
---

- 日本 기업 보도자료 PDF는 뉴스 목록 페이지를 WebFetch로 열어 "PDF href"를 물으면 직접 URL을 준다 (sws.co.jp/sws-news/docs/<해시>.pdf). 그 URL을 source-read fetch.py에 넣으면 텍스트가 잘 나온다. 영문판은 sumitomoelectric.com/sites/default/files/YYYY-MM/download_documents/prsNNN.pdf 형식(번호 추측은 404).
- Skild 공식 블로그 목록은 https://www.skild.ai/blogs 에서 WebFetch로 열린다. 개별 글(/blogs/s1, /blogs/skild-crosses-100m-arr)은 source-read로 저장 가능. 블로그 본문에 영상·그림이 많아 end-effector 같은 시각 정보는 텍스트로 안 나온다.
- WebSearch 요약이 원문과 반대로 답한 사례: "영문 릴리스에 Skild 이름이 없다"고 했으나 PDF 원문에는 명시. 요약은 단서로만 쓰고 PDF로 확인한다. 같은 질문이라도 검색어(일본어/영어)를 바꾸면 결과가 달라진다.
- MONOist 구기사(2015)는 source-read 저장본이 Shift-JIS 깨짐. WebFetch 요약으로만 쓰고 "요약 기준"으로 표시.
- NEDO PDF 번호 URL이 검색 요약과 다른 문서를 가리키는 경우 있음(100095321.pdf는 다른 사업).
- MarkLines는 첫 문단만 무료. X(Twitter)는 시도하지 않음(로그인 벽).
- 내가 한 실수 방지: 기자가 쓴 "Automating"을 1차 소스 시제("working towards deploying")와 비교해 약하게 읽는다. 기존 문서가 기사 시제를 그대로 가져온 경우 수정 대상으로 알린다.
