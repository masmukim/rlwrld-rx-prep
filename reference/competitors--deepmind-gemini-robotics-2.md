---
title: Gemini Robotics 2 brings whole body intelligence to robots
url: https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/
publisher: Google DeepMind (공식 블로그)
published: 2026-07-30
fetched: 2026-10-06
tags: [competitors, gemini-robotics, deepmind]
source_type: 1차
lang: en
---

## 핵심 사실
- 2026-07-30 공개. 모델 3종: Gemini Robotics 2(VLA), Gemini Robotics ER 2(Embodied Reasoning), Gemini Robotics On-Device 2(로컬 VLA).
- 지원 하드웨어: Apptronik Apollo 2 + SharpaWave 손(22 DoF), Apollo 2 + Inspire 손, Franka Duo + Robotiq 그리퍼, Dexmate, SO101, Trossen.
- 성공률(회사 자체 평가, 조건은 블로그 요약 수준): 그리퍼 기반 일반 pick-and-place 74.2%, 정밀 삽입 89.6%. 블로그는 "multi-finger dexterous manipulation remains challenging"이라 쓰고, 다지 손(Apollo + SharpaWave) 작업은 편차가 크다: 전구 끼우기(screw bulb) 36%, 전구 빼기(unscrew bulb) 92% (2026-10 팩트체크의 원문 대조 기준, 최초 WebFetch 요약에는 36%만 있었음).
- 제공 방식: ER 2는 Google AI Studio 공개 + Gemini Enterprise Agent Platform 비공개 프리뷰. VLA와 On-Device 모델은 "early-access partners"에게 제공, Trusted Tester Program 신청 가능.
- 데이터: On-Device 모델은 새 로봇에 "몇 시간의 적응, 보통 200개 미만 예시"로 적응한다고 주장.
- 안전: ASIMOV-Agentic 벤치마크 도입.

## 원문 발췌
> multi-finger dexterous manipulation remains challenging (WebFetch 요약에 인용된 문장)

## 메모
- WebFetch 요약 모델이 정리한 내용이라 수치의 실험 조건(작업 수, 시행 횟수)은 확인하지 못함. 36%가 어느 작업인지는 요약 표기를 따름.
- 손 조작을 "아직 어렵다"고 공식 인정한 점이 RLWRLD 포지셔닝(손 특화)과 관련. A3에서 사용.
