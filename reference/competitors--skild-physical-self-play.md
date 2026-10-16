---
title: Physical Self-Play
url: https://www.skild.ai/blogs/physical-self-play
publisher: Skild AI (공식 블로그)
published: unknown (본문이 "Last month, we introduced S1"로 서술해 S1 공개(2026-08-18) 다음 달인 2026-09 전후로 추정)
fetched: 2026-10-09
tags: [competitors, skild, self-play, post-training]
source_type: 1차
lang: en
---

## 핵심 사실
- S1급 모델이 시뮬레이션에서 자기 자신과 경쟁하며(축구) 매우 정교하고 동적인 작업을 학습한다는 사후학습 결과.
- Skild Brain 단계 도식: 사전학습의 데이터는 "Human videos, gloves, simulation, teleoperation", 이어 컨텍스트 학습, 사후학습 전략은 "Self-improvement via reinforcement learning", 이후 배치 또는 시뮬레이션.
- 한계 인식: "because S1-class models are pre-trained on human data, they are capped at human capability" — 인간 데이터 기반 사전학습 모델은 인간 능력이 상한이라는 자기 서술. 자기 대전으로 인간을 넘는 것이 목표.
- 이 글의 성과는 시뮬레이션 안의 결과이며 현실 휴머노이드 전이는 "successful transfer from simulation to humanoid"라는 서술 한 줄.

## 원문 발췌
> However, because S1-class models are pre-trained on human data, they are capped at human capability. (raw: reference/raw/competitors--skild-physical-self-play.txt, 14행)
> Human videos, gloves, simulation, teleoperation (raw: 같은 파일, 20행)

## 메모
- T2에서 Skild 사전학습 출처 목록(인간 영상, 장갑, 시뮬레이션, 텔레오퍼레이션)의 1차 근거. 출처별 비율은 없음.
- 게시일이 페이지에 표기되지 않아 시점은 `추정`.
