---
id: "011"
title: "Include Master Home SVGs in Previews and Expand to 11 Real Screens Per Project"
type: "feature"
status: "done"
created_at: "2026-11-14"
updated_at: "2026-11-14"
---

# [Feature] Include Master Home SVGs in Previews and Expand to 11 Real Screens Per Project

## Description
Incorporate the exact master homepage SVGs as Screen 01 in each respective project detail gallery, harmonize all other screens to strictly mirror the sidebar geometry, colors, typography, and component styling of the master home SVG, and expand each project suite to 11 high-fidelity functional screens (meeting and exceeding the "minimal 10 preview" mandate) to demonstrate real, finished, working software architectures.

## Acceptance Criteria
- [x] Phase 1: Set Screen 01 to be byte-for-byte identical to the master home SVG for ERP (`assets/project-erp.svg`), E-Commerce (`assets/project-ecommerce.svg`), and CMS (`assets/project-cms.svg`)
- [x] Phase 2: Update `generate_erp_screens.py` with exact sidebar spacing (46px interval), exact colors, and generate 11 ERP screens (including `11-predictive-forecasting.svg`)
- [x] Phase 3: Update `generate_ecommerce_screens.py` with exact store navbar and colors, and generate 11 E-Commerce screens (including `11-promotions-engine.svg`)
- [x] Phase 4: Update `generate_cms_screens.py` with exact sidebar spacing (46px interval), exact colors, and generate 11 CMS screens (including `11-webhook-integrations.svg`)
- [x] Phase 5: Update `project-erp.html`, `project-ecommerce.html`, and `project-cms.html` to display all 11 screens with rich, realistic enterprise captions and specs
- [x] Phase 6: Update `test.sh` to validate at least 11 screens per project, 36+ SVGs XML valid, zero emojis, zero em dashes
- [x] Phase 7: Redeploy Docker container via `redeploy.sh`, run `test.sh`, and push to `devv` and `main`

## Context / Notes
- Target files: 
- Dependencies: None
