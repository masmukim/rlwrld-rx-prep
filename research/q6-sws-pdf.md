# Q6. 住友電装 영문 PDF(bc866af8…) 분석: Skild AI 공동 개발 영문판 릴리스
조사일: 2026-10-09

## 핵심 요약
- **이 PDF는 이미 확보한 일본어판 보도자료(2026-09-17)의 영어 번역본이며, Q2·Q3가 묻던 항목에 새로 답하는 사실은 없다.** 2쪽짜리 텍스트형 PDF이고 이미지는 로고뿐이다. 대상 공정, 로봇, 핸드(end-effector), 센서, 일정, 성과, 투자액은 일본어판처럼 하나도 없고, 자동화율 수치도 없다. URL이 달라 reference상 중복은 아니지만 정보상으로는 일본어판과 같다 [1][2].
- **서술 강도는 "시작(開始)했다"와 "도입한다(導入します)·추진한다(進めます)·목표한다(目指します)"까지다.** 달성이나 가동을 뜻하는 문장이 없다. 영어판은 일본어에 없는 "This will enable robots to…"와 "Sumitomo Wiring Systems and Skild AI are also working…"를 넣어 일본어 원문보다 약간 강하므로, 인용은 일본어 원문 시제를 기준으로 한다 [1][2].
- **PDF에서 링크를 따라가 얻은 부수 결과가 세 가지다.** (a) 중기계획 발표일이 2026-07-16으로 확인됐다. (b) 영어판 중기계획 자료의 "30V and 28M numerical targets" 슬라이드에는 자동화율이 없다(매출·영업이익률·ROIC 등뿐). (c) 같은 자료에 住友電装 자신이 "Global Market Share No. 1"과 자동차용 하네스 세계 점유율 21%(FY2025)를 적고 있어, 기존 문서의 "'1위권'은 근거가 없어 고침" 정정이 지나쳤을 수 있다(자사 표기라는 조건 포함, 5절) [3][4].

## 본문

### 1. 문서 정체
| 항목 | 내용 | 근거 |
|------|------|------|
| 제목 | Sumitomo Wiring Systems and U.S.-Based Skild AI Launch Joint Development of Physical AI Robots for Wire Harness Manufacturing | [1] |
| 발행 주체 | 住友電装株式会社 (Sumitomo Wiring Systems, Ltd., 四日市). 문서 하단 로고는 SUMITOMO ELECTRIC GROUP | [1] |
| 발표일 | 2026-09-17 (본문 날짜, PDF 메타데이터 생성일 2026-09-17 09:34 JST) | [1] |
| 종류 | News Release 영문판 (일본어판 b19d54d9…의 번역). 영문 HTML 안내 페이지 https://www.sws.co.jp/en/sws-news/2026/09171334.html 이 같은 PDF(302.6KB)를 링크 | [1][2] |
| 분량 | A4 2쪽. 1쪽 본문(배경과 목적, Skild AI와의 협력), 2쪽 연락처와 참고 링크 3개 | [1] |
| 텍스트 추출 | **성공**(2,782자). 스캔본이 아니다. 1쪽을 렌더링해 확인한 이미지는 로고 3종뿐이고 공정도, 로봇 사진, 구상도는 없다. 2쪽 이미지는 렌더링하지 않았다(텍스트 추출은 정상이고 2쪽에는 본문이 없다) | [1] |
| 중복 확인 | 기존 住友 reference의 URL은 sws-news/docs/b19d54d9…(일본어 Skild), …bbf14950…(ExaWizards), sumitomoelectric.com prs039(스마트 팩토리), corporation-strategy_jp.pdf 등이다. bc866af8…는 없으므로 **URL 기준 중복 아님**. 내용 기준으로는 b19d54d9…의 영어 번역이다 | reference/ 전수 grep |
| 원문 저장 | reference/raw/case--sws-skild-pdf.txt. reference 파일은 reference/case--sws-skild-release-en.md | |

### 2. 핵심 내용과 수치
이 릴리스에는 숫자가 없다. 포함된 정보는 아래뿐이다.

| 항목 | 원문 표현 (영어판, 일본어판 대응어) | 비고 |
|------|------------------------------------|------|
| 사건 | "launch of a joint development initiative for physical AI robots for the manufacturing of wire harnesses" (共同開発を開始いたしました) | 개시 발표 |
| 배경 | 하네스 제조는 "numerous complex processes"가 있어 기존 로봇 기술이 대체하지 못해 "long-standing reliance on manual labor" (人手作業に依存してきました) | 수작업 비중 수치 없음 |
| 상위 계획 | "2030 VISION" Mid-Term Management Plan 2028(2026년 수립)에서 AI로 "Smart Factory" 구상을 실현하는 방침 | 방침 |
| 회사 전체 활동 | 피지컬 AI 로봇을 "developing and conducting on-site verifications" (開発・現場実証に取り組んでいます) | Skild 프로젝트에 한정되지 않은 회사 전체 활동 |
| Skild 소개 | CMU 출신 미국 스타트업, 하드웨어 독립(hardware-independent) 범용 로보틱스 파운데이션 모델 "Skild Brain" | 본사 "California" |
| 공동 개발 내용 | 최신 모델 "S1" 도입. 로봇이 다양한 작업을 짧은 시간에 학습하고 복잡한 작업에 유연하게 대응. 로봇이 자율적으로 학습하는 시스템을 개발 | 능력의 서술이며 측정값 없음 |
| 목표 | 개발한 피지컬 AI 로봇을 적극 활용해 하네스 제조의 스마트 팩토리 실현 | 목표 |
| 2쪽 참고 링크 | 중기계획 영문 릴리스, Skild 블로그 "The Hidden Pillar of Robotics", 멀티 AI 에이전트(ExaWizards) 영문 릴리스 | Skild 블로그는 기존 확보 [5] |

숫자(%, 대수, 일정, 금액)는 find.py 검색에서 0건이다 [1].

### 3. Q2·Q3에 대해 새로 확정된 것, 바뀌는 것, 여전히 미공개인 것

#### 3.1 Q2 (Skild 공동 개발)
| 항목 | 이 PDF가 주는 것 | 판정 |
|------|------------------|------|
| 대상 공정 | 없음. "wire harness manufacturing"과 "numerous complex processes" 일반론뿐 | **여전히 미공개** |
| 로봇(형태, 대수) | 없음. "physical AI robots"만 언급 | **여전히 미공개** |
| 핸드·end-effector | 없음. Skild Brain이 "hardware-independent"라는 소개만 있다. 이는 하드웨어를 특정하지 않는다는 뜻이지 핸드 종류를 말하지 않는다 | **여전히 미공개** (Q2 3.3 결론 유지) |
| 센서 | 없음 | **여전히 미공개** |
| 일정 | 프로젝트 일정 없음 | **여전히 미공개**. 회사 로드맵(2025-2026 실증, 2027-2028 모델 라인, 2030 글로벌)은 중기계획 자료에만 있다 [4] |
| 성과·상용화 | 없음. 동사가 "launch", "will introduce", "aims to realize"여서 가동이나 달성이 아니다 | Q2 결론 유지: 개시 단계 |
| 협력 범위의 성격 | 공동 개발이 ①S1 도입, ②로봇이 자율 학습하는 시스템 구축의 두 갈래로 서술된다 | **Q2 문서에 없던 정리.** 단, 일본어판에 같은 문장이 있었고(reference/case--sws-skild-joint-dev-release.md) Q2가 쓰지 않았을 뿐이다. 공정이 아니라 기술 구성의 범위이며, 자율 학습의 구체 방식(시연, 강화학습, 현장 데이터)은 미공개 |
| 로봇의 성격 | 회사가 정의한 피지컬 AI 로봇은 "work flexibly in collaboration with humans"(人と協働して). 중기계획 자료는 "무인화 라인"과 "사람·로봇 협업 라인"을 구분한다 [4] | 해석(`추정`): 이 로봇은 완전 무인보다 협업 라인용으로 정의돼 있다. Skild 프로젝트가 어느 라인용인지는 말하지 않는다 |
| Skild 본사 | "California, U.S." (일본어판과 같다) | 불일치(기존 문서 피츠버그) 미해결. 같은 발행처의 번역본이므로 독립 확인이 되지 않는다 |

#### 3.2 Q3 (자동화율, 모델 라인, 분할 하네스, e-STEALTH W/H)
| 항목 | 이 PDF가 주는 것 | 링크로 얻은 것 | 판정 |
|------|------------------|----------------|------|
| 자동화율 15%/50%의 정의·분모·시점 | 없음. 이 릴리스에 자동화율 언급이 없다 | 영어판 중기계획의 "30V and 28M numerical targets" 슬라이드(17쪽)는 매출 2.5조 엔 초과(30V), 영업이익률 7%·ROIC 개선, 신제품 매출비중 15% 이상 등이며 **자동화율 목표가 없다** [4]. 인사 지표 슬라이드에 15%, 50% 숫자가 나오지만 인사 지표다 | **정의 미확정 유지.** Q3 사용자 피딩 요청 #3 중 "수치 목표 슬라이드"는 텍스트로 확인돼 해소(자동화율 없음). 20쪽 로드맵도 영어판에서 읽혔다 |
| 모델 라인 | 없음 | 중기계획 로드맵의 2027-2028 "Building a model line"은 "model production line for next-generation smart factories in Japan"이다 [4]. 일본어 그룹 페이지의 "자동화율 50%의 모델 라인"(세트 공법 + 분할 하네스)과 같은 라인인지는 어느 소스도 말하지 않는다 | **새로 확인된 주의점.** 같은 용어가 두 맥락에 있어 합치지 않는다. 합치는 것은 `추정`이며 근거 없음 |
| 분할 하네스 | 없음 | 영어판(split)과 일본어판(分割) 중기계획 자료 모두에 분할 하네스 용어가 없다(grep 0건) | 변화 없음 |
| e-STEALTH W/H | 없음 | 에어리어 하네스 슬라이드에 "Main harness: e-STEALTH W/H / Branch harnesses: Conventional method"가 영어로 확인된다. "Achieved automation of the production process through (1) flattening the wires, (2) aluminum conductors, (3) simplification of the harness structure" [4] | Q3의 간선/지선 해석 재확인. 단 영어 "Achieved"의 일본어 시제는 일본어 추출문이 끊겨 확인 못 함(4절) |
| 공수(W/H) 정의 | 없음 | 없음 | **여전히 미공개** |

`e-STEALTH W/H`의 "W/H"는 wire harness 약어이며, 이 영어 자료에서도 간선 제품으로 표기된다. 분할 하네스와의 관계는 여전히 `추정`이다(Q3 3절).

### 4. 서술 강도: 일본어 원문 시제 기준
일본어 원문은 reference/raw/case--sws-skild-joint-dev-release.txt 23~44행, 영어는 reference/raw/case--sws-skild-pdf.txt 19~57행이다.

| 서술 | 일본어 원문 | 영어판 | 강도 분류 | 영어판이 더 강한가 |
|------|-------------|--------|-----------|---------------------|
| 공동 개발 | 共同開発を開始いたしました | has announced the launch of a joint development initiative | **사실(개시)** | 아니오 |
| 수작업 의존 | 人手作業に依存してきました | resulting in a long-standing reliance on manual labor | 현황 사실 | 아니오 |
| 중기계획 방침 | 方針を掲げています | has set forth a policy | 방침(계획) | 아니오 |
| 피지컬 AI 로봇 | 開発・現場実証に取り組んでいます | is developing and conducting on-site verifications | 진행 중(회사 전체 활동, Skild 한정 아님) | 아니오 |
| S1 도입 | 「S1」を導入します | will introduce Skild AI's latest model "S1" | **계획(미래형)**. 도입 완료 아님 | 아니오 |
| 능력 | これにより、ロボットがさまざまな作業を短期間で学習し、複雑なタスクにも柔軟に対応するとともに | This will enable robots to learn a wide range of tasks in a short time and respond flexibly to complex tasks | **기대 효과**(일본어는 "これにより"로 효과를 가리킬 뿐 가능하게 한다는 동사가 없음) | **예: "will enable"이 일본어에 없는 확언조** |
| 자율 학습 시스템 | 自律的に学習できるシステムの構築を進めます | Sumitomo Wiring Systems and Skild AI are also working to develop a system | **추진(진행·계획)** | **약간 예**: 영어는 주어에 두 회사를 명시. 일본어는 주어 생략 |
| 스마트 팩토리 | 実現を目指してまいります | aims to realize | **목표** | 아니오 |

규칙: 이 릴리스에서 달성이나 가동을 뜻하는 문장은 없다. 인용할 때는 "개시했다", "S1을 도입할 예정이다", "자율 학습 시스템 구축을 추진한다", "스마트 팩토리 실현을 목표로 한다"까지만 쓰고, "로봇이 짧은 시간에 학습할 수 있다"는 일본어 원문에서 확언이 아닌 기대 효과이므로 단정하지 않는다. 같은 PDF의 중기계획 영어판은 "Achieved automation of the production process through…"(과거형)라고 쓰지만 이는 에어리어 하네스 슬라이드이고 Skild와 무관하다. 일본어판 슬라이드 추출문이 끊겨 원문 시제를 확인하지 못했으므로 인용하지 않는다.

### 5. 수정이 필요한 기존 문서와 위치 (수정은 하지 않음, 메인이 결정)
| # | 파일 | 위치 | 현재 서술 | 필요한 조치 | 근거 |
|---|------|------|-----------|-------------|------|
| 1 | research/q2-skild-sumitomo-harness.md | 3.2절·3.4절(결과·구성), 출처 목록 | 협력 범위를 "공정 미공개"로만 정리. 자율 학습 시스템 구축이 범위에 들어 있다는 점이 없다 | "공동 개발 = S1 도입 + 자율 학습 시스템 구축(자율 학습 방식은 미공개)" 한 줄 추가. 출처에 영문판 PDF 추가(내용 동일) | [1][2] |
| 2 | research/q2-skild-sumitomo-harness.md | 94행(시사점 2), 5.2절 B4 표 | '업계 1위권'은 근거 없다고 정정 | 아래 #3과 함께 "자동차용 하네스 세계 점유율 1위(자사 자료 표기)"로 재검토 | [4] |
| 3 | case/analysis.md 6행·30행, case/b4-proposal.md 45행, case/candidates.md 226행·289행, case/deck-storyline.md 56행, research/skild-pi-deep-dive.md 6행, research/q2 94행, research/q3 59행 | "'업계 1위권'은 근거가 없어 고침, 2026-10-09 fact-check 정정" 문구 | "근거 없음"이라고 쓴 부분은 사실과 다르다. 住友電装 자신의 중기계획 자료(일·영)에 "グローバルシェアNo.1"/"Global Market Share No. 1"과 자동차용 하네스 세계 점유율 21%(2025년도)가 있다. 다만 자사 표기이고, "No.1" 문구가 타임라인의 어느 연도 칸인지는 텍스트 순서로 불확정이며 제3자 점유율은 미확인 | 정정 문구를 "근거 없음"에서 "자사 자료 기준 세계 점유율 1위·21%(2025년도), 제3자 확인 안 됨"으로 바꾸거나 "대형 제조사"를 유지하며 각주 추가. 판단은 메인 | [3][4], reference/raw/case--sws-2030vision-midterm-plan.txt 277·292행 |
| 4 | reference/case--sws-midterm-plan-2028.md | frontmatter published, 핵심 사실 마지막 줄 | "발표 월 미확인", "자동화율의 수치 목표는 확인한 범위에서 찾지 못했다" | 중기계획 발표일 2026-07-16(영문 릴리스) 반영. 수치 목표 슬라이드에 자동화율 없음이 영어판으로 재확인됐다고 추가 | [3][4] |
| 5 | research/q2 출처 [3], research/q3 (해당 없음), reference/case--sws-midterm-plan-2028.md | "2026년도(발표 월 미확인)" | 발표 월 표기 | "릴리스 2026-07-16, 설명 자료 날짜는 미확인"으로 | [3] |
| 6 | research/q3-sumitomo-automation-rate.md | 1절 표 "시점" 행, 5절 영향 표 "50%를 모델 라인 목표" 행 | "모델 라인" 한 곳을 50%의 대상으로 서술 | 각주: 중기계획 로드맵의 "모델 라인"(2027-2028, 스마트 팩토리용)은 별개일 수 있어 같은 라인으로 읽지 않는다 | [4] |
| 7 | research/q3 사용자 피딩 요청 #3 | 3행 | "수치 목표 슬라이드와 20쪽 로드맵 이미지" 미확인 | 영어판 텍스트로 내용 확인(자동화율 없음, 로드맵 영어 확인). 그림 자체는 여전히 미열람이므로 "표·막대 값 매핑"만 남김 | [4] |
| 8 | manual-research.md | 13행·20행·81행 | Q2 #2, Q3 #3 미확인 | 영어판 PDF가 텍스트형이고 이미지는 로고뿐이라는 사실로, "릴리스 구상도 이미지" 중 영문 Skild 릴리스(bc866af8…)는 구상도가 없음을 표시. 일본어 Skild 릴리스(b19d54d9…)도 같은 레이아웃일 가능성이 높으나 그 PDF는 렌더링해 확인하지 않았다 | [1] |
| 9 | knowledge.md | 114행(Q2 정정), 186행(열린 질문), 199행(Skild 본사) | 미공개 목록, 본사 불일치 | 114행은 유지. 199행: 영문판도 "California"라서 住友電装 쪽 표기는 일·영 모두 같음(독립 확인 아님) | [1] |
| 10 | case/analysis.md, case/b4-proposal.md, case/candidates.md | Skild 사실 서술 (b4 80·84·312행, candidates 226행) | "공동 개발을 시작" 서술 | **수정 불필요.** 영문판도 같은 내용이다. 출처에 영문판 reference를 병기하는 정도 | [1] |

### 6. 소스끼리 충돌하거나 확인하지 못한 것
- 일본어판과 영어판 사이의 차이는 위 4절의 두 곳(enable, 주어)뿐이며 사실 내용은 같다. 일본어 원문을 택한다. 이유는 번역본이 원문보다 강하기 때문이다.
- 대표이사 이름의 로마자 표기가 문서마다 다르다(Skild 영문 릴리스 Urushihata, 스마트 팩토리·중기계획 영문 릴리스 Urushibata). 일본어 표기는 漆畑 憲一. 분석에 영향 없음.
- 영어판 중기계획 자료의 "Global Market Share No. 1"이 가리키는 연도와 점유율의 제3자 근거는 미확인. 21%는 자사 표기이다.
- 영어판 PDF의 2쪽 이미지는 렌더링하지 않았다(본문 없음, 링크 안내 페이지).

## RX 관점 시사점
- **고객 제안**: 경쟁 장 서술은 지금 문장 그대로 안전하다. "Skild AI와 住友電装는 2026-09-17 하네스용 피지컬 AI 로봇 공동 개발을 시작했다. 대상 공정, 로봇·핸드 구성, 일정, 성과는 공개되지 않았다." 영문판 확인으로 이 문장에 일본어와 영어 1차 소스를 모두 붙일 수 있다.
- **새로 쓸 수 있는 문장**: 住友電装의 피지컬 AI 로봇은 "사람과 협업해 유연하게 일하는 로봇"으로 정의돼 있고, 같은 회사의 로드맵은 무인화 라인과 협업 라인을 구분한다. 고객 경영진에게는 "협업 라인용 로봇이 사람 작업을 보조·대체하는 구간"이 경쟁 영역일 수 있다는 가설로 제시하되, Skild 프로젝트가 어느 라인용인지 미공개라는 점을 함께 말한다(`추정`).
- **'대형 제조사' 표현**: 住友電装 자체 자료가 세계 점유율 1위·21%를 적고 있으므로 고객 사례 설명에 "자동차 하네스 세계 최대 점유(자사 자료 기준)"를 쓸 수 있다. 외부 검증은 없으므로 "자사 발표"를 붙인다.
- **면접 답변**: "영문판 릴리스도 확인했습니다. 일본어판과 같은 내용이고 달성 시제가 없습니다. 영어판은 'will enable'로 일본어보다 약간 강하게 번역돼 있어 일본어 원문 기준으로 인용했습니다."

## 사용자 피딩 요청 목록
Q2·Q3 목록을 이 PDF 결과로 갱신한 것이다. 아직 못 구한 자료만 남긴다. 우선순위 순.

| # | 무엇을 | 왜 필요한가 | 어디서 / 누구에게 | 상태 |
|---|--------|-------------|-------------------|------|
| 1 | Skild 블로그 S1(https://www.skild.ai/blogs/s1)과 Hidden Pillar(https://www.skild.ai/blogs/skild-crosses-100m-arr)의 **영상·이미지** (Foxconn 셀 영상 포함) | end-effector 형태, 로봇 대수, 카메라 위치를 눈으로 확인할 수 있는 유일한 직접 증거 후보 | 사용자가 브라우저로 직접 시청, 손 부분 캡처 | 미해결 (Q2 #1) |
| 2 | 住友電装 **일본어판** Skild 릴리스 PDF(b19d54d9…)와 스마트 팩토리 릴리스(prs039, 일·영)의 **그림 이미지** (prs039에는 "Smart Factory Concept Image" 캡션이 있음) | 구상도에 로봇 배치나 공정이 그려져 있을 수 있음. 이번 영문 Skild 릴리스에는 구상도가 없었다. 구상도는 스마트 팩토리 릴리스(prs039)에 있을 가능성이 크다. 텍스트 변환에는 그림이 빠진다 | 사용자가 PDF를 열어 구상도 캡처 | 일부 해소(영문 Skild 릴리스는 구상도 없음 확인). prs039 구상도는 미열람 (Q2 #2) |
| 3 | 영어판·일본어판 중기계획 PDF 17쪽(수치 목표)과 20쪽(로드맵)의 **그림 자체** | 막대그래프 값(88%, 85%, 12%, 15%, 22,889)의 연도·사업 대응, "Global Market Share No. 1"이 가리키는 연도 | https://www.sws.co.jp/resource/pdf/corporation-strategy_en.pdf 17·11·12쪽을 사용자가 확인 | 부분 해소(자동화율 없음은 확인). 값 매핑은 미해결 (Q3 #3) |
| 4 | 日経, 日刊工業, 日刊自動車 등 일본 신문·전문지의 독자 취재 기사 (住友電装 スキルド) | 대상 공정, 담당자 발언, 실증 공장 | 사용자의 일본 신문 DB, 도서관 DB | 미해결 (Q2 #4) |
| 5 | 住友電装 광보(TEL 059-354-6201, sws.sm.public-relations@sws.com. 릴리스에 기재)에 대한 공개 문의 결과: 대상 공정, 핸드, 15%/50% 정의 | 두 질문을 직접 확인. RLWRLD 업무로 접촉할지는 사용자 판단 | 사용자 | 미해결 (Q2 #7, Q3 #7) |
| 6 | 住友電工 통합보고서·유가증권보고서(2023~2025)의 "自動化率" 표기, 日刊自動車新聞 2023-09-20 기사 전문, IZB 2026 住友 페이지(404) | 자동화율 정의, 분할 하네스 일정 | Q3 피딩 요청 #1, #2, #4~#6 그대로 | 미해결 |
| 7 | (선택) 자동차용 하네스 세계 점유율의 제3자 자료(예: 시장조사 보고서)와 住友電装 "グローバルシェアNo.1" 주장의 연도 | 5절 #3의 '1위' 표현을 제3자 자료로 뒷받침 | 사용자의 시장조사 DB, 업계 보고서 | 신규 |

## 출처
1. [Sumitomo Wiring Systems and U.S.-Based Skild AI Launch Joint Development of Physical AI Robots for Wire Harness Manufacturing](https://www.sws.co.jp/en/sws-news/docs/bc866af8854aeec61a4d844ec2d41e56c747b051.pdf) - 住友電装, 2026-09-17, 1차, (en) (reference/case--sws-skild-release-en.md)
2. [住友電装と米国 Skild AI、ワイヤーハーネス製造向けフィジカル AI ロボットの共同開発を開始](https://www.sws.co.jp/sws-news/docs/b19d54d9f74ad881f5f8aad4606784b9359d8ff2.pdf) - 住友電装, 2026-09-17, 1차, (ja) (reference/case--sws-skild-joint-dev-release.md) - 영문판과 대조한 원문
3. [Announcement of Sumitomo Wiring Systems Group's "2030 VISION Mid-Term Management Plan 2028"](https://www.sws.co.jp/en/sws-news/docs/b8de6a78c7afc5824832e5c1cc7ec074ca956b5e.pdf) - 住友電装, 2026-07-16, 1차, (en) (reference/case--sws-midterm-release-en.md)
4. [Sumitomo Wiring Systems Group 2030VISION / Mid-term Management Plan 2028 Explanatory Material (English)](https://www.sws.co.jp/resource/pdf/corporation-strategy_en.pdf) - 住友電装, 날짜 미확인, 1차, (en) (reference/case--sws-midterm-plan-2028-en.md). 일본어판: reference/case--sws-midterm-plan-2028.md
5. [The Hidden Pillar of Robotics](https://www.skild.ai/blogs/skild-crosses-100m-arr) - Skild AI, 2026-09-10, 1차, (en) (reference/competitors--skild-hidden-pillar.md)
6. [Sumitomo Wiring Systems Advances Its Smart Factory Concept Through the Collaboration of AI Agents and Physical AI Robots](https://sumitomoelectric.com/sites/default/files/2026-09/download_documents/prs039.pdf) - 住友電装, 2026-09-17, 1차, (en) (reference/case--sws-smartfactory-release.md) - 본문에서 직접 인용하지 않고 구상도 위치 설명에만 참조
