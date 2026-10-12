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
| A10 | (fact-check 2026-10-09 haiku 검증·정정 완료) 선도기업 PoC→배포 프로세스 심층: 9개사(rx-cases.md)의 단계 구분, 기간, KPI, 성공 기준, 계약·가격 구조, 실패·중단 사례 + 일본(Mujin, Telexistence)·한국 사례 보강 + RLWRLD PoC 설계 체크리스트. 입력: research/rx-cases.md, research/skild-pi-deep-dive.md (이미 조사한 내용은 다시 조사하지 말고 깊이를 더할 것) | researcher | 완료 | A7 | research/poc-playbook.md |
| A11 | RLDX-1 공식 기술 블로그 분석 (https://www.rlwrld.ai/ko/insight/blog/14, 원문 저장됨: reference/raw/company--rlwrld-blog-14.txt): 아키텍처, 학습 단계, 데이터, 벤치마크·평가 조건, 하드웨어, 한계, 경쟁 모델 대비 주장, RX·하네스 케이스 시사점. 기존 research/company.md 4절·tech.md와 다른 점과 정정할 점 표시. fact-check 2026-10-09 haiku 검증·정정 완료 | researcher | 완료 | A1 | research/rldx1-tech.md |
| B1 | 후보 공정 3~5개 점수화 및 선정 | case-analyst | 완료 | A1, A4, A5 | case/candidates.md |
| B2 | 선정 공정 심층 분석 (fact-check 2026-10-09 haiku 검증·정정 완료. 7.5절 회수에 손 교체비 반영) | case-analyst | 완료 | B1 | case/analysis.md |
| B3 | ROI 모델 (가정, 계산, 민감도 시트). 2026-10-12 사용자 지시로 보류 해제, Q7·Q8 값을 analysis.md 7절 위에 덮어써서 작성. fact-check 미실시(사용자 지시) | roi-modeler | 완료 | B2, Q7, Q8 | case/roi.xlsx |
| B5 | (fact-check 미실시) B3·Q7·Q8 결과를 기존 문서에 반영: case/analysis.md 7.2 임금총액 정정, 7.4 유지보수비에서 손 소모 분리, 7.5 회수 계산을 roi.xlsx 값으로 갱신, case/b4-proposal.md ROI 장(6장) 수치 교체. 수정 모드 | case-analyst | 완료 | B3, Q7, Q8 | case/analysis.md, case/b4-proposal.md |
| B6 | (fact-check 미실시) DexBench 형식 반영: b4-proposal 8.3절에 하네스 케이스 카드 초안(단자-하우징 삽입, 당김 확인, 분기 케이블 레이업: 초기 상태·목표 상태·실패 조건·인접 DexBench 과제), 완주율·단계 점수·개입 후 완주율 매핑, 성능이 무너지는 범위(breakdown) 측정 파라미터, RLWRLD에 확인할 프로토콜 질문 목록. 공식 프로토콜은 비공개(Q5)라 공개된 형식만 반영. 수정 모드 | case-analyst | 완료 | Q5, B5 | case/b4-proposal.md |
| Q9 | (fact-check 미실시) ALL HANDS UP(https://allhandsup.org/ko/#gallery) 갤러리 분석: RLWRLD가 지원·호환하는 로봇 손 하드웨어 목록(제조사, 모델, DoF, 촉각 유무, 가격·공개 사양), DexBench·RLDX-1과의 관계(어느 손이 RLDX-1 학습·평가에 쓰였는지, 호환 근거), 운영 주체와 갱신 시점, 하네스 PoC 후보 손(Tesollo DG-5F-S, Inspire 등)과의 매칭. JS 렌더링 가능성이 있으니 HTML이 부르는 데이터(JSON 등)를 찾아 reference/raw에 저장. 이 결과를 b4-proposal 평가 플랫폼 절(B6 후속)에 반영 | researcher | 완료 | Q5, A4 | research/q9-allhandsup.md |
| B7 | (fact-check 미실시) b4-proposal 평가 플랫폼·하드웨어 구성 소절 추가(8.3.5 후보): Q9 결과 반영. 구성 3종(다관절 손 + 촉각 / 손만 / 그리퍼 + 힘센서)과 팔·카메라·GPU·제어 주기 고정, RLDX-1 검증 구현체(ALLEX, Franka, OpenArm + Inspire RH56F1)와 이식 단계, Type 1/Type 2 손 선택 프레임에서 DG-5F-S 위치, 5.2절 "한 팔이 쥐고 다른 팔이 삽입"과 analysis.md "고정 지그" 불일치 정리. 수정 모드 | case-analyst | 완료 | B6, Q9 | case/b4-proposal.md |
| B4 | 케이스 제안서 (md 문서로 작성, 장표는 만들지 않음. ROI 장은 B3 후 교체) | main | 진행중 | B2, B3 | case/b4-proposal.md |
| Q1 | (fact-check 미실시, 사용자 지시) 국내 하네스 조립 라인의 실제 인원, 교대, 택트, 품번 수, 외국인 비중 (경신 국내 4개 사업장이 조립 라인인지 포함). 접근 불가·유료·내부 자료는 사용자 피딩 요청 목록으로 정리 | researcher | 완료 | B2 | research/q1-harness-line-facts.md |
| Q2 | (fact-check 미실시, 사용자 지시) Skild AI × 住友電装 하네스 프로젝트의 범위·결과·손 하드웨어 (다관절 손인가 그리퍼인가). 접근 불가 자료는 사용자 피딩 요청 목록으로 정리 | researcher | 완료 | A8, B2 | research/q2-skild-sumitomo-harness.md |
| Q4 | (fact-check 2026-10-09 haiku 검증·정정 완료) 타사 RFM·휴머노이드 기업(Figure, Skild, PI, Agility, Dexterity, Telexistence, Mujin 등)의 고객 심층 분석(고객 유형, 선정 이유, 계약 구조, 투자자=고객 여부) → 고객 선정 패턴 도출 → 한국·아시아 잠재 고객 후보 분석. case/candidates.md에 새 절로 추가 (기존 B1 결정은 유지) | case-analyst | 완료 | A7, A8, A10, B1 | case/candidates.md |
| Q3 | (fact-check 미실시, 사용자 지시) 住友電工·電装의 하네스 자동화율 약 15%와 약 50%의 정의(공수 기준 대 공정 수 기준)와 1차 소스. 접근 불가 자료는 사용자 피딩 요청 목록으로 정리 | researcher | 완료 | B2 | research/q3-sumitomo-automation-rate.md |
| Q5 | (fact-check 미실시) 덱스벤치(DexBench) 공식 사이트 분석 (https://dexbench.org/en/): 18개 과제 목록, 5영역(Grasp Diversity, Spatial/Temporal/Contact Precision, Context Awareness) 매핑, 평가 방식·채점·시행 수, 리더보드와 비교 모델, 공개 범위(코드·데이터), NVIDIA Isaac Lab-Arena 연결. 하네스·커넥터 삽입·케이블 조작과 유사한 과제 유무, B4 8.3절 평가 과제 및 KPI와의 연결. 접근 불가 자료는 사용자 피딩 요청 목록으로 정리 | researcher | 완료 | A1, A11 | research/q5-dexbench.md |
| Q6 | (fact-check 미실시) 住友電装 영문 PDF 분석 (https://www.sws.co.jp/en/sws-news/docs/bc866af8854aeec61a4d844ec2d41e56c747b051.pdf): 문서 정체(발표일, 주제), Skild 공동 개발·자동화율 15%/50%·모델 라인·로드맵과의 관계, 기존 Q2·Q3 결론(범위·손 하드웨어·성과 미공개, 자동화율 분모 미공개)에 새로 확정되거나 바뀌는 점. 사용자 제공 자료 | researcher | 완료 | Q2, Q3 | research/q6-sws-pdf.md |
| Q7 | (fact-check 생략, 사용자 지시) 다관절 로봇 손의 현장 교체 주기와 유지보수비: 손·손가락·텐던·촉각 겔의 수명(MTBF, 사이클 수, 가동 시간), 제조사 자체 시험 대 현장 데이터, 연간 교체·수리 비용(손 가격 대비 %), 교체 소요 시간과 가동 중단. B3 회수 계산(손 교체 주기 연 0.5·1·2회 시나리오)의 입력값. 공개 수치가 없으면 범위 추정과 근거, 사용자 피딩 요청 목록으로 정리 | researcher | 완료 | B2 | research/q7-hand-replacement.md |
| Q8 | (fact-check 생략, 사용자 지시) B3 임금 입력: 2027년 최저임금 고시값(월·시급, 고용노동부 고시), 국내 자동차 와이어 하네스 생산직 임금(시급·월급, 외국인 인력 포함 여부), 사업주 부담 4대보험·퇴직금 등 간접비율, 교대 수당. 하한·기본·상한 시나리오 값 제안. 접근 불가 자료는 사용자 피딩 요청 목록으로 정리 | researcher | 완료 | B2 | research/q8-wage-inputs.md |
