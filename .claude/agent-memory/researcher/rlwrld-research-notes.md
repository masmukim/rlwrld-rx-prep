---
name: rlwrld-research-notes
description: RLWRLD 조사에서 잘 통한 소스/검색어, 막힌 사이트, 소스 충돌 패턴
metadata:
  type: reference
---

- WebSearch 한 번에 요약+URL이 나오므로, 여러 언어 검색(한/영/일)을 병렬로 던진 뒤 핵심만 WebFetch.
- 1차 소스: PR Newswire(시드1 보도자료), arXiv 2605.03269, github.com/RLWRLD/RLDX-1, rlwrld.ai/en/rldx-1, AWS physical-ai 블로그.
- 일본어 소스가 풍부: KDDI MUGENLABO, Impress AI Watch, THE BRIDGE, 日経. 검색어 "RLWRLD KDDI ローソン".
- 막힘: platum.kr, thebridge 일부는 403. koreatimes.com은 DNS 실패. 대체로 벤처스퀘어/besuccess 사용.
- 주의: 2차 기사(R&D World, 데모데이, nate 요약)는 수치 오류가 있음(시드1 $21M 오기, "NVIDIA-backed", 파트너 BMW/Honda 단독 등장). 1차와 대조 필수.
- WebFetch 요약 모델이 날짜를 기사 게시일과 이벤트일로 섞어 보고하는 경우가 있음. 공개일은 GitHub/arXiv로 교차 확인.
