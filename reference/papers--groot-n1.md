---
title: "GR00T N1: An Open Foundation Model for Generalist Humanoid Robots"
url: https://arxiv.org/abs/2503.14734
publisher: arXiv (NVIDIA)
published: 2025-03-18
fetched: 2026-10-06
tags: [papers, vla, competitors, nvidia, humanoid]
source_type: 논문
lang: en
authors: Johan Bjorck, Fernando Castaneda 외 41명 (NVIDIA). 프로젝트 리드 Linxi "Jim" Fan, Yuke Zhu
citations: 미확인
---

## 핵심 사실
- 방법: 이중 시스템 설계. System 2(비전-언어 모듈)가 환경과 지시를 해석하고, System 1(diffusion transformer 모듈)이 실시간으로 부드러운 모터 동작을 생성.
- 데이터: 실로봇 궤적, 인간 영상, 합성 생성 데이터의 이종 혼합.
- 결과: 시뮬레이션 벤치마크와 여러 로봇 구현체에서 기존 모방학습 접근보다 우수하다고 보고. Fourier GR-1 휴머노이드의 양팔 조작에 배포, "높은 데이터 효율"을 주장.
- 한계: 이번 조사에서는 초록 수준만 확인함. 수치는 확인하지 못함.

## 원문 발췌
> The vision-language module (System 2) interprets the environment through vision and language instructions. The subsequent diffusion transformer module (System 1) generates fluid motor actions in real time.

## 메모 (RX 관점)
- RLDX-1이 벤치마크에서 비교한 GR00T N1.6의 초기 버전 논문. 데이터 피라미드(실로봇, 인간 영상, 합성) 접근이 RLDX-1의 데이터 혼합과 유사하다.
