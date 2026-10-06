---
title: "Behavioral Cloning for Robotic Connector Assembly: An Empirical Study"
url: https://arxiv.org/abs/2602.22100
publisher: arXiv (프리프린트)
published: 2026-02-25
fetched: 2026-10-06
tags: [papers, connector-insertion, wire-harness, imitation-learning, force]
source_type: 논문
lang: en
authors: Andreas Kernbach 외 (Daniel Bargmann, Werner Kraus, Marco F. Huber)
citations: 미확인 (최신 논문)
---

## 핵심 사실
- 문제: 자동차, 제어반(electrical cabinet), 항공기 생산의 와이어 하네스 조립은 변형 케이블과 커넥터 형상 다양성 때문에 자동화가 어렵다. 커넥터는 손상을 막으려 제한된 힘으로 삽입해야 하고 자세 편차가 크다.
- 방법: 힘/토크 센서 + 고정 카메라를 융합한 행동 복제(behavioral cloning) 모델. UR5e를 SpaceMouse로 텔레오퍼레이션해 최대 300개의 성공 시연 수집.
- 결과: 5가지 커넥터 형상, 다양한 커넥터 자세에서 전체 삽입 성공률 90% 이상(자체 평가).
- 한계: 초록 기준 단일 팔 + 일반 그리퍼 구성, 커넥터 삽입 단일 동작 평가. 케이블 배선·고정은 범위 밖으로 보임(해석).

## 원문 발췌
> "connectors must be inserted with limited force to avoid damage, while their poses can vary significantly. While humans can do this task intuitively by combining visual and haptic feedback, programming an industrial robot for such a task in an adaptable manner remains difficult."
> "a dataset of up to 300 successful human demonstrations collected via teleoperation of a UR5e robot with a SpaceMouse"

## 메모 (RX 관점)
- 커넥터 "삽입" 한 동작은 그리퍼 + 힘센서 + 모방학습으로 90%대가 보고된다. 다관절 손의 차별성은 삽입 자체보다 케이블을 잡고 끌고 정렬하는 양손 동작에서 찾아야 한다(B1 해석).
- 시연 최대 300개는 단일 작업 PoC 데이터량 감각(Industrial Dexterity Benchmark 단계당 약 100개와 함께 참고).
