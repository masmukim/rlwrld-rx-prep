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
| B1 | 후보 공정 3~5개 점수화 및 선정 | case-analyst | 완료 | A1, A4, A5 | case/candidates.md |
| B2 | 선정 공정 심층 분석 (fact-check는 독립 세션에서 별도 진행) | case-analyst | 완료 | B1 | case/analysis.md |
| B3 | ROI 모델 (가정, 계산, 민감도 시트) (사용자 지시로 보류) | - | 보류(사용자 지시, B2 fact-check 후 진행) | B2 | case/roi.xlsx |
| B4 | 케이스 제안서 (md 문서로 작성, 장표는 만들지 않음. ROI 장은 B3 후 교체) | main | 진행중 | B2, B3 | case/b4-proposal.md |
