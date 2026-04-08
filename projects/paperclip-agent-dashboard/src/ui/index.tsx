import React, { useState, useEffect, useCallback } from "react";
import { usePluginData } from "@paperclipai/plugin-sdk/ui";
import { TabNav } from "./components/TabNav.js";
import { TeamOverview } from "./components/TeamOverview.js";
import { AgentDetail } from "./components/AgentDetail.js";
import { Comparison } from "./components/Comparison.js";
import { OutputsBrowser } from "./components/OutputsBrowser.js";
import { buildTeamOverview, buildAgentDetail } from "./utils/metrics.js";
import type { Agent } from "./types.js";

const TABS = [
  { id: "overview", label: "Team Overview" },
  { id: "detail", label: "Agent Detail" },
  { id: "comparison", label: "Comparison" },
  { id: "outputs", label: "Outputs" },
];

function parseHash(): { tab: string; agentId: string | null } {
  const hash = window.location.hash.slice(1);
  const params = new URLSearchParams(hash);
  return {
    tab: params.get("tab") || "overview",
    agentId: params.get("agent"),
  };
}

function pushHash(tab: string, agentId?: string | null) {
  const params = new URLSearchParams();
  params.set("tab", tab);
  if (agentId) params.set("agent", agentId);
  window.history.pushState(null, "", `#${params.toString()}`);
}

export function AgentPerfPage({ context }: { context: { companyId?: string } }) {
  const initial = parseHash();
  const [activeTab, setActiveTab] = useState(initial.tab);
  const [selectedAgentId, setSelectedAgentId] = useState<string | null>(initial.agentId);

  const handlePopState = useCallback(() => {
    const { tab, agentId } = parseHash();
    setActiveTab(tab);
    setSelectedAgentId(agentId);
  }, []);

  useEffect(() => {
    window.addEventListener("popstate", handlePopState);
    return () => window.removeEventListener("popstate", handlePopState);
  }, [handlePopState]);

  const overviewResult = usePluginData("team-overview");

  function handleSelectAgent(agentId: string) {
    setSelectedAgentId(agentId);
    setActiveTab("detail");
    pushHash("detail", agentId);
  }

  function handleTabChange(tab: string) {
    setActiveTab(tab);
    pushHash(tab, tab === "detail" ? selectedAgentId : null);
  }

  const loading = overviewResult.loading;
  const error = overviewResult.error;

  if (loading) {
    return (
      <div style={{ padding: "32px", color: "#888" }}>
        Loading dashboard data...
      </div>
    );
  }

  if (error) {
    return (
      <div style={{ padding: "32px", color: "#ef4444" }}>
        Error: {error.message}
      </div>
    );
  }

  const rawData = overviewResult.data as {
    agents: Agent[];
    issues: any[];
    runs: any[];
  } | null;

  if (!rawData) {
    return (
      <div style={{ padding: "32px", color: "#888" }}>
        No data available
      </div>
    );
  }

  const teamData = buildTeamOverview(rawData.agents, rawData.issues, rawData.runs);

  return (
    <div style={{ padding: "32px", color: "#e0e0e0", maxWidth: "1200px" }}>
      <h1 style={{ fontSize: "22px", marginBottom: "24px", fontWeight: "600" }}>
        Agent Performance Dashboard
      </h1>

      <TabNav tabs={TABS} activeTab={activeTab} onTabChange={handleTabChange} />

      {activeTab === "overview" && (
        <TeamOverview data={teamData} issues={rawData.issues} onSelectAgent={handleSelectAgent} />
      )}

      {activeTab === "detail" && (() => {
        const agents = rawData.agents.filter((a: Agent) => a.role !== "ceo");
        const agentId = selectedAgentId || agents[0]?.id;
        const agent = agents.find((a: Agent) => a.id === agentId);

        if (!agent) {
          return <div style={{ color: "#888" }}>에이전트를 선택하세요</div>;
        }

        const detail = buildAgentDetail(agent, rawData.issues, rawData.runs, rawData.agents);

        return (
          <AgentDetail
            agent={agent}
            metrics={detail.metrics}
            recentIssues={detail.recentIssues}
            recentRuns={detail.recentRuns}
            agents={agents}
            onSelectAgent={(id) => { setSelectedAgentId(id); pushHash("detail", id); }}
          />
        );
      })()}

      {activeTab === "comparison" && (
        <Comparison allMetrics={teamData.rankings} runs={rawData.runs} />
      )}

      {activeTab === "outputs" && (
        <OutputsBrowser />
      )}
    </div>
  );
}

const PLUGIN_ID = "b77ca91b-6eef-422b-a043-480c11037fe7";

export function AgentPerfSidebar({ context }: { context: { companyId?: string; companyPrefix?: string | null } }) {
  const prefix = context?.companyPrefix ?? "TI";
  return (
    <a
      href={`/${prefix}/plugins/${PLUGIN_ID}`}
      style={{ textDecoration: "none", color: "inherit", display: "block", width: "100%" }}
    >
      Agent Performance
    </a>
  );
}
