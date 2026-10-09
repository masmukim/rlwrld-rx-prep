---
name: sws-pdf-research-notes
description: 住友電装 사이트 PDF를 다룰 때 통한 방법 - 영문/일문 짝 찾기, 이미지 확인, 안내 HTML 구조
metadata:
  type: reference
---

- sws.co.jp 릴리스는 일본어(`/sws-news/docs/<hash>.pdf`)와 영어(`/en/sws-news/docs/<hash>.pdf`)의 해시가 서로 다르다. URL 중복 확인만으로는 "같은 문서의 번역본"을 못 잡으므로, 새 PDF를 받으면 기존 raw와 문장 대조까지 한다.
- 영문 HTML 안내 페이지 `/en/sws-news/2026/091713NN.html`(NN 연속 ID, 32=스마트팩토리, 33=ExaWizards, 34=Skild)은 제목, 날짜, PDF 용량만 있고 본문이 없다. 인접 ID를 순서대로 열면 짝을 찾을 수 있다(30, 31은 404).
- `https://www.sws.co.jp/en/corporation/strategy.html`에 중기계획 일·영·중 PDF 링크가 있다. 영어판(`/resource/pdf/corporation-strategy_en.pdf`)은 일본어판보다 슬라이드 표 텍스트가 읽기 쉽다. 일본어판에서 못 읽은 슬라이드는 영어판으로 먼저 시도한다.
- 텍스트형 PDF인지 이미지형인지 확인: `strings`로 `/Subtype/Image`와 `/Count`를 보고, macOS `qlmanage -t -s 1400 -o <dir> file.pdf`로 1쪽 PNG를 만들어 Read로 본다. pdftoppm, mutool, PIL은 없다. 링크 주소는 `.venv/bin/python -I -c "import pypdf..."`로 `/Annots`의 `/URI`를 읽는다(이미지 추출은 PIL 부재로 불가).
- 다운로드 파일은 scratchpad 하위 폴더에 두고 `-I`로 실행한다.
- 실수: 이전 작업이 "근거 없음"으로 정정한 항목(업계 1위권)을 같은 회사의 다른 1차 자료(중기계획 "グローバルシェアNo.1", 세계 점유율 21%)가 뒷받침했다. fact-check 정정이 "근거 없음"이라고 쓰기 전에 회사 자체 소개 슬라이드를 grep했는지 확인할 것.
- 영어판 번역이 일본어 원문보다 강해지는 패턴이 반복된다(enable, 주어 추가, has been increased). 영문판만 받았을 때도 일본어판과 시제를 대조한다.
