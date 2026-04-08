import React from "react";
import type { TeamOverviewData, AgentMetrics, Issue } from "../types.js";
import { formatDuration, formatPercent } from "../utils/formatters.js";
import { calcRoi, type RoiSummary } from "../utils/roi.js";

const cardContainerStyle: React.CSSProperties = {
  display: "grid",
  gridTemplateColumns: "repeat(4, 1fr)",
  gap: "16px",
  marginBottom: "32px",
};

const cardStyle: React.CSSProperties = {
  padding: "20px",
  background: "#1a1a1a",
  borderRadius: "8px",
  border: "1px solid #2a2a2a",
};

const cardLabel: React.CSSProperties = {
  fontSize: "12px",
  color: "#888",
  textTransform: "uppercase" as const,
  letterSpacing: "0.05em",
  marginBottom: "8px",
};

const cardValue: React.CSSProperties = {
  fontSize: "28px",
  fontWeight: "bold",
  color: "#e0e0e0",
};

function MetricCard({ label, value, unit }: { label: string; value: string | number; unit?: string }) {
  return (
    <div style={cardStyle}>
      <div style={cardLabel}>{label}</div>
      <div style={cardValue}>
        {value}{unit && <span style={{ fontSize: "16px", color: "#888", marginLeft: "4px" }}>{unit}</span>}
      </div>
    </div>
  );
}

const tableStyle: React.CSSProperties = {
  width: "100%",
  borderCollapse: "collapse" as const,
};

const thStyle: React.CSSProperties = {
  textAlign: "left" as const,
  padding: "12px 16px",
  borderBottom: "1px solid #2a2a2a",
  color: "#888",
  fontSize: "12px",
  textTransform: "uppercase" as const,
  letterSpacing: "0.05em",
};

const tdStyle: React.CSSProperties = {
  padding: "12px 16px",
  borderBottom: "1px solid #1a1a1a",
  color: "#e0e0e0",
  fontSize: "14px",
};

function scoreColor(score: number): string {
  if (score >= 70) return "#10b981";
  if (score >= 40) return "#f59e0b";
  return "#ef4444";
}

function statusBadge(status: string): React.ReactNode {
  const colors: Record<string, string> = {
    idle: "#10b981",
    running: "#3b82f6",
    paused: "#888",
    error: "#ef4444",
  };
  return (
    <span style={{
      display: "inline-block",
      width: "8px",
      height: "8px",
      borderRadius: "50%",
      background: colors[status] || "#888",
      marginRight: "6px",
    }} />
  );
}

export function TeamOverview({
  data,
  issues,
  onSelectAgent,
}: {
  data: TeamOverviewData;
  issues: Issue[];
  onSelectAgent: (agentId: string) => void;
}) {
  const { summary, rankings } = data;
  const roi = calcRoi(issues);

  return (
    <div>
      <div style={cardContainerStyle}>
        <MetricCard label="완료 이슈" value={summary.totalCompleted} />
        <MetricCard
          label="평균 완료 시간"
          value={summary.avgCompletionTimeMs > 0 ? formatDuration(summary.avgCompletionTimeMs) : "-"}
        />
        <MetricCard label="실행 성공률" value={formatPercent(summary.teamSuccessRate)} />
        <MetricCard
          label="활성 에이전트"
          value={`${summary.activeAgents}/${summary.totalAgents}`}
        />
      </div>

      {roi.issueCount > 0 && (
        <>
          <h2 style={{ fontSize: "16px", color: "#e0e0e0", marginBottom: "16px" }}>ROI — 시간 절감 효과</h2>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: "16px", marginBottom: "32px" }}>
            <div style={{ ...cardStyle, borderLeft: "3px solid #10b981" }}>
              <div style={cardLabel}>누적 절감 시간</div>
              <div style={cardValue}>
                {roi.totalSavedHours > 0 ? "+" : ""}{roi.totalSavedHours}h
              </div>
              <div style={{ color: "#666", fontSize: "11px" }}>{roi.totalSavedWorkingDays} 워킹일</div>
            </div>
            <div style={{ ...cardStyle, borderLeft: "3px solid #3b82f6" }}>
              <div style={cardLabel}>이번 주 절감</div>
              <div style={cardValue}>
                {roi.thisWeekSavedHours > 0 ? "+" : ""}{roi.thisWeekSavedHours}h
              </div>
            </div>
            <div style={{ ...cardStyle, borderLeft: "3px solid #7c6ef0" }}>
              <div style={cardLabel}>건당 평균 절감</div>
              <div style={cardValue}>
                {roi.avgSavedPerIssueHours > 0 ? "+" : ""}{roi.avgSavedPerIssueHours}h
              </div>
              <div style={{ color: "#666", fontSize: "11px" }}>{roi.issueCount}건 기준</div>
            </div>
          </div>
        </>
      )}

      <h2 style={{ fontSize: "16px", color: "#e0e0e0", marginBottom: "16px" }}>에이전트 랭킹</h2>
      <table style={tableStyle}>
        <thead>
          <tr>
            <th style={thStyle}>#</th>
            <th style={thStyle}>이름</th>
            <th style={thStyle}>담당</th>
            <th style={thStyle}>상태</th>
            <th style={thStyle}>완료 이슈</th>
            <th style={thStyle}>평균 소요</th>
            <th style={thStyle}>성공률</th>
            <th style={thStyle}>실행 횟수</th>
            <th style={thStyle}>종합 점수</th>
          </tr>
        </thead>
        <tbody>
          {rankings.map((m: AgentMetrics, i: number) => (
            <tr
              key={m.agentId}
              style={{ cursor: "pointer" }}
              onClick={() => onSelectAgent(m.agentId)}
              onMouseEnter={(e) => {
                (e.currentTarget as HTMLElement).style.background = "#1a1a1a";
              }}
              onMouseLeave={(e) => {
                (e.currentTarget as HTMLElement).style.background = "transparent";
              }}
            >
              <td style={tdStyle}>{i + 1}</td>
              <td style={{ ...tdStyle, fontWeight: "bold" }}>{m.name}</td>
              <td style={{ ...tdStyle, color: "#888" }}>{m.title || m.role}</td>
              <td style={tdStyle}>{statusBadge(m.status)}{m.status}</td>
              <td style={tdStyle}>{m.issuesDone}</td>
              <td style={tdStyle}>{m.avgRunDurationMs > 0 ? formatDuration(m.avgRunDurationMs) : "-"}</td>
              <td style={tdStyle}>{m.totalRuns > 0 ? formatPercent(m.runSuccessRate) : "-"}</td>
              <td style={tdStyle}>{m.totalRuns}</td>
              <td style={tdStyle}>
                <span style={{
                  fontWeight: "bold",
                  color: scoreColor(m.apiScore),
                }}>
                  {m.apiScore}
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
