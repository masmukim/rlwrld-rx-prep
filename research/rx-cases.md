# RX 방식과 해외 선도기업 도입 사례
조사일: 2026-10-07

## 핵심 요약
- **RLWRLD의 RX는 3단계 컨설팅형 진단이다.** Landscaping(작업·객체·환경 분석, 비용 기준선) → Deep Dive(타당성, 시스템 요건, 파일럿 태스크) → Master Planning(우선순위, 데이터 전략, ROI). 이후 **RLWRLD 랩에서 하는 PoC**(KDDI 편의점 진열 3개월)와 **다년 파트너십**으로 이어진다. 회사는 지능(모델)을 제공하고, 하드웨어·센서·인프라는 생태계 파트너가 맡는다 [1][2][3].
- **해외 사례는 두 갈래다.** 로봇까지 직접 만드는 풀스택(Figure, Agility, Apptronik, Boston Dynamics, Dexterity, Telexistence)과, 남의 로봇에 지능을 얹는 지능 계층(Physical Intelligence, Skild AI). RLWRLD는 후자에 속한다 [1][5][11].
- **공통 패턴:** 첫 작업은 좁고 KPI가 분명한 작업(BMW 판금 적재: 84초 사이클, 정확도 99% 이상, 개입 0회)으로 시작하고, 고객이 투자자를 겸하며(Mercedes-Apptronik, Hyundai-Boston Dynamics), 파일럿에서 확산까지 1~3년이 걸린다 [6][9][10][12].

## 1. RLWRLD의 RX, PoC, 파트너십 (회사 페이지 원문 기준)

| 단계 | 내용 | 산출물·조건 | 출처 |
|------|------|-------------|------|
| **RX** | "기술보다 운영을 먼저 이해한다." 사람의 일을 로봇이 학습할 단위로 분해 | ① RX Diagnosis & Baseline(작업 분석 + ROI용 비용·시간 기준선) ② Robot Application Roadmap(작업별 제안, 하드웨어 요건, 난이도, 비즈니스 임팩트 우선순위) ③ Mid-to-Long-Term Master Plan(데이터 수집 일정, PoC 일정, 연차별 ROI 시뮬레이션) | [1] |
| RX 진행 | 01 Landscaping → 02 Deep Dive → 03 Master Planning | "표준 진행 기준, 범위에 따라 변형 가능" | [1] |
| **PoC** | "데모가 아니다." 실제 객체와 변동성으로 하나의 태스크를 검증 | Scope & Setup(태스크 확정, 환경 재현, 성공 기준 공동 정의) → Execution → Readout(무엇이 되고 안 되는지 기술 문서). **RLWRLD 랩에서 진행.** 전면 도입 약속이나 장기 약정이 아님 | [2] |
| PoC 사례 | KDDI 편의점 진열(전면 정렬, 2단 구성) | **3개월.** "어려움은 집기 자체가 아니라 일관된 방향성" | [2] |
| **파트너십** | "용역 계약이 아니다." 다년간 고객 운영 데이터로 미세조정한 모델을 함께 만듦 | Capture Setup → Skill Extraction → Data Processing → Teleoperation → Fine-tuned Skill Model (RLWRLD Intelligence Layer 위) | [3] |
| 파트너십의 보상 | 내부 가치: 고객 작업 자동화 / **외부 가치: 고객 운영에서 만든 모델을 RLWRLD와 함께 상업 제품으로 확장** | 고객의 숙련이 제품이 되는 구조 | [3] |
| 생태계 | "RLWRLD는 지능을 제공한다." 로봇 하드웨어, 센서·인지, 인프라·통합 파트너와 현장 도입 | 대상 산업: 제조, 물류, 리테일, 호텔, 항공, 식품 | [4] |

## 2. 해외 선도기업 도입 사례

| 회사 (유형) | 고객 | 첫 작업 | 사업 구조 | 기간·확산 | 공개 결과 | 근거 수준 |
|-------------|------|---------|-----------|-----------|-----------|-----------|
| **Figure** (풀스택 휴머노이드) | BMW Spartanburg | 판금 적재: 랙에서 부품 3개를 집어 용접 지그에 올림 (전형적 pick-and-place) | 고객사 라인 직접 투입 | 로봇 가동 6개월 만에 공장 반입, 10개월 만에 본 라인 투입, 11개월 운영. 2026년 Figure 03 40대로 물류 시퀀싱 확장 | 사이클 84초(적재 37초) 목표 달성, 정확도 99% 이상/교대, 5 mm 공차를 2초 안에, 부품 9만 개, 1,250시간, X3 3만 대 생산 기여. **전완부가 최다 고장 부위** | 회사 발표 원문 [6], 확장은 기사 [7] |
| **Agility Robotics** (풀스택 휴머노이드) | GXO(Spanx 물류센터), 이후 Toyota, Mercado Libre, Schaeffler | AMR에서 토트를 내려 컨베이어에 올림 | **RaaS(월 사용료)** + 클라우드 플릿 관리(Arc). 2024-06 업계 첫 다년 RaaS 계약 | 2024 계약 → 2025-11 토트 10만 개 | 9개 시설 6.5만 시간(기사) | 기사 [8] |
| **Apptronik** (풀스택 휴머노이드) | Mercedes-Benz(베를린, 헝가리 케치케메트), Jabil, GXO | 조립 키트 배달, 부품 검사, 공정 간 이동 | 견적 기반 파일럿 계약. **Mercedes가 투자자.** Jabil은 고객이자 위탁 생산자 | 2025~2026 파일럿·평가, 2027 상업 규모 목표 | 정량 결과 미공개 | 기사 [9] |
| **Boston Dynamics** (풀스택, Hyundai 계열) | Hyundai 메타플랜트 (조지아) | 부품 물류 시퀀싱 → 2030년 부품 조립 | 그룹 내부 고객. **공장 옆 전용 훈련센터(RMAC) 2026-09 개소** | 2026년 물량 전량 약정, 향후 Hyundai·Kia 공장에 2.5만 대 계획 | 정량 결과 미공개 | 기사 [10] |
| **Dexterity** (풀스택, 양팔 Mech + Foresight 모델) | FedEx | 트레일러 적재(무작위 크기 상자) | 장기 협력 | 2023 시험 현장(Tracy) → 2026-07 Hagerstown 허브 확장, FedEx가 여러 허브로 확산 의향 | 정량 결과 미공개 | 회사 사례 [12], 기사 [13] |
| **Telexistence** (풀스택, 원격조종 + AI) | FamilyMart 300개 이상, Lawson | 음료 진열 보충 (매장 백룸) | 서비스형 운영, 실패 시 필리핀 원격 조작자 개입. **2025-06 Physical Intelligence와 음료 보충 자동화 파트너십** | 2022-08 도입 시작 → 300개 매장 | 자동 보충 성공 98% 이상(기사) | 기사 [14][15] |
| **Physical Intelligence** (지능 계층) | Weave Robotics(세탁물 개기), Ultra(전자상거래 포장), Telexistence | 고객 하드웨어 위에서 π 모델 구동 | **하드웨어와 현장은 파트너가 소유**, PI는 모델 제공 | 2026-02 배포 사례 공개 | Ultra: Ultra 데이터로 미세조정한 π0.6이 포장 처리량 증가 (한 교대 자율률 96.4%는 검색 요약에만 있고 원문 기사에서 미확인, 2026-10-07 정정). Weave: 개입 50% 감소 | 검색 요약 [5] (PI 원문 미열람, 429) |
| **Skild AI** (지능 계층, 다양한 로봇용 Skild Brain) | Foxconn(NVIDIA Blackwell 조립), ABB, Universal Robots, MiR 파트너 | 양팔 매니퓰레이터의 정밀 조립 | 하드웨어 제조사 파트너십으로 유통 | 상업 배포 10개월 만에 ARR 1억 달러, 유료 고객 60곳 이상(기사) | 정량 성능 미공개 | 기사 [11] |
| **Sanctuary AI** (풀스택, 21-DoF 손) | Magna (자동차 부품) | 미공개 | 전략 파트너십 | 2024 공장 투입 발표 | 대수·결과 미공개 | 기사 [16] |

## 3. 패턴과 RLWRLD에 주는 시사점

| 패턴 | 사례 | RLWRLD·K사 케이스 시사점 |
|------|------|--------------------------|
| **첫 작업은 좁고 단순하게** | Figure의 첫 작업은 손 조작이 아닌 판금 pick-and-place였다. KPI 3개(사이클, 정확도, 개입 횟수)를 숫자로 고정 | 고자유도 손이 꼭 필요한 작업만 고집하면 첫 성과가 늦어진다. K사 A트랙(프리블록)이 이 역할. **KPI에 "교대당 개입 횟수"와 "교대당 자율률"을 추가** |
| **지능 계층 vs 풀스택** | PI·Skild는 하드웨어 파트너에 기대고, Figure·Agility는 자체 로봇 | RLWRLD는 지능 계층. 강점은 하드웨어 선택 유연성, 약점은 **고장·내구성 책임이 파트너에 있어 현장 품질 통제가 어려움** (Figure는 BMW 고장 데이터로 다음 로봇을 설계) |
| **고객 = 투자자** | Mercedes→Apptronik, Hyundai→Boston Dynamics, KDDI·롯데·CJ→RLWRLD | 초기 고객은 "구매자"보다 "현장을 여는 전략 파트너". K사 같은 비투자 중견사는 다른 유인이 필요 |
| **사업 구조** | Agility는 RaaS 월 사용료, RLWRLD는 파트너십 + 모델 상품화 | K사에 셀 구매(3.96억 원, 회수 5.7년)를 파는 대신, **"K사 하네스 숙련을 모델로 만들어 다른 하네스 업체에 함께 판다"(RLWRLD 파트너십의 외부 가치)**가 중견사에 더 강한 제안일 수 있음 |
| **파일럿→확산 1~3년** | Figure 10개월, Dexterity 3년(2023→2026), Telexistence 2022→300개 매장 | 14주 PoC 뒤 바로 확산을 약속하지 말고, Master Plan에 연차별 단계를 둔다 (RLWRLD RX 산출물 ③과 일치) |
| **훈련은 고객 라인 밖에서** | Boston Dynamics RMAC(공장 옆 훈련센터), RLWRLD PoC는 자사 랩 | K사 PoC는 **RLWRLD 랩에 프리블록 작업대를 재현**하는 쪽이 RLWRLD 방식에 맞음. 현재 스토리라인은 K사 현장 PoC를 가정 |
| **같은 시장의 직접 경쟁** | Telexistence × Physical Intelligence 음료 보충 (일본 편의점) | RLWRLD의 KDDI·Lawson 진열 PoC와 시장이 겹친다. 일본 리테일에서는 PI 진영과 경쟁 |

## RX 관점 시사점
- **B4 스토리라인에 반영할 것:** ① PoC 장소를 "RLWRLD 랩에서 K사 작업대 재현"으로 수정 ② 산출물 이름을 RLWRLD RX 산출물(Diagnosis & Baseline, Application Roadmap, Master Plan)에 맞춤 ③ KPI에 교대당 개입 횟수·자율률 추가 ④ 도입 구조 장에 파트너십의 "모델 상품화" 옵션 추가
- **면접에서:** "RLWRLD는 PI·Skild와 같은 지능 계층 회사이고, 풀스택 기업과 달리 하드웨어 파트너 생태계와 고객 데이터가 경쟁력이라 RX가 그 입구"라고 정리할 수 있다. Figure-BMW 사례로 "첫 작업은 좁게, KPI는 숫자로"를 근거로 들 수 있다.

## 확인하지 못한 항목
- Physical Intelligence 파트너 페이지 원문 (429로 차단, 검색 요약만 사용)
- Agility 9개 시설·6.5만 시간, Skild ARR·고객 수, Telexistence 98%는 기사 수치(1차 미확인)
- Apptronik, Boston Dynamics, Dexterity, Sanctuary의 정량 결과
- RLWRLD RX의 기간과 비용 (페이지에 없음)

## 출처
1. [RX 로보틱스 인텔리전스](https://www.rlwrld.ai/ko/business/rx) - RLWRLD, 2026-10-07 열람, 1차, (ko) (raw: reference/raw/company--rlwrld-business-rx.txt)
2. [Validate in the Field (PoC)](https://www.rlwrld.ai/ko/business/poc) - RLWRLD, 2026-10-07 열람, 1차, (ko) (raw: reference/raw/company--rlwrld-business-poc.txt)
3. [Co-build the Industry Model (파트너십)](https://www.rlwrld.ai/ko/business/partnership) - RLWRLD, 2026-10-07 열람, 1차, (ko) (raw: reference/raw/company--rlwrld-business-partnership.txt)
4. [RLWRLD Business](https://www.rlwrld.ai/ko/business) - RLWRLD, 2026-10-07 열람, 1차, (ko) (raw: reference/raw/company--rlwrld-business.txt)
5. [The Physical Intelligence Layer](https://www.pi.website/blog/partner) - Physical Intelligence, 원문 미열람, 검색 요약, (en)
6. [F.02 Contributed to the Production of 30,000 Cars at BMW](https://www.figure.ai/news/production-at-bmw) - Figure, 1차, (en) (raw: reference/raw/rxcase--figure-bmw-production.txt)
7. [BMW to Use Figure AI's Figure 03 for Logistics Work](https://theaiinsider.tech/2026/06/26/bmw-to-use-figure-ais-figure-03-for-logistics-work-at-us-factory/) - The AI Insider, 2026-06-26, 기사, (en)
8. [Digit passes 100,000-tote milestone at GXO](https://roboticsandautomationnews.com/2025/11/24/agility-robotics-digit-humanoid-passes-100000-tote-milestone-in-live-gxo-implementation/96877/) - Robotics & Automation News, 2025-11-24, 기사, (en)
9. [Apptronik Apollo Mercedes-Benz deployment](https://startupfortune.com/apptroniks-apollo-robot-has-left-the-lab-and-is-now-working-factory-shifts-at-mercedes-benz/) - Startup Fortune, 기사, (en)
10. [Boston Dynamics Opens Atlas Training Center at Hyundai's Georgia Metaplant](https://theaiinsider.tech/2026/09/22/boston-dynamics-opens-atlas-training-center-at-hyundais-georgia-metaplant/) - The AI Insider, 2026-09-22, 기사, (en)
11. [Skild AI reaches $100 million ARR after 10 months](https://roboticsandautomationnews.com/2026/09/18/skild-ai-reaches-100-million-in-annual-recurring-revenue-after-10-months/104958/) - Robotics & Automation News, 2026-09-18, 기사, (en)
12. [FedEx Case Study](https://dexterity.ai/blog/case-studies/fedex) - Dexterity, 1차, (en) (raw: reference/raw/rxcase--dexterity-fedex.txt)
13. [FedEx and Dexterity Expand at Hagerstown Hub](https://dexterity.ai/blog/fedex-hagerstown-physical-ai-deployment) - Dexterity, 2026-07, 1차(검색 요약), (en)
14. [Telexistence and Physical Intelligence partnership](https://tx-inc.com/en/blog/2025/06/25/12307/) - Telexistence, 2025-06-25, 1차(검색 요약), (en)
15. [Restocking Robot Rolls Out to Hundreds of Japanese Convenience Stores](https://blogs.nvidia.com/blog/telexistence-convenience-store-robotics/) - NVIDIA Blog, 기사, (en)
16. [Sanctuary AI enters strategic relationship with Magna](https://www.therobotreport.com/sanctuary-ai-enters-strategic-relationship-with-magna-to-build-embodied-ai-robots/) - The Robot Report, 2024-04, 기사, (en)
