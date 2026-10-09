# Q2. Skild AI x 住友電装(Sumitomo Wiring Systems) 와이어 하네스 프로젝트: 범위, 결과, end-effector, 구성
조사일: 2026-10-09

## 핵심 요약
- **공개된 사실은 "2026-09-17에 공동 개발을 시작했다"까지다.** 住友電装 보도자료는 Skild AI의 최신 모델 S1을 도입해 하네스 제조용 피지컬 AI 로봇을 공동 개발한다고만 쓰고, 대상 공정, 로봇·핸드·센서, 일정, 성능, 투자액은 하나도 적지 않았다 [1][2]. Skild 블로그의 시제도 "배치를 향해 일하는 중(working towards deploying)"이다 [5]. 따라서 "Skild가 이미 住友電装의 하네스 조립을 자동화하고 있다"는 기존 문서(research/skild-pi-deep-dive.md, case/b4-proposal.md)의 서술은 본문보다 강했다. 아래 4개 질문에 대한 답은 모두 **미공개**이며, 간접 근거로 만든 것은 `추정`으로 표시했다.
- **end-effector(다관절 손인가 그리퍼인가)는 어떤 공개 소스에서도 확인되지 않는다.** 확인되는 Skild 제조 사례는 양팔(dual-arm) 매니퓰레이터(Foxconn)와 ABB·UR 로봇 탑재까지이고 [5][14], Skild 공개 자료에 다관절 손을 쓴 제조 사례는 없다. "Skild는 손을 안 쓴다"도 확인된 사실이 아니다.
- **B4의 "레이업 단계가 우리 차별점"은 지금 근거로는 주장할 수 없다.** Skild가 어느 단계를 하는지 공개된 적이 없으므로 "Skild는 레이업을 하지 않는다"는 전제가 성립하지 않는다. 안전한 문장은 "Skild-住友電装의 대상 공정은 미공개이며, 우리는 손이 필요한 구간을 PoC에서 그리퍼 대조군과 함께 검증한다"이다 (시사점 절 참고).

## 1. 질문별 답과 확인 수준
확인 수준: **1차** = 住友電装·Skild 공식 문서, **기사** = 2차 보도, `추정` = 간접 근거로 만든 해석, **미공개** = 찾은 어떤 소스에도 없음.

| 질문 | 답 | 확인 수준 | 근거 |
|------|----|-----------|------|
| 범위: 어느 공정 단계(프리블록, 레이업, 테이핑 등)? | **공정 이름 미공개.** "ワイヤーハーネス製造向け(하네스 제조용)", "하네스 제조의 공정들(processes)"이라는 표현뿐 | 미공개 | [1][5] |
| 결과: 성능? | **없음.** 성공률, 사이클 타임, 인력 절감 수치 모두 미공개 | 미공개 | [1][2][5] |
| 결과: 일정? | 프로젝트 단독 일정은 없음. 住友電装 회사 로드맵만 있음 (2025-2026 기반 확립·현장 실증, 2027-2028 국내 모델 라인, 2030 글로벌 전개) | 1차(회사 전체 계획) | [3][4] |
| 결과: 상용화 여부? | **상용 배치 아님.** 공동 개발 개시(2026-09-17) 단계. Skild는 "deploying을 향해 일하는 중"이라고 씀 | 1차 | [1][5] |
| end-effector | **미확인.** 다관절 손 증거도, 그리퍼 증거도 없다 | 미공개 | 3.3절 |
| 로봇·센서 구성 | **미공개.** Foxconn 셀(양팔, 힘 제한 접촉 제어)의 구성을 住友電装 프로젝트에 적용할 근거가 없다 | 미공개 | 3.4절 |

## 2. 확인된 시간순 사실
| 날짜 | 사실 | 소스 | 수준 |
|------|------|------|------|
| 2026-08-18 | Skild, S1 공개. 영상 시연 1개로 과제를 지정하는 in-context learner | [6] | 1차 |
| 2026-08-27 | Skild CEO 인터뷰(TechBlitz)에서 일본 협업처로 "住友, 三井など" 언급. 이름을 못 밝히는 기업도 있다고 함 | [8] | 기사 |
| 2026-09-10 | Skild 블로그: "At Sumitomo Wiring Systems, we are working towards deploying S1 to automate processes in wire harness manufacturing that were considered 'impossible' to automate" (Securities.io는 9월 9일 게시로 보도, 블로그 목록은 9월 10일) | [5] | 1차 |
| 2026-09-17 | 住友電装, Skild AI와 하네스 제조용 피지컬 AI 로봇 **공동 개발 개시** 발표. S1 도입. 같은 날 ExaWizards(AI 에이전트)와 스마트 팩토리 구상 릴리스 | [1][2][4] | 1차 |
| 2026-09-25 | 일본 매체 Response.jp가 보도자료를 그대로 전함. 독자 취재 정보 없음 | [7] | 기사 |

일본어 기사는 이 한 건만 찾았다. 일본 경제지·전문지(日経, 日刊工業, 日刊自動車 등)의 독자 취재 기사는 검색에 잡히지 않았다 (유료 또는 미색인 가능성, 확인 불가).

## 3. 질문별 상세

### 3.1 범위: 어느 공정인가
**공정 단계를 특정하는 문장은 1차 소스에도 기사에도 없다.** 住友電装 릴리스는 배경으로 "하네스 제조는 복잡한 공정이 많아 기존 로봇 기술로 대체하기 어려워 수작업에 의존해 왔다"고만 쓴다 [1]. Skild는 "automate processes in wire harness manufacturing"이라고 복수의 공정을 일반적으로 말한다 [5]. Humanoids Daily는 "변형 전선(deformable wiring)을 기존 컴퓨터 비전 시스템이 잡지 못한다"는 설명을 붙였으나, 이 설명은 Skild 블로그 원문에 없는 기자의 서술이다 [9][5 대조].

간접 근거로 후보를 좁힐 수는 있다. 아래는 모두 `추정`이며 Skild 프로젝트의 범위를 확인해 주지 않는다.

| 간접 근거 | 내용 | 후보를 어느 쪽으로 미나 | 한계 |
|-----------|------|--------------------------|------|
| 住友電装 자체 구조 | 에어리어 하네스 슬라이드에 "간선: e-STEALTH W/H, 지선(枝線): 종래 공법"으로 표시. 구조 단순화로 생산 공정 자동화를 실현한다고 서술 [3] | 자동화 설계가 닿는 간선 대신, 종래 공법으로 남는 지선 쪽 손작업이 로봇 대상일 수 있다 | 슬라이드에 Skild 대상이 적혀 있지 않다 |
| 住友電装의 과거 로봇화 후보 | 2015년 NEDO 사업(オートネットワーク技術研究所와 공동)이 케이블 **분기·결속, 클램프 장착, 외장품 장착**을 로봇화 대상으로 삼고 **복수의 로봇 핸드**+비전을 구상 (WebFetch 요약, 기사) [10] | 분기·결속, 클램프, 외장품 장착 같은 하네스 후반 공정 | 2015년 자료이고 Skild와 무관 |
| 공개 문헌의 병목 | 참고 라인 연구(EasyChair)에서 병목은 레이업이었고 프리블록 7, 레이업 3, 테이핑 12 작업장으로 구성 [13] | 레이업이 사람 수가 몰리는 곳 | 특정 라인 하나의 연구이며 住友電装 라인이 아님 |
| Skild 인터뷰 예시 | CEO가 과제 예시로 "GPU 조립, 칩 제조, 配線を束ねたい(배선을 묶고 싶다)"를 들었다 [8] | 배선 결속(bundling) 쪽 | 일반 예시이고 住友電装를 지목한 발언이 아님 |

종합하면 `추정`으로 "지선 쪽 분기·결속·클램프 장착처럼 케이블을 직접 다루는 구간이 대상일 수 있다"까지는 말할 수 있다. 프리블록(단자 삽입), 레이업, 테이핑 중 어디라고 특정할 근거는 없다. 이 추정은 확정이 아니므로 B4 본문에는 쓰지 말고 "미공개"로 둔다.

### 3.2 결과: 성능, 일정, 상용화
- **성능 수치는 없다.** 두 회사 어느 쪽도 이 프로젝트의 성공률, 사이클 타임, 절감 인력을 발표하지 않았다 [1][2][5].
- **상용화는 아직이다.** 住友電装는 "공동 개발을 시작"했고 [1], 자사의 피지컬 AI 로봇 "개발·현장 실증에 임하고 있다"고 쓴다 [1]. 이 문장은 회사 전반의 활동을 말한 것이고, Skild 로봇이 이미 住友電装 현장에서 가동 중이라는 뜻으로 읽을 수 없다. Skild 쪽 문장은 "deploying을 향해 일하는 중"이다 [5].
- **일정은 회사 로드맵으로만 짐작한다.** 2025-2026 기반 확립·현장 실증 ("현장에서 AI 로봇 실증 실험 시작"), 2027-2028 국내 모델 라인 구축, 2030 글로벌 전개 [3][4]. 이 로드맵이 Skild 프로젝트의 마일스톤이라는 명시는 없다. 두 가지를 이어 읽는 것은 본 조사의 해석(`추정`)이다.
- **Skild의 일반 성능 주장은 하네스 성능이 아니다.** S1의 "처음 보는 장기 과제에서 66% 대 언어 프롬프트 기준선 9%"는 내부 벤치마크의 누적 단계별 성공률이며 (과제 길이 4~8분), 전 단계를 채점하려고 **실패 때 사람이 개입해 복구**했다. 시연 2,000개로 post-training하면 86%라고도 밝혔다 [6]. 시연 과제 예시는 plant potting, pancake, coffee, kit assembly이고 하네스는 없다 [6]. 이 수치를 住友電装 프로젝트의 기대 성능으로 옮기면 안 된다. 참고로 공개 학술 연구의 하네스 조립 수준은 양팔 로봇의 다분기 하네스 조립이 실제 조립 시나리오 2개에서 성공률 55%와 73%였다 [11] (평가 조건이 달라 직접 비교는 불가).
- **매출 기여는 미확인이다.** Skild의 ARR 1억 달러, 유료 고객 60곳 이상 [5]에 이 프로젝트가 포함되는지 알 수 없다. Humanoids Daily는 住友電装를 고객 목록에 올렸지만 [9], Skild 원문은 Foxconn은 "deploying", 住友電装는 "working towards deploying", Mitsui는 "piloting"으로 구분해 쓴다 [5].

### 3.3 end-effector: 다관절 손인가 그리퍼인가
**결론: 확인되지 않는다.** 찾은 소스별로 정리한다.

| 소스 | end-effector 관련 내용 | 결론에 주는 정보 |
|------|------------------------|------------------|
| 住友電装 릴리스 3종 [1][2][3] | 로봇 형태, 손, 그리퍼 언급 없음. 로봇을 "최신 AI 두뇌를 갖고 사람과 협업해 유연하게 작업하는 차세대 로봇"으로만 정의 | 없음 |
| Skild 하네스 문장 [5] | 로봇 형태 언급 없음 | 없음 |
| Skild Foxconn 셀 [5][9] | 양팔(dual-arm) 매니퓰레이터. 모선 삽입, limit block 위치 지정, 접촉 인지 힘 임계값 아래 나사 16개 체결 | 팔 계열 로봇. 손 형태는 미기재. **住友電装 프로젝트의 구성이라는 증거는 아님** |
| Skild S1 블로그 [6] | 본문 텍스트에 손·그리퍼 언급 없음. 로버스트니스 시험 L5가 "반대쪽 팔로 절반의 동작을 수행"이라 쓰여 평가 로봇이 팔 2개 이상임을 시사 | 그림·영상은 텍스트로 추출되지 않아 **end-effector 형태 미확인** |
| Skild 사업 모델 [8] | 고객이 하드웨어를 가지면 두뇌를 그 위에 올리고, 없으면 Skild가 하드웨어를 찾아 서비스로 제공. Skild 공식 문서는 "특정 하드웨어에 의존하지 않는" 모델이라고 소개 [1] | 하드웨어가 프로젝트마다 다를 수 있다는 구조 |
| ABB, UR 탑재 [14] | 산업용 로봇·협동로봇 포트폴리오에 Skild Brain 탑재. 그리퍼·팔 중심 | 산업용 팔 계열이 Skild의 주 채널 |

`추정`: 확인되는 Skild 제조 배치는 모두 산업용 팔 계열이고 다관절 손을 쓴 제조 사례는 공개 자료에 없으므로, 住友電装 프로젝트도 팔+범용 end-effector일 가능성이 다관절 손보다 높다고 볼 수 있다. 다만 이 판단은 **다른 고객 사례에서 옮긴 것**이다. 정면 근거가 아니며, 영상이나 현장 사진으로 직접 확인하기 전까지는 "미확인"이 정답이다. 반대로 "다관절 손을 쓴다"를 뒷받침하는 소스도 하나도 없다. 참고로 하네싱 연구에는 팔 1대+힘/토크 센서만으로 비틀기 동작으로 전선을 클램프에 끼우는 접근도 있어 [12], 하네스 공정이 곧 다관절 손을 요구하는 것은 아니다.

### 3.4 로봇·센서 구성
- 공개된 구성 정보는 **없다.** 어떤 로봇, 몇 대, 카메라 구성, 힘·촉각 센서 여부 모두 미공개 [1][2][5].
- 참고로 Skild의 Foxconn 셀은 "양팔 + 힘 제한 접촉 제어"로 서술된다 [9]. 이는 Humanoids Daily의 설명(기사)이며 Skild 블로그는 양팔 매니퓰레이터와 작업 순서까지만 쓴다 [5].
- 학습 방식은 공개되어 있다: S1은 영상 시연 1개를 프롬프트로 받는다 [6]. 현장 세팅, 시연자(작업자 착용 카메라 여부), 미세조정 여부는 住友電装 건에 대해 공개되지 않았다. Skild 인터뷰에서 CEO는 초기 단계에는 Skild가 직접 미세조정해 제공한다고 말했다 [8].

### 3.5 소스 간 표현 강도와 불일치
| 항목 | 소스별 표현 | 택한 쪽과 이유 |
|------|-------------|----------------|
| 프로젝트 단계 | 住友電装: "共同開発を開始" [1]. Skild: "working towards deploying" [5]. Humanoids Daily: "Automating wire harness assembly" [9] | 1차 두 개를 택함. 기사는 시제를 강하게 바꿨다 |
| Skild 본사 | 住友電装 릴리스: 미국 캘리포니아주 [1]. 기존 문서(skild-pi-deep-dive): 피츠버그 | 미해결. 이번 질문과 직접 관련 없어 확정하지 않음 |
| Skild 블로그 게시일 | 블로그 목록 9월 10일, Securities.io 9월 9일 | 날짜 차이만 있고 내용 영향 없음 |
| 검색 요약 | 검색 도구의 일부 요약은 "住友電装 영문 릴리스에 Skild 이름이 없다"고 답했으나, 원문 PDF에는 Skild AI가 명시되어 있다 [1][2] | 원문 대조로 해소. 요약만 보고 판단하지 않는다 |

## RX 관점 시사점

### B4의 "레이업 단계가 우리 차별점" 주장은 어떻게 달라지는가
| 현재 B4 문구 (case/b4-proposal.md 80행 등) | 이 조사 결과 | 수정 방향 |
|--------------------------------------------|--------------|-----------|
| "Skild AI가 이미 住友電装의 하네스 조립을 자동화하고 있다" | 공동 개발 개시(2026-09-17) 단계. 범위·결과 미공개 [1][5] | "Skild AI와 住友電装가 2026-09-17 하네스용 피지컬 AI 로봇 **공동 개발을 시작**했다. 범위와 결과는 공개되지 않았다" |
| "RLWRLD의 차별점은 새 품번 적응이 아니라 손이 꼭 필요한 레이업 단계에 있다" | Skild가 레이업을 하는지 안 하는지 모른다. "Skild가 못 하는 단계"라는 전제는 근거가 없다 | 차별점을 "상대가 못 하는 단계"에서 **"우리가 검증 가능한 단계"**로 바꾼다. 손이 필요한지는 그리퍼 대조군 PoC로 확인한다 (B4가 이미 이 검증을 항목으로 둠) |
| 상대 end-effector를 암묵적으로 그리퍼로 가정하는 서술이 있다면 | 어떤 소스도 확인하지 않는다 | 가정하지 않는다. "Skild의 end-effector는 미공개"라고 쓴다 |
| "시연으로 새 품번 적응"은 Skild S1도 주장한다 | 맞다. 다만 66%는 사람 개입이 포함된 누적 단계 점수이고 하네스가 아니다 [6] | 이 부분은 그대로 유지: 시연 기반 적응은 차별점이 아니다 |

### 이 결과가 RLWRLD에 주는 의미 (해석, `추정` 포함)
1. **경쟁이 아니라 "아직 열려 있는 단계"로 읽는 편이 정확하다.** 住友電装는 2025-2026을 실증 단계, 2027-2028을 모델 라인 구축으로 두며 [3][4], Skild 프로젝트는 그 초기에 시작했다. 성과가 나오기 전이므로 하네스 자동화의 범위는 아직 확정되지 않았다. 다만 이것이 RLWRLD의 진입 여지라는 해석은 `추정`이다. 住友電装는 같은 날 AI 에이전트는 ExaWizards와 별도로 협업을 시작해 [4], 영역별로 파트너를 나누는 방식을 쓴다는 것은 확인된다.
2. **일본 하네스 1위권이 Skild를 선택했다는 사실 자체가 시장 신호다.** 住友電装는 자체 보도자료에서 하네스를 "기존 로봇 기술로 대체하기 어려워 수작업에 의존"한다고 규정한다 [1]. B1의 문제 정의(수작업 비중)를 업계 1위권이 공식 확인한 문장으로 인용할 수 있다. 단 이 문장은 수치(수작업 비중)를 주지 않는다.
3. **사이클 타임 논리는 유지된다.** Skild 창업자는 "정확도 99.9%라도 10배 느리면 배포 불가"라고 쓴다 [5]. B4의 1순위 KPI(속도비)와 일치한다.
4. **면접·고객 질문 대비.** "Skild가 住友電装에서 이미 하고 있지 않은가?"에는 "공동 개발이 2026-09-17에 시작됐고, 대상 공정과 end-effector, 성과는 공개되지 않았다. 우리는 공개된 사실과 우리 PoC 설계를 구분해서 말한다"라고 답할 수 있다. 위 3.1절의 추정(지선, 분기·결속 쪽)은 "가설"이라고 밝혀야 하며 사실처럼 말하면 안 된다.

### B4에 반영할 때 확인할 항목 (수정은 메인이 결정)
- case/b4-proposal.md 80, 84, 309행: "이미 자동화하고 있다 (기사)" 표현을 위 수정안으로 교체. 309행 "사실 | ... (기사)"는 이제 1차 소스 [1]로 대체 가능.
- case/b4-proposal.md 321행의 "Skild × 住友電装 프로젝트의 범위와 결과, Skild의 손 하드웨어"는 **여전히 미확인**으로 남긴다. 이번 조사로 해소되지 않았다.
- research/skild-pi-deep-dive.md 3.2절 표의 "결과 미공개"는 맞으나 '고객'으로 올린 분류는 약하다. 1차 소스 기준으로는 "공동 개발 개시".
- knowledge.md 105행("Skild AI가 住友電装의 와이어 하네스 조립을 자동화하고 있다")과 열린 질문 164행은 갱신 대상.

## 사용자 피딩 요청 목록
접근 불가(로그인, 유료, 비공개)이거나 사용자만 얻을 수 있는 자료다. 우선순위 순.

| # | 무엇을 | 왜 필요한가 | 어디서 / 누구에게 | 접근 상태 |
|---|--------|-------------|-------------------|-----------|
| 1 | Skild 블로그 S1(https://www.skild.ai/blogs/s1)과 Hidden Pillar(https://www.skild.ai/blogs/skild-crosses-100m-arr)의 **영상·이미지** (Foxconn 셀 영상 포함) | end-effector 형태(그리퍼인지 손인지), 로봇 대수, 카메라 위치를 눈으로 확인할 수 있다. 텍스트 추출에는 영상이 없다. 질문 3.3의 유일한 직접 증거가 될 수 있다 | 사용자가 브라우저로 직접 시청. 가능하면 손 부분 캡처 또는 한 줄 설명 | 텍스트만 확보, 영상 미열람 |
| 2 | 住友電装 보도자료 PDF의 **구상도 이미지** (https://www.sws.co.jp/sws-news/docs/c6868a7b4550762234a752fea8961dfb4cf68761.pdf 의 "スマートファクトリー構想イメージ図", Skild 건 https://www.sws.co.jp/sws-news/docs/b19d54d9f74ad881f5f8aad4606784b9359d8ff2.pdf 도) | 그림에 로봇이 놓이는 공정 단계나 로봇 형태가 그려져 있을 수 있다. 텍스트 변환에서 이미지는 빠졌다 | 사용자가 PDF를 열어 구상도 캡처 | 이미지 미열람 |
| 3 | 住友電装 「2030ビジョン 中期経営計画2028」 PDF(https://www.sws.co.jp/resource/pdf/corporation-strategy_jp.pdf)의 **수치 목표 슬라이드**(「30V・28Mの数値目標」)와 20쪽 로드맵 슬라이드 이미지 | 자동화율 목표, 모델 라인 구체 수치 확인. 텍스트에서는 표 값이 읽히지 않았다. 열린 질문 "자동화율 15%/50%의 정의"에도 관련 | 사용자가 PDF 해당 쪽 확인 | 표·그림 값 미확인 |
| 4 | 日経, 日刊工業, 日刊自動車 등 **일본 신문·전문지의 독자 취재 기사** (キーワード: 住友電装 スキルド / Skild AI フィジカルAI) | 보도자료 이상의 정보(대상 공정, 담당자 발언, 실증 공장)가 있을 가능성. 지금 확보한 일본어 기사는 보도자료 재게재 1건뿐이다 | 사용자의 일본 신문 DB 구독(가능할 경우), 도서관 DB | 유료·미색인 가능성. 검색에 안 잡힘 |
| 5 | MarkLines 기사 전문 (https://www.marklines.com/en/news/351047, "Gen-AI Analysis: Sumitomo Wiring Systems steps up smart factory initiative...") | 보도자료 요약 이상의 분석이 있을 수 있음 | MarkLines 무료 회원 가입 시 "일정 기간 열람 가능"이라고 안내됨. 사용자 가입 필요 | 유료/회원제. 첫 문단만 열림 |
| 6 | Skild CEO Deepak Pathak의 **X(Twitter) 게시물 원문** (Digital Today가 "ARR 1억 달러 게시"로 인용) | 블로그와 같은 내용일 가능성이 높으나, 추가 영상·답글에서 住友電装 영상이 있을 수 있다 | 사용자가 X에서 직접 확인 | **시도하지 않음.** X는 로그인 벽이 일반적이라 시도를 생략했다 |
| 7 | 住友電装 広報·CSR G(공개 문의처 TEL 059-354-6201, Email sws.sm.public-relations@sws.com. 릴리스에 기재된 연락처)에 대한 **공개 문의 결과** | 대상 공정, end-effector, 실증 장소의 공개 가능 범위를 직접 확인. 다만 RLWRLD 업무로 접촉할지는 사용자 판단 | 사용자가 (RX 팀 입장에서 접촉이 적절하다고 판단할 때) 문의 | 공개 정보로는 불가 |
| 8 | Skild AI **채용 공고** (hardware/robotics engineer, "end effector", "hand" 키워드) | 자체 하드웨어 개발 방향(손 개발 여부)의 간접 단서 | Skild 채용 페이지, LinkedIn. 로그인이 필요할 수 있음 | 이번 조사에서 확인 안 함 |
| 9 | 일본 展示会·세미나 자료 (자동차 부품·로봇 전시회에서 住友電装 또는 Skild Japan이 발표한 자료) | 시연 영상 또는 슬라이드로 공정을 확인할 가능성 | 일정은 사용자가 확인. 이번 조사에서 해당 발표를 찾지 못함 | 확인 불가 |

접근 시도에서 막혔거나 쓸 수 없던 것 (기록용): NEDO PDF(nedo.go.jp/content/100095321.pdf)는 404로 열리지 않았고 검색 요약에서도 다른 사업의 보고서로 확인됨. MONOist 2015 기사는 문자 인코딩이 깨져 원문 Grep이 불가하여 WebFetch 요약으로만 인용했다 [10].

## 출처
1. [住友電装と米国 Skild AI、ワイヤーハーネス製造向けフィジカル AI ロボットの共同開発を開始](https://www.sws.co.jp/sws-news/docs/b19d54d9f74ad881f5f8aad4606784b9359d8ff2.pdf) - 住友電装, 2026-09-17, 1차, (ja) (reference/case--sws-skild-joint-dev-release.md)
2. [Sumitomo Wiring Systems Advances Its Smart Factory Concept Through the Collaboration of AI Agents and Physical AI Robots](https://sumitomoelectric.com/sites/default/files/2026-09/download_documents/prs039.pdf) - Sumitomo Electric / Sumitomo Wiring Systems, 2026-09-17, 1차, (en) (reference/case--sws-smartfactory-release.md)
3. [住友電装グループ 2030ビジョン 中期経営計画2028](https://www.sws.co.jp/resource/pdf/corporation-strategy_jp.pdf) - 住友電装, 2026년도(발표 월 미확인), 1차, (ja) (reference/case--sws-midterm-plan-2028.md)
4. [住友電装、エクサウィザーズとフィジカルAI技術を活用した「グローバルの生産現場で稼働するAIエージェント群」を共同開発](https://www.sws.co.jp/sws-news/docs/bbf1495080b19e16ec19fdab2df66eee498e9c48.pdf) - 住友電装, 2026-09-17, 1차, (ja) (reference/case--sws-exawizards-release.md)
5. [The Hidden Pillar of Robotics](https://www.skild.ai/blogs/skild-crosses-100m-arr) - Skild AI, 2026-09-10, 1차, (en) (reference/competitors--skild-hidden-pillar.md)
6. [Introducing S1: In-Context Learning for Robotics](https://www.skild.ai/blogs/s1) - Skild AI, 2026-08-18, 1차(자체 평가), (en) (reference/competitors--skild-s1-blog.md)
7. [住友電装とスキルドAI、ワイヤーハーネス製造向けフィジカルAIロボットを共同開発](https://response.jp/article/2026/09/25/416974.html) - レスポンス, 2026-09-25, 기사, (ja) (reference/case--response-sws-skild.md)
8. [フィジカルAI導入「整ってから」だと遅い Skild AI共同創業者インタビュー後編](https://techblitz.com/startup-interview/skild-ai2/) - TECHBLITZ, 2026-08-27, 기사(인터뷰), (ja) (reference/competitors--skild-techblitz-interview2.md)
9. [Skild AI Crosses $100M ARR in 10 Months...](https://www.humanoidsdaily.com/news/skild-ai-crosses-100m-arr-in-10-months-mounting-an-enterprise-assault-on-robotics-demo-culture) - Humanoids Daily, 2026-09, 기사, (en) (reference/competitors--skild-arr-humanoidsdaily.md)
10. [産業用ロボット(3/4) NEDO ワイヤーハーネス製造自動化の実用化技術開発](https://monoist.itmedia.co.jp/mn/spv/1508/14/news028_3.html) - MONOist, 2015-08-14, 기사(WebFetch 요약만, 원문 저장본 깨짐), (ja) (reference/case--monoist-nedo-harness-2015.md)
11. [A dual-arm robotic system for automated multi-branch wire harness assembly in automotive industry](https://researchportal.tuni.fi/en/publications/a-dual-arm-robotic-system-for-automated-multi-branch-wire-harness/) - Journal of Manufacturing Systems 83, 2025-12, 논문, (en) (reference/papers--dual-arm-multibranch-harness.md) - 본문에서는 하네스 자동화의 공개 연구 수준(실제 조립 시나리오 2개에서 성공률 55%, 73%)을 비교 맥락으로 참고
12. [Harnessing with Twisting: Single-Arm Deformable Linear Object Manipulation for Industrial Harnessing Task](https://arxiv.org/abs/2410.10729) - arXiv, 2024-10-14, 논문, (en) (reference/papers--single-arm-harnessing.md) - 비교 맥락 참고
13. [Improvement of an Assembly Line in the Automotive Industry: A Case Study in Wiring Harness Assembly Line](https://easychair.org/publications/preprint/qSks/open) - EasyChair Preprint No. 10031, 2023-05-09, 논문(프리블록·레이업·테이핑 작업장 구성과 레이업 병목), (en) (reference/case--easychair-harness-line-balancing.md)
14. [The Reindustrial Revolution: Partnering with ABB Robotics, Universal Robots, and NVIDIA](https://www.skild.ai/blogs/reindustrial-revolution) - Skild AI, 2026-03-19, 1차, (en) (reference/competitors--skild-abb-ur-foxconn.md)
