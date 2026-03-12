-- 008: Add anon RLS policies to intel_items, intel_item_topics, intel_item_relations
-- Fix: MCP server uses anon key, but these tables only had service_role policies

CREATE POLICY anon_all ON public.intel_items FOR ALL TO anon USING (true) WITH CHECK (true);
CREATE POLICY anon_all ON public.intel_item_topics FOR ALL TO anon USING (true) WITH CHECK (true);
CREATE POLICY anon_all ON public.intel_item_relations FOR ALL TO anon USING (true) WITH CHECK (true);
