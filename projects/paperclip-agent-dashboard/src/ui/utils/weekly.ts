import type { HeartbeatRun } from "../types.js";

const MIN_OUTPUT_TOKENS = 500;
const KST_OFFSET_MS = 9 * 60 * 60 * 1000;

function getISOWeek(date: Date): string {
  const d = new Date(date.getTime() + KST_OFFSET_MS); // KST 기준
  d.setHours(0, 0, 0, 0);
  d.setDate(d.getDate() + 3 - ((d.getDay() + 6) % 7));
  const yearStart = new Date(d.getFullYear(), 0, 1);
  const weekNum = Math.ceil(((d.getTime() - yearStart.getTime()) / 86400000 + 1) / 7);
  return `W${String(weekNum).padStart(2, "0")}`;
}

export function getRecentWeeks(n: number): string[] {
  const weeks: string[] = [];
  const now = new Date();
  for (let i = n - 1; i >= 0; i--) {
    const d = new Date(now.getTime() - i * 7 * 24 * 60 * 60 * 1000);
    const w = getISOWeek(d);
    if (!weeks.includes(w)) weeks.push(w);
  }
  return weeks;
}

export function groupRunsByWeek(
  runs: HeartbeatRun[],
  agentId: string
): Record<string, number> {
  const result: Record<string, number> = {};
  for (const run of runs) {
    if (run.agentId !== agentId) continue;
    const tokens = run.usageJson?.rawOutputTokens ?? run.usageJson?.outputTokens ?? 0;
    if (tokens < MIN_OUTPUT_TOKENS) continue;
    const week = getISOWeek(new Date(run.startedAt));
    result[week] = (result[week] || 0) + 1;
  }
  return result;
}

export function getWeeklyValues(
  runs: HeartbeatRun[],
  agentId: string,
  weeks: string[]
): number[] {
  const grouped = groupRunsByWeek(runs, agentId);
  return weeks.map((w) => grouped[w] || 0);
}
