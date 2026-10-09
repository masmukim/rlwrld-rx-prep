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
| 덱스벤치 | DexBench | RLWRLD가 고객 현장 워크플로 분석 데이터로 만든 18개 과제의 손재주 평가 벤치마크. NVIDIA Isaac Lab-Arena와 연결 | reference/company--mk-cbo-interview-2026-10.md (2026-10-09 Q5: 사이트 기준 18과제 55케이스, 5영역은 분류축, 평가 프로토콜·리더보드·코드 비공개, Arena 통합은 Coming Soon, 2026-08 발표는 80케이스로 수치 불일치) |
| OSC | Object State Complexity | DexBench의 난이도 6축 벡터(C_geom, C_force, C_contact, C_obs, C_deform, C_dyn) | reference/benchmark--dexbench-site.md |
| 브레이크다운 커브 | Breakdown Curves | 성공률 대신 성능이 무너지는 파라미터 범위를 보는 DexBench 설계 원칙 | reference/benchmark--dexbench-site.md |
| 서브태스크 술어 | Subtask Predicates | Isaac Lab-Arena 0.3의 단계별 마일스톤 추적 기능. 단계 점수 구현 후보 | reference/benchmark--arena-release-0-3.md |
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
| 투자자 겸 고객 | Investor-customer | 공급사에 지분을 투자한 기업이 첫 고객이 되는 구조. Schaeffler–Agility, Mercedes–Apptronik, Magna–Sanctuary | reference/case--agility-schaeffler.md |
| 구매 의향 계약 | Intent-to-purchase agreement | 확정 발주가 아닌 "intends to purchase" 수준의 계약(Schaeffler 공장 100곳) | reference/case--agility-schaeffler.md |
| 숙련공 데이터 | 熟練工のデータ | 정년 전 숙련공의 동작을 카메라·센서로 디지털화해 모방학습 자산으로 삼는 것(矢崎) | reference/case--yazaki-ren-kurumanews.md |
| 상사 경유 진입 | Trading-house channel | 일본 종합상사가 투자, 독점 유통, 금융을 포함한 합작사로 해외 로봇사의 일본 채널이 되는 구조(住友商事–Dexterity) | reference/case--dexterity-sumitomo-jv.md |
| セット工法 | Set operation | 절단·압착한 전선(切圧線)을 자동으로 세트해 리드타임을 줄이는 住友電装 공법 | reference/case--sei-id-v20-04-harness-casee.md |
| e-STEALTH W/H | e-STEALTH Wire Harness | 플랫 구조(융착, 알루미늄 도체)의 차세대 하네스. 에어리어 하네스 간선용, 자동 조립에 유리 | reference/case--sei-id-v28-04-estealth.md |
| 누적 단계별 성공률 | Cumulative per-step success rate | Skild S1 블로그 지표. 실패 시 사람이 개입해 복구하고 전 단계를 채점한 평균 | reference/competitors--skild-s1-blog.md |
| 모델 라인 | Model line | 신공법을 먼저 적용한 특정 시범 라인. 이 라인의 수치는 전사 값이 아님(住友 50%) | reference/case--sumitomo-sws-local-automation.md |
| 국소적 자동화 | 局部的な自動化 | 住友電装 사장이 자사 하네스 자동화 현황을 표현한 말. 50%를 전사 값으로 읽으면 안 된다는 근거 | reference/case--sei-id-v20-04-harness-casee.md |

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
- 한국 빈 일자리는 2025년에 줄었다(미충원 101,000명, -22,000명). 한국 제조 인력난은 "제조업 외국인 취업자 497,000명(전체 외국인 취업자 대비 44.8%, 기사 인용·1차 미확인)" 구조로 서술하고, ROI 프레임은 미충원 해소보다 외국인력 의존 리스크 완화가 후보다(`추정`, 하네스 업종에서는 Q1이 미검증으로 판정) [reference/market--moel-vacancy-2025h2.md, reference/market--korea-foreign-workers-2025.md]
- 서비스 로봇 통계는 이동·운반·청소형 중심이고 손 조작 업무는 따로 잡히지 않는다. RX의 미충족 영역은 통계가 아니라 공정 분해 인터뷰에서 찾는다 [reference/market--ifr-service-robots-2025.md]
- 일본은 2025년 국내 로봇 출하 -8.9%, 신규 설치 -19%로 국내 수요가 약하다. 일본 고객에게는 "기존 FA 로봇으로 안 풀리는 잔여 인력"이 제안 포인트다(`추정`) [reference/market--jara-2025-stats.md, reference/market--ifr-industrial-robots-2026.md]
- 촉각·힘을 VLA에 붙이는 시도는 RLDX-1(2026-05)보다 앞선 ForceVLA(2025-05)와 Tactile-VLA(2025-07)에서 이미 나왔다. RLDX-1의 차별점은 촉각 유무가 아니라 고자유도 손, 현장 데이터 파이프라인, 독립 검증 가능성으로 잡는다(본 문서의 해석) [reference/papers--forcevla.md, reference/papers--tactile-vla-arxiv-listing.md]
- 산업 시나리오를 명시한 공개 평가(Industrial Dexterity Benchmark)는 구성당 48회 시행 수준이고, v3(2026-09-21) 기준 76% 대 36%(v1 초록은 78%)는 데이터센터 케이블 청소 보드(Board #1) 한 과제의 결과다. 자동차 하네스 보드(Board #2)는 설계만 있고 성능 결과가 없으며, 이 수치는 가동률이 아니다. B1 와이어 하니스 후보의 근거는 "확장 단계" 참고로만 쓴다 [reference/papers--industrial-dexterity-benchmark.md] (2026-10-09 fact-check 정정)
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
- RLDX-1의 실세계 증거는 ALLEX 4과제 과제당 24회 시행(FR3는 24회가 기본이나 일부 과제는 96회·54회 상호작용, Egg PnP 61.1%는 24회로 정수가 안 되어 시행 수 불명확), 과제별 시연 40~100개 fine-tune, 해당 모듈만 켠 모델이다. 촉각은 ALLEX가 아니라 Franka 그리퍼 플랫폼에서만 쓰였고, Plug Insertion은 8/24(33.3%, Wilson 95% 구간 약 18~53%, 계산)다. 하네스 PoC에 그리퍼 대조군과 완주율·단계 점수 분리가 필요한 근거다 [research/rldx1-tech.md] (A11)
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
- (Q2 정정 2026-10-09) 住友電装는 2026-09-17 Skild와 하네스용 피지컬 AI 로봇 공동 개발을 시작했다(1차 소스). 대상 공정, 손 하드웨어, 일정, 성과는 미공개이고, 기존 "이미 자동화하고 있다"는 기사 표현이 1차보다 강했다. "레이업이 우리 차별점"은 Skild 범위가 미공개이므로 "우리가 그리퍼 대조군과 함께 검증하는 단계"로 쓴다 [research/q2-skild-sumitomo-harness.md, reference/case--sws-skild-joint-dev-release.md]
- 지능 계층 회사의 두 갈래: PI는 연구 주도·소수 파트너·일부 가중치 공개·매출 비공개, Skild는 배포 주도·로봇 제조사(ABB, UR) 탑재·ARR 1억 달러. RLWRLD의 RX는 깊지만 느린 세 번째 길 [research/skild-pi-deep-dive.md] (A8)
- (2026-10-09 fact-check 정정) 조달 비교는 기준을 밝힌다. RLWRLD 누적 4,100만 달러 대 Skild 단일 라운드 약 14억 달러 = 약 34배(계산). 누적은 Skild 확인 하한 약 17억 달러(2024 시리즈A 3억 + 2026 시리즈C 14억, `추정`), PI 확정 라운드 합 약 10.7억 달러(미발표 시리즈C 포함 약 21억, `추정`)이며 확정 라운드만 합치면 Skild가 PI보다 크다. "약 50배", "Skild 20억 이상"은 폐기. LG는 RLWRLD와 Skild 모두에 투자했다 [research/skild-pi-deep-dive.md] (A8)
- RLWRLD 경영진(CBO)의 프레임: "제조 현장 자동화율이 70~80% 수준이라고 보면 나머지 20~30%에 손재주 작업이 남는다"는 가정형 발언이며 통계가 아니다(분모·출처 없음, 69%와 병치하지 않는다). 경쟁력은 모델 코드가 아니라 숙련자 암묵지 데이터, 수집 방식, 배치 경험, 벤치마크(덱스벤치)다. 인터뷰 게재일은 raw 입력 표기 2026-09-08(확정 보류) [reference/company--mk-cbo-interview-2026-10.md] (2026-10-09 fact-check 정정)
- RLWRLD는 RLDX-1의 가중치·코드·문서를 공개하면서도(비상업 라이선스) 표준(덱스벤치)과 현장 데이터로 해자를 만든다. 오픈소스 + 표준 + 데이터 전략 [reference/company--mk-cbo-interview-2026-10.md]
- 2026-02 기사 서술에 따르면 RLWRLD는 한국·일본 다수 투자자와 PoC·RX 프로젝트를 진행 중이었다(기자 서술). "투자자 = 첫 RX 고객" 구조는 본 팀 해석이다. CJ대한통운 CFO(이종훈)는 "물류 현장에 바로 적용 가능한 로봇 파운데이션 모델을 공동으로 고도화하고 물류센터의 AI 기반 자율운영 전환을 가속화해 나가겠다"고 말했다 [reference/company--unicornfactory-seed2.md] (2026-10-09 fact-check 정정)
- 1차 보도자료도 KPI를 "목표"로만 쓰는 경우가 있다. 사례 수치는 목표와 달성값을 구분해 읽는다 (Figure-BMW 원문에는 달성값이 없음) [research/poc-playbook.md] (A10)
- 확산 계획과 실적의 격차가 크다: 교촌 2023 청사진 1,300여 점 대 2026-07 25개 점·33대, CJ대한통운 "2026년부터 순차 적용" 대 2026-09 첫 투입 2대. PoC 제안은 확산 수량이 아니라 게이트(통과·중단 기준)로 표현한다 [research/poc-playbook.md] (A10, 해석)
- CJ대한통운 2026-09 용인 투입에서 RLWRLD는 RFM 파트너로 명시됐고, 로보티즈(하드웨어)·에이딘로보틱스(핸드)와 함께 협업한다. RLWRLD 단독 성과는 미공개 [research/poc-playbook.md 7.2절] (A10)
- 확산을 막는 요인은 기술 외적인 것이 많다: 값싼 대안(사람+소프트웨어, Walmart-Bossa Nova 5년 실험 종료), 신뢰성, 노사 수용성(현대차 노조 "노사합의 없이 1대도 안 된다") [research/poc-playbook.md 6절] (A10)
- (Q4, 2026-10-09 fact-check 정정) 타사 표 24행(공급사 기준, 고객 미공개 행 포함) 중 투자자·모회사가 고객인 경우는 확인 4건(Schaeffler–Agility, Mercedes–Apptronik, Hyundai 그룹–Boston Dynamics, Magna–Sanctuary), 유통 채널 1건(住友商事–Dexterity), 관계 추정 1건(KDDI–Telexistence)으로 최대 6건이다(NVIDIA는 투자자일 뿐 고객이 아님). RLWRLD 공개 고객 3곳(롯데, CJ대한통운, KDDI/Lawson)도 투자자·그룹사 구조다. 첫 작업은 대부분 그리퍼로 되는 pick-and-place이며, 손 조작이 결정적인 작업 사례는 Foxconn 나사 체결과 住友電装 하네스(공동 개발 단계) 정도다 [case/candidates.md Q4.1]
- (Q4, 2026-10-09 fact-check 정정) 첫 고객 점수 기준(제안) 7개로 매기면 관계 없는 하네스 신규 후보(矢崎 3.70, 경림테크형·유라 3.30, 경신 3.10)는 기존 투자자 고객(KDDI 4.15, 롯데 4.10, CJ 3.95)보다 낮다. C1(투자 관계)을 빼면 矢崎(4.38)만 기존 고객보다 앞서고 경림·유라(3.88)는 롯데와 동점으로 KDDI(3.94)보다 낮다(이전 "경림 4.00이 KDDI보다 앞선다"는 폐기). C1 5점=투자자이면서 현장 접근 공개, 4점=투자만 있음. 첫 유인은 정부 실증 재원, RLWRLD 랩 PoC, 숙련 데이터 권리 배분이다(모두 `추정`, 기준·가중치는 본 팀 제안) [case/candidates.md Q4.2~Q4.3]
- (Q4) 矢崎는 "지금은 휴머노이드가 필요 없다, 도입 이유는 숙련공 데이터 수집"이라 공개 발언했고 2029~2030년 숙련공 재현 피지컬 AI를 로드맵에 넣었다. RLWRLD의 암묵지 논리와 같으나 데이터를 자사 경쟁력으로 보므로 데이터 권리가 협상 쟁점이다 [reference/case--yazaki-ren-kurumanews.md]
- (Q4) 일본 하네스·유연물 영역은 住友電装–Skild, 安川×SoftBank(VLA 하네스 상자 수납 실증), FA 3사 VTLA 등 여러 진영이 이미 들어와 있다. 한국 하네스사는 공개된 RFM 협력이 없어 상대적으로 비어 있다(해석) [reference/case--yaskawa-softbank-harness.md]
- (Q4) KDDI는 RLWRLD와 Telexistence(시리즈 B)에 모두 투자했고 Lawson 의결권 50%(三菱商事와 각 50%)를 가진다. 투자자가 그룹사 현장을 여러 로봇사에 동시에 여는 구조라 기존 고객 안에서도 경쟁이 있다 [reference/company--kddi-lawson-50pct.md]
- (Q1) 국내 하네스사의 국내 생산 인력은 작다(유라 2023 국내 생산직 668명, 국내외 합계의 2.8%, 계산). "국내 라인 수천 개 확산"은 근거가 없고 "국내 소수 라인 PoC → 해외 거점 확산"이 방어 가능하다(`추정`). 외국인력 의존 완화 프레임은 이 업종에서 미검증 [research/q1-harness-line-facts.md]
- (Q3) 업계 대형사의 "자동화율"에는 분모가 없다. 15%·50%는 방향성 근거로만 쓰고 ROI 입력값이나 "수작업 69%"(작업장 수 기준)와 병치하지 않는다. 고객 킥오프에서 분모(직접 공수 SMH, 작업장 수)를 먼저 합의한다 [research/q3-sumitomo-automation-rate.md]
- (Q2·Q3) 기사가 1차 소스의 시제를 강하게 바꾸는 패턴이 반복된다(Humanoids Daily "Automating" 대 Skild "working towards deploying", 住友 영어판 "has been increased" 대 일본어 "高められる"). 경쟁사·고객 사례는 1차 문장의 시제와 원어판까지 확인한다 [research/q2-skild-sumitomo-harness.md, research/q3-sumitomo-automation-rate.md]
- (fact-check) Skild 매출은 조작(manipulation) 약 90%, Mobility 10%이다(회사 블로그 1차). "86%"는 폐기 [reference/competitors--skild-hidden-pillar.md]
- (fact-check) Skild 고객 단계: Mitsui & Co.는 piloting(상업 주방 시범), 住友電装는 working towards deploying이다. 둘 다 배포 완료가 아니며 기사 표현 "Automating"은 1차보다 강하다 [reference/competitors--skild-hidden-pillar.md]
- (fact-check) B2 예비 회수(손 구성 셀 395,584,000원, 기본 시나리오)는 5.7년이 손 교체비 제외 값이다. 손 1개를 연 1회 교체하면 약 10.6년, 2개면 약 77년, 2개를 3년 주기로 교체하면 약 8.2년이다. 속도비 0.5는 PoC의 기술 가능성 게이트이며 ROI 성립 기준이 아니다(회수 15.9년, 교체비 포함 시 음수). 5년 회수에는 연 순절감 약 7,912만 원이 필요하다. 손 교체 주기가 B3의 핵심 변수다 [case/analysis.md 7.5절]
- (fact-check) 기사 속 "업계 일반 단가"를 특정 기업의 구매가로 옮기지 않는다(교촌 조리 로봇 2,000만 원·설치 포함 4,000만 원은 A 제조사 기준 업계 단가이고 교촌 구매가는 미공개). "N개월 내" 기간은 상한이라 두 값의 차이는 실제 간격이 아니다(Figure 4개월은 최대 약 4개월). 계획("300점 확대")을 달성으로 쓰지 않는다(Telexistence-FamilyMart) [research/poc-playbook.md, research/rx-cases.md]
- (fact-check) 표의 비율값을 시행 수로 나눠 정수가 되는지 검산하면 원문 내부 모순을 잡는다(Egg PnP 61.1%는 24회로 불가). 한편 검증 에이전트(haiku)가 이미지 캡션을 놓쳐 "근거 없음"으로 잘못 판정한 사례가 있다(Skild 슬로건, FR3 카메라). "확인불가" 판정은 raw 재확인 후 반영한다 [research/rldx1-tech.md]
- (Q5) DexBench의 현재 실체는 과제 정의 문서다. 사이트(Documentation v1.0)에는 18과제·55케이스·5영역·OSC 6축·케이스별 초기/목표 상태와 실패 조건만 있고, 리더보드·시행 수·점수 산식·제출 절차·하드웨어·라이선스·코드 링크가 없다. RLWRLD GitHub(7개 저장소)·HF(모델 11개, 데이터셋 0개)에도 DexBench 코드·데이터가 없다(2026-10-09 스냅샷). 인용은 "18과제, 사이트 기준 55케이스"로 시점을 붙인다 [research/q5-dexbench.md]
- (Q5) DexBench의 개발 주체는 RLWRLD다(사이트 푸터 "Published by RLWRLD", RLDX-1 논문 기여자 절). NVIDIA는 Arena 통합 협력사이고 롯데·CJ·ANA·Mitsui 같은 파트너는 RLWRLD 투자자·고객 관계가 있어 독립성의 근거가 못 된다. DexBench는 하드웨어 비종속("두 손가락 그리퍼가 5지 손보다 능숙할 수 있다")이라 B4 그리퍼 대조군과 같은 쪽이다 [research/q5-dexbench.md]
- (Q5) 사이트의 영역 태그는 사이트가 제시한 병목 규칙으로 재현되지 않는 경우가 있다(Task 3의 E5, Task 7의 E3). 영역 태그를 정량 근거로 쓰지 않는다. 일부 케이스는 앞 케이스의 결과를 시작 상태로 쓴다(4-A는 3-D, 13-B는 12-A) [research/q5-dexbench.md]
- (Q6) 住友電装는 자사 중기계획 자료(일·영)에 "グローバルシェアNo.1"과 자동차용 하네스 세계 점유율 21%(2025년도)를 적었다. 자사 표기이고 No.1의 연도는 불확정이며 제3자 확인은 없다. "업계 1위권은 근거 없음" 정정은 1차 소스 Grep 없이 한 것이라 틀렸고, "자사 자료 기준 세계 점유율 1위(2025년도 21%, 제3자 미확인)"로 쓴다 [research/q6-sws-pdf.md, reference/case--sws-midterm-plan-2028-en.md]
- (Q6) 사용자 제공 영문 PDF는 2026-09-17 Skild 공동 개발 릴리스의 영어판이며 일본어판과 정보가 같다. 대상 공정·로봇·핸드·센서·일정·성과·자동화율 정의는 없다. 서술 강도는 일본어 기준 "개시/도입한다/추진한다/목표한다"까지이고 영어판이 약간 강하다("This will enable robots to…"). 중기계획 발표일은 2026-07-16이고 수치 목표 슬라이드에 자동화율 목표는 없다 [research/q6-sws-pdf.md]
- (Q6) 같은 회사 자료의 "모델 라인"이 두 맥락에 쓰인다: 자동화율 50% 문장의 세트 공법·분할 하네스 모델 라인, 중기계획 2027-2028 스마트 팩토리 모델 라인. 같은 라인이라는 근거가 없으므로 구분한다 [research/q6-sws-pdf.md]

## 열린 질문
다음 리서치 후보. `/rx-status`가 이 목록을 보고 새 작업을 제안한다.
(형식: `- [ ] 질문 (발견한 작업 ID)`, 해결하면 `- [x]`로 바꾸고 답이 있는 파일을 적는다)
- [ ] RLDX-1 가중치의 비상업 라이선스(RLWRLD Model License v1.0) 아래에서 상용 PoC를 어떻게 계약하는가? (A1)
- [ ] RLWRLD의 공개 고객 중 제조업(자동차, 전자) 사례가 있는가? (A1)
- [ ] RLDX-1 벤치마크를 독립적으로 검증한 결과가 있는가? (A1, A3에서 확인) → DexBench는 RLWRLD 자체 벤치마크이고 공개 리더보드·코드·데이터가 없어 독립 검증 근거가 못 된다(2026-10-09 기준). 그 밖의 독립 검증도 못 찾음 (Q5)
- [ ] 정부 숙련 데이터 디지털화 사업(기사 표기 약 3,300만 달러)의 정확한 사업명과 규모는? A5에서도 못 찾음. 독파모(업스테이지 컨소시엄) 관련성은 1차 소스 필요 (A1, A5)
- [ ] Lawson 진열 PoC는 계획인가 완료인가, 연도는 언제인가? CJ대한통운 MOU(2025-11)의 1차 소스는 무엇인가? (A1)
- [x] RLDX-1 학습에 RL이나 현장 교정 루프가 있는가? ALLEX 실세계 평가는 몇 개 작업, 몇 회 시행인가? → 있음(선택 사항), 과제당 24회. research/rldx1-tech.md (A2, A11)
- [ ] RLDX-1의 Physics 모듈을 켠 경우와 끈 경우의 정량 차이는? 논문은 그림으로만 제시 (A11)
- [ ] 기준선(pi0.5, GR00T N1.6)은 촉각·토크 입력을 받았는가? (A11)
- [x] 블로그의 DexBench 5영역과 CBO가 말한 18과제 DexBench의 관계는? → 5영역은 분류축, 18과제는 과제이며 한 과제에 영역이 2~4개 중복 태그된다. 같은 벤치마크의 다른 층이다. 다만 RLDX-1 논문의 실세계 과제는 DexBench 케이스로 표기되지 않았다. research/q5-dexbench.md (A11, A1, Q5)
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
- [ ] 국내 하네스 라인의 실제 인원, 교대, 택트, 품번 수와 외국인 비중은? 경신 국내 사업장 4곳은 하네스 조립 라인인가? → 라인 단위 국내 수치 없음, 경주만 하네스 확인, 유라 국내 직접고용 외국인 1/2,080. 현직자 인터뷰 필요 (B2, Q1)
- [ ] 住友의 자동화율 약 15%와 약 50%는 공수 기준인가, 공정 수 기준인가? → 1차 소스 5건에 분모 없음, "全工程の約15%"라는 서술만 있어 공정 쪽 정황. 정의 미확정 (B2, Q3)
- [ ] Cellios/TE 셀의 가격과 품번 전환 시간은? (B2, B3)
- [ ] RLDX-1을 산업용 협동로봇과 손 조합으로 옮길 때 재학습 규모와 상용 라이선스 조건은? (B2, A1)
- [ ] 2020년 중기부의 하네스 리쇼어링 자동화 지원(2년 최대 10억 원)은 지금도 이어지는가? (B2, B4)
- [ ] RLWRLD RX 진단의 기간과 비용은? (A7)
- [ ] Telexistence × Physical Intelligence 음료 보충과 RLWRLD × KDDI 진열 PoC는 어떻게 다른가? (A7, A3)
- [ ] Skild의 住友電装 하네스 프로젝트 범위·결과와 사용하는 손 하드웨어(다관절 손인가 그리퍼인가)는? → 공개 1차 소스에 없음(공동 개발 개시까지). 영상·구상도·유료 기사 필요, manual-research.md 5절 (A8, B2, Q2)
- [ ] RLWRLD 하드웨어 파트너(레인보우, 원익, 로보티즈, 위로보틱스)가 Skild-ABB처럼 모델을 탑재해 판매하는 OEM 채널이 될 수 있는가? (A8)
- [x] 덱스벤치 18개 과제 목록과 하네스·커넥터 삽입 유사 과제가 있는가? → 목록 확보(사이트 기준 18과제 55케이스). 유사 과제는 Task 3의 3-B(USB-A)·3-C(110V 플러그)와 Task 10의 10-A·10-B이고 하네스 직결 과제는 없다. research/q5-dexbench.md (A1, B4, Q5)
- [x] 글로벌 오픈 벤치마크 8종은 무엇인가? → 6개 스위트의 8개 점수 열로 추정 (research/rldx1-tech.md 9절 14번, A11)
- [ ] CJ대한통운이 레인보우로보티즈와 협업을 종료한 사유, RLWRLD-CJ PoC의 KPI와 결과는? (A10)
- [ ] Figure-BMW 최종 달성값(정확도, 개입 횟수)의 출처는? (A10)
- [ ] Mujin PoC의 실제 기간·검증 절차 1차 소스(일본어)는? (A10)
- [ ] PoC 단계 대가(무상·유상·공동 부담)를 밝힌 로봇 사례가 있는가? RLWRLD RX·PoC 가격 구조는? (A10, A7)
- [ ] 矢崎 REN의 휴머노이드 제조사와 숙련 데이터 수집 방식은? 외부 협업을 모집하는가? (Q4)
- [ ] 2027 피지컬 AI 실증 공모의 중소제조 분야 수요기업·공급기업 조건은? (Q4)
- [ ] 경신이 住友電装–Skild 성과를 도입할 계획이 있는가? (Q4, Q2)
- [ ] Agility–Schaeffler 구매 의향은 실제 배치로 이어졌는가? Dexterity–住友商事 1,500대 목표는 달성됐는가? (Q4)
- [ ] 유라의 "현대차·기아 하네스 독점 공급" 기사 표현과 2020년 점유율 48.2%는 어떻게 맞춰지는가? (Q4)
- [ ] Skild 본사는 캘리포니아인가 피츠버그인가? (住友電装 릴리스와 기존 문서 불일치) (Q2) → 住友電装 일본어 릴리스와 영문 릴리스 모두 "California"로 같다. 같은 발행처의 번역본이라 독립 확인은 아니며 불일치는 그대로 (Q6)
- [ ] 住友 분할 하네스(4~5모듈)와 e-STEALTH W/H 간선 하네스는 같은 개념인가? 2025 목표 이후 양산 상태는? (Q3)
- [ ] 참고 라인의 작업장별 사이클 타임으로 "수작업 69%"를 공수 비중으로 환산하면 얼마인가? (논문 Fig. 7 필요) (Q3)
- [ ] RLDX-1 논문 FR3 Egg PnP의 실제 시행 수(24회인가 72회인가)와 Spin Tracking 96회·Pong Game 54회의 출처 위치는? (A11)
- [ ] Skild 2025년 라운드(시리즈B) 금액과 누적 총액은? (A8)
- [ ] Dexterity–FedEx 협력의 시작 시점(2023 주장 미확인)과 Figure-BMW 시험·본 라인 투입의 정확한 월은? (A7, A10)
- [ ] 참고 라인의 "lay-up 4"는 작업장이 늘어난 것인가 작업자만 늘어난 것인가? (논문 Figure 9, 11 필요) (B2)
- [ ] 다관절 손의 현장 교체 주기와 유지보수비 중 손 교체 비중은? B3 회수 계산의 핵심 변수 (B2, B3)
- [ ] 2027년 최저임금 고시 값은? 하한 시나리오 갱신에 필요 (B2)
- [ ] 롯데그룹 국책 과제(롯데글로벌로지스)가 호텔 연회 백오피스 PoC의 정부 재원으로 이어지는가? 법인이 달라 C5 4점이 과대일 수 있다 (Q4)
- [ ] Telexistence와 PI의 관계는 무엇인가? 편의점 영역에서 겹치는가? (Q4)
- [ ] 매일경제 CBO 인터뷰의 실제 게재일은? raw 입력 표기는 2026-09-08 (A1)
- [ ] DexBench 평가 프로토콜(시행 수, 채점, 합격 기준, 제출·검증)은 비공개 문서에 있는가? 55케이스(사이트)와 80케이스(2026-08 발표)의 차이는? (Q5)
- [ ] NVIDIA Isaac Lab-Arena의 DexBench 통합은 언제 공개되는가? RLWRLD/IsaacLab-Arena의 dexbench 브랜치 재확인 (Q5)
- [ ] DexBench 파트너 표기 "Fuji Electric"(사이트)과 링크 fuji.co.jp, 8월 발표 "Fuji"는 같은 회사인가? (Q5)
- [ ] RLDX-1 GitHub 저장소는 Apache-2.0으로 표기되는데 가중치 비상업 라이선스(RLWRLD Model License v1.0)와의 관계는 코드와 가중치의 구분인가? (Q5, A1)
- [ ] 住友電装의 "Global Market Share No.1"은 어느 연도·어느 기준이며 제3자 자료로 확인되는가? 중기계획의 2027-2028 모델 라인과 자동화율 50%의 모델 라인은 같은 라인인가? (Q6)
