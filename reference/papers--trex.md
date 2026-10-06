---
title: "T-Rex: Tactile-Reactive Dexterous Manipulation"
url: https://arxiv.org/abs/2606.17055
publisher: arXiv (프리프린트, 게재 여부 미확인)
published: 2026-06-15
fetched: 2026-10-06
tags: [papers, tactile, dexterous, vla]
source_type: 논문
lang: en
authors: Dantong Niu, Zhuoyang Liu, Zekai Wang 외 (총 34명, 소속 초록에 미표기)
citations: 미확인 (최신 논문)
---

## 핵심 사실
- 문제: 기존 VLA는 고주파 촉각 신호에 반응하지 못한다. 촉각 데이터 부족, 표준 평가 부재, VLA 구조 제약, 정적 촉각 인코더 한계가 이유라고 저자는 설명.
- 방법: 가변 속도 Mixture-of-Transformers 구조 + 시간적 촉각 VQ-VAE 인코더. 데이터 효율적 방식으로 100시간 촉각 풍부 데이터셋 구축.
- 결과: 12개 조작 작업(힘 제어, 변형 물체 포함)에서 가장 강한 베이스라인보다 평균 성공률 30% 이상 높음(초록. 상대/%p 구분 없음).
- 한계: 저자는 기존 한계를 지적하는 형태로 서술하며 자체 한계는 초록에 없음.

## 원문 발췌
> over 30% higher average success rate than the strongest baseline (초록 요지)

## 메모 (RX 관점)
- 공저자 Dantong Niu는 EgoScale(reference/papers--egoscale.md) 저자 목록에도 있다. 두 논문의 소속 관계는 초록 페이지에 없어 확인 못함.
- 다관절 손 + 촉각 + VLA에서 가장 최신 사례 중 하나. RLDX-1과 직접 비교 데이터는 없음.
