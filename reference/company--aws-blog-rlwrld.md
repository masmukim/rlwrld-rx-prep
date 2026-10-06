---
title: Putting Dexterous Robots to Work: How RLWRLD Builds Physical AI with AWS
url: https://aws.amazon.com/blogs/physical-ai/putting-dexterous-robots-to-work-how-rlwrld-builds-physical-ai-with-aws/
publisher: AWS Physical AI Blog
published: 2026-06-22
fetched: 2026-10-06
tags: [company, rldx-1, data]
source_type: 공식문서
lang: en
---

## 핵심 사실
- 학습 인프라: EC2 p5e/p5en(H200), 시뮬레이션 g6e(L40S), ParallelCluster(Slurm), S3, FSx for Lustre.
- 수백 TB 규모 실세계 로봇 데이터 파이프라인. 유사 프런티어 모델 대비 약 20% 컴퓨트로 SOTA 주장(회사 주장).
- 데이터: 현장 텔레오퍼레이션 + 멀티카메라/에고센트릭 영상 + 합성 로봇/손 데이터. 직원이 머리, 가슴, 손에 카메라를 착용.
- 고객/파트너: LOTTE HOTEL & RESORT(다년 데이터 파트너십, 40+ 직무군 평가: 식음, 연회, 하우스키핑), CJ Group(물류), Lawson(일본 리테일), 글로벌 자동차 제조사(조립).
- 성능: SIMPLER Google-VM 81.5%, RoboCasa GR-1 Tabletop 58.7%.
- 설립 2024, RLDX-1 런칭 2026-05, 롯데 도입 목표 2030.

## 원문 발췌
> "8.1B-parameter, open-source foundation model" (AWS 블로그 표현)

## 메모
- 롯데 목표: AWS는 2030, R&D World는 2029. 로봇신문은 "청소·백오피스 2029 도입, 2030 전 지점 확산"으로 둘을 모두 설명 -> 단계로 서술.
