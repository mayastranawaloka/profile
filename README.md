# MAYASTRA NAWALOKA

Minimalist corporate landing page for PT MAYASTRA NAWALOKA NUSANTARA.

## Design Philosophy

- Aesthetic: Deep black monochrome canvas (`#000000`) with high-contrast typography and extensive negative space.
- Navigation: Pure minimalist flow with zero navbar overhead.
- Structure: 4 dedicated sections:
  1. Hero: Typography-focused branding ("MAYASTRA NAWALOKA").
  2. Projects: Image-only showcase for mid-market systems (ERP, E-Commerce, and CMS) with interactive hover preview modals.
  3. Contact: High-visibility direct communication link to `contact@mayastranawaloka.com`.
  4. Footer: Corporate attribution (`BY. PT MAYASTRA NAWALOKA NUSANTARA`), navigation indices, and an edge-to-edge faded company emblem backdrop.

## Project Structure

```text
.
├── CNAME                    # Custom domain mapping (www.mayastranawaloka.com)
├── Dockerfile               # Production container image definition (nginx:alpine)
├── docker-compose.yml       # Orchestration specification with 50% hardware resource cap
├── deploy.sh                # Single-enter local deployment script
├── redeploy.sh              # Single-enter redeployment script
├── test.sh                  # Comprehensive verification test suite
├── index.html               # Semantic HTML5 single-page document
├── style.css                # Monochromatic styling and responsive layout rules
├── script.js                # Interactive modal, clipboard, and keyboard controller
├── nginx.conf               # Hardened web server config with gzip and caching
├── assets/
│   ├── logo.png             # Official corporate emblem
│   ├── project-erp.svg      # Enterprise Resource Planning architectural mockup
│   ├── project-ecommerce.svg# E-Commerce platform architectural mockup
│   └── project-cms.svg      # Content Management System architectural mockup
└── tasks/                   # TSKDD local task tracking
```

## Running Locally

### With Docker

Run the single-enter deployment script:

```bash
./deploy.sh
```

The application will be served at `http://localhost:8088`.

To redeploy after modifications:

```bash
./redeploy.sh
```

### Running Tests

Execute the automated test suite:

```bash
./test.sh
```

## GitHub Pages Deployment

The repository is configured for direct static hosting on GitHub Pages via branch `main` using the custom domain specified in `CNAME` (`www.mayastranawaloka.com`).
