---
title: "Training language models to follow instructions with human feedback"
url: https://arxiv.org/abs/2203.02155
publisher: arXiv (OpenAI, NeurIPS 2022)
published: 2022-03
fetched: 2026-10-17
tags: [papers, post-training, rlhf]
source_type: 논문
lang: en
authors: Long Ouyang 외 (OpenAI)
citations: 미조회
---

## 핵심 사실
- 문제 정의: 웹 페이지의 다음 토큰 예측이라는 목표는 "사용자의 지시를 유용하고 안전하게 따르기"와 다르다. 저자는 이를 언어모델링 목표의 misalignment라 부른다.
- 방법: 사람 시연 지도 미세조정 + 사람 선호 피드백 기반 강화학습(RLHF). 모델은 GPT-3와 같은 아키텍처.
- 결과: 자체 API 프롬프트 분포에서 사람 평가자는 13억 파라미터 InstructGPT 출력을 1750억 GPT-3 출력보다 선호(파라미터 100배 이상 적음). 175B InstructGPT 출력은 175B GPT-3보다 85±3%, few-shot 175B GPT-3보다 71±4% 선호.
- 한계: 일부 공개 NLP 데이터셋에서 성능 저하 "alignment tax"가 있다고 서술.

## 원문 발췌
> outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters. (raw: reference/raw/papers--t1-instructgpt.txt, 24-26행)
> the language modeling objective is misaligned. (같은 파일, 59-60행)

## 메모
- T1에서 후훈련이 사전학습 모델의 "사용 가능한 행동"을 크게 바꾼다는 근거. 선호는 사람 평가자와 해당 프롬프트 분포 기준이다.
