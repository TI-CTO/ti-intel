import React, { useState } from "react";
import { usePluginData, usePluginAction } from "@paperclipai/plugin-sdk/ui";
import type { Agent, AgentMetrics, Issue, HeartbeatRun, OutputFile } from "../types.js";
import { formatDuration, formatPercent, timeAgo } from "../utils/formatters.js";

const cardContainerStyle: React.CSSProperties = {
  display: "grid",
  gridTemplateColumns: "repeat(4, 1fr)",
  gap: "16px",
  marginBottom: "32px",
};

const cardStyle: React.CSSProperties = {
  padding: "16px",
  background: "#1a1a1a",
  borderRadius: "8px",
  border: "1px solid #2a2a2a",
};

const thStyle: React.CSSProperties = {
  textAlign: "left" as const,
  padding: "10px 12px",
  borderBottom: "1px solid #2a2a2a",
  color: "#888",
  fontSize: "12px",
  textTransform: "uppercase" as const,
};

const tdStyle: React.CSSProperties = {
  padding: "10px 12px",
  borderBottom: "1px solid #1a1a1a",
  color: "#e0e0e0",
  fontSize: "13px",
};

function statusColor(status: string): string {
  const colors: Record<string, string> = {
    done: "#10b981",
    in_progress: "#3b82f6",
    todo: "#f59e0b",
    backlog: "#888",
    succeeded: "#10b981",
    failed: "#ef4444",
  };
  return colors[status] || "#888";
}

// 에이전트 → 담당 도메인/키워드 매핑
const AGENT_DOMAIN_MAP: Record<string, string[]> = {
  "안춘수": ["voice-ai", "voice"],
  "김보경": ["secure-ai", "secure"],
  "서진": ["agentic-ai", "agentic"],
  "장재현": ["competitor", "경쟁사", "weekly-summary", "summary"],
  "선우혜자": ["startup"],
  "탁현욱": ["secure-ai"],
  "황경민": ["weekly"],
};

function getAgentOutputs(agentName: string, issues: Issue[], files: OutputFile[]): OutputFile[] {
  const mdFiles = files.filter((f) => f.type === "md");
  const found = new Set<string>();

  // 1차: 도메인 매핑 기반
  const domains = AGENT_DOMAIN_MAP[agentName];
  if (domains) {
    for (const f of mdFiles) {
      if (domains.some((d) => f.path.toLowerCase().includes(d) || f.name.toLowerCase().includes(d))) {
        found.add(f.path);
      }
    }
  }

  // 2차: 이슈 기반 매칭 (할당된 이슈의 산출물)
  for (const issue of issues) {
    const matched = matchFilesToIssue(issue, mdFiles);
    for (const f of matched) {
      found.add(f.path);
    }
  }

  return mdFiles
    .filter((f) => found.has(f.path))
    .sort((a, b) => new Date(b.modified).getTime() - new Date(a.modified).getTime())
    .slice(0, 8);
}

function toKSTDate(isoDate: string): string {
  const d = new Date(isoDate);
  const kst = new Date(d.getTime() + 9 * 60 * 60 * 1000);
  return kst.toISOString().slice(0, 10);
}

function matchFilesToIssue(issue: Issue, files: OutputFile[]): OutputFile[] {
  if (!issue.completedAt && !issue.startedAt) return [];
  const refDate = issue.completedAt || issue.startedAt || "";
  if (!refDate) return [];

  const issueDate = toKSTDate(refDate);
  const titleLower = issue.title.toLowerCase();
  const keywords = titleLower
    .replace(/[^\w\s가-힣]/g, "")
    .split(/\s+/)
    .filter((w) => w.length > 2);

  return files.filter((f) => {
    if (f.type !== "md") return false;
    const fileDate = f.name.slice(0, 10);
    if (fileDate !== issueDate) return false;
    // 키워드 매칭 또는 research/weekly/startup 패턴 매칭
    const nameLower = f.name.toLowerCase();
    const keywordMatch = keywords.some((kw) => nameLower.includes(kw));
    const patternMatch = /_(weekly|research|startup|monitor|summary)/.test(nameLower);
    return keywordMatch || patternMatch;
  });
}

const markdownStyles = `
  .md-viewer { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
  .md-viewer h1 { font-size: 1.6em; border-bottom: 1px solid #333; padding-bottom: 8px; margin: 24px 0 16px; color: #f0f0f0; }
  .md-viewer h2 { font-size: 1.3em; border-bottom: 1px solid #2a2a2a; padding-bottom: 6px; margin: 20px 0 12px; color: #e8e8e8; }
  .md-viewer h3 { font-size: 1.1em; margin: 16px 0 8px; color: #e0e0e0; }
  .md-viewer p { margin: 8px 0; line-height: 1.7; }
  .md-viewer ul, .md-viewer ol { padding-left: 24px; margin: 8px 0; }
  .md-viewer li { margin: 4px 0; line-height: 1.6; }
  .md-viewer table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 0.9em; }
  .md-viewer th { background: #1a1a1a; padding: 8px 12px; border: 1px solid #333; text-align: left; color: #aaa; font-weight: 600; }
  .md-viewer td { padding: 6px 12px; border: 1px solid #2a2a2a; }
  .md-viewer code { background: #1a1a1a; padding: 2px 6px; border-radius: 3px; font-size: 0.9em; color: #e8b4b8; }
  .md-viewer pre { background: #111; padding: 16px; border-radius: 6px; overflow-x: auto; border: 1px solid #2a2a2a; }
  .md-viewer pre code { background: none; padding: 0; color: #d0d0d0; }
  .md-viewer blockquote { border-left: 3px solid #7c6ef0; padding: 8px 16px; margin: 12px 0; color: #aaa; background: #1a1a1a20; }
  .md-viewer a { color: #7c6ef0; text-decoration: none; }
  .md-viewer a:hover { text-decoration: underline; }
  .md-viewer strong { color: #f0f0f0; }
  .md-viewer hr { border: none; border-top: 1px solid #2a2a2a; margin: 20px 0; }
`;

function FileViewer({ filePath }: { filePath: string }) {
  const result = usePluginData("file-content", { filePath });

  if (result.loading) {
    return <div style={{ padding: "16px", color: "#888" }}>Loading...</div>;
  }

  const data = result.data as { type?: string; html?: string; error?: string } | null;

  if (!data || data.error) {
    return <div style={{ padding: "16px", color: "#ef4444" }}>{data?.error || "Failed to load"}</div>;
  }

  if (data.type === "pdf") {
    return <div style={{ padding: "16px", color: "#888" }}>PDF 파일은 미리보기를 지원하지 않습니다.</div>;
  }

  return (
    <>
      <style dangerouslySetInnerHTML={{ __html: markdownStyles }} />
      <div
        className="md-viewer"
        style={{
          padding: "24px 32px",
          background: "#0d0d0d",
          borderRadius: "8px",
          border: "1px solid #2a2a2a",
          maxHeight: "600px",
          overflow: "auto",
          fontSize: "14px",
          lineHeight: "1.7",
          color: "#d0d0d0",
        }}
        dangerouslySetInnerHTML={{ __html: data.html || "" }}
        onClick={(e) => {
          const target = e.target as HTMLElement;
          const anchor = target.closest("a");
          if (!anchor) return;
          const href = anchor.getAttribute("href") || "";
          if (href.startsWith("#")) {
            e.preventDefault();
            const el = (e.currentTarget as HTMLElement).querySelector(href);
            if (el) el.scrollIntoView({ behavior: "smooth" });
          }
        }}
      />
    </>
  );
}

export function AgentDetail({
  agent,
  metrics,
  recentIssues,
  recentRuns,
  agents,
  onSelectAgent,
}: {
  agent: Agent;
  metrics: AgentMetrics;
  recentIssues: Issue[];
  recentRuns: HeartbeatRun[];
  agents: Agent[];
  onSelectAgent: (agentId: string) => void;
}) {
  const [viewingFile, setViewingFile] = useState<string | null>(null);
  const outputsResult = usePluginData("output-files");
  const allFiles = ((outputsResult.data as { files?: OutputFile[] } | null)?.files) || [];

  return (
    <div>
      <div style={{ display: "flex", gap: "8px", marginBottom: "24px", flexWrap: "wrap" as const }}>
        {agents.filter((a) => a.role !== "ceo").map((a) => {
          const isActive = a.id === agent.id;
          return (
            <button
              key={a.id}
              onClick={() => onSelectAgent(a.id)}
              style={{
                padding: "6px 14px",
                borderRadius: "20px",
                border: isActive ? "1px solid #7c6ef0" : "1px solid #333",
                background: isActive ? "#7c6ef018" : "transparent",
                color: isActive ? "#e0e0e0" : "#888",
                cursor: "pointer",
                fontSize: "12px",
                fontWeight: isActive ? 600 : 400,
                transition: "all 0.15s",
              }}
            >
              {a.name}
            </button>
          );
        })}
      </div>

      <div style={{
        padding: "20px",
        background: "#1a1a1a",
        borderRadius: "8px",
        border: "1px solid #2a2a2a",
        marginBottom: "24px",
      }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <div>
            <h2 style={{ fontSize: "20px", color: "#e0e0e0", margin: 0 }}>{agent.name}</h2>
            <p style={{ color: "#888", margin: "4px 0 0" }}>{agent.title || agent.role}</p>
          </div>
          <div style={{ textAlign: "right" as const }}>
            <span style={{
              display: "inline-block",
              padding: "4px 12px",
              borderRadius: "12px",
              fontSize: "12px",
              background: agent.status === "idle" ? "#10b98120" : "#3b82f620",
              color: agent.status === "idle" ? "#10b981" : "#3b82f6",
            }}>
              {agent.status}
            </span>
            <p style={{ color: "#666", fontSize: "12px", margin: "4px 0 0" }}>
              Last active: {timeAgo(agent.lastHeartbeatAt)}
            </p>
          </div>
        </div>
      </div>

      <div style={cardContainerStyle}>
        <div style={cardStyle}>
          <div style={{ color: "#888", fontSize: "12px", marginBottom: "6px" }}>완료 이슈</div>
          <div style={{ fontSize: "24px", fontWeight: "bold", color: "#e0e0e0" }}>{metrics.issuesDone}</div>
          <div style={{ color: "#666", fontSize: "11px" }}>/ {metrics.issuesTotal} 전체</div>
        </div>
        <div style={cardStyle}>
          <div style={{ color: "#888", fontSize: "12px", marginBottom: "6px" }}>평균 실행 시간</div>
          <div style={{ fontSize: "24px", fontWeight: "bold", color: "#e0e0e0" }}>
            {metrics.avgRunDurationMs > 0 ? formatDuration(metrics.avgRunDurationMs) : "-"}
          </div>
        </div>
        <div style={cardStyle}>
          <div style={{ color: "#888", fontSize: "12px", marginBottom: "6px" }}>실행 성공률</div>
          <div style={{ fontSize: "24px", fontWeight: "bold", color: "#e0e0e0" }}>
            {metrics.totalRuns > 0 ? formatPercent(metrics.runSuccessRate) : "-"}
          </div>
        </div>
        <div style={cardStyle}>
          <div style={{ color: "#888", fontSize: "12px", marginBottom: "6px" }}>종합 점수</div>
          <div style={{ fontSize: "24px", fontWeight: "bold", color: metrics.apiScore >= 70 ? "#10b981" : metrics.apiScore >= 40 ? "#f59e0b" : "#ef4444" }}>
            {metrics.apiScore}
          </div>
        </div>
      </div>

      {/* 주요 산출물 */}
      {(() => {
        const agentOutputs = getAgentOutputs(agent.name, recentIssues, allFiles);
        if (agentOutputs.length === 0) return null;
        return (
          <>
            <h3 style={{ fontSize: "14px", color: "#e0e0e0", marginBottom: "12px" }}>주요 산출물</h3>
            <div style={{
              display: "grid",
              gridTemplateColumns: "repeat(auto-fill, minmax(220px, 1fr))",
              gap: "8px",
              marginBottom: "32px",
            }}>
              {agentOutputs.map((f) => (
                <button
                  key={f.path}
                  onClick={() => setViewingFile(viewingFile === f.path ? null : f.path)}
                  style={{
                    padding: "12px 14px",
                    background: viewingFile === f.path ? "#7c6ef015" : "#111",
                    border: viewingFile === f.path ? "1px solid #7c6ef060" : "1px solid #2a2a2a",
                    borderRadius: "8px",
                    cursor: "pointer",
                    textAlign: "left" as const,
                    transition: "all 0.15s",
                  }}
                >
                  <div style={{ fontSize: "12px", color: "#e0e0e0", marginBottom: "4px", lineHeight: "1.4" }}>
                    {f.name.replace(/\.md$/, "").slice(11)}
                  </div>
                  <div style={{ fontSize: "10px", color: "#555" }}>
                    {new Date(f.modified).toLocaleDateString("ko-KR")} · {(f.size / 1024).toFixed(0)}KB
                  </div>
                </button>
              ))}
            </div>
          </>
        );
      })()}

      <h3 style={{ fontSize: "14px", color: "#e0e0e0", marginBottom: "12px" }}>최근 이슈</h3>
      <table style={{ width: "100%", borderCollapse: "collapse" as const, marginBottom: "16px" }}>
        <thead>
          <tr>
            <th style={thStyle}>ID</th>
            <th style={thStyle}>제목</th>
            <th style={thStyle}>상태</th>
            <th style={thStyle}>소요 시간</th>
            <th style={thStyle}>산출물</th>
          </tr>
        </thead>
        <tbody>
          {recentIssues.length === 0 ? (
            <tr><td style={{ ...tdStyle, color: "#666" }} colSpan={5}>이슈 없음</td></tr>
          ) : (
            recentIssues.map((issue) => {
              const duration = issue.startedAt && issue.completedAt
                ? new Date(issue.completedAt).getTime() - new Date(issue.startedAt).getTime()
                : null;
              const matched = matchFilesToIssue(issue, allFiles);
              return (
                <tr key={issue.id}>
                  <td style={tdStyle}>{issue.identifier}</td>
                  <td style={tdStyle}>{issue.title.slice(0, 50)}</td>
                  <td style={tdStyle}>
                    <span style={{ color: statusColor(issue.status) }}>{issue.status}</span>
                  </td>
                  <td style={tdStyle}>{duration ? formatDuration(duration) : "-"}</td>
                  <td style={tdStyle}>
                    {matched.length > 0 ? (
                      matched.map((f) => (
                        <button
                          key={f.path}
                          onClick={() => setViewingFile(viewingFile === f.path ? null : f.path)}
                          style={{
                            background: viewingFile === f.path ? "#7c6ef020" : "transparent",
                            border: "1px solid #333",
                            borderRadius: "4px",
                            color: "#7c6ef0",
                            cursor: "pointer",
                            fontSize: "11px",
                            padding: "2px 8px",
                            marginRight: "4px",
                          }}
                        >
                          {f.name.slice(11, 35)}...
                        </button>
                      ))
                    ) : (
                      <span style={{ color: "#555" }}>-</span>
                    )}
                  </td>
                </tr>
              );
            })
          )}
        </tbody>
      </table>

      {viewingFile && (
        <div
          style={{
            position: "fixed",
            top: 0, left: 0, right: 0, bottom: 0,
            background: "rgba(0,0,0,0.7)",
            zIndex: 9999,
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
          onClick={() => setViewingFile(null)}
        >
          <div
            style={{
              width: "80%",
              maxWidth: "900px",
              maxHeight: "85vh",
              background: "#111",
              borderRadius: "12px",
              border: "1px solid #333",
              display: "flex",
              flexDirection: "column" as const,
              overflow: "hidden",
            }}
            onClick={(e) => e.stopPropagation()}
          >
            <div style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              padding: "16px 24px",
              borderBottom: "1px solid #2a2a2a",
              flexShrink: 0,
            }}>
              <span style={{ fontSize: "13px", color: "#aaa" }}>{viewingFile}</span>
              <button
                onClick={() => setViewingFile(null)}
                style={{
                  background: "#222",
                  border: "1px solid #333",
                  borderRadius: "6px",
                  color: "#aaa",
                  cursor: "pointer",
                  fontSize: "13px",
                  padding: "4px 12px",
                }}
              >
                Close
              </button>
            </div>
            <div style={{ overflow: "auto", flex: 1 }}>
              <FileViewer filePath={viewingFile} />
            </div>
          </div>
        </div>
      )}

      <h3 style={{ fontSize: "14px", color: "#e0e0e0", marginBottom: "12px" }}>최근 실행</h3>
      <table style={{ width: "100%", borderCollapse: "collapse" as const }}>
        <thead>
          <tr>
            <th style={thStyle}>상태</th>
            <th style={thStyle}>실행 시간</th>
            <th style={thStyle}>턴 수</th>
            <th style={thStyle}>토큰 (out)</th>
            <th style={thStyle}>시작 시각</th>
          </tr>
        </thead>
        <tbody>
          {recentRuns.length === 0 ? (
            <tr><td style={{ ...tdStyle, color: "#666" }} colSpan={5}>실행 기록 없음</td></tr>
          ) : (
            recentRuns.map((run) => (
              <tr key={run.id}>
                <td style={tdStyle}>
                  <span style={{ color: statusColor(run.status) }}>{run.status}</span>
                </td>
                <td style={tdStyle}>
                  {run.resultJson?.duration_ms ? formatDuration(run.resultJson.duration_ms) : "-"}
                </td>
                <td style={tdStyle}>{run.resultJson?.num_turns ?? "-"}</td>
                <td style={tdStyle}>
                  {run.usageJson?.rawOutputTokens?.toLocaleString() ?? "-"}
                </td>
                <td style={tdStyle}>{timeAgo(run.startedAt)}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}
