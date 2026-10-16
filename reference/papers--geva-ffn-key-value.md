---
title: "Transformer Feed-Forward Layers Are Key-Value Memories"
url: https://arxiv.org/abs/2012.14913
publisher: arXiv (EMNLP 2021)
published: 2020-12
fetched: 2026-10-17
tags: [papers, transformer, interpretability, mlp]
source_type: 논문
lang: en
authors: Mor Geva, Roei Schuster, Jonathan Berant, Omer Levy
citations: 미조회
---

## 핵심 사실
- 주장: 트랜스포머 피드포워드(MLP) 층은 key-value 메모리처럼 동작한다. key는 입력 텍스트 패턴과 상관되고, value는 출력 어휘 분포를 유도한다.
- 결과: 학습된 패턴은 사람이 해석 가능하고, 하위 층은 얕은(shallow) 패턴, 상위 층은 의미적(semantic) 패턴을 잡는다. 상위 층에서 value는 그 패턴 직후에 나올 법한 토큰에 확률을 모은다. 층 출력은 메모리들의 조합이고 잔차 연결이 예측을 층마다 다듬는다(refinement).
- 실험 범위: Baevski & Auli(2019)의 16층 언어모델(247M 파라미터)을 WikiText-103으로 학습한 단일 모델. 현대 대형 LLM에 대한 직접 검증이 아니다.

## 원문 발췌
> lower layers tend to capture shallow patterns, while upper layers learn more semantic ones. (raw: reference/raw/papers--t1-geva-kv.txt, 21-23행)
> the output of a feed-forward layer is a composition of its memories, which is subsequently refined throughout the model's layers via residual connections to produce the final output distribution. (같은 파일, 28-32행)
> a 16-layer transformer language model trained on WikiText-103 (같은 파일, 231-233행)

## 메모
- T1에서 "MLP = 지식 저장(패턴->다음 토큰 분포)" 서술의 1차 근거. 사실 저장이 MLP에 국한된다는 주장은 이 논문이 하지 않는다.
