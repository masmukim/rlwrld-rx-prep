---
title: "FMB: a Functional Manipulation Benchmark for Generalizable Robotic Learning"
url: https://arxiv.org/abs/2401.08553
publisher: arXiv
published: 2024-01-16
fetched: 2026-10-06
tags: [papers, benchmark, industrial, assembly]
source_type: 논문
lang: en
authors: Jianlan Luo, Charles Xu, Fangchen Liu, Liam Tan, Zipeng Lin, Jeffrey Wu, Pieter Abbeel, Sergey Levine (UC Berkeley로 추정)
citations: 미확인
---

## 핵심 사실
- 문제: 파지, 재배치, 조립 등 기능적 조작 기술을 일반화 관점에서 재현 가능하게 평가할 벤치마크가 부족.
- 방법: 3D 프린트로 복제 가능한 절차적 생성 물체와 실세계 작업(파지, 재배치, 여러 조립 행동)으로 구성, 모방학습 정책 세트 제공. 개별 기술과 다단계 작업 조합 평가 가능.
- 결과: 벤치마크와 베이스라인 정책 제공(초록에는 정량 성공률 요약 없음).
- 한계: 모델·데이터 규모를 관리 가능하게 하려고 작업 범위를 좁게 설정. 절차 생성 물체가 실세계 변이를 다 담지는 못할 수 있음(WebFetch 요약 기준).

## 원문 발췌
> fundamental manipulation skills, including grasping, repositioning, and a range of assembly behaviors (초록 요지)

## 메모 (RX 관점)
- 조립 작업 평가 틀의 선례. 고객 공정 PoC의 성공 기준을 "기술 단위로 쪼개 평가"하는 방식의 학술 근거로 쓸 수 있음(본 팀 해석).
