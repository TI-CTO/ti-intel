-- Tech Intelligence Platform — Full Schema
-- Supabase project: tech-intel (ref: wzkmucknomctkyygciof)
-- Last updated: 2026-02-25
-- Tables: 15 total
--
-- KEEP (telco-factbook — real data, no changes):
--   carriers, source_documents, parse_issues, collection_runs, financial_metrics
--
-- SHARED:
--   topics
--
-- TREND-TRACKER (migrated to FK in 002_topic_fk.sql):
--   watch_topics, news_items, trend_snapshots
--
-- RESEARCH-HUB:
--   papers, paper_topics, paper_stats
--
-- PATENT-INTEL:
--   patents, patent_topics, patent_stats

-- ── SHARED ──────────────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS topics (
    id BIGSERIAL PRIMARY KEY,
    slug TEXT NOT NULL UNIQUE,
    display_name TEXT NOT NULL,
    description TEXT,
    parent_id BIGINT REFERENCES topics(id),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_topics_slug ON topics(slug);

-- ── RESEARCH-HUB ────────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS papers (
    id BIGSERIAL PRIMARY KEY,
    external_id TEXT NOT NULL UNIQUE,   -- e.g. arxiv:2312.00752 or doi:10.1234/...
    source TEXT NOT NULL,               -- arxiv | semantic_scholar | pubmed
    title TEXT NOT NULL,
    authors JSONB DEFAULT '[]'::jsonb,
    published_date DATE,
    abstract TEXT DEFAULT '',
    citation_count INTEGER DEFAULT 0,
    reliability_tag CHAR(1) DEFAULT 'A' CHECK (reliability_tag IN ('A', 'B', 'C', 'D')),
    raw_url TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_papers_source ON papers(source);
CREATE INDEX IF NOT EXISTS idx_papers_published ON papers(published_date DESC);

CREATE TABLE IF NOT EXISTS paper_topics (
    paper_id BIGINT NOT NULL REFERENCES papers(id) ON DELETE CASCADE,
    topic_id BIGINT NOT NULL REFERENCES topics(id) ON DELETE CASCADE,
    relevance NUMERIC(4,3) DEFAULT 1.0,
    PRIMARY KEY (paper_id, topic_id)
);

CREATE INDEX IF NOT EXISTS idx_paper_topics_topic_id ON paper_topics(topic_id);

CREATE TABLE IF NOT EXISTS paper_stats (
    id BIGSERIAL PRIMARY KEY,
    topic_id BIGINT NOT NULL REFERENCES topics(id),
    stat_year SMALLINT NOT NULL,
    stat_month SMALLINT NOT NULL CHECK (stat_month BETWEEN 1 AND 12),
    paper_count INTEGER DEFAULT 0,
    avg_citations NUMERIC(10,2) DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(topic_id, stat_year, stat_month)
);

CREATE INDEX IF NOT EXISTS idx_paper_stats_topic_id ON paper_stats(topic_id);
CREATE INDEX IF NOT EXISTS idx_paper_stats_period ON paper_stats(stat_year, stat_month, paper_count DESC);

-- ── PATENT-INTEL ────────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS patents (
    id BIGSERIAL PRIMARY KEY,
    external_id TEXT NOT NULL UNIQUE,   -- e.g. US20240012345A1
    source TEXT NOT NULL,               -- kipris | epo | uspto
    title TEXT NOT NULL,
    applicant TEXT NOT NULL,
    filing_date DATE,
    publication_date DATE,
    ipc_codes JSONB DEFAULT '[]'::jsonb, -- IPC classification codes
    abstract TEXT DEFAULT '',
    reliability_tag CHAR(1) DEFAULT 'A' CHECK (reliability_tag IN ('A', 'B', 'C', 'D')),
    raw_url TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_patents_source ON patents(source);
CREATE INDEX IF NOT EXISTS idx_patents_filing ON patents(filing_date DESC);
CREATE INDEX IF NOT EXISTS idx_patents_applicant ON patents(applicant);

CREATE TABLE IF NOT EXISTS patent_topics (
    patent_id BIGINT NOT NULL REFERENCES patents(id) ON DELETE CASCADE,
    topic_id BIGINT NOT NULL REFERENCES topics(id) ON DELETE CASCADE,
    relevance NUMERIC(4,3) DEFAULT 1.0,
    PRIMARY KEY (patent_id, topic_id)
);

CREATE INDEX IF NOT EXISTS idx_patent_topics_topic_id ON patent_topics(topic_id);

CREATE TABLE IF NOT EXISTS patent_stats (
    id BIGSERIAL PRIMARY KEY,
    topic_id BIGINT NOT NULL REFERENCES topics(id),
    stat_year SMALLINT NOT NULL,
    stat_quarter SMALLINT NOT NULL CHECK (stat_quarter BETWEEN 1 AND 4),
    filing_count INTEGER DEFAULT 0,
    top_applicants JSONB DEFAULT '[]'::jsonb,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(topic_id, stat_year, stat_quarter)
);

CREATE INDEX IF NOT EXISTS idx_patent_stats_topic_id ON patent_stats(topic_id, stat_year DESC, stat_quarter DESC);
