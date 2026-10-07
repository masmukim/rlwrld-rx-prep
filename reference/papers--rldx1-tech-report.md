---
title: RLDX-1 Technical Report
url: https://arxiv.org/abs/2605.03269
publisher: arXiv
published: 2026-05-05
fetched: 2026-10-07
tags: [papers, rldx-1, vla, dexterous]
source_type: 논문
lang: en
authors: Dongyoung Kim 외 (총 68명, 소속은 초록 페이지에 미표기)
citations: 미확인
---

## 핵심 사실
- 문제: 실세계 정교 조작(dexterous manipulation)에서 기존 VLA가 놓치는 기능(동작 인지, 장기 기억, 물리 센싱)을 통합.
- 방법: MM-DiT를 행동 모델링으로 확장한 MSAT. 행동 모델은 flow-matching DiT. 모달리티별 스트림 + joint self-attention. (2026-10-07 갱신) 본문 HTML(arxiv.org/html/2605.03269)을 읽음.
- (2026-10-07 갱신) 사전학습 데이터는 공개 데이터셋 조합: Open-X-Embodiment(1M+ 궤적), DROID 92K, Galaxea Open-World 100K, AgiBot World 275K 샘플, Fourier ActionNet 30K(약 140시간), Humanoid Everyday 10.3K, 합성 GR-1 150K. 사전학습 100K 스텝, 배치 8192, 64 H200에서 약 195시간. Mid-training은 25K 스텝, 64 H200에서 15시간.
- (2026-10-07 갱신) Mid-training 데이터: ALLEX는 사내 텔레오퍼레이션 + 합성 72K(1:1 샘플링으로 읽힘, 원문 렌더링이 중복 숫자로 깨져 있음), FR3는 DROID 92K + 사내 데이터(8:2로 읽힘). 새 입력(기억, 토크, FR3 촉각)의 감독 신호는 사내 데이터뿐.
- (2026-10-07 갱신) Post-training: 대부분 실험은 모방학습. 적응형 데이터 수집(기본 시연 → 정책 배포 → 실패 조건을 겨냥한 추가 시연 반복)과 선택적 RECAP 기반 RL(텍스트 VLM critic). 블로그의 "DAgger"라는 표현은 보고서에 없음.
- (2026-10-07 갱신) RL 결과: ALLEX Light Bulb Twisting(오른손 엄지·검지로 전구 돌리기). BC 1056±326 프레임, 12.7±3.0회 시도 → RECAP3 353±22 프레임, 4.1±0.3회. 약 3배 감소, 인간 텔레오퍼레이션보다 낫다고 서술.
- (2026-10-07 갱신) 실세계 평가: ALLEX 4과제 각 24회 시행. 학습 시연 Conveyor 40, Object-in-Box 90, Card Slide 72, Pouring 62개. Card Slide와 Pouring은 단계별 진행 점수(0.33/0.66/1.0, 0.25/0.5/0.75/1.0). 평가는 과제별 30K 스텝 fine-tune, 해당 기능 모듈만 활성화. ALLEX는 머리 스테레오 카메라 1개만 사용, 토크는 모터 전류 추정. Pouring은 액체 대신 작은 플라스틱 공. Card Slide는 안전 때문에 낮은 쪽 책상 높이에서만 평가.
- (2026-10-07 갱신) FR3 6과제: Plug Insertion은 시연 100개, 위치 3곳 x 8회. Egg PnP 시연 60개, 위치 3곳 x 8회. Franka는 평행 그리퍼 + AnySkin 촉각.
- (2026-10-07 갱신) 결론 문장: ALLEX 과제에서 "approximately 90%, while frontier VLAs remain around 40%". 별도 Limitations 절은 없음(검색 확인).
- v1 2026-05-05, v2 2026-05-06 제출. 저자 68명.

## 원문 발췌
> "RLDX-1 achieves a success rate of approximately 90%, while frontier VLAs remain around 40%." (raw: reference/raw/papers--rldx1-tech-report.txt)
> "we evaluate each policy over 24 trials per task unless otherwise specified." (raw: reference/raw/papers--rldx1-tech-report.txt)
> "For each task, only the module relevant to the target functionality is enabled during fine-tuning and evaluation, while the remaining modules are disabled." (raw: reference/raw/papers--rldx1-tech-report.txt)
> "we adopt this approach in almost all experiments throughout the paper." (IL 사용에 대해, raw: reference/raw/papers--rldx1-tech-report.txt)
> "For safety, small plastic balls are used instead of liquid (e.g., coffee) in the pouring task." (raw: reference/raw/papers--rldx1-tech-report.txt)

## 메모 (RX 관점)
- 접촉이 많은 조작(삽입, 계란 집기 등)과 기억 의존 작업이 강점이라는 점을 고객 공정의 "손 작업" 선별 기준으로 활용 가능. 비교 기준은 자사 선택 작업이므로 PoC에서 고객 공정으로 재검증 필요.
- 2026-10-07 갱신: 시행 수, 시연 수, 평가 방식이 확인되어 A2의 열린 질문(ALLEX 작업 수와 시행 수) 해소. research/rldx1-tech.md에서 사용. 원문 raw는 reference/raw/papers--rldx1-tech-report.txt(숫자가 중복 렌더링된 부분 있음).
