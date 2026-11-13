#!/usr/bin/env bash
set -euo pipefail

echo "[*] Redeploying MAYASTRA NAWALOKA Profile container..."

"$(dirname "$0")/deploy.sh"
