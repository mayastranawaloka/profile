---
id: "003"
title: "Fix SVG XML Entities and Uncropped Panoramic Logo Banner"
type: "bugfix"
status: "done"
created_at: "2026-11-14"
updated_at: "2026-11-14"
---

# [Bugfix] Fix SVG XML Entities and Uncropped Panoramic Logo Banner

## Description
Fix undefined HTML entities in SVGs causing Chrome parse failures on ecommerce and cms mockups, and eliminate bottom logo clipping by generating a widescreen panoramic banner where the lotus emblem is 100% visible and uncropped.

## Acceptance Criteria
- [x] Fix XML entities in assets/project-ecommerce.svg and assets/project-cms.svg (replace &rarr; and &bull; with valid XML entities &#8594; and &#8226;).
- [x] Add automated SVG XML validation to test suite test.sh.
- [x] Resolve bottom logo clipping: generate high-fidelity panoramic assets/logo-banner.png (1920x780) with centered lotus flower having generous margins so petals are never cropped.
- [x] Update CSS and index.html to render full-width banner with height auto and zero clipping.
- [x] E2E Playwright verification over HTTP and file:// protocol.
- [x] Commit and push to devv and main branches.

## Context / Notes
- Target files: `assets/*`, `index.html`, `style.css`, `test.sh`, `scripts/*`
- Dependencies: None
