---
id: "008"
title: "Project Detail Pages with 30 SVGs, Standalone Article Reader, and ID-EN Language"
type: "feature"
status: "done"
created_at: "2026-11-14"
updated_at: "2026-11-14"
---

# [Feature] Project Detail Pages with 30 SVGs, Standalone Article Reader, and ID-EN Language

## Description
Create dedicated project detail pages for ERP, E-Commerce, and CMS with 10 coded preview SVGs each (30 total), replace all popup modals with direct page navigation (including standalone article reader article.html), and harmonize all website copy into natural ID-EN casual professional Gen Z tone.

## Acceptance Criteria
- [x] Generate 30 high-fidelity coded SVGs (10 ERP, 10 E-Commerce, 10 CMS)
- [x] Create dedicated project detail pages: project-erp.html, project-ecommerce.html, project-cms.html
- [x] Create standalone article reader page: article.html with dynamic content loading by URL param
- [x] Update index.html: remove #previewModal, link projects directly to detail pages, rewrite copy to ID-EN casual professional
- [x] Update articles.html: remove #articleModal, link articles directly to article.html?id=X, rewrite copy to ID-EN casual professional
- [x] Update about.html, service.html, contact.html: rewrite copy to ID-EN casual professional
- [x] Update script.js: remove modal logic, support standalone article page rendering
- [x] Update style.css: styles for project detail screens grid, breadcrumbs, article reader
- [x] Update test.sh to verify new pages, zero modals, 30 SVGs, zero emojis, zero em dashes
- [x] All tests pass (green) and Docker redeployed
