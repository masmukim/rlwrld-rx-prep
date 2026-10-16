---
title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
url: https://arxiv.org/abs/2201.11903
publisher: arXiv (Google, NeurIPS 2022)
published: 2022-01
fetched: 2026-10-17
tags: [papers, reasoning, prompting]
source_type: 논문
lang: en
authors: Jason Wei 외 (Google)
citations: 미조회
---

## 핵심 사실
- 방법: few-shot 프롬프트의 예시를 ⟨입력, 사고의 사슬(chain of thought), 출력⟩ 세 쌍으로 구성해 중간 추론 단계를 생성하게 한다.
- 결과: PaLM 540B가 CoT 예시 8개로 GSM8K(수학 문장제)에서 당시 최고 정확도를 기록, 검증기가 붙은 미세조정 GPT-3를 넘었다고 초록에 서술.
- 규모 의존: CoT는 약 100B 파라미터 모델에서만 이득이 있고 작은 모델은 유창하지만 비논리적인 사슬을 낸다(저자 서술). 저자가 emergent ability of model scale이라 부름.
- 저자 단서: 모델 내부 계산의 완전한 특성화는 열린 문제이고, CoT가 실제 추론인지는 이 논문이 주장하지 않는다(해석 가능 창이라고만 서술).
- 저자가 제시한 이점: 다단계 문제를 중간 단계로 분해해 추론 단계가 많은 문제에 추가 연산을 배정할 수 있다.

## 원문 발췌
> chain of thought, in principle, allows models to decompose multi-step problems into intermediate steps, which means that additional computation can be allocated to problems that require more reasoning steps. (raw: reference/raw/papers--t1-cot.txt, 138-140행)
> chain-of-thought prompting does not positively impact performance for small models, and only yields performance gains when used with models of ∼100B parameters. (같은 파일, 277-279행)

## 메모
- T1에서 "출력 토큰이 작업 메모리 역할"의 경험적 근거. 이론적 표현력은 papers--cot-expressivity.md.
