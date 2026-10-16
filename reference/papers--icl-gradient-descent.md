---
title: "Transformers Learn In-Context by Gradient Descent"
url: https://arxiv.org/abs/2212.07677
publisher: arXiv (ICML 2023)
published: 2022-12
fetched: 2026-10-17
tags: [papers, in-context-learning, mechanism, hypothesis]
source_type: 논문
lang: en
authors: von Oswald 외 (ETH Zurich, Google)
citations: 미조회
---

## 핵심 사실
- 방법: 단일 linear self-attention 층이 회귀 손실 경사하강 1단계와 같은 변환을 한다는 가중치 구성(construction)을 보인다. 단순 회귀 과제로 self-attention만 가진 트랜스포머를 학습하면, 학습된 모델이 경사하강으로 얻은 모델과 매우 비슷하거나 가중치가 그 구성과 일치한다.
- 해석: 학습된 트랜스포머가 forward pass 안에서 경사하강으로 모델을 학습하는 "mesa-optimizer"가 된다고 서술.
- 범위(저자): "at least in the domain of regression problems". 선형 회귀 장난감 설정이며 실제 언어모델의 in-context learning이 같은 메커니즘이라는 것은 "hypothesize"한다고 밝힌다. MLP와 self-attention의 상호작용은 future work.
- induction head와의 연결도 논의(induction head를 경사하강 기반 ICL의 특수 사례로 이해할 수 있다고 제안).

## 원문 발췌
> This allows us, at least in the domain of regression problems, to mechanistically understand the inner workings of in-context learning in optimized Transformers. (raw: reference/raw/papers--t1-vonoswald-icl-gd.txt, 26-29행)
> hypothesize that the in-context learning capabilities of language models emerge through mechanisms similar to the ones we discuss here. (같은 파일, 162-164행)

## 메모
- T1에서 "ICL 메커니즘은 가설" 태그의 근거. 증명된 것은 장난감 회귀에서의 구성과 일치이고, 실제 LLM에 대한 확립 주장이 아니다.
