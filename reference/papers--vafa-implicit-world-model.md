---
title: "Evaluating the World Model Implicit in a Generative Model"
url: https://arxiv.org/abs/2406.03689
publisher: arXiv (NeurIPS 2024)
published: 2024-06
fetched: 2026-10-17
tags: [papers, world-model, critique]
source_type: 논문
lang: en
authors: Keyon Vafa 외 (Harvard, MIT, Cornell)
citations: 미조회
---

## 핵심 사실
- 방법: 세계가 유한 상태와 전이 규칙(결정적 유한 오토마톤)으로 요약되는 영역에서, Myhill-Nerode 정리에서 착안한 세계 모델 복원 지표를 제안. 게임(오델로), 논리 퍼즐, 뉴욕 택시 내비게이션 3개 영역에서 평가.
- 결과: 기존 진단(다음 토큰이 유효한지 등)으로는 잘해 보이지만, 새 지표로 보면 세계 모델이 "far less coherent than they appear". 택시 데이터로 학습한 트랜스포머는 다음 방향이 유효한 회전인 비율이 거의 100%였지만, 복원한 거리 지도에는 불가능한 방향과 입체교차가 있었고 우회로(detour)가 생기면 경로 계획 성능이 무너졌다.
- 의미: 합법 수 예측이 좋다는 것이 정확한 세계 모델의 증거는 아니다.

## 원문 발췌
> the generative models we consider do well on existing diagnostics for assessing world models, but our evaluation metrics reveal their world models to be far less coherent than they appear. (raw: reference/raw/papers--t1-vafa-world-model.txt, 24-26행)
> While they sometimes have amazing route planning abilities, their performance breaks down when detours are introduced. (같은 파일, 80-81행)

## 메모
- T1에서 "세계 모델 증거"에 대한 반론. Othello-GPT와 상충이 아니라 "정확도 지표만으로는 부족하다"는 보완 관계로 쓴다.
