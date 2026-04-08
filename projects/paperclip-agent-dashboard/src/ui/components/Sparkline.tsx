import React from "react";

export function Sparkline({
  values,
  width = 100,
  height = 24,
  strokeWidth = 1.5,
}: {
  values: number[];
  width?: number;
  height?: number;
  strokeWidth?: number;
}) {
  if (values.length < 2) return null;

  const min = Math.min(...values);
  const max = Math.max(...values);
  const range = max - min || 1;
  const pad = 3;

  const points = values.map((v, i) => {
    const x = pad + (i / (values.length - 1)) * (width - pad * 2);
    const y = pad + (height - pad * 2) - ((v - min) / range) * (height - pad * 2);
    return { x, y };
  });

  const polyline = points.map((p) => `${p.x.toFixed(1)},${p.y.toFixed(1)}`).join(" ");
  const last = points[points.length - 1];
  const trend = values[values.length - 1] - values[0];
  const color = trend > 0 ? "#10b981" : trend < 0 ? "#ef4444" : "#666";

  return (
    <svg width={width} height={height} viewBox={`0 0 ${width} ${height}`}>
      <polyline
        points={`${points[0].x},${height} ${polyline} ${last.x},${height}`}
        fill={color}
        fillOpacity="0.1"
        stroke="none"
      />
      <polyline
        points={polyline}
        fill="none"
        stroke={color}
        strokeWidth={strokeWidth}
        strokeLinecap="round"
        strokeLinejoin="round"
      />
      <circle cx={last.x} cy={last.y} r="2.5" fill={color} />
    </svg>
  );
}
