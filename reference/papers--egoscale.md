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

## 본문 확인 (2026-10-17 추가, 본문 HTML 원문 Grep, raw: reference/raw/papers--egoscale.txt)
- 1단계 사전학습 데이터 20,854시간: 대부분 야외 일상 에고센트릭 녹화(가정, 산업, 소매, 교육 환경, 9,869 장면, 6,015 작업, 43,237 물체). 정확한 손 추적이 있는 EgoDex(Apple Vision Pro) 829시간 추가. 저자는 비제약 수집이라 노이즈가 크다고 서술.
- 2단계 정렬 중간학습 데이터: 344개 탁상 작업, 인간 약 50시간 + 텔레오퍼레이션 로봇 약 4시간. 인간 쪽은 로봇과 같은 카메라 구성과 같은 모캡(Vive 트래커 + Manus 장갑)으로 수집. 저자는 이 소량 정렬 데이터가 결정적이라고 서술.
- 학습: 1단계 100K 스텝, 256 GB200 GPU, 배치 8,192.
- 인간 손은 21 키포인트를 로봇 손 관절 공간으로 최적화 기반 리타게팅. 손 자유도 22-DoF(Sharpa) 로봇은 Galaxea R1Pro.
- 수치: 초록 "improves average success rate by 54% over a no-pretraining baseline", 본문 "improving average task completion by over 55%"(완료 점수). 상대/%p 구분은 본문 서술만으로 확정되지 않음(표 절대값 미확인). Unitree G1 3지 손은 "over 30% absolute improvement".
- 한계: 사전학습만으로는 부족하고 소량의 정렬된 인간-로봇 데이터가 필요.

## 메모 (RX 관점)
- 에고센트릭 인간 데이터가 다관절 손 조작의 "예측 가능한 데이터 소스"가 될 수 있다는 근거. RX가 고객 작업자 착용 카메라로 데이터를 모으는 전략의 학술적 근거다. 54%는 "사전학습 없는 기준선 대비" 조건이며, 상대 향상인지 %p 향상인지는 초록에 없어 본문 확인이 필요하다.
