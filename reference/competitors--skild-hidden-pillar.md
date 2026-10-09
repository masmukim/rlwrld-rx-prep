---
title: The Hidden Pillar of Robotics
url: https://www.skild.ai/blogs/skild-crosses-100m-arr
publisher: Skild AI (공식 블로그)
published: 2026-09-10 (블로그 목록 표기. Securities.io는 9월 9일로 보도)
fetched: 2026-10-09
tags: [competitors, skild, sumitomo, deployment]
source_type: 1차
lang: en
---

## 핵심 사실
- 10개월간 유료 고객 60곳 이상. Mobility가 매출의 10%(그중 AMR 솔루션 4%), 나머지 약 90%는 주로 조작(manipulation) 작업. ARR 1억 달러 돌파, 배포 시작 후 10개월간 이미 인식된 매출 5,000만 달러 (회사 발표).
- Foxconn·NVIDIA: 양팔(dual-arm) 매니퓰레이터에 Skild Brain을 배치해 NVIDIA Blackwell 시스템을 고정밀 조립.
- **Sumitomo Wiring Systems: "we are working towards deploying S1 to automate processes in wire harness manufacturing that were considered 'impossible' to automate."** 즉 S1 배치를 향해 가는 단계이며 "배치 완료"가 아니다. 공정 이름, 로봇 형태, 성과는 쓰여 있지 않다.
- Mitsui: 단체급식 주방에서 S1 기반 범용 로봇을 시범 운영(piloting).
- 교훈 서술: 속도 대 정확도 (정확도 99.9%라도 10배 느리면 배포 불가), 변화 적응 (새 데이터셋과 post-training을 매번 하면 확장 불가) → S1에 집중.

## 원문 발췌
> At Sumitomo Wiring Systems, we are working towards deploying S1 to automate processes in wire harness manufacturing that were considered “impossible” to automate. (raw: reference/raw/competitors--skild-hidden-pillar.txt, 16행)
> A robot that is 99.9% accurate but ten times too slow is not almost deployable. It’s not deployable. (raw: 같은 파일, 52행)

## 메모
- 이 블로그에 "wire harness"가 나오는 곳은 이 한 문장뿐이다. 앞서 skild-pi-deep-dive가 인용한 humanoidsdaily 기사(고객 목록에 올림)는 이 문장을 "자동화하고 있다(Automating)"로 풀었다. 1차 소스의 시제는 "working towards deploying"이다.
