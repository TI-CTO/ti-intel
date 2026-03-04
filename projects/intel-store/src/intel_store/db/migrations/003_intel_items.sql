-- Migration 003: Unified intel_items table with pgvector and full-text search
-- Depends on: pgvector extension, topics table (from migration 001)

-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- ── Core table: unified intelligence items ──────────────────────────

CREATE TABLE intel_items (
    id              BIGSERIAL PRIMARY KEY,

    -- Type discriminator
    item_type       TEXT NOT NULL
                    CHECK (item_type IN ('news','paper','patent','statement','report','standard')),

    -- Deduplication
    external_id     TEXT,                           -- "ss:abc123", "uspto:US1234", URL, etc.
    content_hash    TEXT NOT NULL,                   -- SHA-256(title + abstract[:200])

    -- Core fields
    title           TEXT NOT NULL,
    abstract        TEXT DEFAULT '',
    source_name     TEXT NOT NULL,                   -- "Semantic Scholar", "USPTO", "조선일보", "Samsung"
    source_url      TEXT,
    published_date  DATE,
    collected_date  DATE NOT NULL DEFAULT CURRENT_DATE,
    language        TEXT DEFAULT 'en'
                    CHECK (language IN ('en','ko','mixed')),

    -- Quality
    reliability     TEXT DEFAULT 'C'
                    CHECK (reliability IN ('A','B','C','D')),

    -- Type-specific extension fields (JSONB)
    metadata        JSONB DEFAULT '{}'::jsonb,

    -- Vector embedding (multilingual-e5-large: 1024 dims)
    embedding       vector(1024),

    -- Full-text search (Korean+English mixed)
    search_text     TSVECTOR,

    -- Timestamps
    created_at      TIMESTAMPTZ DEFAULT NOW(),
    updated_at      TIMESTAMPTZ DEFAULT NOW(),

    -- Composite unique: same type+source+external_id = duplicate
    UNIQUE (item_type, source_name, external_id)
);

-- ── Topic linking (N:M) ─────────────────────────────────────────────

CREATE TABLE intel_item_topics (
    item_id     BIGINT NOT NULL REFERENCES intel_items(id) ON DELETE CASCADE,
    topic_id    BIGINT NOT NULL REFERENCES topics(id) ON DELETE CASCADE,
    relevance   NUMERIC(4,3) DEFAULT 1.000,         -- 0.000~1.000
    assigned_by TEXT DEFAULT 'collector'
                CHECK (assigned_by IN ('collector','embedding','manual')),
    PRIMARY KEY (item_id, topic_id)
);

-- ── Item-to-item relations ──────────────────────────────────────────

CREATE TABLE intel_item_relations (
    source_id       BIGINT NOT NULL REFERENCES intel_items(id) ON DELETE CASCADE,
    target_id       BIGINT NOT NULL REFERENCES intel_items(id) ON DELETE CASCADE,
    relation_type   TEXT NOT NULL
                    CHECK (relation_type IN ('cites','mentions','same_event','updates','contradicts')),
    confidence      NUMERIC(4,3) DEFAULT 1.000,
    created_at      TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (source_id, target_id, relation_type)
);

-- ── Indexes ─────────────────────────────────────────────────────────

-- Full-text search (GIN)
CREATE INDEX idx_intel_search_text
    ON intel_items USING gin (search_text);

-- Filter indexes
CREATE INDEX idx_intel_type          ON intel_items (item_type);
CREATE INDEX idx_intel_published     ON intel_items (published_date DESC);
CREATE INDEX idx_intel_collected     ON intel_items (collected_date DESC);
CREATE INDEX idx_intel_content_hash  ON intel_items (content_hash);
CREATE INDEX idx_intel_external_id   ON intel_items (external_id) WHERE external_id IS NOT NULL;

-- Topic join index
CREATE INDEX idx_item_topics_topic   ON intel_item_topics (topic_id);

-- Relations target index
CREATE INDEX idx_item_relations_target ON intel_item_relations (target_id);

-- NOTE: HNSW vector index is created AFTER embedding backfill (step 10)
-- to avoid slow incremental inserts during bulk load.
-- See: scripts/create_hnsw_index.sql

-- ── Trigger: auto-update search_text on insert/update ───────────────

CREATE OR REPLACE FUNCTION intel_items_search_text_trigger()
RETURNS trigger AS $$
BEGIN
    NEW.search_text :=
        setweight(to_tsvector('simple', COALESCE(NEW.title, '')), 'A') ||
        setweight(to_tsvector('simple', COALESCE(NEW.abstract, '')), 'B');
    NEW.updated_at := NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_intel_items_search_text
    BEFORE INSERT OR UPDATE OF title, abstract
    ON intel_items
    FOR EACH ROW
    EXECUTE FUNCTION intel_items_search_text_trigger();

-- ── SQL function: semantic search ───────────────────────────────────

CREATE OR REPLACE FUNCTION search_intel_semantic(
    query_embedding vector(1024),
    match_threshold float DEFAULT 0.7,
    match_count int DEFAULT 20,
    filter_types text[] DEFAULT NULL,
    filter_topic_id bigint DEFAULT NULL,
    filter_since date DEFAULT NULL
)
RETURNS TABLE (
    id bigint,
    item_type text,
    title text,
    source_name text,
    source_url text,
    published_date date,
    abstract text,
    metadata jsonb,
    similarity float
)
LANGUAGE sql STABLE
AS $$
    SELECT
        i.id,
        i.item_type,
        i.title,
        i.source_name,
        i.source_url,
        i.published_date,
        i.abstract,
        i.metadata,
        1 - (i.embedding <=> query_embedding) AS similarity
    FROM intel_items i
    LEFT JOIN intel_item_topics it ON it.item_id = i.id
    WHERE
        i.embedding IS NOT NULL
        AND 1 - (i.embedding <=> query_embedding) >= match_threshold
        AND (filter_types IS NULL OR i.item_type = ANY(filter_types))
        AND (filter_topic_id IS NULL OR it.topic_id = filter_topic_id)
        AND (filter_since IS NULL OR i.published_date >= filter_since)
    GROUP BY i.id
    ORDER BY i.embedding <=> query_embedding
    LIMIT match_count;
$$;
