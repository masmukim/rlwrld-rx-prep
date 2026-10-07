# 기술 리서치: RFM/VLA, 모방학습, 텔레오퍼레이션, 데이터 수집
조사일: 2026-10-06

## 핵심 요약
- **구조:** 현재 로봇 파운데이션 모델(RFM)의 주류는 사전학습된 VLM에 행동 생성 모듈(flow matching, diffusion transformer 등)을 붙인 VLA(Vision-Language-Action)다. π0, GR00T N1, RLDX-1이 모두 이 계보에 속한다(논문 초록 기준, 계보 분류는 본 문서의 해석) [8][9][1][2]. RLDX-1은 여기에 촉각·힘, 동작 인지, 장기 기억을 더한 "손 특화" 모델을 표방하며, 그 우위는 회사·논문의 자체 평가이고 독립 검증은 확인되지 않았다 [1][2].
- **학습:** 학습의 중심은 여전히 모방학습(Imitation Learning)이고, 시연 품질의 한계를 강화학습(RL)과 현장 교정 개입으로 보완하는 흐름이 나타난다. Physical Intelligence의 π*0.6은 어려운 작업에서 처리량 2배 이상, 실패율 약 50% 감소를 보고했으나 저자 자체 평가다 [11][17].
- **데이터:** 병목은 텔레오퍼레이션 데이터 수집이며(기사 기준 작업자 1명당 하루 50~200 시연, 기사 인용·1차 미확인), 대안은 에고센트릭 인간 영상(EgoScale 20,854시간), 시뮬레이션·합성 데이터, 공유 자율(shared autonomy)이다 [14][13][16]. 다관절 손은 고자유도, 다중 접촉, 시뮬-현실 및 인간-로봇 격차 때문에 어렵고, RLDX-1은 이 셋을 혼합해 대응한다 [15][2].

## 본문

### 1. RFM / VLA 개념과 모델 계보

**정의.** RFM(Robotics Foundation Model)은 대규모 데이터로 사전학습한 뒤 여러 하위 작업과 하드웨어에 적용하는 범용 로봇 AI 모델이다 [16]. VLA는 그중 영상과 언어 지시를 받아 로봇 행동을 출력하는 모델이다. 구조는 보통 "비전-언어 모델(VLM) 백본 + 행동 생성 모듈"이며, 행동 생성은 flow matching [8]이나 diffusion transformer [9]로 구현한다.

**계보 표** (연도순. 성능 수치는 각 논문 자체 평가이며 평가 조건이 서로 달라 직접 비교하지 않는다)

| 단계 | 모델 | 시기 | 기관 | 핵심 아이디어 | 보고된 결과(조건) | 출처 |
|------|------|------|------|---------------|-------------------|------|
| 단일 작업 모방 | ACT / ALOHA | 2023-04 | Stanford 외 | 행동 청크(action chunking) + 저가 양팔 텔레오퍼레이션 | 컵 열기, 배터리 끼우기 80~90%, 작업당 약 10분 시연 | [6] |
| 다중 로봇 데이터 | Open X-Embodiment (RT-X) | 2023-10 | 21개 기관 | 22개 로봇 플랫폼 데이터를 표준화해 공동 학습 | 로봇 간 positive transfer | [5] |
| 오픈 VLA | OpenVLA | 2024-06 | Stanford 외 | Llama 2 7B + DINOv2/SigLIP, 시연 97만 건 | 29개 작업에서 RT-2-X(55B)보다 절대 성공률 +16.5% | [7] |
| 흐름 기반 VLA | π0 | 2024-10 | Physical Intelligence | VLM + flow matching, 다양한 로봇 플랫폼 데이터 | 세탁물 접기, 박스 조립 등 시연(수치는 초록에 없음) | [8] |
| 이중 시스템 | GR00T N1 | 2025-03 | NVIDIA | System 2(VLM) + System 1(diffusion transformer), 실로봇·인간 영상·합성 데이터 혼합 | 시뮬과 Fourier GR-1에서 기존 모방학습보다 우수 주장(수치 미확인) | [9] |
| 오픈월드 일반화 | π0.5 | 2025-04 | Physical Intelligence | 이종 작업 co-training(웹 데이터, 의미 예측 포함) | 처음 보는 가정에서 장기·정교 작업 수행 주장 | [10] |
| 경험 학습 | π*0.6 (RECAP) | 2025-11 | Physical Intelligence | 시연 + 온폴리시 데이터 + 전문가 교정 개입을 advantage conditioning으로 통합 | 어려운 작업에서 처리량 2배 이상, 실패율 약 50% 감소 | [11] |
| 손 특화 | RLDX-1 | 2026-05 | RLWRLD | MSAT(MM-DiT 확장), Motion/Physics/Memory 모듈, 관절 토크 입력(ALLEX)·촉각 입력(Franka 그리퍼에서만) | ALLEX 실세계 4과제 평균 86.8% vs π0.5 39.1%, GR00T N1.6 44.8% (과제당 24회, 진행 점수 2과제 포함, 자체 평가, 작업 설계는 회사) (2026-10-07 A11 정정) | [1][2] |

- 인용 수로 본 영향력(OpenAlex, 2026-10-06): RT-2 270회, π0 247회, DexCap 91회, OpenVLA 45회. OpenAlex가 arXiv판과 학회판을 따로 집계할 수 있어 절대값보다 순위 참고용이다 [18].
- 계보 해석(본 문서): 2023년 단일 작업 모방학습에서 다중 로봇 데이터, VLM 활용, 이중 시스템·오픈월드 일반화, 경험 기반 RL로 이어지고, RLDX-1은 그 위에서 "손과 촉각"에 초점을 맞춘 위치다. π0.5도 "dexterous 조작"을 내세우므로 [10], RLDX-1의 차별점은 "손 조작 가능 여부"가 아니라 촉각·힘 입력, 기억 모듈, 고자유도 손 대상 데이터 파이프라인에 있다고 읽는 편이 정확하다. π0, GR00T N1이 촉각을 쓰는지는 이번 조사에서 확인하지 않았다.

**RLDX-1 요약 (상세는 research/company.md 4절).** 백본 VLM Qwen3-VL 8B, 총 8.1B 파라미터(MT 체크포인트), 모듈은 Motion, Physics(힘·접촉), Memory(과거 상태 추적. Cognition Interface의 64토큰을 재사용)이며, 센서가 없으면 해당 스트림을 끄고 vision-only로 동작한다(graceful degradation, 저하 폭 수치는 미공개) [2] (2026-10-07 A11 정정). GR00T N1.6 대비 RoboCasa Kitchen 70.6% vs 66.2%, LIBERO-Plus 86.7% vs 72.6% 등이 공식 페이지에 있다 [2]. ALLEX 실세계 평가는 4과제, 과제당 24회, 과제별 시연 40~90개로 미세조정, 과제에 필요한 모듈만 켠 조건이다 (research/rldx1-tech.md 5절) (2026-10-07 A11 정정).

### 2. 학습 방식: 모방학습과 강화학습

| 방식 | 핵심 | 장점 | 한계 | 사례 | 출처 |
|------|------|------|------|------|------|
| 모방학습(IL) | 인간 시연을 따라 하도록 지도학습 | 필요 데이터가 상대적으로 적음 | 시연의 정적 행동만 학습해 인간 성능을 넘기 어려움. 작은 오차가 누적(compounding error)되어 신뢰성이 떨어짐 | ACT, OpenVLA, π0, GR00T N1, RLDX-1 | [15][6][7] |
| 강화학습(RL) | 시행착오와 보상으로 행동 최적화 | 시연을 넘는 성능과 자연스러운 동작 기대 | 보상이 희박하고 표본 효율이 낮아 수백만 회 반복이 필요(서베이 서술). 실로봇 적용 시 안전·비용 부담이 클 것(`추정`, 별도 근거 미확인) | 시뮬레이션 기반 손 조작 등 | [15] |
| 결합(IL + RL + 교정) | 시연으로 초기화 후 자율 실행 데이터와 전문가 교정으로 개선 | 현장 배포 후 신뢰성 개선 가능 | 값 함수·보상 설계, 교정 인력 필요(본 문서의 해석, `추정`). RLDX-1은 post-training에 교정 데이터와 RECAP 기반 RL을 선택적으로 둔다. 손 특화 효과 검증은 ALLEX 전구 돌리기 1과제(자체 평가, BC 대비 약 3배)뿐 (2026-10-07 A11 정정) | π*0.6 RECAP [11], 공유 자율 + 교정 텔레오퍼레이션 [13] | [11][13] |

- 동향: 일본 언론(Nikkei xTECH, 2026-01)은 모방학습만으로 만든 VLA의 동작이 어색하다고 평하며 2026년을 VLA에 RL이 본격 도입되는 해로 전망했다. 필자 의견이며 실험 수치는 없다 [17]. 본문의 π*0.6 사례가 이 전망과 같은 방향의 근거다 [11].
- RLDX-1의 위치: 학습은 Pre-training → Mid-training(Motion·Memory·Physics 추가) → Post-training(교정 데이터 + 선택적 RECAP 기반 RL) 3단계다. RL 효과는 1과제 자체 평가로만 확인된다 (research/rldx1-tech.md 3절) (2026-10-07 A11 정정).

### 3. 데이터 수집: 텔레오퍼레이션, 인간 영상, 시뮬레이션

| 방식 | 대표 사례 | 장점 | 한계 | 출처 |
|------|-----------|------|------|------|
| 로봇 텔레오퍼레이션 | ALOHA(저가 양팔, 작업당 약 10분), VR 텔레오퍼레이션 | 로봇 구현체에 맞는 정확한 행동 라벨. 인간-로봇 형태 격차와 시뮬 격차를 모두 피함 | 힘·촉각 피드백이 약하고 지연이 있음. 작업자 1명당 하루 50~200 시연(기사 서술, 근거 불명확·1차 미확인), 인력과 시간 비용 | [6][15][16] |
| 공유 자율 | 조작자는 VR로 팔을, 자율 손 정책(DexGrasp-VLA)이 손가락을 담당. 교정 개입으로 정책 개선 | 조작자 부담 감소, 수집할수록 효율 상승 가능 | 미지 물체 포함 90% 성공(자체 평가, 작업·시행 수 미확인). 손 정책이 이미 있어야 함 | [13] |
| 웨어러블 모캡 | DexCap: SLAM + 전자기장 센서로 손·손목을 가림에 강하게 추적, DexIL로 로봇 행동 변환 | 로봇 없이 휴대하며 현장에서 수집 | 인간-로봇 손 형태 차이를 변환(리타게팅)해야 함. 6개 작업 평가(수치 미확인) | [12][15] |
| 에고센트릭 인간 영상 | EgoScale: 행동 라벨 붙은 에고센트릭 영상 20,854시간, 22-DoF 손 | 규모 확장이 쉽고 스케일링 법칙(log-linear)이 보고됨. 낮은 DoF 손에도 전이 | 사전학습 없는 기준선 대비 평균 성공률 54% 향상(상대 향상인지 %p인지 초록에 없음, 본문 확인 필요). 소량의 정렬된 인간-로봇 데이터가 추가로 필요 | [14] |
| 시뮬레이션·합성 | 시뮬 데이터, 비디오 생성 기반 합성 증강 | 저렴하고 확장 가능 | 마찰 등 물리 모델 오차로 시뮬-현실 격차 | [15][2] |

- **규모 감각.** 기사에 인용된 규모: π0 약 1만 시간, Generalist AI GEN-0 27만 시간, Google RT-1 로봇 13대로 17개월 동안 13만 건 시연 [16]. 이 수치는 1차 소스를 확인하지 못한 기사 인용이다. 반면 확인된 1차 수치로 OpenVLA는 시연 97만 건 [7], EgoScale은 인간 영상 20,854시간 [14]이다. 단위(시간 vs 건)가 달라 서로 비교하지 않는다.
- **RLDX-1의 혼합 전략.** 실 텔레오퍼레이션 + 인간 손 캡처 리타게팅(시간당 200건 이상 시연, 추적→3DGS→리타게팅→시뮬 롤아웃 4단계의 산출이며 산출 기준 미기재) + 비디오 생성 합성 증강(약 5배, ActionNet 30K 대비 150K. GR-1 Tabletop 41.0→50.1, 1,000 시연 조건) [2] (2026-10-07 A11 정정). 현장 데이터는 직원이 머리, 가슴, 손에 카메라를 착용하는 에고센트릭 방식과 멀티카메라, 텔레오퍼레이션 병행 [3]. 대표는 "합성 데이터와 결합하면 실데이터 20%면 충분"이라 발언했고 AWS 블로그는 유사 모델(블로그 기준 GR00T N1.5) 대비 약 20% 컴퓨트로 SOTA를 주장하나 모두 회사 주장이다 [3][4].
- **시뮬·합성 파트너.** 2026-08 피직스심랩(디지털 트윈), 스페이스에이아이(연성체 평가), 엔닷라이트(3D 데이터)와 MOU로 합성·시뮬 파이프라인을 강화하는 중이다 [19].
- **일본 데이터 파트너.** KDDI와 에고센트릭 시점 + 멀티카메라 기반 "연간 3,500시간 상당" 데이터 수집을 목표로 한다 [20]. EgoScale의 20,854시간과 단순 비교하면 약 17%(계산, 3,500/20,854)이나 "3,500시간 상당"이 영상 시간인지 환산치인지 확인되지 않아 규모 감각용 참고치일 뿐이다(`추정`).
- **비용.** 기사는 시스템 통합 비용이 로봇 하드웨어 가격의 50~200%라고 서술한다(기사 인용, 1차 미확인) [16]. B3 ROI에 쓸 경우 1차 소스를 별도 확인해야 한다.

### 4. 로봇 손 조작이 어려운 이유

| 요인 | 설명 | 출처 |
|------|------|------|
| 고자유도 | 인간 손은 20개 이상의 자유도를 가진다. ALLEX 손은 15-DoF, EgoScale 실험 손은 22-DoF. 자유도가 높을수록 탐색 공간이 커진다 | [15][2][14] |
| 다중 접촉 | 여러 손가락이 물체와 동시에 접촉해 역학이 복잡하고 다양하다 | [15] |
| 데이터 부족 | 고품질 손 조작 데이터셋이 부족하다 | [15] |
| 시뮬-현실 격차 | 마찰, 공기저항 모델 오차 등 | [15] |
| 인간-로봇 형태 격차 | 인간 손과 로봇 손의 구조 차이로 시연 변환이 어렵다 | [15] |
| 피드백 | 텔레오퍼레이션은 힘·촉각 피드백이 약하고 지연이 있다 | [15] |
| 장기·기억 | 순차 작업의 진행 상태, 실수 복구에 기억이 필요하다 | [1][2] |

**RLDX-1의 대응 (회사 주장 기준, 효과 검증은 별도).**
| 어려움 | RLDX-1 대응 | 출처 |
|--------|-------------|------|
| 접촉·힘 감지 | Physics 모듈(촉각, 관절 토크), 무게 추정·접촉 감지 (블로그 명시. 슬립 감지는 시연 증거 없음) (2026-10-07 A11 정정) | [2] |
| 장기 작업·실수 복구 | Memory 모듈은 과거 상태 추적(Cognition Interface 64토큰 재사용), 실수 복구는 post-training 교정 데이터 (2026-10-07 A11 정정) | [2] |
| 시간적 동작 | Motion 모듈 | [1][2] |
| 손 데이터 부족 | 인간 손 캡처 리타게팅(시간당 200건 이상, 산출 기준 미기재), 합성 증강 약 5배, 고객 현장 에고센트릭 수집 | [2][3] |
| 형태 차이 | 다중 구현체 학습(ALLEX, Franka Research 3, OpenArm + Inspire 손) | [2] |

### 5. 기술 성숙도 점검 (고객 제안 전 확인할 한계)
| 항목 | 현황 | 출처 |
|------|------|------|
| 벤치마크 독립 검증 | RLDX-1 수치는 회사·논문 자체 평가. 독립 검증 확인 못 함 | [1][2] |
| 비교 조건 | ALLEX 실세계 작업 수와 시행 조건 미확인 | [1] |
| 성공률 수준 | 최고 수치가 80~90%대(ACT 80~90% [6], 공유 자율 90% [13], RLDX-1 86.8% [1]). 모두 평가 작업과 조건이 달라 "현장 가동률"이 아니다 | [1][6][13] |
| RL 적용 | 손 특화 모델에 RL을 적용한 공개 검증은 이번 조사에서 확인하지 못함 | [11][2] |
| 라이선스 | RLDX-1 가중치는 비상업 라이선스(research/company.md) | [21] |

## RX 관점 시사점
- **고객 제안에서:**
  - 공정을 "접촉이 많은가, 기억이 필요한가, 자유도 높은 손이 필요한가"로 분해하면 RFM 적합성을 설명하기 쉽다. 단순 pick-and-place는 기존 그리퍼로 풀릴 수 있어 RLDX-1의 차별성이 약하다는 가설(research/company.md `추정`)과 같은 방향이며, A4에서 하드웨어로 검증한다.
  - 데이터 수집 계획은 PoC의 핵심이다. 방식 선택표: (a) 숙련 작업자 시연이 핵심이고 로봇이 아직 없다면 에고센트릭/웨어러블, (b) 로봇 구현체 행동 라벨이 필요하면 텔레오퍼레이션(공유 자율로 부담 경감), (c) 위험·희귀 상황은 시뮬·합성으로 보강. 롯데호텔 사례(직원 착용 카메라·센서)가 (a)에 해당한다.
  - "시연 수집 -> 자율 실행 -> 교정 개입 -> 재학습" 루프를 PoC 로드맵 후반(B4)에 넣을 근거는 π*0.6 [11]이다. 단, 손 작업 검증은 아니라서 "가능성이 있는 확장 단계"로만 쓴다.
  - ROI 가정(B3): 성공률 80~90%대를 현장 가동률로 쓰지 말고, 평가 조건 차이를 명시한다. 시스템 통합 비용 50~200% 수치는 1차 확인 후 사용한다.
- **면접에서:**
  - "VLA는 VLM 위에 행동 생성 모듈을 얹은 구조이고 RLDX-1은 촉각, 힘, 기억을 더해 손 조작에 특화했다"고 한 문장으로 설명할 수 있다.
  - "데이터 병목을 에고센트릭, 합성, 텔레오퍼레이션의 조합으로 푼다"는 RLWRLD의 접근을 EgoScale(20,854시간, log-linear 스케일링, 기준선 대비 54% 향상)과 연결해 근거를 댈 수 있다.
  - 약점도 안다고 말한다: 독립 검증 부재, 작업 설계 편향, RL 적용 불확실, 비상업 라이선스.

## 확인하지 못한 항목
- RLDX-1 논문 본문(학습 레시피, 작업 목록, ALLEX 평가 조건). 초록과 공식 페이지 수준이다.
- π0, π0.5, GR00T N1의 정량 성능과 촉각 입력 사용 여부. 초록에 수치가 없다.
- 기사 인용 수치(하루 50~200 시연, π0 약 1만 시간, GEN-0 27만 시간, 통합 비용 50~200%)의 1차 소스.
- 서베이(2507.11840) 비교표는 요약 모델이 정리한 내용이라 원문 표현과 다를 수 있다.
- 촉각 센서 종류와 손 하드웨어 비교는 A4에서 다룬다. 경쟁사 비교(Figure Helix, Gemini Robotics 등)는 A3에서 다룬다.

## 출처
1. [RLDX-1 Technical Report](https://arxiv.org/abs/2605.03269) - arXiv, 2026-05-05, 논문, (en) (reference/papers--rldx1-tech-report.md)
2. [RLDX-1 Foundation Model](https://www.rlwrld.ai/en/rldx-1) - RLWRLD 공식, 2026-05-07, 1차, (en) (reference/company--rlwrld-rldx1-page.md)
3. [Putting Dexterous Robots to Work: How RLWRLD Builds Physical AI with AWS](https://aws.amazon.com/blogs/physical-ai/putting-dexterous-robots-to-work-how-rlwrld-builds-physical-ai-with-aws/) - AWS Physical AI Blog, 2026-06-22, 공식문서, (en) (reference/company--aws-blog-rlwrld.md)
4. [리얼월드, RLDX-1 라이브 데모 시연](https://zdnet.co.kr/view/?no=20260610191936) - ZDNet Korea, 2026-06-10, 기사, (ko) (reference/company--zdnet-dexterity-night.md)
5. [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864) - arXiv, 2023-10-13, 논문, (en) (reference/papers--open-x-embodiment.md)
6. [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ALOHA/ACT)](https://arxiv.org/abs/2304.13705) - arXiv, 2023-04-23, 논문, (en) (reference/papers--aloha-act.md)
7. [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) - arXiv, 2024-06-13, 논문, (en) (reference/papers--openvla.md)
8. [π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164) - arXiv, 2024-10-31, 논문, (en) (reference/papers--pi0.md)
9. [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734) - arXiv, 2025-03-18, 논문, (en) (reference/papers--groot-n1.md)
10. [π0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054) - arXiv, 2025-04-22, 논문, (en) (reference/papers--pi05.md)
11. [π*0.6: a VLA That Learns From Experience](https://arxiv.org/abs/2511.14759) - arXiv, 2025-11-18, 논문, (en) (reference/papers--pistar06-recap.md)
12. [DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation](https://arxiv.org/abs/2403.07788) - arXiv (RSS 2024), 2024-03-12, 논문, (en) (reference/papers--dexcap.md)
13. [End-to-End Dexterous Arm-Hand VLA Policies via Shared Autonomy](https://arxiv.org/abs/2511.00139) - arXiv, 2025-10-31, 논문, (en) (reference/papers--shared-autonomy-dexterous-vla.md)
14. [EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data](https://arxiv.org/abs/2602.16710) - arXiv, 2026-02-18, 논문, (en) (reference/papers--egoscale.md)
15. [The Developments and Challenges towards Dexterous and Embodied Robotic Manipulation: A Survey](https://arxiv.org/abs/2507.11840) - arXiv, 2025-07-16, 논문(서베이), (en) (reference/papers--dexterous-survey.md)
16. [로봇 파운데이션 모델, 로봇의 '챗GPT 모먼트' 만들까](https://www.thelec.kr/news/articleView.html?idxno=53444) - 디일렉, 2026-03-13, 기사, (ko) (reference/tech--thelec-robot-fm.md)
17. [ロボットの頭脳、フィジカルAIは「模倣学習＋強化学習」へ](https://xtech.nikkei.com/atcl/nxt/column/18/03431/121600010/?ST=singleview) - 日経クロステック, 2026-01-08, 기사(필자 의견), (ja) (reference/tech--xtech-il-rl.md)
18. [OpenAlex 인용 수 조회](https://api.openalex.org/works?filter=title_and_abstract.search:%22vision-language-action%22,publication_year:%3E2022&per-page=12&sort=cited_by_count:desc) - OpenAlex, 조회일 2026-10-06, 데이터베이스, (en) (reference/tech--openalex-vla-dexterous-citations.md)
19. [리얼월드, 자체 모델 기반 로보틱스 생태계 확장한다](https://www.hellot.net/news/article.html?no=114256) - 헬로티, 2026-08-10, 기사, (ko) (reference/company--hellot-ecosystem-mou.md)
20. [KDDIとRLWRLD、フィジカルAI基盤モデル開発で連携強化](https://ai.watch.impress.co.jp/docs/news/2142380.html) - AI Watch, 2026-09-18, 기사, (ja) (reference/company--impress-kddi-geniac.md)
21. [RLWRLD/RLDX-1](https://github.com/RLWRLD/RLDX-1) - GitHub, 2026-05-06, 1차, (en) (reference/company--github-rldx1.md)
