---
title: "Training Compute-Optimal Large Language Models"
url: https://arxiv.org/abs/2203.15556
publisher: arXiv (DeepMind)
published: 2022-03
fetched: 2026-10-17
tags: [papers, scaling, llm]
source_type: 논문
lang: en
authors: Hoffmann 외 (DeepMind)
citations: 미조회
---

## 핵심 사실
- 결과: 다양한 크기의 모델을 50억~5000억 토큰(원문 "5 to 500 billion tokens") 범위에서 학습해 분석한 결과, 컴퓨트 최적 학습에서는 모델 크기와 학습 토큰 수를 같은 비율로 키워야 한다(모델 2배당 토큰 2배)고 결론.
- 검증: Gopher(280B)와 같은 컴퓨트로 70B 파라미터 Chinchilla를 1.4조 토큰으로 학습. Gopher, GPT-3(175B), Jurassic-1(178B), Megatron-Turing NLG(530B)를 다양한 다운스트림에서 앞섰고 MMLU 평균 정확도 67.5%(Gopher 대비 7% 초과 향상).
- 비교 기준: 당시 대부분 모델은 약 3000억 토큰으로 학습됐다.

## 원문 발췌
> for every doubling of model size the number of training tokens should also be doubled. (raw: reference/raw/papers--t1-chinchilla.txt, 15-16행)
> Chinchilla uniformly and significantly outperforms Gopher (280B), GPT-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large range of downstream evaluation tasks. (같은 파일, 17-20행)

## 메모
- T1에서 "구조(파라미터)만 키우는 것은 충분조건이 아니다. 데이터 양이 같이 늘어야 한다"는 데이터 축 증거. 이 논문은 손실과 벤치마크 정확도를 같이 보고한다.
