import type { Issue } from "../types.js";

export interface TaskType {
  name: string;
  label: string;
  baselineHours: number;
  patterns: RegExp[];
}

const DEFAULT_TASK_TYPES: TaskType[] = [
  {
    name: "startup-analyst",
    label: "스타트업 분석",
    baselineHours: 4,
    patterns: [/조사/i, /분석/i, /startup/i, /스타트업/i, /회사.*대해/i],
  },
  {
    name: "weekly-monitor",
    label: "주간 모니터링",
    baselineHours: 8,
    patterns: [/weekly/i, /모니터링/i, /주간/i, /동향/i],
  },
  {
    name: "wtis",
    label: "기술 검증 (WTIS)",
    baselineHours: 6,
    patterns: [/wtis/i, /기술.*검증/i, /go.*no.*go/i],
  },
  {
    name: "research",
    label: "리서치",
    baselineHours: 4,
    patterns: [/리서치/i, /research/i, /탐색/i, /discover/i],
  },
];

const DEFAULT_BASELINE_HOURS = 2;
const STORAGE_KEY = "agent-dashboard-roi-baselines";

export function getBaselines(): Record<string, number> {
  try {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) return JSON.parse(stored);
  } catch {}
  return {};
}

export function saveBaselines(baselines: Record<string, number>): void {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(baselines));
  } catch {}
}

export function getTaskTypes(): TaskType[] {
  const overrides = getBaselines();
  return DEFAULT_TASK_TYPES.map((t) => ({
    ...t,
    baselineHours: overrides[t.name] ?? t.baselineHours,
  }));
}

export function getDefaultBaselineHours(): number {
  const overrides = getBaselines();
  return overrides["other"] ?? DEFAULT_BASELINE_HOURS;
}

function classifyIssue(title: string, taskTypes: TaskType[]): { type: string; baselineHours: number } {
  for (const t of taskTypes) {
    if (t.patterns.some((p) => p.test(title))) {
      return { type: t.name, baselineHours: t.baselineHours };
    }
  }
  return { type: "other", baselineHours: getDefaultBaselineHours() };
}

export interface RoiDetail {
  issueId: string;
  title: string;
  type: string;
  baselineHours: number;
  agentHours: number;
  savedHours: number;
}

export interface RoiSummary {
  totalSavedHours: number;
  totalSavedWorkingDays: number;
  thisWeekSavedHours: number;
  avgSavedPerIssueHours: number;
  issueCount: number;
  details: RoiDetail[];
}

export function calcRoi(issues: Issue[]): RoiSummary {
  const doneIssues = issues.filter(
    (i) => i.status === "done" && i.startedAt && i.completedAt
  );

  const taskTypes = getTaskTypes();
  const now = Date.now();
  const weekAgo = now - 7 * 24 * 60 * 60 * 1000;

  let totalSaved = 0;
  let weekSaved = 0;
  const details: RoiDetail[] = [];

  for (const issue of doneIssues) {
    const agentMs =
      new Date(issue.completedAt!).getTime() -
      new Date(issue.startedAt!).getTime();
    if (agentMs <= 0) continue;

    const agentHours = agentMs / (1000 * 60 * 60);
    const { type, baselineHours } = classifyIssue(issue.title, taskTypes);
    const saved = baselineHours - agentHours;

    totalSaved += saved;
    details.push({
      issueId: issue.identifier,
      title: issue.title,
      type,
      baselineHours,
      agentHours: Math.round(agentHours * 10) / 10,
      savedHours: Math.round(saved * 10) / 10,
    });

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
      details.length > 0 ? Math.round((totalSaved / details.length) * 10) / 10 : 0,
    issueCount: details.length,
    details,
  };
}
