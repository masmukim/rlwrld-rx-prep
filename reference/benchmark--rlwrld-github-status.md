---
title: RLWRLD GitHub 조직, Arena 포크, Hugging Face 계정의 DexBench 공개 상태 (관찰 기록)
url: https://github.com/RLWRLD
publisher: GitHub, Hugging Face (공개 API 조회)
published: unknown
fetched: 2026-10-09
tags: [benchmark, dexbench, rlwrld]
source_type: 1차
lang: en
---

## 핵심 사실
- RLWRLD 조직 페이지의 저장소 7개: RLDX-1(Apache-2.0 표기, 갱신 2026-09-09), IsaacLab-Arena(포크, 갱신 2026-10-07), IsaacLab(포크), newton(포크), simready-foundation(포크), openarm_description(포크), ethercat_driver_ros2(포크). DexBench 이름의 저장소는 없다.
- RLWRLD/IsaacLab-Arena 브랜치: main, dexbench/main, dexbench/pin-8b3fb4db. dexbench/main은 main보다 4커밋 앞서고 16커밋 뒤처짐(diverged). 변경 파일: .gitmodules, isaaclab_arena/assets/device_library.py, pyproject.toml, submodules/IsaacLab. 커밋(2026-10-07, joocjun): "Point submodules/IsaacLab at RLWRLD/IsaacLab dexbench/main", "Fetch Isaac-GR00T over HTTPS", "Pin Newton to RLWRLD/newton at cf5378db (1.5.2)", "Let an embodiment turn off OpenXR controller button polling".
- 트리 검색: dexbench/main 브랜치와 업스트림 isaac-sim/IsaacLab-Arena main에서 dexbench·rlwrld 이름의 파일 경로 없음.
- Hugging Face(API): RLWRLD 계정 모델 11개(RLDX-1-PT, -PT-IMG, -VLM, -MT-ALLEX, -MT-DROID, -FT-ROBOCASA/-SIMPLER-WIDOWX/-SIMPLER-GOOGLE/-GR1/-RC365/-LIBERO), 데이터셋 0개. "dexbench" 검색 결과는 다른 사용자 항목뿐이고 RLWRLD와의 관계를 확인하지 못했다.

## 원문 발췌
> (조직 페이지 저장소 목록과 GitHub·Hugging Face API 응답을 요약한 관찰 기록이며 인용문 없음) (raw: reference/raw/benchmark--rlwrld-github-org.txt, reference/raw/benchmark--rlwrld-arena-fork.txt)

## 메모
- 2026-10-09 시점의 스냅샷이다. 비공개 저장소는 보이지 않는다. 시간이 지나면 바뀌므로 재확인 대상(피딩 요청 목록).
- RLDX-1 저장소의 Apache-2.0 표기는 코드 기준이며, 가중치 라이선스(knowledge.md의 RLWRLD Model License)와 같은지는 이번에 확인하지 않았다.
