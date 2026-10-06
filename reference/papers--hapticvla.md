---
title: "HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing"
url: https://arxiv.org/abs/2603.15257
publisher: arXiv (프리프린트, 게재 여부 미확인)
published: 2026-03-16
fetched: 2026-10-06
tags: [papers, tactile, vla, distillation, contact-rich]
source_type: 논문
lang: en
authors: Konstantin Gubernatorov, Mikhail Sannikov, Ilya Mikhalchuk 외 (Dzmitry Tsetserukou 포함, 총 10명. 소속 초록에 미표기)
citations: 미확인 (최신 논문)
---

## 핵심 사실
- 문제: 촉각 센서를 추론 시에도 달아야 하는 부담 없이 접촉이 많은 조작을 하고 싶다.
- 방법: 두 단계. (1) Safety-Aware Reward-Weighted Flow Matching(SA-RWFM): 과도한 힘에 벌점을 주는 사전 계산 촉각 보상 반영. (2) Tactile Distillation(TD): 비전과 상태에서 압축 촉각 토큰을 예측하게 해 촉각 인지 교사 모델의 능력을 일반 VLA에 이식.
- 결과: 실세계 실험 평균 성공률 86.7%(초록). 추론 시 직접 촉각 피드백을 준 버전을 포함한 베이스라인 VLA보다 높다고 주장. 작업 수, 시행 수, 베이스라인 이름은 초록에 없음. 버전: v1 2026-03-16, v2 2026-08-02.
- 한계: 초록에 명시되지 않음.

## 원문 발췌
> mean success rate of 86.7% ... Tactile-aware manipulation can be learned offline and deployed without direct haptic feedback at inference (WebFetch 요약의 초록 인용)

## 메모 (RX 관점)
- 고객 현장에 촉각 센서를 달지 않고도 접촉 성능을 얻는 방향의 근거. 센서 비용·유지보수 부담 감소 가능성이 있으나 평가 조건 미확인이므로 가정으로만 쓴다.
- RLDX-1처럼 촉각 입력을 쓰는 모델과 "센서 없이 증류" 모델 사이의 비교 질문(A3)에 쓸 수 있다.
