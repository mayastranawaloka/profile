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
  "project-llm-gateway.html"
  "project-agentic-ops.html"
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

  # Verify all 5 capabilities in footer
  grep -q 'project-erp.html' "$page" || { echo "FAIL: ERP link missing in footer of $page"; exit 1; }
  grep -q 'project-ecommerce.html' "$page" || { echo "FAIL: E-Commerce link missing in footer of $page"; exit 1; }
  grep -q 'project-cms.html' "$page" || { echo "FAIL: CMS link missing in footer of $page"; exit 1; }
  grep -q 'project-llm-gateway.html' "$page" || { echo "FAIL: LLM Gateway link missing in footer of $page"; exit 1; }
  grep -q 'project-agentic-ops.html' "$page" || { echo "FAIL: Agentic Ops link missing in footer of $page"; exit 1; }
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
PROJECT_PAGES=(
  "project-erp.html"
  "project-ecommerce.html"
  "project-cms.html"
  "project-llm-gateway.html"
  "project-agentic-ops.html"
)

for proj in "${PROJECT_PAGES[@]}"; do
  grep -q 'class="project-breadcrumb"' "$proj" || { echo "FAIL: breadcrumb missing in $proj"; exit 1; }
  grep -q 'class="project-specs-grid"' "$proj" || { echo "FAIL: specs grid missing in $proj"; exit 1; }
  grep -q 'class="project-screens-grid"' "$proj" || { echo "FAIL: screens grid missing in $proj"; exit 1; }
  SCREEN_COUNT=$(grep -c 'class="project-screen-card"' "$proj" || true)
  if [[ "$SCREEN_COUNT" -ne 11 ]]; then
    echo "FAIL: Expected 11 project screens in $proj, found ${SCREEN_COUNT}"
    exit 1
  fi
done

# Verify all 55 SVGs exist and are linked in respective pages
for i in {1..11}; do
  NUM=$(printf "%02d" $i)
  grep -q "assets/projects/erp/${NUM}-" project-erp.html || { echo "FAIL: missing SVG ${NUM} in project-erp.html"; exit 1; }
  grep -q "assets/projects/ecommerce/${NUM}-" project-ecommerce.html || { echo "FAIL: missing SVG ${NUM} in project-ecommerce.html"; exit 1; }
  grep -q "assets/projects/cms/${NUM}-" project-cms.html || { echo "FAIL: missing SVG ${NUM} in project-cms.html"; exit 1; }
  grep -q "assets/projects/llm-gateway/${NUM}-" project-llm-gateway.html || { echo "FAIL: missing SVG ${NUM} in project-llm-gateway.html"; exit 1; }
  grep -q "assets/projects/agentic-ops/${NUM}-" project-agentic-ops.html || { echo "FAIL: missing SVG ${NUM} in project-agentic-ops.html"; exit 1; }
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

# 6. Validate XML structure of all 55+ SVG assets
echo "[*] Validating XML structure of all 55+ SVG assets..."
python3 -c '
import xml.etree.ElementTree as ET
import glob, sys

svg_files = glob.glob("assets/**/*.svg", recursive=True)
if len(svg_files) < 55:
    print(f"FAIL: Expected at least 55 SVGs, found {len(svg_files)}")
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
    "project-erp.html", "project-ecommerce.html", "project-cms.html",
    "project-llm-gateway.html", "project-agentic-ops.html", "article.html",
    "style.css", "script.js", "robots.txt", "sitemap.xml"
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

# 9. Verify Strict Ban on External Brand Names in SVGs and HTML
echo "[*] Checking for strict ban on third-party AI/LLM brand names..."
python3 -c '
import glob, sys, re

banned_pattern = re.compile(r"\b(openai|anthropic|claude|chatgpt|gemini|mistral|llama|bedrock|langchain|llamaindex|cohere)\b", re.IGNORECASE)
files = [
    "index.html", "about.html", "service.html", "articles.html", "contact.html",
    "project-erp.html", "project-ecommerce.html", "project-cms.html",
    "project-llm-gateway.html", "project-agentic-ops.html", "article.html"
] + glob.glob("assets/**/*.svg", recursive=True)

failed = False
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()
    m = banned_pattern.search(c)
    if m:
        print(f"FAIL: Banned brand \"{m.group(1)}\" found in {fpath}")
        failed = True

if failed:
    sys.exit(1)
print(f"[*] Verified zero third-party brands across {len(files)} files.")
'

# 10. Verify 100% Strict Monochrome Palette across all SVG assets
echo "[*] Verifying 100% strict monochrome palette across all SVG assets..."
python3 -c '
import glob, re, sys

def has_chromatic_color(hex_str):
    hex_str = hex_str.lstrip("#")
    if len(hex_str) != 6:
        return False
    r = int(hex_str[0:2], 16)
    g = int(hex_str[2:4], 16)
    b = int(hex_str[4:6], 16)
    return max(abs(r - g), abs(g - b), abs(r - b)) > 12

svg_files = glob.glob("assets/**/*.svg", recursive=True)
failed = False
for fpath in svg_files:
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()
    colors = re.findall(r"#[0-9a-fA-F]{6}", c)
    bad = [col for col in colors if has_chromatic_color(col)]
    if bad:
        print(f"FAIL: Non-monochrome chromatic color {set(bad)} found in {fpath}")
        failed = True

if failed:
    sys.exit(1)
print(f"[*] Verified 100% strict monochrome palette across all {len(svg_files)} SVGs.")
'

# 10. Verify robots.txt and sitemap.xml
echo "[*] Verifying robots.txt and sitemap.xml..."
if [[ ! -f "robots.txt" ]]; then
  echo "FAIL: missing robots.txt"
  exit 1
fi
grep -q 'User-agent: \*' robots.txt || { echo "FAIL: missing User-agent: * in robots.txt"; exit 1; }
grep -q 'Allow: /' robots.txt || { echo "FAIL: missing Allow: / in robots.txt"; exit 1; }
grep -q 'Sitemap: https://www.mayastranawaloka.com/sitemap.xml' robots.txt || { echo "FAIL: missing Sitemap in robots.txt"; exit 1; }

if [[ ! -f "sitemap.xml" ]]; then
  echo "FAIL: missing sitemap.xml"
  exit 1
fi

python3 -c '
import xml.etree.ElementTree as ET
import sys

try:
    tree = ET.parse("sitemap.xml")
    root = tree.getroot()
except Exception as e:
    print(f"FAIL: sitemap.xml parse error: {e}")
    sys.exit(1)

urls = root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url")
if len(urls) < 31:
    print(f"FAIL: Expected at least 31 URLs in sitemap, found {len(urls)}")
    sys.exit(1)

locs = [u.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text for u in urls]
for required in [
    "https://www.mayastranawaloka.com/",
    "https://www.mayastranawaloka.com/about.html",
    "https://www.mayastranawaloka.com/service.html",
    "https://www.mayastranawaloka.com/project-erp.html",
    "https://www.mayastranawaloka.com/project-ecommerce.html",
    "https://www.mayastranawaloka.com/project-cms.html",
    "https://www.mayastranawaloka.com/project-llm-gateway.html",
    "https://www.mayastranawaloka.com/project-agentic-ops.html",
    "https://www.mayastranawaloka.com/articles.html",
    "https://www.mayastranawaloka.com/contact.html",
    "https://www.mayastranawaloka.com/article.html"
]:
    if required not in locs:
        print(f"FAIL: Missing required route in sitemap: {required}")
        sys.exit(1)

print(f"[*] Verified sitemap.xml with {len(urls)} entries and valid XML namespace.")
'

# 11. Verify Full SEO Tags & JSON-LD Schemas across all 11 HTML Pages
echo "[*] Verifying SEO metadata and Schema.org JSON-LD across all 11 pages..."
python3 -c '
import re, json, sys

pages = [
    "index.html", "about.html", "service.html", "articles.html", "contact.html",
    "project-erp.html", "project-ecommerce.html", "project-cms.html",
    "project-llm-gateway.html", "project-agentic-ops.html", "article.html"
]

for p in pages:
    with open(p, "r", encoding="utf-8") as f:
        html = f.read()

    # Canonical & Favicons
    if "rel=\"canonical\"" not in html:
        print(f"FAIL: Missing canonical link in {p}")
        sys.exit(1)
    if "rel=\"icon\"" not in html:
        print(f"FAIL: Missing favicon link in {p}")
        sys.exit(1)
    if "rel=\"apple-touch-icon\"" not in html:
        print(f"FAIL: Missing apple-touch-icon in {p}")
        sys.exit(1)
    if "format-detection" not in html:
        print(f"FAIL: Missing format-detection in {p}")
        sys.exit(1)

    # Open Graph & Twitter
    for tag in [
        "og:title", "og:description", "og:image", "og:url", "og:image:width", "og:image:height", "og:image:type",
        "twitter:card", "twitter:title", "twitter:site"
    ]:
        if tag not in html:
            print(f"FAIL: Missing {tag} in {p}")
            sys.exit(1)

    # Robots meta
    if "name=\"robots\"" not in html:
        print(f"FAIL: Missing robots meta in {p}")
        sys.exit(1)

    # JSON-LD Structured Data
    json_ld_matches = re.findall(r"<script type=\"application/ld\+json\"[^>]*>(.*?)</script>", html, re.DOTALL)
    if not json_ld_matches:
        print(f"FAIL: Missing application/ld+json in {p}")
        sys.exit(1)

    for jld in json_ld_matches:
        try:
            data = json.loads(jld)
            assert "@context" in data
        except Exception as err:
            print(f"FAIL: Invalid JSON-LD in {p}: {err}")
            sys.exit(1)

print(f"[*] Verified SEO meta tags and Schema.org JSON-LD across all {len(pages)} pages cleanly.")
'

# 12. Verify About Page Team Photos, Nicknames, and Leadership Directory
echo "[*] Verifying About page leadership team and directory..."
for f in "assets/team/gilang.jpeg" "assets/team/cynthia.jpeg" "assets/team/herdian.jpeg"; do
  if [[ ! -f "$f" ]]; then
    echo "FAIL: Missing team photo $f"
    exit 1
  fi
done
grep -q 'assets/team/gilang.jpeg' about.html || { echo "FAIL: gilang.jpeg missing in about.html"; exit 1; }
grep -q 'assets/team/cynthia.jpeg' about.html || { echo "FAIL: cynthia.jpeg missing in about.html"; exit 1; }
grep -q 'assets/team/herdian.jpeg' about.html || { echo "FAIL: herdian.jpeg missing in about.html"; exit 1; }
grep -q 'GILANG' about.html || { echo "FAIL: GILANG nickname missing in about.html"; exit 1; }
grep -q 'CYNTHIA' about.html || { echo "FAIL: CYNTHIA nickname missing in about.html"; exit 1; }
grep -q 'HERDIAN' about.html || { echo "FAIL: HERDIAN nickname missing in about.html"; exit 1; }
grep -q 'class="leadership-directory"' about.html || { echo "FAIL: leadership-directory missing in about.html"; exit 1; }
grep -q 'Gilang Teja Krishna, S.Kom' about.html || { echo "FAIL: Gilang full name missing in about.html"; exit 1; }
grep -q 'Carmelita Cynthia Dagur, S.Kom' about.html || { echo "FAIL: Cynthia full name missing in about.html"; exit 1; }
grep -q 'Herdian Aji Laksana, S.Kom' about.html || { echo "FAIL: Herdian full name missing in about.html"; exit 1; }

echo "[OK] All 11 pages, 55 project SVGs, team assets, sitemap.xml, and robots.txt passed verification suite cleanly!"
