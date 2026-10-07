# 직접 확인이 필요한 항목

작성일: 2026-10-07
에이전트가 공개 웹에서 확인하지 못한 항목을 **어떻게 구할 수 있는지** 기준으로 정리했다. 각 문서의 "확인하지 못한 항목"을 모은 것이다.

- **우선순위:** ★★★ 제안서(B4)나 면접의 핵심 주장에 직접 영향 / ★★ 수치 정확도에 영향 / ★ 참고
- **확인 후:** 결과를 `reference/`에 저장하거나 메인 세션에 알려 주면 해당 문서에 반영한다.

## 0. 먼저 볼 것 (상위 10개)
| # | 항목 | 왜 중요한가 | 방법 |
|---|------|-------------|------|
| 1 | ★★★ 덱스벤치 18개 과제 목록 (dexbench.org) | B4 8.3절 평가 과제를 RLWRLD 표준에 맞추는 근거 | 공개 사이트. 브라우저로 열어 보거나 "dexbench 읽어 줘"라고 요청 (에이전트가 아직 안 열었을 뿐) |
| 2 | ★★★ Skild × 住友電装 하네스 프로젝트 범위·결과, 사용하는 손 하드웨어 | B4 4장 경쟁 지형의 핵심 근거 | 住友電装 보도자료(일본어), Skild 블로그·뉴스룸, 업계 지인 |
| 3 | ★★★ 국내 하네스 라인의 실제 인원, 교대, 택트, 품번 수 | B2·B4의 경제성 전제(지금은 모로코 참고 라인) | 현직자 인터뷰, 공장 견학, 업계 협회. 공개 자료는 거의 없음 |
| 4 | ★★★ RLWRLD RX·PoC의 기간·가격·성공 기준, 파트너십 수익 배분·데이터권 | B4 7장 도입 구조의 전제 | 공개되지 않음. 면접에서 질문하거나 회사 문의 |
| 5 | ★★★ RLDX-1의 산업용 협동로봇(UR 등) 이식 시 재학습 규모, 상용 라이선스 조건 | B4 5.2절 셀 구성의 전제 | Hugging Face 모델 카드·라이선스 원문(공개), 나머지는 회사 문의 |
| 6 | ★★ 다관절 손·그리퍼·센서 공식 견적 (Tesollo DG-5F-S, Robotiq Hand-E, XELA uSkin, F/T 센서) | B3 ROI 투자비 (지금은 리셀러·DB 표기가) | 제조사 견적 요청 (학생·연구 목적 문의 가능) |
| 7 | ★★ 하네스 생산직 임금, 2026년 사업주 4대보험 요율 원문 | B3 인건비 (지금은 추정 18%) | 4대보험 요율은 근로복지공단·국민연금공단 공개. 업종 임금은 고용노동부 고용형태별근로실태조사 |
| 8 | ★★ 2020년 중기부 하네스 리쇼어링 자동화 지원 사업이 지금도 있는가 | B4 10장 RLWRLD 준비 사항 | 기업마당(bizinfo.go.kr), 중기부 문의 |
| 9 | ★★ 住友의 자동화율 15%·50%가 공수 기준인지 공정 수 기준인지 | B2·B4 2장 인용 | 住友電工·住友電装 일본어 IR·기술 자료 원문 |
| 10 | ★★ Physical Intelligence 파트너 페이지 원문 | A8 PI 사업 구조 | 사이트가 봇 요청을 429로 막음. 브라우저에서는 열림 → Chrome으로 읽기 요청 가능 |

## 1. 접근 권한만 있으면 바로 확인 가능 (로그인, 유료, 봇 차단)
| 항목 | 막힌 이유 | 해결 방법 | 관련 문서 |
|------|-----------|-----------|-----------|
| ★★ PI 파트너 페이지 (pi.website/blog/partner) | 429 (봇 차단) | 브라우저로 열기. Chrome 연동으로 읽기 요청 가능 | research/skild-pi-deep-dive.md, rx-cases.md |
| ★★ 하네스 수작업 85~90% 원문, 협동로봇 하네스 리뷰 (ScienceDirect, MDPI) | 403 | 학교 도서관 프록시·계정으로 PDF 다운로드 후 전달 | research/market.md, case/candidates.md |
| ★★ 일본 물류 수송능력 34.1% 부족 (METI PDF) | 403 | 브라우저로 PDF 직접 다운로드 | research/market.md |
| ★ IFR World Robotics 산업별 설치 대수 | 유료 리포트 | 학교 구독 여부 확인, 또는 보도자료 수준으로 유지 | research/market.md |
| ★ 日経 xTECH 川崎重工·FANUC·安川電機 VTLA 기사 유료 구간 | 유료 | 日経 구독 또는 학교 DB | research/papers.md, hardware.md |
| ★ Skild ARR 기사 (Bloomberg) | 유료 | 이미 Humanoids Daily 원문으로 대체함. 필요 시 Bloomberg 접근 | research/skild-pi-deep-dive.md |
| ★ Figure 소송, Sanctuary 감원, Walmart-Bossa Nova (techspot, axios) | 403 | 브라우저로 열기 | research/poc-playbook.md 6절 |
| ★ Mujin 사례 (monoist) | 문자 깨짐 | 브라우저로 열어 텍스트 복사 | research/poc-playbook.md 7.1절 |
| ★ RLDX-1 블로그·논문의 그림 속 수치 (OpenArm 결과, 데이터 혼합 비율, Physics 모듈 끈 결과) | 그림으로만 제시 | 그림을 보고 수치 읽기 (이미지 전달 시 분석 가능) | research/rldx1-tech.md |

## 2. 공개 1차 자료를 직접 찾으면 되는 것
| 항목 | 어디서 | 관련 문서 |
|------|--------|-----------|
| ★★★ RLDX-1 상용 라이선스 원문 (RLWRLD Model License v1.0) | Hugging Face 모델 페이지, GitHub LICENSE | research/company.md 4절 |
| ★★ 국내 하네스 3사(유라코퍼레이션, 경신, 티에이치엔)의 2022년 이후 생산 거점, 경신 국내 사업장 4곳의 역할 | DART 사업보고서(상장사일 경우), 회사 홈페이지, 지역 언론 | case/analysis.md 0절 |
| ★★ CJ대한통운-RLWRLD PoC 결과, 레인보우로보틱스 협업 종료 사유 | CJ대한통운 보도자료·IR, 업계 기사 | research/poc-playbook.md 7.2절 |
| ★★ Cellios + TE 셀 가격과 품번 전환 시간, クラボウ 패키지 판매 실적 | 회사 보도자료, 전시회 자료, 문의 | case/analysis.md 1.2절 |
| ★★ Agility RaaS 요금(월 8,500달러 설), Mercado Libre·Toyota 계약 | Agility 보도자료, The Robot Report 원문 | research/poc-playbook.md 5절 |
| ★ 정부 숙련 데이터 디지털화 사업의 정확한 사업명과 규모 | 과기정통부·산업부 보도자료 | research/company.md, market.md |
| ★ KDDI·Lawson 진열 PoC가 계획인지 완료인지, 연도 | KDDI·Lawson 보도자료(일본어) | research/company.md 5절 |
| ★ 리크루트웍스 2040 직종별 표 원문 | Recruit Works Institute 보고서 PDF | research/market.md |
| ★ GR00T N1.7 라이선스 조항 원문 | NVIDIA GitHub·Hugging Face | research/competitors.md |
| ★ π0, π0.5, GR00T N1.6이 촉각·힘 입력을 쓰는지 | 각 논문 본문 | research/competitors.md, knowledge.md |

## 3. 공개되지 않아 사람에게 물어야 하는 것
| 항목 | 누구에게 | 비고 |
|------|----------|------|
| ★★★ RLWRLD RX 진단의 기간·비용, PoC 성공 기준 수치, RaaS 운영 여부 | RLWRLD (면접 질문으로 적합) | B4 7·8장 |
| ★★★ 파트너십 수익 배분, 데이터 사용권, 상용 라이선스 계약 구조 | RLWRLD | B4 7장 |
| ★★ 산업용 팔 이식 시 재학습 규모, 하네스·케이블 작업 내부 평가 | RLWRLD 기술팀 | B4 5.2절 |
| ★★ 국내 하네스 라인 운영 수치, 생산직 임금, 외국인 비중 | 하네스 업계 현직자, 협회, 공장 견학 | B2·B3 |
| ★ 다관절 손 연속 가동 신뢰성(MTBF) 현장 데이터 | 손 제조사(Tesollo, Wonik 등) | hardware.md |
| ★ Skild·Samsung·LG 투자 주체(본체 대 벤처 법인) | 공시·보도자료, 필요하면 문의 | competitors.md |

## 4. 실무자 판단이 필요한 것 (리서치로 풀리지 않음)
| 항목 | 위치 |
|------|------|
| B4 KPI 제안값(목표·통과·중단)과 통과 판정 방식(점추정 대 신뢰구간 하한) | case/b4-proposal.md 8.3절 |
| 가상 고객 K사 설정을 유지할지, 실제 기업명을 예시로 쓸지 | case/b4-proposal.md 표지 |
| B2·A10 fact-check를 언제 할지 (B3 착수 전 권장) | plan.md |
| `case/deck-storyline.md`, 빈 Slides 아티팩트 삭제 여부 | - |

## 메인 세션이 대신 할 수 있는 것
- **공개 페이지인데 아직 안 연 것** (dexbench.org, Hugging Face 라이선스, GitHub): 요청하면 researcher가 바로 확인한다.
- **봇 차단 페이지** (pi.website, techspot, axios): 사용자의 Chrome으로 열어 읽을 수 있다 (Chrome 연동 필요).
- **PDF·이미지**: 다운로드한 파일을 전달하면 원문 텍스트로 저장해 분석한다.
