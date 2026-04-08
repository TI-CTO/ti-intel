import React from "react";

const tabStyle: React.CSSProperties = {
  padding: "8px 16px",
  cursor: "pointer",
  border: "none",
  background: "transparent",
  color: "#888",
  fontSize: "14px",
  borderBottom: "2px solid transparent",
};

const activeStyle: React.CSSProperties = {
  ...tabStyle,
  color: "#e0e0e0",
  borderBottom: "2px solid #7c6ef0",
};

export function TabNav({
  tabs,
  activeTab,
  onTabChange,
}: {
  tabs: { id: string; label: string }[];
  activeTab: string;
  onTabChange: (id: string) => void;
}) {
  return (
    <div style={{ display: "flex", gap: "4px", borderBottom: "1px solid #2a2a2a", marginBottom: "24px" }}>
      {tabs.map((tab) => (
        <button
          key={tab.id}
          style={tab.id === activeTab ? activeStyle : tabStyle}
          onClick={() => onTabChange(tab.id)}
        >
          {tab.label}
        </button>
      ))}
    </div>
  );
}
