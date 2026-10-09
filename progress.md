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

## 2026-10-07 16:20 | main | A1 보강
- 한 일: 매일경제 이강욱 CBO 인터뷰(2026-10) 분석. CBO 이력, 덱스벤치(18개 과제), 가중치·코드 공개, 경영진 전략 메시지 6개 정리
- 산출물: reference/company--mk-cbo-interview-2026-10.md, research/company.md(2절 인물, 4절 벤치마크, 6-1절 신설, 시사점, 출처 19), knowledge.md(용어 1, 인사이트 2, 열린 질문 1), case/b4-proposal.md(2장 문제 정의, 8장 평가 과제에 덱스벤치 연결)
- 다음: dexbench.org 원문 확인
- 이슈: A1의 BCG 직급 불일치(파트너 vs 매니징 디렉터)가 "MD & Partner"로 해소됨. fact-check 미실시

## 2026-10-07 16:40 | main | A1 보강
- 한 일: 유니콘팩토리 시드2 기사(2026-02-26) 분석. 금액·투자자는 기존과 일치, 투자자별 역할(Headline Asia 북미, ZVC 일본 실증), CJ대한통운 CFO 발언, "투자자와 PoC·RX 진행 중" 서술을 추가. "SI 중심" 표현의 한계(자산운용사 포함) 메모
- 산출물: reference/company--unicornfactory-seed2.md, research/company.md(3·5·6절, 출처 20), knowledge.md(인사이트 1)
- 다음: 없음
- 이슈: fact-check 미실시

## 2026-10-07 14:05 | researcher | A10
- 한 일: 선도기업 PoC→배포 프로세스 심층 조사. 9개사 + Mujin 단계 표, 단계 모델 매핑, KPI 유형, 계약·가격 구조, 실패·중단·지연 사례(Walmart-Bossa Nova, 교촌, 현대차 노조 등), 일본·한국 보강(CJ대한통운-RLWRLD-로보티즈-에이딘, 교촌, 롯데글로벌로지스·한진), RLWRLD PoC 설계 체크리스트 14항목(G0~G3 게이트)
- 산출물: research/poc-playbook.md, 새 reference 25건(case--poc-*), 기존 문서 정정(rx-cases.md의 Figure "달성"→"목표", Agility 6.5만 시간 미확인; knowledge.md Figure 표현)
- 다음: B4 제안서 8장에 체크리스트 반영(KPI 목표·통과·중단 3종, 자율 성공 대 개입 후 성공 분리, 랩 PoC와 현장 파일럿 게이트 분리, 후속 계약 옵션 사전 제시). B3에 가격 임계 참고값(Mercedes "두 자릿수 천 달러", 교촌 설치 포함 4,000만 원)
- 이슈: **fact-check 미실시 (사용자 지시로 중단)**. 계산치(Figure 4개월, CJ 약 12개월, Telexistence 9개월)와 검색 요약 전용 항목(Agility 월 8,500달러, Mujin 사례 등)이 우선 확인 대상. 비용 $3.55

## 2026-10-07 14:30 | main | B4
- 한 일: A10 체크리스트를 B4 제안서에 반영. 8장을 "게이트 4개(G0~G3), 랩 14주 + 현장 파일럿"으로 재구성: KPI 목표·통과·중단값 표(A트랙 7개, B트랙), 자율 성공과 개입 후 성공 분리 집계, 평가 조건, 운영 원칙 5개, 후속 계약 옵션 3종(구매, RaaS, 공동 모델). 1·7·9·10장 연동 수정
- 산출물: case/b4-proposal.md
- 다음: 실무자 검토. KPI 값은 RLWRLD 제안값(`추정`)이라 근거 보강 필요
- 이슈: KPI 수치 다수가 공개 근거 없는 제안값

## 2026-10-07 17:30 | researcher | A11
- 한 일: RLDX-1 공식 기술 블로그 분석. 아키텍처, 3단계 학습(Pre/Mid/Post), 데이터, 벤치마크·평가 조건(과제당 24회, 시연 40~100개), 하드웨어, 한계, 경쟁 모델 대비 주장, 하네스 RX 시사점. 기존 문서 대비 정정 4건(tech.md의 RL 단계 미확인 등, company.md 센서 행의 촉각, case/analysis.md 120행 Memory 서술), 보완 8건, 해소 2건
- 산출물: research/rldx1-tech.md, 새 reference 3건(company--rlwrld-blog-14, papers--moss-physical-feedback, papers--hamlet-history-vla), reference/papers--rldx1-tech-report.md 갱신, knowledge.md(용어 7, 인사이트 4, 질문 5), 에이전트 메모리 1건
- 다음: 없음(새 시작 가능 작업 없음). B2·B4에 정정 반영 필요(case/analysis.md 120행 Memory 서술, 합의서에 완주율과 단계 점수 분리). tech.md·company.md 정정은 `/rx-refresh`로 반영 가능
- 이슈: fact-check 미실시(사용자 지시). 블로그 서술문과 표 충돌은 표와 논문 결론을 택함. 그림에만 있는 수치(OpenArm, 데이터 혼합 비율)와 논문 HTML 중복 렌더링 숫자(`추정` 표시)는 미확인. 기존 문서 정정은 research/rldx1-tech.md에만 표시하고 tech.md·company.md·analysis.md 본문은 아직 수정하지 않음

## 2026-10-07 18:00 | main | A11 정정 반영
- 한 일: research/rldx1-tech.md 9절 정정표 14건을 원본 문서에 반영. tech.md(RL 단계, Memory 역할, 슬립→무게 추정·접촉 감지, ALLEX 평가 조건, 데이터 수치 조건), company.md(모듈·속도·센서 행, ALLEX 표, GR-1 비교 기준, 8종 목록, 기사 수치 원천, Plug Insertion 33.3%), competitors.md(RLWRLD 증거·센서), case/analysis.md(Memory·Physics 매핑, 센서 서술, 성능 행), case/b4-proposal.md(5.2절 모듈 서술과 공개 근거 한계), knowledge.md(인사이트 2건, 열린 질문 해소 1건)
- 산출물: 위 6개 문서. 각 위치에 "(2026-10-07 A11 정정)" 표시
- 다음: B4 합의서에 완주율·단계 점수 분리, 시행 수 근거 보강(사용자 결정 대기)
- 이슈: 메인 세션이 직접 수정함(사용자 요청, 소규모 정정). fact-check 미실시

## 2026-10-07 18:20 | main | B4
- 한 일: B4 8.3절 보강. KPI를 완주율(전 단계, 판정용)·단계 점수(진단용)·개입 후 완주율로 분리, B트랙도 구간 완주율로 통일. 평가 조건에 지표 정의 고정(RLWRLD 공개 평균의 성공률·진행 점수 혼합 사례), 시행 수 근거(24회 → 8/24 구간 약 18~53%, 100회 → ±6%p), 신뢰구간 보고와 판정 방식 G0 합의 추가
- 산출물: case/b4-proposal.md
- 다음: 실무자 검토
- 이슈: 없음

## 2026-10-09 13:10 | researcher | Q1, Q2, Q3
- 한 일: 열린 질문 중 B3·B4 핵심 3개를 병렬 조사. Q1 국내 하네스 라인 실측(라인 단위 수치 국내 없음, 유라 국내 생산직 668명·외국인 직접고용 1/2,080, 경신 4곳 중 하네스 확인은 경주 1곳), Q2 Skild × 住友電装(1차 소스는 2026-09-17 공동 개발 개시까지, 공정·손 하드웨어·성과 미공개, 기존 "이미 자동화하고 있다"는 기사 표현이 과함), Q3 住友 자동화율(15%는 "全工程の約15%", 50%는 모델 라인 한 곳에서 "높일 수 있다", 분모 미공개)
- 산출물: research/q1-harness-line-facts.md, research/q2-skild-sumitomo-harness.md, research/q3-sumitomo-automation-rate.md, 새 reference 약 25건, manual-research.md 5절(피딩 요청 10개)
- 다음: 기존 문서 정정(case/b4-proposal.md 45·80·84·309행, case/analysis.md 6·30·201·227~228행, case/deck-storyline.md 55행, research/skild-pi-deep-dive.md 3.2절, knowledge.md 105행·열린 질문 164행)은 Q4 완료 후 한 번에 반영. 사용자 피딩 자료 수령 시 reference/raw/에 저장 후 재분석
- 이슈: fact-check 미실시(사용자 지시). Q1 에이전트는 40턴 한도에서 보고 없이 종료했으나 산출물은 완성 상태로 저장됨(메인이 문서를 읽고 확인). 15%·50%는 B3 ROI 입력값으로 쓰지 않음. B3 라인당 32명·2교대·311초는 여전히 모로코 참고값

## 2026-10-09 14:20 | case-analyst | Q4
- 한 일: 타사 RFM·휴머노이드 기업 고객 24건 심층 분석, 첫 고객 선정 패턴 8개와 점수 기준 7개, 한국·일본·아시아 잠재 고객 후보 점수화(矢崎 3.70, 경림테크형 3.40, 유라 3.30, 경신 3.10 vs 기존 투자자 고객 3.95~4.15), 피딩 요청 12건. 타사 첫 고객 24건 중 7건이 투자자·모회사·유통 파트너 겸 고객이고 RLWRLD 공개 고객 3곳도 같은 구조
- 산출물: case/candidates.md Q4절 신설(기존 B1 점수표·결정 유지), 새 reference 18건, manual-research.md 6절
- 다음: fact-check 실시 여부 사용자 결정 대기(점수 기준·가중치는 팀 제안 `추정`). 矢崎 REN, 2027 실증 공모 요강, RLWRLD 내부 RX 파이프라인 피딩 시 후보 점수 재계산
- 이슈: case-analyst가 30턴 한도에서 쓰기 전에 멈춰 SendMessage로 이어서 완료. 검색 요약만 근거인 항목(Figure 2호 고객 UPS 보도, Jabil 파일럿, Lawson의 Telexistence 도입, SoftBank의 ABB 로보틱스 인수)은 `확인필요`로만 표기

## 2026-10-09 14:25 | main | Q1~Q4 정정 반영
- 한 일: Q1~Q3 결과를 기존 문서에 반영. case/b4-proposal.md(2·4·9·10장, 부록 B), case/analysis.md(결론, 0·1.1·5.2·6·7.1절, 확인하지 못한 항목, 출처 40~42), case/deck-storyline.md(2장), research/skild-pi-deep-dive.md(핵심 요약, 1·3.2·5절, 출처), knowledge.md(105행, 열린 질문 4건 갱신, 용어 9, 인사이트 8, 열린 질문 8 추가). 住友電装-Skild는 "이미 자동화"에서 "2026-09-17 공동 개발 개시, 범위·성과 미공개"로, 住友 15%·50%는 "정의 미공개, 50%는 모델 라인 한 곳에서 높일 수 있다"로 정정
- 산출물: 위 문서 각 위치에 "(2026-10-09 Q 정정)" 표시
- 다음: 범위 밖으로 남긴 3건 처리 여부 결정: (1) b4-proposal 4장 94행 "Skild가 사이클 타임과 배포 실적에서 앞서 있다" 근거 미확인, (2) b4 2장·deck 2장 출처 "[3] 住友電工"는 실제로 住友グループ広報委員会 페이지(住友電装 내용), (3) deck-storyline 6장 리스크 표에 "국내 소수 라인 PoC → 해외 거점" 미반영. skild-pi-deep-dive 5절 4번의 "住友電装·Mitsui" 단계 구분(Mitsui piloting)도 미정정. B3 착수 전 B2 fact-check 필요
- 이슈: 정정은 메인이 지시하고 담당 에이전트가 수정(case-analyst, researcher). Q1~Q3 fact-check 미실시(사용자 지시)

## 2026-10-09 17:30 | main | fact-check 일괄 (A1 보강, A7, A8, A10, A11, B2, Q4)
- 한 일: fact-check가 밀린 7건을 haiku fact-checker 9개로 병렬 검증(보고만) 후 담당 에이전트(case-analyst, researcher, sonnet)가 정정. Q1~Q3는 사용자 지시로 제외. 주요 정정:
  - 조달 비교: "약 50배", "PI 21억(보도)", "Skild 20억 이상" 폐기. 단일 라운드 약 34배(계산), 누적은 Skild 하한 약 17억·PI 확정 약 10.7억(`추정`). 확정 라운드만 합치면 Skild가 PI보다 큼
  - Skild 매출 86%→약 90%(1차). Mitsui는 piloting, 住友電装는 working towards deploying
  - B2 7.5절 회수에 손 교체비 누락: 기본 5.7년은 교체비 제외 값, 손 1개 연 1회 교체 시 약 10.6년, 2개 약 77년. 속도비 0.5는 기술 가능성 게이트이며 ROI 기준 아님
  - 산업 벤치마크 78%→v3 76%, 데이터센터 케이블 청소 보드(Board #1) 결과이며 하네스 보드는 성능 결과 없음
  - Q4: "투자자 겸 고객 7건"→확인 4+유통 1+추정 1(최대 6건). C1·C5 기준 확정 후 재채점(롯데 4.10, LG 3.35, 경림테크형 3.30). C1 제외 시 경림이 KDDI보다 앞선다는 결론 폐기
  - A1 보강: CFO 인용 원문화, Headline Asia 역할 추론 삭제, CBO 70~80%는 가정형 발언(통계 아님), CBO 인터뷰 게재일 raw 입력 2026-09-08
  - A10: 교촌 4,000만 원은 업계 단가(교촌 구매가 아님). Figure 4개월은 상한, CJ 약 11~12개월. 검색 요약 전용 항목 수치 삭제
  - A11: Mid-training 가중치 서술, Egg PnP 61.1% 시행 수 불명확, "과제당 24회"는 ALLEX 한정
- 산출물: research/ 6개(skild-pi-deep-dive, rx-cases, competitors, poc-playbook, rldx1-tech, company, papers), case/ 4개(candidates, analysis, b4-proposal, deck-storyline), reference 정정 4건·신규 1건, knowledge.md
- 다음: B3 착수 가능(B2 fact-check 완료). 입력은 case/analysis.md 7절(손 교체비 반영 후). 사용자 피딩 자료(manual-research.md 5·6절)가 들어오면 가정값 갱신. 남은 `확인필요`: 레이업 lay-up 4 해석, 손 교체 주기, 2027 최저임금, 住友電装 C5 점수 재검토, 롯데 C5 4점 과대 여부
- 이슈: haiku 검증 에이전트가 이미지 캡션을 놓친 오판 2건(Skild 슬로건, FR3 카메라)이 있어 정정 단계에서 raw 재확인으로 걸러냄. A11 검증과 Q1 조사 에이전트가 턴 한도에서 멈춰 SendMessage로 이어서 완료. A2~A6 fact-check는 이전에 완료
