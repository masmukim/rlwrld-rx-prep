---
title: "FAST: Efficient Action Tokenization for Vision-Language-Action Models"
url: https://arxiv.org/abs/2501.09747
publisher: arXiv (Physical Intelligence, UC Berkeley, Stanford)
published: 2025-01
fetched: 2026-10-17
tags: [papers, vla, action-tokenization]
source_type: 논문
lang: en
authors: Karl Pertsch 외
citations: 미조회
---

## 핵심 사실
- 문제 진술: 시차(per-timestep)와 차원(per-dimension) 단위 binning 같은 단순 토큰화는 고주파 로봇 데이터로 dexterous 기술을 학습할 때 대체로 성능이 낮다. 인접 시점 사이의 상관이 크면 다음 토큰 예측 목표의 효과가 떨어진다.
- 방법: 이산 코사인 변환(DCT)으로 행동 시퀀스를 주파수 공간에서 압축한 뒤 토큰화(FAST). 토큰 간 상관을 줄이려는 압축 기반 접근.
- 결과: FAST로 학습한 자기회귀 VLA(π0-FAST)가 dexterous·장기 과제에서 π0 diffusion VLA와 비슷한 성능이며 학습은 5배 빠르다고 서술(저자 자체 평가).

## 원문 발췌
> Highly correlated action tokens diminish the effectiveness of the next token prediction objective (raw: reference/raw/papers--t1-fast.txt, 64-65행)
> train autoregressive VLAs for highly dexterous and high-frequency tasks where standard discretization methods fail completely. (같은 파일, 24-25행)

## 메모
- T1에서 "연속 고주파 행동에 다음 토큰 예측 유추가 깨지는 지점"과 그 한 가지 해법(토큰화를 바꿈)의 1차 근거. 연속 생성 접근(flow matching)과 병존하는 해법이다.
