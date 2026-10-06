---
title: RLDX-1 Foundation Model (RLWRLD 공식 페이지)
url: https://www.rlwrld.ai/en/rldx-1
publisher: RLWRLD
published: 2026-05-07
fetched: 2026-10-06
tags: [company, rldx-1]
source_type: 1차
lang: en
---

## 핵심 사실
- 공개일 표기 2026-05-07. 8.1B(mid-trained). 베이스 VLM Qwen3-VL 8B(RLDX-1-VLM으로 fine-tune).
- 체크포인트: RLDX-1-PT, RLDX-1-MT-ALLEX, RLDX-1-MT-DROID.
- 모듈: Motion, Physics(힘/접촉), Memory(64 cognition tokens). 센서 부재 시 vision-only로 degrade.
- 벤치마크(vs π0.5, π0-FAST, GR00T N1.6): RoboCasa Kitchen 70.6%(GR00T N1.6 66.2%), RoboCasa GR-1 Tabletop 58.7%(47.6%), RoboCasa 365 32.1%(26.9%), LIBERO-Plus 86.7%(72.6%).
- 하드웨어: ALLEX 휴머노이드(48-DoF, 양손 각 15-DoF), Franka Research 3(7-DoF), OpenArm + Inspire 손.
- 데이터: 비디오 생성 기반 합성 증강(약 5배), 인간 손 캡처 리타게팅(시간당 200+ 데모), 실 텔레오퍼레이션.
- 문의: partnerships@rlwrld.com.

## 원문 발췌
(해당 페이지 요약 기준)

## 메모
- 공개일: 공식 페이지 5/7, GitHub 5/6, arXiv v1 5/5(제출). 표기 차이는 시차/게시 시점 때문으로 보이며, 본문은 "2026-05-06 전후"로 서술.
