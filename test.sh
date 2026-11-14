#!/usr/bin/env bash
set -euo pipefail

echo "[*] Running verification test suite..."

PAGES=("index.html" "about.html" "service.html" "articles.html" "contact.html")

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

# 2. Page Specific Content Verifications
echo "[*] Verifying page-specific contents..."
grep -q 'id="hero"' index.html || { echo "FAIL: hero section missing in index.html"; exit 1; }
grep -q 'id="projects"' index.html || { echo "FAIL: projects section missing in index.html"; exit 1; }
grep -q 'id="articles-cta"' index.html || { echo "FAIL: articles CTA section missing in index.html"; exit 1; }

# About page: 3 photos side-by-side and computer programming / IT / software copy
grep -q 'assets/team/person-1.svg' about.html || { echo "FAIL: team photo 1 missing in about.html"; exit 1; }
grep -q 'assets/team/person-2.svg' about.html || { echo "FAIL: team photo 2 missing in about.html"; exit 1; }
grep -q 'assets/team/person-3.svg' about.html || { echo "FAIL: team photo 3 missing in about.html"; exit 1; }
grep -qi 'pemrograman komputer' about.html || { echo "FAIL: computer programming copy missing in about.html"; exit 1; }

# Service page: services list
grep -q 'Enterprise Resource Planning' service.html || { echo "FAIL: ERP missing in service.html"; exit 1; }

# Articles page: 20 article cards (10 insight + 10 how-we-work) and reader modal
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

grep -q 'id="articleModal"' articles.html || { echo "FAIL: articleModal missing in articles.html"; exit 1; }
grep -q 'id="articleSearchInput"' articles.html || { echo "FAIL: search input missing in articles.html"; exit 1; }

# Contact page: email link
grep -q 'contact@mayastranawaloka.com' contact.html || { echo "FAIL: contact email missing in contact.html"; exit 1; }

# 3. Verify assets existence
for asset in assets/project-erp.svg assets/project-ecommerce.svg assets/project-cms.svg assets/logo.png assets/team/person-1.svg assets/team/person-2.svg assets/team/person-3.svg; do
  if [[ ! -f "$asset" ]]; then
    echo "FAIL: missing asset $asset"
    exit 1
  fi
done

# 4. Validate XML structure of all SVG assets
echo "[*] Validating XML structure of all SVG assets..."
python3 -c '
import xml.etree.ElementTree as ET
import glob, sys

for svg in glob.glob("assets/**/*.svg", recursive=True):
    try:
        ET.parse(svg)
    except Exception as e:
        print(f"FAIL: SVG parse error in {svg}: {e}")
        sys.exit(1)
'

# 5. Verify CNAME
if [[ ! -f "CNAME" ]]; then
  echo "FAIL: missing CNAME"
  exit 1
fi
grep -q 'www.mayastranawaloka.com' CNAME || { echo "FAIL: CNAME content mismatch"; exit 1; }

# 6. Verify Zero Emojis and Zero Em Dashes
echo "[*] Checking for banned characters (emojis, em dashes)..."
python3 -c '
import re, sys

banned_chars = ["—", "–"]
files = ["index.html", "about.html", "service.html", "articles.html", "contact.html", "style.css", "script.js"]

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    for b in banned_chars:
        if b in content:
            print(f"FAIL: Banned dash found in {path}")
            sys.exit(1)
    emoji_pattern = re.compile(r"[\U00010000-\U0010ffff]", flags=re.UNICODE)
    if emoji_pattern.search(content):
        print(f"FAIL: Emoji detected in {path}")
        sys.exit(1)
'

echo "[OK] All checks passed successfully!"
