---
id: "004"
title: "Seamless Organic Ambient Glow for Footer Logo"
type: "bugfix"
status: "done"
created_at: "2026-11-14"
updated_at: "2026-11-14"
---

# [Bugfix] Seamless Organic Ambient Glow for Footer Logo

## Description
Eliminate rectangular border lines and center square seams on the footer logo banner by replacing artificial vignetting with a continuous quartic elliptical ambient aura that smoothly dissolves into pitch black (#000000) with zero visible edges.

## Acceptance Criteria
- [x] Eliminate rectangular and beveled border lines on the left and right of the logo banner.
- [x] Eliminate the center patch boundary around the lotus flower.
- [x] Apply an elliptical quartic smooth decay function fading the blue glow seamlessly to pure #000000 at all edges.
- [x] E2E verification across 1440px and 1920px viewports ensuring edge pixels are 100% black with zero visible lines.
- [x] Commit and push to devv and main branches.

## Context / Notes
- Target files: `assets/logo-banner.png`, `scripts/generate_banner.py`
- Dependencies: None
