# Guide: startup-db UI Implementation Roadmap

Based on research of professional platforms (Crunchbase, PitchBook, CB Insights, Tracxn, Dealroom), this guide provides actionable implementation priorities for startup-db dashboard.

---

## Quick Reference: UI Pattern Summary

### 5 Core Patterns (Verified Across All Major Platforms)

1. **Left Sidebar + Top Tabs** Navigation (Material Design)
   - Left: Vertical navigation (sections, filters, saved items)
   - Top: Horizontal tabs (Companies, Investors, Signals, etc.)
   - Center/Right: Content area (profile, table, chart)

2. **Faceted Search** with Dynamic Filters
   - Multi-select checkboxes
   - Live item count per filter
   - "Show More" for overflow
   - Edit Columns customization

3. **4-Tier Information Hierarchy**
   - Tier 1: At-a-glance (company name, score, status)
   - Tier 2: Quick assessment (About, Highlights sections)
   - Tier 3: Analysis (expandable tabs)
   - Tier 4: Detail view (tables, charts)

4. **Collections + Tagging** System
   - Create lists from search results (3 methods)
   - Bulk tagging of companies
   - Tag-based market landscape building

5. **Market Visualization**
   - 2-axis market maps (innovation vs market size, etc.)
   - Time-series charts (funding, headcount growth)
   - Comparative side-by-side views
   - Geographic ecosystem comparison (Dealroom pattern)

---

## Implementation Phases

### Phase 1: Foundation (Must-Have)

**Estimated effort**: 4-6 weeks

#### 1.1 Profile Page Layout

```
┌─ Header ──────────────────────────────────────────┐
│  [Logo] Company Name        [Status] [Score: 85]   │
│         Description                                 │
└───────────────────────────────────────────────────┘

┌─ Left Sidebar    ┌─ Main Content ────────────────┐
│ • About          │ [Overview Tab] [Details] [..] │
│ • Highlights     │                               │
│ • Tech Stack     │ ┌─ Section 1 ─────────────┐   │
│ • Team           │ │ Key data here          │   │
│ • Financials     │ └────────────────────────┘   │
│ • Signals        │                               │
│ • Competitors    │ ┌─ Section 2 ─────────────┐   │
│ • Related        │ │ More details           │   │
│                  │ └────────────────────────┘   │
└──────────────────└───────────────────────────────┘
```

**Data to include per section:**

| Section | Data Points | Format |
|---------|---|---|
| **About** | Description, Headquarters, Founded, Stage, Employee Count | Text + Key-value |
| **Highlights** | Total Funding, Valuation, Last Round, Recent News | Cards |
| **Tech Stack** | Technologies, Platforms, Tools (scraped or manual) | Badge list |
| **Team** | Founders, C-suite, Key roles (LinkedIn links) | Avatar + Name |
| **Financials** | Funding rounds, Exit status, Revenue estimate | Timeline + Table |
| **Signals** | Recent news, acquisitions, team changes | Activity log |
| **Competitors** | Similar companies (ML-based or manual) | Card list |

#### 1.2 Search Interface

```
┌─ Search Header ───────────────────┐
│ Search: [___________]  [Filter ▼] │
└───────────────────────────────────┘

┌─ Filter Panel ─────────────────────┐
│ ✕ Clear All                        │
│                                    │
│ ▼ Location                         │
│   ☐ San Francisco (125)           │
│   ☐ New York (89)                 │
│   ☐ London (34)                   │
│   [+ Show More]                    │
│                                    │
│ ▼ Industry                         │
│   ☐ AI & ML (234)                 │
│   ☐ SaaS (189)                    │
│   ☐ Fintech (156)                 │
│   [+ Show More]                    │
│                                    │
│ ▼ Funding Stage                    │
│   ☐ Seed (45)                     │
│   ☐ Series A (78)                 │
│   ☐ Series B+ (123)               │
│                                    │
│ ▼ Headcount                        │
│   [≥ ___] [≤ ___] employees       │
│                                    │
│ [Apply] [Reset]                   │
└───────────────────────────────────┘

Results: 456 companies found
┌─ Results Table ────────────────────┐
│ [Edit Columns ▼]                   │
│                                    │
│ Company    | Location | Stage      │
│ StartupA   | SF       | Series A   │
│ StartupB   | NYC      | Seed       │
│ StartupC   | London   | Series B   │
│                                    │
│ [← Prev] [1] [2] [3] [...] [Next →]│
└───────────────────────────────────┘
```

**Filters to implement** (Priority order):

| Priority | Filter | Type | Use Case |
|----------|--------|------|----------|
| P0 | Industry / Sector | Multi-select | Most common search |
| P0 | Location / Region | Multi-select | Geographic focus |
| P0 | Funding Stage | Multi-select | Deal flow segmentation |
| P0 | Headcount | Range slider | Size filtering |
| P1 | Founding Year | Date range | Cohort analysis |
| P1 | Total Funding | Currency range | Deal size filtering |
| P1 | Status (Active/Acquired/IPO) | Multi-select | Exit tracking |
| P2 | Company Score/Rating | Range slider | Quality filtering |
| P2 | Growth Rate | Comparison | Momentum signals |

#### 1.3 Company List + Collections

```
Search Results Table:
┌─ Actions ─────────────────────────────┐
│ [☐ Select All] [+ Add to List ▼]     │
└───────────────────────────────────────┘

☐ Company Name  | Location | Funding | Status
☐ Startup A     | SF       | $5.2M   | Active
☐ Startup B     | NYC      | $12M    | Active
☐ Startup C     | London   | Seed    | Active

[Create New List] or [Add to Existing]:
  • My Watchlist
  • Series A Targets
  • Competitors - AI Space
```

**List operations:**
- [ ] Create from search (select rows → Save to List)
- [ ] Quick Add (open list → add manually)
- [ ] Email alerts (when new companies match list criteria)
- [ ] Export to CSV

---

### Phase 2: Advanced Features (Should-Have)

**Estimated effort**: 3-4 weeks

#### 2.1 Visualization Dashboard

**Funding Trends Chart** (Time series):
```
Funding Over Time (2021-2026)
┌─────────────────────────────────┐
│ $50M │                          │
│      │    ╱╲                    │
│ $40M │   ╱  ╲    ╱─╲             │
│      │  ╱    ╲  ╱   ╲           │
│ $30M │ ╱      ╲╱     ╲╱         │
│      └─────────────────────────  │
│ Year: 2021  2022  2023  2024   │
└─────────────────────────────────┘
```

**Market Map** (2-axis scatter):
```
Market Size (Y-axis)

      Large ●●●●
            ●●●  (Established Players)
      ●●● ●
    ●● ●●● ●●   (Mid-tier)
   ● ●● ● ●●
  ●●●● ● ●●●
    (Early-stage)
          Small ●●●

      Low ← Innovation → High
```

**Headcount Growth** (Bar + Trend):
```
Team Size Progress (2024-2026)
├─ 2024: 45 employees
├─ 2025: 78 employees (+73%)
└─ 2026: 124 employees (+59%)

Visual: ▓▓▓░  Growth trend 🟢 Positive
```

#### 2.2 Company Comparison View

```
Comparison: Startup A vs Startup B vs Startup C

┌─────────────────────────────────────────────────┐
│           | Startup A | Startup B | Startup C   │
├─────────────────────────────────────────────────┤
│ Founding  │ 2019      │ 2020      │ 2018        │
│ Location  │ SF        │ NYC       │ London      │
│ Funding   │ $12.5M    │ $8.2M     │ $25M        │
│ Stage     │ Series B  │ Series A  │ Series C    │
│ Employees │ 45        │ 28        │ 89          │
│ Status    │ Active    │ Active    │ Active      │
│ Score     │ 78/100    │ 62/100    │ 85/100      │
└─────────────────────────────────────────────────┘

[Download as PNG] [Export to Excel]
```

#### 2.3 Company Score / Health Metric

Design a startup-db specific scoring model (inspired by CB Insights Mosaic):

```
Startup Health Score (0-100)

Overall: 78/100 🟢

Components:
├─ Funding Health (25%):        72/100
│  └─ Recent rounds, burn rate
├─ Team Quality (25%):          85/100
│  └─ Founder background, experience
├─ Market Opportunity (25%):    75/100
│  └─ TAM, growth rate, competition
└─ Growth Signals (25%):        82/100
   └─ User growth, revenue, hires
```

---

### Phase 3: Ecosystem & Analytics (Nice-to-Have)

**Estimated effort**: 4-6 weeks

#### 3.1 Ecosystem View (per City/Country)

```
Startup Ecosystem: Silicon Valley

Statistics (Left Panel):
├─ Total Companies: 3,247
├─ VC Investment 2026: $8.4B (↑12%)
├─ Unicorns: 47
├─ Avg Valuation: $45M
├─ Top Sector: AI/ML (23%)

Interactive Map (Center):
┌─────────────────────────────┐
│ 🗺️  [Map View]  [List View]  │
│                             │
│ ○ ○ ○ ○ ○ ○ ○ ○ ○         │
│ ○ ○ ○ ○ ○ ○ ○ ○ ○         │
│ ○ ○ ● ○ ○ ○ ○ ○ ○         │
│ ○ ○ ○ ○ ○ ○ ○ ○ ○         │
│                             │
│ Bubble size: Funding amount │
│ Color: Growth rate         │
└─────────────────────────────┘

Comparison (Right Panel):
┌─ Compare With ──────────────┐
│ [SF vs NYC]                 │
│ [SF vs London]              │
│ [SF vs Tokyo]               │
│                             │
│ SF: 3,247 companies         │
│ NYC: 2,156 companies        │
│ London: 1,834 companies     │
└─────────────────────────────┘
```

#### 3.2 Predictive Signals

```
Growth Signals for Startup A

🔴 Critical:
  └─ Revenue growth slowing (from +180% to +45%)

🟡 Warning:
  ├─ Employee churn increased (5% → 8%)
  └─ Series funding delay (expected Q1, now Q2?)

🟢 Positive:
  ├─ New strategic partnership announced
  └─ Product milestone: 100k users reached
```

---

## Implementation Checklist

### UI Components (Reusable)

- [ ] **ProfileCard**: Logo, name, score, status badge, tags
- [ ] **FilterPanel**: Expandable filter groups with checkboxes + counts
- [ ] **DataTable**: Sortable columns, searchable rows, Edit Columns
- [ ] **ComparisonTable**: Side-by-side multi-row view
- [ ] **LineChart**: Time-series (Chart.js or Recharts)
- [ ] **ScatterChart**: 2-axis market map
- [ ] **BubbleChart**: Geographic or market position
- [ ] **StatusBadge**: Active, Acquired, IPO, Stealth
- [ ] **StageBadge**: Seed, Series A/B/C/D+
- [ ] **TagList**: Company tags (industry, region, etc.)
- [ ] **SearchBar**: With recent searches, saved filters
- [ ] **CollectionSelector**: Dropdown to save to list

### Database Schema Extensions

Based on UI needs:

```sql
-- Company profile enrichment
ALTER TABLE companies ADD COLUMN (
  health_score INT,  -- 0-100 (Phase 2)
  recent_signals JSONB,  -- news, team changes, funding
  tech_stack JSONB,  -- technologies array
  team_data JSONB,  -- key people + roles
  market_score INT,  -- market opportunity (Phase 2)
  growth_rate NUMERIC  -- YoY or QoQ %
);

-- Collections (lists with rules)
CREATE TABLE collections (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL,
  name VARCHAR(255),
  description TEXT,
  is_dynamic BOOLEAN,  -- rules-based vs static
  filter_rules JSONB,  -- saved filter set
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);

CREATE TABLE collection_items (
  id UUID PRIMARY KEY,
  collection_id UUID REFERENCES collections,
  company_id UUID REFERENCES companies,
  tags JSONB,  -- array of string tags
  added_at TIMESTAMP
);

-- Saved searches
CREATE TABLE saved_searches (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL,
  name VARCHAR(255),
  filters JSONB,  -- filter state
  sort_by VARCHAR(50),
  created_at TIMESTAMP
);
```

### Frontend Routes (SPA Structure)

```
/companies
  /
    ├─ ?search=...&industry=...&location=...
    ├─ [Results table with filters sidebar]

/companies/:id
  ├─ [Profile page with sections]
  ├─ /comparable (side-by-side comparison)
  ├─ /history (funding timeline)

/collections
  ├─ [List of user's collections]
  ├─ /:collectionId
    ├─ [Spreadsheet-like view]
    ├─ [Bulk tagging]
    ├─ [Export CSV]

/ecosystem
  ├─ /[city-slug]
  ├─ [Map + benchmarking]
  ├─ /compare?cities=sf,nyc,london

/analytics
  ├─ [Funding trends]
  ├─ [Market maps]
  ├─ [Team metrics]
```

---

## Design System Tokens

### Color Palette

```
Primary: #007AFF (Blue)         - Active, CTAs
Success: #34C759 (Green)        - Positive signals
Warning: #FF9500 (Orange)       - Caution signals
Error: #FF3B30 (Red)            - Critical signals
Neutral: #8E8E93               - Secondary text
Background: #F5F5F7            - Light BG
```

### Funding Stage Colors

```
Seed:       #E8F4F8 (Light blue)
Series A:   #D4E9F7 (Blue)
Series B:   #9BCFEA (Bright blue)
Series C:   #4A90E2 (Deep blue)
Series D+:  #1E40AF (Navy)
IPO:        #34C759 (Green)
Acquired:   #8E8E93 (Gray)
```

### Typography

```
Headings:
  h1: 32px, Bold (600)      - Profile name
  h2: 24px, Semibold (600)  - Section titles
  h3: 18px, Semibold (600)  - Subsection titles

Body:
  Large: 16px, Regular       - Main content
  Normal: 14px, Regular      - Secondary info
  Small: 12px, Regular       - Labels, metadata

Mono:
  Code: 13px, monospace      - IDs, amounts
```

### Spacing Scale

```
xs: 4px
sm: 8px
md: 16px
lg: 24px
xl: 32px
```

---

## Success Metrics

### Phase 1 (Foundation)

- [ ] Profile pages load in < 2s (90th percentile)
- [ ] Filter responsiveness: < 500ms per facet change
- [ ] Search results display 100+ rows smoothly (virtual scroll)
- [ ] Mobile navigation usable on screens < 375px

### Phase 2 (Advanced)

- [ ] Market maps render < 1s
- [ ] Comparison view supports 3+ companies
- [ ] Health score calculated in < 100ms
- [ ] Collections feature adoption > 40% of users

### Phase 3 (Ecosystem)

- [ ] Ecosystem map loads with 100+ bubbles
- [ ] Live benchmarking data updates hourly
- [ ] Signals alerts sent within 1 hour of event
- [ ] Export to Excel/PNG < 2s

---

## Dependencies & Tech Stack

### Recommended Frontend

- **React 18+** (component reusability)
- **React Query** (data fetching, caching)
- **Recharts** or **Chart.js** (visualizations)
- **Tanstack/React Table** (complex data tables)
- **Zustand** or **Jotai** (lightweight state)
- **Tailwind CSS** (utility styling)

### Backend Considerations

- **Search Engine**: Elasticsearch or Postgres full-text search (for 100k+ records)
- **Real-time Updates**: WebSocket or Server-Sent Events (for signals)
- **Caching**: Redis (for aggregated metrics, market maps)
- **Background Jobs**: Celery or Bull (for score calculations)

---

## References

- Research: `/docs/research-startup-db-ui-patterns.md`
- Dashboard Guide: `/docs/guide-startup-db-ui.md` (if exists)
- Existing UI Spec: `/docs/spec-dashboard-ui.md` (if exists)

---

*Last updated: 2026-03-17*
