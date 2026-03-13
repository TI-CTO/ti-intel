-- startup-db schema: 11 tables with su_ prefix
-- Target: Supabase wzkmucknomctkyygciof (shared with intel-store)

-- ① Companies (master)
CREATE TABLE su_companies (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    slug TEXT UNIQUE NOT NULL,
    description TEXT,
    website TEXT,
    logo_url TEXT,
    founded_date DATE,
    status TEXT DEFAULT 'active' CHECK (status IN ('active', 'acquired', 'ipo', 'defunct', 'unknown')),
    main_category TEXT,
    sub_category TEXT,
    tags TEXT[] DEFAULT '{}',
    country TEXT,
    city TEXT,
    technology TEXT,
    main_product TEXT,
    discovery_source TEXT,
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_su_companies_slug ON su_companies (slug);
CREATE INDEX idx_su_companies_category ON su_companies (main_category);
CREATE INDEX idx_su_companies_status ON su_companies (status);
CREATE INDEX idx_su_companies_country ON su_companies (country);

-- ② People
CREATE TABLE su_people (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    title TEXT,
    organization TEXT,
    linkedin_url TEXT,
    email TEXT,
    bio TEXT,
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);

-- ③ Investors
CREATE TABLE su_investors (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    slug TEXT UNIQUE NOT NULL,
    investor_type TEXT CHECK (investor_type IN ('vc', 'angel', 'pe', 'cvc', 'accelerator', 'government', 'other')),
    description TEXT,
    website TEXT,
    country TEXT,
    portfolio_count INT DEFAULT 0,
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_su_investors_slug ON su_investors (slug);

-- ④ Funding rounds
CREATE TABLE su_funding_rounds (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    company_id UUID NOT NULL REFERENCES su_companies(id) ON DELETE CASCADE,
    round_type TEXT NOT NULL CHECK (round_type IN (
        'pre_seed', 'seed', 'series_a', 'series_b', 'series_c',
        'series_d', 'series_e', 'series_f', 'bridge', 'grant',
        'ipo', 'undisclosed', 'other', 'acquired'
    )),
    raised_amount NUMERIC,
    currency TEXT DEFAULT 'KRW',
    announced_date DATE,
    pre_money_valuation NUMERIC,
    post_money_valuation NUMERIC,
    lead_investor_id UUID REFERENCES su_investors(id),
    source_url TEXT,
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_su_funding_company ON su_funding_rounds (company_id);
CREATE INDEX idx_su_funding_type ON su_funding_rounds (round_type);

-- ⑤ Round investors (N:M)
CREATE TABLE su_round_investors (
    round_id UUID REFERENCES su_funding_rounds(id) ON DELETE CASCADE,
    investor_id UUID REFERENCES su_investors(id) ON DELETE CASCADE,
    role TEXT DEFAULT 'participant' CHECK (role IN ('lead', 'participant', 'co_lead')),
    amount NUMERIC,
    PRIMARY KEY (round_id, investor_id)
);

-- ⑥ Acquisitions
CREATE TABLE su_acquisitions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    acquirer_id UUID NOT NULL REFERENCES su_companies(id),
    acquired_id UUID NOT NULL REFERENCES su_companies(id),
    acquisition_type TEXT CHECK (acquisition_type IN ('full', 'acqui_hire', 'majority_stake', 'asset_purchase')),
    price NUMERIC,
    currency TEXT,
    announced_date DATE,
    source_url TEXT,
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- ⑦ Company-people relations
CREATE TABLE su_company_people (
    company_id UUID REFERENCES su_companies(id) ON DELETE CASCADE,
    person_id UUID REFERENCES su_people(id) ON DELETE CASCADE,
    role TEXT NOT NULL CHECK (role IN ('founder', 'ceo', 'cto', 'advisor', 'board_member', 'employee', 'other')),
    is_current BOOLEAN DEFAULT true,
    start_date DATE,
    end_date DATE,
    PRIMARY KEY (company_id, person_id, role)
);

-- ⑧ Company-company relations
CREATE TABLE su_company_relations (
    company_id UUID REFERENCES su_companies(id) ON DELETE CASCADE,
    related_company_id UUID REFERENCES su_companies(id) ON DELETE CASCADE,
    relation_type TEXT NOT NULL CHECK (relation_type IN ('competitor', 'partner', 'customer', 'supplier', 'spin_off')),
    description TEXT,
    source_url TEXT,
    created_at TIMESTAMPTZ DEFAULT now(),
    PRIMARY KEY (company_id, related_company_id, relation_type)
);

-- ⑨ Collections
CREATE TABLE su_collections (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    description TEXT,
    collection_type TEXT DEFAULT 'watchlist' CHECK (collection_type IN ('watchlist', 'market_map', 'shortlist', 'report')),
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE su_collection_items (
    collection_id UUID REFERENCES su_collections(id) ON DELETE CASCADE,
    company_id UUID REFERENCES su_companies(id) ON DELETE CASCADE,
    display_order INT,
    note TEXT,
    PRIMARY KEY (collection_id, company_id)
);

-- ⑩ Scores
CREATE TABLE su_scores (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    company_id UUID NOT NULL REFERENCES su_companies(id) ON DELETE CASCADE,
    tech_strength INT CHECK (tech_strength BETWEEN 1 AND 10),
    market_potential INT CHECK (market_potential BETWEEN 1 AND 10),
    team_quality INT CHECK (team_quality BETWEEN 1 AND 10),
    business_fit INT CHECK (business_fit BETWEEN 1 AND 10),
    traction INT CHECK (traction BETWEEN 1 AND 10),
    overall_score INT CHECK (overall_score BETWEEN 0 AND 100),
    scored_by TEXT,
    rationale TEXT,
    scored_at TIMESTAMPTZ DEFAULT now(),
    UNIQUE (company_id, scored_at)
);

CREATE INDEX idx_su_scores_company ON su_scores (company_id);

-- ⑪ Signals (intel-store link)
CREATE TABLE su_signals (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    company_id UUID NOT NULL REFERENCES su_companies(id) ON DELETE CASCADE,
    intel_item_id UUID,
    signal_type TEXT NOT NULL CHECK (signal_type IN ('mentioned_in', 'funding_news', 'patent_filed', 'partnership', 'hiring')),
    title TEXT,
    source_url TEXT,
    published_date DATE,
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_su_signals_company ON su_signals (company_id);

-- updated_at trigger
CREATE OR REPLACE FUNCTION su_set_updated_at()
RETURNS trigger AS $$
BEGIN
    NEW.updated_at := now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_su_companies_updated
    BEFORE UPDATE ON su_companies
    FOR EACH ROW EXECUTE FUNCTION su_set_updated_at();

CREATE TRIGGER trg_su_people_updated
    BEFORE UPDATE ON su_people
    FOR EACH ROW EXECUTE FUNCTION su_set_updated_at();

CREATE TRIGGER trg_su_investors_updated
    BEFORE UPDATE ON su_investors
    FOR EACH ROW EXECUTE FUNCTION su_set_updated_at();

-- RLS policies (anon read access, matching intel-store pattern)
ALTER TABLE su_companies ENABLE ROW LEVEL SECURITY;
ALTER TABLE su_people ENABLE ROW LEVEL SECURITY;
ALTER TABLE su_investors ENABLE ROW LEVEL SECURITY;
ALTER TABLE su_funding_rounds ENABLE ROW LEVEL SECURITY;
ALTER TABLE su_round_investors ENABLE ROW LEVEL SECURITY;
ALTER TABLE su_acquisitions ENABLE ROW LEVEL SECURITY;
ALTER TABLE su_company_people ENABLE ROW LEVEL SECURITY;
ALTER TABLE su_company_relations ENABLE ROW LEVEL SECURITY;
ALTER TABLE su_collections ENABLE ROW LEVEL SECURITY;
ALTER TABLE su_collection_items ENABLE ROW LEVEL SECURITY;
ALTER TABLE su_scores ENABLE ROW LEVEL SECURITY;
ALTER TABLE su_signals ENABLE ROW LEVEL SECURITY;

CREATE POLICY anon_read_su_companies ON su_companies FOR SELECT TO anon USING (true);
CREATE POLICY anon_read_su_people ON su_people FOR SELECT TO anon USING (true);
CREATE POLICY anon_read_su_investors ON su_investors FOR SELECT TO anon USING (true);
CREATE POLICY anon_read_su_funding_rounds ON su_funding_rounds FOR SELECT TO anon USING (true);
CREATE POLICY anon_read_su_round_investors ON su_round_investors FOR SELECT TO anon USING (true);
CREATE POLICY anon_read_su_acquisitions ON su_acquisitions FOR SELECT TO anon USING (true);
CREATE POLICY anon_read_su_company_people ON su_company_people FOR SELECT TO anon USING (true);
CREATE POLICY anon_read_su_company_relations ON su_company_relations FOR SELECT TO anon USING (true);
CREATE POLICY anon_read_su_collections ON su_collections FOR SELECT TO anon USING (true);
CREATE POLICY anon_read_su_collection_items ON su_collection_items FOR SELECT TO anon USING (true);
CREATE POLICY anon_read_su_scores ON su_scores FOR SELECT TO anon USING (true);
CREATE POLICY anon_read_su_signals ON su_signals FOR SELECT TO anon USING (true);

-- anon write policies for MCP server operations
CREATE POLICY anon_insert_su_companies ON su_companies FOR INSERT TO anon WITH CHECK (true);
CREATE POLICY anon_update_su_companies ON su_companies FOR UPDATE TO anon USING (true) WITH CHECK (true);
CREATE POLICY anon_insert_su_people ON su_people FOR INSERT TO anon WITH CHECK (true);
CREATE POLICY anon_update_su_people ON su_people FOR UPDATE TO anon USING (true) WITH CHECK (true);
CREATE POLICY anon_insert_su_investors ON su_investors FOR INSERT TO anon WITH CHECK (true);
CREATE POLICY anon_update_su_investors ON su_investors FOR UPDATE TO anon USING (true) WITH CHECK (true);
CREATE POLICY anon_insert_su_funding_rounds ON su_funding_rounds FOR INSERT TO anon WITH CHECK (true);
CREATE POLICY anon_insert_su_round_investors ON su_round_investors FOR INSERT TO anon WITH CHECK (true);
CREATE POLICY anon_insert_su_acquisitions ON su_acquisitions FOR INSERT TO anon WITH CHECK (true);
CREATE POLICY anon_insert_su_company_people ON su_company_people FOR INSERT TO anon WITH CHECK (true);
CREATE POLICY anon_update_su_company_people ON su_company_people FOR UPDATE TO anon USING (true) WITH CHECK (true);
CREATE POLICY anon_insert_su_company_relations ON su_company_relations FOR INSERT TO anon WITH CHECK (true);
CREATE POLICY anon_insert_su_collections ON su_collections FOR INSERT TO anon WITH CHECK (true);
CREATE POLICY anon_update_su_collections ON su_collections FOR UPDATE TO anon USING (true) WITH CHECK (true);
CREATE POLICY anon_insert_su_collection_items ON su_collection_items FOR INSERT TO anon WITH CHECK (true);
CREATE POLICY anon_insert_su_scores ON su_scores FOR INSERT TO anon WITH CHECK (true);
CREATE POLICY anon_insert_su_signals ON su_signals FOR INSERT TO anon WITH CHECK (true);
CREATE POLICY anon_delete_su_collection_items ON su_collection_items FOR DELETE TO anon USING (true);
