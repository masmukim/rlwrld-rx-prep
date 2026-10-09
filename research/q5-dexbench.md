# 덱스벤치(DexBench) 공식 사이트 분석: 무엇이 공개되어 있고 무엇이 없는가
조사일: 2026-10-09 (Q5. 이번 세션에서 저장한 원문만 사용. 저장했으나 읽지 못한 자료는 사용자 피딩 요청 목록에 표시)

## 핵심 요약
- **DexBench는 현재 "과제 정의 문서"다.** dexbench.org(Documentation v1.0)에는 18개 과제, 55개 평가 케이스, 5영역 분류, 케이스별 초기 상태·목표 상태·실패 조건, 구매 가능한 물체 목록만 있다. 리더보드, 시행 수, 점수 산식, 제출·검증 절차, 하드웨어 플랫폼, 라이선스, 코드·데이터 링크는 사이트에서 확인되지 않았다 [1]. 2026-10-09 기준 GitHub(RLWRLD 조직, Arena 포크)와 Hugging Face에서도 DexBench 코드·데이터·체크포인트를 찾지 못했고, NVIDIA Arena 저장소는 DexBench 통합을 "coming soon"으로 적고 있다 [4][6].
- **주체는 RLWRLD이며 독립 벤치마크가 아니다.** 사이트 푸터가 "Published by RLWRLD"이고 RLDX-1 논문 기여자 절에 DexBench 설계자가 명시되어 있으며, 블로그는 이 분류를 RLDX-1 부품 설계 논거로 쓴다 [1][7][8]. NVIDIA는 Arena 통합 협력사이고, 파트너 기업 일부는 RLWRLD 투자자·고객이다. 독립 검증 결과는 확인되지 않았다(열린 질문 답: "없음").
- **하네스 직결 과제는 없다.** 가장 가까운 것은 Task 3(Precision Insertion)의 3-B(USB-A)·3-C(110V 플러그)와 Task 10(Cable Winding)의 10-A·10-B다. B4 8.3절은 "덱스벤치 형식으로 케이스 카드를 쓰고 인접 과제를 표기"하는 수준으로 맞추고, 공식 호환·인증은 주장하지 않는다. 또 "18과제"와 "Five Regimes"는 대립 개념이 아니라 과제(18)와 분류축(5)이다.

## 본문

### 1. 소스 접근과 문서 성격
| 항목 | 확인된 내용 | 출처 |
|------|-------------|------|
| 렌더링 | 홈 HTML을 단순 수집하면 87자만 남는다(JS 렌더링). WebFetch 요약은 메뉴 이름만 돌려줬다 | 본 조사 |
| 우회 | HTML 스크립트가 `/data/contents_<en,kr,jp>.json`을 불러오는 구조임을 확인하고 JSON 3종을 직접 저장했다. 영어·한국어·일본어 모두 "Documentation v1.0", 18과제·55케이스로 표기가 같다 | [1] |
| 구조 | 한 페이지 안의 패널(Home, OSC Axes, Dexterity Regimes, 과제 18개, Object Reference). sitemap.xml에는 /en/, /ko/, /ja/ 3개만 있고 lastmod는 2026-06-23이다. /leaderboard, /docs, /paper, /results 등은 404였다 | [1] |
| 링크 | 외부 링크는 파트너 로고, 문의 메일(inquiry@dexbench.org, 일본어판은 partnership.jp@rlwrld.ai), 로봇 손 아카이브 "ALL HANDS UP"(allhandsup.org)뿐이다. GitHub·arXiv·Hugging Face·문서 링크는 없다 | [1] |
| 미반영 가능성 | 사이트는 55케이스인데 2026-08-07 RLWRLD 발표는 "80 representative use cases"라고 쓴다. 사이트 마지막 갱신 표기(06-23)가 이후 변경을 반영하지 않았을 수 있다(`추정`) | [1][3] |

### 2. 개발 주체와 이해관계 (항목 6)
| 근거 | 내용 | 출처 |
|------|------|------|
| 사이트 푸터·메타 | "DexBench · Published by RLWRLD · 2026", HTML meta author=RLWRLD, Platform Partners = RLWRLD, NVIDIA | [1] |
| RLDX-1 논문 | 기여자 절 "Dexterity Benchmark for Industry Conversion": Hensen Ahn "Designed and curated DexBench, the industry-oriented dexterity benchmark for evaluating RLDX-1 in industry conversion scenarios", Junho Cho "DexBench narrative and figure direction", Kangwook Lee "Defined the dexterity standards for industry conversion" | [7] |
| 보도자료 | "RLWRLD's DexBench", NVIDIA Isaac Lab-Arena에 통합 예정. NVIDIA 측은 Amit Goel(Robotics Ecosystem) 인용문이 있다 | [2] |
| NVIDIA 측 | Arena README와 0.3 공지가 "RLWRLD (DexBench)"를 통합 예정 파트너 벤치마크로 나열한다. NVIDIA가 DexBench를 설계했다는 서술은 없다 | [4][5] |
| 파트너 | 사이트 Industry Partners 9곳: Hotel Lotte, Himart, SK Telecom, Hyosung, HL Mando, CJ Logistics, Fuji Electric, ANA, Mitsui Chemicals. 8월 RLWRLD 발표의 목록은 Lotte, SK Telecom, CJ Logistics, Hyosung, HL Mando, Fuji, ANA, Mitsui Chemicals로 Himart가 빠지고 "Fuji"로 표기된다. 역할(과제 제공, 장소 제공, 자문)은 어디에도 없다 | [1][3] |

**이해관계 판단 (본 문서 판단)**
- 벤치마크와 평가 대상 모델의 개발사가 같다. 블로그는 5영역을 RLDX-1 각 부품의 존재 이유로 연결하고 DexBench를 "고객 요구를 5영역으로 정리한 것"이라 설명한다 [8]. 따라서 DexBench 점수가 나오더라도 RLWRLD 모델 우위의 중립 증거로 쓸 수 없다.
- 파트너 가운데 Hotel Lotte, CJ Logistics는 RLWRLD의 공개 투자자·고객, ANA·Mitsui는 투자 관계가 확인된 곳이다(knowledge.md 인사이트). 파트너 로고는 독립성의 근거가 아니라 RLWRLD 고객 생태계의 표시로 읽는다.
- CBO는 "코드가 아니라 벤치마크와 표준이 핵심 자산"이라고 말했다 [11]. 즉 DexBench는 평가 도구이면서 해자 전략의 일부다.
- "Fuji Electric" 표기의 링크 도메인이 fuji.co.jp인데 이 도메인의 회사가 Fuji Electric인지 확인하지 못했다(`확인필요`, 피딩 요청 참조).

### 3. 18개 과제 전체 표 (항목 1, 2)
출처는 모두 [1]이다. 영역 E1 Grasp Diversity, E2 Spatial Precision, E3 Temporal Precision, E4 Contact Precision, E5 Context Awareness. 산업 M=Manufacturing, S=Service, L=Logistics. 설명은 사이트의 부제(actionName)를 번역했다.

| # | 과제 | 설명(사이트 부제) | 영역 | OSC 축 | 산업 | 케이스 |
|---|------|-------------------|------|--------|------|:---:|
| 0 | Special Picking | 환경을 이용한 파지, 접근이 막힌 곳에서 꺼내기 | E1 E2 E4 | geom, contact, force | M S L | 4 |
| 1 | In-Hand Reorientation | 한 손으로 물체 자세 바꾸기 | E1 E4 E5 | geom, contact, obs, force | M S L | 4 |
| 2 | Bimanual Regrasping | 양손 인계, 하중 이동 재파지 | E1 E3 E4 | geom, contact, force, dyn | M L S | 3 |
| 3 | Precision Insertion | 좁은 공차 조립, 펙인홀 | E2 E4 E5 | geom, force, contact | M L | 6 |
| 4 | Hand Fastening | 맨손 체결, 토크 제한 조이기 | E1 E4 E5 | force, contact, geom, obs | M S | 3 |
| 5 | Constrained-Axis Manipulation | 고정축 따라 힘 조절 회전 | E4 E5 | force, contact, geom, obs | M S | 5 |
| 6 | Control Interface Actuation | 버튼·스위치·래치 상태 전환 | E2 E4 | contact, force | M S L | 4 |
| 7 | Force-Regulated Wiping | 힘 조절 연속 접촉 닦기 | E3 E4 | force, contact, dyn | S M | 2 |
| 8 | Flowable Material Control | 유량 조절, 힘 인지 붓기 | E3 E4 E5 | force, contact, dyn | M S | 4 |
| 9 | Fabric Folding | 가장자리 정렬, 양손 협응 | E1 E5 | geom, contact, deform | S L | 2 |
| 10 | Cable Winding | 선형물 경로, 케이블 정리 | E1 E4 E5 | geom, contact, deform | S L M | 2 |
| 11 | Package Handling | 밀봉 절단, 테이프 제거, 제품 삽입 | E1 E2 E4 E5 | geom, force, deform | S L M | 3 |
| 12 | Selective Sorting & Binning | 시각 구분, 범주별 배치 | E1 E2 E5 | obs, geom, dyn, contact | L S M | 1 |
| 13 | Heterogeneous Bin Packing | 이형 물체 적재, 공간 효율 | E1 E2 E5 | geom, obs, contact | S L | 2 |
| 14 | Box Sealing | 연속 경로 추종, 양손 도구 사용 | E1 E2 E4 E5 | geom, contact, deform | M L | 1 |
| 15 | Precision Arrangement | 시각 서보, 미세 배치 | E1 E2 E5 | obs, geom, contact | S L | 3 |
| 16 | Tool-Use | 도구 보조 조립, 토크 인가 | E1 E2 E4 E5 | geom, force, contact, obs | M S | 4 |
| 17 | Moving Object Interaction | 움직이는 표적 추적·가로채기 | E1 E2 E3 E5 | dyn, obs, geom, contact | M L | 2 |
| 합계 | | | | | | 55 |

- 영역별 과제 수(사이트 과제 태그 기준, 본 문서 계산): E1 13, E2 10, E3 4, E4 13, E5 14. 산업별: Manufacturing 15, Service 15, Logistics 13 [1].
- 케이스 이름은 과제 안에서 객체 유형을 나눈다(예: Task 3 = 3-A 얇은 직육면체, 3-B 비대칭 커넥터, 3-C 이중날 플러그, 3-D 볼트 나사산, 3-E 와셔, 3-F 너트 나사산). 일부 케이스는 앞 케이스의 결과 상태를 시작 상태로 쓴다(4-A는 3-D 결과, 4-B는 3-F 결과, 13-B는 12-A 결과) [1].
- 본 문서 대조: 사이트의 병목 규칙(예: C_dyn + C_obs → E3, C_deform + C_obs → E5)을 기계적으로 적용하면 일부 태그는 재현되지 않는다. Task 3의 OSC에는 C_obs·C_deform이 없는데 E5가 붙어 있고, Task 7은 C_obs가 없는데 E3가 붙어 있다 [1]. 영역 태그는 규칙으로 자동 산출된 값이 아니라 설계자의 판단이 섞인 값으로 읽는다(`추정`).

### 4. 5영역과 OSC 정의 (항목 2)
| 영역 | 정의(사이트) | 병목 | 지배 OSC | 핵심 정밀 지표(이름만, 값 없음) | 대표 실패 |
|------|--------------|------|----------|----------------------------------|-----------|
| E1 Grasp Diversity | 형상·재질·접근 제약에 걸친 성공 접촉 구성의 폭 | 하드웨어 기구학, 접촉면 설계 | geom + contact + HW | 해 공간 커버리지(파지 성공 물체 비율) | 물체 밑으로 못 들어감, 곡면에서 접촉 불안정 |
| E2 Spatial Precision | 접촉·정렬·삽입 조건이 좁을 때 자세·형상 정밀도 | 센서 해상도, 기구 정확도, 순응 조정 | geom | 자세·형상 시그마(mm, 도) | 0.5 mm 어긋나 걸림, 커넥터 핀 휨, 나사 비스듬히 시작 |
| E3 Temporal Precision | 동적 환경에서 동작 시작·전환·재계획 시점 | 지각 지연, 제어 주기, 예측 정확도 | dyn + obs | 타이밍·지연 tau(ms) | 파지 창을 놓침, 붓기 정지 늦음 |
| E4 Contact Precision | 접촉 후 힘·토크·임피던스의 고주파 조절 | 힘센서 대역폭, 백드라이브성, 임피던스 제어 | force + contact + obs | 힘·임피던스 편차(N, Nm) | 계란 파손, 과토크로 나사 비틀림, PCB 부품 전단 |
| E5 Context Awareness | 불완전 관측·이력 의존 하에서 단계 분해, 실패 진단, 복구 분기 | 가림 상황 상태 추정, 과제 그래프, 재계획 | deform + obs | 단계·분기 정확도 | 접기 순서 오류, 케이블 매듭, 낯선 포장 개봉 실패 |

- OSC(Object State Complexity)는 난이도의 원인을 6축 벡터로 분해한다: C_geom, C_force, C_contact, C_obs, C_deform, C_dyn. 사이트는 "70% 성공률은 실패 원인을 알려주지 않는다"고 쓰고, 5영역은 "그 어려움을 흡수하는 능력"이라고 둔다 [1].
- **B4에 중요한 문장:** "Dexterity is not a property of the hand... A two-finger gripper that solves a high-contact-complexity task with finger gaiting is more dexterous, in context, than a five-finger hand that cannot." 사이트의 영역 정의는 하드웨어 비종속이라, 그리퍼 대조군을 같은 과제 정의 위에서 평가하는 B4 설계와 충돌하지 않는다 [1].
- 영역별 센서·데이터 권고(사이트): E4는 F/T 센서·촉각, 임피던스·어드미턴스 제어, E2는 고해상 스테레오·레이저 프로파일러 [1]. 기준은 권고이며 평가 의무 조건은 아니다.

### 5. 평가 방식 (항목 3)
| 항목 | 사이트에 있는 것 | 사이트에 없는 것 |
|------|------------------|-------------------|
| 설계 원칙 4개 | State Transition(방법이 아니라 상태 변화를 정의), State-Based Judgment(종료 상태 검증, 궤적 유사도 아님), Real Objects(구매 가능 물체와 규격), Breakdown Curves("성공률이 아니라 성능이 무너지는 지점") [1] | 원칙을 수치로 옮긴 절차 |
| 케이스 기술 | 케이스마다 객체, 초기 상태, 목표 상태, 실패 조건 목록. 총 55개 [1] | 시행 횟수, 합격 기준(성공률 몇 %), 신뢰구간 |
| 채점 | 이진 판정에 가깝다: 목표 상태 달성 + 실패 조건 미발생. 일부 실패 조건에 수치 한계가 있다(8-A 목표 부피 오차 50 ml 초과, 8-C 30 ml 초과, 8-D 20 ml 초과, 9-A 가장자리 어긋남 1 cm 초과, 10-A 감은 다발 지름 12 cm 초과, 10-B 코일 지름 10 cm 초과, 3-B 오삽입 후 재삽입 2회 초과) [1] | 성공률과 진행 점수의 구분, 단계 점수, 사이클 타임, 속도 기준 |
| 공통 실패 | "external object assistance"(외부 물체의 도움), "two-hand use"(한 손 과제에서 양손 사용), "tool use"(맨손 과제에서 도구 사용), "forced insertion", 물체 낙하·파손 [1] | 사람 개입(원격 조작, 리셋)의 처리 규정 |
| 시뮬레이션 대 실세계 | 사이트는 언급하지 않는다. 보도자료는 Arena 통합으로 "시뮬레이션과 실세계 양쪽 검증"을 계획한다고 쓴다 [2]. 사이트의 케이스는 구매 목록(Amazon 링크 45개 항목)과 3D 프린트 키트 5종(Custom outlet, hole, hexagonal bulb, valve, switch kit) 설명이 있어 실물 재현을 전제로 보인다 [1] | 어떤 케이스가 시뮬레이션 자산을 갖는지 |
| 하드웨어 플랫폼 | 하드웨어 비종속을 명시. 일부 케이스는 양손(0-D, 2-A~C, 9, 14)·컨베이어 뒤 로봇(17)을 전제한다 [1] | 지원 로봇·손 목록 |
| 제출·검증 | 없음. 문의 메일만 있다 [1] | 제출 형식, 검증 기관, 재현 의무 |

- 사이트의 "Breakdown Curves" 원칙은 B4가 요구하는 "변동 조건별 성능"과 같은 방향이다. 다만 곡선 작성 절차(변수, 범위, 시행 수)는 없다 [1].
- 사이트에는 "성공률 대 진행 점수" 구분이 없다. RLDX-1 논문의 ALLEX 평균 86.8%가 성공률과 진행 점수를 섞은 것(research/rldx1-tech.md)과 달리, DexBench 문서는 점수화 자체를 정의하지 않았다. 따라서 DexBench 결과가 나와도 이 구분은 별도로 확인해야 한다.
- NVIDIA Arena 0.3은 "Subtask Predicates"(단계별 마일스톤 추적)와 환경 변이·민감도 분석 기능을 제공한다 [5]. DexBench가 Arena에 들어오면 단계 점수와 변동 스윕은 이 기능으로 구현될 수 있으나, DexBench가 이를 쓴다는 서술은 없다(`추정`).

### 6. 리더보드와 비교 모델 (항목 4)
- **미확인(없음).** dexbench.org에는 리더보드, 모델 이름, 수치가 없고 /leaderboard는 404였다 [1]. π0.5, GR00T N1.6/N1.7, RLDX-1의 DexBench 점수는 어떤 저장 소스에도 없다.
- RLDX-1의 실세계 수치(ALLEX 4과제, FR3 6과제)는 논문과 블로그에서 DexBench 결과로 표기되지 않았다. 논문에서 DexBench는 기여자 절의 두 문장(raw 2912, 2916행)에서만 확인되었고 결과 절에서는 찾지 못했다(검색어 DexBench|regimes로 확인) [7]. 블로그는 DexBench를 "고객 요구를 5영역으로 정리한 벤치마크"로만 소개한다 [8].
- 2026-06-09 보도자료가 말하는 "8개 시뮬레이션 벤치마크 최고 성능(vs GR00T N1.6, π0.5)"은 RoboCasa Kitchen, GR-1 Tabletop, LIBERO-Plus 등 기존 벤치마크의 자체 평가이며 DexBench 결과가 아니다. 보도자료도 DexBench를 "기존 벤치마크가 포착하지 못하는 손재주를 다루는 다음 단계"로 구분한다 [2].

### 7. 공개 범위와 NVIDIA Isaac Lab-Arena 연결 (항목 5)
| 항목 | 상태(2026-10-09 확인 범위) | 출처 |
|------|----------------------------|------|
| 과제 정의 | 공개(사이트 JSON, 영·한·일) | [1] |
| 물체 규격·구매 목록 | 공개(48개 물체 목록, 45개 구매 항목, 맞춤 키트 5종 설명) | [1] |
| 평가 코드 | 확인되지 않음. RLWRLD GitHub 조직의 저장소 7개(RLDX-1, IsaacLab-Arena 포크, IsaacLab 포크, newton 포크, simready-foundation 포크, openarm_description 포크, ethercat_driver_ros2 포크)에 DexBench 이름이 없다 | [6] |
| Arena 포크 | RLWRLD/IsaacLab-Arena에 dexbench/main, dexbench/pin-8b3fb4db 브랜치가 있다. dexbench/main은 main보다 4커밋 앞서고 16커밋 뒤처졌으며(2026-10-07), 변경 파일은 .gitmodules, device_library.py, pyproject.toml, submodules/IsaacLab이다. 커밋 제목은 서브모듈 포인터, Newton 1.5.2 고정, OpenXR 컨트롤러 폴링 끄기 등 인프라성이다. 트리에서 dexbench 이름의 파일은 찾지 못했다 | [6] |
| 업스트림 Arena | README는 "benchmark integrations from ecosystem partners including RLWRLD (DexBench)"를 Coming Soon으로 둔다. Arena는 Apache 2.0 알파이고 "Do not use this in production", Isaac Sim의 일부 구성요소는 독점 라이선스다. 업스트림 트리에서 dexbench·rlwrld 경로는 없었다 | [4][6] |
| 게시 방식 | Arena는 벤치마크를 각자 저장소에서 관리하고 Arena 통합 브랜치나 패키지로 두라고 권한다. RLWRLD의 dexbench 브랜치는 이 방식과 맞지만 내용은 아직 인프라 수준이다 | [4][6] |
| 가중치·데이터 | Hugging Face의 RLWRLD 계정에는 RLDX-1 계열 모델 11개가 있고 데이터셋은 0개다. DexBench 이름의 항목은 다른 계정의 동명 항목뿐이다(관계 미확인, 설명상 무관해 보임) | [6] |
| 라이선스 | 사이트에 표기 없음(미확인). 8월 발표는 "open-source project로 개발 중"이라고 쓴다 [3]. 이는 계획 서술이며 현재 공개 상태의 증거가 아니다 | [1][3] |
| 공개 시점 | 미확인. 보도자료는 지표를 "open industry specification으로 제안할 것"(will be proposed)이라는 미래 시제로 쓴다 | [2] |

- **사이트 서술 대 기사 서술:** 사이트는 18과제·55케이스, 기사·발표(8월)는 18과제·80케이스다. 같은 8월 발표에 소프트 바디 트랙(두부, 과일, 고무 부품; SpaceAI 담당)이 추가로 나오는데 사이트의 물체 목록(48개)에는 두부·과일이 없다. 80은 확장 계획이거나 사이트 미반영분일 가능성이 있다(`추정`) [1][3][10].
- 8월 발표는 NdotLight(시뮬레이션 자산 생성 TRINIX), Physics Sim Lab(디지털 트윈과 도메인 랜덤화), SpaceAI(변형·취약 물체 트랙)와 각각 MOU를 맺었다고 한다. 이는 협약 체결이며 결과물 공개가 아니다 [3].
- 같은 이름의 외부 항목(예: LLM 평가용 DexBench, 다른 사용자의 Hugging Face 항목)이 있어 검색 시 혼동된다. RLWRLD의 DexBench와 연결할 근거는 없다.

### 8. 하네스·커넥터·케이블·변형체 유사 과제와 조건 (항목 7)
| 후보 | 사이트의 조건 [1] | 하네스와의 차이 |
|------|-------------------|-----------------|
| 3-B 비대칭 커넥터 (USB-A + Custom outlet kit) | 시작: USB-A를 쥔 상태, 벽에 붙은 키트의 포트 노출. 목표: 올바른 방향으로 결합 완료. 실패: 강제 삽입, 오삽입 후 2회 초과 재삽입, 커넥터 파손. 영역 E2 E4 E5 | 단자(terminal)를 하우징 캐비티에 꽂고 락을 확인하는 동작이 아니라 완성 커넥터 결합. 케이블이 아닌 고정 키트. "집기" 단계는 시작 상태에 이미 포함 |
| 3-C 이중날 플러그 (110V cord + outlet kit) | 시작: 플러그가 앞을 향하게 쥔 상태, 콘센트가 앞에 위치. 목표: 두 날이 올바른 위치에 삽입. 실패: 플러그 방향 반전, 강제 삽입, 파손 | 딱딱한 소켓 고정. 코드의 휨은 평가 변수가 아니다 |
| 3-D~F 볼트·와셔·너트 | 약 1 mm 피치 나사산, 목표는 나사산 맞춤 후 살짝 돌려 고정. 실패에 "tool use" 포함 | 하네스 단계가 아님. 맨손 체결 계열 |
| 10-A 본체 부착 코드 감기 (power strip) | 시작: 본체를 쥐고 코드가 뻗은 상태. 목표: 코드가 본체에 감김. 실패: 매듭, 본체 미사용, 풀림, 다발 지름 12 cm 초과 | 한쪽이 고정된 선형 변형체. 분기·커넥터 없음 |
| 10-B 단독 케이블 | 시작: 테이블에 불규칙하게 펼쳐진 케이블. 목표: 지름 10 cm 이하 원형 코일 | 정리(코일링)이지 조립 경로 설치가 아님 |

- 사이트는 Task 10의 제조 예시로 "Hose and wire harness winding in production"을, Task 3의 제조 예시로 "Connector mating, board-level component insertion, bolt-thread alignment"를 든다 [1]. 즉 하네스·커넥터를 염두에 둔 서술은 있으나 해당 케이스는 없다.
- **없는 것:** 압착 단자를 커넥터 캐비티에 삽입(프리블록), 조립판 위 경로 설치·걸기·분기 정리(레이업), 테이프 감기, 다품종 커넥터 변형. 테이프는 Task 14(상자 밀봉)에만 있다.
- 참고: NVIDIA Arena 0.3의 "What's Next"에는 Newton 기반 접촉 위주 삽입·조립, 소프트바디 pick-and-place, 케이블 라우팅의 참조 평가가 로드맵으로 있고, 저장소에는 "cable asset class" 추가 커밋이 있다 [5][6]. 이는 Arena의 계획이며 DexBench 범위는 아니다.
- RLDX-1 논문의 FR3 Plug Insertion(소켓이 카메라에서 완전히 가림, 24회 중 8회 33.3%, research/rldx1-tech.md)은 이름과 성격상 3-C와 가까워 보이나, 논문이 이를 DexBench 케이스라고 밝힌 곳은 없다(`추정`).

### 9. 독립 검증 가능성 (항목 8, 열린 질문 답)
- **답: 독립 검증 결과는 확인되지 않았다.** 근거: (a) 사이트에 결과 자체가 없음, (b) 코드·데이터·체크포인트가 공개 저장소에 없음, (c) 제3자 사용 보도 없음(검색 범위 내), (d) Arena 통합은 "coming soon" [1][4][6].
- 재현 가능성의 현재 수준: 물체는 구매·제작 가능하고 초기·목표 상태가 서술되어 있어 **사람이 실물 케이스를 재현하는 것은 가능**하다. 그러나 시행 수·채점 방식·시뮬레이션 자산이 없어 **다른 기관이 같은 수치를 산출할 수는 없다**(본 문서 판단).
- RLDX-1 가중치 자체는 공개되어 있어(knowledge.md) 제3자가 RLDX-1을 DexBench 케이스에 돌려 볼 수는 있으나, 그 결과 공개는 확인되지 않았다.

### 10. Five Regimes와 18과제의 관계 (항목 10, 열린 질문 답)
- **분류축 대 과제의 관계다.** 사이트는 모든 과제를 OSC(왜 어려운가)와 Dexterity Regimes(어떤 능력이 필요한가)의 두 축에 놓는다. 한 과제는 2~4개 영역에 중복 태그된다(§3) [1]. 보도자료도 "5 core evaluation domains ... spanning 18 Key Atomic Tasks"라고 쓴다 [2]. CBO의 "18개 과제 덱스벤치"와 블로그의 "5영역"은 같은 벤치마크의 다른 층이다 [8][11].
- **RLDX-1 논문의 실세계 과제는 DexBench 과제로 표기되지 않는다.** 논문은 ALLEX 4과제와 FR3 6과제를 "benchmark"라 부르되 DexBench와의 대응을 쓰지 않는다 [7]. 이름이 닮은 대응은 다음과 같다(모두 `추정`, 이름·성격 유사만):

| RLDX-1 논문 과제 | 닮은 DexBench 과제 | 차이 |
|------------------|--------------------|------|
| Conveyor Pick-and-Place (상자를 집어 선반에 놓기, ALLEX) | Task 17 (17-A: 마우스·마우스 상자를 두 상자에 분류) | 물체, 목적지가 다름 |
| Card Slide-and-Pick (밀고 집고 전달, ALLEX) | Task 0 (0-A: 평평한 명함 집기) | 전달 단계는 DexBench 케이스에 없음 |
| Pot-to-Cup Pouring (플라스틱 공, ALLEX) | Task 8 (8-A: 주전자로 물 300 ml 붓기) | 논문은 공으로 대체 |
| Plug Insertion (FR3, 그리퍼) | 3-C 이중날 플러그 | 논문은 소켓이 가려진 조건 |
| Object-in-Box, Shell Game, Swap Cup (기억) | 대응 없음 | 사이트에 기억 중심 케이스 없음 |

- 블로그의 영역별 부품 연결(Contact → Physics 모듈, Context → Memory·Recovery)은 RLDX-1 설계 설명이고, 사이트의 영역 정의는 하드웨어·모델 비종속으로 쓰여 있다. 두 문서의 영역 이름은 같지만 정의의 초점이 다르다(블로그는 "모델 부품", 사이트는 "과제 난이도에 대한 능력") [1][8].

## 9. B4 8.3절 평가 과제를 덱스벤치에 맞추는 제안 (항목 9)
전제: 덱스벤치는 시행 수·채점 산식·인증 절차가 없으므로 **"덱스벤치 호환"이 아니라 "덱스벤치 케이스 카드 형식을 따르고 인접 과제를 표기"**로 쓴다. 공식 호환은 RLWRLD와의 합의가 필요한 사항이다(미확인).

### 9.1 과제 이름 대응
| B4 8.3 트랙·단계 | 대응 덱스벤치 과제(인접) | 쓰임 | 비고 |
|------------------|--------------------------|------|------|
| A 프리블록 - 집기 | Task 0 (0-C: 밀집 더미에서 1개만 꺼내기) | 단자 1개 분리 집기와 유사 | 단자 트레이 형상은 별도 정의 |
| A - 방향 맞춤 | Task 1 (1-D: 비대칭 USB를 앞면 정렬 핀치) | 인핸드 방향 조정 | |
| A - 삽입 | **Task 3 (3-B, 3-C)** | 핵심 대응. 영역 E2 E4 E5 | 캐비티·락·당김 확인은 없음 |
| A - 당김 확인 | 대응 없음 | 신규 케이스 | 사이트에 인장 시험 없음 |
| B 레이업(손 대 그리퍼) | **Task 10 (10-A, 10-B)**, 분기 정리는 대응 없음 | E1 E4 E5, C_deform | 분기 케이블 케이스는 신규 |
| 변동 조건 | Breakdown Curves 원칙 | 커넥터 5종, 위치·방향, 조명, 교대를 스윕 변수로 | 사이트에 곡선 절차 없음 |

### 9.2 KPI 정합
| B4 KPI | 덱스벤치 대응 | 정합 방식 |
|--------|---------------|-----------|
| 완주율(자율) | 목표 상태 달성 + 실패 조건 미발생(이진) | 동일 취지. 사람 개입은 덱스벤치 실패 조건("external object assistance")과 같은 계열이므로 자율 완주에서 제외하는 B4 규칙과 맞는다 |
| 단계 점수 | 정의 없음 (Arena의 Subtask Predicates로 구현 가능) | B4 자체 지표로 유지. 덱스벤치 점수로 부르지 않는다 |
| 개입 후 완주율 | 정의 없음 | B4 자체 지표 |
| 속도비, 연속 가동, 새 커넥터 적응 | 정의 없음 | 고객 합의 KPI. 덱스벤치가 다루지 않는 영역임을 문서에 명시 |
| 단자 손상률 | 실패 조건 "connector damage"(이진) | 사람 기준선 대비 비율은 B4 자체 정의 |
| 개입 횟수 | 정의 없음 | B4 자체 지표 |
| 시행 수 100회 이상 | 덱스벤치에 시행 수 없음 | B4 값 유지. 덱스벤치와 같은 값이라고 쓰지 않는다 |
| 영역 보고 | 과제별 영역 태그 | 보고서에 E2/E4/E5 태그를 달고 실패를 영역별로 분해 |

### 9.3 b4-proposal.md에 쓸 문장 제안
"평가 케이스는 DexBench(RLWRLD 발행, 2026-10-09 기준 과제 정의만 공개)의 케이스 기술 형식(초기 상태, 목표 상태, 실패 조건)으로 작성하고, 가장 가까운 DexBench 과제(Task 3, Task 10)를 인접 과제로 표기한다. 시행 수, 채점, 합격 기준은 DexBench에 정의가 없으므로 본 제안의 값을 쓴다. DexBench 공식 호환 여부는 G0에서 RLWRLD와 확인한다."

## RX 관점 시사점
- **고객 제안:** 덱스벤치는 "고객 공정 → 케이스 카드(초기·목표·실패 조건) → 영역 태그"로 합의 문서를 쓰는 틀로 유용하다. 단, 고객에게 "표준 벤치마크로 검증된다"고 말하지 않는다. 현 시점에서 리더보드·제3자 검증이 없고 RLWRLD 자체 문서다.
- **PoC 설계:** 사이트의 하드웨어 비종속 정의와 Breakdown Curves 원칙은 그리퍼 대조군, 변동 조건별 성능 보고와 맞는다. 하네스 단계는 덱스벤치에 없으므로 신규 케이스를 RLWRLD와 공동 정의하는 제안(표준 자산화)은 B4가 이미 쓴 논리와 합치되며, 이때 데이터 권리와 공개 범위를 G0에서 정한다.
- **면접:** "덱스벤치는 어떤 벤치마크인가"에 대해 "RLWRLD가 발행한 18과제·55케이스(사이트 기준) 정의 문서이고, 공개 시점의 리더보드·코드는 확인되지 않으며, 같은 회사 모델 평가에 쓰이므로 독립성은 낮다. 그래서 PoC에서는 시행 수와 채점을 별도로 고정한다"로 답할 수 있다. 18과제와 5영역은 과제와 분류축의 관계라고 설명한다.

## 확인하지 못한 항목
- 평가 시행 수, 합격 기준, 채점 산식, 제출·검증 절차 (사이트에 없음, 비공개 문서 가능성)
- 사이트 55케이스와 8월 발표 80케이스의 차이 원인, 소프트 바디 트랙의 케이스 목록
- 사이트 갱신 여부 (sitemap lastmod 2026-06-23 이후)
- 라이선스, 공개 일정, Arena 통합 완료 시점
- 파트너별 역할, Fuji 표기(Fuji Electric 대 Fuji)의 실체
- 저장했으나 이번에 읽지 못한 자료: ddaily, mt.co.kr, byline.network, PRTimes(ALL HANDS UP), The Robot Report, fuji.co.jp (reference/raw/benchmark--dexbench-ddaily.txt 등). 본문은 이 자료를 사용하지 않았다.
- engineering.com 기사(403으로 수집 실패)

## 사용자 피딩 요청 목록
| 대상 | 왜 필요한가 | 어디서 얻나 |
|------|-------------|--------------|
| DexBench 평가 프로토콜(시행 수, 채점, 합격 기준, 제출·검증 절차) | B4 8.3의 "덱스벤치 형식" 정합과 독립 검증 가능성 판단. 공개 소스에 없음 | RLWRLD RX 담당자 문의: inquiry@dexbench.org (일본어판 partnership.jp@rlwrld.ai). 비공개일 수 있음 |
| 80케이스 명세 및 소프트 바디 트랙(두부, 과일, 고무 부품) | 사이트 55케이스와 불일치. 과제 수 인용값 확정에 필요 | 같은 문의 경로. 또는 Chrome 연동으로 dexbench.org 최신 화면 열람 후 JSON 변경 비교 |
| engineering.com "RLWRLD teams with NVIDIA on robot dexterity benchmarks" | 403으로 수집 실패. 추가 사실(있다면) 확인 | Chrome 연동으로 열어 본문 붙여넣기 |
| 저장한 미열람 raw 6건 (ddaily, mt.co.kr, byline, PRTimes ALL HANDS UP, Robot Report, fuji.co.jp) | 파트너 역할, 80케이스 서술 출처, Fuji 정체, ALL HANDS UP 관계를 확인할 수 있음 | reference/raw/benchmark--dexbench-ddaily.txt 등을 다음 세션에서 find.py로 읽기 |
| RLDX-1 블로그 각주 1 | 컨베이어·육각 너트 문장의 각주가 DexBench 대응을 알려 줄 수 있음. 크롤 텍스트에 각주 본문 없음 | Chrome 연동으로 rlwrld.ai/ko/insight/blog/14 열기 |
| RLDX-1 논문 부록 | 실세계 과제와 DexBench 케이스의 공식 대응 여부 | arXiv 2605.03269 PDF를 사용자가 확인 (source-read로 이미 저장된 텍스트에는 대응 서술 없음) |
| 매일경제 CBO 인터뷰 게재일 | knowledge.md 열린 질문 | 매일경제 원문 페이지 (확인 방법은 사용자 판단) |
| DexBench Arena 통합 일정 | 공개 시점. 보도자료는 미래 시제 | github.com/RLWRLD/IsaacLab-Arena 의 dexbench 브랜치와 isaac-sim/IsaacLab-Arena 릴리스를 분기별로 재확인 |

## 출처
1. [DexBench 공식 사이트 (홈 HTML, contents_en/kr/jp.json, sitemap)](https://dexbench.org/en/) - RLWRLD 발행, Documentation v1.0, 열람 2026-10-09, (en)(ko)(ja) (reference/benchmark--dexbench-site.md)
2. [RLWRLD Launches DexBench Initiative ... in Collaboration with NVIDIA](https://en.prnasia.com/releases/global/rlwrld-launches-dexbench-initiative-to-define-next-generation-industry-standards-for-humanoid-ai-in-collaboration-with-nvidia-536553.shtml) - PR Newswire APAC(RLWRLD 보도자료), 2026-06-09, 1차, (en) (reference/benchmark--dexbench-pr-nvidia.md)
3. [RLWRLD Signs MOUs with Three Korean Robotics and Simulation Startups](https://www.rlwrld.ai/en/news/94) - RLWRLD, 2026-08-07, 1차, (en) (reference/benchmark--rlwrld-news-94-mou.md)
4. [isaac-sim/IsaacLab-Arena README](https://github.com/isaac-sim/IsaacLab-Arena) - NVIDIA, 열람 2026-10-09, 1차, (en) (reference/benchmark--arena-readme.md)
5. [Isaac Lab-Arena 0.3 (Alpha) Release Announcement, Discussion #1245](https://github.com/isaac-sim/IsaacLab-Arena/discussions/1245) - NVIDIA, 2026-09-10, 1차, (en) (reference/benchmark--arena-release-0-3.md)
6. [RLWRLD GitHub 조직, RLWRLD/IsaacLab-Arena 포크, Hugging Face RLWRLD 계정 (GitHub·HF API 조회)](https://github.com/RLWRLD) - 관찰 기록 2026-10-09, 1차(저장소 메타데이터), (en) (reference/benchmark--rlwrld-github-status.md)
7. [RLDX-1 Technical Report](https://arxiv.org/abs/2605.03269) - arXiv, 2026-05-05, 논문, (en) (reference/papers--rldx1-tech-report.md; 기여자 절은 raw 2908~2920행)
8. [RLDX-1: A Dexterity-First Foundation Model for Robot Hands (Tech Blog)](https://www.rlwrld.ai/ko/insight/blog/14) - RLWRLD, 2026-05-07, 1차, (en) (reference/company--rlwrld-blog-14.md)
9. [엔비디아 손잡은 리얼월드, 휴머노이드 '표준 손' 선점 도전](https://www.news1.kr/industry/sb-founded/6192385) - 뉴스1, 2026-06-09, 기사, (ko) (reference/benchmark--dexbench-news1.md)
10. [리얼월드, 국내 3사와 손잡고 휴머노이드 '손재주' 평가 기준 만든다](https://aimatters.co.kr/news-report/48213/) - AI매터스, 2026-08-07, 기사, (ko) (reference/benchmark--dexbench-aimatters.md)
11. [이강욱 리얼월드 CBO 인터뷰](https://www.mk.co.kr/news/culture/12146778) - 매일경제, 게재일 확정 보류(raw 표기 2026-09-08), 기사, (ko) (reference/company--mk-cbo-interview-2026-10.md)
