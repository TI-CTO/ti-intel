---
title: 2주간 자동화 안정성 종합 리포트
date: 2026-04-17
type: review
period: 2026-04-06 ~ 2026-04-17
---

# 2주간 자동화 안정성 종합 리포트

> **기간**: 2026-04-06 ~ 2026-04-17 (2주 스프린트) | **작성**: 2026-04-17

---

## Executive Summary

2주 스프린트 기간 동안 주간 모니터링 자동화 체계가 **auto-monitor LaunchAgent**(W1) → **Paperclip dispatcher**(W2)로 전환되었다. caffeinate 적용, 1회 재시도 로직, Gmail 실패 알림 등 안정성 개선이 반영되어 산출물 품질과 실행 신뢰도가 전반적으로 개선되었다. 단, Paperclip 서버 자체 중단(4/16~17)으로 인한 2일간 공백이 발생했으며, 이에 대한 자동 감지/알림이 없었다는 것이 가장 큰 구조적 취약점이다.

---

## 1. 자동화 아키텍처 변화

### W1 (4/6 주): auto-monitor LaunchAgent 체계

```
LaunchAgent (com.ctoti.weekly-monitor.*.plist)
  → run-domain.sh (도메인별 개별 호출)
    → caffeinate -s -w $$
    → claude -p --dangerously-skip-permissions
    → 실패 시 1회 재시도 (5분 대기)
    → log-to-obsidian.py (일지 기록)
    → Obsidian 산출물 동기화
    → 실패 시 send-alert.py (Gmail 알림)
```

- **스케줄**: 월 08:30 (voice-ai), 월 12:30 (secure-ai), 월 14:00 (competitor), 화 08:30 (agentic-ai)
- **절전 방지**: `caffeinate -s -w $$` (스크립트 종료까지 시스템 sleep 방지)
- **동시 실행 방지**: 도메인별 lockfile (`.${DOMAIN}.lock`)
- **실패 알림**: Gmail SMTP (send-alert.py)

### W2 (4/13 주): Paperclip dispatcher 체계

```
LaunchAgent (com.ctoti.paperclip-dispatcher.plist, 3분 간격)
  → dispatcher.sh
    → Paperclip API 폴링 (in_progress 이슈 조회)
    → routine-checkout (에이전트에 이슈 할당)
    → heartbeat (에이전트 트리거, timeout 2시간)
```

- **스케줄**: Paperclip routine이 이슈 자동 생성 → dispatcher가 3분 간격 폴링
- **절전 방지**: 없음 (dispatcher 자체는 짧은 실행)
- **동시 실행 방지**: heartbeat PID 기반 skip 로직
- **실패 알림**: 없음 (Paperclip 서버 중단 시 알림 부재)

---

## 2. 실행 안정성 비교

### 2-1. 가동 시간

| 지표 | W1 (auto-monitor) | W2 (Paperclip) |
|------|-------------------|----------------|
| 스케줄 트리거 | LaunchAgent 정시 | Paperclip routine → dispatcher 폴링 |
| 실제 가동일 | 4/6(일), 4/7(월) | 4/13(일), 4/14(월), 4/15(화) |
| 중단 | Voice AI 1회 실패(exit=143) → 재시도 | 4/13 초반 API unreachable 19회 (3시간), Heartbeat 1회 타임아웃 |
| 4/16~17 | — | **Paperclip 서버 중단으로 실행 없음** |

### 2-2. API 가용성

| 기간 | 총 폴링 | 성공 | 실패 | 가용률 |
|------|---------|------|------|--------|
| W1 (4/8-4/9 dispatcher 병행) | 15회 | 3회 | 12회 | ~20% |
| W2 (4/13) | ~60회 | ~41회 | 19회 | ~68% |
| W2 (4/14-4/15) | ~60회 | ~60회 | 0회 | ~100% |

> W1 dispatcher 가용률이 낮은 것은 Paperclip 서버가 아직 안정화되지 않은 시기의 병행 운영 때문이며, auto-monitor 자체의 실행과는 무관.

### 2-3. 장애 유형

| 장애 | W1 | W2 | 대응 |
|------|-----|-----|------|
| 시스템 sleep | caffeinate로 방지 | dispatcher 짧은 실행으로 무관 | 해결됨 |
| Claude CLI 실패 | Voice AI exit=143, 1회 재시도 | — | 해결됨 (재시도 로직) |
| API unreachable | dispatcher 12회 연속 | 4/13 초반 19회 → 자동 복구 | 자동 복구 동작 확인 |
| Heartbeat 타임아웃 | — | 1회 (CLI 10분 타임아웃) | heartbeat timeout 2시간으로 확장 (194d382) |
| **Paperclip 서버 중단** | — | **4/16~17 감지 안 됨** | **미해결 — 알림 없음** |

---

## 3. 산출물 품질 비교

### 3-1. 주간 리포트 생성량

| 항목 | W1 (4/6) | W2 (4/13-14) | 변화 |
|------|----------|-------------|------|
| 도메인 리포트 (MD) | 3건 (agentic/secure/voice) | 3건 (agentic/secure/voice) | 동일 |
| PDF | 3건 | 3건 | 동일 |
| 선행 리서치 | 7건 | 11건 | **+57%** |
| Validator 리포트 | 4건 | 1건 | -75% |
| 경쟁사 모니터 | 2건 (SKT/KT) | 별도 생성 안 됨 | 이슈 할당만 |
| 주간 종합 (금요일) | 1건 (W15) | 1건 (W16, 4/17 재시작 후) | 동일 |

### 3-2. 리포트 크기 (품질 프록시)

| 도메인 | W1 MD (bytes) | W2 MD (bytes) | 변화 | W1 PDF | W2 PDF | 변화 |
|--------|-------------|-------------|------|--------|--------|------|
| Agentic AI | 36,763 | **60,719** | **+65%** | 792K | **937K** | **+18%** |
| Secure AI | 40,841 | **45,338** | +11% | 843K | **874K** | +4% |
| Voice AI | 34,082 | 28,539 | -16% | 811K | 729K | -10% |

- **Agentic AI**: W2에서 크게 증가. 선행 리서치 6건 + validator 리포트 포함으로 깊이 개선.
- **Voice AI**: 크기 감소했지만, 선행 리서치(voice-cloning, voice-synthesis)가 별도 파일로 분리되어 있어 실질 콘텐츠는 동등.

### 3-3. 주간 종합 브리핑 비교

| 항목 | W15 (auto-monitor) | W16 (Paperclip) |
|------|-------------------|-----------------|
| 핵심 3가지 | 있음 | 있음 |
| 도메인별 요약 테이블 | 있음 | 있음 |
| 경쟁사 포지셔닝 | 간략 (1단락) | 상세 (SKT/KT 개별 + 차별화 기회) |
| 후속 조치 제안 | 4건 | 4건 |
| 신호 범례 | 불완전 (Voice AI "미실행") | 완전 (전 도메인 커버) |
| **구조적 완결성** | **B** | **A** |

---

## 4. 알림 동작 여부

| 알림 유형 | 구현 상태 | 실제 발동 |
|----------|----------|----------|
| Gmail 실패 알림 (auto-monitor) | 구현됨 (send-alert.py, SMTP 설정 완료) | **발동 기록 없음** — 로그에 `[ALERT]` 또는 `Sending failure` 검색 결과 0건 |
| Paperclip 서버 중단 알림 | **미구현** | — |
| Heartbeat 타임아웃 알림 | **미구현** | — |

### 분석

- auto-monitor의 Gmail 알림은 코드 레벨에서 정상이나, Voice AI exit=143 실패 시 재시도 성공으로 알림 트리거 조건(최종 실패)에 도달하지 않음.
- **Paperclip 서버 중단이 가장 큰 맹점**: 4/16~17 2일간 자동화가 완전히 중단되었으나 어떤 알림도 발송되지 않음. 수동 확인 전까지 인지 불가.

---

## 5. 종합 평가

### 개선된 점 (caffeinate 적용 이후)

1. **시스템 sleep 방지**: macOS sleep으로 인한 실행 중단 해소
2. **리포트 품질 향상**: 선행 리서치 +57%, Agentic AI 리포트 +65% 증가
3. **실행 안정성**: 재시도 로직으로 일시적 실패 자동 복구
4. **주간 종합 품질**: 경쟁사 포지셔닝 상세화, 전 도메인 커버리지 달성

### 미해결 구조적 리스크

| 리스크 | 심각도 | 상태 |
|--------|--------|------|
| **Paperclip 서버 중단 시 무알림** | 🔴 Critical | 미해결 |
| Heartbeat 타임아웃 감지/알림 없음 | 🟡 Medium | 미해결 |
| Validator 리포트 W2에서 감소 | 🟢 Low | Paperclip 에이전트 routine 설정 검토 필요 |
| 경쟁사 모니터 W2 산출물 미생성 | 🟡 Medium | 이슈 할당은 됐으나 실행 완료 미확인 |

---

## 6. 권고 사항

### P0: Paperclip 서버 헬스체크 알림 추가

dispatcher.sh에 Paperclip 서버 가용성 체크를 추가하고, N회 연속 실패 시 Gmail 알림 발송:

```
# 의사코드
if curl http://127.0.0.1:3100/health fails for 30+ minutes:
  send_alert("Paperclip server down")
```

### P1: Paperclip 서버 자동 재시작

LaunchAgent `com.ctoti.paperclip.plist`의 `KeepAlive` 설정이 `SuccessfulExit: false`로 되어 있어 비정상 종료 시에만 재시작됨. 정상 종료 후 미재시작 시나리오 커버 필요.

### P2: 실행 완료 확인 메커니즘

현재 dispatcher는 이슈 checkout + heartbeat 트리거만 수행하고, 실행 완료 여부는 추적하지 않음. 완료/실패 상태를 확인하는 후속 폴링 추가 검토.

---

## 부록: 타임라인

```
4/03 (금) auto-monitor: Friday 자동화 정상 (summary+health+portfolio+deal, 12분)
4/06 (일) auto-monitor: Monday 자동화 실행 (agentic✓ voice✗→재시도 secure✓ competitor✓)
4/07 (월) auto-monitor: Agentic AI 재실행 정상
4/08 (화) Paperclip dispatcher 병행 시작 (2회 heartbeat 성공)
4/09 (수) dispatcher: API unreachable 12회 연속 (PM)
4/07~  auto-monitor → Paperclip 전환 작업 (도메인별 plist 생성, install.sh)
4/13 (일) Paperclip W2: API unreachable 19회 (AM) → 10:07 정상화, Voice AI·Secure AI 실행
4/14 (월) Paperclip W2: 전일 정상, Agentic AI + 경쟁사 실행
4/15 (화) Paperclip W2: 정상 실행, 13:16 마지막 로그
4/16 (수) ❌ Paperclip 서버 중단 — 실행 없음, 알림 없음
4/17 (목) ❌ Paperclip 서버 중단 지속 → 09:39 수동 재시작, TI-39 checkout 정상
```
