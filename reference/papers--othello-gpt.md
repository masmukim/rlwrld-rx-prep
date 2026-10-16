---
title: "Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic Task"
url: https://arxiv.org/abs/2210.13382
publisher: arXiv (ICLR 2023)
published: 2022-10
fetched: 2026-10-17
tags: [papers, world-model, interpretability]
source_type: 논문
lang: en
authors: Kenneth Li 외 (Harvard 등)
citations: 미조회
---

## 핵심 사실
- 설정: 오델로 게임 기록(수의 나열)만으로 합법 수를 예측하도록 GPT 변형(Othello-GPT)을 학습. 규칙에 대한 사전 지식 없음.
- 정확도: 합법 수 예측 오류율이 합성 데이터셋 학습 시 0.01%, 챔피언십 데이터셋 학습 시 5.17%, 미학습 모델 93.29%.
- 발견: 비선형 probe로 내부 활성에서 보드 상태를 높은 정확도로 읽을 수 있고 선형 probe는 결과가 나빴다. 활성을 반사실 보드 상태에 맞게 바꾸는 개입(intervention)으로 출력이 달라져, 이 표현이 예측에 인과적으로 쓰인다는 증거를 제시.
- 한계: 합성 과제(규칙이 작고 완전히 정의된 게임)에서의 결과다. 일반 LLM의 세계 모델 존재 증명이 아니다.

## 원문 발췌
> we uncover evidence of an emergent nonlinear internal representation of the board state. Interventional experiments indicate this representation can be used to control the output of the network. (raw: reference/raw/papers--t1-othello-gpt.txt, 26-28행)
> The error rate is 0.01% for Othello-GPT trained on the synthetic dataset and 5.17% for Othello-GPT trained on the championship dataset. (같은 파일, 174-175행)

## 메모
- T1에서 "다음 토큰 예측이 내부 상태 표현을 낳을 수 있다"는 존재 증명(제한된 영역). 반론/수정은 papers--othello-linear-nanda.md, papers--vafa-implicit-world-model.md.
