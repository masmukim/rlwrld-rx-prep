---
name: rx-status
description: plan.md와 progress.md를 읽고 완료, 진행 중, 다음에 할 일을 3줄로 보고한다. 세션을 시작할 때 사용한다.
disable-model-invocation: true
---

## 현재 계획
@plan.md

## 작업 기록
@progress.md

## 도메인 지식
@knowledge.md

## 할 일
위 두 파일만 근거로 사용자에게 아래 3줄을 보고한다. 파일이 없으면 CLAUDE.md의 형식으로 새로 만든다고 알리고 만든다.

1. **완료:** 완료된 작업 ID와 이름
2. **진행 중:** 작업 ID, 담당, progress.md에 적힌 마지막 `다음:` 내용
3. **다음 추천:** 선행 작업이 모두 `완료`인 `대기` 작업. 여러 개면 `/rx-parallel`을 함께 제안한다.

`보류` 작업이 있으면 사유를 한 줄 덧붙인다.

knowledge.md에 풀리지 않은 `열린 질문`이 있으면 개수를 알리고, 중요한 것 1~2개를 새 리서치 작업(ID `Q<번호>`)으로 plan.md에 추가할지 사용자에게 묻는다.
