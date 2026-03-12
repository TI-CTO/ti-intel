---
topic: agency-agents GitHub 저장소 심층 분석
date: 2026-03-12
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
---

# Research Report: agency-agents 프로젝트 심층 분석

## Executive Summary

> `msitarzewski/agency-agents`는 120개+ 전문 AI 에이전트 persona를 정의한 오픈소스 컬렉션으로, GitHub 30.7k 스타를 기록한 대형 커뮤니티 프로젝트다. 핵심 설계는 **단일 에이전트 = 단일 마크다운 파일** 원칙으로, YAML frontmatter(메타데이터) + 마크다운 본문(프롬프트)으로 구성된다. 에이전트 간 협업은 런타임 오케스트레이션 엔진 없이 **인간이 orchestrator 역할**을 하며, 이전 에이전트 출력을 다음 에이전트의 입력에 복사-붙여넣기하는 sequential handoff 방식이다. MCP memory 서버를 연결하면 cross-session 상태 유지가 가능해진다. 이 설계의 강점은 툴 독립성과 극단적인 단순성이며, 약점은 에이전트 간 실시간 통신과 자동 오케스트레이션 부재다.

---

## 연구 질문

> 1. 에이전트가 어떻게 정의되는가 (스키마, 구조)?
> 2. 에이전트들이 어떻게 협업하는가 (통신, 핸드오프)?
> 3. 워크플로우가 어떻게 설계되는가 (오케스트레이션, 상태 관리)?
> 4. 도구 시스템과 툴 통합은 어떻게 이루어지는가?
> 5. 설계 철학과 핵심 원칙은 무엇인가?

---

## 1. 프로젝트 구조

#### 디렉토리 레이아웃

```
agency-agents/
├── engineering/          # 16개 에이전트 (Frontend, Backend, DevOps, Security 등)
├── design/               # UI/UX, Brand, Visual Storytelling
├── marketing/            # 18개 에이전트 (소셜미디어, 중국 플랫폼 포함)
├── paid-media/           # 7개 광고/미디어 에이전트
├── product/              # 4개 에이전트 (Sprint, Trend, Feedback, Nudge)
├── project-management/   # 6개 에이전트 (Shepherd, Producer 등)
├── sales/                # 8개 에이전트
├── testing/              # QA 전문 에이전트
├── specialized/          # 블록체인, 컴플라이언스 등 특수 도메인
├── spatial-computing/    # AR/VR/XR 전문 에이전트
├── game-development/     # Unity, Unreal, Godot, Roblox 전문
├── support/              # 인프라/운영 에이전트
├── examples/             # 멀티 에이전트 워크플로우 시나리오 4개
├── integrations/         # 툴별 변환 파일
│   ├── claude-code/      # 네이티브 .md 형식
│   ├── cursor/           # .mdc 규칙 파일
│   ├── aider/            # CONVENTIONS.md (단일 파일 통합)
│   ├── windsurf/         # .windsurfrules (단일 파일 통합)
│   ├── github-copilot/   # 네이티브 .md 형식
│   ├── gemini-cli/       # Extension + skill 파일
│   ├── openclaw/         # SOUL.md + AGENTS.md + IDENTITY.md
│   ├── opencode/         # .opencode/agents/ 디렉토리
│   ├── antigravity/      # SKILL.md 형식
│   └── mcp-memory/       # MCP 메모리 통합 예시
├── scripts/
│   ├── install.sh        # 대화형 설치 스크립트 (9개 툴 지원)
│   └── convert.sh        # 에이전트 파일 → 툴별 포맷 변환
└── README.md
```

**규모**: 30.7k 스타, 4.8k 포크, 142 커밋 (2026-03 기준) [[G-01]](#ref-g-01)

---

## 2. 에이전트 정의 방식

#### 파일 스키마 (YAML Frontmatter + Markdown Body)

모든 에이전트는 단일 `.md` 파일로 정의된다. Claude Code의 sub-agent 포맷과 동일하다.

```yaml
---
name: Frontend Developer
description: Expert frontend developer specializing in modern web technologies,
             React/Vue/Angular frameworks, UI implementation, and performance optimization
color: cyan
emoji: 🖥️
vibe: "Builds responsive, accessible web apps with pixel-perfect precision."
services:          # 선택 항목 — 외부 의존성 명시
  - name: Vercel
    url: https://vercel.com
    tier: freemium
---
```

**frontmatter 필드 설명:**

| 필드 | 필수 | 설명 |
|------|------|------|
| `name` | O | 에이전트 고유 이름 (Claude Code에서 활성화 키) |
| `description` | O | 한 줄 전문 분야 요약 |
| `color` | O | UI 색상 식별자 (named color 또는 hex) |
| `emoji` | O | 시각적 식별자 |
| `vibe` | O | 개성을 담은 한 문장 슬로건 |
| `services` | X | 외부 서비스 의존성 목록 |

#### 마크다운 본문 구조 (프롬프트 템플릿)

CONTRIBUTING.md에서 정의한 표준 섹션 구성 [[G-06]](#ref-g-06):

```markdown
## 🧠 Your Identity & Memory
- **Role**: [전문 역할 정의]
- **Personality**: [4가지 성격 특성]
- **Memory**: [학습/기억 대상]
- **Experience**: [경험적 배경]

## 🎯 Your Core Mission
### [책임영역 1]
- [구체적 작업 목록]
### [책임영역 2]
- [구체적 작업 목록]

## 🚨 Critical Rules You Must Follow
### [규칙 범주 1]
- [절대 준수 사항]

## 📋 Your Technical Deliverables
[실제 동작하는 코드 예시 포함]

## 🔄 Your Workflow Process
### Step 1: [단계명]
### Step 2: [단계명]
### Step 3: [단계명]
### Step 4: [단계명]

## 📋 Your Deliverable Template
[출력 마크다운 템플릿]

## 💭 Your Communication Style
- [표현 패턴 예시들]

## 🔄 Learning & Memory
[기억할 패턴 목록]

## 🎯 Your Success Metrics
[정량 지표들]

## 🚀 Advanced Capabilities
[고급 전문 역량]
```

#### 실제 Frontend Developer 에이전트 코드 예시

에이전트 본문에는 실제 실행 가능한 코드 예시가 포함된다:

```tsx
// Modern React component with performance optimization
import React, { memo, useCallback } from 'react';
import { useVirtualizer } from '@tanstack/react-virtual';

export const DataTable = memo<DataTableProps>(({ data, columns, onRowClick }) => {
  const rowVirtualizer = useVirtualizer({
    count: data.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 50,
    overscan: 5,
  });

  return (
    <div ref={parentRef} role="table" aria-label="Data table">
      {rowVirtualizer.getVirtualItems().map((virtualItem) => (
        <div key={virtualItem.key} role="row" tabIndex={0}>
          ...
        </div>
      ))}
    </div>
  );
});
```

**핵심 포인트**: 에이전트 파일은 "프롬프트 + 예시 코드 + 출력 템플릿"의 완전한 패키지다. LLM이 이 파일을 시스템 프롬프트로 로드하는 방식이다. [[G-02]](#ref-g-02)

---

## 3. 에이전트 간 협업 패턴

#### 기본 패턴: Sequential Handoff (순차 핸드오프)

프로젝트의 핵심 협업 방식은 **런타임 오케스트레이션 없는 수동 핸드오프**다. 공식 문서에 명시된 원칙:

> "Sequential handoffs: Each agent's output becomes the next agent's input"
> "Always paste previous agent outputs into the next prompt — agents don't share memory"

즉, 에이전트 A의 출력 → 인간이 복사 → 에이전트 B의 입력 프롬프트에 붙여넣기.

#### 패턴 1: Sequential Pipeline

```
[Sprint Prioritizer] → [UX Researcher] → [Backend Architect]
        |                    |                    |
   스프린트 계획          경쟁사 분석           API 설계
        ↓                    ↓                    ↓
         ─────────────────────→ [Frontend Developer]
                                      |
                                   UI 구현
                                      ↓
                               [Reality Checker]
                                  품질 게이트
```

#### 패턴 2: Parallel Fan-out (병렬 분기)

독립적인 작업은 동시 실행 가능:

```
[킥오프 요청]
      ├──→ [Content Creator]  : 마케팅 카피 작성
      └──→ [UI Designer]      : 시각 디자인 사양

      (두 작업 완료 후)
      ↓
[Frontend Developer] : 양쪽 출력을 받아 통합 구현
      ↓
[Growth Hacker] : 전환율 최적화 검토
      ↓
[배포]
```

Nexus Spatial 예시에서는 8개 에이전트가 **완전 병렬** 실행으로 ~10분 내 전략 도출 [[G-03]](#ref-g-03):

```
[단일 프로덕트 브리프]
    ├──→ Product Trend Researcher  (시장 검증)
    ├──→ Backend Architect          (기술 아키텍처)
    ├──→ Brand Guardian             (포지셔닝)
    ├──→ Growth Hacker              (GTM 전략)
    ├──→ Support Responder          (지원 시스템 설계)
    ├──→ UX Researcher              (사용자 연구)
    ├──→ XR Interface Architect     (공간 UI 설계)
    └──→ Project Shepherd           (타임라인·리스크)

[인간이 8개 출력 통합 → 전략 수렴]
```

#### 패턴 3: Quality Gate (품질 게이트)

Reality Checker 에이전트가 중간 검증자 역할:

```
[Week 1 개발 결과]
      ↓
[Reality Checker] → "실현 가능성 평가 + 스코프 삭감 권고"
      ↓ (승인)
[Week 2 계속 개발]
      ↓
[Reality Checker] → "런치 전 최종 품질 게이트"
      ↓ (승인)
[배포]
```

**수렴 포인트 (Convergence)**: Nexus 케이스에서 8개 에이전트가 독립적으로 동일한 결론("2D-first, WebXR 우선")에 도달하는 교차 검증 효과가 발생했다. [[G-03]](#ref-g-03)

---

## 4. 워크플로우/오케스트레이션 설계

#### 4주 스타트업 MVP 워크플로우

`examples/workflow-startup-mvp.md`에서 정의한 실전 워크플로우 [[G-04]](#ref-g-04):

**Week 1 — Discovery & Architecture**

```
병렬 실행:
├── Sprint Prioritizer: 4주 스프린트 분해
└── UX Researcher: 경쟁사 분석

순차 실행:
→ Backend Architect: API + DB 스키마 설계 (두 출력 수신)
```

**Week 2 — Core Development**

```
병렬 실행:
├── Frontend Developer: UI 구현
└── Backend (계속): 서버 구현

중간 게이트:
→ Reality Checker: 중간 점검 + 필수 스코프 삭감 결정
```

**Week 3-4 — Polish & Launch**

```
병렬 실행:
├── Growth Hacker: 런치 마케팅 전략
└── Frontend Developer: 마무리 구현

최종 게이트:
→ Reality Checker: 프로덕션 준비도 검증
→ 배포
```

#### 1일 랜딩페이지 스프린트

`examples/workflow-landing-page.md` [[G-04]](#ref-g-04):

```
09:00  병렬: Content Creator + UI Designer (독립 작업)
12:00  Frontend Developer: 두 출력 통합 → 구현
14:00  Growth Hacker: 전환율 검토
15:30  Frontend Developer: 최적화 반영
16:30  배포
```

#### Project Shepherd 에이전트의 오케스트레이션 역할

Project Shepherd는 다른 에이전트들의 조율자 역할을 담당하며 4단계 운영 사이클을 따른다 [[G-05]](#ref-g-05):

1. **프로젝트 착수**: 차터 개발, 성공 기준 정의, 리스크 식별
2. **팀 구성 & 킥오프**: 리소스 배분, 역할 명확화
3. **실행 조율**: 진행 모니터링, 의존성 관리, 이슈 에스컬레이션
4. **품질 확인 & 종료**: 전달물 검증, 문서화, 레트로스펙티브

**성공 지표**: 납기 준수율 95%, 스코프 크리프 10% 미만, 식별된 리스크 90% 사전 완화.

---

## 5. 도구(Tools) 시스템

#### 에이전트 자체에는 도구가 없다

이 프로젝트에서 "Tools"는 LLM이 호출하는 function tools를 의미하지 않는다. 각 에이전트는 **프롬프트 파일**이며, 실제 도구 호출은 Claude Code, Cursor 등 호스트 IDE가 담당한다.

에이전트가 활용하는 "도구"는 사실상 에이전트가 전문으로 하는 기술 스택이다:

**Backend Architect 에이전트의 기술 도구**:
- Infrastructure: PostgreSQL, Redis, Kafka, Elasticsearch
- Cloud: AWS/GCP/Azure
- API: FastAPI, gRPC, GraphQL
- Monitoring: Prometheus, Grafana

**AI Engineer 에이전트의 기술 도구**:
- ML Frameworks: TensorFlow, PyTorch, Hugging Face
- Deployment: FastAPI, MLflow, Docker
- Vector DB: Pinecone, Weaviate, Chroma

#### MCP Memory 연동: 유일한 실질적 Tool

`integrations/mcp-memory/`에 정의된 4개 MCP 도구가 유일한 실질적 Tool 연동이다 [[G-07]](#ref-g-07):

```json
// MCP 서버 설정 예시
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-memory"]
    }
  }
}
```

**MCP 메모리 4개 도구:**

| 도구 | 역할 | 사용 시점 |
|------|------|-----------|
| `remember` | 결정/산출물 저장 | 작업 완료 후 |
| `recall` | 이전 컨텍스트 검색 | 세션 시작 시 |
| `search` | 특정 정보 검색 | 핸드오프 시 |
| `rollback` | 이전 상태 복원 | QA 실패 시 |

**메모리 통합 패턴 예시 (Backend Architect with Memory):**

```markdown
## 🧠 Memory Integration

**On startup**: Search for previous context:
- recall("backend-architect [project-name]")
- recall("architecture decisions [project-name]")

**After key decisions**: Store with tags:
- remember("Database: PostgreSQL chosen for ACID compliance",
           tags=["backend-architect", "project-name", "database"])

**Before handoff**: Document for next agent:
- remember("Completed: API schema v2, Pending: Redis integration",
           tags=["handoff", "frontend-developer", "project-name"])

**On failure**: Rollback capability:
- search("last stable state [project-name]")
- rollback to known-good checkpoint
```

**일관된 태깅 원칙**: `[에이전트명]`, `[프로젝트명]`, `[토픽]` 3개 태그를 항상 포함해야 검색이 정확하다.

---

## 6. 상태 관리

#### 기본 모드: 무상태 (Stateless)

에이전트 간 상태 전달의 기본 메커니즘은 **프롬프트 내 텍스트 복사**다:

```
Agent A 출력:
"API 스키마: /users POST {name, email}, /posts GET [pagination]"

↓ 인간이 복사

Agent B 입력 프롬프트:
"이전 Backend Architect 출력:
[위 텍스트 붙여넣기]
이를 기반으로 프론트엔드를..."
```

이 방식의 한계: 세션 종료 시 컨텍스트 소실, 장기 프로젝트에서 누적 컨텍스트 관리 어려움.

#### 고급 모드: MCP Memory 기반 Persistent State

MCP 메모리 연동 시 상태 관리가 구조화된다:

```
[세션 1 — Backend Architect]
remember("DB: PostgreSQL + Prisma", tags=["retroboard", "backend", "database"])
remember("Auth: JWT + refresh tokens", tags=["retroboard", "backend", "auth"])

[세션 종료]

[세션 2 — Frontend Developer]
recall("retroboard backend")  →  "PostgreSQL + Prisma, JWT Auth..."
// 이전 세션 컨텍스트 자동 복원
```

**롤백 시나리오**:

```
[Reality Checker] → "Week 2 구현 품질 미달"

[Backend Architect]
search("retroboard last stable")
rollback("pre-week2-implementation")
// 알려진 안정 상태로 복원, 재구현 시작
```

---

## 7. Plan-Execute-Review 패턴

이 프로젝트는 명시적 Plan-Execute-Review 사이클을 채택하고 있다.

#### 에이전트 내부 사이클

각 에이전트의 Workflow Process 섹션이 이 패턴을 따른다:

```
[AI Engineer 에이전트 내부 사이클]
1. Plan:    requirements analysis → 비즈니스 문제 → ML 접근법 선택
2. Execute: model development → production deployment
3. Review:  drift detection → automated retraining → 성능 모니터링
```

```
[Backend Architect 내부 사이클]
1. Plan:    요구사항 분석 → 아키텍처 패턴 결정
2. Execute: 스키마 설계 → API 구현
3. Review:  보안 감사 → 성능 테스트
```

#### 워크플로우 레벨 사이클

Reality Checker 에이전트가 외부 Review 역할을 담당:

```
Sprint Prioritizer     → Plan   (스프린트 분해)
Backend + Frontend     → Execute (구현)
Reality Checker        → Review (품질 게이트)
       ↓ 승인
다음 스프린트 반복
```

**Quality Gate 기준 예시** (Reality Checker):
- 기능 구현 완성도 체크
- 성능 지표 달성 여부
- 범위 초과 여부 (스코프 크리프)
- 기술 부채 수준

---

## 8. 핵심 설계 철학

#### 원칙 1: 툴 독립성 (Tool Agnosticism)

동일한 에이전트 파일이 Claude Code, Cursor, Aider, Windsurf, Gemini CLI 등 9개 툴에서 동작한다. `convert.sh`가 포맷 변환을 자동화한다:

```bash
./scripts/convert.sh --tool cursor   # → .mdc 규칙 파일
./scripts/convert.sh --tool aider    # → CONVENTIONS.md 단일 파일
./scripts/convert.sh --tool openclaw # → SOUL.md + AGENTS.md + IDENTITY.md
```

#### 원칙 2: 좁고 깊은 전문화 (Deep Specialization)

CONTRIBUTING.md에서 명시한 핵심 원칙:

> "Narrow, deep specialization" — NOT generic personas
> "Strong Personality: Create distinctive voice; be specific rather than generic"

나쁜 예: "I help with frontend development"
좋은 예: "I default to finding 3-5 issues and require visual proof"

#### 원칙 3: 측정 가능한 성공 지표

모든 에이전트는 정량 지표를 포함해야 한다:

| 에이전트 | 지표 예시 |
|----------|-----------|
| Frontend Developer | Lighthouse 90+, 3G 로드 3초 미만 |
| AI Engineer | 정확도 85%+, 추론 지연 100ms 미만 |
| DevOps Automator | MTTR 30분 미만, 가동률 99.9%+ |
| Project Shepherd | 납기 준수 95%, 스코프 크리프 10% 미만 |

#### 원칙 4: 프롬프트 = 코드

에이전트 파일에 실제 실행 가능한 코드 예시를 포함해야 한다:

> "Concrete code examples... Practical: Real, runnable code — never pseudo-code"

#### 원칙 5: 개성 주도 (Personality-Driven)

`vibe` 필드로 에이전트 개성을 한 문장으로 압축:
- DevOps Automator: "Automates infrastructure so your team ships faster and sleeps better."
- Frontend Developer: "Builds responsive, accessible web apps with pixel-perfect precision."
- Rapid Prototyper: "Validates your idea in days, not weeks — ships first, perfects later."

---

## 9. 전략적 시사점

**기술 트렌드**

- 에이전트 정의의 표준화가 커뮤니티 주도로 진행 중: YAML frontmatter + 마크다운 본문이 de facto 스키마로 부상
- Plan-Execute-Review 패턴이 단일 에이전트 내부 루프와 멀티 에이전트 워크플로우 양쪽에서 동일하게 적용됨
- MCP 메모리 연동이 에이전트 협업의 핵심 인프라로 부상 (cross-session state)

**기회**

- ctoti 워크스페이스의 `.claude/skills/` 구조와 설계 철학이 유사: 스킬별 마크다운 파일 + 오케스트레이터 패턴
- `integrations/mcp-memory/` 패턴은 현재 운영 중인 intel-store MCP와 유사한 방식으로 적용 가능
- 에이전트 정의 시 "좁고 깊은 전문화" 원칙을 research-deep, validator 에이전트에 적용 검토 가치 있음
- Nexus Spatial 예시의 "독립 병렬 실행 후 수렴" 패턴은 현재 weekly-monitor Tier 2 병렬 처리와 동일한 설계

**위협 / 한계**

- 런타임 오케스트레이션 엔진 부재: 실제 에이전트 간 자동 통신 없이 인간 개입 필수
- 상태 관리의 취약성: 기본 모드에서 세션 종료 시 전체 컨텍스트 소실
- 5개+ 병렬 에이전트 실행 시 human orchestrator 부담 급증 (ctoti 워크스페이스의 hang 문제와 동일한 근원)

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- 에이전트 파일 스키마 (YAML frontmatter + 마크다운 본문): 실제 소스 파일 직접 확인 [A]
- Sequential handoff 방식이 기본 협업 패턴임: 공식 문서 + 예시 파일 교차 확인 [A]
- MCP memory 연동 구조: integrations/mcp-memory 디렉토리 및 README 직접 확인 [A]
- 30.7k 스타, 4.8k 포크 규모: GitHub 메인 페이지 직접 확인 [A]

**추가 검증 필요 [C/D]:**
- Reality Checker 에이전트의 실제 구현 내용 (파일 직접 미확인)
- 각 카테고리별 에이전트 전수 분석 (대표 샘플만 확인)
- `services` frontmatter 필드가 실제로 활용되는 사례 수

**데이터 공백:**
- 에이전트 실제 사용 통계 (사용자별 활성화 에이전트 수, 워크플로우 완료율)
- Community가 공유한 실전 워크플로우 패턴의 성공/실패 사례 분포
- 각 IDE 통합별 에이전트 동작 차이 상세

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | msitarzewski/agency-agents — GitHub 메인 페이지 | [링크](https://github.com/msitarzewski/agency-agents) | repo | 2026-03-12 | [A] |
| <a id="ref-g-02"></a>G-02 | agency-agents — Frontend Developer 에이전트 파일 | [링크](https://raw.githubusercontent.com/msitarzewski/agency-agents/main/engineering/engineering-frontend-developer.md) | agent-file | 2026-03-12 | [A] |
| <a id="ref-g-03"></a>G-03 | agency-agents — Nexus Spatial Discovery 예시 | [링크](https://raw.githubusercontent.com/msitarzewski/agency-agents/main/examples/nexus-spatial-discovery.md) | example | 2026-03-12 | [A] |
| <a id="ref-g-04"></a>G-04 | agency-agents — Startup MVP + Landing Page 워크플로우 | [링크](https://raw.githubusercontent.com/msitarzewski/agency-agents/main/examples/workflow-startup-mvp.md) | example | 2026-03-12 | [A] |
| <a id="ref-g-05"></a>G-05 | agency-agents — Project Shepherd 에이전트 | [링크](https://raw.githubusercontent.com/msitarzewski/agency-agents/main/project-management/project-management-project-shepherd.md) | agent-file | 2026-03-12 | [A] |
| <a id="ref-g-06"></a>G-06 | agency-agents — CONTRIBUTING.md (에이전트 스키마 정의) | [링크](https://raw.githubusercontent.com/msitarzewski/agency-agents/main/CONTRIBUTING.md) | doc | 2026-03-12 | [A] |
| <a id="ref-g-07"></a>G-07 | agency-agents — MCP Memory 통합 README | [링크](https://raw.githubusercontent.com/msitarzewski/agency-agents/main/integrations/mcp-memory/README.md) | doc | 2026-03-12 | [A] |
| <a id="ref-g-08"></a>G-08 | agency-agents — integrations README (툴별 변환 방식) | [링크](https://raw.githubusercontent.com/msitarzewski/agency-agents/main/integrations/README.md) | doc | 2026-03-12 | [A] |
| <a id="ref-g-09"></a>G-09 | agency-agents — convert.sh 소스 | [링크](https://raw.githubusercontent.com/msitarzewski/agency-agents/main/scripts/convert.sh) | script | 2026-03-12 | [A] |
| <a id="ref-g-10"></a>G-10 | agency-agents — Backend Architect with Memory 예시 | [링크](https://raw.githubusercontent.com/msitarzewski/agency-agents/main/integrations/mcp-memory/backend-architect-with-memory.md) | example | 2026-03-12 | [A] |
| <a id="ref-g-11"></a>G-11 | agency-agents — Workflow with Memory 예시 | [링크](https://raw.githubusercontent.com/msitarzewski/agency-agents/main/examples/workflow-with-memory.md) | example | 2026-03-12 | [A] |
