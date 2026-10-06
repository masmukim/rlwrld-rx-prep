---
title: RLWRLD releases RLDX-1, a dexterity-first foundation model for robot hands
url: https://www.therobotreport.com/rlwrld-releases-rldx-1-a-dexterity-first-foundation-model-for-robot-hands/
publisher: The Robot Report
published: unknown
fetched: 2026-10-06
tags: [company, rldx-1]
source_type: 기사
lang: en
---

## 핵심 사실
- 8.1B 파라미터, 체크포인트 3종(RLDX-1-PT, RLDX-1-MT-ALLEX, RLDX-1-MT-DROID) Hugging Face 공개.
- 아키텍처: Multi-Stream Action Transformer(MSAT), Qwen3-VL 8B 기반 VLM, Motion Module, Physics Module(촉각/토크), 64개 learnable token의 Cognition Interface, FIFO 슬라이딩 캐시 Memory Module.
- 추론 22.1 Hz (cognition interface 압축으로 35% 속도 향상).
- 센서: RGB, 촉각, 관절 토크. 센서가 없으면 vision-only로 graceful degradation.
- 대상 플랫폼: 싱글암(Franka Research 3), 듀얼암, 휴머노이드(ALLEX), 5지 손.
- ALLEX 휴머노이드 작업: 약 90% 성공 vs 기준 VLA 30% 미만 (기사 표기. 논문의 86.8% 대 약 40%와 상이, 아래 메모).
- 대상 작업: 커피 따르기, 컨베이어 피킹, 정밀 조립 등 접촉이 많은 조작.

## 원문 발췌
(기사 요약만 확인. 정확 수치는 논문 reference 참조)

## 메모
- 기사 수치(약 90%/30% 미만)와 논문 초록(86.8%/약 40%)이 다름 -> 논문 값 채택. 발행일은 확인 못함.
