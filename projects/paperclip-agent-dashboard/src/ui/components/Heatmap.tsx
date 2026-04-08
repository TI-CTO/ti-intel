import React from "react";

export function Heatmap({
  agents,
  weeks,
  data,
}: {
  agents: { id: string; name: string }[];
  weeks: string[];
  data: Record<string, Record<string, number>>;
}) {
  const allValues = agents.flatMap((a) =>
    weeks.map((w) => data[a.id]?.[w] ?? 0)
  );
  const maxValue = Math.max(...allValues, 1);

  return (
    <div style={{ overflowX: "auto" }}>
      <div
        style={{
          display: "grid",
          gridTemplateColumns: `100px repeat(${weeks.length}, 1fr)`,
          gap: "3px",
          minWidth: weeks.length * 48 + 100,
        }}
      >
        {/* Header */}
        <div />
        {weeks.map((w) => (
          <div
            key={w}
            style={{
              fontSize: "10px",
              color: "#666",
              textAlign: "center" as const,
              paddingBottom: "4px",
            }}
          >
            {w}
          </div>
        ))}

        {/* Rows */}
        {agents.map((agent) => (
          <React.Fragment key={agent.id}>
            <div
              style={{
                fontSize: "12px",
                color: "#aaa",
                display: "flex",
                alignItems: "center",
                paddingRight: "8px",
                whiteSpace: "nowrap" as const,
              }}
            >
              {agent.name}
            </div>
            {weeks.map((w) => {
              const val = data[agent.id]?.[w] ?? 0;
              const ratio = val / maxValue;
              return (
                <div
                  key={w}
                  title={`${agent.name} ${w}: ${val}건`}
                  style={{
                    height: "28px",
                    borderRadius: "4px",
                    background: val > 0
                      ? `rgba(124, 110, 240, ${0.15 + ratio * 0.75})`
                      : "#1a1a1a",
                    cursor: "default",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    fontSize: "10px",
                    color: ratio > 0.5 ? "#e0e0e0" : "#555",
                  }}
                >
                  {val > 0 ? val : ""}
                </div>
              );
            })}
          </React.Fragment>
        ))}
      </div>
    </div>
  );
}
