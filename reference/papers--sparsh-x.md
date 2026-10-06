---
title: "Tactile Beyond Pixels: Multisensory Touch Representations for Robot Manipulation (Sparsh-X)"
url: https://arxiv.org/abs/2506.14754
publisher: arXiv (Meta FAIR 관련 저자 구성, 소속은 초록에 미표기. 추정)
published: 2025-06-17
fetched: 2026-10-06
tags: [papers, tactile, representation, digit-360]
source_type: 논문
lang: en
authors: Carolina Higuera, Akash Sharma, Taosha Fan 외 (Mustafa Mukadam, Mike Lambeta 포함)
citations: 미확인
---

## 핵심 사실
- 문제: 영상 기반 촉각만으로는 힘, 진동, 압력 정보를 놓친다.
- 방법: Digit 360 센서의 4가지 촉각 모달리티(이미지, 오디오, 모션, 압력)를 처리하는 Sparsh-X. 약 100만 건의 접촉 상호작용으로 사전학습.
- 결과: 종단간 촉각 이미지 모델 대비 정책 성공률 63% 향상, 물체 상태 복원 강건성 90% 향상, 물성 추정 정확도 48% 향상(초록. 상대/%p 구분은 초록에 없음).
- 한계: 초록에 명시되지 않음.

## 원문 발췌
> four tactile modalities: image, audio, motion, and pressure ... approximately 1 million contact-rich interactions (초록 요지)

## 메모 (RX 관점)
- 촉각 사전학습이 정책 성능을 올린다는 증거. 센서(Digit 360) 종속이라 고객 하드웨어와 맞출 때 센서 선택이 변수(A4 하드웨어와 연결).
