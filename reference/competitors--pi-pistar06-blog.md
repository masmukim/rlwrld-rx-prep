---
title: "π*0.6: a VLA that Learns from Experience (PI 블로그)"
url: https://www.pi.website/blog/pistar06
publisher: Physical Intelligence (공식 블로그)
published: 2025-11-17
fetched: 2026-10-17
tags: [competitors, physical-intelligence, recap, data-flywheel]
source_type: 1차
lang: en
---

## 핵심 사실
- 학습 3단계 비유: 지시(시연으로 기본 학습), 코칭(전문가 텔레오퍼레이션 교정), 연습(강화학습). 시연만 쓰는 현 방식은 "성공 반쯤 만들기는 쉬우나 매번 성공은 어렵다"고 서술.
- 교정(coaching): 최선의 현 정책을 돌리다 실수 때 사람이 텔레오퍼레이션으로 "taking over". 정책이 실제로 빠지는 상황에 대한 감독을 얻는다. 한계도 명시: 교정의 질은 사람이 개입 시점을 알아채고 고품질 교정을 주는 능력에 묶임.
- 본문 요약: 에스프레소(오전 5:30~오후 11:30 중단 없이), 새 가정에서 낯선 세탁물 50종 접기, 실제 공장에서 초콜릿 포장 상자 59개 조립·라벨링(영상 서술).
- 전망(결론부): 시연으로 만든 데이터는 사람 노력이 들고 사람 수준으로 속도·견고성이 제한됨. 배치 로봇이 늘면 "learning from experience might become a significant source of training data". 시연은 새 행동 정의, 코칭은 전략 정교화, 자율 경험은 "potentially the largest source of data".
- 협업 모집: "We are particularly excited to work with companies scaling up data collection with robots deployed for real-world applications, who are looking to collaborate on autonomy."

## 원문 발췌
> Today, robotic foundation models primarily use demonstration data that is collected manually by people (e.g., teleoperation). (raw: reference/raw/competitors--pi-pistar06-blog.txt, 437행)
> autonomous experience – potentially the largest source of data – will serve to perfect the behaviors (raw: 같은 파일, 437행)

## 메모
- 논문(reference/papers--pistar06-recap.md)의 수치는 논문 본문 기준. 블로그의 "59 boxes" 등은 영상 서술이라 수치 근거로는 약함.
- PI도 "배치 로봇의 경험을 데이터원으로" 본다는 1차 근거. Skild의 Physical RSI와 수렴하는 지점이다.
