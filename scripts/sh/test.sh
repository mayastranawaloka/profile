#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$REPO_ROOT"

echo "[*] Running verification test suite..."

# 0. Root Directory Hygiene and Subfolder Enforcement
echo "[*] Verifying Root Directory Hygiene..."
ROOT_HTML_COUNT=$(find . -maxdepth 1 -name "*.html" | wc -l)
if [[ "$ROOT_HTML_COUNT" -ne 1 ]]; then
  echo "FAIL: Expected only index.html in root, found ${ROOT_HTML_COUNT} html files"
  find . -maxdepth 1 -name "*.html"
  exit 1
fi
if [[ ! -f "index.html" ]]; then
  echo "FAIL: index.html missing from root"
  exit 1
fi

ROOT_PY_COUNT=$(find . -maxdepth 1 -name "*.py" | wc -l)
if [[ "$ROOT_PY_COUNT" -ne 0 ]]; then
  echo "FAIL: Found python scripts in root, should be in scripts/py/"
  find . -maxdepth 1 -name "*.py"
  exit 1
fi

ROOT_SH_COUNT=$(find . -maxdepth 1 -name "*.sh" | wc -l)
if [[ "$ROOT_SH_COUNT" -ne 0 ]]; then
  echo "FAIL: Found shell scripts in root, should be in scripts/sh/"
  find . -maxdepth 1 -name "*.sh"
  exit 1
fi

ROOT_CSS_COUNT=$(find . -maxdepth 1 -name "*.css" | wc -l)
if [[ "$ROOT_CSS_COUNT" -ne 0 ]]; then
  echo "FAIL: Found CSS in root, should be in assets/css/"
  find . -maxdepth 1 -name "*.css"
  exit 1
fi

ROOT_JS_COUNT=$(find . -maxdepth 1 -name "*.js" | wc -l)
if [[ "$ROOT_JS_COUNT" -ne 0 ]]; then
  echo "FAIL: Found JS in root, should be in assets/js/"
  find . -maxdepth 1 -name "*.js"
  exit 1
fi

# Verify no loose files in assets/ (everything must be strictly structured in subdirectories)
ASSETS_LOOSE_COUNT=$(find assets -maxdepth 1 -type f | wc -l)
if [[ "$ASSETS_LOOSE_COUNT" -ne 0 ]]; then
  echo "FAIL: Found loose files directly in assets/, should be neatly placed in subfolders"
  find assets -maxdepth 1 -type f
  exit 1
fi

# Verify no loose scripts in scripts/ (must be in py/, js/, sh/)
SCRIPTS_LOOSE_COUNT=$(find scripts -maxdepth 1 -type f | wc -l)
if [[ "$SCRIPTS_LOOSE_COUNT" -ne 0 ]]; then
  echo "FAIL: Found loose files directly in scripts/, should be in py/, js/, or sh/"
  find scripts -maxdepth 1 -type f
  exit 1
fi

PAGES=(
  "index.html"
  "pages/about.html"
  "pages/service.html"
  "pages/articles.html"
  "pages/contact.html"
  "pages/project-erp.html"
  "pages/project-ecommerce.html"
  "pages/project-cms.html"
  "pages/project-llm-gateway.html"
  "pages/project-agentic-ops.html"
  "pages/article.html"
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
  grep -q 'assets/brand/logo.png"' "$page" || { echo "FAIL: original logo missing in $page"; exit 1; }

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
  "pages/project-erp.html"
  "pages/project-ecommerce.html"
  "pages/project-cms.html"
  "pages/project-llm-gateway.html"
  "pages/project-agentic-ops.html"
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
  grep -q "assets/projects/erp/${NUM}-" pages/project-erp.html || { echo "FAIL: missing SVG ${NUM} in project-erp.html"; exit 1; }
  grep -q "assets/projects/ecommerce/${NUM}-" pages/project-ecommerce.html || { echo "FAIL: missing SVG ${NUM} in project-ecommerce.html"; exit 1; }
  grep -q "assets/projects/cms/${NUM}-" pages/project-cms.html || { echo "FAIL: missing SVG ${NUM} in project-cms.html"; exit 1; }
  grep -q "assets/projects/llm-gateway/${NUM}-" pages/project-llm-gateway.html || { echo "FAIL: missing SVG ${NUM} in project-llm-gateway.html"; exit 1; }
  grep -q "assets/projects/agentic-ops/${NUM}-" pages/project-agentic-ops.html || { echo "FAIL: missing SVG ${NUM} in project-agentic-ops.html"; exit 1; }
done

# 4. Standalone Article Reader Page Verification
echo "[*] Verifying standalone article reader page..."
grep -q 'id="articleReaderView"' pages/article.html || { echo "FAIL: articleReaderView missing in pages/article.html"; exit 1; }
grep -q 'id="articleCategoryBadge"' pages/article.html || { echo "FAIL: category badge missing in pages/article.html"; exit 1; }
grep -q 'id="articleTitle"' pages/article.html || { echo "FAIL: title element missing in pages/article.html"; exit 1; }
grep -q 'id="articleBody"' pages/article.html || { echo "FAIL: body element missing in pages/article.html"; exit 1; }

# 5. Articles page: 20 article cards (10 insight + 10 how-we-work) and direct links
echo "[*] Verifying articles count and structure..."
INSIGHT_COUNT=$(grep -c 'data-category="insight"' pages/articles.html || true)
SERVICE_COUNT=$(grep -c 'data-category="how-we-work"' pages/articles.html || true)

if [[ "$INSIGHT_COUNT" -ne 10 ]]; then
  echo "FAIL: Expected 10 insight articles, found ${INSIGHT_COUNT}"
  exit 1
fi

if [[ "$SERVICE_COUNT" -ne 10 ]]; then
  echo "FAIL: Expected 10 how-we-work articles, found ${SERVICE_COUNT}"
  exit 1
fi

grep -q 'id="articleSearchInput"' pages/articles.html || { echo "FAIL: search input missing in pages/articles.html"; exit 1; }

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
    "index.html", "pages/about.html", "pages/service.html", "pages/articles.html", "pages/contact.html",
    "pages/project-erp.html", "pages/project-ecommerce.html", "pages/project-cms.html",
    "pages/project-llm-gateway.html", "pages/project-agentic-ops.html", "pages/article.html",
    "assets/css/style.css", "assets/js/script.js"
] + glob.glob("assets/**/*.svg", recursive=True)

# Regex matching emojis across standard unicode blocks
emoji_pattern = re.compile(
    "[\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map
    "\U0001F1E0-\U0001F1FF"  # flags
    "\U00002702-\U000027B0"
    "\U000024C2-\U0001F251"
    "\U0001F900-\U0001F9FF"  # supplemental symbols
    "\U0001FA70-\U0001FAFF"  # symbols and pictographs extended-a
    "]+", flags=re.UNICODE
)

failed = False
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    for bc in banned_chars:
        if bc in content:
            print(f"FAIL: Banned dash {bc} found in {fpath}")
            failed = True
    match = emoji_pattern.search(content)
    if match:
        print(f"FAIL: Emoji {match.group(0)} found in {fpath}")
        failed = True

if failed:
    sys.exit(1)
print(f"[*] Verified zero emojis and zero em dashes across {len(files)} files.")
'

# 9. Verify Strict Ban on Third-Party AI/LLM Brand Names
echo "[*] Checking for strict ban on third-party AI/LLM brand names..."
python3 -c '
import re, sys, glob

banned_brands = [
    r"\bOpenAI\b", r"\bChatGPT\b", r"\bGPT-4\b", r"\bGPT-3\b",
    r"\bClaude\b", r"\bAnthropic\b",
    r"\bGemini\b", r"\bDeepSeek\b",
    r"\bLlama\b", r"\bMeta\s+AI\b",
    r"\bMistral\b", r"\bQwen\b"
]

files = [
    "index.html", "pages/about.html", "pages/service.html", "pages/articles.html", "pages/contact.html",
    "pages/project-erp.html", "pages/project-ecommerce.html", "pages/project-cms.html",
    "pages/project-llm-gateway.html", "pages/project-agentic-ops.html", "pages/article.html"
] + glob.glob("assets/**/*.svg", recursive=True)

failed = False
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    for bb in banned_brands:
        match = re.search(bb, content, re.IGNORECASE)
        if match:
            print(f"FAIL: Banned brand match \"{match.group(0)}\" ({bb}) found in {fpath}")
            failed = True

if failed:
    sys.exit(1)
print(f"[*] Verified zero third-party brands across {len(files)} files.")
'

# 10. Verify Refined Brand Red Accents in Project SVGs and Strict Monochrome in Non-Project SVGs
echo "[*] Verifying refined brand red accents in project SVGs and strict monochrome in non-project SVGs..."
python3 -c '
import glob, re, sys

APPROVED_RED_ACCENTS = {"#ef4444", "#dc2626", "#b91c1c", "#c10f1e", "#991b1b", "#f87171"}

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
project_count = 0
non_project_count = 0

for fpath in svg_files:
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()
    colors = re.findall(r"#[0-9a-fA-F]{6}", c)
    chromatic = [col.lower() for col in colors if has_chromatic_color(col)]
    
    is_project_svg = "assets/projects/" in fpath or "assets/projects-light/" in fpath
    if is_project_svg:
        project_count += 1
        # Must have at least one approved red accent
        red_accents = [col for col in chromatic if col in APPROVED_RED_ACCENTS]
        if not red_accents:
            print(f"FAIL: Missing required red accent in project SVG: {fpath}")
            failed = True
        # Must have zero unauthorized chromatic colors
        bad_colors = [col for col in chromatic if col not in APPROVED_RED_ACCENTS]
        if bad_colors:
            print(f"FAIL: Unauthorized chromatic color {set(bad_colors)} in project SVG: {fpath}")
            failed = True
    else:
        non_project_count += 1
        # Non-project SVGs (maps, team) must be 100% strict monochrome
        if chromatic:
            print(f"FAIL: Non-monochrome chromatic color {set(chromatic)} in non-project SVG: {fpath}")
            failed = True

if failed:
    sys.exit(1)
print(f"[*] Verified refined red accents across {project_count} project SVGs and strict monochrome across {non_project_count} non-project SVGs cleanly.")
'

# 11. Verify robots.txt and sitemap.xml
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
    "https://www.mayastranawaloka.com/pages/about.html",
    "https://www.mayastranawaloka.com/pages/service.html",
    "https://www.mayastranawaloka.com/pages/project-erp.html",
    "https://www.mayastranawaloka.com/pages/project-ecommerce.html",
    "https://www.mayastranawaloka.com/pages/project-cms.html",
    "https://www.mayastranawaloka.com/pages/project-llm-gateway.html",
    "https://www.mayastranawaloka.com/pages/project-agentic-ops.html",
    "https://www.mayastranawaloka.com/pages/articles.html",
    "https://www.mayastranawaloka.com/pages/contact.html",
    "https://www.mayastranawaloka.com/pages/article.html"
]:
    if required not in locs:
        print(f"FAIL: Missing required route in sitemap: {required}")
        sys.exit(1)

print(f"[*] Verified sitemap.xml with {len(urls)} entries and valid XML namespace.")
'

# 12. Verify Full SEO Tags & JSON-LD Schemas across all 11 HTML Pages
echo "[*] Verifying SEO metadata and Schema.org JSON-LD across all 11 pages..."
python3 -c '
import re, json, sys

pages = [
    "index.html", "pages/about.html", "pages/service.html", "pages/articles.html", "pages/contact.html",
    "pages/project-erp.html", "pages/project-ecommerce.html", "pages/project-cms.html",
    "pages/project-llm-gateway.html", "pages/project-agentic-ops.html", "pages/article.html"
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

# 13. Verify About Page Team Photos, Nicknames, and Leadership Directory
echo "[*] Verifying About page leadership team and directory..."
for f in "assets/team/gilang.jpeg" "assets/team/cynthia.jpeg" "assets/team/herdian.jpeg"; do
  if [[ ! -f "$f" ]]; then
    echo "FAIL: Missing team photo $f"
    exit 1
  fi
done
grep -q 'assets/team/gilang.jpeg' pages/about.html || { echo "FAIL: gilang.jpeg missing in pages/about.html"; exit 1; }
grep -q 'assets/team/cynthia.jpeg' pages/about.html || { echo "FAIL: cynthia.jpeg missing in pages/about.html"; exit 1; }
grep -q 'assets/team/herdian.jpeg' pages/about.html || { echo "FAIL: herdian.jpeg missing in pages/about.html"; exit 1; }
grep -q 'GILANG' pages/about.html || { echo "FAIL: GILANG nickname missing in pages/about.html"; exit 1; }
grep -q 'CYNTHIA' pages/about.html || { echo "FAIL: CYNTHIA nickname missing in pages/about.html"; exit 1; }
grep -q 'HERDIAN' pages/about.html || { echo "FAIL: HERDIAN nickname missing in pages/about.html"; exit 1; }
grep -q 'class="leadership-directory"' pages/about.html || { echo "FAIL: leadership-directory missing in pages/about.html"; exit 1; }
grep -q 'Gilang Teja Krishna, S.Kom' pages/about.html || { echo "FAIL: Gilang full name missing in pages/about.html"; exit 1; }
grep -q 'Carmelita Cynthia Dagur, S.Kom' pages/about.html || { echo "FAIL: Cynthia full name missing in pages/about.html"; exit 1; }
grep -q 'Herdian Aji Laksana, S.Kom' pages/about.html || { echo "FAIL: Herdian full name missing in pages/about.html"; exit 1; }

# 14. Verify Enterprise AI Integration SEO Priority Across Pages & Sitemap
echo "[*] Verifying Enterprise AI Integration SEO Priority..."
python3 -c '
import re, sys, glob

# Verify strict ban on pretentious buzzword "pelopor"
for html_file in glob.glob("pages/*.html") + ["index.html"]:
    with open(html_file, "r", encoding="utf-8") as f:
        c = f.read()
    if re.search(r"\bpelopor\b", c, re.IGNORECASE):
        print(f"FAIL: Banned buzzword pelopor found in {html_file}")
        sys.exit(1)

checks = [
    ("index.html", r"<title>PT MAYASTRA NAWALOKA NUSANTARA - Enterprise AI &amp; LLM Integration Architecture</title>"),
    ("index.html", r"content=\"PT Mayastra Nawaloka Nusantara adalah perusahaan rekayasa software dan arsitektur sistem digital di Indonesia"),
    ("pages/service.html", r"<title>Enterprise AI &amp; LLM Integration Services - PT MAYASTRA NAWALOKA NUSANTARA</title>"),
    ("pages/about.html", r"<title>About PT MAYASTRA NAWALOKA NUSANTARA - Enterprise AI &amp; Architectural Systems Profile</title>"),
    ("pages/contact.html", r"<title>Enterprise AI &amp; Software Consultations - PT MAYASTRA NAWALOKA NUSANTARA</title>"),
    ("pages/articles.html", r"<title>Enterprise AI &amp; Engineering Research Insights - PT MAYASTRA NAWALOKA NUSANTARA</title>"),
    ("pages/article.html", r"<title>Enterprise AI &amp; Engineering Research Reader - PT MAYASTRA NAWALOKA NUSANTARA</title>"),
    ("pages/project-llm-gateway.html", r"<title>Enterprise AI LLM Gateway &amp; API Key Harness - PT MAYASTRA NAWALOKA NUSANTARA</title>"),
    ("pages/project-agentic-ops.html", r"<title>Enterprise Autonomous Agentic AI &amp; RAG Systems - PT MAYASTRA NAWALOKA NUSANTARA</title>"),
]

for filename, pattern in checks:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    if not re.search(pattern, content):
        print(f"FAIL: Pattern {pattern} not matched in {filename}")
        sys.exit(1)

with open("sitemap.xml", "r", encoding="utf-8") as f:
    sitemap = f.read()
if "pages/project-llm-gateway.html</loc>\n    <lastmod>2026-11-14</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.95</priority>" not in sitemap:
    print("FAIL: pages/project-llm-gateway.html not elevated to 0.95 priority in sitemap.xml")
    sys.exit(1)
if "pages/project-agentic-ops.html</loc>\n    <lastmod>2026-11-14</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.95</priority>" not in sitemap:
    print("FAIL: pages/project-agentic-ops.html not elevated to 0.95 priority in sitemap.xml")
    sys.exit(1)

print("[*] Verified Enterprise AI Integration SEO priority across all pages and sitemap cleanly.")
'

# 15. Verify Tap Highlight Disabled and Faded Grey Text Selection Styling
echo "[*] Verifying Tap Highlight Disabled and Faded Grey Selection in assets/css/style.css..."
grep -q -- '-webkit-tap-highlight-color: transparent' assets/css/style.css || { echo "FAIL: tap-highlight-color not disabled in assets/css/style.css"; exit 1; }
grep -q '::selection' assets/css/style.css || { echo "FAIL: ::selection not defined in assets/css/style.css"; exit 1; }
grep -q '::-moz-selection' assets/css/style.css || { echo "FAIL: ::-moz-selection not defined in assets/css/style.css"; exit 1; }
echo "[*] Verified tap highlight reset and custom selection in assets/css/style.css cleanly."

echo "[OK] All 11 pages, 55 project SVGs, team assets, sitemap.xml, and robots.txt passed verification suite cleanly!"
