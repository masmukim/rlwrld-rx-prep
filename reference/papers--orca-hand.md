---
title: "ORCA: An Open-Source, Reliable, Cost-Effective, Anthropomorphic Robotic Hand for Uninterrupted Dexterous Task Learning"
url: https://arxiv.org/abs/2504.04259
publisher: arXiv (IROS 2025 채택)
published: 2025-04-05
fetched: 2026-10-06
tags: [papers, hardware, dexterous-hand, durability, open-source]
source_type: 논문
lang: en
authors: Clemens C. Christoph 외 (ETH Zurich, Katzschmann 그룹)
citations: 미확인
---

## 핵심 사실
- 문제: 고가이고 내구성이 낮은 로봇 손이 장시간 학습 데이터 수집과 연구를 막음
- 방법: 17-DoF 텐던 구동 인체형 손, 팝핑 조인트, 자동 캘리브레이션, 텐션 시스템으로 복잡도를 낮추고 신뢰성 향상. 촉각 센서 통합
- 결과: 재료비 2,000 CHF 미만, 조립 8시간 미만, 10,000회 이상 연속 동작(약 20시간) 무고장
- 오픈소스(설계, 코드, 문서 공개)

## 원문 발췌
> "withstanding more than 10,000 continuous operation cycles - equivalent to approximately 20 hours - without hardware failure"

## 메모 (RX 관점)
- 텐던 구동 손의 신뢰성은 "20시간" 단위로 검증되는 연구 단계다. 제조 현장 가동 시간(일 16~24시간, 수천 시간)과 격차가 있어 PoC 하드웨어 선정 시 내구성 시험 요구사항을 별도로 넣어야 한다.
- 데이터 수집 장시간 운전("Uninterrupted")이 핵심 요구라는 점이 RLWRLD 데이터 파이프라인과 연결됨.
