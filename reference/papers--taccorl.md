---
title: "TacCoRL: Integrating Tactile Feedback into VLA via Simulation"
url: https://arxiv.org/abs/2606.11743
publisher: arXiv (프리프린트, 게재 여부 미확인)
published: 2026-06-10
fetched: 2026-10-06
tags: [papers, tactile, vla, reinforcement-learning, simulation, assembly]
source_type: 논문
lang: en
authors: Siyu Ma, Yuqi Liang, Chang Yu, Yunuo Chen, Hao Su, Yixin Zhu, Yin Yang, Chenfanfu Jiang
citations: 미확인 (최신 논문)
---

## 핵심 사실
- 문제: 촉각 피드백이 행동을 어떻게 바꿔야 하는지는 위험하고 드문 상황에서 필요한데, 일반 시연에는 그런 장면이 거의 없다.
- 방법: 물리 정렬 시뮬레이터에서 sim-real 공동 학습 + 강화학습으로 사전학습 VLA에 촉각 인지 행동을 주입.
- 결과: 4개 양팔 접촉 작업 평균 성공률 72.5% vs 베이스라인 50.0%(초록). 소개된 작업에 시험관 삽입, 모양 퍼즐, 하드웨어 조립 2종(검색 결과 요약 기준).
- 한계: 실제와 정렬된 시뮬레이터가 필요하고, 평가는 4개 양팔 작업뿐.

## 원문 발췌
> an average success rate of 72.5%, compared to baseline of 50.0% (초록 요지)

## 메모 (RX 관점)
- 촉각 + RL + 시뮬레이션 결합 사례. 고객 현장 시뮬(디지털 트윈) 파트너십(피직스심랩 등, research/tech.md 3절)의 학술 근거 후보. 단 4개 작업 규모.
