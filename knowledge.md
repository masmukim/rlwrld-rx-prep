# 도메인 지식 노트

RX 팀이 작업하면서 배운 산업 지식을 쌓는 파일이다. 모든 에이전트가 작업 시작 전에 읽는다.
수정은 메인 에이전트만 한다 (`/rx-done`에서 서브에이전트가 반환한 "새로 배운 것"을 반영).
각 항목 끝에는 근거 reference 파일이나 작업 ID를 적는다.

## 용어집
| 용어 | 영어 | 뜻 | 근거 |
|------|------|----|------|
| RFM | Robotics Foundation Model | 다양한 로봇과 작업에 범용으로 쓰는 대규모 로봇 AI 모델 | reference/company--rx-intern-posting.md |
| RX | Robotics Transformation | RFM을 고객 현장에 도입시키는 RLWRLD의 사업 부문 | reference/company--rx-intern-posting.md |
| VLA | Vision-Language-Action model | 영상과 언어 지시를 받아 로봇 동작을 출력하는 모델. 보통 사전학습 VLM 백본 + 행동 생성 모듈(flow matching, diffusion transformer) 구조 | research/tech.md 1절 |
| 액션 청킹 | Action Chunking with Transformers (ACT) | 행동을 시퀀스 단위로 예측해 모방학습의 오차 누적을 줄이는 방법 | reference/papers--aloha-act.md |
| 흐름 매칭 | Flow matching | π0가 VLM 위에 행동 생성용으로 쓴 생성 모델 방식 | reference/papers--pi0.md |
| 이중 시스템 | Dual-system (System 2 / System 1) | VLM이 해석·계획, diffusion transformer가 실시간 동작을 맡는 GR00T N1 구조 | reference/papers--groot-n1.md |
| 공유 자율 | Shared autonomy | 조작자는 팔의 큰 움직임, 자율 정책은 손가락 미세 동작을 담당하는 텔레오퍼레이션 | reference/papers--shared-autonomy-dexterous-vla.md |
| RECAP | RL with Experience and Corrections via Advantage-conditioned Policies | 시연, 자율 실행 데이터, 전문가 교정을 합쳐 VLA를 개선하는 π*0.6의 방법 | reference/papers--pistar06-recap.md |
| 구현체 간 학습 | Cross-embodiment learning | 서로 다른 로봇의 데이터를 합쳐 하나의 정책을 학습 | reference/papers--open-x-embodiment.md |
| 리타게팅 | Retargeting | 인간 손 동작을 로봇 손의 관절 명령으로 변환 | reference/papers--dexcap.md |
| 로봇 밀도 | Robot density | 제조업 종사자 1만 명당 가동 산업용 로봇 수. 2024년 한국 1,220, 일본 446, 세계 132 | reference/market--ifr-robot-density-2024.md |
| 미충원인원/미충원율 | Unfilled vacancies | 구인했으나 채우지 못한 인원/비율. 고용노동부 직종별사업체노동력조사 지표 | reference/market--moel-vacancy-2025h2.md |
| RaaS | Robot-as-a-Service | 로봇을 구독·임대로 제공하는 방식. 2024년 서비스 로봇 RaaS +31% | reference/market--ifr-service-robots-2025.md |
| 노동공급제약사회 | 労働供給制約社会 | 리크루트웍스의 일본 2040 전망 프레임. 수요가 있어도 노동 공급이 못 따라가는 사회 | reference/market--recruit-works-2040.md |
| PoC | Proof of Concept | 고객 현장에서 기술 적용 가능성을 검증하는 시범 프로젝트 | reference/company--rx-intern-posting.md |
| MSAT | Multi-Stream Action Transformer | RLDX-1 아키텍처. MM-DiT를 행동 모델링으로 확장해 모달리티별 스트림을 joint self-attention으로 결합 | reference/papers--rldx1-tech-report.md |
| ALLEX | ALLEX humanoid (WIRobotics) | 48-DoF 휴머노이드, 양손 각 15-DoF. RLDX-1 주 실험 플랫폼 | reference/company--rlwrld-rldx1-page.md |
| GENIAC | Generative AI Accelerator Challenge | 일본 경제산업성의 생성AI 개발 지원 프로그램. KDDI와 RLWRLD 채택 | reference/company--impress-kddi-geniac.md |
| 에고센트릭 데이터 | Egocentric data | 작업자가 착용한 카메라로 찍은 1인칭 작업 영상 데이터 | reference/company--aws-blog-rlwrld.md |
| VTLA | Vision-Tactile-Language-Action model | VLA에 촉각 입력을 더한 모델. 일본 川崎重工·FANUC·安川電機 3사가 개발 중이라고 보도됨 | reference/tech--xtech-visuotactile-japan.md |
| 視触覚 | Visuo-tactile sensing | 카메라 영상으로 촉각 정보를 얻는 방식. 별도 힘·촉각 센서를 쓰지 않음 | reference/tech--xtech-visuotactile-japan.md |
| HIL-SERL | Human-in-the-Loop Sample-Efficient Robotic RL | 시연, 사람 교정, 표본 효율 RL을 합친 실로봇 학습. 학습 1~2.5시간, 베이스라인 대비 평균 2배 성공률 | reference/papers--hil-serl.md |
| UMI | Universal Manipulation Interface | 손에 쥐는 그리퍼로 로봇 없이 현장 시연을 모으는 데이터 수집 방식 | reference/papers--umi.md |
| FVLMoE | Force-aware VLA Mixture-of-Experts | ForceVLA에서 힘 신호를 단계별로 융합하는 MoE 모듈 | reference/papers--forcevla.md |
| 시각 기반 촉각 센서 | Vision-Based Tactile Sensor (VBTS) | 탄성 겔과 카메라로 접촉 변형을 영상으로 읽는 촉각 센서. GelSight, DIGIT, FingerVision 방식 | reference/papers--vbts-survey.md |
| 텐던 구동 | Tendon-driven | 와이어로 손가락을 당기는 방식. 모터를 전완에 둘 수 있으나 신장과 마모로 수명 문제가 있음 | reference/papers--orca-hand.md |
| Taxel | Tactile pixel | 촉각 센서의 감지 단위. Digit 360은 약 830만 | reference/papers--digit360.md |
| 구현체 불문 두뇌 | Omni-bodied model | 몸체 형태를 모르고도 사족보행, 휴머노이드, 팔을 모두 제어한다는 Skild Brain의 표현 | reference/competitors--skild-series-funding.md |
| 전신 제어 3계층 | System 0/1/2 (Helix 02) | S0 1 kHz 균형, S1 200 Hz 감각-관절 변환, S2 추론 | reference/competitors--figure-helix-02.md |
| 조합 일반화 | Compositional generalization | 서로 다른 맥락의 기술을 조합해 학습에 거의 없던 작업을 푸는 능력(PI π0.7의 주장) | reference/competitors--pi-pi07-techcrunch.md |
| 데이터 플라이휠 | Data flywheel | 배치된 로봇이 만드는 데이터로 모델을 개선하는 순환 구조(Skild 설명) | reference/competitors--skild-abb-ur-foxconn.md |
| 월드 파운데이션 모델 | World Foundation Model (WFM) | 물리 세계 변화를 예측하는 모델. 한국 과기정통부 과제에서 LG전자가 개발 담당 | reference/competitors--korea-msit-physical-ai-lg-kt.md |
| Early Access | Early Access | 일반 공개 전에 파트너나 신청자에게만 모델을 제공하는 단계(GR00T N1.7, Gemini Robotics 2) | reference/competitors--nvidia-groot-n17.md |
| 상대 향상 대 %p 향상 | Relative vs absolute (percentage points) improvement | "N% 향상"이 기준선의 N% 증가인지 성공률이 N%p 오른 것인지의 구분 | reference/papers--forcevla.md |
| 프리블록 | Pre-block | 압착 단자를 도면에 따라 커넥터 캐비티에 손으로 꽂는 하네스 조립 첫 단계 | reference/case--easychair-harness-line-balancing.md |
| 레이업 | Lay-up | 조립판에 서브 어셈블리를 배치하고 배선하며 남은 단자를 꽂는 단계. 참고 라인의 병목 | reference/case--easychair-harness-line-balancing.md |
| 조립판 | Form board / routing board | 하네스 경로 지그가 달린 작업판 | reference/case--ams-cellios-automated-harness.md |
| SMH | Standard Man Hour | 작업자 1명이 하네스 1개를 만드는 표준 공수. 참고 라인은 2.16시간 | reference/case--easychair-harness-line-balancing.md |
| 분기형 선형 변형체 | Branched DLO (BDLO) | 갈라지는 케이블 다발. 분기점에서 힘과 변형 전파가 복잡함 | reference/papers--deft-branched-dlo.md |
| 분할 하네스 | 分割ハーネス | 하네스를 4~5개 영역으로 나눠 적은 품번 조합으로 약 250품종을 만드는 住友電工 공법 | reference/case--netdenjd-sumitomo-split-harness.md |
| 이동형 산업 | Migratory industry | 최저 인건비 국가로 생산이 계속 옮겨 가는 산업. 하네스의 별칭 | reference/case--ams-cellios-automated-harness.md |
| 덱스벤치 | DexBench | RLWRLD가 고객 현장 워크플로 분석 데이터로 만든 18개 과제의 손재주 평가 벤치마크. NVIDIA Isaac Lab-Arena와 연결 | reference/company--mk-cbo-interview-2026-10.md |
| 시간 제한 시험 | Time-boxed deployment | 기간과 범위를 정한 소규모 현장 시험. Boston Dynamics는 이를 상설 RMAC 훈련센터로 대체 | reference/case--poc-robotreport-rmac.md |
| RMAC | Robotics Metaplant Application Center | Hyundai 공장 안 상설 로봇 훈련·검증 시설. 시퀀싱 2028, 조립 2030 로드맵 | reference/case--poc-hyundai-ces2026-atlas.md |
| 파일럿 정체 | Pilot purgatory | 데모는 되지만 운영으로 승격하지 못하는 상태 | research/poc-playbook.md 6절 |
| 서비스 운영형 | Service-operated robotics | 로봇을 판매하지 않고 운영 서비스(원격 복구 포함)로 제공. Telexistence 방식 | reference/case--poc-tx-ghost-service.md |
| 손재주 5영역 | Five Regimes of Dexterity | DexBench 분류. Grasp Diversity, Spatial Precision, Temporal Precision, Contact Precision, Context Awareness | reference/company--rlwrld-blog-14.md |
| 인지 토큰 | Cognition tokens / Cognition Interface | VLM 입력에 붙인 학습 가능 토큰 64개. VLM 출력을 고정 크기로 압축하고 Memory의 단위로도 재사용 | reference/company--rlwrld-blog-14.md |
| 진행 점수 | Progress score | 단계별 부분 점수(예: 0.33/0.66/1.0). 성공률과 다른 지표 | reference/papers--rldx1-tech-report.md |
| 진행도 인지 RL | Progress-aware RL / VLM critic | 진행도 추정 VLM을 dense reward로 쓰는 RL. RLDX-1 논문은 RECAP 기반 텍스트 VLM critic | reference/papers--rldx1-tech-report.md |
| 적응형 데이터 수집 | Adaptive data collection | 기본 시연으로 학습 후 실패 조건을 겨냥해 추가 시연을 모으는 반복. 블로그는 DAgger로 부름 | reference/papers--rldx1-tech-report.md |
| 우아한 성능 저하 | Graceful degradation | 센서가 없으면 해당 스트림을 꺼서 vision-only로 동작 | reference/company--rlwrld-blog-14.md |
| STSS | Spatio-Temporal Self-Similarity | 영상 특징의 시공간 자기유사도로 회전·속도를 포착. Motion Module의 한 부분 | reference/company--rlwrld-blog-14.md |

## 핵심 인사이트
(작업이 끝날 때마다 추가. 형식: `- 인사이트 [근거]`)
- RX는 영업 접점이자 데이터 확보 채널이다. 회사는 해자를 "모델이 아니라 현장 데이터와 적용 엔지니어링"으로 설명한다 [reference/company--tech42-rx-model.md]
- "투자자 = 고객"으로 확인된 곳은 롯데호텔, CJ대한통운, KDDI/Lawson뿐이다. LG, SK, ANA, Mitsui 등은 투자 관계만 확인된다 [research/company.md 5절]
- 롯데호텔의 "30~40% 대체 가능"은 연회 백오피스에 한정된 관계자 발언이다. ROI 자동화율 수치의 근거로 쓰지 말고 "100%는 아니다"라는 정성 근거로만 쓴다 [reference/company--irobotnews-lotte-hotel.md]
- RLDX-1 벤치마크(ALLEX 86.8% vs 39.1%·44.8%)는 자체 평가다. 2차 기사 수치가 1차와 어긋나는 일이 잦으므로(시드1 2,100만 달러 등. "약 90% vs 30% 미만"은 회사 블로그 서술문 자체가 원천, A11 정정) 1차 소스(보도자료, arXiv, GitHub)와 대조한다 [reference/papers--rldx1-tech-report.md]
- 에고센트릭 인간 영상은 규모와 성능 사이에 log-linear 스케일링이 보고됐다(EgoScale, 20,854시간, 22-DoF 손). 고객 작업자 착용 카메라로 데이터를 모으는 RX 전략의 학술 근거다. "54% 향상"은 기준선 대비이며 상대/%p 구분은 미확인 [reference/papers--egoscale.md]
- 공개된 최고 성공률은 80~90%대에 몰려 있다(ACT, 공유 자율, RLDX-1). 평가 조건이 서로 달라 ROI의 현장 가동률 근거로 쓰지 않는다 [research/tech.md 5절]
- 강화학습·교정 개입 결합(π*0.6, 일본 언론 전망)이 다음 흐름이다. RLDX-1도 post-training에 교정 데이터와 RECAP 기반 RL을 선택적으로 둔다(A11 정정, 효과 검증은 1과제) [reference/papers--pistar06-recap.md, reference/tech--xtech-il-rl.md]
- arXiv 초록의 "N% 향상"은 상대인지 %p인지 구분되지 않는 경우가 많다. 본문 확인 전에는 "기준선 대비"까지만 쓴다 [A2 fact-check]
- 한국 빈 일자리는 2025년에 줄었다(미충원 101,000명, -22,000명). 한국 제조 인력난은 "외국인력 497,000명(제조 외국인 취업자 44.8%) 의존" 구조로 서술하고, ROI 프레임은 미충원 해소보다 외국인력 의존 리스크 완화가 후보다(`추정`) [reference/market--moel-vacancy-2025h2.md, reference/market--korea-foreign-workers-2025.md]
- 서비스 로봇 통계는 이동·운반·청소형 중심이고 손 조작 업무는 따로 잡히지 않는다. RX의 미충족 영역은 통계가 아니라 공정 분해 인터뷰에서 찾는다 [reference/market--ifr-service-robots-2025.md]
- 일본은 2025년 국내 로봇 출하 -8.9%, 신규 설치 -19%로 국내 수요가 약하다. 일본 고객에게는 "기존 FA 로봇으로 안 풀리는 잔여 인력"이 제안 포인트다(`추정`) [reference/market--jara-2025-stats.md, reference/market--ifr-industrial-robots-2026.md]
- 촉각·힘을 VLA에 붙이는 시도는 RLDX-1(2026-05)보다 앞선 ForceVLA(2025-05)와 Tactile-VLA(2025-07)에서 이미 나왔다. RLDX-1의 차별점은 촉각 유무가 아니라 고자유도 손, 현장 데이터 파이프라인, 독립 검증 가능성으로 잡는다(본 문서의 해석) [reference/papers--forcevla.md, reference/papers--tactile-vla-arxiv-listing.md]
- 산업 시나리오(케이블 하니스, 커넥터 삽입, 기어박스)를 명시한 공개 평가는 구성당 48회 시행 수준이고 78% 대 36%는 가동률이 아니다. B1 와이어 하니스 후보의 근거는 "확장 단계" 참고로만 쓴다 [reference/papers--industrial-dexterity-benchmark.md]
- 일본에서는 GR00T 계열 PoC(ABEJA×村田製作所, 기사 기준)와 대형 로봇 3사의 VTLA 내재화가 함께 보인다. 일본 고객 제안에서 경쟁 또는 내재화 변수로 본다 [reference/tech--robotstart-abeja-murata.md, reference/tech--xtech-visuotactile-japan.md]
- NVIDIA GR00T N1.7(2026-04)이 EgoScale과 같은 20,854시간 에고센트릭 데이터로 공개됐다. RLDX-1 벤치마크의 비교 상대(N1.6)는 이보다 한 세대 앞서므로 N1.7에는 적용되지 않는다 [reference/competitors--nvidia-groot-n17.md, A6 fact-check]
- 다관절 손은 가격과 DoF가 비례하지 않고(20 DoF급에서 Allegro 약 $15,000 대 Shadow 약 $65,000~110,000, 모두 `추정`), 내구성 수치는 대부분 제조사 자체 시험이다. PoC 시험 항목에 "연속 N시간 가동"을 넣고 B3 ROI에서는 손·겔 교체 주기 비용을 변수로 둔다 [research/hardware.md, reference/papers--orca-hand.md]
- 한·일 부품사가 손과 촉각을 조합하는 사례(Tesollo+XELA, Wonik+DIGIT 360)가 있어 한·일 고객 제안의 조달 가능성 근거가 된다. 일본 FA 3사 VTLA(NEDO 최대 20억 엔)는 경쟁인지 협력 가능성인지 따져야 한다 [reference/hardware--xela-tesollo-integration.md, reference/hardware--sbbit-kawasaki-fanuc-yaskawa-vtla.md]
- 로봇용 깊이 카메라 공급망이 재편 중이다(RealSense 2025-07 Intel 분사, 2026-09 Cognex 인수 발표, 마감 2026 Q4 예정). PoC 하드웨어 선정 시 대체 공급사를 함께 둔다(`추정`) [reference/hardware--calcalist-realsense-cognex.md]
- 한 소스의 수치를 다른 소스 번호에 붙이는 인용 번호 오류가 반복된다. 단일 소스 수치는 그 소스를 직접 단다(Tesla Optimus 25 액추에이터 사례) [A4 fact-check]
- 해외 경쟁사는 사업 방식이 갈린다: 모델 전문(PI), 풀스택 휴머노이드(Figure, Tesla), 산업용 로봇 내장(Skild), 오픈 모델·플랫폼(NVIDIA), 파트너 조기 접근(DeepMind). RLWRLD는 손 특화 모델과 고객 현장 데이터(RX)로 구분되나 자금은 크게 뒤진다(누적 4,100만 달러 대 Skild 단일 라운드 약 14억 달러, 약 34배, 계산) [research/competitors.md]
- 에고센트릭 인간 영상 전략은 RLWRLD만의 것이 아니다(GR00T N1.7, 20,854시간, 22-DoF 손, 자체 주장). 해자는 데이터 방식이 아니라 고객 공정의 현장 데이터와 촉각·기억 통합으로 설명한다 [reference/competitors--nvidia-groot-n17.md]
- DeepMind 블로그는 같은 로봇의 전구 끼우기 36%와 빼기 92%를 함께 보고한다. 손 조작 수치는 같은 작업군의 최고값과 최저값을 같이 적고, 고객에게는 "어떤 작업에서 몇 회 시행한 수치인지"를 먼저 묻는다 [reference/competitors--deepmind-gemini-robotics-2.md, A3 fact-check]
- (A11 정정) RLDX-1에는 교정 데이터와 RECAP 기반 RL이 있다. 다만 RL은 선택 사항이고 효과는 전구 돌리기 1과제의 자체 평가로만 확인된다. 위 "RL 단계가 확인되지 않는다"는 서술을 대체한다 [research/rldx1-tech.md, reference/papers--rldx1-tech-report.md]
- 블로그 서술문("기준선 30% 미만, RLDX-1 거의 90%")은 블로그 Table 4(기준선 평균 39.1, 44.8)와 어긋나고, ALLEX 평균 86.8%에는 성공률이 아닌 진행 점수 과제 2개가 섞여 있다. 회사 수치는 논문 부록의 지표 정의와 시행 수를 확인한 뒤 쓴다 [research/rldx1-tech.md] (A11)
- RLDX-1의 실세계 증거는 과제당 24회 시행, 과제별 시연 40~100개 fine-tune, 해당 모듈만 켠 모델이다. 촉각은 ALLEX가 아니라 Franka 그리퍼 플랫폼에서만 쓰였고, Plug Insertion은 8/24(33.3%, Wilson 95% 구간 약 18~53%, 계산)다. 하네스 PoC에 그리퍼 대조군과 완주율·단계 점수 분리가 필요한 근거다 [research/rldx1-tech.md] (A11)
- Memory 모듈은 순서 추적을 맡고, 실수 복구는 post-training 교정 데이터가 맡는다. case/analysis.md 120행의 서술은 정정 필요하다 [research/rldx1-tech.md] (A11, 2026-10-07 반영 완료)
- 정부 과제 예산은 컨소시엄 전체 금액이고 주관 기업별로 나뉘지 않는 경우가 많다(497억 원은 LG전자 컨소시엄 전체, KT 단독 아님) [reference/competitors--korea-msit-physical-ai-lg-kt.md]
- 투자자 관계가 경쟁사에 걸쳐 있다(NVIDIA는 Figure와 Skild에, Mirae Asset은 RLWRLD 시드1과 Skild에 이름이 있음). 같은 법인인지는 미확인 [reference/competitors--figure-series-c.md, reference/competitors--skild-series-funding.md]
- 웹 요약 모델은 기사 속 회사명을 요약마다 다르게 바꾸는 경우가 있다(nate 한국 RFM 기사: 셀렉트스타, OPTIMUS DX, 삼성DX). 회사명은 원출처로 대조한다 [A3 fact-check]
- WebFetch 요약 모델은 초록에 근거가 없어도 "상대/%p"를 단정한다(같은 ForceVLA 23.2%를 페이지별로 상반되게 답함). 구분은 논문 표의 절대값으로만 확정한다 [A6 fact-check]
- IFR World Robotics는 매년 9월 말에 나온다. 시장 문서 최신성은 이 시점을 기준으로 점검한다. 통계는 집계 범위(회원사만 vs 회원+비회원)가 섞이기 쉬우니 성장률 역산으로 대조한다 [A5 fact-check]
- B1 결정: 케이스 공정은 자동차 와이어 하네스 조립이다. RLWRLD에 맞는 작업군은 산업이 아니라 "유연물 조작 + 정밀 삽입 + 접촉이 많은 조립"으로 정의하는 편이 낫다 [case/candidates.md 결정, reference/case--external-b1-target-analysis.md]
- 잠재 고객을 찾을 때 기업 목록보다 "지금 생산·조립 인력을 채용 중인가"가 더 강한 신호다. 다만 채용 신호는 그 작업이 수작업이라는 증거는 아니다 [reference/case--external-b1-target-analysis.md]
- 하네스 자동화의 가장 큰 장벽은 기술보다 다품종 경제성이다. 업계 대응은 저임금 국가 이전, 설계 재설계(분할 하네스), 전용 셀 세 갈래이고, RFM 제안은 "다품종·소량" 영역으로 한정해야 방어할 수 있다 [reference/case--kyunglim-gyeongsan-robot.md, reference/case--ams-cellios-automated-harness.md] (B2, 미검증)
- 최신 전용 셀도 시제품은 사람보다 느리다(4배 빨라져야 동등). 손 조작 RFM의 ROI는 성공률보다 속도비에서 먼저 갈린다 [reference/case--ams-cellios-automated-harness.md, case/analysis.md 7.5] (B2, 미검증)
- 커넥터 삽입은 그리퍼 + 힘센서로 90% 이상이 보고된다. 다관절 손의 근거는 레이업(전선 훑기·걸기·분기 정리)에 있으므로, PoC에는 그리퍼 대조군을 넣는다 [reference/papers--bc-connector-assembly.md, reference/papers--dexterous-cable-taxonomy.md] (B2, 미검증)
- RLWRLD는 PI·Skild와 같은 "지능 계층" 회사다. 하드웨어·센서·인프라는 생태계 파트너가 맡고, PoC는 자사 랩에서 고객 작업을 재현해 진행한다(KDDI 3개월) [reference/company--rlwrld-business-rx-poc-partnership.md] (A7)
- 파트너십의 외부 가치: 고객 운영 데이터로 만든 모델을 RLWRLD와 함께 상업 제품으로 확장할 수 있다. 셀 구매가 부담인 중견 고객에게 "숙련을 제품으로" 제안할 근거 [reference/company--rlwrld-business-rx-poc-partnership.md] (A7)
- 해외 사례의 첫 작업은 좁고 KPI가 숫자로 고정된 작업이다(Figure-BMW 판금 적재: 목표 84초, 99% 초과, 개입 0회. 달성값은 미공개). 확산까지 1~3년 [research/rx-cases.md] (A7, A10에서 "목표"로 정정)
- Skild AI가 住友電装(Sumitomo Wiring Systems)의 와이어 하네스 조립을 자동화하고 있다. B1·B2의 하네스 케이스에서 RLWRLD의 차별점은 "시연으로 새 품번 적응"(Skild S1도 주장)이 아니라 손이 꼭 필요한 레이업 단계에 있다 [research/skild-pi-deep-dive.md] (A8)
- 지능 계층 회사의 두 갈래: PI는 연구 주도·소수 파트너·일부 가중치 공개·매출 비공개, Skild는 배포 주도·로봇 제조사(ABB, UR) 탑재·ARR 1억 달러. RLWRLD의 RX는 깊지만 느린 세 번째 길 [research/skild-pi-deep-dive.md] (A8)
- 조달 규모: PI 약 21억 달러, Skild 20억 달러 이상, RLWRLD 4,100만 달러(약 50배 차이). LG는 RLWRLD와 Skild 모두에 투자했다 [research/skild-pi-deep-dive.md] (A8)
- RLWRLD 경영진(CBO)의 프레임: "제조 자동화율 70~80%, 남은 20~30%가 손재주 작업". 경쟁력은 모델 코드가 아니라 숙련자 암묵지 데이터, 수집 방식, 배치 경험, 벤치마크(덱스벤치)다. B4 제안서의 "수작업 69%"와 같은 문제 정의 [reference/company--mk-cbo-interview-2026-10.md]
- RLWRLD는 RLDX-1의 가중치·코드·문서를 공개하면서도(비상업 라이선스) 표준(덱스벤치)과 현장 데이터로 해자를 만든다. 오픈소스 + 표준 + 데이터 전략 [reference/company--mk-cbo-interview-2026-10.md]
- 투자자 = 첫 RX 고객 구조는 회사 발표로 확인된다(2026-02 "한국·일본 다수 투자자와 PoC·RX 진행 중"). CJ대한통운 CFO는 목표를 "RFM 공동 고도화 + 물류센터 자율운영 전환"으로 말해, 파트너십의 공동 모델 구조와 일치한다 [reference/company--unicornfactory-seed2.md]
- 1차 보도자료도 KPI를 "목표"로만 쓰는 경우가 있다. 사례 수치는 목표와 달성값을 구분해 읽는다 (Figure-BMW 원문에는 달성값이 없음) [research/poc-playbook.md] (A10)
- 확산 계획과 실적의 격차가 크다: 교촌 2023 청사진 1,300여 점 대 2026-07 25개 점·33대, CJ대한통운 "2026년부터 순차 적용" 대 2026-09 첫 투입 2대. PoC 제안은 확산 수량이 아니라 게이트(통과·중단 기준)로 표현한다 [research/poc-playbook.md] (A10, 해석)
- CJ대한통운 2026-09 용인 투입에서 RLWRLD는 RFM 파트너로 명시됐고, 로보티즈(하드웨어)·에이딘로보틱스(핸드)와 함께 협업한다. RLWRLD 단독 성과는 미공개 [research/poc-playbook.md 7.2절] (A10)
- 확산을 막는 요인은 기술 외적인 것이 많다: 값싼 대안(사람+소프트웨어, Walmart-Bossa Nova 5년 실험 종료), 신뢰성, 노사 수용성(현대차 노조 "노사합의 없이 1대도 안 된다") [research/poc-playbook.md 6절] (A10)

## 열린 질문
다음 리서치 후보. `/rx-status`가 이 목록을 보고 새 작업을 제안한다.
(형식: `- [ ] 질문 (발견한 작업 ID)`, 해결하면 `- [x]`로 바꾸고 답이 있는 파일을 적는다)
- [ ] RLDX-1 가중치의 비상업 라이선스(RLWRLD Model License v1.0) 아래에서 상용 PoC를 어떻게 계약하는가? (A1)
- [ ] RLWRLD의 공개 고객 중 제조업(자동차, 전자) 사례가 있는가? (A1)
- [ ] RLDX-1 벤치마크를 독립적으로 검증한 결과가 있는가? (A1, A3에서 확인)
- [ ] 정부 숙련 데이터 디지털화 사업(기사 표기 약 3,300만 달러)의 정확한 사업명과 규모는? A5에서도 못 찾음. 독파모(업스테이지 컨소시엄) 관련성은 1차 소스 필요 (A1, A5)
- [ ] Lawson 진열 PoC는 계획인가 완료인가, 연도는 언제인가? CJ대한통운 MOU(2025-11)의 1차 소스는 무엇인가? (A1)
- [x] RLDX-1 학습에 RL이나 현장 교정 루프가 있는가? ALLEX 실세계 평가는 몇 개 작업, 몇 회 시행인가? → 있음(선택 사항), 과제당 24회. research/rldx1-tech.md (A2, A11)
- [ ] RLDX-1의 Physics 모듈을 켠 경우와 끈 경우의 정량 차이는? 논문은 그림으로만 제시 (A11)
- [ ] 기준선(pi0.5, GR00T N1.6)은 촉각·토크 입력을 받았는가? (A11)
- [ ] 블로그의 DexBench 5영역과 CBO가 말한 18과제 DexBench의 관계는? 어느 실세계 벤치마크가 DexBench 과제인가? (A11, A1)
- [ ] 전구 돌리기 RL(약 3배)의 프레임 속도와 시행 수는? 다른 과제에도 RL이 적용되었는가? (A11)
- [ ] 사전학습 데이터 혼합 비율(Figure 6, Table 5)과 OpenArm 결과(Figure 16)는? 그림에만 있어 미확인 (A11)
- [ ] 텔레오퍼레이션 "하루 50~200 시연"과 시스템 통합 비용 "하드웨어의 50~200%"의 1차 소스는? B3 ROI 가정에 필요 (A2)
- [ ] π0, π0.5, GR00T N1.6은 촉각·힘 입력을 쓰는가? RLDX-1 차별성 판단에 필요 (A2, A3에서 확인)
- [ ] EgoScale의 +54%는 상대 향상인가 %p 향상인가? KDDI "연 3,500시간 상당"의 단위는? (A2)
- [ ] 와이어 하네스·전자 조립의 수작업 비중(85~90%) 원문 근거는? B1 후보 4번 근거 (A5)
- [ ] 일본 물류 2030년 수송능력 34.1% 부족의 1차 소스(METI/NX総研)는? (A5)
- [ ] 한국 피지컬 AI 실증 사업(2027년 500곳 이상)의 기획예산처 1차 자료와 PoC 참여 조건은? (A5, B4)
- [ ] 손 조작 로봇/RFM 전용 시장 규모 소스가 있는가? 없다면 상향식 SAM 계산 방식은? (A5, B3)
- [ ] IFR 2026판 기준 2025년 로봇 밀도에서 한국이 1위를 유지했는가? (A5)
- [ ] 川崎重工·FANUC·安川電機 VTLA 협력의 1차 소스(발표 자료)와 벤처 기업명, 일정은? (A6, A3에서 확인)
- [ ] GR00T N1.7은 촉각·힘 입력을 쓰는가? NVIDIA 블로그에는 언급 없음. 기존 π0, π0.5 질문과 함께 확인 (A6)
- [ ] ForceVLA 23.2%와 EgoScale 54%는 본문 표에서 상대 향상인가 %p 향상인가? (A6)
- [ ] ForceVLA 이후 RLDX-1의 Physics 모듈을 같은 조건(ALLEX 또는 동일 작업)에서 비교한 결과가 있는가? (A6)
- [ ] Industrial Dexterity Benchmark v3(2026-09-21) 개정에서 수치가 바뀌었는가? (A6)
- [ ] 평행 그리퍼로 풀리지 않는 공정의 경계는 어디인가? B1에서 공정별 end-effector 후보를 매핑 (A4)
- [ ] Shadow, Sharpa, Allegro, Tesollo, Inspire의 공식 가격과 리드타임은? Inspire 공식 $24,399.99는 어떤 구성의 값인가? B3 가정값에 필요 (A4)
- [ ] 다관절 손의 연속 가동 신뢰성(MTBF 등)에 현장 데이터가 있는가? Sharpa 40 kg payload와 150 N 파지력은 어떤 조건에서 정합하는가? (A4)
- [ ] RLDX-1은 손 종류를 바꿀 때 재학습이 얼마나 필요한가? (A4, A1)
- [ ] 일본·한국 산업용 그리퍼 업체(SMC, 로보티스 등)와 대면적 전자피부의 상용 제품은? (A4)
- [ ] RLDX-1을 π0.7, GR00T N1.7과 동일 조건으로 비교한 공개 결과가 있는가? π0.7, N1.7, Gemini Robotics 2는 촉각·힘 입력을 쓰는가? (A3)
- [ ] GR00T N1.7의 정확한 라이선스 조항은? 오픈 모델이 상용 PoC에서 RLDX-1(비상업 가중치)의 대체재가 되는가? (A3, A1)
- [ ] 일본 국내 경쟁 주체(SoftBank 컨소시엄, NEDO 기반모델 사업, AIRoA)의 1차 소스는? 일본어 소스가 1건뿐 (A3)
- [ ] 한국 국내 RFM 기업(KT, NC AI 등)의 모델과 손 조작 수준은? nate 기사의 삼성DX 협력과 RLDX-1 개발사 표기를 이데일리 원문으로 확인 (A3)
- [ ] Telexistence의 Lawson 배치 실적과 RLWRLD-KDDI-Lawson PoC의 경쟁·중복 여부는? (A3, A1)
- [ ] LG 계열 투자 주체(LG전자 본체 대 LG Technology Ventures 등)는 법인이 같은가? PI 시리즈C(약 10.5억 달러)의 정식 발표 여부는? (A3)
- [ ] Tesla Optimus 현행 손 사양: Musk 4월 발언(설계 변경)과 Tech Times 9월 서술(22 DoF)을 가를 1차 소스가 있는가? (A4, A3)
- [ ] 국내 하네스 기업(경신, 유라코퍼레이션 등)의 2022년 이후 국내 조립 라인 규모와 리쇼어링 현황은? (B1)
- [ ] 하네스 조립을 노동집약·자동화 난제로 규정한 국내 R&D 자료(GAFIC)의 원문은? (B1)
- [ ] 국내 하네스 라인의 실제 인원, 교대, 택트, 품번 수와 외국인 비중은? 경신 국내 사업장 4곳은 하네스 조립 라인인가? (B2)
- [ ] 住友의 자동화율 약 15%와 약 50%는 공수 기준인가, 공정 수 기준인가? (B2)
- [ ] Cellios/TE 셀의 가격과 품번 전환 시간은? (B2, B3)
- [ ] RLDX-1을 산업용 협동로봇과 손 조합으로 옮길 때 재학습 규모와 상용 라이선스 조건은? (B2, A1)
- [ ] 2020년 중기부의 하네스 리쇼어링 자동화 지원(2년 최대 10억 원)은 지금도 이어지는가? (B2, B4)
- [ ] RLWRLD RX 진단의 기간과 비용은? (A7)
- [ ] Telexistence × Physical Intelligence 음료 보충과 RLWRLD × KDDI 진열 PoC는 어떻게 다른가? (A7, A3)
- [ ] Skild의 住友電装 하네스 프로젝트 범위·결과와 사용하는 손 하드웨어(다관절 손인가 그리퍼인가)는? (A8, B2)
- [ ] RLWRLD 하드웨어 파트너(레인보우, 원익, 로보티즈, 위로보틱스)가 Skild-ABB처럼 모델을 탑재해 판매하는 OEM 채널이 될 수 있는가? (A8)
- [ ] 덱스벤치 18개 과제 목록과 하네스·커넥터 삽입 유사 과제가 있는가? (A1, B4)
- [x] 글로벌 오픈 벤치마크 8종은 무엇인가? → 6개 스위트의 8개 점수 열로 추정 (research/rldx1-tech.md 9절 14번, A11)
- [ ] CJ대한통운이 레인보우로보티즈와 협업을 종료한 사유, RLWRLD-CJ PoC의 KPI와 결과는? (A10)
- [ ] Figure-BMW 최종 달성값(정확도, 개입 횟수)의 출처는? (A10)
- [ ] Mujin PoC의 실제 기간·검증 절차 1차 소스(일본어)는? (A10)
- [ ] PoC 단계 대가(무상·유상·공동 부담)를 밝힌 로봇 사례가 있는가? RLWRLD RX·PoC 가격 구조는? (A10, A7)
