export interface Agent {
  id: string;
  name: string;
  title: string;
  role: string;
  status: string;
  lastHeartbeatAt: string | null;
  reportsTo: string | null;
}

export interface Issue {
  id: string;
  identifier: string;
  title: string;
  status: string;
  priority: string;
  assigneeAgentId: string | null;
  startedAt: string | null;
  completedAt: string | null;
  createdAt: string;
  parentId: string | null;
}

export interface HeartbeatRun {
  id: string;
  agentId: string;
  status: string;
  startedAt: string;
  finishedAt: string | null;
  invocationSource: string;
  exitCode: number | null;
  usageJson: {
    costUsd?: number;
    rawInputTokens?: number;
    rawOutputTokens?: number;
    outputTokens?: number;
    inputTokens?: number;
    cachedInputTokens?: number;
  } | null;
  resultJson: {
    duration_ms?: number;
    num_turns?: number;
    is_error?: boolean;
    stop_reason?: string;
    total_cost_usd?: number;
    usage?: {
      input_tokens?: number;
      output_tokens?: number;
      cache_read_input_tokens?: number;
      server_tool_use?: {
        web_search_requests?: number;
        web_fetch_requests?: number;
      };
    };
  } | null;
}

export interface AgentMetrics {
  agentId: string;
  name: string;
  title: string;
  role: string;
  status: string;
  issuesDone: number;
  issuesTotal: number;
  completionRate: number;
  avgCompletionTimeMs: number;
  totalRuns: number;
  successfulRuns: number;
  runSuccessRate: number;
  avgRunDurationMs: number;
  avgTurns: number;
  errorRate: number;
  apiScore: number;
}

export interface TeamOverviewData {
  summary: {
    totalCompleted: number;
    avgCompletionTimeMs: number;
    teamSuccessRate: number;
    activeAgents: number;
    totalAgents: number;
  };
  rankings: AgentMetrics[];
}

export interface OutputFile {
  name: string;
  path: string;
  size: number;
  modified: string;
  type: "md" | "pdf" | "other";
}

export interface AgentDetailData {
  agent: Agent;
  metrics: AgentMetrics;
  recentIssues: Issue[];
  recentRuns: HeartbeatRun[];
}
