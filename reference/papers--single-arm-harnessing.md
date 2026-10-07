---
title: "Harnessing with Twisting: Single-Arm Deformable Linear Object Manipulation for Industrial Harnessing Task"
url: https://arxiv.org/abs/2410.10729
publisher: arXiv
published: 2024-10-14
fetched: 2026-10-06
tags: [papers, wire-harness, deformable, force]
source_type: 논문
lang: en
authors: Xiang Zhang 외 3명 (소속 초록 미표기)
citations: 미확인
---

## 핵심 사실
- 문제: 변형 전선의 복잡한 동역학 때문에 하네싱(전선을 클램프에 끼우며 배선) 자동화가 어렵다. 기존 방법은 양팔 로봇이나 촉각 센서에 기대 적응성·비용·확장성에 한계가 있다고 저자는 본다.
- 방법: 팔 1대 + 힘/토크 센서. 비틀기 동작으로 장력을 만들고 Koopman 기반 MPC로 장력 추종, 웨이포인트 계획, 클램프 삽입 프리미티브, 고정점 전환.
- 결과: 산업 수준 하네싱 작업에서 단일·다중 전선 모두 높은 성공률(초록, 수치 없음).

## 원문 발췌
> "Traditional methods, often reliant on dual-robot arms or tactile sensing, face limitations in adaptability, cost, and scalability."
(raw: reference/raw/papers--single-arm-harnessing.txt)

## 메모 (RX 관점)
- 반대 논거로 중요하다: 양팔·촉각 없이 모델 기반 제어로 클램프 배선을 푸는 접근이 있다. 다관절 손을 제안할 때 "왜 이 방식이 아닌가"에 답해야 한다.
