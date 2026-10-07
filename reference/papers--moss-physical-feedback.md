---
title: Modular Sensory Stream for Integrating Physical Feedback in Vision-Language-Action Models (MoSS)
url: https://arxiv.org/abs/2604.23272
publisher: arXiv
published: 2026-04
fetched: 2026-10-07
tags: [papers, rldx-1, tactile, torque, vla]
source_type: 논문
lang: en
authors: Jimin Lee, Huiwon Jang 외 (KAIST, 일부 저자 RLWRLD 소속 병기)
citations: 미확인
---

## 핵심 사실
- 문제: 기존 방식은 단일 물리 신호만 다루고, 신호를 추가하면 성능이 떨어지는 경우가 있음.
- 방법: 모달리티별 분리 스트림을 joint cross-modal self-attention으로 행동 스트림에 연결, 2단계 학습(초기에 사전학습 VLA 파라미터 고정), 미래 물리 신호 예측 보조 과제. RLDX-1 Physics 모듈의 출처 논문으로 RLDX-1 보고서가 인용.
- 결과: 접촉이 많은 실세계 과제에서 베이스 VLA(GR00T N1.5 평균 20.8%, pi0 27.1%) 대비 GR00T N1.5에서 평균 28.2% 개선(상대/%p 미확인). PnP Egg에서 GR00T N1.5 + MoSS(촉각) 66.7%, GR00T N1.5 + ForceVLA 54.2%.
- 어블레이션: 단일 스트림 DiT 대비 분리 스트림이 Unstack Cup에서 20.9% 개선, 2단계 학습이 단일 단계 대비 16.7% 개선(원문 표기, 상대/%p 미확인).
- 한계: 이번에는 본문 일부(검색된 줄)만 읽음. 평가 베이스는 GR00T N1.5와 pi0이며 RLDX-1이 아님.
- 소속: 저자 중 Huiwon Jang, Myungkyu Koo, Jinwoo Shin에 RLWRLD 소속 병기. 독립 검증 아님.

## 원문 발췌
> "we introduce decoupled modality streams that integrate heterogeneous physical signals into the action stream via joint cross-modal self-attention." (raw: reference/raw/papers--moss-physical-feedback.txt)
> "for GR00T N1.5, we achieve an average improvement of 28.2% over the base model" (raw: reference/raw/papers--moss-physical-feedback.txt)

## 메모 (RX 관점)
- RLDX-1의 "촉각·토크 별도 스트림" 설계의 근거 논문. RLWRLD 소속 저자가 있어 회사 주장의 독립 검증은 아니지만, 설계 아이디어는 RLDX-1 외 모델에도 적용된다는 점을 보여준다.
- 사용: research/rldx1-tech.md (A11).
