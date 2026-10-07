# RLWRLD RX Prep

RLWRLD(리얼월드) **Robotics Transformation(RX)** 팀의 업무를 실무자 관점에서 직접 수행해 보는 프로젝트다. 채용공고의 주요 업무(사업 기회 발굴, 공정 분석, 타당성·ROI, 전략 보고서, 기술·시장 리서치, PoC 지원)를 실제 산출물로 만든다.

Claude Code의 에이전트, 커맨드, 스킬로 리서치와 분석을 나눠 돌리고, 결과와 근거를 이 저장소에 쌓는다.

> 모든 내용은 공개 정보만 사용했다. 고객 케이스의 "K사"는 가상 기업이다. 회사 발표 수치는 대부분 자체 주장이며, 확인하지 못한 값은 `추정` 또는 `확인필요`로 표시했다.

## 주요 산출물

| 문서 | 내용 |
|------|------|
| [case/b4-proposal.md](case/b4-proposal.md) | **최종 제안서.** 자동차 와이어 하네스 조립 RX 제안 (공정, 난제, 경쟁, 솔루션, 경제성, 도입 구조, 게이트형 PoC, 리스크) |
| [case/analysis.md](case/analysis.md) | 하네스 조립 공정 심층 분석, ROI 가정값 표 |
| [case/candidates.md](case/candidates.md) | 후보 공정 5개 점수화와 선정 근거 |
| [research/company.md](research/company.md) | RLWRLD 회사, 투자, 인물, RLDX-1, 경영진 전략 |
| [research/poc-playbook.md](research/poc-playbook.md) | 선도기업 PoC→배포 프로세스와 RLWRLD PoC 설계 체크리스트 |
| [research/rx-cases.md](research/rx-cases.md) | RLWRLD RX 방식과 해외 9개사 도입 사례 |
| [research/skild-pi-deep-dive.md](research/skild-pi-deep-dive.md) | Skild AI, Physical Intelligence 심층 비교 |
| [research/](research/) | 기술(tech), 경쟁사(competitors), 하드웨어(hardware), 시장(market), 논문(papers) |

## 진행 현황

| ID | 작업 | 상태 |
|----|------|------|
| A1~A6 | 회사, 기술, 경쟁사, 하드웨어, 시장, 논문 리서치 | 완료 |
| A7, A8 | RX 방식·해외 사례, Skild·PI 심층 | 완료 |
| A10 | PoC→배포 플레이북 | 완료 (fact-check 미실시) |
| B1 | 후보 공정 선정 → 와이어 하네스 조립 | 완료 |
| B2 | 공정 심층 분석 | 완료 (fact-check 미실시) |
| B3 | ROI 엑셀 모델 | 보류 |
| B4 | 제안서 | 진행 중 (실무자 검토) |

작업별 상세 상태는 [plan.md](plan.md), 작업 기록은 [progress.md](progress.md)를 본다.

## 폴더 구조

```
CLAUDE.md          # Claude Code 규칙: 역할, 협업 절차, 토큰 배분
plan.md            # 작업 목록, 담당, 상태 (무엇을 할지)
progress.md        # 작업 기록, 추가만 함 (어디까지 했는지)
knowledge.md       # 팀 공용 산업 지식: 용어집, 인사이트, 열린 질문
research/          # 주제별 리서치 결론
case/              # 하네스 고객 케이스 (B1~B4)
reference/         # 근거 원자료, 소스 1건당 파일 1개 (<태그>--<슬러그>.md)
reference/raw/     # 원문 텍스트 (저작권 때문에 커밋하지 않음)
.claude/
  settings.json    # 프로젝트 권한, 기본 모델
  agents/          # 서브에이전트 4개
  skills/          # 커맨드(rx-*)와 방법론 스킬
  agent-memory/    # 에이전트별 노하우
```

## 지식이 쌓이는 방식

| 층 | 위치 | 담는 것 |
|----|------|---------|
| 원자료 | `reference/` | 기사, 공식 문서, 논문 1건당 1파일. 핵심 사실과 원문 발췌 |
| 결론 | `research/`, `case/` | 작업 산출물 |
| 공용 지식 | `knowledge.md` | 용어집, 인사이트, 열린 질문 (열린 질문이 다음 작업 후보가 됨) |
| 노하우 | `.claude/agent-memory/` | 에이전트별로 쓸모 있던 소스, 막힌 사이트, 실수 |

## 사용법 (Claude Code)

### 준비
```bash
git clone https://github.com/masmukim/rlwrld-rx-prep.git
cd rlwrld-rx-prep
/usr/bin/python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
claude   # 처음 열 때 폴더 신뢰를 허용해야 .claude/settings.json 권한이 적용된다
```

### 커맨드
| 커맨드 | 동작 |
|--------|------|
| `/rx-status` | 완료, 진행 중, 다음에 할 일 3줄 보고 |
| `/rx-run A1` | 작업 하나를 담당 에이전트에 배정 → 실행 → 검증 → 완료 처리 |
| `/rx-parallel` | 시작할 수 있는 대기 작업을 모두 동시에 실행 |
| `/rx-done A1` | plan·progress·knowledge 갱신 후 커밋·푸시 |
| `/rx-refresh competitors` | 기존 리서치를 최신 정보로 갱신 |
| `/rx-interview 케이스` | 자료 기반 모의 면접 |

### 에이전트
| 이름 | 담당 | 모델 |
|------|------|------|
| researcher | 웹·논문 리서치 (한국어, 영어, 일본어) | sonnet |
| case-analyst | 후보 공정 선정, 공정 분석 | opus |
| roi-modeler | ROI 엑셀 모델 | sonnet |
| fact-checker | 원문 대조 검증 (수정하지 않고 보고만) | sonnet |

메인 세션은 지휘와 기록만 하고, 조사와 수정은 에이전트에게 맡긴다. 세부 규칙은 [CLAUDE.md](CLAUDE.md)에 있다.

### 스킬
| 스킬 | 내용 |
|------|------|
| reference | reference/ 찾기·저장 |
| source-read | 원문(웹, PDF, arXiv 전문)을 저장하고 `find.py`로 필요한 줄만 검색 |
| paper-search | arXiv, OpenAlex, Semantic Scholar 논문 검색 |
| research-format | 리서치 문서 템플릿, 다국어·출처 규칙 |
| process-analysis | 후보 공정 점수표, 작업 동작 분해 |
| roi-model | ROI 시트 구성과 계산식 |
| consulting-deck | 컨설팅 문서 작성 원칙 |

## 운영 메모
- **헤드리스 실행:** `claude -p`로 돌릴 때는 백그라운드 에이전트를 기본 10분까지만 기다린다. 긴 작업은 `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0`을 붙인다.
- **Python:** 항상 `.venv/bin/python`을 쓴다. 시스템 Anaconda는 openpyxl을 불러올 때 오류가 난다.
- **비용 기록:** 작업별 테스트 비용과 개선 내역은 [CLAUDE.md](CLAUDE.md)의 "토큰 배분"에 있다.
