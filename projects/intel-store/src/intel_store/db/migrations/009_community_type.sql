-- Migration 009: Add 'community' to item_type CHECK constraint
-- Enables Reddit, HackerNews, Polymarket community signal collection

ALTER TABLE intel_items DROP CONSTRAINT intel_items_item_type_check;
ALTER TABLE intel_items ADD CONSTRAINT intel_items_item_type_check
  CHECK (item_type IN ('news','paper','patent','statement','report','standard','community'));
