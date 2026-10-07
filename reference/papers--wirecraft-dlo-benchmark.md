---
title: "WireCraft: A Simulation Benchmark for Industrial DLO Manipulation"
url: https://arxiv.org/abs/2606.18097
publisher: arXiv (프리프린트)
published: 2026-06-16
fetched: 2026-10-06
tags: [papers, deformable, benchmark, vla, connector-insertion, wire-harness]
source_type: 논문
lang: en
authors: Chongyu Zhu 외 7명 (Chi-Guhn Lee 포함, 소속 초록 미표기)
citations: 미확인 (최신)
---

## 핵심 사실
- 산업 DLO 조작 시뮬레이션 벤치마크. 작업군 3개: 커넥터 삽입(connector insertion), 클립 배선(clip routing), 채널 안착(channel seating). DLO 물리 모델 2종, 시뮬레이션과 실제 UR5 궤적 포함.
- RL, 모방학습(IL), VLA 정책을 같은 지표로 비교.
- 특권 상태(privileged state) 기반 RL은 각 작업군 대표 설정에서 82% 이상 성공.
- 커넥터 삽입에서는 소켓 접근 → 접촉이 많은 정렬로 넘어가는 구간이 비전 기반 RL, IL, VLA 모두의 핵심 병목.
- 결론: 산업 DLO 조작은 현재 비전 기반 학습에 여전히 열린 과제.

## 원문 발췌
> "For connector insertion, however, the transition from reaching the socket to contact-rich alignment remains a key bottleneck for vision RL, IL, and VLA policies."
> "industrial DLO manipulation, though tractable under privileged state, remains an open challenge for current vision-based learning."
(raw: reference/raw/papers--wirecraft-dlo-benchmark.txt, 초록 v1)

## 메모 (RX 관점)
- 하네스 3개 요소 작업(삽입, 클립 배선, 채널 안착)과 거의 같은 과제 구성. "비전만 쓰는 VLA는 접촉 정렬에서 막힌다"는 근거라 RLDX-1의 Physics(촉각·토크) 모듈 제안 논리와 연결된다(본 팀 해석). 시뮬레이션 결과이며 VLA 성공률 수치는 초록에 없다.
