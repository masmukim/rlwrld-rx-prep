---
title: "PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change"
url: https://arxiv.org/abs/2206.10498
publisher: arXiv (Arizona State University, NeurIPS 2023 Datasets 트랙, 확인필요)
published: 2022-06
fetched: 2026-10-17
tags: [papers, limitation, planning]
source_type: 논문
lang: en
authors: Karthik Valmeekam 외 (ASU)
citations: 미조회
---

## 핵심 사실
- 목적: 상식 과제에서는 LLM이 계획하는지 세계 지식에서 검색하는지 구분하기 어렵다는 문제의식에서, 국제 계획 대회(IPC) 유형의 Blocksworld, Logistics 도메인과 난독화(obfuscated) 버전으로 계획 능력을 테스트하는 벤치마크.
- 결과(Blocksworld, 600개 인스턴스, 계획 생성 one-shot): GPT-4 206/600(34.3%), Instruct-GPT3(text-davinci-002) 41/600(6.8%).
- 결론(저자): plan generation을 포함한 여러 핵심 능력에서 최신 모델도 성능이 한참 모자란다.

## 원문 발췌
> on many critical capabilities–including plan generation–LLM performance falls quite short, even with the SOTA models. (raw: reference/raw/papers--t1-planbench.txt, 40-42행)
> 206/600 (34.3%) 41/600 (6.8%) (같은 파일, Table 1 Plan Generation 행, 468-471행)

## 메모
- T1에서 계획 한계의 1차 근거(2022~2023년 모델 기준). 이후 LRM(o1) 결과는 papers--planbench-o1.md. 현재 모델에 그대로 적용하지 않는다.
