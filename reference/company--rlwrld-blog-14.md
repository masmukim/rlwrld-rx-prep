---
title: "RLDX-1: A Dexterity-First Foundation Model for Robot Hands (RLWRLD Tech Blog)"
url: https://www.rlwrld.ai/ko/insight/blog/14
publisher: RLWRLD
published: 2026-05-07
fetched: 2026-10-07
tags: [company, rldx-1, tech-blog]
source_type: 1차
lang: en
---

## 핵심 사실
- 한국어 경로(/ko/)지만 본문은 영어. 게시일 May 7, 2026, 저자 "RLWRLD Team". 논문 arXiv:2605.03269, 코드 github.com/RLWRLD/RLDX-1, 체크포인트는 Hugging Face 컬렉션으로 링크.
- 아키텍처: MSAT(Multi-Stream Action Transformer). 모달리티(vision-language, proprioception, action, memory, tactile, torque)마다 전용 스트림, 초기 블록은 병렬, 후기 블록에서 융합. VLM은 Qwen3-VL 8B를 로봇 VQA로 fine-tune한 RLDX-1-VLM(RoboCasa 57.50 → 60.92, +3.42).
- 모듈: Motion(영상 토큰 평균 풀링 압축 + STSS), Physics(촉각·토크 스트림, 미래 토크 예측, 센서 없으면 vision-only로 graceful degradation), Cognition Interface(64 cognition tokens, 16.3 → 22.1 Hz) + Memory(FIFO 슬라이딩 캐시).
- 학습 3단계: Pre-training(단일팔·양팔·휴머노이드, 공개 실데이터 + 합성, 임베디먼트 태그 무작위 드롭) → Mid-training(ALLEX, Franka Research 3. Memory·Physics 모듈을 처음부터 초기화해 추가) → Post-training(DAgger + progress-aware RL).
- 데이터: 합성(Cosmos-Predict2 fine-tune + 역동역학 모델 라벨 + 필터, 약 5배, GR-1 Tabletop 평균 성공률 9.2% 향상), 인간 손(맨손 기록, 손·물체 추적 → 3D Gaussian Splatting 작업공간 → 리타게팅 → 시뮬 롤아웃, 시간당 200+ 시연).
- 체크포인트: RLDX-1-PT, RLDX-1-MT-ALLEX, RLDX-1-MT-DROID(MT는 각 8.1B).
- 추론: RTX 5090 + Intel Core Ultra 7 265K, ALLEX, 듀얼뷰 192x256, 4프레임, 액션 청크 40, denoising 4스텝 조건에서 p50 41.59 ms(모듈 제외), 43.70 ms(all-modality), PyTorch Eager 대비 1.61x, 1.63x.
- 시뮬 벤치마크 8종(RLDX-1-PT): LIBERO 97.8, SIMPLER Google-VM 81.5 / Google-VA 77.4 / WidowX 71.9, RoboCasa Kitchen 70.6(기준선 62.1~66.2), GR-1 Tabletop 58.7(N1.5 48.0, N1.6 47.6), RoboCasa 365 32.1(N1.6 26.9), LIBERO-Plus 86.7 vs N1.6 72.6, pi0-FAST 64.2.
- ALLEX 실세계(Table 4, 표시는 success rate): pi0.5 29.2/33.3/55.3/38.5 평균 39.1, N1.6 50.0/29.2/62.3/37.5 평균 44.8, RLDX-1 87.5/91.7/97.2/70.8 평균 86.8 (Conveyor, Object-in-Box, Card Slide-and-Pick, Pot-to-Cup Pouring).
- DROID/Franka(Table 5) 평균: RLDX-1 68.5, pi0.5 34.4, N1.6 31.6. Plug Insertion 33.3 vs 20.8/16.7, Egg PnP 61.1 vs 45.8/37.5, Swap Cup 45.8 vs 25.0/12.5, Shell Game 91.7 vs 45.8/54.2.
- Future Direction(6-4): 과제별 데이터 요구량 상이, 장기(시간 단위) 상호작용 미확장, PT 정책의 zero-shot은 열린 과제, video/world model 확장.

## 원문 발췌
> "RLDX-1 reaches 70.6, the first and only VLA to break the 70% mark on this suite, a +4.4%p jump over the next best." (raw: reference/raw/company--rlwrld-blog-14.txt)
> "the major baselines achieve success rates below 30%, while RLDX-1 reaches nearly 90%." (raw: reference/raw/company--rlwrld-blog-14.txt)
> "Imitation learning alone leaves room for improvement for better success rate and optimal motions." (raw: reference/raw/company--rlwrld-blog-14.txt)
> "Per-task data requirements vary. Some tasks converge quickly with few demonstrations; others need relatively extensive post-training." (raw: reference/raw/company--rlwrld-blog-14.txt)
> "zero-shot generalization as a pre-trained policy remains an open direction." (raw: reference/raw/company--rlwrld-blog-14.txt)

## 메모
- 서술문 "기준선 30% 미만, RLDX-1 거의 90%"는 같은 블로그 Table 4(기준선 평균 39.1, 44.8)와 맞지 않는다. 논문 결론은 "approximately 90% vs around 40%".
- 블로그 본문에는 평가 시행 수, 학습 시연 수가 없다. 논문(papers--rldx1-tech-report.md)에서 확인.
- Memory·Physics 모듈은 mid-training에서 추가되므로 PT 기준 시뮬 벤치마크는 이 두 모듈의 효과를 보여주지 않는다(5-2절 서술에서 읽은 것).
- 같은 날 A11 작업에서 research/rldx1-tech.md에 사용.
