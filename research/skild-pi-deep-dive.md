# 심층 분석: Skild AI와 Physical Intelligence
조사일: 2026-10-07

## 핵심 요약
- **둘 다 RLWRLD와 같은 "지능 계층" 회사지만 전략은 정반대다.** Physical Intelligence(PI)는 연구 주도형으로, 소수의 파트너와 깊게 일하고 일부 모델을 공개하며 공개된 매출이 없다. Skild AI는 배포 주도형으로, ABB·Universal Robots 같은 로봇 제조사(OEM)를 유통 채널로 삼아 상업 배포 10개월 만에 연 반복 매출(ARR) 1억 달러, 유료 고객 60곳 이상을 보고했다 [S2][P2][P5].
- **우리 B2 케이스와 직접 겹친다.** Skild의 고객 중 하나가 **住友電装(Sumitomo Wiring Systems)의 와이어 하네스 조립 자동화**다. B2에서 업계 1위권 근거로 인용한 회사다. 또 Skild S1은 "영상 1개로 새 작업을 몇 분 안에 배운다"고 주장해, 우리가 RLWRLD의 강점으로 내세운 "시연 몇 개로 새 품번 적응"과 같은 영역을 노린다 [S2][S3].
- **규모 격차가 크다.** PI는 약 21억 달러, Skild는 20억 달러 이상을 조달했다. RLWRLD 누적 4,100만 달러의 약 50배다. RLWRLD가 이길 곳은 범용성 경쟁이 아니라 **다섯 손가락 정밀 조작, 한국·일본 산업 데이터, RX 컨설팅의 깊이**로 좁혀야 한다 [P1][S4][A1].

## 1. 회사 개요

| 항목 | Physical Intelligence (π) | Skild AI | (참고) RLWRLD |
|------|---------------------------|----------|---------------|
| 설립·본사 | 2024, 샌프란시스코 | 피츠버그 | 2024-07, 서울·샌프란시스코·도쿄 |
| 창업자 | Karol Hausman, Sergey Levine, Chelsea Finn, Brian Ichter 등 (Google DeepMind, Stanford, UC Berkeley 출신) [P1] | Deepak Pathak, Abhinav Gupta (CMU 출신) [S2] | 류중희 |
| 투자 | 2024 4억 달러(기업가치 약 24억 달러), 2025-11 6억 달러(56억 달러, CapitalG 주도), 2026 10억 달러 규모 협상(110억 달러) 보도. 누적 약 21억 달러(보도) [P1][P6] | 2025 중반 기업가치 45억 달러, **2026-01 시리즈 C 14억 달러(140억 달러 이상, SoftBank 주도, NVIDIA, Bezos, Samsung, LG, Schneider, Salesforce Ventures 참여)**. 누적 20억 달러 이상 [S4] | 누적 4,100만 달러 (research/company.md) |
| 정체성 | "로봇과 물리 장치를 제어하는 머신러닝 모델" 개발. 하드웨어를 만들지 않음 [P1] | "움직이는 모든 기계를 제어하는 통합 파운데이션 모델". 슬로건 "any robot, any task, one brain" [S1] | "Dexterity is Intelligence", 다섯 손가락 조작 특화 |
| 상업화 | 공개된 상용 제품·매출 없음(보도) [P3] | **ARR 1억 달러(상업 배포 10개월), 유료 고객 60곳 이상**, 매출의 약 86%가 조작(manipulation) 작업 [S2] | 공개 매출 없음. RX → PoC → 파트너십 |

## 2. Physical Intelligence: 연구 주도형

### 2.1 모델 계보
| 시기 | 모델 | 핵심 | 근거 |
|------|------|------|------|
| 2024-10 | π0 | VLM + flow matching, 다양한 로봇 데이터 | research/tech.md |
| 2025-02 | openpi 공개 | π0 코드(Apache 2.0)와 가중치, 미세조정 도구 공개. π0.5 기본 가중치는 2025-09 공개, 그 이후 모델은 가중치 비공개 | [P3] |
| 2025-04 | π0.5 | 이종 데이터 공동 학습으로 처음 보는 가정에서 작업 | research/tech.md |
| 2025-11 | π*0.6 (RECAP) | 시연 + 전문가 교정 + 자율 시도 강화학습. 어려운 작업에서 처리량 2배 이상, 실패 절반 이하. 에스프레소 18시간 연속, 새 세탁물 50벌, 공장 상자 59개 조립 | [P4] |
| 2026-02 | π0.6 배포 데이터 공개 | 파트너 하드웨어 위 실제 운영 데이터 (아래 2.2) | [P2] |
| 2026-04-16 | **π0.7** | 5B 파라미터. **조합적 일반화**(배운 개념을 섞어 처음 보는 작업 수행), 셔츠 접기 데이터가 없던 양팔 UR5e에서 셔츠 접기, 말로 코칭해 새 가전 사용. 단일 모델이 RL로 특화한 π*0.6과 같거나 나은 성능 | [P5] |

### 2.2 파트너 배포 (2026-02 공개)
- **Weave Robotics (세탁물 개기, 7,999달러 고정형 기계 Isaac 0):** π0.5 → π0.6 전환으로 전체 시간 대비 자율 비율 증가. Weave 데이터를 사전학습에 넣자 집기 실패 42% 감소, 세탁물 1회분당 원격 조작자 개입 50% 감소 [P2].
- **Ultra Robotics (전자상거래 포장, 양팔 고정형 OP1):** Ultra 데이터로 미세조정한 π0.6이 포장 처리량(시간당 품목 수)을 크게 높임. 작업을 하위 작업으로 나누고, 실패 상황에서 더 다양한 복구 전략을 고름 [P2].
- **Telexistence (일본 편의점 음료 보충):** 2025-06 파트너십 발표 (research/rx-cases.md).
- 자체 시험: 샌프란시스코 단기 임대 숙소의 세탁물 개기, Dandelion Chocolate 백룸 상자 접기 [P1].

### 2.3 사업 방식
- **파트너가 하드웨어와 현장을 소유하고, PI는 모델을 공급**하는 구조. 언론은 이를 "로봇의 API화"로 부른다. 앱 개발자가 LLM API를 부르듯 로봇 회사가 PI 모델을 부른다는 그림이다 [P2].
- 파트너 데이터를 사전학습에 섞어 모델을 키우고(+WPT, +UPT), 그 결과를 다시 파트너 성능 향상으로 돌려준다 [P2].
- 공개된 가격·계약 구조는 없다.

## 3. Skild AI: 배포 주도형

### 3.1 모델과 학습 방식
- **Skild Brain:** 다양한 로봇 형태를 하나의 모델로 제어하는 "omni-bodied" 모델. 여러 로봇의 데이터를 한 모델에 모으는 데이터 플라이휠을 노린다 [S1].
- **사전학습 데이터:** "인터넷 규모의 로봇 데이터가 없다"는 문제를 **인터넷 인간 영상 + 대규모 시뮬레이션**으로 푼다. NVIDIA Isaac Lab·Sim으로 물리 시뮬레이션, Cosmos로 합성 데이터 [S1].
- **현장 적용:** 기본 모델을 적은 작업 데이터로 미세조정(post-training). 데이터가 "꼭 실로봇에서 나올 필요는 없다"고 밝힘 [S1].
- **S1 (2026-08):** 가중치 업데이트 없이 **영상 1개를 보여 주면 몇 분 안에 새 공정을 수행**하는 시각적 in-context learning. 처음 보는 다단계 작업에서 단계 성공률 66%, 이는 텔레오퍼레이션 약 380회로 얻던 수준과 같다고 주장 [S2][S3].
- **"Physical RSI":** 현장에 배포 → 예외 상황 데이터 수집 → 특화 학습 결과를 기본 모델로 증류하는 순환 [S2].

### 3.2 고객과 배포
| 고객 | 작업 | 공개 결과 | 근거 |
|------|------|-----------|------|
| **Foxconn + NVIDIA** (휴스턴) | Blackwell 서버 조립: 버스바 배치 → 리밋 블록 → 나사 16개 연속 체결 → 리밋 블록 제거. 양팔, 힘 제한 접촉 제어, 수 분짜리 장기 작업을 in-context 메모리로 수행 | 설계 변경을 재프로그래밍 없이 흡수한다고 주장. 정량 성공률 미공개 | [S1][S2] |
| **住友電装 (Sumitomo Wiring Systems)** | **와이어 하네스 조립** (변형체 전선) | 결과 미공개 | [S2] |
| Mitsui & Co. (AIM Services) | 단체급식 접시 담기. AIM은 하루 약 140만 식 제공 | 결과 미공개 | [S2] |
| G10 Fulfillment | 전자상거래 피킹·포장 | **시간당 50라인 → 130~140라인** (G10 COO 발언) | [S2] |
| STN Inc. | 데이터센터 점검 | - | [S2] |
| ABB, Universal Robots, MiR (2026-03) | **로봇 제조사 포트폴리오에 Skild Brain 탑재** | 파트너십 단계 | [S1] |

### 3.3 사업 방식과 철학
- **유통:** OEM 탑재(ABB, UR, MiR) + 기업 고객 직접 배포 + 산업별 솔루션 모듈. 언론 분석은 API·라이선스형 B2B로 설명하지만 가격은 비공개 [S1][S5].
- **단계적 확장:** 반정형 환경(공장) → 덜 정형화된 환경(병원, 호텔) → 가정 [S1].
- **"데모 문화" 비판:** "정확도 5%, 10%, 99%짜리 로봇의 성공 영상은 똑같아 보인다." "정확도 99.9%라도 10배 느리면 배포 직전이 아니라 배포 불가다." 공정 사이클 타임을 핵심 지표로 본다 [S2].

## 4. 세 회사 비교

| 항목 | Physical Intelligence | Skild AI | RLWRLD |
|------|-----------------------|----------|--------|
| 무엇을 파나 | 범용 모델 (파트너 하드웨어용) | 범용 모델 + OEM 탑재 + 산업 솔루션 | 손 조작 특화 모델 + RX 컨설팅 + 공동 모델 |
| 강조점 | 일반화, 강화학습으로 현장 개선 | 배포 속도, 사이클 타임, 모든 로봇 형태 | 다섯 손가락 정밀 조작, 촉각·힘 |
| 데이터 | 파트너 운영 데이터 + 자체 수집 | 인간 영상 + 시뮬레이션 + 고객 현장 | 에고센트릭 + 텔레오퍼레이션 + 합성, 고객 공동 데이터 |
| 새 작업 적응 | 언어 코칭, 조합적 일반화 (π0.7) | 영상 1개 in-context (S1) | 소량 시연 미세조정 (회사 주장) |
| 유통 | 소수 파트너 직접 협업 | **로봇 제조사 탑재** + 기업 직접 | **RX(컨설팅)** → 랩 PoC → 다년 파트너십 |
| 일본·한국 | Telexistence(일본) | 住友電装, Mitsui(일본), 투자자 Samsung·LG | KDDI·Lawson(일본), 롯데·CJ·LG·SK(한국) |
| 상업화 | 매출 비공개 | ARR 1억 달러 | 매출 비공개 |
| 공개 정책 | π0, π0.5 가중치 공개 | 비공개 | 코드 공개, 가중치 비상업 라이선스 |

## 5. 비판적 시사점 (RLWRLD와 우리 케이스)

1. **하네스 케이스의 차별점을 다시 세워야 한다.** Skild가 이미 住友電装에서 하네스 자동화를 하고 있다. B2 스토리라인의 "시연으로 새 품번을 배우는 범용 셀"은 Skild S1의 주장과 같다. RLWRLD만의 근거는 **다섯 손가락 + 촉각이 필요한 단계(레이업의 전선 훑기·분기 정리)**에 있고, 그래서 B2의 B트랙(손이 꼭 필요한지 검증)이 오히려 차별화의 핵심이 된다. 그리퍼 대조군에서 손이 이기지 못하면 RLWRLD는 Skild와 가격으로 경쟁하게 된다.
2. **사이클 타임이 승부처라는 B2 결론은 Skild도 같은 말을 한다.** "99.9% 정확해도 10배 느리면 배포 불가." B2 ROI의 1순위 변수(속도비)와 일치한다. RLWRLD 공개 수치에는 사이클 타임이 없다. 고객 제안에서 이 공백을 먼저 채워야 한다.
3. **유통 경로의 차이가 확장 속도를 가른다.** Skild는 ABB·UR 같은 로봇 제조사를 통해 이미 깔린 로봇에 들어간다. RLWRLD의 RX는 고객마다 진단부터 시작하므로 깊지만 느리다. RLWRLD도 하드웨어 파트너(레인보우로보틱스, 원익로보틱스, 로보티즈, 위로보틱스)를 **OEM 탑재 채널**로 쓸 수 있는지가 중요한 질문이다.
4. **일본은 이미 경쟁 시장이다.** RLWRLD가 도쿄 거점과 KDDI로 공략하는 일본에서 Skild는 住友電装·Mitsui, PI는 Telexistence와 일한다. "한국 AI + 일본 제조 데이터"라는 RLWRLD의 서사는 독점이 아니다.
5. **한국 대기업 관계도 독점이 아니다.** LG는 RLWRLD 시드 투자자이면서 Skild 시리즈 C에도 참여했다. Samsung도 Skild 투자자다.
6. **규모 격차를 전제로 전략을 세워야 한다.** 조달액이 약 50배 차이다. 범용 모델 경쟁으로는 이기기 어렵고, 손 조작이 결정적인 공정과 한국·일본 현장 데이터를 깊게 쌓는 쪽이 현실적이다. 면접에서 이 격차를 알고 있다고 말하는 것 자체가 신뢰를 높인다.
7. **두 회사의 수치도 대부분 자체 발표다.** Skild의 ARR·고객 수, PI의 개입 50% 감소 모두 회사 발표나 언론 보도이고 독립 검증은 없다. RLWRLD의 86.8%를 "자체 평가"로 표시한 것과 같은 기준으로 다뤄야 한다.

## RX 관점 시사점
- **B4 스토리라인에 반영 제안:** ① 경쟁 장에 "Skild × 住友電装 하네스"를 넣고 RLWRLD의 차별점을 레이업(손이 필요한 단계)으로 명확히 함 ② PoC KPI의 1순위를 사이클 타임(속도비)으로 유지 ③ 확산 시나리오에 하드웨어 파트너 탑재 경로 추가
- **면접에서:** "PI는 연구, Skild는 배포 속도로 앞서 있다. RLWRLD는 손 조작이 결정적인 공정과 아시아 산업 데이터로 좁혀야 하고, RX는 그 데이터를 확보하는 입구다."

## 확인하지 못한 항목
- PI 파트너 프로그램 페이지 원문 (pi.website 접속 제한 429)
- 이전 문서(research/rx-cases.md)에 적은 "Ultra 한 교대 자율률 96.4%"는 이번에 읽은 원문 기사에서 확인되지 않았다. 검색 요약에서 온 수치라 `확인필요`로 낮춘다.
- Skild의 가격·계약 구조, 住友電装 프로젝트의 범위와 결과, Foxconn 셀의 성공률과 사이클 타임
- Skild의 손 하드웨어 (다관절 손을 쓰는지, 그리퍼인지)
- PI의 Series C 실제 체결 여부 (보도와 등기 기반 추정만 있음)

## 출처
- [S1] [The Reindustrial Revolution: Partnering with ABB Robotics, Universal Robots, and NVIDIA](https://www.skild.ai/blogs/reindustrial-revolution) - Skild AI, 2026-03-19, 1차, (en) (raw: reference/raw/competitors--skild-reindustrial.txt)
- [S2] [Skild AI Crosses $100M ARR in 10 Months](https://www.humanoidsdaily.com/news/skild-ai-crosses-100m-arr-in-10-months-mounting-an-enterprise-assault-on-robotics-demo-culture) - Humanoids Daily, 2026-09, 기사(창업자 에세이 인용 포함), (en) (raw: reference/raw/competitors--skild-arr-humanoidsdaily.txt)
- [S3] [Skild AI Taps NVIDIA Physical AI to Teach Robots New Tasks From a Single Video](https://blogs.nvidia.com/blog/skild-ai-s1-physical-ai/) - NVIDIA Blog, 2026, 기사, (en) (raw: reference/raw/competitors--skild-s1-nvidia.txt)
- [S4] [Skild AI Raises $1.4B, Now Valued Over $14B](https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-$1.4B-Now-Valued-Over-$14B) - Business Wire, 2026-01-14, 1차(보도자료, 검색 요약), (en)
- [S5] [Report: Skild AI Business Breakdown](https://research.contrary.com/company/skild-ai) - Contrary Research, 분석 보고서, (en) (raw: reference/raw/competitors--skild-contrary.txt)
- [P1] [Physical Intelligence Inc.](https://en.wikipedia.org/wiki/Physical_Intelligence_Inc.) - Wikipedia, 2026-10-07 열람, (en) (raw: reference/raw/competitors--pi-wikipedia.txt)
- [P2] [The API-fication of Robotics: PI Unveils Real-World Performance Data with Weave and Ultra](https://www.humanoidsdaily.com/news/the-api-fication-of-robotics-physical-intelligence-unveils-real-world-performance-data-with-weave-and-ultra) - Humanoids Daily, 2026-02, 기사, (en) (raw: reference/raw/competitors--pi-weave-ultra-humanoidsdaily.txt)
- [P3] [Physical Intelligence platform intel](https://github.com/redhat-et/physical-ai-platform-intel/blob/main/deliverables/intel/companies/physical-intelligence.md) - Red Hat ET, 분석 문서(검색 요약), (en)
- [P4] [π*0.6: a VLA That Learns From Experience](https://www.pi.website/download/pistar06.pdf) - Physical Intelligence, 2025-11, 1차(검색 요약), (en)
- [P5] [Physical Intelligence Unveils π0.7](https://www.humanoidsdaily.com/news/physical-intelligence-unveils-0-7-the-rise-of-compositional-generalization-in-robotics) - Humanoids Daily, 2026-04, 기사(검색 요약), (en)
- [P6] [Physical Intelligence is reportedly in talks to raise $1B, again](https://techcrunch.com/2026/03/27/physical-intelligence-is-reportedly-in-talks-to-raise-1-billion-again/) - TechCrunch, 2026-03-27, 기사(검색 요약), (en)
- [A1] research/company.md (RLWRLD 누적 투자, 투자자)
