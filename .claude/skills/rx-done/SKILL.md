---
name: rx-done
description: 작업 하나를 완료 처리한다. plan.md 상태를 바꾸고 progress.md에 기록한 뒤 커밋하고 푸시한다.
argument-hint: "[작업 ID] [한 줄 요약]"
arguments: [task_id]
disable-model-invocation: true
allowed-tools: Bash(git add *) Bash(git commit *) Bash(git push*) Bash(git status*) Bash(date*)
---

## 완료 처리: $task_id

1. plan.md에서 $task_id 행의 상태를 `완료`로 바꾼다. 담당은 그대로 둔다.
2. `date "+%Y-%m-%d %H:%M"`으로 현재 시각을 얻어 progress.md **맨 아래에** 추가한다. 이전 기록은 수정하지 않는다.
   ```
   ## YYYY-MM-DD HH:MM | <담당> | $task_id
   - 한 일:
   - 산출물:
   - 다음:
   - 이슈:
   ```
   `다음:`에는 이 작업 덕분에 새로 시작할 수 있게 된 작업 ID를 적는다.
3. 이 작업의 산출물, plan.md, progress.md만 스테이징한다. `git add -A`는 쓰지 않는다.
4. 커밋 메시지는 `[$task_id] 한 줄 요약` 형식으로 쓰고, 끝에 세션 지침의 Co-Authored-By 줄을 붙인다.
5. `git push`를 실행하고 결과를 한 줄로 보고한다. 실패하면 오류 메시지를 그대로 보여 준다.
