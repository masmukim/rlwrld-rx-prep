# ALL HANDS UP(allhandsup.org) 로봇 손 갤러리 분석: 무엇이 있고, "지원"은 무엇을 뜻하는가
조사일: 2026-10-12 (Q9. 사이트 홈 HTML, 데이터 파일 2종, 블로그 Part 1·2를 reference/raw/에 저장해 Grep·파싱으로 읽음. 렌더된 화면은 직접 보지 못함)

## 핵심 요약
- **갤러리는 RLWRLD가 운영하는 손 "분석 아카이브"이지 RLDX-1 호환 목록이 아니다.** 사이트는 RLWRLD 발행이고, 취지는 "10종 이상을 직접 운용한 경험으로 설계 트레이드오프와 URDF·사양을 공유"하는 것이다. 어느 페이지에도 "RLDX-1이 이 손을 학습·지원한다"는 문장이 없다 [1][2][3][4]. 현재 데이터 파일 기준 22건 중 4건이 숨김(hidden)이라 화면에는 18종이 노출되는 것으로 읽힌다(코드 기준 추정) [1].
- **B4 구성안과의 대조: Tesollo DG-5F-S는 목록에 있고 RLWRLD가 직접 평가했다. Robotiq Hand-E와 XELA uSkin은 사이트 범위(다관절 손) 밖이라 없다.** Inspire는 RH56DFX가 아니라 RH56F1이 올라 있고, 이는 RLDX-1 논문의 OpenArm 실험 손과 같은 모델이다 [1][8]. RLWRLD 서술상 DG-5F-S는 약 $7,500이며 SharpaWave(약 $50,000)와 DexBench에서 "거의 같은 결과"라고 하나 점수는 공개되어 있지 않다(자체 서술) [3].
- **정정 후보 1건이 B3에 직접 걸린다.** case/analysis.md와 roi.xlsx의 DG-5F-S 단가는 제품 DB 표기 $23,000이고, RLWRLD 블로그는 약 $7,500이다(약 3배 차이, 두 값 모두 공식가 아님). 어느 값이 맞는지 모르므로 단가를 바꾸지 말고 민감도 시나리오로 추가하는 것을 제안한다(7절).

## 본문

### 1. 사이트 정체와 운영 주체 (항목 1)
| 항목 | 확인된 내용 | 출처 |
|------|-------------|------|
| 운영 주체 | 푸터 "All Hands Up · Published by RLWRLD · 2026". 저자 Max Chang Hwan Kim, Mark Seungjae Lee. RLDX-1 논문 기여자 절에 같은 이름의 Chang Hwan Kim이 "analyzed/integrated various upper body, arms, dexterous hands and sensors, especially for OpenArm"로 나온다(동일 인물로 보이나 확정 불가, `추정`) | [1][8] |
| 도메인 | allhandsup.org(보도자료 공식 주소). HTML canonical은 allhandsup.rlwrld.co | [1][4] |
| 발표일 | 한국 보도 2026-06-22(바이라인), 일본 PR TIMES 2026-07-01, 영문 Robotics & Automation News 2026-07-07. 최초 공개일은 가장 이른 한국 보도 기준 2026-06-22로 본다 | [4][5][6] |
| 갱신 | 보도자료는 "분기마다 정기 콘텐츠 업데이트"를 예고했다. 데이터 파일에는 갱신 날짜 필드가 없고 ETag만 있다. 항목 노트에 2026-09-14, 2026-09-29 날짜가 남아 있어 최소 9월 말까지 편집이 이어졌다. 블로그 §3은 "Coming Soon", 전완 일체형 손은 "later this year" 별도 다룬다고 쓴다 | [1][3][4][6] |
| 취지(사이트 서술) | 제조사 설계 검증 기준, 산업 파트너의 솔루션 선택 지원, 생태계 공통 기반. 보도자료는 "단순 제품 비교 사이트가 아니라 실운용 데이터를 공유하는 오픈 플랫폼" | [2][4][6] |
| 제조사 접점 | 푸터 "손 제조사라면 샘플을 보내라, 테스트 후 이곳에 소개하겠다". 블로그 문의 partnership@rlwrld.ai | [1][3] |
| 다국어 | UI는 en/ko/ja/zh 4개. 손 데이터는 언어 공통이고 블로그 Part 1·2는 영·한·일 수치가 일치(일본어판은 수치만 대조) | [1][3] |

- 접근 방법: 홈이 SPA라 단순 수집은 1,470자만 남는다. HTML이 `hands_urdf/_registry.json`과 `_kapandji.json`, `blog/part1·2(.ko/.ja)`를 불러오는 구조임을 확인하고 직접 저장했다. sitemap·robots는 SPA 홈으로 대체 응답한다 [1].

### 2. 갤러리의 손 목록 전부 (항목 2)
출처는 모두 [1](레지스트리 JSON을 파싱, 2026-10-12). "-"는 사이트 값이 비어 있음이다. 역구동/외전/촉각은 사이트의 Yes/No 표기를 그대로 옮겼고 정의(예: 촉각 Yes가 내장인지 옵션인지)는 사이트에 없다. K는 Kapandji 점수(11점 만점, URDF 시뮬레이션 값)다. **가격과 구동 방식(텐던/직접)은 사이트에 필드가 없다.** 링크는 항목별 외부 링크 없이 URDF·메시를 사이트가 직접 제공한다(라이선스 열 참조).

| # | 제조사 | 모델 | DoF | 역구동 | 외전 | 촉각 손바닥/손가락 | 무게 g | 길이 | 손끝 힘 | 훅 하중 kg | 통신 | K | URDF 라이선스 |
|---|--------|------|-----|--------|------|-------------------|--------|------|---------|------------|------|---|----------------|
| 1 | Agibot | Omnihand Pro | 12 | No | Yes | Yes/Yes | 750 | 207 mm | 20 | 35 | CAN-FD | 10 | Mulan PSL v2 |
| 2 | Wonik Robotics | Allegro V5 Plus | 16 | Yes | No | No/Yes | 1,024 | 255 mm | - | 15 | CAN 500 Hz | 9 | BSD-2 |
| 3 | BrainCo | Revo2 | 11(능동 6) | - | - | -/Yes | 383 | 160 mm | 15 N 핀치 / 50 N 파지 | 20 | RS-485/CAN-FD/EtherCAT 1 kHz | 5 | Apache 2.0 |
| 4 | Tesollo | DG-5F-M | 20 | Yes | Yes | No/Yes | 1,763 | - | 97 N | 12 | Modbus/Ethernet 250 Hz | 10 | 제조사 제공(조건 미표기) |
| 5 | **Tesollo** | **DG-5F-S** | 20 | Yes | Yes | -/Yes | 880 | 210 mm | 19.4 N | 12 | Ethernet/Modbus TCP 500 Hz | 10 | 제조사 제공(조건 미표기) |
| 6 | **Inspire Robotics** | **RH56F1** | 6(조인트 12) | Yes | No | Yes/Yes | 630 | 183.3 mm | 15 | 30 | EtherCAT+RS485 1 kHz | 5 | MIT |
| 7 | CMU | LEAP Hand V1 | 16 | Yes | Yes | No/No | 595 | 232 mm | - | - | UART 500 Hz(위치만) | 8 | MIT |
| 8 | Linkerbot | L20 | 16(조인트 21) | No | Yes | Yes/Yes | 1,000 | 263.5 mm | 10 | 5 | CAN/RS485 5 kHz(토크 루프) | 8 | Apache 2.0 |
| 9 | OYMotion | ROHand | 6 능동(조인트 11) | - | - | -/Yes | 680 | - | 0.1 N 분해능 | 30 | UART/RS485/CAN FD | 6 | MIT |
| 10 | ETH Zurich SRL | ORCA Hand V1 | 16 | Yes | Yes | No/No | 1,100 | 330 mm | - | 2 | UART | 7 | MIT |
| 11 | PSYONIC | Ability Hand | 6 | - | No | No/Yes | 490 | - | - | - | Bluetooth/USB/API | 5 | MIT |
| 12 | Robotis | HX5-D20 | 20 | Yes | Yes | No/Yes | 1,360 | - | 14 | 15 | RS-485 Dynamixel 1 kHz | 11 | Apache 2.0 |
| 13 | Sharpa Robotics | Wave | 22 | Yes | Yes | No/Yes | 1,300 | 200 mm | - | 15 | Ethernet 500 Hz | 9 | Apache 2.0 |
| 14 | Wuji Tech | Wuji Hand V1.1 | 20 | No | Yes | No/No | 590 | 201 mm | 15 | 20 | USB+RS485/EtherCAT/CANFD 1 kHz | 10 | MIT |
| 15 | Robotera | XHAND 1 | 12 | Yes | Yes | No/Yes | 1,100 | 191 mm | 15 | - | EtherCAT/RS485 | 8 | BSD-3 |
| 16 | BrainCo | Revo3 | 21 | Yes | Yes | Yes/Yes | - | - | 20 | - | - | 11 | 제조사 제공 |
| 17 | Wuji Tech | Wuji Hand V2 | 20 | Yes | Yes | No/No | 800 | 180 mm | 15 | - | Ethernet 1 kHz | 10 | MIT |
| 18 | ETH Zurich SRL | ORCA Hand V2 | 17 | - | Yes | No/Yes | 1,250 | - | - | - | - | 9 | MIT |

- **숨김 4건(레지스트리에는 있으나 갤러리 코드가 걸러냄):** Robotera XHAND 1 Pro(21 DoF, 884 g), Xynova Flex 2(23 DoF), Xynova Prima 1(22 DoF), Agibot Omnihand V3(능동 10 DoF). 이유는 "벤더가 준 URDF의 라이선스 미확정"이고, 사양이 비어 있거나 개발 중이라는 내부 메모가 붙어 있다 [1]. 스테이징 데이터라 고객 대면 자료에 인용하지 않는다.
- 집계(본 문서 계산): 노출 18종 중 DoF 20 이상 7종(DG-5F-M, DG-5F-S, HX5-D20, Sharpa Wave, Wuji V1.1, Wuji V2, Revo3), 손가락 촉각 Yes 14종 / No 4종(LEAP, ORCA V1, Wuji V1.1, Wuji V2), 손바닥 촉각 Yes는 4종(Omnihand Pro, RH56F1, L20, Revo3).
- 숫자의 성격: "10종 이상"이라는 보도 표현보다 현재 노출 수(18)가 많다. 블로그가 "직접 운용했다"는 손은 10종 이상이지만 모델명이 나온 것은 4종(SharpaWave, DG-5F-S, Wuji V1.1, ALLEX)뿐이라, 갤러리 전체가 "RLWRLD가 운용한 손"이라는 근거는 없다(3절).
- 구동 방식: 사이트에는 없다. 다른 소스로는 ORCA 계열이 텐던 구동(reference/papers--orca-hand.md [10])이고, ALLEX는 전완 일체형 텐던 구동이라고 블로그가 쓴다 [3]. 나머지는 `미확인`.
- 사양값 주의: 사양은 제조사 값, 사이트 자체 계산, 자체 측정이 섞여 있다. 예컨대 Wuji V2의 길이 180 mm는 카탈로그 외형 기준이고 URDF 계산값은 209 mm라는 메모가 있다. 손끝 힘 열은 정의가 섞여 있다(ROHand 0.1 N은 센서 분해능, XHAND 1 Pro 노트는 "0.1-25N은 센서 범위이지 출력 힘이 아님") [1].

### 3. "지원"의 의미: 사이트가 실제로 말하는 것 (항목 3)
| 구분 | 근거 문장(요지) | 읽는 법 | 출처 |
|------|----------------|---------|------|
| 직접 운용 | "Drawing on direct operation of more than ten dexterous hands across diverse real-world tasks, RLWRLD is releasing its documented observations" | 운용 경험의 공개. 호환 보증 아님 | [2] |
| 평가 DB | "RLWRLD maintains an internal evaluation database of commercially available modular wrist-mounted hands" | 평가 대상 목록. DB 자체는 비공개(갤러리는 그 일부 사양과 URDF) | [3] |
| 모델 비종속 | "RLWRLD develops a Robot Foundation Model that is not bound to any embodiment" | 특정 손에 묶이지 않는다는 지향. 손별 지원 선언의 반대에 가깝다 | [3] |
| 평가의 범위 한정 | "This evaluation reflects RLWRLD's specific development and operational objectives. Results may differ..." | 자사 목적 기준의 자체 평가임을 사이트가 명시 | [3] |
| 제조사 초대 | "We'd love to test your hand and feature it here after testing" | 갤러리 등재 = 테스트 후 소개라는 방침. 단 URDF가 오픈소스인 LEAP, ORCA(MIT)는 외부 공개 모델을 올린 것일 수 있다(`추정`) | [1] |
| 보도자료 | "リアルワールドが評価したロボットハンドのURDF"를 제공 | 갤러리를 "평가한 손"으로 소개 | [4] |
| Kapandji | 모든 점수는 URDF 위 시뮬레이션 스윕 | 갤러리 항목의 "평가" 일부는 실물이 아니라 모델 기반 | [1] |

- **결론:** 사이트는 "RLDX-1이 학습·평가·호환하는 손" 목록을 어디에도 주지 않는다. "지원"에 가까운 단어는 목적 항목의 "산업 파트너의 솔루션 선택 지원"뿐이며 이는 의사결정 지원이다 [2]. 사용자 설명("RLWRLD가 지원하는 하드웨어가 여기 있다")은 사이트 서술보다 강하다. 안전한 표현은 "RLWRLD가 운용·평가해 자체 DB에 둔 손 중 일부와 공개 URDF를 모은 아카이브"다.
- **RLDX-1 쪽의 실제 근거는 별도다.** 공개 체크포인트는 RLDX-1-MT-ALLEX와 RLDX-1-MT-DROID뿐이고, 다른 로봇은 사용자가 modality 설정과 EmbodimentTag로 파인튜닝하는 구조다 [9]. 논문의 실로봇 실험은 OpenArm + Inspire RH56F1(6 DoF), ALLEX(48 DoF 상체, 손 각 15 DoF), Franka Research 3(그리퍼 + AnySkin 촉각)이다 [8]. 이 중 갤러리에 있는 것은 Inspire RH56F1뿐이다 [1][8].
- 갤러리의 나머지 17종이 RLDX-1 데이터로 학습되었거나 파인튜닝 검증되었다는 공개 근거는 없다. 손을 바꿀 때 재학습이 얼마나 필요한지도 이번 조사에서 확인하지 못했다(열린 질문 유지).

### 4. 블로그가 직접 평가한 손 4종: 갤러리·기존 reference와의 대조 (항목 2, 6)
| 손 | 블로그 서술(RLWRLD) | 레지스트리 값 | 불일치·메모 |
|----|---------------------|---------------|-------------|
| SharpaWave | 22 DoF, 역구동, 200 mm, 1,200 g, 손끝 20 N, 약 $50,000, 손끝당 1,000 tactile pixel 이상, "NVIDIA를 비롯한 여러 연구 그룹의 연구 플랫폼" | 22, Yes, 200 mm, 1,300 g, 손끝 힘 빈칸, 훅 15 kg, 손끝 촉각 Yes | 무게 1,200 대 1,300 g. 기존 research/hardware.md는 1.3 kg(공식), 약 $50,000(2차)이므로 가격은 RLWRLD 서술과 일치 [3][12] |
| DG-5F-S | 20 DoF, 역구동, 208.5 mm, 880 g, 19.5 N, 약 $7,500, 소지 CMC 능동, 손끝 모듈 교체, 개발자 모드, 마찰 낮음 | 20, Yes, 210 mm, 880 g, 19.4 N, 훅 12 kg, 손끝 촉각 Yes, 손바닥 빈칸 | 길이·힘은 근사. **가격 $7,500 대 기존 $23,000** (7절) [3][12] |
| Wuji Hand V1.1 | 20 DoF, 역구동 아님, 195 mm, 590 g, 15 N, 충격에 관절 손상 | 20, No, 201 mm, 590 g, 15 N, 훅 20 kg, 촉각 No | 길이 195 대 201 mm. V2는 역구동 Yes, 800 g, 180 mm로 설계가 바뀐 것으로 보이나 블로그에 V2 서술은 없다 [3][1] |
| ALLEX (참고) | 15 DoF, 역구동, 40 N, 전완 일체형 텐던 | 갤러리에 없음 | 블로그가 "wrist-mounted가 본 범위, forearm-integrated는 올해 안에 별도"로 범위에서 뺐다 [3] |

- 블로그가 쓴 DexBench 연결: "T00~T17 중 하드웨어에 민감한 과제에 기준이 대응", "DG-5F-S는 DexBench에서 SharpaWave와 거의 같은 결과", "Wuji는 T16의 4 mm 육각 렌치에서 우수", "SharpaWave는 DexBench의 힘 관련 과제 대부분을 물체·손 손상 없이 수행" [3]. **손별 점수, 시행 수, 과제별 표는 없다.** Q5 결론(DexBench 평가 프로토콜·결과 비공개)과 일치한다 [11].

### 5. DexBench·RLDX-1과의 관계 (항목 4)
| 대상 | 관계 | 근거 |
|------|------|------|
| DexBench | 사이트 간 상호 연결. DexBench 사이트는 ALL HANDS UP(allhandsup.org)을 외부 링크로 둔다. All Hands Up 보도자료는 DexBench 18과제로 손별 특성·한계를 분석했다고 쓰고, 블로그 Part 2는 T00~T17로 평가한다고 쓴다. 두 사이트 모두 RLWRLD 발행이라 독립 검증이 아니다 | [11][3][4] |
| 가치 관점 | DexBench 사이트는 "Dexterity is not a property of the hand"(하드웨어 비종속), All Hands Up은 손 하드웨어 변수를 평가. 서로 모순이라기보다 과제 정의(DexBench)와 손 선택(All Hands Up)의 분업 | [11][3] |
| RLDX-1 | 보도는 "RLDX-1 개발 과정에서 쌓은 손 운용 경험"을 바탕으로 한다고 설명(벤처스퀘어). RLDX-1 지원 선언은 아님. 논문의 OpenArm 실험 손(Inspire RH56F1)만 겹침 | [7][8] |
| ALLEX / Franka Research 3 / OpenArm | ALLEX는 블로그 aside에만, FR3(그리퍼)는 손이 아니라서 없음, OpenArm의 Inspire RH56F1은 갤러리에 있음 | [3][8][1] |
| Type 1 / Type 2 | 사이트가 제시한 하드웨어 이원화 프레임. Type 2(학습 데이터 수집)가 역구동·토크 신호를 학습 데이터로 쓰는 쪽이라 RLDX-1이 ALLEX 관절 토크를 학습 데이터에 포함한다는 서술과 이어진다 | [3] |

### 6. 하네스 PoC 후보 손이 목록에 있는가 (항목 5)
| 후보 | 갤러리 | 비고 |
|------|--------|------|
| Tesollo DG-5F-S (B4 구성안) | **있음** (DG-5F-M도) | 블로그 직접 서술. 소지 CMC 능동, 손끝 모듈 교체 가능(촉각 맞춤 근거), 마찰 낮음(공구 조작 불안정)은 하네스 전선 취급에서 확인할 한계 [3] |
| Inspire | RH56F1이 있음(RH56DFX는 없음) | 기존 reference는 RH56DFX [12]. RH56F1은 6 DoF, 외전 No, 손바닥·손가락 촉각 Yes, 630 g, 훅 30 kg. RLDX-1 논문의 OpenArm 실험 손과 같은 모델 [1][8] |
| Robotiq Hand-E (그리퍼 대조군) | **없음** | 사이트 범위가 다관절 손이다. "미지원"이 아니라 범위 밖이다 [3] |
| XELA uSkin (촉각) | **없음** | 사이트는 촉각을 Yes/No 플래그로만 표기. 센서 모델은 다루지 않는다 [1] |
| Allegro | V5 Plus가 있음 (기존 reference는 V4/V6 F) | 세대가 다르다 [1][12] |

- **스펙표 스크리닝(본 문서 계산, 레지스트리 빈칸은 판정 불가):** RLWRLD가 제시한 Type 목표(길이, 무게, 능동 DoF ≥20, 훅 그립 ≥15 kg, 손끝 정지력)를 DoF 20 이상 7종에 적용했다 [1][3].

| 손 | Type 1(길이 <205 mm, 무게 <600 g) | Type 2(길이 <220 mm, 무게 <900 g, 역구동) | 메모 |
|----|:---:|:---:|------|
| DG-5F-S | 미충족(210 mm, 880 g) | 길이·무게 충족. 훅 12 kg은 목표 15 kg 미달 | 목표 대비 가장 가까운 Type 2형. 손바닥 촉각은 미표기 |
| DG-5F-M | 미충족 | 미충족(1,763 g) | |
| Sharpa Wave | 미충족 | 무게 미충족(1,200~1,300 g) | $50,000 |
| Robotis HX5-D20 | 미충족 | 무게 미충족(1,360 g) | 길이 빈칸 |
| Wuji V1.1 | 길이·무게·훅 20 kg·힘 충족 | 역구동 No | Type 1형이나 충격 파손 위험을 블로그가 지적 |
| Wuji V2 | 무게 미충족(800 g) | 길이·무게·역구동 충족, 훅 빈칸 | 블로그 서술 없음 |
| BrainCo Revo3 | 판정 불가 | 판정 불가 | 무게·길이 빈칸 |

- 해석: RLWRLD 자체 기준으로도 DG-5F-S는 "학습·데이터 수집용 Type 2에 가깝고 현장 배포용 Type 1은 아니다". B4가 DG-5F-S를 PoC 평가 플랫폼으로 쓰는 것은 방향이 맞지만, 배포형 하네스 셀에는 더 가볍고 단단한 손이 필요할 수 있다(`추정`). 훅 그립 12 kg는 제조사 정의 미확인이고 기존 reference의 "6 kg strength"와도 다르다(조건 미표기) [1][12].

### 7. 기존 research/hardware.md·reference와 다른 점, 정정 후보 (항목 6)
| # | 기존 | All Hands Up 소스 | 판단·조치 |
|---|------|-------------------|-----------|
| 1 | DG-5F-S $23,000(humanoid.guide 제품 DB, 공식가 미확인). case/analysis.md 단가와 roi.xlsx 손 소모비가 이 값에 의존 | RLWRLD 블로그 "approximately $7,500 per hand" [3] | **충돌.** 둘 다 공식 견적이 아니다. 블로그는 RLWRLD의 구매·견적 경로일 수 있고(`추정`), DB는 시점·구성이 불명. 단가 교체 대신 B3 민감도에 $7,500을 추가하고 Tesollo 견적으로 확정 |
| 2 | Inspire는 RH56DFX 기준(540 g, 압력 센서 6개) | 갤러리·논문은 RH56F1(630 g, 손바닥·손가락 촉각 Yes) | 모델이 다르다. hardware.md에 RH56F1 행 추가, "OpenArm + Inspire"를 RH56F1로 명시 |
| 3 | Sharpa 1.3 kg, 약 $50,000(2차 소스) | 블로그 1,200 g, 약 $50,000, 손끝 20 N | 가격은 일치. 무게 차이는 구성(손목 등) 차이일 수 있다(`추정`) |
| 4 | Allegro V4 / V6 F | 갤러리는 V5 Plus | 세대 구분 표기 |
| 5 | Wuji, Robotis HX5, Linkerbot L20, BrainCo, Agibot 등 미수록 | 갤러리에 사양 있음 | hardware.md 표를 늘릴 때 레지스트리 값을 "RLWRLD 사이트 표기"로 출처 표기 |
| 6 | DG-5F-S payload "6 kg strength"(제품 DB) | 훅 그립 하중 12 kg | 정의가 달라 보임. 둘 다 조건 미표기 |
| 7 | "Type 1/Type 2" 개념 없음 | 사이트의 손 선택 프레임 | hardware.md 6절(end-effector 선정 프레임)에 RLWRLD 자체 기준으로 추가 |

**B3 영향 계산(본 문서 계산, `추정`, B3 재실행 전 참고용).** 손 단가만 $23,000에서 $7,500으로 바꾸고 나머지는 case/analysis.md 7.5절 기본값(환율 1,400원, 손 2개, 교체 20%, 셀 합계 연 4회 교체)을 유지하면:
- 손 투자 감소 = 2 x (23,000 - 7,500) x 1,400 = 43,400,000원.
- 손 소모비 = 4 x 0.2 x 7,500 x 1,400 = 8,400,000원/년(기존 25,760,000원), 연 17,360,000원 감소.
- 단순 회수 약 (395,600,000 - 43,400,000) / (88,060,000 + 17,360,000) = 약 3.3년(기존 약 4.5년). 통합비·유지보수비가 손 가격에 연동되면 더 짧아지므로 이 값은 근사다.
- 즉 손 단가는 B3의 1~2순위 변수다. 단가 확정 없이 헤드라인 회수 연수를 바꾸지 않는다.

### 8. 사이트의 한계와 읽을 때의 주의
- 가격, 구동 방식, 내구성 수명, 시행 수가 갤러리에 없다. 사양은 제조사 값, 자체 계산, 자체 측정이 섞여 있다.
- 평가 점수(DexBench 손별 결과, 평가 DB 점수)는 공개되어 있지 않다. "고득점", "거의 같은 결과" 같은 서술만 있다.
- 사이트의 손 이미지는 AI 생성이며 실제 제품과 다를 수 있다고 고지한다 [1].
- 레지스트리는 편집 중인 파일이다. 같은 URL이 시간이 지나면 다를 수 있으므로 인용 시 조회일(2026-10-12)을 붙인다.
- 숨김 4건은 공개 파일에 남아 있지만 사이트가 의도적으로 노출하지 않는 스테이징 데이터다. 사용하지 않는다.
- 렌더된 화면은 열어 보지 못했다. 노출 18종은 JSON과 필터 코드(`!h.hidden`)로 추정한 것이다.

## RX 관점 시사점
- **고객 제안:** B4의 PoC 평가 플랫폼 서술을 "RLDX-1 지원 하드웨어"가 아니라 "RLWRLD가 공개 평가 서술을 가진 손 중 하나(DG-5F-S)로 구성하고, 그리퍼 대조군(Hand-E)과 촉각(uSkin)은 별도 조달"로 쓴다. 호환 보증이나 사전 검증 완료로 읽히는 문장은 피한다.
- **DG-5F-S 근거:** RLWRLD 서술 기준 가격이 SharpaWave의 약 1/7인데 DexBench 결과는 비슷하다는 점이 비용 근거다. 단 점수 비공개의 자체 평가라 "RLWRLD 서술에 따르면"으로 표기한다. 마찰이 낮아 공구를 불안정하게 쥔다는 서술은 하네스 전선 취급에서 손끝 모듈(마찰 소재) 교체를 PoC 시험 항목에 넣는 근거다.
- **Inspire:** RLDX-1 논문에 실로봇 결과가 있는 유일한 갤러리 손이다(RH56F1, 단순 pick-and-place 계열). 하네스 레이업에는 외전이 없고 6 DoF라 한계가 있어, 저가 비교 손(대조군) 후보로 둘 수 있다(`추정`).
- **B3:** 손 단가 $7,500 대 $23,000은 민감도 변수로 추가한다. 이 값은 사실 확인 전까지 헤드라인에 쓰지 않는다.
- **면접:** "ALL HANDS UP은 무엇인가"는 "RLWRLD가 10종 이상의 손을 운용한 경험으로 낸 손 분석·URDF 아카이브이고, 설계 트레이드오프(크기·파지력·역구동)와 학습용(Type 2)/배포용(Type 1) 이원화를 제안한다. 호환 목록이 아니라 평가 자료이며, 점수는 비공개다"로 답할 수 있다.

## 확인하지 못한 항목
- 렌더된 갤러리의 실제 노출 수와 순서(JSON 추정).
- "지원(호환·학습)"의 회사 공식 정의. 사이트에는 없음.
- 갤러리 18종 중 RLWRLD가 실제로 운용한 손의 범위, DexBench 손별 점수.
- DG-5F-S의 실제 구매가($7,500 대 $23,000)와 DG-5F 대비 가격 비율(검색 요약은 "DG-5F의 약 60% 수준 책정 예정"이라 하나 기사 미열람, `추정`).
- 일본어판 블로그 본문의 서술 차이(수치만 대조).
- Part 3 공개 일정, 갤러리 갱신 주기의 실제 이행.
- 훅 그립 하중·손끝 힘의 측정 정의.

## 사용자 피딩 요청 목록
| 대상 | 왜 필요한가 | 어디서 얻나 |
|------|-------------|--------------|
| 브라우저로 allhandsup.org/ko/ 갤러리 화면 캡처(노출 손 수, SOON 타일 유무) | JSON 기반 18종 추정을 확정 | Chrome에서 직접 열람. 스크린샷 첨부 |
| 손 상세 패널의 "specs complete/pending" 표시 | 사양 신뢰도 판단 | 같은 화면(손 선택 시 우측 패널) |
| DG-5F-S 공식 견적(구성, 수량, 환율) | $7,500 대 $23,000 충돌 해소. B3 핵심 변수 | Tesollo 영업 문의 (tesollo.com) |
| 손 지원(호환) 정의와 DexBench 손별 결과 | 사용자 설명 "RLWRLD가 지원하는 하드웨어"의 근거 확인 | partnership@rlwrld.ai (블로그 문의처) |
| 갤러리 변경 이력 | 분기별 갱신 확인 | allhandsup.org/hands_urdf/_registry.json을 분기마다 재저장 후 비교 |

## 출처
1. [All Hands Up! 사이트 홈, _registry.json, _kapandji.json](https://allhandsup.org/ko/) - RLWRLD 발행, 열람 2026-10-12, 1차, (en) (reference/hardware--allhandsup-gallery.md)
2. [All Hands Up! Part 1 - Why Dexterity Matters](https://allhandsup.org/blog/part1) - RLWRLD, 열람 2026-10-12, 1차, (en)(ko 대조) (reference/hardware--allhandsup-blog-part1.md)
3. [All Hands Up! Part 2 - What Makes a Good Robot Hand](https://allhandsup.org/blog/part2) - RLWRLD, 열람 2026-10-12, 1차, (en)(ko·ja 수치 대조) (reference/hardware--allhandsup-blog-part2.md)
4. [リアルワールド、ロボットハンド分析プラットフォーム「All Hands Up!」を公開](https://prtimes.jp/main/html/rd/p/000000003.000183256.html) - PR TIMES(RLWRLD 보도자료), 2026-07-01, 1차, (ja) (reference/hardware--allhandsup-prtimes.md)
5. [리얼월드, 로봇 손 분석 플랫폼 '올핸즈업!' 공개](https://byline.network/2026/06/22_1928373/) - 바이라인네트워크, 2026-06-22, 기사, (ko) (reference/hardware--allhandsup-byline.md)
6. [RLWRLD launches All Hands Up robotic hand benchmarking platform](https://roboticsandautomationnews.com/2026/07/07/rlwrld-launches-open-platform-to-benchmark-dexterous-robotic-hands/103146/) - Robotics & Automation News, 2026-07-07, 기사, (en) (reference/hardware--allhandsup-ran.md)
7. ["좋은 로봇 손은 무엇인가"…리얼월드, 로봇 손 성능 비교 플랫폼 공개](https://www.venturesquare.net/1092581/) - 벤처스퀘어, 열람 2026-10-12, 기사, (ko) (raw: reference/raw/hardware--allhandsup-venturesquare.txt, 별도 reference 파일 없음)
8. [RLDX-1 Technical Report](https://arxiv.org/abs/2605.03269) - arXiv, 2026-05-05, 논문, (en) (reference/papers--rldx1-tech-report.md; Figure 12 설명과 6.2절은 raw 925~929행, 기여자 절 2837~2847행)
9. [RLWRLD/RLDX-1 GitHub README](https://github.com/RLWRLD/RLDX-1) - RLWRLD, 열람 2026-10-09, 1차, (en) (reference/company--github-rldx1.md; raw 286~346행)
10. [ORCA: An Open-Source, Reliable, Cost-Effective, Anthropomorphic Robotic Hand](https://arxiv.org/abs/2504.04259) - arXiv, 논문, (en) (reference/papers--orca-hand.md)
11. [DexBench 공식 사이트](https://dexbench.org/en/) - RLWRLD, 열람 2026-10-09, 1차, (en)(ko)(ja) (reference/benchmark--dexbench-site.md, research/q5-dexbench.md)
12. 기존 하드웨어 reference: reference/hardware--tesollo-dg5f-s.md(humanoid.guide 제품 DB), reference/hardware--inspire-rh56dfx.md, reference/hardware--sharpa-wave-spec.md, research/hardware.md (2026-10-06)
