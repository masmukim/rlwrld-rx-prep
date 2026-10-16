---
title: "A Mathematical Framework for Transformer Circuits"
url: https://transformer-circuits.pub/2021/framework/index.html
publisher: Transformer Circuits Thread (Anthropic)
published: 2021-12
fetched: 2026-10-17
tags: [papers, transformer, interpretability, residual-stream]
source_type: 논문
lang: en
authors: Elhage 외 (Anthropic)
citations: 미조회
---

## 핵심 사실
- 잔차 스트림(residual stream) 관점: 토큰 임베딩, 어텐션 헤드, MLP 층, 언임베딩이 잔차 스트림의 서로 다른 부분공간을 읽고 쓰며 서로 통신한다. 각 층의 결과가 스트림에 더해진다.
- 분석 범위: 대부분 MLP가 없는 attention-only 트랜스포머로 단순화해 분석한다(저자 스스로 "very dramatic simplification"이라 표기).
- 1층 attention-only 모델은 바이그램 모델과 여러 skip-trigram 모델의 앙상블로 이해될 수 있다고 주장한다.

## 원문 발췌
> All components of a transformer (the token embedding, attention heads, MLP layers, and unembedding) communicate with each other by reading and writing to different subspaces of the residual stream. (raw: reference/raw/papers--t1-tc-framework.txt, 64행)
> we focus on "attention-only" transformers, which don't have MLP layers. This is a very dramatic simplification of the transformer architecture. (같은 파일, 78행)
> one-layer attention-only transformers can be understood as an ensemble of a bigram model and several "skip-trigram" models (같은 파일, 194행)

## 메모
- 동료심사 학술지가 아니라 연구 블로그형 논문(1차 소스). 소규모 단순화 모델에서의 결과가 대형 모델에 그대로 성립하는지는 이 문서가 보장하지 않는다.
