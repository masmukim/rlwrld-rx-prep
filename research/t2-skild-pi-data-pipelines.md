# Skild AI와 Physical Intelligence(PI)의 데이터 파이프라인 비교 근거표
조사일: 2026-10-17

## 핵심 요약
- **대비가 선명한 곳은 두 군데뿐이다.** (a) 선언된 규모의 출처: Skild는 시뮬레이션과 인터넷 인간 영상을 사전학습의 본체로 내세우고[1][2], PI는 논문에서 자체 수집 로봇 시연(π0는 약 10,000시간·9억 3백만 타임스텝, π*0.6은 "수만 시간")과 이종 로봇·웹 데이터를 보여 준다[11][12][13]. 다만 Skild는 출처별 비율과 규모를 공개하지 않아 이 대비는 "서술 대 논문 수치"의 비대칭 비교다. (b) 사업 구조: Skild는 로봇 제조사(OEM) 탑재와 직접 배포, PI는 파트너 하드웨어 위의 모델·API 공급이다[2][16][17].
- **"Skild=인간 영상·시뮬, PI=실로봇"이라는 이분법은 허수아비 위험이 크다.** Skild도 텔레오퍼레이션·장갑·UMI를 쓴다고 쓰고[3][5], PI도 인간 에고센트릭 데이터(수십 시간)와 웹 데이터를 쓴다[12][15]. 두 회사는 배포 후 데이터를 모델로 되돌리는 순환(Skild "Physical RSI", PI "Recap")에서 수렴한다[4][13][14]. 차이는 비율과 우선순위의 선언이며, 공개 정보로는 비율을 확정할 수 없다.
- **병목은 공개 근거가 있는 것만 적었다.** Skild 쪽은 인간 영상의 도메인 격차·행동 라벨 부재(Skild 자신의 표와 PI·EgoScale 논문), 인간 데이터 상한(Skild 자기 서술), 환류 데이터의 권한과 규모 미공개다. PI 쪽은 실로봇 수집의 사람 노동(라벨·개입·리셋, 논문 한계 절), 사전학습 구성 최적화 미해결(π0 한계 절), 파트너 의존과 데이터 권리 미공개다. 두 회사의 성능 수치는 모두 자체 평가이고 평가 조건이 달라 서로 비교할 수 없다.

## 본문

### 0. 읽는 법
공개 수준 태그를 모든 주장에 붙인다.

| 태그 | 뜻 | 이 문서에서의 예 |
|------|-----|------------------|
| 공식 1차 | 회사 자신의 블로그·보도자료 | Skild 블로그, PI 블로그 |
| 논문 본문 | arXiv 본문을 저장해 Grep으로 확인 | π0, π0.5, π*0.6, 인간→로봇 전이, EgoScale, OXE |
| 초록·서술 | 초록이나 회사 서술 수준(수치 근거가 약함) | 논문 초록의 요약 문장, 회사의 "주장" |
| 보도·2차 | 기사, 협력사(NVIDIA) 게시물, 인터뷰 보도 | Humanoids Daily, NVIDIA 블로그, TECHBLITZ |
| 추론 | 본 팀 해석. 근거 문장이 없음 | OEM 탑재의 데이터 의미 등 |

시점: 각 사실에 근거 날짜를 적었다. Skild 데이터 철학의 최초 서술은 2025-07-29[1]로 1년 이상 됐고, 이후 글에서 출처 목록이 넓어졌다. PI의 최신 모델 π0.7(2026-04)의 데이터 구성은 1차 소스를 확보하지 못했다(`확인필요`).

### 1. Skild AI의 파이프라인

#### 1.1 사전학습 데이터 소스

| 출처 | 공개된 내용 | 태그 | 근거 시점 |
|------|-------------|------|-----------|
| 인터넷 인간 영상 | "large-scale simulation and internet video data to pre-train" [1]. "internet-scale human videos and large-scale robot simulations for pretraining" [2]. 사람도 "a form of robot"로 보고 형태가 다른 데이터를 함께 학습한다고 서술 [1]. 영상에서 affordance(물체를 어떻게 다뤄야 하는지)를 추출한다는 설명은 NVIDIA 고객 사례에 있음 [6] | 공식 1차 [1][2] / 보도·2차(공급사) [6] | 2025-07, 2026-03, NVIDIA 문서 날짜 미확인 |
| 시뮬레이션·합성 | Isaac Lab·Sim으로 물리 시뮬레이션, Cosmos로 합성 데이터 생성·증강 [2]. NVIDIA 문서는 "billions of training examples" 생성을 서술 [6] | 공식 1차 [2] / 보도·2차(공급사) [6] | 2026-03, 날짜 미확인 |
| 텔레오퍼레이션·장갑·UMI | S1 단계 도식에 사전학습 데이터를 "Human videos, gloves, simulation, teleoperation"으로 적음 [5]. S1 블로그 데이터 엔진 절: 텔레오퍼레이션(하드웨어 근접성 높음, 다양성·확장성 낮음), UMI(모두 중간), 에고센트릭 영상(근접성 낮음, 다양성·확장성 높음), 시뮬레이션(중간/낮음/높음)으로 평가하고 "Skild has been scaling all of them in-house"라고 씀 [3] | 공식 1차 [3][5] | 2026-08, 2026-09경(날짜 `추정`) |
| 배치 데이터 | "where permitted, deployment data" [7]. Skild 자신은 배치 데이터를 특화에 쓰고 일반 모델로 되돌린다고 서술 [4] | 보도·2차(협력사) [7] / 공식 1차 [4] | 2026 |

- 출처별 비율, 시간, 건수는 어느 소스에도 없다. S1 블로그의 "1k~100k시간"은 "사전학습 풀의 필터링된 부분집합"에서 뽑은 통제 실험 크기이며 전체 풀의 크기나 구성이 아니다[3]. 공식 1차.
- 규모 철학: "achieving scale requires collecting trillions of examples - and there is no way just real world data can achieve this scale in near future"[1]. 공식 1차(주장, 각주는 지구 전 인구가 모아도 100조 궤적까지 수년 걸린다는 개략 계산). 실데이터를 "less than 1%" 얹는 방식의 모델은 "행동 정보가 없다"고 비판하지만 대상 회사를 지목하지 않는다[1]. 공식 1차.
- 시점 변화: 2025-07에는 "시뮬레이션과 인터넷 영상 + 목표 실데이터 후학습"[1], 2026-08~09에는 텔레오퍼레이션·UMI·장갑이 목록에 들어온다[3][5]. 출처가 늘어난 것인지 서술 범위만 넓어진 것인지는 소스로 가를 수 없다. 추론.
- 품질 관리: "For every dollar we spend on collecting data, we spend three on quality control. Every data point entering pre-training is screened for low-level precision, task coherence, and annotation fidelity"[3]. 공식 1차(주장, 절차·통과율 비공개).

#### 1.2 현장 적응과 post-training

| 단계 | 내용 | 태그 |
|------|------|------|
| 기본 방식 | 기본 모델을 "small amount of task data"로 후학습(post-training)하는 것이 기본안 [2] | 공식 1차, 2026-03 |
| S1(2026-08) | 영상 시연 1개를 프롬프트로 주면 가중치 갱신 없이 새 작업 수행(컨텍스트 학습). 처음 보는 작업, 100k시간 사전학습 조건에서 성공률 66% 대 언어 프롬프트 VLA 9%. 시연 1개가 약 380개 후학습 시연과 동급이며 380은 측정점 사이 보간 추정. 380개 수집에 텔레오퍼레이션 50~100시간 [3] | 공식 1차(자체 벤치마크) |
| 평가 조건 | 지표는 누적 단계 성공률 평균. 모든 단계를 채점하려고 실패 시 사람이 개입해 복구했고 개입은 주로 VLA 기준선에 쓰였음. 비교 VLA는 같은 데이터·구조로 Skild가 직접 학습한 기준선 [3] | 공식 1차 |
| 한계의 자기 서술 | 생산 수준의 속도·신뢰성이 필요하면 배치 데이터로 특화(후학습)한다 [4] | 공식 1차, 2026-09 |

- 해석 주의: "텔레오퍼레이션 없이 새 작업"이라는 문장은 S1의 시연 프롬프트 방식에 한정된다. 같은 회사가 생산 수준에서는 후학습을 병행한다고 쓰므로[4], 현장에서 텔레오퍼레이션 수집이 사라진다는 근거는 없다. 논문 아닌 회사 서술 사이의 정합성 판단이므로 추론.
- 66%는 하네스 같은 특정 산업 성능이 아니라 일반 장기 과제의 내부 벤치마크 값이다[3]. 공식 1차.

#### 1.3 구현체 불문(omni-bodied) 모델의 데이터 전략

| 항목 | 내용 | 태그 |
|------|------|------|
| 주장 | 사족보행, 휴머노이드, 탁상 팔, 모바일 매니퓰레이터를 하나의 모델이 제어. 다양한 형태가 학습 데이터를 늘리고 하드웨어 변화·고장에 견고하게 만든다 [1] | 공식 1차, 2025-07 |
| 구조 | 저주파 상위 정책(조작·이동 계획) + 고주파 하위 정책(관절 각도·모터 토크). 배포 시 미세조정·증류 [1] | 공식 1차 |
| 정량 증거 | 형태 다양성이 효과를 낸다는 별도의 어블레이션 수치는 읽은 Skild 1차 글(위 [1]~[5])에서 찾지 못했다 | 공식 1차 범위 내 미확인 |
| 독립 근거(타사) | 형태 간 공동 학습의 긍정 전이는 OXE에서 보고되나 데이터가 적은 구현체에서 뚜렷하고, 대규모 데이터 도메인에서 RT-1-X(소형)는 구현체 단독 기준선을 넘지 못했다(55B RT-2-X는 넘음) [19]. π0.5는 다른 로봇 데이터(ME, CE)를 빼면 성능이 크게 떨어졌다 [12] | 논문 본문 |

- "모든 몸체를 하나의 모델로"가 데이터 효율에 도움이 된다는 방향은 타사 논문이 지지한다. 그러나 Skild 자신의 효과 크기는 공개되지 않았다. 추론.

#### 1.4 현장 데이터 수집과 배포 순환("Physical RSI", 데이터 플라이휠)
- 서술: 여러 로봇·작업·구현체로 학습한 기반 모델을 배치 → 컨텍스트 학습으로 변화에 적응, 필요하면 배치 데이터로 특화 → 많은 배치의 데이터를 일반 모델로 되돌려 다음 배치는 더 강한 모델에서 시작[4]. 공식 1차, 2026-09-10.
- 자기 인정: 배치 데이터에 대해 "배치가 궁극의 데이터원"과 "너무 좁다"는 두 견해가 모두 부분적으로 맞다고 쓰고, 이미 숙달한 전문 시스템에 같은 동작 수천 건을 더해도 얻을 것이 적다고 적는다. 가치는 많은 전문 시스템의 학습이 일반 모델로 돌아올 때 생긴다는 주장이다[4]. 공식 1차.
- 플라이휠: 옴니 보디드라 여러 로봇의 데이터를 흡수하고, 현장 로봇이 다음 세대 학습 데이터를 모은다고 서술[2]. 공식 1차. CEO 인터뷰는 2년 목표를 "배치 수를 늘려 데이터를 두뇌로 계속 되돌리는 것"이라 말했다[9]. 보도·2차(인터뷰).
- 미공개: 환류 데이터의 양과 비율, 증류 방법, 고객 데이터를 모델 학습에 쓸 권한. NVIDIA 문서가 "where permitted"라는 조건을 붙인 것이 유일한 단서다[7]. 보도·2차.
- 판매 방식(데이터 흐름에 영향): 목표는 RaaS(월·연 요금). 현 단계는 두뇌 단독 판매 없이 Skild가 직접 미세조정해 제공한다고 CEO가 말했다[9]. 보도·2차(인터뷰).

#### 1.5 로봇 제조사 탑재(ABB, UR)가 데이터에 주는 의미

| 층위 | 내용 | 태그 |
|------|------|------|
| 공개된 사실 | 2026-03-19 글에서 ABB Robotics, UR(Teradyne), MiR을 OEM 파트너로 나열하나 통합 서술은 ABB·UR에 대해 "our goal is to integrate"(목표 문구)이고 MiR은 이름만 있다 [2]. 이미 배치된 산업 로봇에 "shared intelligence layer"를 넣는다는 설명 [2] | 공식 1차 |
| 공개된 사실(데이터) | "the Skild brain can ingest data from different robots ... existing robots in the field help gather data to train the next improved generation" [2] | 공식 1차 |
| 미공개 | OEM이 판매·설치한 로봇의 데이터가 Skild로 되돌아오는 계약 구조, 수집 인프라, 고객 동의 방식 | 확인필요 |
| 우리 추론 | OEM 설치 기반이 데이터 환류 채널이 되려면 (1) 원격 수집 인프라 (2) 고객·OEM 계약의 데이터 사용 권한 (3) 로봇 모델이 달라도 통합 형식이 필요하다. 공개 소스에는 셋 다 없다. OEM 탑재는 "목표" 단계이고 현 단계는 Skild 직접 미세조정이므로[2][9], OEM 경로의 데이터 효과는 아직 증거가 아니라 가설이다 | 추론 |
| 고객 단계(일본) | 住友電装: "공동 개발 개시"(일본어 릴리스), Skild 블로그는 "working towards deploying". 대상 공정·로봇·핸드·성과 미공개 [8][4] | 공식 1차 |

### 2. Physical Intelligence의 파이프라인

#### 2.1 모델별 데이터 구성(논문 본문 확인)

| 모델 | 데이터 구성 | 태그·시점 |
|------|-------------|-----------|
| π0 (2024-10-31 제출, 2026-01 개정) | 사전학습 혼합에서 오픈소스(OXE, Bridge v2, DROID)가 9.1%. 나머지는 자체 데이터 903M 타임스텝(단일팔 106M, 양팔 797M), 약 10,000시간 시연(논문 서술), 7개 로봇 구성, 68개 작업. 오픈소스는 2~10 Hz, 자체는 최대 50 Hz. 사전학습된 VLM에서 시작해 인터넷 규모 의미 지식을 상속. 후학습 데이터는 작업별로 가장 쉬운 것 5시간, 복잡한 것 100시간 이상 [11] | 논문 본문 |
| π0.5 (2025-04) | 이동형 매니퓰레이터 가정 데이터(MM, 약 400시간, 약 100개 가정) + 고정형 로봇 다환경(ME) + 실험실 교차 구현체(CE, OXE 포함) + 하위작업 예측(HL, 수동 주석) + 웹 멀티모달(WD) + 후학습의 말 지시 시연(VI). 사전학습 예시의 97.6%가 이동형 매니퓰레이터의 가사 작업이 아닌 다른 로봇·웹 출처 [12] | 논문 본문 |
| π*0.6 (RECAP, 2025-11) | 사전학습: "tens of thousands of hours of demonstrations from numerous tasks and a variety of different robots" + 웹 비전-언어 데이터. 이후 작업별로 시연 → 자율 롤아웃 → 전문가 교정(텔레오퍼레이션 개입) → 값 함수·정책 재학습 반복 [13] | 논문 본문 |
| 인간→로봇 전이 (2025-12) | π0.5에 머리 장착 카메라 에고센트릭 인간 데이터를 공동 학습. 작업별 3~5시간, 합 14시간(계산). 저자 표현 "10s of hours". 결과(작업 점수): 향신료 32→71%, 서랍장 25→50%, 정리 53→63%, 달걀 분류 정확도 57→78% [15] | 논문 본문 |
| π0.6 파트너 데이터 (2026-02) | Weave 데이터를 사전학습에 넣으면 놓친 파지 42% 감소, 세탁물 1판당 사람 개입 50% 감소(특화 학습 조건). 두 수치는 조건이 다르다 [16] | 보도·2차 |
| π0.7 (2026-04-16) | 조합적 일반화, 웹 규모 데이터 + 작업별 데이터라는 기사 서술. 데이터 구성의 1차 소스 미확보 [18] | 보도·2차, `확인필요` |

- 시간 환산: 논문 서술은 사전학습 혼합이 "about 10,000 hours of demonstrations"(+ OXE)다[11]. 903M 타임스텝을 10,000시간으로 나누면 평균 약 25 Hz(계산)로, 로봇별 제어 주파수(20~50 Hz)와 모순되지 않는다. 논문 본문.
- π*0.6 데이터량 예: 다양한 세탁물 평가 450 + 교정 287 에피소드, 상자 조립은 배포 현장에서 반복당 600 + 교정 360 에피소드(로봇 3대). 이 600은 본문(autonomous trials)과 부록(demonstrations)이 다르게 적혀 확정하지 못했다[13]. 논문 본문(내부 불일치).
- 학습 데이터로서의 시뮬레이션: π0, π0.5, π*0.6 본문에서 시뮬레이션 데이터 사용 서술을 찾지 못했다(키워드 검색에서 참고문헌 제목 1건뿐)[11][12][13]. 단 "찾지 못함"이지 "사용하지 않음"의 증명은 아니다. 논문 본문(부정 확인의 한계).

#### 2.2 파트너 운영 데이터와 교정 루프
- 구조: 파트너가 하드웨어와 현장을 소유하고 PI는 모델을 공급한다는 언론의 정리[16]. 보도·2차.
- API 베타(기사 표기 2026-10-13): 팀이 시연을 올려 PI 인프라에서 미세조정하고 로봇에서 시험한 뒤 실패 주변 데이터를 더 모으는 흐름. 신청서가 보유 텔레오퍼레이션 데이터와 예정 시뮬레이션 데이터를 묻는다. 데이터 소유·사용 조건과 가격은 기사에 없다[17]. 보도·2차(PI 1차 페이지 미열람).
- PI 블로그: 시연은 새 행동을 정의하고, 코칭(교정)은 전략을 다듬고, 자율 경험은 "potentially the largest source of data"로 완성도를 높인다는 전망. 배치 로봇 데이터를 모으는 기업과의 협업을 모집한다[14]. 공식 1차(2025-11-17).
- 교정 방식의 한계(PI 자신): 교정의 질은 사람이 개입 시점을 알아채고 고품질 교정을 주는 능력에 묶인다[14]. 공식 1차. 시스템은 "relies on human labeling and effort for reward feedback, interventions, and episode resets"[13]. 논문 본문.

### 3. 두 회사의 대비축 (선명한 축과 겹치는 축)

| 축 | Skild | PI | 판정 | 근거 |
|----|-------|----|------|------|
| 규모의 출처 | 시뮬레이션·인터넷 인간 영상을 본체로 서술, 비율 비공개 [1][2] | 자체 수집 로봇 시연이 본체(π0 약 10,000시간·903M 타임스텝, π*0.6 "tens of thousands of hours"), 웹·타 로봇 데이터 병용 [11][12][13] | **선명(단, 비대칭 비교)** | Skild는 서술, PI는 논문 수치 |
| 인간 영상 사용 | 사전학습의 한 축 [1][2] | 수십 시간 규모의 공동 학습, 로봇 사전학습 다양성이 선행 조건 [15] | 겹침 | 사용 여부는 같고 규모·역할이 다름 |
| 텔레오퍼레이션 | 사용(데이터 엔진 표의 한 줄, 380 시연=50~100시간 비교 기준) [3][5] | 핵심 데이터(시연 + 교정) [11][13] | 겹침 | 양사 모두 사용 |
| 시뮬레이션 | 핵심 축(Isaac, Cosmos, 자기 대전) [2][5] | 논문 본문에서 사용 서술 못 찾음 [11][12][13] | 선명(PI는 "찾지 못함") | 부정 확인의 한계 |
| 품질 관리 | 수집 $1당 QC $3, 모든 사전학습 데이터 검사(절차 비공개) [3] | 작업·로봇 조합 가중(n^0.43), 후학습에 성공 에피소드·길이 임계 필터, 사람 평가자 성공 라벨 [11][12][13] | 비교 불가 | Skild 절차 비공개 |
| 비용 | 380 시연 = 50~100시간 텔레오퍼레이션(S1 비교 기준) [3] | 작업별 후학습 5~100시간 이상, 라벨·개입·리셋의 사람 노동 [11][13] | 비교 불가 | 비용 단위가 다름, 금액 없음 |
| 일반화 | 처음 보는 작업 66% 대 VLA 9%(내부 벤치마크, 개입 포함) [3] | 처음 보는 가정 일반화(훈련 가정 수 3→104, 작업당 10회 시행), 조합 일반화 주장(π0.7, 기사) [12][18] | 비교 불가 | 평가 프로토콜 상이, 모두 자체 평가 |
| 구현체 종속성 | omni-bodied 주장, 사족보행·휴머노이드 포함, 정량 어블레이션 미확인 [1] | 7개 로봇 구성, 타 로봇 데이터 어블레이션 있음 [11][12]. 보행 등 범위 밖은 후속 과제라고 씀 [11] | 부분 선명(범위) | 둘 다 교차 구현체 지향, 범위가 다름 |
| 배포 후 교정 루프 | Physical RSI: ICL로 재학습 회피 + 배치 데이터 특화 → 일반 모델로 환류 [4] | Recap: 시연 + 자율 롤아웃 + 교정 → 값 함수 → 재학습, 파트너 데이터 사전학습 반영 [13][16] | **수렴** | 양사 1차 소스가 배치 경험을 핵심 데이터원으로 지목 |
| 사업 구조 | OEM 탑재 목표 + 직접 미세조정 제공 + RaaS 목표 [2][9] | 파트너 하드웨어 위 모델·API 공급, 일부 체크포인트(openpi) 공개(기사) [16][17] | 선명 | 데이터 환류 경로에 영향(추론) |
| 데이터 권리 | "where permitted" 한 줄 [7] | 공개 없음 [17] | 양쪽 미공개 | 확인필요 |

### 4. 이분법이 허수아비일 수 있다는 점 검토
1. **반례가 양방향에 있다.** Skild는 텔레오퍼레이션·장갑·UMI를 쓰고[3][5], PI는 인간 에고센트릭과 웹 데이터를 쓴다[12][15]. "한쪽은 실로봇, 한쪽은 비로봇"은 홍보 수준의 선언일 때만 성립한다.
2. **Skild의 "<1% 실로봇" 비판은 PI를 지목하지 않는다.** 그리고 PI 논문은 로봇 데이터를 타임스텝·시간으로 보고하고[11][13], 웹 대비 비율은 정의할 수 없다. 이 비판을 PI에 대한 사실로 쓰면 안 된다[1].
3. **PI의 인간 영상 논문은 오히려 Skild와 가까운 쪽으로 이동하는 신호다.** 단 조건이 붙는다. 인간 데이터는 로봇 사전학습의 다양성이 충분히 클 때만 이득이 났고, 규모는 수십 시간이었다[15]. 인간 영상이 사전학습의 본체인 연구는 EgoScale(20,854시간)와 GR00T N1.7이다[20][21].
4. **선언과 비율을 구분한다.** 세 가지가 공개돼야 이분법을 검증할 수 있다: 출처별 학습 시간(또는 비중), 출처 제거 어블레이션, 배치 데이터의 환류량. Skild는 셋 다 없고 PI는 둘째까지 일부(π0.5의 타 로봇·웹 제거 어블레이션)만 있다[12].
5. **결론.** 실제로 선명한 차이는 (i) 사업 구조가 데이터 접근권에 미치는 영향, (ii) 시뮬레이션에 대한 의존 선언, (iii) 보행 포함 여부 정도다. 이 중 (i)은 추론이다.

### 5. 장단점과 리스크(근거가 있는 것만)

| 접근 | 장점 | 병목·리스크 | 근거와 태그 |
|------|------|-------------|-------------|
| Skild: 시뮬+인간 영상 중심 | 확장성이 높다고 자체 평가 | **도메인 격차**: 자사 표에서 에고센트릭 영상은 하드웨어 근접성 낮음, 시뮬레이션은 다양성 낮음으로 적음 [3] (공식 1차). **행동 라벨 부재·리타게팅**: EgoScale은 인간 손을 로봇 손 관절로 최적화 리타게팅하고 비제약 수집의 노이즈를 인정, 소량 정렬 데이터(인간 약 50시간+로봇 약 4시간)가 필요하다고 씀 [20] (논문 본문). PI 논문은 그리퍼 개폐를 인간 영상에서 근사하지 않음 [15] (논문 본문). Skild가 같은 문제를 어떻게 푸는지는 1차 글에서 확인 못함 | 위 태그 |
| Skild: 인간 데이터 상한 | - | 인간 데이터로 사전학습한 모델은 "capped at human capability"라고 Skild가 스스로 쓰고 자기 대전으로 넘으려 한다. 단 그 결과는 시뮬레이션 내 축구이고 현실 전이는 한 줄 서술 [5] | 공식 1차 |
| Skild: 시뮬레이션 | 실패 시나리오를 안전하게 대량 경험(공급사 설명) [6] | **시뮬-현실 간극**: 공급사 문서는 Cosmos가 sim-to-real 전이를 개선한다고 서술[2][6]하나, 접촉이 많은 손 조작에서 시뮬 데이터가 기여했다는 수치는 공개 소스에 없다. Foxconn 나사 체결 셀의 학습 데이터 구성도 비공개 [2] | 공식 1차 + 보도·2차, 수치 `확인필요` |
| Skild: 컨텍스트 학습 | 변화마다 재수집·재학습 회피 | 평가가 내부 벤치마크, 사람 개입 포함, 비교 VLA를 Skild가 학습, 380은 보간 추정 [3]. 생산 수준에서는 후학습 병행 [4] | 공식 1차 |
| Skild: OEM·배치 | 설치 기반 확대(추론) | 환류 데이터의 양·권한 미공개 [4][7]. OEM 탑재는 목표 문구 [2], 현 단계는 직접 미세조정 [9]. 배치 데이터가 좁다는 점을 Skild가 인정 [4] | 공식 1차, 보도·2차 |
| PI: 실로봇 시연 + 교정 | 데이터 구성과 어블레이션이 논문에 공개(타 로봇 제거 시 하락 등) [12] | **수집 비용·속도**: PI도 "data requires human effort ... limited to human-level"을 인정 [14]. 교정·보상 라벨·리셋에 사람 노동 [13]. 후학습이 작업별 5~100시간 이상 [11] | 공식 1차, 논문 본문 |
| PI: 사전학습 구성 | 이종 로봇·웹 병용 | 어떤 데이터를 얼마나 섞을지는 미해결("we combined all data available to us")이고 다른 영역(보행 등)으로의 확장은 후속 과제 [11] | 논문 본문 |
| PI: 평가 범위 | 문서화된 평가 | π*0.6의 반복 개선 실험은 6-DoF 팔 2개 + 평행 조 그리퍼의 정적 양팔에서 수행 [13]. 다지 손에서의 증거는 이 논문에 없다 | 논문 본문 |
| PI: 파트너 의존 | 파트너 현장 데이터를 사전학습에 반영(+WPT), 분산된 배치 | 하드웨어·현장은 파트너 소유 [16]. 데이터 소유·사전학습 사용 허용 조건 비공개 [17]. 파트너 데이터는 이질적이라 도메인별 특화가 필요(추론) | 보도·2차, 추론 |
| 공통: 인간 영상 | 규모 확장성(EgoScale에서 log-linear 스케일링 보고) [20] | 소량의 정렬된 인간-로봇 데이터가 여전히 필요 [20]. 로봇 사전학습의 다양성이 임계 수준에 못 미치면 전이가 안 됨 [15]. EgoScale의 +54%는 상대/%p가 본문 서술만으로 확정되지 않음(초록 "54% average success rate", 본문 "over 55% task completion") [20] | 논문 본문 |

### 6. 세 번째 기준점: RLWRLD의 위치
RLWRLD는 두 회사의 중간이 아니라 세 번째 축에 있다. RLDX-1 사전학습은 공개 데이터셋 조합(OXE, DROID, AgiBot World 등)이고 사내 데이터는 mid-training의 새 입력(기억·토크·촉각)의 감독 신호로 쓰이며, 블로그는 사전학습 데이터를 "다양한 실제 데이터셋"으로만 서술한다[22]. 데이터 확보 방식은 직원 착용 카메라 에고센트릭 수집, 텔레오퍼레이션(ALLEX), 인간 손 캡처 리타게팅, 비디오 생성 합성이며, 롯데호텔·KDDI 등 고객·투자자 현장에서 모으고 KDDI와 연 3,500시간 상당을 목표로 한다[22][23]. 철학만 보면 에고센트릭의 확장성(Skild식)과 텔레오퍼레이션 교정(PI식)을 함께 쓰고 고객 현장을 데이터원으로 둔 것이 특징이다. 단, 고객 현장 데이터가 성능에 기여한 정량 증거는 공개된 것이 없고, 에고센트릭 접근은 EgoScale·GR00T N1.7과도 겹친다[20][21]. 이상은 기존 조사 문서에 근거한 정리이며 새 조사가 아니다.

### 7. 꼬리질문 10개와 근거 있는 답의 요지

| # | 질문 | 답의 요지 | 출처·태그 |
|---|------|-----------|-----------|
| 1 | Skild는 실로봇 데이터를 안 쓰나? | 쓴다. 사전학습 도식에 텔레오퍼레이션·장갑이 있고 S1 블로그가 텔레오퍼레이션·UMI·에고센트릭·시뮬레이션을 모두 키운다고 쓴다. 다만 비율은 비공개 | [3][5] 공식 1차 |
| 2 | PI는 인간 영상을 안 쓰나? | 쓴다. 단 수십 시간(합 14시간)이고, 로봇 사전학습이 충분히 다양할 때만 이득이 났다 | [15] 논문 본문 |
| 3 | S1의 66% 대 9%는 Skild가 PI보다 낫다는 뜻인가? | 아니다. 같은 데이터로 Skild가 직접 학습한 언어 조건 VLA와의 비교이고, 내부 벤치마크이며 사람 개입 포함 누적 단계 점수다. PI 모델과 비교한 결과가 아니다 | [3] 공식 1차 |
| 4 | 인간 영상의 가장 큰 병목은? | 행동 라벨이 없고 인간-로봇 형태가 달라 리타게팅·정렬이 필요하다. EgoScale도 소량 정렬 데이터(인간 약 50시간 + 로봇 약 4시간)를 쓰고, Skild 자신의 표도 도메인 격차가 가장 크다고 적는다 | [20][3] 논문 본문 + 공식 1차 |
| 5 | 시뮬레이션 데이터가 손 조작에도 충분한가? | 근거가 없다. Skild의 시뮬 성과 사례는 보행·축구 자기 대전이고, 접촉 많은 손 조작에 시뮬이 기여한 수치는 공개되지 않았다. 학습 데이터 구성도 비공개 | [5][6][2] 공식 1차 + 보도·2차, `확인필요` |
| 6 | Physical RSI는 실제로 작동하나? | 개념 서술이고 정량 결과가 없다. 같은 방향을 PI도 Recap으로 논문 수준에서 수치(처리량 2배 이상, 실패율 약 절반, 자체 평가)와 함께 보였다. 수렴 방향이나 Skild 쪽은 입증이 없다 | [4][13][14] 공식 1차 + 논문 본문 |
| 7 | OEM 탑재가 데이터 우위를 주나? | 가설이다. 탑재는 "목표" 문구이고 현 단계는 직접 미세조정이다. 환류 계약·수집 인프라·고객 데이터 권한이 공개되지 않았다 | [2][9] 공식 1차 + 보도·2차, 추론 |
| 8 | omni-bodied가 데이터 효율을 높이나? | 방향은 타사 논문이 지지하나 조건부다. π0.5는 타 로봇 데이터를 빼면 성능이 떨어졌고, OXE는 데이터가 적은 구현체와 큰 모델에서 이득이 뚜렷했다. Skild 자체 어블레이션은 확인 못함 | [12][19] 논문 본문 |
| 9 | PI의 파트너 데이터 전략 리스크는? | 하드웨어·현장은 파트너 소유이고 데이터 소유·사전학습 사용 조건이 공개되지 않았다. 또 파트너 데이터를 넣을 때 도메인별 특화가 필요한 이질성이 있을 수 있다(추론). Weave의 42%·50%는 조건이 다른 두 수치다 | [16][17] 보도·2차 |
| 10 | RLWRLD는 어느 쪽에 가깝고 약점은? | 에고센트릭(Skild식 확장성)과 텔레오퍼레이션(PI식)을 혼합하고 고객 현장을 데이터원으로 둔다. 약점은 사전학습이 공개 데이터셋 기반이고 현장 데이터의 성능 기여 수치가 없다는 점, 자금 규모 격차다 | [22][23] 보도·2차 + 기존 조사 |

보조 질문(조건 확인용): "텔레오퍼레이션 비용은?" → 금액은 소스에 없고 Skild는 380 시연=50~100시간[3], PI는 작업별 5~100시간 이상[11]이라는 시간 단위만 있다. 금액 환산은 `추정`이며 쓰지 않는다.

### 8. 확인하지 못한 것과 피딩 요청 목록

| 항목 | 상태 | 필요한 자료 |
|------|------|-------------|
| Skild 사전학습 풀의 출처별 비율·시간 | 미공개 | Skild 기술 보고서·논문, 후속 블로그 |
| Skild의 인간 영상 행동 추출 방법(라벨링, 리타게팅) | 1차 글에서 미확인 | Skild 논문(Affordances from Human Videos 계열 이후 연구) 또는 후속 블로그 |
| omni-bodied 효과의 정량 어블레이션 | 미확인 | 위와 같음 |
| Foxconn 셀·住友電装 프로젝트의 학습 데이터 구성, 손 하드웨어 | 미공개 | 영상·구상도·유료 기사 |
| Skild 환류 데이터의 양·고객 데이터 사용 권한("where permitted"의 뜻) | 미공개 | 계약 조건, 개인정보·데이터 정책 문서 |
| OEM(ABB·UR) 설치 로봇의 데이터 수집 구조 | 미공개 | OEM·Skild 공동 발표의 상세 문서 |
| PI π0.7·π0.6의 학습 데이터 구성 | 1차 미확보 | pi.website 블로그·기술 보고서(과거 접속 제한 429 사례 있음, 이번 π*0.6 블로그는 열림) |
| PI 파트너 데이터 사전학습 프로그램과 API의 데이터 권리 | 기사 수준(검색 요약에 "Partner Data Pre-Training Program" 언급, 1차 미열람) | PI 파트너·API 페이지 원문, 이용약관 |
| NVIDIA 고객 사례 문서의 게시일, Skild 사전학습 풀 규모 | 날짜 없음 | 페이지 메타데이터 |
| EgoScale의 +54%가 상대 향상인지 %p인지 | 본문 표 미확인 | 논문 표(과제별 절대값) |
| π*0.6 상자 조립 "600"의 성격(시연 대 자율 시도) | 본문과 부록 불일치 | 저자 정오표 또는 PDF 원본 확인 |
| Contrary Research(2024-11)의 "경쟁 모델 대비 1K배 데이터" 서술 | 2차, 근거 불명, 이 문서에서 인용하지 않음 | Skild 원 주장 출처 |
| 유료·접근 불가 | 이번 조사에서 유료 자료는 열지 않음 | 업계 애널리스트 리포트(Skild·PI 데이터 전략), 투자 설명 자료 |

## RX 관점 시사점
- 고객 제안: 데이터 철학을 설명할 때 "A사는 시뮬, B사는 실로봇"이 아니라 **출처 믹스, 품질 관리, 배치 후 환류, 데이터 권리**의 4개 항목으로 묻는 틀이 방어된다. 고객 현장 데이터는 환류 경로이고 이를 모델 개선에 쓸 권한(소유·재사용 범위)이 계약 쟁점이다. Skild와 PI 모두 공개 소스에서 이 조건이 확인되지 않으므로 고객 PoC 계약에서 먼저 정할 항목이다.
- 비교표를 쓸 때는 각 수치에 "자체 평가 / 평가 조건 / 시점"을 붙인다. 특히 66% 대 9%(내부 벤치마크, 개입 포함), 처리량 2배(오프라인 RL+SFT 대비)는 서로 비교하지 않는다.
- 병목 질문 목록(고객·파트너와의 대화에서 확인할 것): 현장 시연 1건당 수집 시간, 교정 개입 비율, 리셋·라벨 인력, 환류 데이터의 소유 구조, 시뮬 도입 시 접촉 모델 검증 방법.
- 팀 내부: 기존 팀 문서(research/skild-pi-deep-dive.md)는 "Skild: 인터넷 인간 영상 + 시뮬레이션, 데이터가 꼭 실로봇에서 나올 필요는 없다"로 요약했는데, 1차 소스에서 Skild가 텔레오퍼레이션·UMI·장갑도 병행함을 확인했으므로 "비로봇 중심 선언 + 실로봇 병행"으로 정확히 쓴다.

## 출처
1. [Building the general-purpose robotic brain](https://www.skild.ai/blogs/building-the-general-purpose-robotic-brain) - Skild AI, 2025-07-29, 공식 1차, (en) (reference/competitors--skild-general-purpose-brain.md)
2. [The Reindustrial Revolution: Partnering with ABB Robotics, Universal Robots, and NVIDIA](https://www.skild.ai/blogs/reindustrial-revolution) - Skild AI, 2026-03-19, 공식 1차, (en) (reference/competitors--skild-abb-ur-foxconn.md)
3. [Introducing S1: In-Context Learning for Robotics](https://www.skild.ai/blogs/s1) - Skild AI, 2026-08-18, 공식 1차, (en) (reference/competitors--skild-s1-blog.md)
4. [The Hidden Pillar of Robotics](https://www.skild.ai/blogs/skild-crosses-100m-arr) - Skild AI, 2026-09-10, 공식 1차, (en) (reference/competitors--skild-hidden-pillar.md)
5. [Physical Self-Play](https://www.skild.ai/blogs/physical-self-play) - Skild AI, 날짜 미표기(2026-09경 `추정`), 공식 1차, (en) (reference/competitors--skild-physical-self-play.md)
6. [Skild AI Builds Omni-Bodied Robot Brain With NVIDIA](https://www.nvidia.com/en-eu/case-studies/skild-ai/) - NVIDIA 고객 사례, 날짜 미확인, 공급사 문서, (en) (reference/competitors--skild-nvidia-case-study.md)
7. [Skild AI Taps NVIDIA Physical AI to Teach Robots New Tasks From a Single Video](https://blogs.nvidia.com/blog/skild-ai-s1-physical-ai/) - NVIDIA Blog, 2026, 협력사 게시, (en) (reference/competitors--skild-s1-nvidia.md)
8. [住友電装と米国 Skild AI、ワイヤーハーネス製造向けフィジカル AI ロボットの共同開発を開始](https://www.sws.co.jp/sws-news/docs/b19d54d9f74ad881f5f8aad4606784b9359d8ff2.pdf) - 住友電装, 2026-09-17, 1차, (ja) (reference/case--sws-skild-joint-dev-release.md)
9. [フィジカルAI導入「整ってから」だと遅い Skild AI共同創業者インタビュー後編](https://techblitz.com/startup-interview/skild-ai2/) - TECHBLITZ, 2026-08-27, 인터뷰 기사, (ja) (reference/competitors--skild-techblitz-interview2.md)
10. [Skild AI Crosses $100M ARR in 10 Months](https://www.humanoidsdaily.com/news/skild-ai-crosses-100m-arr-in-10-months-mounting-an-enterprise-assault-on-robotics-demo-culture) - Humanoids Daily, 2026-09, 기사, (en) (reference/competitors--skild-arr-humanoidsdaily.md) (본문에서는 Physical RSI 도해 확인용으로만 사용, 인용 수치 없음)
11. [π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164) - Physical Intelligence, arXiv 2024-10-31(2026-01 개정), 논문, (en) (reference/papers--pi0.md; raw: reference/raw/papers--pi0.txt)
12. [π0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054) - Physical Intelligence, arXiv 2025-04-22, 논문, (en) (reference/papers--pi05.md; raw: reference/raw/papers--pi05.txt)
13. [π*0.6: a VLA That Learns From Experience](https://arxiv.org/abs/2511.14759) - Physical Intelligence, arXiv 2025-11-18, 논문, (en) (reference/papers--pistar06-recap.md; raw: reference/raw/papers--pistar06-recap.txt)
14. [π*0.6: a VLA that Learns from Experience (PI 블로그)](https://www.pi.website/blog/pistar06) - Physical Intelligence, 2025-11-17, 공식 1차, (en) (reference/competitors--pi-pistar06-blog.md)
15. [Emergence of Human to Robot Transfer in Vision-Language-Action Models](https://arxiv.org/abs/2512.22414) - Physical Intelligence·Georgia Tech, arXiv 2025-12-27, 논문, (en) (reference/papers--pi-human-to-robot.md; raw: reference/raw/papers--pi-human-to-robot.txt)
16. [The API-fication of Robotics: PI Unveils Real-World Performance Data with Weave and Ultra](https://www.humanoidsdaily.com/news/the-api-fication-of-robotics-physical-intelligence-unveils-real-world-performance-data-with-weave-and-ultra) - Humanoids Daily, 2026-02(PI 업데이트 2026-02-24), 기사, (en) (reference/competitors--pi-weave-ultra-humanoidsdaily.md)
17. [Physical Intelligence Opens API Beta for Robot Model Training and Inference](https://www.humanoidsdaily.com/news/physical-intelligence-api-beta-robot-training-inference) - Humanoids Daily, 2026-10, 기사, (en) (reference/competitors--pi-api-beta-humanoidsdaily.md)
18. [Physical Intelligence, a hot robotics startup, says its new robot brain can figure out tasks it was never taught (π0.7)](https://techcrunch.com/2026/04/16/physical-intelligence-a-hot-robotics-startup-says-its-new-robot-brain-can-figure-out-tasks-it-was-never-taught/) - TechCrunch, 2026-04-16, 기사, (en) (reference/competitors--pi-pi07-techcrunch.md)
19. [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864) - Open X-Embodiment Collaboration, arXiv 2023-10-13, 논문, (en) (reference/papers--open-x-embodiment.md; raw: reference/raw/papers--open-x-embodiment.txt)
20. [EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data](https://arxiv.org/abs/2602.16710) - arXiv 2026-02-18, 논문, (en) (reference/papers--egoscale.md; raw: reference/raw/papers--egoscale.txt)
21. [NVIDIA Isaac GR00T N1.7](https://huggingface.co/blog/nvidia/gr00t-n1-7) - NVIDIA(Hugging Face), 2026-04-17, 공식 1차(공급사, 평가 조건 미확인), (en) (reference/competitors--nvidia-groot-n17.md)
22. RLDX-1 기술 보고서·블로그 정리 (research/rldx1-tech.md, reference/papers--rldx1-tech-report.md), 2026-05 공개, 논문·회사 서술, (en/ko)
23. research/company.md (RLWRLD 회사 조사, 투자·고객·데이터 확보 방식)
24. research/skild-pi-deep-dive.md (기존 팀 문서, 2026-10-09 정정판)
