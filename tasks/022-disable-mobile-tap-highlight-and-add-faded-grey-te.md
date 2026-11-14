---
id: "022"
title: "Disable Mobile Tap Highlight and Add Faded Grey Text Selection Styling"
type: "style"
status: "done"
created_at: "2026-11-14"
updated_at: "2026-11-14"
---

# [Style] Disable Mobile Tap Highlight and Add Faded Grey Text Selection Styling

## Description
Disable the mobile blue tap highlight indicator (-webkit-tap-highlight-color: transparent) across mobile views and customize the text selection highlight (block teks) with a sleek, faded monochrome zinc-grey color palette (::selection and ::-moz-selection) that harmonizes with our design system, as well as refining callout/blockquote text blocks.

## Acceptance Criteria
- [x] Disabled -webkit-tap-highlight-color across all elements, links, buttons, and inputs
- [x] Custom ::selection and ::-moz-selection styled with soft faded zinc-grey (#27272a / rgba(161, 161, 170, 0.28)) and crisp text
- [x] Text blocks (blockquote and article callouts) styled with refined faded grey accents (#52525b border, #a1a1aa text, subtle dark surface)
- [x] Verification test suite passes 100%
- [x] Container redeployed
- [x] Changes committed with conventional commit format (closes task-022)
- [x] Pushed to devv and merged to main

## Context / Notes
- Target files: style.css, test.sh
