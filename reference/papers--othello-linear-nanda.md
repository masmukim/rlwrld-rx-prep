---
title: "Emergent Linear Representations in World Models of Self-Supervised Sequence Models"
url: https://arxiv.org/abs/2309.00941
publisher: arXiv (BlackboxNLP 2023, 확인필요)
published: 2023-09
fetched: 2026-10-17
tags: [papers, world-model, interpretability]
source_type: 논문
lang: en
authors: Neel Nanda, Andrew Lee, Martin Wattenberg
citations: 미조회
---

## 핵심 사실
- 주장: Li 등(2023)의 비선형 표현과 밀접히 관련된 선형 표현이 있다. 보드를 흑/백이 아니라 "내 말/상대 말"(MINE/YOURS)로 선형 probe하면 거의 완벽한 정확도로 읽힌다(Table 1, 층이 깊어지면 90.9%에서 99%대).
- 활용: 단순한 벡터 연산으로 모델 동작을 조절(steering)할 수 있다고 보고. Li 등의 개입보다 단순하고 해석이 쉽다고 서술.
- 의미: Li 등이 "선형 probe는 실패"라고 한 결과는 표현 좌표를 흑/백으로 잡은 데서 온 것이라는 수정이다.

## 원문 발췌
> we provide evidence of a closely related linear representation of the board. In particular, we show that probing for "my colour" vs. "opponent's colour" may be a simple yet powerful way to interpret the model's internal state. (raw: reference/raw/papers--t1-nanda-linear-othello.txt, 17-22행)

## 메모
- T1에서 Othello-GPT 세계 모델 증거의 보강. 여전히 오델로 한 영역의 결과다.
