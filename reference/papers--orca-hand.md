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
- (2026-10-12 갱신, v2 본문 확인) 내구성 시험 3종은 정의가 서로 다르다: (a) 초록 "10,000회 이상 연속 동작 사이클, 약 20시간, 무고장, 유일한 제약은 실험 시간"; (b) 2.5시간 연속 구동, 4초마다 전 손가락 파지 = 2,250회 파지 사이클, 파손·모터 정지·과도한 텐던 느슨함 없음, 고장이 아니라 자발적 종료; (c) 정책 배치 7시간 17분(약 2,000회 파지), 텐던 느슨함·파단 없음.
- (2026-10-12 갱신) 저자 명시 한계: "장시간 사용에는 성능 유지를 위해 수동 재장력(re-tensioning)이 필요하다." 래칫 스풀로 사용자가 재장력할 수 있게 설계.
- (2026-10-12 갱신) 저자 서술: Shadow Hand는 100,000 CHF 이상이고 상당한 유지보수가 필요하며 독점·고집적 설계라 수리가 어렵다.

## 원문 발췌
> "withstanding more than 10,000 continuous operation cycles - equivalent to approximately 20 hours - without hardware failure"
> "The hand successfully completed 2,250 grasping cycles without breakage, motor shutdown, or excessive tendon slack ... The experiment was ended voluntarily after 2.5 hours, not due to failure." (raw: reference/raw/papers--orca-hand-v2.txt)
> "Prolonged use requires manual re-tensioning to maintain performance." (raw: reference/raw/papers--orca-hand-v2.txt)

## 메모 (RX 관점)
- 텐던 구동 손의 신뢰성은 "20시간" 단위로 검증되는 연구 단계다. 제조 현장 가동 시간(일 16~24시간, 수천 시간)과 격차가 있어 PoC 하드웨어 선정 시 내구성 시험 요구사항을 별도로 넣어야 한다.
- 데이터 수집 장시간 운전("Uninterrupted")이 핵심 요구라는 점이 RLWRLD 데이터 파이프라인과 연결됨.
- 같은 논문 안에서 "10,000 사이클 = 약 20시간"(시간당 500회)과 "2,250 사이클 = 2.5시간"(시간당 900회)의 사이클 정의가 맞지 않는다(계산). 사이클 수는 정의가 다른 숫자라 소스끼리 직접 비교할 수 없다 (Q7).
