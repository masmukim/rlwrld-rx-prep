---
title: The Reindustrial Revolution: Partnering with ABB Robotics, Universal Robots, and NVIDIA
url: https://www.skild.ai/blogs/reindustrial-revolution
publisher: Skild AI (공식 블로그)
published: 2026-03-19
fetched: 2026-10-06
tags: [competitors, skild, partnerships]
source_type: 1차
lang: en
---

## 핵심 사실
- ABB Robotics, Universal Robots(UR)의 로봇 포트폴리오에 Skild Brain의 "shared intelligence layer"를 내장하는 방식. 작업별 코드 없이 다양한 로봇 지원이 목표.
- NVIDIA: Isaac Lab, Isaac Sim, Cosmos 기반 사전학습 협력. Foxconn과 NVIDIA Blackwell GPU 생산 라인에 배치.
- Foxconn 라인 적용: 양팔 로봇이 pick-and-place, 연속 나사 16개 체결 등 복합 조립 수행.
- 하드웨어 전략: 산업용 로봇 OEM 파트너십 중심, "any robot, any task, one brain".
- 데이터: 배치된 로봇에서 나오는 "data flywheel", 인터넷 규모 인간 영상과 대규모 시뮬레이션으로 사전학습. 반구조화(공장) -> 덜 구조화(병원, 호텔) -> 비구조화 환경으로 단계 확장.
- 수치는 블로그에 없음.

- (2026-10-09 원문 대조 추가) OEM 파트너로 ABB Robotics, Teradyne Robotics의 Universal Robots(UR), Mobile Industrial Robots(MiR)를 서두에 나열. 다만 본문의 통합 서술은 ABB와 UR에만 있고 목표 문구("our goal is to integrate")다. MiR은 이름만 언급돼 탑재 내용은 확인되지 않음.
- (2026-10-09 원문 대조 추가) Foxconn 라인 작업: 양팔 로봇이 busbar를 집어 놓고, limit block을 놓은 뒤, 나사 16개를 연속 체결하고, limit block을 제거. 이 작업은 현재 Foxconn 공장 라인에서 사람이 하는 것이라고 Skild가 설명. 표현은 "we will ship ... to control dual robotic arms on NVIDIA's Blackwell GPU production lines".

## 원문 발췌
> embedding the Skild Brain's shared intelligence layer into widely deployed industrial robots (WebFetch 요약의 인용)
> The robot needs to pick and place a busbar, followed by a limit block, then drill 16 screws in succession, and finally remove the limit block. This is a real task, currently done by humans at a line in a Foxconn factory.
> partnering with major robotics OEMs (original equipment manufacturers): ABB Robotics, Teradyne Robotics' Universal Robots (UR) and Mobile Industrial Robots (MiR).
(raw: reference/raw/competitors--skild-reindustrial.txt)

## 메모
- 그리퍼·팔 중심 작업 사례(나사 체결)이며 고자유도 손 사례는 확인되지 않음.
- SoftBank가 ABB 로보틱스 부문 인수에 합의했다는 내용은 검색 요약에서만 확인(원문 미열람).
