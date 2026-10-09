---
title: "Industrial Dexterity Benchmark: A Hardware-Software Benchmarking Platform for Industrial Dexterous Manipulation"
url: https://arxiv.org/abs/2607.14021
publisher: arXiv (프리프린트, 게재 여부 미확인)
published: 2026-07-15
fetched: 2026-10-06
tags: [papers, benchmark, industrial, cable, assembly]
source_type: 논문
lang: en
authors: Honglu He, Jacob Laufer, Zhiwu Zheng 외 11명 (Colm Prendergast 포함. 소속 초록에 미표기)
citations: 미확인 (최신 논문)
---

## 핵심 사실
- 문제: 산업 현장의 정교한 조작(케이블, 커넥터, 정밀 조립)을 평가할 하드웨어·소프트웨어 벤치마크가 필요.
- 대상 시나리오: 데이터센터 케이블 관리, 자동차 케이블 하니스, 기어박스 조립. 주 평가는 케이블 청소와 삽입 작업.
- 결과 (2026-10-09 fact-check 정정: v1 초록은 78%, v3(2026-09-21) 초록은 76%. raw는 v3이며 최신 판 값은 76%. 평가 과제는 데이터센터 케이블 청소 보드(IDB Board #1)의 케이블 청소 작업이고, 자동차 케이블 하니스 보드(Board #2)의 성능 결과는 논문에 없다): 멀티모달 Diffusion Policy가 파지+삽입 결합 작업에서 v1 78% / v3 76% 성공, 단일 카메라 RGB Diffusion Policy 기준선은 36%. 작업 단계(phase)당 텔레오퍼레이션 시연 약 100개. 구성당 48회 시행(초록 및 WebFetch 요약 기준).
- 한계: 48회 시행이라 소규모 검증이며, 특정 구조화된 산업 작업에 한정(WebFetch 요약의 해석).

## 원문 발췌
> reaches a 78% grasp and insert combined task success rate, compared to 36% ... single-camera RGB DP baseline (v1 초록 요지)

> reaches a 76% grasp and insert combined task success rate. This performance marks a significant improvement over the 36% observed from the single-camera RGB DP baseline (v3 초록, arXiv:2607.14021v3 21 Sep 2026) (raw: reference/raw/papers--industrial-dexterity-benchmark.txt)

## 메모 (RX 관점)
- (2026-10-09 fact-check 정정) 78%는 v1 초록, 최신 v3(2026-09-21)은 76%다. 76%는 데이터센터 케이블 청소 보드(Board #1)의 결과이며, 하니스 보드(Board #2)는 설계만 있고 성능 결과가 없다. 아래 "하니스와 직접 연결" 문장은 보드 설계 수준의 연결로만 읽는다.
- "자동차 케이블 하니스"는 B1 후보(와이어 하니스, 전자 조립)와 연결되는 보드 설계이지만 정책 평가 결과는 없다. 76%(v1은 78%)는 현장 가동률이 아님. "단계당 약 100개 시연"은 PoC 데이터량 감각으로 쓸 수 있으나 단일 연구실 결과.
