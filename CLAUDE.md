# RLWRLD RX Intern 지원 준비 프로젝트

RLWRLD(리얼월드) Robotics Transformation(RX) Intern 지원을 위한 리서치와 포트폴리오 작업 공간.
- **A. 회사·산업 리서치**: 회사, 기술, 경쟁사, 하드웨어 및 센서 동향 조사
- **B. 미니 RX 케이스**: 공정 1개를 골라 분석, ROI 계산, PoC 로드맵을 담은 포트폴리오 제작

## 직무 맥락 (모든 작업의 기준)
- RLWRLD: Robotics Foundation Model(RFM) 개발사. 핵심은 **고자유도 로봇 손의 정밀 조작**. 최신 모델은 RLDX-1이며 제조, 물류, 서비스 산업을 타깃으로 함.
- RX 직무: 고객 공정 분석 → 솔루션 제안 → 기술·운영·재무 타당성 및 ROI 분석 → 경영진 보고서 작성 → Data/PoC 파트너십 실행.
- 결과물 톤: 컨설팅 스타일. 결론을 먼저 쓰고, 수치에는 근거를 달고, 장표는 1장 1메시지.

## 역할 설정
- **사용자는 RLWRLD RX 팀 실무자다.** 이 프로젝트는 지원 준비용 자료 정리가 아니라, 채용공고의 주요 업무를 실제로 수행하는 것처럼 진행한다.
- 기준 문서는 `reference/company--rx-intern-posting.md`(채용공고)다. 산출물은 공고의 주요 업무에 대응한다.
  - 사업 기회 발굴 → B1, 공정 심층 분석 → B2, 타당성·ROI → B3, 전략 보고서 → B4
  - 기술·시장·경쟁 리서치 → A2~A5, Data/PoC 실행 지원 → B4의 PoC 로드맵
- 산출물의 독자는 **가상의 고객사 경영진과 실무진**, 그리고 RX 팀 내부다. "지원자가 공부한 내용"이 아니라 "RX 팀이 고객에게 내는 결과물"처럼 쓴다.
- 판단이 필요한 지점(어떤 공정을 고객 케이스로 삼을지 등)은 실무자인 사용자가 결정한다.

## 세션 시작 시 필수 절차
새 세션은 작업 전에 반드시 다음 순서를 따른다.
1. `plan.md`와 `progress.md`를 읽고 사용자에게 3줄로 보고한다. 절차는 `/rx-status`와 같다.
   - 완료된 일
   - 진행 중인 일과 담당
   - 다음에 할 일 추천 (선행 작업이 모두 `완료`인 `대기` 작업 중에서)
2. 사용자가 지시한 작업이 plan.md에 없으면 먼저 plan.md에 추가한 뒤 시작한다.

## 멀티 에이전트 협업 (plan.md / progress.md)
- **plan.md = 무엇을 할지.** 작업 목록이자 담당 배정표다. 현재 상태의 기준은 이 파일이다.
- **progress.md = 어디까지 했는지.** 작업 기록이다. 항목은 맨 아래에 추가만 하고, 이전 기록은 수정하거나 삭제하지 않는다.

### plan.md 형식
```
| ID | 작업 | 담당 | 상태 | 선행 작업 | 산출물 |
|----|------|------|------|-----------|--------|
| A1 | RLWRLD 회사 리서치 | researcher | 진행중 | - | research/company.md |
| A3 | 경쟁사 비교표 | - | 대기 | A2 | research/competitors.md |
```
- 상태 값은 `대기`, `진행중`, `완료`, `보류(사유)` 네 가지만 쓴다.
- 담당에는 에이전트 이름(`researcher`, `case-analyst`, `roi-modeler`) 또는 `main`을 쓴다.

### progress.md 형식
```
## 2026-10-06 14:30 | researcher | A1
- 한 일: 회사 개요, 투자 이력 정리
- 산출물: research/company.md
- 다음: RLDX-1 기술 세부 조사 필요
- 이슈: 투자 금액 소스마다 다름 → 추정 표기
```

### 작업 규칙
1. **plan.md, progress.md 수정과 git 커밋은 메인 에이전트만 한다.** 서브에이전트는 자기 산출물 파일만 쓰고, 결과를 메인 에이전트에게 반환한다.
2. **시작할 때:** 메인 에이전트가 plan.md의 담당과 상태(`진행중`)를 먼저 바꾼 뒤 에이전트를 띄운다.
3. **다른 작업과의 충돌:** 이미 `진행중`인 작업은 다시 시작하지 않는다.
4. **끝날 때:** `fact-checker`로 검증한 뒤 `/rx-done` 절차를 따른다. 상태를 `완료`로 바꾸고, progress.md에 기록하고, `[A1] 요약` 형식으로 커밋하고 푸시한다.
5. **중단될 때:** 상태는 `진행중`으로 두고, progress.md의 `다음:`에 이어서 할 지점을 구체적으로 적는다.

## 학습 구조 (작업할수록 쌓이는 지식)
| 층 | 파일 | 담는 것 | 쓰는 주체 |
|----|------|---------|-----------|
| 원자료 | `reference/` | 소스 1건당 1파일 (기사, 공식문서, 논문) | researcher, case-analyst |
| 주제별 결론 | `research/`, `case/` | 작업 산출물 | 담당 에이전트 |
| 팀 공용 산업 지식 | `knowledge.md` | 용어집, 핵심 인사이트, 열린 질문 | 메인 에이전트 (`/rx-done`) |
| 에이전트별 노하우 | `.claude/agent-memory/<에이전트>/MEMORY.md` | 좋은 소스, 잘 통한 검색어, 실수 | 각 에이전트 (`memory: project`) |

- 모든 에이전트는 작업 전에 `knowledge.md`를 읽고, 작업 후 `새로 배운 것`(용어, 인사이트, 열린 질문)을 반환한다.
- 열린 질문은 `/rx-status`가 새 리서치 작업(`Q<번호>`)으로 제안한다. 이렇게 작업 → 지식 → 새 질문 → 작업으로 순환한다.
- **다국어 리서치:** 영어(기술, 경쟁사, 글로벌), 한국어(국내 시장, 정책), 일본어(일본 시장, 로봇 제조사)로 검색한다. 기술 주제는 `paper-search`로 논문(arXiv, OpenAlex, Semantic Scholar)도 찾는다.

## 에이전트, 커맨드, 스킬
세부 방법론은 스킬에 있다. 이 파일에는 규칙과 협업 절차만 둔다.

**에이전트** (`.claude/agents/`)
| 이름 | 담당 | 프리로드 스킬 |
|------|------|---------------|
| researcher | A1~A6, 리서치 갱신 | research-format, reference, paper-search |
| case-analyst | B1, B2 | process-analysis, reference, paper-search |
| roi-modeler | B3 | roi-model, reference |
| fact-checker | 모든 산출물 검증 (보고만, 수정 안 함) | reference |

**커맨드** (`.claude/skills/rx-*`, 사용자가 직접 호출)
| 커맨드 | 동작 |
|--------|------|
| `/rx-status` | 완료, 진행 중, 다음 추천을 3줄로 보고 |
| `/rx-run A1` | 작업 하나를 배정 → 실행 → 검증 → 완료 처리 |
| `/rx-parallel` | 시작할 수 있는 대기 작업을 모두 동시에 실행 |
| `/rx-done A1` | plan.md, progress.md 갱신 후 커밋, 푸시 |
| `/rx-refresh competitors` | 기존 리서치를 최신 정보로 갱신 |
| `/rx-interview 케이스` | 자료 기반 모의 면접 |

**방법론 스킬** (`.claude/skills/`, 필요할 때 자동으로 불러옴)
| 스킬 | 내용 |
|------|------|
| reference | `reference/` 조사 자료 찾기·저장 (`/reference find 키워드`로 직접 호출도 가능) |
| paper-search | 영어 논문 검색 (arXiv, OpenAlex, Semantic Scholar), 요약, reference 저장 |
| research-format | 리서치 문서 템플릿, 출처 규칙, 주제별 본문 구성 |
| process-analysis | 후보 공정 점수표, 작업 동작 분해, RFM 적합성 판단 |
| roi-model | ROI 엑셀 시트 구성, 계산식, 민감도 |
| consulting-deck | 장표 작성 원칙, 미니 RX 케이스 8장 구성 |

## 디렉토리 구조
```
CLAUDE.md
plan.md              # 작업 목록, 담당, 상태 (무엇을 할지)
progress.md          # 작업 기록, 추가만 함 (어디까지 했는지)
knowledge.md         # 팀 공용 산업 지식: 용어집, 인사이트, 열린 질문
.claude/
  settings.json      # 프로젝트 권한 (웹 조사, 산출물 폴더 쓰기, git 커밋·푸시 허용)
  agents/            # 서브에이전트 정의
  agent-memory/      # 에이전트별 노하우 (MEMORY.md, 커밋함)
  skills/            # 커맨드(rx-*)와 방법론 스킬
reference/           # 조사 원자료. 소스 1건당 파일 1개 (<태그>--<슬러그>.md)
requirements.txt     # Python 패키지 (.venv에 설치, .venv는 커밋 제외)
research/            # A. 리서치 결과 (reference를 종합한 결론)
  company.md         # RLWRLD 회사, 투자, 인물, RLDX-1
  tech.md            # RFM/VLA, 모방학습, 텔레오퍼레이션, 데이터 수집
  competitors.md     # 경쟁사 비교표
  hardware.md        # 로봇 손, 그리퍼, 촉각 및 비전 센서
  market.md          # 산업별 자동화 수요, 인력난, 시장 규모
  papers.md          # 핵심 논문 지도
case/                # B. 미니 RX 케이스
  candidates.md      # 후보 공정 비교 및 선정 근거
  analysis.md        # 선정 공정의 심층 분석과 ROI 가정값 표
  roi.xlsx           # ROI 모델 (가정, 계산, 민감도 시트)
  deck               # 최종 장표 (Slides 아티팩트 또는 .pptx)
```

## 규칙
- **조사 전에 `reference/`부터 찾는다.** 결과물에 인용한 소스는 `reference/`에 저장한다. 형식은 `reference` 스킬을 따른다.
- **사실을 지어내지 않는다.** 확인되지 않은 수치는 `추정`이라고 표시하고 계산 근거를 함께 적는다.
- RLWRLD 내부 정보나 고객사를 아는 것처럼 쓰지 않는다. 공개 정보만 사용한다.
- Python은 항상 `.venv/bin/python`으로 실행한다. 시스템의 Anaconda `python3`는 openpyxl을 불러오면 MKL 오류로 종료된다. `.venv`가 없으면 `/usr/bin/python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`로 만든다.
- 숫자에는 단위, 기준 연도, 통화를 명시한다.
- 산출물은 한국어로 쓰고 기술 용어는 영어를 병기한다. 예: 모방학습(Imitation Learning)
