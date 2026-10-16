---
title: "π0: A Vision-Language-Action Flow Model for General Robot Control"
url: https://arxiv.org/abs/2410.24164
publisher: arXiv (RSS 2025)
published: 2024-10-31
fetched: 2026-10-06
tags: [papers, vla, competitors, physical-intelligence]
source_type: 논문
lang: en
authors: Kevin Black, Noah Brown, Danny Driess 외 (Physical Intelligence)
citations: 247 (OpenAlex, RSS 2025 버전, 2026-10-06 기준)
---

## 핵심 사실
- 문제: 유연하고 견고한 범용 로봇 정책(generalist policy)을 만든다.
- 방법: 사전학습된 VLM 위에 flow matching 아키텍처를 얹어 인터넷 규모의 의미 지식을 상속.
- 데이터: 단일 팔, 양팔, 모바일 매니퓰레이터 등 여러 dexterous 로봇 플랫폼의 대규모 다양 데이터.
- 평가: 사전학습 후 zero-shot 수행, 자연어 지시 따르기, 미세조정으로 새 기술 습득. 세탁물 접기, 테이블 정리, 박스 조립 등 실세계 작업.
- v1 2024-10-31 제출, 2026-01-08 개정.

## 원문 발췌
> a novel flow matching architecture built on top of a pre-trained vision-language model (VLM) to inherit Internet-scale semantic knowledge

## 본문 확인 (2026-10-17 추가, 본문 HTML 원문 Grep, raw: reference/raw/papers--pi0.txt)
- 사전학습 혼합: 오픈소스(OXE, Bridge v2, DROID)가 학습 혼합의 9.1%. 나머지는 자체 데이터 903M 타임스텝(단일팔 106M, 양팔 797M), 7개 로봇 구성, 68개 작업. 오픈소스 데이터는 카메라 1~2대, 제어 주파수 2~10 Hz이고 자체 데이터는 최대 50 Hz 제어.
- 작업·로봇 조합별 표본 수 n에 n^0.43 가중치를 줘 과대표 조합(세탁물 접기)을 낮춤.
- 후학습(미세조정) 데이터량은 작업별로 가장 쉬운 작업 5시간, 가장 복잡한 작업 100시간 이상.
- 한계(저자): "our experiments do not yet provide a comprehensive understanding of how the pre-training datasets should be composed: we combined all data available to us" — 사전학습 데이터를 어떻게 구성·가중해야 하는지는 미해결. 서로 다른 작업·로봇을 섞을 때 긍정 전이가 얼마나 있는지도 미해결이라고 씀.
- 시간 수치: 논문 서술은 사전학습 혼합이 "about 10,000 hours of demonstrations, complemented by the open-source OXE dataset"(raw 본문 및 결론부 "10,000 hours of dexterous manipulation data from 7 different robot configurations and 68 tasks"). 903M 타임스텝/10,000시간은 평균 약 25 Hz(계산).

## 본문 확인 2 (2026-10-17, T1 작업, raw: reference/raw/papers--t1-pi0.txt)
- 기존 VLA는 "autoregressive discretization to represent actions in a manner analogous to text tokens"를 쓰고, π0는 VLM을 flow matching(확산의 변형)으로 행동을 내도록 미세조정해 최대 50 Hz 행동 청크와 고난도 dexterous 과제를 다룬다. 저자는 이 과제들이 이전 자기회귀 VLA에 "major challenge"였다고 서술(173-177행, 218-227행).
- 사전학습: 로봇 데이터 10,000시간 이상(210행), flow matching으로 연속 행동 분포 표현(172-175행).

## 메모 (RX 관점)
- Physical Intelligence(경쟁사)의 기반 모델. "VLM + 행동 생성 모듈(flow matching)" 구조는 RLDX-1(MSAT), GR00T N1(diffusion transformer)과 같은 계보다. A3 경쟁사 비교의 기준점으로 사용.
- 초록에는 성공률 수치가 없어 정량 비교는 하지 못함.
