---
title: "In-context Learning and Induction Heads"
url: https://arxiv.org/abs/2209.11895
publisher: arXiv / Transformer Circuits Thread (Anthropic)
published: 2022-09
fetched: 2026-10-17
tags: [papers, transformer, interpretability, in-context-learning]
source_type: 논문
lang: en
authors: Olsson 외 (Anthropic)
citations: 미조회
---

## 핵심 사실
- 가설: induction head(패턴 [A][B] ... [A] -> [B]를 완성하는 어텐션 헤드)가 대형 트랜스포머 in-context learning의 대부분을 담당할 수 있다.
- 증거 수준: 6개 논거. 작은 attention-only 모델은 "strong, causal evidence", MLP가 있는 큰 모델은 "correlational evidence". 저자가 "preliminary and indirect evidence", "circumstantial case"라고 스스로 규정한다.
- 관측: 학습 초기에 모든 크기의 모델(2층 이상)에서 phase change가 있고, 이때 induction head 형성과 in-context learning 향상이 동시에 일어난다(손실 곡선의 bump).
- 아키텍처를 바꿔 induction head 형성 시점이 이동하면 in-context learning 향상 시점도 같이 이동한다(논거 2).

## 원문 발췌
> we present preliminary and indirect evidence for a hypothesis that induction heads might constitute the mechanism for the majority of all "in-context learning" in large transformer models (raw: reference/raw/papers--t1-induction-heads.txt, 23-25행)
> For small attention-only models, we present strong, causal evidence; for larger models with MLPs, we present correlational evidence. (같은 파일, 29-30행)

## 메모
- T1에서 어텐션 헤드 회로가 in-context learning과 연결된다는 증거. 확립(작은 모델, 인과) / 가설(큰 모델)로 나눠 쓴다.
