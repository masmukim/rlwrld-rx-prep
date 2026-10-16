---
title: "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters"
url: https://arxiv.org/abs/2408.03314
publisher: arXiv (UC Berkeley, Google DeepMind)
published: 2024-08
fetched: 2026-10-17
tags: [papers, reasoning, test-time-compute]
source_type: 논문
lang: en
authors: Charlie Snell 외
citations: 미조회
---

## 핵심 사실
- 질문: 추론 시점에 고정된 LLM에 연산을 더 주면 어려운 프롬프트 성능이 얼마나 오르는가.
- 방법: 검증기 보상모델(PRM)에 대한 탐색, 그리고 응답 분포를 프롬프트에 맞게 적응적으로 갱신(수정)하는 두 방식을 비교.
- 결과: 방식별 효과가 프롬프트 난이도에 크게 좌우된다. 난이도에 따라 연산을 배분하는 "compute-optimal" 전략은 best-of-N 대비 효율을 4배 넘게 올린다. FLOPs를 맞춘 비교에서, 작은 기반 모델이 어느 정도 성공률을 내는 문제에서는 14배 큰 모델을 넘을 수 있다.
- 한계: 추론 대 사전학습 토큰 비율이 커지면 어려운 문제에서는 사전학습 확대가 낫다(Figure 1 캡션). 즉 대체재가 아니라 난이도 의존 교환관계다. 평가 모델은 PaLM 2-S* 계열(원문 확인).

## 원문 발췌
> the effectiveness of different approaches to scaling test-time compute critically varies depending on the difficulty of the prompt. (raw: reference/raw/papers--t1-snell-ttc.txt, 19-21행)
> on harder questions, pretraining is preferable in these settings. (같은 파일, 144-145행)

## 메모
- T1에서 "추론 시간 연산이 규모의 일부를 대체할 수 있으나 난이도·기반 모델 능력에 의존"의 근거.
