-- Enable RLS on all public tables and grant full access to service_role only.
-- anon/authenticated keys will be blocked from all tables.

-- 1. Enable RLS
ALTER TABLE public.carriers ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.collection_runs ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.financial_metrics ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.intel_item_relations ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.intel_item_topics ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.intel_items ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.parse_issues ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.source_documents ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.topics ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.trend_snapshots ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.watch_topics ENABLE ROW LEVEL SECURITY;

-- 2. Allow service_role full access (bypasses RLS by default, but explicit policy is safer)
CREATE POLICY "service_role_all" ON public.carriers FOR ALL TO service_role USING (true) WITH CHECK (true);
CREATE POLICY "service_role_all" ON public.collection_runs FOR ALL TO service_role USING (true) WITH CHECK (true);
CREATE POLICY "service_role_all" ON public.financial_metrics FOR ALL TO service_role USING (true) WITH CHECK (true);
CREATE POLICY "service_role_all" ON public.intel_item_relations FOR ALL TO service_role USING (true) WITH CHECK (true);
CREATE POLICY "service_role_all" ON public.intel_item_topics FOR ALL TO service_role USING (true) WITH CHECK (true);
CREATE POLICY "service_role_all" ON public.intel_items FOR ALL TO service_role USING (true) WITH CHECK (true);
CREATE POLICY "service_role_all" ON public.parse_issues FOR ALL TO service_role USING (true) WITH CHECK (true);
CREATE POLICY "service_role_all" ON public.source_documents FOR ALL TO service_role USING (true) WITH CHECK (true);
CREATE POLICY "service_role_all" ON public.topics FOR ALL TO service_role USING (true) WITH CHECK (true);
CREATE POLICY "service_role_all" ON public.trend_snapshots FOR ALL TO service_role USING (true) WITH CHECK (true);
CREATE POLICY "service_role_all" ON public.watch_topics FOR ALL TO service_role USING (true) WITH CHECK (true);
