---
title: "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control"
url: https://arxiv.org/abs/2307.15818
publisher: arXiv
published: 2023-07-28
fetched: 2026-10-06
tags: [papers, vla, foundation, google-deepmind]
source_type: 논문
lang: en
authors: Anthony Brohan, Noah Brown, Justice Carbajal 외 (Google DeepMind, 공저자 총 50여 명 이상)
citations: 270 (OpenAlex, 2026-10-06 기준)
---

## 핵심 사실
- 문제: 인터넷 규모 비전-언어 데이터의 지식을 로봇 제어로 옮길 수 있는가.
- 방법: 로봇 행동을 텍스트 토큰으로 표현해 언어 모델 학습 데이터와 함께 학습한다. 이 구조에 "VLA(Vision-Language-Action)"라는 이름이 붙었다.
- 결과: 6,000회 평가 시행(6k evaluation trials)에서 새 물체에 대한 일반화와, 로봇 학습 데이터에 없던 지시 해석 같은 창발 능력을 보고했다(초록, 수치별 성공률은 초록에 없음).
- 한계: 초록에 명시된 한계 없음.

## 원문 발췌
> expressing robot actions as text tokens ... incorporated into standard language model training (초록 요지, WebFetch 요약 기준)

## 본문 확인 (2026-10-17, T1 작업, raw: reference/raw/papers--t1-rt2.txt)
- 행동 표현: 연속 차원(종료 명령 제외)을 256개 bin으로 균등 이산화해 정수 8개로 표현하고, 언어 토큰과 같은 방식으로 학습 데이터에 넣는다(234-236행).
- 추론 속도: 55B 모델은 1-3 Hz, 5B 모델은 약 5 Hz로 클라우드 서비스에서 구동(278-280행). 저자는 고주파 제어가 필요한 환경에서는 실시간 추론이 병목이 될 수 있다고 서술(512-514행).
- 학습: 인터넷 규모 VQA와 로봇 궤적 데이터를 함께 co-fine-tune(초록, 22-25행).

## 메모 (RX 관점)
- VLA 개념의 출발점. 이후 OpenVLA, π0가 이 계보 위에서 오픈화, 연속 행동 생성(flow matching)으로 발전했다 (research/tech.md 1절).
- 인용 수는 OpenAlex 집계로 arXiv와 학회판이 분리될 수 있다.
