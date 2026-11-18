---
id: "028"
title: "Remove Square Grid Motifs and Preserve Structural Grid Borders"
type: "feature"
status: "done"
created_at: "2026-11-18"
updated_at: "2026-11-18"
---

# [Feature] Remove Square Grid Motifs and Preserve Structural Grid Borders

## Description
Remove Square Grid Motifs and Preserve Structural Grid Borders

## Acceptance Criteria
- [x] Remove 64px square blueprint grid background lines from .sketch-frame in style.css (both default Dark Mode and [data-theme="light"])
- [x] Remove 32px square grid pattern from .section-title-box in style.css (both default Dark Mode and [data-theme="light"])
- [x] Retain outer diagonal gutter hatch pattern on body (-45deg repeating linear gradient) on both left and right margins as requested
- [x] Retain all primary structural borders (sketch-frame left/right borders, sketch-divider, card borders, section-title-box border and '+' markers, column grids)
- [x] Verify clean, crisp flat backgrounds inside the central sketch frame across both Dark and Light modes
- [x] Verify test suite in scripts/sh/test.sh passes 100% green
- [x] Push changes to origin devv and main branches

## Context / Notes
- Target files: 
- Dependencies: None
