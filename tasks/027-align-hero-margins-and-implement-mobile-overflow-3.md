---
id: "027"
title: "Align Hero Margins and Implement Mobile Overflow 3-Dots Navbar"
type: "feature"
status: "done"
created_at: "2026-11-18"
updated_at: "2026-11-18"
---

# [Feature] Align Hero Margins and Implement Mobile Overflow 3-Dots Navbar

## Description
Align Hero Margins and Implement Mobile Overflow 3-Dots Navbar

## Acceptance Criteria
- [x] Align hero section margins (.hero-container) to strictly match .container and .nav-container (padding: 0 40px on desktop, 0 24px / 0 16px responsive) so left and right text blocks align perfectly with section headers and navbar
- [x] Add 3-dots overflow button (kebab ellipsis icon) to navbar in all 11 pages (index.html and 10 pages in pages/)
- [x] Implement responsive mobile navigation dropdown: on mobile (<= 768px), nav links collapse into clean 3-dots overflow dropdown while keeping live WIB clock and theme toggle accessible
- [x] Implement mobile overflow toggle behavior in script.js (click toggle, close on link click, close on click outside, close on Escape key)
- [x] Style mobile overflow menu with strict monochrome Dark and Light mode parity in style.css
- [x] Fix dangling CSS block at line 439 in style.css
- [x] Verify responsive layout across mobile, tablet, and desktop viewports in browser
- [x] Verify test suite in scripts/sh/test.sh passes 100% green
- [x] Push changes to origin devv and main branches

## Context / Notes
- Target files: 
- Dependencies: None
