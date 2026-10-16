---
title: "The Reversal Curse: LLMs trained on \"A is B\" fail to learn \"B is A\""
url: https://arxiv.org/abs/2309.12288
publisher: arXiv (ICLR 2024)
published: 2023-09
fetched: 2026-10-17
tags: [papers, limitation, generalization]
source_type: 논문
lang: en
authors: Lukas Berglund 외
citations: 미조회
---

## 핵심 사실
- 현상: "A는 B다"로 학습한 자기회귀 LLM은 "B는 A다"로 자동 일반화하지 못한다. 가상 사실 미세조정 실험에서 역방향 질문의 정답 로그확률이 무작위 이름 수준.
- 범위: GPT-3, Llama-1을 가상 문장으로 미세조정. 모델 크기와 모델 계열에 걸쳐 견고하고 데이터 증강으로 완화되지 않았다고 서술.
- 실세계 점검: GPT-4는 유명인의 어머니 이름 질문에는 79% 정답이지만 어머니의 이름으로 아들을 묻는 역방향은 33%.
- 단서: "A is B"가 컨텍스트 안에 있으면 모델은 역관계를 추론할 수 있다.

## 원문 발췌
> if a model is trained on a sentence of the form "A is B", it will not automatically generalize to the reverse direction "B is A". (raw: reference/raw/papers--t1-reversal-curse.txt, 23-25행)
> if "A is B" appears in-context, models can deduce the reverse relationship. (같은 파일, 30-31행)
> GPT-4 correctly answers questions like the former 79% of the time, compared to 33% for the latter. (같은 파일, 39-40행)

## 메모
- T1에서 가중치(in-weights)에 저장된 지식과 컨텍스트 내 추론의 비대칭 한계. 원인 설명은 저자의 가설이다.
