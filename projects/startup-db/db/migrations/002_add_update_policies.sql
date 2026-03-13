-- Add missing UPDATE and DELETE policies for anon role
-- Needed for data correction (e.g. currency fix) and general MCP tool operations

CREATE POLICY anon_update_su_funding_rounds ON su_funding_rounds FOR UPDATE TO anon USING (true) WITH CHECK (true);
CREATE POLICY anon_update_su_round_investors ON su_round_investors FOR UPDATE TO anon USING (true) WITH CHECK (true);
CREATE POLICY anon_update_su_acquisitions ON su_acquisitions FOR UPDATE TO anon USING (true) WITH CHECK (true);
CREATE POLICY anon_update_su_company_people ON su_company_people FOR UPDATE TO anon USING (true) WITH CHECK (true);
CREATE POLICY anon_update_su_company_relations ON su_company_relations FOR UPDATE TO anon USING (true) WITH CHECK (true);
CREATE POLICY anon_update_su_scores ON su_scores FOR UPDATE TO anon USING (true) WITH CHECK (true);
CREATE POLICY anon_update_su_signals ON su_signals FOR UPDATE TO anon USING (true) WITH CHECK (true);
CREATE POLICY anon_update_su_collections ON su_collections FOR UPDATE TO anon USING (true) WITH CHECK (true);
CREATE POLICY anon_update_su_collection_items ON su_collection_items FOR UPDATE TO anon USING (true) WITH CHECK (true);

-- Delete policies for tables that need it
CREATE POLICY anon_delete_su_company_relations ON su_company_relations FOR DELETE TO anon USING (true);
CREATE POLICY anon_delete_su_scores ON su_scores FOR DELETE TO anon USING (true);
CREATE POLICY anon_delete_su_signals ON su_signals FOR DELETE TO anon USING (true);
CREATE POLICY anon_delete_su_collections ON su_collections FOR DELETE TO anon USING (true);
CREATE POLICY anon_delete_su_funding_rounds ON su_funding_rounds FOR DELETE TO anon USING (true);
CREATE POLICY anon_delete_su_round_investors ON su_round_investors FOR DELETE TO anon USING (true);
