---
title: All Hands Up! Part 1 - Why Dexterity Matters (동기·목적·트레이드오프)
url: https://allhandsup.org/blog/part1
publisher: RLWRLD (All Hands Up 사이트)
published: unknown
fetched: 2026-10-12
tags: [hardware, allhandsup, dexterous-hand, tradeoff]
source_type: 1차
lang: en
---

## 핵심 사실
- 목적 4가지: 실제 dexterity를 좌우하는 설계 변수와 트레이드오프의 하드웨어 수준 기준 마련, 제조사가 설계를 검증할 기준 제공, 산업 파트너의 조작 솔루션 선택 지원, 공통 기반 구축.
- 근거는 "10종 이상의 dexterous hand를 다양한 실제 환경 태스크에서 직접 운용한 경험"이다(한국어판 "10종 이상", 영어판 "more than ten").
- DexBench는 "Where task-level evaluation is useful, we reference the benchmark tasks defined by DexBench"로만 언급되고, 분석은 하드웨어 중심이라고 밝힌다.
- 세 축: (1) 한 손으로 다양한 물체(손가락 수, 크기, DoF; 5지 사람 크기가 가장 넓은 커버리지), (2) 파지력, (3) 힘 감지·제어(촉각, 역구동성, 힘 투명성). 크기·파지력·역구동성은 서로 상충한다.
- 사례 3개(손 모델명은 비공개): 저DoF 소형(약 6 DoF), 사람 크기를 넘는 고출력(1.7 kg 손을 3 kg 정격 양팔 로봇에 달면 유효 페이로드가 크게 감소), 역구동성 없는 고출력 사람 크기 손(충격 누적으로 관절 기구 파손, 대부분의 상용 저역구동 손은 게인 조정 인터페이스를 제공하지 않음).
- 시각화에 쓴 URDF는 WIRobotics ALLEX의 것이고 "illustrative purposes only"다.

## 원문 발췌
> Drawing on direct operation of more than ten dexterous hands across diverse real-world tasks, RLWRLD is releasing its documented observations to contribute to a healthier ecosystem (raw: reference/raw/hardware--allhandsup-blog-part1-en.txt)

> Where task-level evaluation is useful, we reference the benchmark tasks defined by DexBench; the analysis here, however, is hardware-centric and stands on its own. (raw: reference/raw/hardware--allhandsup-blog-part1-en.txt)

> To support industrial partners in selecting manipulation solutions appropriate to the specific problems they face. (raw: reference/raw/hardware--allhandsup-blog-part1-en.txt)

## 메모
- "지원"이라는 단어는 목적 항목의 "산업 파트너의 솔루션 선택 지원"에만 나오며 RLDX-1 호환 보증이 아니다.
- 영어·한국어판 구조(237~261줄)가 같다. 사용처: Q9.
