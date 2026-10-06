# 도메인 지식 노트

RX 팀이 작업하면서 배운 산업 지식을 쌓는 파일이다. 모든 에이전트가 작업 시작 전에 읽는다.
수정은 메인 에이전트만 한다 (`/rx-done`에서 서브에이전트가 반환한 "새로 배운 것"을 반영).
각 항목 끝에는 근거 reference 파일이나 작업 ID를 적는다.

## 용어집
| 용어 | 영어 | 뜻 | 근거 |
|------|------|----|------|
| RFM | Robotics Foundation Model | 다양한 로봇과 작업에 범용으로 쓰는 대규모 로봇 AI 모델 | reference/company--rx-intern-posting.md |
| RX | Robotics Transformation | RFM을 고객 현장에 도입시키는 RLWRLD의 사업 부문 | reference/company--rx-intern-posting.md |
| VLA | Vision-Language-Action model | 영상과 언어 지시를 받아 로봇 동작을 출력하는 모델 | (A2에서 보강) |
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

## 열린 질문
다음 리서치 후보. `/rx-status`가 이 목록을 보고 새 작업을 제안한다.
(형식: `- [ ] 질문 (발견한 작업 ID)`, 해결하면 `- [x]`로 바꾸고 답이 있는 파일을 적는다)
- [ ] RLDX-1 가중치의 비상업 라이선스(RLWRLD Model License v1.0) 아래에서 상용 PoC를 어떻게 계약하는가? (A1)
- [ ] RLWRLD의 공개 고객 중 제조업(자동차, 전자) 사례가 있는가? (A1)
- [ ] RLDX-1 벤치마크를 독립적으로 검증한 결과가 있는가? (A1, A3에서 확인)
- [ ] 정부 숙련 데이터 디지털화 사업(기사 표기 약 3,300만 달러)의 정확한 사업명과 규모는? (A1, A5에서 확인)
- [ ] Lawson 진열 PoC는 계획인가 완료인가, 연도는 언제인가? CJ대한통운 MOU(2025-11)의 1차 소스는 무엇인가? (A1)
