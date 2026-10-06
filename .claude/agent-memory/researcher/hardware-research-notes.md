---
name: hardware-research-notes
description: 하드웨어·센서 리서치(A4)에서 통한 소스, 막힌 사이트, 가격 신뢰도 패턴
metadata:
  type: reference
---

- 잘 열린 1차: sharpa.com/pages/wave, shadowrobot.com/dexterous-hand-series/, gelsight.com 제품 페이지, zivid.com/zivid-3, fingervision.jp/en, robotiq.com(Hand-E 사양, 2F-85 사양은 없음), arXiv abs(ORCA 2504.04259, Digit 360 2411.02479).
- 막힘/불량: opencv.org 블로그와 humanoid.guide의 일부(DG-5F-S는 열림)는 403 또는 404 혼재, realsenseai.com D405 404, shadowrobot.com 스펙 PDF는 이진 데이터로 깨짐, arcweb.com 403.
- 가격은 공식 페이지에 거의 없다. 검색 요약의 가격은 리셀러(Knoxlabs, usrobotstore, roboticscenter.ai, robozaps)이고 서로 3~5배 충돌하므로 "검색 요약, `추정`"으로 표기하고 범위로 쓴다. 특히 Inspire는 공식 스토어 $24,399.99 vs 리셀러 $4.5~8.9k.
- 한국어 검색어 "원익로보틱스 앨러그로 핸드 V6 F", "테솔로 DG-5F"가 로봇신문/네이트 기사로 연결. 일본어 "川崎重工 ファナック 安川電機 視触覚 VTLA"로 FA 3사 NEDO 프로젝트(sbbit.jp)를 찾음.
- WebFetch 요약 모델이 기사에 없는 값을 채우는 경우가 있었음(Tesollo 기사에서 "grip force 40% 감소"로 오역). 기사 원문 제목과 대조하고 불확실하면 쓰지 않는다.
- 이번 작업은 WebFetch 약 24회로 15개 가이드를 넘김(소스당 1파일 저장 규칙 때문). 다음엔 아그리게이터 대신 1차 페이지 우선, 열기 전 필요성 판단.
