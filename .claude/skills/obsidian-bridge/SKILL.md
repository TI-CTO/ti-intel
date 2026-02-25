---
name: obsidian-bridge
description: "워크스페이스의 산출물을 Obsidian 볼트로 동기화한다. frontmatter를 추가하고 볼트에 복사한다."
user-invokable: true
argument-hint: "[file-path] [type: research|implementation|project]"
---

# Obsidian Bridge

워크스페이스 파일을 Obsidian 볼트에 동기화한다.

## Arguments
- 첫 번째 인자: 소스 파일 경로
- 두 번째 인자: 노트 타입 (destination 결정)

## Destination Mapping
| Type           | Obsidian Vault Path                                          |
|----------------|--------------------------------------------------------------|
| research       | /Users/ctoti/Obsidian/Obsidian_Work/70-Research/Sessions/    |
| implementation | /Users/ctoti/Obsidian/Obsidian_Work/60-ClaudeCode/Implementations/ |
| project        | /Users/ctoti/Obsidian/Obsidian_Work/10-Projects/             |

## Process

1. **소스 파일 읽기:** 첫 번째 인자의 파일을 Read로 읽는다

2. **기존 frontmatter 확인:** YAML frontmatter가 있으면 보존하고, 없으면 새로 생성

3. **Obsidian 형식으로 변환:**
   - 타입별 태그 추가: `tags: [claude-code, {type}]`
   - `created` 날짜 추가 (오늘)
   - `updated` 날짜 추가 (오늘)
   - 타입별 추가 필드:
     - research: `topic`, `confidence`, `status`, `related_project`
     - implementation: `project`, `complexity`, `status`
     - project: `status`

4. **파일명 결정:**
   - 원본 파일명이 YYYY-MM-DD 접두사를 가지면 그대로 사용
   - 없으면 오늘 날짜를 접두사로 추가: `{YYYY-MM-DD}_{original-name}.md`

5. **대상 폴더에 저장**

6. **결과 보고:**
   - 생성된 파일의 전체 경로
   - Obsidian에서 열 수 있는지 안내
