-- Migration 002: Add key_highlights + source_refs table
-- Date: 2026-02-25
-- Description:
--   1. Add key_highlights column to papers, patents, news_items
--   2. Create source_refs table for whitepapers, standards, internal docs, general URLs
--   3. Create source_ref_topics junction table

-- ── 1. key_highlights on existing tables ────────────────────────────────────

ALTER TABLE papers ADD COLUMN IF NOT EXISTS key_highlights TEXT;
ALTER TABLE patents ADD COLUMN IF NOT EXISTS key_highlights TEXT;
ALTER TABLE news_items ADD COLUMN IF NOT EXISTS key_highlights TEXT;

-- ── 2. source_refs ───────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS source_refs (
    id              BIGSERIAL PRIMARY KEY,
    source_type     TEXT NOT NULL
                    CHECK (source_type IN ('whitepaper', 'standard', 'internal', 'url', 'report')),
    title           TEXT NOT NULL,
    organization    TEXT,                   -- 발행 기관 (삼성, ITU, LG U+ 등)
    url             TEXT,                   -- 접근 가능한 경우
    file_path       TEXT,                   -- references/ 폴더 상대경로 (파일인 경우)
    published_date  DATE,
    abstract        TEXT,                   -- 원문 개요 (있는 경우)
    key_highlights  TEXT,                   -- Claude 분석 후 주목 포인트
    reliability_tag CHAR(1) DEFAULT 'B'
                    CHECK (reliability_tag IN ('A', 'B', 'C', 'D')),
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_source_refs_type
    ON source_refs(source_type);
CREATE INDEX IF NOT EXISTS idx_source_refs_published
    ON source_refs(published_date DESC);

-- ── 3. source_ref_topics (junction) ─────────────────────────────────────────

CREATE TABLE IF NOT EXISTS source_ref_topics (
    source_ref_id   BIGINT NOT NULL REFERENCES source_refs(id) ON DELETE CASCADE,
    topic_id        BIGINT NOT NULL REFERENCES topics(id) ON DELETE CASCADE,
    PRIMARY KEY (source_ref_id, topic_id)
);

CREATE INDEX IF NOT EXISTS idx_source_ref_topics_topic_id
    ON source_ref_topics(topic_id);
