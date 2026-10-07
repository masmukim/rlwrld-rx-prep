---
title: "DEFT: Differentiable Branched Discrete Elastic Rods for Modeling Furcated DLOs in Real-Time"
url: https://arxiv.org/abs/2502.15037
publisher: arXiv
published: 2025-02-20 (v5 2025-05-06)
fetched: 2026-10-06
tags: [papers, deformable, wire-harness, simulation, branched]
source_type: 논문
lang: en
authors: Yizhou Chen 외 6명 (Ram Vasudevan 포함, 소속 초록 미표기)
citations: 미확인
---

## 핵심 사실
- 문제: 하네스 자율 조립에는 분기된 케이블(BDLO, Branched DLO)을 정밀하게 다뤄야 한다. 분기점에서 힘과 변형 전파가 복잡해 단일 DLO 모델을 이어 붙여서는 안 된다.
- 방법: 미분 가능한 물리 모델 + 학습 결합. 분기점 동역학, 중간 파지 모델링, 실시간 추론, 손 조작 계획.
- 결과: 실세계 실험에서 정확도·계산 속도·일반화가 기존 대비 우수(초록, 수치 없음).

## 원문 발췌
> "Autonomous wire harness assembly requires robots to manipulate complex branched cables with high precision and reliability."
> "The junction points in BDLOs create complex force interactions and strain propagation patterns that cannot be adequately captured by simply connecting multiple single-DLO models."
(raw: reference/raw/papers--deft-branched-dlo.txt, 초록 v5)

## 메모 (RX 관점)
- 하네스의 "분기"가 단순 케이블보다 어렵다는 근거. 시뮬레이션 사전학습·평가 환경 후보.
