-- 004: Add deal pipeline stage to su_companies
-- Tracks internal deal progression: discovered → screening → dd → proposed → invested → passed

ALTER TABLE su_companies
ADD COLUMN IF NOT EXISTS deal_stage TEXT CHECK (deal_stage IN (
    'discovered',   -- 발굴 (startup-scout 등으로 발견)
    'screening',    -- 1차 스크리닝 (startup-analyst 분석 중)
    'due_diligence',-- DD 진행 (기술/재무/법률 실사)
    'proposed',     -- 투자위 상정
    'invested',     -- 투자 완료
    'partnership',  -- 제휴/협력 체결
    'passed'        -- 검토 후 패스
));

-- Index for filtering by deal stage
CREATE INDEX IF NOT EXISTS idx_su_companies_deal_stage ON su_companies(deal_stage);

-- RLS policy for anon access (consistent with existing policies)
-- No additional RLS needed; existing su_companies policies cover this column
