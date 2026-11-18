#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$REPO_ROOT"

echo "[*] Deploying MAYASTRA NAWALOKA Profile container..."

if ! command -v docker >/dev/null 2>&1; then
  echo "Error: docker is required." >&2
  exit 1
fi

IMAGE_NAME="mayastra-profile:latest"
CONTAINER_NAME="mayastra-profile-web"

# Stop and remove existing container if running
docker stop "$CONTAINER_NAME" 2>/dev/null || true
docker rm "$CONTAINER_NAME" 2>/dev/null || true

# Build image
echo "[*] Building Docker image..."
docker build -t "$IMAGE_NAME" .

# Run container with strict resource limits (<= 50% host cap)
echo "[*] Starting container with 1.0 CPU and 256MB RAM cap..."
docker run -d \
  --name "$CONTAINER_NAME" \
  --cpus=1.0 \
  --memory=256m \
  -p 8088:80 \
  --restart unless-stopped \
  "$IMAGE_NAME"

echo "[OK] Deployment successful. Service listening at http://localhost:8088"
