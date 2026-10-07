---
title: AI-based Framework for Robust Model-Based Connector Mating in Robotic Wire Harness Installation
url: https://arxiv.org/abs/2503.09409
publisher: arXiv
published: 2025-03-12 (v2 2025-06-09)
fetched: 2026-10-06
tags: [papers, connector-mating, wire-harness, visuotactile, industrial]
source_type: 논문
lang: en
authors: Claudius Kienle 외 4명 (소속 초록 미표기)
citations: 미확인
---

## 핵심 사실
- 문제: 자동차 조립에 산업용 로봇이 널리 쓰이지만 하네스 장착(installation)은 정밀하고 유연한 조작이 필요해 대부분 수작업이다.
- 방법: 힘 제어 + 시각·촉각·고유수용 데이터로 학습한 멀티모달 트랜스포머로 탐색·삽입 전략을 최적화. 결과 프로그램은 표준 산업용 컨트롤러에서 실행돼 사람이 감사·인증할 수 있다.
- 결과: 센터 콘솔 조립 작업에서 기존 로봇 프로그래밍 대비 사이클 타임과 강건성이 크게 개선(초록, 수치 없음).

## 원문 발췌
> "wire harness installation remains a largely manual process, as it requires precise and flexible manipulation"
(raw: reference/raw/papers--harness-installation-mating.txt, 초록 v2)

## 메모 (RX 관점)
- 완성차 라인의 하네스 "장착"(차체에 배선) 쪽 근거. B2 대상(하네스 제조)과 단계가 다르지만, 커넥터 체결에 시각·촉각 융합이 쓰인다는 점은 같다.
- "감사 가능한 산업 컨트롤러 프로그램" 접근은 end-to-end VLA와 다른 경쟁 접근이다(본 문서 해석).
