---
title: "Emergent Abilities of Large Language Models"
url: https://arxiv.org/abs/2206.07682
publisher: arXiv / TMLR (08/2022)
published: 2022-06
fetched: 2026-10-17
tags: [papers, emergence, scaling]
source_type: 논문
lang: en
authors: Jason Wei 외 (Google, Stanford, DeepMind, UNC)
citations: 미조회
---

## 핵심 사실
- 정의: 작은 모델에는 없고 큰 모델에는 있는 능력. 작은 모델의 성능을 외삽해서는 예측할 수 없다.
- 패턴: 규모-성능 곡선에서 임계 규모까지는 무작위 수준이다가 그 뒤 무작위 위로 올라간다.
- 사례 범주: few-shot 프롬프팅과 augmented prompting 전략(CoT 등)에서 관찰.
- 범위: 규모는 학습 연산량과 파라미터 수로 측정.

## 원문 발췌
> We consider an ability to be emergent if it is not present in smaller models but is present in larger models. (raw: reference/raw/papers--t1-emergent.txt, 27-28행)
> performance is near-random until a certain critical threshold of scale is reached, after which performance increases to substantially above random. (같은 파일, 65-66행)

## 메모
- T1에서 "창발" 주장의 원 논문. Schaeffer 2023이 지표 착시 반론(papers--emergent-mirage.md).
