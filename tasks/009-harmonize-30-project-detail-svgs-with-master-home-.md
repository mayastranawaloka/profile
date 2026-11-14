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
- [x] Phase 1: Define and verify exact design system specs from master home SVGs
- [x] Phase 2: Redesign 10 ERP detail SVGs matching MAYA ERP design system
  - [x] 01-executive-overview.svg
  - [x] 02-warehouse-inventory.svg
  - [x] 03-procurement-pipeline.svg
  - [x] 04-financial-ledger.svg
  - [x] 05-sales-dispatch.svg
  - [x] 06-supply-chain-flow.svg
  - [x] 07-employee-rbac.svg
  - [x] 08-asset-maintenance.svg
  - [x] 09-audit-logs.svg
  - [x] 10-system-settings.svg
- [x] Phase 3: Redesign 10 E-Commerce detail SVGs matching KRONIK COMMERCE design system
  - [x] 01-curated-storefront.svg
  - [x] 02-product-detail.svg
  - [x] 03-instant-search-filters.svg
  - [x] 04-slide-cart-ledger.svg
  - [x] 05-streamlined-checkout.svg
  - [x] 06-payment-gateway.svg
  - [x] 07-order-tracking.svg
  - [x] 08-merchant-dashboard.svg
  - [x] 09-inventory-sync.svg
  - [x] 10-customer-loyalty.svg
- [x] Phase 4: Redesign 10 CMS detail SVGs matching PULSE CMS design system
  - [x] 01-editorial-workspace.svg
  - [x] 02-content-repository.svg
  - [x] 03-seo-optimizer.svg
  - [x] 04-media-library.svg
  - [x] 05-publishing-workflow.svg
  - [x] 06-revision-history.svg
  - [x] 07-taxonomy-manager.svg
  - [x] 08-audience-analytics.svg
  - [x] 09-api-distribution.svg
  - [x] 10-access-governance.svg
- [ ] Phase 5: XML validation, zero emojis, zero em dashes, test.sh green
- [ ] Phase 6: Headless Chrome screenshot visual audit & Docker redeploy
- [ ] Phase 7: Push changes to devv and main

## Context / Notes
- Home master SVGs (assets/project-erp.svg, assets/project-ecommerce.svg, assets/project-cms.svg) MUST NEVER BE CHANGED.
- All detail SVGs must look like real, high-fidelity screenshots of the respective application.
