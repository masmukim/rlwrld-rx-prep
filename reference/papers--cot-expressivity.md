---
title: "The Expressive Power of Transformers with Chain of Thought"
url: https://arxiv.org/abs/2310.07923
publisher: arXiv (ICLR 2024)
published: 2023-10
fetched: 2026-10-17
tags: [papers, reasoning, theory]
source_type: 논문
lang: en
authors: William Merrill, Ashish Sabharwal
citations: 미조회
---

## 핵심 사실
- 질문: 중간 토큰 생성이 디코더 트랜스포머의 계산 능력을 근본적으로 늘리는가.
- 이론 결과(복잡도 이론 추측 가정 하): 표준 트랜스포머(바로 답하는)는 일부 문제를 증명 가능하게 못 푼다. 중간 단계가 로그 개수면 한계를 조금만 넓히고, 선형 개수면 모든 정규 언어(regular language) 인식이라는 명확한 새 능력을 더하며 문맥민감 언어 안에 머문다. 다항 개수(일반화된 pre-norm)면 정확히 다항시간 풀이 가능 문제를 인식한다.
- 의미: 중간 토큰이 일종의 순환 상태처럼 쓰일 수 있음을 이론적으로 뒷받침. 이론은 표현력(할 수 있는가)이지 학습 가능성(학습으로 찾는가)이 아니다.

## 원문 발췌
> We show that the answer is yes, but the amount of increase depends crucially on the amount of intermediate generation. (raw: reference/raw/papers--t1-cot-expressivity.txt, 23-24행)
> such methods could unlock greater expressive power on sequential reasoning problems because the model can use each intermediate token as a kind of recurrent state. (같은 파일, 51-53행)

## 메모
- T1에서 "출력 토큰 = 작업 메모리" 서술의 이론 근거. 표현력 결과를 학습 결과로 오해하지 않도록 구분한다(본 팀의 구분).
