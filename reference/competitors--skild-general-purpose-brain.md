---
title: Building the general-purpose robotic brain
url: https://www.skild.ai/blogs/building-the-general-purpose-robotic-brain
publisher: Skild AI (공식 블로그)
published: 2025-07-29
fetched: 2026-10-17
tags: [competitors, skild, data-strategy, omni-bodied]
source_type: 1차
lang: en
---

## 핵심 사실
- 모델 정의: 사족보행, 휴머노이드, 탁상 팔, 모바일 매니퓰레이터 등 여러 형태에서 동작하는 "omni-bodied" 모델. 사람 데이터도 포함해 학습한다("humans are also a form of robot"). 형태 다양성이 학습 데이터를 늘리고 하드웨어 변화·고장에 견고하다고 주장.
- 구조: 저주파 상위 조작·이동 정책 + 고주파 하위 정책(관절 각도와 모터 토크로 변환)의 계층 구조. 배포용으로 미세조정·증류.
- 데이터 철학: 로봇 대규모 데이터가 없고, 하드웨어로 실데이터를 모으는 것은 느리고 비싸다. 경쟁자들이 기존 VLM에 "less than 1% of real-world robot data"를 얹는 방식을 취한다고 비판(회사명은 지목하지 않음). 이런 모델은 의미적 일반화는 보이나 "행동 정보"가 없다고 주장.
- 규모 주장: "scale does not mean million or billion examples, achieving scale requires collecting trillions of examples - and there is no way just real world data can achieve this scale in near future". 각주: 지구 전 인구가 데이터를 모아도 100조 궤적까지 수년 걸린다는 개략 계산.
- 방법: "large-scale simulation and internet video data to pre-train", 이후 "post-train this foundation model using targeted real-world data".
- 이 글은 2024년 성과를 먼저 공개한다고 쓰며 수치 데이터(시간, 건수)는 없음.

## 원문 발췌
> start with an existing vision-and-language model (VLM) and sprinkle in less than 1% of real-world robot data to build a "robotics foundation model" (raw: reference/raw/competitors--skild-general-purpose-brain.txt, 23행)
> At Skild AI, we tackle this challenge through large-scale simulation and internet video data to pre-train our omni-bodied brain. We post-train this foundation model using targeted real-world data to deliver working solutions to our customers. (raw: 같은 파일, 25행)

## 메모
- 공개 2025-07-29는 S1(2026-08) 이전이다. 이후 글(S1, Physical Self-Play)은 사전학습 출처에 "gloves, teleoperation"을 추가해 서술하므로 시점별로 출처 목록이 늘어난 것으로 읽힌다(해석).
- "<1% 실로봇 데이터" 비판의 대상은 명시되지 않았다. PI를 지목한 글이 아니다. T2에서는 대조 근거로 쓰되 PI 자체 논문의 수치와 충돌하는지 구분한다.
