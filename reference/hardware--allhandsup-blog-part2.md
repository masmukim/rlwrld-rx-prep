---
title: All Hands Up! Part 2 - What Makes a Good Robot Hand (평가 기준, 대표 손 4종, Type 1/Type 2)
url: https://allhandsup.org/blog/part2
publisher: RLWRLD (All Hands Up 사이트)
published: unknown
fetched: 2026-10-12
tags: [hardware, allhandsup, dexterous-hand, dexbench, tesollo, sharpa, wuji]
source_type: 1차
lang: en
---

## 핵심 사실
- 범위: 일반 7축 양팔 로봇에 구조 변경 없이 붙는 손목 장착형(modular wrist-mounted) 손. 전완 일체형(forearm-integrated)은 "later this year" 별도 다룬다고 한다. 근거는 "more than ten modular wrist-mounted hands"의 직접 운용.
- RLWRLD는 상용 손의 내부 평가 데이터베이스를 유지한다: DoF, 손가락별 ROM, 마디 길이·두께·폭, 무게, 손가락별 최대 파지력, 역구동 토크, 반복 정밀도, 파지 속도, 촉각 센서 유무. 제조사 사양이 없으면 자체 측정한다.
- 태스크 평가는 DexBench T00~T17(18과제)을 쓴다고 하나 손별 점수표는 없다.
- 평가 항목: 엄지 가동범위(Kapandji), DIP 독립 구동, 최소 파지 직경(5~8 mm 선형물에는 ROM과 마디 길이비가 모두 필요), 손끝·외피 재질(Shore A 10~30 실리콘이 자사 환경에 적합).
- 대표 손 4종과 서술(가격은 RLWRLD 서술, 공식가 아님):
  - SharpaWave: 22 DoF, 역구동, 200 mm, 1,200 g, 손끝 20 N. 평가 DB 고득점 손 중 하나, "NVIDIA를 비롯한 여러 연구 그룹의 연구 플랫폼으로 채택". 약 $50,000/개가 장벽. 손끝당 1,000 tactile pixel 이상.
  - DG-5F-S (Tesollo): 20 DoF, 역구동, 208.5 mm, 880 g, 손끝 19.5 N, 약 $7,500/개. 소지 CMC 능동 구동, 손끝 모듈 교체 지원(센서·팁 형상 맞춤), 개발자 모드로 관절별 저수준 데이터 실시간 교환. "DG-5F-S showed almost the same result as SharpaWave in DexBench"(수치 없음). 한계: 손가락 단면이 사각이고 마디 표면에 금속 하우징이 노출되어 마찰이 낮아 커터칼 같은 공구 조작이 불안정.
  - Wuji Hand V1.1: 20 DoF, 역구동 아님, 195 mm, 590 g, 손끝 15 N. 사람 손에 가장 가까운 무게·치수, 접착성 실리콘 외피, 4 mm 육각 렌치(T16)에 강함. 한계: 역구동이 없어 예기치 않은 충격으로 관절 기구가 손상됨(반복 데이터 수집 시 운용 연속성 위험). 촉각 장갑 모듈은 출시 예정.
  - (Aside) ALLEX (WIRobotics): 15 DoF, 역구동, 손끝 40 N, 전완 일체형 텐던 구동. 약 100 g 접촉력을 관절 토크로 추정, 이 토크 데이터를 학습 데이터에 직접 포함한다고 서술.
- 두 유형: Type 1(소형·경량·중간 역구동, 현장 배포용)과 Type 2(중형·고역구동, 데이터 수집·학습용). 목표 사양표: Type 1 길이 <205 mm, 무게 <600 g, 능동 DoF ≥20; Type 2 길이 <220 mm, 무게 <900 g, 능동 DoF ≥20. 공통: 훅 그립 최대 하중 ≥15 kg(30초 유지), 손끝 정지력 Type 1 ≥15 N / Type 2 ≥12 N, 전 손가락 닫힘 ≤0.3 초, 반복 정밀도 ≤±0.2 mm, 손바닥 전체 촉각 ≥1축 힘, 손끝당 ≥50 pixel, PID 게인 조정 가능, URDF/MJCF/USD 제공, 온도 85도 이하.
- "No currently marketed hand simultaneously satisfies high DoF, small form factor, sufficient force, and high back-drivability."
- 한계 고지: "This evaluation reflects RLWRLD's specific development and operational objectives. Results may differ under other operational conditions or task definitions."
- 영어·한국어·일본어판의 수치(50,000, 7,500, 1,200 g, 880 g, 19.5 N 등)는 일치(일본어판은 HTML에서 수치 추출 대조).
- 문의: partnership@rlwrld.ai

## 원문 발췌
> RLWRLD maintains an internal evaluation database of commercially available modular wrist-mounted hands. (raw: reference/raw/hardware--allhandsup-blog-part2-en.txt)

> DG-5F-S showed almost the same result as SharpaWave in DexBench. (raw: reference/raw/hardware--allhandsup-blog-part2-en.txt)

> RLWRLD develops a Robot Foundation Model that is not bound to any embodiment. (raw: reference/raw/hardware--allhandsup-blog-part2-en.txt)

> The price is approximately $7,500 per hand. (raw: reference/raw/hardware--allhandsup-blog-part2-en.txt)

## 메모
- 사이트 어디에도 "RLDX-1이 이 손을 지원/호환한다"는 문장이 없다. 평가 서술이다.
- DG-5F-S 가격 $7,500은 기존 reference/hardware--tesollo-dg5f-s.md의 $23,000(제품 DB)과 약 3배 충돌한다. 사용처: Q9, B3 가정값 점검.
