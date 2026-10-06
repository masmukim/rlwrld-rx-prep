---
title: "π*0.6: a VLA That Learns From Experience"
url: https://arxiv.org/abs/2511.14759
publisher: arXiv (Physical Intelligence)
published: 2025-11-18
fetched: 2026-10-06
tags: [papers, vla, reinforcement-learning, physical-intelligence]
source_type: 논문
lang: en
authors: Physical Intelligence (공저자 55명)
citations: 미확인
---

## 핵심 사실
- 방법: RECAP(RL with Experience and Corrections via Advantage-conditioned Policies). 시연, 온폴리시 수집 데이터, 자율 실행 중 전문가 텔레오퍼레이션 개입(교정)을 함께 쓰는 advantage conditioning. 먼저 오프라인 RL을 하고 이후 작업별로 온로봇 데이터로 특화.
- 작업: 실제 가정의 세탁물 접기, 박스 조립, 전문 에스프레소 머신 조작.
- 결과: 가장 어려운 작업에서 처리량(throughput)이 2배 넘게 증가, 실패율은 약 50% 감소(저자 자체 평가, 작업별 조건은 이번 조사에서 확인하지 못함).

## 원문 발췌
> demonstrations, data from on-policy collection, and expert teleoperated interventions provided during autonomous execution

## 메모 (RX 관점)
- "모방학습 후 현장에서 RL과 교정 개입으로 신뢰성 개선"의 사례. PoC 로드맵에 "시연 수집 -> 자율 실행 -> 교정 -> 재학습" 루프를 넣는 근거가 된다. 단, 손 작업 특화 검증은 아니다.
