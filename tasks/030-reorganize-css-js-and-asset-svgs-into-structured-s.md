---
id: "030"
title: "Reorganize CSS, JS, and Asset SVGs into Structured Subdirectories"
type: "feature"
status: "done"
created_at: "2026-11-18"
updated_at: "2026-11-18"
---

# [Feature] Reorganize CSS, JS, and Asset SVGs into Structured Subdirectories

## Description
Reorganize CSS, JS, and Asset SVGs into Structured Subdirectories

## Acceptance Criteria
- [x] Move style.css to assets/css/style.css and script.js to assets/js/script.js
- [x] Structure assets/ subdirectories into brand/, css/, js/, maps/, projects/, projects-light/, and team/ with zero loose files
- [x] Reorganize scripts/ into js/, py/, and sh/ with zero loose scripts
- [x] Update all 11 HTML pages, sitemap.xml, script.js theme switcher, and nginx.conf with backward-compatible 301 redirects
- [x] Verify zero broken links across all pages and pass 100% automated test suite in scripts/sh/test.sh

## Context / Notes
- Target files: 
- Dependencies: None
