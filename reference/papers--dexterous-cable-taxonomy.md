---
title: "Dexterous Cable Manipulation: Taxonomy, Multi-Fingered Hand Design, and Long-Horizon Manipulation"
url: https://arxiv.org/abs/2502.00396
publisher: arXiv
published: 2025-02 (v2 2025-02-06)
fetched: 2026-10-06
tags: [papers, deformable, dexterous-hand, cable, wire-harness]
source_type: 논문
lang: en
authors: Sun Zhaole 외 (Xiao Gao, Xiaofeng Mao, Jihong Zhu, Aude Billard, Robert B. Fisher; University of Edinburgh, EPFL, University of York)
citations: 미확인
---

## 핵심 사실
- 문제: 기존 케이블 조작 연구는 2지 그리퍼에 의존해, 사람처럼 케이블을 쥐고 손 안에서 옮기고 U자로 구부려 거는 동작을 하기 어렵다. 2지 그리퍼는 "쥐고 놓기"만 가능하다고 저자는 본다.
- 방법: 케이블 조작 분류 체계(taxonomy)를 만들고, 엄지-검지 협조가 핵심이라는 분석에서 엄지-검지 쌍을 대칭으로 2개 둔 25-DoF 5지 손을 설계. 프리미티브를 시연으로 수집하고 유한상태기계(FSM)로 장기 작업을 구성.
- 결과: 프리미티브 8개, 프리미티브당 시연 1개로 같은 재질·다른 굵기 케이블 3종에서 시연 재생 성공률 88%, 재질·강성이 매우 다른 케이블 3종에서 75% 이상. 장기 작업 4개에서 64%. 사람 기준선과 비슷한 수준이라고 주장.
- 한계(저자): 프리미티브 전환을 사람이 안내한다(human-guided transitions). 손이 고정돼 있어 매듭처럼 팔 이동이 필요한 작업은 못 한다. 장기 작업은 1회 30초 이상이라 오차가 누적된다.
- 데이터 수집: 모션 캡처나 텔레오퍼레이션은 다중 접촉과 촉각 피드백이 필요한 케이블 손 조작에는 "거의 불가능"하다고 서술하고 별도 시연 수집 파이프라인을 만들었다.

## 원문 발췌
> "Existing research that addressed cable manipulation relied on two-fingered grippers, which make it difficult to perform similar cable manipulation tasks that humans perform."
> "This taxonomy revealed that coordination between the thumb and the index finger is critical for cable manipulation"
> "these methods, requiring motion capture or teleoperation, are almost impossible to use for dexterous cable manipulation, which is a multi-contact problem and requires intensive haptic feedback."
(raw: reference/raw/papers--dexterous-cable-taxonomy.txt)

## 메모 (RX 관점)
- B2: 하네스 레이업(전선 잡고 훑기, 걸기, 당기기)에서 "왜 그리퍼가 아니라 손인가"의 근거. 동시에 "엄지 1개인 사람형 손은 케이블 작업에 제약이 있다"는 주장이라 상용 사람형 손(DG-5F-S 등) 선택의 리스크 근거이기도 하다.
- 손 텔레오퍼레이션이 케이블 작업에서 어렵다는 서술은 데이터 계획(에고센트릭 인간 시연 + 리타게팅 우선)의 근거.
- 성공률은 시연 "재생"이고 학습 정책이 아니다. 시행 수와 조건은 본문 표 확인 전이므로 정성 근거로 쓴다.
