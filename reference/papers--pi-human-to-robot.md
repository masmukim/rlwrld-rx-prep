---
title: Emergence of Human to Robot Transfer in Vision-Language-Action Models
url: https://arxiv.org/abs/2512.22414
publisher: arXiv (Physical Intelligence, Georgia Tech)
published: 2025-12-27
fetched: 2026-10-17
tags: [papers, physical-intelligence, egocentric, human-video, data]
source_type: 논문
lang: en
authors: Simar Kareer, Karl Pertsch 외 (Physical Intelligence; Judy Hoffman, Danfei Xu: Georgia Tech)
citations: 미확인
---

## 핵심 사실
- 문제: VLA가 인간 영상(행동 라벨 없는 것)에서 기술을 배울 수 있는가. 명시적 정렬 없이 단순 공동 학습만으로 되는가.
- 방법: π0.5에 머리 장착 카메라 에고센트릭 인간 데이터를 공동 학습(π0.5+ego). 시각 SLAM으로 머리 6D 운동과 양손 17개 3D 키포인트를 복원해 행동으로 사용(인간 행동 18차원). 그리퍼 개폐는 추정이 어려워 인간 데이터에서 근사하지 않고 로봇 데이터로만 학습. 인간 영상에도 텍스트 하위작업 주석.
- 인간 데이터 규모: 작업별 3시간(정리, 향신료, 서랍장), 5시간(달걀 분류). 합 14시간. 저자도 "we ultimately only use 10s of hours of human data".
- 결과(작업 점수): 향신료 32→71%, 서랍장 25→50%, 정리 53→63%, 달걀 분류 정확도 57→78%. 모두 인간 데이터에만 있는 장면·물체·작업 일반화를 겨냥한 평가. 그림 요약은 "nearly double the score on the target tasks".
- 핵심 조건: 로봇 사전학습의 다양성(장면×작업 조합 비율 0/25/50/75/100%, 100%+타 구현체)이 충분해야 인간 데이터 전이가 나타남. 0~25%에서는 이득이 없음. 다양성이 커질수록 인간·로봇 표현 임베딩이 겹침(TSNE 분석).
- 한계: 인간 데이터만으로 하위 정책을 학습하면 명령을 정확히 따르지 못하는 실패 모드. 인간 데이터 수집은 에피소드 방식. 저자는 수동적 대규모 인간 데이터는 "additional work"가 필요하다고 서술.

## 원문 발췌
> we ultimately only use 10s of hours of human data, and this data is collected in an episodic manner (raw: reference/raw/papers--pi-human-to-robot.txt, 217행)
> We find that with limited pretraining diversity, VLAs fail to transfer knowledge from human data, but as pretraining diversity grows past a critical threshold, transfer emerges. (raw: 같은 파일, 217행)

## 메모 (RX 관점)
- "PI는 로봇 데이터만, Skild는 인간 영상" 이분법의 반례. PI도 인간 에고센트릭 데이터를 쓰지만 규모는 수십 시간이고 "대규모 로봇 사전학습이 선행 조건"이라는 방향이다. EgoScale(20,854시간, 인간 영상이 사전학습 본체)과 대비.
- 평가 대상은 소수 작업·한정된 로봇(ARX 계열)이다. 점수 표기는 작업 점수이며 시행 수는 이번에 확인하지 못함.
