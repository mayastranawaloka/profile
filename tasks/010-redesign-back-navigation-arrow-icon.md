---
id: "010"
title: "Redesign Back Navigation Arrow Icon"
type: "feature"
status: "in-progress"
created_at: "2026-11-14"
updated_at: "2026-11-14"
---

# [Feature] Redesign Back Navigation Arrow Icon

## Description
Replace raw HTML unicode back arrow entity (&larr;) with a bespoke, razor-sharp minimalist SVG arrow icon across all detail and reader pages (project-erp.html, project-ecommerce.html, project-cms.html, article.html), with refined CSS styling and smooth micro-interaction on hover.

## Acceptance Criteria
- [ ] Replace `<span>&larr;</span>` with inline minimalist SVG arrow in `project-erp.html`
- [ ] Replace `<span>&larr;</span>` with inline minimalist SVG arrow in `project-ecommerce.html`
- [ ] Replace `<span>&larr;</span>` with inline minimalist SVG arrow in `project-cms.html`
- [ ] Replace `<span>&larr;</span>` with inline minimalist SVG arrow in `article.html`
- [ ] Update `style.css` `.project-breadcrumb` and `.breadcrumb-arrow` with high-precision layout, alignment, and hover physics (`translateX(-4px)`)
- [ ] Verify `./test.sh` passes completely (zero emojis, zero em dashes, XML well-formed)
- [ ] Redeploy Docker container via `./redeploy.sh`
- [ ] Commit and push to `devv` and `main`

## Context / Notes
- Target files: 
- Dependencies: None
