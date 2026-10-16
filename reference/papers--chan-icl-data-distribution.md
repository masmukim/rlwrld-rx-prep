---
title: "Data Distributional Properties Drive Emergent In-Context Learning in Transformers"
url: https://arxiv.org/abs/2205.05055
publisher: arXiv (DeepMind, NeurIPS 2022)
published: 2022-05
fetched: 2026-10-17
tags: [papers, in-context-learning, data]
source_type: 논문
lang: en
authors: Stephanie C.Y. Chan 외 (DeepMind)
citations: 미조회
---

## 핵심 사실
- 주장: in-context learning은 학습 데이터의 분포 특성(burstiness: 항목이 몰려서 나타남, 드물게 나오는 클래스가 많음, 의미가 동적임)이 있을 때 나타난다. 균등 i.i.d. 분포로는 잘 안 나타난다.
- 구조와의 관계: 자연스러운 데이터 분포로는 트랜스포머에서만 in-context learning이 유도되고 순환(recurrent) 모델에서는 유도되지 않았다. 즉 구조와 데이터 특성이 함께 작동한다.
- 범위: 언어가 아니라 Omniglot(1,623개 문자 클래스, 클래스당 손글씨 20개) 이미지-라벨 few-shot 시퀀스의 통제 실험이다(본문 확인: raw 249-253행). 언어모델 직접 실험이 아니다.

## 원문 발췌
> In-context learning emerges when the training data exhibits particular distributional properties such as burstiness ... and having large numbers of rarely occurring classes. (raw: reference/raw/papers--t1-chan-icl-data.txt, 26-29행)
> naturalistic data distributions were only able to elicit in-context learning in transformers, and not in recurrent models. (같은 파일, 39-42행)

## 메모
- T1에서 "구조는 필요조건이되 충분조건이 아니고 데이터 분포가 같이 필요하다"를 직접 지지하는 소규모 통제 실험 증거(초록 수준 확인, 실험 설정은 확인필요).
