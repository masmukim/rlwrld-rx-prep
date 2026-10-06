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
