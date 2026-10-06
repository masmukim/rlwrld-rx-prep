---
title: Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ALOHA / ACT)
url: https://arxiv.org/abs/2304.13705
publisher: arXiv (RSS 2023)
published: 2023-04-23
fetched: 2026-10-06
tags: [papers, imitation-learning, teleoperation, bimanual]
source_type: 논문
lang: en
authors: Tony Z. Zhao 외 (Vikash Kumar, Sergey Levine, Chelsea Finn)
citations: 미확인
---

## 핵심 사실
- 문제: 저가 하드웨어로 정밀한 양팔 조작을 모방학습으로 학습할 수 있는가.
- 방법: Action Chunking with Transformers(ACT). 행동 시퀀스에 대한 생성 모델로 모방학습의 오차 누적과 불일관한 시연 문제를 완화. 커스텀 텔레오퍼레이션 인터페이스로 데이터 수집.
- 결과: 반투명 조미료 컵 열기, 배터리 끼우기 등에서 80~90% 성공. 작업당 약 10분의 인간 시연만 사용.
- 한계: 이번 조사에서는 초록 수준만 확인. 작업 종류와 시행 수는 확인하지 못함.

## 원문 발췌
> opening a translucent condiment cup and slotting a battery with 80-90% success

## 메모 (RX 관점)
- 텔레오퍼레이션 + 모방학습의 고전 기준선. 소수 시연으로도 단일 작업은 가능하다는 근거이나 "작업당 시연", "저가 그리퍼 양팔" 조건이라 다관절 손과 다양한 작업에 일반화할 수 없다.
