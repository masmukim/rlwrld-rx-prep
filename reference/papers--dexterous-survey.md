---
title: The Developments and Challenges towards Dexterous and Embodied Robotic Manipulation: A Survey
url: https://arxiv.org/abs/2507.11840
publisher: arXiv
published: 2025-07-16
fetched: 2026-10-06
tags: [papers, dexterous, survey, data-collection]
source_type: 논문
lang: en
authors: Gaofeng Li, Ruize Wang, Peisen Xu, Qi Ye, Jiming Chen
citations: 미확인
---

## 핵심 사실 (초록 + HTML 본문 서술 기준)
- 범위: 다관절 손 조작의 데이터 수집(시뮬레이션, 인간 시연 캡처, 텔레오퍼레이션)과 학습 프레임워크(모방학습, 강화학습) 정리.
- 어려움: 다관절 손은 자유도가 높고 상호작용 공간이 다양해 고차원 탐색이 어렵고, 물체와의 다중 접촉이 복잡한 역학을 만든다. 인간 손은 20개 이상의 자유도를 가진다.
- 데이터 3대 과제: (1) 고품질 데이터셋 부족, (2) 시뮬레이션과 현실 격차(마찰, 공기저항 모델 오차), (3) 인간과 로봇 손의 형태 차이.
- 수집 방식 비교: 시뮬레이션(저렴, 확장성 / 시뮬-현실 격차), 인간 영상(실세계 상호작용 / 인간-로봇 형태 격차), 텔레오퍼레이션(두 격차를 모두 피함 / 힘·촉각 피드백 약함, 지연).
- 학습: 모방학습은 데이터가 적게 들지만 시연의 정적 행동만 학습해 인간 성능을 넘기 어렵고, 강화학습은 보상이 희박하고 표본 효율이 낮아 수백만 회 반복이 필요하다.

## 원문 발췌
> the multi-fingered dexterous hand has a higher degree of freedom (DoF) and a more variable interaction space, which greatly increases the difficulty of searching in high-dimensional space

## 메모 (RX 관점)
- tech.md의 "손 조작이 어려운 이유"와 "데이터 수집 방식 비교"의 1차 근거. 서베이이므로 개별 수치는 원 논문 확인이 필요하다. 표의 비교는 WebFetch 요약 모델이 정리한 것이라 원문 표현과 다를 수 있다.
