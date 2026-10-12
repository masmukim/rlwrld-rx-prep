---
name: xlsx-recalc-without-libreoffice
description: 이 환경에는 LibreOffice가 없어 openpyxl 수식 셀에 캐시 값이 없다. .venv의 formulas 패키지로 재계산해 검증하는 방법
metadata:
  type: reference
---

soffice/libreoffice 없음 (2026-10-12 확인). openpyxl로 저장한 수식은 캐시 값이 없어 `data_only=True`로 읽으면 None이다.

**How to apply:** `.venv/bin/pip install formulas` (설치됨, 약 1분) 후 `formulas.ExcelModel().loads(path).finish()`, `.calculate()`, `.write(dirpath=...)`로 계산본(대문자 ROI.XLSX)을 scratchpad에 만들고 data_only로 읽어 검증한다. 원본에는 `wb.calculation.fullCalcOnLoad = True`를 설정해 Excel에서 열 때 재계산되게 한다. 한글 시트명, INDEX, CHOOSE, NPV, PV, RANK, TEXT, COUNTIF 모두 잘 계산됨. 계산본은 서식이 빠지므로 산출물로 쓰지 않는다.
