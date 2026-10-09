---
title: "Introducing S1: In-Context Learning for Robotics"
url: https://www.skild.ai/blogs/s1
publisher: Skild AI (공식 블로그)
published: 2026-08-18 (블로그 목록 표기)
fetched: 2026-10-09
tags: [competitors, skild, s1, in-context-learning]
source_type: 1차
lang: en
---

## 핵심 사실
- S1은 과제를 언어가 아니라 **영상 시연 1개**로 지정받는 in-context learner. 가중치 갱신 없이 사전학습에 없던 장기 과제(최대 10분)를 수행한다고 주장.
- 평가: 내부 벤치마크 2종 (사전학습 분포 내 과제, 처음 보는 과제). 과제 길이 4~8분. 지표는 **누적 단계별 성공률의 평균**. 모든 단계를 채점하기 위해 **실패 시 사람이 개입해 복구**했고, 개입은 주로 VLA 기준선에 쓰였다 (안 쓰면 기준선은 0점).
- 사전학습 10만 시간 데이터에서 처음 보는 과제 성공률: ICL 66% 대 언어 프롬프트 VLA 9%. 시연 1개가 약 380개 post-training 시연과 동급(보간 추정). 380개 수집에 텔레오퍼레이션 50~100시간. 시연 2,000개로 post-training하면 86%. 사전학습에 있던 과제는 ICL 약 96%.
- 시연 과제 예: plant potting, pancake cooking, pour-over coffee, **kit assembly**. 하네스 과제는 없다.
- 하드웨어: 본문 텍스트에 그리퍼·다관절 손·로봇 모델명 언급 없음. 로버스트니스 시험 L5가 "반대쪽 팔로 절반의 동작을 수행"이라고 쓰여, 평가 로봇이 **팔이 둘 이상**임을 시사한다 (그림·영상은 텍스트로 추출되지 않아 end-effector 형태는 미확인).
- 데이터 출처: 텔레오퍼레이션(하드웨어에 가장 가깝고 확장성 최악), 에고센트릭 영상(확장성 최고, 도메인 격차 최대) 등을 모두 키운다고 서술.

## 원문 발췌
> To ensure all steps are graded cumulatively, we use human intervention to recover from failures during policy rollouts. (raw: reference/raw/competitors--skild-s1-blog.txt, 232행)
> A single demonstration in context is worth roughly 380 post-training examples (the exact crossing was estimated by interpolating between measured points). (raw: 같은 파일, 328행)

## 메모
- 66%는 하네스 성능이 아니다. 일반 장기 과제의 내부 벤치마크 값이고 사람 개입이 포함된 누적 단계 점수다.
