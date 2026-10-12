---
title: Benchmarking Resilience and Sensitivity of Polyurethane-Based Vision-Based Tactile Sensors
url: https://arxiv.org/abs/2511.07797
publisher: arXiv (cs.RO)
published: 2025-11-11
fetched: 2026-10-12
tags: [papers, hardware, tactile, durability, gel]
source_type: 논문
lang: en
authors: Benjamin Davis, Hannah Stuart (UC Berkeley, Embodied Dexterity Group)
citations: 미확인
---

## 핵심 사실
- 문제: 시각 기반 촉각 센서(VBTS)의 실리콘 겔은 감도는 높지만 하중과 표면 마모로 쉽게 열화한다. 겔 내구성의 표준 평가가 없다.
- 방법: 실리콘(SI)과 폴리우레탄(PU) 겔을 압축, 전단, 마모 시험으로 비교. 재질마다 겔 3개, 시험마다 다른 겔을 써 총 24개 제작.
- 결과(실험실 조건): 4 mm 구형 압자에 15 N 압축 하중을 반복하면 실리콘 샘플 3개 중 2개가 250~500 사이클 안에 관통으로 치명적 파손. 국소 전단(압축 10 N + 측방 5 N)에서도 실리콘 2개가 500 사이클 전에 관통·찢김. 평면 횡전단 1,000 사이클에서는 변화가 작았다(경미한 박리). PU 겔 3개는 압축·전단에서 변화가 미미했다.
- 병뚜껑 조이기·풀기 시연: 실리콘 겔은 16번째 조임 이후 찢어졌고 PU 겔은 50 사이클을 완주.
- 한계: PU는 낮은 하중에서 실리콘보다 감도가 낮을 수 있다고 저자가 밝힘.

## 원문 발췌
> "Silicone samples 1 and 2 fail catastrophically due to puncture within 250-500 cycles" (raw: reference/raw/papers--pu-vbts-durability.txt)

## 메모 (RX 관점)
- 실험실 가속 조건(15 N 집중 하중)이라 하네스 단자 삽입의 접촉 하중과 다르다. 현장 겔 수명으로 환산하지 않는다. 겔은 손에서 가장 먼저 소모되는 부품 후보이고, 겔 교체 단가·주기는 공개 수치가 없다.
