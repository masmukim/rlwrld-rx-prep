---
title: Claude Code 스킬(Skills)과 슬래시 커맨드 문서
url: https://code.claude.com/docs/en/skills
publisher: Anthropic
published: unknown
fetched: 2026-10-06
tags: [claude-code, skills, commands]
source_type: 공식문서
---

## 핵심 사실
- 커스텀 커맨드는 스킬로 통합되었다. `.claude/commands/x.md`와 `.claude/skills/x/SKILL.md`는 둘 다 `/x`를 만든다. 새로 만들 때는 스킬을 권장한다 (보조 파일, 호출 제어, 자동 로딩 지원). (출처: https://code.claude.com/docs/en/slash-commands)
- 구조: `.claude/skills/<이름>/SKILL.md`(필수)와 보조 파일(reference.md, scripts/ 등)
- 위치: 엔터프라이즈 > 개인 `~/.claude/skills/` > 프로젝트 `.claude/skills/` > 플러그인(`/플러그인:스킬`)
- 프론트매터: `name`(생략하면 디렉토리명), `description`(권장, `when_to_use`와 합쳐 최대 1,536자), `when_to_use`, `disable-model-invocation`(true면 사용자만 호출), `user-invocable`(false면 Claude만 호출), `allowed-tools`, `disallowed-tools`, `argument-hint`, `arguments`, `paths`, `context: fork`, `agent`, `model`, `effort`, `shell`, `hooks`, `metadata`
- 치환자: `$ARGUMENTS`, `$0`/`$1`, `$이름`(`arguments`에 선언한 경우), `${CLAUDE_SKILL_DIR}`, `${CLAUDE_PROJECT_DIR}`, `${CLAUDE_SESSION_ID}`
- 셸 주입: `` !`명령` `` 또는 ` ```! ` 블록은 Claude가 내용을 보기 전에 실행된다. `@파일`은 파일 내용을 포함한다.
- `anthropic-skills` 이름은 claude.ai에서 동기화된 스킬용으로 예약되어 있다.
- 검증 명령: `claude plugin validate .claude/skills`

## 원문 발췌
> Custom commands have been merged into skills.

> Set `true` to prevent Claude from auto-invoking (manual `/name` only)

## 메모
- `disable-model-invocation: true`인 스킬은 Claude가 Skill 도구로 부를 수 없다. 그래서 `rx-run`은 `rx-done`을 호출하지 않고 그 SKILL.md 파일을 읽어서 절차를 따른다.
- 기본 명령 `/status`, 기존 `run` 스킬과 이름이 겹치지 않도록 커맨드에 `rx-` 접두어를 붙였다.
