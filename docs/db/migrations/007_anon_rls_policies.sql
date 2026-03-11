-- Add anon role RLS policies for trend-tracker tables (2026-03-11)
-- trend-tracker MCP uses anon key, needs read/write access.

-- topics: anon can read (needed for slug → id resolution)
CREATE POLICY anon_read ON topics FOR SELECT TO anon USING (true);

-- watch_topics: anon can CRUD (manage_watch_topics tool)
CREATE POLICY anon_all ON watch_topics FOR ALL TO anon USING (true) WITH CHECK (true);

-- trend_snapshots: anon can CRUD (upsert_snapshot, compare_snapshots)
CREATE POLICY anon_all ON trend_snapshots FOR ALL TO anon USING (true) WITH CHECK (true);
