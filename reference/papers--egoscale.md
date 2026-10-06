---
title: "EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data"
url: https://arxiv.org/abs/2602.16710
publisher: arXiv
published: 2026-02-18
fetched: 2026-10-06
tags: [papers, egocentric, data-scaling, dexterous, vla]
source_type: 논문
lang: en
authors: Ruijie Zheng, Dantong Niu 외 (Trevor Darrell, Yuke Zhu, Danfei Xu, Linxi Fan 포함. 소속은 초록 페이지에 미표기, NVIDIA 연관 가능성은 공저자 구성으로 추정)
citations: 미확인
---

## 핵심 사실
- 데이터: 행동 라벨이 붙은 에고센트릭 인간 영상 20,854시간 이상(이전 연구의 20배 이상).
- 법칙: 인간 데이터 규모와 검증 손실 사이에 log-linear 스케일링 법칙을 발견. 검증 손실이 실로봇 성능과 강하게 상관.
- 로봇: 22-DoF 다관절 로봇 손으로 실험, 자유도가 낮은 손으로도 전이.
- 결과: 사전학습 없는 기준선 대비 평균 성공률 54% 향상. 소량의 정렬된 인간-로봇 중간 학습(mid-training)으로 one-shot 작업 적응.
- 방법: 대규모 인간 사전학습 + 경량 정렬 중간학습의 2단계 전이.

## 원문 발췌
> a log linear scaling law between human data scale and validation loss

## 메모 (RX 관점)
- 에고센트릭 인간 데이터가 다관절 손 조작의 "예측 가능한 데이터 소스"가 될 수 있다는 근거. RX가 고객 작업자 착용 카메라로 데이터를 모으는 전략의 학술적 근거다. 54%는 "사전학습 없는 기준선 대비" 조건이며, 상대 향상인지 %p 향상인지는 초록에 없어 본문 확인이 필요하다.
