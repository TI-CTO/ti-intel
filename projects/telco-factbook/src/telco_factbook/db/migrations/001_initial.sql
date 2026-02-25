-- Telco Factbook: Initial Schema
-- Run this in Supabase SQL Editor

-- Carriers
CREATE TABLE IF NOT EXISTS carriers (
    id TEXT PRIMARY KEY,
    name_ko TEXT NOT NULL,
    name_en TEXT NOT NULL,
    stock_code TEXT
);

INSERT INTO carriers (id, name_ko, name_en, stock_code) VALUES
    ('SKT', 'SK텔레콤', 'SK Telecom', '017670'),
    ('KT', 'KT', 'KT Corp', '030200')
ON CONFLICT (id) DO NOTHING;

-- Source documents metadata
CREATE TABLE IF NOT EXISTS source_documents (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    carrier_id TEXT NOT NULL REFERENCES carriers(id),
    year INT NOT NULL,
    quarter INT NOT NULL,
    doc_type TEXT NOT NULL,
    source_url TEXT NOT NULL,
    local_path TEXT,
    file_hash TEXT,
    downloaded_at TIMESTAMPTZ NOT NULL,
    parsed_at TIMESTAMPTZ,
    UNIQUE(carrier_id, year, quarter, doc_type)
);

-- Core financial metrics
CREATE TABLE IF NOT EXISTS financial_metrics (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    carrier_id TEXT NOT NULL REFERENCES carriers(id),
    year INT NOT NULL,
    quarter INT NOT NULL,
    period_type TEXT NOT NULL,

    -- Income statement (million KRW)
    revenue BIGINT,
    operating_income BIGINT,
    net_income BIGINT,
    ebitda BIGINT,

    -- Revenue breakdown
    revenue_mobile BIGINT,
    revenue_fixed BIGINT,
    revenue_media BIGINT,
    revenue_enterprise BIGINT,

    -- Profitability (%)
    operating_margin NUMERIC(5,2),
    net_margin NUMERIC(5,2),

    -- Balance sheet
    total_assets BIGINT,
    total_debt BIGINT,
    capex BIGINT,

    -- Subscribers
    mobile_subscribers BIGINT,
    mobile_5g_subscribers BIGINT,
    iptv_subscribers BIGINT,
    broadband_subscribers BIGINT,
    arpu_mobile INT,

    -- Meta
    source_doc_id BIGINT REFERENCES source_documents(id),
    unit TEXT DEFAULT 'million_krw',
    notes TEXT,
    created_at TIMESTAMPTZ DEFAULT now(),

    UNIQUE(carrier_id, year, quarter, period_type)
);

-- Parse issues tracking
CREATE TABLE IF NOT EXISTS parse_issues (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    source_doc_id BIGINT REFERENCES source_documents(id),
    field_name TEXT,
    raw_value TEXT,
    issue_type TEXT,
    resolved BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- Collection run log
CREATE TABLE IF NOT EXISTS collection_runs (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    started_at TIMESTAMPTZ NOT NULL,
    completed_at TIMESTAMPTZ,
    carrier_id TEXT,
    year_from INT,
    year_to INT,
    documents_found INT DEFAULT 0,
    documents_downloaded INT DEFAULT 0,
    documents_parsed INT DEFAULT 0,
    errors INT DEFAULT 0,
    status TEXT DEFAULT 'running',
    error_log TEXT
);

-- Indexes for common queries
CREATE INDEX IF NOT EXISTS idx_metrics_carrier_year
    ON financial_metrics(carrier_id, year, quarter);
CREATE INDEX IF NOT EXISTS idx_docs_carrier_year
    ON source_documents(carrier_id, year, quarter);
