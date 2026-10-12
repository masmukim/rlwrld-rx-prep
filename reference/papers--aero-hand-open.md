---
title: "Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning"
url: https://arxiv.org/abs/2608.28578
publisher: arXiv (cs.RO)
published: 2026-08
fetched: 2026-10-12
tags: [papers, hardware, dexterous-hand, tendon, durability]
source_type: 논문
lang: en
authors: Nan Wang 외 (Chestnut Robotics, Caltech)
citations: 미확인
---

## 핵심 사실
- 7개 서보로 구동하는 3D 프린트 텐던 구동 손(374 g). 설계·펌웨어·제어를 전부 공개하여 마모·파손 부품은 재주문이 아니라 재출력으로 교체한다. BOM의 약 2/3가 서보 7개(208.81 USD).
- 내구성(저자 시험): 손 전체를 완전 개방-완전 폐쇄로 순환시켜 케이블 파손이나 가동 범위 손실 없이 400,000 풀 액추에이션 사이클 이상. 공칭 1.2 Hz에서 90시간 이상의 연속 관절 구동에 해당(계산 일치).
- 케이블 인장 강도 약 680 N, 시험 최악 장력 약 66 N의 약 10배 여유.
- 사양: 5지, 구동 7 DoF, 질량 374 g, 가격 314 USD(논문 Table 1, v2 2026-09-23 기준).
- 한계: 시험은 완전 개방-완전 폐쇄 순환이며 파지 하중 조건은 언급이 없다. 90시간은 현장 가동 수천 시간에 비해 작다(계산: 2교대 연 약 3,700시간의 약 2.4%).

## 원문 발췌
> "the transmission survives more than 400,000 full-actuation cycles without cable failure or loss of range, which at the nominal 1.2 Hz cycle rate corresponds to over 90 h of continuous articulation." (raw: reference/raw/papers--aero-hand-open.txt)

## 메모 (RX 관점)
- 텐던(케이블) 자체는 40만 사이클을 견딘다는 실험실 수치. 구동 7 DoF 저가 손이라 20-DoF 상용 손과 같은 범주가 아니다. 현장 수명은 케이블보다 풀리, 모터, 피부 패드, 충격 같은 다른 요소가 정한다는 점을 보여주는 비교 참고치.
