---
title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
url: https://arxiv.org/abs/2302.04761
publisher: arXiv (Meta AI)
published: 2023-02
fetched: 2026-10-17
tags: [papers, tool-use]
source_type: 논문
lang: en
authors: Timo Schick 외 (Meta AI)
citations: 미조회
---

## 핵심 사실
- 방법: 텍스트에 API 호출(계산기, 검색, 달력 등)을 삽입한 데이터셋을 만들고, 호출 결과가 뒤따르는 토큰의 다음 토큰 예측 손실을 줄이는 호출만 남겨 모델을 미세조정한다. 사람 라벨이 거의 필요 없는 자기지도 방식.
- 결과: 6.7B 파라미터 GPT-J에 적용해 제로샷 성능이 크게 향상, 훨씬 큰 GPT-3(175B)를 여러 과제에서 앞섰다고 서술. 핵심 언어모델링 성능은 해치지 않았다고 서술.
- 한계(저자): 도구를 연쇄(한 도구의 출력을 다른 도구 입력으로)로 쓰지 못한다. API 호출이 독립적으로 생성되어 연쇄 사용 예시가 학습 데이터에 없기 때문.

## 원문 발췌
> filter out all calls which do not reduce the loss L_i over the next tokens. (raw: reference/raw/papers--t1-toolformer.txt, 123행 부근)
> the inability of Toolformer to use tools in a chain (같은 파일, 967-968행)

## 메모
- T1에서 도구 호출이 텍스트 토큰 시퀀스로 표현되므로 같은 학습 목표 안에서 다룰 수 있다는 점의 근거. 상세 성능 수치는 이번에 인용하지 않았다.
