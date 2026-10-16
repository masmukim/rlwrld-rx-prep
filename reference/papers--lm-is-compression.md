---
title: "Language Modeling Is Compression"
url: https://arxiv.org/abs/2309.10668
publisher: arXiv (DeepMind, ICLR 2024)
published: 2023-09
fetched: 2026-10-17
tags: [papers, compression, scaling, in-context-learning]
source_type: 논문
lang: en
authors: Grégoire Delétang, Anian Ruoss 외 (Google DeepMind)
citations: 미조회
---

## 핵심 사실
- 논지: 예측 모델은 무손실 압축기로 바뀔 수 있고 그 반대도 성립한다(Shannon 정리, 산술부호화). 우도 최대화는 메시지당 비트 수 최소화와 같다. 이는 오래 확립된 사실이고 논문의 기여는 대형 모델 평가이다.
- 결과: 주로 텍스트로 학습한 Chinchilla 70B가 ImageNet 패치를 원본의 43.4%, LibriSpeech 샘플을 16.4%로 압축해 PNG(58.5%), FLAC(30.3%)를 앞섰다. 모델 파라미터 크기를 고려하지 않은 raw 압축률 기준이다(adjusted 압축률은 파라미터 크기를 포함하며 대형 모델은 큰 불이익을 받는다).
- 스케일링: 데이터셋 크기가 모델 크기에 대한 hard limit를 만들고 "model scaling is not a silver bullet"이라 서술.
- 해석: 사전학습 모델은 in-context learning으로 (메타)학습된 모델을 과제에 조건화해 압축 성능을 낸다고 설명.

## 원문 발췌
> Chinchilla 70B, while trained primarily on text, compresses ImageNet patches to 43.4% and LibriSpeech samples to 16.4% of their raw size, beating domain-specific compressors like PNG (58.5%) or FLAC (30.3%) (raw: reference/raw/papers--t1-lm-compression.txt, 19-22행)
> outperforming domain-specific standard compressors (not accounting for model parameter size). (같은 파일, 129행)
> the dataset size provides a hard limit on model size in terms of compression performance and that model scaling is not a silver bullet. (같은 파일, 145-146행)

## 메모
- T1에서 압축 관점: "예측 = 압축"의 수학적 동치는 확립, "그러므로 LLM이 세계 모델을 가진다"는 이 논문의 주장이 아니다(본 팀의 구분).
