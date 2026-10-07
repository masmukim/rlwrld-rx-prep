---
title: "HAMLET: Switch your Vision-Language-Action Model into a History-Aware Policy"
url: https://arxiv.org/abs/2510.00695
publisher: arXiv
published: 2025-10
fetched: 2026-10-07
tags: [papers, rldx-1, memory, vla]
source_type: 논문
lang: en
authors: Myungkyu Koo, Daewon Choi 외 (KAIST, Jinwoo Shin은 RLWRLD 소속 병기)
citations: 미확인
---

## 핵심 사실
- 문제: 대부분 VLA는 현재 관측만 보고 행동해 과거 맥락이 필요한 과제에 약함.
- 방법: 시점별 지각 정보를 압축한 moment tokens(시간 대조 학습으로 초기화) + 경량 Transformer 메모리 모듈이 과거 토큰을 요약. RLDX-1 보고서가 Memory Module의 근거로 인용.
- 결과: GR00T N1.5 기반으로 이력 의존 실세계 과제 평균 76.4%, 기준선보다 47.2% 높음(상대/%p 미확인). RoboCasa Kitchen(100 데모 설정) 64.1% → 66.4%, LIBERO 95.6% → 97.6%. 실세계는 과제별 24회 시행.
- 단순 moment 토큰 이어붙이기는 성능이 오르지 않았다고 서술(Moment Concat., Table 5).
- 소속: Jinwoo Shin에 KAIST와 RLWRLD 병기. 독립 검증 아님.

## 원문 발췌
> "on top of GR00T N1.5, HAMLET achieves an average success rate of 76.4% on history-dependent real-world tasks, surpassing the baseline performance by 47.2%." (raw: reference/raw/papers--hamlet-history-vla.txt)
> "We report the success rate (%, over 24 trials per task)" (raw: reference/raw/papers--hamlet-history-vla.txt)

## 메모 (RX 관점)
- RLDX-1 Memory Module의 선행 연구. 기억 모듈이 일반 시뮬 벤치마크에서는 이득이 작고(RoboCasa +2.3, LIBERO +2.0, 원문 표기 기준) 이력 의존 과제에서 크다는 패턴은 RLDX-1 블로그의 설명과 같은 방향이다. 고객 공정에서 "순서·진행 상태 기억이 필요한가"를 묻는 근거.
- 사용: research/rldx1-tech.md (A11).
