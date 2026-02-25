-- Trend Tracker: migrate topic TEXT → topic_id FK
-- Requires: topics table already created (001_initial from platform schema)
-- Run this in Supabase SQL Editor or via Management API

-- Drop old tables (data was empty)
DROP TABLE IF EXISTS watch_topics CASCADE;
DROP TABLE IF EXISTS trend_snapshots CASCADE;
DROP TABLE IF EXISTS news_items CASCADE;

-- News items collected from various sources
CREATE TABLE IF NOT EXISTS news_items (
    id BIGSERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    source TEXT NOT NULL,
    url TEXT NOT NULL UNIQUE,
    published_date DATE,
    collected_date DATE NOT NULL DEFAULT CURRENT_DATE,
    topic_id BIGINT NOT NULL REFERENCES topics(id),
    summary TEXT DEFAULT '',
    reliability_tag CHAR(1) DEFAULT 'C' CHECK (reliability_tag IN ('A', 'B', 'C', 'D')),
    keywords JSONB DEFAULT '[]'::jsonb,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_news_items_topic_id ON news_items(topic_id);
CREATE INDEX IF NOT EXISTS idx_news_items_published ON news_items(published_date DESC);
CREATE INDEX IF NOT EXISTS idx_news_items_collected ON news_items(collected_date DESC);

-- Periodic trend snapshots per topic and source type
CREATE TABLE IF NOT EXISTS trend_snapshots (
    id BIGSERIAL PRIMARY KEY,
    topic_id BIGINT NOT NULL REFERENCES topics(id),
    snapshot_date DATE NOT NULL DEFAULT CURRENT_DATE,
    source_type TEXT NOT NULL DEFAULT 'news' CHECK (source_type IN ('news', 'papers', 'patents', 'combined')),
    summary TEXT NOT NULL,
    key_signals JSONB DEFAULT '[]'::jsonb,
    item_count INTEGER DEFAULT 0,
    sentiment TEXT DEFAULT 'neutral' CHECK (sentiment IN ('positive', 'neutral', 'negative', 'mixed')),
    change_level TEXT DEFAULT 'none' CHECK (change_level IN ('none', 'minor', 'notable', 'urgent')),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(topic_id, snapshot_date, source_type)
);

CREATE INDEX IF NOT EXISTS idx_trend_snapshots_topic_id ON trend_snapshots(topic_id, source_type, snapshot_date DESC);

-- Topics registered for periodic monitoring
CREATE TABLE IF NOT EXISTS watch_topics (
    id BIGSERIAL PRIMARY KEY,
    topic_id BIGINT NOT NULL UNIQUE REFERENCES topics(id),
    keywords JSONB DEFAULT '[]'::jsonb,
    frequency TEXT DEFAULT 'weekly' CHECK (frequency IN ('daily', 'weekly', 'monthly')),
    is_active BOOLEAN DEFAULT TRUE,
    last_scanned TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_watch_topics_active ON watch_topics(is_active) WHERE is_active = TRUE;
