#!/usr/bin/env bash
set -euo pipefail

echo "[*] Running verification test suite..."

PAGES=(
  "index.html"
  "about.html"
  "service.html"
  "articles.html"
  "contact.html"
  "project-erp.html"
  "project-ecommerce.html"
  "project-cms.html"
  "article.html"
)

# 1. Structural Checks on all pages
for page in "${PAGES[@]}"; do
  echo "[*] Verifying structural standards on ${page}..."
  if [[ ! -f "$page" ]]; then
    echo "FAIL: missing page $page"
    exit 1
  fi
  # Verify Navbar with clock (UTC+7, no dot) and menus
  grep -q 'class="navbar"' "$page" || { echo "FAIL: navbar missing in $page"; exit 1; }
  grep -q 'id="wibClock"' "$page" || { echo "FAIL: clock missing in $page"; exit 1; }
  grep -q 'UTC+7' "$page" || { echo "FAIL: UTC+7 missing in $page"; exit 1; }
  if grep -q 'wib-dot' "$page"; then
    echo "FAIL: unwanted wib-dot found in $page"
    exit 1
  fi
  grep -q 'data-page="home"' "$page" || { echo "FAIL: home link missing in $page"; exit 1; }
  grep -q 'data-page="about"' "$page" || { echo "FAIL: about link missing in $page"; exit 1; }
  grep -q 'data-page="service"' "$page" || { echo "FAIL: service link missing in $page"; exit 1; }
  grep -q 'data-page="articles"' "$page" || { echo "FAIL: articles link missing in $page"; exit 1; }
  grep -q 'data-page="contact"' "$page" || { echo "FAIL: contact link missing in $page"; exit 1; }

  # Verify Tailwind & Figma Grid Sketch Layout
  grep -q 'class="sketch-frame"' "$page" || { echo "FAIL: sketch-frame missing in $page"; exit 1; }
  grep -q 'class="sketch-divider"' "$page" || { echo "FAIL: sketch-divider missing in $page"; exit 1; }

  # Verify Footer and original logo image
  grep -q 'BY. PT MAYASTRA NAWALOKA NUSANTARA' "$page" || { echo "FAIL: footer info missing in $page"; exit 1; }
  grep -q 'src="assets/logo.png"' "$page" || { echo "FAIL: original logo missing in $page"; exit 1; }
done

# 2. Strict Zero Popups Check (Zero Modals across entire site)
echo "[*] Verifying Strict Zero Popups across all pages..."
for page in "${PAGES[@]}"; do
  if grep -q 'id="previewModal"' "$page"; then
    echo "FAIL: unwanted previewModal found in $page (strict zero popups mandate)"
    exit 1
  fi
  if grep -q 'id="articleModal"' "$page"; then
    echo "FAIL: unwanted articleModal found in $page (strict zero popups mandate)"
    exit 1
  fi
done

# 3. Dedicated Project Pages Verifications
echo "[*] Verifying dedicated project detail pages..."
for proj in "project-erp.html" "project-ecommerce.html" "project-cms.html"; do
  grep -q 'class="project-breadcrumb"' "$proj" || { echo "FAIL: breadcrumb missing in $proj"; exit 1; }
  grep -q 'class="project-specs-grid"' "$proj" || { echo "FAIL: specs grid missing in $proj"; exit 1; }
  grep -q 'class="project-screens-grid"' "$proj" || { echo "FAIL: screens grid missing in $proj"; exit 1; }
  SCREEN_COUNT=$(grep -c 'class="project-screen-card"' "$proj" || true)
  if [[ "$SCREEN_COUNT" -ne 10 ]]; then
    echo "FAIL: Expected 10 project screens in $proj, found ${SCREEN_COUNT}"
    exit 1
  fi
done

# Verify all 30 SVGs exist and are linked in respective pages
for i in {1..10}; do
  NUM=$(printf "%02d" $i)
  grep -q "assets/projects/erp/${NUM}-" project-erp.html || { echo "FAIL: missing SVG ${NUM} in project-erp.html"; exit 1; }
  grep -q "assets/projects/ecommerce/${NUM}-" project-ecommerce.html || { echo "FAIL: missing SVG ${NUM} in project-ecommerce.html"; exit 1; }
  grep -q "assets/projects/cms/${NUM}-" project-cms.html || { echo "FAIL: missing SVG ${NUM} in project-cms.html"; exit 1; }
done

# 4. Standalone Article Reader Page Verification
echo "[*] Verifying standalone article reader page..."
grep -q 'id="articleReaderView"' article.html || { echo "FAIL: articleReaderView missing in article.html"; exit 1; }
grep -q 'id="articleCategoryBadge"' article.html || { echo "FAIL: category badge missing in article.html"; exit 1; }
grep -q 'id="articleTitle"' article.html || { echo "FAIL: title element missing in article.html"; exit 1; }
grep -q 'id="articleBody"' article.html || { echo "FAIL: body element missing in article.html"; exit 1; }

# 5. Articles page: 20 article cards (10 insight + 10 how-we-work) and direct links
echo "[*] Verifying articles count and structure..."
INSIGHT_COUNT=$(grep -c 'data-category="insight"' articles.html || true)
SERVICE_COUNT=$(grep -c 'data-category="how-we-work"' articles.html || true)

if [[ "$INSIGHT_COUNT" -ne 10 ]]; then
  echo "FAIL: Expected 10 insight articles, found ${INSIGHT_COUNT}"
  exit 1
fi

if [[ "$SERVICE_COUNT" -ne 10 ]]; then
  echo "FAIL: Expected 10 how-we-work articles, found ${SERVICE_COUNT}"
  exit 1
fi

grep -q 'id="articleSearchInput"' articles.html || { echo "FAIL: search input missing in articles.html"; exit 1; }

# 6. Validate XML structure of all SVG assets
echo "[*] Validating XML structure of all 30+ SVG assets..."
python3 -c '
import xml.etree.ElementTree as ET
import glob, sys

svg_files = glob.glob("assets/**/*.svg", recursive=True)
if len(svg_files) < 30:
    print(f"FAIL: Expected at least 30 SVGs, found {len(svg_files)}")
    sys.exit(1)

for svg in svg_files:
    try:
        ET.parse(svg)
    except Exception as e:
        print(f"FAIL: SVG parse error in {svg}: {e}")
        sys.exit(1)
print(f"[*] Validated {len(svg_files)} SVGs successfully.")
'

# 7. Verify CNAME
if [[ ! -f "CNAME" ]]; then
  echo "FAIL: missing CNAME"
  exit 1
fi
grep -q 'www.mayastranawaloka.com' CNAME || { echo "FAIL: CNAME content mismatch"; exit 1; }

# 8. Verify Zero Emojis and Zero Em Dashes
echo "[*] Checking for banned characters (emojis, em dashes)..."
python3 -c '
import re, sys, glob

banned_chars = ["—", "–", "&#8212;", "&#8211;", "&mdash;", "&ndash;"]
files = [
    "index.html", "about.html", "service.html", "articles.html", "contact.html",
    "project-erp.html", "project-ecommerce.html", "project-cms.html", "article.html",
    "style.css", "script.js"
] + glob.glob("assets/**/*.svg", recursive=True)

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    for b in banned_chars:
        if b in content:
            print(f"FAIL: Banned dash {b} found in {path}")
            sys.exit(1)
    emoji_pattern = re.compile(r"[\U00010000-\U0010ffff]", flags=re.UNICODE)
    if emoji_pattern.search(content):
        print(f"FAIL: Emoji detected in {path}")
        sys.exit(1)
print(f"[*] Verified zero emojis and zero em dashes across {len(files)} files.")
'

echo "[OK] All 9 pages and 30 project SVGs passed verification suite cleanly!"
