export function formatDuration(ms: number): string {
  if (ms < 0 || !isFinite(ms)) return "-";
  const totalSec = Math.round(ms / 1000);
  if (totalSec < 60) return `${totalSec}s`;
  const min = Math.floor(totalSec / 60);
  const sec = totalSec % 60;
  if (min < 60) return sec > 0 ? `${min}m ${sec}s` : `${min}m`;
  const hr = Math.floor(min / 60);
  const remMin = min % 60;
  return `${hr}h ${remMin}m`;
}

export function formatPercent(value: number): string {
  if (!isFinite(value)) return "-";
  return `${Math.round(value * 10) / 10}%`;
}

export function formatNumber(value: number): string {
  if (!isFinite(value)) return "-";
  return value.toLocaleString();
}

export function toKST(isoDate: string): Date {
  return new Date(new Date(isoDate).getTime() + 9 * 60 * 60 * 1000);
}

export function toKSTDateString(isoDate: string): string {
  return toKST(isoDate).toISOString().slice(0, 10);
}

export function timeAgo(isoDate: string | null): string {
  if (!isoDate) return "-";
  const diff = Date.now() - new Date(isoDate).getTime();
  const min = Math.floor(diff / 60000);
  if (min < 1) return "방금";
  if (min < 60) return `${min}분 전`;
  const hr = Math.floor(min / 60);
  if (hr < 24) return `${hr}시간 전`;
  const day = Math.floor(hr / 24);
  return `${day}일 전`;
}
