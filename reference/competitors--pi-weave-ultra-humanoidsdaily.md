---
title: The API-fication of Robotics: Physical Intelligence Unveils Real-World Performance Data with Weave and Ultra
url: https://www.humanoidsdaily.com/news/the-api-fication-of-robotics-physical-intelligence-unveils-real-world-performance-data-with-weave-and-ultra
publisher: Humanoids Daily
published: unknown (본문: Physical Intelligence가 2026-02-24 기술 업데이트 공개. 기사 게시일은 원문에 없음)
fetched: 2026-10-07
tags: [competitors, physical-intelligence, weave, ultra]
source_type: 기사
lang: en
---

## 핵심 사실
- Physical Intelligence(PI)가 2026-02-24 기술 업데이트로, 제3자 하드웨어 위에서 π 모델을 "intelligence layer"로 쓰는 실제 배포 데이터를 Weave Robotics(가정용 로봇)와 Ultra(산업 자동화)에 대해 공개했다고 기사가 서술.
- Weave: 샌프란시스코 빨래방 라이브 배포. π0.5 → π0.6 전환으로 "전체 시간 대비 자율 비율"이 증가. Weave 데이터를 사전학습에 넣으면(+WPT) 놓친 파지 시퀀스가 42% 감소, 세탁물 한 판당 사람 텔레오퍼레이터 개입이 50% 감소. 평균 한 판을 30~90분에 갬(티셔츠, 바지, 수건). 수치의 출처는 PI가 공개한 데이터(기사 인용)이며 회사 주장.
- Ultra: 이커머스 포장용 산업 AI 로봇 회사. 기존 워크스테이션에 들어가도록 설계, 변형 가능한 우편 봉투와 바뀌는 품목 같은 롱테일 포장을 다룸. Ultra 전용 사전학습 데이터(+UPT)로 미세조정하면 포장 처리량(시간당 품목)이 크게 증가했다고 서술(수치 없음).
- 기사 말미 회사 소개: Ultra Robotics의 OP1은 고정형 양팔 AI 로봇으로 주문 포장, 분류, 키팅, 반품 처리를 자동화(미국 창고).
- 이 기사 원문에는 Telexistence 언급이 없다.

## 원문 발췌
> Human teleoperator interventions per full laundry load dropped by 50% when the model was trained on specialized data.
> Through a partnership with Ultra, Physical Intelligence's π0.6 model is being used to automate complex, 'long tail' e-commerce order packaging in live warehouse environments.
(raw: reference/raw/competitors--pi-weave-ultra-humanoidsdaily.txt)

## 메모
- Q4(case/candidates.md Q4.1 행 16)의 출처. 기존 출처는 research/skild-pi-deep-dive.md 2.2절이었으나 2026-10-09 fact-check에서 Telexistence 파트너 언급이 이 기사 원문에 없음이 확인돼 정정.
- 하드웨어와 현장은 파트너 소유이고 PI는 모델 공급자라는 구조는 기사 서술(plug-and-play intelligence layer)에서 도출.
