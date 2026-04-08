import { definePlugin, runWorker } from "@paperclipai/plugin-sdk";
import { readdirSync, readFileSync, statSync } from "node:fs";
import { join, resolve, extname } from "node:path";
import { marked } from "marked";

const API_BASE = "http://127.0.0.1:3100/api";
const COMPANY_ID = "a8aeda24-7cd4-47d2-b235-ac4dbf09b22a";
const REPORTS_ROOT = "/Users/ctoti/Project/ClaudeCode/outputs/reports";

async function fetchJSON(path: string) {
  const res = await fetch(`${API_BASE}${path}`);
  if (!res.ok) throw new Error(`API ${res.status}: ${path}`);
  return res.json();
}

function scanFiles(dir: string, base: string = ""): any[] {
  const results: any[] = [];
  try {
    const entries = readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
      const relPath = base ? `${base}/${entry.name}` : entry.name;
      const fullPath = join(dir, entry.name);
      if (entry.isDirectory()) {
        results.push(...scanFiles(fullPath, relPath));
      } else if (/\.(md|pdf)$/.test(entry.name)) {
        const stat = statSync(fullPath);
        const ext = extname(entry.name).slice(1);
        results.push({
          name: entry.name,
          path: relPath,
          size: stat.size,
          modified: stat.mtime.toISOString(),
          type: ext === "md" ? "md" : ext === "pdf" ? "pdf" : "other",
        });
      }
    }
  } catch {
    // directory doesn't exist or not readable
  }
  return results;
}

const plugin = definePlugin({
  async setup(ctx) {
    ctx.logger.info("Agent Dashboard plugin started");

    ctx.data.register("team-overview", async () => {
      const [agents, issues, runs] = await Promise.all([
        fetchJSON(`/companies/${COMPANY_ID}/agents`),
        fetchJSON(`/companies/${COMPANY_ID}/issues`),
        fetchJSON(`/companies/${COMPANY_ID}/heartbeat-runs`),
      ]);
      return { agents, issues, runs };
    });

    ctx.data.register("agent-detail", async (params) => {
      const agentId = (params as { agentId?: string })?.agentId;
      if (!agentId) return { error: "agentId required" };

      const [agents, issues, runs] = await Promise.all([
        fetchJSON(`/companies/${COMPANY_ID}/agents`),
        fetchJSON(`/companies/${COMPANY_ID}/issues`),
        fetchJSON(`/companies/${COMPANY_ID}/heartbeat-runs`),
      ]);

      const agent = (agents as any[]).find((a: any) => a.id === agentId);
      if (!agent) return { error: "agent not found" };

      return { agent, agents, issues, runs };
    });

    ctx.data.register("output-files", async () => {
      return { files: scanFiles(REPORTS_ROOT) };
    });

    ctx.data.register("file-content", async (params) => {
      const filePath = (params as { filePath?: string })?.filePath;
      if (!filePath) return { error: "filePath required" };

      // Security: only allow files under REPORTS_ROOT
      const resolved = resolve(REPORTS_ROOT, filePath);
      if (!resolved.startsWith(REPORTS_ROOT)) {
        return { error: "access denied" };
      }

      const ext = extname(resolved).slice(1);
      if (ext === "pdf") {
        return { type: "pdf", message: "PDF preview not supported" };
      }

      try {
        const content = readFileSync(resolved, "utf-8");
        const html = marked(content) as string;
        return { type: "md", content, html, filename: filePath };
      } catch {
        return { error: "file not found" };
      }
    });
  },
});

export default plugin;
runWorker(plugin, import.meta.url);
