# 하드웨어·센서 동향: 로봇 손, 그리퍼, 촉각·비전 센서
조사일: 2026-10-06

## 핵심 요약
- **손 가격은 자유도(DoF)와 비례하지 않고 공급 국가·용도별로 층이 갈린다.** 공개 가격 기준으로 6-DoF Inspire 계열은 리셀러·구성별 표기 약 $4,500~10,500 이상(원문 미열람 포함, 공식 스토어 표기 $24,399.99는 구성 미확인으로 충돌) [3], 20-DoF 한국 Tesollo DG-5F-S는 제품 DB 표기 $23,000(공식가 미확인, `추정`) [4], 22-DoF Sharpa Wave는 약 $50,000(2차 소스, `추정`), Shadow Dexterous Hand는 소스별 약 60,000 EUR, 65,000~110,000 USD(`추정`)이다. 20 DoF급 손끼리도 Allegro V6 F 약 $15,000(`추정`) 대 Shadow 약 65,000~110,000 USD(`추정`)로 약 4~7배 벌어진다(본 문서 계산, 대부분 공식가 미확인).
- **내구성 수치는 제조사 자체 시험이거나 연구용 규모에 그친다.** Sharpa Wave 250만 회 press 시험(자체) [1], Robotiq Hand-E 보증 500만 사이클(평행 그리퍼) [17], ORCA 손은 10,000회·약 20시간 무고장(연구 프로토타입) [10]. 다관절 손의 현장 연속 가동 검증은 확인하지 못했고, 학계 서베이도 센서 내구성과 제조 확장성을 미해결 과제로 꼽는다 [12].
- **제조·물류의 단순 pick-and-place에는 평행 그리퍼와 3D 카메라가 이미 성숙했고, 다관절 손과 촉각이 의미 있는 영역은 소형 부품·유연체·조립이다.** 일본 FA 3사(川崎重工, FANUC, Yaskawa)가 촉각을 넣은 VTLA 모델과 "視触覚" 핸드를 NEDO 지원(최대 20억 엔)으로 개발 중이며 [13], 한·일 부품사(Tesollo, Wonik, XELA, FingerVision)도 손+촉각 조합을 내놓고 있다 [4][5][14][15]. 본 문서의 적합성 판단은 공개 사양에 근거한 해석이며 현장 검증은 아니다.

## 본문

### 1. 고자유도 로봇 손 비교

가격은 USD, 조사일(2026-10) 기준 공개 표기다. "신뢰도"는 가격 출처의 성격이다. 판매 구성(좌/우, 손목, 센서 옵션)이 달라 직접 비교용이 아니라 층 구분용이다.

| 제품 | 제조사(국가) | DoF | 무게 | 촉각·센서 | 가격(USD) | 내구성 정보 | 가격 신뢰도·출처 |
|------|--------------|-----|------|-----------|-----------|-------------|------------------|
| Shadow Dexterous Hand | Shadow Robot (영국) | 20 actuated + 4 under-actuated, 총 24 joints | 4.3 kg | 센서 100개 이상(1 kHz), Tactile Fingertip 표준 2개(최대 5), 텐던 부하 센서 40개 | 약 60,000 EUR, 65,000~110,000 USD(소스별 상이) | 미확인 | 낮음(검색 요약, 원문 미열람, `추정`). 사양 [2] |
| Sharpa Wave | Sharpa (싱가포르, 검색 요약 기준) | 22 | 1.3 kg | 손끝 촉각 240x240 px(standard), 힘 0~30 N, 180 fps, 지연 20 ms | 약 50,000 | 250만 회 press, 30 g 충격 3,200회, 연속 1,000시간 이상(공식 페이지에 온도 사이클 시험 항목으로 표기, 원문 재확인 필요). 전부 자체 시험 | 낮음(2차, `추정`). 사양 [1] |
| Allegro Hand V4 | Wonik Robotics (한국) | 16 (4지) | 미확인 | 기본 없음. DIGIT 360 통합 발표 [8] | 약 15,000~24,500 | 미확인 | 낮음(검색 요약, `추정`) |
| Allegro Hand V6 F | Wonik Robotics (한국) | 20 (5지) | 미확인 | 손끝, 마디, 손바닥 압력 센서, 손끝 LED | 약 15,000(미국 판매) | 미확인 | 낮음(검색 요약, `추정`). 사양 [5] |
| DG-5F-S | Tesollo (한국) | 20 (5지) | 0.88 kg | 촉각·힘 센서 포함 표기. XELA uSkin 통합판 있음 [15] | 23,000(`추정`) | 미확인 | 낮음~중간(제품 DB 표기, 공식가 미확인). [4] |
| RH56DFX 등 RH56 계열 | Inspire Robots (중국) | 6 DoF, 모터 조인트 12 | 약 540 g(검색 요약) | 압력 센서 6개 | 리셀러·구성별 약 4,500~10,500 이상 vs 공식 스토어 표기 24,399.99(구성 미확인) | 미확인 | **충돌**. 아래 설명 [3] |
| Linker Hand L30 | Linkerbot (중국) | 21(표기) | 미확인 | 미확인 | 약 14,000~20,000 | 미확인 | 낮음(검색 요약, `추정`) |
| DexH13 | PaXini (중국) | 16 (4지) | 미확인 | 촉각 센서 1,140개, 손에 8MP 카메라(검색 요약) | 약 17,200~29,700 | 미확인 | 낮음(검색 요약, `추정`) |
| ORCA | ETH Zurich (스위스, 오픈소스) | 17 (텐던) | 미확인 | 촉각 센서 통합 | 재료비 2,000 CHF 미만 | 10,000회(약 20시간) 무고장 | 높음(논문). [10] |
| Figure 03 손 | Figure AI (미국) | 미확인 | 미확인 | 손끝 촉각(3 g 힘 검출), 손바닥 카메라 | 단품 판매 아님 | 미확인 | 기사. [6] |
| Optimus 손 | Tesla (미국) | 특허 설계와 Tech Times(단일 소스)는 22 DoF, 액추에이터 25개(Tech Times 서술). 현행 사양 미확정 | 미확인 | 미확인 | 단품 판매 아님 | 미확인 | 아래 설명 [7][20] |

**해석 포인트**
- **Inspire 가격 충돌.** 공식 스토어 페이지는 RH56DFX를 $24,399.99로 표기한다 [3]. 반면 리셀러는 RH56 계열을 $4,500~10,500 이상으로 적는다(검색 요약 기준 Knoxlabs·usrobotstore 등 $4,500~9,250, Robotics Center·Toborlife $10,500은 코디네이터 확인분, 모두 원문 미열람 또는 구성별 가격). 공식 $24,399.99가 좌/우/양손, 손목 옵션 중 어느 구성인지 확인하지 못해 둘 다 적고 결론을 내리지 않는다. 다만 Inspire는 6 DoF(조인트 12개)로 손가락 개별 제어가 제한된다는 점에서 20-DoF 이상 손과 같은 범주가 아니다 [3].
- **중국산 손의 가격대.** 한 구매 가이드(sourcebotics.com, 검색 요약, 원문 미열람)는 중국산 다관절 손이 $1,400~15,000 이상, 서구 동급은 $45,000~300,000이라고 적는다. 신뢰도가 낮아 참고치로만 둔다.
- **RLWRLD와의 연결.** RLDX-1은 ALLEX(손 15-DoF), Franka Research 3, OpenArm + Inspire 손에서 학습되었다고 공식 페이지에 나온다 [19] (research/tech.md 4절). 고객 PoC에서 손 선택이 모델 재학습을 얼마나 요구하는지는 확인하지 못했다.
- **Tesla Optimus 손.** 특허가 공개한 설계는 텐던 구동, 22 DoF, 액추에이터를 전완에 둔 구조라고 기사는 서술한다 [7]. Musk는 2026-04-19 X에서 "We already changed the design. This one didn't actually work."라고 말했다(기사 해석: 이 22-DoF 특허 설계를 가리킴) [7]. 반면 2026-09-28 Tech Times는 V3 손을 텐던 구동 22 DoF, 전완 액추에이터 25개로 서술하고 Fremont 라인의 V3 유닛 상당수가 재작업이 필요하다고 전한다(단일 기사 서술, 1차 미확인) [20]. 두 소스가 충돌하고 각각 단일 소스이므로 현행 손 사양은 미확정이다. 손이 로봇 전체 엔지니어링 난이도의 약 60%라는 서술은 기사의 의역이다 [7].
- **Figure 03 손.** 손끝 촉각 센서가 3 g의 힘을 검출하고 손바닥 카메라가 가림 상황에서 근접 시각을 제공하며, 손을 "manufacturability and cost in mind"로 재설계했다고 한다 [6]. DoF와 payload는 확인하지 못했다.
- **Sharpa Wave 사양 주의.** 공식 페이지는 payload 40 kg(standard) / 24 kg(alternate)로 적지만 1.3 kg 손의 파지력 150 N(약 15 kgf)과 조건이 정합한지 알 수 없다(마찰·형상 조건 미표기) [1]. 2차 소스는 "손끝당 1,000개 이상 tactile pixel"이라 적어 공식(240x240)과 다르다. 공식 쪽을 택했다.

### 2. 산업용 그리퍼 (엔드이펙터)

| 유형 | 대표 | 대표 사양 | 가격(검색 요약, `추정`) | 제조·물류 적용성 (본 문서 해석) |
|------|------|-----------|--------------------------|--------------------------------|
| 평행 전동 그리퍼 | Robotiq Hand-E | 스트로크 50/100 mm, payload 7 kg, 파지력 20~185 N, 반복 정밀도 0.025 mm, IP67, 보증 500만 사이클 [17] | Hand-E 약 $7,250 | 형상이 정해진 부품 반복 파지, 머신 텐딩에 적합. 손가락 개별 제어 없음 |
| 적응형 2지 | Robotiq 2F-85/2F-140 | 페이지에서 사양 미확인 | 2F-85 약 $5,825 | 형상 변화가 있는 박스·부품 파지. 호환 로봇 목록은 Hand-E 페이지 기준(UR, FANUC CRX, Doosan, Hanwha, Yaskawa 등)이며 2F-85/2F-140 호환성은 미확인 [17] |
| 협동로봇용 번들 | OnRobot, Schunk 등 | 2FG7 payload 약 11 kg 등(검색 요약) | OnRobot $989~14,806, Schunk EGP/EGH $3,000~6,000+ | 단순 반복 작업의 사실상 표준. 미열람 소스 |
| 진공·특수 | 진공 그리퍼 등 | 미조사 | 미조사 | 박스 물류 piece picking. 이번 조사 범위 밖 |

- 가격 비교(본 문서 계산, `추정`): DG-5F-S $23,000(제품 DB 표기, 공식가 미확인) [4]를 평행 그리퍼 Hand-E 약 $7,250으로 나누면 약 3.2배다. 다관절 손이 정당화되려면 평행 그리퍼로 풀리지 않는 공정이어야 한다는 가설(research/tech.md 시사점)의 비용 근거가 된다. 다만 Hand-E 가격은 미열람 소스다.
- 일본·한국 그리퍼 제조사(SMC, Schmalz 계열 외, 한국 로보티스 등)는 이번 조사에서 사양과 가격을 확인하지 못했다. 열린 질문으로 남긴다.

### 3. 촉각 센서

| 센서 | 방식 | 핵심 수치 | 가격 | 비고 | 출처 |
|------|------|-----------|------|------|------|
| GelSight Mini | 광학식(겔 + 카메라, vision-based) | 640x480 RGB, 30 fps(검색 요약) | $510 | 겔 소모품. 2025-01부터 재배합 겔로 수명 개선 주장 | [9] |
| DIGIT | 광학식 | 320x240, 60 fps, 20x27x18 mm(검색 요약) | $355(검색 요약) | Meta-GelSight 협업 | 검색 요약 |
| Digit 360 | 광학식 다모달 손끝 | 7 um 특징, 법선력 1.01 mN, 약 830만 taxel, 10 kHz 진동, 온도·냄새 감지 | 미확인 | 연구용 최고 사양. Wonik Allegro에 통합 발표 | [11][8] |
| Sharpa Wave 손끝 | 광학식 추정(공식 페이지에 방식 미기재) | 240x240 px, 0.02 N 분해능, 180 fps, 지연 20 ms, 센서 수명 100,000 press 이상 | 손에 포함 | 센서 수명이 손 시험(250만 회)과 다름 | [1] |
| XELA uSkin | 3축 촉각, 손끝·마디·손바닥 분산 | 손끝당 12 sensing points, 최소 0.1 gf, 센서 21.15x25.72x22.02 mm | 미확인 | 일본. Tesollo DG-5F 통합 출하 2025 Q4 | [15] |
| FingerVision | 광학식(투명 탄성 스킨 + 카메라) | 힘 분포 x/y/z, 미끄러짐, 질감 추정. 분해능 수치 미공개 | 미확인 | 일본. FA 3사 프로젝트 파트너 | [14][13] |
| Figure 03 손끝 | 미확인 | 3 g 힘 검출 | 로봇에 포함 | 1세대 센서 | [6] |
| Allegro V6 F | 압력 센서(손끝, 마디, 손바닥) | 수치 미공개 | 손에 포함 | 접촉 위치·시점·압력 기록 | [5] |

- **방식별 구분.** 광학식은 해상도가 높고 저렴하나 겔(elastomer)이 소모품이고 손끝 크기와 두께가 제약이다. 분산형 3축 센서(XELA)는 손바닥·마디까지 덮는다. 이 구분은 센서 설명(원문 서술)에 근거한 본 문서의 정리이며 성능 우열 판단이 아니다.
- **수명.** 광학식 겔 수명 수치는 GelSight 페이지에 없다 [9]. Sharpa는 센서 수명 100,000 press 이상이라고 적는다(자체) [1]. 2026-08 서베이는 센서 내구성, 표준화, 제조 확장성을 아직 풀리지 않은 배치 장벽으로 든다 [12].
- **촉각 없이 가능한가.** WIRobotics ALLEX는 별도 촉각 센서 없이 100 gf 미세 힘을 감지한다고 발표했다(2025-08 기사 검색 요약, 원문 미열람, 회사 주장). RLDX-1은 센서가 없으면 vision-only로 성능이 저하된 채 동작한다 [19]. 따라서 촉각이 모든 PoC의 필수 사양인지는 공정별로 판단해야 한다.
- **전자피부(e-skin).** 대면적 전자피부의 상용 제품과 가격은 이번 조사에서 확인하지 못했다(XELA의 분산 배치가 가장 가까운 사례).
- **일본의 비용 인식.** 일본 xTECH(검색 요약, 원문 미열람)는 촉각 센서 탑재 핸드의 비용 문제 때문에 FA 3사가 카메라로 촉각을 측정하는 "視触覚" 방식을 택했다고 설명한다.

### 4. 비전·깊이 센서

| 제품군 | 방식 | 대표 수치 | 가격 | 용도 | 출처 |
|--------|------|-----------|------|------|------|
| Zivid 3 | 레이저 구조광 | 8 MP, 최대 800만 포인트, 트루니스 오차 0.2% 미만, 4.5 m까지 mm 수준, 촬영 500 ms | 미공개 | 팔레트 해체, bin picking, 조립, 검사. 고정 설치 | [16] |
| Intel RealSense D455 | 능동 IR 스테레오 | 1280x720 깊이, 범위 0.4~6 m, 4 m에서 오차 2% 미만 | 약 $400 | 장면 카메라 (검색 요약, 원문 403·미열람) | 검색 요약 |
| RealSense D405 | 근거리 스테레오 | 51 g, 최소 거리 7 cm | 미확인 | 손목 장착 근접 조작 (검색 요약, 공식 페이지 404) | 검색 요약 |
| Orbbec Gemini 335 | 능동 IR 스테레오 | 1280x800, 범위 0.15~5 m | 약 $250 | 장면 카메라. 반사면에서 D455보다 안정적이라는 비교(검색 요약) | 검색 요약 |

- **공급망 이벤트.** RealSense는 2025-07 Intel에서 분사하며 $50M을 조달했고 [18], 2026-09 Cognex가 현금 $500M(리텐션 등 포함 약 $600M)에 인수한다고 발표했다. 마감은 2026년 4분기 예정이다 [18]. 회사 주장으로 로봇용 깊이 카메라는 AMR·휴머노이드의 다수에 탑재(분사 시 약 60%라는 주장, 검색 요약)된다. 소유 구조 변화로 가격·로드맵이 달라질 수 있어 PoC 하드웨어 선정 시 대체 공급사(Orbbec 등)를 함께 두는 편이 안전하다(`추정`, 근거: 인수 마감 전).
- **가격 대비.** 로봇용 스테레오 카메라는 수백 달러, 산업용 구조광은 별도 견적이다. 비전 센서 비용은 손 비용(수천~수만 달러)보다 한 자릿수 작다(가격대 비교, 본 문서 해석).
- Zivid 외 Photoneo 등 구조광 경쟁사의 사양은 조사하지 못했다.

### 5. 한국·일본 제조사와 공급망

| 구분 | 기업 | 제품/활동 | 확인 수준 | 출처 |
|------|------|-----------|-----------|------|
| 한국 손 | 원익로보틱스(Wonik Robotics) | Allegro Hand V4(16 DoF) → V6 F(5지 20 DoF, 전손 압력 센싱, 크기 20% 이상 축소). 완주 공장 확장에 3,500억 원 투자 계획. Meta와 DIGIT 360 통합 협력 | 기사, 보도 | [5][8] |
| 한국 손 | 테솔로(Tesollo) | DG-5F(20 DoF, 1.4 kg, Modbus 지원은 검색 요약) / DG-5F-S(0.88 kg, $23,000). XELA uSkin 통합 | 제품 DB(DG-5F-S), 기사(XELA 통합) | [4][15] |
| 한국 휴머노이드 | 위로보틱스(WIRobotics) | ALLEX 손 15-DoF, RLDX-1 주 플랫폼 [19]. 손끝 반복정밀도 0.3 mm 이하는 한경 2025-08-18 기사 검색 요약(원문 미열람) | 공식 페이지 + 검색 요약 | [19] |
| 일본 촉각 | XELA Robotics | uSkin 3축 촉각 | 보도 | [15] |
| 일본 촉각 | FingerVision | 광학 촉각 센서, 식품·식물 공장 사례 | 공식 사이트 | [14] |
| 일본 로봇 3사 | 川崎重工, FANUC, Yaskawa | VTLA(영상-촉각-언어-행동) 모델과 視触覚 핸드 데이터셋. 2026-08~2027-07, NEDO 최대 20억 엔, 영상·촉각·동작 5,000시간 수집 | 기사 | [13] |
| 일본 연구 | Honda | 손톱 있는 4지 핸드로 캔 뚜껑(풀탭) 개봉 (검색 요약) | 검색 요약, 미열람 | 검색 요약 |

- **한·일의 구도(본 문서 해석).** 한국은 손 본체(Wonik, Tesollo)와 휴머노이드(WIRobotics), 일본은 촉각 센서(XELA, FingerVision)와 산업용 로봇 3사의 데이터·모델 개발이 강점으로 드러난다. 한국 정부는 2030년 핵심 부품 국산화율 80% 목표를 제시했다는 보도가 있다(research/market.md 정책 항목 참조, 본 조사에서 재확인하지 않음).
- **일본 FA 3사의 의미.** 일본 고객에게 RLWRLD가 제안할 때, 같은 일본 시장에서 제조 현장 데이터로 VTLA를 만드는 3사 컨소시엄과 접점·경쟁이 생긴다. 그 프로젝트는 하드웨어 비의존 데이터 생태계를 표방한다 [13]. 경쟁인지 협력 가능성인지는 판단하지 못했다. A3로 넘긴다.
- **중국 공급망.** 중국 업체(Inspire, Linkerbot, PaXini 등)가 저가·다양한 라인업을 내고 있다(검색 요약). 한 산업 분석(ARC Advisory, 검색 요약, 원문 403)은 국산 손이 단기 데모는 잘하나 연속 사이클 수명, 충격 내성, 고저온 안정성의 장기·대규모 산업 검증이 부족하다고 평가한다(미열람 요약이라 참고용).
- **부품 수준 공급망**(마이크로 모터, 감속기, 스크류 등)은 이번 조사에서 확인하지 못했다.

### 6. 공정에 맞는 end-effector 선정 프레임 (본 문서 해석, 실측 아님)

| 공정 특징 | 우선 후보 | 근거 |
|-----------|-----------|------|
| 형상 고정 부품의 반복 파지, 박스 pick-and-place | 평행·적응형 그리퍼 + 3D 카메라 | 가격 약 $5천~7천급, 보증 500만 사이클 [17], 구조광 카메라가 팔레트·bin picking에 특화 [16] |
| 형상이 다양한 물체, 부드러운 물체, 도구 사용 | 15~22 DoF 다관절 손(DG-5F-S, Allegro V6 F, ALLEX 등) | 손가락 개별 제어 필요 |
| 접촉이 많은 조립(케이블, 커넥터), 미끄러짐 민감 | 다관절 손 + 촉각(광학식 또는 분산형) | 일본 FA 3사가 "細かな部品や柔らかいケーブル"를 목표로 VTLA를 개발 [13] |
| 연속 가동 24시간, 먼지·충격 | 현재 다관절 손은 검증 부족 | 내구성 수치가 자체 시험·연구 수준 [1][10], 서베이도 내구성을 장벽으로 [12] |

## RX 관점 시사점
- **고객 제안에서:**
  - 하드웨어는 모델과 분리해 고객이 고른다는 전제로 가격·내구성·납기를 비교표로 제시한다. 공정이 평행 그리퍼로 풀리면 다관절 손은 제안하지 않는 정직함이 오히려 신뢰를 준다. 비용 근거는 손 약 3.2배(DG-5F-S 대 Hand-E, `추정`).
  - B3 ROI에 하드웨어 단가를 넣을 때 가격 범위를 "공식가 확인 후 확정"으로 두고, 신뢰도 낮은 값(Shadow, Sharpa, Allegro, 중국산)은 시나리오 변수로 둔다. 내구성은 교체 주기(손, 겔) 비용으로 반영한다. 수명 수치는 대부분 자체 시험이므로 PoC 시험 항목에 "연속 N시간 가동"을 넣는다.
  - 촉각은 "필수"가 아니라 "접촉 민감 공정의 선택 사양"으로 제안한다. RLDX-1이 vision-only로도 동작한다는 점 [19]과 ALLEX가 촉각 센서 없이 힘 반응을 주장한다는 점(미열람)이 근거다. 단, 두 주장 모두 회사 발표다.
  - 일본 고객에게는 "손 + 촉각 하드웨어는 한·일 공급망에서 조달 가능"하다는 점(Tesollo+XELA, Wonik+DIGIT 360)과 FA 3사 프로젝트의 존재를 함께 설명해야 한다.
- **고객 설명·내부 브리핑 포인트:**
  - "다관절 손은 가격이 약 6~24배 벌어지지만(Inspire 리셀러·구성별 약 $4,500~10,500 이상 대 Shadow 약 65,000~110,000 USD, 본 문서 계산, 모두 `추정`) 내구성은 자체 시험 수준이라 PoC에서 가동 시간을 직접 검증해야 한다"고 설명할 수 있다.
  - "Musk가 특허 설계는 작동하지 않았고 설계를 바꿨다고 말했지만(기사 해석: 22-DoF 설계) [7], 9월 Tech Times는 V3 손을 22 DoF로 서술해 [20] 현행 사양이 미확정이다. 손은 아직 설계가 수렴하지 않은 부품"이라고 업계 불확실성을 설명할 수 있다.
  - "RealSense가 Cognex에 인수되는 중이라 로봇 비전 공급망이 재편 중"이라는 사실로 공급망 감각을 보일 수 있다 [18].

## 확인하지 못한 항목
- Shadow, Sharpa, Allegro, Linkerbot, PaXini의 공식 가격(전부 검색 요약). Inspire 공식 스토어 가격과 리셀러 가격의 충돌 원인.
- Wonik V6 F, DG-5F-S의 payload·손끝 힘·공식 가격. DG-5F 기사 "가격 40% 더 싸게"의 기준 가격(기사 본문 미확인).
- 다관절 손의 장시간 가동 신뢰성(MTBF, 연속 가동 시간) 현장 데이터. 현재는 제조사 자체 시험과 연구 프로토타입 수치뿐.
- Tesla Optimus 현행 손 사양(Musk 4월 발언과 Tech Times 9월 서술이 충돌, 각각 단일 소스), Figure 03 손 DoF.
- 일본·한국 산업용 그리퍼 업체(SMC, Schmalz 외, 로보티스 등), Photoneo, 전자피부(대면적) 상용 제품, 마이크로 모터·감속기 등 부품 공급망.
- DIGIT 360의 실제 출시와 가격.
- 검색 요약만 본 항목: RealSense/Orbbec 사양·가격, OnRobot·Schunk 가격, ALLEX 손끝 정밀도, Honda 핸드, xTECH "視触覚" 비용 설명, ARC Advisory 평가.

## 출처
1. [Sharpa Wave](https://www.sharpa.com/pages/wave) - Sharpa, 날짜 미확인, 1차, (en) (reference/hardware--sharpa-wave-spec.md)
2. [Shadow Dexterous Hand Series](https://shadowrobot.com/dexterous-hand-series/) - Shadow Robot, 날짜 미확인, 1차, (en) (reference/hardware--shadow-dexterous-hand.md)
3. [Inspire Robots RH56DFX](https://inspire-robots.store/products/the-dexterous-hands-rh56dfx-series) - Inspire Robots 스토어, 날짜 미확인, 1차(스토어), (en) (reference/hardware--inspire-rh56dfx.md)
4. [DG-5F-S Humanoid Robotic Hand](https://humanoid.guide/product/dg-5f-s/) - humanoid.guide, 날짜 미확인, 제품 DB, (en) (reference/hardware--tesollo-dg5f-s.md)
5. [원익로보틱스, 5지 로봇핸드 '알레그로 핸드 V6 F' 출시](https://www.irobotnews.com/news/articleView.html?idxno=48266) - 로봇신문, 2026-09, 기사, (ko) (reference/hardware--irobotnews-allegro-v6f.md)
6. [Figure AI designs Figure 03 humanoid for AI, home use, and scaling](https://www.therobotreport.com/figure-ai-designs-figure-03-humanoid-ai-home-use-scaling/) - The Robot Report, 2025-10(추정), 기사, (en) (reference/hardware--therobotreport-figure03.md)
7. [Tesla Filed a Patent for the Optimus V3 Hand, Then Elon Musk Said It 'Didn't Actually Work'](https://wetalktesla.com/2026/04/20/tesla-filed-patent-optimus-v3-hand-then-elon/) - We Talk Tesla, 2026-04-20, 기사(블로그), (en) (reference/hardware--wetalktesla-optimus-hand.md)
8. [GelSight, Meta AI release Digit 360 tactile sensor for robotic fingers](https://www.therobotreport.com/gelsight-meta-ai-release-digit-360-tactile-sensor-for-robotic-fingers/) - The Robot Report, 2024-11-02, 기사, (en) (reference/hardware--therobotreport-digit360.md)
9. [GelSight Mini System](https://www.gelsight.com/product/gelsight-mini-system/) - GelSight, 날짜 미확인, 1차, (en) (reference/hardware--gelsight-mini.md)
10. [ORCA: An Open-Source, Reliable, Cost-Effective, Anthropomorphic Robotic Hand for Uninterrupted Dexterous Task Learning](https://arxiv.org/abs/2504.04259) - arXiv(IROS 2025), 2025-04-05, 논문, (en) (reference/papers--orca-hand.md)
11. [Digitizing Touch with an Artificial Multimodal Fingertip](https://arxiv.org/abs/2411.02479) - arXiv, 2024-11-04, 논문, (en) (reference/papers--digit360.md)
12. [Vision-Based Tactile Intelligence for Robotics: Sensing, Learning, and Embodied Manipulation](https://arxiv.org/abs/2608.15490) - arXiv, 2026-08-16, 논문(서베이), (en) (reference/papers--vbts-survey.md)
13. [川崎重工業、ファナック、安川電機、フィジカルAIで協業、VTLAモデル開発へ](https://www.sbbit.jp/article/st/185993) - ビジネス+IT, 2026-07 전후(미확인), 기사, (ja) (reference/hardware--sbbit-kawasaki-fanuc-yaskawa-vtla.md)
14. [FingerVision](https://www.fingervision.jp/en) - FingerVision Inc., 날짜 미확인, 1차, (en) (reference/hardware--fingervision.md)
15. [XELA Robotics adds uSkin tactile sensors to Tesollo DG-5F robot hand](https://roboticsandautomationnews.com/2025/12/04/xela-robotics-adds-high-precision-tactile-sensing-to-tesollo-robot-hand/97352/) - Robotics & Automation News, 2025-12-04, 기사, (en) (reference/hardware--xela-tesollo-integration.md)
16. [Zivid 3](https://www.zivid.com/zivid-3) - Zivid, 날짜 미확인, 1차, (en) (reference/hardware--zivid-3.md)
17. [Robotiq Hand-E adaptive gripper](https://robotiq.com/products/hand-e-adaptive-robot-gripper) - Robotiq, 날짜 미확인, 1차, (en) (reference/hardware--robotiq-hand-e.md)
18. [How RealSense went from an Intel shutdown candidate to a $600 million sale](https://www.calcalistech.com/ctechnews/article/94b0yn8vr) - Calcalist, 2026-09-23, 기사, (en) (reference/hardware--calcalist-realsense-cognex.md)
20. [Tesla Optimus Production Hit Two Walls: Robot Hands It Cannot Build, Workers It Cannot Train](https://www.techtimes.com/articles/328097/20260928/tesla-optimus-production-hit-two-walls-robot-hands-it-cannot-build-workers-it-cannot-train.htm) - Tech Times, 2026-09-28, 기사(단일 소스, 1차 미확인), (en) (reference/competitors--tesla-optimus-sep2026.md)
19. [RLDX-1 Foundation Model](https://www.rlwrld.ai/en/rldx-1) - RLWRLD 공식, 2026-05-07, 1차, (en) (reference/company--rlwrld-rldx1-page.md)

**미열람 검색 요약 참고 (본문에서 "검색 요약"으로만 사용)**: Wonik Allegro 가격 등 [knoxlabs.com Allegro V4/V6 F](https://www.knoxlabs.com/products/wonik-robotics-allegro-hand-v4), [sourcebotics.com 중국산 손 가이드](https://sourcebotics.com/guides/chinese-dexterous-hands-2026-buyers-guide/), [위로보틱스 ALLEX 한국경제](https://www.hankyung.com/article/202508186476i), [xTECH 視触覚](https://xtech.nikkei.com/atcl/nxt/column/18/03727/082400003/), [OpenCV 블로그 Orbbec/RealSense 비교(403)](https://opencv.org/blog/a-quick-comparison-of-the-orbbec-and-realsense-3d-cameras/), [ARC Advisory 중국 손 공급망(403)](https://www.arcweb.com/blog/china-humanoid-robot-dexterous-hands-localization-technology-routes-leading-suppliers).
