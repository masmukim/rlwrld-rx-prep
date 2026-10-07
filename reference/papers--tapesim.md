---
title: "TAPESIM: Efficient Simulation of Adhesive Tape Dispensing for Robotic Manipulation"
url: https://arxiv.org/abs/2609.28766
publisher: arXiv
published: 2026-09-23 (v2 2026-09-28)
fetched: 2026-10-06
tags: [papers, taping, simulation, wire-harness, deformable]
source_type: 논문
lang: en
authors: Zhaofeng Luo 외 12명 (Minchen Li 포함, 소속 초록 미표기)
citations: 미확인 (최신)
---

## 핵심 사실
- 문제: 하네스 고정이나 포장 밀봉에 테이프를 붙이려면 유연한 테이프, 움직이는 롤, 붙었다 떨어지는 표면을 함께 다뤄야 한다. 이를 반복 가능하게 시뮬레이션하려는 연구.
- 결과(초록): 32턴에서 물리 스텝 3.2~3.4배 가속, 실제 동작 재생 5건에서 랜드마크 오차 23~29% 감소, Peel 100쌍에서 균형 정확도 50% → 72.9~76.3%.
- 텔레오퍼레이션 박스 밀봉 시퀀스로 부착·풀기·자르기·밀봉 연속 작업을 시연.

## 원문 발췌
> "Applying adhesive tape to secure wire harnesses or seal packages requires robots to coordinate a flexible strip, a moving roll, and surfaces that attach and detach."
(raw: reference/raw/papers--tapesim.txt, 초록 v2)

## 메모 (RX 관점)
- 테이핑이 2026년에도 시뮬레이터부터 만드는 단계의 연구 과제라는 근거. 실로봇 하네스 테이핑 성공률은 이 논문에 없다.
- 72.9~76.3%는 시뮬레이터 예측 정확도이지 로봇 작업 성공률이 아니다.
