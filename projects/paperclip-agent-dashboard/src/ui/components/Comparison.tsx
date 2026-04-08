import React from "react";
import type { AgentMetrics, HeartbeatRun } from "../types.js";
import { formatDuration, formatPercent } from "../utils/formatters.js";
import { getRecentWeeks, groupRunsByWeek, getWeeklyValues } from "../utils/weekly.js";
import { Sparkline } from "./Sparkline.js";
import { Heatmap } from "./Heatmap.js";

// --- Badges ---

interface BadgeRule {
  id: string;
  label: string;
  icon: string;
  color: string;
}

function getBadges(m: AgentMetrics, all: AgentMetrics[], weeklyValues: number[]): BadgeRule[] {
  const badges: BadgeRule[] = [];
  const active = all.filter((a) => a.totalRuns > 0 || a.issuesDone > 0);
  if (active.length === 0) return badges;

  if (m.issuesDone > 0 && m.issuesDone === Math.max(...active.map((a) => a.issuesDone))) {
    badges.push({ id: "top", label: "Top Producer", icon: "^", color: "#7c6ef0" });
  }
  if (m.avgRunDurationMs > 0 && m.avgRunDurationMs === Math.min(...active.filter((a) => a.avgRunDurationMs > 0).map((a) => a.avgRunDurationMs))) {
    badges.push({ id: "fast", label: "Fastest", icon: "*", color: "#0891b2" });
  }
  if (m.runSuccessRate > 0 && m.runSuccessRate === Math.max(...active.filter((a) => a.totalRuns > 0).map((a) => a.runSuccessRate))) {
    badges.push({ id: "reliable", label: "Most Reliable", icon: "v", color: "#059669" });
  }
  // Rising: last 2 weeks vs previous 2 weeks
  if (weeklyValues.length >= 4) {
    const recent = weeklyValues.slice(-2).reduce((a, b) => a + b, 0);
    const prev = weeklyValues.slice(-4, -2).reduce((a, b) => a + b, 0);
    if (prev > 0 && recent / prev >= 1.2) {
      badges.push({ id: "rising", label: "Rising", icon: "+", color: "#d97706" });
    }
  }
  // Consistent: last 4 weeks all > 0
  if (weeklyValues.length >= 4 && weeklyValues.slice(-4).every((v) => v > 0)) {
    badges.push({ id: "consistent", label: "Consistent", icon: "=", color: "#10b981" });
  }

  return badges;
}

function Badge({ badge }: { badge: BadgeRule }) {
  return (
    <span
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: "3px",
        padding: "2px 8px",
        borderRadius: "999px",
        fontSize: "11px",
        fontWeight: 600,
        color: badge.color,
        background: `${badge.color}18`,
        border: `1px solid ${badge.color}40`,
      }}
    >
      {badge.label}
    </span>
  );
}

// --- Progress Bar ---

function ProgressBar({ value, max, color }: { value: number; max: number; color: string }) {
  const pct = max > 0 ? Math.min((value / max) * 100, 100) : 0;
  return (
    <div style={{ flex: 1, background: "#111", borderRadius: "4px", height: "6px" }}>
      <div style={{ width: `${Math.max(pct, 1)}%`, height: "100%", background: color, borderRadius: "4px", transition: "width 0.3s" }} />
    </div>
  );
}

// --- Score color ---

function scoreColor(score: number): string {
  if (score >= 70) return "#10b981";
  if (score >= 40) return "#f59e0b";
  return "#ef4444";
}

// --- Main ---

export function Comparison({
  allMetrics,
  runs,
}: {
  allMetrics: AgentMetrics[];
  runs: HeartbeatRun[];
}) {
  const weeks = getRecentWeeks(8);
  const active = allMetrics.filter((m) => m.totalRuns > 0 || m.issuesDone > 0);
  const inactive = allMetrics.filter((m) => m.totalRuns === 0 && m.issuesDone === 0);

  const maxIssues = Math.max(...active.map((m) => m.issuesDone), 1);
  const maxRuns = Math.max(...active.map((m) => m.totalRuns), 1);

  // Heatmap data
  const heatmapData: Record<string, Record<string, number>> = {};
  for (const m of active) {
    heatmapData[m.agentId] = groupRunsByWeek(runs, m.agentId);
  }

  return (
    <div>
      {/* Activity Heatmap */}
      <h3 style={{ fontSize: "14px", color: "#e0e0e0", marginBottom: "16px" }}>Activity Heatmap</h3>
      <div style={{
        padding: "20px",
        background: "#0d0d0d",
        borderRadius: "8px",
        border: "1px solid #2a2a2a",
        marginBottom: "32px",
      }}>
        <Heatmap
          agents={active.map((m) => ({ id: m.agentId, name: m.name }))}
          weeks={weeks}
          data={heatmapData}
        />
      </div>

      {/* Agent KPI Cards */}
      <h3 style={{ fontSize: "14px", color: "#e0e0e0", marginBottom: "16px" }}>Agent KPI</h3>
      <div style={{ display: "flex", flexDirection: "column" as const, gap: "12px" }}>
        {active.map((m) => {
          const weeklyValues = getWeeklyValues(runs, m.agentId, weeks);
          const badges = getBadges(m, allMetrics, weeklyValues);

          return (
            <div
              key={m.agentId}
              style={{
                padding: "16px 20px",
                background: "#1a1a1a",
                borderRadius: "8px",
                border: "1px solid #2a2a2a",
                display: "grid",
                gridTemplateColumns: "160px 1fr auto",
                gap: "16px",
                alignItems: "center",
              }}
            >
              {/* Profile + Badge */}
              <div>
                <div style={{ display: "flex", alignItems: "center", gap: "8px", marginBottom: "4px" }}>
                  <span style={{
                    fontSize: "18px",
                    fontWeight: "bold",
                    color: scoreColor(m.apiScore),
                  }}>
                    {m.apiScore}
                  </span>
                  <span style={{ fontSize: "15px", fontWeight: "bold", color: "#e0e0e0" }}>{m.name}</span>
                </div>
                <div style={{ fontSize: "11px", color: "#666", marginBottom: "8px" }}>{m.title || m.role}</div>
                {badges.length > 0 && (
                  <div style={{ display: "flex", gap: "4px", flexWrap: "wrap" as const }}>
                    {badges.map((b) => <Badge key={b.id} badge={b} />)}
                  </div>
                )}
              </div>

              {/* KPI bars */}
              <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: "12px" }}>
                <div>
                  <div style={{ fontSize: "10px", color: "#555", marginBottom: "4px" }}>완료 이슈</div>
                  <div style={{ fontSize: "14px", fontWeight: "bold", color: "#e0e0e0", marginBottom: "4px" }}>{m.issuesDone}</div>
                  <ProgressBar value={m.issuesDone} max={maxIssues} color="#7c6ef0" />
                </div>
                <div>
                  <div style={{ fontSize: "10px", color: "#555", marginBottom: "4px" }}>실행 횟수</div>
                  <div style={{ fontSize: "14px", fontWeight: "bold", color: "#e0e0e0", marginBottom: "4px" }}>{m.totalRuns}</div>
                  <ProgressBar value={m.totalRuns} max={maxRuns} color="#3b82f6" />
                </div>
                <div>
                  <div style={{ fontSize: "10px", color: "#555", marginBottom: "4px" }}>성공률</div>
                  <div style={{ fontSize: "14px", fontWeight: "bold", color: "#e0e0e0", marginBottom: "4px" }}>
                    {m.totalRuns > 0 ? formatPercent(m.runSuccessRate) : "-"}
                  </div>
                  <ProgressBar value={m.runSuccessRate} max={100} color={m.runSuccessRate >= 90 ? "#10b981" : "#f59e0b"} />
                </div>
                <div>
                  <div style={{ fontSize: "10px", color: "#555", marginBottom: "4px" }}>평균 시간</div>
                  <div style={{ fontSize: "14px", fontWeight: "bold", color: "#e0e0e0" }}>
                    {m.avgRunDurationMs > 0 ? formatDuration(m.avgRunDurationMs) : "-"}
                  </div>
                </div>
              </div>

              {/* Sparkline */}
              <div style={{ textAlign: "center" as const }}>
                <div style={{ fontSize: "10px", color: "#555", marginBottom: "4px" }}>8주 추세</div>
                <Sparkline values={weeklyValues} width={100} height={28} />
              </div>
            </div>
          );
        })}
      </div>

      {/* Inactive */}
      {inactive.length > 0 && (
        <div style={{ marginTop: "24px" }}>
          <span style={{ fontSize: "12px", color: "#444" }}>
            미활동: {inactive.map((m) => m.name).join(", ")}
          </span>
        </div>
      )}
    </div>
  );
}
