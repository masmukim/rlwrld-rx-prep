---
title: Open X-Embodiment: Robotic Learning Datasets and RT-X Models
url: https://arxiv.org/abs/2310.08864
publisher: arXiv (Open X-Embodiment Collaboration)
published: 2023-10-13
fetched: 2026-10-06
tags: [papers, vla, dataset, cross-embodiment]
source_type: 논문
lang: en
authors: Open X-Embodiment Collaboration (400여 명, 21개 기관)
citations: 미확인
---

## 핵심 사실
- 문제: NLP와 비전처럼 로봇도 다양한 데이터로 범용 모델을 학습할 수 있는가. "generalist X-robot policy"를 새 로봇, 작업, 환경에 효율적으로 적응시킬 수 있는가.
- 방법: 21개 기관의 데이터를 통합 형식으로 표준화한 Open X-Embodiment(OXE) 데이터셋 구축. RT-1-X, RT-2-X 정책 학습.
- 결과: 22개 로봇 플랫폼, 527개 스킬, 160,266개 작업. 로봇 간 positive transfer(다른 로봇의 경험이 성능을 높임)를 보고.
- 한계: 이번 조사에서는 초록 수준만 확인함.

## 원문 발췌
> Can we instead train generalist X-robot policy that can be adapted efficiently to new robots, tasks, and environments?

## 본문 확인 (2026-10-17 추가, PDF 원문 Grep, raw: reference/raw/papers--open-x-embodiment.txt)
- 데이터셋 규모: 22개 구현체, 100만+ 궤적, 21개 기관(본문 서술). 527개 스킬, 160,266개 작업(초록).
- 소규모 데이터 도메인: RT-1-X가 로봇별 원 방법을 5개 중 4개에서 앞서고 평균 개선이 큼(공동 학습 이익).
- 대규모 데이터 도메인(표 I): RT-1-X는 해당 구현체 단독 학습 RT-1 기준선을 넘지 못함(저자는 과소적합으로 해석). 55B RT-2-X는 앞섬. 즉 긍정 전이는 데이터가 적은 구현체와 큰 모델에서 뚜렷하고, 데이터가 많은 구현체에서는 모델 용량에 의존.

## 메모 (RX 관점)
- 교차 구현체(cross-embodiment) 학습의 기반 데이터셋. OpenVLA 초록은 RT-2-X(55B)를 비교 대상으로 쓴다 [papers--openvla.md].
- A2 tech.md에서 "다중 로봇 데이터 통합" 단계의 근거로 사용.
