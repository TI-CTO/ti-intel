# 워크스페이스 구조 개편: 도메인 분리 + 공통 자산 심볼릭 링크

> **상태**: 설계 확정 — 이종 도메인 추가 시점에 실행
> **작성일**: 2026-03-03
> **갱신일**: 2026-03-04 (intel-store 통합 반영, dead project 정리)
> **트리거**: 새 도메인 프로젝트(예: 주식매매) 추가가 필요해지는 시점

## Context

현재 `/Users/ctoti/Project/ClaudeCode/`는 단일 git root에 4개 MCP 프로젝트 + 10개 스킬 + 5개 에이전트가 공존한다. 모든 자산이 "LG U+ 기술전략 인텔리전스" 도메인에 특화되어 있어, 이종 도메인(주식매매 등) 프로젝트 추가 시 컨텍스트 오염, MCP 서버 전역 노출, git history 혼재 문제가 발생한다.

**목표**: 향후 이종 도메인 프로젝트 추가 시 즉시 적용 가능한 구조 설계안을 확정한다. 지금 당장 실행하지 않고, 필요한 시점에 참조하여 마이그레이션한다.

## 현재 자산 분류

### 도메인 무관 (공통) — 12개
| 유형 | 자산 | 경로 |
|------|------|------|
| agent | researcher, implementer, reviewer | `.claude/agents/` |
| skill | new-project, obsidian-bridge, work-log, research-session, slides, report-pdf | `.claude/skills/` |
| rule | python-style, testing, commit-message | `.claude/rules/` |
| hook | validate-no-secrets, post-edit-format | `.claude/hooks/` |
| project | design-system | `projects/design-system/` |

### 도메인 특화 (Tech-Intel) — 8개
| 유형 | 자산 |
|------|------|
| agent | research-deep, validator |
| skill | wtis, discover, monitor, weekly-monitor |
| project | intel-store, trend-tracker, telco-factbook |

> **참고**: `research-hub`, `patent-intel`은 `intel-store`로 통합 완료 (2026-03-04).
> 폴더는 잔존하나 `.mcp.json`에서 제거됨. 마이그레이션 시점에 폴더 삭제 예정.

## 권장 구조

```
/Users/ctoti/Project/
├── claude-common/                  ← 공통 자산 git repo (신규)
│   ├── rules/                      (3개 파일)
│   ├── hooks/                      (2개 파일)
│   ├── agents/                     (researcher, implementer, reviewer)
│   └── skills/                     (new-project, obsidian-bridge, work-log,
│                                    research-session, slides, report-pdf)
│
├── TechIntel/                      ← 기존 ClaudeCode/ 리네임
│   ├── .claude/
│   │   ├── settings.json
│   │   ├── rules/       → symlink → ../../claude-common/rules/
│   │   ├── hooks/       → symlink → ../../claude-common/hooks/
│   │   ├── agents/
│   │   │   ├── *.md     → symlink (공통 3개)
│   │   │   ├── research-deep.md   (도메인 전용)
│   │   │   └── validator.md       (도메인 전용)
│   │   └── skills/
│   │       ├── */       → symlink (공통 6개)
│   │       ├── wtis/              (도메인 전용)
│   │       ├── discover/          (도메인 전용)
│   │       ├── monitor/           (도메인 전용)
│   │       └── weekly-monitor/    (도메인 전용)
│   ├── .mcp.json                   (tech-intel MCP만)
│   ├── CLAUDE.md                   (LG U+ 도메인 컨텍스트)
│   └── projects/                   (intel-store, trend-tracker, telco-factbook, design-system)
│
└── {NewDomain}/                    ← 향후 새 도메인
    ├── .claude/
    │   ├── rules/       → symlink → ../../claude-common/rules/
    │   ├── hooks/       → symlink → ../../claude-common/hooks/
    │   ├── agents/      → symlink (공통) + 도메인 전용
    │   └── skills/      → symlink (공통) + 도메인 전용
    ├── .mcp.json                   (도메인 MCP + design-system 절대경로)
    ├── CLAUDE.md                   (도메인 컨텍스트)
    └── projects/
```

## 핵심 설계 결정

### 1. ClaudeCode → TechIntel 리네임
- **이유**: 현재 이름이 실체(LG U+ Tech Intel)와 불일치
- **비용**: `~/.claude/projects/` 세션 데이터 경로 변경됨 → MEMORY.md만 수동 복사
- **MEMORY.md 절대경로**: `sed`로 `/ClaudeCode/` → `/TechIntel/` 일괄 치환

### 2. design-system 공유
- TechIntel에 유지, 다른 워크스페이스에서 `.mcp.json`에 절대경로로 참조:
```json
{
  "design-system": {
    "command": "uv",
    "args": ["--directory", "/Users/ctoti/Project/TechIntel/projects/design-system",
             "run", "python", "-m", "design_system.mcp_server"]
  }
}
```

### 3. Supabase 분리
- 도메인별 별도 Supabase 프로젝트 (무료 플랜 2개까지)
- topics FK 체계가 도메인마다 다르므로 공유할 이유 없음

### 4. research-session 토픽 슬러그 하드코딩 제거
- `.claude/skills/research-session/SKILL.md` 56번 라인의 8개 토픽 슬러그를 제거
- "사용 가능한 MCP 서버에서 자동 감지" 방식으로 변경

### 5. 심볼릭 링크 전략
- **디렉토리 단위 심링크**: `rules/`, `hooks/` → 전체 디렉토리
- **파일 단위 심링크**: `agents/`, `skills/` → 공통 파일만 (도메인 전용과 혼재하므로)
- git은 심볼릭 링크를 정상 추적 (단일 머신 운영이므로 이식성 문제 없음)

## 실행 순서 (필요 시점에 참조)

### Phase 1: claude-common 준비
```bash
mkdir -p /Users/ctoti/Project/claude-common/{rules,hooks,agents,skills}
cd /Users/ctoti/Project/claude-common && git init
```
- 공통 자산 12개 복사
- research-session SKILL.md 토픽 슬러그 제거

### Phase 2: TechIntel 마이그레이션
```bash
mv /Users/ctoti/Project/ClaudeCode /Users/ctoti/Project/TechIntel
rm -rf /Users/ctoti/Project/TechIntel/projects/research-hub
rm -rf /Users/ctoti/Project/TechIntel/projects/patent-intel
```
- dead project 폴더 삭제 (research-hub, patent-intel → intel-store로 통합 완료)
- `.claude/rules/` → 기존 파일 삭제 후 `ln -s ../../claude-common/rules/ .claude/rules`
- `.claude/hooks/` → 동일
- `.claude/agents/{researcher,implementer,reviewer}.md` → 개별 심링크
- `.claude/skills/{6개 공통}/` → 개별 심링크
- MEMORY.md 경로 치환

### Phase 3: 검증
- TechIntel에서 Claude Code 세션 → 기존 스킬/에이전트 동작 확인
- 심볼릭 링크 파일 읽기/수정 정상 확인

### Phase 4: 새 도메인 추가 (향후)
- `/Users/ctoti/Project/{DomainName}/` 생성
- `.claude/` 구조 + 심링크 설정
- 도메인 전용 CLAUDE.md, .mcp.json, agents, skills 작성

## 옵션 비교 요약

| 기준 | 단일 루트 유지 | **도메인 분리 + 심링크 (권장)** |
|------|:---:|:---:|
| 컨텍스트 격리 | 나쁨 | 우수 |
| 공통 자산 재사용 | 우수 | 우수 (심링크) |
| 확장성 (5개 도메인) | 나쁨 | 우수 |
| git 이력 분리 | 나쁨 | 우수 |
| 초기 비용 | 0 | 약 2시간 |
