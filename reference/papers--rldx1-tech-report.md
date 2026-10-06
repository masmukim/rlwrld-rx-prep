---
title: RLDX-1 Technical Report
url: https://arxiv.org/abs/2605.03269
publisher: arXiv
published: 2026-05-05
fetched: 2026-10-06
tags: [papers, rldx-1, vla, dexterous]
source_type: 논문
lang: en
authors: Dongyoung Kim 외 (총 68명, 소속은 초록 페이지에 미표기)
citations: 미확인
---

## 핵심 사실
- 문제: 실세계 정교 조작(dexterous manipulation)에서 기존 VLA가 놓치는 기능(동작 인지, 장기 기억, 물리 센싱)을 통합.
- 방법: MM-DiT를 행동 모델링으로 확장한 MSAT. 모달리티별 스트림 + cross-modal joint self-attention. 합성 증강 학습 파이프라인과 실시간 추론 스택.
- 결과: ALLEX 휴머노이드 작업 성공률 86.8% vs π0.5와 GR00T N1.6 약 40%. 시뮬레이션 벤치마크에서도 우위(공식 페이지 수치 참조).
- v1 2026-05-05, v2 2026-05-06 제출. 저자 68명.
- 한계: 이번 조사에서는 본문을 읽지 않음(초록과 요약 수준).

## 원문 발췌
> motion awareness, long-term memory, and physical sensing (초록 요지)

## 메모 (RX 관점)
- 접촉이 많은 조작(삽입, 계란 집기 등)과 기억 의존 작업이 강점이라는 점을 고객 공정의 "손 작업" 선별 기준으로 활용 가능. 비교 기준은 자사 선택 작업이므로 PoC에서 고객 공정으로 재검증 필요.
