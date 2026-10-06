---
title: "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion"
url: https://arxiv.org/abs/2303.04137
publisher: arXiv (RSS 2023, IJRR 2024)
published: 2023-03-07
fetched: 2026-10-06
tags: [papers, imitation-learning, diffusion, foundation]
source_type: 논문
lang: en
authors: Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song
citations: 510 (OpenAlex, RSS 2023판) / 550 (IJRR 2024판), 2026-10-06 기준. 버전별 분리 집계
---

## 핵심 사실
- 문제: 로봇 정책이 다봉(multimodal) 행동 분포와 고차원 행동 공간을 안정적으로 다뤄야 한다.
- 방법: 로봇 정책을 조건부 디노이징 확산(diffusion) 과정으로 표현. receding horizon 제어, 시각 조건화, 시계열 diffusion transformer를 사용.
- 결과: 4개 로봇 조작 벤치마크의 12개 작업에서 기존 최고 방법 대비 평균 46.9% 향상(초록. 상대인지 %p인지는 초록에 없음).
- 한계: 초록에 명시되지 않음.

## 원문 발췌
> an average improvement of 46.9% (12 tasks from 4 robot manipulation benchmarks) (초록 요지)

## 메모 (RX 관점)
- GR00T N1의 System 1, RLDX-1의 MM-DiT 행동 모델링 등 diffusion transformer 계열의 뿌리 논문(계보는 본 팀 해석).
- 산업용 벤치마크(Industrial Dexterity Benchmark)의 기준선이 Diffusion Policy다.
