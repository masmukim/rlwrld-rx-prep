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

## 메모 (RX 관점)
- Physical Intelligence(경쟁사)의 기반 모델. "VLM + 행동 생성 모듈(flow matching)" 구조는 RLDX-1(MSAT), GR00T N1(diffusion transformer)과 같은 계보다. A3 경쟁사 비교의 기준점으로 사용.
- 초록에는 성공률 수치가 없어 정량 비교는 하지 못함.
