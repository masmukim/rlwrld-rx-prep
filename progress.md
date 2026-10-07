# 작업 기록

## 2026-10-06 | main | setup
- 한 일: CLAUDE.md 작성, research/ case/ 폴더 생성, GitHub 저장소 연결, plan.md 초기 작업 목록 작성
- 산출물: CLAUDE.md, plan.md, progress.md
- 다음: 선행 작업이 없는 A1, A2, A5부터 병렬로 시작 가능
- 이슈: 없음

## 2026-10-06 15:29 | researcher | A1
- 한 일: RLWRLD 회사 개요, 투자 이력(시드1 1,500만 달러 + 시드2 2,600만 달러 = 누적 4,100만 달러), 인물, RLDX-1(8.1B, MSAT, ALLEX 86.8% 자체 평가), 파트너·공개 고객(롯데호텔, CJ대한통운, KDDI/Lawson), RX 사업 구조 정리. fact-checker 검증 결과 오류 3건과 누락 7건이 나왔고, 메인 에이전트가 수정함
- 산출물: research/company.md, 새 reference 17건 (company-- 16건, papers--rldx1-tech-report 1건)
- 다음: A2, A5 시작 가능 (A1 완료로 새로 열리는 작업은 없음. B1은 A4, A5 완료 대기)
- 이슈(확인필요): 본사 표기가 소스마다 다름(보도자료 서울·도쿄, 데모데이 미국, 홈페이지 샌프란시스코) / 원화 환산은 기사 표기를 따랐고 환율은 미공개 / Robot Report·R&D World 기사 날짜 미확인 / R&D World의 "무인화" 인용은 reference 발췌에 없음 / 가중치 라이선스 원문(LICENSE) 미열람 / RLDX-1 논문은 초록 수준만 확인

## 2026-10-06 15:41 | researcher | A2
- 한 일: VLA 모델 계보(ACT부터 RLDX-1까지), 모방학습·강화학습·교정 결합, 데이터 수집 방식 비교(텔레오퍼레이션, 공유 자율, 웨어러블 모캡, 에고센트릭, 합성), 손 조작 난제와 RLDX-1의 대응, 기술 성숙도 한계 정리. fact-checker 검증 결과 오류 1건(라이선스 출처)과 누락 4건(출처에 없는 서술, 추정 표기 누락)이 나왔고, 메인 에이전트가 수정함. EgoScale +54% 표기도 상대/%p 미구분으로 고침(reference 메모 포함)
- 산출물: research/tech.md, 새 reference 14건 (papers-- 11건, tech-- 3건)
- 다음: A3, A4, A6 시작 가능
- 이슈(확인필요): 기사 인용 수치(하루 50~200 시연, π0 약 1만 시간, GEN-0 27만 시간, 통합 비용 하드웨어의 50~200%) 1차 소스 미확인 / RLDX-1 논문 본문(학습 레시피, ALLEX 평가 조건) 미열람 / π0·π0.5·GR00T N1의 정량 성능과 촉각 입력 여부 미확인 / 서베이 비교표는 요약 경유

## 2026-10-06 15:44 | researcher | A5
- 한 일: 글로벌 설치 대수·로봇 밀도, 한국·일본 인력난(미충원, 외국인력, TDB 부족 응답, 리크루트웍스 2040 전망), 산업별 자동화 미충족 영역, 시장 규모(근거 수준 구분), 국내 정책 예산, B1 후보 공정 long-list 6개 정리. fact-checker 검증 결과 오류 2건(JARA 집계 기준 혼용, 2024년 기준 국가별 감소 서술)과 누락 6건이 나왔고, 메인 에이전트가 수정함. IFR World Robotics 2026(2026-09-24) 수치로 갱신하고, reference 없는 독파모·벤더 시장 규모 행은 삭제함. "면접에서" 항목은 고객 보고 인용 원칙으로 바꿈
- 산출물: research/market.md, 새 reference 13건 (market-- 13건, IFR 2026 1건은 메인 에이전트가 저장)
- 다음: B1은 A4 완료 대기 (A1, A5 완료). A3, A4, A6 시작 가능
- 이슈(확인필요): 와이어 하네스 수작업 비중 85~90%·일본 물류 2030년 34.1% 부족 원문 403 / JARA 회원+비회원 기준 수치 원문 미대조 / Goldman 원문, 기획예산처 1차 문서 미확인 / 리크루트웍스 직종별 표는 요약 경유 / IFR 2026판 기준 로봇 밀도 미확인 / 독파모 관련성 1차 소스 없음

## 2026-10-06 17:20 | researcher | A6
- 한 일: VLA/RFM, 정밀 손 조작, 촉각·힘, 데이터 수집, 산업 적용 5개 주제의 핵심 논문 지도(초록 확인 27편, 추가 후보 7편) 작성. 촉각·힘 입력은 ForceVLA(2025-05), Tactile-VLA(2025-07)가 RLDX-1(2026-05)보다 앞서므로 차별점은 고자유도 손, 데이터 파이프라인, 독립 검증으로 정리. fact-checker 검증 결과 수치 불일치는 없었고, GR00T N1.7 1차 소스 서술 오류, 경쟁 맥락(NVIDIA 동일 20,854시간) 누락, HapticVLA 원문 확인 등 6건을 researcher 수정 모드로 반영함
- 산출물: research/papers.md, 새 reference 18건 (papers-- 15건, tech-- 2건, hapticvla 포함) + 기존 reference 2건 정정
- 다음: 새로 열리는 작업 없음. B1은 A4 완료 대기 (A3는 A4, A6와 무관)
- 이슈(확인필요): ForceVLA 23.2%, Sparsh-X 63%, T-Rex 30%, EgoScale 54%, Diffusion Policy 46.9%의 상대/%p 구분 미확인(WebFetch 요약이 같은 수치를 상반되게 답함) / ABEJA×村田製作所의 N1.7 사용, 일본 3사 VTLA는 기사 기준 / Industrial Dexterity Benchmark는 v3(2026-09-21) 개정 후 수치 변동 미확인 / researcher WebFetch 약 22건(한도 15건 초과)

## 2026-10-06 17:21 | researcher | A4
- 한 일: 다관절 손(Shadow, Allegro, Inspire, Tesollo, Sharpa, ORCA, Figure, Tesla), 산업용 그리퍼, 촉각 센서(DIGIT 360, GelSight, FingerVision, XELA), 깊이 카메라(RealSense, Orbbec, Zivid) 사양·가격·내구성 비교와 end-effector 선정 프레임(공정 특징별 우선 후보) 정리. fact-checker 검증 결과 수치는 원문 7건 모두 일치했고, 인용 번호 오류(Optimus 25 액추에이터 등), Tesla 현행 사양 충돌 미표기, Inspire 리셀러 가격 상한 오류, "면접에서" 표현 등 11건을 researcher 수정 모드로 반영함
- 산출물: research/hardware.md, 새 reference 18건 (hardware-- 15건, papers-- 3건)
- 다음: B1 시작 가능 (A1, A4, A5 완료). 단 공정 선정은 사용자 결정(4-1 단계) 필요
- 이슈(확인필요): Inspire RH56DFX 공식 $24,399.99의 구성 미확인, 리셀러 $4,500~10,500 이상(일부는 코디네이터 확인분) / 대부분 손 가격이 리셀러·제품 DB 기준 `추정` / Sharpa 1,000시간·payload 40 kg 대 파지력 150 N 정합 미확인 / Tesla 현행 손 사양 미확정(Musk 4월 발언 대 Tech Times 9월) / 내구성은 제조사 자체 시험 수준 / researcher WebFetch 약 24건(한도 초과)

## 2026-10-06 17:22 | researcher | A3
- 한 일: RLWRLD 대 Physical Intelligence, Figure, Skild AI, Google DeepMind, NVIDIA, Tesla 및 한국 국내(삼성, LG, KT 등) 비교. 모델, 하드웨어, 데이터 전략, 타깃 산업, 투자(RLWRLD 누적 4,100만 달러 대 Skild 단일 라운드 약 14억 달러, 약 34배 계산), 한·일 접점 정리. NVIDIA GR00T N1.7(2026-04)이 에고센트릭 20,854시간과 22-DoF 손을 공개해 데이터 전략 자체는 차별점이 아님. fact-checker 검증 결과 핵심 수치는 원문과 일치했고, DeepMind 36% 선택 인용(같은 로봇 92% 병기), KT 예산 귀속 오류, NC AI 협력사 추정 오류, PI 누적 조달 합산 설명 등 9건을 researcher 수정 모드로 반영함
- 산출물: research/competitors.md, 새 reference 16건 (competitors-- 15건, papers--gemini-robotics 1건) + 기존 reference 정정
- 다음: 새로 열리는 작업 없음. B1은 이미 시작 가능 (A1, A4, A5 완료), 사용자 결정 필요
- 이슈(확인필요): 삼성DX 협력과 RLDX-1 개발사 표기는 nate 요약마다 달라 이데일리 원문 재확인 필요 / DeepMind 92%, 삼성DX는 팩트체크 대조 기준이며 researcher 미확인 / KT 단독 예산 미확인 / PI 라운드 금액은 검색 요약 수준 / Tesla V3 공개 여부 미확인 / 일본어 소스 1건뿐이라 일본 경쟁 주체 미조사 / researcher WebFetch 약 20건(한도 초과)

## 2026-10-06 22:16 | case-analyst | B1
- 한 일: 공고 7개 산업을 스크리닝해 후보 5개(호텔 연회 4.25, 물류 피킹·포장 4.00, 와이어 하네스 3.70, 전자 커넥터 3.60, 편의점 진열 2.90)를 점수화. fact-checker 검증 후 새 case-analyst 수정 모드로 고침. 실무자가 제공한 외부 분석을 참고해 **와이어 하네스 조립**으로 결정 (점수표 3위를 고른 이유와 리스크는 candidates.md `결정` 절)
- 산출물: case/candidates.md, 새 reference 7건 (외부 분석 요약 1건 포함)
- 다음: B2 시작 가능. 첫 확인 항목은 국내 하네스 조립 라인 존재 여부
- 이슈: 헤드리스 실행이 세션 사용량 한도로 완료 처리 직전에 멈춰 메인 세션이 마무리함. source-read는 권한 거부로 이번 작업에서 쓰이지 않음(69f2de6에서 수정). 공정별 인원·사이클 타임·시급 공개 수치 미확보

## 2026-10-07 12:40 | case-analyst | B2
- 한 일: 자동차 와이어 하네스 조립 공정 심층 분석. 참고 라인 작업장 32개 중 프리블록·레이업·테이핑 22개(69%)가 RFM 대상. 자동화 장벽은 기술보다 다품종 경제성으로 정리하고, PoC를 2트랙(A 프리블록 셀 + 그리퍼 대조군, B 레이업 고자유도 손 검증)으로 제안. 셀 1기 약 3.96억 원, 2교대·사람과 같은 속도면 회수 약 5.7년(`추정`), 속도비가 1순위 민감도 변수. B3용 가정값 표 포함
- 산출물: case/analysis.md, 인용 reference 24건(이전 중단 시도에서 저장한 것), 가상 고객 K사는 모로코 참고 라인 구성을 가정
- 다음: B3 시작 가능. **B2 fact-check는 아직 하지 않음 (사용자가 독립 세션에서 진행 예정)**
- 이슈: 서브에이전트의 case/analysis.md 쓰기를 Claude Code가 막아("Subagents should return findings as text, not write report files") 메인이 반환된 전문을 수정 없이 저장함. B2는 헤드리스 시도 4회(10분 대기 제한 2회, 사용량 한도 1회) 끝에 완료, 누적 비용 약 $10.1. 확인필요: 경신 국내 사업장 역할, 하네스 생산직 임금, 住友 자동화율 정의, Cellios 가격, 손·센서 공식 견적, 중기부 지원 지속 여부, 텔레오퍼레이션 "하루 50~200개"·"통합비 50~200%" 1차 소스

## 2026-10-07 13:05 | main | B4
- 한 일: B4 장표 스토리라인 초안 작성. 8장 헤드라인(주장 문장), 장별 본문·시각 요소·출처, `[검토]` 표시 14곳, 실무자 결정 사항 6개. ROI 장은 B2 7.5절 예비 계산 사용
- 산출물: case/deck-storyline.md
- 다음: 실무자가 스토리라인 수정 → 장표 제작. B3 완료 후 ROI 장 수치 교체
- 이슈: B2 fact-check 전이라 수치가 바뀔 수 있음. B3는 사용자 지시로 보류

## 2026-10-07 14:10 | main | A7
- 한 일: RLWRLD Business 페이지(RX, PoC, 파트너십, 생태계) 원문 확인, 해외 도입 사례 9개사(Figure, Agility, Apptronik, Boston Dynamics, Dexterity, Telexistence, Physical Intelligence, Skild AI, Sanctuary AI) 정리와 패턴 7개 도출
- 산출물: research/rx-cases.md, reference/company--rlwrld-business-rx-poc-partnership.md
- 다음: B4 스토리라인에 PoC 장소(RLWRLD 랩), RX 산출물 명칭, KPI(교대당 개입·자율률), 모델 상품화 옵션 반영 검토
- 이슈: 사용자 요청으로 메인 세션이 직접 조사(researcher 미사용), fact-check 미실시. PI 파트너 페이지 원문 미열람(429). 기사 수치 다수 1차 미확인

## 2026-10-07 14:50 | main | A8
- 한 일: Skild AI와 Physical Intelligence 심층 분석(개요, 투자, 모델 계보, 배포 사례, 사업 방식, RLWRLD와 3자 비교, 비판적 시사점 7개). Skild × 住友電装 하네스 사례 발견
- 산출물: research/skild-pi-deep-dive.md, reference/raw 원문 6건
- 다음: B4 스토리라인에 경쟁(Skild 하네스), 차별점(레이업), OEM 확산 경로 반영 검토
- 이슈: 메인 세션 직접 조사, fact-check 미실시. rx-cases.md의 "Ultra 자율률 96.4%"가 원문 미확인으로 드러나 정정함. PI 원문(pi.website) 429로 미열람

## 2026-10-07 15:45 | main | B4
- 한 일: 사용자 지시로 장표 대신 md 제안서 작성. 스토리라인에 A7(RLWRLD RX 방식: 랩 PoC, 공동 모델 상품화)과 A8(Skild × 住友電装 하네스 경쟁) 반영. 10개 장 + 부록 3개. 경쟁 지형, 도입 구조 장 신설, PoC 통과 기준과 상용화 기준 분리, KPI에 교대당 개입 횟수 추가
- 산출물: case/b4-proposal.md (deck-storyline.md는 이전 초안으로 남김)
- 다음: 실무자 검토. B3 완료 후 6장 수치 교체. B2 fact-check 결과 반영
- 이슈: Slides 아티팩트를 시작했다가 사용자 지시로 중단 (빈 아티팩트 1개 남음, 내용 미게시)
