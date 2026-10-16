---
title: "Scaling Laws for Neural Language Models"
url: https://arxiv.org/abs/2001.08361
publisher: arXiv (OpenAI)
published: 2020-01
fetched: 2026-10-17
tags: [papers, scaling, llm]
source_type: 논문
lang: en
authors: Kaplan 외 (OpenAI, Johns Hopkins)
citations: 미조회
---

## 핵심 사실
- 대상: 자기회귀(autoregressive) 트랜스포머 언어모델의 교차 엔트로피 손실(cross-entropy loss). 다운스트림 과제 정확도가 아니다.
- 결과: 손실은 모델 크기 N(임베딩 제외), 데이터 크기 D, 학습 연산량 C와 각각 멱법칙(power-law)을 따르고, 다른 둘에 병목이 되지 않을 때 성립한다. 일부 추세는 7자릿수 이상에 걸친다.
- 모양 의존도: 깊이 대 너비 같은 아키텍처 하이퍼파라미터에는 거의 의존하지 않는다("very weakly").
- 과적합: 성능은 N^0.74/D 비에 의존하고, 모델을 8배 키우면 데이터는 약 5배만 키우면 페널티를 피한다.
- 저자 단서: 성능은 결국 평탄해져야 한다("must flatten out eventually").

## 원문 발췌
> Performance depends strongly on scale, weakly on model shape (raw: reference/raw/papers--t1-kaplan-scaling.txt, 95행)
> every time we increase the model size 8x, we only need to increase the data by roughly 5x to avoid a penalty. (같은 파일, 106-107행)

## 메모
- T1에서 "손실은 규모에 대해 예측 가능, 능력은 별개"의 근거. Chinchilla가 N:D 배분을 수정했다(papers--chinchilla.md).
