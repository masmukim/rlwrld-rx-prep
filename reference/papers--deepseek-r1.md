---
title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
url: https://arxiv.org/abs/2501.12948
publisher: arXiv (DeepSeek-AI; 저장본은 Nature 게재판 형식의 본문)
published: 2025-01
fetched: 2026-10-17
tags: [papers, reasoning, reinforcement-learning, post-training]
source_type: 논문
lang: en
authors: DeepSeek-AI
citations: 미조회
---

## 핵심 사실
- 주장: 사람이 라벨링한 추론 궤적 없이 순수 강화학습(RL)만으로 LLM의 추론 능력을 끌어낼 수 있다. 자기반성, 검증, 전략 전환 같은 패턴이 RL 중에 나타난다고 서술.
- 기반: DeepSeek-R1-Zero는 사전학습된 DeepSeek-V3-Base 위에서 RL을 한다. 즉 사전학습 모델이 전제다.
- 결과: R1-Zero의 AIME 2024 평균 pass@1이 RL 학습 중 15.6%에서 77.9%로 상승.
- 보상: 수학, 코딩 등 규칙 기반으로 검증 가능한 과제에서 규칙 기반 보상 사용. 신경 보상모델은 대규모 RL에서 reward hacking 위험이 있어 쓰지 않았다고 서술.
- 한계(저자): 가독성 저하와 언어 혼용, 구조적 출력과 도구 사용(검색, 계산기)은 R1이 못 한다. 신뢰할 보상 신호를 얻기 어려운 과제에서는 순수 RL 확장이 열린 문제.

## 원문 발췌
> the reasoning abilities of LLMs can be incentivized through pure reinforcement learning (RL), obviating the need for human-labeled reasoning trajectories. (raw: reference/raw/papers--t1-deepseek-r1.txt, 14-16행)
> jumping from an initial 15.6% to 77.9% (같은 파일, 202행)
> DeepSeek-R1 cannot leverage tools, such as search engines and calculators (같은 파일, 495-496행)
> for complex tasks that cannot be effectively evaluated by a reliable reward model, scaling up pure RL methods remains an open challenge. (같은 파일, 530-531행)

## 메모
- T1에서 후훈련 RL이 추론을 강화한다는 근거(자체 보고). 독립 재현 여부는 이번에 확인하지 않음.
