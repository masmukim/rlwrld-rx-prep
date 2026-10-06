---
title: "Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning"
url: https://arxiv.org/abs/2410.21845
publisher: arXiv, Science Robotics 2025 (OpenAlex 기준)
published: 2024-10-29
fetched: 2026-10-06
tags: [papers, reinforcement-learning, industrial, assembly, human-in-the-loop]
source_type: 논문
lang: en
authors: Jianlan Luo, Charles Xu, Jeffrey Wu, Sergey Levine (UC Berkeley로 추정, 초록 페이지에 소속 미표기)
citations: 66 (OpenAlex, Science Robotics판, 2026-10-06 기준)
---

## 핵심 사실
- 문제: 정밀 조립, 동적 조작, 양팔 협응 같은 어려운 작업을 실로봇에서 비전 기반으로 학습.
- 방법: 시연과 사람의 교정(human corrections), 표본 효율이 높은 RL 알고리즘, 시스템 설계를 통합(HIL-SERL).
- 결과: 베이스라인(모방학습, 기존 RL) 대비 평균 2배 성공률 향상, 1.8배 빠른 실행, 학습 시간 1~2.5시간에 거의 완벽한 성공률(초록).
- 한계: 초록 수준에서 명시되지 않음. 작업별 상세와 손(hand) 사용 여부는 미확인.
- 검색 요약 기준(2차, 원문 미열람): HG-DAgger 평균 49.7% 대비 대부분 작업에서 100%.

## 원문 발췌
> average 2x improvement in success rate and 1.8x faster execution ... 1 to 2.5 hours (초록 요지)

## 메모 (RX 관점)
- "사람 교정 + RL로 현장에서 신뢰성을 올린다"는 근거. 같은 저자 그룹의 FMB(산업 조립 벤치마크)와 연결. π*0.6 RECAP과 같은 방향이다.
- 고객에게는 "학습 1~2.5시간"을 그대로 약속하지 말고 작업 단순도와 단일 작업 조건을 확인해야 한다(본 팀 해석).
