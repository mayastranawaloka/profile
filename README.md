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
├── index.html               # Semantic HTML5 single-page document
├── style.css                # Monochromatic styling and responsive layout rules
├── script.js                # Interactive navigation, knowledge engine, and clock controller
├── nginx.conf               # Hardened web server config with gzip, routing, and caching
├── robots.txt               # Search engine crawler policies
├── sitemap.xml              # Complete sitemap with 31 verified entries
├── assets/                  # Corporate emblem, team portraits, and 64 monochrome SVGs
├── pages/                   # Dedicated sub-pages (About, Services, Articles, Projects)
│   ├── about.html           # Corporate profile and leadership directory
│   ├── service.html         # Enterprise capabilities and architectural services
│   ├── articles.html        # Comprehensive research knowledge base
│   ├── article.html         # Full-screen deep-dive article reader
│   ├── contact.html         # Direct inquiry channel
│   ├── project-erp.html     # ERP architecture showcase
│   ├── project-ecommerce.html # E-Commerce platform showcase
│   ├── project-cms.html     # CMS studio platform showcase
│   ├── project-llm-gateway.html # Enterprise AI LLM gateway showcase
│   └── project-agentic-ops.html # Autonomous agentic systems showcase
├── scripts/                 # Development and operations scripts
│   ├── py/                  # Python vector and screen generators
│   └── sh/                  # Shell orchestration (deploy, redeploy, test, task-helper)
└── tasks/                   # TSKDD local task tracking
```

## Running Locally

### With Docker

Run the deployment script:

```bash
./scripts/sh/deploy.sh
```

The application will be served at `http://localhost:8088`.

To redeploy after modifications:

```bash
./scripts/sh/redeploy.sh
```

### Running Tests

Execute the automated verification test suite:

```bash
./scripts/sh/test.sh
```

## GitHub Pages Deployment

The repository is configured for direct static hosting on GitHub Pages via branch `main` using the custom domain specified in `CNAME` (`www.mayastranawaloka.com`).
