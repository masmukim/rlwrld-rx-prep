---
title: "OpenVLA: An Open-Source Vision-Language-Action Model"
url: https://arxiv.org/abs/2406.09246
publisher: arXiv
published: 2024-06-13
fetched: 2026-10-06
tags: [papers, vla, open-source]
source_type: 논문
lang: en
authors: Moo Jin Kim 외 (Stanford, MIT 등)
citations: 45 (OpenAlex, arXiv ID 기준, 2026-10-06 기준. 버전별 분리 집계 가능)
---

## 핵심 사실
- 문제: 기존 VLA(예: RT-2-X 55B)가 비공개이고 무겁다.
- 방법: Llama 2 언어 모델 + DINOv2와 SigLIP을 결합한 비전 인코더. 7B 파라미터. 실세계 로봇 시연 97만 건으로 학습.
- 결과: 29개 작업에서 RT-2-X(55B)보다 절대 성공률 16.5% 높음(파라미터 7분의 1). 미세조정 설정에서 Diffusion Policy보다 20.4% 높음.
- 효율: LoRA로 일반 소비자용 GPU에서 미세조정, 양자화 배포 가능(성능 저하 없다고 주장).
- 공개: 체크포인트, 미세조정 노트북, PyTorch 코드를 공개.

## 원문 발췌
> outperform closed models such as RT-2-X (55B) by 16.5% in absolute task success rate across 29 tasks

## 메모 (RX 관점)
- 오픈 VLA의 기준점. 고객이 "범용 VLA를 직접 미세조정하면 되지 않나"라고 물을 때 비교 기준. 기본 구조는 단일 팔과 그리퍼 중심이며 다관절 손 평가는 이번 조사에서 확인하지 않았다.
