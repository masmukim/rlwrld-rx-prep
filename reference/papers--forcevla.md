---
title: "ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation"
url: https://arxiv.org/abs/2505.22159
publisher: arXiv, NeurIPS 2025 (초록 페이지 기준 accepted)
published: 2025-05-28
fetched: 2026-10-06
tags: [papers, vla, force, tactile, contact-rich]
source_type: 논문
lang: en
authors: Jiawen Yu, Hairuo Liu, Qiaojun Yu 외 (Cewu Lu, Wenqiang Zhang 포함. 소속 초록에 미표기)
citations: 미확인
---

## 핵심 사실
- 문제: 기존 VLA는 힘 제어가 필요한 접촉 작업에서 어려움을 겪는다.
- 방법: 엔드이펙터의 6축 힘/토크 신호를 "first-class modality"로 두고, Mixture-of-Experts 모듈(FVLMoE)로 시각-언어 표현과 힘 피드백을 단계별로 융합. 동기화된 비전, 고유수용감각, 힘-토크 데이터셋 ForceVLA-Data 공개(5개 접촉 작업).
- 결과: π0 기반 베이스라인 대비 평균 작업 성공률 23.2% 향상, 플러그 삽입 등에서 최대 80%(초록. 23.2%가 상대인지 %p인지 초록에 없음).
- 한계: 5개 작업 규모. 시야 가림이나 동적 불확실성 조건의 작업이 포함됨.

## 원문 발췌
> treats external force sensing as a first-class modality within VLA systems (초록 요지)

## 메모 (RX 관점)
- π0를 기반으로 힘을 붙이면 접촉 작업이 좋아진다는 근거. RLDX-1의 Physics 모듈이 같은 문제의식이라는 점을 확인해 주지만, RLDX-1이 이 논문과 어떻게 다른지는 비교하지 않았다.
- 손이 아니라 힘-토크 센서(엔드이펙터) 중심이라 다관절 손의 촉각과는 다르다(본 팀 해석).
