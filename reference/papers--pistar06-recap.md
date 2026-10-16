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

## 본문 확인 (2026-10-17 추가, 본문 HTML 원문 Grep, raw: reference/raw/papers--pistar06-recap.txt)
- 사전학습 데이터: "tens of thousands of hours of demonstrations from numerous tasks and a variety of different robots" + 웹 비전-언어 데이터 + 하위작업 예측. 정확한 시간·로봇 수는 본문에 없음.
- 평가 지표: 처리량(시간당 성공 수행 수)과 성공률. 성공 라벨은 사람 평가자가 여러 품질 지표를 합쳐 판정.
- 본문 결과 서술: 온로봇 데이터를 더한 최종 모델이 오프라인 RL+SFT 대비 다양한 세탁물·에스프레소에서 처리량 2배 이상, 실패율 약 절반. 세탁물(다양) 외 작업은 성공률 90%대 이상.
- 데이터량(부록): T셔츠 접기는 자율 데이터만(교정 없이) 반복당 300궤적(4대). 다양한 세탁물은 평가 450 + 교정 287 에피소드. 상자 조립은 배포 현장(오프사이트)에서 반복당 600 + 교정 360 에피소드, 로봇 3대. 단 600의 성격이 본문(5절 "600 autonomous trials")과 부록("600 demonstrations")에서 다르게 적혀 있어 자율 시도인지 시연인지 확정하지 못함(원문 내부 불일치).
- 한계(저자): "our system is not fully autonomous: it relies on human labeling and effort for reward feedback, interventions, and episode resets." 탐색은 대체로 탐욕적, 배치 방식의 오프라인 갱신.
- 평가 로봇은 정적 양팔(6-DoF 팔 2개, 평행 조 그리퍼).
- 블로그(pi.website/blog/pistar06, 2025-11-17, reference/competitors--pi-pistar06-blog.md)는 "배치 로봇의 경험이 주요 데이터원이 될 수 있다"고 서술.

## 메모 (RX 관점)
- "모방학습 후 현장에서 RL과 교정 개입으로 신뢰성 개선"의 사례. PoC 로드맵에 "시연 수집 -> 자율 실행 -> 교정 -> 재학습" 루프를 넣는 근거가 된다. 단, 손 작업 특화 검증은 아니다.
