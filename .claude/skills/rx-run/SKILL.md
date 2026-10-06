---
name: rx-run
description: plan.md의 작업 하나를 담당 에이전트에게 맡겨 실행하고, 검증과 완료 처리까지 진행한다.
argument-hint: "[작업 ID, 예: A1]"
arguments: [task_id]
disable-model-invocation: true
model: sonnet
---

## 실행할 작업: $task_id

@plan.md

### 1. 실행 가능한지 확인
- plan.md에 $task_id가 없으면 멈추고 사용자에게 알린다.
- 상태가 `진행중`이면 담당자와 함께 알리고 멈춘다.
- 선행 작업 중 `완료`가 아닌 것이 있으면 목록을 보여 주고 멈춘다.

### 2. 담당 배정
plan.md에서 $task_id 행의 담당을 에이전트 이름으로, 상태를 `진행중`으로 바꾼다.

| 작업 | 담당 |
|------|------|
| A1~A5 | `researcher` 에이전트 |
| B1, B2 | `case-analyst` 에이전트 |
| B3 | `roi-modeler` 에이전트 |
| B4 | `/rx-run`으로 진행하지 않는다. 장표는 최종 결과물이라 사용자의 기본 모델(Opus) 세션에서 일반 요청으로 `consulting-deck` 스킬을 써서 만든다. B4가 들어오면 이 안내만 하고 멈춘다. |
| 그 외 | 작업 성격에 가장 가까운 에이전트, 없으면 메인 에이전트 |

### 3. 실행
에이전트에게 작업 ID, 작업 내용, 산출물 경로, 선행 작업 산출물 경로를 넘긴다.

### 4. 검증
`fact-checker` 에이전트에게 산출물을 넘긴다. `오류`와 `누락`은 메인 에이전트가 직접 고친다. `확인필요`는 progress.md의 이슈에 적는다.

### 4-1. 사용자 결정 (B1만)
B1은 완료 처리하기 전에 멈춘다. 후보 공정 점수표와 추천안을 보여 주고, 실무자인 사용자에게 고객 케이스로 삼을 공정을 고르게 한다. 고른 공정과 이유를 case/candidates.md 끝의 `## 결정` 섹션에 적은 뒤 완료 처리한다.

### 5. 완료
`.claude/skills/rx-done/SKILL.md`를 읽고 그 절차대로 plan.md와 progress.md를 갱신하고 커밋, 푸시한다.
작업이 중간에 끊기면 상태는 `진행중`으로 두고 progress.md의 `다음:`에 이어서 할 지점을 적는다.
