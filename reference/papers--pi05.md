---
title: "π0.5: a Vision-Language-Action Model with Open-World Generalization"
url: https://arxiv.org/abs/2504.16054
publisher: arXiv (Physical Intelligence)
published: 2025-04-22
fetched: 2026-10-06
tags: [papers, vla, competitors, physical-intelligence]
source_type: 논문
lang: en
authors: Physical Intelligence (공저자 35명)
citations: 미확인
---

## 핵심 사실
- 방법: π0 위에서 이종 작업의 co-training으로 폭넓은 일반화를 추구. 학습 입력은 여러 로봇의 관측, 의미 예측, 웹 데이터, 객체 검출, 저수준 행동 명령.
- 결과: 처음 보는 가정에서 주방이나 침실 정리 같은 장기(long-horizon)이면서 dexterous한 조작을 end-to-end 학습으로 수행했다고 주장(저자 자체 평가).
- 한계: 이번 조사에서는 초록 수준만 확인함. 성공률 수치는 확인하지 못함.

## 원문 발췌
> long-horizon and dexterous manipulation skills, such as cleaning a kitchen or bedroom, in entirely new homes (초록 요지)

## 본문 확인 (2026-10-17 추가, 본문 HTML 원문 Grep, raw: reference/raw/papers--pi05.txt)
- 사전학습 구성: 이동형 매니퓰레이터 가정 데이터 MM(약 400시간, 약 100개 가정), 고정형 로봇 다환경 데이터 ME, 실험실 교차 구현체 데이터 CE(OXE 포함), 상위 하위작업 예측 HL(수동 주석), 웹 멀티모달 WD(캡셔닝, VQA, 객체 위치). 후학습에서 말 지시 시연 VI 추가, CE 제외.
- 원문: 사전학습 예시의 97.6%는 이동형 매니퓰레이터의 가사 작업이 아니라 다른 로봇이나 웹 등 다른 출처("97.6% during the first training phase").
- 어블레이션(10회 시행/작업): ME 또는 CE 제외 시 성능 크게 저하, 둘 다 제외 시 더 저하. 웹 데이터 WD 제외는 모의 가정 과제에서는 통계적으로 유의하지 않으나, 처음 보는 물체에 대한 언어 따르기(OOD)에는 중요.
- 훈련 가정 수를 3~104곳으로 바꾸면 평균 성능이 대체로 상승. 104곳 모델은 테스트 가정을 학습에 넣은 대조군과 비슷한 성능이라고 보고.
- 말 지시 데이터 VI는 고수준 이동 조작 예시의 약 11%인데 결정적이라고 서술.
- 한계(저자): 서랍 손잡이 등 낯선 환경, 부분 관측, 하위작업 추론의 산만함에서 여전히 오류.

## 메모 (RX 관점)
- RLDX-1이 비교 대상으로 쓴 π0.5의 원 논문. "새 환경 일반화"가 π0.5의 주장이고 RLDX-1은 "손 정밀 조작 + 촉각 + 기억"을 내세운다는 차이를 구분해서 쓴다.
