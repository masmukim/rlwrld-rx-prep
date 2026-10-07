# 선도기업 PoC에서 배포까지의 프로세스와 RLWRLD PoC 설계 체크리스트
조사일: 2026-10-07

## 핵심 요약
- **공개된 단계 구분은 회사마다 다르지만, "좁은 작업 1개 → 고객 현장 상시 가동 → 확산 약정" 순서는 같다.** 기간이 확인되는 사례는 Figure(가동 후 6개월에 공장 시험, 10개월에 본 라인 투입), Agility(2023년 말 PoC → 2024-06 다년 RaaS 계약), Telexistence(2021-11 점포 1곳 → 2022-08 300점 도입 발표), CJ대한통운(2025-09 군포 실증 → 2026-09 용인 2대 투입)이다. 확산(수십~수천 대)은 계획만 있고 실적이 아닌 곳이 대부분이다 [1][3][10][11][21][22].
- **KPI 목표는 Figure만 숫자로 공개했고(사이클 84초, 정확도 99% 초과, 개입 0회), 그것도 원문에는 "요구·목표"로만 적혀 있어 달성값은 확인되지 않는다.** 나머지는 자동 성공률(Telexistence 98% 이상, 기사), 개입 감소율(PI-Weave 50%, 기사), ROI 프레임(Agility "시급 30달러 대비 2년 미만")에 그친다. 계약·가격은 대부분 비공개이며, 공개된 것은 구조(RaaS, 지분 투자 병행, 서비스 운영, OEM 탑재)와 일부 임계 가격(Mercedes "두 자릿수 천 달러", 교촌 조리 로봇 2,000만 원, 설치 포함 4,000만 원)뿐이다 [1][5][6][12][24][27].
- **확산이 멈추거나 느려진 사례는 기술 외 요인이 겹친다.** Walmart는 Bossa Nova를 5년 실험 뒤 종료했고(사람+소프트웨어 대안), 교촌은 2023년 1,300여 점 청사진 대비 2026-07 25개 점·33대(테스트 단계), 현대차 노조는 "노사합의 없이 1대도 안 된다"고 밝혔다. 이를 바탕으로 RLWRLD PoC 설계 체크리스트 14개 항목을 8절에 정리했다(사례 근거 항목과 본 문서의 제안 항목을 구분) [9][19][24][25].

## 1. 범위와 읽는 법
- 대상: `research/rx-cases.md`의 9개사(Figure, Agility, Apptronik, Boston Dynamics, Dexterity, Telexistence, Physical Intelligence, Skild AI, Sanctuary AI) + 일본 보강(Mujin, Telexistence-일본 편의점 3사) + 한국 보강(CJ대한통운, 교촌, 현대차, 롯데글로벌로지스·한진).
- 이미 조사한 PI·Skild는 `research/skild-pi-deep-dive.md`를 근거로 두고 이번에 새로 확인한 부분만 더했다 [27].
- 표기: **원문 확인**(1차 또는 기사 원문을 읽음), **기사**(2차), **검색 요약**(원문 미열람, 본문에는 `확인필요`와 함께만 사용). "본 문서의 해석"은 소스에 없는 분석이다.
- 공개 정보만 사용했다. 회사 발표 수치는 대부분 자체 주장이며 독립 검증이 없다.

## 2. 9개사와 Mujin의 PoC→배포 단계

| 회사 | 공개된 단계(순서대로) | 기간·시점 | KPI·성공 기준(공개된 것) | 계약·가격(공개된 것) | 근거 수준 |
|------|----------------------|-----------|--------------------------|----------------------|-----------|
| **Figure** (BMW) | ① 로봇 가동 준비 → 공장 인도·시험 ② 가동 라인 본 배치(근무일 매일) ③ 11개월 운영 후 F.02 퇴역, F.03로 이관 | 가동 후 6개월 내 시험 시작, 10개월 내 본 라인 투입, 총 11개월 [1] | 첫 작업: 판금 적재. KPI 3개: 사이클 84초(적재 37초), 교대당 정확도 99% 초과, 교대당 개입 0회. 공차 5 mm를 2초 안에. **모두 요구·목표로만 표기, 달성값은 없음** [1] | 비공개 | 회사 원문 [1] |
| **Agility** (GXO) | ① PoC 파일럿(Spanx 시설) ② 다년 RaaS 계약 ③ 운영 누적, 추가 용도 탐색 | PoC 2023년 말 → 계약 2024-06-27 → 100,000 토트 2025-11 [3][4] | 공개 KPI 없음. 마일스톤은 토트 수. CEO가 "사람 완전 부담 시급 30달러 대비 2년 미만 ROI"를 목표라 설명 [5] | **RaaS(다년)** + 클라우드 Arc. 요금 비공개 [3] | 회사 원문 [3], 기사 [4][5] |
| **Apptronik** (Mercedes) | ① 지분 투자 + 시험(Marienfelde, Kecskemet) ② 텔레오퍼레이션으로 작업 학습 → 자율화 목표 | 2025-03 시점 시험 중 [6] | 공개 KPI 없음. Mercedes 생산 총괄: 비용이 "두 자릿수 천 달러"가 되면 흥미로워짐 [6] | Mercedes가 "low double-digit million-euro" 투자. 로봇 가격 비공개 [6] | 기사(Reuters) [6] |
| **Boston Dynamics** (Hyundai) | ① 시간 제한 소규모 시험(엔지니어 상주) ② 상설 훈련센터 RMAC(공장 안, 첫 단계 가동) ③ HMGMA 부품 시퀀싱 ④ 조립 | 시퀀싱 2028, 조립 2030, RMAC 약 10배 확장 건물 이듬해 [7][8] | 공개 KPI 없음. RMAC 목표: "허용 가능한 신뢰성"에 필요한 현장·외부·시뮬레이션 데이터 배합을 찾는 것 [8] | 그룹 내부 고객. 현대·기아 공장 25,000대 계획(계획) [8] | 회사 원문 [7], 기사 [8] |
| **Dexterity** (FedEx) | ① 2023 트레일러 로더 공개 ② 2026 Investor Day 시연 ③ 여러 허브로 확산 의향 | 약 3년 [2] | 공개 KPI·수치 없음 | 비공개 | 회사 원문 [2] |
| **Telexistence** (FamilyMart 등) | ① FamilyMart의 정부 TF 참여(2019-11) ② 점포 1곳 도입(2021-11) ③ 300점 순차 도입 발표(2022-08) ④ 하드웨어 교체(TX GHOST), PI와 오류 복구 학습 루프(2025-06) ⑤ 7-Eleven 파일럿, 휴머노이드 2029 목표 | 1곳 → 300점 발표까지 9개월(계산), 7-Eleven 휴머노이드는 2025 → 2029 계획 [10][11][13][14] | 자동 보충 성공 98% 이상(NVIDIA 블로그, 조건 미공개). 실패 시 원격 조작으로 복구해 진열이 "100% 성립"하도록 설계 [10][12] | 로봇 판매가 아닌 **서비스 운영**. 요금 비공개 [15] | 회사·고객 원문 [10][11][13][14], 기사 [12] |
| **Physical Intelligence** | ① 파트너 하드웨어에서 모델 구동 ② 파트너 운영 데이터를 사전학습에 반영 ③ 개선 모델을 파트너에 되돌림 | 2026-02 공개 [27] | Weave: 세탁물 1회분당 원격 조작자 개입 50% 감소, 집기 실패 42% 감소(Weave 데이터를 사전학습에 포함했을 때) [27] | 하드웨어·현장은 파트너 소유. 가격·계약 비공개 [27] | 기사 [27] (Ultra "96.4%"는 원문 미확인으로 이미 `확인필요`) |
| **Skild AI** | ① 고객·OEM에 배포 ② 예외 데이터 수집 ③ 특화 학습을 기본 모델로 증류 | 첫 상업 배포 후 10개월에 ARR 1억 달러, 유료 고객 60곳 이상(회사 주장) [27] | 사이클 타임을 핵심 지표로 강조("정확도 99.9%라도 10배 느리면 배포 불가"). G10: 시간당 50라인 → 130~140라인(고객 발언, 기사) [27] | ABB, UR, MiR 제품군에 탑재(OEM) + 직접 배포. 가격 비공개 [27] | 기사 [27] |
| **Sanctuary AI** (Magna) | ① 투자자 = 제조 파트너 = 고객의 3중 관계 ② Phoenix 생산분을 Magna 시설에 배치해 학습 데이터 수집 | 2024-04 발표, "올해 만드는 시스템은 데이터 수집에 소비된다" [18] | 공개 KPI 없음. 목적을 생산이 아니라 데이터 수집으로 명시 [18] | 지분 + 위탁 생산 + 고객. 금액 비공개 [18] | 기사 [18] |
| **Mujin** (일본) | ① 컨설팅(현황 파악, 전체 구상, 요건 정의) ② MujinOS로 통합 시스템 구축(SI 파트너 경유 확대) ③ 제품 주도형으로 이행 | 시리즈 D 2025-12. 기간·ROI는 "현장별로 제안 시 안내"만 공개 [16][17] | 공개 KPI 없음 | 로봇 솔루션형 인티그레이션 → 제품 주도형 이행 중. 하드웨어 비종속 [16][17] | 기사 [16][17] |

해석(본 문서): 9개사 중 단계별 **기간과 정량 KPI가 모두 공개된 곳은 없다.** Figure가 가장 가깝지만 달성값이 빠져 있다. 따라서 공개 사례만으로 "업계 표준 PoC 기간"을 정할 수 없고, 아래 사례별 기간은 참고 범위로만 쓴다.

## 3. 단계 모델과 사례 매핑 (본 문서의 해석)

| 게이트 | 목적 | 공개 사례의 대응 | 기간 참고(계산) |
|--------|------|------------------|-----------------|
| **G0 진단·기준선** | 현재 작업 시간, 인원, 오류를 측정하고 대안과 비교 | Telexistence가 로봇과 함께 점원 위치 태그로 작업 시간을 시간대별로 측정하는 TX Work Analytics 도입 [11]. Mujin의 컨설팅 선행 [17]. RLWRLD RX(Landscaping → Deep Dive → Master Planning) [26] | 소스에 기간 없음. RLWRLD도 RX 기간·비용 비공개 |
| **G1 제한 환경 PoC** | 하나의 작업이 되는지 검증, 되는 것과 안 되는 것을 문서화 | Agility 2023 말 PoC [3]. 점포 1곳(Telexistence 2021-11) [10]. Hyundai의 time-boxed 시험 [8]. RLWRLD 랩 PoC(KDDI 진열 3개월) [26] | 3개월(RLWRLD, 사례 1건) |
| **G2 현장 상시 가동** | 실제 교대에서 매일 돌며 신뢰성과 개입을 측정 | Figure 본 라인(시험 시작 후 4개월 안에 본 라인, 10-6 계산) [1]. Agility RaaS(GXO) [3]. CJ 용인 2대 [22] | Figure 시험~본 라인 약 4개월, CJ 군포 실증 → 용인 투입 약 12개월(2025-09 중순 → 2026-09-03, 계산) |
| **G3 확산 약정·수량** | 다수 사이트·대수로 확장 | Hyundai 25,000대(계획), FedEx "여러 허브 확산 의향", 교촌 1,300여 점(청사진), Telexistence 300점 발표 [2][8][11][24] | 3년 안팎(Dexterity 2023 → 2026, Telexistence 7-Eleven 2025 → 2029 계획) |

- **계획 대비 실적 격차(계산·비교):** CJ대한통운은 2025-09 시점에 "연말까지 실증 완료, 2026년부터 주요 센터 순차 적용"을 계획했으나 실제 첫 현장 투입은 2026-09, 2대였다 [21][22]. 교촌은 2023년 1,300여 점 단계 도입 청사진을 밝혔고 2026-07에 25개 점·33대로 "아직 테스트 기간"이라고 말했다 [24][25]. 확산 계획 수치는 실적과 구분해서 읽어야 한다.
- **하드웨어는 PoC에서 확산까지 바뀐다:** Telexistence는 점포 1곳 도입 때 TX SCARA(2021)였고 2025년에는 TX GHOST가 서비스를 운영한다 [10][15]. Figure는 11개월 운영 뒤 F.02를 퇴역시키고 F.03로 넘어갔으며 전완이 최다 고장 부위였다 [1]. 지능 계층 회사(RLWRLD)는 하드웨어 교체에도 모델이 이어지는 구조를 PoC 설계에 넣어야 한다(해석).

## 4. KPI·성공 기준의 유형

| 유형 | 공개 사례 | 한계 | RLWRLD PoC에서의 쓰임(제안) |
|------|-----------|------|-----------------------------|
| 속도(사이클 타임) | Figure 84초/적재 37초 [1]. Skild "10배 느리면 배포 불가" [27]. G10 시간당 라인 수 [27] | Figure는 달성값 없음 | 속도비(로봇 대 숙련자)를 1순위로 둠 (B2 결론과 일치) |
| 품질(성공률) | Figure 교대당 99% 초과 목표 [1]. Telexistence 98% 이상 [12] | 시행 수·객체 다양성 미공개 | 시행 횟수와 객체 변동 조건을 KPI 정의에 포함 |
| 자율성(개입) | Figure 교대당 0회 목표 [1]. PI-Weave 개입 50% 감소 [27]. Telexistence 원격 복구 [10][12] | 개입의 정의가 회사마다 다름 | "자율 성공"과 "원격·인간 개입 후 성공"을 분리 집계 |
| 신뢰성·가동 | Figure 1,250시간 이상, 전완 고장 [1]. Jabil "80%는 쉽고 99.9%는 어렵다, 새벽 2시 고장" [20]. Agility 배터리 8시간, 2:1 [5] | 가동률 수치 없음 | 연속 가동 시간, 복구 시간, 교체 부품을 KPI에 포함 |
| 경제성 | Agility "시급 30달러 대비 2년 미만" [5]. Mercedes "두 자릿수 천 달러" [6]. 교촌 로봇 2,000만 원, 설치 포함 4,000만 원, 가맹점 창업비 평균 1억 원 [24] | 모두 목표 또는 업계 발언 | 대안(인력, 기존 자동화, 소프트웨어) 대비 비용을 PoC 입력값으로 확정 |
| 안전·수용성 | Agility는 사람 근처 작업 안 함, 기능 안전 경로 설명 [5]. 현대차 노조 반대 [9]. Jabil: 노조, 안전 문화, 여론 [20] | 정량 기준 없음 | 안전 범위와 노사 협의를 PoC 사전 조건으로 |

RLWRLD 공개 정보에서 KPI는 "성공 기준을 공동 정의"라고만 적혀 있고 수치가 없다 [26].

## 5. 계약·가격 구조

| 구조 | 사례 | 공개된 조건 | 비고 |
|------|------|-------------|------|
| RaaS(구독) | Agility-GXO 다년 [3] | 요금 비공개. 일부 2차 자료가 월 8,500달러 + 설치비 약 25,000달러를 주장하나 원문 미확인이라 사용하지 않음 | 로봇 대수당 ROI는 충전 비율(2:1)에 좌우 [5] |
| 서비스 운영형 | Telexistence 음료 진열 서비스 [15] | 요금 비공개 | 원격 오퍼레이터 인력이 서비스 원가에 포함(해석) |
| 지분 투자 + 시험 | Mercedes → Apptronik [6], Magna → Sanctuary [18] | Mercedes low double-digit 백만 유로 [6] | 고객이 투자자인 구조 |
| 그룹 내부 | Hyundai → Boston Dynamics [8] | 2026년 생산분 전량 Hyundai(검색 요약) | 외부 고객 확산과 별개 |
| OEM 탑재·라이선스 | Skild-ABB/UR [27], Mujin의 SI 네트워크 [17] | 가격 비공개 | 유통 채널이 확산 속도를 좌우 |
| 모델 API·데이터 공유 | PI-Weave/Ultra/Telexistence [13][27] | 파트너 데이터를 사전학습에 반영 | 데이터 권리는 PoC 계약에서 정할 항목 |
| 제품 판매 | 교촌 조리 로봇 [24], Weave 7,999달러 고정형(기사) [27] | 2,000만 원, 설치 포함 4,000만 원 | 소규모 사업자 투자 부담이 확산 제약 |
| 공동 모델 파트너십 | RLWRLD [26] | "용역 계약이 아니다", 고객 운영 데이터로 만든 모델을 상업 제품으로 확장 | 가격·지분 구조 비공개 |

해석(본 문서): 공개 소스에서 **PoC 단계의 대가(무상, 유상, 공동 부담)를 밝힌 사례는 확인하지 못했다.** RLWRLD가 PoC 대가와 후속 계약 옵션을 어떻게 제시하는지는 소스로 확정할 수 없다.

## 6. 실패·중단·지연 사례

| 사례 | 내용 | 원인(소스에 있는 것) | 근거 |
|------|------|----------------------|------|
| **Walmart - Bossa Nova** (재고 스캔, 조작 로봇은 아님) | 5년 실험을 종료. 같은 해 초 1,000점 확대를 발표했었음 | Walmart는 사람이 재고 확인을 로봇만큼 잘할 수 있다고 설명. 온라인 주문 인력이 늘어난 영향. 검색 요약: 약 500점 배치, Bossa Nova 약 50% 감원, 소비자 인식 우려 | 기사 [19] + 검색 요약 |
| **CJ대한통운 - 레인보우로보티즈** | 이전 협업 종료, 로보티즈로 전환 | 사유 미공개 | 기사 [21] |
| **교촌 조리 로봇** | 1,300여 점 청사진 대비 25개 점·33대, 테스트 단계 | 회사: 가맹점 변수 통제를 위해 확대보다 품질 향상에 집중. 업계: 투자 부담(설치 포함 4,000만 원). BBQ는 재현 한계로 회의적 | 기사 [24][25] |
| **현대차 Atlas** | 노조 "노사합의 없이 1대도 안 된다" 성명(2026-01) | 고용 충격과 해외 물량 이관 우려. 이후 협의 결과 미확인 | 기사 [9] |
| **Sanctuary** | Magna 배치는 데이터 수집 목적. 2024-11 CEO 퇴임과 감원(검색 요약, "30명 이상") | 소스에 인과 설명 없음 | 기사 [18] + 검색 요약 |
| **Figure** | 전 안전 엔지니어가 부당 해고 소송(2025-11), 로봇 충격력과 안전 로드맵 축소를 주장. 회사는 성과 부진 때문이라며 부인 | 주장 단계. 원문(법원 서류, 기사) 미열람 | 검색 요약 `확인필요` |
| **K-Scale Labs** | 2025-11 청산 보도 | 후속 투자 실패. 고객 파일럿과 무관한 공급사 존속 사례 | 검색 요약 `확인필요` |

**공통 패턴(본 문서의 해석, 소스 [19][20][24][25][9] 종합):** ① 사람·소프트웨어 같은 값싼 대안과의 비교에서 밀림 ② 파일럿 규모에서 확산 규모로 갈 때 신뢰성(99.9%)과 유지보수 요구가 커짐 ③ 구매자(점주, 노조, 소비자)의 수용성 ④ 확산 계획은 발표하지만 실제 조건(변수 통제, 피드백 검증)이 충족될 때까지 지연. PoC 설계는 이 4가지를 사전에 시험해야 한다. 별개 근거로 검색 요약에 "PoC 33건 중 4건만 생산 단계(IDC)"라는 AI 프로젝트 통계가 있으나 로봇 PoC 통계가 아니라서 본문 결론에는 쓰지 않았다.

## 7. 일본·한국 사례 보강

### 7.1 일본
| 항목 | 내용 | 근거 |
|------|------|------|
| Telexistence 단계 | 정부 TF → 1점포 → 300점 발표 → TX GHOST 서비스 → PI와 오류 복구 모델 → 7-Eleven 휴머노이드(2029). 로봇 교체 속에서도 "원격 복구 + 데이터 수집" 구조가 유지됨 | [10][11][13][14][15] |
| 데이터 루프 | PI는 오류 복구 정책을 개발하고, TX는 로봇과 텔레오퍼레이션 데이터를 제공해 "데이터 주입 → 학습 → 재배포" 루프를 구성 | [13] |
| Mujin | 시리즈 D(2025-12) 첫 클로즈 364억 엔(증자 209억 + 부채 155억), 누적 596억 엔. 인티그레이터형에서 제품형으로 이행. 일본에는 자동화 컨설팅 전담팀. "현황 파악, 전체 구상, 요건 정의가 안 되면 자동화 프로젝트가 실패할 수 있다" | [16][17] |
| RLWRLD와의 경쟁·중복 | Lawson 진열 PoC(4월 현장 시찰, 8월 진열 PoC) [29]와 Telexistence 음료 보충(7-Eleven 파일럿)은 일본 편의점 현장에서 겹친다. Mujin은 팔레타이징·트럭 하차 등 물류 응용과 통합 제어 레이어가 중심이라(회사 설명), 손 조작 모델과 직접 경쟁하는지는 소스에 없음(해석) | [14][15][29] |

### 7.2 한국
| 사례 | 단계와 결과 | RLWRLD 관련 |
|------|-------------|-------------|
| **CJ대한통운** | 2025-09 로보티즈와 협약, 군포 FC 완충재 보충 실증 → 2026-09 용인 양지 올리브영 센터 포장 라인 2대 투입. 목표: 피킹·분류·검수·포장으로 확대 [21][22] | RFM 파트너로 RLWRLD 명시(에이딘로보틱스 핸드, 로보티즈 하드웨어). CFO는 "RFM 공동 고도화 + 물류센터 자율운영 전환" [22][23][30]. **RLWRLD-CJ 개별 PoC의 성과는 공개된 바 없음** |
| **교촌·bhc** | 교촌: 2021 뉴로메카 협약 → 2023 4개 매장 → 2026-07 25개 점·33대 테스트. bhc는 LG전자 튀봇 3개 점 시범(2023) [24][25] | 가맹점 구조에서 설치 포함 4,000만 원이 확산 제약 |
| **현대차·Boston Dynamics** | 노조 협의가 선행 조건으로 부상 [9] | 한국 대기업 제조 고객 제안의 사전 변수 |
| **롯데글로벌로지스·한진** | 롯데: 로브로스 이족보행 실증(국책 과제), 투입 논의 중. 한진: LA 센터에 Locus AMR 기반 피킹 [23] | 물류 분야는 AMR(검증된 자동화) → 휴머노이드(실증) 순으로 단계 구분 |

## 8. RLWRLD PoC 설계 체크리스트

각 항목의 "근거"는 위 사례이고, "제안"은 사례에서 도출한 본 문서의 의견이다. 수치형 통과 기준은 고객과 합의할 칸이며 이 문서에서 값을 정하지 않았다.

### A. 시작 전 (G0)
| # | 점검 항목 | 확인 질문 | 근거·제안 |
|---|-----------|-----------|-----------|
| 1 | 작업 선택 | 좁고 반복적이며 KPI를 숫자로 고정할 수 있는가? 다섯 손가락이 꼭 필요한 구간인가, 그리퍼 대조군으로 충분하지 않은가? | 근거: Figure 첫 작업은 pick-and-place [1], RLWRLD PoC는 "하나의 태스크" [26]. 제안: 손 필요성 대조군 포함 |
| 2 | 기준선 측정 | 현재 작업 시간, 인원, 오류율, 대안(사람, 기존 자동화, 소프트웨어)을 실측했는가? | 근거: TX Work Analytics [11], Mujin 컨설팅 [17], Bossa Nova 종료 [19]. |
| 3 | KPI 3~5개 사전 합의 | 사이클 타임(속도비), 성공률, 개입 횟수, 연속 가동, 복구 시간. 각 KPI에 목표값, 최소 통과값, 중단값을 적었는가? | 근거: Figure 3 KPI [1], Skild 사이클 타임 [27]. 제안: 3값 구조, 달성값도 반드시 공개·기록 (Figure는 달성값 누락) |
| 4 | 평가 조건 | 시행 횟수, 객체 종류, 변동(위치, 방향, 조명), 교대 시간, 평가자(고객 입회)를 정했는가? | 근거: RLWRLD PoC "실제 객체와 변동성" [26]. 제안: 조건 없는 성공률은 쓰지 않음 |

### B. 실행 (G1~G2)
| # | 점검 항목 | 확인 질문 | 근거·제안 |
|---|-----------|-----------|-----------|
| 5 | 장소와 이전 | 랩 PoC와 현장 상시 가동을 별도 게이트로 나눴는가? 현장 이전 시 재검증 항목은? | 근거: Hyundai time-boxed 시험 → 상설 RMAC [8], Figure 시험 → 본 라인 [1], RLWRLD 랩 PoC [26] |
| 6 | 개입 설계 | 인간 개입·원격 조작을 허용하는 범위와 KPI 집계 방식을 정했는가? | 근거: Telexistence 원격 복구 [10][12], PI-Weave 개입 감소 [27] |
| 7 | 하드웨어 책임 분담 | 손·로봇 파트너의 고장, 교체, 연속 가동 책임은 누구인가? 하드웨어가 바뀌어도 모델이 이어지는가? | 근거: Figure 전완 고장 [1], TX 하드웨어 교체 [10][15]. 제안: 연속 가동 시험과 교체 부품 목록 |
| 8 | 데이터 루프와 권리 | PoC에서 생기는 데이터의 소유, 학습 사용 범위, 재배포 계획은? | 근거: TX-PI 루프 [13], PI 파트너 데이터 사전학습 [27], RLWRLD 파트너십 외부 가치 [26]. 라이선스 쟁점(비상업 가중치)은 열린 질문 |
| 9 | 안전·노사·수용성 | 사람 근처 작업 여부, 안전 기준, 노조·작업자 설명은 사전에 했는가? | 근거: Agility [5], 현대차 노조 [9], Jabil [20] |

### C. 종료와 전환 (G2~G3)
| # | 점검 항목 | 확인 질문 | 근거·제안 |
|---|-----------|-----------|-----------|
| 10 | Readout | 되는 것과 안 되는 것, 실패 모드를 문서로 남겼는가? | 근거: RLWRLD PoC Readout [26] |
| 11 | Go / No-Go 사전 정의 | 통과 시 다음 단계(소수 대 현장 파일럿), 미통과 시 중단 또는 재설계 조건을 PoC 시작 전에 합의했는가? | 근거: 교촌·CJ 계획 대비 지연 [21][22][24][25]. 제안: 확산 수치를 PoC 계약에 쓰지 않고 단계별 게이트로 표현 |
| 12 | 경제성 | 대안 대비 비용 차이, 로봇 가격 임계, 투자 회수를 PoC 결과로 업데이트했는가? | 근거: Mercedes 가격 임계 [6], 교촌 설치 포함 4,000만 원 [24], Agility ROI 프레임 [5] |
| 13 | 후속 계약 옵션 | RaaS, 서비스, 공동 모델, OEM 탑재 중 어떤 구조를 제시하는가? | 근거: [3][15][17][26][27]. 제안: PoC 전에 후속 구조 후보를 고객에게 보여 줌 |
| 14 | 확산 이해관계자 | 투자자 겸 고객 여부, 구매 결정자(현장, 경영, 노조), 확산 시 운영 책임(원격 오퍼레이터, 유지보수)은? | 근거: Mercedes·Magna 투자 구조 [6][18], 롯데호텔·CJ·KDDI 투자자 = 고객 [30], Jabil [20] |

## RX 관점 시사점
- **고객 제안에서:** ① PoC 제안서 첫 장에 KPI 표(목표값, 통과값, 중단값, 평가 조건)와 중단 기준을 넣는다. 공개 사례에서 가장 부족한 부분이라 차별점이 된다. ② "확산 대수"를 약속하지 않고 G1 → G2 → G3 게이트로 표현한다(교촌, CJ 격차). ③ 후속 계약 옵션(RaaS, 서비스, 공동 모델)을 PoC 전에 제시한다. ④ 안전과 노사 협의를 사전 조건으로 둔다.
- **B4 연계:** K사 PoC의 KPI에 "교대당 개입 횟수, 자율 성공 대 개입 후 성공 분리, 연속 가동, 속도비"를 쓰고 달성값을 기록하는 표를 만든다. 랩 PoC → 현장 파일럿 2단계는 Hyundai·Figure의 구조와 일치한다.
- **면접에서:** "공개 사례는 계약·가격과 달성값을 거의 밝히지 않습니다. Figure조차 KPI는 공개했지만 달성값은 적지 않았습니다. 그래서 RLWRLD PoC는 시작 전에 통과·중단 기준을 합의하고, 결과를 달성값으로 남기는 설계가 필요하다고 봅니다."라고 말할 수 있다.

## 확인하지 못한 항목
- **정정:** `research/rx-cases.md` 2절 Figure 행의 "사이클 84초(적재 37초) 목표 달성, 정확도 99% 이상/교대"는 원문에서 **목표·요구 조건**으로만 확인된다. 달성값은 원문에 없다. `knowledge.md`의 "Figure-BMW 판금 적재: 84초, 99% 이상, 개입 0회"도 같은 방식으로 "목표"로 읽어야 한다. 또 같은 표의 "Agility 9개 시설 6.5만 시간"은 이번에 읽은 100,000 토트 기사 원문에서 확인되지 않았다.
- Agility RaaS 요금(월 8,500달러 등), Mercado Libre(2025-12)·Toyota(2026-02) 상업 계약: 검색 요약만 확인.
- Apptronik-Mercedes 상업 계약 체결 시점(2024-03 주장)과 Jabil·GXO 파일럿 세부: 원문 미열람.
- Figure 소송, Sanctuary 감원, K-Scale 청산, Walmart 500점·50% 감원: 검색 요약. 원문(techspot 403, axios 403 등) 미열람.
- Mujin 구현 기간(2달 미만), 협력사 사례(Kyowa Shiko 출하량 70% 증가, 2020년 블로그와 검색 요약), 오카야마 시험 센터, MujinOS 도입 2,000개사: 원문 미확인(monoist 문자 깨짐, 미열람).
- CJ-레인보우로보티즈 협업 종료 사유, CJ-RLWRLD 개별 PoC 결과, 현대차 노사 협의 이후 결과.
- Dexterity Hagerstown 확장(2026-07, rx-cases [13])과 PI 파트너 페이지 원문(429).
- RLWRLD RX와 PoC의 가격, 기간(KDDI 3개월 외), 성공 기준의 구체 수치.

## 출처
1. [F.02 Contributed to the Production of 30,000 Cars at BMW](https://www.figure.ai/news/production-at-bmw) - Figure AI, 2025-11-19, 1차, (en) (reference/case--poc-figure-bmw.md)
2. [FedEx Case Study](https://dexterity.ai/blog/case-studies/fedex) - Dexterity, 2026, 1차, (en) (reference/case--poc-dexterity-fedex.md)
3. [GXO Signs Industry-First Multi-Year Agreement with Agility Robotics](https://agilityrobotics.com/content/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics) - Agility Robotics, 2024-06-27, 1차, (en) (reference/case--poc-gxo-agility-release.md)
4. [Digit passes 100,000-tote milestone at GXO](https://roboticsandautomationnews.com/2025/11/24/agility-robotics-digit-humanoid-passes-100000-tote-milestone-in-live-gxo-implementation/96877/) - Robotics & Automation News, 2025-11-24, 기사, (en) (reference/case--poc-agility-100k-totes.md)
5. [Here's what it could cost to hire a Digit humanoid](https://www.therobotreport.com/heres-what-it-could-cost-to-hire-a-digit-humanoid/) - The Robot Report, 2024, 기사, (en) (reference/case--poc-robotreport-digit-cost.md)
6. [Mercedes-Benz takes stake in robotics maker Apptronik, tests robots in factories](https://www.aol.com/news/mercedes-benz-takes-stake-robotics-150148224.html) - Reuters(AOL), 2025-03-18, 기사, (en) (reference/case--poc-mercedes-apptronik-reuters.md)
7. [Hyundai Motor Group AI Robotics Strategy at CES 2026](https://www.hyundaimotorgroup.com/en/story/hyundai-motor-group-ai-robotics-ces-2026) - Hyundai Motor Group, 2026-01, 1차, (en) (reference/case--poc-hyundai-ces2026-atlas.md)
8. [Boston Dynamics opens Metaplant Application Center to train Atlas humanoids](https://www.therobotreport.com/boston-dynamics-opens-metaplant-application-center-train-atlas-humanoid-robots/) - The Robot Report, 2026-09, 기사, (en) (reference/case--poc-robotreport-rmac.md)
9. [현대차 노조, '아틀라스'와 사실상 전면전](https://www.heraldk.com/article/2026012123220409613) - 미주헤럴드경제, 2026-01-21, 기사, (ko) (reference/case--poc-heraldk-hyundai-union.md)
10. [Telexistence社新型ロボット『TX SCARA』をファミリーマート経済産業省店に導入](https://www.family.co.jp/company/news_releases/2021/20211102_01.html) - ファミリーマート, 2021-11-02, 1차, (ja) (reference/case--poc-familymart-telexistence-2021.md)
11. [飲料補充AIロボットを300店舗へ導入](https://www.family.co.jp/company/news_releases/2022/20220810_01.html) - ファミリーマート, 2022-08-10, 1차, (ja) (reference/case--poc-familymart-telexistence-2022.md)
12. [Restocking Robot Rolls Out to Hundreds of Japanese Convenience Stores](https://blogs.nvidia.com/blog/telexistence-convenience-store-robotics/) - NVIDIA Blog, 2022-08, 기사, (en) (reference/case--poc-nvidia-telexistence.md)
13. [Telexistence and Physical Intelligence Announce Partnership](https://tx-inc.com/en/blog/2025/06/25/12307/) - Telexistence, 2025-06-25, 1차, (en) (reference/case--poc-tx-pi-partnership.md)
14. [Seven-Eleven Japan and Telexistence Partner to Pioneer Humanoid Robots](https://tx-inc.com/?p=12542) - Telexistence, 2025-09-29, 1차, (en) (reference/case--poc-tx-seven-eleven.md)
15. [Telexistence Expands Beverage Shelf-Stocking Service with "TX Ghost" Robots](https://tx-inc.com/?p=12519) - Telexistence, 2025, 1차, (en) (reference/case--poc-tx-ghost-service.md)
16. [Mujin、シリーズD初回クローズで総額364億円を調達](https://thebridge.jp/2025/12/mujin-raises-36-4-billion-yen-series-d-first-close) - THE BRIDGE, 2025-12-03, 기사, (ja) (reference/case--poc-mujin-series-d-thebridge.md)
17. [Mujin raises $233M to advance industrial adoption of MujinOS](https://www.automatedwarehouseonline.com/mujinos-raises-233m-advance-industrial-adoption/) - Automated Warehouse, 2025-12, 기사, (en) (reference/case--poc-mujin-awo-233m.md)
18. [Sanctuary AI enters strategic relationship with Magna](https://www.therobotreport.com/sanctuary-ai-enters-strategic-relationship-with-magna-to-build-embodied-ai-robots/) - The Robot Report, 2024-04, 기사, (en) (reference/case--poc-sanctuary-magna.md)
19. [Walmart drops Bossa Nova inventory program](https://www.therobotreport.com/walmart-drops-bossa-nova-inventory-program-highlighting-retail-robotics-challenges/) - The Robot Report, 2020-11, 기사, (en) (reference/case--poc-robotreport-walmart-bossanova.md)
20. [The 2 a.m. problem: A Jabil executive on what really stalls robotics at scale](https://www.rdworldonline.com/the-2-a-m-problem-a-jabil-executive-on-what-really-stalls-robotics-at-scale/) - R&D World, 2026, 기사(인터뷰), (en) (reference/case--poc-rdworld-jabil-scale.md)
21. [CJ대한통운, 업계 최초 AI 휴머노이드 로봇 현장 실증…로보티즈와 MOU 체결](https://byline.network/2025/09/_25_2918287/) - 바이라인네트워크, 2025-09-25, 기사, (ko) (reference/case--poc-byline-cj-robotis.md)
22. ["로봇이 올리브영 상품 포장"...CJ대한통운, 휴머노이드 로봇 현장 투입](https://economist.co.kr/article/view/ecn202609030047) - 이코노미스트, 2026-09-03, 기사, (ko) (reference/case--poc-economist-cj-2026-09.md)
23. [휴머노이드 첫 일터는 물류센터…CJ·롯데·한진 '로봇 전쟁'](https://www.inews24.com/view/2002131) - 아이뉴스24, 2026(추정), 기사, (ko) (reference/case--poc-inews24-logistics-humanoid.md)
24. [치킨 업계에 부는 '로봇 열풍'…안성맞춤 vs 시기상조](https://v.daum.net/v/20231218144404874) - 다음 뉴스, 2023-12-18, 기사, (ko) (reference/case--poc-daum-kyochon-2023.md)
25. [교촌에프앤비, 25개 매장서 33대 협동 조리 로봇](https://biz.newdaily.co.kr/site/data/html/2026/07/15/2026071500262.html) - 뉴데일리경제, 2026-07, 기사, (ko) (reference/case--poc-newdaily-kyochon-2026.md)
26. RLWRLD Business 페이지(RX, PoC, 파트너십) - RLWRLD, 2026-10-07 열람, 1차, (ko) (reference/company--rlwrld-business-rx-poc-partnership.md)
27. research/skild-pi-deep-dive.md - Skild·PI 수치(Humanoids Daily 기사 원문: reference/raw/competitors--pi-weave-ultra-humanoidsdaily.txt, reference/raw/competitors--skild-arr-humanoidsdaily.txt), 2026-10-07
28. research/rx-cases.md - 9개사 기존 조사, 2026-10-07
29. [Impress AI Watch, KDDI·RLWRLD GENIAC 기사](reference/company--impress-kddi-geniac.md) - Impress, (ja) (reference/company--impress-kddi-geniac.md)
30. [Unicorn Factory 시드2 기사](reference/company--unicornfactory-seed2.md) - 유니콘팩토리, 2026-02, 기사, (ko) (reference/company--unicornfactory-seed2.md)
