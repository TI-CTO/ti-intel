-- Tech Intelligence Platform — Full Schema
-- Supabase project: tech-intel (ref: wzkmucknomctkyygciof)
-- Last updated: 2026-03-11
-- Tables: 11 total (migration 003 완료, deprecated 9개 삭제 완료)
--
-- KEEP (telco-factbook — real data, no changes):
--   carriers, source_documents, parse_issues, collection_runs, financial_metrics
--
-- SHARED:
--   topics
--
-- INTEL-STORE (migration 003 — unified intelligence):
--   intel_items, intel_item_topics, intel_item_relations
--
-- TREND-TRACKER (축소 — news CRUD는 intel-store로 이관):
--   watch_topics, trend_snapshots
--
-- DROPPED (2026-03-04, intel-store 마이그레이션 완료 후 삭제):
--   news_items, papers, paper_topics, paper_stats,
--   patents, patent_topics, patent_stats,
--   source_refs, source_ref_topics

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

-- ── RLS POLICIES (migrations 005, 006, 007) ──────────────────────────────────
-- topics:           service_role_all (ALL), anon_read (SELECT)
-- watch_topics:     service_role_all (ALL), anon_all (ALL)
-- trend_snapshots:  service_role_all (ALL), anon_all (ALL)
-- intel_items:      service_role_all (ALL), anon_all (ALL)
-- intel_item_topics: service_role_all (ALL), anon_all (ALL)
-- intel_item_relations: service_role_all (ALL), anon_all (ALL)
-- See: docs/db/migrations/005_intel_store_rls.sql, 007_anon_rls_policies.sql

-- ── INTEL-STORE (migration 003) ────────────────────────────────────────────
-- Full DDL: projects/intel-store/src/intel_store/db/migrations/003_intel_items.sql
-- Unified intelligence table with pgvector embeddings and full-text search.
-- Replaces papers, patents, news_items, source_refs with a single table.
-- HNSW index created after embedding backfill (2026-03-04).
