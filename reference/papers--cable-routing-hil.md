---
title: Multi-Stage Cable Routing through Hierarchical Imitation Learning
url: https://arxiv.org/abs/2307.08927
publisher: arXiv (IEEE Transactions on Robotics 2024 게재, 검색 요약 기준)
published: 2023-07-18
fetched: 2026-10-06
tags: [papers, cable-routing, deformable, imitation-learning, wire-harness]
source_type: 논문
lang: en
authors: Jianlan Luo 외 (Charles Xu, Xinyang Geng, Gilbert Feng, Kuan Fang, Liam Tan, Stefan Schaal, Sergey Levine)
citations: 미확인
---

## 핵심 사실
- 문제: 케이블을 여러 클립에 순서대로 끼우는 다단계 작업. 변형체, 시각 피드백, 단계별 실패 누적이 난점.
- 방법: 하위(클립 삽입 모터 제어)와 상위(프리미티브 선택) 모두 시연으로 학습한 계층적 모방학습. Franka Panda 1대, 손목 RGB 카메라 2대, RealSense 2대, SpaceMouse 텔레오퍼레이션.
- 데이터: 하위 정책 시연 1,442개(성공 약 800, 의도적 실패 후 복구 약 600), 궤적당 약 3~5초, 5 Hz.
- 결과(HTML 본문, 분포 내): 1클립 19/24, 2클립 14/24, 3클립 12/24(합계 45/72). 평면(flat) BC와 BeT는 24회 중 0%.
- 하위 클립 삽입 단독 46%(쉬운 형상 18/25, 어려운 형상 5/25). 사람 텔레오퍼레이션 성공률 대략 60%.
- 미세조정: 새 배치 4개에 추가 시연 10개씩으로 50% → 85%(배치당 10회, 총 40회).
- 한계(저자): 절대 성공률이 산업 적용에는 아직 충분하지 않다.

## 원문 발췌
> "the absolute success rate is still not perfect for industrially relevant applications"
> "our system was able to improve its performance from 50% to 85% with only ten additional demonstrations"
> "roughly a human can achieve a 60% success rate by teleoperating the robot"
(raw: reference/raw/papers--cable-routing-hil.txt)

## 메모 (RX 관점)
- 하네스 레이업(지그·클립에 배선)의 학술 대리 과제. 단계가 늘면 성공률이 떨어지고(19→12/24) 실패 복구가 핵심이라는 근거 → RLDX-1 Memory(실수 복구) 주장과 연결.
- "추가 시연 10개로 새 배치 적응"은 다품종 품번 전환 비용 논리의 근거(단일 연구실, 소규모 시행).
- 평행 그리퍼 1팔 구성이다. 다관절 손이 필요하다는 근거는 아니다.
