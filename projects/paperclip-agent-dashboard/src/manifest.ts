export default {
  id: "agent-dashboard",
  pluginKey: "agent-dashboard",
  apiVersion: 1 as const,
  displayName: "Agent Performance Dashboard",
  description: "에이전트별 산출물 관리 및 성과 비교 대시보드",
  version: "0.1.0",
  author: "ctoti",
  categories: ["ui" as const],
  entrypoints: {
    worker: "dist/worker.js",
    ui: "dist/ui",
  },
  capabilities: [
    "ui.page.register",
    "ui.sidebar.register",
    "http.outbound",
    "plugin.state.read",
    "plugin.state.write",
  ],
  ui: {
    slots: [
      {
        type: "page" as const,
        id: "agent-perf",
        displayName: "Agent Performance",
        exportName: "AgentPerfPage",
      },
      {
        type: "sidebar" as const,
        id: "agent-perf-nav",
        displayName: "Agent Performance",
        exportName: "AgentPerfSidebar",
      },
    ],
  },
};
