# 경쟁사 비교: RFM 및 로봇 손 조작 경쟁 구도
조사일: 2026-10-06

## 핵심 요약
- 비교한 6개 해외 경쟁사는 사업 방식이 서로 다르다. Physical Intelligence는 모델 전문, Figure와 Tesla는 자체 휴머노이드까지 만드는 풀스택, Skild AI는 산업용 로봇 OEM에 두뇌를 내장하는 방식, NVIDIA는 오픈 모델과 시뮬레이션·연산 플랫폼, Google DeepMind는 파트너 대상 조기 접근 제공이다 [8][11][22][14][19][15]. RLWRLD는 "손 특화 모델 + 고객 현장 데이터 확보(RX)"로 이들과 구분되지만(본 문서의 해석) 자금 규모에서는 크게 뒤진다. 누적 4,100만 달러 대 Skild 단일 라운드 약 14억 달러(약 34배, 계산) [3][4][13].
- 에고센트릭 인간 영상으로 손 조작을 확장하는 전략은 RLWRLD만의 것이 아니다. NVIDIA는 GR00T N1.7을 에고센트릭 영상 20,854시간, 22-DoF 손 지원, "commercially licensed" 표기로 공개했고(2026-04, 자체 주장), Tesla도 작업자 착용 카메라로 데이터를 모은다는 단일 기사 보도가 있다 [19][22]. RLDX-1의 차별점은 데이터 방식 자체보다 촉각·토크 입력(Physics 모듈), 기억 모듈, 고객 공정과 연결된 RX 구조에 있다고 읽는 편이 정확하다(본 문서의 해석).
- 한국 대기업은 여러 곳에 걸쳐 있다. LG 계열 이름이 RLWRLD(시드1), Figure(시리즈C), Skild(전략 투자자 명단)에 나오고 NVIDIA와도 로보틱스 협력을 한다 [3][12][13][18]. 소스별 표기가 달라 같은 법인인지는 확인하지 못했다. 일본은 PI와 Telexistence, Skild와 SoftBank 접점이 확인된다 [10][13]. 경쟁 구도와 고객·투자 구도가 겹치므로 RX 제안 시 고객사의 다른 로봇 AI 관계를 먼저 확인해야 한다. 단, RLDX-1의 성능 우위는 자체 평가이고 비교 대상이 π0.5, GR00T N1.6이라, 2026-04 공개된 π0.7, GR00T N1.7과의 비교는 확인하지 못했다 [1][2][8][19].

## 본문

### 1. 비교표 (템플릿 항목)
모든 수치는 각 회사의 자체 주장 또는 기사 서술이다. 독립 비교 벤치마크는 확인하지 못했다.

| 회사 | 국가 | 최신 모델 (공개일) | 접근 방식 | 타깃 하드웨어 | 타깃 산업 | 투자 규모 | RLWRLD 대비 차별점 |
|------|------|--------------------|-----------|---------------|-----------|-----------|--------------------|
| RLWRLD | 한국(서울), 미국(SF HQ 표기), 일본 사무소 | RLDX-1 (2026-05) [1][2] | 손 특화 VLA(MSAT, 촉각·토크, 기억), 코드 Apache 2.0 / 가중치 비상업 라이선스 [2][21] | ALLEX(양손 15-DoF), Franka Research 3, OpenArm + Inspire 손 [2] | 제조, 물류, 서비스 [2] | 누적 4,100만 달러(USD, 시드1 1,500만 + 시드2 2,600만) [3][4] | 기준 |
| Physical Intelligence (PI) | 미국 | π0.7 (2026-04-16) [8] | 모델 전문. 웹 규모 사전학습 + 작업 데이터, 조합 일반화(compositional generalization) 주장 [8] | 기사에 상세 없음. 파트너 로봇 사용 [8][10] | 가정 작업 시연(세탁물, 에스프레소, 박스 조립 등 [7]), 편의점 음료 진열(Telexistence 협력) [10] | 협의 보도: 약 10억 달러, 기업가치 110억 달러 이상(2026-03-28, 미발표) [9] | 모델 전문이라 고객 공정 분해(RX) 조직은 확인 못함. 일반화에 초점, 손 특화를 내세우지는 않음 |
| Figure AI | 미국 | Helix 02 (2026-01-27), Figure 03 [11] | 자체 휴머노이드 + 3계층 전신 제어(S0 1 kHz / S1 200 Hz / S2 추론) [11] | 자사 Figure 03 (손끝 촉각 센서 3 g 수준, 손바닥 카메라) [11] | 가정·상업 현장 [12]. 고객은 공식 발표에 명시 없음 [12] | 시리즈C 10억 달러 이상 확약, post-money 390억 달러(2025-09-16) [12] | 자사 하드웨어와 모델을 묶는 구조(해석: 다른 고객 로봇 적용은 확인 못함). RLWRLD는 여러 손에서 실험(ALLEX, Franka, Inspire) [2] |
| Skild AI | 미국 | Skild Brain ("omni-bodied") [13] | 구현체 불문 범용 두뇌. ABB·UR 로봇에 내장, "any robot, any task, one brain" [13][14] | 사족보행, 휴머노이드, 탁상 팔, 모바일 매니퓰레이터 [13]. 사례는 팔 기반 나사 체결 [14] | 보안, 점검, 배송, 창고, 제조, 데이터센터, 건설 [13]. Foxconn 조립 라인 [14] | 약 14억 달러, 기업가치 140억 달러 초과(2026-01-14) [13] | 사례 공개된 작업은 팔 기반이고 고자유도 손 사례는 확인하지 못함. 산업용 OEM 채널(ABB, UR)은 RLWRLD에 없는 유통망 [14] |
| Google DeepMind | 미국/영국 | Gemini Robotics 2, ER 2, On-Device 2 (2026-07-30) [15] | 대형 VLM(Gemini) 기반 VLA + 추론 모델 분리. 조기 접근 파트너 제공 [15] | Apptronik Apollo 2 + SharpaWave 손(22 DoF), Inspire 손, Franka + Robotiq 그리퍼 등 [15] | 휴머노이드 일반 작업(전구 끼우기, 쓰레기봉투 묶기 등 시연은 검색 요약 수준) [15] | Alphabet 내부 사업으로 별도 투자 정보 없음(확인 못함) | 공식 블로그가 다지(多指) 손 조작은 여전히 어렵다고 인정, 작업별 편차가 크다(전구 끼우기 36%, 같은 로봇의 전구 빼기 92%) [15]. 손 특화 모델을 내세우는 RLWRLD와 같은 문제를 보는 중 |
| NVIDIA | 미국 | GR00T N1.6 (2026-01-05), N1.7 (2026-04-17, Early Access) [18][19] | 오픈 VLA(이중 시스템, 3B) + Isaac/Cosmos 시뮬레이션 + Jetson Thor 연산 플랫폼 [18][19] | Unitree G1, YAM, AGIBot Genie 1 등. 22-DoF 손 지원 [19] | 제조, 리테일, 의료, 가정 작업 범주 [19]. 파트너: Boston Dynamics, LG전자, NEURA 등 [18] | 상장사. Figure, Skild에 투자 참여 [12][13] | 에고센트릭 20,854시간 + 22-DoF 손 + 상업 사용 가능 표기로 RLWRLD 데이터 전략과 가장 직접 겹침. 촉각 입력은 열람 자료에서 미확인 [19] |
| Tesla Optimus | 미국 | Optimus V3 (2026-04-22 발언 기준 공개는 "2026 중반" 예정으로 지연 [24]. 2026-09 기사는 V3 유닛 생산과 재작업을 서술하나 공식 공개 여부는 미확인 [22]) | 자사 휴머노이드 + 자사 AI, 작업자 착용 카메라 기반 모방학습(기사) [22] | 자사 Optimus. 손 사양은 미확정(특허 22-DoF 설계는 "작동하지 않았다"는 Musk 발언) [22][23] | 초기 V3는 창고 고객에게 임대, 본격 판매는 2027년 말 이후(기사) [22] | 상장사(해당 없음) | 모델 외부 제공 계획은 확인하지 못함. 당장은 고객 시장 경쟁보다 손 하드웨어·데이터 방식의 참고 사례 |

### 2. 손 조작 근거 비교 (공개된 증거 수준)
| 회사 | 손 조작 관련 공개 증거 | 촉각·힘 입력 | 증거 성격 |
|------|-------------------------|--------------|-----------|
| RLWRLD | ALLEX 실세계 4과제 평균 86.8%(π0.5 39.1%, GR00T N1.6 44.8%), 과제당 24회, 진행 점수 혼합. Plug Insertion 33.3% [1] | RGB + 관절 토크(ALLEX), 촉각은 Franka 그리퍼에서만. 없으면 vision-only로 동작(저하 폭 미공개) (2026-10-07 A11 정정) [2] | 자체 평가, 작업은 회사 설계 |
| PI | π*0.6: 어려운 작업에서 처리량 2배 이상, 실패율 약 50% 감소 [7]. π0.7: 학습에 거의 없던 작업을 말 지시로 수행하나 프롬프트에 따라 성공률 5~95%로 변동(기사) [8] | 열람한 자료에서 확인하지 못함 | 자체 평가, 외부 표준 벤치마크 없음(기사) [8] |
| Figure | 시연: 알약 꺼내기, 5 ml 주사기 분주, 병뚜껑 풀기, 61개 동작의 약 4분 식기세척기 작업 [11]. 성공률 수치 없음 | 손끝 촉각(3 g 수준)과 손바닥 카메라를 S1 입력에 포함 [11] | 시연 영상 중심 |
| Skild | 사례는 Foxconn 라인의 양팔 로봇 조립, 연속 나사 16개 체결 [14] | 확인하지 못함 | 회사 블로그, 수치 없음 |
| DeepMind | 그리퍼 기반 pick-and-place 74.2%, 정밀 삽입 89.6%. 다지 손(Apollo + SharpaWave)은 작업별 편차가 커서 전구 끼우기(screw bulb) 36%, 전구 빼기(unscrew bulb) 92% [15] | 확인하지 못함 | 자체 평가, 조건 요약 수준(36%와 92% 수치는 팩트체크의 원문 대조 기준) |
| NVIDIA | 에고센트릭 1k -> 20k시간에서 평균 작업 완료율 2배 이상(블로그 주장), 22-DoF 손 지원 [19] | 열람 자료에 언급 없음(미확인) | 자체 평가, 조건 미확인 |
| Tesla | 손 성능 수치 없음. 손 설계는 재설계 중 [23] | 확인하지 못함 | Musk 발언과 기사 |

- 이 표의 수치는 작업, 로봇, 평가 방식이 모두 달라 서로 비교하면 안 된다. 같은 기준의 공개 비교는 RLDX-1 논문이 π0.5, GR00T N1.6과 맞붙은 것 하나이며, 논문 공개 시점(2026-05)에 이미 π0.7(2026-04-16), GR00T N1.7(2026-04-17)이 나온 상태였다 [1][8][19]. 최신 버전과의 비교는 확인하지 못했다.
- 특이점: DeepMind는 자사 블로그에서 다지 손 조작이 어렵다고 밝힌다 [15]. 반대로 손 조작 가능성을 앞세우는 회사가 많아, 고객에게는 "어떤 작업에서 몇 회 시행한 수치인가"를 먼저 묻도록 안내해야 한다.

### 3. 하드웨어 전략과 데이터 전략
| 회사 | 하드웨어 전략 | 데이터 전략 | 출처 |
|------|---------------|-------------|------|
| RLWRLD | 하드웨어 비종속. 여러 손과 로봇에서 실험(ALLEX, Franka, OpenArm + Inspire) | 실 텔레오퍼레이션 + 인간 손 캡처 리타게팅(시간당 200건 이상) + 합성 증강(약 5배), 고객 현장 에고센트릭 수집 | [2] |
| PI | 모델 전문(자체 로봇 판매 확인 못함). 파트너 로봇 사용 | 광범위한 이종 데이터 + 파트너 현장 데이터. Telexistence는 편의점 로봇 텔레오퍼레이션 데이터를 제공하고 PI는 오류 복구 정책을 학습 | [8][10] |
| Figure | 풀스택. 자체 휴머노이드와 제조(BotQ) | 사람 영상과 멀티모달 감각 입력 수집, 사람 모션 1,000시간 이상 리타게팅(S0), GPU 인프라 투자 | [11][12] |
| Skild | 산업용 로봇 OEM 내장(ABB, UR). 자체 본체 판매는 확인 못함 | 배치 로봇이 만드는 데이터 플라이휠, 인터넷 인간 영상, 대규모 시뮬레이션. 반구조화(공장) -> 비구조화 환경 순서로 확장 | [14] |
| DeepMind | 파트너 로봇(Apptronik, Franka 등). 제3자 손(SharpaWave, Inspire) 지원 | On-Device 모델은 새 로봇에 수 시간, 약 200개 미만 예시로 적응한다고 주장. Apptronik "Robot Park"에서 Apollo 2 데이터 수집(검색 요약) | [15] |
| NVIDIA | 플랫폼 공급. 로봇은 파트너가 제작(참고 설계 Unitree 예정, 검색 요약) | 인간 에고센트릭 영상 20,854시간 + 합성(Cosmos) | [18][19] |
| Tesla | 풀스택 | 작업자가 5대 카메라 헬멧과 백팩 착용, 누적 50만 시간 이상(Tech Times 단일 기사 서술, 1차 미확인) | [22] |

- 고객 현장 데이터를 해자로 삼는다는 점에서 비슷한 사례: PI와 Telexistence(일본 편의점 로봇 운영 데이터), Skild와 Foxconn(공장 라인) [10][14]. RLWRLD의 "RX가 데이터 채널" 구조는 같은 방향이다.
- 계보 해석(본 문서): 같은 에고센트릭 수치(20,854시간)가 NVIDIA 블로그와 EgoScale에서 모두 나온다. EgoScale 저자에 NVIDIA 소속으로 알려진 연구자(Linxi Fan)가 있어 같은 연구 계열로 추정하나, 초록 페이지에 소속 표기는 없다 [19][26].

### 4. 투자 규모
| 회사 | 최근 확인된 라운드 | 금액(USD) | 기업가치 | 일자 | 신뢰도 | 출처 |
|------|--------------------|-----------|----------|------|--------|------|
| RLWRLD | 시드2 (누적 시드 2회) | 2,600만(약 390억 원), 누적 4,100만 | 약 400억 원은 2025-09 기준 기업가치(기사 추정치, 공식 아님, research/company.md 3절)이며 시드2 라운드 금액(약 390억 원)과 다른 값이다 | 2026-02-26 | 높음(보도자료 + 기사, 기업가치는 `추정`) | [3][4] |
| PI | 신규 라운드 협의 | 약 10억 | 110억 이상 (직전 56억) | 2026-03-28 보도 | 협의 보도, 미발표 | [9] |
| Figure | 시리즈C | 10억 이상 확약 | post-money 390억 | 2025-09-16 | 높음(1차) | [12] |
| Skild | 14억 라운드 (SoftBank 리드) | 약 14억 | 140억 초과 | 2026-01-14 | 높음(보도자료). 매출 약 3,000만 달러(2025)는 회사 주장 | [13] |
| DeepMind, NVIDIA, Tesla | 해당 없음(대기업·상장사 내부 투자) | - | - | - | - | - |

- PI 누적 조달은 소스 간 충돌이 아니라 합산 범위의 차이로 설명된다. 기사 [9]의 "10억 달러 이상"은 시리즈C 이전 합계에 해당한다: 시드 약 7,000만 + 시리즈A 약 4억 + 시리즈B 약 6억 = 약 10.7억 달러(`추정`). 시리즈C 약 10.5억 달러(2026-05 기업 공시에 보이나 회사가 발표하지 않았다는 서술)를 포함하면 약 21억 달러(`추정`). 라운드별 금액과 합산 근거는 검색 요약(2차 집계 사이트) 수준이며 원문을 열지 못했다.
- Figure 누적 약 19억 달러는 2차 집계 사이트의 값이라 `추정`이다. 1차 소스에서 확인되는 값은 시리즈C 10억 달러 이상이다 [12].
- 크기 비교(계산): Skild 라운드 14억 / RLWRLD 누적 0.41억 = 약 34배. RLWRLD는 자본·연산 경쟁이 아니라 영역 특화와 파트너 구조로 경쟁하는 위치다.
- NVIDIA는 Figure(시리즈C 참여)와 Skild(NVentures 참여)의 투자자다 [12][13]. RLWRLD는 시드 공식 투자자 목록에 NVIDIA가 없다(research/company.md 3절).

### 5. 한국·일본 시장 위치
| 회사 | 한국 접점 | 일본 접점 | 출처 |
|------|-----------|-----------|------|
| RLWRLD | 서울 R&D, LG전자·SK텔레콤·CJ대한통운·롯데벤처스 등 투자, 롯데호텔 데이터 수집 | 도쿄 사무소, KDDI(GENIAC)·ANA·Mitsui Chemicals 투자, KDDI/Lawson 에고센트릭 데이터 | [3][4][27], research/company.md |
| PI | 확인하지 못함 | Telexistence와 편의점 음료 진열 협력(2025-06-25). 매장 수(FamilyMart·Lawson 300곳 이상)는 검색 요약 수준이라 `추정` | [10] |
| Figure | LG Technology Ventures가 시리즈C 참여 | 확인하지 못함 | [12] |
| Skild | Samsung, LG 전략 투자자, Mirae Asset, "KIC"(약칭, 기관 미확인) | SoftBank가 14억 달러 라운드 리드. SoftBank의 ABB 로보틱스 인수 합의는 검색 요약 수준(원문 미열람) | [13][14] |
| Google DeepMind | 확인된 한국 접점 없음. (참고, **검색 요약만 근거, 원문 미열람**: Boston Dynamics(Hyundai 계열) Atlas와 Gemini 협력 보도(CES 2026) [S1]) | 확인하지 못함 | [S1] |
| NVIDIA | LG전자(보도자료 파트너) [18], Hyundai·LG·Doosan·SK·Naver 협력(2026-06 서울 방문) [20] | 확인하지 못함(보도자료에 일본 기업 언급 없음) | [18][20] |
| Tesla | 한국 공급사 언급 없음 | 일본 공급사 언급 없음(핵심 모터·기어 공급사가 중국 닝보에 집중, 기사) | [22] |

- LG는 RLWRLD 시드1 투자자, Figure 시리즈C 참여(LG Technology Ventures), Skild 전략 투자자 명단, NVIDIA GR00T 협력 파트너에 모두 이름이 있다 [3][12][13][18]. 각 투자 주체가 LG전자 본체인지 계열 벤처 조직인지는 소스마다 표기가 달라 같은 법인으로 단정하지 않는다.
- 삼성: Skild 전략 투자자 명단에 있고 [13], 자체 휴머노이드와 RX 조직을 운영한다는 보도가 있다. ZDNet Korea 보도를 재인용한 기사로 삼성 공식 발표는 아니다 [25].
- 조사 범위의 한계(언어 편중): 일본어 소스는 AI Watch 1건 [27]뿐이고 일본 경쟁·정책 주체는 원문을 열지 못했다. 일본 접점 열은 영어 소스(Telexistence, Skild 보도자료)에 의존하므로 일본 시장 위치는 부분적이다.

### 6. 한국 국내 유사 주체
| 주체 | 내용 | 신뢰도 | 출처 |
|------|------|--------|------|
| LG전자 컨소시엄 (과기정통부·IITP 과제) | 월드 파운데이션 모델(WFM) 개발. 참여: 마음AI, 크라우드웍스, 알체라, 로보티즈, 홀리데이로보틱스(전자신문 기재). 컨소시엄 전체 과제 금액 497억 원(정부 340억 + 민간 157억, 기사 표기). 범위는 실내 복합 환경 이동형 매니퓰레이션 | 기사 | [28] |
| KT | 같은 기사에서 로봇 파운데이션 모델(RFM) 개발 담당으로 거론. 497억 원은 LG전자 컨소시엄 전체 금액이며 KT 단독 금액이 아니다. KT 몫은 확인하지 못함 | 기사 | [28] |
| 삼성전자 | RX 사업추진실(CEO 직속)과 자체 휴머노이드, 월드 모델, 구미 "Data Factory". 계열사 Rainbow Robotics와 별도 트랙. ZDNet Korea 보도 재인용 | 기사(2차), 공식 확인 못함 | [25] |
| 기타 | LG CNS(제조용 RFM 플랫폼), ETRI(RFM 표준 V1.0), NC AI와 협력하는 산업 현장용 RFM 기업(삼성DX, 원문 요약 기준, 재확인 필요) | 낮음(원문 요약마다 회사 표기가 달라 재확인 필요) | [29] |

- 이 국내 과제들은 이동형 매니퓰레이션과 월드 모델 중심이며, 고자유도 손 정밀 조작을 명시한 과제는 이번 조사에서 확인하지 못했다 [28]. RLWRLD가 공개 정보상 "손 특화"로 빈 영역에 있다는 해석은 본 문서의 해석이며, 국내 기업 전체를 조사하지는 않았다.
- 일본 국내 경쟁 주체(소프트뱅크·NEC·Honda·Sony 컨소시엄, NEDO 사업 등)는 검색 요약에서만 보였고 원문을 열지 못해 본문 표에 넣지 않았다.

### 7. 포지셔닝 정리
| 유형 | 회사 | 강점 | 약점·불확실성 |
|------|------|------|---------------|
| 모델 전문 | PI | 자금(10억 달러 협의), 일반화 연구 | 사업 모델·상용화 시점 미공개(기사) [8][9] |
| 풀스택 | Figure, Tesla | 하드웨어와 모델 통합, 손끝 촉각 | 자사 로봇에 종속, Tesla는 손 설계 재작업 [11][23] |
| OEM 내장 두뇌 | Skild | ABB·UR 유통망, Foxconn 적용, SoftBank 후원 | 손 조작 사례 미확인 [13][14] |
| 오픈 플랫폼 | NVIDIA | 시뮬레이션·연산·오픈 모델 | 촉각 입력 미확인, 고객 공정 지원 구조는 파트너 의존(`추정`) [18][19] |
| 빅테크 파트너형 | DeepMind | Gemini 추론, 파트너 로봇 다수 | 다지 손은 아직 어렵다고 스스로 인정, 접근이 조기 접근 파트너 한정 [15] |
| 손 특화 + RX | RLWRLD | 촉각·토크·기억, 한국·일본 투자자 겸 고객, 현장 데이터 | 자금 규모, 비상업 가중치 라이선스, 자체 평가, 상용 고객 사례 부족 [1][2][21] |

## RX 관점 시사점
- **고객 제안에서:**
  - 제안서 경쟁 비교는 "모델 순위"가 아니라 공정 적합성 기준으로 쓴다. 고객이 "NVIDIA 오픈 모델(GR00T N1.7)을 쓰면 안 되나"라고 물으면 [19] 답변 축은 (a) 해당 공정의 접촉·기억 요구, (b) 고객 현장 데이터 수집과 학습 파이프라인, (c) 라이선스 조건이다. RLDX-1 가중치는 비상업 라이선스라 고객 입장에서는 약점으로 읽힐 수 있다(research/company.md 4절). 계약 구조는 열린 질문이다.
  - 일본 편의점·리테일 PoC는 PI와 Telexistence 협력과 겹칠 수 있다(`추정`: KDDI/Lawson 진열 PoC [27]와 편의점 음료 진열 [10]). 일본 리테일 후보 공정을 B1에 넣는다면 이 사례를 비교 대상으로 둔다.
  - 한국 대기업 고객은 다른 로봇 AI에도 투자·협력하는 경우가 많다(LG, 삼성). 제안 전에 고객사의 NVIDIA, Figure, Skild 관계를 확인하고, 경쟁이 아니라 보완(특정 공정의 손 정밀 조작)으로 포지셔닝할 여지를 본다.
  - ROI에 경쟁 성공률을 쓰지 않는다. 같은 기준의 비교 데이터가 없고(2절), DeepMind도 다지 손 작업의 편차가 크다고 공개한다(전구 끼우기 36%, 빼기 92%) [15].
- **면접에서:**
  - "RFM 경쟁은 모델 전문(PI), 풀스택(Figure, Tesla), OEM 내장(Skild), 플랫폼(NVIDIA), 빅테크(DeepMind)로 나뉘고, RLWRLD는 손 특화와 현장 데이터를 가진 RX 구조로 구분된다"고 한 문장으로 말할 수 있다.
  - "에고센트릭 데이터 전략은 NVIDIA도 같은 규모(20,854시간)로 공개했으니, 해자는 데이터 방식이 아니라 고객 공정에서 얻는 현장 데이터와 촉각·기억 통합이라고 본다"고 근거와 함께 말할 수 있다.
  - 약점도 안다고 말한다: 자금 규모 약 34배 격차(Skild 라운드 대비), 벤치마크 비교 대상이 구 버전, 비상업 라이선스, 한국·일본 대기업의 다중 투자 구조.

## 확인하지 못한 항목
- π0.7, GR00T N1.7, Gemini Robotics 2의 촉각·힘 입력 사용 여부(열람한 자료에 언급 없음). 열린 질문 "π0, π0.5, GR00T N1.6은 촉각·힘 입력을 쓰는가"에 대한 답은 이번에도 미확정.
- RLDX-1과 최신 모델(π0.7, GR00T N1.7)의 동일 조건 비교, 독립 검증.
- PI 누적 조달(시리즈C 이전 약 10.7억 달러 `추정` / 시리즈C 포함 약 21억 달러 `추정`)과 라운드별 금액, Figure 누적 조달(약 19억 달러)은 모두 2차 집계(검색 요약) 수준.
- Figure Series C 이후 라운드, Figure 고객 실적(BMW 등)은 공식 발표에서 확인하지 못했다(검색 요약에 BMW 30,000대, 로봇 740대 등이 있으나 2차 집계라 사용하지 않음).
- Tesla V3 손의 현행 사양, V3 공식 공개 여부, 생산 수량과 누적 50만 시간(Tech Times 단일 기사).
- Skild 투자자 "KIC"의 기관명, Samsung·LG의 투자 주체(본체 vs 벤처).
- 한국 국내 RFM 기업 목록(nate 기사 원출처는 이데일리로 확인되었으나 요약마다 회사 표기가 달라 재확인 필요), 일본 국내 주체(소프트뱅크 컨소시엄, NEDO 사업). 일본어 소스는 1건뿐이다.
- GR00T N1.7 라이선스 조항 원문(블로그는 "commercially licensed", 검색 요약은 Apache 2.0), GR00T N2의 2026년 말 일정(검색 요약).
- DeepMind와 Hyundai/Boston Dynamics 협력 내용(검색 요약 수준).

## 출처
1. [RLDX-1 Technical Report](https://arxiv.org/abs/2605.03269) - arXiv, 2026-05-05, 논문, (en) (reference/papers--rldx1-tech-report.md)
2. [RLDX-1 Foundation Model](https://www.rlwrld.ai/en/rldx-1) - RLWRLD 공식, 2026-05-07, 1차, (en) (reference/company--rlwrld-rldx1-page.md)
3. [RLWRLD Raises $15M to Build 'GPT for Robots'](https://www.prnewswire.com/news-releases/rlwrld-raises-15m-to-build-gpt-for-robots-backed-by-asias-industrial-giants-302427574.html) - PR Newswire, 2025-04-14, 1차, (en) (reference/company--prnewswire-seed1.md)
4. [리얼월드, 시드2 투자 유치.. "누적 600억 원"](https://www.venturesquare.net/1040934) - 벤처스퀘어, 2026-02-26, 기사, (ko) (reference/company--venturesquare-seed2.md)
5. [π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164) - arXiv, 2024-10-31, 논문, (en) (reference/papers--pi0.md)
6. [π0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054) - arXiv, 2025-04-22, 논문, (en) (reference/papers--pi05.md)
7. [π*0.6: a VLA That Learns From Experience](https://arxiv.org/abs/2511.14759) - arXiv, 2025-11-18, 논문, (en) (reference/papers--pistar06-recap.md)
8. [Physical Intelligence says its new robot brain can figure out tasks it was never taught](https://techcrunch.com/2026/04/16/physical-intelligence-a-hot-robotics-startup-says-its-new-robot-brain-can-figure-out-tasks-it-was-never-taught/) - TechCrunch, 2026-04-16, 기사, (en) (reference/competitors--pi-pi07-techcrunch.md)
9. [Physical Intelligence is reportedly in talks to raise $1 billion, again](https://finance.yahoo.com/sectors/technology/articles/physical-intelligence-reportedly-talks-raise-235940073.html) - Yahoo Finance, 2026-03-28, 기사, (en) (reference/competitors--pi-funding-talks.md)
10. [Telexistence and Physical Intelligence Announce Partnership](https://tx-inc.com/en/blog/2025/06/25/12307/) - Telexistence, 2025-06-25, 1차(보도자료), (en) (reference/competitors--pi-telexistence.md)
11. [Introducing Helix 02: Full-Body Autonomy](https://www.figure.ai/news/helix-02) - Figure AI, 2026-01-27, 1차, (en) (reference/competitors--figure-helix-02.md)
12. [Figure Series C](https://www.figure.ai/news/series-c) - Figure AI, 2025-09-16, 1차, (en) (reference/competitors--figure-series-c.md)
13. [Skild AI Raises $1.4B, Now Valued Over $14B](https://finance.yahoo.com/news/skild-ai-raises-1-4b-150800863.html) - Business Wire 보도자료(Yahoo Finance 재게재), 2026-01-14, 1차, (en) (reference/competitors--skild-series-funding.md)
14. [The Reindustrial Revolution: Partnering with ABB Robotics, Universal Robots, and NVIDIA](https://www.skild.ai/blogs/reindustrial-revolution) - Skild AI, 2026-03-19, 1차, (en) (reference/competitors--skild-abb-ur-foxconn.md)
15. [Gemini Robotics 2 brings whole body intelligence to robots](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/) - Google DeepMind, 2026-07-30, 1차, (en) (reference/competitors--deepmind-gemini-robotics-2.md)
16. [Gemini Robotics: Bringing AI into the Physical World](https://arxiv.org/abs/2503.20020) - arXiv, 2025-03-25, 논문, (en) (reference/papers--gemini-robotics.md)
17. [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734) - arXiv, 2025-03-18, 논문, (en) (reference/papers--groot-n1.md)
18. [NVIDIA Releases New Physical AI Models as Global Partners Unveil Next-Generation Robots](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Releases-New-Physical-AI-Models-as-Global-Partners-Unveil-Next-Generation-Robots/default.aspx) - NVIDIA, 2026-01-05, 1차, (en) (reference/competitors--nvidia-physical-ai-2026-01.md)
19. [NVIDIA Isaac GR00T N1.7](https://huggingface.co/blog/nvidia/gr00t-n1-7) - Hugging Face(NVIDIA), 2026-04-17, 1차, (en) (reference/competitors--nvidia-groot-n17.md)
20. [Seoul Purpose: How NVIDIA and South Korea Are Building the Future of AI](https://blogs.nvidia.com/blog/korea-ecosystem-2026/) - NVIDIA 블로그, 2026-06, 1차, (en) (reference/competitors--nvidia-korea-2026.md)
21. [RLWRLD/RLDX-1](https://github.com/RLWRLD/RLDX-1) - GitHub, 2026-05-06, 1차, (en) (reference/company--github-rldx1.md)
22. [Tesla Optimus Production Hit Two Walls](https://www.techtimes.com/articles/328097/20260928/tesla-optimus-production-hit-two-walls-robot-hands-it-cannot-build-workers-it-cannot-train.htm) - Tech Times, 2026-09-28, 기사(단일 소스), (en) (reference/competitors--tesla-optimus-sep2026.md)
23. [Tesla Filed a Patent for the Optimus V3 Hand, Then Elon Musk Said It 'Didn't Actually Work'](https://wetalktesla.com/2026/04/20/tesla-filed-patent-optimus-v3-hand-then-elon/) - We Talk Tesla, 2026-04-20, 기사(블로그), (en) (reference/hardware--wetalktesla-optimus-hand.md, A4 저장본)
24. [Tesla pushes Optimus V3 reveal later this year - again](https://electrek.co/2026/04/22/tesla-optimus-production-fremont-model-sx-line/) - Electrek, 2026-04-22, 기사, (en) (reference/competitors--tesla-q1-2026-earnings.md)
25. [Samsung Accelerates In-House Humanoid Development](https://www.humanoidsdaily.com/news/samsung-accelerates-in-house-humanoid-development-with-dedicated-rx-unit-and-world-model-ai) - Humanoids Daily(ZDNet Korea 재인용), 2026-08-17, 기사(2차), (en) (reference/competitors--samsung-rx-humanoid.md)
26. [EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data](https://arxiv.org/abs/2602.16710) - arXiv, 2026-02-18, 논문, (en) (reference/papers--egoscale.md)
27. [KDDIとRLWRLD、フィジカルAI基盤モデル開発で連携強化](https://ai.watch.impress.co.jp/docs/news/2142380.html) - AI Watch, 2026-09-18, 기사, (ja) (reference/company--impress-kddi-geniac.md)
28. [한국형 피지컬 AI 시동...LG전자 '월드모델'-KT '로봇모델' 개발한다](https://www.etnews.com/20260508000229) - 전자신문, 2026-05, 기사, (ko) (reference/competitors--korea-msit-physical-ai-lg-kt.md)
29. ["피지컬 AI 전장 확대...RFM 주도권 경쟁 본격화"](https://news.nate.com/view/20260531n08368) - 네이트 뉴스, 2026-05-31, 기사(원출처 이데일리, 요약마다 회사 표기 상이), (ko) (reference/competitors--nate-rfm-korea-landscape.md)
- [S1] [Boston Dynamics and Google DeepMind partner (CES 2026)](https://www.digitimes.com/news/a20260106VL212/boston-dynamics-google-deepmind-gemini-partnership-humanoid-robot.html) - Digitimes, 2026-01-06, 기사, (en). 검색 결과 요약만 확인, 원문 미열람이라 reference 미저장.
