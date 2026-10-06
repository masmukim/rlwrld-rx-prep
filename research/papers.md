# 핵심 논문 지도: VLA/RFM, 정밀 손 조작, 촉각, 데이터 수집, 산업 적용
조사일: 2026-10-06

## 핵심 요약
- **지도 범위:** 5개 주제(VLA/RFM, 정밀 손 조작, 촉각·힘, 데이터 수집, 산업 적용)에서 초록을 확인한 논문 27편과, 목록 수준만 확인한 촉각 VLA 후보 7편을 정리했다. 모든 성능 수치는 각 논문의 자체 평가이며 평가 조건이 달라 서로 비교하지 않는다.
- **흐름:** 모델은 RT-2(2023)에서 π0, GR00T N1, Gemini Robotics를 거쳐 RLDX-1(2026-05)로 이어지고 [1][2][5][8][9], 최근 논문은 힘·촉각 입력(ForceVLA 2025-05, Tactile-VLA 2025-07)과 사람 교정·RL 결합(HIL-SERL, π*0.6)을 붙이는 방향이다 [7][13][16][17]. 따라서 "촉각·힘 입력"만으로는 RLDX-1의 차별점이 되기 어렵고, 차별점은 고자유도 손, 현장 데이터 파이프라인, 독립 검증 가능성에서 찾아야 한다(본 문서의 해석).
- **산업 적용 근거는 아직 얇다:** 산업 시나리오를 다룬 논문은 소규모 평가 수준이다(예: Industrial Dexterity Benchmark는 구성당 48회 시행, 78% 대 36%) [27]. 실제 라인의 가동률을 보고한 논문은 이번 조사에서 확인하지 못했다. 일본 제조사(川崎重工, FANUC, 安川電機)도 촉각 VLA(VTLA)를 개발 중이나 기사 공개 구간에는 수치가 없다 [28].

## 본문

### 0. 읽는 법
- 한 주제당 기반 논문 + 최근 논문 + 산업 관련 사례 순으로 골랐다. 인용 수는 OpenAlex(2026-10-06)이며 같은 논문이 arXiv판과 학회판으로 나뉘어 집계돼 절대값이 아니라 순위 참고용이다 [31][32].
- "초록 확인"은 arXiv 초록 페이지만 읽었다는 뜻이다. 본문 표와 실험 조건은 읽지 않았다. 따라서 수치의 "상대 향상인지 %p인지"는 대부분 확인하지 못했다.
- 2026년 제출 논문은 대부분 arXiv 프리프린트이며 게재 여부는 확인하지 않았다.

### 1. VLA/RFM: 모델 계보 (기반 논문과 경쟁사)
| 논문 | 시기·기관 | 한 줄 요약 | RX 시사점 | 출처 |
|------|-----------|-----------|-----------|------|
| RT-2 (인용 270) | 2023-07, Google DeepMind | 로봇 행동을 텍스트 토큰으로 표현해 웹 규모 비전-언어 데이터와 함께 학습. 6,000회 평가에서 새 물체 일반화와 창발 능력 보고 | VLA 개념의 출발점. 고객에게 "왜 언어 모델 기반인가"를 설명할 때 기원 논문 | [2][31] |
| Open X-Embodiment | 2023-10, 21개 기관 | 22개 로봇 데이터를 표준화해 공동 학습, 로봇 간 positive transfer | 서로 다른 로봇 데이터를 합치는 것의 근거. 고객 하드웨어가 달라도 모델을 재사용한다는 주장의 학술 근거 | [3] |
| Diffusion Policy (인용 510~550) | 2023-03, Cheng Chi, Shuran Song 외 | 정책을 조건부 diffusion 과정으로 표현. 4개 벤치마크 12개 작업에서 기존 최고 대비 평균 46.9% 향상(상대/%p 미확인) | GR00T N1의 System 1(diffusion transformer [8])이 이 계열이라는 관계는 본 문서의 해석이다. 산업 벤치마크 기준선은 Diffusion Policy다 [27]. 행동 생성의 기본 부품 | [10][27][32] |
| OpenVLA (인용 45) | 2024-06, Stanford 외 | 7B VLA, 시연 97만 건 학습. 29개 작업에서 55B RT-2-X보다 절대 성공률 +16.5% | 7B 오픈 모델이 55B 모델(RT-2-X)보다 높은 성공률을 낼 수 있다는 근거(29개 작업 조건). 다만 그리퍼 중심 작업 | [4][31] |
| π0 (인용 247) | 2024-10, Physical Intelligence | VLM + flow matching으로 다양한 로봇 플랫폼 데이터를 학습. 세탁물 접기, 박스 조립 시연(초록에 수치 없음) | 주요 경쟁사의 기준 모델. RLDX-1이 비교한 π0.5의 전신 | [5][31] |
| π0.5 | 2025-04, Physical Intelligence | 이종 작업 co-training으로 처음 보는 가정에서 장기·정교 작업 수행 주장 | RLDX-1 벤치마크의 비교 대상. "손 조작 가능"은 이미 주장되므로 차별점은 다른 곳에서 | [6][1] |
| GR00T N1 | 2025-03, NVIDIA | System 2(VLM)와 System 1(diffusion transformer)의 이중 구조. 실로봇, 인간 영상, 합성 데이터 혼합 | 후속판 GR00T N1.7(2026-04-17 Early Access, 3B, 인간 에고센트릭 영상 20,854시간 학습, 22-DoF 손 지원)이 NVIDIA 블로그(1차)로 확인됨 [34]. 일본 PoC에서 GR00T N1.7을 썼다는 사례는 기사 기준(ABEJA×村田製作所) [29]. 경쟁 구도에서 가장 자주 만날 오픈 모델 | [8][34][29] |
| π*0.6 (RECAP) | 2025-11, Physical Intelligence | 시연 + 자율 실행 데이터 + 전문가 교정을 통합. 어려운 작업에서 처리량 2배 이상, 실패율 약 50% 감소(자체 평가) | "배포 후 개선" 루프의 학술 근거. PoC 후반 로드맵 항목 후보. 손 작업 검증은 아님 | [7] |
| Gemini Robotics | 2025-03, Google DeepMind | Gemini 기반 VLA와 Embodied Reasoning 변형. 소량(최소 100개) 시연으로 새 작업 학습, 새 구현체 적응 주장(초록) | PoC 데이터 요구량 비교 기준(주장 수준). 평가 조건은 확인하지 못함 | [9] |

### 2. 정밀 손 조작
| 논문 | 시기·기관 | 한 줄 요약 | RX 시사점 | 출처 |
|------|-----------|-----------|-----------|------|
| Dexterous & Embodied Manipulation 서베이 | 2025-07, Gaofeng Li 외 | 손 조작의 어려움을 고자유도, 다중 접촉, 데이터 부족, 시뮬-현실 격차, 인간-로봇 형태 격차 등으로 정리 | 공정 분해 질문지의 이론적 뼈대. 서베이 비교표는 요약 모델이 만든 것일 수 있어 원문 대조 필요 | [15] |
| DexGraspVLA (AAAI 2026, 인용 7) | 2025-02, Yifan Zhong 외 | VLM 상위 계획 + diffusion 하위 제어. 처음 보는 어지러운 장면 수천 개에서 90% 이상 파지 성공(초록) | 물류 피킹 계열 근거. 파지에 한정되어 조립·삽입의 근거는 아님 | [12][32] |
| HIL-SERL (Science Robotics 2025, 인용 66) | 2024-10, Jianlan Luo, Sergey Levine 외 | 시연 + 사람 교정 + RL로 정밀 조립, 동적 조작, 양팔 협응 학습. 베이스라인 대비 평균 2배 성공률, 1.8배 빠른 실행, 학습 1~2.5시간(초록) | 현장 교정으로 신뢰성을 올린다는 근거. 단일 작업 기준이며 손 사용 여부는 확인하지 못함. 학습 시간을 고객에게 그대로 약속하지 않는다 | [13][31] |
| EgoScale (※4절에서 상세) | 2026-02 | 인간 에고센트릭 영상 20,854시간, 22-DoF 손 | 4절 참고 | [14] |

### 3. 촉각·힘 센싱
| 논문 | 시기·기관 | 한 줄 요약 | RX 시사점 | 출처 |
|------|-----------|-----------|-----------|------|
| ForceVLA (NeurIPS 2025) | 2025-05, Jiawen Yu 외 | 6축 힘/토크를 first-class 모달리티로 보고 MoE로 융합. π0 기반 베이스라인 대비 평균 23.2% 향상, 플러그 삽입 등에서 최대 80%(5개 작업, 상대/%p 미확인) | 힘 입력 VLA는 RLDX-1 이전에 이미 있었다. RLDX-1 Physics 모듈과의 직접 비교는 미확인. π0 기본 구성에 힘 입력이 없다는 간접 신호이나 π0 논문에서 직접 확인하지는 않았다 | [16][1][5] |
| Tactile-VLA | 2025-07, Jialei Huang, Yang Gao 외 | 비전, 언어, 행동, 촉각을 융합하고 하이브리드 위치-힘 제어. 소수 시연으로 접촉 작업의 zero-shot 일반화 주장 | 촉각 VLA의 초기 사례. 수치는 초록에 없음 | [17] |
| Sparsh-X "Tactile Beyond Pixels" | 2025-06, Carolina Higuera 외(소속 미표기) | Digit 360의 4가지 촉각 모달리티(이미지, 오디오, 모션, 압력)를 약 100만 건으로 사전학습. 종단간 촉각 이미지 모델 대비 정책 성공률 63% 향상(상대/%p 미확인) | 촉각 사전학습의 효과 근거. 센서에 종속되므로 고객 하드웨어 선택(A4)과 함께 판단 | [18] |
| TacCoRL | 2026-06, Siyu Ma 외 | 물리 정렬 시뮬레이터에서 sim-real 공동 학습 + RL로 촉각 인지 행동 주입. 4개 양팔 접촉 작업 평균 72.5% 대 50.0% | 시뮬 + RL로 희귀 접촉 상황을 보강하는 근거. 정렬된 시뮬레이터가 전제이며 평가는 4개 작업 | [20] |
| HapticVLA | 2026-03(v2 2026-08), Konstantin Gubernatorov 외 | 촉각 보상 반영 flow matching + 촉각 증류로, 추론 시 촉각 센서 없이 접촉 작업. 실세계 평균 성공률 86.7%이며 추론 시 촉각 피드백을 준 베이스라인 VLA보다 높다고 주장(초록, 작업·시행 수 미확인) | 고객 현장에 촉각 센서를 달지 않는 선택지의 근거. 프리프린트이고 평가 조건 미확인이라 가정으로만 사용 | [35] |
| T-Rex | 2026-06, 34명 공저 | 시간적 촉각 인코딩 + 가변 속도 Mixture-of-Transformers, 100시간 촉각 데이터. 12개 작업에서 최강 베이스라인보다 평균 30% 이상 높음(상대/%p 미확인) | 다관절 손 + 촉각 + VLA의 최신 사례. 공저자 Dantong Niu는 EgoScale 저자 목록에도 있으나 소속 관계는 확인하지 못함. RLDX-1과의 직접 비교는 없음 | [19][14] |

**추가 후보 (arXiv API 목록 요약만 확인, 초록 미열람).** 검색 상위 10건 중 8건이 2026년 제출이다: TacFiLM(2603.14604), TAP-VLA(2606.29089), AT-VLA(2605.07308), VLA-Touch(2507.17294, 2025), UniTacVLA(2606.31723), TaF-VLA(2601.20321), TacVLA(2603.12665) [21] (HapticVLA는 아래 표에서 초록까지 확인). 관련도순 상위 10건이라 전체 동향의 대표 표본은 아니지만, 촉각을 VLA에 붙이는 시도가 연구계에서 빠르게 늘고 있다는 방향성 근거로는 쓸 수 있다. HapticVLA는 추론 시 촉각 센서 없이 촉각 인지 능력을 증류하는 방식이라, "센서 없이도 접촉 성능을 얻는" 방향의 경쟁이 있음을 시사한다(해석) [35].

### 4. 데이터 수집·텔레오퍼레이션
| 논문 | 시기·기관 | 한 줄 요약 | RX 시사점 | 출처 |
|------|-----------|-----------|-----------|------|
| ALOHA / ACT (RSS 2023, 인용 616) | 2023-04, Stanford 외 | 저가 양팔 텔레오퍼레이션 하드웨어 + action chunking. 컵 열기, 배터리 끼우기 등 80~90%, 작업당 약 10분 시연 | 텔레오퍼레이션 데이터 수집의 출발점. 성공률은 연구실 평가 조건 | [11][32] |
| UMI (RSS 2024, 인용 168) | 2024-02, Cheng Chi, Shuran Song 외 | 손에 쥐는 그리퍼로 로봇 없이 현장 시연 수집. 하드웨어 독립 정책, 오픈소스 | 고객 현장에서 로봇 없이 시연을 모으는 선례. 그리퍼용이라 다관절 손에는 확장판(DexUMI 등)이 별도로 존재(제목만 확인) | [23][32] |
| DexCap (RSS 2024, 인용 91) | 2024-03, Stanford | SLAM + 전자기장 센서로 손·손목을 추적하는 웨어러블 모캡. 인간 손 동작을 로봇 손 행동으로 변환(DexIL) | 리타게팅 기반 손 데이터 수집의 대표 사례. RLDX-1의 인간 손 캡처 방식과 같은 계열(해석) | [22][31] |
| 공유 자율(Shared Autonomy) | 2025-10, Zhibin Li 그룹 | 조작자는 VR로 팔을, 자율 손 정책이 손가락을 담당하고 교정으로 개선. 미지 물체 포함 90% 성공(자체 평가, 시행 수 미확인) | 텔레오퍼레이터 부담 경감 방식. 손 정책이 먼저 있어야 함 | [24] |
| EgoScale | 2026-02 | 행동 라벨 붙은 에고센트릭 영상 20,854시간, 22-DoF 손 사전학습. log-linear 스케일링 보고. 사전학습 없는 기준선 대비 평균 54% 향상(상대/%p 미확인) | 고객 작업자 착용 카메라 데이터 수집 전략의 학술 근거. "54%"는 기준선 대비까지만 쓴다. NVIDIA도 같은 20,854시간 규모의 에고센트릭 데이터로 GR00T N1.7을 공개했다(research/competitors.md 참조, NVIDIA 블로그 [34]). 이 전략은 RLWRLD만의 것이 아니다 | [14][34] |

### 5. 산업 적용 사례
| 논문·사례 | 시기 | 한 줄 요약 | 산업 근접도와 한계 | RX 시사점 | 출처 |
|-----------|------|-----------|------------------|-----------|------|
| IndustReal (RSS 2023, 인용 44) | 2023-05, NVIDIA, USC, Stanford 외 | 접촉이 많은 조립(pick, place, insertion)을 시뮬레이션에서 학습해 실로봇에 전이하는 4가지 알고리즘과 도구 공개 | 시뮬 전이 조립. 초록에 성공률 없음, 그리퍼 기반(해석) | 시뮬 파트너십(디지털 트윈) 제안의 선행 연구. NVIDIA 연구진이 저자 | [26][32] |
| FMB (Functional Manipulation Benchmark) | 2024-01, Jianlan Luo, Sergey Levine 외 | 파지, 재배치, 조립 기술을 3D 프린트 물체로 재현 가능하게 평가하는 벤치마크 | 작업 범위를 좁게 설정했고 절차 생성 물체의 실세계 변이 한계가 있다고 서술(WebFetch 요약) | PoC 성공 기준을 기술 단위로 나누어 평가하는 방식의 선례(해석) | [25] |
| Industrial Dexterity Benchmark | 2026-07 | 데이터센터 케이블, 자동차 케이블 하니스, 기어박스 조립 시나리오. 파지+삽입 결합 작업에서 멀티모달 Diffusion Policy 78% 대 단일 카메라 RGB 36%. 단계당 시연 약 100개, 구성당 48회. arXiv v3(2026-09-21) 기준 확인, 개정 후 수치 변동 여부는 미확인 | 산업 시나리오를 명시한 가장 직접적인 사례이나 소규모 평가, 프리프린트 | B1 후보(와이어 하니스·전자 조립)와 직접 연결. 78%는 현장 가동률이 아님. 시연 약 100개는 PoC 데이터량 감각용 | [27] |
| HIL-SERL | 2024-10 | 2절 참고. 정밀 조립을 사람 교정 + RL로 해결 | 실로봇이지만 단일 작업 중심 | 신뢰성 개선 로드맵 근거 | [13] |
| TacCoRL | 2026-06 | 3절 참고. 시험관 삽입, 하드웨어 조립 포함 4개 양팔 작업(검색 요약 기준) | 정렬된 시뮬레이터 필요 | 시뮬 + RL 보강 근거 | [20] |
| ABEJA × 村田製作所 (기업 사례, 기사) | 2026-08-31 | VLA 양팔 로봇이 부품 持ち替え(왼팔 파지 → 오른팔 인계·회전 → 랙 삽입)를 검증 환경에서 성공. GR00T N1.7 사용(ABEJA가 사용했다는 서술은 기사 기준, N1.7 모델 자체는 NVIDIA 블로그로 확인 [34]), 원격 조작 시연 수백 건 | 검증 환경, 정량 성공률 없음. 기사이며 ABEJA 발표의 1차 소스는 확인하지 못함 | 일본 제조업 고객의 PoC 규모 감각(수백 건 시연). 경쟁 모델이 GR00T인 사례 | [29] |
| 川崎重工·FANUC·安川電機 VTLA 개발 (기업 동향, 기사) | 2026-09-02 | VLA에 촉각을 더한 VTLA를 구축 중. 카메라 영상에서 촉각을 얻는 視触覚 핸드, 첫 적용은 자동차 공장 | 유료 기사의 공개 구간만 확인. 수치, 일정, 벤처 기업명 미확인 | 일본 대형 제조사가 같은 방향을 개발 중이므로 일본 고객 제안 시 "내재화 가능성"이 변수. A3에서 후속 확인 | [28] |

- **간극(해석).** 연구는 (a) 시뮬 전이 조립(IndustReal), (b) 실로봇 RL(HIL-SERL), (c) 소규모 벤치마크(FMB, Industrial Dexterity Benchmark)로 나뉘고, 라인 가동률이나 장기 운용 데이터를 보고한 논문은 이번 조사에서 확인하지 못했다. 이 간극이 RX가 현장 PoC에서 데이터를 만드는 이유이기도 하다.

### 6. RLWRLD 관련 연구
| 논문 | 시기 | 내용 | 확인 상태 | 출처 |
|------|------|------|-----------|------|
| RLDX-1 Technical Report | 2026-05-05 | MSAT(MM-DiT 확장), Motion/Physics/Memory 모듈, 촉각·토크 입력. ALLEX 실세계 작업 86.8% 대 π0.5·GR00T N1.6 약 40%(자체 평가) | 초록과 공식 페이지 수준. 논문 본문(작업 수, 시행 조건)은 열람하지 못함 | [1][33] |
- RLDX-1 벤치마크의 비교 대상은 GR00T N1.6이라 후속판 N1.7(2026-04)에는 적용되지 않는다 [1][34].
- RLWRLD 소속 저자의 다른 arXiv 논문은 이번 WebSearch에서 찾지 못했다. 소속은 초록 페이지에 표기되지 않아 저자 목록만으로는 판별할 수 없다.
- RLDX-1과 직접 맞닿는 선행 연구: 에고센트릭 스케일링(EgoScale [14]), 힘·촉각 VLA(ForceVLA, Tactile-VLA [16][17]), 계층·이중 구조 VLA(GR00T N1, DexGraspVLA [8][12]).

### 7. 주제 간 연결과 우선순위
| 우선순위 | 논문 | 이유 |
|----------|------|------|
| 1 | RLDX-1 TR [1] | 고객 대화의 기준점. 본문(작업 수, 시행 조건)을 읽는 것이 필요 |
| 2 | π0, π*0.6 [5][7] | 가장 직접적인 경쟁사 기술과 "배포 후 개선" 흐름 |
| 3 | ForceVLA, T-Rex [16][19] | 촉각·힘 입력의 현재 수준. RLDX-1 차별점 검증 |
| 4 | EgoScale, DexCap, UMI [14][22][23] | 고객 현장 데이터 수집 설계 |
| 5 | HIL-SERL, Industrial Dexterity Benchmark [13][27] | 산업 정밀 작업의 현실적 성능 수준 |

## RX 관점 시사점
- **고객 제안에서:**
  - 공정 적합성 설명에 논문을 연결한다. 파지·피킹은 DexGraspVLA, 접촉이 많은 삽입·조립은 ForceVLA, HIL-SERL, Industrial Dexterity Benchmark, 장기 작업과 기억은 RLDX-1 Memory 모듈 순이다 [12][16][13][27][1].
  - 데이터 수집 계획은 4절 표로 선택한다: 로봇 없이 현장에서 시작하면 UMI형(그리퍼)이나 DexCap형(손), 고객 작업자 영상은 EgoScale, 로봇 라벨이 필요하면 텔레오퍼레이션 + 공유 자율 [23][22][14][24].
  - PoC 후반에 "자율 실행 → 교정 → 재학습" 루프를 넣을 근거는 HIL-SERL과 π*0.6이다. 두 논문 모두 손 작업 전용 검증은 아니라서 "확장 단계"로만 쓴다 [13][7].
  - ROI 가정(B3)에 논문 성공률(78%, 80~90%대)을 가동률로 쓰지 않는다. 시연 수량(단계당 약 100개 [27], 수백 건 [29])은 PoC 데이터량 감각으로만 쓰고 고객 공정 기준으로 다시 산정한다.
  - 일본 고객에게는 대형 제조사의 VTLA 내재화 가능성 [28]과 GR00T 기반 PoC [29]를 경쟁 변수로 둔다.
- **면접에서:**
  - "촉각·힘 입력은 ForceVLA(2025-05)처럼 이미 다른 팀이 시도했고, RLDX-1의 차별점은 고자유도 손, 현장 데이터 파이프라인, 그리고 아직 없는 독립 검증이 관건이라고 본다"고 말할 수 있다 [16][1].
  - "EgoScale의 log-linear 스케일링이 에고센트릭 데이터 전략의 근거이고, HIL-SERL과 π*0.6은 배포 후 개선의 근거"라고 두 갈래로 정리할 수 있다 [14][13][7].
  - 논문 성능 수치를 언급할 때는 "기준선 대비 향상"까지만 말하고 "N% 향상"을 상대 향상인지 %p인지 단정하지 않는다(ForceVLA 23.2%, Sparsh-X 63%, T-Rex 30%, EgoScale 54%, Diffusion Policy 46.9% 모두 해당).
  - 약점도 말한다: 산업 적용 논문은 소규모 평가이고, 2026년 논문은 대부분 프리프린트다.

## 확인하지 못한 항목
- 본문 수치 대부분이 초록 수준이다. 상대 향상인지 %p인지(ForceVLA 23.2%, Sparsh-X 63%, T-Rex 30%, EgoScale 54%, Diffusion Policy 46.9%)는 미확인.
- RLDX-1 본문의 ALLEX 작업 수와 시행 조건. π0, GR00T N1의 정량 성능과 촉각 입력 사용 여부(직접 확인 안 함).
- 촉각 VLA 추가 후보 7편(HapticVLA 제외)의 초록 원문.
- 소속 정보: 다수 논문의 소속이 초록 페이지에 표기되지 않아 표에는 기관명 대신 저자명을 적었다(기관이 적힌 항목은 기존 reference 파일 또는 검색 결과 기준).
- 川崎重工·FANUC·安川電機 기사의 유료 구간(벤처 기업명, 일정, "データの歩留まり率30％の改善"의 의미), ABEJA×村田製作所 발표의 1차 소스(N1.7 모델 자체는 NVIDIA 블로그로 확인됨).
- 2026년 프리프린트의 게재 여부와 후속 반박·재현 여부.

## 출처
1. [RLDX-1 Technical Report](https://arxiv.org/abs/2605.03269) - arXiv, 2026-05-05, 논문, (en) (reference/papers--rldx1-tech-report.md)
2. [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818) - arXiv, 2023-07-28, 논문, (en) (reference/papers--rt2.md)
3. [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864) - arXiv, 2023-10-13, 논문, (en) (reference/papers--open-x-embodiment.md)
4. [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) - arXiv, 2024-06-13, 논문, (en) (reference/papers--openvla.md)
5. [π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164) - arXiv, 2024-10-31, 논문, (en) (reference/papers--pi0.md)
6. [π0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054) - arXiv, 2025-04-22, 논문, (en) (reference/papers--pi05.md)
7. [π*0.6: a VLA That Learns From Experience](https://arxiv.org/abs/2511.14759) - arXiv, 2025-11-18, 논문, (en) (reference/papers--pistar06-recap.md)
8. [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734) - arXiv, 2025-03-18, 논문, (en) (reference/papers--groot-n1.md)
9. [Gemini Robotics: Bringing AI into the Physical World](https://arxiv.org/abs/2503.20020) - arXiv, 2025-03-25, 논문, (en) (reference/papers--gemini-robotics.md)
10. [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137) - arXiv (RSS 2023), 2023-03-07, 논문, (en) (reference/papers--diffusion-policy.md)
11. [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ALOHA/ACT)](https://arxiv.org/abs/2304.13705) - arXiv, 2023-04-23, 논문, (en) (reference/papers--aloha-act.md)
12. [DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping](https://arxiv.org/abs/2502.20900) - arXiv/AAAI 2026, 2025-02-28, 논문, (en) (reference/papers--dexgraspvla.md)
13. [Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning](https://arxiv.org/abs/2410.21845) - arXiv/Science Robotics 2025, 2024-10-29, 논문, (en) (reference/papers--hil-serl.md)
14. [EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data](https://arxiv.org/abs/2602.16710) - arXiv, 2026-02-18, 논문, (en) (reference/papers--egoscale.md)
15. [The Developments and Challenges towards Dexterous and Embodied Robotic Manipulation: A Survey](https://arxiv.org/abs/2507.11840) - arXiv, 2025-07-16, 논문(서베이), (en) (reference/papers--dexterous-survey.md)
16. [ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](https://arxiv.org/abs/2505.22159) - arXiv/NeurIPS 2025, 2025-05-28, 논문, (en) (reference/papers--forcevla.md)
17. [Tactile-VLA: Unlocking Vision-Language-Action Model's Physical Knowledge for Tactile Generalization](https://arxiv.org/abs/2507.09160) - arXiv, 2025-07-12, 논문, (en) (reference/papers--tactile-vla.md)
18. [Tactile Beyond Pixels: Multisensory Touch Representations for Robot Manipulation](https://arxiv.org/abs/2506.14754) - arXiv, 2025-06-17, 논문, (en) (reference/papers--sparsh-x.md)
19. [T-Rex: Tactile-Reactive Dexterous Manipulation](https://arxiv.org/abs/2606.17055) - arXiv, 2026-06-15, 논문(프리프린트), (en) (reference/papers--trex.md)
20. [TacCoRL: Integrating Tactile Feedback into VLA via Simulation](https://arxiv.org/abs/2606.11743) - arXiv, 2026-06-10, 논문(프리프린트), (en) (reference/papers--taccorl.md)
21. [arXiv API 검색 목록: tactile AND vision-language-action](https://export.arxiv.org/api/query?search_query=all:%22tactile%22+AND+all:%22vision-language-action%22&max_results=10&sortBy=relevance) - arXiv API, 조회일 2026-10-06, 논문 목록, (en) (reference/papers--tactile-vla-arxiv-listing.md)
22. [DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation](https://arxiv.org/abs/2403.07788) - arXiv (RSS 2024), 2024-03-12, 논문, (en) (reference/papers--dexcap.md)
23. [Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots](https://arxiv.org/abs/2402.10329) - arXiv (RSS 2024), 2024-02-15, 논문, (en) (reference/papers--umi.md)
24. [End-to-End Dexterous Arm-Hand VLA Policies via Shared Autonomy](https://arxiv.org/abs/2511.00139) - arXiv, 2025-10-31, 논문, (en) (reference/papers--shared-autonomy-dexterous-vla.md)
25. [FMB: a Functional Manipulation Benchmark for Generalizable Robotic Learning](https://arxiv.org/abs/2401.08553) - arXiv, 2024-01-16, 논문, (en) (reference/papers--fmb.md)
26. [IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality](https://arxiv.org/abs/2305.17110) - arXiv/RSS 2023, 2023-05-26, 논문, (en) (reference/papers--industreal.md)
27. [Industrial Dexterity Benchmark](https://arxiv.org/abs/2607.14021) - arXiv, 2026-07-15, 논문(프리프린트), (en) (reference/papers--industrial-dexterity-benchmark.md)
28. [国内ロボ3社が期待、ハンド進化の新潮流「視触覚」 まずは自動車工場へ](https://xtech.nikkei.com/atcl/nxt/column/18/03727/082400003/) - 日経クロステック, 2026-09-02, 기사(유료 기사 공개 구간만 확인), (ja) (reference/tech--xtech-visuotactile-japan.md)
29. [VLAモデルを用いた双腕ロボットのフィジカルAI技術検証を発表 ABEJA×村田製作所](https://robotstart.info/article/2026/08/31/382349.html) - ロボスタ, 2026-08-31, 기사, (ja) (reference/tech--robotstart-abeja-murata.md)
30. [ロボットの頭脳、フィジカルAIは「模倣学習＋強化学習」へ](https://xtech.nikkei.com/atcl/nxt/column/18/03431/121600010/?ST=singleview) - 日経クロステック, 2026-01-08, 기사(필자 의견), (ja) (reference/tech--xtech-il-rl.md). 본문 인용 없음, 배경 참고
31. [OpenAlex 인용 수 조회 (VLA, dexterous)](https://api.openalex.org/works?filter=title_and_abstract.search:%22vision-language-action%22,publication_year:%3E2022&per-page=12&sort=cited_by_count:desc) - OpenAlex, 2026-10-06, 데이터베이스, (en) (reference/tech--openalex-vla-dexterous-citations.md)
32. [OpenAlex 인용 수 조회 (A6 논문 지도용)](https://api.openalex.org/works?filter=title.search:%22Universal%20Manipulation%20Interface%22|%22ForceVLA%22|%22Gemini%20Robotics%3A%20Bringing%22|%22DexGraspVLA%22|%22Learning%20Fine-Grained%20Bimanual%22|%22IndustReal%22|%22Tactile-VLA%22&per-page=15&select=title,publication_year,cited_by_count,doi) - OpenAlex, 2026-10-06, 데이터베이스, (en) (reference/papers--openalex-map-citations.md)
33. [RLDX-1 Foundation Model](https://www.rlwrld.ai/en/rldx-1) - RLWRLD 공식, 2026-05-07, 1차, (en) (reference/company--rlwrld-rldx1-page.md)
34. [NVIDIA Isaac GR00T N1.7: Open Reasoning VLA Model for Humanoid Robots](https://huggingface.co/blog/nvidia/gr00t-n1-7) - Hugging Face 블로그(NVIDIA 게시), 2026-04-17, 1차, (en) (reference/competitors--nvidia-groot-n17.md)
35. [HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing](https://arxiv.org/abs/2603.15257) - arXiv, 2026-03-16, 논문(프리프린트), (en) (reference/papers--hapticvla.md)
