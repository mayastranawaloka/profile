#!/usr/bin/env bash
set -euo pipefail

echo "[*] Running verification test suite..."

# 1. Structural Checks on index.html
echo "[*] Checking sections in index.html..."
grep -q 'id="hero"' index.html || { echo "FAIL: hero section missing"; exit 1; }
grep -q 'id="projects"' index.html || { echo "FAIL: projects section missing"; exit 1; }
grep -q 'id="contact"' index.html || { echo "FAIL: contact section missing"; exit 1; }
grep -q 'id="footer"' index.html || { echo "FAIL: footer section missing"; exit 1; }

# Verify NO NAVBAR
if grep -qi '<nav' index.html; then
  echo "FAIL: navbar detected. Specification requires no navbar."
  exit 1
fi

# Verify EXACT text requirements
grep -q 'MAYASTRA NAWALOKA' index.html || { echo "FAIL: Hero text missing"; exit 1; }
grep -q 'contact@mayastranawaloka.com' index.html || { echo "FAIL: contact email missing"; exit 1; }
grep -q 'BY. PT MAYASTRA NAWALOKA NUSANTARA' index.html || { echo "FAIL: footer info missing"; exit 1; }

# Verify 3 project assets
for asset in assets/project-erp.svg assets/project-ecommerce.svg assets/project-cms.svg assets/logo.png; do
  if [[ ! -f "$asset" ]]; then
    echo "FAIL: missing asset $asset"
    exit 1
  fi
done

# Verify CNAME
if [[ ! -f "CNAME" ]]; then
  echo "FAIL: missing CNAME"
  exit 1
fi
grep -q 'www.mayastranawaloka.com' CNAME || { echo "FAIL: CNAME content mismatch"; exit 1; }

# Verify Zero Emojis and Zero Em Dashes
echo "[*] Checking for banned characters (emojis, em dashes)..."
python3 -c '
import re, sys

banned_chars = ["—", "–"]
files = ["index.html", "style.css", "script.js"]

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    for b in banned_chars:
        if b in content:
            print(f"FAIL: Banned dash found in {path}")
            sys.exit(1)
    # Check emojis
    emoji_pattern = re.compile(r"[\U00010000-\U0010ffff]", flags=re.UNICODE)
    if emoji_pattern.search(content):
        print(f"FAIL: Emoji detected in {path}")
        sys.exit(1)
'

echo "[OK] All checks passed successfully!"
