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
| PoC | Proof of Concept | 고객 현장에서 기술 적용 가능성을 검증하는 시범 프로젝트 | reference/company--rx-intern-posting.md |
| MSAT | Multi-Stream Action Transformer | RLDX-1 아키텍처. MM-DiT를 행동 모델링으로 확장해 모달리티별 스트림을 joint self-attention으로 결합 | reference/papers--rldx1-tech-report.md |
| ALLEX | ALLEX humanoid (WIRobotics) | 48-DoF 휴머노이드, 양손 각 15-DoF. RLDX-1 주 실험 플랫폼 | reference/company--rlwrld-rldx1-page.md |
| GENIAC | Generative AI Accelerator Challenge | 일본 경제산업성의 생성AI 개발 지원 프로그램. KDDI와 RLWRLD 채택 | reference/company--impress-kddi-geniac.md |
| 에고센트릭 데이터 | Egocentric data | 작업자가 착용한 카메라로 찍은 1인칭 작업 영상 데이터 | reference/company--aws-blog-rlwrld.md |

## 핵심 인사이트
(작업이 끝날 때마다 추가. 형식: `- 인사이트 [근거]`)
- RX는 영업 접점이자 데이터 확보 채널이다. 회사는 해자를 "모델이 아니라 현장 데이터와 적용 엔지니어링"으로 설명한다 [reference/company--tech42-rx-model.md]
- "투자자 = 고객"으로 확인된 곳은 롯데호텔, CJ대한통운, KDDI/Lawson뿐이다. LG, SK, ANA, Mitsui 등은 투자 관계만 확인된다 [research/company.md 5절]
- 롯데호텔의 "30~40% 대체 가능"은 연회 백오피스에 한정된 관계자 발언이다. ROI 자동화율 수치의 근거로 쓰지 말고 "100%는 아니다"라는 정성 근거로만 쓴다 [reference/company--irobotnews-lotte-hotel.md]
- RLDX-1 벤치마크(ALLEX 86.8% vs 약 40%)는 자체 평가다. 2차 기사에는 수치 오류가 잦으므로(약 90% vs 30% 미만, 시드1 2,100만 달러 등) 1차 소스(보도자료, arXiv, GitHub)와 대조한다 [reference/papers--rldx1-tech-report.md]
- 에고센트릭 인간 영상은 규모와 성능 사이에 log-linear 스케일링이 보고됐다(EgoScale, 20,854시간, 22-DoF 손). 고객 작업자 착용 카메라로 데이터를 모으는 RX 전략의 학술 근거다. "54% 향상"은 기준선 대비이며 상대/%p 구분은 미확인 [reference/papers--egoscale.md]
- 공개된 최고 성공률은 80~90%대에 몰려 있다(ACT, 공유 자율, RLDX-1). 평가 조건이 서로 달라 ROI의 현장 가동률 근거로 쓰지 않는다 [research/tech.md 5절]
- 강화학습·교정 개입 결합(π*0.6, 일본 언론 전망)이 다음 흐름인데, RLDX-1 공개 학습 설명에는 RL 단계가 확인되지 않는다. A3 경쟁 비교 포인트다 [reference/papers--pistar06-recap.md, reference/tech--xtech-il-rl.md]
- arXiv 초록의 "N% 향상"은 상대인지 %p인지 구분되지 않는 경우가 많다. 본문 확인 전에는 "기준선 대비"까지만 쓴다 [A2 fact-check]

## 열린 질문
다음 리서치 후보. `/rx-status`가 이 목록을 보고 새 작업을 제안한다.
(형식: `- [ ] 질문 (발견한 작업 ID)`, 해결하면 `- [x]`로 바꾸고 답이 있는 파일을 적는다)
- [ ] RLDX-1 가중치의 비상업 라이선스(RLWRLD Model License v1.0) 아래에서 상용 PoC를 어떻게 계약하는가? (A1)
- [ ] RLWRLD의 공개 고객 중 제조업(자동차, 전자) 사례가 있는가? (A1)
- [ ] RLDX-1 벤치마크를 독립적으로 검증한 결과가 있는가? (A1, A3에서 확인)
- [ ] 정부 숙련 데이터 디지털화 사업(기사 표기 약 3,300만 달러)의 정확한 사업명과 규모는? (A1, A5에서 확인)
- [ ] Lawson 진열 PoC는 계획인가 완료인가, 연도는 언제인가? CJ대한통운 MOU(2025-11)의 1차 소스는 무엇인가? (A1)
- [ ] RLDX-1 학습에 RL이나 현장 교정 루프가 있는가? ALLEX 실세계 평가는 몇 개 작업, 몇 회 시행인가? 논문 본문 확인 필요 (A2)
- [ ] 텔레오퍼레이션 "하루 50~200 시연"과 시스템 통합 비용 "하드웨어의 50~200%"의 1차 소스는? B3 ROI 가정에 필요 (A2)
- [ ] π0, π0.5, GR00T N1.6은 촉각·힘 입력을 쓰는가? RLDX-1 차별성 판단에 필요 (A2, A3에서 확인)
- [ ] EgoScale의 +54%는 상대 향상인가 %p 향상인가? KDDI "연 3,500시간 상당"의 단위는? (A2)
