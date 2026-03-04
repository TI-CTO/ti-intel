-- Run AFTER embedding backfill is complete.
-- HNSW index is much faster to build on pre-populated data vs incremental inserts.

CREATE INDEX idx_intel_embedding
    ON intel_items USING hnsw (embedding vector_cosine_ops)
    WITH (m = 16, ef_construction = 128);
