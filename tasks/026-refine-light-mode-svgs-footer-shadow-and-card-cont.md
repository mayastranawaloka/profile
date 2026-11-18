---
id: "026"
title: "Refine Light Mode SVGs Footer Shadow and Card Contrast"
type: "feature"
status: "done"
created_at: "2026-11-18"
updated_at: "2026-11-18"
---

# [Feature] Refine Light Mode SVGs Footer Shadow and Card Contrast

## Description
Refine Light Mode SVGs Footer Shadow and Card Contrast

## Acceptance Criteria
- [x] Map 100% of all 41 hex colors in generate_light_svgs.py so no dark container/canvas hex remains in Light Mode SVGs
- [x] Regenerate all 61 light SVGs (5 master SVGs, 55 detail SVGs, 1 Indonesia map SVG) with crisp, high-contrast monochrome light rendering
- [x] Fix footer logo shadow in style.css: change .giant-logo-container background to #ffffff and ::before gradient from black to pure white stops without altering positioning, percentages, or layout
- [x] Fix project-deepdive-box in style.css under [data-theme="light"] (light background, neutral border, dark title, muted body text)
- [x] Fix project-screen-caption in style.css under [data-theme="light"] (light background, dark title, readable description, crisp badge)
- [x] Fix project-spec-card, project-cta-banner, article-reader-footer-box, blockquote in style.css under [data-theme="light"]
- [x] Audit all pages in browser across light and dark modes to ensure zero contrast or visual defects
- [x] Verify test suite in scripts/sh/test.sh passes 100% green
- [x] Push to devv and main branches

## Context / Notes
- Target files: 
- Dependencies: None
