---
title: "Attention Is All You Need"
url: https://arxiv.org/abs/1706.03762
publisher: arXiv (NeurIPS 2017)
published: 2017-06
fetched: 2026-10-17
tags: [papers, transformer, architecture]
source_type: 논문
lang: en
authors: Vaswani 외 (Google)
citations: 미조회
---

## 핵심 사실
- 문제: 순환(recurrence)·합성곱 없이 시퀀스 변환 모델을 만들 수 있는가. 평가는 기계번역(WMT 2014 영독 등)이며 언어모델 사전학습 논문이 아니다.
- 방법: 순환을 버리고 어텐션만으로 입력과 출력의 전역 의존성을 만든다. 각 값(value)의 가중치는 질의(query)와 키(key)의 compatibility function으로 계산된다.
- 구조: 인코더는 동일한 층 N=6개, 층마다 multi-head self-attention과 position-wise 피드포워드 두 하위층, 각 하위층에 잔차 연결 + 층 정규화(LayerNorm(x + Sublayer(x))).
- 병렬성: self-attention 층은 모든 위치를 상수 횟수의 순차 연산으로 연결하고, 순환 층은 O(n)번의 순차 연산이 필요하다(Table 1).
- 한계(원문 서술): 상수 연산으로 줄인 대가로 effective resolution이 줄어든다("at the cost of reduced effective resolution").

## 원문 발췌
> a self-attention layer connects all positions with a constant number of sequentially executed operations, whereas a recurrent layer requires O(n) sequential operations. (raw: reference/raw/papers--t1-attention.txt, 263-264행)
> relying entirely on an attention mechanism to draw global dependencies between input and output. (같은 파일, 78-79행)
> the output of each sub-layer is LayerNorm(x + Sublayer(x)) (같은 파일, 118-119행)

## 메모
- T1(LLM 구조 근거표)에서 "병렬 학습", "내용 기반 라우팅(질의-키 호환도로 가중)", "깊이에 따른 조합(층 쌓기 + 잔차)"의 1차 근거. "내용 기반 라우팅"이라는 표현은 본 팀의 해석이고 논문 용어가 아니다.
