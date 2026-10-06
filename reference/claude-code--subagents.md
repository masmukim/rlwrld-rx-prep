---
title: Claude Code 서브에이전트(Subagents) 문서
url: https://code.claude.com/docs/en/sub-agents
publisher: Anthropic
published: unknown
fetched: 2026-10-06
tags: [claude-code, agents]
source_type: 공식문서
---

## 핵심 사실
- 위치(우선순위 순): 관리형 설정 > `--agents` CLI 플래그 > 프로젝트 `.claude/agents/` > 사용자 `~/.claude/agents/` > 플러그인 `agents/`
- 형식: YAML 프론트매터 + 마크다운 본문(시스템 프롬프트)
- 필수 필드: `name`(`:` 포함 불가, `-`로 시작 불가), `description`(언제 위임할지)
- 주요 선택 필드: `tools`(생략하면 전체 도구 상속), `disallowedTools`, `model`(`sonnet`, `opus`, `haiku`, `fable`, 전체 ID, `inherit`), `permissionMode`, `maxTurns`, `skills`(시작할 때 스킬 전문 주입), `mcpServers`, `hooks`, `memory`(`user`/`project`/`local`), `background`, `omitClaudeMd`, `effort`, `isolation: worktree`, `color`
- `tools` 형식: 쉼표 구분 문자열 또는 YAML 리스트. `Agent(worker, researcher)`처럼 띄울 수 있는 서브에이전트를 제한할 수 있다.
- 서브에이전트는 `tools`에 `Agent`가 있으면 다른 서브에이전트를 띄울 수 있다. 기본 깊이 제한은 3단계, 동시 실행은 기본 20개다.
- `.claude/agents/`는 변경을 감시하므로 재시작 없이 몇 초 안에 반영된다.
- 검증 명령: `claude plugin validate .claude/agents`

## 원문 발췌
> Inherits all available tools if omitted.

> Full skill content is injected at startup

## 메모
- 이 프로젝트의 `.claude/agents/*.md` 작성에 사용했다.
- 서브에이전트는 사용자와 대화를 주고받을 수 없어서 모의 면접은 스킬(`rx-interview`)로 만들었다.
