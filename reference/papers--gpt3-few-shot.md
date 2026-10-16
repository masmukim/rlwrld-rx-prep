---
title: "Language Models are Few-Shot Learners"
url: https://arxiv.org/abs/2005.14165
publisher: arXiv (OpenAI, NeurIPS 2020)
published: 2020-05
fetched: 2026-10-17
tags: [papers, llm, in-context-learning]
source_type: 논문
lang: en
authors: Brown 외 (OpenAI)
citations: 미조회
---

## 핵심 사실
- 모델: 1750억 파라미터 자기회귀 언어모델 GPT-3. 이전 비희소(non-sparse) 언어모델보다 10배 크다고 서술.
- 평가 방식: 그래디언트 업데이트나 미세조정 없이, 과제와 few-shot 시연을 텍스트 인터페이스만으로 제시(in-context learning). 컨텍스트에 맞는 만큼(보통 10~100개) 예시를 준다.
- 결과: few-shot 성능은 컨텍스트 내 예시 수와 모델 크기에 따라 크게 향상. 일부 과제에서 미세조정된 최신 모델과 경쟁하거나 드물게 넘는다.
- 한계(저자): few-shot이 여전히 어려운 데이터셋이 있고, 대규모 웹 코퍼스 학습에서 오는 방법론적 문제(오염 등)가 있는 데이터셋이 있다.

## 원문 발췌
> GPT-3 is applied without any gradient updates or fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction with the model. (raw: reference/raw/papers--t1-gpt3.txt, 23-24행)
> Few-shot learning also improves dramatically with model size. (같은 파일, 158-159행)

## 메모
- T1에서 "다음 토큰 예측 목표만으로 학습한 모델이 텍스트 입력만으로 새 과제를 수행한다"는 사실의 1차 근거. 메커니즘은 논문이 설명하지 않는다.
