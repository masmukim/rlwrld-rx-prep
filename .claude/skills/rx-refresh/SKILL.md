---
name: rx-refresh
description: 기존 리서치 파일을 최신 정보로 갱신한다. 지원 직전이나 면접 전에 사용한다.
argument-hint: "[주제: company | tech | competitors | hardware | market | all]"
arguments: [topic]
disable-model-invocation: true
---

## 리서치 갱신: $topic

1. 대상 파일을 정한다. `all`이면 research/ 아래 모든 파일이 대상이다. 대상 파일이 없으면 `/rx-run`으로 먼저 작성하라고 안내하고 멈춘다.
2. plan.md 맨 아래에 `R-<주제>-<MMDD>` ID로 갱신 작업을 추가하고 `진행중`으로 둔다. 예: `R-competitors-1006`
3. 대상마다 `researcher` 에이전트를 **갱신 모드**로 띄운다. 여러 개면 동시에 띄운다.
   - 기존 파일의 조사일 이후 바뀐 사실만 반영한다.
   - 바뀐 줄에는 `(YYYY-MM-DD 갱신)` 표시를 붙인다.
4. `fact-checker`로 바뀐 부분을 검증한다.
5. `.claude/skills/rx-done/SKILL.md`의 절차로 완료 처리한다.
6. 사용자에게 바뀐 내용만 요약해서 보고한다. 바뀐 게 없으면 없다고 말한다.
