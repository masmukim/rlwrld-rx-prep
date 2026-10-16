---
title: "LLMs Still Can't Plan; Can LRMs? A Preliminary Evaluation of OpenAI's o1 on PlanBench"
url: https://arxiv.org/abs/2409.13373
publisher: arXiv (Arizona State University)
published: 2024-09
fetched: 2026-10-17
tags: [papers, limitation, planning, reasoning]
source_type: 논문
lang: en
authors: Karthik Valmeekam, Kaya Stechly, Subbarao Kambhampati
citations: 미조회
---

## 핵심 사실
- 결과: o1(LRM)은 PlanBench의 3~5개 블록 Blocksworld 600문제 중 97.8%, Mystery Blocksworld(난독화) 52.8%, 무작위 문자열 난독화 37.3%를 맞췄다. 이전 모델은 난독화 버전에서 거의 0이었다고 서술.
- 한계: 6~20개 블록, 20~40단계 최적 계획이 필요한 110문제에서 o1-preview는 23.63%로 급락. 저자는 정확도 향상이 일반적이거나 견고하지 않다고 결론.
- 저자 해석 각주: o1의 구조는 비공개이고 CoT 기반 RL 시스템일 수 있다는 것은 저자의 추측(speculate)이다.

## 원문 발췌
> Far surpassing any LLM, o1 correctly answers 97.8% of these instances. (raw: reference/raw/papers--t1-planbench-lrm.txt, 262행)
> over these 110 instances, o1-preview only manages 23.63% (같은 파일, 273-274행)

## 메모
- T1에서 "추론 시간 연산/RL 후훈련이 계획 성능을 크게 올리지만 길이 일반화는 여전히 약하다"의 증거. 저자 자체 평가(Preliminary, 특정 모델 한 시점).
