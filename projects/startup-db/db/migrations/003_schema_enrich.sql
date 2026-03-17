-- 003_schema_enrich.sql
-- Part A: Company metadata enrichment columns
-- Part B: L1/L2/L3 taxonomy mapping table (su_company_topics)

-- ── Part A: New columns on su_companies ──────────────────────

ALTER TABLE su_companies
  ADD COLUMN IF NOT EXISTS one_liner TEXT;

ALTER TABLE su_companies
  ADD COLUMN IF NOT EXISTS employee_range TEXT CHECK (employee_range IN (
    '1-10','11-50','51-200','201-500','501-1000','1001-5000','5000+'
  ));

ALTER TABLE su_companies
  ADD COLUMN IF NOT EXISTS growth_stage TEXT CHECK (growth_stage IN (
    'pre-seed','seed','early','growth','late','public'
  ));

ALTER TABLE su_companies
  ADD COLUMN IF NOT EXISTS linkedin_url TEXT;

ALTER TABLE su_companies
  ADD COLUMN IF NOT EXISTS total_raised NUMERIC DEFAULT 0;

ALTER TABLE su_companies
  ADD COLUMN IF NOT EXISTS last_funding_date DATE;

ALTER TABLE su_companies
  ADD COLUMN IF NOT EXISTS last_funding_type TEXT;

-- ── Part B: Company topics table ─────────────────────────────

CREATE TABLE IF NOT EXISTS su_company_topics (
    company_id UUID REFERENCES su_companies(id) ON DELETE CASCADE,
    l3_slug TEXT NOT NULL,
    assigned_by TEXT,
    assigned_at TIMESTAMPTZ DEFAULT now(),
    PRIMARY KEY (company_id, l3_slug)
);

CREATE INDEX IF NOT EXISTS idx_company_topics_l3
  ON su_company_topics(l3_slug);

-- RLS
ALTER TABLE su_company_topics ENABLE ROW LEVEL SECURITY;

CREATE POLICY anon_read_company_topics ON su_company_topics
  FOR SELECT TO anon USING (true);

CREATE POLICY anon_insert_company_topics ON su_company_topics
  FOR INSERT TO anon WITH CHECK (true);

CREATE POLICY anon_update_company_topics ON su_company_topics
  FOR UPDATE TO anon USING (true) WITH CHECK (true);

CREATE POLICY anon_delete_company_topics ON su_company_topics
  FOR DELETE TO anon USING (true);
