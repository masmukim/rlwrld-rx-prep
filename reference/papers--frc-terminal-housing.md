---
title: Automated Terminal-to-Housing Assembly System for Flat Ribbon Cable Harness
url: https://arxiv.org/abs/2608.06996
publisher: arXiv (IEEE 투고, 심사 전)
published: 2026-08-07 (v1)
fetched: 2026-10-06
tags: [papers, wire-harness, terminal-insertion, korea, automation]
source_type: 논문
lang: en
authors: Eunkyu Choi 외 (Joonho Seo, Seungmin Lee, Seokhwan Jeong; 서강대 기계공학과). 대하전선(DAEHA CABLE CO., LTD.)과 한국연구재단 지원
citations: 미확인 (최신)
---

## 핵심 사실
- 하네스 상류 공정(탈피, 절단, 단자 압착)은 이미 널리 자동화됐고, 단자-하우징 조립이 하네스 생산의 주요 병목이라고 서술.
- 낱선 하네스(DWH)는 전선이 분리돼 단자를 하나씩 정렬·삽입할 수 있어 단일 단자 삽입 자동화가 산업에 도입됐다. 반면 평판 리본 케이블 하네스(FRCH)는 단자가 리본으로 묶여 있어 실무에서 여전히 수작업 의존.
- 방법: 비전·능동 힘 센싱 없이 기구만으로(Cable Alignment, Lean & Slide, Weaving, Clamping) 6핀 하우징 2종에 삽입. Lean & Slide는 사람의 수작업 동작을 본뜸.
- 결과: 80회 시행 종단 성공률 83.75%(전반 85.0%, 후반 82.5%). 사이클 33초(절반 속도 운전). 비교용 평행 접근(Parallel Approach)은 3/20(15%).
- 한계: 실험실 규모 검증.

## 원문 발췌
> "Several upstream manufacturing processes, such as wire stripping, cutting, and terminal crimping, have already been widely automated. However, the terminal-housing assembly step remains a major bottleneck in wire harness production"
> "This structural independence has made single-terminal insertion a practical automation strategy and has supported its industrial adoption."
> "achieved an 83.75% end-to-end process success rate over 80 trials ... The cycle time was 33 s under half-speed operation."
(raw: reference/raw/papers--frc-terminal-housing.txt)

## 메모 (RX 관점)
- B2: 국내 하네스 기업(대하전선)이 조립 자동화 연구를 지원한다는 국내 수요 정황. 하네스 종류(평판 리본, 전자·산업용 추정)가 자동차 낱선 하네스와 다르다.
- "단일 단자 삽입은 산업 도입" 서술은 Cellios 기사("배선과 단자 삽입이 가장 어렵다")와 결이 다르다. 단순 리드선의 단일 삽입 장비는 있지만 다커넥터 하네스의 프리블록·레이업은 수작업이라는 식으로 둘을 함께 쓴다(본 팀 해석).
- 전용 기구가 센서 없이 83.75%를 냈다는 점은 "품종이 고정되면 RFM 없이도 된다"는 반대 논거다.
