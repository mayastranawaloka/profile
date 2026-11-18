---
id: "024"
title: "Reorganize Root Directory with Pages and Scripts Subfolders and Fortify Linking"
type: "feature"
status: "done"
created_at: "2026-11-18"
updated_at: "2026-11-18"
---

# [Feature] Reorganize Root Directory with Pages and Scripts Subfolders and Fortify Linking

## Description
Reorganize Root Directory with Pages and Scripts Subfolders and Fortify Linking

## Acceptance Criteria
- [x] Move all HTML files other than index.html into pages/ directory
- [x] Move all Python generator scripts into scripts/py/
- [x] Move all shell scripts into scripts/sh/ and update working directories and relative paths
- [x] Update all hyperlinks, assets, stylesheet, script, and canonical URLs across index.html and all pages in pages/
- [x] Update script.js navigation and link detection to support pages/ directory
- [x] Update nginx.conf and sitemap.xml to match new pages/ layout
- [x] Update test suite in scripts/sh/test.sh to verify new directory structure and link integrity
- [x] Update README.md with clean root structure
- [x] Verify test suite passes 100% green
- [x] Push to devv and main branches as instructed

## Context / Notes
- Target files: 
- Dependencies: None
