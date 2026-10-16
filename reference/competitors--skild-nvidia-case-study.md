---
title: Skild AI Builds Omni-Bodied Robot Brain With NVIDIA (NVIDIA 고객 사례)
url: https://www.nvidia.com/en-eu/case-studies/skild-ai/
publisher: NVIDIA (고객 사례 페이지, 공급사 마케팅 문서)
published: unknown (페이지에 날짜 없음)
fetched: 2026-10-17
tags: [competitors, skild, nvidia, simulation, human-video]
source_type: 1차
lang: en
---

## 핵심 사실
- 데이터 부족 서술: 실로봇 수집은 고품질 시연 1건에 몇 분이 걸리나 AI에는 수십억 건이 필요하다고 기술.
- 두 대체 출처: (1) 물리 기반 합성 데이터(Isaac Lab, Omniverse), (2) 인터넷 인간 영상. 시뮬레이션은 "thousands of robot instances across multiple embodiments"를 수천 환경에 복제, "billions of training examples"를 생성한다고 서술.
- Cosmos Transfer로 조명·환경 변이를 프롬프트로 증강. 실패 시나리오를 안전하게 다량 경험시킨다는 점을 강조("robots have countless ways to fail compared to the limited ways they can succeed").
- 인간 영상: 인터넷의 수조 건 영상에서 "affordances"(물체를 어떻게 조작해야 하는지)를 추출. "treating humans as biological robots".
- 성과 주장: 피츠버그에서 휴머노이드가 "60%–80% task performance within hours of data collection". 작업 정의, 시행 수, 성공 기준은 없음(회사·공급사 주장).
- 이 문서는 NVIDIA의 사례 소개로, 두 회사 홍보 성격이다.

## 원문 발췌
> To overcome the data shortage, Skild AI leverages two alternative data sources: physics-based synthetic data generation and human videos from the internet. (raw: reference/raw/competitors--skild-nvidia-case-study.txt, 56행)
> achieving 60%–80% task performance within hours of data collection (raw: 같은 파일, 86행)

## 메모
- 60~80%는 작업 정의가 없어 다른 수치와 비교 불가. T2에서는 "주장"으로만 인용.
- 같은 NVIDIA의 S1 블로그(reference/raw/competitors--skild-s1-nvidia.txt)는 "simulation, human video, teleoperation and, where permitted, deployment data"를 학습 데이터로 열거. 배치 데이터에는 "where permitted" 조건이 붙는다.
