import React, { useState } from "react";
import { usePluginData } from "@paperclipai/plugin-sdk/ui";
import type { OutputFile } from "../types.js";

const markdownStyles = `
  .output-md-viewer { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
  .output-md-viewer h1 { font-size: 1.6em; border-bottom: 1px solid #333; padding-bottom: 8px; margin: 24px 0 16px; color: #f0f0f0; }
  .output-md-viewer h2 { font-size: 1.3em; border-bottom: 1px solid #2a2a2a; padding-bottom: 6px; margin: 20px 0 12px; color: #e8e8e8; }
  .output-md-viewer h3 { font-size: 1.1em; margin: 16px 0 8px; color: #e0e0e0; }
  .output-md-viewer p { margin: 8px 0; line-height: 1.7; }
  .output-md-viewer ul, .output-md-viewer ol { padding-left: 24px; margin: 8px 0; }
  .output-md-viewer li { margin: 4px 0; line-height: 1.6; }
  .output-md-viewer table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 0.9em; }
  .output-md-viewer th { background: #1a1a1a; padding: 8px 12px; border: 1px solid #333; text-align: left; color: #aaa; font-weight: 600; }
  .output-md-viewer td { padding: 6px 12px; border: 1px solid #2a2a2a; }
  .output-md-viewer code { background: #1a1a1a; padding: 2px 6px; border-radius: 3px; font-size: 0.9em; color: #e8b4b8; }
  .output-md-viewer pre { background: #111; padding: 16px; border-radius: 6px; overflow-x: auto; border: 1px solid #2a2a2a; }
  .output-md-viewer pre code { background: none; padding: 0; color: #d0d0d0; }
  .output-md-viewer blockquote { border-left: 3px solid #7c6ef0; padding: 8px 16px; margin: 12px 0; color: #aaa; }
  .output-md-viewer a { color: #7c6ef0; text-decoration: none; }
  .output-md-viewer strong { color: #f0f0f0; }
  .output-md-viewer hr { border: none; border-top: 1px solid #2a2a2a; margin: 20px 0; }
`;

const thStyle: React.CSSProperties = {
  textAlign: "left" as const,
  padding: "10px 12px",
  borderBottom: "1px solid #2a2a2a",
  color: "#888",
  fontSize: "12px",
  textTransform: "uppercase" as const,
  cursor: "pointer",
};

const tdStyle: React.CSSProperties = {
  padding: "10px 12px",
  borderBottom: "1px solid #1a1a1a",
  color: "#e0e0e0",
  fontSize: "13px",
};

const selectStyle: React.CSSProperties = {
  background: "#1a1a1a",
  color: "#e0e0e0",
  border: "1px solid #333",
  borderRadius: "6px",
  padding: "6px 10px",
  fontSize: "13px",
};

function formatSize(bytes: number): string {
  if (bytes < 1024) return `${bytes}B`;
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)}KB`;
  return `${(bytes / (1024 * 1024)).toFixed(1)}MB`;
}

function getFolder(path: string): string {
  const parts = path.split("/");
  return parts.length > 1 ? parts.slice(0, -1).join("/") : "/";
}

function FileViewer({ filePath }: { filePath: string }) {
  const result = usePluginData("file-content", { filePath });

  if (result.loading) return <div style={{ padding: "16px", color: "#888" }}>Loading...</div>;

  const data = result.data as { type?: string; html?: string; error?: string } | null;
  if (!data || data.error) return <div style={{ padding: "16px", color: "#ef4444" }}>{data?.error || "Failed"}</div>;
  if (data.type === "pdf") return <div style={{ padding: "16px", color: "#888" }}>PDF 미리보기 미지원</div>;

  return (
    <>
      <style dangerouslySetInnerHTML={{ __html: markdownStyles }} />
      <div
        className="output-md-viewer"
        style={{
          padding: "24px 32px",
          background: "#0d0d0d",
          fontSize: "14px",
          lineHeight: "1.7",
          color: "#d0d0d0",
        }}
        dangerouslySetInnerHTML={{ __html: data.html || "" }}
        onClick={(e) => {
          const anchor = (e.target as HTMLElement).closest("a");
          if (!anchor) return;
          const href = anchor.getAttribute("href") || "";
          if (href.startsWith("#")) {
            e.preventDefault();
            (e.currentTarget as HTMLElement).querySelector(href)?.scrollIntoView({ behavior: "smooth" });
          }
        }}
      />
    </>
  );
}

export function OutputsBrowser() {
  const result = usePluginData("output-files");
  const [folderFilter, setFolderFilter] = useState<string>("all");
  const [sortKey, setSortKey] = useState<"name" | "modified" | "size">("modified");
  const [sortDesc, setSortDesc] = useState(true);
  const [viewingFile, setViewingFile] = useState<string | null>(null);

  if (result.loading) return <div style={{ padding: "16px", color: "#888" }}>Loading files...</div>;

  const allFiles = ((result.data as { files?: OutputFile[] } | null)?.files) || [];
  const mdFiles = allFiles.filter((f) => f.type === "md");

  const folderSet = new Set(mdFiles.map((f) => getFolder(f.path)));
  const folders = ["all", ...Array.from(folderSet).sort()];

  let filtered = folderFilter === "all" ? mdFiles : mdFiles.filter((f) => getFolder(f.path) === folderFilter);
  filtered = [...filtered].sort((a, b) => {
    let cmp = 0;
    if (sortKey === "name") cmp = a.name.localeCompare(b.name);
    else if (sortKey === "modified") cmp = new Date(a.modified).getTime() - new Date(b.modified).getTime();
    else cmp = a.size - b.size;
    return sortDesc ? -cmp : cmp;
  });

  function handleSort(key: "name" | "modified" | "size") {
    if (sortKey === key) setSortDesc(!sortDesc);
    else { setSortKey(key); setSortDesc(true); }
  }

  const sortIndicator = (key: string) => sortKey === key ? (sortDesc ? " v" : " ^") : "";

  return (
    <div>
      <div style={{ display: "flex", gap: "8px", alignItems: "center", marginBottom: "20px", flexWrap: "wrap" as const }}>
        {folders.map((f) => {
          const isActive = folderFilter === f;
          const label = f === "all" ? "All" : f.replace(/\//g, "");
          const count = f === "all" ? mdFiles.length : mdFiles.filter((file) => getFolder(file.path) === f).length;
          return (
            <button
              key={f}
              onClick={() => setFolderFilter(f)}
              style={{
                padding: "6px 14px",
                borderRadius: "20px",
                border: isActive ? "1px solid #7c6ef0" : "1px solid #333",
                background: isActive ? "#7c6ef018" : "transparent",
                color: isActive ? "#7c6ef0" : "#888",
                cursor: "pointer",
                fontSize: "12px",
                fontWeight: isActive ? 600 : 400,
                transition: "all 0.15s",
              }}
            >
              {label} <span style={{ color: isActive ? "#7c6ef080" : "#555", marginLeft: "4px" }}>{count}</span>
            </button>
          );
        })}
      </div>

      <table style={{ width: "100%", borderCollapse: "collapse" as const }}>
        <thead>
          <tr>
            <th style={thStyle} onClick={() => handleSort("name")}>파일명{sortIndicator("name")}</th>
            <th style={{ ...thStyle, width: "120px" }}>폴더</th>
            <th style={{ ...thStyle, width: "80px" }} onClick={() => handleSort("size")}>크기{sortIndicator("size")}</th>
            <th style={{ ...thStyle, width: "120px" }} onClick={() => handleSort("modified")}>수정일{sortIndicator("modified")}</th>
            <th style={{ ...thStyle, width: "60px" }}>보기</th>
          </tr>
        </thead>
        <tbody>
          {filtered.length === 0 ? (
            <tr><td style={{ ...tdStyle, color: "#555" }} colSpan={5}>파일 없음</td></tr>
          ) : (
            filtered.map((f) => (
              <tr key={f.path}>
                <td style={tdStyle}>{f.name}</td>
                <td style={{ ...tdStyle, color: "#666", fontSize: "11px" }}>{getFolder(f.path)}</td>
                <td style={{ ...tdStyle, color: "#666" }}>{formatSize(f.size)}</td>
                <td style={{ ...tdStyle, color: "#666", fontSize: "11px" }}>{new Date(f.modified).toLocaleDateString("ko-KR")}</td>
                <td style={tdStyle}>
                  <button
                    onClick={() => setViewingFile(viewingFile === f.path ? null : f.path)}
                    style={{
                      background: viewingFile === f.path ? "#7c6ef020" : "transparent",
                      border: "1px solid #333",
                      borderRadius: "4px",
                      color: "#7c6ef0",
                      cursor: "pointer",
                      fontSize: "11px",
                      padding: "2px 8px",
                    }}
                  >
                    {viewingFile === f.path ? "Close" : "Open"}
                  </button>
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>

      {viewingFile && (
        <div
          style={{
            position: "fixed",
            top: 0, left: 0, right: 0, bottom: 0,
            background: "rgba(0,0,0,0.7)",
            zIndex: 9999,
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
          onClick={() => setViewingFile(null)}
        >
          <div
            style={{
              width: "80%",
              maxWidth: "900px",
              maxHeight: "85vh",
              background: "#111",
              borderRadius: "12px",
              border: "1px solid #333",
              display: "flex",
              flexDirection: "column" as const,
              overflow: "hidden",
            }}
            onClick={(e) => e.stopPropagation()}
          >
            <div style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              padding: "16px 24px",
              borderBottom: "1px solid #2a2a2a",
              flexShrink: 0,
            }}>
              <span style={{ fontSize: "13px", color: "#aaa" }}>{viewingFile}</span>
              <button
                onClick={() => setViewingFile(null)}
                style={{
                  background: "#222",
                  border: "1px solid #333",
                  borderRadius: "6px",
                  color: "#aaa",
                  cursor: "pointer",
                  fontSize: "13px",
                  padding: "4px 12px",
                }}
              >
                Close
              </button>
            </div>
            <div style={{ overflow: "auto", flex: 1 }}>
              <FileViewer filePath={viewingFile} />
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
