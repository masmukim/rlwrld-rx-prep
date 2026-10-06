---
title: "DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping"
url: https://arxiv.org/abs/2502.20900
publisher: arXiv, AAAI 2026 (Vol. 40, pp. 18836-18844, 검색 결과 기준)
published: 2025-02-28
fetched: 2026-10-06
tags: [papers, vla, dexterous, grasping]
source_type: 논문
lang: en
authors: Yifan Zhong, Xuchuan Huang, Ruochong Li 외 (Yuanpei Chen, Yaodong Yang 포함. 소속은 초록 페이지에 미표기)
citations: 7 (OpenAlex, AAAI판, 2026-10-06 기준)
---

## 핵심 사실
- 문제: 언어 지시를 따르는 범용 다관절 손 파지(dexterous grasping).
- 방법: 사전학습 VLM을 상위 계획기로, diffusion 기반 저수준 행동 제어기를 하위로 쓰는 계층 구조.
- 결과: "수천 개의 처음 보는 어지러운 장면"에서 90% 이상 파지 성공률(초록). 자유 형식 장기 지시, 적대적 물체와 사람 방해에 대한 강건성, 실패 복구를 함께 시연. 손 종류와 정확한 물체 수는 초록에 없음.
- 한계: 초록은 파지(grasping)에 한정. 조립·삽입 같은 접촉 작업은 범위 밖.

## 원문 발췌
> a 90+% dexterous grasping success rate under thousands of challenging unseen cluttered scenes (초록)

## 메모 (RX 관점)
- 다관절 손 + VLM 계층 구조 사례. 구조는 GR00T N1의 이중 시스템과 유사(본 팀 해석). "물류 피킹 계열"에는 근거가 되나 정밀 조립은 별도 증거 필요.
