---
name: wage-research-notes
description: 한국 임금·사업주 보험료·최저임금 조사(Q8)에서 통한 1차 소스, 막힌 곳, WebSearch 요약 오류 패턴
metadata:
  type: reference
---

- 잘 열린 1차: moel.go.kr 보도자료(news_seq=19744 등, 최저임금), mohw.go.kr board.es(건보·장기요양 요율), nps.or.kr(연금 보험료), comwel.or.kr/comwel/paym/insu/chek3.jsp(고용보험 표), kbiz.or.kr download.do(중기중앙회 임금조사 PDF), law.go.kr lsPdfPrint(법령 텍스트), easylaw.go.kr.
- 막힘/불가: 산재 업종별 요율표(hwp 첨부), albamon(JS), futurechosun(연결 끊김), DART, 잡플래닛.
- 검색어: "2027년 적용 최저임금 고시", "중소제조업 직종별 임금조사 2026 부품조립원", "사업종류별 산재보험료율 2026".
- WebSearch 요약 오류 사례: 산재 1.47%를 "제조업 평균"이라 라벨(실제 전 업종 평균), 최저임금 표결 "17대 11"(1차는 11/15/무효1). 수치는 1차 raw로 대조.
- 기사 속 직종명은 직종해설과 대조: 중기중앙회 '전선원'은 코일 권선공이지 하네스 조립원이 아님.
- 경총 "임금총액"은 정액+특별(초과 제외)이라 산술(418.8 = 363.8 + 55.0)로 정의를 역추적할 수 있음. 앞서 문서의 "초과 포함" 서술이 틀렸던 사례.
- 일급 정의(중기중앙회): 기본급+통상수당, 주휴·식대 제외, /월정상근로시간 x 8h. 연장·야간 가산 미포함이라 시급 = 일급/8.
- 실수: 한 번에 reference 파일 여러 개를 Write할 때 Write에 `title` 같은 잘못된 파라미터를 넣어 실패한 적 있음. file_path와 content만 쓴다. 인용문 안에 타이핑 실수가 들어가지 않게 raw에서 복사한다.
