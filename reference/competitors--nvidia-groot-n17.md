---
title: NVIDIA Isaac GR00T N1.7: Open Reasoning VLA Model for Humanoid Robots
url: https://huggingface.co/blog/nvidia/gr00t-n1-7
publisher: Hugging Face 블로그 (NVIDIA 게시)
published: 2026-04-17
fetched: 2026-10-06
tags: [competitors, nvidia, groot, dexterity]
source_type: 1차
lang: en
---

## 핵심 사실
- 2026-04-17 Early Access 공개(블로그 표기). 3B 파라미터. 구조: Cosmos-Reason2-2B 비전-언어 백본 + 32층 Diffusion Transformer 행동 모듈(이중 시스템).
- 라이선스: 블로그 요약은 "commercially licensed"로 표기. 검색 요약(2차)은 Apache 2.0이라 서술하나 라이선스 원문은 확인하지 못함.
- 학습 데이터: 인간 에고센트릭 영상 20,854시간, 제조·리테일·의료·가정 등 20개 이상 작업 범주.
- 손: 22-DoF 손 지원, 접촉이 많은 조작. 핵심 발견: 에고센트릭 데이터를 1k시간에서 20k시간으로 늘리면 평균 작업 완료율이 2배 넘게 오른다(블로그 주장, 평가 조건은 확인하지 못함).
- 검증 영역: 전신 이동 조작(loco-manipulation), 탁상 조작, 양손 dexterous 작업.
- 지원 로봇: Unitree G1, Bimanual Manipulator YAM, AGIBot Genie 1. LeRobot 데이터셋 형식 지원.
- 촉각/힘 입력: 열람한 블로그 요약에는 언급 없음(미확인).

## 원문 발췌
> More human egocentric data produces predictable, consistent improvements in dexterous manipulation capability — going from 1k to 20k hours more than doubles average task completion. (WebFetch 요약의 인용)

## 메모
- 20,854시간은 reference/papers--egoscale.md의 EgoScale 규모와 같은 숫자(공저자에 NVIDIA GEAR의 Linxi Fan 포함, 동일 연구 계열로 추정).
- RLWRLD가 내세우는 "에고센트릭 데이터로 손 조작 스케일링" 전략을 NVIDIA가 오픈 모델로 이미 내놓은 셈이라 A3의 핵심 경쟁 포인트.
- 비교 대상 GR00T N1.6(RLDX-1 논문의 비교 모델) 이후 버전이므로 RLDX-1 벤치마크가 N1.7에는 적용되지 않는다.
