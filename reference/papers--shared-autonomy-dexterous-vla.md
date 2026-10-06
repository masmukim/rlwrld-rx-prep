---
title: "End-to-End Dexterous Arm-Hand VLA Policies via Shared Autonomy: VR Teleoperation Augmented by Autonomous Hand VLA Policy for Efficient Data Collection"
url: https://arxiv.org/abs/2511.00139
publisher: arXiv
published: 2025-10-31
fetched: 2026-10-06
tags: [papers, teleoperation, data-collection, dexterous, vla, shared-autonomy]
source_type: 논문
lang: en
authors: Yu Cui, Yujian Zhang, Lina Tao, Yang Li, Xinyu Yi, Zhibin Li
citations: 미확인
---

## 핵심 사실
- 문제: 다관절 손의 VR 텔레오퍼레이션은 조작자 부담이 커 고품질 시연 수집이 비효율적.
- 방법: 공유 자율(shared autonomy). 조작자는 VR로 팔의 큰 움직임을 지시하고, 자율 DexGrasp-VLA 정책이 촉각과 시각 입력으로 손가락의 미세 동작을 담당. 교정 텔레오퍼레이션으로 정책을 지속 개선하는 human-in-the-loop 구조.
- 결과: 미지의 물체를 포함한 다양한 물체에서 90% 성공률(저자 자체 평가, 작업 수와 시행 수는 확인하지 못함).

## 원문 발췌
> divides control between macro and micro motions

## 메모 (RX 관점)
- 텔레오퍼레이션 비용이 병목이라는 문제를 "정책이 손 부분을 대신하는" 방식으로 줄이려는 시도. 데이터가 쌓일수록 수집 효율이 올라가는 순환 구조가 PoC 데이터 수집 계획에 쓸 수 있는 아이디어다.
