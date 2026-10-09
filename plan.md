# 작업 계획

| ID | 작업 | 담당 | 상태 | 선행 작업 | 산출물 |
|----|------|------|------|-----------|--------|
| A1 | RLWRLD 회사 리서치 (회사, 투자, 인물, RLDX-1) | researcher | 완료 | - | research/company.md |
| A2 | 기술 리서치 (RFM/VLA, 모방학습, 텔레오퍼레이션, 데이터 수집) | researcher | 완료 | - | research/tech.md |
| A3 | 경쟁사 비교표 | researcher | 완료 | A2 | research/competitors.md |
| A4 | 하드웨어·센서 동향 (로봇 손, 그리퍼, 촉각·비전 센서) | researcher | 완료 | A2 | research/hardware.md |
| A5 | 시장 리서치 (산업별 자동화 수요, 인력난, 시장 규모) | researcher | 완료 | - | research/market.md |
| A6 | 논문 리서치 (VLA, 로봇 손 조작, 촉각, 산업 적용 사례) | researcher | 완료 | A2 | research/papers.md |
| A7 | RLWRLD RX 방식과 해외 선도기업 도입 사례 | main | 완료 | A1 | research/rx-cases.md |
| A8 | Skild AI, Physical Intelligence 심층 분석 | main | 완료 | A3, A7 | research/skild-pi-deep-dive.md |
| A10 | (fact-check 미실시, 사용자 지시) 선도기업 PoC→배포 프로세스 심층: 9개사(rx-cases.md)의 단계 구분, 기간, KPI, 성공 기준, 계약·가격 구조, 실패·중단 사례 + 일본(Mujin, Telexistence)·한국 사례 보강 + RLWRLD PoC 설계 체크리스트. 입력: research/rx-cases.md, research/skild-pi-deep-dive.md (이미 조사한 내용은 다시 조사하지 말고 깊이를 더할 것) | researcher | 완료 | A7 | research/poc-playbook.md |
| A11 | RLDX-1 공식 기술 블로그 분석 (https://www.rlwrld.ai/ko/insight/blog/14, 원문 저장됨: reference/raw/company--rlwrld-blog-14.txt): 아키텍처, 학습 단계, 데이터, 벤치마크·평가 조건, 하드웨어, 한계, 경쟁 모델 대비 주장, RX·하네스 케이스 시사점. 기존 research/company.md 4절·tech.md와 다른 점과 정정할 점 표시. fact-check 생략(사용자 지시) | researcher | 완료 | A1 | research/rldx1-tech.md |
| B1 | 후보 공정 3~5개 점수화 및 선정 | case-analyst | 완료 | A1, A4, A5 | case/candidates.md |
| B2 | 선정 공정 심층 분석 (fact-check는 독립 세션에서 별도 진행) | case-analyst | 완료 | B1 | case/analysis.md |
| B3 | ROI 모델 (가정, 계산, 민감도 시트) (사용자 지시로 보류) | - | 보류(사용자 지시, B2 fact-check 후 진행) | B2 | case/roi.xlsx |
| B4 | 케이스 제안서 (md 문서로 작성, 장표는 만들지 않음. ROI 장은 B3 후 교체) | main | 진행중 | B2, B3 | case/b4-proposal.md |
| Q1 | (fact-check 미실시, 사용자 지시) 국내 하네스 조립 라인의 실제 인원, 교대, 택트, 품번 수, 외국인 비중 (경신 국내 4개 사업장이 조립 라인인지 포함). 접근 불가·유료·내부 자료는 사용자 피딩 요청 목록으로 정리 | researcher | 완료 | B2 | research/q1-harness-line-facts.md |
| Q2 | (fact-check 미실시, 사용자 지시) Skild AI × 住友電装 하네스 프로젝트의 범위·결과·손 하드웨어 (다관절 손인가 그리퍼인가). 접근 불가 자료는 사용자 피딩 요청 목록으로 정리 | researcher | 완료 | A8, B2 | research/q2-skild-sumitomo-harness.md |
| Q4 | 타사 RFM·휴머노이드 기업(Figure, Skild, PI, Agility, Dexterity, Telexistence, Mujin 등)의 고객 심층 분석(고객 유형, 선정 이유, 계약 구조, 투자자=고객 여부) → 고객 선정 패턴 도출 → 한국·아시아 잠재 고객 후보 분석. case/candidates.md에 새 절로 추가 (기존 B1 결정은 유지) | case-analyst | 진행중 | A7, A8, A10, B1 | case/candidates.md |
| Q3 | (fact-check 미실시, 사용자 지시) 住友電工·電装의 하네스 자동화율 약 15%와 약 50%의 정의(공수 기준 대 공정 수 기준)와 1차 소스. 접근 불가 자료는 사용자 피딩 요청 목록으로 정리 | researcher | 완료 | B2 | research/q3-sumitomo-automation-rate.md |
