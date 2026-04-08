import type { Agent, Issue, HeartbeatRun, AgentMetrics, TeamOverviewData } from "../types.js";

const MIN_OUTPUT_TOKENS = 500;

function isMeaningfulRun(run: HeartbeatRun): boolean {
  const usage = run.usageJson;
  const tokens = usage?.rawOutputTokens ?? usage?.outputTokens ?? 0;
  return tokens >= MIN_OUTPUT_TOKENS;
}

function calcAgentMetrics(
  agent: Agent,
  issues: Issue[],
  runs: HeartbeatRun[]
): AgentMetrics {
  const agentIssues = issues.filter((i) => i.assigneeAgentId === agent.id);
  const doneIssues = agentIssues.filter((i) => i.status === "done");

  // Filter: only meaningful runs (not heartbeat-only inbox checks)
  const allAgentRuns = runs.filter((r) => r.agentId === agent.id);
  const agentRuns = allAgentRuns.filter(isMeaningfulRun);
  const successRuns = agentRuns.filter((r) => r.status === "succeeded");

  const completionTimes = doneIssues
    .filter((i) => i.startedAt && i.completedAt)
    .map((i) => new Date(i.completedAt!).getTime() - new Date(i.startedAt!).getTime())
    .filter((t) => t > 0);

  const runDurations = agentRuns
    .map((r) => r.resultJson?.duration_ms)
    .filter((d): d is number => typeof d === "number" && d > 0);

  const turns = agentRuns
    .map((r) => r.resultJson?.num_turns)
    .filter((t): t is number => typeof t === "number");

  const errorCount = agentRuns.filter((r) => r.resultJson?.is_error).length;

  const issuesDone = doneIssues.length;
  const issuesTotal = agentIssues.length;
  const completionRate = issuesTotal > 0 ? (issuesDone / issuesTotal) * 100 : 0;
  const avgCompletionTimeMs = completionTimes.length > 0
    ? completionTimes.reduce((a, b) => a + b, 0) / completionTimes.length
    : 0;
  const totalRuns = agentRuns.length;
  const successfulRuns = successRuns.length;
  const runSuccessRate = totalRuns > 0 ? (successfulRuns / totalRuns) * 100 : 0;
  const avgRunDurationMs = runDurations.length > 0
    ? runDurations.reduce((a, b) => a + b, 0) / runDurations.length
    : 0;
  const avgTurns = turns.length > 0
    ? turns.reduce((a, b) => a + b, 0) / turns.length
    : 0;
  const errorRate = totalRuns > 0 ? (errorCount / totalRuns) * 100 : 0;

  return {
    agentId: agent.id,
    name: agent.name,
    title: agent.title,
    role: agent.role,
    status: agent.status,
    issuesDone,
    issuesTotal,
    completionRate,
    avgCompletionTimeMs,
    totalRuns,
    successfulRuns,
    runSuccessRate,
    avgRunDurationMs,
    avgTurns,
    errorRate,
    apiScore: 0,
  };
}

function rankScore(value: number, allValues: number[]): number {
  if (value === 0) return 0;
  const sorted = [...new Set(allValues.filter((v) => v > 0))].sort((a, b) => a - b);
  if (sorted.length <= 1) return 100;
  const idx = sorted.indexOf(value);
  // Scale 50-100 so even lowest active agent gets 50
  return Math.round(50 + (idx / (sorted.length - 1)) * 50);
}

function calcApiScore(m: AgentMetrics, allMetrics: AgentMetrics[]): number {
  if (m.totalRuns === 0 && m.issuesDone === 0) return 0;


  const active = allMetrics.filter((a) => a.totalRuns > 0 || a.issuesDone > 0);
  if (active.length === 0) return 0;

  // 양 60%: 완료 이슈 수 순위 30% + 총 실행 횟수 순위 30%
  const issueRank = rankScore(m.issuesDone, active.map((a) => a.issuesDone));
  const runRank = rankScore(m.totalRuns, active.map((a) => a.totalRuns));
  const quantityScore = issueRank * 0.3 + runRank * 0.3;

  // 질 40%: 실행 성공률 20% + 에러율(역) 20%
  const successScore = m.runSuccessRate * 0.2;
  const errorScore = (100 - m.errorRate) * 0.2;
  const qualityScore = successScore + errorScore;

  return Math.round(quantityScore + qualityScore);
}

export function buildTeamOverview(
  agents: Agent[],
  issues: Issue[],
  runs: HeartbeatRun[]
): TeamOverviewData {
  const allMetrics = agents
    .filter((a) => a.role !== "ceo")
    .map((a) => calcAgentMetrics(a, issues, runs));

  allMetrics.forEach((m) => {
    m.apiScore = calcApiScore(m, allMetrics);
  });

  const rankings = [...allMetrics].sort((a, b) => b.apiScore - a.apiScore);

  const doneIssues = issues.filter((i) => i.status === "done");
  const completionTimes = doneIssues
    .filter((i) => i.startedAt && i.completedAt)
    .map((i) => new Date(i.completedAt!).getTime() - new Date(i.startedAt!).getTime())
    .filter((t) => t > 0);

  const meaningfulRuns = runs.filter(isMeaningfulRun);
  const successRuns = meaningfulRuns.filter((r) => r.status === "succeeded");
  const activeAgents = agents.filter((a) => !["paused", "archived"].includes(a.status));

  return {
    summary: {
      totalCompleted: doneIssues.length,
      avgCompletionTimeMs: completionTimes.length > 0
        ? completionTimes.reduce((a, b) => a + b, 0) / completionTimes.length
        : 0,
      teamSuccessRate: meaningfulRuns.length > 0
        ? (successRuns.length / meaningfulRuns.length) * 100
        : 0,
      activeAgents: activeAgents.length,
      totalAgents: agents.length,
    },
    rankings,
  };
}

export function buildAgentDetail(
  agent: Agent,
  issues: Issue[],
  runs: HeartbeatRun[],
  allAgents: Agent[]
): {
  metrics: AgentMetrics;
  recentIssues: Issue[];
  recentRuns: HeartbeatRun[];
} {
  const allMetrics = allAgents.map((a) => calcAgentMetrics(a, issues, runs));
  const metrics = calcAgentMetrics(agent, issues, runs);
  metrics.apiScore = calcApiScore(metrics, allMetrics);

  const recentIssues = issues
    .filter((i) => i.assigneeAgentId === agent.id)
    .sort((a, b) => new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime())
    .slice(0, 10);

  // Detail shows all runs (including heartbeat-only) for transparency
  const recentRuns = runs
    .filter((r) => r.agentId === agent.id)
    .sort((a, b) => new Date(b.startedAt).getTime() - new Date(a.startedAt).getTime())
    .slice(0, 10);

  return { metrics, recentIssues, recentRuns };
}
