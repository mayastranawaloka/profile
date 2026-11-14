---
id: "009"
title: "Harmonize 30 Project Detail SVGs with Master Home Design Systems"
type: "feature"
status: "in-progress"
created_at: "2026-11-14"
updated_at: "2026-11-14"
---

# [Feature] Harmonize 30 Project Detail SVGs with Master Home Design Systems

## Description
Redesign all 30 project detail SVGs (10 ERP, 10 E-Commerce, 10 CMS) to strictly adhere to the exact design system, canvas dimensions (1600x1000), browser headers, navigation bars, sidebars, typography, colors, and visual language of the 3 master home SVGs (assets/project-erp.svg, assets/project-ecommerce.svg, assets/project-cms.svg), ensuring 100% authenticity and visual coherence as real application screenshots. Home SVGs remain strictly untouched.

## Acceptance Criteria
- [ ] Phase 1: Define and verify exact design system specs from master home SVGs
- [ ] Phase 2: Redesign 10 ERP detail SVGs matching MAYA ERP design system
  - [ ] 01-executive-overview.svg
  - [ ] 02-warehouse-inventory.svg
  - [ ] 03-procurement-pipeline.svg
  - [ ] 04-financial-ledger.svg
  - [ ] 05-sales-dispatch.svg
  - [ ] 06-supply-chain-flow.svg
  - [ ] 07-employee-rbac.svg
  - [ ] 08-asset-maintenance.svg
  - [ ] 09-audit-logs.svg
  - [ ] 10-system-settings.svg
- [ ] Phase 3: Redesign 10 E-Commerce detail SVGs matching KRONIK COMMERCE design system
  - [ ] 01-curated-storefront.svg
  - [ ] 02-product-detail.svg
  - [ ] 03-instant-search-filters.svg
  - [ ] 04-slide-cart-ledger.svg
  - [ ] 05-streamlined-checkout.svg
  - [ ] 06-payment-gateway.svg
  - [ ] 07-order-tracking.svg
  - [ ] 08-merchant-dashboard.svg
  - [ ] 09-inventory-sync.svg
  - [ ] 10-customer-loyalty.svg
- [ ] Phase 4: Redesign 10 CMS detail SVGs matching PULSE CMS design system
  - [ ] 01-editorial-workspace.svg
  - [ ] 02-content-repository.svg
  - [ ] 03-seo-optimizer.svg
  - [ ] 04-media-library.svg
  - [ ] 05-publishing-workflow.svg
  - [ ] 06-revision-history.svg
  - [ ] 07-taxonomy-manager.svg
  - [ ] 08-audience-analytics.svg
  - [ ] 09-api-distribution.svg
  - [ ] 10-access-governance.svg
- [ ] Phase 5: XML validation, zero emojis, zero em dashes, test.sh green
- [ ] Phase 6: Headless Chrome screenshot visual audit & Docker redeploy
- [ ] Phase 7: Push changes to devv and main

## Context / Notes
- Home master SVGs (assets/project-erp.svg, assets/project-ecommerce.svg, assets/project-cms.svg) MUST NEVER BE CHANGED.
- All detail SVGs must look like real, high-fidelity screenshots of the respective application.
