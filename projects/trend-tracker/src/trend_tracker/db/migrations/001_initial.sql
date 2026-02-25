-- Trend Tracker: initial schema
-- Run this in Supabase SQL Editor

-- News items collected from various sources
CREATE TABLE IF NOT EXISTS news_items (
    id BIGSERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    source TEXT NOT NULL,
    url TEXT NOT NULL UNIQUE,
    published_date DATE,
    collected_date DATE NOT NULL DEFAULT CURRENT_DATE,
    topic TEXT NOT NULL,
    summary TEXT DEFAULT '',
    reliability_tag CHAR(1) DEFAULT 'C' CHECK (reliability_tag IN ('A', 'B', 'C', 'D')),
    keywords JSONB DEFAULT '[]'::jsonb,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_news_items_topic ON news_items(topic);
CREATE INDEX IF NOT EXISTS idx_news_items_published ON news_items(published_date DESC);
CREATE INDEX IF NOT EXISTS idx_news_items_collected ON news_items(collected_date DESC);

-- Periodic trend snapshots per topic
CREATE TABLE IF NOT EXISTS trend_snapshots (
    id BIGSERIAL PRIMARY KEY,
    topic TEXT NOT NULL,
    snapshot_date DATE NOT NULL DEFAULT CURRENT_DATE,
    summary TEXT NOT NULL,
    key_signals JSONB DEFAULT '[]'::jsonb,
    news_count INTEGER DEFAULT 0,
    sentiment TEXT DEFAULT 'neutral' CHECK (sentiment IN ('positive', 'neutral', 'negative', 'mixed')),
    change_level TEXT DEFAULT 'none' CHECK (change_level IN ('none', 'minor', 'notable', 'urgent')),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(topic, snapshot_date)
);

CREATE INDEX IF NOT EXISTS idx_trend_snapshots_topic ON trend_snapshots(topic);
CREATE INDEX IF NOT EXISTS idx_trend_snapshots_date ON trend_snapshots(snapshot_date DESC);

-- Topics registered for periodic monitoring
CREATE TABLE IF NOT EXISTS watch_topics (
    id BIGSERIAL PRIMARY KEY,
    topic TEXT NOT NULL UNIQUE,
    keywords JSONB DEFAULT '[]'::jsonb,
    frequency TEXT DEFAULT 'weekly' CHECK (frequency IN ('daily', 'weekly', 'monthly')),
    is_active BOOLEAN DEFAULT TRUE,
    last_scanned TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_watch_topics_active ON watch_topics(is_active) WHERE is_active = TRUE;
