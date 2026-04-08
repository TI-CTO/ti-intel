import type { Issue } from "../types.js";

interface TaskType {
  name: string;
  baselineHours: number;
  patterns: RegExp[];
}

const TASK_TYPES: TaskType[] = [
  {
    name: "startup-analyst",
    baselineHours: 4,
    patterns: [/조사/i, /분석/i, /startup/i, /스타트업/i, /회사.*대해/i],
  },
  {
    name: "weekly-monitor",
    baselineHours: 8,
    patterns: [/weekly/i, /모니터링/i, /주간/i, /동향/i],
  },
  {
    name: "wtis",
    baselineHours: 6,
    patterns: [/wtis/i, /기술.*검증/i, /go.*no.*go/i],
  },
  {
    name: "research",
    baselineHours: 4,
    patterns: [/리서치/i, /research/i, /탐색/i, /discover/i],
  },
];

const DEFAULT_BASELINE_HOURS = 2;

function classifyIssue(title: string): { type: string; baselineHours: number } {
  for (const t of TASK_TYPES) {
    if (t.patterns.some((p) => p.test(title))) {
      return { type: t.name, baselineHours: t.baselineHours };
    }
  }
  return { type: "other", baselineHours: DEFAULT_BASELINE_HOURS };
}

export interface RoiSummary {
  totalSavedHours: number;
  totalSavedWorkingDays: number;
  thisWeekSavedHours: number;
  avgSavedPerIssueHours: number;
  issueCount: number;
}

export function calcRoi(issues: Issue[]): RoiSummary {
  const doneIssues = issues.filter(
    (i) => i.status === "done" && i.startedAt && i.completedAt
  );

  const now = Date.now();
  const weekAgo = now - 7 * 24 * 60 * 60 * 1000;

  let totalSaved = 0;
  let weekSaved = 0;
  let count = 0;

  for (const issue of doneIssues) {
    const agentMs =
      new Date(issue.completedAt!).getTime() -
      new Date(issue.startedAt!).getTime();
    if (agentMs <= 0) continue;

    const agentHours = agentMs / (1000 * 60 * 60);
    const { baselineHours } = classifyIssue(issue.title);
    const saved = baselineHours - agentHours;

    totalSaved += saved;
    count++;

    const completedAt = new Date(issue.completedAt!).getTime();
    if (completedAt >= weekAgo) {
      weekSaved += saved;
    }
  }

  return {
    totalSavedHours: Math.round(totalSaved * 10) / 10,
    totalSavedWorkingDays: Math.round((totalSaved / 8) * 10) / 10,
    thisWeekSavedHours: Math.round(weekSaved * 10) / 10,
    avgSavedPerIssueHours:
      count > 0 ? Math.round((totalSaved / count) * 10) / 10 : 0,
    issueCount: count,
  };
}
